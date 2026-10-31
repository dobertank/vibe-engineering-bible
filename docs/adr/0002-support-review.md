# ADR 0002. Review support instead of retiring projects by commit age

- **Status:** accepted by the owner on 2026-10-31; local implementation, not published.
- **Date:** 2026-10-31.
- **Process context:** the owner approved a narrow K05 change to §4 II and the related Production branch of `#zombie`. This is an owner decision before the first registered adoption, not promotion of a field pattern; the general Appendix E gate is unchanged.
- **Trigger:** missing commits alone do not establish missing support or justify automatic retirement of a working project.

## Decision

1. In Production, 90 and 180 days without commits are signals to check ownership, support and security. They are not automatic deadlines for `deprecated`/`archived` or proof of abandonment. The owner decides status and retirement based on that review.
2. The Production branch of `#zombie` concerns continued use with confirmed absence of ownership and support, or past a retirement date explicitly set by the owner. Commit age or an unperformed review alone does not establish this sin; do not assume a retirement decision without evidence.
3. Synchronize the canon and actual repetitions. Templates list lifecycle statuses without automatic deadlines and need no change. Introduce no new deadlines, artifacts or gates.

## Consequences

A supported project can remain active without recent commits. Unknown support needs verification rather than an automatic label. Explicit owner retirement decisions and their dates remain in force.

## Deliberately not changed

The Prototype ≤30-day rule, Production transition events, other ownership and security requirements, consequences, two covenants / eight commandments / thirteen sins, auto-merge, customer requirements, solo checks, data controls, K07, §5 #41 and future Appendix E changes. ADR 0001 remains the history of a separate decision; this ADR makes no license or publication choice.
