from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory import (
    build_controlled_sequence_memory_dataset,
    sample_to_dict,
)
from evolution.micro_tasks.sequence_memory_mechanism import mechanism_scorecard


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out_root",
        default="results/r3_sequence_memory_mechanism",
    )
    parser.add_argument("--seed", type=int, default=20260319)
    parser.add_argument("--size", type=int, default=128)
    parser.add_argument("--trace_width", type=int, default=5)
    args = parser.parse_args()

    out_root = Path(args.out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    dataset = build_controlled_sequence_memory_dataset(
        seed=args.seed,
        size=args.size,
        seq_len=8,
        alphabet_size=4,
        min_gap=2,
        max_gap=4,
    )
    scorecard = mechanism_scorecard(dataset, trace_width=args.trace_width)
    manifest = {
        "environment_id": "controlled_sequence_memory",
        "task_id": "TASK-7610",
        "seed": args.seed,
        "size": args.size,
        "trace_width": args.trace_width,
        "dataset_size": len(dataset),
    }

    (out_root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (out_root / "dataset.json").write_text(
        json.dumps([sample_to_dict(sample) for sample in dataset], indent=2) + "\n"
    )
    (out_root / "mechanism_scorecard.json").write_text(
        json.dumps(scorecard, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
