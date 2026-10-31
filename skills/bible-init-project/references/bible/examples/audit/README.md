# Example: a prototype that already has a user

A synthetic documentation project: [fixture/](./fixture/), two Markdown files. No application, real users, secrets, or network calls. The stated users are task assumptions; classify the project by those assumptions, not by publication of this example.

Use the [first-audit prompt](../../README.md#first-audit) with the absolute path to `fixture/`, purpose "internal team glossary", declared level "Prototype", customers "no", and next step "merge". Read only the fixture and Bible resources. Compare the result with the [report](./report.md) and [reproduction steps](./verification.md).

Expected facts: a colleague's use means Production (§2); absence of both baseline files is a DoD #2 gap before the next merge. Missing local CI files do not prove missing hosted checks. The agent's finding count and phrasing may vary; check evidence, applicability and the minimal fix.

The change author prepared this example to make facts reproducible. It is not an independent evaluation, a quality benchmark, or an installed-skill execution record. Do not register the fixture in `registry.md`.
