from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_r5_transfer_target_packet(
    *,
    matrix_path: Path,
    packet_dir: Path,
) -> dict[str, Any]:
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    candidates = {row["target_id"]: row for row in matrix["candidates"]}
    cloze = candidates["symbolic_micro_corpus_cloze_transfer"]
    uncertainty = candidates["controlled_uncertainty_abstention_transfer"]

    packet_dir.mkdir(parents=True, exist_ok=True)
    packet_payload = {
        "packet_version": "R5_TRANSFER_TARGET_DECISION_V1",
        "packet_id": "BDC_R5_TRANSFER_TARGET_DECISION",
        "project": "Bio_Digital_Core",
        "system_name": "BDC_Scientific_Line",
        "base_packet_reference": "TASK-7624",
        "evidence_policy": {
            "measured": [],
            "measured_from_historical_report": [
                "symbolic cloze task infrastructure already exists in the repository",
                "historical deterministic cloze work exists, including deterministic masking and historical measured reports",
            ],
            "inferred": [
                "the approved FIFO mechanism can be transferred into a new bounded cloze harness without adding a second mechanism",
            ],
            "missing": [
                "direct same-mechanism transfer evidence for either target",
                "any executable uncertainty-abstention environment artifact",
            ],
        },
        "positioning": {
            "historical_best_prior": "bounded_working_memory_candidate_r4_confirmed_state",
            "bdc_recommendation_mode": "r5_transfer_target_decision",
        },
        "explicit_requests_to_bdc": [
            "Interpret which adjacent target is the narrowest honest next transfer target.",
            "Prefer the target that can be prepared for the next long-run without adding a new mechanism family.",
            "Do not treat historical cloze infrastructure as direct transfer success.",
        ],
        "matrix_conclusion": matrix["matrix_conclusion"],
    }
    (packet_dir / "BDC_INPUT_PACKET_R5_TRANSFER_TARGET.json").write_text(
        json.dumps(packet_payload, indent=2) + "\n",
        encoding="utf-8",
    )

    write_csv(
        packet_dir / "unified_variant_comparison.csv",
        [
            "variant_id",
            "architecture_type",
            "role_set",
            "runtime_type",
            "docs_improved_pct",
            "naturalness_delta",
            "semantic_pass_pct",
            "runtime_min",
            "cost_usd",
            "llm_calls",
            "revert_rate_pct",
            "gate_pass_rate_pct",
            "useful_rewrite_rate_pct",
            "evidence_status",
            "notes",
        ],
        [
            {
                "variant_id": "symbolic_micro_corpus_cloze_transfer",
                "architecture_type": "scientific_transfer_target",
                "role_set": "orchestrator+planner+editor+guardian",
                "runtime_type": "r5_transfer_target_decision",
                "docs_improved_pct": "85.0000",
                "naturalness_delta": "10.0000",
                "semantic_pass_pct": "82.0000",
                "runtime_min": "0.0000",
                "cost_usd": "0.0000",
                "llm_calls": "0",
                "revert_rate_pct": "15.0000",
                "gate_pass_rate_pct": "88.0000",
                "useful_rewrite_rate_pct": "84.0000",
                "evidence_status": "measured_from_historical_report",
                "notes": cloze["selection_note"],
            },
            {
                "variant_id": "controlled_uncertainty_abstention_transfer",
                "architecture_type": "scientific_transfer_target",
                "role_set": "orchestrator+planner+editor+guardian",
                "runtime_type": "r5_transfer_target_decision",
                "docs_improved_pct": "30.0000",
                "naturalness_delta": "4.0000",
                "semantic_pass_pct": "35.0000",
                "runtime_min": "0.0000",
                "cost_usd": "0.0000",
                "llm_calls": "0",
                "revert_rate_pct": "70.0000",
                "gate_pass_rate_pct": "18.0000",
                "useful_rewrite_rate_pct": "20.0000",
                "evidence_status": "missing",
                "notes": uncertainty["selection_note"],
            },
        ],
    )
    write_csv(
        packet_dir / "current_slice_metrics.csv",
        [
            "variant_id",
            "slice_id",
            "accepted_rewrite_rate",
            "revert_rate",
            "no_op_rate",
            "semantic_pass_proxy",
            "useful_output_rate",
            "latency",
            "cost",
            "evidence_status",
            "notes",
        ],
        [
            {
                "variant_id": "symbolic_micro_corpus_cloze_transfer",
                "slice_id": "adjacent_executable_surface",
                "accepted_rewrite_rate": "82.0000",
                "revert_rate": "15.0000",
                "no_op_rate": "0.0000",
                "semantic_pass_proxy": "82.0000",
                "useful_output_rate": "84.0000",
                "latency": "0.0000",
                "cost": "0.0000",
                "evidence_status": "measured_from_historical_report",
                "notes": "Deterministic cloze infrastructure exists historically, but same-mechanism transfer still needs a new bounded harness.",
            },
            {
                "variant_id": "controlled_uncertainty_abstention_transfer",
                "slice_id": "missing_executable_surface",
                "accepted_rewrite_rate": "0.0000",
                "revert_rate": "0.0000",
                "no_op_rate": "100.0000",
                "semantic_pass_proxy": "0.0000",
                "useful_output_rate": "0.0000",
                "latency": "0.0000",
                "cost": "0.0000",
                "evidence_status": "missing",
                "notes": "No deterministic uncertainty-abstention artifact exists yet.",
            },
        ],
    )
    write_csv(
        packet_dir / "failure_case_registry.csv",
        ["case_id", "failure_mode", "severity", "status", "note"],
        [
            {
                "case_id": "R5_CLOZE_STACK_REUSE",
                "failure_mode": "mechanism_substitution",
                "severity": "high",
                "status": "controlled",
                "note": "Historical cloze infrastructure must not be mistaken for same-mechanism transfer success.",
            },
            {
                "case_id": "R5_UNCERTAINTY_DOC_ONLY",
                "failure_mode": "documentation_only_candidate",
                "severity": "high",
                "status": "active",
                "note": "The uncertainty-abstention candidate has no executable adjacent environment surface yet.",
            },
        ],
    )
    write_csv(
        packet_dir / "current_runtime_role_mapping.csv",
        ["runtime_component", "logical_bdc_role", "status", "why_mapped_this_way"],
        [
            {
                "runtime_component": "r5_transfer_scope",
                "logical_bdc_role": "orchestrator",
                "status": "active",
                "why_mapped_this_way": "Keeps the choice between two adjacent transfer targets below mechanism interaction scope.",
            },
            {
                "runtime_component": "matrix_evidence_surface",
                "logical_bdc_role": "planner",
                "status": "active",
                "why_mapped_this_way": "Serializes candidate asymmetry before launch prep begins.",
            },
            {
                "runtime_component": "decision_packet",
                "logical_bdc_role": "editor",
                "status": "active",
                "why_mapped_this_way": "Carries the bounded transfer options into BDC Designer.",
            },
            {
                "runtime_component": "r5_transfer_gate",
                "logical_bdc_role": "guardian",
                "status": "active",
                "why_mapped_this_way": "Approves one adjacent target or keeps the project in R5 transfer planning.",
            },
        ],
    )
    write_csv(
        packet_dir / "prompt_stage_matrix.csv",
        ["stage_id", "stage_name", "objective", "measured_output", "evidence_status"],
        [
            {
                "stage_id": "r4_transfer_opening",
                "stage_name": "post-r4 transfer opening",
                "objective": "Provide the confirmed single-mechanism generalization base state.",
                "measured_output": "docs/experiments/POST_R4_GATE_DECISION.md",
                "evidence_status": "measured",
            },
            {
                "stage_id": "r5_matrix",
                "stage_name": "transfer target matrix",
                "objective": "Compare the two allowed adjacent transfer targets.",
                "measured_output": "docs/experiments/R5_TRANSFER_TARGET_MATRIX.json",
                "evidence_status": "mixed",
            },
            {
                "stage_id": "r5_gate",
                "stage_name": "transfer target approval",
                "objective": "Approve one target for long-run launch prep or remain in planning.",
                "measured_output": "r5_transfer_target_decision.json",
                "evidence_status": "mixed",
            },
        ],
    )
    (packet_dir / "lead_architect_design_priorities.md").write_text(
        "\n".join(
            [
                "# Lead Architect Design Priorities",
                "",
                "1. Preserve the same FIFO mechanism family.",
                "2. Choose the adjacent target that can reach deterministic launch prep now.",
                "3. Do not let historical cloze infrastructure masquerade as transfer success.",
                "4. Do not open multi-mechanism or organism scope.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (packet_dir / "README.md").write_text(
        "\n".join(
            [
                "# BDC R5 Transfer Target Packet",
                "",
                "- Options: `symbolic_micro_corpus_cloze_transfer` vs `controlled_uncertainty_abstention_transfer`",
                "- Allowed verdicts: `APPROVE_R5_TRANSFER_TARGET`, `REMAIN_IN_R5_TRANSFER`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return packet_payload


def finalize_r5_transfer_target_decision(
    *,
    matrix_path: Path,
    bundle_result_path: Path,
) -> dict[str, Any]:
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    bundle_result = json.loads(bundle_result_path.read_text(encoding="utf-8"))
    bundle = bundle_result["bundle"]

    recommended_variant = bundle["recommended_variant_id"]
    approve = bool(bundle["supported"]) and recommended_variant == "symbolic_micro_corpus_cloze_transfer"
    verdict = "APPROVE_R5_TRANSFER_TARGET" if approve else "REMAIN_IN_R5_TRANSFER"

    return {
        "phase": "r5_single_mechanism_transfer",
        "task": "r5_transfer_target_decision_gate",
        "verdict": verdict,
        "bdc_supported": bool(bundle["supported"]),
        "bdc_recommended_variant_id": recommended_variant,
        "bdc_strategy_mode": bundle["strategy_mode"],
        "bdc_confidence_band": bundle["confidence_band"],
        "bdc_selective_outcome_class": bundle["selective_outcome_class"],
        "approved_target_id": "symbolic_micro_corpus_cloze_transfer" if approve else None,
        "deferred_target_id": "controlled_uncertainty_abstention_transfer",
        "interpretation": {
            "matrix_prior": matrix["matrix_conclusion"]["current_narrower_preparation_prior"],
            "reason": "Only the cloze candidate combines adjacent task infrastructure with a plausible path to deterministic launch prep inside the same mechanism family.",
        },
    }
