from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DAILY_SIGNALS_DIR, LATEST_DIR, RESEARCH_LATEST_DIR, main_price_date_from_freshness, normalize_date  # noqa: E402


SIGNAL_LOG = DAILY_SIGNALS_DIR / "daily_candidate_signal_log.csv"
PERFORMANCE_CSV = DAILY_SIGNALS_DIR / "daily_candidate_signal_performance.csv"
SUMMARY_CSV = LATEST_DIR / "daily_signal_performance_summary_latest.csv"
SUMMARY_MD = LATEST_DIR / "daily_signal_performance_summary_latest.md"
WEEKLY_MD = LATEST_DIR / "daily_signal_performance_weekly_latest.md"
WEEKLY_PDF = LATEST_DIR / "daily_signal_performance_weekly_latest.pdf"
MONTHLY_MD = LATEST_DIR / "daily_signal_performance_monthly_latest.md"
MONTHLY_PDF = LATEST_DIR / "daily_signal_performance_monthly_latest.pdf"
VALIDATION_MD = RESEARCH_LATEST_DIR / "daily_signal_performance_validation_latest.md"

FORBIDDEN = ["我的持股", "個人部位", "成本", "損益", "融資風險", "持有張數"]


def fail(errors: list[str]) -> int:
    lines = ["# Daily Signal Performance Validation", "", "status: fail", ""]
    lines.extend(f"- {err}" for err in errors)
    VALIDATION_MD.write_text("\n".join(lines), encoding="utf-8")
    for err in errors:
        print(f"ERROR: {err}")
    return 1


def main() -> int:
    errors: list[str] = []
    main_date = main_price_date_from_freshness()
    required_files = [SIGNAL_LOG, PERFORMANCE_CSV, SUMMARY_CSV, SUMMARY_MD, WEEKLY_MD, WEEKLY_PDF, MONTHLY_MD, MONTHLY_PDF]
    for path in required_files:
        if not path.exists():
            errors.append(f"missing file: {path}")
        elif path.suffix.lower() == ".pdf" and path.stat().st_size < 1000:
            errors.append(f"pdf too small: {path}")
    if errors:
        return fail(errors)

    log = pd.read_csv(SIGNAL_LOG, dtype=str, keep_default_na=False)
    perf = pd.read_csv(PERFORMANCE_CSV, dtype=str, keep_default_na=False)
    summary = pd.read_csv(SUMMARY_CSV, dtype=str, keep_default_na=False)

    log_cols = {
        "signal_id",
        "signal_date",
        "stock_id",
        "category",
        "score",
        "rank",
        "is_construction_recognition",
        "recognition_type",
        "market_regime",
        "benchmark_index",
        "theme_strength_score",
        "catalyst_strength_score",
        "catalyst_tags",
        "fundamental_catalyst_score",
        "fundamental_catalyst_tags",
        "event_catalyst_tags",
        "price_reaction_level",
        "similar_to_shihsinko_flag",
        "low_reaction_after_catalyst",
        "already_reacted_to_catalyst",
    }
    perf_cols = {
        "signal_id",
        "return_d1",
        "return_d5",
        "mfe_d10",
        "mae_d10",
        "relative_return_vs_benchmark_d10",
        "available_days_after_signal",
        "theme_strength_score",
        "catalyst_strength_score",
        "catalyst_tags",
        "fundamental_catalyst_score",
        "price_reaction_level",
        "similar_to_shihsinko_flag",
        "low_reaction_after_catalyst",
        "already_reacted_to_catalyst",
    }
    missing_log = log_cols - set(log.columns)
    missing_perf = perf_cols - set(perf.columns)
    if missing_log:
        errors.append(f"signal_log missing columns: {sorted(missing_log)}")
    if missing_perf:
        errors.append(f"performance missing columns: {sorted(missing_perf)}")
    if "signal_date" in log.columns:
        today_rows = log[log["signal_date"].map(normalize_date) == main_date]
        if today_rows.empty:
            errors.append(f"no signal log rows for main_price_date={main_date}")
    if "category" in log.columns and log["category"].astype(str).str.len().eq(0).any():
        errors.append("category contains blanks")
    if not summary.empty and "dimension" not in summary.columns:
        errors.append("summary missing dimension column")

    for path in [SUMMARY_MD, WEEKLY_MD, MONTHLY_MD]:
        text = path.read_text(encoding="utf-8", errors="replace")
        for word in FORBIDDEN:
            if word in text:
                errors.append(f"forbidden personal term in {path}: {word}")

    if errors:
        return fail(errors)

    lines = [
        "# Daily Signal Performance Validation",
        "",
        "status: pass",
        f"main_price_date: `{main_date}`",
        f"signal_log_rows: `{len(log)}`",
        f"performance_rows: `{len(perf)}`",
        f"summary_rows: `{len(summary)}`",
        "",
    ]
    VALIDATION_MD.write_text("\n".join(lines), encoding="utf-8")
    print("Daily signal performance validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
