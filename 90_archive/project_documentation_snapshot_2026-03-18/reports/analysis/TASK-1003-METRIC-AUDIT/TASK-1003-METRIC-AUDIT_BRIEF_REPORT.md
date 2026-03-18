# TASK-1003-METRIC-AUDIT BRIEF REPORT

## Scope
- Audit metric correctness for entropy, perplexity, cross-entropy relationship, repetition rate semantics, and softmax validity.
- Add unit tests for entropy and perplexity invariants.

## Changes
- `scripts/wiki_pilot/run_once.py`
  - Added `softmax_probabilities(logits)` with assert: `softmax.sum(dim=-1) ~= 1.0`.
  - Added `entropy_from_probabilities(probs)` with `clamp_min(EPS)` guard against `log(0)`.
  - `token_entropy(logits)` now explicitly computes entropy from softmax probabilities.
  - Added `perplexity_from_loss(loss)` and switched perplexity logging to `exp(val_loss)`.
  - Confirmed `repetition_rate` measures adjacent token repeats (`pred[:,1:] == pred[:,:-1]`) and documented it.
  - Added diagnostics to metrics CSV: `mean_prob_max`, `mean_prob_min`, `mean_logits_std`.
- `scripts/wiki_pilot/tests/test_entropy.py` (new)
  - Uniform distribution over 10 tokens -> entropy ~= `log(10)`.
  - One-hot distribution -> entropy ~= `0`.
- `scripts/wiki_pilot/tests/test_perplexity.py` (new)
  - `loss=0 -> perplexity=1`.
  - `loss=log(10) -> perplexity~=10`.
- `scripts/wiki_pilot/compare_runs.py`
  - No logic change required for this audit.

## Verification (L0)
- `pytest scripts/wiki_pilot/tests/` -> PASS (4 passed)
- `python scripts/wiki_pilot/run_once.py --dry_run` -> PASS
- `python scripts/wiki_pilot/compare_runs.py --verify --root results/wiki_pilot` -> PASS

## Artifacts
- `scripts/wiki_pilot/run_once.py`
- `scripts/wiki_pilot/tests/test_entropy.py`
- `scripts/wiki_pilot/tests/test_perplexity.py`
- `reports/analysis/TASK-1003-METRIC-AUDIT/TASK-1003-METRIC-AUDIT_BRIEF_REPORT.md`

## Risks / Limitations
- This task audits metric correctness and diagnostics only; it does not resolve stability failure (`entropy_collapse`) root cause.

## Rollback
- Revert updated files from TASK-1003 and rerun verification suite.
