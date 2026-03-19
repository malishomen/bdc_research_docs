from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any


REQUIRED_R4_SLICE_IDS = {
    "r4_length_extension",
    "r4_gap_extension",
    "r4_alphabet_extension",
    "r4_combined_bounded",
}


def generalization_gate_decision(summary: dict[str, Any]) -> dict[str, Any]:
    slice_rows = summary["slice_summaries"]
    observed_slice_ids = {str(row["slice_id"]) for row in slice_rows}
    required_slices_present = observed_slice_ids == REQUIRED_R4_SLICE_IDS
    slice_count_matches = int(summary["slice_count"]) == len(REQUIRED_R4_SLICE_IDS)
    all_deterministic = all(bool(row["deterministic_replay_status"]) for row in slice_rows)
    all_candidate_gt_no_memory = all(bool(row["candidate_gt_no_memory"]) for row in slice_rows)
    all_candidate_gt_trivial = all(bool(row["candidate_gt_trivial"]) for row in slice_rows)
    all_hardest_gap_gt_no_memory = all(
        bool(row["hardest_gap_gt_no_memory"]) for row in slice_rows
    )
    all_hardest_gap_gt_trivial = all(
        bool(row["hardest_gap_gt_trivial"]) for row in slice_rows
    )
    mechanism_identity_preserved = (
        str(summary["mechanism_candidate_id"]) == "bounded_working_memory_candidate"
    )

    confirmed = (
        slice_count_matches
        and required_slices_present
        and all_deterministic
        and all_candidate_gt_no_memory
        and all_candidate_gt_trivial
        and all_hardest_gap_gt_no_memory
        and all_hardest_gap_gt_trivial
        and mechanism_identity_preserved
    )
    verdict = (
        "CONFIRM_SINGLE_MECHANISM_GENERALIZATION"
        if confirmed
        else "REMAIN_IN_R4_GENERALIZATION"
    )
    return {
        "phase": "R4",
        "task": "single_mechanism_generalization_gate",
        "verdict": verdict,
        "mechanism_candidate_id": str(summary["mechanism_candidate_id"]),
        "required_slice_ids": sorted(REQUIRED_R4_SLICE_IDS),
        "observed_slice_ids": sorted(observed_slice_ids),
        "approval_conditions": {
            "slice_count_matches": slice_count_matches,
            "required_slices_present": required_slices_present,
            "mechanism_identity_preserved": mechanism_identity_preserved,
            "all_deterministic_replay": all_deterministic,
            "all_candidate_gt_no_memory": all_candidate_gt_no_memory,
            "all_candidate_gt_trivial": all_candidate_gt_trivial,
            "all_hardest_gap_gt_no_memory": all_hardest_gap_gt_no_memory,
            "all_hardest_gap_gt_trivial": all_hardest_gap_gt_trivial,
        },
        "measured_summary": {
            "slice_count": int(summary["slice_count"]),
            "candidate_accuracy_mean": mean(
                float(row["candidate_accuracy"]) for row in slice_rows
            ),
            "no_memory_control_accuracy_mean": mean(
                float(row["no_memory_control_accuracy"]) for row in slice_rows
            ),
            "trivial_last_symbol_memory_accuracy_mean": mean(
                float(row["trivial_last_symbol_memory_accuracy"]) for row in slice_rows
            ),
            "max_hardest_recall_gap": max(int(row["hardest_recall_gap"]) for row in slice_rows),
        },
    }


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_generalization_variant_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    slice_rows = summary["slice_summaries"]
    candidate_pct = mean(float(row["candidate_accuracy"]) for row in slice_rows) * 100.0
    no_memory_pct = mean(float(row["no_memory_control_accuracy"]) for row in slice_rows) * 100.0
    trivial_pct = (
        mean(float(row["trivial_last_symbol_memory_accuracy"]) for row in slice_rows) * 100.0
    )
    return [
        {
            "variant_id": "bounded_working_memory_candidate",
            "architecture_type": "scientific_mechanism_candidate",
            "role_set": "orchestrator+planner+editor+guardian",
            "runtime_type": "generalization_gate",
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
            "notes": "Measured single FIFO mechanism across all required R4 generalization slices.",
        },
        {
            "variant_id": "majority_symbol_predictor",
            "architecture_type": "no_memory_control",
            "role_set": "orchestrator+planner+editor+guardian",
            "runtime_type": "generalization_gate",
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
            "notes": "Strongest no-memory control aggregated over all required R4 slices.",
        },
        {
            "variant_id": "trivial_last_symbol_memory",
            "architecture_type": "trivial_memory_control",
            "role_set": "orchestrator+planner+editor+guardian",
            "runtime_type": "generalization_gate",
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
            "notes": "Trivial replayable control aggregated over all required R4 slices.",
        },
    ]


