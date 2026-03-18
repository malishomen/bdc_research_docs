# Experiments Documentation Layer

This directory stores detailed, concept-level descriptions for key roadmap experiments.

These documents complement task-level reports in `reports/analysis/TASK-*` and do not replace them.

## Naming Standard

- Format: `EXP-<code>_<SHORT-NAME>_<YYYY-MM-DD>.md`
- Example: `EXP-0300_COMPLEXITY_REGIME_SWEEP_2026-02-27.md`

## Required Structure

Each EXP document must use this structure:

1. `# EXP-XXXX: Title (YYYY-MM-DD)`
2. `## Background`
3. `## Hypotheses & Relation to CANON/ADR`
4. `## Protocol` (N/G/P, configs, scripts/commands)
5. `## Results` (tables + key metrics)
6. `## Interpretation`
7. `## Impact on roadmap`
8. `## Links to TASK reports + ADR`

## Scope Rule

- Create EXP documents only for key experiments:
  - roadmap phase gates,
  - major R2 changes,
  - experiments that drive architectural/governance decisions.
- Routine or local smoke runs remain in task reports only.
