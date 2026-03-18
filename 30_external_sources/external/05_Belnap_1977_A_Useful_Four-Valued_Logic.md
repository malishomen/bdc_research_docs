# A Useful Four-Valued Logic

**Author:** Nuel D. Belnap Jr.
**Year:** 1977
**Source:** Chapter in *Modern Uses of Multiple-Valued Logic* (ed. J. M. Dunn, G. Epstein), Episteme vol. 2, Springer, Dordrecht, pp. 5–37.
**DOI:** 10.1007/978-94-010-1161-7_2
**Citations:** ~1621 (Semantic Scholar)
**Status:** PDF behind Springer paywall. Content reconstructed из открытых источников.

---

## Core Argument (TLDR)

A sophisticated question-answering machine that has the capability of making inferences from its data base should employ a certain four-valued logic. The motivating consideration is that minor inconsistencies in its data should not be allowed to lead (as in classical two-valued logic) to irrelevant conclusions.

## Context and Motivation

Belnap's paper addresses the fundamental problem of reasoning with inconsistent or incomplete information. In classical logic, a single contradiction renders everything provable (the principle of explosion, *ex contradictione quodlibet*). This makes classical logic unsuitable for databases and knowledge systems where:

1. Data may come from multiple independent sources that occasionally contradict each other.
2. Information may be incomplete — neither a proposition nor its negation is known.

Belnap proposes a **four-valued logic** where a proposition can take one of four truth values:

| Value | Symbol | Meaning |
|-------|--------|---------|
| **True** | **T** | Told only True |
| **False** | **F** | Told only False |
| **Both** | **B** | Told both True and False (contradiction) |
| **None** | **N** | Told neither True nor False (gap) |

## The Four-Valued Lattice

Belnap organizes these four values in **two distinct orderings**:

### 1. Truth ordering (≤_t)
F ≤_t N ≤_t T
F ≤_t B ≤_t T

This is the logical ordering where F is the least true and T is the most true.

### 2. Information ordering (≤_k — "knowledge")
N ≤_k T ≤_k B
N ≤_k F ≤_k B

Here N ("None") has the least information and B ("Both") has the most.

The four values form a **bilattice** — a structure with two lattice orderings that interact in specific ways.

## Logical Operations

### Negation (¬)
- ¬T = F
- ¬F = T
- ¬B = B (negation of a contradiction is still a contradiction)
- ¬N = N (negation of unknown is still unknown)

### Conjunction (∧) — meet in truth ordering
| ∧ | T | F | B | N |
|---|---|---|---|---|
| T | T | F | B | N |
| F | F | F | F | F |
| B | B | F | B | F |
| N | N | F | F | N |

### Disjunction (∨) — join in truth ordering
| ∨ | T | F | B | N |
|---|---|---|---|---|
| T | T | T | T | T |
| F | T | F | B | N |
| B | T | B | B | T |
| N | T | N | T | N |

## Key Properties

1. **Containment of contradictions:** If a database contains both P and ¬P, we get B for P, but this does not infect unrelated propositions.
2. **No explosion:** From B(P), we cannot derive T(Q) for arbitrary Q.
3. **Truth-functionality preserved:** All operations are defined truth-functionally (value of compound depends only on values of components).
4. **De Morgan laws hold:** ¬(A ∧ B) = ¬A ∨ ¬B and ¬(A ∨ B) = ¬A ∧ ¬B.
5. **Double negation:** ¬¬A = A for all four values.

## Entailment

Belnap defines entailment via the truth ordering: A entails B if whenever A is at least as true as T (i.e., T or B), then B is also at least as true as T.

Valid entailment: A ∧ B ⊨ A
Invalid: A, ¬A ⊨ B (explosion is blocked)

## Influence and Applications

### In Computer Science
- Database systems with inconsistent sources
- Default reasoning and non-monotonic logic
- Paraconsistent logic programming
- Knowledge representation under uncertainty

### In Philosophy
- Foundation for relevance logic and paraconsistent logic
- Bridge between classical logic and practical reasoning
- Formalization of "degrees of truth" without fuzzy logic

### In BDC Project Context
Belnap's four-valued logic is foundational for the BDC (Bio Digital Core) quaternary logic system. BDC extends the idea of four-valued computation to a bio-inspired processing architecture, where the four values map to quaternary states analogous to DNA nucleotide encoding (A, T, G, C). The containment of contradictions is particularly relevant for BDC's error-handling model.

## Relation to Other Work in the Dissertation

- **Bimbo (06):** SEP article on many-valued logic provides broader context for four-valued systems.
- **Geisel/Freeman (07, 08):** Reed-Solomon and forward error correction parallel the error-containment property.
- **BDC Designer:** Uses four-valued state logic internally for confidence signaling.

---

## Bibliography

Belnap, N. D. (1977). A Useful Four-Valued Logic. In J. M. Dunn & G. Epstein (Eds.), *Modern Uses of Multiple-Valued Logic* (pp. 5–37). Springer, Dordrecht. https://doi.org/10.1007/978-94-010-1161-7_2

Reprinted in: Omori, H. & Wansing, H. (Eds.) (2019). *New Essays on Belnap-Dunn Logic*. Springer. https://doi.org/10.1007/978-3-030-31136-0_5
