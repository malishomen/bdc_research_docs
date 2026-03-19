from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory import (
    build_control_resistant_sequence_memory_dataset,
    majority_symbol_for_sequence,
)
from evolution.micro_tasks.sequence_memory_mechanism import mechanism_scorecard


def test_control_resistant_dataset_is_deterministic() -> None:
    first = build_control_resistant_sequence_memory_dataset(seed=20260319, size=16)
    second = build_control_resistant_sequence_memory_dataset(seed=20260319, size=16)
    assert first == second


def test_control_resistant_dataset_excludes_last_and_majority_shortcuts() -> None:
    dataset = build_control_resistant_sequence_memory_dataset(seed=20260319, size=32)
    for sample in dataset:
        assert int(sample.target_symbol) != int(sample.sequence[-1])
        assert int(sample.target_symbol) != majority_symbol_for_sequence(sample.sequence)


def test_bounded_memory_candidate_still_beats_controls() -> None:
    dataset = build_control_resistant_sequence_memory_dataset(seed=20260319, size=64)
    scorecard = mechanism_scorecard(dataset, trace_width=7)
    assert scorecard["candidate_accuracy"] > scorecard["no_memory_control_accuracy"]
    assert scorecard["candidate_accuracy"] > scorecard["trivial_last_symbol_memory_accuracy"]


def test_hardest_gap_is_present_and_supported() -> None:
    dataset = build_control_resistant_sequence_memory_dataset(seed=20260319, size=128)
    scorecard = mechanism_scorecard(dataset, trace_width=7)
    assert scorecard["hardest_recall_gap"] == 6
    hardest = scorecard["hardest_gap_accuracy"]
    assert hardest["candidate_accuracy"] > hardest["no_memory_control_accuracy"]
    assert hardest["candidate_accuracy"] > hardest["trivial_last_symbol_memory_accuracy"]
