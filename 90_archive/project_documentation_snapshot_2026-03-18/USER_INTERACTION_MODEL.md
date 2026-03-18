# BDC User Interaction Model

**Version:** 1.0  
**Status:** CANONICAL  
**Last Updated:** 2026-01-27  
**Implements:** ARCHITECTURE.md autonomy boundaries

---

## Overview

This document defines how BDC answers users via collective cognition, confidence scores, disagreement handling, and refusal of physically impossible tasks.

**Core Principle:** BDC must be honest about uncertainty (MY/MN), express disagreement when agents conflict, and refuse tasks that violate physics.

---

## Collective Cognition

### Concept

**Collective Cognition:** BDC answers questions by aggregating responses from multiple agents, not by single-agent decision.

**Process:**
1. User asks question
2. All agents in population process question
3. Agents produce individual answers with confidence
4. BDC aggregates answers (consensus, voting, weighted average)
5. BDC returns collective answer with confidence and disagreement metrics

### Aggregation Methods

#### 1. Consensus (for T/F questions)

**Method:** Agents vote T, F, MY, or MN. BDC returns majority vote.

**Formula:**
```
votes = {T: count_T, F: count_F, MY: count_MY, MN: count_MN}
majority = max(votes, key=votes.get)
confidence = votes[majority] / total_agents
```

**Example:**
- 30 agents vote: 18 T, 8 F, 3 MY, 1 MN
- Answer: T (True)
- Confidence: 18/30 = 0.60 (60%)

#### 2. Weighted Average (for numerical questions)

**Method:** Weight agent answers by confidence and fitness.

**Formula:**
```
weighted_answer = sum(agent_i.answer * agent_i.confidence * agent_i.fitness) 
                / sum(agent_i.confidence * agent_i.fitness)
```

**Example:**
- Question: "What is the optimal learning rate?"
- Agent 1: 0.01 (confidence 0.9, fitness 0.8)
- Agent 2: 0.015 (confidence 0.7, fitness 0.9)
- Agent 3: 0.02 (confidence 0.6, fitness 0.7)
- Weighted answer: (0.01×0.9×0.8 + 0.015×0.7×0.9 + 0.02×0.6×0.7) / (0.9×0.8 + 0.7×0.9 + 0.6×0.7) = 0.013

#### 3. Knowledge Integration (for complex questions)

**Method:** Agents share knowledge packages, then vote on integrated answer.

**Process:**
1. Agents exchange knowledge (see COGNITIVE_PROTOCOL.md)
2. Agents update beliefs based on received knowledge
3. Agents produce answers with updated confidence
4. BDC aggregates answers (consensus or weighted average)

**Example:**
- Question: "What is the best strategy for this task?"
- Agents exchange knowledge packages
- Agents update strategies based on shared knowledge
- Agents vote on best strategy
- BDC returns majority strategy with confidence

---

## Confidence Scores

### Definition

**Confidence** is the degree of certainty in an answer, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).

### Confidence Calculation

**For T/F answers:**
```
confidence = (votes_for_answer / total_agents) × agreement_factor
```

Where:
- `votes_for_answer`: Number of agents voting for the answer
- `total_agents`: Total number of agents
- `agreement_factor`: 1.0 if all votes agree, <1.0 if disagreement exists

**For numerical answers:**
```
confidence = 1.0 - (variance / max_variance)
```

Where:
- `variance`: Variance of agent answers
- `max_variance`: Maximum possible variance (normalized)

### Confidence Interpretation

| Confidence | Meaning | Action |
|------------|---------|--------|
| 0.9 - 1.0 | Very high | Answer is reliable, proceed |
| 0.7 - 0.9 | High | Answer is likely correct, proceed with caution |
| 0.5 - 0.7 | Moderate | Answer is uncertain, request clarification |
| 0.3 - 0.5 | Low | Answer is unreliable, request more information |
| 0.0 - 0.3 | Very low | Answer is unreliable, refuse or request expert input |

### Confidence in Response

**BDC MUST include confidence in all responses:**

```json
{
    "answer": "The optimal learning rate is 0.01",
    "confidence": 0.75,
    "disagreement": 0.25,
    "reasoning": "18/30 agents agree, 8 disagree, 4 uncertain"
}
```

