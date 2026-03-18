from __future__ import annotations

import argparse
import csv
import json
import math
import time
from collections import defaultdict
from pathlib import Path
from statistics import mean


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Aggregate Phase R1 selection-physics sweep outputs.")
    ap.add_argument("--in_root", default="results/selection_physics_reboot_r1")
    ap.add_argument("--out_dir", default="")
    return ap.parse_args()


def _to_float(value: str) -> float:
    try:
        return float(value)
    except Exception:
        return float("nan")


def _finite_mean(values: list[float]) -> float:
    vals = [v for v in values if math.isfinite(v)]
    return mean(vals) if vals else float("nan")


def _read_last_metrics_row(metrics_path: Path) -> dict:
    with metrics_path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit(f"Empty metrics file: {metrics_path}")
    return rows[-1]


def _load_run_index(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit(f"Empty run index: {path}")
    return rows


def _decision_for_records(records: list[dict]) -> str:
    candidate_records = [
        row
        for row in records
        if row["selection_regime"] not in {"legacy_linear_control", "no_penalty_diagnostic"}
    ]
    for row in candidate_records:
        if (
            row["feasible_growth"]
            and row["runtime_pass_rate"] >= 0.8
            and row["collapse_rate"] <= 0.5
            and row["trivial_strategy_rate"] < 0.8
            and row["mean_penalty"] > 0.0
        ):
            return "PASS_TO_R2"
    return "REMAIN_IN_R1"


def main() -> int:
    args = parse_args()
    in_root = Path(args.in_root)
    run_index_path = in_root / "run_index.csv"
    resolved_manifest_path = in_root / "resolved_manifest.json"
    if not run_index_path.exists():
        raise SystemExit(f"Missing run index: {run_index_path}")
    if not resolved_manifest_path.exists():
        raise SystemExit(f"Missing resolved manifest: {resolved_manifest_path}")

    out_dir = Path(args.out_dir) if args.out_dir else in_root / "aggregates"
    out_dir.mkdir(parents=True, exist_ok=True)

    run_rows = _load_run_index(run_index_path)
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in run_rows:
        grouped[(row["genome_version"], row["selection_regime"])].append(row)

    regime_records: list[dict] = []
    for (genome_version, selection_regime), rows in sorted(grouped.items()):
        final_max_fitness = []
        final_max_accuracy = []
        final_mean_load = []
        final_mean_penalty = []
        final_diversity = []
        final_functional_diversity = []
        trivial_rates = []
        collapse_count = 0
        runtime_pass_count = 0

        for row in rows:
            run_dir = Path(row["run_dir"])
            summary_path = run_dir / "summary.json"
            metrics_path = run_dir / "metrics.csv"
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            last_metrics = _read_last_metrics_row(metrics_path)

            runtime_pass = row["returncode"] == "0" and row["summary_exists"] == "True" and row["metrics_exists"] == "True"
            if runtime_pass:
                runtime_pass_count += 1
            if summary.get("kill_status", {}).get("status") != "PASS":
                collapse_count += 1

            final_max_fitness.append(_to_float(last_metrics["max_fitness"]))
            final_max_accuracy.append(_to_float(last_metrics["max_accuracy"]))
            final_mean_load.append(_to_float(last_metrics["mean_complexity"]))
            final_mean_penalty.append(_to_float(last_metrics["mean_penalty"]))
            final_diversity.append(_to_float(last_metrics["diversity_index"]))
            final_functional_diversity.append(_to_float(last_metrics.get("functional_diversity", "nan")))
            trivial_rates.append(_to_float(last_metrics["trivial_strategy_rate"]))

        runtime_pass_rate = runtime_pass_count / len(rows)
        collapse_rate = collapse_count / len(rows)
        mean_penalty = _finite_mean(final_mean_penalty)
        mean_accuracy = _finite_mean(final_max_accuracy)
        record = {
            "genome_version": genome_version,
            "selection_regime": selection_regime,
            "runs_total": len(rows),
            "runtime_pass_rate": runtime_pass_rate,
            "collapse_rate": collapse_rate,
            "trivial_strategy_rate": _finite_mean(trivial_rates),
            "diversity_index_final": _finite_mean(final_diversity),
            "functional_diversity_final": _finite_mean(final_functional_diversity),
            "final_max_fitness_mean": _finite_mean(final_max_fitness),
            "final_max_accuracy_mean": mean_accuracy,
            "mean_load": _finite_mean(final_mean_load),
            "mean_penalty": mean_penalty,
        }
        regime_records.append(record)

    legacy_rows = [row for row in regime_records if row["selection_regime"] == "legacy_linear_control"]
    if not legacy_rows:
        raise SystemExit("Legacy control missing from aggregate set.")

    legacy_fitness_by_genome = {
        row["genome_version"]: row["final_max_fitness_mean"] for row in legacy_rows
    }
    for row in regime_records:
        legacy_baseline = legacy_fitness_by_genome.get(row["genome_version"], float("nan"))
        required_accuracy = legacy_baseline + row["mean_penalty"] if math.isfinite(legacy_baseline) and math.isfinite(row["mean_penalty"]) else float("nan")
        row["legacy_baseline_fitness"] = legacy_baseline
        row["required_accuracy_to_beat_legacy"] = required_accuracy
        row["feasible_growth"] = bool(math.isfinite(required_accuracy) and required_accuracy <= 1.0)

    regime_summary_csv = out_dir / "r1_regime_summary.csv"
    with regime_summary_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "genome_version",
                "selection_regime",
                "runs_total",
                "runtime_pass_rate",
                "collapse_rate",
                "trivial_strategy_rate",
                "diversity_index_final",
                "functional_diversity_final",
                "final_max_fitness_mean",
                "final_max_accuracy_mean",
                "mean_load",
                "mean_penalty",
                "legacy_baseline_fitness",
                "required_accuracy_to_beat_legacy",
                "feasible_growth",
            ],
        )
        writer.writeheader()
        for row in regime_records:
            writer.writerow(row)

    regime_summary_json = out_dir / "r1_regime_summary.json"
    regime_summary_json.write_text(json.dumps({"records": regime_records}, indent=2), encoding="utf-8")

    verdict = _decision_for_records(regime_records)
    gate_summary = {
        "task": "selection_physics_reboot_r1_gate_audit",
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "in_root": str(in_root),
        "out_dir": str(out_dir),
        "verdict": verdict,
        "required_legacy_control_present": True,
        "records_evaluated": len(regime_records),
    }
    (out_dir / "r1_gate_decision.json").write_text(json.dumps(gate_summary, indent=2), encoding="utf-8")
    print(json.dumps(gate_summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
