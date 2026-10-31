# ADR 0001. Correct evidence and clarify solo checks and data controls

- **Status:** accepted by the owner on 2026-10-31; local implementation, not published.
- **Date:** 2026-10-31.
- **Process context:** affects §3, §4 IV/VI/VII, §4½ `#tautological`/`#sycophancy`, §5 #11, §9, and Appendix D/E. The owner authorized corrections to errors and inconsistencies before the first registered adoption. No field confirmations were collected; this is an owner decision, not promotion of a new pattern. The general Appendix E gate is unchanged.
- **Trigger:** incorrect Haroon interpretation, a blanket two-person DoD inconsistent with solo use, a mandatory gateway inconsistent with small-team adoption, and unsupported enforcement/test-generation rationales.

## Decisions

1. **Evidence.** Haroon et al. reports that more than 99% of tests failing on a semantically changed program pass on the original. This is not a mutation-survival rate. Meta ACH compares mutation-guided and coverage-guided test generation, not independent and same-author generation. Correct Appendix D and remove the unsupported rationales; keep separate-context tests and mutation testing as author policy.
2. **Human check.** In teams, the person assigning the task does not approve the agent's PR. Solo Production without customers permits a human author check, described honestly as non-independent. Sensitive data alone does not exclude this check; mandatory human confirmation for actions involving it and data controls still apply. Preserve all customer requirements and the exact §3 auto-merge exception.
3. **Data controls.** New access requires verifiable access and data-flow restrictions. A gateway is an optional implementation. Record permitted data/systems, destinations, enforcement and verification in baseline §3.1. Existing adopter policies remain binding.
4. **Enforcement claims.** Hooks, settings and CI enforce specific boundaries under checked prerequisites; their presence is not an absolute safety guarantee. The lethal trifecta creates exfiltration risk, not evidence of an inevitable or completed leak. Keep the required walls and gates.

## Consequences

Author checks support solo adoption without pretending to provide an independent opinion. AI review still cannot replace a required human check. An audit checks controls and evidence; missing a gateway alone is not a violation, and baseline text alone proves no enforcement.

Synchronize the public canon, baseline, init/audit/review playbooks, audit format and usage instructions. Two covenants, eight commandments and thirteen sins remain. Sources and their limits are in Appendix D.

## Deliberately not changed

Auto-merge eligibility, the customer ban on auto-merge, sensitive-data confirmation, customer DoD, Prototype boundaries, §5 #41 and its NOW status, calibration thresholds, lifecycle deadlines and future Appendix E promotion requirements.
