/* OMN Robot Manager dashboard client.
   Connects to the robot manager backend via Server-Sent Events and renders:
   live localization map, health monitor, lifecycle, task status and the
   SLAM performance chart. Vanilla JS, no dependencies. */

'use strict';

const $ = (id) => document.getElementById(id);

const els = {
  connDot: $('conn-dot'), modeChip: $('mode-chip'),
  lifecycleBadge: $('lifecycle-badge'), healthChip: $('health-chip'),
  batteryChip: $('battery-chip'), estopBtn: $('estop-btn'),
  banner: $('alert-banner'),
  mapCanvas: $('map-canvas'), mapWrap: $('map-wrap'), mapMeta: $('map-meta'),
  poseX: $('pose-x'), poseY: $('pose-y'), poseYaw: $('pose-yaw'),
  poseSpeed: $('pose-speed'),
  pipeline: $('pipeline'), lifecycleHistory: $('lifecycle-history'),
  activeTask: $('active-task'), taskHistory: $('task-history'),
  exploreBtn: $('explore-btn'), remapBtn: $('remap-btn'),
  followRedBtn: $('follow-red-btn'), cancelBtn: $('cancel-btn'),
  healthBody: $('health-body'), simTools: $('sim-tools'), faultBtn: $('fault-btn'),
  slamConfidence: $('slam-confidence'), slamHold: $('slam-hold'),
  slamUnknown: $('slam-unknown'), slamFrontier: $('slam-frontier'),
  slamGrowth: $('slam-growth'),
  slamChart: $('slam-chart'), chartTip: $('chart-tip'),
  toast: $('toast'),
};

const state = {
  latest: null,
  map: null,            // {width,height,resolution,origin_x,origin_y,cells}
  mapCanvasOff: null,   // offscreen canvas with the rendered grid
  trail: [],
  faultOn: false,
  view: { scale: 1, offX: 0, offY: 0 }, // grid->screen transform
};

const css = (name) =>
  getComputedStyle(document.documentElement).getPropertyValue(name).trim();

/* ================= connection ================= */

function connect() {
  const source = new EventSource('/events');
  window.__eventSource = source; // exposed for debugging / test tooling
  source.addEventListener('state', (event) => {
    state.latest = JSON.parse(event.data);
    els.connDot.classList.add('on');
    render();
  });
  source.addEventListener('map', (event) => {
    const payload = JSON.parse(event.data);
    decodeMap(payload);
    renderMapOffscreen();
    drawMap();
  });
  source.onerror = () => {
    els.connDot.classList.remove('on');
    source.close();
    setTimeout(connect, 1500);
  };
}

async function sendCommand(payload) {
  try {
    const response = await fetch('/api/command', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const result = await response.json();
    if (!result.ok) toast(result.error || 'command failed', true);
    return result;
  } catch (error) {
    toast('backend unreachable', true);
    return { ok: false };
  }
}

let toastTimer = null;
function toast(message, isError) {
  els.toast.textContent = message;
  els.toast.classList.toggle('error', !!isError);
  els.toast.classList.remove('hidden');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => els.toast.classList.add('hidden'), 3200);
}

/* ================= map rendering ================= */

function decodeMap(payload) {
  const binary = atob(payload.data_b64 || '');
  const cells = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) cells[i] = binary.charCodeAt(i);
  state.map = { ...payload, cells };
  els.mapMeta.textContent =
    `${payload.width}×${payload.height} @ ${payload.resolution.toFixed(2)} m/cell`;
}

function renderMapOffscreen() {
  const map = state.map;
  if (!map || !map.width) return;
  const off = document.createElement('canvas');
  off.width = map.width;
  off.height = map.height;
  const ctx = off.getContext('2d');
  const image = ctx.createImageData(map.width, map.height);

  const freeColor = hexToRgb(css('--map-free'));
  const occColor = hexToRgb(css('--map-occ'));
  const unkColor = hexToRgb(css('--map-unknown'));

  for (let py = 0; py < map.height; py++) {
    const gy = map.height - 1 - py;         // grid row 0 is at the bottom
    for (let px = 0; px < map.width; px++) {
      const value = map.cells[gy * map.width + px];
      const color = value === 0 ? freeColor : value === 100 ? occColor : unkColor;
      const at = (py * map.width + px) * 4;
      image.data[at] = color[0];
      image.data[at + 1] = color[1];
      image.data[at + 2] = color[2];
      image.data[at + 3] = 255;
    }
  }
  ctx.putImageData(image, 0, 0);
  state.mapCanvasOff = off;
}

