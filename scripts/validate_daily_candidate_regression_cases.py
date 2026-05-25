from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import stock_daily_monitor as monitor


LATEST_DIR = Path("output/latest")
OUTPUT_CSV = LATEST_DIR / "daily_candidate_regression_2484_latest.csv"
OUTPUT_MD = LATEST_DIR / "daily_candidate_regression_2484_latest.md"
OUTPUT_JSON = LATEST_DIR / "daily_candidate_regression_2484_latest.json"

CASE_STOCK_ID = "2484"
CASE_STOCK_NAME = "希華"
CASE_DATES = [
    "20260511",
    "20260512",
    "20260513",
    "20260514",
    "20260515",
    "20260518",
    "20260519",
    "20260520",
    "20260521",
    "20260522",
    "20260525",
]


def safe_text(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    return str(value)


def pick(metrics: dict[str, Any] | None, key: str) -> str:
    if not metrics:
        return ""
    return safe_text(metrics.get(key, ""))


def build_rows() -> tuple[pd.DataFrame, dict[str, Any]]:
    price_data = monitor.load_official_price_history()
    case_history = price_data[price_data["ticker"].eq(CASE_STOCK_ID)].copy()
    case_history = case_history.sort_values("date").reset_index(drop=True)

    raw_universe = not case_history.empty
    rows: list[dict[str, Any]] = []

    for case_date in CASE_DATES:
        history = case_history[case_history["date"] <= case_date].copy()
        metrics = monitor.calculate_breakout_score(history) if not history.empty else None

        rows.append(
            {
                "stock_id": CASE_STOCK_ID,
                "stock_name": CASE_STOCK_NAME,
                "case_date": case_date,
                "raw_history_rows": len(history),
                "breakout_type": pick(metrics, "breakout_type"),
                "score": pick(metrics, "score"),
                "close": pick(metrics, "close"),
                "volume_ratio": pick(metrics, "volume_ratio"),
                "previous_20d_high": pick(metrics, "previous_20d_high"),
                "previous_60d_high": pick(metrics, "previous_60d_high"),
                "neckline_price": pick(metrics, "neckline_price"),
                "neckline_distance_pct": pick(metrics, "neckline_distance_pct"),
                "w_bottom_flag": pick(metrics, "w_bottom_flag"),
                "w_bottom_right_side_flag": pick(metrics, "w_bottom_right_side_flag"),
                "platform_base_flag": pick(metrics, "platform_base_flag"),
                "platform_right_side_flag": pick(metrics, "platform_right_side_flag"),
                "pullback_entry_zone_flag": pick(metrics, "pullback_entry_zone_flag"),
                "pullback_right_side_flag": pick(metrics, "pullback_right_side_flag"),
                "ma20_reclaim_setup_flag": pick(metrics, "ma20_reclaim_setup_flag"),
                "early_attack_volume_flag": pick(metrics, "early_attack_volume_flag"),
                "early_entry_watch_flag": pick(metrics, "early_entry_watch_flag"),
                "right_side_follow_through_flag": pick(metrics, "right_side_follow_through_flag"),
                "rebound_from_5d_low_pct": pick(metrics, "rebound_from_5d_low_pct"),
                "neckline_challenge_flag": pick(metrics, "neckline_challenge_flag"),
                "neckline_breakout_flag": pick(metrics, "neckline_breakout_flag"),
                "platform_breakout_flag": pick(metrics, "platform_breakout_flag"),
                "volume_confirmed_breakout": pick(metrics, "volume_confirmed_breakout"),
                "breakout_close_near_high_flag": pick(metrics, "breakout_close_near_high_flag"),
                "false_breakout_risk": pick(metrics, "false_breakout_risk"),
                "pattern_stage": pick(metrics, "pattern_stage"),
            }
        )

    out = pd.DataFrame(rows)

    latest = out[out["case_date"].eq("20260525")]
    entry_zone = out[
        out["case_date"].isin(["20260511", "20260512", "20260513", "20260514"])
        & out["pattern_stage"].eq("pullback_entry_zone")
    ]
    early_entry = out[
        out["case_date"].isin(["20260518", "20260519"])
        & out["early_entry_watch_flag"].eq("True")
    ]
    right_side_attack = out[
        out["case_date"].isin(["20260520", "20260521"])
        & out["breakout_type"].eq("range_rebound")
        & pd.to_numeric(out["score"], errors="coerce").ge(65)
    ]
    prewarning = out[
        out["case_date"].isin(["20260520", "20260521", "20260522"])
        & out["pattern_stage"].isin(["platform_right_side", "neckline_challenge", "platform_breakout", "neckline_breakout"])
    ]

    validation = {
        "stock_id": CASE_STOCK_ID,
        "stock_name": CASE_STOCK_NAME,
        "raw_universe": raw_universe,
        "raw_history_rows": len(case_history),
        "pullback_entry_zone_detected": not entry_zone.empty,
        "early_entry_watch_detected": not early_entry.empty,
        "right_side_attack_detected": not right_side_attack.empty,
        "prewarning_detected": not prewarning.empty,
        "first_entry_zone_date": safe_text(entry_zone["case_date"].iloc[0]) if not entry_zone.empty else "",
        "first_early_entry_date": safe_text(early_entry["case_date"].iloc[0]) if not early_entry.empty else "",
        "first_attack_date": safe_text(right_side_attack["case_date"].iloc[0]) if not right_side_attack.empty else "",
        "first_trigger_date": safe_text(early_entry["case_date"].iloc[0]) if not early_entry.empty else "",
        "latest_breakout_detected": (
            not latest.empty
            and safe_text(latest.iloc[0].get("breakout_type")) == "true_breakout"
            and safe_text(latest.iloc[0].get("pattern_stage")) == "breakout_confirmed"
        ),
    }

    errors: list[str] = []
    if not raw_universe:
        errors.append("2484 missing from official raw price universe")
    if not validation["pullback_entry_zone_detected"]:
        errors.append("2484 20260511-20260514 pullback entry zone not detected")
    if not validation["early_entry_watch_detected"]:
        errors.append("2484 20260518-20260519 early entry watch not detected")
    if not validation["right_side_attack_detected"]:
        errors.append("2484 20260520-20260521 high-emphasis right-side attack not detected")
    if not validation["prewarning_detected"]:
        errors.append("2484 pre-breakout pattern warning not detected on 20260520-20260522")
    if not validation["latest_breakout_detected"]:
        errors.append("2484 20260525 volume-confirmed breakout not detected")
    validation["errors"] = errors
    validation["status"] = "pass" if not errors else "fail"

    return out, validation


def render_markdown(df: pd.DataFrame, validation: dict[str, Any]) -> str:
    lines = [
        "# Daily Candidate Regression: 2484",
        "",
        f"- stock_id: `{CASE_STOCK_ID}`",
        f"- stock_name: `{CASE_STOCK_NAME}`",
        f"- status: `{validation['status']}`",
        f"- raw_universe: `{validation['raw_universe']}`",
        f"- raw_history_rows: `{validation['raw_history_rows']}`",
        f"- first_entry_zone_date: `{validation['first_entry_zone_date']}`",
        f"- first_early_entry_date: `{validation['first_early_entry_date']}`",
        f"- first_attack_date: `{validation['first_attack_date']}`",
        f"- latest_breakout_detected: `{validation['latest_breakout_detected']}`",
        "",
        "## Expected Regression Behavior",
        "",
        "- 20260511-20260514 should mark the pullback entry-zone context after the prior impulse.",
        "- 20260518-20260519 should trigger early-entry / right-side watch before the platform breakout.",
        "- 20260520-20260521 should trigger high-emphasis range-strength / right-side attack before the limit-up breakout.",
        "- 20260522 should trigger range-strength / neckline breakout context.",
        "- 20260525 should trigger strict breakout with volume confirmation.",
        "",
        "## Case Replay",
        "",
    ]

    display_cols = [
        "case_date",
        "breakout_type",
        "score",
        "close",
        "volume_ratio",
        "pattern_stage",
        "neckline_price",
        "neckline_distance_pct",
        "pullback_entry_zone_flag",
        "early_entry_watch_flag",
        "right_side_follow_through_flag",
        "platform_right_side_flag",
        "neckline_breakout_flag",
        "platform_breakout_flag",
        "volume_confirmed_breakout",
        "false_breakout_risk",
    ]
    lines.append(df[display_cols].to_markdown(index=False))
    lines.append("")

    if validation["errors"]:
        lines.append("## Errors")
        lines.append("")
        for err in validation["errors"]:
            lines.append(f"- {err}")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    df, validation = build_rows()

    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    OUTPUT_JSON.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(df, validation), encoding="utf-8")

    print(f"Saved: {OUTPUT_CSV}")
    print(f"Saved: {OUTPUT_MD}")
    print(f"Saved: {OUTPUT_JSON}")

    if validation["errors"]:
        for err in validation["errors"]:
            print(f"ERROR: {err}")
        return 1

    print("Daily candidate regression cases passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
