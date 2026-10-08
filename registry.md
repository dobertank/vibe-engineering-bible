# Adoption registry

> **One registry — two ways to use it.** In the public upstream repo it is an
> opt-in list of adopters. In an organization's internal copy of the repo it is an
> index of projects where the bible is actually applied: init, audit, review,
> gates. It is not an inventory of all repositories: a service catalog, a wiki, or a
> separate table exists for that.
>
> **Registering in the public repo = disclosure.** The PR is signed by your GitHub
> account, it is visible in the fork network, and the commit's author email often
> carries a corporate domain. So confidential projects **do not register in the
> public upstream — and that is normal**: absence from the list ≠ non-use. The list
> deliberately undercounts.
>
> Need an aggregate entry without disclosing identity? That goes through a private
> channel (not via a PR), see [`CONTRIBUTING.md`](./CONTRIBUTING.md), §4. In v1 the
> channel itself is not built yet — message the maintainer, the door is open.

## How to get into the registry

Optional. The procedure is **the agent prepares, a human confirms** (a PR to
someone else's repo is an outward action under Commandment VI of the bible): the
agent prepares the row and a draft PR, you review and open the PR yourself. Details
— [`CONTRIBUTING.md`](./CONTRIBUTING.md), §3.

Add a project after its first real application (init, audit, review), not in
advance. The row format and field values —
[`templates/project-registry-entry.md`](./templates/project-registry-entry.md).
Only **Project** and **Date** are required; in an internal copy — also **Owner**
and **Mode**.

## Projects

| Project / adopter | Repo (if public) | Owner / contact | Profile | Tier | Mode | Baseline | Last audit | Status | Next action | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| _Example Org / project_ | _github.com/example/repo_ | _@handle_ | _II_ | _T2_ | _audit_ | _CLAUDE.md_ | _2026-06-21_ | _advisory_ | _enable deterministic checks in CI_ | _2026-06-21_ |

<!-- The row above is a sample. Delete it when adding the first real entry. -->

## Maintenance rules

- Update the row after an audit, a change of risk tier, enabling a gate, or archiving.
- Do not keep secrets, internal links with sensitive data, or long reports here.
  Details live in audit reports; this is only an index.
- If a project became the source of a change to the bible, say so in a proposal per
  [`templates/bible-change-proposal.md`](./templates/bible-change-proposal.md), not
  in this table.
