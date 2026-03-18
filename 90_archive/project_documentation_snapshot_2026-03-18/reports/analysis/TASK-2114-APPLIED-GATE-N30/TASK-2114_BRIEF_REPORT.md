# TASK-2114 BRIEF REPORT

## Scope
- Conditional applied gate run `N=30` (GPU+CPU), allowed only if TASK-2113 passes both pilots.

## Status
- **BLOCKED / NOT EXECUTED** (formal stop by governance).

## Stop-Rule Evidence
- From TASK-2113 diagnostic rerun:
  - `gpu.verdict_pass = False`
  - `cpu.verdict_pass = True`
- Gate precondition requires both `True` under ADR-0013/ADR-0014.

## Verification (L0)
- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/exp_0700_applied_v3/diagnostic/aggregates/exp0700_diagnostic_summary.json').read_text(encoding='utf-8')); print(d['gpu']['verdict_pass'], d['cpu']['verdict_pass'], d['gpu']['stats']['ci95_low'])"`
- Result: PASS
- Output summary: `False True -0.17206888915672247`.

## Artifacts
- `reports/analysis/TASK-2114-APPLIED-GATE-N30/TASK-2114_BRIEF_REPORT.md`

## Risks / Limitations
- No gate `N=30` artifacts are produced in this task by design.
- Next attempt requires new iteration scope while preserving ADR-0013 criteria.

## Rollback
- Not applicable (no run/code changes executed in this task).
