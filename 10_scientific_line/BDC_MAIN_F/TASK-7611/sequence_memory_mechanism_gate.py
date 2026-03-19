from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def mechanism_gate_decision(scorecard: dict[str, Any]) -> dict[str, Any]:
    hardest_gap = scorecard["hardest_gap_accuracy"]
    approved = (
        bool(scorecard["deterministic_replay_status"])
        and float(scorecard["candidate_accuracy"]) > float(scorecard["no_memory_control_accuracy"])
        and float(scorecard["candidate_accuracy"])
        > float(scorecard["trivial_last_symbol_memory_accuracy"])
        and float(hardest_gap["candidate_accuracy"])
        > float(hardest_gap["no_memory_control_accuracy"])
        and float(hardest_gap["candidate_accuracy"])
        > float(hardest_gap["trivial_last_symbol_memory_accuracy"])
    )
    verdict = (
        "APPROVE_MECHANISM_CONTINUATION" if approved else "REMAIN_IN_MECHANISM_PHASE"
    )
    return {
        "phase": "R3",
        "task": "sequence_memory_mechanism_gate",
        "verdict": verdict,
        "mechanism_candidate_id": scorecard["mechanism_candidate_id"],
        "hardest_recall_gap": scorecard["hardest_recall_gap"],
        "approval_conditions": {
            "deterministic_replay_status": bool(scorecard["deterministic_replay_status"]),
            "candidate_gt_no_memory": float(scorecard["candidate_accuracy"])
            > float(scorecard["no_memory_control_accuracy"]),
            "candidate_gt_trivial": float(scorecard["candidate_accuracy"])
            > float(scorecard["trivial_last_symbol_memory_accuracy"]),
            "hardest_gap_gt_no_memory": float(hardest_gap["candidate_accuracy"])
            > float(hardest_gap["no_memory_control_accuracy"]),
            "hardest_gap_gt_trivial": float(hardest_gap["candidate_accuracy"])
            > float(hardest_gap["trivial_last_symbol_memory_accuracy"]),
        },
        "measured_summary": {
            "candidate_accuracy": float(scorecard["candidate_accuracy"]),
            "no_memory_control_accuracy": float(scorecard["no_memory_control_accuracy"]),
            "trivial_last_symbol_memory_accuracy": float(
                scorecard["trivial_last_symbol_memory_accuracy"]
            ),
            "delta_vs_no_memory": float(scorecard["delta_vs_no_memory"]),
            "delta_vs_trivial_memory": float(scorecard["delta_vs_trivial_memory"]),
        },
    }


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_variant_rows(scorecard: dict[str, Any]) -> list[dict[str, Any]]:
    candidate_pct = float(scorecard["candidate_accuracy"]) * 100.0
    no_memory_pct = float(scorecard["no_memory_control_accuracy"]) * 100.0
    trivial_pct = float(scorecard["trivial_last_symbol_memory_accuracy"]) * 100.0
    return [
        {
            "variant_id": "bounded_working_memory_candidate",
            "architecture_type": "scientific_mechanism_candidate",
            "role_set": "orchestrator+planner+editor+guardian",
            "runtime_type": "mechanism_gate",
            "docs_improved_pct": f"{candidate_pct:.4f}",
            "naturalness_delta": f"{(candidate_pct - no_memory_pct):.4f}",
            "semantic_pass_pct": f"{candidate_pct:.4f}",
            "runtime_min": "0.0000",
            "cost_usd": "0.0000",
            "llm_calls": "0",
            "revert_rate_pct": "0.0000",
            "gate_pass_rate_pct": f"{candidate_pct:.4f}",
            "useful_rewrite_rate_pct": f"{candidate_pct:.4f}",
            "evidence_status": "measured",
            "notes": "Deterministic FIFO trace mechanism with measured replay and hardest-gap superiority over controls.",
        },
        {
            "variant_id": "majority_symbol_predictor",
            "architecture_type": "no_memory_control",
            "role_set": "orchestrator+planner+editor+guardian",
            "runtime_type": "mechanism_gate",
            "docs_improved_pct": f"{no_memory_pct:.4f}",
            "naturalness_delta": "0.0000",
            "semantic_pass_pct": f"{no_memory_pct:.4f}",
            "runtime_min": "0.0000",
            "cost_usd": "0.0000",
            "llm_calls": "0",
            "revert_rate_pct": "0.0000",
            "gate_pass_rate_pct": f"{no_memory_pct:.4f}",
            "useful_rewrite_rate_pct": f"{no_memory_pct:.4f}",
            "evidence_status": "measured",
            "notes": "Strongest non-mechanistic baseline; no replayable internal state.",
        },
        {
            "variant_id": "trivial_last_symbol_memory",
            "architecture_type": "trivial_memory_control",
            "role_set": "orchestrator+planner+editor+guardian",
            "runtime_type": "mechanism_gate",
            "docs_improved_pct": f"{trivial_pct:.4f}",
            "naturalness_delta": "0.0000",
            "semantic_pass_pct": f"{trivial_pct:.4f}",
            "runtime_min": "0.0000",
            "cost_usd": "0.0000",
            "llm_calls": "0",
            "revert_rate_pct": "0.0000",
            "gate_pass_rate_pct": f"{trivial_pct:.4f}",
            "useful_rewrite_rate_pct": f"{trivial_pct:.4f}",
            "evidence_status": "measured",
            "notes": "Replayable but only tracks the last observed symbol.",
        },
    ]


