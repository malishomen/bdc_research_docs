# BDC Research Methodology

**Version:** 1.0  
**Status:** CANONICAL  
**Last Updated:** 2026-01-27  
**Implements:** ARCHITECTURE.md principles

---

## Overview

This document defines the formal research standard for BIO-DIGITAL CORE (BDC). All experiments, validations, and claims must adhere to this methodology.

**Core Principle:** Infrastructure success does NOT imply cognitive success. Each task class (see ARCHITECTURE.md) must be validated independently.

---

## Kill-Criteria Framework

Kill-criteria are **law**. If a kill-criterion triggers, the direction is closed or redefined. No exceptions.

### Canonical Hypotheses and Kill-Criteria

#### H1: Quaternary Logic Improves Calibration

**Hypothesis:** S={T, F, MY, MN} with conflict_flag improves calibration and reduces false confidence vs. binary baseline.

**Metrics:**
- ECE (Expected Calibration Error) or Brier score improvement
- Selective prediction utility under MY/MN allowance
- False-confidence rate

**Kill-Criteria:**
1. Improvement in ECE or Brier < 10% vs. baseline at equal compute budget
2. MY/MN share > X% without utility gain (X must be fixed in EXPERIMENT_SPEC.md before experiment)
3. No statistically stable reduction in false-confidence rate

**Status:** NOT VALIDATED — Requires full EXPERIMENT_SPEC.md with N≥30, baselines, and thresholds.

#### H2: DNA-Inspired Memory Yields Scalable Long Context

**Hypothesis:** Memory with index, integrity, and random access provides scalable long context with exact recall.

**Metrics:**
- Exact recall accuracy (bit/qubit level)
- Random access latency (target class: O(log n) by index)
- Compression ratio (if claimed)
- Integrity rate (checksums/ECC)

**Kill-Criteria:**
1. Exact recall < 99.9% on fixed test length
2. Random access latency exceeds target class (must be fixed in EXPERIMENT_SPEC.md)
3. Compression degrades recall or causes uncontrolled loss

**Status:** PARTIALLY VALIDATED — memory/ modules exist, but full H2 validation with 99.9% threshold not completed.

#### H3: Self-Replication/Regeneration Without Error Accumulation

**Hypothesis:** Organism (genome + VM + controller) can replicate, detect damage, and recover without accelerating error accumulation.

**Metrics:**
- Replication fidelity (structure/behavior match)
- Recovery rate (proportion of successful recoveries)
- Error accumulation slope (errors per generation)

**Kill-Criteria:**
1. Recovery rate < 70% on "small damage" scenarios (parameters must be formalized in EXPERIMENT_SPEC.md)
2. Error accumulation accelerates across generations (positive feedback without correction)
3. Works only in noise-free conditions (fails under minimal noise)

**Status:** NOT VALIDATED — Requires full EXPERIMENT_SPEC.md with formalized damage scenarios and N≥30 seeds.

---

## PiStream as Mandatory Evolutionary Validation

**Rule:** PiStream (or equivalent synthetic test) is **mandatory** before real data runs for Class 1 tasks.

### PiStream Purpose

PiStream serves **exclusively** as:
1. **Deterministic seed source** for environment generation, mutations, noise
2. **Test data** for memory exact recall validation
3. **Control markers** and checksum signatures

**Forbidden:** Describing Pi as "training meaning source" or "intelligence source."

### PiStream Stagnation (v1)

**Root Cause:** PiStream v1 stagnated due to:
1. **Insufficient evolutionary pressure:** Mutation strength too low, selection pressure too weak
2. **Premature convergence:** Population diversity dropped below 0.15 without recovery
3. **Signal-to-noise degradation:** Fitness improvements became indistinguishable from noise
4. **Lack of diversity enforcement:** No mechanism to prevent convergence to local optima

**Resolution (v2):**
- Increased mutation strength (see EVOLUTION_ENGINE.md)
- Explicit diversity enforcement mechanisms
- Stop-scaling criteria based on signal-to-noise ratio
- Population Governor to prevent premature convergence

### PiStream Stream Separation

**Mandatory streams (never reuse across subsystems):**
- `ENV_PISTREAM`: Environment generation
- `INIT_PISTREAM`: Initial states
- `NOISE_PISTREAM`: Sensor/environment noise
- `MUT_DECISION_PISTREAM`: Mutation locations/targets
- `MUT_MAGNITUDE_PISTREAM`: Mutation magnitudes
- `QUERY_PISTREAM`: Memory query selection (random access)

**Violation:** Reusing a stream across subsystems invalidates reproducibility.

---

## Evidence Standard

Every claim must include:

1. **EXPERIMENT_SPEC.md:**
   - Goal, hypotheses, metrics, thresholds
   - Baselines (at least 2 for comparison)
   - Constraints and anti-cheat measures
   - Kill-criteria with fixed thresholds

2. **SEEDS.md:**
   - Master seed and all derived stream seeds
   - Stream start/length for each PiStream
   - SHA-256 of Pi digits file

