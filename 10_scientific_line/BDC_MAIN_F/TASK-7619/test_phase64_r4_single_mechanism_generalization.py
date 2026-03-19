from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory_generalization import (
    build_dataset_for_generalization_slice,
    load_generalization_slice_specs,
    write_generalization_measurements,
)
from evolution.micro_tasks.sequence_memory import majority_symbol_for_sequence


MATRIX_PATH = (
    REPO_ROOT / "docs" / "experiments" / "R4_SINGLE_MECHANISM_GENERALIZATION_PRESSURE_MATRIX.json"
)


def test_generalization_matrix_loads_four_required_slices() -> None:
    specs = load_generalization_slice_specs(MATRIX_PATH)
    assert [spec.slice_id for spec in specs] == [
        "r4_length_extension",
        "r4_gap_extension",
        "r4_alphabet_extension",
        "r4_combined_bounded",
    ]
    for spec in specs:
        assert spec.trace_width == spec.max_gap + 1


def test_generalization_slice_generation_is_deterministic() -> None:
    spec = load_generalization_slice_specs(MATRIX_PATH)[0]
    first = build_dataset_for_generalization_slice(spec)
    second = build_dataset_for_generalization_slice(spec)
    assert first == second


def test_control_resistant_r4_slices_preserve_required_constraints() -> None:
    for spec in load_generalization_slice_specs(MATRIX_PATH):
        dataset = build_dataset_for_generalization_slice(spec)
        if not spec.control_resistant:
            continue
        for sample in dataset:
            assert int(sample.target_symbol) != int(sample.sequence[-1])
            assert int(sample.target_symbol) != majority_symbol_for_sequence(sample.sequence)


def test_generalization_runner_writes_all_slice_outputs(tmp_path: Path) -> None:
    summary = write_generalization_measurements(
        matrix_path=MATRIX_PATH,
        out_root=tmp_path,
    )
    assert summary["slice_count"] == 4
    for slice_summary in summary["slice_summaries"]:
        assert slice_summary["candidate_gt_no_memory"] is True
        assert slice_summary["candidate_gt_trivial"] is True
        assert slice_summary["hardest_gap_gt_no_memory"] is True
        assert slice_summary["hardest_gap_gt_trivial"] is True
        assert slice_summary["deterministic_replay_status"] is True
        slice_dir = tmp_path / slice_summary["slice_id"]
        assert (slice_dir / "manifest.json").exists()
        assert (slice_dir / "dataset.json").exists()
        assert (slice_dir / "mechanism_scorecard.json").exists()
    parsed = json.loads((tmp_path / "generalization_summary.json").read_text(encoding="utf-8"))
    assert parsed["slice_count"] == 4
