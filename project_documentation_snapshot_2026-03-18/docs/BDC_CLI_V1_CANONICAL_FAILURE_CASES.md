# BDC CLI v1 Canonical Failure Cases

## Purpose
This document freezes the known failure cases that must remain available as regression and calibration gates during BDC CLI v2 development.

## Mandatory failure cases

### 1. TextAI_Auto
- Case type: evidence-rich text workflow architecture decision
- Why it matters: contains tested architecture variants and a clear evidence-aware winner
- v1 failure:
  - over-recommends `5` roles
  - over-recommends `full_hybrid_search`
- Expected v2 correction:
  - stop defaulting to inflated role count when tested role inflation already failed
  - stop defaulting to full hybrid search when a strong architecture winner exists

### 2. Unknown family fallback
- Case type: descriptor with family outside known rulebook
- Why it matters: exposes how v1 behaves when priors are weak
- v1 behavior:
  - defaults to generic role weights
  - falls back to pruning or hybrid logic with low confidence
- Risk:
  - acceptable as low-confidence fallback
  - unacceptable if later systems inherit this without explicit insufficiency labeling

### 3. Deep and wide planner-augmented workflow
- Case type: planner-augmented descriptor with high asymmetry and high DAG complexity
- v1 behavior:
  - still recommends `5` roles and `full_hybrid_search`
- Risk:
  - complexity warnings exist, but no evidence-aware mechanism prevents over-search

## Frozen benchmark fixture set
The committed v1 baseline fixture set contains these case IDs:
- `predictor_baseline`
- `symmetric_low_budget`
- `planner_augmented_deep`
- `multi_stage_high`
- `unknown_low_budget`
- `textai_auto_proxy`

## Rule for v2
A v2 release is not ready if:
- it regresses on the frozen v1 fixture mechanics unexpectedly, or
- it still reproduces the TextAI_Auto failure mode as if it were the correct answer.
