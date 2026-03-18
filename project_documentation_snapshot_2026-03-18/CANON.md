## BIO-DIGITAL CORE CANON (BDC)

Canonical discipline for BDC. This is the single source of truth for process rules.
Source: `docs/project/CANON_DISCIPLINE_SOURCE_RU.md`.

## 0) Main principle
No claims without artifacts and metrics. Any statement like "works", "better", "scales"
is valid only with:
- experiment protocol,
- fixed seeds,
- raw results,
- statistics,
- commit/tag reference.

## 1) Non-negotiables
- Reproducibility by default: same commit + same seeds + same environment => same results
  (within tolerances).
- Kill-criteria are law: if a kill-criterion triggers, the direction is closed or redefined.
- Separation of contours: qcore, memory, env, agent, evolution are isolated; no hidden deps.
- No "magical" meaning sources: Pi is only a deterministic stream/seed source.
- No hardware until TRL5 is closed.

## 2) Evidence standard
Every claim must include:
- `EXPERIMENT_SPEC.md` (goal, hypotheses, metrics, thresholds, baselines, constraints),
- `SEEDS.md` (all seeds + stream split),
- `RUN_COMMANDS.md` (exact commands),
- `RESULTS/*.csv` (raw results),
- `ANALYSIS.ipynb` or `analysis.py` (deterministic metric calc),
- `REPORT.md` (conclusions + links to files),
- commit hash + experiment release tag.
Statistics are mandatory: N >= 30 seeds unless stated; CIs; thresholds fixed upfront.

## 3) Change control
- Any change affecting results must update `EXPERIMENT_SPEC.md` or an ADR.
- Change classes:
  - R0: refactor (no numerical change; requires regression verification).
  - R1: method change (new experiment version).
  - R2: hypothesis/kill-criteria change (new roadmap revision).

## 4) Canonical repo structure
Minimum structure:
- `qcore/`, `memory/`, `env/`, `agent/`, `evolution/`, `experiments/`, `decisions/`,
  `results/`, `docs/`, `scripts/`.

Mandatory files (single source of truth):
- `CANON.md`
- `SEMANTICS.md`
- `KILL_CRITERIA.yaml`
- `SEED_POLICY.md`
- `REPRODUCIBILITY.md`
- `VERSIONING.md`

## 5) PiStream seed policy (summary)
Separate streams are mandatory:
ENV, INIT, NOISE, MUT_DECISION, MUT_MAGNITUDE, QUERY.
The exact conversion of Pi digits to base-4 is defined in `SEED_POLICY.md`.

## 6) TRL gating (summary)
Transition is allowed only via checklists. For TRL-3 (Paramecium MVP):
- one-command run,
- N >= 30 fixed seeds,
- at least 2 baselines,
- anti-cheat constraints (MY/MN share, energy/scan penalties, genome size),
- pass kill-criteria or close the direction.

## 7) Anti-self-deception
No success by a single metric. Minimum: utility, calibration/error, cost, robustness.
No post-hoc threshold tuning. Black-box wins are invalid without mechanism evidence.

## 8) Logging and ADRs
Weekly status report and ADRs are mandatory for principle changes.

## 9) Security/IP (minimum)
Artifacts must carry license/access policy. External data is audited (source, rights, reproducibility).
Dependencies are fixed via lockfiles.

## 10) Canon violations
Violations invalidate results, require a "Canon Violation" issue, and a corrective release.