function hexToRgb(hex) {
  hex = hex.replace('#', '');
  if (hex.length === 3) hex = hex.split('').map((c) => c + c).join('');
  const n = parseInt(hex, 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}

function worldToScreen(x, y) {
  const map = state.map, view = state.view;
  const gx = (x - map.origin_x) / map.resolution;
  const gy = (y - map.origin_y) / map.resolution;
  return [view.offX + gx * view.scale,
          view.offY + (map.height - gy) * view.scale];
}

function screenToWorld(sx, sy) {
  const map = state.map, view = state.view;
  const gx = (sx - view.offX) / view.scale;
  const gy = map.height - (sy - view.offY) / view.scale;
  return [map.origin_x + gx * map.resolution,
          map.origin_y + gy * map.resolution];
}

function drawMap() {
  const canvas = els.mapCanvas;
  const wrap = els.mapWrap;
  const dpr = window.devicePixelRatio || 1;
  const cssWidth = wrap.clientWidth, cssHeight = wrap.clientHeight;
  if (canvas.width !== cssWidth * dpr || canvas.height !== cssHeight * dpr) {
    canvas.width = cssWidth * dpr;
    canvas.height = cssHeight * dpr;
  }
  const ctx = canvas.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, cssWidth, cssHeight);

  const map = state.map;
  if (!map || !state.mapCanvasOff) {
    ctx.fillStyle = css('--muted');
    ctx.font = '13px system-ui';
    ctx.textAlign = 'center';
    ctx.fillText('waiting for map…', cssWidth / 2, cssHeight / 2);
    return;
  }

  // Fit map into view (letterboxed, centered).
  const scale = Math.min(cssWidth / map.width, cssHeight / map.height);
  state.view.scale = scale;
  state.view.offX = (cssWidth - map.width * scale) / 2;
  state.view.offY = (cssHeight - map.height * scale) / 2;

  ctx.imageSmoothingEnabled = false;
  ctx.drawImage(state.mapCanvasOff, state.view.offX, state.view.offY,
                map.width * scale, map.height * scale);

  const snapshot = state.latest;
  if (!snapshot) return;

  // trail
  if (state.trail.length > 1) {
    ctx.strokeStyle = css('--muted');
    ctx.globalAlpha = 0.55;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    state.trail.forEach(([x, y], index) => {
      const [sx, sy] = worldToScreen(x, y);
      index === 0 ? ctx.moveTo(sx, sy) : ctx.lineTo(sx, sy);
    });
    ctx.stroke();
    ctx.globalAlpha = 1;
  }

  // planned path
  const path = snapshot.nav && snapshot.nav.path;
  if (path && path.length > 1) {
    ctx.strokeStyle = css('--series-1');
    ctx.lineWidth = 2;
    ctx.setLineDash([]);
    ctx.beginPath();
    path.forEach(([x, y], index) => {
      const [sx, sy] = worldToScreen(x, y);
      index === 0 ? ctx.moveTo(sx, sy) : ctx.lineTo(sx, sy);
    });
    ctx.stroke();
  }

  // goal
  const goal = snapshot.nav && snapshot.nav.goal;
  if (goal) {
    const [gx, gy] = worldToScreen(goal.x, goal.y);
    ctx.strokeStyle = css('--series-5');
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.arc(gx, gy, 8, 0, Math.PI * 2);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(gx - 12, gy); ctx.lineTo(gx + 12, gy);
    ctx.moveTo(gx, gy - 12); ctx.lineTo(gx, gy + 12);
    ctx.stroke();
  }

  // red cube (follow_red task, sim mode)
  const cube = snapshot.nav && snapshot.nav.cube;
  if (cube) {
    const [cx, cy] = worldToScreen(cube.x, cube.y);
    const half = Math.max(4, 0.12 / state.map.resolution * state.view.scale);
    ctx.fillStyle = '#d62828';
    ctx.strokeStyle = css('--surface');
    ctx.lineWidth = 1.5;
    ctx.fillRect(cx - half, cy - half, half * 2, half * 2);
    ctx.strokeRect(cx - half, cy - half, half * 2, half * 2);
  }

  // robot (triangle showing heading)
  const robot = snapshot.robot;
  if (robot && robot.has_pose) {
    const [rx, ry] = worldToScreen(robot.x, robot.y);
    const yaw = -robot.yaw; // canvas y is flipped
    const size = Math.max(7, 0.25 / state.map.resolution * state.view.scale);
    ctx.save();
    ctx.translate(rx, ry);
    ctx.rotate(yaw);
    ctx.fillStyle = css('--series-8');
    ctx.strokeStyle = css('--surface');
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(size, 0);
    ctx.lineTo(-size * 0.7, size * 0.6);
    ctx.lineTo(-size * 0.4, 0);
    ctx.lineTo(-size * 0.7, -size * 0.6);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
  }
}

