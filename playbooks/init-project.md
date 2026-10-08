---
name: bible-init-project
description: Initialize a new project per the "Vibe Engineering Bible" — mode and risk tier, baseline CLAUDE.md/AGENTS.md, what the environment enforces, registry entry. Use when an idea turns into a new repo, folder, or prototype ("set up a project", "initialize per the bible", "init project").
---

# Playbook: init a new project

> Development-agent skill: this file can be shipped as `SKILL.md` (see `usage.md` §6). Framing — Appendix F of the bible.

## Goal

Turn an idea into a repo or folder where, from day one, the goal, owner, mode and risk tier, what the environment enforces, and the rules for AI agents are clear.

Init does not have to build a production-grade system. It has to prevent an experiment from quietly pretending to be T2/T3.

## Inputs

- What we are building and for whom; what outcome we expect.
- Who the owner is.
- Who will use it: only the author, the team, internal users, external users.
- What data is needed: public, synthetic, internal, customer, secrets.
- Expected lifetime: an evening, 30 days, a quarter, a long-lived product.
- Preferred stack or paved road.
- Whether deploy, shared state, or external integrations are needed.

## Deciding the mode and tier (§2–§3 of the bible)

- **Experiment (T0, Covenant of Freedom)** — no production data, no work secrets, no shared state, lifetime up to 30 days. The agent acts on its own in an isolated environment.
- **Engineering mode (Covenant of Discipline)** — anything used by someone other than the author. Inside it, risk tiers:
  - **T1** — a prototype others see. Needs README, owner, sunset date, baseline.
  - **T2** — an internal tool others use. Needs tests, deterministic checks in CI, a basic threat model, a spec for non-trivial changes.
  - **T3** — a product for customers or a public release. Needs the full DoD §5, the two-person rule, a release process, a runbook.

The transition is triggered by an event, not by feel: shown outside your team; someone other than the author started using it; real data, secrets, or shared state became necessary; asked for it to be put on the roadmap. If in doubt between two tiers, pick the lower one for speed, but explicitly write down the event that moves it to the next.

## Steps

1. Write a short project brief: goal, expected outcome, users, data, expected lifetime, owner.
2. Assign the mode and tier T0/T1/T2/T3 and explain why; write down the transition event.
3. Take the baseline `templates/CLAUDE.md.template.md`. If you already have extra infrastructure (service catalog, LLM proxy, managed settings, mandatory PR template), add links to it in section 8 of the copied file.
4. Copy the baseline into the project as `CLAUDE.md` and/or `AGENTS.md`.
5. Fill in the baseline placeholders §1–§3 — including §3.1 "What the environment enforces, and what this file says" — and section 8. Do not rewrite rules §4–§7. Keep the file short: only the non-obvious, target ≤~150 lines.
6. Create or update the `README`: what it is, how to run it, who the owner is, lifecycle, sunset date for T1.
7. For T2+, turn on deterministic checks in CI from day one: build and tests, secrets, slopsquatting check / internal package mirror, SAST high/critical, license scan, CODEOWNERS (including agent configuration). Probabilistic checks (AI review) — advisory only.
8. For T2+, create `openspec/` or record the first spec before code; name the expected outcome in it.
9. Prepare the `registry.md` entry using `templates/project-registry-entry.md`.
10. Fill in `templates/init-result.md` and put the next actions into the nearest PR/issue.

## Definition of Ready

The project is ready for its first meaningful PR if:

- There is an owner.
- The mode and tier are recorded in the README or the registry; the transition event is named.
- There is a `CLAUDE.md`/`AGENTS.md` for T1+, with §3.1 filled in.
- For T1 there is a sunset date.
- For T2+ the deterministic checks are on in CI, or recorded as explicit debt with an owner and a deadline.
- For T2+ there is no direct lethal trifecta: private data + untrusted input + external channel.
- For T2+ the expected outcome is named.
