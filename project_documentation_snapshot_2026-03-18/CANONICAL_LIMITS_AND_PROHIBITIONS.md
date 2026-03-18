# BDC Canonical Limits and Prohibitions

**Version:** 1.0  
**Status:** CANONICAL  
**Last Updated:** 2026-01-27  
**Implements:** ARCHITECTURE.md autonomy boundaries and USER_INTERACTION_MODEL.md refusal rules

---

## Overview

This document explicitly lists forbidden task classes (perpetual motion, physics violations, etc.) and defines how BDC must explain impossibility.

**Core Principle:** BDC must refuse physically impossible tasks and explain why they are impossible.

---

## Forbidden Task Classes

### 1. Perpetual Motion Machines

**Definition:** Systems that produce more energy than they consume, or run indefinitely without energy input.

**Why Forbidden:**
- Violates **first law of thermodynamics** (conservation of energy)
- Energy cannot be created from nothing
- Friction and losses always consume energy

**BDC Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "Violates conservation of energy (first law of thermodynamics)",
    "explanation": "Perpetual motion machines are impossible because energy cannot be created from nothing. All systems lose energy to friction, heat, and other losses. To run indefinitely, a system would need infinite energy input or zero losses, both of which are physically impossible.",
    "alternatives": [
        "Use renewable energy sources (solar, wind, hydroelectric)",
        "Implement energy storage (batteries, flywheels, compressed air)",
        "Design high-efficiency systems to minimize losses"
    ]
}
```

### 2. Faster-Than-Light Communication

**Definition:** Sending information faster than the speed of light in vacuum (c ≈ 299,792,458 m/s).

**Why Forbidden:**
- Violates **special relativity** (speed of light is universal limit)
- Causality would be violated (effects before causes)
- Time dilation and length contraction prevent FTL travel

**BDC Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "Violates special relativity (speed of light is universal limit)",
    "explanation": "Faster-than-light communication is impossible because the speed of light in vacuum (c) is a fundamental constant that cannot be exceeded. Attempting to send information faster than light would violate causality (effects occurring before causes) and contradict experimental evidence from particle physics and astronomy.",
    "alternatives": [
        "Use quantum entanglement for correlation (not communication)",
        "Optimize communication protocols for near-light-speed transmission",
        "Use relay networks for long-distance communication"
    ]
}
```

### 3. Time Travel to the Past

**Definition:** Moving backward in time to change past events.

**Why Forbidden:**
- Violates **causality** (effects before causes)
- Creates **paradoxes** (grandfather paradox, bootstrap paradox)
- No experimental evidence supports backward time travel

**BDC Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "Violates causality and creates temporal paradoxes",
    "explanation": "Time travel to the past is impossible because it would violate causality (effects occurring before causes) and create logical paradoxes (e.g., grandfather paradox: if you kill your grandfather, you would never exist to kill him). While forward time travel is possible through time dilation (special relativity), backward time travel has no theoretical or experimental support.",
    "alternatives": [
        "Use time dilation for forward time travel (special relativity)",
        "Simulate past scenarios using historical data",
        "Analyze past events through records and evidence"
    ]
}
```

### 4. Division by Zero

**Definition:** Mathematical operations that divide by zero (e.g., 1/0, x/0).

**Why Forbidden:**
- **Mathematically undefined** (not a number)
- Leads to **infinite or undefined results**
- Breaks mathematical consistency

**BDC Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "Mathematically undefined (division by zero)",
    "explanation": "Division by zero is mathematically undefined. Any number divided by zero results in an undefined value, not infinity. Attempting to compute 1/0 or x/0 breaks mathematical consistency and leads to contradictions.",
    "alternatives": [
        "Use limit as denominator approaches zero: lim(x→0) 1/x",
        "Check for zero before division: if denominator != 0, then divide",
        "Use alternative formulations that avoid division by zero"
    ]
}
```

### 5. Logical Contradictions

**Definition:** Statements that are both true and false simultaneously (A and not-A).

**Why Forbidden:**
- Violates **law of non-contradiction** (A and not-A cannot both be true)
- Breaks logical consistency
- Makes reasoning impossible

**BDC Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "Violates law of non-contradiction",
    "explanation": "Logical contradictions are impossible. A statement cannot be both true and false simultaneously. The law of non-contradiction is fundamental to logic and reasoning. If A is true, then not-A must be false, and vice versa.",
    "alternatives": [
        "Clarify which statement is actually true",
        "Reformulate the problem to avoid contradiction",
        "Use paraconsistent logic (if applicable, with explicit justification)"
    ]
}
```

### 6. Infinite Precision

**Definition:** Computing with infinite precision or infinite accuracy.

**Why Forbidden:**
- **Computationally impossible** (finite memory, finite time)
- **Physically impossible** (quantum uncertainty, measurement limits)
- **Mathematically problematic** (real numbers are uncountable)

**BDC Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "Infinite precision is computationally and physically impossible",
    "explanation": "Infinite precision is impossible because: (1) computers have finite memory and cannot store infinite digits, (2) physical measurements have inherent uncertainty (quantum mechanics, measurement errors), and (3) real numbers are uncountable, making exact representation impossible. All computations must use finite precision (floating-point, fixed-point, or symbolic).",
    "alternatives": [
        "Use high-precision arithmetic (arbitrary precision libraries)",
        "Specify acceptable error tolerance",
        "Use symbolic computation for exact results (where applicable)"
    ]
}
```

### 7. Creating Information from Nothing

**Definition:** Generating information without input or prior knowledge.

**Why Forbidden:**
- Violates **information theory** (information cannot be created ex nihilo)
- Requires infinite knowledge or infinite computation
- Breaks conservation of information

