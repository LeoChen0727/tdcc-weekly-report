from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd


LATEST_DIR = Path("output/latest")
PACKET_MD = LATEST_DIR / "tdcc_chatgpt_tracking_packet_latest.md"
STRENGTH_CSV = LATEST_DIR / "tdcc_strength_ranking_top_latest.csv"
ABM_CSV = LATEST_DIR / "tdcc_pre_move_abm_top_latest.csv"
PHASE_MD = LATEST_DIR / "tdcc_phase_distribution_latest.md"
PHASE_CSV = LATEST_DIR / "tdcc_phase_distribution_latest.csv"
TOP_RISK_MD = LATEST_DIR / "tdcc_top_risk_list_latest.md"
TOP_RISK_CSV = LATEST_DIR / "tdcc_top_risk_list_latest.csv"
WEEKLY_INCREASE_MD = LATEST_DIR / "tdcc_weekly_increase_ranking_latest.md"
WEEKLY_INCREASE_CSV = LATEST_DIR / "tdcc_weekly_increase_ranking_latest.csv"
CONSECUTIVE_MD = LATEST_DIR / "tdcc_consecutive_accumulation_ranking_latest.md"
CONSECUTIVE_CSV = LATEST_DIR / "tdcc_consecutive_accumulation_ranking_latest.csv"
MODEL_CROSS_MD = LATEST_DIR / "tdcc_weekly_model_cross_summary_latest.md"
MODEL_CROSS_CSV = LATEST_DIR / "tdcc_weekly_model_cross_summary_latest.csv"
WEEKLY_HIGHLIGHT_MD = LATEST_DIR / "tdcc_weekly_candidate_highlight_latest.md"
WEEKLY_FULL_MD = LATEST_DIR / "tdcc_weekly_candidate_full_latest.md"
README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
VALIDATION_MD = LATEST_DIR / "tdcc_chatgpt_tracking_validation_latest.md"
VALIDATION_JSON = LATEST_DIR / "tdcc_chatgpt_tracking_validation_latest.json"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str)
    except Exception:
        return pd.DataFrame()


def require_columns(df: pd.DataFrame, columns: list[str], label: str, errors: list[str]) -> None:
    missing = [col for col in columns if col not in df.columns]
    if missing:
        errors.append(f"{label} missing columns: {', '.join(missing)}")


