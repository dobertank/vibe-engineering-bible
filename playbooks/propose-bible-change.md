---
name: bible-propose-change
description: Propose a change to the "Vibe Engineering Bible", the template, or a playbook from repeated practice — an entry in patterns.md, a proposal per the template, and for the core a reasoned ADR. Use when a finding has repeated 3+ times or a new risk class with evidence has appeared ("propose a bible change", "this should go into the standard", "propose bible change"). The agent prepares a draft; a human opens the PR.
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
5. For the core (§4 commandments, §4½ sins, §5 DoD) — only through the Appendix E gate: an entry in `patterns.md` → ≥3 independent confirmations from different adopters → candidate → a reasoned ADR in `docs/adr/` (context, decision, basis with a link to the source, consequences). Cadence — no more than once a quarter.
6. Fill in `templates/bible-change-proposal.md`.
7. Check the cross-file semantics from the bible repo's `CLAUDE.md`.
8. If there are figures, CVEs, or studies — update Appendix D in the same change.
9. Make a small PR: one reason, one set of files. The agent prepares the draft; a human opens and confirms the upstream PR (Commandment VI).
10. After merge, update `registry.md` or the relevant audit/report if the change came from a specific application.

## Maturity rule

New material first lands in a playbook, the template, or `patterns.md`. It reaches the bible core only if it has become a stable norm, affects DoD/sins/commandments, or is needed for a shared language across projects — and only through the Appendix E gate. The quarterly review removes the outdated, not only adds.
