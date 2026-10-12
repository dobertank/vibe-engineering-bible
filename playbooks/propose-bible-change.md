---
name: bible-propose-change
description: Propose a change to the "Vibe Engineering Bible", the template, or a playbook from repeated practice — an entry in patterns.md, a proposal in the built-in format, and for the core a reasoned ADR. Use when a finding has repeated 3+ times or a new risk class with evidence has appeared ("propose a bible change", "this should go into the standard", "propose bible change"). The agent prepares a draft; a human opens the PR.
---

# Playbook: propose a change to the bible

> Development-agent skill: this file can be shipped as `SKILL.md` (see `usage.md` §6). Framing — Appendix F and the Appendix E gate of the bible.

## Goal

Keep the bible alive but not noisy: new rules come from repeated facts, not from one-off irritation or one reviewer's taste. Outdated rules are removed as explicitly as new ones are added.

## When to run

- The same audit finding repeated in 3+ projects.
- The same instruction to the agent repeated 3+ times and clearly reduces risk.
- A new class of AI/security risk appeared with verifiable evidence.
- A practice from a pilot became the paved road and should go into the template, a playbook, or the environment.
- A rule is outdated or already enforced by the environment — time to remove it.

## When not to run

- The change concerns only one repo: that is section 8 of the local `CLAUDE.md`/`AGENTS.md`.
- There is only an opinion without evidence.
- There is a new figure/study, but the source is not verified and not ready for Appendix D.
- You need to bypass a rule temporarily for a hotfix: that is an exception in the PR/release, not a change to the canon.

## Steps

1. Describe the trigger: where and when the pattern arose.
2. Collect evidence: links to PRs, audit reports, incident reviews, meeting notes — no secrets.
3. Determine the scope:
   - `playbooks/` — the way of applying the bible changes.
   - `templates/CLAUDE.md.template.md` — the baseline for product repos changes.
   - `patterns.md` — a new field pattern or a sin candidate (advisory, not canon).
   - `vibe-engineering-bible.md` — the canon changes: commandment, DoD, sin, glossary, appendix.
   - `README.md` / `usage.md` — navigation and user flow change.
4. If a machine can check the rule, first propose moving it into the environment (managed settings, hooks, CI) rather than adding it to the text.
5. For the core (§4 commandments, §4½ sins, §5 DoD) — only through the Appendix E gate (confirmation threshold, candidate, cadence): an entry in `patterns.md` → candidate → a reasoned ADR in `docs/adr/`.
6. Write the proposal in the format below; for the core — an ADR.
7. Cross-check the affected files against the "you edit X → check Y" table in the bible repo's `AGENTS.md`.
8. If there are figures, CVEs, or studies — update Appendix D in the same change.
9. Make a small PR: one reason, one set of files. The agent prepares the draft; a human opens and confirms the upstream PR (Commandment VI).
10. After merge, update `registry.md` or the relevant audit/report if the change came from a specific application.

## Output

A proposal — as the PR or issue text:

```md
# Proposal: <short title>
Status: draft · Author: <name/team> · Date: <YYYY-MM-DD>
Class: <satellite (playbook, template, usage) / patterns.md / core — only through the Appendix E gate>
Type: <add / change / remove outdated / move from text into the environment>

## Trigger and evidence
<What happened; links to audit reports, PRs, incident reviews. For the core — independent confirmations: N, entries in patterns.md.>

## Problem
<Which risk repeats; why section 8 of the local file is not enough; can the environment enforce it instead of text.>

## Proposed Change
<A diff of meaning, not an essay. Affected files; links cross-checked against `AGENTS.md`.>

## Sources and rollout
<New figures/CVEs → Appendix D in the same change. How to apply to projects in registry.md: a deterministic check — block immediately with a fix path; a probabilistic one — advisory → calibration → block; a text rule — a template diff.>

## Rejection Criteria
<Under which facts to reject it or keep it as one repo's rule.>
```

For the core — a reasoned ADR `docs/adr/<NNNN>-<name>.md` in this format:

```md
# ADR <NNNN>. <The decision in one sentence>
- **Status:** proposed / accepted <date>.
- **Date:** <YYYY-MM-DD>.
- **Process context.** <Which core sections are affected; the Appendix E gate is passed: candidate, confirmations.>
- **Trigger:** <What happened; links to patterns.md entries and Appendix D sources.>

## Decisions
### 1. <Decision>
- **Context.** <Why.>
- **Decision.** <What changes in §4 / §4½ / §5; the basis with a link to the source.>
- **Consequences.** <The cost; which files were synced (the `AGENTS.md` table), the counts.>

## Deliberately not changed
<What stayed as it was, and why.>
```

## Maturity rule

New material first lands in a playbook, the template, or `patterns.md`. It reaches the bible core only if it has become a stable norm, affects DoD/sins/commandments, or is needed for a shared language across projects — and only through the Appendix E gate. The quarterly review removes the outdated, not only adds.
