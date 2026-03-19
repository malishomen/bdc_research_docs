from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

from evolution.micro_tasks.sequence_memory import (
    SequenceMemorySample,
    build_control_resistant_sequence_memory_dataset,
    build_controlled_sequence_memory_dataset,
    sample_to_dict,
)
from evolution.micro_tasks.sequence_memory_mechanism import mechanism_scorecard


@dataclass(frozen=True)
class GeneralizationSliceSpec:
    slice_id: str
    pressure_axes: tuple[str, ...]
    purpose: str
    seed: int
    dataset_size: int
    seq_len: int
    alphabet_size: int
    min_gap: int
    max_gap: int
    trace_width: int
    control_resistant: bool


def _validate_generalization_spec(spec: GeneralizationSliceSpec) -> None:
    if spec.dataset_size <= 0:
        raise ValueError("dataset_size must be > 0")
    if spec.trace_width != spec.max_gap + 1:
        raise ValueError(
            f"{spec.slice_id} violates trace width rule: "
            f"trace_width={spec.trace_width} must equal max_gap + 1={spec.max_gap + 1}"
        )


def load_generalization_slice_specs(matrix_path: Path) -> list[GeneralizationSliceSpec]:
    payload = json.loads(matrix_path.read_text(encoding="utf-8"))
    specs: list[GeneralizationSliceSpec] = []
    for raw_spec in payload["required_r4_slices"]:
        spec = GeneralizationSliceSpec(
            slice_id=str(raw_spec["slice_id"]),
            pressure_axes=tuple(str(axis) for axis in raw_spec["pressure_axes"]),
            purpose=str(raw_spec["purpose"]),
            seed=int(raw_spec["seed"]),
            dataset_size=int(raw_spec["dataset_size"]),
            seq_len=int(raw_spec["seq_len"]),
            alphabet_size=int(raw_spec["alphabet_size"]),
            min_gap=int(raw_spec["min_gap"]),
            max_gap=int(raw_spec["max_gap"]),
            trace_width=int(raw_spec["trace_width"]),
            control_resistant=bool(raw_spec["control_resistant"]),
        )
        _validate_generalization_spec(spec)
        specs.append(spec)
    return specs


def build_dataset_for_generalization_slice(
    spec: GeneralizationSliceSpec,
) -> list[SequenceMemorySample]:
    if spec.control_resistant:
        return build_control_resistant_sequence_memory_dataset(
            seed=spec.seed,
            size=spec.dataset_size,
            seq_len=spec.seq_len,
            alphabet_size=spec.alphabet_size,
            min_gap=spec.min_gap,
            max_gap=spec.max_gap,
            max_attempts=max(20000, spec.dataset_size * 500),
        )
    return build_controlled_sequence_memory_dataset(
        seed=spec.seed,
        size=spec.dataset_size,
        seq_len=spec.seq_len,
        alphabet_size=spec.alphabet_size,
        min_gap=spec.min_gap,
        max_gap=spec.max_gap,
    )


def slice_manifest(spec: GeneralizationSliceSpec) -> dict[str, Any]:
    manifest = {
        "phase": "R4",
        "task_id": "TASK-7619",
        "environment_family": "controlled_sequence_memory",
        "mechanism_candidate_id": "bounded_working_memory_candidate",
        "slice_id": spec.slice_id,
        "pressure_axes": list(spec.pressure_axes),
        "purpose": spec.purpose,
        "seed": spec.seed,
        "dataset_size": spec.dataset_size,
        "seq_len": spec.seq_len,
        "alphabet_size": spec.alphabet_size,
        "min_gap": spec.min_gap,
        "max_gap": spec.max_gap,
        "trace_width": spec.trace_width,
        "control_resistant": spec.control_resistant,
        "trace_width_rule": "trace_width = max_gap + 1",
        "required_controls": [
            "majority_symbol_predictor",
            "always_repeat_last_symbol",
        ],
    }
    if spec.control_resistant:
        manifest["required_conditions"] = [
            "target_symbol != last_symbol",
            "target_symbol != majority_symbol",
        ]
    return manifest


def _slice_summary_entry(
    spec: GeneralizationSliceSpec,
    *,
    scorecard: dict[str, Any],
) -> dict[str, Any]:
    hardest_gap = scorecard["hardest_gap_accuracy"]
    return {
        "slice_id": spec.slice_id,
        "pressure_axes": list(spec.pressure_axes),
        "trace_width": spec.trace_width,
        "dataset_size": spec.dataset_size,
        "control_resistant": spec.control_resistant,
        "candidate_accuracy": float(scorecard["candidate_accuracy"]),
        "no_memory_control_accuracy": float(scorecard["no_memory_control_accuracy"]),
        "trivial_last_symbol_memory_accuracy": float(
            scorecard["trivial_last_symbol_memory_accuracy"]
        ),
        "delta_vs_no_memory": float(scorecard["delta_vs_no_memory"]),
        "delta_vs_trivial_memory": float(scorecard["delta_vs_trivial_memory"]),
        "hardest_recall_gap": int(scorecard["hardest_recall_gap"]),
        "hardest_gap_candidate_accuracy": float(hardest_gap["candidate_accuracy"]),
        "hardest_gap_no_memory_control_accuracy": float(
            hardest_gap["no_memory_control_accuracy"]
        ),
        "hardest_gap_trivial_last_symbol_memory_accuracy": float(
            hardest_gap["trivial_last_symbol_memory_accuracy"]
        ),
        "deterministic_replay_status": bool(scorecard["deterministic_replay_status"]),
        "candidate_gt_no_memory": float(scorecard["candidate_accuracy"])
        > float(scorecard["no_memory_control_accuracy"]),
        "candidate_gt_trivial": float(scorecard["candidate_accuracy"])
        > float(scorecard["trivial_last_symbol_memory_accuracy"]),
        "hardest_gap_gt_no_memory": float(hardest_gap["candidate_accuracy"])
        > float(hardest_gap["no_memory_control_accuracy"]),
        "hardest_gap_gt_trivial": float(hardest_gap["candidate_accuracy"])
        > float(hardest_gap["trivial_last_symbol_memory_accuracy"]),
    }


def write_generalization_measurements(
    *,
    matrix_path: Path,
    out_root: Path,
) -> dict[str, Any]:
    specs = load_generalization_slice_specs(matrix_path)
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "pressure_matrix_snapshot.json").write_text(
        matrix_path.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    slice_summaries: list[dict[str, Any]] = []
    for spec in specs:
        dataset = build_dataset_for_generalization_slice(spec)
        scorecard = mechanism_scorecard(dataset, trace_width=spec.trace_width)
        manifest = slice_manifest(spec)

        slice_dir = out_root / spec.slice_id
        slice_dir.mkdir(parents=True, exist_ok=True)
        (slice_dir / "manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n",
            encoding="utf-8",
        )
        (slice_dir / "dataset.json").write_text(
            json.dumps([sample_to_dict(sample) for sample in dataset], indent=2) + "\n",
            encoding="utf-8",
        )
        (slice_dir / "mechanism_scorecard.json").write_text(
            json.dumps(scorecard, indent=2) + "\n",
            encoding="utf-8",
        )
        slice_summaries.append(_slice_summary_entry(spec, scorecard=scorecard))

    summary = {
        "phase": "R4",
        "task_id": "TASK-7619",
        "environment_family": "controlled_sequence_memory",
        "mechanism_candidate_id": "bounded_working_memory_candidate",
        "matrix_path": str(matrix_path).replace("\\", "/"),
        "slice_count": len(specs),
        "slice_summaries": slice_summaries,
    }
    (out_root / "generalization_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    return summary
