# TASK-1802 BRIEF REPORT

## Scope
- Integrate Phase 4 collective multirole run path into cloze evolution runner via `--collective` flag.
- Keep cloze-only default behavior backward-compatible.
- Add smoke orchestration script for exp_0600 2-task MVP.
- Close TASK-1801 hash-follow-up log debt (append-only).

## Changes
- Updated `evolution/cloze_symbolic/run_generations.py`:
  - Added CLI flags:
    - `--collective`
    - `--collective_cloze_weight`
    - `--collective_entity_weight`
  - Added guard: `--collective` cannot be combined with `--energy_model` (Phase 4 policy).
  - In collective mode:
    - computes per-individual `cloze_acc` and `entity_acc`
    - computes individual fitness by Scheme S1: `max(cloze_acc, entity_acc)`
    - computes population collective score via weighted mean of best-per-task.
  - Extended `metrics.csv` (collective mode only) with:
    - `mean_entity_accuracy`, `max_entity_accuracy`
    - `mean_individual_collective_fitness`, `max_individual_collective_fitness`
    - `collective_score`, `best_cloze_accuracy`, `best_entity_accuracy`
  - Extended `summary.json` with:
    - `collective` flag and `collective_weights`
    - `entity_baselines`
    - final collective/entity metrics.
- Added `scripts/edp1/run_phase4_multirole.py`:
  - smoke/diagnostic orchestration for Phase 4 2-task MVP
  - per-seed run delegation to `run_generations --collective`
  - aggregate JSON/CSV output.
- Added `tests/test_phase4_multirole_run.py`:
  - backcompat path test (without `--collective`)
  - collective summary/metrics field presence test
  - smoke orchestrator 2-seed execution test.
- Append-only log fix for TASK-1801 hash follow-up:
  - `AGENTS_LOG.md`
  - `WEEKLY_STATUS.md`.

## Verification (L0)
- Command: `git status --short`
- Result: PASS
- Output summary: only intended files changed; no staged artifacts from `results/`.

- Command: `python -m py_compile evolution/cloze_symbolic/run_generations.py evolution/micro_tasks/entity.py evolution/collective_fitness.py scripts/edp1/run_phase4_multirole.py`
- Result: PASS
- Output summary: all target modules compile.

- Command: `pytest -q tests/test_phase4_entity_overlay.py tests/test_phase4_collective_fitness.py tests/test_phase4_multirole_run.py`
- Result: PASS
- Output summary: `10 passed`.

- Command: `python -m evolution.cloze_symbolic.run_generations --dry_run --genome_version v2 --use_skip_bigram --seed 1337 --out_dir results/tmp_task1802_cloze_only`
- Result: PASS
- Output summary: summary written; default cloze-only path executes successfully.

- Command: `python -m evolution.cloze_symbolic.run_generations --dry_run --collective --genome_version v2 --use_skip_bigram --seed 1337 --out_dir results/tmp_task1802_collective`
- Result: PASS
- Output summary: summary written; collective path executes successfully.

- Command: `python scripts/edp1/run_phase4_multirole.py --level smoke --seeds 2 --base_seed 1337 --out_root results/edp1_exp0600_multirole_smoke`
- Result: PASS
- Output summary: 2 seed runs completed; aggregate summary created.

- Command: `git show --name-only --oneline HEAD`
- Result: PASS (after commit)

## Artifacts
- `evolution/cloze_symbolic/run_generations.py` - collective path integration.
- `scripts/edp1/run_phase4_multirole.py` - exp_0600 smoke runner.
- `tests/test_phase4_multirole_run.py` - integration tests for collective mode.
- `reports/analysis/TASK-1802-INTEGRATE/TASK-1802_BRIEF_REPORT.md` - task report.
- `AGENTS_LOG.md` - append-only TASK-1801 follow-up + TASK-1802 entries.
- `WEEKLY_STATUS.md` - append-only TASK-1801 follow-up + TASK-1802 section.

## Risks / Limitations
- Collective mode currently targets 2-task MVP (cloze + entity); category task remains intentionally deferred.
- `entity_baselines` are heuristic-proxy-based and should be treated as interim governance signals.

## Rollback
- Revert this task commit:
  - `git revert <TASK-1802-INTEGRATE-commit-hash>`
