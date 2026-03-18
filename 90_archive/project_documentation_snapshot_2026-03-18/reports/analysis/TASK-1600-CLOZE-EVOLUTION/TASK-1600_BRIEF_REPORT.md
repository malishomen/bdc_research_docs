# TASK-1600 BRIEF REPORT

## Scope
- Implemented Phase 2 bridge experiment (`exp_0400`) as a separate module `evolution/cloze_symbolic`.
- Added canonical ClozeGenome v0 specification and deterministic wiki subset protocol.
- Preserved constraints:
  - no changes to `evolution/edp1_symbolic/*` (hidden_rule line untouched),
  - no changes to wiki LM training scripts.
- Used canonical complexity regime `B` (ADR-0005) directly in cloze module.

## Changes
- New docs:
  - `docs/CLOZE_GENOME_SPEC.md`
  - `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md`
- New module:
  - `evolution/cloze_symbolic/__init__.py`
  - `evolution/cloze_symbolic/genome.py`
  - `evolution/cloze_symbolic/task.py`
  - `evolution/cloze_symbolic/evaluate.py`
  - `evolution/cloze_symbolic/mutate.py`
  - `evolution/cloze_symbolic/select.py`
  - `evolution/cloze_symbolic/run_generations.py`
- New runner:
  - `scripts/edp1/run_cloze_exp_0400.py`
- Updated protocol:
  - `docs/REMOTE_COMPUTE_PROTOCOL.md` (exp_0400 queen smoke example).

## Verification (L0)
- Command: `python scripts/edp1/run_cloze_exp_0400.py --smoke --seeds 2 --generations 5 --population 20 --out_root results/.tmp_task1600_cloze_smoke`
  - Result: PASS
  - Output summary:
    - both seed runs completed,
    - `metrics.csv` + `summary.json` created per seed,
    - aggregate summary created at `results/.tmp_task1600_cloze_smoke/aggregates/summary.json`.
- Command: `Get-Content results/.tmp_task1600_cloze_smoke/seed_1337/metrics.csv -TotalCount 3`
  - Result: PASS
  - Output summary: required columns present (`max/mean_accuracy`, `complexity`, `penalty`, `fitness`).
- Command: `Get-Content results/.tmp_task1600_cloze_smoke/seed_1337/summary.json`
  - Result: PASS
  - Output summary: contains `complexity_regime="B"`, baseline accuracies, stream seeds, final metrics.
- Command: `Get-ChildItem evolution/cloze_symbolic/*.py | ForEach-Object { python -m py_compile $_.FullName }; python -m py_compile scripts/edp1/run_cloze_exp_0400.py`
  - Result: PASS
  - Output summary: no syntax errors.
- Command: `git diff --name-only`
  - Result: PASS
  - Output summary: no modifications to hidden_rule runtime module and no changes to wiki LM training stack.

## Baseline vs Evolution (smoke)
- Aggregate from `results/.tmp_task1600_cloze_smoke/aggregates/summary.json`:
  - `final_max_accuracy_mean = 0.026509`
  - `best_baseline_accuracy_mean = 0.161516`
  - `meets_5pct_gain_flag = false`
- Interpretation:
  - Functional pipeline is working.
  - Success criterion ">=5% absolute over best baseline" is not met on smoke.
  - Full run (`N=30, G=50, P=100`) is required for final Phase 2 gate decision.

## Artifacts
- `docs/CLOZE_GENOME_SPEC.md` — canonical ClozeGenome v0 spec.
- `evolution/cloze_symbolic/*` — new exp_0400 evolution module.
- `scripts/edp1/run_cloze_exp_0400.py` — multi-seed runner with aggregation.
- `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md` — experiment-level interpretation.
- `reports/analysis/TASK-1600-CLOZE-EVOLUTION/TASK-1600_BRIEF_REPORT.md` — this report.
- Runtime-only (not committed):
  - `results/.tmp_task1600_cloze_smoke/`.

## Risks / Limitations
- Current scientific evidence is smoke-only (`N=2,G=5,P=20`), not canonical full-scale.
- Strong bigram baseline dominates evolved accuracy in smoke; genome representation may need refinement if this persists at full N=30.
- Results should not be used to claim Phase 2 PASS until full-run confidence interval criteria are evaluated.

## Follow-up Note (TASK-1601)
- Additional R0 diagnostics were executed in `TASK-1601-CLOZE-DIAGNOSTIC-R0` and captured in:
  - `reports/analysis/TASK-1601-CLOZE-DIAGNOSTIC/TASK-1601_BRIEF_REPORT.md`
  - `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md` (Diagnostic Addendum)
- Summary: ClozeGenome v0 can represent frequency baseline exactly (no representational defect for that baseline), but search/task gap vs bigram baseline remains the main limiter.

## Rollback
- `git revert <TASK-1600-commit-hash>`
