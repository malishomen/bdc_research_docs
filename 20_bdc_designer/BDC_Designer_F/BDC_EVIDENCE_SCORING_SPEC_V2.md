# BDC Evidence Scoring Spec v2

## Purpose
This document defines the first evidence-aware scoring contract used by `TASK-7480`.

## Scoring components
For each tested variant, v2 computes:
- `performance_score`
- `coordination_penalty`
- `total_score = performance_score - coordination_penalty`

## Performance score inputs
Current deterministic inputs:
- `docs_improved_pct`
- `naturalness_delta`
- `runtime_min`
- `cost_usd`
- `guardian_intervention_rate` when present

## Coordination penalty inputs
Current deterministic inputs:
- role count
- ontology coordination cost priors
- role inflation above the smallest tested role count

## Rejection reason rules
The scorer emits rejection reasons when present, including:
- `negative_naturalness_delta`
- `cost_inflation`
- `role_inflation_penalty`
- `harmonizer_requires_positive_evidence`

## Hard expectation for TextAI_Auto
The scorer must rank:
- Variant D above Variant E
- `guardian` as positive contribution relative to planner+editor alone
- `harmonizer` as non-default because over-segmentation failed

## Boundary
This scorer is deterministic and evidence-aware, but it is not yet the final operator-facing strategy or confidence layer.
