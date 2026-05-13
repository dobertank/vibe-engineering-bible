# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is a **documentation-only repo** — a policy for working with AI assistants for teams of any size: from a solo developer or OSS maintainer to a large organization. There is no code, no tests, no build, no linters. Do not suggest `npm`, `pytest`, `make`, or similar commands — there is nothing here to apply them to.

It holds two files:

- **`vibe-engineering-bible.md`** — the canonical "bible". Core (§§1–10): two covenants (Freedom for T0, Discipline for T1+), eight commandments, thirteen sins (§4½ — a normalized shortcode vocabulary for merge rejections), a DoD table across T0–T3, spec-driven workflow, an AI-code reviewer checklist, baseline-template principles, scaling KPIs, glossary. Sources are in Appendix D.
- **`templates/CLAUDE.md.template.md`** — baseline template for AI agents in a product repo. Applies to a team of any size. Teams copy it into their repo as `CLAUDE.md` or `AGENTS.md` and extend only section 8.

The template is the single source of truth for the baseline. §8 of the bible describes the principles; the template body lives only in `templates/CLAUDE.md.template.md`.

## Cross-file semantics

- **The bible** holds the shared model: commandments, sins, DoD, KPIs, spec-driven workflow, reviewer checklist.
- **The template** holds concrete instructions for AI agents in product repos. Teams copy it as `CLAUDE.md` or `AGENTS.md`, extend section 8 (repo-specific) only; sections 1–7 are not edited.
- When editing the bible or the template, check the other file for semantic consistency. The mapping is not 1:1:
  - **Commandments §4 of the bible → §4 of the template:** V/VI → §4.1–4.2 (security, dependencies); VII → §4.3–4.4 (size, tests); VIII → §4.6 (documentation).
  - **Commandment IV (one stack, paved road) → §2 of the template** ("Stack and commands"). The template holds `{{...}}` placeholders — the team fills them in for their stack.
  - **DoD table §5 of the bible → §6 of the template** ("Definition of Done for this tier"). §6 of the template pre-fills three variants (T1/T2/T3); the team deletes the two that do not apply.
  - **Spec-driven §6 of the bible → §5 of the template** (the "For T2+ changes…" block) **and §7 of the bible item 8** (reviewer checklist). Any change to the `openspec/changes/<x>/{proposal,specs,design,tasks}.md` artifacts must be reflected in all three places.
  - **Covenants §2–§3 of the bible** have no direct counterpart in the template: T0 is not described in the template (the template is installed in T1+ repos).
  - **Sins §4½ of the bible** are a normalized shortcode vocabulary for merge rejections. There is no direct counterpart in the template (the template describes rules; sins are the language of their violation). When adding/removing a sin, sync the *Sins here:* cross-references in the corresponding §4 commandment and the §10 glossary entries. Every row of §4½ must have a live "root" in §4/§5/§7 — a sin without a root cannot be written.
  - **Sources for figures in §1 and §4½ → Appendix D of the bible.** Any claim with a figure or a CVE must have a link in Appendix D. Change figures only when a newer version of the research appears, and update the link in the same commit.

## Editing principles for these files

The document describes itself — follow its rules when making edits:

- **Brevity over completeness.** The target for the root `CLAUDE.md` in a product repo is ≤2000 tokens. If a line can be removed without losing meaning — remove it.
- **Imperative, not description.** "Use pytest" — yes. "This project historically uses pytest" — no.
- **Concrete, not ideological.** Rules must be verifiable.
- The bible is structured into numbered sections (1–10) plus §4½ "Sins" between Commandments (§4) and DoD (§5), plus Appendix D after §10. The fractional §4½ is intentional — it preserves anchor stability for §5–§10. When inserting new material, preserve this scheme: new sections only as 4½/4¾, inside existing ones, or as a new Appendix.
- Write and respond in **English** — all files and all discourse are in English.
- Commits follow Conventional Commits (`feat`, `fix`, `chore`, `docs`, …).

## What NOT to do

- Do not turn these documents into a README with project history or marketing.
- Do not return a duplicate of the template into the bible: §8 of the bible holds only principles and a link to the template; the template body lives in `templates/CLAUDE.md.template.md`.
- Do not add repo-specific content to the template — section 8 of the template is for that (filled in by the team that owns the service repo, not this repo).
- Do not insert links or citations that are not in Appendix D without an explicit user request — Appendix D is deliberately anchored to vetted publications (METR, USENIX Spracklen, GitClear, Veracode, Stanford Perry, CodeRabbit, Apiiro, Mollick/BCG, MCP CVE list, Anthropic auto-mode, etc.).
- Do not edit figures in §1 and §4½ by feel. Percentages, sample sizes, years, CVE IDs, CVSS scores are pinned to specific publications in Appendix D. Change them only when a newer version of the research appears, and update the Appendix D link in the same commit.

## Terminology (minimum for navigation)

- **Covenant of Freedom / Covenant of Discipline** — the bible's meta-structure. Freedom is §2 for T0; Discipline is §3+ for T1+. The boundary runs along the personal experiment.
- **T0 / T1 / T2 / T3** — four tiers of code (experiment / prototype / internal tool / production). Each tier has a row in DoD §5 of the bible. Mapping to lifecycle metadata (experiment/prototype/mvp/beta/production/deprecated) is in §3 of the bible.
- **Lethal trifecta** — (private data) + (untrusted input) + (external channel). Simon Willison's formulation.
- **Paved road / Golden Path** — the supported default path.
- **Slopsquatting** — a supply-chain attack via names that LLMs often hallucinate.
- **Spec-driven workflow / OpenSpec** — for T2+: artifacts `openspec/changes/<x>/{proposal.md, specs/, design.md, tasks.md}`; after release, the delta is merged into `openspec/specs/`. §6 of the bible. OpenSpec supports 20+ AI agents.
- **Sins (mortal / venial)** — a normalized vocabulary of 13 shortcodes (§4½ of the bible). Mortal (7): `#sandbox-bypass`, `#trifecta`, `#promptable`, `#test-del`, `#merge-pray`, `#workslop`, `#hidden-ai`. Venial (6): `#slot-machine`, `#self-auto`, `#confident-wrong`, `#tautological`, `#sycophancy`, `#zombie-t0`. The list is normalized: reviewers do not invent names.