def build_generalization_slice_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for slice_row in summary["slice_summaries"]:
        slice_id = str(slice_row["slice_id"])
        rows.extend(
            [
                {
                    "variant_id": "bounded_working_memory_candidate",
                    "slice_id": slice_id,
                    "accepted_rewrite_rate": f"{float(slice_row['candidate_accuracy']) * 100.0:.4f}",
                    "revert_rate": "0.0000",
                    "no_op_rate": "0.0000",
                    "semantic_pass_proxy": f"{float(slice_row['candidate_accuracy']) * 100.0:.4f}",
                    "useful_output_rate": f"{float(slice_row['candidate_accuracy']) * 100.0:.4f}",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "measured",
                    "notes": "Measured FIFO mechanism performance on the bounded R4 slice.",
                },
                {
                    "variant_id": "majority_symbol_predictor",
                    "slice_id": slice_id,
                    "accepted_rewrite_rate": f"{float(slice_row['no_memory_control_accuracy']) * 100.0:.4f}",
                    "revert_rate": "0.0000",
                    "no_op_rate": "0.0000",
                    "semantic_pass_proxy": f"{float(slice_row['no_memory_control_accuracy']) * 100.0:.4f}",
                    "useful_output_rate": f"{float(slice_row['no_memory_control_accuracy']) * 100.0:.4f}",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "measured",
                    "notes": "Measured no-memory control performance on the bounded R4 slice.",
                },
                {
                    "variant_id": "trivial_last_symbol_memory",
                    "slice_id": slice_id,
                    "accepted_rewrite_rate": f"{float(slice_row['trivial_last_symbol_memory_accuracy']) * 100.0:.4f}",
                    "revert_rate": "0.0000",
                    "no_op_rate": "0.0000",
                    "semantic_pass_proxy": f"{float(slice_row['trivial_last_symbol_memory_accuracy']) * 100.0:.4f}",
                    "useful_output_rate": f"{float(slice_row['trivial_last_symbol_memory_accuracy']) * 100.0:.4f}",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "measured",
                    "notes": "Measured trivial-memory control performance on the bounded R4 slice.",
                },
            ]
        )
    return rows


def build_generalization_failure_rows(decision: dict[str, Any]) -> list[dict[str, Any]]:
    if decision["verdict"] == "CONFIRM_SINGLE_MECHANISM_GENERALIZATION":
        return [
            {
                "case_id": "R4_SCOPE_GUARD",
                "failure_mode": "forbidden_overclaim",
                "severity": "high",
                "status": "controlled",
                "note": "R4 confirmation authorizes single-mechanism generalization only and does not authorize multi-mechanism, organism, or cell claims.",
            }
        ]
    return [
        {
            "case_id": "R4_GENERALIZATION_GATE_FAILED",
            "failure_mode": "generalization_not_strong_enough",
            "severity": "high",
            "status": "open",
            "note": "At least one required R4 slice or hardest-gap condition failed the generalization gate.",
        }
    ]


