from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import time
from itertools import product
from pathlib import Path


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Phase R1 selection-physics reboot sweep runner.")
    ap.add_argument("--manifest", default="scripts/edp1/selection_physics_manifest.json")
    ap.add_argument("--out_root", default="results/selection_physics_reboot_r1")
    ap.add_argument("--max_seeds", type=int, default=0)
    ap.add_argument("--dry_run", action="store_true")
    return ap.parse_args()


def load_manifest(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    required = ["task_environment", "genome_versions", "selection_regimes", "seeds", "runner_defaults"]
    missing = [key for key in required if key not in payload]
    if missing:
        raise SystemExit(f"Manifest missing required keys: {missing}")
    return payload


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest)
    manifest = load_manifest(manifest_path)
    out_root = Path(args.out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    seeds = list(manifest["seeds"])
    if args.max_seeds > 0:
        seeds = seeds[: args.max_seeds]

    resolved_manifest = dict(manifest)
    resolved_manifest["seeds"] = seeds
    resolved_manifest["dry_run"] = bool(args.dry_run)
    resolved_manifest["generated_at_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    write_json(out_root / "resolved_manifest.json", resolved_manifest)

    run_records: list[dict] = []
    env_cfg = manifest["task_environment"]
    defaults = manifest["runner_defaults"]

    for genome_version, selection_regime, seed in product(
        manifest["genome_versions"],
        manifest["selection_regimes"],
        seeds,
    ):
        run_dir = out_root / genome_version / selection_regime / "seeds" / f"seed_{seed}"
        run_dir.mkdir(parents=True, exist_ok=True)
        stdout_path = run_dir / "stdout.log"
        stderr_path = run_dir / "stderr.log"

        cmd = [
            sys.executable,
            "-m",
            env_cfg["module"],
            "--out_dir",
            str(run_dir),
            "--genome_version",
            str(genome_version),
            "--seed",
            str(seed),
            "--population",
            str(env_cfg["population"]),
            "--generations",
            str(env_cfg["generations"]),
            "--dataset_size",
            str(env_cfg["dataset_size"]),
            "--bit_len",
            str(env_cfg["bit_len"]),
            "--complexity_regime",
            str(selection_regime),
            "--complexity_lambda",
            str(defaults["complexity_lambda"]),
            "--lambda_v1",
            str(defaults["lambda_v1"]),
            "--lambda_v1_5",
            str(defaults["lambda_v1_5"]),
            "--lambda_v2",
            str(defaults["lambda_v2"]),
            "--phase0_min_generations",
            str(defaults["phase0_min_generations"]),
            "--phase0_diversity_threshold",
            str(defaults["phase0_diversity_threshold"]),
            "--selection_top_pct_phase1",
            str(defaults["selection_top_pct_phase1"]),
            "--plateau_window",
            str(defaults["plateau_window"]),
            "--plateau_improvement_pct",
            str(defaults["plateau_improvement_pct"]),
            "--diversity_collapse_threshold",
            str(defaults["diversity_collapse_threshold"]),
            "--diversity_collapse_patience",
            str(defaults["diversity_collapse_patience"]),
            "--trivial_strategy_threshold",
            str(defaults["trivial_strategy_threshold"]),
            "--trivial_strategy_patience",
            str(defaults["trivial_strategy_patience"]),
        ]
        if args.dry_run:
            cmd.append("--dry_run")

        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        stdout_path.write_text(proc.stdout, encoding="utf-8")
        stderr_path.write_text(proc.stderr, encoding="utf-8")

        summary_path = run_dir / "summary.json"
        metrics_path = run_dir / "metrics.csv"
        summary_payload = None
        if summary_path.exists():
            summary_payload = json.loads(summary_path.read_text(encoding="utf-8"))

        run_records.append(
            {
                "genome_version": genome_version,
                "selection_regime": selection_regime,
                "seed": seed,
                "returncode": proc.returncode,
                "summary_exists": summary_path.exists(),
                "metrics_exists": metrics_path.exists(),
                "kill_status": (summary_payload or {}).get("kill_status", {}).get("status", "MISSING"),
                "kill_reason": (summary_payload or {}).get("kill_status", {}).get("reason", "missing"),
                "run_dir": str(run_dir),
                "stdout_path": str(stdout_path),
                "stderr_path": str(stderr_path),
            }
        )

    run_index_path = out_root / "run_index.csv"
    with run_index_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "genome_version",
                "selection_regime",
                "seed",
                "returncode",
                "summary_exists",
                "metrics_exists",
                "kill_status",
                "kill_reason",
                "run_dir",
                "stdout_path",
                "stderr_path",
            ],
        )
        writer.writeheader()
        for row in run_records:
            writer.writerow(row)

    total_runs = len(run_records)
    pass_runs = sum(1 for row in run_records if row["returncode"] == 0 and row["summary_exists"] and row["metrics_exists"])
    fail_runs = total_runs - pass_runs
    summary = {
        "task": manifest.get("task", "selection_physics_reboot_r1"),
        "manifest_path": str(manifest_path),
        "out_root": str(out_root),
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_runs": total_runs,
        "pass_runs": pass_runs,
        "fail_runs": fail_runs,
        "selection_regimes": manifest["selection_regimes"],
        "genome_versions": manifest["genome_versions"],
        "seeds": seeds,
    }
    write_json(out_root / "runner_summary.json", summary)
    print(json.dumps(summary, indent=2))
    return 0 if fail_runs == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
