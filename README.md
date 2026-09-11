<p align="center">
  <img src="docs/assets/hero-20-ink.png" alt="moshi-moshi — Hello? AI speaking." width="100%">
</p>

<h1 align="center">moshi-moshi</h1>

<p align="center">
  <strong>Hello? AI speaking.</strong><br>
  A miniature AI call center where voice agents answer real phone calls.
</p>

<p align="center">
  <img alt="status: milestone 1" src="https://img.shields.io/badge/status-milestone%201-D2A94E">
  <img alt="backend: FastAPI" src="https://img.shields.io/badge/backend-FastAPI-2E5480">
  <img alt="frontend: React" src="https://img.shields.io/badge/frontend-React-2E5480">
  <img alt="development: AI-DLC" src="https://img.shields.io/badge/development-AI--DLC-16304E">
</p>

---

## Overview

**moshi-moshi** replaces the first line of a phone support desk with AI.

Someone calls a real phone number, an AI voice agent picks up, understands what they
need, looks up the answer, and either resolves the call or hands it over to a human.
That is the whole idea — a call center, shrunk down to something one person can build.

> **On the name.** In Japan a phone call opens with *"moshi moshi"* (もしもし) — the
> equivalent of "hello?" when you pick up the receiver. This project starts where every
> phone call starts.

