---
name: bible-review-pr
description: Pre-PR / PR review per the "Vibe Engineering Bible" — scope, AI disclosure (Assisted-by), dependencies and agent configuration, tests, security, spec, evidence bundle and outcome; a verdict with sin shortcodes. Use before opening or merging an AI PR and before a T2/T3 release ("review this PR against the bible", "pre-PR review", "review this diff"). Advisory; a human decides on the merge.
---

# Playbook: pre-PR / PR review per the bible

> Development-agent skill: this file can be shipped as `SKILL.md` (see `usage.md` §6). Framing — Appendix F of the bible.

## Goal

Check a change before merge: has the scope spread, have AI-specific risks appeared, is the DoD of the current tier met, is there an evidence bundle, and are there grounds to reject it with a normalized sin shortcode.

This review is a probabilistic check: it advises, a human decides. The agent does not review its own diff as the final reviewer, and its "LGTM" does not replace human review.

## When to run

- Before opening a large PR.
- Before merging an AI-tagged PR.
- Before a T2/T3 release.
- After the agent produced a substantial part of the diff.

## Inputs

- Diff, branch, or PR.
- Project tier T1/T2/T3.
- Related spec: `openspec/changes/<x>/proposal.md` or the task plan.
- Which checks have already been run.

## Steps

1. Read §7 of the bible as the main checklist.
2. Check AI disclosure: the `Assisted-by:` trailer in commits and `[ai]` in the PR title if AI contributed a substantial part. The responsible author is a human.
3. Check PR size: target ≤200 LOC, ceiling 400 LOC. If larger — propose a split: human review time is limited.
4. Check scope: the diff changes only what was declared.
5. Check new dependencies: existence, reputation, lockfile, license/security scan. Agent configuration (skills, plugins, MCP, hooks, `AGENTS.md`) is a dependency too: owner, review, pinning.
6. Check tests: no deleted assertions, no tautological tests, tests check the requirement from the spec, written in a separate context.
7. Check security: secret leaks, input validation, authz, SQL/HTML injection, fail-open, lethal trifecta, agent autonomy beyond the tier.
8. For T2+, check conformance to the spec/proposal, closed `tasks.md`, and whether the expected outcome is named.
9. Check the evidence bundle: link to the spec, check run, known gaps.
10. Check who approves: whoever assigned the task to the agent does not approve that agent's PR; AI review without a human is `#sycophancy`.
11. For T3, check the two-person rule, the release process/runbook, and the critical DoD §5 rows.
12. Formulate the result: blocker, must-fix before merge, advisory, follow-up.

## PR comments

Every blocker must reference one of:

- a specific §7 item;
- a DoD §5 row;
- a §4½ sin shortcode;
- a deviation from the spec per §6.

Consequences follow §4½: a mortal sin blocks (the PR is not merged until fixed; blameless review), a venial sin goes back for rework. Do not use new shortcodes or candidates from `patterns.md`. If a new class of violation is needed, that is not a PR comment but a proposal via `playbooks/propose-bible-change.md`.

## Output

Short format:

```md
## Verdict
Blocker / Must-fix / Advisory / Looks good — the merge decision is a human's

## Findings
- [blocker] `#shortcode` / §5 #N / §7 item N — what was found, why it matters, minimal fix.

## Checks
- Tests: ...
- Security: ...
- Dependencies / agent configuration: ...
- Spec / evidence bundle / outcome: ...
```

If the PR is clean, still list what was checked. "LGTM" without checks is `#sycophancy`.
