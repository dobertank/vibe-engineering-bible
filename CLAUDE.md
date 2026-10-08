# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is a **documentation-only repo** of the "Vibe Engineering Bible" — a policy for working with AI assistants for teams of any size: from a solo developer or OSS maintainer to a large organization. There is no code, no tests, no build, no linters. Do not suggest `npm`, `pytest`, `make`, or similar commands — there is nothing here to apply them to.

It holds the canon, the baseline template, the application process layer, and the evolution mechanism — all in English:

- **`vibe-engineering-bible.md`** — the canonical "bible". Universal core (§§1–10): two covenants (Freedom — experiment mode, T0; Discipline — engineering mode with risk tiers T1–T3 and an event-triggered transition), eight commandments, thirteen sins (§4½ — a normalized shortcode vocabulary for merge rejections, blameless consequences), a DoD table across T0–T3 with a gate-class column (D / P / H), the loop "spec → agent → verification → rollout → outcome" (§6), an AI-code reviewer checklist (§7, *Inquisitio Codicis*), context files and development-agent skills (§8), paired metrics and ownership (§9), glossary. Sources — Appendix D. Standard evolution — Appendix E. Applying the bible to projects — Appendix F.
- **`templates/CLAUDE.md.template.md`** — baseline template for AI agents in a product repo. Applies to a team of any size. Teams copy it into their repo as `CLAUDE.md` and/or `AGENTS.md`, fill in the placeholders in §1–§3, and extend section 8.
- **`usage.md`** — how to use the repo as a "point of righteousness": roles, init/audit/review/proposal modes, two classes of checks, playbooks as development-agent skills, artifacts.
- **`playbooks/`** — operational scenarios: `init-project.md`, `audit-project.md`, `review-pr.md`, `propose-bible-change.md`. Each has a YAML header `name`/`description` and can be shipped as a `SKILL.md`. Playbooks describe a process; they do not replace the bible's canon.
- **`templates/audit-report.md`, `templates/init-result.md`, `templates/project-registry-entry.md`, `templates/bible-change-proposal.md`** — forms for the playbooks' output artifacts. They are not baseline instructions for product repos.
- **`patterns.md`** — an advisory catalog of field patterns + staging for sin candidates (queue and candidates). A growing surface of self-evolution (Appendix E). Not canon: promotion into the core only through the gate.
- **`registry.md`** — the adoption registry: in this public upstream — an opt-in list of adopters and applications; in an organization's internal copy — an index of projects where the bible is actually applied (tier, owner, init/audit/review/gate mode, last audit, next step). Deliberately incomplete.
- **`CONTRIBUTING.md`** — the process for both upstream channels (patterns, registry) + the governance gate. Contribution is always opt-in + human-confirmed.
- **`docs/adr/`** — reasoned ADRs on core changes (starting with `0001-bible-2.0.md`).

The template is the single source of truth for the baseline. §8 of the bible describes the principles; the template body lives only in `templates/CLAUDE.md.template.md`.

## Cross-file semantics