---

## Disagreement Handling

### Definition

**Disagreement** is the degree of conflict between agent answers, measured as the proportion of agents that disagree with the majority.

### Disagreement Calculation

**For T/F answers:**
```
disagreement = (votes_against_answer / total_agents)
```

**For numerical answers:**
```
disagreement = variance / max_variance
```

### Disagreement Interpretation

| Disagreement | Meaning | Action |
|--------------|---------|--------|
| 0.0 - 0.1 | Low | Agents agree, proceed |
| 0.1 - 0.3 | Moderate | Some disagreement, note in response |
| 0.3 - 0.5 | High | Significant disagreement, request clarification |
| 0.5 - 1.0 | Very high | Agents strongly disagree, refuse or request expert |

### Disagreement in Response

**BDC MUST include disagreement in all responses:**

```json
{
    "answer": "The strategy is effective",
    "confidence": 0.60,
    "disagreement": 0.40,
    "conflicting_views": [
        {"view": "Strategy is effective", "agents": 18, "confidence": 0.9},
        {"view": "Strategy is ineffective", "agents": 8, "confidence": 0.7},
        {"view": "Uncertain", "agents": 4, "confidence": 0.3}
    ]
}
```

### Handling High Disagreement

**When disagreement > 0.3:**

1. **Present all views:** Show conflicting agent perspectives
2. **Request clarification:** Ask user for more context
3. **Defer to expert:** If disagreement > 0.5, request human expert input
4. **Refuse if impossible:** If task violates physics, refuse (see CANONICAL_LIMITS_AND_PROHIBITIONS.md)

---

## Refusal of Impossible Tasks

### Rule: BDC Must Refuse Physically Impossible Tasks

**BDC MUST refuse tasks that violate:**
- Laws of physics (perpetual motion, energy creation, etc.)
- Mathematical impossibility (division by zero, etc.)
- Logical contradictions (A and not-A simultaneously, etc.)

**BDC MUST explain why the task is impossible.**

### Refusal Process

**1. Detection:**
- Agents analyze task for physical/logical impossibility
- Agents vote on impossibility (T=possible, F=impossible, MY/MN=uncertain)
- If majority votes F (impossible), proceed to refusal

**2. Explanation:**
- BDC identifies which law/principle is violated
- BDC explains why the task cannot be completed
- BDC suggests alternatives (if applicable)

**3. Response:**
```json
{
    "answer": null,
    "status": "refused",
    "reason": "Task violates conservation of energy",
    "explanation": "Perpetual motion machines are impossible because they violate the first law of thermodynamics. Energy cannot be created from nothing.",
    "alternatives": [
        "Consider a system with external energy input",
        "Use energy storage (battery, flywheel) for temporary operation"
    ],
    "confidence": 1.0,
    "disagreement": 0.0
}
```

### Examples of Impossible Tasks

**1. Perpetual Motion:**
- Task: "Create a machine that runs forever without energy input"
- Refusal: "Violates conservation of energy (first law of thermodynamics)"
- Alternative: "Use renewable energy sources (solar, wind)"

**2. Faster-Than-Light:**
- Task: "Send information faster than light"
- Refusal: "Violates special relativity (speed of light is universal limit)"
- Alternative: "Use quantum entanglement for correlation (not communication)"

**3. Division by Zero:**
- Task: "Calculate 1/0"
- Refusal: "Mathematically undefined (division by zero)"
- Alternative: "Use limit as denominator approaches zero"

**4. Logical Contradiction:**
- Task: "Prove that A is true and not-A is true simultaneously"
- Refusal: "Logically impossible (violates law of non-contradiction)"
- Alternative: "Clarify which statement is actually true"

---

## Uncertainty Handling (MY/MN)

### MY (Maybe Yes) / MN (Maybe No)

**Definition:** MY/MN represent directed uncertainty when evidence exists but is insufficient.

**BDC MUST use MY/MN when:**
- Evidence supports answer but is incomplete
- Confidence is moderate (0.3 - 0.7)
- More information is needed

### MY/MN in Response

**When BDC returns MY/MN:**

