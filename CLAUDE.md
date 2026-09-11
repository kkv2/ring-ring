# CLAUDE.md

Conventions for AI contributors to `kkv2/moshi-moshi`.

## The prime rule

**No human writes a line of the code.** Specs, review and direction are human; the
implementation is not. This project is a personal experiment in AI-DLC as much as it is a
voice bot, so the rule is the point — not a convenience.

GitHub Spec Kit and Spec Driven Development are the intended vehicle, but they are optional.
The rule above is not.

## Workflow

Every change follows the same path:

```
GitHub issue  →  branch cut from main  →  pull request  →  main
```

Never commit directly to `main`.

### 1. Issue

Open an issue before starting work. Every issue gets:

- **Assignee:** `@me` — the GitHub account Claude Code is authenticated as, which is the
  person who asked for the work. Never hardcode a username; see *Assignment* below.
- **Project:** [moshi-moshi kanban](https://github.com/users/kkv2/projects/7/views/1)
  (project `7`, owner `kkv2`). The board belongs to the repository, so this one *is* fixed.

```bash
gh issue create --title "<title>" --body "<body>" --assignee "@me"
gh project item-add 7 --owner kkv2 --url <issue-url>
```

### 2. Branch

Cut from an up-to-date `main`. Name it:

```
<type>/<issue-number>-<short-description>
```

For example `feature/12-model-selector`, `chore/3-tech-stack-setup`,
`docs/1-readme-and-roadmap`.

| Type | For |
|---|---|
| `feature` | New capability |
| `fix` | Bug fix |
| `chore` | Tooling, dependencies, repo plumbing |
| `docs` | Documentation and project assets |
| `refactor` | Behaviour-preserving change |
| `test` | Tests only |

### 3. Pull request

One PR per issue, into `main`. Every PR gets:

- **Assignee:** `@me`, the same account as the issue.
- **A closing keyword** in the body — `Closes #<n>` — so merging resolves the issue.

**Do not add pull requests to the project board.** Issues and PRs move as a pair, so a PR on
the board is the same work tracked twice. The issue is the card; the PR is how it gets done.

```bash
gh pr create --base main --title "<title>" --body "…Closes #<n>" --assignee "@me"
```

### Assignment

Issues and PRs are assigned to **whoever ran Claude Code**, resolved at the time of the call —
not to a name written down here. `gh` expands `@me` to the authenticated account, so
`--assignee "@me"` is the whole mechanism.

Today that account is `kkv2`, and while this stays a solo project it always will be. That is a
fact about who is working, not a rule, and the convention must not encode it. If a second
person ever contributes, their work should land under their own name without anyone editing
this file.

### Commits

Present tense, imperative, scoped to one idea. Claude Code appends its trailer:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

## House rules

**Language.** Everything committed to the repository — README, roadmap, docs, code comments,
issues, PRs, commit messages — is written in **English**. The *product* is Japanese-only
(see the README's out-of-scope note); the *repository* is not.

**Design.** Colours, type and the dial mark are already decided and written down in
[`docs/design/BRAND.md`](docs/design/BRAND.md), with values in
[`docs/design/tokens.css`](docs/design/tokens.css). Build UI from those tokens. Do not
introduce a new colour without changing `BRAND.md` in the same PR.

**Honesty about state.** The repository is at Milestone 0 — nothing is wired up yet. Do not
write documentation that describes behaviour which does not exist. If a document must mention
a future capability, say which milestone it arrives at. See [`ROADMAP.md`](ROADMAP.md).

**Scope.** Do the issue. If something adjacent is broken, open another issue rather than
widening the PR.

## Layout

Planned monorepo shape — directories appear as milestones land.

```
apps/api/     Python · FastAPI — Twilio webhooks, media bridge, agent tools
apps/web/     TypeScript · React — tenant and operator consoles
packages/     shared types and contracts
specs/        GitHub Spec Kit specs and plans
docs/design/  BRAND.md, tokens.css, dial.svg
docs/assets/  hero banner
```

## Commands

Nothing is set up yet; the toolchain arrives with
[Milestone 0](ROADMAP.md#milestone-0--set-up-the-repository). When it does, it will be
`uv`, `ruff`, `mypy` and `pytest` for the backend, `alembic` for schema changes once
[Milestone 2](ROADMAP.md#milestone-2--manage-call-sessions) lands, and Vite for the frontend. Update this
section in the PR that introduces them.
