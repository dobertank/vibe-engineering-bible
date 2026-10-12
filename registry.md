# Adoption registry

An index of projects where the bible is actually applied: in this public upstream — an opt-in list of adopters; in an organization's internal copy — that organization's projects.
Not an inventory of all repositories and not a place for secrets or reports: details live in audit reports. Deliberately incomplete.
A row is added after the first real init / audit / review and updated after an audit, a change of level or mode, or archiving. How to get in and what about anonymity — [`CONTRIBUTING.md`](./CONTRIBUTING.md).

| Project | Owner | Level | Mode | Last audit | Next action |
|---|---|---|---|---|---|
| _Example Org / project_ | _@handle_ | _Production_ | _audit_ | _2026-06-21_ | _enable deterministic checks in CI_ |

<!-- The row above is a sample. Delete it when adding the first real entry. -->

- **Project** — a human-readable name; a link to the repo — only if it is public. Required.
- **Owner** — the team or person who makes decisions; in the public registry — a handle. Required in an internal copy.
- **Level** — the actual one, not the desired one (§2–§3 of the bible): Prototype, Production, or Production + customers ("+ customers" is an overlay, not a third level).
- **Mode** — how the bible is applied now: `init`, `audit`, `review` (pre-PR/PR), `gate` (deterministic checks block in CI, probabilistic ones are calibrated or advisory), `archived`. Required in an internal copy.
- **Last audit** — a date or a link to a report per [`templates/audit-report.md`](./templates/audit-report.md); until there has been an audit — the date of the entry. Required.
- **Next action** — one concrete step.
