from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Sequence

from evolution.micro_tasks.sequence_memory_mechanism_gate import (
    build_failure_rows,
    build_slice_rows,
    build_variant_rows,
    write_csv,
)


def control_resistant_conditions_pass(dataset_rows: Sequence[dict[str, Any]]) -> bool:
    for row in dataset_rows:
        sequence = [int(symbol) for symbol in row["sequence"]]
        target_symbol = int(row["target_symbol"])
        if target_symbol == int(sequence[-1]):
            return False
        counts: dict[int, int] = {}
        for symbol in sequence:
            counts[symbol] = counts.get(symbol, 0) + 1
        majority_symbol = min((-count, symbol) for symbol, count in counts.items())[1]
        if target_symbol == int(majority_symbol):
            return False
    return True


def second_bounded_signal_decision(
    scorecard: dict[str, Any],
    *,
    control_conditions_pass: bool,
) -> dict[str, Any]:
    hardest_gap = scorecard["hardest_gap_accuracy"]
    confirmed = (
        bool(scorecard["deterministic_replay_status"])
        and bool(control_conditions_pass)
        and float(scorecard["candidate_accuracy"]) > float(scorecard["no_memory_control_accuracy"])
        and float(scorecard["candidate_accuracy"])
        > float(scorecard["trivial_last_symbol_memory_accuracy"])
        and float(hardest_gap["candidate_accuracy"])
        > float(hardest_gap["no_memory_control_accuracy"])
        and float(hardest_gap["candidate_accuracy"])
        > float(hardest_gap["trivial_last_symbol_memory_accuracy"])
    )
    verdict = (
        "CONFIRM_SECOND_BOUNDED_SIGNAL"
        if confirmed
        else "REMAIN_IN_R3_CONTINUATION"
    )
    return {
        "phase": "R3",
        "task": "second_bounded_signal_gate",
        "verdict": verdict,
        "mechanism_candidate_id": scorecard["mechanism_candidate_id"],
        "control_resistant_conditions_pass": bool(control_conditions_pass),
        "approval_conditions": {
            "deterministic_replay_status": bool(scorecard["deterministic_replay_status"]),
            "control_resistant_conditions_pass": bool(control_conditions_pass),
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
            "hardest_recall_gap": int(scorecard["hardest_recall_gap"]),
        },
    }


