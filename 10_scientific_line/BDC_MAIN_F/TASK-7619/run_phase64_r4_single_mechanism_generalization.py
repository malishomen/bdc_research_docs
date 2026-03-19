from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.sequence_memory_generalization import (
    write_generalization_measurements,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--matrix_path",
        default="docs/experiments/R4_SINGLE_MECHANISM_GENERALIZATION_PRESSURE_MATRIX.json",
    )
    parser.add_argument(
        "--out_root",
        default="results/r4_single_mechanism_generalization",
    )
    args = parser.parse_args()

    summary = write_generalization_measurements(
        matrix_path=Path(args.matrix_path),
        out_root=Path(args.out_root),
    )
    out_root = Path(args.out_root)
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "run_manifest.json").write_text(
        json.dumps(
            {
                "phase": "R4",
                "task_id": "TASK-7619",
                "matrix_path": args.matrix_path,
                "out_root": args.out_root,
                "slice_count": summary["slice_count"],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
