# Deterministic Reproducibility Check

## Scope
- Two consecutive reruns for seeds: 1339, 1347, 1364.
- Tolerance: `1e-6` for delta and loss traces.

## Results
| Seed | delta_run1 | delta_run2 | abs_diff(delta) | max_diff(train_loss_trace) | max_diff(val_loss_trace) | PASS |
|---:|---:|---:|---:|---:|---:|:---:|
| 1339 | -0.307258605957 | -0.307258605957 | 0.000000000000 | 0.000000000000 | 0.000000000000 | TRUE |
| 1347 | 1.880709330241 | 1.880709330241 | 0.000000000000 | 0.000000000000 | 0.000000000000 | TRUE |
| 1364 | 0.904759724935 | 0.904759724935 | 0.000000000000 | 0.000000000000 | 0.000000000000 | TRUE |

## Verdict
- Overall PASS: True
- Tolerance: 1e-06
