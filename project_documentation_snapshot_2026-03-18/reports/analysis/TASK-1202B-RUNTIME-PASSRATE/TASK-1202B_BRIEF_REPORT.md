# TASK-1202B BRIEF REPORT

## Scope
- Извлечен runtime-only pass_rate по canonical source `summary.json.kill_status`.
- Без пересчета kill-criteria.

## Method (L0)
- Источники:
  - `results/edp1_exp0200_v2/seeds/*/summary.json`
  - `results/edp1_exp0200_speciation/seeds/*/summary.json`
- Учет:
  - `runs_pass` iff `kill_status.status == "PASS"`
  - `runs_fail` iff `kill_status.status == "FAIL"`
  - `pass_rate = runs_pass / runs_total`

## Results
- v2:
  - `runs_total = 30`
  - `runs_pass = 30`
  - `runs_fail = 0`
  - `pass_rate = 1.0`
- v1 baseline:
  - `runs_total = 30`
  - `runs_pass = 30`
  - `runs_fail = 0`
  - `pass_rate = 1.0`

## Conclusion
- Under canonical runtime criteria (`summary.json.kill_status`), v2 does **not** outperform v1 by pass_rate.
- Both are equal: `1.0 vs 1.0`.

## Verification (L0)
- `Get-ChildItem results/edp1_exp0200_v2/seeds -Directory | Measure-Object` -> 30
- `Get-ChildItem results/edp1_exp0200_speciation/seeds -Directory | Measure-Object` -> 30
- JSON extraction script completed without missing summaries.

## Artifacts
- `reports/analysis/TASK-1202B-RUNTIME-PASSRATE/runtime_passrate_v2.json`
- `reports/analysis/TASK-1202B-RUNTIME-PASSRATE/runtime_passrate_v1.json`
- `reports/analysis/TASK-1202B-RUNTIME-PASSRATE/TASK-1202B_BRIEF_REPORT.md`

## Risks / Limitations
- This report intentionally ignores post-hoc aggregate kill recalculation.
- Interpretation is strictly runtime-canonical only.
