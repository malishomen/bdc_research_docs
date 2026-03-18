# Restricted BDC: Manuscript Draft

## 1. Introduction
This draft consolidates restricted BDC claims into a publication-ready narrative with explicit positive and negative results.

## 2. Theory Scope
- Restricted theory status: `restricted`
- Transition portability supported: `False`

## 3. Positive Results
- Supported claim count: `3`
- OOD core transfer supported: `True`
- OOD equilibrium transfer pass-rate: `0.8333`
- OOD hybrid transfer pass-rate: `1.0000`
- OOD role-count transfer pass-rate: `1.0000`

## 4. Negative Results
- Falsified claim count: `4`
- Portable low-dimensional transition law was not recovered under tested settings.

## 5. Engineering Implications
- Playbook supported: `True`
- Strategy selection accuracy: `1.0000`
- Mean performance delta vs default: `-0.0134`
- Mean cost reduction vs default: `1.2857`

## 6. Limitations
- Findings are validated under the defined synthetic and OOD benchmark envelopes, not all possible real-world distributions.
- Engineering value is strongest in hybrid-guided workflows and weaker as standalone architecture selection.

## 7. Reproducibility
- Core claims matrix, scope statement, and OOD/playbook summaries are linked in the section and figure manifests.
- Independent reproduction package is available from TASK-6920.

## 8. Conclusion
Restricted BDC remains scientifically defensible as a causal-equilibrium and architecture-prior framework with practical value in hybrid search settings.
