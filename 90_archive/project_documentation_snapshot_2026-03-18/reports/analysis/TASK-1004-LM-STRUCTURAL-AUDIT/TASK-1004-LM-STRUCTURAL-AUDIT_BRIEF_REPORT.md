# TASK-1004-LM-STRUCTURAL-AUDIT BRIEF REPORT

## Scope
- Structural LM training audit for shift/mask/loss/data alignment and report-status correctness.
- Constraints preserved: no seed/optimizer/lr changes, no architecture rewrite, determinism flags unchanged.

## Changes
- `scripts/wiki_pilot/run_once.py`
  - Added explicit shape asserts for `input_ids`, `labels`, `logits`.
  - Added shift-alignment assert: `labels[:, :-1] == input_ids[:, 1:]`.
  - Added causal-mask builder with strict assertions (shape/dtype/strict upper-triangular/no diagonal masking).
  - Added first-batch debug logs: first 16 `input_ids`, `labels`, `argmax(pred)`, and `next_token_acc`.
  - Added loss-sanity checks:
    - `F.cross_entropy(logits.view(-1, V), labels.view(-1), ignore_index=-100)`.
    - labels range audit via `fraction_ignore_index` / `fraction_oob_labels` + assert oob==0.
  - Added data/tokenizer alignment logs:
    - `max_token_id_in_batch`, `top1_token_freq`, `special_pad_freq`, `special_unk_freq`.
  - Added `--steps` alias for short diagnostics (`--steps N` -> `max_steps=N`).
- `scripts/wiki_pilot/generate_report.py`
  - Final status now separated and corrected:
    - `Status=PASS` only if determinism PASS AND all run kill statuses PASS.
    - Added explicit `Determinism: PASS/FAIL` and `Run Health: PASS/FAIL`.
    - Added per-run kill status block.
- New tests:
  - `scripts/wiki_pilot/tests/test_shift_alignment.py`
  - `scripts/wiki_pilot/tests/test_loss_sanity.py`

## Verification (L0)
- `pytest scripts/wiki_pilot/tests/` -> PASS (10 passed)
- `python scripts/wiki_pilot/run_once.py --dry_run` -> PASS (new audit logs emitted)
- `python scripts/wiki_pilot/run_once.py --steps 50 --seed 1337 --out_dir results/wiki_pilot/run_diag_50` -> PASS
- `python scripts/wiki_pilot/compare_runs.py --verify --root results/wiki_pilot` -> PASS (after restoring `run_1` full output)
- `python scripts/wiki_pilot/generate_report.py` -> PASS; `results/wiki_pilot/FINAL_REPORT.md` now reports:
  - `Status: FAIL`
  - `Determinism: PASS`
  - `Run Health: FAIL`

## Audit Conclusion
- Shift alignment: validated by assert + unit test (no mismatch).
- Causal mask: validated by assert + unit test (no future leakage mask defect).
- Loss path: uses raw logits into `cross_entropy` (correct), label range/oob checks show clean labels.
- Data alignment: token IDs within vocab, no pad/unk dominance in sampled batch.
- Deterministic collapse still reproduces at step 200 with high confidence and low entropy.
- Concrete observed failure pattern: model becomes overconfident (`mean_prob_max ~0.9745`, `token_entropy ~0.0638`) while next-token accuracy on debug batch is 0.0, i.e. confident wrong-token regime.

## Artifacts
- `scripts/wiki_pilot/run_once.py`
- `scripts/wiki_pilot/generate_report.py`
- `scripts/wiki_pilot/tests/test_shift_alignment.py`
- `scripts/wiki_pilot/tests/test_loss_sanity.py`
- `reports/analysis/TASK-1004-LM-STRUCTURAL-AUDIT/TASK-1004-LM-STRUCTURAL-AUDIT_BRIEF_REPORT.md`

## Risks / Limitations
- Root-cause class narrowed to model dynamics/data-contract regime, but not fully eliminated at algorithmic level in this task (by scope).

## Rollback
- Revert TASK-1004 commit and rerun test suite.
