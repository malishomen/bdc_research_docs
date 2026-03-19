# R5 Transfer Target Matrix

## Purpose

This matrix defines the bounded adjacent transfer target surface for `R5`.

It does not approve the target by itself.
It serializes the current evidence asymmetry before the `BDC`-assisted decision gate.

## Candidates

### 1. `symbolic_micro_corpus_cloze_transfer`

- Adjacent family:
  - `micro_corpus_cloze`
- Why it is adjacent:
  - still a bounded symbolic prediction task,
  - still deterministic,
  - still allows the same FIFO memory mechanism to act over a bounded context window.
- Existing surface already present:
  - `evolution/cloze_symbolic/task.py`
  - `scripts/edp1/run_cloze_exp_0400.py`
  - `reports/analysis/TASK_0139_BRIEF_REPORT.md`
- Current evidence state:
  - deterministic historical cloze scaffolding exists,
  - historical measured cloze work exists,
  - direct same-mechanism transfer evidence does not yet exist.
- Main risk:
  - the old cloze runtime is not the same as the approved FIFO mechanism family,
  - historical `exp_0400_cloze_symbolic` summaries show that the older cloze evolutionary surface should not be relaunched blindly.
- Honest reading:
  - this is the only candidate with enough executable adjacent surface to justify launch preparation now,
  - but it requires a new bounded transfer harness rather than reuse of the old cloze loop as-is.

### 2. `controlled_uncertainty_abstention_transfer`

- Adjacent family:
  - `controlled_uncertainty_abstention`
- Why it is adjacent:
  - keeps the project inside bounded quaternary-like uncertainty semantics,
  - preserves single-mechanism scope more conservatively than a richer corpus task.
- Existing surface already present:
  - documentation only
- Current evidence state:
  - candidate exists in `R2` design documents,
  - no deterministic artifact exists,
  - no runner exists,
  - no measured surface exists.
- Main risk:
  - choosing it now would force another package-design cycle instead of long-run preparation.
- Honest reading:
  - conceptually attractive,
  - but not launch-preparable yet.

## Comparison Summary

### Deterministic surface availability
- `symbolic_micro_corpus_cloze_transfer`: present
- `controlled_uncertainty_abstention_transfer`: absent

### Historical measured support
- `symbolic_micro_corpus_cloze_transfer`: present as historical cloze work, but not as same-mechanism transfer evidence
- `controlled_uncertainty_abstention_transfer`: absent

### Scope-preservation risk
- `symbolic_micro_corpus_cloze_transfer`: medium
- `controlled_uncertainty_abstention_transfer`: low

### Long-run preparation readiness
- `symbolic_micro_corpus_cloze_transfer`: medium
- `controlled_uncertainty_abstention_transfer`: low

### Need for a new bounded harness
- `symbolic_micro_corpus_cloze_transfer`: yes
- `controlled_uncertainty_abstention_transfer`: yes

The key asymmetry is:
- cloze already has executable adjacent task infrastructure,
- uncertainty abstention still has only paper-surface intent.

## Matrix Conclusion

At the matrix stage:
- `symbolic_micro_corpus_cloze_transfer` is the only honest candidate for immediate launch preparation,
- `controlled_uncertainty_abstention_transfer` remains a legitimate later path, but not the right next long-run target.

## Constraint For The Next Gate

If `symbolic_micro_corpus_cloze_transfer` is approved, the next implementation step must:
- preserve the same FIFO mechanism family,
- build a new bounded transfer harness,
- avoid reusing the older cloze evolutionary stack as proof of transfer success.

If that constraint cannot be met, the project must remain in `R5` transfer planning.
