# How to apply the Vibe Engineering Bible

The order of operations by which live projects go through init, audit, PR review, and feed findings back into the bible. The canonical framing is Appendix F of the bible. The bible sets the norm, the language of violations, and the minimum of artifacts, to reduce chaos rather than add manual braking; the final call — merge, postpone, move the project to Production, update the bible — is made by a human.

## 1. Roles

**Owner group** — a small group that accepts changes to `vibe-engineering-bible.md`, the template, and the playbooks; one owner per part. In a small team the owner-developer or tech lead wears this hat.

**Harness owner** — owns the agent's environment: managed settings, access and data-flow controls (a proxy if used), the catalog of development-agent skills. Moves what the bible makes mandatory from text into the environment.

**Project owner** — makes sure the project applies the bible correctly: level (Prototype / Production, "+ customers"), baseline file, DoD, optional registry entry, follow-ups.

**Reviewer** — checks a PR or an audit report against §7 of the bible and the sin shortcodes from §4½.

**AI agent** — helps read the repo, find discrepancies, and prepare the report, but does not become the source of truth and does not review its own diff as the final reviewer. The source of truth is git, the bible, and the owner's decision.

## 2. Four application modes

| Mode | When to use | Input | Output |
|---|---|---|---|
| Init a new project | There is an idea; a new repo/folder/prototype is needed | Goal, users, data, expected lifetime | `README`, `CLAUDE.md`/`AGENTS.md`, level (Prototype / Production, customers yes / no), optional `registry.md` draft row, the init summary (format — in `playbooks/init-project.md`) |
| Audit an existing project | The project exists; you need to understand maturity and risks | Repo path, project goal, declared level | Audit report per `templates/audit-report.md`: blocker/warn/note and next actions |
| Pre-PR / PR review | Before a large commit, a PR, or a release | Diff/branch/PR, project level, related spec | Findings per §7, DoD gaps, sin shortcodes, evidence bundle |
| Feedback loop into the bible | A useful pattern or a new risk repeated | Observation, evidence, where it repeated | An entry in `patterns.md` or a proposal to change the bible, the template, or a playbook (format — in `playbooks/propose-bible-change.md`) |

## 3. Basic process

1. Pick a mode from the table above.
2. Open the matching playbook in `playbooks/` (or invoke it as an agent skill — §6).
3. Ask the agent to read not only the project but also the bible: at least §2–§3 (levels and "+ customers"), §4, §4½, §5, §6 (the loop), §7, §8, and §10.
4. Get the report in the format from the playbook or `templates/audit-report.md`.
5. The project owner decides: fix now, open a follow-up, move the rule into the environment, turn on a check.
6. After a real application, optionally prepare a `registry.md` draft row with the owner's consent; a human opens the upstream PR.
7. If the same pattern repeated 3+ times, run `playbooks/propose-bible-change.md`.

## 4. Example agent request

Use the [first-audit prompt](./README.md#first-audit): it separates the Bible root from the target project, states the next step, and limits execution. Keep unknown environment settings separate from confirmed gaps. A solo author check is permitted without customers (§3), but is not independent review; a gateway is optional, verifiable data controls are mandatory.

For a PR:

```text
Read vibe-engineering-bible.md and playbooks/review-pr.md.
Review the current diff as a pre-PR review for Production without customers.
Show blocker/warn/note first, then propose minimal fixes.
```

## 5. Checks, consequences, principles — by reference

Check classes (D / P / H) and the "advisory → calibration → block" path — §5 of the bible; consequences — §4½; the loop and the outcome — §6; application principles — Appendix F; file map — [`README.md`](./README.md).

## 6. Playbooks as development-agent skills

The playbooks are the source of truth. Copying a playbook alone loses dependencies. The builder creates four relocatable packages:

| Skill | Source |
|---|---|
| `bible-init-project` | `playbooks/init-project.md` |
| `bible-audit-project` | `playbooks/audit-project.md` |
| `bible-review-pr` | `playbooks/review-pr.md` |
| `bible-propose-change` | `playbooks/propose-bible-change.md` |

Each contains a short `SKILL.md` router, the public resources under `references/bible/`, and `SOURCE.json`. All Bible-relative paths resolve from that bundled root; the target project is a separate input. Output belongs in the destination requested by the user, outside skill resources.

For the pinned v2.1.1-en source and local installation, use the [README commands](./README.md#install-v211-en-skills). The commands below build from any reviewed checkout.

### Build and check

From this checkout, with Python 3.9+ and no third-party packages:

```sh
python3 -m unittest discover -s tests -v
skill_build=$(mktemp -d)
python3 scripts/package_skills.py --output "$skill_build/skills"
```

The builder reads an allowlist of public source paths; it does not download anything or change client settings. It rejects resource symlinks, an output symlink, and existing skill folders; it validates inputs and all four destination names before writing. `SOURCE.json` records the git base commit when available, a hash of the actual source content, the builder hash, and hashes of every packaged file. A dirty checkout is a local content snapshot, not the pristine base commit. Keep the manifest with the files; hashes detect changes, not trustworthiness. Git is optional; an unpacked snapshot has a null base commit.

### Install into an isolated project

Review the sources first. The following creates a new temporary project and installs all four packages into its local skills directory. Run it from the Bible checkout:

```sh
skill_demo=$(mktemp -d)
mkdir -p "$skill_demo/.agents/skills"
python3 scripts/package_skills.py --output "$skill_demo/.agents/skills"
printf 'Open this project in your agent: %s\n' "$skill_demo"
```

A local installation controls where skill files reside; it does not make the model local. Use only the model and data scope already authorized by the project owner. Files read by a hosted model enter its context; the first-audit prompt prohibits additional external tool calls and uploads. Existing access and data-flow controls still apply.

Open that temporary project in Codex, start a new session, and request `$bible-audit-project` with an absolute target-project path, purpose, users, level and execution limits. Where another client supports project-local Agent Skills, use its documented skills directory and copy each entire package, preserving `references/` and `SOURCE.json`. Discovery and behavior depend on the client; packaging alone does not prove compatibility. No global installation is needed.

For an existing project, choose a reviewed destination and build there explicitly. Existing packages are never replaced: review an update in a separate directory before changing an installed version. Keep the catalog in git with owners and reviewed changes; external skills are dependencies under Commandment V.

### Verification limits

Local unit tests and build/install checks verify package structure, dependencies, hashes, relocation, and refusal behavior. They do not measure audit quality or establish compatibility with every agent. The [public example](./examples/audit/README.md) lets a person reproduce the stated facts without running project code. Client smoke results, when available, are bounded observations; no cross-client or general reliability claim follows from them.

A skill packages the procedure; the canon and the user's authorized scope still apply. Registration is opt-in, the agent prepares a draft, and a human opens any upstream PR.
