# BDC Designer CLI Usage

`tools/bdc_designer_cli.py` exposes the restricted BDC architecture-prior recommendation logic as a command-line tool.

## Single input mode

```bash
python tools/bdc_designer_cli.py \
  --task_family predictor_dominant \
  --causal_asymmetry 0.75 \
  --dag_depth 3 \
  --dag_branching 2 \
  --budget_tier medium \
  --pretty
```

## Batch input mode

```bash
python tools/bdc_designer_cli.py \
  --input_json examples/bdc_designer_cli_examples.json \
  --pretty
```

## Save output

```bash
python tools/bdc_designer_cli.py \
  --task_family planner_augmented \
  --causal_asymmetry 0.58 \
  --dag_depth 6 \
  --dag_branching 4 \
  --budget_tier high \
  --out_json results/tmp_bdc_designer_single.json
```

## Output schema (`bdc_designer_cli_v1`)

- `schema_version`
- `input`
- `recommendation`
- `caution_flags`

`recommendation` contains:

- `effective_role_count`
- `role_weights.predictor`
- `role_weights.critic`
- `role_weights.aggregator`
- `strategy_mode`
- `confidence`

## Strategy modes

- `standalone_bdc_prior`
- `bdc_warm_start`
- `bdc_pruning`
- `full_hybrid_search`

## Notes

- Unknown families degrade confidence and increase caution flags.
- Low budget may trigger `bdc_pruning` instead of full hybrid mode.
