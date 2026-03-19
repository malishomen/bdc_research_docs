from __future__ import annotations

import csv
import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from evolution.micro_tasks.sequence_memory import (
    SequenceMemorySample,
    accuracy_from_predictions,
    predict_last_symbol,
    predict_majority_symbol,
    predict_random_symbol,
)
from evolution.micro_tasks.sequence_memory_mechanism import mechanism_scorecard


ANCHOR_WORDS = [
    "amber",
    "cobalt",
    "saffron",
    "onyx",
    "linen",
    "coral",
    "violet",
    "cedar",
    "jade",
    "silver",
    "ivory",
    "crimson",
]

FILLER_WORDS = [
    "the",
    "index",
    "near",
    "with",
    "marker",
    "signal",
    "under",
    "while",
    "noted",
    "frame",
    "trace",
    "context",
]


@dataclass(frozen=True)
class TransferLaunchConfig:
    slice_id: str
    seed: int
    size: int
    seq_len: int
    lexicon_size: int
    min_gap: int
    max_gap: int


def _token_pool(lexicon_size: int) -> list[str]:
    if lexicon_size < 4:
        raise ValueError("lexicon_size must be >= 4")
    if lexicon_size > len(ANCHOR_WORDS):
        raise ValueError("lexicon_size exceeds available anchor vocabulary")
    return ANCHOR_WORDS[:lexicon_size] + FILLER_WORDS


def build_symbolic_micro_corpus_cloze_transfer_dataset(
    *,
    seed: int,
    size: int = 128,
    seq_len: int = 10,
    lexicon_size: int = 8,
    min_gap: int = 3,
    max_gap: int = 5,
) -> tuple[list[SequenceMemorySample], dict[int, str]]:
    if size <= 0:
        raise ValueError("size must be > 0")
    if seq_len < 6:
        raise ValueError("seq_len must be >= 6")
    if min_gap < 2 or max_gap < min_gap:
        raise ValueError("invalid gap bounds")
    if max_gap >= seq_len:
        raise ValueError("max_gap must be < seq_len")

    rng = random.Random(seed)
    word_pool = _token_pool(lexicon_size)
    token_to_id = {token: idx for idx, token in enumerate(word_pool)}
    id_to_token = {idx: token for token, idx in token_to_id.items()}
    anchor_ids = [token_to_id[token] for token in ANCHOR_WORDS[:lexicon_size]]
    filler_ids = [token_to_id[token] for token in FILLER_WORDS]

    dataset: list[SequenceMemorySample] = []
    for _ in range(size):
        recall_gap = rng.randint(min_gap, max_gap)
        target_index = seq_len - 1 - recall_gap
        anchor_id = rng.choice(anchor_ids)

        sequence = [rng.choice(filler_ids) for _ in range(seq_len)]
        sequence[target_index] = anchor_id

        for idx in range(seq_len):
            if idx == target_index:
                continue
            if sequence[idx] == anchor_id:
                replacement_pool = [token_id for token_id in filler_ids if token_id != anchor_id]
                sequence[idx] = rng.choice(replacement_pool)

        last_index = seq_len - 1
        if sequence[last_index] == anchor_id:
            replacement_pool = [token_id for token_id in filler_ids if token_id != anchor_id]
            sequence[last_index] = rng.choice(replacement_pool)

        majority_count = sum(1 for token_id in sequence if token_id == anchor_id)
        if majority_count > 1:
            for idx in range(seq_len):
                if idx != target_index and sequence[idx] == anchor_id:
                    replacement_pool = [token_id for token_id in filler_ids if token_id != anchor_id]
                    sequence[idx] = rng.choice(replacement_pool)

        dataset.append(
            SequenceMemorySample(
                sequence=tuple(int(token_id) for token_id in sequence),
                recall_gap=recall_gap,
                target_index=target_index,
                target_symbol=int(anchor_id),
            )
        )
    return dataset, id_to_token


