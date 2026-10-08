# How to apply the Vibe Engineering Bible

This repository can serve as a **point of righteousness**: a git-first source of rules against which live projects go through initialization, audit, PR review, and feedback into the bible itself. The canonical framing is Appendix F of the bible ("Applying the bible to projects"); this file holds the order of operations.

The bible does not replace an engineering decision. It sets the norm, the language of violations, and the minimal set of artifacts. A human still makes the final call: merge, postpone, rewrite, change the risk tier, or update the bible itself.

## 1. Roles

**Owner group** — a small group that accepts changes to `vibe-engineering-bible.md`, the template, and the playbooks; one owner per part. In a small team the owner-developer or tech lead wears this hat.

**Harness owner** — owns the agent's environment: managed settings, the LLM proxy, the catalog of development-agent skills. Moves what the bible makes mandatory from text into the environment.

**Project owner** — makes sure the project applies the bible correctly: mode and risk tier, baseline file, DoD, registry entry, follow-ups.

**Reviewer** — checks a PR or an audit report against §7 of the bible and the sin shortcodes from §4½.

**AI agent** — helps read the repo, find discrepancies, and prepare the report, but does not become the source of truth and does not review its own diff as the final reviewer. The source of truth is git, the bible, and the owner's decision.

## 2. Four application modes

| Mode | When to use | Input | Output |
|---|---|---|---|
| Init a new project | There is an idea; a new repo/folder/prototype is needed | Goal, users, data, expected lifetime | `README`, `CLAUDE.md`/`AGENTS.md`, mode and tier T0–T3, `registry.md` entry, init result |
| Audit an existing project | The project exists; you need to understand maturity and risks | Repo path, project goal, declared tier | Audit report with blocker/warn/note and next actions |
| Pre-PR / PR review | Before a large commit, a PR, or a release | Diff/branch/PR, project tier, related spec | Findings per §7, DoD gaps, sin shortcodes, evidence bundle |
| Feedback loop into the bible | A useful pattern or a new risk repeated | Observation, evidence, where it repeated | An entry in `patterns.md` or a proposal to change the bible, the template, or a playbook |

## 3. Basic process

1. Pick a mode from the table above.
2. Open the matching playbook in `playbooks/` (or invoke it as an agent skill — §6).
3. Ask the agent to read not only the project but also the bible: at least §3 (risk tiers), §4, §4½, §5, §6 (the loop), §7, §8, and §10.
4. Get the report in the format from `templates/`.
5. The project owner decides: fix now, open a follow-up, move the rule into the environment, turn on a check.
6. If the application became real, add or update the row in `registry.md`.
7. If the same pattern repeated 3+ times, run `playbooks/propose-bible-change.md`.

## 4. Example agent request

```text
Read vibe-engineering-bible.md, usage.md and playbooks/audit-project.md.
Audit the project at /path/to/repo as T2.
Produce the report using templates/audit-report.md.
Do not change project files without a separate confirmation.
```

For a PR:

```text
Read vibe-engineering-bible.md and playbooks/review-pr.md.
Review the current diff as a pre-PR review for T2.
Show blocker/warn/note first, then propose minimal fixes.
```

## 5. Checks: two classes

The first application of the bible to a project is an audit: a report, an explanation, next actions. After that, checks are turned on by class (the "Gate" column in DoD §5 and §9 of the bible):

- **Deterministic** — build and tests, secrets, packages only from an internal mirror / slopsquatting check, SAST high/critical, license scan, human review (whoever assigned the task to the agent does not approve that agent's PR), ban on auto-merge. They block from the first day they are turned on — together with a path to fix.
- **Probabilistic** — AI review, LLM judge, mutation score, soft PR-size limit. The path is advisory → calibration → block: block only after calibration on your own data.
- **Human decisions** — sign-offs, proposal approval, threat model: DoD rows, not an automatic gate.

**Consequences** (§4½ of the bible). A mortal sin blocks: the PR is not merged until it is fixed; blameless review. A venial sin — back for rework. A recurring pattern is a reason to fix the process or the environment, not the person.

**The loop and the outcome** (§6 of the bible). Audit and review check not only the code but the loop: is there a spec sized to the task, an evidence bundle (spec + check run + known gaps), is the expected outcome named, and how will it be confirmed after rollout.

The rule is simple: the bible must reduce chaos, not become a new source of manual braking.

## 6. Playbooks as development-agent skills

Every playbook in `playbooks/` is a ready development-agent skill: it has a `name` / `description` YAML header in the `SKILL.md` format. To ship a playbook as a skill (§8 of the bible):

1. Copy the file into your team's skills catalog as `<name>/SKILL.md` (for example, `.claude/skills/bible-audit-project/SKILL.md` for Claude Code, or your agent's equivalent).
2. Put the forms it needs from `templates/` next to it, and point the skill at a pinned version of the bible (a commit or tag), not at "latest".
3. The skills catalog lives in git with owners (CODEOWNERS); changes go through a reviewed PR. A skill from an external marketplace is the same kind of dependency as a package (Commandment V): review, pinning, only through an internal catalog.

A skill does not change the norm: it only packages the order of operations. The decision stays with a human.

## 7. Where the artifacts live

- `vibe-engineering-bible.md` — the canon: norms, DoD, sins, the loop, glossary; Appendix F — the application framing.
- `templates/CLAUDE.md.template.md` — baseline instructions for product repos.
- `playbooks/` — operational application scenarios (also development-agent skills).
- `templates/audit-report.md` — audit report format.
- `templates/init-result.md` — init result format.
- `templates/bible-change-proposal.md` — format of a proposal to change the bible.
- `templates/project-registry-entry.md` — row format for `registry.md`.
- `registry.md` — adoption registry: projects where the bible is actually applied.
- `patterns.md`, `CONTRIBUTING.md`, `docs/adr/` — standard evolution (Appendix E): pattern catalog, process, reasoned ADRs for core changes.

## 8. What not to do

- Do not put a probabilistic check into blocking mode before calibration, and do not postpone deterministic gates "until the first audit".
- Do not keep what is mandatory only in the text of `CLAUDE.md`/`AGENTS.md`: whatever a machine can check belongs in managed settings, hooks, CI.
- Do not rewrite the template for a single project: placeholders §1–§3 are filled in, repo specifics live in section 8 of the copied `CLAUDE.md`/`AGENTS.md`, rules §4–§7 do not change.
- Do not drag one-off findings straight into the bible core. First a playbook, the template, or `patterns.md`; into the core — only through the Appendix E gate.
- Do not register everything in `registry.md`. The registry is a list of live applications, not an inventory of every repository in the organization.
