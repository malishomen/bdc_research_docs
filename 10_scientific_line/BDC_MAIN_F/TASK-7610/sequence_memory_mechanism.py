from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Sequence

from evolution.micro_tasks.sequence_memory import (
    SequenceMemorySample,
    accuracy_from_predictions,
    predict_last_symbol,
    predict_majority_symbol,
)


@dataclass(frozen=True)
class WorkingMemoryState:
    trace_width: int
    trace: tuple[int, ...]
    steps_seen: int


@dataclass(frozen=True)
class ReplayStep:
    step_index: int
    observed_symbol: int
    trace_before: tuple[int, ...]
    trace_after: tuple[int, ...]


def initial_working_memory_state(*, trace_width: int = 5) -> WorkingMemoryState:
    if trace_width <= 0:
        raise ValueError("trace_width must be > 0")
    return WorkingMemoryState(trace_width=trace_width, trace=(), steps_seen=0)


def update_working_memory_state(
    state: WorkingMemoryState,
    *,
    observed_symbol: int,
) -> WorkingMemoryState:
    next_trace = state.trace + (int(observed_symbol),)
    if len(next_trace) > state.trace_width:
        next_trace = next_trace[-state.trace_width :]
    return WorkingMemoryState(
        trace_width=state.trace_width,
        trace=next_trace,
        steps_seen=state.steps_seen + 1,
    )


def replay_sequence_with_working_memory(
    sequence: Sequence[int],
    *,
    trace_width: int = 5,
) -> tuple[WorkingMemoryState, list[ReplayStep]]:
    state = initial_working_memory_state(trace_width=trace_width)
    replay: list[ReplayStep] = []
    for idx, symbol in enumerate(sequence):
        next_state = update_working_memory_state(state, observed_symbol=int(symbol))
        replay.append(
            ReplayStep(
                step_index=idx,
                observed_symbol=int(symbol),
                trace_before=state.trace,
                trace_after=next_state.trace,
            )
        )
        state = next_state
    return state, replay


def predict_from_working_memory_state(
    state: WorkingMemoryState,
    *,
    recall_gap: int,
) -> int:
    required_depth = int(recall_gap) + 1
    if required_depth <= 0:
        raise ValueError("recall_gap must be >= 0")
    if required_depth > len(state.trace):
        raise ValueError("working-memory trace does not cover required recall depth")
    return int(state.trace[-required_depth])


def predict_with_bounded_working_memory(
    dataset: Sequence[SequenceMemorySample],
    *,
    trace_width: int = 5,
) -> list[int]:
    predictions: list[int] = []
    for sample in dataset:
        final_state, _ = replay_sequence_with_working_memory(
            sample.sequence,
            trace_width=trace_width,
        )
        predictions.append(
            predict_from_working_memory_state(
                final_state,
                recall_gap=sample.recall_gap,
            )
        )
    return predictions


def gap_accuracy_summary(
    dataset: Sequence[SequenceMemorySample],
    *,
    trace_width: int = 5,
) -> dict[str, dict[str, float]]:
    candidate_preds = predict_with_bounded_working_memory(dataset, trace_width=trace_width)
    no_memory_preds = predict_majority_symbol(dataset)
    trivial_preds = predict_last_symbol(dataset)

    by_gap: dict[int, list[int]] = {}
    for idx, sample in enumerate(dataset):
        by_gap.setdefault(int(sample.recall_gap), []).append(idx)

    summary: dict[str, dict[str, float]] = {}
    for gap, indices in sorted(by_gap.items()):
        gap_dataset = [dataset[idx] for idx in indices]
        summary[str(gap)] = {
            "candidate_accuracy": accuracy_from_predictions(
                gap_dataset, [candidate_preds[idx] for idx in indices]
            ),
            "no_memory_control_accuracy": accuracy_from_predictions(
                gap_dataset, [no_memory_preds[idx] for idx in indices]
            ),
            "trivial_last_symbol_memory_accuracy": accuracy_from_predictions(
                gap_dataset, [trivial_preds[idx] for idx in indices]
            ),
        }
    return summary


def deterministic_replay_status(
    dataset: Sequence[SequenceMemorySample],
    *,
    trace_width: int = 5,
) -> bool:
    for sample in dataset[: min(8, len(dataset))]:
        first_state, first_replay = replay_sequence_with_working_memory(
            sample.sequence,
            trace_width=trace_width,
        )
        second_state, second_replay = replay_sequence_with_working_memory(
            sample.sequence,
            trace_width=trace_width,
        )
        if first_state != second_state or first_replay != second_replay:
            return False
    return True


def replay_examples(
    dataset: Sequence[SequenceMemorySample],
    *,
    trace_width: int = 5,
    limit: int = 3,
) -> list[dict[str, object]]:
    examples: list[dict[str, object]] = []
    for sample in dataset[:limit]:
        final_state, replay = replay_sequence_with_working_memory(
            sample.sequence,
            trace_width=trace_width,
        )
        predicted_symbol = predict_from_working_memory_state(
            final_state,
            recall_gap=sample.recall_gap,
        )
        examples.append(
            {
                "sequence": list(sample.sequence),
                "recall_gap": int(sample.recall_gap),
                "target_index": int(sample.target_index),
                "target_symbol": int(sample.target_symbol),
                "predicted_symbol": int(predicted_symbol),
                "final_state": {
                    "trace_width": final_state.trace_width,
                    "trace": list(final_state.trace),
                    "steps_seen": final_state.steps_seen,
                },
                "replay": [
                    {
                        "step_index": step.step_index,
                        "observed_symbol": step.observed_symbol,
                        "trace_before": list(step.trace_before),
                        "trace_after": list(step.trace_after),
                    }
                    for step in replay
                ],
            }
        )
    return examples


def mechanism_scorecard(
    dataset: Sequence[SequenceMemorySample],
    *,
    trace_width: int = 5,
) -> dict[str, object]:
    candidate_preds = predict_with_bounded_working_memory(dataset, trace_width=trace_width)
    no_memory_preds = predict_majority_symbol(dataset)
    trivial_preds = predict_last_symbol(dataset)

    candidate_accuracy = accuracy_from_predictions(dataset, candidate_preds)
    no_memory_accuracy = accuracy_from_predictions(dataset, no_memory_preds)
    trivial_accuracy = accuracy_from_predictions(dataset, trivial_preds)
    gap_summary = gap_accuracy_summary(dataset, trace_width=trace_width)

    hardest_gap = max((int(key) for key in gap_summary), default=0)
    hardest_gap_summary = gap_summary[str(hardest_gap)] if hardest_gap else {
        "candidate_accuracy": 0.0,
        "no_memory_control_accuracy": 0.0,
        "trivial_last_symbol_memory_accuracy": 0.0,
    }

    return {
        "mechanism_candidate_id": "bounded_working_memory_candidate",
        "trace_width": trace_width,
        "candidate_accuracy": candidate_accuracy,
        "no_memory_control_accuracy": no_memory_accuracy,
        "trivial_last_symbol_memory_accuracy": trivial_accuracy,
        "delta_vs_no_memory": candidate_accuracy - no_memory_accuracy,
        "delta_vs_trivial_memory": candidate_accuracy - trivial_accuracy,
        "gap_accuracy_by_recall_gap": gap_summary,
        "hardest_recall_gap": hardest_gap,
        "hardest_gap_accuracy": hardest_gap_summary,
        "deterministic_replay_status": deterministic_replay_status(
            dataset,
            trace_width=trace_width,
        ),
        "replay_examples": replay_examples(dataset, trace_width=trace_width),
    }
