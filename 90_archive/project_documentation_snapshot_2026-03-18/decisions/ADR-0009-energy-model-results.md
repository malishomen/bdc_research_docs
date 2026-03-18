# ADR-0009: Phase 3 Energy Model Results and Closure

Date: 2026-03-01
Status: ACCEPTED

## Context
- Phase 3 (`TASK-1700`) introduced resource-bounded evolution (`--energy_model`) as a replacement for direct fitness penalty.
- Full standard sweep was executed in `TASK-1700-RUN`: `9` configurations (`E_0 x cost_function`) x `10` seeds = `90` runs.
- Objective was to establish stable complexity-resource dynamics while preserving learning performance.

## Evidence
- Source: `results/edp1_exp0500_energy/aggregates/energy_sweep_summary.json`.
- `0/9` configurations passed all Phase 3 success criteria.
- Mass-extinction kill criterion triggered in `5/9` configurations.
- Complexity variance remained low (`~0.0096` to `~0.0143`) with no robust complexity gradient across configurations.
- Aggregate conclusions are documented in:
  - `reports/analysis/TASK-1700-ENERGY-MODEL/TASK-1700_BRIEF_REPORT.md`
  - `AGENTS_LOG.md` entries for `TASK-1700-RUN`.

## Decision
- Phase 3 is formally closed as **FAIL at current genome scale**.
- Energy model implementation is preserved as an optional mechanism behind `--energy_model`.
- Phase 4 proceeds using the Phase 2 penalty model from ADR-0005:
  - complexity regime `B`
  - `lambda = 0.01`.

## Root Cause
- Current v2 genome parameter space is too small/narrow for effective energy-based differentiation.
- At this scale (roughly low-double-digit parameters, effective range around `7-11` in Phase 3 usage), energy pressure did not produce informative selection gradients.

## Consequences
- `evolution/energy_model.py` and related tooling remain in repository for future reuse.
- Phase 4 planning and execution are unblocked under the proven penalty regime (ADR-0005), not the Phase 3 energy regime.
- Energy model should be revisited when genome scale is materially larger (target: `> 50` parameters) or when stronger resource-sensitive signals are introduced.
- FFT diagnostics (P2) and phi-balance logging (P1) remain available as monitoring tools in subsequent phases.

## Alternatives Considered
- Keep Phase 3 as a hard gate and block Phase 4 until energy model passes.
  - Rejected: current evidence indicates model-scale mismatch, not broad project invalidation.
- Immediate redesign of energy model equations.
  - Rejected for now: would expand scope beyond closure task and requires a new R1/R2 experiment plan.

## Rollback
- Revert ADR-0009 commit:
  - `git revert <commit-hash-containing-ADR-0009>`
- Operationally restore prior roadmap gating semantics for Phase 3 only if a superseding ADR is accepted.
