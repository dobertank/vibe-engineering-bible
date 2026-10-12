# Init result: <project>

Date: <YYYY-MM-DD>
Owner: <name/team>
Level: <Prototype / Production> · customers: <yes / no>
Expected lifetime: <duration>
Baseline: <CLAUDE.md / AGENTS.md / both / none>

## Project Brief

<What we are building, for whom, which data, which constraints.>

Expected outcome: <what will change in the product and how we will confirm it; mandatory for Production>

## Level Decision

Chosen level: <Prototype / Production> · customers: <yes / no>

Why:

- <reason>
- <reason>

Transition event (Prototype → Production or Production → "+ customers"; by event, not by feel):

- <trigger>

Agent autonomy at this level: <Prototype — acts on its own in an isolated environment / Production — works on its own, changes reach shared code only after human review / + customers and sensitive data — only proposals or actions with human confirmation>

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
| Level and the "customers" flag recorded; transition event named | pass/fail | |
| Prototype: the environment holds the three boundaries, lifetime ≤30 days | pass/fail/n-a | |
| Baseline installed, §3.1 "What the environment enforces" filled in | pass/fail/n-a | |
| Production deterministic checks on, or recorded as debt with an owner | pass/fail/n-a | |
| Outcome named in advance (Production) | pass/fail/n-a | |
| Lethal trifecta excluded | pass/fail/n-a | |

## Next Actions

1. <first action>
2. <second action>
3. <third action>
