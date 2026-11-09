# Local tasks

**What this is:** the append-only task queue for this repository.

A task is one JSON file. The file is the task. No creator, platform, status, or
sync metadata.

The canonical schema, template, and lifecycle live in
`templates/md/docs/issues/`.

- Filename: `<rank>-<slug>.json`; one to six fractional digits, no trailing zero.
- Rank: `3.x` bug, `2.x` documentation or chore, `1.x` feature or refactor.
  Higher fraction = more important.
- Pick the highest-ranked task; open one work PR.
- The PR deletes the task file; merge completes the task.
- A failed attempt appends to `attempts` and keeps the file.
