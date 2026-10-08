# Template for a registry.md entry

One row per project where the bible is actually applied. Add it after the first
real init/audit/review, not in advance.

```md
| <Project / adopter> | <Repo, if public> | <Owner / contact> | <I/II/III> | <T0/T1/T2/T3> | <init/audit/review/gate> | <Baseline> | <Last audit> | <Status> | <Next action> | <YYYY-MM-DD> |
```

Column order matches the `registry.md` header:
`| Project / adopter | Repo (if public) | Owner / contact | Profile | Tier | Mode | Baseline | Last audit | Status | Next action | Date |`

Fields:

- **Project / adopter** — a human-readable name. Required.
- **Repo** — a link, only if the repo is public. An internal path belongs only in an organization's internal copy of the registry.
- **Owner / contact** — the team or person who makes decisions; in the public registry — a handle.
- **Profile** — I small (1–10) / II mid-size (10–100) / III large (100+) — team-size bands from §9 of the bible.
- **Tier** — the current tier per §3 of the bible, not the desired one. T0 is experiment mode; T1–T3 are risk tiers within the Covenant of Discipline.
- **Mode** — how the bible is applied now: `init`, `audit`, `review` (pre-PR/PR), `gate` (checks are on in CI).
- **Baseline** — `none`, `CLAUDE.md`, `AGENTS.md`, `both`.
- **Last audit** — a date or a link to a report per `templates/audit-report.md`.
- **Status** — `pilot`, `advisory`, `active`, `gated` (deterministic checks block, probabilistic ones are calibrated or advisory), `archived`.
- **Next action** — one concrete step.
- **Date** — the date of the entry or its last update. Required.
