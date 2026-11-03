# Vibe Engineering Bible

![Vibe Engineering Bible 2.0](./assets/banner-en.jpg)

Rules and working playbooks for developers and maintainers using AI assistants. Start with a repository audit: findings tied to evidence, Bible requirements, and minimal fixes. A human decides what to change.

The main product is Markdown: the canon, templates, and four playbooks. Start with an audit, compare the evidence, and choose one fix. The repository includes four ready skills; [installation](#install-ready-skills) does not require Python. Python is only a [maintenance tool](./usage.md#maintaining-the-generated-skills).

## First audit

Use `bible-audit-project` in a file-reading agent with a model already authorized for these files; a hosted model receives the context it reads. The skill includes its Bible resources, so no separate Bible checkout is needed. State the purpose and known users; leave unknown facts as `unknown`. Without installing a skill, the same procedure is available in the [source playbook](./playbooks/audit-project.md).

```text
Use $bible-audit-project.
Target project: /absolute/path/to/project
Purpose and users: <what it does, who uses it>
Declared level: <Prototype / Production / unknown>; customers: <yes / no / unknown>.
Mode: first audit; next step: <merge / release / orientation>.
Use the skill's bundled Bible and audit-report template.
Return blocker/warn/note findings with evidence (target path:lines or
command and result), requirement, minimal fix and recheck.
Mark inaccessible settings and unrun checks unknown, not failed.
Read only: do not edit files, install dependencies or run project code.
Do not make external tool calls or uploads beyond the authorized model context.
```

Try it on [the synthetic fixture](./examples/audit/fixture/) using the scope in [the complete example](./examples/audit/README.md). Its report illustrates a `warn` for an outdated level, a `blocker` for the missing Production baseline before merge, and a `note` about the limits of local CI evidence. Reproduction commands include one fix, a recheck, and a negative control.

Check the evidence, choose one fix, and repeat the relevant check. An audit report does not certify project safety; unverified checks remain visible. The example is synthetic and is not a benchmark or a registered adoption.

<a id="install-ready-skills-local-candidate"></a>

## Install ready skills

Ready skills are published on `main`. From your target project, with Node.js 22.20+:

```sh
DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 npx --yes skills@1.7.4 add https://github.com/dobertank/vibe-engineering-bible/tree/main --copy --agent codex --skill bible-audit-project --yes
```

This copies the audit skill into the current project's local skills directory. Start a fresh agent session, then use the first-audit prompt above. Choose `bible-init-project`, `bible-review-pr` or `bible-propose-change` for the other scenarios; [usage §6](./usage.md#6-playbooks-as-development-agent-skills) lists all four.

`main` can change. For an immutable published commit and a release-tag command, see [version-pinned installation](./usage.md#version-pinned-installation). The older `v2.1.1-en` tag predates the ready folders. The npm runner may fetch the pinned CLI on first use; using the installed skill needs neither Python nor the original checkout. Review source and permissions before use.

**Version 2.0 · October 2026** — the first version for adoption. Core changes after it go through a reasoned ADR (Appendix E of the bible).

## Contents

- **[`vibe-engineering-bible.md`](./vibe-engineering-bible.md)** — the canonical "bible". Two covenants — two maturity levels: the **Covenant of Freedom** — Prototype, with three unbreakable boundaries; the **Covenant of Discipline** — Production, everything someone other than the author uses, with the "+ customers" overlay and an event-triggered transition. Inside — eight commandments, thirteen sins (§4½, a normalized shortcode vocabulary for merge rejections), DoD "Prototype / Production / + customers" with gate classes, the loop "spec → agent → verification → rollout → outcome", an AI-code reviewer checklist, context files and development-agent skills, metrics and ownership, glossary. Sources for figures — Appendix D; standard evolution — Appendix E; applying the bible to projects — Appendix F.
- **[`usage.md`](./usage.md)** — how to apply the repo to live projects: roles, four modes, the process, example agent requests, playbooks as skills.
- **[`playbooks/`](./playbooks/)** — init of a new project, audit of an existing one, pre-PR/PR review, a proposal to change the bible. Each has YAML metadata and an output format; the builder creates a `SKILL.md` router with matching resources.
- **[`templates/CLAUDE.md.template.md`](./templates/CLAUDE.md.template.md)** — baseline template for AI agents in a product repo; applies to a team of any size.
- **[`templates/audit-report.md`](./templates/audit-report.md)** — the audit report format; **[`intent.md`](./templates/intent.md)** and **[`REVIEW.md`](./templates/REVIEW.md)** — starter files for a product repo: the intent (§6) and the AI review policy (§7).
- **[`patterns.md`](./patterns.md)** · **[`registry.md`](./registry.md)** · **[`CONTRIBUTING.md`](./CONTRIBUTING.md)** · **[core change log](./vibe-engineering-bible.md#appendix-e-standard-evolution)** — **standard evolution** (Appendix E): an advisory catalog of field patterns and a queue of sin candidates, the adoption registry (opt-in), the upstream contribution process, a short record of core changes.
- **[`AGENTS.md`](./AGENTS.md)** — instructions for agents editing this repo: what to cross-check and what not to do (`CLAUDE.md` imports it).

## How to use

1. Pick a playbook: a new project — [`init-project.md`](./playbooks/init-project.md), an existing one — [`audit-project.md`](./playbooks/audit-project.md), a diff/PR — [`review-pr.md`](./playbooks/review-pr.md), a new rule from practice — [`propose-bible-change.md`](./playbooks/propose-bible-change.md); order and roles — [`usage.md`](./usage.md).
2. For Production, copy the baseline into the product repo as `CLAUDE.md` (Claude Code) and/or `AGENTS.md` (Codex, Cursor, and others that support `agents.md`).
3. Fill in §1–§3 (including §3.1 "what the environment enforces") and section 8; do not edit the rules in §4–§7. Cross-check against DoD §5 of the bible.
4. Optionally, after a real application and owner consent, propose a draft entry in [`registry.md`](./registry.md); a pattern that generalizes goes to [`patterns.md`](./patterns.md) per [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Owner

The owner group of the AI-code policy in your team or organization (a small group, one owner per part; in a small team — the owner-developer) and the harness owner. The quarterly review of the bible and the template removes what is outdated, not only adds.

## License

Project-authored materials are licensed under [MIT](./LICENSE). Third-party materials retain their own terms and notices; preserve those notices when copying them.
