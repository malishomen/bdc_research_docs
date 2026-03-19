from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Merge completed parallel R1 worker outputs into a root-level aggregate-ready view.")
    ap.add_argument("--in_root", default="results/selection_physics_reboot_r1_full")
    return ap.parse_args()


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> int:
    args = parse_args()
    in_root = Path(args.in_root)
    if not in_root.exists():
        raise SystemExit(f"Missing in_root: {in_root}")

    worker_roots = sorted(path for path in in_root.iterdir() if path.is_dir() and path.name.startswith("worker_"))
    if not worker_roots:
        raise SystemExit(f"No worker roots found under: {in_root}")

    merged_rows: list[dict[str, str]] = []
    all_regimes: list[str] = []
    all_seeds: list[int] = []
    genome_versions: list[str] = []
    task_environment: dict | None = None
    task_name = "selection_physics_reboot_r1"
    description = ""
    worker_summaries: list[dict] = []

    for worker_root in worker_roots:
        run_index_path = worker_root / "run_index.csv"
        manifest_path = worker_root / "resolved_manifest.json"
        runner_summary_path = worker_root / "runner_summary.json"
        if not run_index_path.exists():
            raise SystemExit(f"Missing worker run_index.csv: {run_index_path}")
        if not manifest_path.exists():
            raise SystemExit(f"Missing worker resolved_manifest.json: {manifest_path}")
        if not runner_summary_path.exists():
            raise SystemExit(f"Missing worker runner_summary.json: {runner_summary_path}")

        manifest = _read_json(manifest_path)
        runner_summary = _read_json(runner_summary_path)
        rows = _read_csv(run_index_path)
        if not rows:
            raise SystemExit(f"Empty worker run index: {run_index_path}")

        task_name = manifest.get("task", task_name)
        description = manifest.get("description", description)
        task_environment = manifest.get("task_environment", task_environment)
        genome_versions.extend(str(v) for v in manifest.get("genome_versions", []))
        all_regimes.extend(str(v) for v in manifest.get("selection_regimes", []))
        all_seeds.extend(int(v) for v in manifest.get("seeds", []))
        worker_summaries.append(runner_summary)
        merged_rows.extend(rows)

    merged_run_index_path = in_root / "run_index.csv"
    merged_alias_path = in_root / "merged_run_index.csv"
    fieldnames = [
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
    ]
    for path in (merged_run_index_path, merged_alias_path):
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in merged_rows:
                writer.writerow(row)

    merged_manifest = {
        "task": task_name,
        "description": description,
        "task_environment": task_environment or {},
        "genome_versions": sorted(set(genome_versions)),
        "selection_regimes": sorted(set(all_regimes)),
        "seeds": sorted(set(all_seeds)),
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_mode": "merged_parallel_workers",
        "worker_count": len(worker_roots),
    }
    _write_json(in_root / "resolved_manifest.json", merged_manifest)
    _write_json(in_root / "merged_resolved_manifest.json", merged_manifest)

    total_runs = len(merged_rows)
    pass_runs = sum(1 for row in merged_rows if row["returncode"] == "0" and row["summary_exists"] == "True" and row["metrics_exists"] == "True")
    fail_runs = total_runs - pass_runs
    merged_summary = {
        "task": task_name,
        "out_root": str(in_root),
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "worker_count": len(worker_roots),
        "total_runs": total_runs,
        "pass_runs": pass_runs,
        "fail_runs": fail_runs,
        "selection_regimes": merged_manifest["selection_regimes"],
        "genome_versions": merged_manifest["genome_versions"],
        "seeds": merged_manifest["seeds"],
        "worker_summaries": worker_summaries,
    }
    _write_json(in_root / "runner_summary.json", merged_summary)
    _write_json(in_root / "merged_runner_summary.json", merged_summary)
    print(json.dumps(merged_summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
