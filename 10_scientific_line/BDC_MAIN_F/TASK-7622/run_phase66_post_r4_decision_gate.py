from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.post_r4_decision_gate import (
    build_post_r4_decision_packet,
    finalize_post_r4_decision,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["packet", "finalize"], required=True)
    parser.add_argument(
        "--r4_gate",
        default="results/r4_single_mechanism_generalization/generalization_gate_decision.json",
    )
    parser.add_argument(
        "--packet_dir",
        default="docs/experiments/BDC_POST_R4_DECISION_PACKET",
    )
    parser.add_argument(
        "--bundle_result",
        default="docs/experiments/BDC_POST_R4_DECISION_PACKET/BDC_CLIENT_BUNDLE_OUTPUT/bundle_result.json",
    )
    parser.add_argument(
        "--decision_out",
        default="docs/experiments/BDC_POST_R4_DECISION_PACKET/post_r4_gate_decision.json",
    )
    args = parser.parse_args()

    if args.stage == "packet":
        build_post_r4_decision_packet(
            r4_gate_decision_path=Path(args.r4_gate),
            packet_dir=Path(args.packet_dir),
        )
        return

    decision = finalize_post_r4_decision(
        r4_gate_decision_path=Path(args.r4_gate),
        bundle_result_path=Path(args.bundle_result),
    )
    decision_path = Path(args.decision_out)
    decision_path.parent.mkdir(parents=True, exist_ok=True)
    decision_path.write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
