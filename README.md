# API Playground

A throwaway repository used to exercise GitHub REST API endpoints — sync flows, CRUD actions, workflow runs, and review state.

## What's here

- `src/` — toy Python module so commits and file-tree calls have varied paths.
- `tests/` — a single passing test that the CI workflow runs.
- `docs/` — long-form markdown to give the contents endpoints something to read.
- `.github/workflows/` — three workflows: a passing CI, a failing release pipeline, and a manual dispatch.

## Running locally

```bash
python -m pytest
```

That's it. Nothing in here is meant to be useful — only meaningful to API tests.
