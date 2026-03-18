# QUATERNARY ROUTER SPEC (DRAFT) — Adult Mode

Status: DRAFT (not canonical)

Purpose
Define deterministic routing rules for Quaternary Logic tasks (YES/NO/MAYBE_YES/MAYBE_NO)
with strict evidence gates and no adaptive tuning.

Definitions
- YES: Sufficient evidence exists; route to CPU executor for authoritative decision.
- NO: Evidence indicates failure/invalidity; route to CPU executor for negative verdict.
- MAYBE_YES: Evidence suggests a viable region but requires bounded exploration; GPU allowed only under gates.
- MAYBE_NO: Evidence insufficient or conflicting; CPU holds decision, GPU exploration prohibited.

Core Principles (Adult Mode)
- Deterministic routing: identical inputs -> identical outputs.
- Evidence-gated: no GPU MAYBE_YES without documented evidence and hashes.
- No adaptive tuning: only pre-registered parameter grids; post-hoc analysis allowed.
- Infra success ≠ cognitive success (explicit separation).

Evidence Gates (Required)
- EXP_0007 Phase-0 full sweep analysis present:
  - reports/analysis/EXP_0007_PHASE0_FULLSWEEP_ANALYSIS.md
  - run_dir + sha256 hashes referenced in that analysis
- Run metadata hashes must match:
  - metrics_sha256: ba375c427d9452fcb36b7cc941cff4a2661190f1dd37e51b357fe8ac36e08b4d
  - summary_sha256: ffc728d283762cfb06c74f74d18de68fa6f19dea602317047eaa5436759eabb1

Evidence Summary (from EXP_0007)
- 32 configs total; 21 configs with pass_rate=1.0; 11 configs with pass_rate=0.0.
- KC1_EARLY_COLLAPSE dominates failures (clonal_init + low mutation intensity).
- Random_init configurations consistently pass (all 16).

Routing Policy
1) CPU (YES/NO) is mandatory for:
   - evidence_analysis tasks
   - governance/kill-criteria decisions
   - any task that changes canonical claims
2) GPU MAYBE_YES is permitted only if:
   - evidence gates are satisfied
   - task is marked "acceleration_allowed"
   - task does not change logic (compute-only acceleration)
3) GPU MAYBE_NO is default when:
   - evidence gates missing or hashes mismatch
   - task is not acceleration-only

When GPU MAYBE_YES becomes YES
- Budget: fixed time and compute budget declared (no adaptive expansion).
- Logging: GPU device info and utilization logged.
- Replication: at least 2 independent runs with identical inputs.
- Determinism: outputs byte-identical for identical inputs.
- If all gates pass, GPU result is promoted to CPU YES; otherwise reverts to MAYBE_NO.

Kill Criteria (Routing Failures)
- Non-deterministic routing for same inputs => FAIL.
- GPU used without evidence gates => FAIL.
- Any adaptive tuning based on results => FAIL.
- Missing or mismatched hashes => FAIL.

Notes
- This draft is a strict routing policy for "adult mode".
- Promotion to canonical requires ADR if conflicts arise.
