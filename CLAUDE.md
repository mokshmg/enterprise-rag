# enterprise-rag

Document Q&A over public banking documents (RBI circulars, product T&Cs, fee schedules)
with citations, measured by an evaluation pipeline. Portfolio project, built as a learning exercise.

## Stack
- Python 3.12, managed with **uv** (never use pip or `uv pip install`)
- FastAPI + Pydantic v2, pydantic-settings for config
- Postgres 16 + pgvector (runs in Docker via docker-compose)
- Streamlit (UI), pytest (tests), ruff (lint + format), pre-commit

## Dependencies (requirements.txt workflow)
- Runtime packages are listed in `requirements.txt`; dev-only packages in `requirements-dev.txt`.
- To add a package: add it to the right file, then run
  `uv add -r requirements.txt` or `uv add --dev -r requirements-dev.txt`.
- To remove a package: delete its line from the file AND run `uv remove <pkg>`
  (or `uv remove --dev <pkg>`).
- Never run `uv add <pkg>` directly; the txt files must always match pyproject.toml.
- Ask me before adding any new dependency.

## Commands
- Install deps: `uv sync`
- Run API: `uv run uvicorn app.api.main:app --reload`
- Run tests: `uv run pytest -q`
- Lint + format: `uv run ruff check --fix . && uv run ruff format .`
- Start database: `docker compose up -d`
- Run all hooks: `uv run pre-commit run --all-files`

## Project layout
- `app/api/` — FastAPI routes and request/response models
- `app/core/` — config, logging, shared utilities
- `app/ingestion/` — loading, cleaning, chunking, embedding, upsert
- `app/retrieval/` — vector, keyword and hybrid search, reranking
- `evals/` — golden questions and evaluation scripts
- `tests/` — pytest tests, mirroring the `app/` structure
- `data/raw/` — source PDFs (git-ignored)

## Conventions
- Type hints on every function; Pydantic models at API boundaries
- All settings come from `app/core/config.py` (environment variables); never hard-code values
- Small, focused functions; no new dependency without asking first
- Every new feature or bug fix comes with a test
- Commit messages follow Conventional Commits: `feat:`, `fix:`, `test:`, `docs:`, `chore:`, `refactor:`

## Never
- Read, print or commit `.env` or any secret / API key
- Edit files in `data/raw/` or commit PDFs
- Change unrelated files while doing a task
- Run destructive commands (`git push --force`, `docker compose down -v`, `rm -rf`) without asking

## How to work with me (learning mode)
I am learning industry practices with this project.
- Before writing code for a non-trivial task, propose a short plan and wait for my OK.
- Keep changes small: one concern per change.
- After a change, explain *what* you did and *why* in a few bullets, and name any concept I should look up.
- When debugging, give ranked hypotheses and how to confirm each before fixing.
- Run tests and ruff before saying a task is done.