3. **RUN_COMMANDS.md:**
   - Exact commands to reproduce experiment
   - Environment setup (OS, toolchain versions)
   - One-command run capability (for TRL-3+)

4. **RESULTS/*.csv:**
   - Raw results (no post-processing)
   - All metrics per seed
   - Timestamps and commit hashes

5. **ANALYSIS.ipynb or analysis.py:**
   - Deterministic metric calculation
   - Statistical tests (t-test, CIs)
   - Visualization (if applicable)

6. **REPORT.md:**
   - Conclusions with links to files
   - Kill-criteria pass/fail status
   - Limitations and deviations

7. **Commit hash + experiment release tag**

**Statistics Requirements:**
- N ≥ 30 seeds unless explicitly stated otherwise
- Confidence intervals (CIs) for all metrics
- Thresholds fixed upfront (no post-hoc tuning)

---

## Separation: Infrastructure vs. Cognitive Success

**Critical Rule:** Infrastructure success does NOT imply cognitive success.

### Infrastructure Success Indicators

- System runs without crashes
- GPU utilization maintained at target
- Checkpoints save/load correctly
- Metrics are collected
- Training completes

**These do NOT validate:**
- H1 (quaternary logic calibration)
- H2 (memory exact recall)
- H3 (regeneration without error accumulation)

### Cognitive Success Indicators

- H1: ECE/Brier improvement > 10%, false-confidence reduction
- H2: Exact recall ≥ 99.9%, latency within target class
- H3: Recovery rate ≥ 70%, error accumulation stable/negative

**Validation Required:**
- Explicit EXPERIMENT_SPEC.md with baselines
- N≥30 seeds with statistical significance
- Kill-criteria pass/fail determination

### Example: TRL-10.1

**Infrastructure Success:**
- ✅ 8-hour GPU training completed
- ✅ Fitness reached 1.0, diversity 96.47
- ✅ GPU utilization maintained at 75%

**Cognitive Success:**
- ❌ NOT VALIDATED — TRL-10.1 does not test H1, H2, or H3
- ❌ No qcore, no S={T,F,MY,MN}, no conflict_flag
- ❌ No PiStream validation before real data

**Conclusion:** TRL-10.1 validates knowledge integration infrastructure, not canonical cognitive hypotheses.

---

## TRL Ladder Requirements

### TRL Transition Rules

1. **Checklist completion:** All items in Definition of Done must be met
2. **Kill-criteria pass:** No kill-criterion may trigger
3. **Evidence standard:** Full EXPERIMENT_SPEC.md, SEEDS.md, RUN_COMMANDS.md, RESULTS, REPORT.md
4. **Reproducibility:** One-command run with N≥30 seeds (for TRL-3+)
5. **ADR for exceptions:** Any deviation from canonical roadmap requires ADR

### TRL-3 Paramecium MVP Definition of Done

- Deterministic 2D environment by ENV_PISTREAM
- Agent sensors with NOISE_PISTREAM
- qcore S={T,F,MY,MN} + conflict_flag with truth tables/tests
- Genome+VM interpretation documented and tested
- Evolution loop with MUT_DECISION/MUT_MAGNITUDE streams
- One-command experiment run with N≥30 fixed seeds
- RUN_COMMANDS.md, EXPERIMENT_SPEC.md, DECISIONS/, AGENTS_LOG.md present

### TRL Advancement Beyond Canonical Roadmap

**Rule:** TRL 7-10 (Cognitive & Knowledge Integration) are extensions beyond canonical TRL 1-5.

**Requirements:**
- ADR (R2) documenting rationale
- Explicit kill-criteria for new TRL levels
- Clear separation from Class 1 validation
- No claim that Class 2/3 success validates Class 1

---

## Anti-Self-Deception Rules

1. **No single-metric success:** Minimum metrics: utility, calibration/error, cost, robustness
2. **No post-hoc threshold tuning:** All thresholds fixed in EXPERIMENT_SPEC.md before experiment
3. **No black-box wins without mechanism:** Must explain HOW improvement occurs, not just THAT it occurs
4. **No infrastructure success as cognitive proof:** See separation above

---

## Reproducibility Requirements

**Contract:** Same commit + same seeds + same environment → same results (within tolerances)

**Requirements:**
- Operating system and toolchain versions recorded
- Deterministic seeding via PiStream (see SEED_POLICY.md)
- Fixed experiment protocol (EXPERIMENT_SPEC.md)
- No external dependencies (or locked versions)
- One-command run capability (for TRL-3+)

**Violation:** Non-reproducible results invalidate claims.

---

## Change Control

Any change affecting results must update EXPERIMENT_SPEC.md or an ADR.

**Change Classes:**
- **R0:** Refactor (no numerical change; requires regression verification)
- **R1:** Method change (new experiment version)
- **R2:** Hypothesis/kill-criteria change (roadmap revision)

**ADR Required For:**
- R2 changes
- Exceptions to canonical roadmap
- New TRL levels beyond TRL-5
- Hardware use before TRL5 closure

---

**RESEARCH_METHODOLOGY.md Status:** CANONICAL & OPERATIONAL  
**Next Review:** After kill-criteria updates or major methodology changes
