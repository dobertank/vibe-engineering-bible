# ADR 0002. Artifact chain, closing the loop, metrics from git, `REVIEW.md`

- **Status:** accepted 2026-10-12 (release 2.0).
- **Date:** 2026-10-12.
- **Process context.** The core (§4, §4½, §5) does not change, so the Appendix E gate is not required. The changes touch §6, §7, §9, and §10, the satellite files, and Appendix D. The ADR records the rationale because the edit cuts across files: the §6 loop is kept in sync with §5 of the template, §7 item 8, and the review playbook.
- **Basis:** owner decision, 2026-10-12: the bible is still being written; the changes are part of release 2.0.
- **Trigger:** a new source. Anthropic, *The AI-native SDLC playbook* (August 21, 2026, Appendix D, [vendor]). The source independently arrived at the same core as bible 2.0 ("a skill is advice, a hook is a guarantee", agent configuration under CI, the author does not approve their own agent's PR, evals from 20–50 real tasks). At the same time it has five mechanisms the bible did not have.

## Decisions

### 1. The artifact chain is the audit trail (§6)
- **Context.** The §6 loop described the steps but not the link between them. An idea from a non-engineer had no entry point: a proposal is written by an engineer.
- **Decision.** Every step of the loop commits an artifact; the next step reads it. There is only one new link — the intent `intent/<date>-<name>.md`. Anyone writes it together with the agent, and the product owner accepts or closes it. The other links are existing `openspec/` artifacts: the Anthropic playbook's `spec.md` corresponds to proposal + delta spec, its `plan.md` — to design + tasks. No parallel set of files is introduced. The plan changes in the same commit as the implementation. Over time an accepted artifact triggers the next step on its own.
- **Consequences.** The §6 lifecycle gets an optional Intent accepted step. §5 of the template and `playbooks/review-pr.md` (inputs, step 8) are updated. The check against the plan in §7 item 8 already existed — what is new is that the chain counts as the audit trail, and the entry point through an intent.

### 2. One source of truth per artifact (§6)
- **Context.** Organizations have trackers, requirements systems, and approvals that auditors recognize. A markdown chain without a rule creates a second source of truth.
- **Decision.** Each link is assigned exactly one source of truth: the repo, an external system (the agent reads and writes via MCP in the same session), or at minimum mutual links. Two sources without links are not acceptable.

### 3. The loop closes itself (§6)
- **Context.** The "outcome" step closed the loop only for a product metric, and only by hand.
- **Decision.** The detector is deterministic, lives in the repo, and is covered by tests. The response thresholds are set in a config: log → read-only diagnosis → a PR into the review gate or a pre-approved runbook. The agent has no direct production permissions (Commandment VI, §3). The agent's diagnosis is written as an `intent.md`; a fixed incident becomes an eval case (§5 #38). The mechanism is switched on last — after the review gate, the deterministic gates, and a rehearsed rollback (§5 #29).
- **Consequences.** It does not go into the template: this is infrastructure, not an instruction to the agent.

### 4. Metrics from the traces you already have (§9)
- **Context.** The §9 metric pairs did not say where the data comes from. Manual reporting dies first.
- **Decision.** For each practice — a leading indicator from git timestamps and PR metadata and a lagging one (rework, rollbacks, incidents). The table is in §9.

### 5. The AI review policy — `REVIEW.md` (§7)
- **Context.** Row #37 required AI review with a usefulness assessment but did not say where the policy lives or how calibration works.
- **Decision.** `REVIEW.md` in the repo root sets the passes, what counts as important, the nit limit, and what not to review. Monthly labeling of findings "useful / not useful" is the class-P calibration. The file is agent configuration under CODEOWNERS (#35). A recurring finding turns into an edit to the context file (§8).
- **Boundary with the core.** The Anthropic playbook has a third pass — conformance of the diff to the spec and the plan. Row #37 limited AI review to bugs and security. Extending #37 with this pass was accepted in the same release 2.0 (ADR 0003); `REVIEW.md` now describes three passes.

### 6. Usability: oversight, acceptance, economics, starter templates (§6, §9, `templates/`)
- **Context.** The same research pass of 2026-10-12 (Appendix D): Anthropic (shadow mode for new AI reviewers, sampling of automated approvals, a log of agent actions), BCG Platinion (acceptance scenarios out of the agents' reach), DORA ROI 2026 (the J-curve), Cloudflare (cost of review). Selection rule: one sentence in the canon, the mechanism in the process layer.
- **Decision.** §6 "Check": human-approved acceptance scenarios live where the agent cannot write. §9: paragraphs on oversight after calibration and on the cost of the transition. Starter templates `templates/intent.md` and `templates/REVIEW.md`, so the new loop artifacts can be picked up rather than invented. The SDD status date in the Thoughtworks Radar — November 2025.

## Deliberately not changed
- The core within this ADR: §4, §4½, §5. Core changes accepted the same day are recorded separately in ADR 0003. The counts "two covenants / eight commandments / thirteen sins" did not change.
- Version: the changes are part of release 2.0.
- Ties to the vendor's products: the bible takes only the patterns, without product names.
