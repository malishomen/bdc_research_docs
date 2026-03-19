from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evolution.micro_tasks.r5_cloze_transfer_launch_prep import (
    TransferLaunchConfig,
    build_launch_prep_packet,
    build_longrun_manifest,
    finalize_launch_prep_decision,
    run_longrun_from_manifest,
    write_smoke_artifact,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stage",
        choices=["smoke", "manifest", "packet", "finalize", "longrun"],
        required=True,
    )
    parser.add_argument(
        "--smoke_out",
        default="results/r5_cloze_transfer_launch_prep_smoke",
    )
    parser.add_argument(
        "--manifest_path",
        default="scripts/analysis/r5_cloze_transfer_longrun_manifest.json",
    )
    parser.add_argument(
        "--packet_dir",
        default="docs/experiments/BDC_R5_TRANSFER_LAUNCH_PREP_PACKET",
    )
    parser.add_argument(
        "--bundle_result",
        default="docs/experiments/BDC_R5_TRANSFER_LAUNCH_PREP_PACKET/BDC_CLIENT_BUNDLE_OUTPUT/bundle_result.json",
    )
    parser.add_argument(
        "--decision_out",
        default="docs/experiments/BDC_R5_TRANSFER_LAUNCH_PREP_PACKET/r5_transfer_launch_prep_decision.json",
    )
    parser.add_argument(
        "--longrun_out",
        default="results/r5_cloze_transfer_longrun",
    )
    args = parser.parse_args()

    if args.stage == "smoke":
        payload = write_smoke_artifact(
            out_root=Path(args.smoke_out),
            config=TransferLaunchConfig(
                slice_id="base_cloze_transfer_smoke",
                seed=20260319,
                size=128,
                seq_len=10,
                lexicon_size=8,
                min_gap=3,
                max_gap=5,
            ),
        )
        print(json.dumps(payload, indent=2))
        return

    if args.stage == "manifest":
        manifest = build_longrun_manifest(manifest_path=Path(args.manifest_path))
        print(json.dumps(manifest, indent=2))
        return

    if args.stage == "packet":
        packet = build_launch_prep_packet(
            smoke_scorecard_path=Path(args.smoke_out) / "scorecard.json",
            manifest_path=Path(args.manifest_path),
            packet_dir=Path(args.packet_dir),
        )
        print(json.dumps(packet, indent=2))
        return

    if args.stage == "finalize":
        decision = finalize_launch_prep_decision(
            bundle_result_path=Path(args.bundle_result),
        )
        out_path = Path(args.decision_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(decision, indent=2))
        return

    summary = run_longrun_from_manifest(
        manifest_path=Path(args.manifest_path),
        out_root=Path(args.longrun_out),
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
