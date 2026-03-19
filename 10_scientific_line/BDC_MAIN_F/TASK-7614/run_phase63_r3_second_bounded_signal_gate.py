from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.control_resistant_sequence_memory_gate import (
    write_second_signal_packet,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scorecard",
        default="results/r3_control_resistant_sequence_memory/mechanism_scorecard.json",
    )
    parser.add_argument(
        "--dataset",
        default="results/r3_control_resistant_sequence_memory/dataset.json",
    )
    parser.add_argument(
        "--packet_dir",
        default="docs/experiments/BDC_R3_SECOND_BOUNDED_SIGNAL_PACKET",
    )
    parser.add_argument(
        "--decision_out",
        default="results/r3_control_resistant_sequence_memory/second_bounded_signal_decision.json",
    )
    args = parser.parse_args()

    decision = write_second_signal_packet(
        scorecard_path=Path(args.scorecard),
        dataset_path=Path(args.dataset),
        packet_dir=Path(args.packet_dir),
    )
    decision_path = Path(args.decision_out)
    decision_path.parent.mkdir(parents=True, exist_ok=True)
    decision_path.write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
