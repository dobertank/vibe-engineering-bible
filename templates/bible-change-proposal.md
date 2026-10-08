# Proposal: <short title>

Status: draft
Author: <name/team>
Date: <YYYY-MM-DD>
Change class: <satellite (playbook, template, usage) / patterns.md / core (§4, §4½, §5 — only through the Appendix E gate)>
Type: <add / change / remove outdated / move from text into the environment>

## Trigger

<What happened: repeated audit finding, incident, pilot result, new source, outdated rule.>

## Evidence

- <link/path to audit report, PR, incident note, meeting note>
- <second evidence item if any>

Independent confirmations (the core needs ≥3 from different adopters): <N, links to entries in patterns.md>

## Problem

<Which risk or friction repeats. Why the project's local §8 is not enough. Can this be enforced by the environment (managed settings, hooks, CI) rather than by text.>

## Proposed Change

<What exactly changes. Write it as a diff of meaning, not an essay.>

## Scope

Files:

- `vibe-engineering-bible.md`
- `templates/CLAUDE.md.template.md`
- `usage.md`
- `playbooks/...`
- `patterns.md`
- `docs/adr/<NNNN>-<name>.md` — for core changes (reasoned ADR)
- other: <...>

## Compatibility

<What must stay consistent: §4 → template §3–§4, DoD §5 → template §6, the loop §6 → template §5 and bible §7 item 8, Appendix F → usage/playbooks/templates/registry, Appendix D for figures; the counts "two covenants / eight commandments / thirteen sins".>

## Source Impact

New figures/CVEs/studies: <none / list>
Appendix D needs an update: <yes/no>

## Rollout

<How to apply the change to projects in registry.md: a deterministic check — block immediately together with a path to fix; a probabilistic one — advisory → calibration → block; a text rule — a template diff.>

## Rejection Criteria

<Under which facts the proposal should be rejected or kept as a repo-specific rule.>
