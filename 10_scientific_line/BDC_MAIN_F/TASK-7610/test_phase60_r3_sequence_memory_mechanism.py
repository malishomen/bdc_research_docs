from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory import build_controlled_sequence_memory_dataset
from evolution.micro_tasks.sequence_memory_mechanism import (
    deterministic_replay_status,
    initial_working_memory_state,
    mechanism_scorecard,
    replay_sequence_with_working_memory,
    update_working_memory_state,
)


def test_working_memory_fifo_update_rule() -> None:
    state = initial_working_memory_state(trace_width=3)
    state = update_working_memory_state(state, observed_symbol=1)
    state = update_working_memory_state(state, observed_symbol=2)
    state = update_working_memory_state(state, observed_symbol=3)
    state = update_working_memory_state(state, observed_symbol=4)
    assert state.trace == (2, 3, 4)
    assert state.steps_seen == 4


def test_replay_sequence_is_deterministic() -> None:
    sequence = (0, 1, 2, 3, 0, 1, 2, 3)
    first_state, first_replay = replay_sequence_with_working_memory(sequence, trace_width=5)
    second_state, second_replay = replay_sequence_with_working_memory(sequence, trace_width=5)
    assert first_state == second_state
    assert first_replay == second_replay


def test_candidate_beats_controls_on_sequence_memory_dataset() -> None:
    dataset = build_controlled_sequence_memory_dataset(seed=20260319, size=64)
    scorecard = mechanism_scorecard(dataset, trace_width=5)
    assert scorecard["candidate_accuracy"] > scorecard["no_memory_control_accuracy"]
    assert scorecard["candidate_accuracy"] > scorecard["trivial_last_symbol_memory_accuracy"]


def test_candidate_beats_controls_on_hardest_gap() -> None:
    dataset = build_controlled_sequence_memory_dataset(seed=20260319, size=128)
    scorecard = mechanism_scorecard(dataset, trace_width=5)
    hardest = scorecard["hardest_gap_accuracy"]
    assert hardest["candidate_accuracy"] > hardest["no_memory_control_accuracy"]
    assert hardest["candidate_accuracy"] > hardest["trivial_last_symbol_memory_accuracy"]


def test_deterministic_replay_status_is_true() -> None:
    dataset = build_controlled_sequence_memory_dataset(seed=20260319, size=32)
    assert deterministic_replay_status(dataset, trace_width=5) is True
