from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory import (
    accuracy_from_predictions,
    baseline_scorecard,
    build_controlled_sequence_memory_dataset,
    predict_last_symbol,
)


def test_sequence_memory_dataset_is_deterministic() -> None:
    first = build_controlled_sequence_memory_dataset(seed=20260319, size=16)
    second = build_controlled_sequence_memory_dataset(seed=20260319, size=16)
    assert first == second


def test_sequence_memory_requires_nontrivial_recall_gap() -> None:
    dataset = build_controlled_sequence_memory_dataset(
        seed=20260319,
        size=32,
        seq_len=8,
        min_gap=2,
        max_gap=4,
    )
    assert all(sample.recall_gap >= 2 for sample in dataset)
    assert all(sample.target_index < len(sample.sequence) - 1 for sample in dataset)


def test_last_symbol_baseline_is_not_perfect() -> None:
    dataset = build_controlled_sequence_memory_dataset(seed=20260319, size=64)
    score = accuracy_from_predictions(dataset, predict_last_symbol(dataset))
    assert score < 1.0


def test_baseline_scorecard_is_deterministic() -> None:
    dataset = build_controlled_sequence_memory_dataset(seed=20260319, size=64)
    first = baseline_scorecard(dataset, seed=17, alphabet_size=4)
    second = baseline_scorecard(dataset, seed=17, alphabet_size=4)
    assert first == second
    assert set(first) == {
        "random_symbol_predictor",
        "always_repeat_last_symbol",
        "majority_symbol_predictor",
    }
