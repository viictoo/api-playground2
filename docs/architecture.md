# Architecture

This is intentionally fluff. The repo exists so GitHub API tests have a non-empty
file tree, and so endpoints like `get-file-contents` and the recursive `git/trees`
call have multi-directory data to chew on.

## Layers

1. **Entrypoint** (`src/main.py`) — calls into utilities.
2. **Utilities** (`src/utils.py`) — pure functions, easy to test.
3. **Tests** (`tests/`) — covered by CI.

## Why three workflows

- `ci.yml` proves a happy-path run exists.
- `release.yml` is intentionally broken so a failed run exists for rerun tests.
- `manual.yml` exists only so `workflow_dispatch` has a target.