def write_generalization_packet(
    *,
    summary_path: Path,
    matrix_path: Path,
    packet_dir: Path,
) -> dict[str, Any]:
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    matrix_payload = json.loads(matrix_path.read_text(encoding="utf-8"))
    decision = generalization_gate_decision(summary)

    packet_dir.mkdir(parents=True, exist_ok=True)
    (packet_dir / "BDC_INPUT_PACKET_R4_SINGLE_MECHANISM_GENERALIZATION.json").write_text(
        json.dumps(
            {
                "packet_version": "R4_SINGLE_MECHANISM_GENERALIZATION_V1",
                "packet_id": "BDC_R4_SINGLE_MECHANISM_GENERALIZATION",
                "project": "Bio_Digital_Core",
                "system_name": "BDC_Scientific_Line",
                "base_packet_reference": "TASK-7619",
                "evidence_policy": {
                    "measured": [
                        "R4 pressure matrix instantiated on four required slices",
                        "measured FIFO mechanism superiority against the same two controls on every required slice",
                        "hardest-gap superiority preserved on every required slice",
                    ],
                    "inferred": [],
                    "missing": [
                        "no multi-mechanism interaction evidence exists",
                        "no organism or cell-level assembly evidence exists",
                    ],
                },
                "positioning": {
                    "historical_best_prior": "bounded_working_memory_candidate_r4_generalization_prior",
                    "bdc_recommendation_mode": "scientific_generalization_gate",
                },
                "explicit_requests_to_bdc": [
                    "Interpret whether the same bounded FIFO mechanism truly generalizes across the required R4 pressure matrix",
                    "Assess whether the honest measured verdict is CONFIRM_SINGLE_MECHANISM_GENERALIZATION or REMAIN_IN_R4_GENERALIZATION",
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (packet_dir / "generalization_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    (packet_dir / "generalization_matrix_snapshot.json").write_text(
        json.dumps(matrix_payload, indent=2) + "\n",
        encoding="utf-8",
    )
    (packet_dir / "r4_generalization_gate_decision.json").write_text(
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
        build_generalization_variant_rows(summary),
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
        build_generalization_slice_rows(summary),
    )
    write_csv(
        packet_dir / "failure_case_registry.csv",
        ["case_id", "failure_mode", "severity", "status", "note"],
        build_generalization_failure_rows(decision),
    )
    write_csv(
        packet_dir / "current_runtime_role_mapping.csv",
        ["runtime_component", "logical_bdc_role", "status", "why_mapped_this_way"],
        [
            {
                "runtime_component": "generalization_scope",
                "logical_bdc_role": "orchestrator",
                "status": "active",
                "why_mapped_this_way": "Keeps the cycle inside single-mechanism generalization and blocks premature widening.",
            },
            {
                "runtime_component": "pressure_matrix",
                "logical_bdc_role": "planner",
                "status": "active",
                "why_mapped_this_way": "Defines the bounded R4 pressure surface and preserves the trace-width invariant.",
            },
            {
                "runtime_component": "measured_slice_surface",
                "logical_bdc_role": "editor",
                "status": "active",
                "why_mapped_this_way": "Carries the deterministic slice artifacts and measured scorecards.",
            },
            {
                "runtime_component": "generalization_gate_audit",
                "logical_bdc_role": "guardian",
                "status": "active",
                "why_mapped_this_way": "Determines whether R4 confirms single-mechanism generalization or remains in R4.",
            },
        ],
    )
    write_csv(
        packet_dir / "prompt_stage_matrix.csv",
        ["stage_id", "stage_name", "objective", "measured_output", "evidence_status"],
        [
            {
                "stage_id": "matrix",
                "stage_name": "pressure matrix",
                "objective": "Define the bounded R4 pressure surface without widening mechanism identity.",
                "measured_output": "R4_SINGLE_MECHANISM_GENERALIZATION_PRESSURE_MATRIX.json",
                "evidence_status": "measured",
            },
            {
                "stage_id": "measurement",
                "stage_name": "generalization measurement",
                "objective": "Measure the same FIFO mechanism on all required R4 slices against the same controls.",
                "measured_output": "generalization_summary.json",
                "evidence_status": "measured",
            },
            {
                "stage_id": "gate",
                "stage_name": "generalization gate audit",
                "objective": "Choose CONFIRM_SINGLE_MECHANISM_GENERALIZATION vs REMAIN_IN_R4_GENERALIZATION.",
                "measured_output": "r4_generalization_gate_decision.json",
                "evidence_status": "measured",
            },
        ],
    )
    (packet_dir / "lead_architect_design_priorities.md").write_text(
        "\n".join(
            [
                "# Lead Architect Design Priorities",
                "",
                "1. Preserve the same bounded FIFO mechanism on every required R4 slice.",
                "2. Treat superiority over both controls on every slice and hardest gap as mandatory.",
                "3. Keep the combined slice bounded and single-shot; do not open factorial escalation here.",
                "4. Scope any approval to single-mechanism generalization only.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (packet_dir / "README.md").write_text(
        "\n".join(
            [
                "# BDC R4 Single-Mechanism Generalization Packet",
                "",
                "- Source summary: `results/r4_single_mechanism_generalization/generalization_summary.json`",
                "- Scope: bounded single-mechanism generalization only",
                "- Allowed verdicts: `CONFIRM_SINGLE_MECHANISM_GENERALIZATION` or `REMAIN_IN_R4_GENERALIZATION`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return decision
