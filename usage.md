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

The local candidate ships four ready folders under `skills/`; installation does not run Python. The [README installation](./README.md#install-ready-skills-local-candidate) uses a local checkout because these folders have not been published yet. The existing `v2.1.1-en` release is the earlier builder-based package, not this candidate.

| Skill | Use | Source |
|---|---|---|
| `bible-audit-project` | Requested existing-project Bible audit | `playbooks/audit-project.md` |
| `bible-review-pr` | Requested review of a supplied diff or exact base/head | `playbooks/review-pr.md` |
| `bible-init-project` | Requested Bible initialization/adoption | `playbooks/init-project.md` |
| `bible-propose-change` | Local proposal to change the Bible standard | `playbooks/propose-bible-change.md` |

Use the audit first when assessing an existing repository. A feature request does not activate a Bible audit or standard-change proposal. A review needs an actual comparison; init preserves existing project instructions; proposal drafts do not authorize upstream actions.

Each `SKILL.md` is generated from its source playbook's contract. It includes triggers, exclusions, inputs, output, reading order and boundaries. All Bible paths resolve under its adjacent `references/bible/`; the target project is a separate input. No separate Bible checkout or builder execution is needed during use. Keep each entire folder with its `SOURCE.json` and MIT LICENSE.

The bundle keeps the full public corpus and banner. Bible-maintenance instructions are retained as inert `AGENTS.maintenance.md` and `CLAUDE.maintenance.md`, with their maintenance links/import mapped to those names. They are not active target instructions. Actual target instructions and the user's requested language govern responses. The original root AGENTS/CLAUDE are unchanged and still apply when maintaining this repository.

### Maintaining the generated skills

Python 3.9+ standard library is only for maintainers. From a source checkout:

```sh
python3 -B -m unittest discover -s tests -v
python3 scripts/package_skills.py --check
skill_build=$(mktemp -d)
python3 scripts/package_skills.py --output "$skill_build/skills"
```

`--check` compares current generated files without writing, including missing, extra, changed or symlink entries. To update, generate into a new output, inspect its diff against the four checked-in trees, confirm no unknown local changes, then copy only those reviewed trees. Existing destinations are never overwritten by `--output`; no installer or refresh manager is provided. Checked-in `skills/` is never a generator input, so packages do not recursively include themselves.

`SOURCE.json` records exact bundled-resource content identity, builder hash and all packaged file hashes; it excludes itself. `base_commit` is always null: moving HEAD without changing source bytes cannot create drift, and unpacked copies produce identical bytes. Git revision belongs in an external report or release tag. Canon and LICENSE are copied byte-for-byte; only maintenance filenames and their bounded links/import are mapped. Hashes detect change, not trustworthiness.

The bundled maintenance source can regenerate packages into a fresh destination without the original checkout. Checkout-only `--check` expects the four checked-in trees; an installed package intentionally has no recursive `skills/` copy. Its portable unit fixtures run independently, with that one checkout-only test skipped.

### Verification limits

Packaging checks cover metadata, content identity, complete references/license, inert maintenance instructions, relocation, refusal behavior and freshness. Real local CLI installation and bounded synthetic Codex cases are recorded separately in local implementation evidence; neither structural checks nor a small behavioral comparison proves effectiveness, whole-system safety or compatibility with every client. Claude execution is not established. The [public example](./examples/audit/README.md) supports reproducing its facts and one fix/recheck, not scoring an agent.

Local installation does not make a hosted model local. Use only a model and data scope already authorized by the project owner; keep access/data-flow controls. A skill grants no additional external permissions. Registration is opt-in; the agent prepares a draft and a human opens any upstream PR.