def write_second_signal_packet(
    *,
    scorecard_path: Path,
    dataset_path: Path,
    packet_dir: Path,
) -> dict[str, Any]:
    scorecard = json.loads(scorecard_path.read_text(encoding="utf-8"))
    dataset_rows = json.loads(dataset_path.read_text(encoding="utf-8"))
    control_pass = control_resistant_conditions_pass(dataset_rows)
    decision = second_bounded_signal_decision(
        scorecard,
        control_conditions_pass=control_pass,
    )

    packet_dir.mkdir(parents=True, exist_ok=True)
    (packet_dir / "BDC_INPUT_PACKET_R3_SECOND_BOUNDED_SIGNAL.json").write_text(
        json.dumps(
            {
                "packet_version": "R3_SECOND_BOUNDED_SIGNAL_V1",
                "packet_id": "BDC_R3_SECOND_BOUNDED_SIGNAL",
                "project": "Bio_Digital_Core",
                "system_name": "BDC_Scientific_Line",
                "base_packet_reference": "TASK-7613",
                "evidence_policy": {
                    "measured": [
                        "control-resistant dataset artifact",
                        "bounded FIFO mechanism scorecard on stricter slice",
                        "control-resistant conditions verified over the dataset",
                    ],
                    "inferred": [],
                    "missing": [
                        "no multi-mechanism evidence exists",
                        "no organism-level assembly evidence exists",
                    ],
                },
                "positioning": {
                    "historical_best_prior": "bounded_working_memory_candidate_r3_continuation",
                    "bdc_recommendation_mode": "scientific_second_signal_gate",
                },
                "explicit_requests_to_bdc": [
                    "Interpret whether the control-resistant continuation confirms a second bounded signal for the same memory mechanism",
                    "Assess whether the honest measured verdict is CONFIRM_SECOND_BOUNDED_SIGNAL or REMAIN_IN_R3_CONTINUATION",
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
    (packet_dir / "control_resistant_dataset.json").write_text(
        json.dumps(dataset_rows, indent=2) + "\n",
        encoding="utf-8",
    )
    (packet_dir / "r3_second_bounded_signal_decision.json").write_text(
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
        build_failure_rows(
            {
                "verdict": (
                    "APPROVE_MECHANISM_CONTINUATION"
                    if decision["verdict"] == "CONFIRM_SECOND_BOUNDED_SIGNAL"
                    else "REMAIN_IN_MECHANISM_PHASE"
                )
            }
        ),
    )
    write_csv(
        packet_dir / "current_runtime_role_mapping.csv",
        ["runtime_component", "logical_bdc_role", "status", "why_mapped_this_way"],
        [
            {
                "runtime_component": "continuation_scope",
                "logical_bdc_role": "orchestrator",
                "status": "active",
                "why_mapped_this_way": "Keeps the cycle inside the same environment and mechanism family.",
            },
            {
                "runtime_component": "control_resistant_conditions",
                "logical_bdc_role": "planner",
                "status": "active",
                "why_mapped_this_way": "Defines target != last and target != majority as mandatory slice constraints.",
            },
            {
                "runtime_component": "measured_artifact_surface",
                "logical_bdc_role": "editor",
                "status": "active",
                "why_mapped_this_way": "Carries the stricter dataset and measured scorecard.",
            },
            {
                "runtime_component": "second_signal_gate",
                "logical_bdc_role": "guardian",
                "status": "active",
                "why_mapped_this_way": "Determines whether a second bounded signal is confirmed.",
            },
        ],
    )
    write_csv(
        packet_dir / "prompt_stage_matrix.csv",
        ["stage_id", "stage_name", "objective", "measured_output", "evidence_status"],
        [
            {
                "stage_id": "continuation_package",
                "stage_name": "control-resistant package",
                "objective": "Define a stricter continuation inside the same environment family.",
                "measured_output": "EXP-0806_R3_CONTROL_RESISTANT_SEQUENCE_MEMORY_CONTINUATION.md",
                "evidence_status": "measured",
            },
            {
                "stage_id": "artifact",
                "stage_name": "control-resistant artifact",
                "objective": "Generate the stricter dataset and re-measure the same FIFO mechanism.",
                "measured_output": "mechanism_scorecard.json, control_resistant_dataset.json",
                "evidence_status": "measured",
            },
            {
                "stage_id": "gate",
                "stage_name": "second bounded signal gate",
                "objective": "Choose CONFIRM_SECOND_BOUNDED_SIGNAL vs REMAIN_IN_R3_CONTINUATION.",
                "measured_output": "r3_second_bounded_signal_decision.json",
                "evidence_status": "measured",
            },
        ],
    )
    (packet_dir / "lead_architect_design_priorities.md").write_text(
        "\n".join(
            [
                "# Lead Architect Design Priorities",
                "",
                "1. Preserve the same bounded FIFO mechanism; do not add a second mechanism.",
                "2. Treat control-resistant conditions as mandatory, not advisory.",
                "3. Confirm a second bounded signal only if measured superiority survives the stricter slice.",
                "4. Do not widen beyond bounded mechanism continuation.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (packet_dir / "README.md").write_text(
        "\n".join(
            [
                "# BDC R3 Second Bounded Signal Packet",
                "",
                "- Source scorecard: `results/r3_control_resistant_sequence_memory/mechanism_scorecard.json`",
                "- Scope: stricter continuation inside the same sequence-memory family",
                "- Allowed verdicts: `CONFIRM_SECOND_BOUNDED_SIGNAL` or `REMAIN_IN_R3_CONTINUATION`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return decision
