# moshi-moshi Constitution

The rules every spec, plan and implementation in this repository is held to. It restates
what [`CLAUDE.md`](../../CLAUDE.md), [`README.md`](../../README.md) and
[`ROADMAP.md`](../../ROADMAP.md) already commit to, in the form Spec Kit reads.

## Core Principles

### I. No human writes a line of the code (NON-NEGOTIABLE)

Specs, review and direction are human; the implementation is not. moshi-moshi is an
experiment in AI-DLC as much as it is a voice bot, so this rule is the point of the
project rather than a convenience. A change a human hand-edited does not belong in a PR.

### II. Issue → branch → pull request

Every change starts as a GitHub issue, is built on a branch named
`<type>/<issue-number>-<short-description>` cut from an up-to-date `main`, and lands
through one pull request carrying `Closes #<n>`. Nothing is committed directly to `main`.
Issues go on the project board; pull requests do not — the pair is one piece of work.

### III. Honesty about state

Documentation describes what exists. A capability that has not been built is named with
the milestone it arrives at, never in the present tense. Progress is recorded by the Status
markers defined in [Recording progress](../../ROADMAP.md#recording-progress), flipped by the
same pull request that earns them: if a milestone's Done-when is not met, the milestone is
not done, and no marker says otherwise.

### IV. Ship the smallest thing that works

Infrastructure arrives when it is needed and not before — no cloud, no database, no RAG
ahead of the milestone that requires it. A spec that reaches past its milestone is over
scope. If something adjacent is broken, it becomes another issue rather than widening the
current pull request.

### V. Green before merge

`ruff format --check`, `ruff check`, `mypy` and `pytest` all pass before a pull request is
merged, enforced by CI rather than by assertion. Types are strict; a new module is typed
the day it is written. Behaviour worth keeping is worth a test.

## Technology Constraints

The stack is decided and recorded in the README: Python 3.12+ with FastAPI on the backend,
TypeScript with React and Vite on the frontend, Gemini Live for speech-to-speech, Twilio
for telephony, PostgreSQL reached through SQLAlchemy with Alembic owning every schema
change, and uv, Ruff, mypy and pytest as the toolchain. A spec that wants something else
changes the README in the same pull request or does not use it.

The product is Japanese-only. The repository — documentation, comments, issues, pull
requests, commit messages — is written in English.

UI is built from the tokens in [`docs/design/BRAND.md`](../../docs/design/BRAND.md) and
[`docs/design/tokens.css`](../../docs/design/tokens.css). No new colour without amending
`BRAND.md` in the same pull request.

## Development Workflow

Specs live in `specs/`, one directory per feature, produced by `/speckit-specify` and
planned by `/speckit-plan` before implementation starts. Spec Kit is the intended vehicle
for Spec Driven Development, but it is optional — Principle I is not.

Commits are present tense, imperative, and scoped to one idea, carrying the
`Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` trailer.

## Governance

This constitution supersedes habit and convenience. Amending it means changing this file
in a pull request of its own, with the reason stated; where it overlaps `CLAUDE.md`, both
move together. Every pull request is reviewed against these principles, and complexity
that cannot be justified against Principle IV is removed rather than explained.

**Version**: 1.0.0 | **Ratified**: 2026-09-11 | **Last Amended**: 2026-09-11
