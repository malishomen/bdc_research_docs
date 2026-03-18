# TASK-7597 BRIEF REPORT

## Scope
- Create the formal pre-experiment gate instance for canonical `Phase R1`.
- Run a fresh smoke execution into a new output root.
- Verify that runner and aggregation artifacts are preserved correctly.
- Build a synthetic generic packet and experimentally check whether `BDC Designer` accepts it.

## Changes
- Created `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE.md`.
- Created `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/` with a synthetic intake-complete packet and copied smoke-run summaries.
- Created `tasks/TASK-7597-BDC-R1-PREEXPERIMENT-GATE-SMOKE-AND-DESIGNER-CHECK.json`.
- Generated a fresh smoke root at `results/selection_physics_reboot_r1_gate_smoke_2026-03-19`.
- Generated experimental BDC bundle outputs under `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/BDC_CLIENT_BUNDLE_OUTPUT`.

## Verification (L0)
- Command: `python scripts/edp1/run_selection_physics_reboot_sweep.py --manifest scripts/edp1/selection_physics_manifest.json --out_root results/selection_physics_reboot_r1_gate_smoke_2026-03-19 --max_seeds 1 --dry_run`
- Result: PASS
- Output summary: `total_runs=6`, `pass_runs=6`, `fail_runs=0`.

- Command: `python scripts/edp1/aggregate_selection_physics_reboot.py --in_root results/selection_physics_reboot_r1_gate_smoke_2026-03-19 --out_dir results/selection_physics_reboot_r1_gate_smoke_2026-03-19/aggregates`
- Result: PASS
- Output summary: wrote `r1_regime_summary.csv`, `r1_regime_summary.json`, `r1_gate_decision.json`; smoke verdict=`PASS_TO_R2`.

- Command: `python tools/bdc_designer_v2.py --pretty client-bundle --folder_path docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET --out_root docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/BDC_CLIENT_BUNDLE_OUTPUT --out_json docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/BDC_CLIENT_BUNDLE_OUTPUT/bundle_result.json`
- Result: PASS
- Output summary: `supported=true`, `recommended_variant_id=no_penalty_diagnostic`, `confidence_band=medium`, `selective_outcome_class=recommend_with_guardrails`, `recommended_logical_split=4_role_logical_redesign`.

## Artifacts
- `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE.md` - formal scientific pre-experiment gate memo for the canonical full `R1` sweep.
- `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/README.md` - scope and integrity note for the synthetic gate packet.
- `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/BDC_INPUT_PACKET_R1_FULL_SWEEP_PREEXPERIMENT_GATE.json` - structured synthetic packet metadata.
- `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/unified_variant_comparison.csv` - invariant-format variant table derived from smoke aggregate outputs.
- `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/current_slice_metrics.csv` - invariant-format slice table for the smoke outputs.
- `results/selection_physics_reboot_r1_gate_smoke_2026-03-19/` - fresh smoke-run output root.
- `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE_PACKET/BDC_CLIENT_BUNDLE_OUTPUT/bundle_result.json` - experimental intake result from `BDC Designer`.

## Risks / Limitations
- The smoke run remains a tooling-only preservation check and cannot authorize `R2`.
- The synthetic packet is accepted by the current generic intake contract, but this is experimental compatibility rather than a dedicated scientific-line native schema.
- `BDC Designer` currently recommends `no_penalty_diagnostic` on the smoke packet because the synthetic metrics surface is intentionally sparse and client-oriented heuristics are still active.
- `measurement_gaps.json` remains expressed in current client/runtime vocabulary, not a scientific reboot vocabulary.

## Rollback
- Revert with `git revert <task-commit-hash>` after identifying the final commit for `TASK-7597`.
