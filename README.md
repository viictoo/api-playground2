# API Playground 

A lightweight repository designed to make GitHub REST API experimentation more readable and repeatable. Use this project to explore API request patterns, observe workflow and review-state behavior, and keep examples organized with a simple docs landing page.

## Why this repo exists 🤔

This repository is not an application or a product. It is a deliberate testbed for:

- exercising GitHub REST API endpoints in a controlled repo layout 🧪
- validating sync, CRUD, and workflow interactions 🔄
- keeping auto-generated or manual API content easy to review 📄
- making documentation the first stop with a dedicated `docs/` landing page 📚

## What’s included ✨

- `src/` — small Python module used to create code paths, commits, and repository content for API tests 🐍.
- `tests/` — a minimal test suite that confirms the repo structure and verifies CI behavior ✅.
- `docs/` — markdown pages that serve as the docs landing area for API examples and content-driven endpoints 📘.
- `.github/workflows/` — workflow definitions for CI, release automation, and manual dispatch scenarios ⚙️.

## Quick start ▶️

1. Clone the repository.
2. Install dependencies if needed.
3. Run the tests:

```bash
python -m pytest
```

That’s all it takes to exercise the sample project and verify the CI pipeline.

## How to use this repo

- Inspect `src/` for example code that provides varied file paths and commit content.
- Open `docs/` to see how markdown pages are used as payload content for API calls.
- Check `.github/workflows/` to observe workflow definitions and how CI is wired into the repository.

## Notes 📝

- This repository is intentionally small and focused on API behavior rather than real application logic.
- The docs here are intended as a landing page for API examples and a place to store meaningful markdown content for tests.

<!-- second commit -->
