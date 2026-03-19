from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory_generalization_gate import (
    write_generalization_packet,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--summary",
        default="results/r4_single_mechanism_generalization/generalization_summary.json",
    )
    parser.add_argument(
        "--matrix",
        default="docs/experiments/R4_SINGLE_MECHANISM_GENERALIZATION_PRESSURE_MATRIX.json",
    )
    parser.add_argument(
        "--packet_dir",
        default="docs/experiments/BDC_R4_SINGLE_MECHANISM_GENERALIZATION_PACKET",
    )
    parser.add_argument(
        "--decision_out",
        default="results/r4_single_mechanism_generalization/generalization_gate_decision.json",
    )
    args = parser.parse_args()

    decision = write_generalization_packet(
        summary_path=Path(args.summary),
        matrix_path=Path(args.matrix),
        packet_dir=Path(args.packet_dir),
    )
    decision_path = Path(args.decision_out)
    decision_path.parent.mkdir(parents=True, exist_ok=True)
    decision_path.write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
