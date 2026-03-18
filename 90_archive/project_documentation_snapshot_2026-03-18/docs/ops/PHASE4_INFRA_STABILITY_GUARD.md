# Phase 4 Infra Stability Guard

Date: 2026-03-04  
Status: ACTIVE

## Purpose
Define mandatory runtime policy for long-running Phase 4 experiments so infrastructure incidents do not contaminate scientific interpretation.

## Allowed Execution Modes

1. `HIVE_AUTONOMOUS`:
   - supervisor + monitor enabled,
   - auto-resume from checkpoints,
   - periodic health checks (CPU/RAM/disk/backup freshness),
   - stale lock cleanup and bounded retry logic.
2. `LOCAL_FROZEN_GATE`:
   - HIVE compute frozen,
   - checkpoint migrated with integrity verification,
   - gate run finalized on local machine using identical protocol.

Any mixed mode requires explicit logging of handoff point and integrity checks.

## Mandatory Controls

- Preflight before long run:
  - backup timer active,
  - backup freshness <= 35 minutes,
  - writable results path,
  - dataset path present.
- Checkpoint integrity for migration:
  - seed-count match,
  - file-count/hash manifest match.
- Resume policy:
  - restart only missing/incomplete seeds,
  - never overwrite completed `summary.json`/`metrics.csv` without explicit task directive.

## Incident Handling

- Infra incidents are classified as `NON-SCIENCE` unless they alter:
  - run protocol (`N/G/P/flags`),
  - dataset/subset,
  - metric formulas/governance.
- Every incident must be logged with:
  - timestamp,
  - signature/root cause,
  - recovery action,
  - proof that scientific artifacts remain valid.

## Phase 4 Interpretation Guard

- `RUN COMPLETE` answers only execution completeness.
- `GATE PASS/FAIL/NOT PASSED YET` is decided only by canonical metrics/ADR governance.
- Infra incidents may delay completion, but cannot be used to weaken or reinterpret gate thresholds.

## References

- `docs/ops/HIVE_LONGRUN_PLAYBOOK.md`
- `decisions/ADR-0010-phase4-3task-gate-governance.md`
- `reports/analysis/TASK-1813-PHASE4-GATE/PHASE4_GATE_DECISION.md`
