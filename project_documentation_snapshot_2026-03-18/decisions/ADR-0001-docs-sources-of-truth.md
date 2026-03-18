## ADR-0001: Docs sources of truth

Date: 2026-01-07

## Context
Documentation included duplicated canonical rules inside project reference documents,
which risks divergence and ambiguity. The project requires a single source of truth.

## Decision
Normative (single source of truth) files are:
- `CANON.md`
- `SEMANTICS.md`
- `SEED_POLICY.md`
- `KILL_CRITERIA.yaml`
- `REPRODUCIBILITY.md`
- `VERSIONING.md`

Reference-only files live under `docs/project/` and must not duplicate canon content.
If canon text is needed in a reference file, it is replaced with a link to `CANON.md`.

## Consequences
- Canonical rules are maintained once, in the root.
- Reference documents remain archival sources and can be updated without redefining norms.
- Any change to normative files requires an ADR or experiment spec update as applicable.

