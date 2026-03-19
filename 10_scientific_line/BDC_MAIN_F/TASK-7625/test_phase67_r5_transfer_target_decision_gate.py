from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.r5_transfer_target_gate import (
    build_r5_transfer_target_packet,
    finalize_r5_transfer_target_decision,
)


MATRIX_PATH = REPO_ROOT / "docs" / "experiments" / "R5_TRANSFER_TARGET_MATRIX.json"


def test_packet_builder_writes_required_files(tmp_path: Path) -> None:
    build_r5_transfer_target_packet(
        matrix_path=MATRIX_PATH,
        packet_dir=tmp_path,
    )
    assert (tmp_path / "BDC_INPUT_PACKET_R5_TRANSFER_TARGET.json").exists()
    assert (tmp_path / "unified_variant_comparison.csv").exists()
    assert (tmp_path / "current_slice_metrics.csv").exists()
    assert (tmp_path / "failure_case_registry.csv").exists()


def test_finalize_approves_cloze_when_bdc_recommends_it(tmp_path: Path) -> None:
    bundle_result = {
        "bundle": {
            "supported": True,
            "recommended_variant_id": "symbolic_micro_corpus_cloze_transfer",
            "strategy_mode": "direct_architecture_selection",
            "confidence_band": "high",
            "selective_outcome_class": "recommend_ready",
        }
    }
    bundle_path = tmp_path / "bundle_result.json"
    bundle_path.write_text(json.dumps(bundle_result, indent=2) + "\n", encoding="utf-8")
    decision = finalize_r5_transfer_target_decision(
        matrix_path=MATRIX_PATH,
        bundle_result_path=bundle_path,
    )
    assert decision["verdict"] == "APPROVE_R5_TRANSFER_TARGET"
    assert decision["approved_target_id"] == "symbolic_micro_corpus_cloze_transfer"


def test_finalize_remains_when_bdc_recommends_docs_only_target(tmp_path: Path) -> None:
    bundle_result = {
        "bundle": {
            "supported": True,
            "recommended_variant_id": "controlled_uncertainty_abstention_transfer",
            "strategy_mode": "full_hybrid_search",
            "confidence_band": "medium",
            "selective_outcome_class": "recommend_with_guardrails",
        }
    }
    bundle_path = tmp_path / "bundle_result.json"
    bundle_path.write_text(json.dumps(bundle_result, indent=2) + "\n", encoding="utf-8")
    decision = finalize_r5_transfer_target_decision(
        matrix_path=MATRIX_PATH,
        bundle_result_path=bundle_path,
    )
    assert decision["verdict"] == "REMAIN_IN_R5_TRANSFER"
    assert decision["approved_target_id"] is None