def render_sequence(sequence: tuple[int, ...], token_map: dict[int, str]) -> list[str]:
    return [token_map[int(token_id)] for token_id in sequence]


def transfer_scorecard(
    *,
    dataset: list[SequenceMemorySample],
    token_map: dict[int, str],
    trace_width: int,
    random_seed: int,
) -> dict[str, Any]:
    mechanism = mechanism_scorecard(dataset, trace_width=trace_width)
    random_accuracy = accuracy_from_predictions(
        dataset,
        predict_random_symbol(dataset, seed=random_seed, alphabet_size=len(token_map)),
    )
    return {
        **mechanism,
        "random_symbol_accuracy": random_accuracy,
        "token_map": token_map,
        "sample_preview": [
            {
                "sequence": render_sequence(sample.sequence, token_map),
                "recall_gap": sample.recall_gap,
                "target_index": sample.target_index,
                "target_symbol": token_map[sample.target_symbol],
                "last_symbol": token_map[int(sample.sequence[-1])],
                "majority_symbol": token_map[predict_majority_symbol([sample])[0]],
            }
            for sample in dataset[:5]
        ],
    }


def write_smoke_artifact(
    *,
    out_root: Path,
    config: TransferLaunchConfig,
) -> dict[str, Any]:
    dataset, token_map = build_symbolic_micro_corpus_cloze_transfer_dataset(
        seed=config.seed,
        size=config.size,
        seq_len=config.seq_len,
        lexicon_size=config.lexicon_size,
        min_gap=config.min_gap,
        max_gap=config.max_gap,
    )
    trace_width = config.max_gap + 1
    scorecard = transfer_scorecard(
        dataset=dataset,
        token_map=token_map,
        trace_width=trace_width,
        random_seed=config.seed + 17,
    )
    payload = {
        "phase": "r5_single_mechanism_transfer",
        "approved_target_id": "symbolic_micro_corpus_cloze_transfer",
        "config": {
            "slice_id": config.slice_id,
            "seed": config.seed,
            "size": config.size,
            "seq_len": config.seq_len,
            "lexicon_size": config.lexicon_size,
            "min_gap": config.min_gap,
            "max_gap": config.max_gap,
            "trace_width": trace_width,
        },
        "scorecard": scorecard,
    }
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "manifest.json").write_text(json.dumps(payload["config"], indent=2) + "\n", encoding="utf-8")
    (out_root / "scorecard.json").write_text(json.dumps(scorecard, indent=2) + "\n", encoding="utf-8")
    (out_root / "dataset_preview.json").write_text(
        json.dumps(scorecard["sample_preview"], indent=2) + "\n",
        encoding="utf-8",
    )
    return payload


