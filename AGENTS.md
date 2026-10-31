# AGENTS.md

Instructions for agents editing the "Vibe Engineering Bible" repo. File map — [README.md](./README.md); terms — the glossary, §10 of the bible.

## Language and style

- Write and respond in **English**. Commits follow Conventional Commits. The main product is Markdown; the skill packager uses Python 3.9+ and the standard library. Check it with `python3 -m unittest discover -s tests -v`. Text edits need no build; do not suggest `npm`, `pytest`, `make`.
- When editing text, follow the principles of §8 of the bible: only the non-obvious, imperative, verifiable specifics; a line that can be removed without losing meaning gets removed.
- One thought — one place: the canon states the norm, the mechanism lives in the process layer (`usage.md`, `playbooks/`, `templates/`); link instead of repeating.
- The sacral register (covenants, commandments, sins) is mnemonic, not ideology. The counts "two covenants / eight commandments / thirteen sins" are the same in all files.

## You edit X → check Y

| You edit | Check |
|---|---|
| A §4 commandment | the template: I → §4.5; IV → §2, §3.1; V → §4.2, §3.2; VI → §4.1; VII → §4.3–§4.5; VIII → §5 |
| Paved road (Commandment IV) | §2 of the template holds only placeholders; the concrete list belongs to the adopter |
| Levels, "+ customers", autonomy (§2–§3) | §1, §3.1 (auto-merge), and §5 of the template; Prototype is not described in the template |
| A §5 DoD row | §6 of the template (only what is not in its §3–§5), deterministic gates in §3.1; classes D / P / H — playbooks, `templates/audit-report.md` |
| The §6 loop | §5 of the template, §7 items 8 and 10, `templates/intent.md`, `playbooks/review-pr.md` |
| The §7 checklist | `playbooks/review-pr.md`, `templates/REVIEW.md` |
| §8 (context files, skills) | header, §3, and §8 of the template; `usage.md` §6 |
| A §4½ sin | "Sins here" in the §4 commandment, the §10 glossary, consequences in §7 of the template, `review-pr.md`, `audit-project.md`, `audit-report.md`; every sin has a root in §4/§5/§7; a new sin — the "thirteen" count everywhere (intro, §4½, glossary, Appendix E, coda, README, this file) |
| §9 (metrics, ownership) | `usage.md` §1 (roles) |
| A figure or CVE in any file | the source in Appendix D (label [independent] / [vendor] / [self-report]) |
| Appendix E | `patterns.md`, `registry.md`, `CONTRIBUTING.md`, `docs/adr/` |
| Appendix F | `usage.md` (modes table), `playbooks/`, `templates/audit-report.md`, `registry.md`: modes, check classes, consequences |

## What not to do

- Do not bring back T0–T3 or a third level: there are two levels, "+ customers" is an overlay on Production; the 1.x labels appear only in the glossary (§3, glossary).
- Do not bring back hard sanctions: a mortal sin blocks the merge until fixed, blameless review; a venial one goes back for rework; no reports, escalations, or access restrictions on top (§4½).
- Do not bring back "advisory → hard gate for everything": deterministic gates block from day one, probabilistic ones after calibration, the exception is §5 #41 (§5).
- Do not widen auto-merge: only low-risk Production changes without customers per a calibrated risk assessment, with customers — never (§3).
- Do not hardcode an agent auto-PR into the template, the playbooks, or the mechanisms: the agent prepares a draft, a human opens the PR (Appendix E, Commandment VI).
- Do not promote `patterns.md` entries into the core (§4 / §4½ / §5) bypassing the Appendix E gate; candidates are not rejection shortcodes.
- Do not duplicate the template body in the bible: §8 holds the principles and a link to `templates/CLAUDE.md.template.md`.
- Do not add repo-specific content to the template outside the §1–§3 placeholders and section 8.
- Do not tie the core §§1–10 to a specific organization: org-specific release steps, roles, internal systems, tool lists, autonomy ladders belong in section 8 of an adopter's copy of the template or in the adopter's fork.
- Do not add figures, CVEs, links, or citations that are not in Appendix D without an explicit request; change figures only for a new version of the research, updating Appendix D in the same commit.
- Do not renumber the bible: new material goes inside a section, as 4¾, or as a new Appendix; §4½, the Appendix letters, and gaps in DoD numbering are intentional anchors.
- Do not turn `registry.md` into an organization's inventory and do not promise anonymity there (`CONTRIBUTING.md`, §2).
- Do not turn the documents into a README with project history or marketing.
