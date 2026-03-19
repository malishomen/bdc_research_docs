from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.control_resistant_sequence_memory_gate import (
    control_resistant_conditions_pass,
    second_bounded_signal_decision,
)
from evolution.micro_tasks.sequence_memory import (
    build_control_resistant_sequence_memory_dataset,
    sample_to_dict,
)
from evolution.micro_tasks.sequence_memory_mechanism import mechanism_scorecard


def test_control_resistant_conditions_are_verified() -> None:
    dataset = build_control_resistant_sequence_memory_dataset(seed=20260319, size=32)
    assert control_resistant_conditions_pass([sample_to_dict(sample) for sample in dataset]) is True


def test_second_signal_gate_confirms_measured_signal() -> None:
    dataset = build_control_resistant_sequence_memory_dataset(seed=20260319, size=64)
    scorecard = mechanism_scorecard(dataset, trace_width=7)
    decision = second_bounded_signal_decision(scorecard, control_conditions_pass=True)
    assert decision["verdict"] == "CONFIRM_SECOND_BOUNDED_SIGNAL"