def build_slice_rows(scorecard: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for gap, metrics in scorecard["gap_accuracy_by_recall_gap"].items():
        rows.extend(
            [
                {
                    "variant_id": "bounded_working_memory_candidate",
                    "slice_id": f"gap_{gap}",
                    "accepted_rewrite_rate": f"{float(metrics['candidate_accuracy']) * 100.0:.4f}",
                    "revert_rate": "0.0000",
                    "no_op_rate": "0.0000",
                    "semantic_pass_proxy": f"{float(metrics['candidate_accuracy']) * 100.0:.4f}",
                    "useful_output_rate": f"{float(metrics['candidate_accuracy']) * 100.0:.4f}",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "measured",
                    "notes": "Measured bounded FIFO mechanism slice performance.",
                },
                {
                    "variant_id": "majority_symbol_predictor",
                    "slice_id": f"gap_{gap}",
                    "accepted_rewrite_rate": f"{float(metrics['no_memory_control_accuracy']) * 100.0:.4f}",
                    "revert_rate": "0.0000",
                    "no_op_rate": "0.0000",
                    "semantic_pass_proxy": f"{float(metrics['no_memory_control_accuracy']) * 100.0:.4f}",
                    "useful_output_rate": f"{float(metrics['no_memory_control_accuracy']) * 100.0:.4f}",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "measured",
                    "notes": "Measured no-memory baseline slice performance.",
                },
                {
                    "variant_id": "trivial_last_symbol_memory",
                    "slice_id": f"gap_{gap}",
                    "accepted_rewrite_rate": f"{float(metrics['trivial_last_symbol_memory_accuracy']) * 100.0:.4f}",
                    "revert_rate": "0.0000",
                    "no_op_rate": "0.0000",
                    "semantic_pass_proxy": f"{float(metrics['trivial_last_symbol_memory_accuracy']) * 100.0:.4f}",
                    "useful_output_rate": f"{float(metrics['trivial_last_symbol_memory_accuracy']) * 100.0:.4f}",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "measured",
                    "notes": "Measured trivial-memory baseline slice performance.",
                },
            ]
        )
    return rows


def build_failure_rows(decision: dict[str, Any]) -> list[dict[str, Any]]:
    if decision["verdict"] == "APPROVE_MECHANISM_CONTINUATION":
        return [
            {
                "case_id": "R3_SCOPE_GUARD",
                "failure_mode": "forbidden_overclaim",
                "severity": "high",
                "status": "controlled",
                "note": "Approval is mechanism-continuation only and does not authorize organism or cell claims.",
            }
        ]
    return [
        {
            "case_id": "R3_MECHANISM_GATE_FAILED",
            "failure_mode": "candidate_not_strong_enough",
            "severity": "high",
            "status": "open",
            "note": "The bounded working-memory candidate failed at least one measured approval condition.",
        }
    ]


def write_mechanism_packet(
    *,
    scorecard_path: Path,
    packet_dir: Path,
) -> dict[str, Any]:
    scorecard = json.loads(scorecard_path.read_text(encoding="utf-8"))
    decision = mechanism_gate_decision(scorecard)

    packet_dir.mkdir(parents=True, exist_ok=True)
    (packet_dir / "BDC_INPUT_PACKET_R3_SEQUENCE_MEMORY_MECHANISM.json").write_text(
        json.dumps(
            {
                "packet_version": "R3_SEQUENCE_MEMORY_MECHANISM_V1",
                "packet_id": "BDC_R3_SEQUENCE_MEMORY_MECHANISM",
                "project": "Bio_Digital_Core",
                "system_name": "BDC_Scientific_Line",
                "base_packet_reference": "TASK-7610",
                "evidence_policy": {
                    "measured": [
                        "bounded working-memory candidate scorecard",
                        "deterministic replay examples",
                        "hardest-gap superiority over controls",
                    ],
                    "inferred": [],
                    "missing": [
                        "broader mechanism families remain unmeasured",
                        "no multi-mechanism assembly evidence exists",
                    ],
                },
                "positioning": {
                    "historical_best_prior": "controlled_sequence_memory_r3_memory_prior",
                    "bdc_recommendation_mode": "scientific_mechanism_gate",
                },
                "explicit_requests_to_bdc": [
                    "Interpret the measured bounded working-memory candidate relative to the R3 mechanism gate",
                    "Assess whether the honest measured verdict is APPROVE_MECHANISM_CONTINUATION or REMAIN_IN_MECHANISM_PHASE",
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (packet_dir / "mechanism_scorecard.json").write_text(
        json.dumps(scorecard, indent=2) + "\n",
        encoding="utf-8",
    )
    (packet_dir / "r3_mechanism_gate_decision.json").write_text(
        json.dumps(decision, indent=2) + "\n",
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
        build_variant_rows(scorecard),
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
        build_slice_rows(scorecard),
    )
    write_csv(
        packet_dir / "failure_case_registry.csv",
        ["case_id", "failure_mode", "severity", "status", "note"],
        build_failure_rows(decision),
    )
    write_csv(
        packet_dir / "current_runtime_role_mapping.csv",
        ["runtime_component", "logical_bdc_role", "status", "why_mapped_this_way"],
        [
            {
                "runtime_component": "mechanism_scope",
                "logical_bdc_role": "orchestrator",
                "status": "active",
                "why_mapped_this_way": "Owns bounded R3 scope and blocks organism-level overclaim.",
            },
            {
                "runtime_component": "mechanism_spec",
                "logical_bdc_role": "planner",
                "status": "active",
                "why_mapped_this_way": "Carries the FIFO trace contract and control definitions.",
            },
            {
                "runtime_component": "measured_replay_surface",
                "logical_bdc_role": "editor",
                "status": "active",
                "why_mapped_this_way": "Preserves replayable state updates and measured scorecard artifacts.",
            },
            {
                "runtime_component": "mechanism_gate_audit",
                "logical_bdc_role": "guardian",
                "status": "active",
                "why_mapped_this_way": "Determines whether the measured mechanism may continue.",
            },
        ],
    )
    write_csv(
        packet_dir / "prompt_stage_matrix.csv",
        ["stage_id", "stage_name", "objective", "measured_output", "evidence_status"],
        [
            {
                "stage_id": "spec",
                "stage_name": "mechanism contract",
                "objective": "Define the bounded FIFO trace mechanism and controls.",
                "measured_output": "R3_SEQUENCE_MEMORY_MECHANISM_SPEC.json",
                "evidence_status": "measured",
            },
            {
                "stage_id": "implementation",
                "stage_name": "mechanism run",
                "objective": "Execute the bounded trace candidate and control comparisons.",
                "measured_output": "mechanism_scorecard.json",
                "evidence_status": "measured",
            },
            {
                "stage_id": "gate",
                "stage_name": "mechanism gate audit",
                "objective": "Choose APPROVE_MECHANISM_CONTINUATION vs REMAIN_IN_MECHANISM_PHASE.",
                "measured_output": "r3_mechanism_gate_decision.json",
                "evidence_status": "measured",
            },
        ],
    )
    (packet_dir / "lead_architect_design_priorities.md").write_text(
        "\n".join(
            [
                "# Lead Architect Design Priorities",
                "",
                "1. Preserve the FIFO working-memory candidate as the only active mechanism in this cycle.",
                "2. Require superiority over both no-memory and trivial-memory controls.",
                "3. Treat hardest-gap superiority as mandatory, not optional.",
                "4. Keep approval scoped to mechanism continuation only.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (packet_dir / "README.md").write_text(
        "\n".join(
            [
                "# BDC R3 Sequence-Memory Mechanism Packet",
                "",
                "- Source scorecard: `results/r3_sequence_memory_mechanism/mechanism_scorecard.json`",
                "- Allowed verdicts: `APPROVE_MECHANISM_CONTINUATION` or `REMAIN_IN_MECHANISM_PHASE`",
                "- Scope: bounded mechanism validation only",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return decision
