from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory_generalization_gate import (
    generalization_gate_decision,
    write_generalization_packet,
)


SUMMARY_PATH = (
    REPO_ROOT / "results" / "r4_single_mechanism_generalization" / "generalization_summary.json"
)
MATRIX_PATH = (
    REPO_ROOT / "docs" / "experiments" / "R4_SINGLE_MECHANISM_GENERALIZATION_PRESSURE_MATRIX.json"
)


def test_generalization_gate_confirms_measured_surface() -> None:
    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    decision = generalization_gate_decision(summary)
    assert decision["verdict"] == "CONFIRM_SINGLE_MECHANISM_GENERALIZATION"
    assert decision["approval_conditions"]["required_slices_present"] is True
    assert decision["approval_conditions"]["all_deterministic_replay"] is True


def test_packet_writer_emits_required_r4_gate_files(tmp_path: Path) -> None:
    decision = write_generalization_packet(
        summary_path=SUMMARY_PATH,
        matrix_path=MATRIX_PATH,
        packet_dir=tmp_path,
    )
    assert decision["verdict"] == "CONFIRM_SINGLE_MECHANISM_GENERALIZATION"
    assert (tmp_path / "BDC_INPUT_PACKET_R4_SINGLE_MECHANISM_GENERALIZATION.json").exists()
    assert (tmp_path / "generalization_summary.json").exists()
    assert (tmp_path / "generalization_matrix_snapshot.json").exists()
    assert (tmp_path / "r4_generalization_gate_decision.json").exists()
    assert (tmp_path / "unified_variant_comparison.csv").exists()
    assert (tmp_path / "current_slice_metrics.csv").exists()
