# Field pattern catalog

> **An advisory catalog, not canon.** This is where patterns found in practice
> land — by teams that use the "Vibe Engineering Bible": what systematically
> breaks, or conversely reliably works, when working with AI agents. Entries here
> are observations and proposals, not core rules.
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
                     Candidate (staging below) → reasoned ADR by the owner group (docs/adr/)
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
- Status: submitted | accepted | candidate | promoted(→§X) | rejected(…) | deprecated
```

`submitted` — the entry has been filed but has not yet been deduplicated against
the core and the catalog and has not gathered confirmations.

**The root rule.** Every entry must have a "root" — which commandment, sin, or
DoD line it maps to (or an explicit "new area"). A pattern without a root is not
accepted (mirror of the §4½ rule: "a sin without a root may not be written").

**The removal rule.** The quarterly review moves to `deprecated` the entries that
are outdated or already enforced by the environment (agent settings, hooks, CI).

## Field patterns

Empty so far. Format — "Record schema" above.

## Sin candidates (staging)

Two levels:

- **Queue** — contenders for sins that have fewer than three confirmations so far
  (`submitted` / `accepted`). These are not sins: a reviewer does not use their
  shortcodes to reject a merge — only as a reference to the catalog entry.
- **Candidate** — entries with ≥3 independent confirmations that map to a missing
  sin / commandment / DoD line and are queued for a reasoned ADR by the owner
  group. The class (mortal / venial) is decided by the ADR. Promotion into the core
  — ≤ once per quarter (in sync with the quarterly bible review). Process —
  [`CONTRIBUTING.md`](./CONTRIBUTING.md), §2.

### Queue

#### P-001 · Unvetted agent skill — contender `#unvetted-skill`
- Context: all profiles · T1–T3 · agent clients that support skills, plugins, MCP
- Observation: a skill, plugin, or MCP server is connected to the repo or to the
  agent's environment without review, an owner, or version pinning — from a
  marketplace or via a link.
- Proposed rule: skills, plugins, MCP servers, hooks, and `AGENTS.md` are under
  owners (CODEOWNERS), with review and version pinning; external ones — only
  through an internal catalog or mirror.
- Root: Commandment V (agent configuration is a dependency too); adjacent — §4½ `#promptable`, `#trifecta`.
- Evidence: Liu et al., *Agent Skills in the Wild*, arXiv 2601.10338 — 26.1% of
  marketplace skills contain vulnerabilities, skills with scripts are 2.12 times
  riskier; OWASP Top 10 for Agentic Applications 2026. No field confirmations from
  adopters yet.
- Independent confirmations: 0
- Submitted by: owner group, Bible 2.0 (`docs/adr/0001-bible-2.0.md`)
- Status: submitted

#### P-002 · Rule only in text — contender `#rules-in-prompt`
- Context: all profiles · T1–T3
- Observation: a mandatory rule (secrets, forbidden commands, pre-merge checks)
  lives only in `CLAUDE.md`/`AGENTS.md` or in a prompt, without enforcement in
  agent settings, hooks, or CI.
- Proposed rule: a rule that a machine can check is enforced by the environment;
  the text for the agent holds only the non-obvious.
- Root: Commandment IV (The law lives in the environment); §8 (context files).
- Evidence: ETH, arXiv 2602.11988 — context files on average do not raise task
  success and make the work more than 20% more expensive; Anthropic, *Claude Code
  sandboxing*. No field confirmations from adopters yet.
- Independent confirmations: 0
- Submitted by: owner group, Bible 2.0 (`docs/adr/0001-bible-2.0.md`)
- Status: submitted

#### P-003 · Closed without an outcome — contender `#metric-free`
- Context: all profiles · T2–T3
- Observation: work is closed on PR merge; the expected outcome in the product is
  neither named in the spec nor verified after rollout.
- Proposed rule: the outcome is named in the spec before code; the task is closed
  when the outcome is confirmed (or explicitly refuted), not when the code is merged.
- Root: Commandment VIII (Done means proven); §6 (the loop, the "Outcome" step).
- Evidence: advisory, no field evidence; grounded in the §6 loop and DORA 2025
  (speed with AI grows together with instability).
- Independent confirmations: 0
- Submitted by: owner group, Bible 2.0 (`docs/adr/0001-bible-2.0.md`)
- Status: submitted

### Candidate

Empty.
