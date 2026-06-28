from __future__ import annotations

import csv
import fnmatch
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

DAILY_CANDIDATE_DOCS_MIRROR_FILES = (
    "daily_candidate_model_parameters_latest.csv",
    "daily_candidate_model_parameters_latest.md",
    "daily_candidate_model_signals_latest.csv",
    "daily_candidate_model_signals_latest.md",
    "daily_candidate_model_signals_for_report_latest.csv",
    "daily_candidate_model_signals_for_report_latest.md",
    "daily_candidate_frontpage_unique_latest.csv",
    "daily_candidate_frontpage_unique_latest.md",
    "daily_candidate_same_model_repeat_latest.csv",
    "daily_candidate_same_model_repeat_latest.md",
    "daily_candidate_model_layer_packet_latest.md",
    "daily_candidate_model_layer_validation_latest.json",
    "daily_candidate_model_layer_validation_latest.md",
    "daily_candidate_model_selection_audit_latest.json",
    "daily_candidate_model_selection_audit_latest.md",
    "daily_candidate_pipeline_integrity_audit_latest.json",
    "daily_candidate_pipeline_integrity_audit_latest.md",
    "daily_candidate_group_rotation_latest.csv",
    "daily_candidate_group_rotation_latest.md",
    "daily_report_model_registry_latest.csv",
    "daily_report_model_registry_latest.md",
    "daily_candidate_model_summary_for_report_latest.csv",
    "daily_candidate_model_summary_for_report_latest.md",
)

INDICATOR_GUIDE_MIRROR_FILES = (
    "chatgpt_indicator_usage_guide_latest.md",
    "CHATGPT_INDICATOR_USAGE_GUIDE.txt",
)

REPORT_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
INDICATOR_GUIDE_MD = LATEST_DIR / "chatgpt_indicator_usage_guide_latest.md"


FORBIDDEN_STAGED_PATTERNS = {
    "output/latest/tdcc_*": "TDCC latest outputs are owned by tdcc_weekly/research workflows",
    "docs/latest/tdcc_*": "TDCC Pages outputs are owned by tdcc_weekly/research workflows",
    "output/history/tdcc_signals/*": "TDCC signal history is not a daily production output",
    "output/history/research/*": "research history is owned by research_backtest_pipeline",
    "output/history/surge_model/*": "surge model history is owned by research_backtest_pipeline",
    "output/history/msci_index_reviews/*": "MSCI review history is owned by research_backtest_pipeline",
    "output/history/volume_breakout/*": "volume-breakout backtest history is owned by research_backtest_pipeline",
    "output/latest/weekly_surge_*": "weekly surge research outputs are not daily production outputs",
    "docs/latest/weekly_surge_*": "weekly surge Pages outputs are not daily production outputs",
    "output/latest/explosive_volume_up_*": "explosive-volume research outputs are not daily production outputs",
    "docs/latest/explosive_volume_up_*": "explosive-volume Pages outputs are not daily production outputs",
    "output/latest/surge_model_*": "surge precondition research outputs are not daily production outputs",
    "docs/latest/surge_model_*": "surge precondition Pages outputs are not daily production outputs",
    "output/latest/msci_taiwan_rebalance_*": "MSCI rebalance research outputs are not daily production outputs",
    "docs/latest/msci_taiwan_rebalance_*": "MSCI rebalance Pages outputs are not daily production outputs",
    "output/latest/daily_signal_performance_*": "signal performance reports are not daily production outputs",
    "docs/latest/daily_signal_performance_*": "signal performance Pages outputs are not daily production outputs",
    "output/latest/daily_model_parameter_research_*": "model parameter research is not a daily production output",
    "docs/latest/daily_model_parameter_research_*": "model parameter research Pages output is not daily production output",
    "output/latest/daily_model_parameter_recommendations_*": "model parameter recommendations are not committed by daily production",
    "docs/latest/daily_model_parameter_recommendations_*": "model parameter recommendation Pages output is not daily production output",
}


def staged_files() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def validate_docs_latest_mirrors() -> list[str]:
    errors: list[str] = []
    for name in DAILY_CANDIDATE_DOCS_MIRROR_FILES + INDICATOR_GUIDE_MIRROR_FILES:
        output_path = LATEST_DIR / name
        docs_path = DOCS_LATEST_DIR / name
        if not output_path.exists():
            continue
        if not docs_path.exists():
            errors.append(f"missing docs/latest mirror: docs/latest/{name}")
            continue
        if output_path.read_bytes() != docs_path.read_bytes():
            errors.append(f"docs/latest mirror differs from output/latest: docs/latest/{name}")
    return errors


def validate_indicator_guide_counts() -> list[str]:
    errors: list[str] = []
    if not REPORT_SIGNALS_CSV.exists() or not INDICATOR_GUIDE_MD.exists():
        return errors

    with REPORT_SIGNALS_CSV.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    counts = Counter(str(row.get("model_id") or "").strip() for row in rows)
    counts.pop("", None)

    guide_text = INDICATOR_GUIDE_MD.read_text(encoding="utf-8", errors="replace")
    expected_row_count = (
        f"| daily_candidate_model_signals_for_report_latest.csv | ready | {len(rows)} |"
    )
    if expected_row_count not in guide_text:
        errors.append(
            "chatgpt_indicator_usage_guide_latest.md row count does not match "
            f"daily_candidate_model_signals_for_report_latest.csv: expected {len(rows)}"
        )

    missing_counts = [f"{model_id}={count}" for model_id, count in sorted(counts.items()) if f"{model_id}={count}" not in guide_text]
    if missing_counts:
        errors.append(
            "chatgpt_indicator_usage_guide_latest.md model counts do not match "
            f"daily_candidate_model_signals_for_report_latest.csv: missing {missing_counts}"
        )
    return errors


def main() -> int:
    errors: list[str] = []
    for path in staged_files():
        for pattern, reason in FORBIDDEN_STAGED_PATTERNS.items():
            if fnmatch.fnmatch(path, pattern):
                errors.append(f"{path}: {reason}")
    errors.extend(validate_docs_latest_mirrors())
    errors.extend(validate_indicator_guide_counts())

    if errors:
        print("ERROR: daily production staged path or latest mirror validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("daily staged path and latest mirror validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