- **The bible** holds the shared model: covenants and risk tiers, commandments, sins and their consequences, DoD, the loop, KPIs, reviewer checklist.
- **The template** holds concrete instructions for AI agents in product repos. Teams copy it as `CLAUDE.md` or `AGENTS.md`, fill in the §1–§3 placeholders (including §3.1 "what the environment enforces") and extend section 8 (repo-specific); the rules in §4–§7 are not edited.
- **`usage.md` and `playbooks/`** hold the process of applying the bible to projects: init, audit, PR review, a proposal to change the canon.
- **`templates/audit-report.md` and the sibling forms** hold the structure of the playbooks' output artifacts, not rules of agent behavior.
- **`registry.md`** links the canon to real projects: project, tier, owner, application mode, last audit, baseline, next step.
- When editing the bible or the template, check the other files for semantic consistency. The mapping is not 1:1:
  - **Commandments §4 of the bible → template:** I (`Assisted-by:`, the responsible author is a human) → §4.5; IV (The law lives in the environment) → §2 (stack) and §3.1 (what the environment enforces); V (dependencies and agent configuration) → §4.2 and §3.2; VI → §4.1; VII (review, human review capacity) → §4.3–4.5; VIII (Done means proven) → §4.6 and §5 (evidence bundle, outcome). When editing a commandment, check the template.
  - **Commandment IV (paved road) → §2 of the template.** The template holds `{{...}}` placeholders — the adopting team fills them in for its stack. A concrete paved-road list belongs to the adopter, not to this repo.
  - **Risk tiers and agent autonomy (§3 of the bible) → §1 and §5 of the template.** Mapping autonomy onto a specific organization's levels stays out of the core and out of the template.
  - **DoD table §5 of the bible → §6 of the template** ("Definition of Done for this tier") **and §3.1 of the template** (class-D deterministic gates). §6 of the template pre-fills three variants (T1/T2/T3) in compact form; the team deletes the two that do not apply. Gate classes (D / P / H) — the "Gate" column in §5 of the bible; `usage.md` and `templates/audit-report.md` use the same classes. When editing a DoD row, check the template.
  - **The loop §6 of the bible → §5 of the template** (spec sized to the task, the `openspec/changes/<x>/{proposal,specs,design,tasks}.md` artifacts, evidence bundle, outcome) **and §7 of the bible, items 8 and 10** (reviewer checklist: spec; evidence bundle and outcome). Any change to the spec artifacts must be reflected in all these places.
  - **§8 of the bible (context files and development-agent skills) → header, §3 and §8 of the template + `usage.md` §6.** The principles "only the non-obvious, ≤~150 lines, mandatory rules live in the environment" live in §8 of the bible; the template follows them; `usage.md` describes shipping playbooks as skills.
  - **§9 of the bible (metrics and ownership) → `usage.md` §1 (roles) and §5 (two classes of checks).** §9 is the general frame (paired metrics, adoption ≠ result, review capacity, gate classes, owner group and harness owner, sizing to the team); `usage.md` must not contradict it.
  - **Covenants §2–§3 of the bible**: experiment mode (T0) is not described in the template (the template is installed in T1+ repos). The Covenant of Freedom is for humans, not for AI agents in product repos.
  - **Sins §4½ of the bible** are a normalized shortcode vocabulary for merge rejections. There is no direct counterpart in the template (the template describes rules; sins are the language of their violation); the consequences are briefly repeated in §7 of the template, in `playbooks/review-pr.md`, `playbooks/audit-project.md`, and `templates/audit-report.md`. When adding/removing a sin, sync the *Sins here:* cross-references in the corresponding §4 commandment and the §10 glossary entries. Every row of §4½ must have a live "root" in §4/§5/§7 — a sin without a root cannot be written. The §4½ list is closed; it legitimately grows only through the Appendix E gate (staging in `patterns.md` → reasoned ADR in `docs/adr/`). When promoting a new sin, also sync the "thirteen" count everywhere (intro, §3, README, this `CLAUDE.md`, glossary).
  - **Sources for figures in §1, §4, §4½, §8, §9 → Appendix D of the bible.** Any claim with a figure or a CVE — in any file of the repo — must have a link in Appendix D (with the [independent] / [self-report] / [vendor] label where it has one). Change figures only when a newer version of the research appears, and update the link in the same commit.
  - **Appendix E of the bible (standard evolution) → `patterns.md` / `registry.md` / `CONTRIBUTING.md` / `docs/adr/`.** The core (§4/§4½/§5) is closed; it grows only through the Appendix E gate. `patterns.md` is an advisory catalog; promotion into the core is by reasoned ADR, ≤ once per quarter, with a threshold of ≥3 independent confirmations and an update of all cross-references. The "Contributing upstream" hook in the template (§7) points to these files. When you edit any of them, check Appendix E and the template hook for consistency, and vice versa. Contribution is always opt-in + human-confirmed (Commandment VI); an auto-PR by an agent is forbidden.
  - **Appendix F of the bible (applying the bible to projects) → `usage.md`, `playbooks/`, `templates/{audit-report,init-result,project-registry-entry,bible-change-proposal}.md`, `registry.md`.** Appendix F is the short canonical frame; detailed steps live in the playbooks; report formats in `templates/`; the list of applications in `registry.md`. When you edit one of these files, check the others for divergence in the four modes (init/audit/review/proposal), the two classes of checks, and the consequences.