**BDC Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "Violates information theory (information cannot be created from nothing)",
    "explanation": "Information cannot be created from nothing. All information must come from: (1) prior knowledge, (2) observations, (3) computations on existing data, or (4) external sources. Creating information ex nihilo would require infinite knowledge or violate the conservation of information principle.",
    "alternatives": [
        "Use existing knowledge bases and databases",
        "Collect information through observations or experiments",
        "Generate information through computations on existing data"
    ]
}
```

### 8. Predicting True Randomness

**Definition:** Predicting the outcome of truly random processes (quantum measurements, true random number generators).

**Why Forbidden:**
- **Fundamentally random** (no deterministic pattern)
- **Quantum uncertainty** (Heisenberg uncertainty principle)
- **Information-theoretic impossibility** (true randomness has no pattern)

**BDC Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "True randomness is fundamentally unpredictable",
    "explanation": "True randomness is fundamentally unpredictable. Quantum measurements, true random number generators, and other truly random processes have no deterministic pattern. The Heisenberg uncertainty principle states that certain pairs of properties (e.g., position and momentum) cannot be simultaneously known with arbitrary precision. Predicting true randomness would require violating quantum mechanics or information theory.",
    "alternatives": [
        "Use pseudorandom number generators (deterministic but unpredictable without seed)",
        "Estimate probability distributions (not individual outcomes)",
        "Use statistical methods to analyze random processes"
    ]
}
```

---

## How BDC Explains Impossibility

### Explanation Structure

**BDC MUST provide:**

1. **Reason:** Which law/principle is violated (one sentence)
2. **Explanation:** Why the task is impossible (2-3 sentences)
3. **Alternatives:** Suggest feasible alternatives (if applicable)

### Explanation Requirements

**MUST:**
- Reference specific physical laws or mathematical principles
- Explain why the law/principle applies
- Be clear and concise (avoid jargon when possible)
- Suggest alternatives (if applicable)

**MUST NOT:**
- Simply say "it's impossible" without explanation
- Use vague language ("doesn't work", "can't be done")
- Suggest alternatives that are also impossible
- Apologize excessively (be direct and factual)

### Example Explanations

#### Good Explanation:
```
"Perpetual motion machines are impossible because they violate the first law of thermodynamics (conservation of energy). Energy cannot be created from nothing, and all systems lose energy to friction, heat, and other losses. To run indefinitely, a system would need infinite energy input or zero losses, both of which are physically impossible."
```

#### Bad Explanation:
```
"It's impossible. Sorry, I can't do that."
```

---

## Detection Mechanisms

### Agent-Based Detection

**Process:**
1. All agents analyze task for impossibility
2. Agents vote on impossibility (T=possible, F=impossible, MY/MN=uncertain)
3. If majority votes F (impossible), BDC refuses
4. BDC identifies which law/principle is violated
5. BDC generates explanation

### Rule-Based Detection

**Predefined rules:**
- Check for perpetual motion keywords ("forever", "infinite energy", "no input")
- Check for FTL keywords ("faster than light", "instantaneous")
- Check for division by zero (denominator = 0)
- Check for logical contradictions (A and not-A)

### Validation

**All refusals must be validated:**
- Majority of agents agree on impossibility
- Specific law/principle identified
- Explanation is clear and accurate
- Alternatives are feasible (if suggested)

---

## Edge Cases

### Uncertain Impossibility (MY/MN)

**Scenario:** Agents are uncertain whether task is impossible.

**Handling:**
- If majority votes MY/MN (uncertain), BDC requests clarification
- BDC explains why uncertainty exists
- BDC asks user to clarify task or provide more context

**Response:**
```json
{
    "answer": null,
    "status": "uncertain",
    "reason": "Uncertain whether task is possible",
    "explanation": "Agents are uncertain whether this task is possible. 12/30 agents vote MY (maybe impossible), 10 vote T (possible), 8 vote F (impossible).",
    "request_clarification": [
        "What are the exact constraints?",
        "What is the success criterion?",
        "What is the expected outcome?"
    ]
}
```

### Partial Impossibility

**Scenario:** Task is partially impossible (some aspects violate physics, others are feasible).

**Handling:**
- BDC identifies which aspects are impossible
- BDC suggests modifications to make task feasible
- BDC offers to proceed with feasible aspects only

**Response:**
```json
{
    "answer": "Partially feasible",
    "confidence": 0.70,
    "status": "answered",
    "reasoning": "Task is partially feasible. Aspect A is possible, but Aspect B violates conservation of energy.",
    "impossible_aspects": [
        {
            "aspect": "Aspect B: Perpetual motion",
            "reason": "Violates conservation of energy",
            "suggestion": "Use external energy input"
        }
    ],
    "feasible_aspects": [
        "Aspect A: High-efficiency system (feasible with energy input)"
    ]
}
```

---

## Relationship to Other Documents

- **ARCHITECTURE.md:** Defines autonomy boundaries (implements)
- **USER_INTERACTION_MODEL.md:** Defines refusal process (implements)
- **RESEARCH_METHODOLOGY.md:** Defines validation requirements (references)

---

## Implementation Requirements

### Mandatory Components

1. **Impossibility detection:** System must detect forbidden tasks
2. **Law identification:** System must identify which law/principle is violated
3. **Explanation generation:** System must generate clear explanations
4. **Alternative suggestion:** System must suggest feasible alternatives (when applicable)

### Validation

**All refusals must be validated:**
- Majority of agents agree on impossibility
- Specific law/principle correctly identified
- Explanation is accurate and clear
- Alternatives are feasible (if suggested)

---

**CANONICAL_LIMITS_AND_PROHIBITIONS.md Status:** CANONICAL & OPERATIONAL  
**Next Review:** After new forbidden task classes are identified or explanation requirements change
