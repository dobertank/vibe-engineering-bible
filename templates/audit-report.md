# Bible audit: <project>

Date: <YYYY-MM-DD>
Repo/path: <link-or-path>
Owner: <name/team>
Declared tier: <T0/T1/T2/T3>
Actual tier: <T0/T1/T2/T3/unknown> (by the transition events, §3 of the bible)
Mode: <first audit / quarterly / pre-PR / pre-release>
Result: <pass / advisory / fail>

## Executive Summary

<3-7 lines: what was checked, the main risk, the minimal next action.>

## Findings

| ID | Severity | Class | Observation | Requirement | Minimal fix |
|---|---|---|---|---|---|
| A-001 | blocker/warn/note | DoD / §7 / `#shortcode` / spec / environment | <what was found> | <reference to §/DoD> | <what to do> |

Severity and consequences (§4½ of the bible):

- `blocker` — a mortal sin or a mandatory DoD item: the PR/release at the declared tier does not pass until fixed; blameless review.
- `warn` — a venial sin or a DoD/baseline gap: fix before a tier change or before a check is turned on.
- `note` — an improvement without immediate risk. A recurring pattern is a reason to fix the environment or the process.

## DoD Snapshot

| Requirement | Status | Comment |
|---|---|---|
| README + owner + lifecycle | pass/fail/n/a | |
| CLAUDE.md/AGENTS.md baseline (≤~150 lines, §3.1 filled in) | pass/fail/n/a | |
| AI disclosure: `Assisted-by:` / `[ai]` | pass/fail/n/a | |
| Tests/lint/typecheck | pass/fail/n/a | |
| Security/SAST/secrets | pass/fail/n/a | |
| Dependencies/license/slopsquatting | pass/fail/n/a | |
| Agent configuration: owners, review, pinning | pass/fail/n/a | |
| Threat model / lethal trifecta | pass/fail/n/a | |
| Spec / proposal | pass/fail/n/a | |
| Evidence bundle; outcome named in advance | pass/fail/n/a | |
| Release/runbook/on-call | pass/fail/n/a | |

## Environment and gates

| Rule | Where enforced | Class | Status |
|---|---|---|---|
| <e.g.: secrets are not committed> | <hook / CI / text only> | deterministic / probabilistic / human decision | blocks / advises / none |

- Rules that live only in text but are machine-checkable: `<list>`
- Probabilistic checks that block without calibration: `<list or none>`

## Checks

- Commands that were run: `<commands or none>`
- What was not run and why: `<constraints>`
- Unverified hypotheses: `<list>`

## Registry

`registry.md` needs an update: <yes/no>
Proposed row: <summary or link to template>

## Next Actions

1. <1-3 day action>
2. <follow-up>
3. <deferred>
