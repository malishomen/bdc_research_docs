# TASK-0118 BRIEF REPORT

- Commit: pending-commit
- Selected KC1_TTT candidate(s):
  - Primary (KC1_TTT_V2): `H=5`, `T=0.075`
  - Backup: `H=4`, `T=0.05`
- Why selected (queue11 on exp_0012 metrics, trade-off evidence):
  - Baseline `H=3,T=0.10`: `configs_fail_rate_1p0=5` (systematic false negatives on 5/11).
  - Primary `H=5,T=0.075`: `configs_fail_rate_1p0=0`, `configs_fail_rate_0p0=10`, `mean_fail_rate_over_11=0.018182`.
  - Backup `H=4,T=0.05`: `configs_fail_rate_1p0=0`, but `configs_fail_rate_0p0=11` (KC1 disappears on this evidence set).
- Next experiment (pre-registered):
  - Spec: `experiments/exp_0015_kc1_ttt_vnext_validation/SPEC.md`
  - Runbook: `experiments/exp_0015_kc1_ttt_vnext_validation/RUN_COMMANDS.md`
  - Command (print-only): `python tools/analysis/exp0012_kc1_ttt_horizon_sweep.py --print_tradeoff_only --queue ... --metrics ...`
- Risks + rollback:
  - Risk: KC1_TTT_V2 may be too permissive outside queue11; requires vNext validation before adoption in any runner.
  - Rollback: revert to baseline `KC1_TTT(H=3,T=0.10)` in the next experiment version if sanity worsens; no retroactive changes.

