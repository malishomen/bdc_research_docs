# Project Knowledge Consolidated: BIO-DIGITAL CORE (BDC)

**Date:** 2026-02-27

## Current canonical docs

- `docs/project/project_main_doc.md` - master project document.
- `docs/project/project_roadmap.md` - active roadmap.
- `CANON.md` - top-level process canon.
- `ARCHITECTURE.md` - architecture structure and invariants.
- `SEMANTICS.md` - quaternary semantics and system terms.
- `KILL_CRITERIA.yaml` - canonical kill criteria and line status.
- `REPRODUCIBILITY.md` - reproducibility contract.
- `VERSIONING.md` - versioning and change discipline.

## 1. Project Purpose and Core Concepts

The **BIO-DIGITAL CORE (BDC)** is a research platform for simulating and studying the evolution of "digital organisms" with developing cognitive architectures. The project is highly disciplined, emphasizing reproducible experiments, strict validation, and evidence-based development.

The core innovation of BDC is **Quaternary Logic**, a system that treats uncertainty as a first-class computational state. Instead of just TRUE and FALSE, it uses a set of four states: `S={T, F, MY, MN}` (True, False, Maybe-Yes, Maybe-No), which allows agents to express uncertainty without halting computation.

## 2. Architecture and Methodology

The project is structured into three distinct **Task Classes**:

*   **Class 1 (Core Validation):** Focuses on validating the foundational hypotheses of the project, including the core logic (`qcore`), a "DNA-inspired" memory system, and a simple "Paramecium" agent. This class is restricted to CPU-only simulations to ensure deterministic results.
*   **Class 2 (Cognitive Co-Evolution):** Explores how agents interact, develop collective intelligence, and self-organize. This is where higher-level cognitive functions are developed and tested.
*   **Class 3 (Knowledge Integration):** Involves training agents on real-world data, such as the Wikipedia corpus, to study knowledge extraction and population dynamics. This is the only class where GPU acceleration is permitted.

The project follows a strict methodology with several key principles:
*   **Reproducibility:** A paramount rule is that given the same initial seeds and environment, the simulation must produce the same results. This is achieved through the use of a deterministic pseudo-random number generator called **PiStream**.
*   **Kill-Criteria:** Every experiment must have pre-defined "kill-criteria" — conditions under which the experiment is considered a failure and is stopped.
*   **Evidence-Based Development:** All claims and results must be backed by detailed experiment specifications, run commands, results, and reports.
*   **Separation of Concerns:** The core components of the system (`qcore`, `memory`, `env`, `agent`, `evolution`) are kept isolated to prevent hidden dependencies.

## 3. The Evolution Engine

The evolution of digital organisms is driven by the **Evolution Engine**, which is based on three main forces:

*   **Selection:** Agents with higher "fitness" are more likely to be selected for reproduction. The project defines specific fitness functions for different task classes.
*   **Mutation:** Variation is introduced into the population through mutations. All mutations are deterministic and are controlled by the `PiStream` to ensure reproducibility. The system has learned from a previous version (v1) and now uses a higher mutation rate and magnitude (in v2) to avoid stagnation.
*   **Diversity Enforcement:** To prevent the population from becoming too homogeneous and getting stuck in local optima, the system has explicit mechanisms to maintain diversity. These include "immigration" of new random agents and "mutation boosts".

A **Population Governor** automatically monitors the simulation and stops it if certain criteria are met, suchs as low signal-to-noise ratio, or a collapse in diversity.

## 4. Code Implementation

The concepts from the documentation are clearly reflected in the project's source code:

*   **`agent/`**: This directory contains the basic building blocks of the digital organisms.
    *   `genome.py`: Defines the simple, deterministic genome of the agents, which is initialized and mutated using the `PiStream`.
    *   `controller.py`: Contains the agent's decision-making logic.

*   **`evolution/`**: This directory implements the core evolutionary loop.
    *   `mutate.py` and `select.py`: Contain the implementation of the mutation and selection mechanisms.
    *   `pistream_v2_engine.py` and `pistream_v2_streams.py`: Provide the deterministic randomness that is crucial for reproducibility.

*   **`memory/`**: This directory contains the implementation of the "DNA-inspired" memory system.
    *   `core.py`: The main file for the memory system.
    *   `ecc.py`: Likely implements an Error Correction Code, which supports the "DNA-inspired" nature of the memory.

*   **`cognitive/`**: This directory implements the higher-level cognitive functions for Class 2 and 3 tasks.
    *   `core.py`: Defines the `CognitiveAgent` class, which has a complex internal state, including `CognitiveMemory`, `Beliefs`, and states like "exploring", "learning", and "teaching". This is the core of the co-evolutionary framework.
    *   `gpu_training_engine.py` and related files: These are used for the Class 3 knowledge integration tasks, which involve training on large datasets.

## 5. Summary

The Bio-Digital Core project is a sophisticated and highly disciplined research platform for studying the evolution of digital organisms. Its unique approach to handling uncertainty, its strict emphasis on reproducibility, and its multi-layered architecture make it a powerful tool for research in artificial life and artificial intelligence. The project is well-documented, and the code appears to be a clear and direct implementation of the concepts described in the documentation.
