# ADR-0004: Formal closure of EDP1 hidden_rule as product direction

Date: 2026-02-27

## Context
- Phase 0 in `docs/project/project_roadmap.md` requires formal closure of `hidden_rule` as a product direction and preservation of the line as a controlled laboratory benchmark.
- Canon requires decision-level formalization when direction status changes (`CANON.md`, change control R2).
- This ADR is governance-only: no evolution code, no run scripts, no experiment logic changes.

## Status Quo
- EDP1 `hidden_rule` has multiple validated runs (`TASK-1100+`) and is deterministic/operational as an experimental harness.
- `v1_speciation` is the strongest validated reference point for current regime (`final_max_fitness_mean = 0.7881661019442968`).
- `v1_5` failed target thresholds in N=30/G=100 validation.
- `v2*` under current fitness regime is mathematically blocked from beating `v1_speciation`.
- `docs/project/project_main_doc.md` and `docs/project/project_roadmap.md` classify `hidden_rule` as exhausted/toy and require strategic transition to new architecture/task lines.

## Evidence
- `reports/analysis/TASK-1203A-MRTN-DIAGNOSTIC/TASK-1203A_BRIEF_REPORT.md`:
  - MRTN `v2` diagnostics show no meaningful fitness gain signal from shock and high diversity without fitness progress.
- `reports/analysis/TASK-1300-GENOME-V1_5/TASK-1300_BRIEF_REPORT.md`:
  - `final_max_accuracy_mean = 0.8117838541666667`, `final_max_fitness_mean = 0.7637578865767252`, status `FAIL`.
- `reports/analysis/TASK-1400-COMPLEXITY-AUDIT/TASK-1400_BRIEF_REPORT.md`:
  - Baseline anchor `v1_speciation final_max_fitness_mean = 0.7881661019442968`.
- `reports/analysis/TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM/TASK-1400B_BRIEF_REPORT.md`:
  - `v2/v2_prior/v2_staged required_accuracy_to_beat_v1 > 1.0` (`~1.1301`), i.e. impossible at `accuracy in [0,1]` under current regime.
- `reports/analysis/PROJECT_KNOWLEDGE_CONSOLIDATED_20260227.md` + `docs/project/project_main_doc.md` + `docs/project/project_roadmap.md`:
  - Strategic framing: `hidden_rule` is toy/exhausted for product goals; next phases move to physics fix and wiki-derived evolution.

## Decision
1. EDP1 `hidden_rule` line is declared **exhausted as a product strategy** (`product direction: CLOSED`).
2. EDP1 `hidden_rule` is retained as a **laboratory benchmark/physics stand** for controlled R0/R1 experiments (Phase 1 physics validation).
3. `v1_speciation` is fixed as **PERMANENT BASELINE** for `hidden_rule` comparisons and governance references.
4. Core hypotheses `H1-H3` are **not closed** by this ADR; they are transferred to the new architectural line described in `docs/project/project_main_doc.md` and operationalized by phased roadmap (`docs/project/project_roadmap.md`).

## Consequences
- No further roadmap progress can be claimed from `hidden_rule` score improvements alone.
- New `hidden_rule` runs are allowed only as laboratory evidence for regime/physics checks and must be classified as R0/R1 without strategic claim inflation.
- Decision governance is explicit in canonical files (`KILL_CRITERIA.yaml`, `ARCHITECTURE.md`).
- Historical artifacts remain valid as evidence base; no retroactive rewriting.

## Alternatives considered
- Keep `hidden_rule` as active product direction:
  - Rejected, because evidence shows structural non-viability for architectural growth in current regime and poor product relevance.
- Close `hidden_rule` completely (no further use):
  - Rejected, because the line remains valuable as a deterministic lab stand for controlled physics experiments and regression checks.
- Close hypotheses `H1-H3` together with `hidden_rule`:
  - Rejected, because `hidden_rule` closure is task-line closure, not hypothesis falsification across all future environments.

## Rollback
- Revert governance package commit introducing ADR-0004 and linked canonical doc updates:
  - `git revert <TASK-1500-commit-hash>`
- Any rollback requires a superseding ADR documenting why `hidden_rule` is reopened as a product direction.
