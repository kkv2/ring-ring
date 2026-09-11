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

- **Assignee:** the person driving the work — the git operator. Today that is `kkv2`.
- **Project:** [moshi-moshi kanban](https://github.com/users/kkv2/projects/7/views/1) (project `7`, owner `kkv2`).

```bash
gh issue create --title "<title>" --body "<body>" --assignee kkv2
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

- **Assignee:** the same git operator as the issue — `kkv2`.
- **Project:** the same project board, `7`.
- **A closing keyword** in the body — `Closes #<n>` — so merging resolves the issue.

```bash
gh pr create --base main --title "<title>" --body "…Closes #<n>" --assignee kkv2
gh project item-add 7 --owner kkv2 --url <pr-url>
```

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
`uv`, `ruff`, `mypy` and `pytest` for the backend, and Vite for the frontend. Update this
section in the PR that introduces them.