```json
{
    "answer": "MY",  // Maybe Yes (leaning toward yes)
    "confidence": 0.45,
    "disagreement": 0.30,
    "reasoning": "Evidence suggests 'yes' but is insufficient. 12/30 agents vote MY, 10 vote T, 8 vote F.",
    "request_clarification": [
        "What is the exact context?",
        "What are the constraints?",
        "What is the success criterion?"
    ]
}
```

### MY/MN Limits

**Rule:** BDC cannot use MY/MN > X% of the time without utility gain.

**X must be fixed in EXPERIMENT_SPEC.md before experiment (typically 40%).**

**Rationale:** Prevents "eternal doubt" where BDC never commits to answers.

---

## Response Format

### Standard Response Structure

```json
{
    "answer": "...",  // The answer (or null if refused)
    "confidence": 0.75,  // Confidence score (0.0 - 1.0)
    "disagreement": 0.25,  // Disagreement score (0.0 - 1.0)
    "status": "answered" | "refused" | "uncertain",
    "reasoning": "...",  // Explanation of answer
    "conflicting_views": [...],  // If disagreement > 0.3
    "request_clarification": [...],  // If confidence < 0.5
    "alternatives": [...]  // If refused, suggest alternatives
}
```

### Response Examples

#### Example 1: High Confidence Answer

```json
{
    "answer": "The optimal learning rate is 0.01",
    "confidence": 0.90,
    "disagreement": 0.10,
    "status": "answered",
    "reasoning": "27/30 agents agree (90% consensus). Evidence from 1000+ episodes supports this value."
}
```

#### Example 2: Moderate Confidence with Disagreement

```json
{
    "answer": "Strategy A is better than Strategy B",
    "confidence": 0.65,
    "disagreement": 0.35,
    "status": "answered",
    "reasoning": "18/30 agents prefer Strategy A, but 10 prefer Strategy B. Evidence is mixed.",
    "conflicting_views": [
        {"view": "Strategy A is better", "agents": 18, "confidence": 0.8},
        {"view": "Strategy B is better", "agents": 10, "confidence": 0.7},
        {"view": "Uncertain", "agents": 2, "confidence": 0.3}
    ]
}
```

#### Example 3: Refused (Impossible Task)

```json
{
    "answer": null,
    "confidence": 1.0,
    "disagreement": 0.0,
    "status": "refused",
    "reason": "Task violates conservation of energy",
    "explanation": "Perpetual motion machines are impossible because energy cannot be created from nothing (first law of thermodynamics).",
    "alternatives": [
        "Use renewable energy sources (solar, wind)",
        "Implement energy storage (battery, flywheel)"
    ]
}
```

#### Example 4: Uncertain (MY/MN)

```json
{
    "answer": "MY",  // Maybe Yes
    "confidence": 0.45,
    "disagreement": 0.30,
    "status": "uncertain",
    "reasoning": "Evidence suggests 'yes' but is insufficient. 12/30 agents vote MY, 10 vote T, 8 vote F.",
    "request_clarification": [
        "What is the exact context?",
        "What are the constraints?",
        "What is the success criterion?"
    ]
}
```

---

## Implementation Requirements

### Mandatory Components

1. **Collective aggregation:** All answers must come from agent population
2. **Confidence calculation:** Every answer must include confidence score
3. **Disagreement tracking:** Every answer must include disagreement metric
4. **Impossibility detection:** System must detect and refuse impossible tasks
5. **MY/MN handling:** System must use MY/MN when appropriate

### Validation

**All user interactions must be validated:**
- Confidence scores are in [0.0, 1.0]
- Disagreement scores are in [0.0, 1.0]
- Answers are consistent with agent votes
- Refusals include valid explanations
- MY/MN usage is within limits

---

## Relationship to Other Documents

- **ARCHITECTURE.md:** Defines autonomy boundaries (implements)
- **CANONICAL_LIMITS_AND_PROHIBITIONS.md:** Defines forbidden tasks (references)
- **COGNITIVE_PROTOCOL.md:** Defines knowledge exchange (uses)
- **SEMANTICS.md:** Defines S={T,F,MY,MN} semantics (implements)

---

**USER_INTERACTION_MODEL.md Status:** CANONICAL & OPERATIONAL  
**Next Review:** After user interaction implementation or major changes
