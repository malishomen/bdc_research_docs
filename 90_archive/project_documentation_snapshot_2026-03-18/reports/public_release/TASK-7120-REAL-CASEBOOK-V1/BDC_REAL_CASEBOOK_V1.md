# BDC Real Casebook v1

## Purpose
This casebook demonstrates how Restricted BDC v1 operates across multiple real workflow patterns.

## Flagship Case
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
- Role weights: `pred

## Additional Validated Cases
- `rt_001` planner-executor-checker: time win=True, quality win=True, cost win=True, wins=3
- `rt_002` proposer-verifier-judge: time win=True, quality win=True, cost win=True, wins=3
- `rt_003` retriever-reasoner-critic: time win=True, quality win=True, cost win=True, wins=3
- `rt_004` content-draft-review: time win=True, quality win=True, cost win=True, wins=3
- `rt_005` lead-triage-proposal-review: time win=True, quality win=True, cost win=True, wins=3

## Workflow Pattern Matrix
- `planner-executor-checker`: cases=1, avg_wins=3.0, majority_success_rate=1.0
- `proposer-verifier-judge`: cases=1, avg_wins=3.0, majority_success_rate=1.0
- `retriever-reasoner-critic`: cases=1, avg_wins=3.0, majority_success_rate=1.0
- `content-draft-review`: cases=1, avg_wins=3.0, majority_success_rate=1.0
- `lead-triage-proposal-review`: cases=1, avg_wins=3.0, majority_success_rate=1.0

## Scope Boundaries
The casebook presents restricted, validated architecture-guidance value.
It does not claim universal optimization behavior.
