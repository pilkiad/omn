"""Robot manager dashboard server.

Standard-library-only HTTP server (no flask / websockets dependency, so it
runs unchanged on the Tortugabot laptop and on any dev machine):

- serves the single-page dashboard from ``web/``
- ``GET  /api/state``  -> full state snapshot (JSON)
- ``GET  /api/map``    -> occupancy grid payload (JSON, base64 cells)
- ``POST /api/command``-> commands: navigate / explore / cancel / estop / ...
- ``GET  /events``     -> Server-Sent Events stream: ``state`` events at 5 Hz
                          and a ``map`` event whenever the map changes

The server talks to a *backend* object (SimBackend or the ROS 2 node's
RosBackend) through three methods: ``state()``, ``map_payload()``,
``command(payload)``.

Run without ROS:  ``python -m robot_manager.dashboard_server --sim``
"""

import argparse
import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

WEB_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web')

_CONTENT_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.svg': 'image/svg+xml',
    '.png': 'image/png',
    '.ico': 'image/x-icon',
}


def make_handler(backend):
    class DashboardHandler(BaseHTTPRequestHandler):
        protocol_version = 'HTTP/1.1'

        # ---- helpers -------------------------------------------------
        def _send_json(self, obj, status=200):
            body = json.dumps(obj).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(body)

        def _send_file(self, relative_path):
            path = os.path.normpath(os.path.join(WEB_ROOT, relative_path))
            if not path.startswith(WEB_ROOT) or not os.path.isfile(path):
                self.send_error(404)
                return
            extension = os.path.splitext(path)[1].lower()
            with open(path, 'rb') as handle:
                body = handle.read()
            self.send_response(200)
            self.send_header('Content-Type',
                             _CONTENT_TYPES.get(extension, 'application/octet-stream'))
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(body)

        # ---- routes --------------------------------------------------
        def do_GET(self):
            path = self.path.split('?', 1)[0]
            if path in ('/', '/index.html'):
                self._send_file('index.html')
            elif path == '/api/state':
                self._send_json(backend.state())
            elif path == '/api/map':
                self._send_json(backend.map_payload())
            elif path == '/events':
                self._stream_events()
            elif path.startswith('/web/'):
                self._send_file(path[len('/web/'):])
            else:
                self._send_file(path.lstrip('/'))

        def do_POST(self):
            path = self.path.split('?', 1)[0]
            if path != '/api/command':
                self.send_error(404)
                return
            try:
                length = int(self.headers.get('Content-Length', '0'))
                payload = json.loads(self.rfile.read(length) or b'{}')
            except (ValueError, json.JSONDecodeError):
                self._send_json({'ok': False, 'error': 'invalid JSON'}, 400)
                return
            try:
                result = backend.command(payload)
            except Exception as error:  # keep the server alive
                result = {'ok': False, 'error': str(error)}
            self._send_json(result)

        def _stream_events(self):
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()

            last_map_version = -1
            try:
                while True:
                    state = backend.state()
                    self._sse('state', state)
                    if state.get('map_version') != last_map_version:
                        self._sse('map', backend.map_payload())
                        last_map_version = state.get('map_version')
                    time.sleep(0.2)
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError):
                return

        def _sse(self, event, obj):
            data = json.dumps(obj)
            chunk = 'event: {}\ndata: {}\n\n'.format(event, data)
            self.wfile.write(chunk.encode('utf-8'))
            self.wfile.flush()

        def log_message(self, format, *args):  # noqa: A002 - stdlib signature
            pass  # keep the console clean

    return DashboardHandler


class DashboardServer:
    def __init__(self, backend, host='0.0.0.0', port=8765):
        self.httpd = ThreadingHTTPServer((host, port), make_handler(backend))
        self.host = host
        self.port = port
        self._thread = None

    def start_background(self):
        self._thread = threading.Thread(target=self.httpd.serve_forever,
                                        daemon=True)
        self._thread.start()

    def serve_forever(self):
        self.httpd.serve_forever()

    def shutdown(self):
        self.httpd.shutdown()


def _default_map_search_paths():
    """Locations where the recorded map may live, relative to this package."""
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = []
    # repo layout: <repo>/ros_ws/src/robot_manager/robot_manager/
    repo_root = os.path.abspath(os.path.join(here, '..', '..', '..', '..'))
    for base in (
        repo_root,
        os.path.join(repo_root, 'ros_ws', 'src', 'navigation_gazebo', 'maps'),
        os.path.join(repo_root, 'ros_ws', 'src', 'slam'),
        os.getcwd(),
    ):
        candidates.append((os.path.join(base, 'my_map_1.pgm'),
                           os.path.join(base, 'my_map_1.yaml')))
        candidates.append((os.path.join(base, 'my_map.pgm'),
                           os.path.join(base, 'my_map.yaml')))
    return candidates


def main(argv=None):
    parser = argparse.ArgumentParser(description='Robot manager dashboard')
    parser.add_argument('--sim', action='store_true',
                        help='run against the built-in robot simulator '
                             '(no ROS required)')
    parser.add_argument('--premapped', action='store_true',
                        help='sim: start with the map already built')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args(argv)

    if not args.sim:
        # ROS mode is started through the robot_manager node so that the
        # backend shares the rclpy executor. Keep this entry point sim-only.
        parser.error('run "ros2 run robot_manager robot_manager" for ROS mode, '
                     'or pass --sim for the simulator')

    from .sim_backend import SimBackend
    backend = SimBackend(map_search_paths=_default_map_search_paths(),
                         premapped=args.premapped)

    server = DashboardServer(backend, host=args.host, port=args.port)
    print('Robot manager dashboard (sim mode, map: {}) on '
          'http://localhost:{}'.format(backend.map_name, args.port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
