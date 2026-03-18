# TASK-2006 BRIEF REPORT

## Scope
- Conditional `N=30` applied gate run (both pilots) under ADR-0013.

## Result
- **NOT EXECUTED** by governance.

## Reason
- ADR-0013 prerequisite was not met:
  - Pilot A diagnostic gate = FAIL (`CI95_low(delta_gpu) < 0`, `stability_fail_rate=0.6`)
  - Pilot B diagnostic gate = PASS
- Rule requires both pilots PASS before `N=30`.

## Verification (L0)
- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json').read_text(encoding='utf-8')); print(d['gpu']['verdict_pass'], d['cpu']['verdict_pass'])"`
- Result: PASS (prints `False True`)

## Artifacts
- `reports/analysis/TASK-2006-APPLIED-GATE-N30/TASK-2006_BRIEF_REPORT.md`

## Risks / Limitations
- Applied gate remains incomplete for this iteration by design (stop-rule compliance).

## Rollback
- `git revert <commit-hash-containing-task-2006>`
