from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory import build_controlled_sequence_memory_dataset
from evolution.micro_tasks.sequence_memory_mechanism import mechanism_scorecard
from evolution.micro_tasks.sequence_memory_mechanism_gate import (
    build_slice_rows,
    build_variant_rows,
    mechanism_gate_decision,
)


def test_mechanism_gate_approves_measured_candidate() -> None:
    dataset = build_controlled_sequence_memory_dataset(seed=20260319, size=128)
    scorecard = mechanism_scorecard(dataset, trace_width=5)
    decision = mechanism_gate_decision(scorecard)
    assert decision["verdict"] == "APPROVE_MECHANISM_CONTINUATION"


def test_variant_rows_include_candidate_and_controls() -> None:
    dataset = build_controlled_sequence_memory_dataset(seed=20260319, size=32)
    scorecard = mechanism_scorecard(dataset, trace_width=5)
    rows = build_variant_rows(scorecard)
    assert {row["variant_id"] for row in rows} == {
        "bounded_working_memory_candidate",
        "majority_symbol_predictor",
        "trivial_last_symbol_memory",
    }


def test_slice_rows_cover_all_gaps() -> None:
    dataset = build_controlled_sequence_memory_dataset(seed=20260319, size=64)
    scorecard = mechanism_scorecard(dataset, trace_width=5)
    rows = build_slice_rows(scorecard)
    gap_ids = {row["slice_id"] for row in rows}
    assert gap_ids == {"gap_2", "gap_3", "gap_4"}
