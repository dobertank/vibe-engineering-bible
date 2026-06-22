# Field pattern catalog

> **An advisory catalog, not canon.** This is where patterns found in practice
> land — by teams that use the "Vibe Coding Bible": what systematically breaks,
> or conversely reliably works, when working with AI agents. Entries here are
> observations and proposals, not core rules.
>
> **Invariant:** `accepted ≠ canonical`. The bible core (§4 commandments, §4½
> sins, §5 DoD) is closed and moves **only through the gate** — rarely, via a
> reasoned ADR, updating every cross-reference. The catalog grows freely; the
> core does not. The full framing is Appendix E of the bible. How to submit a
> pattern and how it gets promoted into the core — [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Record lifecycle

```
Local → Submitted → Accepted (this catalog, advisory)
                        │
                        ▼  ≥3 independent confirmations + mapping to a gap in the core
                     Candidate (staging below) → reasoned ADR by the bible owner
                        │
                        ▼  approved, ≤ once per quarter
                     Promoted (→ §4 / §4½ / §5 of the core)
   or Rejected(reason) / Deprecated(superseded)
```

Step details and roles — [`CONTRIBUTING.md`](./CONTRIBUTING.md), §2.

## Record schema

```
### P-NNN · Short name
- Context: profile · tier · stack (where observed)
- Observation: what went wrong / what worked (1–3 lines, ideally with an incident)
- Proposed rule: imperative, verifiable
- Root: which commandment / sin / DoD it maps to (or "new area")
- Evidence: link / incident / repro — or "advisory, no evidence"
- Independent confirmations: N (≥3 needed for promotion)
- Submitted by: github-handle / "anon via maintainer"
- Status: accepted | candidate | promoted(→§X) | rejected(…) | deprecated
```

**The root rule.** Every entry must have a "root" — which commandment, sin, or
DoD line it maps to (or an explicit "new area"). A pattern without a root is not
accepted (mirror of the §4½ rule: "a sin without a root may not be written").

## Field patterns

### P-000 · FORMAT SAMPLE (not a real pattern — delete on the first entry)
- Context: profile II · tier T2 · Python stack
- Observation: on an unrelated task the agent "also" updates unrelated entries in
  the lockfile, sneaking a major bump of a transitive dependency past review.
- Proposed rule: lockfile changes outside an explicit bump request — a separate
  PR; the lockfile diff within the task scope is reviewed line by line.
- Root: Commandment VII (scope), §4½ `#merge-pray`; DoD #5 (PR scope).
- Evidence: advisory, no evidence (sample).
- Independent confirmations: 0
- Submitted by: sample
- Status: rejected(format illustration, not a real observation)

## Sin candidates (staging)

Empty. Entries with status `candidate` rise here — patterns with ≥3 independent
confirmations that map to a missing sin / commandment / DoD line and are queued
for a reasoned ADR. Promotion into the core — ≤ once per quarter (in sync with the
quarterly bible review). Process — [`CONTRIBUTING.md`](./CONTRIBUTING.md), §2.