## Editing principles for these files

The document describes itself — follow its rules when making edits:

- **Brevity over completeness.** The target for the root `CLAUDE.md` in a product repo is ≤~150 lines, only the non-obvious; mandatory rules live in the environment (agent settings, hooks, CI), not in text. If a line can be removed without losing meaning — remove it.
- **Imperative, not description.** "Use pytest" — yes. "This project historically uses pytest" — no.
- **Concrete, not ideological.** Rules must be verifiable.
- The bible is structured into numbered sections (1–10) plus §4½ "Sins" between Commandments (§4) and DoD (§5), plus Appendix D, E, and F after §10. The fractional §4½ is intentional — it preserves anchor stability for §5–§10. Appendix letters and DoD row numbers are stable anchors: do not re-letter or renumber them; gaps in the sequences are intentional. When inserting new material, preserve this scheme: new sections only as 4½/4¾, inside existing ones, or as a new Appendix.
- The name is "Vibe Engineering Bible". The register is sacral (covenants, commandments, sins, Latin) — mnemonic, not ideology. The counts "two covenants / eight commandments / thirteen sins" are the same in all files.
- Write and respond in **English** — all files and all discourse are in English.
- Commits follow Conventional Commits (`feat`, `fix`, `chore`, `docs`, …).

## What NOT to do

- Do not turn these documents into a README with project history or marketing.
- Do not return a duplicate of the template into the bible: §8 of the bible holds only principles and a link to the template; the template body lives in `templates/CLAUDE.md.template.md`.
- Do not add repo-specific content to the template outside the provided placeholders in §1–§3 and section 8 (filled in by the team that owns the service repo, not this repo).
- Do not insert links or citations that are not in Appendix D without an explicit user request — Appendix D is deliberately anchored to vetted publications (METR, USENIX Spracklen, GitClear, Veracode, Stanford Perry, CodeRabbit, Apiiro, Mollick/BCG, DORA, ETH AGENTS.md, MCP CVE list, Anthropic auto-mode, etc.).
- Do not edit figures in §1 and §4½ by feel. Percentages, sample sizes, years, CVE IDs, CVSS scores are pinned to specific publications in Appendix D. Change them only when a newer version of the research appears, and update the Appendix D link in the same commit.
- Do not tie the core to a specific organization. Organization-specific release processes, roles, internal systems, tool lists, or autonomy levels are never mandatory in §§1–10; the core names generic concepts (service catalog, LLM proxy, release process) as optional. Organization specifics belong in section 8 of an adopter's copy of the template or in the adopter's own fork, not in this repo.
- Do not bring back hard sanctions: a mortal sin is blocking (the PR does not merge until fixed; blameless review), a venial one goes back for rework. No consequences on top of the block: incident reports, escalations to a body, access restrictions, "conversations with the tech lead".
- Do not mix gate classes: deterministic checks block from day one, together with a fix path; probabilistic ones (AI review, LLM judge, mutation score) — only after calibration on your own data. Do not bring back the "advisory → hard gate for everything" principle.
- Do not let `patterns.md` entries into the core (§4/§4½/§5) bypassing the Appendix E gate. The catalog is advisory; queued candidates are not rejection shortcodes; promotion is only by reasoned ADR with a threshold of ≥3 independent confirmations, ≤ once per quarter.
- Do not turn `registry.md` into a full inventory of an organization: it is a registry of bible applications, not a service catalog.
- Do not promise anonymity in `registry.md`: a self-registration PR reveals the author (GitHub handle, fork, often a corporate email in the commit). An anonymous/aggregate tier is only via a non-PR channel (`CONTRIBUTING.md` §4), and it is not built in v1.
- Do not hardcode an agent auto-PR into the template, the playbooks, or the mechanisms: upstream contribution is opt-in + human-confirmed (Commandment VI). The agent prepares a draft, a human opens the PR.

## Terminology (minimum for navigation)

