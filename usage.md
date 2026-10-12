# How to apply the Vibe Engineering Bible

The order of operations by which live projects go through init, audit, PR review, and feed findings back into the bible. The canonical framing is Appendix F of the bible. The bible sets the norm, the language of violations, and the minimum of artifacts, to reduce chaos rather than add manual braking; the final call — merge, postpone, move the project to Production, update the bible — is made by a human.

## 1. Roles

**Owner group** — a small group that accepts changes to `vibe-engineering-bible.md`, the template, and the playbooks; one owner per part. In a small team the owner-developer or tech lead wears this hat.

**Harness owner** — owns the agent's environment: managed settings, the LLM proxy, the catalog of development-agent skills. Moves what the bible makes mandatory from text into the environment.

**Project owner** — makes sure the project applies the bible correctly: level (Prototype / Production, "+ customers"), baseline file, DoD, registry entry, follow-ups.

**Reviewer** — checks a PR or an audit report against §7 of the bible and the sin shortcodes from §4½.

**AI agent** — helps read the repo, find discrepancies, and prepare the report, but does not become the source of truth and does not review its own diff as the final reviewer. The source of truth is git, the bible, and the owner's decision.

## 2. Four application modes

| Mode | When to use | Input | Output |
|---|---|---|---|
| Init a new project | There is an idea; a new repo/folder/prototype is needed | Goal, users, data, expected lifetime | `README`, `CLAUDE.md`/`AGENTS.md`, level (Prototype / Production, customers yes / no), `registry.md` row, the init summary (format — in `playbooks/init-project.md`) |
| Audit an existing project | The project exists; you need to understand maturity and risks | Repo path, project goal, declared level | Audit report per `templates/audit-report.md`: blocker/warn/note and next actions |
| Pre-PR / PR review | Before a large commit, a PR, or a release | Diff/branch/PR, project level, related spec | Findings per §7, DoD gaps, sin shortcodes, evidence bundle |
| Feedback loop into the bible | A useful pattern or a new risk repeated | Observation, evidence, where it repeated | An entry in `patterns.md` or a proposal to change the bible, the template, or a playbook (format — in `playbooks/propose-bible-change.md`) |

## 3. Basic process

1. Pick a mode from the table above.
2. Open the matching playbook in `playbooks/` (or invoke it as an agent skill — §6).
3. Ask the agent to read not only the project but also the bible: at least §2–§3 (levels and "+ customers"), §4, §4½, §5, §6 (the loop), §7, §8, and §10.
4. Get the report in the format from the playbook or `templates/audit-report.md`.
5. The project owner decides: fix now, open a follow-up, move the rule into the environment, turn on a check.
6. If the application became real, add or update the row in `registry.md`.
7. If the same pattern repeated 3+ times, run `playbooks/propose-bible-change.md`.

## 4. Example agent request

```text
Read vibe-engineering-bible.md, usage.md and playbooks/audit-project.md.
Audit the project at /path/to/repo as Production without customers.
Produce the report using templates/audit-report.md.
Do not change project files without a separate confirmation.
```

For a PR:

```text
Read vibe-engineering-bible.md and playbooks/review-pr.md.
Review the current diff as a pre-PR review for Production without customers.
Show blocker/warn/note first, then propose minimal fixes.
```

## 5. Checks, consequences, principles — by reference

Check classes (D / P / H) and the "advisory → calibration → block" path — §5 of the bible; consequences — §4½; the loop and the outcome — §6; application principles — Appendix F; file map — [`README.md`](./README.md).

## 6. Playbooks as development-agent skills

Every playbook in `playbooks/` is a ready development-agent skill: it has a `name` / `description` YAML header in the `SKILL.md` format, and its output format is described inside. To ship a playbook as a skill (§8 of the bible):

1. Copy the file into your team's skills catalog as `<name>/SKILL.md` (for example, `.claude/skills/bible-audit-project/SKILL.md` for Claude Code, or your agent's equivalent).
2. For an audit, put `templates/audit-report.md` next to it; point the skill at a pinned version of the bible (a commit or tag), not at "latest".
3. The skills catalog lives in git with owners (CODEOWNERS); changes go through a reviewed PR. A skill from an external marketplace is the same kind of dependency as a package (Commandment V): review, pinning, only through an internal catalog.

A skill does not change the norm: it only packages the order of operations. The decision stays with a human.