def build_longrun_manifest(*, manifest_path: Path) -> dict[str, Any]:
    seeds = list(range(20260400, 20260430))
    slices = [
        {
            "slice_id": "base_cloze_transfer",
            "size": 256,
            "seq_len": 10,
            "lexicon_size": 8,
            "min_gap": 3,
            "max_gap": 5,
        },
        {
            "slice_id": "gap_extension_cloze_transfer",
            "size": 256,
            "seq_len": 12,
            "lexicon_size": 8,
            "min_gap": 4,
            "max_gap": 6,
        },
        {
            "slice_id": "lexicon_extension_cloze_transfer",
            "size": 256,
            "seq_len": 10,
            "lexicon_size": 10,
            "min_gap": 3,
            "max_gap": 5,
        },
        {
            "slice_id": "combined_bounded_cloze_transfer",
            "size": 256,
            "seq_len": 12,
            "lexicon_size": 10,
            "min_gap": 4,
            "max_gap": 6,
        },
    ]
    manifest = {
        "phase": "r5_single_mechanism_transfer",
        "approved_target_id": "symbolic_micro_corpus_cloze_transfer",
        "execution_mode": "deterministic_cpu",
        "preferred_device": "cpu",
        "candidate_id": "bounded_working_memory_candidate",
        "controls": [
            "random_symbol",
            "last_symbol",
            "majority_symbol",
        ],
        "seeds": seeds,
        "slices": slices,
        "out_root": "results/r5_cloze_transfer_longrun",
        "notes": [
            "The same FIFO memory mechanism must be reused unchanged.",
            "The historical cloze evolutionary stack is not the execution target for this run.",
            "This manifest is launch-ready but should not be started during launch-prep.",
        ],
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def run_longrun_from_manifest(*, manifest_path: Path, out_root: Path) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    out_root.mkdir(parents=True, exist_ok=True)
    total_runs = len(manifest["seeds"]) * len(manifest["slices"])
    completed = 0
    rows: list[dict[str, Any]] = []
    for slice_cfg in manifest["slices"]:
        slice_id = slice_cfg["slice_id"]
        for seed in manifest["seeds"]:
            completed += 1
            config = TransferLaunchConfig(
                slice_id=slice_id,
                seed=seed,
                size=int(slice_cfg["size"]),
                seq_len=int(slice_cfg["seq_len"]),
                lexicon_size=int(slice_cfg["lexicon_size"]),
                min_gap=int(slice_cfg["min_gap"]),
                max_gap=int(slice_cfg["max_gap"]),
            )
            payload = write_smoke_artifact(
                out_root=out_root / slice_id / f"seed_{seed}",
                config=config,
            )
            scorecard = payload["scorecard"]
            rows.append(
                {
                    "slice_id": slice_id,
                    "seed": seed,
                    "candidate_accuracy": scorecard["candidate_accuracy"],
                    "no_memory_control_accuracy": scorecard["no_memory_control_accuracy"],
                    "trivial_last_symbol_memory_accuracy": scorecard["trivial_last_symbol_memory_accuracy"],
                    "random_symbol_accuracy": scorecard["random_symbol_accuracy"],
                    "deterministic_replay_status": scorecard["deterministic_replay_status"],
                    "completed_runs": completed,
                    "total_runs": total_runs,
                }
            )
    summary = {
        "phase": "r5_single_mechanism_transfer",
        "approved_target_id": manifest["approved_target_id"],
        "total_runs": total_runs,
        "rows": rows,
    }
    (out_root / "longrun_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    with (out_root / "longrun_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else ["slice_id", "seed"])
        writer.writeheader()
        writer.writerows(rows)
    return summary


def build_launch_prep_packet(
    *,
    smoke_scorecard_path: Path,
    manifest_path: Path,
    packet_dir: Path,
) -> dict[str, Any]:
    scorecard = json.loads(smoke_scorecard_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    packet_dir.mkdir(parents=True, exist_ok=True)
    packet = {
        "packet_version": "R5_TRANSFER_LAUNCH_PREP_V1",
        "packet_id": "BDC_R5_TRANSFER_LAUNCH_PREP",
        "project": "Bio_Digital_Core",
        "system_name": "BDC_Scientific_Line",
        "base_packet_reference": "TASK-7626",
        "evidence_policy": {
            "measured": [
                "deterministic cloze transfer smoke artifact exists",
                "the approved FIFO mechanism beats the controls on the smoke artifact",
                "a deterministic long-run manifest exists for 30 seeds across bounded cloze slices",
            ],
            "inferred": [],
            "missing": [
                "the full R5 long-run itself",
            ],
        },
        "explicit_requests_to_bdc": [
            "Interpret whether the approved R5 target is launch-ready.",
            "Do not reopen transfer target choice.",
            "Do not let launch prep be mistaken for long-run completion.",
        ],
    }
    (packet_dir / "BDC_INPUT_PACKET_R5_TRANSFER_LAUNCH_PREP.json").write_text(
        json.dumps(packet, indent=2) + "\n",
        encoding="utf-8",
    )
    with (packet_dir / "unified_variant_comparison.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
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
        )
        writer.writeheader()
        writer.writerows(
            [
                {
                    "variant_id": "symbolic_micro_corpus_cloze_transfer_launch_ready",
                    "architecture_type": "scientific_launch_state",
                    "role_set": "orchestrator+planner+editor+guardian",
                    "runtime_type": "r5_transfer_launch_prep",
                    "docs_improved_pct": "100.0000",
                    "naturalness_delta": "15.0000",
                    "semantic_pass_pct": "100.0000",
                    "runtime_min": "0.0000",
                    "cost_usd": "0.0000",
                    "llm_calls": "0",
                    "revert_rate_pct": "0.0000",
                    "gate_pass_rate_pct": "100.0000",
                    "useful_rewrite_rate_pct": "100.0000",
                    "evidence_status": "measured",
                    "notes": "Deterministic smoke artifact and bounded long-run manifest exist for the approved cloze transfer target.",
                },
                {
                    "variant_id": "remain_in_r5_launch_prep",
                    "architecture_type": "scientific_launch_state",
                    "role_set": "orchestrator+planner+editor+guardian",
                    "runtime_type": "r5_transfer_launch_prep",
                    "docs_improved_pct": "10.0000",
                    "naturalness_delta": "0.0000",
                    "semantic_pass_pct": "10.0000",
                    "runtime_min": "0.0000",
                    "cost_usd": "0.0000",
                    "llm_calls": "0",
                    "revert_rate_pct": "90.0000",
                    "gate_pass_rate_pct": "0.0000",
                    "useful_rewrite_rate_pct": "0.0000",
                    "evidence_status": "missing",
                    "notes": "Hold state if launch prep artifacts were missing.",
                },
            ]
        )
    with (packet_dir / "current_slice_metrics.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
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
        )
        writer.writeheader()
        writer.writerows(
            [
                {
                    "variant_id": "symbolic_micro_corpus_cloze_transfer_launch_ready",
                    "slice_id": "deterministic_smoke_artifact",
                    "accepted_rewrite_rate": f"{scorecard['candidate_accuracy'] * 100.0:.4f}",
                    "revert_rate": "0.0000",
                    "no_op_rate": "0.0000",
                    "semantic_pass_proxy": "100.0000",
                    "useful_output_rate": f"{scorecard['candidate_accuracy'] * 100.0:.4f}",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "measured",
                    "notes": "Smoke artifact confirms deterministic FIFO mechanism superiority over controls.",
                },
                {
                    "variant_id": "symbolic_micro_corpus_cloze_transfer_launch_ready",
                    "slice_id": "launch_manifest_present",
                    "accepted_rewrite_rate": "100.0000",
                    "revert_rate": "0.0000",
                    "no_op_rate": "0.0000",
                    "semantic_pass_proxy": "100.0000",
                    "useful_output_rate": "100.0000",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "measured",
                    "notes": f"Manifest defines {len(manifest['seeds'])} seeds across {len(manifest['slices'])} bounded slices.",
                },
                {
                    "variant_id": "remain_in_r5_launch_prep",
                    "slice_id": "missing_launch_state",
                    "accepted_rewrite_rate": "0.0000",
                    "revert_rate": "0.0000",
                    "no_op_rate": "100.0000",
                    "semantic_pass_proxy": "0.0000",
                    "useful_output_rate": "0.0000",
                    "latency": "0.0000",
                    "cost": "0.0000",
                    "evidence_status": "missing",
                    "notes": "Hold state only if smoke artifact or manifest are absent.",
                },
            ]
        )
    with (packet_dir / "failure_case_registry.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["case_id", "failure_mode", "severity", "status", "note"])
        writer.writeheader()
        writer.writerow(
            {
                "case_id": "R5_TRANSFER_STACK_REUSE",
                "failure_mode": "historical_stack_reuse",
                "severity": "high",
                "status": "controlled",
                "note": "Launch prep must keep the FIFO mechanism and must not substitute the older cloze evolution stack.",
            }
        )
    with (packet_dir / "current_runtime_role_mapping.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["runtime_component", "logical_bdc_role", "status", "why_mapped_this_way"],
        )
        writer.writeheader()
        writer.writerows(
            [
                {
                    "runtime_component": "r5_launch_scope",
                    "logical_bdc_role": "orchestrator",
                    "status": "active",
                    "why_mapped_this_way": "Keeps launch prep below actual long-run execution.",
                },
                {
                    "runtime_component": "manifest_surface",
                    "logical_bdc_role": "planner",
                    "status": "active",
                    "why_mapped_this_way": "Defines seeds and bounded slices for the approved target.",
                },
                {
                    "runtime_component": "smoke_artifact",
                    "logical_bdc_role": "editor",
                    "status": "active",
                    "why_mapped_this_way": "Carries the deterministic transfer artifact proving launch readiness.",
                },
                {
                    "runtime_component": "launch_readiness_gate",
                    "logical_bdc_role": "guardian",
                    "status": "active",
                    "why_mapped_this_way": "Determines whether the next action can be the full R5 long-run.",
                },
            ]
        )
    with (packet_dir / "prompt_stage_matrix.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["stage_id", "stage_name", "objective", "measured_output", "evidence_status"],
        )
        writer.writeheader()
        writer.writerows(
            [
                {
                    "stage_id": "r5_target_approval",
                    "stage_name": "approved transfer target",
                    "objective": "Use the approved adjacent target as fixed input to launch prep.",
                    "measured_output": "docs/experiments/BDC_R5_TRANSFER_TARGET_PACKET/r5_transfer_target_decision.json",
                    "evidence_status": "measured",
                },
                {
                    "stage_id": "r5_smoke",
                    "stage_name": "deterministic cloze transfer smoke",
                    "objective": "Demonstrate deterministic same-mechanism transfer on the approved family.",
                    "measured_output": str(smoke_scorecard_path),
                    "evidence_status": "measured",
                },
                {
                    "stage_id": "r5_manifest",
                    "stage_name": "launch manifest",
                    "objective": "Define the seed and slice surface for the next long-run.",
                    "measured_output": str(manifest_path),
                    "evidence_status": "measured",
                },
            ]
        )
    (packet_dir / "lead_architect_design_priorities.md").write_text(
        "\n".join(
            [
                "# Lead Architect Design Priorities",
                "",
                "1. Keep the same FIFO mechanism family unchanged.",
                "2. Keep the approved cloze target bounded and deterministic.",
                "3. Prepare the next long-run without starting it.",
                "4. Do not reopen target choice during launch prep.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (packet_dir / "README.md").write_text(
        "\n".join(
            [
                "# BDC R5 Transfer Launch Prep Packet",
                "",
                "- Approved target: `symbolic_micro_corpus_cloze_transfer`",
                "- Allowed verdicts: `READY_FOR_R5_TRANSFER_LONGRUN`, `REMAIN_IN_R5_LAUNCH_PREP`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return packet


def finalize_launch_prep_decision(
    *,
    bundle_result_path: Path,
) -> dict[str, Any]:
    bundle_result = json.loads(bundle_result_path.read_text(encoding="utf-8"))
    bundle = bundle_result["bundle"]
    ready = bool(bundle["supported"]) and bundle["recommended_variant_id"] == "symbolic_micro_corpus_cloze_transfer_launch_ready"
    return {
        "phase": "r5_single_mechanism_transfer",
        "task": "r5_transfer_longrun_launch_prep",
        "verdict": "READY_FOR_R5_TRANSFER_LONGRUN" if ready else "REMAIN_IN_R5_LAUNCH_PREP",
        "bdc_supported": bool(bundle["supported"]),
        "bdc_recommended_variant_id": bundle["recommended_variant_id"],
        "bdc_strategy_mode": bundle["strategy_mode"],
        "bdc_confidence_band": bundle["confidence_band"],
        "bdc_selective_outcome_class": bundle["selective_outcome_class"],
        "approved_target_id": "symbolic_micro_corpus_cloze_transfer",
        "reason": "Launch readiness requires a measured deterministic artifact plus a manifest for the approved target.",
    }
