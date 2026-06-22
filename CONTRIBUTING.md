# How to contribute

The "Vibe Coding Bible" is a living standard with two upstream feedback channels
(field → bible): **patterns** and the **registry**. The full framing is Appendix E
of the bible.

The principle running through both channels: **the agent prepares, a human
confirms.** A PR to this (upstream) repo is an outward-directed action; under
Commandment VI of the bible and 12-factor agents (factor 7) an agent does not
perform such an action autonomously. The agent may prepare a draft entry and PR
text; a human opens and confirms the PR. An auto-PR by an agent is forbidden
(otherwise the bible would be teaching agents exactly what it itself forbids, and
would risk the `#workslop` sin).

## 1. Submit a pattern

If while working with an AI agent you found a pattern that **generalizes beyond
your repo** (not specific to your domain) — its place is here, in
[`patterns.md`](./patterns.md), not in a direct edit of the core.

The boundary: repo-specific → §8 of your own `CLAUDE.md` (the "repeated to the
agent 3+ times → a line in §8" rule). Generalizable → here.

Procedure:
1. Phrase the entry per the schema in [`patterns.md`](./patterns.md) ("Record
   schema"). A **root** is required — which commandment / sin / DoD it maps to (or
   "new area"). A pattern without a root is not accepted.
2. The agent prepares a draft entry and PR; **you review and open the PR yourself.**
3. The maintainer deduplicates against the core and the catalog and merges it as
   `accepted` (advisory) — this is **not** canon, but a visible part of the standard.

Preference goes to patterns with evidence (an incident, a repro); they rank higher
in the promotion queue. Pure opinion stays advisory.

## 2. The governance gate: how a pattern reaches the core

The core (§4 commandments, §4½ sins, §5 DoD) is **closed** and moves only through
this gate. The lifecycle:

```
Local → Submitted → Accepted (patterns.md, advisory)
                       │  ≥3 INDEPENDENT confirmations + mapping to a gap in the core
                       ▼
                    Candidate (staging) → reasoned ADR by the bible owner
                       │  approved, ≤ once per quarter
                       ▼
                    Promoted (→ §4 / §4½ / §5)   or Rejected / Deprecated
```

- **Promotion threshold — ≥3 independent confirmations** from different adopters.
  (Echoes the number 3 from §4½, but it is a different metric: there it is
  repetitions by one author per quarter; here it is independent adopters.)
- **Cadence** — promotion into the core no more than once a quarter (in sync with
  the quarterly bible review).
- **On promotion** a core edit drags ALL cross-references: for a new sin — the §4½
  table, the "Sins here" lines in the matching §4 commandment, the §10 glossary
  entry, and the "thirteen" count everywhere; for a DoD line — §5 + §6 of the
  template; for a figure/CVE source — Appendix D. The link map is in the project
  `CLAUDE.md`.

**Who is the owner.** In a large organization this may be a dedicated AI-code
group; in a small team the owner-developer or tech lead wears the hat. The gate
works even with a single maintainer — what matters is not the size of the body,
but that the core does not change by ad-hoc edits on the fly.

## 3. Register in the registry

Optional. Adds your repo/org to [`registry.md`](./registry.md) — the named, public
list of adopters.

The procedure is the same **the agent prepares, a human confirms**: the agent
prepares the table row and a draft PR, you review and open the PR yourself. Only
the **Adopter** and **Date** fields are required.

Remember: registration is **public**. The PR is signed by your GitHub account,
often with a corporate email in the commit. If disclosure is unacceptable — do not
register (that is fine, see §4) or request an aggregate entry.

## 4. Confidential adopters

Internal / enterprise repos, by the spirit of the bible itself, do not disclose the
fact or details of their use. For them:

- **Not registering is normal.** The registry deliberately undercounts; absence
  from it ≠ non-use.
- **Need an aggregate entry without disclosure** (a pseudonym like "fintech, ~200
  engineers, profile III, tiers T2–T3") — that goes through a **private channel,
  not a PR** (only a non-PR transport preserves anonymity; a PR deanonymizes the
  author). In v1 the channel is not built yet — message the maintainer directly,
  the door is open, we will add the infrastructure on demand.

## 5. Why exactly this way (self-consistency)

- A human-confirmed registry PR is a **working example** of Commandment VI of the
  bible: an outward action passes through a human.
- An advisory catalog + a gate into the core → the claim "the core does not move"
  is sharpened to "moves only through Appendix E", which is stricter, not weaker.
- The ≥3 threshold and the quarterly cadence reuse numbers that already exist in
  the bible — no new magic constants.

## 6. Editing the bible files themselves

If you edit the bible or the template directly (rather than submitting a pattern) —
follow the principles in the project [`CLAUDE.md`](./CLAUDE.md): brevity over
completeness, imperative over description, concrete over ideological; when editing
any file, check the others for consistency (the link map is there too). Commits
follow Conventional Commits (`feat`, `fix`, `chore`, `docs`, …). The figures in §1
and §4½ are pinned to Appendix D — change them only with an updated link.