def file_ok(path: Path, errors: list[str]) -> None:
    if not path.exists() or path.stat().st_size <= 0:
        errors.append(f"missing or empty file: {path.as_posix()}")


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    for path in [
        PACKET_MD,
        STRENGTH_CSV,
        ABM_CSV,
        PHASE_MD,
        PHASE_CSV,
        TOP_RISK_MD,
        TOP_RISK_CSV,
        WEEKLY_INCREASE_MD,
        WEEKLY_INCREASE_CSV,
        CONSECUTIVE_MD,
        CONSECUTIVE_CSV,
        MODEL_CROSS_MD,
        MODEL_CROSS_CSV,
        WEEKLY_HIGHLIGHT_MD,
        WEEKLY_FULL_MD,
    ]:
        file_ok(path, errors)

    packet_text = PACKET_MD.read_text(encoding="utf-8", errors="replace") if PACKET_MD.exists() else ""
    packet_lines = packet_text.splitlines()
    if len(packet_lines) <= 1:
        errors.append("tdcc_chatgpt_tracking_packet_latest.md appears to be single-line compressed output")
    if len(packet_lines) < 100:
        errors.append(f"packet line count too small: {len(packet_lines)}")
    if len(packet_lines) > 800:
        warnings.append(f"packet line count exceeds target 800 lines: {len(packet_lines)}")

    required_sections = [
        "# TDCC CHATGPT TRACKING PACKET",
        "## Metadata",
        "## Data Quality Notes",
        "## Mature Sample Status",
        "## TDCC Strength Ranking Top 30",
        "## Pre-Move Accumulation / ABM Top 30",
        "## Theme Mainstream Summary",
        "## Top Risk List",
        "## TDCC Weekly Increase and Consecutive Candidate Reports",
        "## Model Tuning Recommendation",
    ]
    for section in required_sections:
        if section not in packet_text:
            errors.append(f"packet missing section: {section}")
    if "tuning_status: not_ready" not in packet_text:
        errors.append("packet must keep tuning_status: not_ready")
    if "forbidden_changes: core_weight_change" not in packet_text:
        errors.append("packet must forbid core weight changes")

    strength = read_csv(STRENGTH_CSV)
    require_columns(
        strength,
        ["rank", "stock_id", "theme", "theme_mainstream_status", "tdcc_price_phase", "risk_bucket", "interpretation"],
        "strength ranking",
        errors,
    )
    abm = read_csv(ABM_CSV)
    require_columns(
        abm,
        ["abm_rank", "stock_id", "theme", "theme_mainstream_status", "tracking_priority", "trigger_to_watch", "tdcc_price_phase"],
        "ABM ranking",
        errors,
    )
    phase = read_csv(PHASE_CSV)
    require_columns(phase, ["section", "tdcc_price_phase"], "phase distribution", errors)
    top_risk = read_csv(TOP_RISK_CSV)
    require_columns(top_risk, ["risk_group", "stock_id", "theme", "theme_mainstream_status", "tdcc_price_phase", "risk_bucket"], "top risk list", errors)

    weekly_increase = read_csv(WEEKLY_INCREASE_CSV)
    require_columns(
        weekly_increase,
        [
            "rank",
            "stock_id",
            "stock_name",
            "tdcc_weekly_increase_score",
            "tdcc_1w_change_400",
            "tdcc_1w_change_600",
            "tdcc_1w_change_800",
            "tdcc_1w_change_1000",
            "tdcc_phase_group_zh",
            "ranking_note_zh",
        ],
        "weekly increase ranking",
        errors,
    )
    consecutive = read_csv(CONSECUTIVE_CSV)
    require_columns(
        consecutive,
        [
            "rank",
            "stock_id",
            "stock_name",
            "tdcc_consecutive_accumulation_score",
            "tdcc_consecutive_up_weeks",
            "tdcc_phase_group_zh",
            "ranking_note_zh",
        ],
        "consecutive accumulation ranking",
        errors,
    )
    model_cross = read_csv(MODEL_CROSS_CSV)
    require_columns(
        model_cross,
        ["tdcc_list_type", "tdcc_rank", "stock_id", "model_id", "model_name_zh", "model_score"],
        "TDCC weekly model cross summary",
        errors,
    )

    if not strength.empty and "theme" in strength.columns:
        other_pct = strength["theme"].astype(str).str.lower().isin(["", "other", "nan", "none"]).mean() * 100
        if other_pct > 50:
            warnings.append(f"theme mapping still has high other ratio in strength ranking: {other_pct:.2f}%")
    if not abm.empty and "tracking_priority" in abm.columns:
        valid = {"A_prime_watch", "B_confirm_needed", "C_weak_or_discounted", "D_insufficient_data"}
        bad = sorted(set(abm["tracking_priority"].dropna().astype(str)) - valid)
        if bad:
            errors.append(f"ABM ranking has invalid tracking_priority values: {', '.join(bad)}")

    readme = README_TXT.read_text(encoding="utf-8", errors="replace") if README_TXT.exists() else ""
    for key in [
        "tdcc_chatgpt_tracking_packet_raw_url",
        "tdcc_strength_ranking_top_md_raw_url",
        "tdcc_pre_move_abm_top_md_raw_url",
        "tdcc_phase_distribution_md_raw_url",
        "tdcc_top_risk_list_md_raw_url",
        "tdcc_top_risk_list_csv_raw_url",
        "tdcc_weekly_increase_ranking_csv_raw_url",
        "tdcc_weekly_increase_ranking_md_raw_url",
        "tdcc_consecutive_accumulation_ranking_csv_raw_url",
        "tdcc_consecutive_accumulation_ranking_md_raw_url",
        "tdcc_weekly_model_cross_summary_csv_raw_url",
        "tdcc_weekly_model_cross_summary_md_raw_url",
        "tdcc_weekly_candidate_highlight_md_raw_url",
        "tdcc_weekly_candidate_full_md_raw_url",
    ]:
        if key not in readme:
            errors.append(f"READ_ME missing key: {key}")

    status = "pass" if not errors else "fail"
    result: dict[str, Any] = {
        "status": status,
        "packet_line_count": len(packet_lines),
        "errors": errors,
        "warnings": warnings,
    }

    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# TDCC ChatGPT Tracking Validation",
        "",
        f"- status: {status}",
        f"- packet_line_count: {len(packet_lines)}",
        f"- error_count: {len(errors)}",
        f"- warning_count: {len(warnings)}",
        "",
        "## Errors",
        "",
    ]
    lines.extend([f"- {item}" for item in errors] or ["- none"])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {item}" for item in warnings] or ["- none"])
    VALIDATION_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
