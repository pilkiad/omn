# AGENTS.md

You are working inside a self-contained ROS 2 Jazzy Markdown wiki for coding agents.

## Operating Rules

- Treat `content/` as the authoritative ROS 2 Jazzy documentation corpus.
- Start broad queries with `llms.txt`, `index.md`, or the relevant `wiki/*-map.md` file.
- Use `rg` to search the wiki before answering implementation questions.
- Prefer local wiki links over external web links when citing ROS 2 Jazzy docs.
- External links are preserved for upstream package indexes, community resources, and non-Jazzy distributions.
- Do not expect `upstream/`, `_build/`, or a Python virtualenv to exist; this wiki is the final artifact.

## Fast Routes

- Setup and common workflows: [Task map](wiki/task-map.md)
- Concepts and architecture: [Concept map](wiki/concept-map.md)
- Tutorial progression: [Tutorial paths](wiki/tutorial-paths.md)
- Debugging and troubleshooting: [Troubleshooting map](wiki/troubleshooting-map.md)
- Releases, project process, package docs, and tooling: [Tooling map](wiki/tooling-map.md)

## Answering Questions

When answering a ROS 2 question, cite the most specific local content page you used. If a user asks for commands or code, inspect the relevant tutorial or how-to page first so examples match Jazzy-era documentation.
