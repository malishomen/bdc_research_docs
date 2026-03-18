# EXPERIMENT: Quaternary Logic — Delayed Decision Architecture

**Version:** 1.0  
**Status:** RESEARCH SPECIFICATION  
**Last Updated:** 2026-01-27  
**Type:** Research Direction  
**Related:** SEMANTICS.md, qcore/, ARCHITECTURE.md

---

## Executive Summary

Quaternary logic extends binary logic with two intermediate states (`MAYBE_YES`, `MAYBE_NO`) to enable **delayed decision-making** where agents can express uncertainty without committing to a final answer. This experiment explores the computational and cognitive benefits of allowing agents to defer binary decisions until sufficient evidence accumulates.

**Core Innovation:** GPU explores probability space and hypotheses, CPU orchestrates final binary decisions. This separation enables parallel exploration without premature commitment.

---

## Motivation: Delayed Decision-Making

### Problem Statement

**Binary Logic Limitation:**
- Agents must commit to YES/NO immediately.
- Uncertainty forced into binary choice (often wrong).
- No mechanism to express "I need more information."

**Quaternary Logic Solution:**
- Agents can express uncertainty explicitly (`MAYBE_YES`, `MAYBE_NO`).
- Decisions deferred until sufficient evidence accumulates.
- Final binary decision made by CPU orchestrator after GPU exploration.

### Use Cases

1. **Ambiguous Input:** Agent receives unclear signal → responds `MAYBE_YES` → GPU explores probabilities → CPU decides YES/NO.
2. **Insufficient Evidence:** Agent needs more data → responds `MAYBE_NO` → GPU gathers evidence → CPU decides YES/NO.
3. **Conflicting Signals:** Agent receives contradictory inputs → responds `MAYBE_YES` or `MAYBE_NO` → GPU resolves conflict → CPU decides YES/NO.

---

## Quaternary State Semantics

### Four States: S = {NO, YES, MAYBE_YES, MAYBE_NO}

| State | Symbol | Meaning | Commitment Level |
|-------|--------|---------|-----------------|
| **NO** | `F` | Definite negative | High (100%) |
| **YES** | `T` | Definite positive | High (100%) |
| **MAYBE_YES** | `MY` | Probable positive | Low (deferred) |
| **MAYBE_NO** | `MN` | Probable negative | Low (deferred) |

### State Transitions

**Allowed Transitions:**
- `MY` → `YES` (evidence accumulates)
- `MY` → `NO` (evidence contradicts)
- `MN` → `NO` (evidence accumulates)
- `MN` → `YES` (evidence contradicts)
- `YES` → `MY` (new uncertainty)
- `NO` → `MN` (new uncertainty)

**Forbidden Transitions:**
- `YES` → `NO` (direct flip requires `MY` or `MN` intermediate)
- `NO` → `YES` (direct flip requires `MY` or `MN` intermediate)

**Rationale:** Direct YES↔NO flips indicate contradiction. Intermediate states (`MY`, `MN`) required for smooth transitions.

---

## Architecture: GPU Exploration + CPU Orchestration

### Role Separation

#### GPU Role: Probability Exploration

**Responsibilities:**
- Explore probability space for `MAYBE_YES` / `MAYBE_NO` states.
- Generate hypotheses and test them in parallel.
- Compute confidence scores for each hypothesis.
- Return probability distributions to CPU.

**Operations:**
- **Hypothesis Generation:** Create candidate explanations for uncertain states.
- **Probability Computation:** Calculate likelihood of each hypothesis.
- **Parallel Exploration:** Test multiple hypotheses simultaneously.
- **Confidence Scoring:** Assign confidence to each hypothesis.

**Output:** Probability distribution over {YES, NO} for each `MY`/`MN` state.

#### CPU Role: Binary Orchestration

**Responsibilities:**
- Receive probability distributions from GPU.
- Make final binary decisions (YES/NO).
- Coordinate multiple agents' decisions.
- Enforce consistency across decision chain.

**Operations:**
- **Decision Thresholding:** Convert probabilities to binary decisions.
- **Consistency Checking:** Ensure decisions are logically consistent.
- **Conflict Resolution:** Resolve conflicts between agents.
- **Final Output:** Binary YES/NO for each agent.

**Output:** Final binary decisions for all agents.

### Computational Flow

```
Agent receives input
    ↓
Agent responds: MY or MN (if uncertain)
    ↓
GPU explores probabilities:
    - Generate hypotheses
    - Compute probabilities
    - Score confidence
    ↓
GPU returns: P(YES), P(NO) for each MY/MN state
    ↓
CPU orchestrates:
    - Threshold probabilities
    - Resolve conflicts
    - Make final decisions
    ↓
CPU outputs: Binary YES/NO for each agent
```

---

## Metrics and Validation

### Entropy Metric

**Purpose:** Measure uncertainty in quaternary state distribution.

**Formula:**
```
entropy = -Σ P(state) * log2(P(state))
```

**Interpretation:**
- High entropy: Many `MY`/`MN` states (high uncertainty).
- Low entropy: Many `YES`/`NO` states (low uncertainty).

**Target:** Entropy should decrease over time as decisions are made.

### False-Confidence Rate

**Purpose:** Measure how often agents commit to wrong decisions prematurely.

**Formula:**
```
false_confidence_rate = (premature_commits / total_decisions) * 100%
```