/* ================= panels ================= */

const PIPELINE_STATES = ['initializing', 'mapping', 'saving_map', 'ready', 'executing'];

function render() {
  const snapshot = state.latest;
  if (!snapshot) return;

  // top bar
  els.modeChip.textContent = snapshot.mode === 'sim' ? 'SIMULATION' : 'ROS 2 LIVE';
  const lifecycleState = snapshot.lifecycle.state;
  els.lifecycleBadge.textContent = lifecycleState.replace('_', ' ');
  els.lifecycleBadge.className = 'lifecycle-badge ' + lifecycleState;

  const health = snapshot.health;
  els.healthChip.textContent = 'health: ' + health.overall.toUpperCase();
  els.batteryChip.textContent = health.battery_percent == null
    ? 'battery: n/a'
    : 'battery: ' + health.battery_percent.toFixed(0) + '%';

  els.estopBtn.textContent = snapshot.estopped ? 'RELEASE E-STOP' : 'E-STOP';
  els.estopBtn.classList.toggle('released', snapshot.estopped);

  // alert banner
  if (lifecycleState === 'fault') {
    const note = lastNote(snapshot.lifecycle.history, 'fault');
    els.banner.textContent = '⚠ CRITICAL FAULT — ' +
      (note ? note + ' lost. ' : '') + 'Robot stopped; waiting for recovery.';
    els.banner.classList.remove('hidden');
  } else if (lifecycleState === 'estopped') {
    els.banner.textContent = '⚠ EMERGENCY STOP engaged — release to resume.';
    els.banner.classList.remove('hidden');
  } else {
    els.banner.classList.add('hidden');
  }

  // pose
  const robot = snapshot.robot;
  els.poseX.textContent = robot.x.toFixed(2);
  els.poseY.textContent = robot.y.toFixed(2);
  const yawNorm = Math.atan2(Math.sin(robot.yaw), Math.cos(robot.yaw));
  els.poseYaw.textContent = (yawNorm * 180 / Math.PI).toFixed(0);
  els.poseSpeed.textContent = robot.speed == null ? '–' : robot.speed.toFixed(2);

  // trail
  if (robot.has_pose) {
    const last = state.trail[state.trail.length - 1];
    if (!last || Math.hypot(robot.x - last[0], robot.y - last[1]) > 0.05) {
      state.trail.push([robot.x, robot.y]);
      if (state.trail.length > 3000) state.trail.shift();
    }
  }

  renderPipeline(snapshot.lifecycle);
  renderTasks(snapshot.task, lifecycleState);
  renderHealth(health);
  renderSlam(snapshot.slam);
  drawMap();

  // sim tools
  els.simTools.hidden = snapshot.mode !== 'sim';
  state.faultOn = (snapshot.injected_faults || []).includes('scan');
  els.faultBtn.textContent = state.faultOn ? 'Restore LiDAR (sim)' : 'Drop LiDAR (sim)';
}

function lastNote(history, targetState) {
  for (let i = history.length - 1; i >= 0; i--) {
    if (history[i].state === targetState) return history[i].note;
  }
  return '';
}

function renderPipeline(lifecycle) {
  const current = lifecycle.state;
  const parts = [];
  const currentIndex = PIPELINE_STATES.indexOf(current);
  PIPELINE_STATES.forEach((name, index) => {
    let cls = 'pl-step';
    if (name === current) cls += ' current';
    else if (currentIndex > index || current === 'ready' && index < 3) cls += ' done';
    parts.push(`<span class="${cls}">${name.replace('_', ' ')}</span>`);
    if (index < PIPELINE_STATES.length - 1) parts.push('<span class="pl-arrow">→</span>');
  });
  if (current === 'fault' || current === 'estopped') {
    parts.push('<span class="pl-arrow">→</span>');
    parts.push(`<span class="pl-step alert">${current}</span>`);
  }
  els.pipeline.innerHTML = parts.join('');

  const items = lifecycle.history.slice(-6).reverse().map((entry) => {
    const when = new Date(entry.time * 1000).toLocaleTimeString();
    const note = entry.note ? ` (${entry.note})` : '';
    return `<li><span class="t">${when}</span><span>→ ${entry.state}${note}</span></li>`;
  });
  els.lifecycleHistory.innerHTML = items.join('');
}

