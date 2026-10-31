# Bible audit: Team glossary (synthetic)

Date: 2026-10-31
Repo/path: `examples/audit/fixture/`
Owner: demo-maintainer (fictional)
Bible version: the English local candidate shipped with this example; use the checkout commit and local diff, or the package's `SOURCE.json`, to identify the exact snapshot.
Project version and scope: only the two files in this fixture, as shipped with the same checkout or package.
Agent / model: not applicable — author-prepared expected report, not an agent execution record.
Declared level: Prototype · customers: no
Actual level: Production · customers: no (under the fixture assumptions)
Mode: first audit
Next step: merge the next glossary edit into the team's shared repository
Result: advisory — first audit; A-002 blocks treating the next merge as DoD-compliant. This is not a general project pass.

## Executive Summary

A colleague uses the glossary, so Prototype exemptions no longer apply. The README level is stale and the baseline is missing. Correct the level, then prepare a baseline for the owner's review. Hosted CI, branch protection and agent controls remain unknown.

## Findings

Evidence paths below are relative to the target project, `fixture/`. [verification.md](./verification.md) contains reproduction commands from the Bible root and is not a target-project file.

| ID | Severity | Class | Observation | Evidence | Requirement | Minimal fix |
|---|---|---|---|---|---|---|
| A-001 | warn | environment | Declared Prototype, but a colleague uses the result | `README.md:5,7` | §2–§3: use by someone other than the author triggers Production | Record Production; recheck per `verification.md`; other DoD still applies |
| A-002 | blocker | DoD | Neither CLAUDE.md nor AGENTS.md exists at the fixture root | Complete two-file listing and both absence checks in `verification.md` | §5 #2: Production baseline required before the next merge | Prepare a filled baseline and verify its content and controls with the owner |
| A-003 | note | evidence | Remote checks cannot be inferred from this local snapshot | `README.md:11`; the complete file listing | Audit playbook: unknown is not confirmed absence | Ask the owner for hosted-check and branch-protection evidence; retain unknown meanwhile |

## DoD Snapshot

| Requirement | Status | Comment |
|---|---|---|
| README + owner + lifecycle | fail | Present, but declared level is stale (A-001) |
| CLAUDE.md/AGENTS.md baseline | fail | Both absent (A-002) |
| Disclosure, tests/lint, security, dependencies, agent controls, review, threat model | unknown | No evidence supplied; no application code executed |
| Spec / proposal / evidence bundle / outcome | unknown | Next change not supplied |
| Release/runbook/on-call | n/a | Current step is an internal documentation merge, without customers |

This is a partial snapshot; no claim that every §5 row has been checked.

## Environment and gates

Hosted CI, branch protection, access/data-flow controls and #41 wiring/settings/fail-closed behavior: unknown. No confirmed enforcement claim or inference of absent remote controls.

## Checks

Run the file listing, numbered README, glossary read, and baseline absence checks in `verification.md`. The same page demonstrates the A-001 fix in a temporary copy and the limits of a file-presence check. No application, CI, security scan, or agent client is part of this expected report.

## Registry

No update: this fixture is not a real adoption.

## Next Actions

1. Fix A-001 and repeat its check.
2. Prepare and review the baseline for A-002 before the next merge.
3. Request remote-control evidence, update unknowns, then assess merge readiness separately.
