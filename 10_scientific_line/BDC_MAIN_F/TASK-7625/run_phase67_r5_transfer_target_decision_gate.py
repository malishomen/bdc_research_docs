from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.r5_transfer_target_gate import (
    build_r5_transfer_target_packet,
    finalize_r5_transfer_target_decision,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["packet", "finalize"], required=True)
    parser.add_argument(
        "--matrix_path",
        default="docs/experiments/R5_TRANSFER_TARGET_MATRIX.json",
    )
    parser.add_argument(
        "--packet_dir",
        default="docs/experiments/BDC_R5_TRANSFER_TARGET_PACKET",
    )
    parser.add_argument(
        "--bundle_result",
        default="docs/experiments/BDC_R5_TRANSFER_TARGET_PACKET/BDC_CLIENT_BUNDLE_OUTPUT/bundle_result.json",
    )
    parser.add_argument(
        "--decision_out",
        default="docs/experiments/BDC_R5_TRANSFER_TARGET_PACKET/r5_transfer_target_decision.json",
    )
    args = parser.parse_args()

    if args.stage == "packet":
        build_r5_transfer_target_packet(
            matrix_path=Path(args.matrix_path),
            packet_dir=Path(args.packet_dir),
        )
        return

    decision = finalize_r5_transfer_target_decision(
        matrix_path=Path(args.matrix_path),
        bundle_result_path=Path(args.bundle_result),
    )
    out_path = Path(args.decision_out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
