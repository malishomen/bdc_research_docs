from __future__ import annotations

import random
from dataclasses import asdict, dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class SequenceMemorySample:
    sequence: tuple[int, ...]
    recall_gap: int
    target_index: int
    target_symbol: int


def build_controlled_sequence_memory_dataset(
    *,
    seed: int,
    size: int = 128,
    seq_len: int = 8,
    alphabet_size: int = 4,
    min_gap: int = 2,
    max_gap: int = 4,
) -> list[SequenceMemorySample]:
    if size <= 0:
        raise ValueError("size must be > 0")
    if seq_len < 4:
        raise ValueError("seq_len must be >= 4")
    if alphabet_size < 2:
        raise ValueError("alphabet_size must be >= 2")
    if min_gap < 1 or max_gap < min_gap:
        raise ValueError("invalid recall gap bounds")
    if max_gap >= seq_len:
        raise ValueError("max_gap must be < seq_len")

    rng = random.Random(seed)
    dataset: list[SequenceMemorySample] = []
    for _ in range(size):
        sequence = tuple(rng.randrange(alphabet_size) for _ in range(seq_len))
        recall_gap = rng.randint(min_gap, max_gap)
        target_index = seq_len - 1 - recall_gap
        target_symbol = int(sequence[target_index])
        dataset.append(
            SequenceMemorySample(
                sequence=sequence,
                recall_gap=recall_gap,
                target_index=target_index,
                target_symbol=target_symbol,
            )
        )
    return dataset


def sample_to_dict(sample: SequenceMemorySample) -> dict[str, object]:
    payload = asdict(sample)
    payload["sequence"] = list(sample.sequence)
    return payload


def predict_random_symbol(
    dataset: Sequence[SequenceMemorySample],
    *,
    seed: int,
    alphabet_size: int,
) -> list[int]:
    if alphabet_size < 2:
        raise ValueError("alphabet_size must be >= 2")
    rng = random.Random(seed)
    return [rng.randrange(alphabet_size) for _ in dataset]


def predict_last_symbol(dataset: Sequence[SequenceMemorySample]) -> list[int]:
    return [int(sample.sequence[-1]) for sample in dataset]


def majority_symbol_for_sequence(sequence: Sequence[int]) -> int:
    counts: dict[int, int] = {}
    for symbol in sequence:
        counts[int(symbol)] = counts.get(int(symbol), 0) + 1
    return int(min((-count, symbol) for symbol, count in counts.items())[1])


def predict_majority_symbol(dataset: Sequence[SequenceMemorySample]) -> list[int]:
    return [majority_symbol_for_sequence(sample.sequence) for sample in dataset]


def build_control_resistant_sequence_memory_dataset(
    *,
    seed: int,
    size: int = 128,
    seq_len: int = 10,
    alphabet_size: int = 5,
    min_gap: int = 3,
    max_gap: int = 6,
    max_attempts: int = 20000,
) -> list[SequenceMemorySample]:
    if max_attempts <= 0:
        raise ValueError("max_attempts must be > 0")
    rng = random.Random(seed)
    dataset: list[SequenceMemorySample] = []
    attempts = 0
    while len(dataset) < size:
        attempts += 1
        if attempts > max_attempts:
            raise RuntimeError("unable to build control-resistant dataset within max_attempts")
        candidate = build_controlled_sequence_memory_dataset(
            seed=rng.randrange(10**9),
            size=1,
            seq_len=seq_len,
            alphabet_size=alphabet_size,
            min_gap=min_gap,
            max_gap=max_gap,
        )[0]
        last_symbol = int(candidate.sequence[-1])
        majority_symbol = majority_symbol_for_sequence(candidate.sequence)
        if int(candidate.target_symbol) == last_symbol:
            continue
        if int(candidate.target_symbol) == majority_symbol:
            continue
        dataset.append(candidate)
    return dataset


def accuracy_from_predictions(
    dataset: Sequence[SequenceMemorySample],
    predictions: Iterable[int],
) -> float:
    preds = list(predictions)
    if len(preds) != len(dataset):
        raise ValueError("predictions length must equal dataset length")
    if not dataset:
        return 0.0
    correct = 0
    for sample, pred in zip(dataset, preds):
        if int(pred) == int(sample.target_symbol):
            correct += 1
    return correct / len(dataset)


def baseline_scorecard(
    dataset: Sequence[SequenceMemorySample],
    *,
    seed: int,
    alphabet_size: int,
) -> dict[str, float]:
    return {
        "random_symbol_predictor": accuracy_from_predictions(
            dataset,
            predict_random_symbol(dataset, seed=seed, alphabet_size=alphabet_size),
        ),
        "always_repeat_last_symbol": accuracy_from_predictions(
            dataset,
            predict_last_symbol(dataset),
        ),
        "majority_symbol_predictor": accuracy_from_predictions(
            dataset,
            predict_majority_symbol(dataset),
        ),
    }
