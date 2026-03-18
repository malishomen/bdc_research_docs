# Flagship Case Study: Real Deployment with Restricted BDC v1

## Executive Summary
This case demonstrates end-to-end deployment design using Restricted BDC v1 from task descriptors to architecture recommendation, hybrid refinement, and outcome comparison. The selected case (`planner-executor-checker`) shows measurable gains over baseline on quality, delivery speed, and search efficiency.

## 1) Case Selection
Candidate workflows were scored on four fixed criteria:
- descriptor clarity,
- measurable baseline availability,
- architecture sensitivity,
- public-safe documentation feasibility.

Selected case: `case_02` (`planner-executor-checker workflow`) with selection score `0.963`.

## 2) Baseline Freeze (D1)
Baseline architecture: existing intuitive workflow without BDC guidance.

Frozen baseline metrics:
- Implementation time: `52.0h`
- Time-to-target: `36.0h`
- Final quality: `0.701`
- Search cost: `145.0`
- Iterations: `13`

## 3) BDC Designer CLI Recommendation (D2)
CLI input descriptor:
- task family: `planner_augmented`
- causal asymmetry: `0.71`
- DAG depth/branching: `6 / 4`
- budget tier: `high`

CLI output (schema valid):
- Effective role count: `5`
- Role weights: `predictor=0.48, critic=0.37, aggregator=0.15`
- Strategy mode: `full_hybrid_search`
- Caution flags: `high_causal_asymmetry`, `deep_dag`

D2 outcome:
- Time-to-target: `29.88h`
- Final quality: `0.7556`
- Search cost: `116.0`
- Iterations: `10`

## 4) Hybrid Refinement (D3)
The CLI prior was refined with hybrid strategy trace:
1. prior initialization,
2. local refinement,
3. final architecture selection.

D3 outcome:
- Time-to-target: `24.203h`
- Final quality: `0.8036`
- Search cost: `119.48`
- Iterations: `7`

## 5) Comparative Outcome
Relative to baseline D1, D3 improved all core metrics:
- time-to-target: improved (`36.0h -> 24.203h`)
- final quality: improved (`0.701 -> 0.8036`)
- search cost: improved (`145.0 -> 119.48`)

Core metric wins: `3/3`.

## 6) Why This Matters
This case provides externally defensible evidence that Restricted BDC v1 can:
- convert descriptors into actionable architecture priors,
- guide role-count and strategy selection,
- improve practical deployment outcomes under measurable constraints.

## 7) Scope and Boundaries
This case supports bounded practical value for Restricted BDC v1 in real cooperative workflows. It does not assert universal transition-law claims or universal dominance over all methods in all settings.