- **Covenant of Freedom / Covenant of Discipline** — the bible's meta-structure. Freedom is experiment mode (T0, §2): three boundaries (no production/customer data, no work secrets, no shared state), ≤30 days. Discipline is engineering mode (§3+): everything someone other than the author uses.
- **Event-triggered transition** — you showed it outside your team; someone other than the author started using it; real data, secrets, or shared state became necessary; you asked for it to be put on the roadmap.
- **T0 / T1 / T2 / T3** — T0 is experiment mode; T1 (prototype) / T2 (internal tool) / T3 (product for customers, public release) are **risk tiers inside the Covenant of Discipline**, not separate modes. Each has a row set in DoD §5 of the bible. Mapping to lifecycle metadata (experiment/prototype/mvp/beta/production/deprecated) is in §3 of the bible.
- **Agent autonomy by tier** — T0: on its own in an isolated environment; T1–T2: on its own, into shared code only after human review; T3 and sensitive data: only proposals or actions with confirmation. Auto-merge without a human — only after the checks are calibrated on your own data.
- **The loop** — spec → agent does → verification → rollout → outcome (→ refines the spec). §6 of the bible. Work is closed when the outcome is confirmed, not when the code is merged.
- **Evidence bundle** — spec + check run + known gaps; attached to the PR.
- **Gate classes D / P / H** — deterministic checks block from day one; probabilistic (AI-assisted or threshold-based) ones follow "advisory → calibration → block"; human decisions are DoD rows, not automated gates.
- **Calibration** — comparing a probabilistic check with human decisions on your own data (target — TPR/TNR > 90% on dev and held-out sets) before it may block.
- **Human review capacity** — the bottleneck: PR size and time to first human review are part of the paired metrics.
- **Harness / harness owner** — the agent's environment (agent settings, hooks, LLM proxy, isolated environment, skills catalog) and the person responsible for it.
- **Development-agent skills** — skills (`SKILL.md`) in a git catalog with owners; the init/audit/review/proposal playbooks are packaged as skills. Agent configuration is a dependency too (Commandment V).
- **Owner group** — a small group from the teams doing the adoption work, one owner per part; accepts changes to the bible and the template. Not a committee.
- **Lethal trifecta** — (private data) + (untrusted input) + (external channel). Simon Willison's formulation.
- **Paved road / Golden Path** — the supported default path.
- **Slopsquatting** — a supply-chain attack via names that LLMs often hallucinate.
- **Spec-driven workflow / OpenSpec** — spec sized to the task; for non-trivial T2+ changes — artifacts `openspec/changes/<x>/{proposal.md, specs/, design.md, tasks.md}`; after release, the delta is merged into `openspec/specs/`. §6 of the bible. OpenSpec / Spec Kit / Kiro are candidates; the team fixes one.
- **Sins (mortal / venial)** — a normalized vocabulary of 13 shortcodes (§4½ of the bible). Mortal (7): `#sandbox-bypass`, `#trifecta`, `#promptable`, `#test-del`, `#merge-pray`, `#workslop`, `#hidden-ai` — block the merge until fixed, blameless review. Venial (6): `#slot-machine`, `#self-auto`, `#confident-wrong`, `#tautological`, `#sycophancy`, `#zombie-t0` — back for rework; a recurring pattern is a reason to fix the process or the environment. The list is normalized: reviewers do not invent names.
- **Point of righteousness** — a git-first repository of rules, templates, and playbooks through which projects go through init/audit/review and get a common language of quality.
- **Bible audit** — an advisory check of a project against §3–§8 with a blocker/warn/note report. Not the same as automated refactoring.
- **Adoption registry** — `registry.md`: an index of projects where the bible is actually applied, plus the opt-in list of adopters.
- **Standard evolution (Appendix E)** — upstream field→bible channels: `patterns.md` (advisory catalog + staging for sin candidates), `registry.md` (adoption registry, opt-in), `CONTRIBUTING.md` (process + gate), `docs/adr/` (reasoned ADRs). The core grows only through the gate: staging → reasoned ADR, threshold ≥3 independent confirmations, ≤ once per quarter. The quarterly review removes what is outdated. Contribution is opt-in + human-confirmed (Commandment VI); an auto-PR by an agent is forbidden.
