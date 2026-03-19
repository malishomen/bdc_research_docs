from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory import (
    baseline_scorecard,
    build_controlled_sequence_memory_dataset,
    sample_to_dict,
)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Generate deterministic controlled-sequence-memory artifact.")
    ap.add_argument("--out_root", default="results/r2_controlled_sequence_memory_artifact")
    ap.add_argument("--seed", type=int, default=20260319)
    ap.add_argument("--size", type=int, default=64)
    ap.add_argument("--seq_len", type=int, default=8)
    ap.add_argument("--alphabet_size", type=int, default=4)
    ap.add_argument("--min_gap", type=int, default=2)
    ap.add_argument("--max_gap", type=int, default=4)
    return ap.parse_args()


def main() -> int:
    args = parse_args()
    out_root = Path(args.out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    dataset = build_controlled_sequence_memory_dataset(
        seed=args.seed,
        size=args.size,
        seq_len=args.seq_len,
        alphabet_size=args.alphabet_size,
        min_gap=args.min_gap,
        max_gap=args.max_gap,
    )
    scorecard = baseline_scorecard(dataset, seed=args.seed + 1, alphabet_size=args.alphabet_size)

    dataset_payload = [sample_to_dict(sample) for sample in dataset]
    manifest = {
        "task": "r2_controlled_sequence_memory_artifact",
        "seed": args.seed,
        "size": args.size,
        "seq_len": args.seq_len,
        "alphabet_size": args.alphabet_size,
        "min_gap": args.min_gap,
        "max_gap": args.max_gap,
        "dataset_path": str(out_root / "dataset.json"),
        "baseline_scorecard_path": str(out_root / "baseline_scorecard.json"),
    }

    (out_root / "dataset.json").write_text(json.dumps(dataset_payload, indent=2), encoding="utf-8")
    (out_root / "baseline_scorecard.json").write_text(json.dumps(scorecard, indent=2), encoding="utf-8")
    (out_root / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps({"manifest": manifest, "baseline_scorecard": scorecard}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
