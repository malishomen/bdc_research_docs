# Phase-4 GPU Profile Search Space (Predeclared)

## Scope
- Track: Applied (parallel to scientific Phase-4 verdict).
- Purpose: remove cherry-picking risk by fixing admissible GPU optimization space before final closure decisions.

## Predeclared Space
- `batch_size in {4, 8, 16}`
- `steps in {80, 120}`
- `lr in {1e-5, 3e-5, 1e-4}`
- `AMP in {on}`
- `fp32_critical in {on}`
- `clip in {1}`

## Seed Policy
- `random_seed_range = [1337..1366]`

## Selected v4 Reference Profile
- `profile_id: gpu_profile_v4_reference`
- `selected_from_predeclared_space: true`
- `parameters:` `batch_size=8`, `steps=120`, `lr=3e-5`, `AMP=on`, `fp32_critical=on`, `clip=1`.

## Governance Notes
- Hard/Advisory fairness split is governed by ADR-0015.
- Selection from this space does not alter ADR-0013 pass/fail thresholds.