function renderTasks(tasks, lifecycleState) {
  const active = tasks.active;
  if (active) {
    els.activeTask.className = 'active-task';
    els.activeTask.innerHTML = `
      <div class="task-title"><span>${active.label}</span>
        <span class="status-chip active">active</span></div>
      <div class="task-detail">${active.detail || 'in progress…'}
        ${active.duration_s != null ? ' · ' + active.duration_s.toFixed(0) + 's' : ''}</div>
      <div class="progress"><i style="width:${(active.progress * 100).toFixed(1)}%"></i></div>`;
  } else {
    els.activeTask.className = 'active-task none';
    els.activeTask.textContent = lifecycleState === 'ready'
      ? 'no active task — click the map to navigate'
      : 'no active task';
  }

  els.taskHistory.innerHTML = tasks.history.slice(0, 6).map((task) => `
    <li><span class="status-chip ${task.status}">${task.status}</span>
      <span class="grow">${task.label}</span>
      <span>${task.duration_s != null ? task.duration_s.toFixed(0) + 's' : ''}</span></li>`
  ).join('');

  const busy = !!active;
  els.exploreBtn.disabled = busy || lifecycleState !== 'ready';
  els.followRedBtn.disabled = busy || lifecycleState !== 'ready';
  els.remapBtn.disabled = busy || lifecycleState !== 'ready';
  els.cancelBtn.disabled = !busy;
}

function renderHealth(health) {
  els.healthBody.innerHTML = health.components.map((component) => {
    const age = component.age_s == null ? '–'
      : component.age_s < 10 ? component.age_s.toFixed(1) + 's'
      : component.age_s.toFixed(0) + 's';
    const rate = component.rate_hz > 0 ? component.rate_hz.toFixed(1) + ' Hz' : '–';
    const star = component.critical ? '<span class="crit-star" title="critical component">★</span>' : '';
    return `<tr>
      <td>${component.label}${star}</td>
      <td><span class="hstat ${component.status}"><span class="hdot"></span>${component.status}</span></td>
      <td>${rate}</td><td>${age}</td></tr>`;
  }).join('');
}

/* ================= SLAM chart ================= */

function renderSlam(slam) {
  const latest = slam.latest;
  els.slamConfidence.textContent = latest ? (latest.confidence * 100).toFixed(1) + '%' : '–';
  els.slamUnknown.textContent = latest && latest.unknown_ratio != null
    ? (latest.unknown_ratio * 100).toFixed(1) + '%' : '–';
  els.slamFrontier.textContent = latest && latest.frontier_ratio != null
    ? (latest.frontier_ratio * 100).toFixed(2) + '%' : '–';
  els.slamGrowth.textContent = latest && latest.growth_ratio != null
    ? (latest.growth_ratio * 100).toFixed(2) + '%' : '–';
  els.slamHold.textContent = slam.converged
    ? 'converged ✓'
    : slam.hold_progress > 0
      ? `holding ${(slam.hold_progress * 100).toFixed(0)}% of ${'5s'}`
      : `threshold ${(slam.threshold * 100).toFixed(0)}%`;

  drawSlamChart(slam);
}

