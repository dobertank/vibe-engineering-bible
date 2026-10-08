---
name: bible-audit-project
description: Audit an existing project against the "Vibe Engineering Bible" — risk tier, DoD, environment vs. text, agent configuration, gates, the loop and the outcome; a blocker/warn/note report without changing files. Use before the first application of the bible to a repo, before a tier change, after an incident, and quarterly ("audit this project", "check the project against the bible", "audit project").
---

# Playbook: audit an existing project

> Development-agent skill: this file can be shipped as `SKILL.md` (see `usage.md` §6). Framing — Appendix F of the bible.

## Goal

Understand how well the project matches the bible, which risks block further progress, and which fixes give the most effect without bureaucratic noise.

An audit is not a refactoring. First the report, then the owner's decision, then the edits. The audit itself is an advisory check: a human makes the decisions.

## When to run

- Before the first application of the bible to an existing repo.
- Before a large commit or a tier change T1 → T2 / T2 → T3.
- Before turning on new checks in CI.
- After an incident from the §4½ sin classes (blameless review).
- Quarterly, for projects listed in `registry.md`.

## Inputs

- Repo path.
- A short project goal: what it does, for whom, where it is used, what outcome it should deliver.
- Declared tier T0/T1/T2/T3, if known.
- Constraints: what must not be changed, which checks must not be run.
- Desired result format: full audit or a pre-PR short form.

## Steps

1. Read the bible: §3 (risk tiers), §4, §4½, §5, §6 (the loop), §7, §8, §10, Appendix F.
2. Inspect the repo without changing anything:
   - `README` or equivalent: goal, how to run, owner, lifecycle.
   - `CLAUDE.md`/`AGENTS.md`: is there a baseline, are §3.1 and the repo-specific section filled in, is it bloated (target ≤~150 lines, no repo overviews).
   - **Environment vs. text:** which mandatory rules are enforced by managed settings, hooks, CI, and which live only in text.
   - **Gates:** do deterministic checks (build and tests, secrets, mirror / slopsquatting check, SAST high/critical, license scan, CODEOWNERS) block? Do probabilistic ones (AI review, LLM judge, mutation score) block only after calibration?
   - **Agent configuration:** skills, plugins, MCP servers, hooks — do they have owners (CODEOWNERS), review, version pinning; where were they installed from.
   - **The loop:** is there a spec sized to the task (`openspec/` for T2+), an evidence bundle in PRs, is the expected outcome named and how is it confirmed.
   - Tests/specs: are there tests, ADRs, a threat model; are tests written from the spec, not from the code.
   - Dependencies: new/rare runtime dependencies, lockfile, license/security scans.
   - Data/secrets/agents: signs of the lethal trifecta, external LLM calls, `.env`, agent autonomy beyond the tier.
3. Classify the project's actual tier by the transition events. If the declared and actual tiers differ, record it as a separate finding.
4. Compare the project with DoD §5 for that tier.
5. Go through §7 as an AI-code reviewer: scope, hallucinated APIs, tests, security, edge cases, architecture, spec.
6. Look for §4½ sins using only the normalized shortcodes. Do not invent new ones. Candidates from `patterns.md` are not rejection shortcodes: write a match with a candidate as a note and propose a confirmation via `playbooks/propose-bible-change.md`.
7. Fill in `templates/audit-report.md`.
8. Propose a minimal next action for 1–3 days and a separate list of deferred actions. For a rule a machine can check, propose moving it into the environment rather than adding it to the text.

## Severity

**Blocker** — a mortal sin (the PR or release does not pass until fixed), a breach of an experiment-mode boundary, non-compliance with the mandatory DoD for the current merge/release, a risk of data/secret leakage.

**Warn** — a DoD or baseline mismatch that does not block the current step but must be fixed before a tier change or before a check is turned on; a venial sin.

**Note** — an improvement to process, documentation, environment, or observability without immediate risk.

## Agent behavior rules

- Do not change project files during the audit without a separate confirmation.
- Do not run destructive commands or migrations.
- Do not treat a missing test command as missing tests until you have inspected the README, CI, and manifest.
- Do not raise a blocker over matters of taste. A blocker must reference a § of the bible, a DoD row, or a sin shortcode.
- If a fact is not verified, mark it as a hypothesis and say how to verify it.
- Look for the cause in the environment and the process, not for someone to blame.
