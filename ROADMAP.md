# Roadmap

The guiding principle: **get "the phone is talking to an AI" working as fast as possible.**

No AWS, no database, no RAG, no admin console at the start. A Mac running FastAPI locally,
exposed through a tunnel, answering a real phone call. Infrastructure comes later, when
there is something worth deploying.

Each milestone is a visible step up:

> **M1 it's a phone call! → M2 it keeps records → M3 it does real work → M4 it looks
> things up → M5 it's a call center → M6 it's a service.**

## Recording progress

Every milestone below carries a **Status** line. It is one of three things:

| Marker | Meaning |
|---|---|
| ✅ **Complete** | The milestone's *Done when* is met, dated, and linked to the pull request that met it |
| ▶ **Current** | What the repository is working toward now. Says nothing about what exists yet |
| ☐ **Planned** | Not started |

Exactly one milestone is **Current** at a time, and it is the one the README's status badge
names.

**The pull request that meets a milestone's *Done when* flips its Status in the same pull
request** — the claim and the evidence land together, and no later tidy-up is owed. Flipping
one means four edits, all of them in that PR:

1. this file — the finished milestone becomes ✅ with today's date and its PR link, and the
   next one becomes ▶
2. [`README.md`](README.md) — the marker in the Roadmap table
3. [`README.md`](README.md) — the status badge at the top, renamed to the new **Current**
   milestone
4. [`README.md`](README.md) — any Features row the milestone delivers, ☐ → ☑

A milestone whose *Done when* is not demonstrably met stays ▶. Partial credit is not a
marker.

---

## Milestone 0 — Set up the repository

**Status:** ✅ Complete — 2026-09-11 ([#4](https://github.com/kkv2/moshi-moshi/pull/4))

Build the foundation of `kkv2/moshi-moshi`.

**Scope**

- Python / FastAPI / uv / pytest / Ruff / mypy set up and running
- GitHub Spec Kit in place, so SDD and AI-DLC can actually drive development
- Issue → branch → PR workflow established, conventions written into `CLAUDE.md`

**Not yet:** the phone, the AI. Neither is connected at this stage, and that's fine.

**Done when:** a fresh clone can install, lint, type-check, and run the test suite.

---

## Milestone 1 — Talk to an AI over the phone

**Status:** ▶ Current

**The first big one.**

Call a Twilio number from your own phone, reach FastAPI running on your Mac, and have a
real-time voice conversation with Gemini Live.

**Architecture — the minimum that can possibly work**

```
📱 phone → Twilio → tunnel → localhost FastAPI → Gemini Live API
```

FastAPI runs locally; ngrok or Cloudflare Tunnel makes it reachable from Twilio.

**Not yet:** AWS, databases, RAG, admin console. None of it.

**Done when:**

> You call your own phone number and hold a natural back-and-forth with the AI for
> several turns.

That's the entire success criterion.

---

## Milestone 2 — Manage call sessions

**Status:** ☐ Planned

Turn "an AI that answers the phone" into something that behaves like a system.

**Scope**

- Call lifecycle: start, end, call ID, duration, disconnect reason
- Logs good enough to reconstruct what happened during any single call

**Persistence:** introduce PostgreSQL at the point where it's actually needed, not before —
reached through SQLAlchemy, with Alembic owning the schema from the first migration. Never let
the schema drift ahead of a migration.

**Done when:** any past call can be traced end to end from its records.

---

## Milestone 3 — Let the AI call the backend

**Status:** ☐ Planned

Give Gemini tools.

Ask "what are your business hours?" and the model doesn't bluff — it calls something like
`check_business_hours` on the Python side and answers from the result.

This is the step where a **conversational AI becomes a voice bot that does work**.

**Done when:** a caller gets an answer that provably came from backend code, not from the
model's imagination.

---

## Milestone 4 — Answer from internal knowledge (RAG)

**Status:** ☐ Planned

Prepare a knowledge base — FAQs, the manual of a fictional company — and let the agent
search it.

When a caller asks a question, the AI runs RAG retrieval as a tool and answers from what
it finds.

At this point it starts to genuinely resemble **a first-line call center AI**.

**Done when:** a question answerable only from the knowledge base gets answered correctly
over the phone.

---

## Milestone 5 — Become a miniature call center

**Status:** ☐ Planned

The actual point of moshi-moshi.

**Scope**

- Customer lookup
- Inquiry classification
- Interaction history
- Call summarization
- Escalation to a human agent
- An admin console, if and when one is warranted

**Graduating from local PoC**

Once it's worth it, and only then:

```
Docker → AWS (ECS / Fargate) → RDS → monitoring
```

**Done when:** a call can be taken, resolved or escalated, summarized, and reviewed
afterwards — end to end.

---

## Milestone 6 — Become a multi-tenant service

**Status:** ☐ Planned

Turn one call center into many.

Everything up to here serves a single organisation. M6 makes every layer tenant-scoped and
adds the console the operator uses to run the whole thing.

**Scope**

- **Tenant isolation** across calls, sessions, knowledge and history — no tenant can reach
  another tenant's data
- **Per-tenant dashboard** — call volume, resolution rate, escalations, recent calls
- **Per-tenant AI staff editor** — persona, voice, greeting, escalation rules, configured in
  a screen rather than in code
- **Per-tenant knowledge registration** — the RAG corpus from M4, uploaded and maintained by
  the tenant itself
- **Per-tenant phone numbers** — an inbound call resolves to the right tenant by the number
  it arrived on
- **An operator console** above all of it, for the person running the service

**The open question: provisioning**

Creating a tenant and getting a phone number for it may not be automatable end to end. Buying
a Twilio number, carrier registration and any local requirements are not one API call in every
case. The likely shape is that a tenant applies, and the operator buys and wires the number by
hand from the operator console. Treat fully automatic provisioning as a stretch goal, not a
requirement — the milestone does not depend on it.

**On scope.** This is the *architecture* of a SaaS, not a business. moshi-moshi stays a hobby
project and is not being taken to market; see the README's out-of-scope note.

**Done when:** two tenants run side by side on their own numbers, with their own knowledge and
their own AI staff, and neither can see the other's calls.
