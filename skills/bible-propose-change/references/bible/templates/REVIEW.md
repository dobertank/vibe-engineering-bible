# AI review policy

<!-- Goes into the repo root. This is agent configuration: edits go through a PR approved by CODEOWNERS (§5 #35 of the bible). AI review advises; a human approves through branch protection (§5 #37); the answers to the §7 checklist are signed off by a human. -->

## Passes
Label every finding with its pass and severity.
- **Bugs:** logic errors, edge cases, regressions.
- **Security:** injections, authorization gaps, secrets and personal data in logs.
- **Conformance:** the diff matches the spec and the plan (`proposal.md`, `design.md`, `tasks.md` — if they exist for this change) and the design principles; deviations are named.

## What matters
What matters is whatever breaks behavior, exposes data, or violates policy. Style and naming are nits.

## Nit limit
No more than {{5}} nits per review; the rest as a single counter line.

## What not to review
- {{generated files: path/to/generated}}
- Everything CI already checks: linter, formatting, types.

## Calibration
Once a month the review owner ({{name}}) labels the findings "useful / not useful" and edits this file. A recurring finding becomes an edit to `AGENTS.md` / `CLAUDE.md`.
