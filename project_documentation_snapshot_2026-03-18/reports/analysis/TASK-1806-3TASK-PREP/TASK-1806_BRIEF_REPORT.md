# TASK-1806 BRIEF REPORT

## Scope
- Fix logging gap from TASK-1805 (final hash row for `3615595`, append-only).
- Add 3rd micro-task category proxy and wire optional 3-task collective scoring.
- Preserve 2-task collective backcompat when category flag is disabled.
- Validate with smoke runs only (no full N=30).

## Changes
- Added `evolution/micro_tasks/category.py` with deterministic category accuracy helper.
- Updated `evolution/cloze_symbolic/task.py`:
  - added `doc_category_label` in samples,
  - added deterministic category overlay fields in `ClozeTaskData`:
    - `candidate_category_label`, `target_category_label`.
- Updated `evolution/collective_fitness.py`:
  - added 3-task S1 helpers:
    - `individual_fitness_s1_3task(...)`
    - `collective_fitness_s1_3task(...)`.
- Updated `evolution/cloze_symbolic/run_generations.py`:
  - added flags:
    - `--use_category_task`
    - `--collective_category_weight`
  - 3-task metrics emitted only when category task is enabled.
  - 2-task path remains unchanged when flag is off.
- Updated `scripts/edp1/run_phase4_multirole.py`:
  - optional `--use_category_task` and category weight support,
  - aggregate now includes `max_category_accuracy` when present.
- Added tests:
  - `tests/test_phase4_category_proxy.py`
  - `tests/test_phase4_multirole_3task_run.py`
- Updated docs:
  - `docs/experiments/EXP-0600_MULTI_ROLE_2026-03-01.md`
  - `docs/project/project_roadmap.md`

## Verification (L0)
- Command: `git status --short`
- Result: PASS
- Output summary: expected tracked file set only; no `results/` tracked.

- Command: `python -m py_compile evolution/micro_tasks/category.py evolution/cloze_symbolic/task.py evolution/cloze_symbolic/run_generations.py evolution/collective_fitness.py scripts/edp1/run_phase4_multirole.py`
- Result: PASS

- Command: `pytest -q tests/test_phase4_category_proxy.py tests/test_phase4_multirole_3task_run.py`
- Result: PASS
- Output summary: tests passed; deterministic labels and 2-task/3-task behavior validated.

- Command: `python -m evolution.cloze_symbolic.run_generations --dry_run --collective --genome_version v2 --use_skip_bigram --seed 1337 --use_category_task --out_dir results/tmp_task1806_3task_collective`
- Result: PASS

- Command: `python scripts/edp1/run_phase4_multirole.py --level smoke --seeds 2 --base_seed 1337 --use_category_task --out_root results/edp1_exp0600_multirole_3task_smoke`
- Result: PASS

## Backcompat
- With `--collective` and without `--use_category_task`:
  - `summary.json` keeps 2-task semantics.
  - category fields are not emitted in final metrics.

## Artifacts
- `evolution/micro_tasks/category.py`
- `evolution/cloze_symbolic/task.py`
- `evolution/cloze_symbolic/run_generations.py`
- `evolution/collective_fitness.py`
- `scripts/edp1/run_phase4_multirole.py`
- `tests/test_phase4_category_proxy.py`
- `tests/test_phase4_multirole_3task_run.py`
- `reports/analysis/TASK-1806-3TASK-PREP/TASK-1806_BRIEF_REPORT.md`

## Risks / Limitations
- Category proxy is intentionally minimal (doc-level binary) and may need richer formulation before final gate.
- No N=30 gate run performed in this task by design.

## Rollback
- Revert this task commit:
  - `git revert <TASK-1806-3TASK-PREP-commit-hash>`
