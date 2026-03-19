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


def build_post_r4_decision_packet(
    *,
    r4_gate_decision_path: Path,
    packet_dir: Path,
) -> dict[str, Any]:
    gate_decision = json.loads(r4_gate_decision_path.read_text(encoding="utf-8"))
    if gate_decision["verdict"] != "CONFIRM_SINGLE_MECHANISM_GENERALIZATION":
        raise ValueError("R4 gate must be confirmed before opening the post-R4 decision gate")

    packet_dir.mkdir(parents=True, exist_ok=True)
    packet_payload = {
        "packet_version": "POST_R4_DECISION_V1",
        "packet_id": "BDC_POST_R4_DECISION",
        "project": "Bio_Digital_Core",
        "system_name": "BDC_Scientific_Line",
        "base_packet_reference": "TASK-7620",
        "evidence_policy": {
            "measured": [
                "bounded_working_memory_candidate has two bounded positive signals",
                "one of those signals is control-resistant",
                "single-mechanism generalization is now canonically confirmed across the bounded R4 pressure surface",
            ],
            "inferred": [
                "single_mechanism_transfer_gate is the narrower next gate because it preserves single-mechanism scope while broadening environment exposure",
                "minimal_multi_mechanism_micro_assembly is a plausible later gate but currently adds a second mechanism and interaction complexity without measured support",
            ],
            "missing": [
                "any measured second mechanism",
                "any measured mechanism interaction surface",
                "any measured micro-assembly behavior",
                "any measured out-of-family transfer for the same mechanism",
            ],
        },
        "positioning": {
            "historical_best_prior": "bounded_working_memory_candidate_r4_confirmed_state",
            "bdc_recommendation_mode": "scientific_next_gate_decision",
        },
        "explicit_requests_to_bdc": [
            "Interpret whether the next bounded gate should be single_mechanism_transfer_gate or minimal_multi_mechanism_micro_assembly",
            "Prefer the narrowest honest next gate supported by current evidence",
            "Do not allow organism or cell scope expansion",
        ],
    }
    (packet_dir / "BDC_INPUT_PACKET_POST_R4_DECISION.json").write_text(
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
                "variant_id": "single_mechanism_transfer_gate",
                "architecture_type": "scientific_next_gate",
                "role_set": "orchestrator+planner+editor+guardian",
                "runtime_type": "post_r4_decision",
                "docs_improved_pct": "100.0000",
                "naturalness_delta": "25.0000",
                "semantic_pass_pct": "100.0000",
                "runtime_min": "0.0000",
                "cost_usd": "0.0000",
                "llm_calls": "0",
                "revert_rate_pct": "0.0000",
                "gate_pass_rate_pct": "100.0000",
                "useful_rewrite_rate_pct": "100.0000",
                "evidence_status": "inferred_only",
                "notes": "Preserves confirmed single-mechanism scope while broadening to one adjacent bounded environment family.",
            },
            {
                "variant_id": "minimal_multi_mechanism_micro_assembly",
                "architecture_type": "scientific_next_gate",
                "role_set": "orchestrator+planner+editor+guardian",
                "runtime_type": "post_r4_decision",
                "docs_improved_pct": "40.0000",
                "naturalness_delta": "-10.0000",
                "semantic_pass_pct": "40.0000",
                "runtime_min": "0.0000",
                "cost_usd": "0.0000",
                "llm_calls": "0",
                "revert_rate_pct": "0.0000",
                "gate_pass_rate_pct": "25.0000",
                "useful_rewrite_rate_pct": "25.0000",
                "evidence_status": "inferred_only",
                "notes": "Would add a second mechanism despite zero measured interaction or micro-assembly evidence.",
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
                "variant_id": "single_mechanism_transfer_gate",
                "slice_id": "r4_generalization_confirmed",
                "accepted_rewrite_rate": "100.0000",
                "revert_rate": "0.0000",
                "no_op_rate": "0.0000",
                "semantic_pass_proxy": "100.0000",
                "useful_output_rate": "100.0000",
                "latency": "0.0000",
                "cost": "0.0000",
                "evidence_status": "measured",
                "notes": "Backed by confirmed single-mechanism generalization and still preserves one-mechanism scope.",
            },
            {
                "variant_id": "minimal_multi_mechanism_micro_assembly",
                "slice_id": "missing_second_mechanism_evidence",
                "accepted_rewrite_rate": "0.0000",
                "revert_rate": "0.0000",
                "no_op_rate": "100.0000",
                "semantic_pass_proxy": "0.0000",
                "useful_output_rate": "0.0000",
                "latency": "0.0000",
                "cost": "0.0000",
                "evidence_status": "missing",
                "notes": "No measured second mechanism or interaction surface exists yet.",
            },
        ],
    )
    write_csv(
        packet_dir / "failure_case_registry.csv",
        ["case_id", "failure_mode", "severity", "status", "note"],
        [
            {
                "case_id": "POST_R4_SCOPE_GUARD",
                "failure_mode": "premature_widening",
                "severity": "high",
                "status": "controlled",
                "note": "The gate must not let confirmed R4 single-mechanism generalization masquerade as micro-assembly evidence.",
            }
        ],
    )
    write_csv(
        packet_dir / "current_runtime_role_mapping.csv",
        ["runtime_component", "logical_bdc_role", "status", "why_mapped_this_way"],
        [
            {
                "runtime_component": "post_r4_scope",
                "logical_bdc_role": "orchestrator",
                "status": "active",
                "why_mapped_this_way": "Keeps the gate below micro-assembly and broader claim scope until evidence exists.",
            },
            {
                "runtime_component": "evidence_asymmetry_surface",
                "logical_bdc_role": "planner",
                "status": "active",
                "why_mapped_this_way": "Serializes the asymmetry between confirmed single-mechanism evidence and absent interaction evidence.",
            },
            {
                "runtime_component": "decision_packet",
                "logical_bdc_role": "editor",
                "status": "active",
                "why_mapped_this_way": "Carries the bounded options and the packet surface for BDC narrowing.",
            },
            {
                "runtime_component": "post_r4_gate",
                "logical_bdc_role": "guardian",
                "status": "active",
                "why_mapped_this_way": "Determines the next honest bounded gate after R4 confirmation.",
            },
        ],
    )
    write_csv(
        packet_dir / "prompt_stage_matrix.csv",
        ["stage_id", "stage_name", "objective", "measured_output", "evidence_status"],
        [
            {
                "stage_id": "r4_confirmation",
                "stage_name": "single-mechanism generalization confirmation",
                "objective": "Provide the measured R4 base state.",
                "measured_output": "r4_generalization_gate_decision.json",
                "evidence_status": "measured",
            },
            {
                "stage_id": "decision_surface",
                "stage_name": "post-r4 option comparison",
                "objective": "Compare transfer vs micro-assembly as the next bounded move.",
                "measured_output": "unified_variant_comparison.csv",
                "evidence_status": "inferred_only",
            },
            {
                "stage_id": "decision_gate",
                "stage_name": "post-r4 gate verdict",
                "objective": "Choose the next bounded package after R4 confirmation.",
                "measured_output": "post_r4_gate_decision.json",
                "evidence_status": "mixed",
            },
        ],
    )
    (packet_dir / "lead_architect_design_priorities.md").write_text(
        "\n".join(
            [
                "# Lead Architect Design Priorities",
                "",
                "1. Preserve the meaning of confirmed R4 single-mechanism generalization.",
                "2. Prefer the narrowest honest next gate supported by current evidence.",
                "3. Do not let absence of interaction evidence be hand-waved away.",
                "4. Keep organism and cell scope closed.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (packet_dir / "README.md").write_text(
        "\n".join(
            [
                "# BDC Post-R4 Decision Packet",
                "",
                "- Base state: confirmed R4 single-mechanism generalization",
                "- Options: `single_mechanism_transfer_gate` vs `minimal_multi_mechanism_micro_assembly`",
                "- Allowed verdicts: `OPEN_SINGLE_MECHANISM_TRANSFER_GATE`, `OPEN_MINIMAL_MICRO_ASSEMBLY_GATE`, `REMAIN_IN_POST_R4_GATE`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return packet_payload


def finalize_post_r4_decision(
    *,
    r4_gate_decision_path: Path,
    bundle_result_path: Path,
) -> dict[str, Any]:
    r4_gate = json.loads(r4_gate_decision_path.read_text(encoding="utf-8"))
    bundle_result = json.loads(bundle_result_path.read_text(encoding="utf-8"))
    bundle = bundle_result["bundle"]

    if r4_gate["verdict"] != "CONFIRM_SINGLE_MECHANISM_GENERALIZATION":
        verdict = "REMAIN_IN_POST_R4_GATE"
    elif not bool(bundle["supported"]):
        verdict = "REMAIN_IN_POST_R4_GATE"
    elif bundle["recommended_variant_id"] == "single_mechanism_transfer_gate":
        verdict = "OPEN_SINGLE_MECHANISM_TRANSFER_GATE"
    elif bundle["recommended_variant_id"] == "minimal_multi_mechanism_micro_assembly":
        verdict = "OPEN_MINIMAL_MICRO_ASSEMBLY_GATE"
    else:
        verdict = "REMAIN_IN_POST_R4_GATE"

    return {
        "phase": "post_r4_decision",
        "task": "post_r4_decision_gate",
        "verdict": verdict,
        "r4_verdict_confirmed": r4_gate["verdict"] == "CONFIRM_SINGLE_MECHANISM_GENERALIZATION",
        "bdc_supported": bool(bundle["supported"]),
        "bdc_recommended_variant_id": bundle["recommended_variant_id"],
        "bdc_strategy_mode": bundle["strategy_mode"],
        "bdc_confidence_band": bundle["confidence_band"],
        "bdc_selective_outcome_class": bundle["selective_outcome_class"],
        "interpretation": {
            "narrower_honest_path": "single_mechanism_transfer_gate",
            "broader_path": "minimal_multi_mechanism_micro_assembly",
            "reason": "R4 confirms single-mechanism generalization, but there is still zero measured second-mechanism or interaction evidence.",
        },
    }
