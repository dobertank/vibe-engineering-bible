# Bible audit: <project>

Date: <YYYY-MM-DD>
Repo/path: <link-or-path>
Owner: <name/team>
Bible version: <commit SHA / snapshot; local changes, if any>
Project version and scope: <commit SHA / snapshot; included and excluded paths>
Agent / model: <observed version or unknown>
Declared level: <Prototype / Production / unknown> · customers: <yes / no / unknown>
Actual level: <Prototype / Production / unknown> · customers: <yes / no / unknown> (by the transition events, §2–§3 of the bible)
Mode: <first audit / quarterly / pre-PR / pre-release>
Next step: <merge / release / orientation>
Result: <pass / advisory / fail> — within the inspected scope; unknown does not mean pass.

## Executive Summary

<3-7 lines: what was checked, the main risk, the minimal next action.>

## Findings

| ID | Severity | Class | Observation | Evidence | Requirement | Minimal fix |
|---|---|---|---|---|---|---|
| A-001 | blocker/warn/note | DoD / §7 / `#shortcode` / spec / environment | <verified fact> | <path:lines or command and result; search scope for absence> | <§/DoD and applicability to the next step> | <what to do and how to recheck> |

Severity and consequences (§4½ of the bible):

- `blocker` — a mortal sin, a Prototype boundary breach, a leakage risk, or a mandatory DoD item for the current step: the PR/release at the declared level does not pass until fixed; blameless review.
- `warn` — a venial sin or a DoD/baseline gap: fix before the move to Production, onboarding customers, or turning on a check.
- `note` — an improvement without immediate risk. A recurring pattern is a reason to fix the environment or the process.

## DoD Snapshot

| Requirement | Status | Comment |
|---|---|---|
| README + owner + lifecycle | pass/fail/unknown/n/a | |
| CLAUDE.md/AGENTS.md baseline (≤~150 lines, §3.1 filled in) | pass/fail/unknown/n/a | |
| AI disclosure: `Assisted-by:` / `[ai]` | pass/fail/unknown/n/a | |
| Tests/lint/typecheck | pass/fail/unknown/n/a | |
| Security/SAST/secrets | pass/fail/unknown/n/a | |
| Dependencies/license/slopsquatting | pass/fail/unknown/n/a | |
| Agent configuration: owners, review, pinning | pass/fail/unknown/n/a | |
| Threat model / lethal trifecta | pass/fail/unknown/n/a | |
| Spec / proposal | pass/fail/unknown/n/a | |
| Evidence bundle; outcome named in advance | pass/fail/unknown/n/a | |
| Release/runbook/on-call | pass/fail/unknown/n/a | |

`unknown` means unverified or insufficient evidence; `n/a` means inapplicable with a reason. Missing files in the inspected scope are facts; they do not establish the state of hosted CI or branch protection. This snapshot summarizes the audit, not every applicable §5 requirement.

## Environment and gates

| Rule | Where enforced | Class | Status |
|---|---|---|---|
| <e.g.: secrets are not committed> | <hook / CI / text only> | deterministic / probabilistic / human decision | blocks / advises / none / unknown |

- Rules that live only in text but are machine-checkable: `<list>`
- Probabilistic checks that block without calibration (except fail-closed security gates on untrusted input, §5 #41): `<list or none>`

## Checks

- Commands that were run: `<commands or none>`
- What was not run and why: `<constraints>`
- Unverified hypotheses: `<list>`

## Registry

Propose a `registry.md` update (opt-in, `CONTRIBUTING.md`): <yes/no>; owner consent: <given / not requested>
Proposed row: <per the legend under the `registry.md` table>

## Next Actions

1. <1-3 day action>
2. <follow-up>
3. <deferred>
