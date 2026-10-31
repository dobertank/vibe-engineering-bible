---
name: bible-init-project
description: Use when an idea becomes a new repository, folder, or prototype that will adopt the Vibe Engineering Bible.
---

# Playbook: init a new project

> Development-agent skill: the builder creates a `SKILL.md` router and pinned resources from this source (see `usage.md` §6). Framing — Appendix F of the bible.

## Goal

Turn an idea into a repo or folder where, from day one, the goal, owner, level, what the environment enforces, and the rules for AI agents are clear.

Init does not have to build a production-grade system. It has to prevent a prototype from quietly becoming Production and bypassing the DoD.

## Inputs

- What we are building and for whom; what outcome we expect.
- Who the owner is.
- Who will use it: only the author, the team, internal users, external users.
- What data is needed: public, synthetic, internal, customer, secrets.
- Expected lifetime: an evening, 30 days, a quarter, a long-lived product.
- Preferred stack or paved road.
- Whether deploy, shared state, or external integrations are needed.

## Deciding the level (§2–§3 of the bible)

- **Prototype (Covenant of Freedom)** — the author's personal experiment with no production or customer data, no work secrets, no shared state, lifetime up to 30 days. No rituals and no baseline; the agent acts on its own in an isolated environment.
- **Production (Covenant of Discipline)** — anything used by someone other than the author: from a utility for the neighboring team to a customer-facing service. Needs README, owner, baseline, catalog entry, tests and deterministic checks in CI, human review, a basic threat model, a spec for non-trivial changes.
- **"+ customers"** — an overlay on Production, not a third level: customers, customer data, or a public release. Adds a full threat model, mutation testing, a second senior+ reviewer, gradual rollout with rollback, a runbook, a kill-switch.

The transition is triggered by an event, not by feel: shown outside your team; someone other than the author started using it; real data, secrets, or shared state became necessary; asked for it to be put on the roadmap. Showing it inside your own team is not a transition. Pick Prototype only if all three boundaries hold, and explicitly write down the event that moves it to Production.

## Steps

1. Write a short project brief: goal, expected outcome, users, data, expected lifetime, owner.
2. Assign the level (Prototype / Production; for Production — customers: yes / no) and explain why; write down the transition event. For Production, name the §3 human-check mode: team review or solo author check without customers; auto-merge only under §3 conditions.
3. For Production (steps 3–8; a prototype does not need them), take the baseline `templates/CLAUDE.md.template.md`. If you already have extra infrastructure (service catalog, LLM proxy, managed settings, mandatory PR template), add links to it in section 8 of the copied file.
4. Copy the baseline into the project as `CLAUDE.md` and/or `AGENTS.md`.
5. Fill in the baseline placeholders §1–§3 — including §3.1 "What the environment enforces, and what this file says" — including access and data-flow controls and how they are verified; a gateway is optional — and section 8. Do not rewrite rules §4–§7. Keep the file short: only the non-obvious, target ≤~150 lines.
6. For Production, create or update the `README`: what it is, how to run it, who the owner is, lifecycle.
7. For Production, turn on deterministic checks (class D, §5 of the bible) in CI from day one; set up branch protection in the repository settings, out of the agent's reach. Probabilistic checks (AI review) — advisory only; the exception is a fail-closed gate on the agent's untrusted input, set up as a harness hook rather than in CI (§5 #41).
8. For Production, create `openspec/` or record the first spec before code; name the expected outcome in it.
9. Optionally prepare a `registry.md` draft row (fields — the legend under the registry table); upstream registration requires the owner's consent and a human-opened PR.
10. Output the result in the format below and put the next actions into the nearest PR/issue.

## Definition of Ready

The project is ready for its first meaningful PR if:

- There is an owner.
- The level and the "customers" flag are recorded in the README or the registry; the transition event is named.
- For a prototype the environment holds the three boundaries; lifetime ≤30 days.
- For Production there is a `CLAUDE.md`/`AGENTS.md`, with §3.1 filled in.
- For Production the deterministic checks are on in CI, or recorded as explicit debt with an owner and a deadline.
- For Production there is no direct lethal trifecta: private data + untrusted input + external channel.
- For Production the expected outcome is named.

Mark unverified environment evidence `unknown`, not `fail`; `fail` means a confirmed mismatch. An unknown mandatory item leaves readiness unconfirmed. A statement in the baseline is not evidence that its control works.

## Output

```md
# Init: <project>
Date: <YYYY-MM-DD> · Owner: <name/team> · Expected lifetime: <duration> · Baseline: <CLAUDE.md / AGENTS.md / both / none>

## Brief
<What we are building, for whom, which data, constraints.> Expected outcome: <what will change and how we will confirm it; mandatory for Production>

## Level
<Prototype / Production> · customers: <yes / no>. Why: <reasons>. Transition event: <trigger>.
Agent autonomy: <Prototype — on its own in an isolated environment / Production — into shared code only after human review / + customers — only proposals or actions with confirmation>

## Created / updated
README · CLAUDE.md/AGENTS.md · openspec/ · CI: deterministic checks, probabilistic (advisory) · CODEOWNERS on agent configuration · row in registry.md — <yes / no / path / n-a for each>

## Definition of Ready
| Item (list above) | pass / fail / unknown / n-a | Comment |
|---|---|---|

## Next Actions
1. <first action>
2. <second>
3. <third>
```
