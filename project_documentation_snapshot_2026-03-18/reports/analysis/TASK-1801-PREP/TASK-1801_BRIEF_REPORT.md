# TASK-1801 BRIEF REPORT

## Scope
- Prepare Phase 4 MVP foundations without changing cloze-only execution semantics.
- Add deterministic entity overlay in cloze dataset builder.
- Add collective fitness core (Scheme S1) as reusable module.
- Add focused tests for overlay determinism, entity scoring, and collective aggregation.

## Changes
- Updated `evolution/cloze_symbolic/task.py`:
  - Added case-preserving tokenization path (`tokenize_case_preserving`) while preserving existing lowercase tokenization (`tokenize`).
  - Added deterministic entity heuristic (`is_entity_token`) and entity overlay generation in `build_cloze_task`.
  - Extended `ClozeSample` with `target_is_entity` (default-safe).
  - Extended `ClozeTaskData` with `candidate_is_entity` and `target_is_entity` overlay fields.
- Added `evolution/micro_tasks/entity.py`:
  - `is_entity_prediction(...)`
  - `entity_accuracy_from_predictions(...)`
- Added `evolution/micro_tasks/__init__.py` exports.
- Added `evolution/collective_fitness.py`:
  - `weighted_mean(...)`
  - `individual_fitness_s1(...)`
  - `collective_fitness_s1(...)`
  - `population_collective_fitness_s1(...)`
- Added tests:
  - `tests/test_phase4_entity_overlay.py`
  - `tests/test_phase4_collective_fitness.py`

## Verification (L0)
- Command: `git status --short`
- Result: PASS
- Output summary: changes only in intended Phase 4 prep files.

- Command: `python -m py_compile evolution/cloze_symbolic/task.py evolution/micro_tasks/entity.py evolution/collective_fitness.py`
- Result: PASS
- Output summary: compilation successful, no syntax errors.

- Command: `pytest -q tests/test_phase4_entity_overlay.py tests/test_phase4_collective_fitness.py`
- Result: PASS
- Output summary: `7 passed in 0.11s`.

- Command: `python -m evolution.cloze_symbolic.run_generations --dry_run --genome_version v2 --use_skip_bigram --seed 1337 --out_dir results/tmp_task1801_dryrun`
- Result: PASS
- Output summary: summary written; dry-run completed with no regression/exceptions.

- Command: `git diff --name-only`
- Result: PASS
- Output summary: tracked diff limited to `evolution/cloze_symbolic/task.py`.

## Artifacts
- `evolution/cloze_symbolic/task.py` - deterministic entity overlay added with cloze backcompat preserved.
- `evolution/micro_tasks/entity.py` - entity micro-task accuracy helpers.
- `evolution/micro_tasks/__init__.py` - module exports.
- `evolution/collective_fitness.py` - Scheme S1 collective/individual fitness core.
- `tests/test_phase4_entity_overlay.py` - overlay determinism + backcompat tests.
- `tests/test_phase4_collective_fitness.py` - S1 aggregation tests.
- `reports/analysis/TASK-1801-PREP/TASK-1801_BRIEF_REPORT.md` - this report.

## Risks / Limitations
- Entity labeling heuristic is intentionally simple (`TitleCase` proxy) and may under-represent true NER semantics.
- Collective fitness module is not yet wired into Phase 4 run loop in this task; integration remains for run-stage tasks.

## Rollback
- Revert commit:
  - `git revert <TASK-1801-PREP-commit-hash>`
