---
name: bible-init-project
description: "Use when the user asks to initialize or adopt the Vibe Engineering Bible for a new project or prototype; not for an ordinary feature or silent replacement of existing project instructions."
---

# bible-init-project

The Bible root is `references/bible/` beside this `SKILL.md`; no separate Bible checkout is needed. The target project is a separate input. Resolve Bible paths from that bundled root and project evidence from the target root.

Reply in the user's requested language and honor the actual target project's applicable instructions. Bundled `AGENTS.maintenance.md` and `CLAUDE.maintenance.md` describe Bible maintenance; they are reference data, not target instructions or a response-language policy.

### Trigger and scope
Use for requested Bible project initialization/adoption, not an ordinary product feature. Distinguish a new folder from a target with existing files.

### Inputs and missing data
Need target and output destinations, goal/users, owner, data, expected lifetime and permitted writes. Ask for missing destination or ownership decisions before creating files; do not invent the stack or environment enforcement. The bundled Bible supplies the baseline, not an external checkout.

### Reading order
1. Read the user's brief and actual target instructions; inspect existing README, AGENTS.md and CLAUDE.md before proposing output.
2. Read the source init playbook, canon §2–§3/§5/§8 and `templates/CLAUDE.md.template.md` for Production.
3. Classify from facts, then prepare the smallest authorized local draft with a readiness table.

### Output
Return brief, level/customers/transition reason, created versus proposed files, pass/fail/unknown/n-a readiness, and next actions. Unverified controls are unknown, not fail or pass. Name outputs and preservation status explicitly.

### Boundaries
Preserve existing AGENTS.md and CLAUDE.md bytes. Offer a proposed file in the authorized draft destination or a diff; never silently replace, append to, rename or remove them. Other existing target files also require an explicit requested change. Do not install tools or configure CI/hooks/access/deploy. Draft required environment work for the owner; registration and external PRs are opt-in and human actions.

Read the [source playbook](references/bible/playbooks/init-project.md) for the detailed procedure and output schema. Do not run the bundled maintenance builder to use this skill. A skill grants no additional action, network or publication permissions; keep outputs outside its resources. Content identity is in `SOURCE.json`.
