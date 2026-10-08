# Init result: <project>

Date: <YYYY-MM-DD>
Owner: <name/team>
Mode and tier: <experiment (T0) / T1 / T2 / T3>
Expected lifetime: <duration>
Baseline: <CLAUDE.md / AGENTS.md / both / none>

## Project Brief

<What we are building, for whom, which data, which constraints.>

Expected outcome: <what will change in the product and how we will confirm it; mandatory for T2+>

## Tier Decision

Chosen tier: <T0/T1/T2/T3>

Why:

- <reason>
- <reason>

Event that moves it to the next tier (by event, not by feel):

- <trigger>

Agent autonomy at this tier: <T0 — acts on its own in an isolated environment / T1–T2 — works on its own, changes reach shared code only after human review / T3 and sensitive data — only proposals or actions with mandatory human confirmation>

## Created / Updated

- README: <yes/no/path>
- CLAUDE.md / AGENTS.md: <yes/no/path>
- openspec/: <yes/no/path/n-a>
- CI: deterministic checks: <yes/no/path/n-a>; probabilistic (advisory): <yes/no/n-a>
- Agent configuration under CODEOWNERS: <yes/no/n-a>
- Registry entry (`registry.md`): <yes/no>

## Initial DoD

| Requirement | Status | Comment |
|---|---|---|
| Owner assigned | pass/fail | |
| Mode and tier recorded; transition event named | pass/fail | |
| Sunset date for T1 | pass/fail/n-a | |
| Baseline installed, §3.1 "What the environment enforces" filled in | pass/fail/n-a | |
| T2+ deterministic checks on, or recorded as debt with an owner | pass/fail/n-a | |
| Outcome named in advance (T2+) | pass/fail/n-a | |
| Lethal trifecta excluded | pass/fail/n-a | |

## Next Actions

1. <first action>
2. <second action>
3. <third action>
