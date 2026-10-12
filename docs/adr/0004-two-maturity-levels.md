# ADR 0004. Two maturity levels — Prototype and Production — instead of T0–T3

- **Status:** accepted 2026-10-12 (release 2.0).
- **Date:** 2026-10-12.
- **Process context.** The change touches §2–§5 and §4½, including the core, so it goes through a reasoned ADR per the Appendix E gate. The bible is still being written and the adoption registry is empty, so the change goes into release 2.0 (like ADR 0001–0003).
- **Trigger.** An independent usability review of the bible on 2026-10-12: the reader had to hold two coordinate systems at once — two covenants with four labels T0–T3 inside them. The bible itself already said there were only two modes, with the labels as an overlay inside the second; the four labels added a distinction the reader did not need.

## Decision

- **Two maturity levels = two covenants.** **Prototype** — the Covenant of Freedom: the author's personal experiment, up to 30 days, three boundaries (§2). **Production** — the Covenant of Discipline: everything used by anyone other than the author, from a utility for the neighboring team to a customer-facing service (§3).
- **"+ customers" is an overlay, not a third level.** When the result touches customers, customer data, or a public release, a "+ customers" column is added to the Production DoD: a full threat model, mutation testing, a second senior+ reviewer, gradual rollout with rollback, a runbook, a kill-switch.
- **DoD (§5):** columns "Prototype | Production | + customers" instead of the four label columns. Transfer rule: Prototype = former T0, Production = former T1–T2 (everything required at T1 or T2), "+ customers" = former T3. Rows #3 (only synthetic data) and #4 (`PROTOTYPE` marking + sunset date) are removed: synthetic data is already a prototype boundary (#1), and the marking applied to a prototype that others see, which is now Production. The remaining rows keep their numbers. Row #5 gets a dash for Prototype: §2 never required `[ai]` marking from an experiment.
- **Autonomy (§3):** Prototype — the agent acts on its own in an isolated environment; Production — on its own, into shared code only after human review; "+ customers" and sensitive data — only proposals or actions with human confirmation. Auto-merge — only in Production without the customer overlay and only for low-risk changes (ADR 0003).
- **`#zombie-t0` → `#zombie`.** The label leaves the vocabulary; the meaning stays: a prototype older than 30 days without a move to Production or deletion, or Production code without an owner and commits past its retirement date. Roots — §2, §4 II, DoD #6. The count "thirteen" does not change.
- **Transition by event** — as before: shown outside your team; someone other than the author uses it; real data, secrets, or shared state are needed; asked for it on the roadmap. Showing it inside your own team is not a transition.
- **Backward compatibility.** In the glossary: version 1.x labels — T0 = prototype, T1–T2 = production, T3 = production + customers.

## Consequences

- **The price of simplification (accepted by the owner).** The former T1 — a prototype others see — had a lighter DoD. Now any use beyond the author is Production: tests, SAST, review by a second person, `AGENTS.md`, a catalog entry. This also removes the ambiguity over whether a prototype others see needs tests.
- Instead of three DoD variants, the template gets one (Production) and an "if you have customers" block; the satellite files (`README.md`, `CLAUDE.md`, `usage.md`, `playbooks/`, `templates/`) move to the two levels.

## Deliberately not changed

- The counts: two covenants, eight commandments, thirteen sins.
- Gate classes D / P / H, rows #35–#41, DoD numbering: the remaining rows keep their numbers and anchors.
