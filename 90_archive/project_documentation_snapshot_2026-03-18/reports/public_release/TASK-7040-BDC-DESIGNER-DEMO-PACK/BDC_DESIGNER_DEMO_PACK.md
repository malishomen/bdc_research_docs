# BDC Designer Demo Pack

## Demo Goal
Show BDC Designer core workflow in under 5 minutes with reproducible examples and measurable before/after value.

## Demo Narrative Sequence
1. Introduce restricted scope and what BDC does/does not claim.
2. Run one-command example 1 (simple family).
3. Run one-command example 2 (higher asymmetry).
4. Run one-command example 3 (deep DAG + caution flags).
5. Show flagship case baseline vs hybrid outcome table.

## Canned Examples
- `s1`: demo_case_1 -> `python tools/bdc_designer_cli.py --task_family predictor_dominant --causal_asymmetry 0.75 --dag_depth 3 --dag_branching 2 --budget_tier medium --pretty`
- `s2`: demo_case_2 -> `python tools/bdc_designer_cli.py --task_family critic_dominant --causal_asymmetry 0.7 --dag_depth 4 --dag_branching 2 --budget_tier medium --pretty`
- `s3`: demo_case_3 -> `python tools/bdc_designer_cli.py --task_family aggregator_dominant --causal_asymmetry 0.65 --dag_depth 5 --dag_branching 3 --budget_tier high --pretty`

## Output Snapshots
- `s1`: strategy=`bdc_pruning`, role_count=`5`, caution=`hard_failure_family|high_causal_asymmetry`
- `s2`: strategy=`bdc_pruning`, role_count=`5`, caution=`hard_failure_family|high_causal_asymmetry`
- `s3`: strategy=`bdc_pruning`, role_count=`5`, caution=`hard_failure_family`

## Flagship Before/After
- `D1` Current baseline architecture: time_to_target=36.0, quality=0.701, cost=145.0
- `D2` BDC Designer CLI recommendation only: time_to_target=29.88, quality=0.7556, cost=116.0
- `D3` BDC CLI + hybrid refinement: time_to_target=24.203, quality=0.8036, cost=119.48

## Reproducibility
All demo commands and expected snapshots are defined in manifests under `results/demo_pack/`.
