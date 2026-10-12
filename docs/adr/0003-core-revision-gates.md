# ADR 0003. Core 2.0, addendum: review gates, protecting the gates, fail-closed on input, risk-based auto-merge

- **Status:** accepted 2026-10-12 (release 2.0).
- **Date:** 2026-10-12.
- **Process context.** The core (§4, §4½, §5) moves only through the Appendix E gate — by a reasoned ADR. The bible is still being written and there are no live applications in `registry.md`, so the changes go into the same release 2.0 as ADR 0001: the version number does not change. The quarterly cadence of core edits switches on with the first entry in the registry (Appendix E).
- **Trigger:** new sources checked on 2026-10-12: the Anthropic playbook (ADR 0002), MuleSoft Golden Gate, GitHub Next Canary, Meta RADAR, Zalando. All of them are in Appendix D.
- **Basis:** owner decision, 2026-10-12: the bible is still being written; the changes are part of release 2.0.

## Decisions

### 1. AI review also checks conformance to the spec and the plan (#37, Commandment VII, §7)
- **Context.** Row #37 limited AI review to bugs and security to avoid style noise. In the Anthropic playbook the third pass is conformance of the diff to the spec and the plan. This is not noise but exactly the check for which the artifact chain (ADR 0002) commits the plan before the code.
- **Decision.** #37: AI review before the human works per `REVIEW.md` and makes three passes — bugs, security, conformance to the spec and the plan; no style; the usefulness of findings is assessed. `REVIEW.md` limits the noise (the nit limit, "what not to review"). The answers to the §7 checklist, including items 1 and 8, are still signed off by a human.
- **Consequences.** §4 VII, §7 (the `REVIEW.md` paragraph), §6 of the template (Production DoD). The "boundary with the core" from ADR 0002 is closed.

### 2. The environment protects itself: a gate on weakened checks (#40, Commandment IV, §7 item 9)
- **Context.** Commandment IV moves what is mandatory into the environment, but the environment can be weakened by the same PR: disable a linter rule, add `continue-on-error`, skip a test, add a SAST exception. An agent can also change its own configuration. MuleSoft catches such PRs with a separate check: 369 findings on 2,200+ PRs, 3 of them incorrect.
- **Decision.** A new row #40 (Production, class D): weakened checks are caught by a separate check — CODEOWNERS on config paths and a pattern detector. Such a change can be merged only with the approval of the checks' owner. Branch protection and required reviewers are set in the repository settings, out of the agent's reach. The mechanism is deterministic; the MuleSoft AI skill is an argument, not the way to implement it.
- **Consequences.** The "The environment protects itself" paragraph in Commandment IV, checklist item 9, §3.1, §3.2, and §6 of the template, `usage.md`, the init and audit playbooks.

### 3. A fail-closed security gate on untrusted input (#41, class P, Commandment VI)
- **Context.** Probabilistic gates follow the path "advisory → calibration → block". For a gate that protects an agent with write permissions from prompt injection, advisory mode means letting the attack through. GitHub Next Canary: several narrow detectors without tools decide by quorum, and uncertainty does not turn into permission. At the same time, Commandment VI says prompt filters are not enough.
- **Decision.** Class P gets an exception: security gates on untrusted input work fail-closed from day one. An uncertain, contradictory, or missing answer means block; a human triages false positives, and calibration proceeds on them. A new row #41 (Production, like #13; "P (fail-closed)", NOW — a harness hook). The gate sits **on top of** breaking the trifecta (#13), not instead of it. This is stated in §5, in Commandment VI, and in the glossary, so that the detector does not read as "a filter instead of architecture".
- **Consequences.** §9, the glossary (deterministic / probabilistic check, lethal trifecta), §3.1 of the template (the Hooks line — the gate lives in the harness, not in CI) and §6 (Production DoD), `usage.md`, `templates/audit-report.md`.

### 4. Auto-merge — only for low-risk changes per risk assessment (§3, Commandment VII, #5)
- **Context.** The 2.0 draft allowed auto-merge for what is now Production (ADR 0004) after the checks were calibrated but did not say which changes it applies to. Meta RADAR merged 331k low-risk diffs without a human; they have 1/3 the rollback rate and 1/50 the production incident rate of the rest. Zalando automatically approves the 33% of PRs that are low-risk. Both figures are self-reports and apply to low-risk changes backed by heavy risk-assessment infrastructure.
- **Decision.** This is a tightening, not a loosening. Auto-merge in Production is acceptable only for low-risk changes. The risk is assessed by a deterministic model (paths, size, rollback history). Sensitive paths are on a deny-list. There is a daily cap. Humans spot-check what was merged automatically, with an emphasis on the risky. If the rollback rate grows, auto-merge switches itself off. With customers ("+ customers", ADR 0004) — never.
- **Consequences.** #5, Commandment VII, the "Auto-merge" placeholder in §3.1 of the template, the repo's `CLAUDE.md`, `usage.md`. The oversight of AI gates beyond the core (spot audits, shadow mode for new reviewers, an agent action log) is a separate edit outside the core, in §9.

### 5. Every agent has its own identity (Commandment VI)
- **Context.** Anthropic describes an incident-response agent that, on its own initiative, asked a coding agent to push a fix; a human review gate stopped it. The lesson: "draw the boundary around access and actions, not around a model's instructions". GitHub Agentic Workflows: the agent is read-only; writes go through pre-declared safe outputs in a separate step.
- **Decision.** A bullet in Commandment VI: every agent has its own identity and task-scoped permissions; the boundary is drawn around access and actions, including one agent's requests to another; writing outward happens in a separate step with its own permissions, not by an agent holding a human's token.

### 6. Cadence of core revisions (Appendix E, `CONTRIBUTING.md`)
- **Decision.** The quarterly cadence switches on with the first record of a live application in `registry.md`. Until then the core is edited by reasoned ADR without waiting for the quarter.

## Deliberately not changed
- The counts: two covenants, eight commandments, thirteen sins. No new sins.
- DoD numbering and anchors: the new rows are #40 and #41; the old ones are not renumbered.
- The version number: 2.0.
