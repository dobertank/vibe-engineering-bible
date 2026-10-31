# How to contribute

Two upstream channels — patterns and the adoption registry; the framing, the pattern lifecycle, and the gate into the core — Appendix E of the bible.
The principle running through both: **the agent prepares, a human confirms.** A PR to the upstream repo is an outward action (Commandment VI): the agent
prepares a draft entry and the PR text, a human opens and confirms the PR. An auto-PR by an agent is forbidden.

## 1. Submit a pattern

Repo-specific — into section 8 of your own `CLAUDE.md`/`AGENTS.md` (repeated to the agent 3+ times → a line). What generalizes beyond
your domain — into [`patterns.md`](./patterns.md), not as an edit of the core.

1. Phrase the entry per the [`patterns.md`](./patterns.md) schema; a root is required.
2. The agent prepares a draft entry and PR — conveniently with the [`playbooks/propose-bible-change.md`](./playbooks/propose-bible-change.md) skill; **you review and open the PR yourself.**
3. The maintainer deduplicates against the core and the catalog and merges it as `accepted` — advisory, not canon.
   Patterns with evidence (an incident, a repro) rank higher in the promotion queue; pure opinion stays advisory.

To let a product repo's agent know about this channel, the team can add a line to section 8 of its file:
"A generalizable pattern is an entry in the bible upstream's `patterns.md`, not an edit of the core; a human opens the PR, the agent prepares the draft. Process — `CONTRIBUTING.md`: {{link to upstream}}".

## 2. Register in the registry

Optional, after the first real application. The agent prepares a row per the [`registry.md`](./registry.md) legend and a draft PR;
you review and open the PR yourself. The required fields are in the legend.

**Registering in the public repo is disclosure.** The PR is signed by your account, it is visible in the fork network, and the commit's author email often
carries a corporate domain. So:

- **Not registering is normal.** The registry deliberately undercounts; absence from it ≠ non-use.
- **An aggregate entry without disclosure** (a pseudonym like "fintech, ~200 engineers, Production + customers") — only through a private channel,
  not a PR: a PR deanonymizes the author. In v1 the channel is not built — message the maintainer directly.

## 3. Editing the files themselves

Editing the bible, the template, or the playbooks directly — follow [`AGENTS.md`](./AGENTS.maintenance.md): the "you edit X → check Y" table
and "what not to do". A core change (§4, §4½, §5) — only through the Appendix E gate and a reasoned ADR included in the proposal/PR text
(format — in [`playbooks/propose-bible-change.md`](./playbooks/propose-bible-change.md)). The gate works even with a single maintainer:
what matters is not the size of the owner group, but that the core does not change by ad-hoc edits on the fly. Commits follow Conventional Commits.
