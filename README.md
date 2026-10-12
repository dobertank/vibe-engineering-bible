# Vibe Engineering Bible

![Vibe Engineering Bible 2.0](./assets/banner-en.jpg)

A policy for working with AI assistants (Claude Code, Cursor, Codex, Claude Cowork,
and others) for teams of any size — solo developer, OSS maintainer, a team of 5
or 5000 people.

The repository is meant to be a **point of righteousness**: a git-first source of rules,
templates, and playbooks with which you can initialize a new project, audit an existing
one, run a pre-PR review, and feed useful findings back into the bible.

This is a documentation-only repo: no code, tests, or build here.

**Version 2.0 · October 2026** — the first version for adoption. Core changes after it go through a reasoned ADR (Appendix E of the bible).

## Contents

- **[`vibe-engineering-bible.md`](./vibe-engineering-bible.md)** — the canonical "bible". Two covenants — two maturity levels: the **Covenant of Freedom** — Prototype, with three unbreakable boundaries; the **Covenant of Discipline** — Production, everything someone other than the author uses, with the "+ customers" overlay and an event-triggered transition. Inside — eight commandments, thirteen sins (§4½, a normalized shortcode vocabulary for merge rejections), DoD "Prototype / Production / + customers" with gate classes, the loop "spec → agent → verification → rollout → outcome", an AI-code reviewer checklist, context files and development-agent skills, metrics and ownership, glossary. Sources for figures — Appendix D; standard evolution — Appendix E; applying the bible to projects — Appendix F.
- **[`usage.md`](./usage.md)** — how to apply the repo to live projects: roles, four modes, the process, example agent requests, playbooks as skills.
- **[`playbooks/`](./playbooks/)** — init of a new project, audit of an existing one, pre-PR/PR review, a proposal to change the bible. Each is an agent skill (`SKILL.md`) with its output format inside.
- **[`templates/CLAUDE.md.template.md`](./templates/CLAUDE.md.template.md)** — baseline template for AI agents in a product repo; applies to a team of any size.
- **[`templates/audit-report.md`](./templates/audit-report.md)** — the audit report format; **[`intent.md`](./templates/intent.md)** and **[`REVIEW.md`](./templates/REVIEW.md)** — starter files for a product repo: the intent (§6) and the AI review policy (§7).
- **[`patterns.md`](./patterns.md)** · **[`registry.md`](./registry.md)** · **[`CONTRIBUTING.md`](./CONTRIBUTING.md)** · **[`docs/adr/`](./docs/adr/)** — **standard evolution** (Appendix E): an advisory catalog of field patterns and a queue of sin candidates, the adoption registry (opt-in), the upstream contribution process, reasoned ADRs on core changes.
- **[`AGENTS.md`](./AGENTS.md)** — instructions for agents editing this repo: what to cross-check and what not to do (`CLAUDE.md` imports it).

## How to use

1. Pick a playbook: a new project — [`init-project.md`](./playbooks/init-project.md), an existing one — [`audit-project.md`](./playbooks/audit-project.md), a diff/PR — [`review-pr.md`](./playbooks/review-pr.md), a new rule from practice — [`propose-bible-change.md`](./playbooks/propose-bible-change.md); order and roles — [`usage.md`](./usage.md).
2. For Production, copy the baseline into the product repo as `CLAUDE.md` (Claude Code) and/or `AGENTS.md` (Codex, Cursor, and others that support `agents.md`).
3. Fill in §1–§3 (including §3.1 "what the environment enforces") and section 8; do not edit the rules in §4–§7. Cross-check against DoD §5 of the bible.
4. After the first real application, add the project to [`registry.md`](./registry.md); a pattern that generalizes goes to [`patterns.md`](./patterns.md) per [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Owner

The owner group of the AI-code policy in your team or organization (a small group, one owner per part; in a small team — the owner-developer) and the harness owner. The quarterly review of the bible and the template removes what is outdated, not only adds.