**Premature Commit:** Agent commits to YES/NO before sufficient evidence, then flips to opposite.

**Target:** False-confidence rate < 10% (vs. baseline binary logic).

### Decision Latency

**Purpose:** Measure time from `MY`/`MN` to final `YES`/`NO`.

**Formula:**
```
decision_latency = time(final_decision) - time(initial_uncertainty)
```

**Target:** Decision latency < threshold (TBD in experiment spec).

### Accuracy Improvement

**Purpose:** Compare quaternary logic accuracy vs. binary logic baseline.

**Formula:**
```
accuracy_improvement = (quaternary_accuracy - binary_accuracy) / binary_accuracy * 100%
```

**Target:** Accuracy improvement > 5% over binary baseline.

---

## Experimental Design

### Hypothesis

**H1:** Quaternary logic with GPU exploration and CPU orchestration improves decision accuracy and reduces false-confidence rate compared to binary logic.

### Experimental Setup

**Baseline:** Binary logic (YES/NO only).

**Treatment:** Quaternary logic (YES/NO/MY/MN) with GPU exploration and CPU orchestration.

**Population:** 30 agents (TRL-3 requirement).

**Tasks:**
- Ambiguous input classification.
- Insufficient evidence scenarios.
- Conflicting signal resolution.

### Kill-Criteria

**1. Accuracy Regression:**
```
IF quaternary_accuracy < binary_accuracy:
    KILL: Quaternary logic degrades accuracy
```

**2. False-Confidence Increase:**
```
IF false_confidence_rate > baseline * 1.1:
    KILL: Quaternary logic increases false confidence
```

**3. Decision Latency Explosion:**
```
IF decision_latency > threshold * 10:
    KILL: Quaternary logic causes unacceptable latency
```

**4. Entropy Non-Decrease:**
```
IF entropy does not decrease over time:
    KILL: Quaternary logic fails to resolve uncertainty
```

### Success Criteria

**Minimum Requirements:**
- Accuracy improvement > 5% over binary baseline.
- False-confidence rate < 10%.
- Decision latency < threshold.
- Entropy decreases over time.

**Target Metrics:**
- Accuracy improvement > 10%.
- False-confidence rate < 5%.
- Decision latency < threshold / 2.
- Entropy decreases smoothly.

---

## Relationship to BDC Architecture

### Task Class Alignment

**Quaternary Logic belongs to Class 1 (Core Validation):**
- Validates foundational hypothesis (H1: Quaternary logic improves calibration).
- CPU/simulation only (GPU used for exploration, not core validation).
- PiStream tests, exact recall, recovery rate.

### Integration Points

- **SEMANTICS.md:** Defines quaternary semantics S={T,F,MY,MN} and conflict_flag.
- **qcore/:** Implements quaternary logic operations.
- **ARCHITECTURE.md:** Implements Class 1 requirements.
- **RESEARCH_METHODOLOGY.md:** Follows kill-criteria validation.

### Separation from PiStream

**Important:** Quaternary logic is a **separate research direction** from PiStream v3.

- **PiStream v3:** Evolution and diversity mechanisms.
- **Quaternary Logic:** Decision-making and uncertainty handling.

**No Direct Dependency:** Quaternary logic can be validated independently of PiStream v3.

---

## Implementation Considerations

### GPU Exploration Implementation

**Approach 1: Parallel Hypothesis Testing**
- Generate N hypotheses in parallel.
- Test each hypothesis on GPU.
- Return probability distribution.

**Approach 2: Monte Carlo Sampling**
- Sample probability space.
- Compute likelihood for each sample.
- Aggregate samples into distribution.

**Approach 3: Neural Network Probability Estimation**
- Train network to estimate P(YES|MY) and P(NO|MN).
- Use network for fast probability computation.

### CPU Orchestration Implementation

**Approach 1: Threshold-Based**
- Set threshold (e.g., P(YES) > 0.7 → YES).
- Convert probabilities to binary decisions.

**Approach 2: Bayesian Inference**
- Use Bayesian updating to combine probabilities.
- Make decisions based on posterior probabilities.

**Approach 3: Consensus Voting**
- Multiple agents vote on decisions.
- CPU aggregates votes and makes final decision.

---

## Future Research Directions

### Extensions

1. **Tertiary Logic:** Three states (YES, NO, UNCERTAIN) as simplification.
2. **Fuzzy Logic:** Continuous probability values instead of discrete states.
3. **Multi-Agent Coordination:** How agents coordinate `MY`/`MN` states.
4. **Temporal Logic:** How `MY`/`MN` states evolve over time.

### Research Questions

1. **Optimal Thresholds:** What probability thresholds maximize accuracy?
2. **GPU Efficiency:** How to optimize GPU exploration for speed?
3. **CPU Orchestration:** What orchestration strategy minimizes conflicts?
4. **Entropy Dynamics:** How does entropy evolve in quaternary systems?

---

## References

- **SEMANTICS.md:** Quaternary logic semantics and conflict_flag.
- **qcore/:** Quaternary logic implementation.
- **ARCHITECTURE.md:** BDC architecture and task classes.
- **RESEARCH_METHODOLOGY.md:** Kill-criteria and validation standards.

---

**EXPERIMENT_QUATERNARY_LOGIC.md Status:** RESEARCH SPECIFICATION  
**Next Review:** After initial experiments or major design changes  
**Implementation Priority:** MEDIUM (separate from PiStream v3)
