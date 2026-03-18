## ADR-0002: BEP-1 scope gating (non-core)

Date: 2026-01-07

## Context
BEP-1 defines extensions (ledger + digital panspermia) that are not part of the core
TRL-3 Paramecium MVP. Without explicit gating, there is risk of scope creep.

## Decision
- BEP-1 is non-core and MUST NOT be included in TRL-3 Paramecium scope.
- BEP-1 work can start only after TRL-3 Definition of Done is closed OR via a
  dedicated epic with its own kill-criteria for iteration speed and determinism.

## Consequences
- TRL-3 remains focused on core qcore/agent/env/evolution validation.
- Any BEP-1 work requires a separate decision and kill-criteria before execution.