**Status: Milestone 1.** [M0](ROADMAP.md#milestone-0--set-up-the-repository) is done —
the repository installs, lints, type-checks and tests. None of the features below is wired
up yet; the phone call is what is being built now. See [ROADMAP.md](ROADMAP.md) for where
each milestone stands, and [Getting started](#getting-started) for what runs today.

## Features

| | Feature | Milestone |
|---|---|---|
| ☐ | **Real phone calls** over the PSTN via Twilio, bridged into a web backend | [M1](ROADMAP.md#milestone-1--talk-to-an-ai-over-the-phone) |
| ☐ | **Natural voice conversation** using a speech-to-speech model (Gemini Live API) — no STT → LLM → TTS chain, no robot cadence | [M1](ROADMAP.md#milestone-1--talk-to-an-ai-over-the-phone) |
| ☐ | **Call session management** — call IDs, duration, disconnect reasons, traceable logs | [M2](ROADMAP.md#milestone-2--manage-call-sessions) |
| ☐ | **Tool calling** — the agent runs real backend functions instead of guessing | [M3](ROADMAP.md#milestone-3--let-the-ai-call-the-backend) |
| ☐ | **RAG over internal knowledge** — FAQs and manuals searched mid-call, so the first response is actually interactive | [M4](ROADMAP.md#milestone-4--answer-from-internal-knowledge-rag) |
| ☐ | **Escalation to a human** as the second line, when the AI can't close the call | [M5](ROADMAP.md#milestone-5--become-a-miniature-call-center) |
| ☐ | **Multi-tenant operation** — each tenant with its own number, knowledge, AI staff and dashboard, behind one operator console | [M6](ROADMAP.md#milestone-6--become-a-multi-tenant-service) |

## How it works

```mermaid
flowchart LR
    C["📱 Caller"] -->|PSTN| TW[Twilio]
    TW <-->|"Media Streams<br/>(WebSocket, μ-law 8kHz)"| TN["Tunnel<br/>ngrok / Cloudflare"]
    TN <--> API["FastAPI<br/>(localhost)"]
    API <-->|"bidirectional audio"| G["Gemini Live API"]
    G -.->|tool calls| API
    API --> KB[("Knowledge base<br/>RAG")]
    API --> HU["👤 Human agent"]
    API --> UI["React console"]
```

Audio flows both ways in real time: Twilio streams the caller's voice to FastAPI over a
WebSocket, FastAPI relays it to Gemini Live, and the model's speech goes straight back
down the same pipe. Everything runs on a laptop, exposed through a tunnel — no cloud
infrastructure until it's actually needed.

## Tech stack

| Layer | Choice |
|---|---|
| Backend | Python 3.12+ · [FastAPI](https://fastapi.tiangolo.com/) · [SQLAlchemy](https://www.sqlalchemy.org/) + [Alembic](https://alembic.sqlalchemy.org/) for persistence and migrations (from [M2](ROADMAP.md#milestone-2--manage-call-sessions)) |
| Frontend | TypeScript · React · [Vite](https://vite.dev/) · Tailwind CSS |
| Voice AI | [Gemini Live API](https://ai.google.dev/gemini-api/docs/live) (Gemini 2.5, GA) — speech-to-speech |
| Telephony | [Twilio](https://www.twilio.com/docs/voice) Programmable Voice + Media Streams |
| Data | [PostgreSQL](https://www.postgresql.org/) — call sessions, history, tenants (arrives at [M2](ROADMAP.md#milestone-2--manage-call-sessions)) |
| Vector store | [pgvector](https://github.com/pgvector/pgvector) — RAG embeddings (arrives at [M4](ROADMAP.md#milestone-4--answer-from-internal-knowledge-rag)). Not finally decided; it is the default because Postgres is already there. |
| Tooling | [uv](https://docs.astral.sh/uv/) · [Ruff](https://docs.astral.sh/ruff/) · mypy · pytest |
| Packaging | Docker |
| Process | [GitHub Spec Kit](https://github.com/github/spec-kit) (Spec Driven Development) |

Infrastructure and cloud are deliberately deferred. Everything runs locally first.

## Repository layout

A monorepo. Directories marked *planned* appear as milestones land:

```
moshi-moshi/
├── apps/
│   ├── api/          # Python / FastAPI — Twilio webhooks, media bridge, agent tools
│   └── web/          # TypeScript / React — tenant and operator consoles   (planned)
├── packages/         # shared types and contracts                          (planned)
├── specs/            # GitHub Spec Kit specs and plans                     (planned)
├── .specify/         # Spec Kit templates, scripts, constitution
├── docs/
│   ├── design/       # palette, dial mark, type — see BRAND.md
│   └── assets/       # hero banners
├── pyproject.toml    # uv workspace — Ruff, mypy and pytest configured once
├── CLAUDE.md         # conventions for AI contributors
└── ROADMAP.md
```

## Design

The banner above is the identity: a prepaid telephone card in deep navy, printed in ivory, with
brass punch marks. The palette, the dial mark and the type rules are written down in
[`docs/design/BRAND.md`](docs/design/BRAND.md), with the values as CSS custom properties in
[`docs/design/tokens.css`](docs/design/tokens.css) — the operator console should be built from those
rather than from fresh choices.

## Getting started

There is no phone call to make until [Milestone 1](ROADMAP.md#milestone-1--talk-to-an-ai-over-the-phone)
lands, but the backend runs and the checks pass today.

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/); it fetches Python
3.12 itself.

```bash
git clone https://github.com/kkv2/moshi-moshi.git
cd moshi-moshi
uv sync
```

Then, from the repository root:

```bash
uv run ruff check .   # lint
uv run mypy           # type-check (strict)
uv run pytest         # test
uv run uvicorn moshi_moshi_api.main:app --reload
```

The API comes up on <http://127.0.0.1:8000>, where `GET /health` answers and `/docs` shows
the schema. That is the entire surface today — Twilio and Gemini Live are wired up at
[M1](ROADMAP.md#milestone-1--talk-to-an-ai-over-the-phone).

## Roadmap

| | | Milestone | Outcome |
|---|---|---|---|
| ✅ | **M0** | [Development environment](ROADMAP.md#milestone-0--set-up-the-repository) | The repo is ready to build in |
| ▶ | **M1** | [Talk to an AI over the phone](ROADMAP.md#milestone-1--talk-to-an-ai-over-the-phone) | **It's a phone call!** |
| ☐ | **M2** | [Manage call sessions](ROADMAP.md#milestone-2--manage-call-sessions) | It keeps records |
| ☐ | **M3** | [Let the AI call the backend](ROADMAP.md#milestone-3--let-the-ai-call-the-backend) | It does real work |
| ☐ | **M4** | [Answer from internal knowledge](ROADMAP.md#milestone-4--answer-from-internal-knowledge-rag) | It looks things up |
| ☐ | **M5** | [Become a miniature call center](ROADMAP.md#milestone-5--become-a-miniature-call-center) | It's a call center |
| ☐ | **M6** | [Become a multi-tenant service](ROADMAP.md#milestone-6--become-a-multi-tenant-service) | It's a service |

✅ complete · ▶ current · ☐ planned — the same markers the milestones carry in
[ROADMAP.md](ROADMAP.md), which explains how and when they are flipped. Full detail there
too.

## Development

This project is an experiment in **AI-DLC (AI-Driven Life Cycle)** as much as it is a
voice bot. Development runs on Spec Driven Development with GitHub Spec Kit, and one rule
holds above all others:

> **No human writes a line of the code.** Specs, review, and direction are human. The
> implementation is not. Spec Kit itself is optional; this rule is not.

Working conventions:

- Work starts from a GitHub issue, on a branch cut from `main`, and lands through a pull
  request into `main`.
- Branches are named `<type>/<issue-number>-<short-description>` — for example
  `feature/12-model-selector` or `chore/3-tech-stack-setup`.
- Detailed conventions for AI contributors live in `CLAUDE.md`.

## Out of scope

- **Languages other than Japanese.** Japanese only, for now. Other languages are a maybe,
  not a plan.
- **Commercial use.** This is a personal, hobby project and is not headed for production
  as a product.
