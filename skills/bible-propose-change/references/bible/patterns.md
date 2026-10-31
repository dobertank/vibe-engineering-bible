# Field pattern catalog

Advisory catalog, not canon: `accepted ≠ canonical`. The record lifecycle, the threshold, and the gate into the core — Appendix E of the bible; how to submit — [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Record schema

```
### P-NNN · Short name
- Context: team size · level · stack (where observed)
- Observation: what went wrong / what worked (1–3 lines, ideally with an incident)
- Proposed rule: imperative, verifiable
- Root: which commandment / sin / DoD it maps to (or "new area") — required, an entry without a root is not accepted
- Evidence: link / incident / repro — or "advisory, no evidence"
- Independent confirmations: N
- Submitted by: github-handle / "anon via maintainer"
- Status: submitted | accepted | candidate | promoted(→§X) | rejected(…) | deprecated
```

`submitted` — filed, not yet deduplicated against the core and the catalog; `deprecated` — outdated or already enforced by the environment
(agent settings, hooks, CI), moved at the quarterly review.

## Field patterns

Empty so far. Format — "Record schema" above.

## Sin candidates (staging)

- **Queue** — contenders that have not yet reached the Appendix E threshold (`submitted` / `accepted`). These are not sins: a reviewer
  does not use their shortcodes to reject a merge — only as a reference to the catalog entry.
- **Candidate** — reached the threshold and map to a missing sin / commandment / DoD line; await a reasoned ADR by the owner
  group, the class (mortal / venial) is decided by the ADR.

### Queue

#### P-001 · Unvetted agent skill — contender `#unvetted-skill`
- Context: all team sizes · Production · agent clients that support skills, plugins, MCP
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
- Submitted by: owner group, while preparing Bible 2.0
- Status: submitted

#### P-002 · Rule only in text — contender `#rules-in-prompt`
- Context: all team sizes · Production
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
- Submitted by: owner group, while preparing Bible 2.0
- Status: submitted

#### P-003 · Closed without an outcome — contender `#metric-free`
- Context: all team sizes · Production
- Observation: work is closed on PR merge; the expected outcome in the product is
  neither named in the spec nor verified after rollout.
- Proposed rule: the outcome is named in the spec before code; the task is closed
  when the outcome is confirmed (or explicitly refuted), not when the code is merged.
- Root: Commandment VIII (Done means proven); §6 (the loop, the "Outcome" step).
- Evidence: advisory, no field evidence; grounded in the §6 loop and DORA 2025
  (speed with AI grows together with instability).
- Independent confirmations: 0
- Submitted by: owner group, while preparing Bible 2.0
- Status: submitted

### Candidate

Empty.
