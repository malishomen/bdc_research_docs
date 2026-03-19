from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.r5_cloze_transfer_launch_prep import (
    TransferLaunchConfig,
    build_launch_prep_packet,
    build_longrun_manifest,
    build_symbolic_micro_corpus_cloze_transfer_dataset,
    finalize_launch_prep_decision,
    write_smoke_artifact,
)


def test_transfer_dataset_is_deterministic() -> None:
    first, first_map = build_symbolic_micro_corpus_cloze_transfer_dataset(seed=20260319)
    second, second_map = build_symbolic_micro_corpus_cloze_transfer_dataset(seed=20260319)
    assert first == second
    assert first_map == second_map


def test_smoke_artifact_candidate_beats_controls(tmp_path: Path) -> None:
    payload = write_smoke_artifact(
        out_root=tmp_path,
        config=TransferLaunchConfig(
            slice_id="smoke",
            seed=20260319,
            size=64,
            seq_len=10,
            lexicon_size=8,
            min_gap=3,
            max_gap=5,
        ),
    )
    scorecard = payload["scorecard"]
    assert scorecard["candidate_accuracy"] > scorecard["no_memory_control_accuracy"]
    assert scorecard["candidate_accuracy"] > scorecard["trivial_last_symbol_memory_accuracy"]
    assert scorecard["candidate_accuracy"] > scorecard["random_symbol_accuracy"]


def test_manifest_builder_writes_bounded_longrun_surface(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    manifest = build_longrun_manifest(manifest_path=manifest_path)
    assert manifest_path.exists()
    assert len(manifest["seeds"]) == 30
    assert len(manifest["slices"]) == 4


def test_finalize_marks_ready_for_launch_when_bdc_accepts(tmp_path: Path) -> None:
    bundle_path = tmp_path / "bundle_result.json"
    bundle_path.write_text(
        json.dumps(
            {
                "bundle": {
                    "supported": True,
                    "recommended_variant_id": "symbolic_micro_corpus_cloze_transfer_launch_ready",
                    "strategy_mode": "direct_architecture_selection",
                    "confidence_band": "high",
                    "selective_outcome_class": "recommend_ready",
                }
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    decision = finalize_launch_prep_decision(bundle_result_path=bundle_path)
    assert decision["verdict"] == "READY_FOR_R5_TRANSFER_LONGRUN"


def test_launch_packet_builder_writes_required_files(tmp_path: Path) -> None:
    smoke_root = tmp_path / "smoke"
    write_smoke_artifact(
        out_root=smoke_root,
        config=TransferLaunchConfig(
            slice_id="smoke",
            seed=20260319,
            size=32,
            seq_len=10,
            lexicon_size=8,
            min_gap=3,
            max_gap=5,
        ),
    )
    manifest_path = tmp_path / "manifest.json"
    build_longrun_manifest(manifest_path=manifest_path)
    build_launch_prep_packet(
        smoke_scorecard_path=smoke_root / "scorecard.json",
        manifest_path=manifest_path,
        packet_dir=tmp_path / "packet",
    )
    assert (tmp_path / "packet" / "BDC_INPUT_PACKET_R5_TRANSFER_LAUNCH_PREP.json").exists()
    assert (tmp_path / "packet" / "unified_variant_comparison.csv").exists()
    assert (tmp_path / "packet" / "current_slice_metrics.csv").exists()
