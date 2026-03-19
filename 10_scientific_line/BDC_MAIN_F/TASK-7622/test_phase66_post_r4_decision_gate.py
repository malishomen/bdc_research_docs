from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.post_r4_decision_gate import (
    build_post_r4_decision_packet,
    finalize_post_r4_decision,
)


R4_GATE_PATH = (
    REPO_ROOT / "results" / "r4_single_mechanism_generalization" / "generalization_gate_decision.json"
)


def test_packet_builder_writes_required_files(tmp_path: Path) -> None:
    build_post_r4_decision_packet(
        r4_gate_decision_path=R4_GATE_PATH,
        packet_dir=tmp_path,
    )
    assert (tmp_path / "BDC_INPUT_PACKET_POST_R4_DECISION.json").exists()
    assert (tmp_path / "unified_variant_comparison.csv").exists()
    assert (tmp_path / "current_slice_metrics.csv").exists()
    assert (tmp_path / "failure_case_registry.csv").exists()


def test_finalize_chooses_transfer_gate_for_supported_transfer_bundle(tmp_path: Path) -> None:
    bundle_result = {
        "bundle": {
            "supported": True,
            "recommended_variant_id": "single_mechanism_transfer_gate",
            "strategy_mode": "direct_architecture_selection",
            "confidence_band": "high",
            "selective_outcome_class": "recommend_ready",
        }
    }
    bundle_path = tmp_path / "bundle_result.json"
    bundle_path.write_text(json.dumps(bundle_result, indent=2) + "\n", encoding="utf-8")
    decision = finalize_post_r4_decision(
        r4_gate_decision_path=R4_GATE_PATH,
        bundle_result_path=bundle_path,
    )
    assert decision["verdict"] == "OPEN_SINGLE_MECHANISM_TRANSFER_GATE"
