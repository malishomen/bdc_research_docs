from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping

from .genome import MultiRuleGenome, RuleGenome, RuleGenomeV1_5

LEGACY_COMPLEXITY_REGIMES = ("A", "B", "C", "D", "E")

CANONICAL_SELECTION_REGIMES = (
    "legacy_linear_control",
    "maintenance_cost",
    "energy_budget",
    "resource_allocation",
    "bounded_hybrid",
    "class_weighted_legacy",
    "no_penalty_diagnostic",
)

SELECTION_REGIME_ALIASES = {
    "A": "legacy_linear_control",
    "B": "maintenance_cost",
    "C": "energy_budget",
    "D": "class_weighted_legacy",
    "E": "no_penalty_diagnostic",
}

REQUIRED_R1_REGIMES = (
    "legacy_linear_control",
    "energy_budget",
    "maintenance_cost",
    "resource_allocation",
    "bounded_hybrid",
    "no_penalty_diagnostic",
)


@dataclass(frozen=True)
class SelectionPhysicsSpec:
    regime_id: str
    label: str
    description: str
    diagnostic: bool = False
    legacy_alias: str | None = None


SELECTION_PHYSICS_SPECS = {
    "legacy_linear_control": SelectionPhysicsSpec(
        regime_id="legacy_linear_control",
        label="Legacy linear control",
        description="Historical linear complexity penalty preserved as the explicit reboot control.",
        legacy_alias="A",
    ),
    "maintenance_cost": SelectionPhysicsSpec(
        regime_id="maintenance_cost",
        label="Maintenance cost",
        description="Recurring bounded maintenance burden using mean parameter load.",
        legacy_alias="B",
    ),
    "energy_budget": SelectionPhysicsSpec(
        regime_id="energy_budget",
        label="Energy budget",
        description="Energy-style bounded cost using square-root-normalized parameter load.",
        legacy_alias="C",
    ),
    "resource_allocation": SelectionPhysicsSpec(
        regime_id="resource_allocation",
        label="Resource allocation",
        description="Log-bounded allocation pressure over representational capacity.",
    ),
    "bounded_hybrid": SelectionPhysicsSpec(
        regime_id="bounded_hybrid",
        label="Bounded hybrid",
        description="Hybrid pressure combining maintenance and energy signals without zero-cost complexity.",
    ),
    "class_weighted_legacy": SelectionPhysicsSpec(
        regime_id="class_weighted_legacy",
        label="Class-weighted legacy",
        description="Historical class-weighted linear penalty retained for backward comparison.",
        legacy_alias="D",
    ),
    "no_penalty_diagnostic": SelectionPhysicsSpec(
        regime_id="no_penalty_diagnostic",
        label="No-penalty diagnostic",
        description="Accuracy-only diagnostic ceiling used as a floor/ceiling reference.",
        diagnostic=True,
        legacy_alias="E",
    ),
}

SUPPORTED_SELECTION_REGIMES = LEGACY_COMPLEXITY_REGIMES + tuple(
    regime for regime in CANONICAL_SELECTION_REGIMES if regime not in LEGACY_COMPLEXITY_REGIMES
)


def normalize_selection_regime_id(regime_id: str) -> str:
    normalized = regime_id.strip()
    canonical = SELECTION_REGIME_ALIASES.get(normalized, normalized)
    if canonical not in SELECTION_PHYSICS_SPECS:
        raise ValueError(f"Unsupported selection regime: {regime_id}")
    return canonical


def selection_physics_spec(regime_id: str) -> SelectionPhysicsSpec:
    return SELECTION_PHYSICS_SPECS[normalize_selection_regime_id(regime_id)]


def _genome_version(genome: RuleGenome) -> str:
    if isinstance(genome, MultiRuleGenome):
        return "v2"
    if isinstance(genome, RuleGenomeV1_5):
        return "v1_5"
    return "v1"


def parameter_count(genome: RuleGenome) -> int:
    if isinstance(genome, MultiRuleGenome):
        return 44
    if isinstance(genome, RuleGenomeV1_5):
        return 11
    return 8


def compute_selection_load_and_penalty(
    genome: RuleGenome,
    *,
    selection_regime: str,
    complexity_lambda: float,
    lambda_by_genome: Mapping[str, float] | None = None,
) -> tuple[SelectionPhysicsSpec, float, float]:
    spec = selection_physics_spec(selection_regime)
    base_complexity = genome.complexity()
    k = max(1, parameter_count(genome))

    if spec.regime_id == "legacy_linear_control":
        load = base_complexity
        penalty = complexity_lambda * load
    elif spec.regime_id == "maintenance_cost":
        load = base_complexity / k
        penalty = complexity_lambda * load
    elif spec.regime_id == "energy_budget":
        load = base_complexity / math.sqrt(k)
        penalty = complexity_lambda * load
    elif spec.regime_id == "resource_allocation":
        load = base_complexity / (1.0 + math.log2(max(2, k)))
        penalty = complexity_lambda * load
    elif spec.regime_id == "bounded_hybrid":
        maintenance_load = base_complexity / k
        energy_load = base_complexity / math.sqrt(k)
        load = 0.5 * maintenance_load + 0.5 * energy_load
        penalty = complexity_lambda * load
    elif spec.regime_id == "class_weighted_legacy":
        load = base_complexity
        version = _genome_version(genome)
        lambdas = dict(lambda_by_genome or {})
        class_lambda = float(lambdas.get(version, complexity_lambda))
        penalty = class_lambda * load
    else:
        load = base_complexity
        penalty = 0.0

    return spec, load, penalty