let chartGeom = null;
function drawSlamChart(slam) {
  const canvas = els.slamChart;
  const dpr = window.devicePixelRatio || 1;
  const cssWidth = canvas.clientWidth || canvas.parentElement.clientWidth;
  const cssHeight = 150;
  canvas.width = cssWidth * dpr;
  canvas.height = cssHeight * dpr;
  const ctx = canvas.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, cssWidth, cssHeight);

  const pad = { l: 30, r: 6, t: 8, b: 16 };
  const plotW = cssWidth - pad.l - pad.r;
  const plotH = cssHeight - pad.t - pad.b;
  const history = slam.history || [];

  // gridlines + y labels (0, 50, 100 %)
  ctx.strokeStyle = css('--grid');
  ctx.fillStyle = css('--muted');
  ctx.font = '10px system-ui';
  ctx.textAlign = 'right';
  ctx.lineWidth = 1;
  [0, 0.5, 1].forEach((frac) => {
    const y = pad.t + plotH * (1 - frac) + 0.5;
    ctx.beginPath();
    ctx.moveTo(pad.l, y); ctx.lineTo(cssWidth - pad.r, y);
    ctx.stroke();
    ctx.fillText((frac * 100).toFixed(0) + '%', pad.l - 5, y + 3);
  });

  if (history.length < 2) {
    ctx.textAlign = 'center';
    ctx.fillText('waiting for SLAM data…', cssWidth / 2, cssHeight / 2);
    chartGeom = null;
    return;
  }

  const t0 = history[0].time;
  const t1 = history[history.length - 1].time;
  const span = Math.max(1, t1 - t0);
  const px = (t) => pad.l + ((t - t0) / span) * plotW;
  const py = (v) => pad.t + plotH * (1 - Math.max(0, Math.min(1, v)));
  chartGeom = { px, py, history, pad, plotW, plotH };

  // threshold line
  ctx.strokeStyle = css('--muted');
  ctx.setLineDash([4, 4]);
  ctx.beginPath();
  ctx.moveTo(pad.l, py(slam.threshold));
  ctx.lineTo(cssWidth - pad.r, py(slam.threshold));
  ctx.stroke();
  ctx.setLineDash([]);

  // series
  const drawSeries = (key, color) => {
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    let started = false;
    history.forEach((sample) => {
      const value = sample[key];
      if (value == null) return;
      const x = px(sample.time), y = py(value);
      started ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
      started = true;
    });
    ctx.stroke();
  };
  drawSeries('unknown_ratio', css('--series-3'));
  drawSeries('confidence', css('--series-1'));

  // x labels: elapsed seconds
  ctx.fillStyle = css('--muted');
  ctx.textAlign = 'center';
  ctx.fillText('-' + span.toFixed(0) + 's', pad.l + 12, cssHeight - 4);
  ctx.fillText('now', cssWidth - pad.r - 14, cssHeight - 4);
}

els.slamChart.addEventListener('mousemove', (event) => {
  if (!chartGeom) return;
  const rect = els.slamChart.getBoundingClientRect();
  const mx = event.clientX - rect.left;
  let best = null, bestDx = Infinity;
  chartGeom.history.forEach((sample) => {
    const dx = Math.abs(chartGeom.px(sample.time) - mx);
    if (dx < bestDx) { bestDx = dx; best = sample; }
  });
  if (!best || bestDx > 30) { els.chartTip.classList.add('hidden'); return; }
  const when = new Date(best.time * 1000).toLocaleTimeString();
  els.chartTip.innerHTML =
    `<b>${when}</b><br>confidence ${(best.confidence * 100).toFixed(1)}%` +
    (best.unknown_ratio != null ? `<br>unknown ${(best.unknown_ratio * 100).toFixed(1)}%` : '');
  els.chartTip.classList.remove('hidden');
  const tipX = Math.min(chartGeom.px(best.time) + 10,
                        els.slamChart.clientWidth - 130);
  els.chartTip.style.left = tipX + 'px';
  els.chartTip.style.top = '8px';
});
els.slamChart.addEventListener('mouseleave', () =>
  els.chartTip.classList.add('hidden'));

/* ================= interactions ================= */

els.mapCanvas.addEventListener('click', (event) => {
  if (!state.map || !state.latest) return;
  const rect = els.mapCanvas.getBoundingClientRect();
  const [wx, wy] = screenToWorld(event.clientX - rect.left, event.clientY - rect.top);
  sendCommand({ action: 'navigate', x: +wx.toFixed(3), y: +wy.toFixed(3) })
    .then((result) => {
      if (result.ok) toast(`navigation goal sent: (${wx.toFixed(2)}, ${wy.toFixed(2)})`);
    });
});

els.estopBtn.addEventListener('click', () => {
  const engaged = state.latest && state.latest.estopped;
  sendCommand({ action: 'estop', engage: !engaged });
});
els.exploreBtn.addEventListener('click', () => sendCommand({ action: 'explore' }));
els.followRedBtn.addEventListener('click', () => sendCommand({ action: 'follow_red' }));
els.remapBtn.addEventListener('click', () => sendCommand({ action: 'remap' }));
els.cancelBtn.addEventListener('click', () => sendCommand({ action: 'cancel' }));
els.faultBtn.addEventListener('click', () =>
  sendCommand({ action: 'inject_fault', component: 'scan', enable: !state.faultOn }));

window.addEventListener('resize', drawMap);
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
  renderMapOffscreen();
  drawMap();
});

connect();
