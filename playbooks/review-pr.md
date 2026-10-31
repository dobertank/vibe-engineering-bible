---
name: bible-review-pr
description: Use when an AI-assisted diff or pull request needs review against the Vibe Engineering Bible before opening, merging, or a Production release.
---

# Playbook: pre-PR / PR review per the bible

> Development-agent skill: the builder creates a `SKILL.md` router and pinned resources from this source (see `usage.md` §6). Framing — Appendix F of the bible.

## Goal

Check a change before merge: has the scope spread, have AI-specific risks appeared, is the DoD of the current level met, is there an evidence bundle, and are there grounds to reject it with a normalized sin shortcode.

This review is a probabilistic check: it advises, a human decides. The agent does not review its own diff as the final reviewer, and its "LGTM" does not replace human review.

## When to run

- Before opening a large PR.
- Before merging an AI-tagged PR.
- Before a Production release.
- After the agent produced a substantial part of the diff.

## Inputs

- Diff, branch, or PR.
- Project level (Prototype / Production) and the "customers" flag (yes / no).
- Related spec: `openspec/changes/<x>/proposal.md` or the task plan.
- The accepted intent `intent/<date>-<name>.md`, if the change started from one.
- `REVIEW.md` in the repo root, if there is one: passes, what matters, the nit limit, what not to review (§7 of the bible).
- Which checks have already been run.

## Steps

1. Read §7 of the bible as the main checklist.
2. Check AI disclosure: the `Assisted-by:` trailer in commits and `[ai]` in the PR title if AI contributed a substantial part. The responsible author is a human.
3. Check PR size: target ≤200 LOC, ceiling 400 LOC. If larger — propose a split: human review time is limited.
4. Check scope: the diff changes only what was declared.
5. Check new dependencies: existence, reputation, lockfile, license/security scan. Agent configuration (skills, plugins, MCP, hooks, `AGENTS.md`) is a dependency too: owner, review, pinning.
6. Check tests: no deleted assertions, no tautological tests, tests check the requirement from the spec, written in a separate context.
7. Check security: secret leaks, input validation, authz, SQL/HTML injection, fail-open, lethal trifecta, agent autonomy beyond the level.
8. If §6 requires a proposal for this change, check conformance to it and closed `tasks.md`; otherwise check the stated task. Check that the expected outcome is named. Where `design.md`/`tasks.md` exist, the diff matches them and deviations are recorded in the same PR.
9. Check the evidence bundle: link to the spec, check run, known gaps.
10. Check the §3 mode: in a team the approver did not assign the task to the agent; solo without customers permits a human author check, not independent review. AI review does not replace it. Auto-merge is allowed only under the existing §3 conditions; otherwise this is `#sycophancy`.
11. With customers, check the second senior+ reviewer, the release process/runbook, and the DoD §5 rows in the "+ customers" column.
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
- [blocker] `#shortcode` / §5 #N / §7 item N — finding, evidence (path:lines or command and result), impact, minimal fix.
- Unverified: hypothesis and how to check it; do not present it as a confirmed blocker.

## Checks
- Tests: ...
- Security: ...
- Dependencies / agent configuration: ...
- Spec / evidence bundle / outcome: ...
```

If the PR is clean, still list what was checked. "LGTM" without checks is `#sycophancy`.
