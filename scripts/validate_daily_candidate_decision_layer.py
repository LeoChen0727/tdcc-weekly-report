from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, main_price_date_from_freshness, normalize_date, read_csv, safe_str  # noqa: E402


DECISION_CSV = LATEST_DIR / "daily_candidate_decision_latest.csv"
DECISION_MD = LATEST_DIR / "daily_candidate_decision_latest.md"
DECISION_PACKET = LATEST_DIR / "daily_candidate_decision_chatgpt_packet_latest.md"
ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
REGRESSION_2484_JSON = LATEST_DIR / "daily_candidate_regression_2484_latest.json"
VALIDATION_JSON = LATEST_DIR / "daily_candidate_decision_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "daily_candidate_decision_validation_latest.md"

REQUIRED_COLUMNS = [
    "source_row_index",
    "signal_date",
    "stock_id",
    "stock_name",
    "original_category",
    "pattern_stage",
    "pattern_mapped_category",
    "decision_priority",
    "decision_score",
    "tdcc_status",
    "repeat_appear_label",
    "downgrade_flags",
    "next_confirmation",
    "action_rating",
    "action_rating_label_zh",
    "entry_style",
    "position_sizing",
    "entry_prerequisites",
    "post_entry_watch_items",
    "confidence_level",
    "thesis_state",
    "must_not_overstate",
]


def line_count(path: Path) -> int:
    if not path.exists():
        return 0
    return path.read_text(encoding="utf-8", errors="replace").count("\n") + 1


def validate() -> tuple[dict[str, object], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    main_date = main_price_date_from_freshness()

    df = read_csv(DECISION_CSV, dtype=str, keep_default_na=False)
    if df.empty:
        errors.append(f"missing_or_empty: {DECISION_CSV}")
    else:
        missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing:
            errors.append(f"missing_columns: {missing}")
        if "signal_date" in df.columns:
            dates = {normalize_date(x) for x in df["signal_date"].tolist() if normalize_date(x)}
            if main_date and main_date not in dates:
                warnings.append(f"main_price_date={main_date} not in decision signal_date values={sorted(dates)}")
        if "decision_priority" in df.columns:
            valid = {"A_priority_watch", "B_confirm_needed", "C_watch_only", "D_risk_downgrade"}
            invalid = sorted({safe_str(x) for x in df["decision_priority"].tolist() if safe_str(x) and safe_str(x) not in valid})
            if invalid:
                errors.append(f"invalid_decision_priority: {invalid}")
        if "action_rating" in df.columns:
            valid_actions = {
                "buy_now",
                "scale_in",
                "starter_position",
                "wait_pullback",
                "wait_reclaim",
                "hold_only",
                "take_profit",
                "reduce",
                "avoid",
            }
            invalid_actions = sorted(
                {safe_str(x) for x in df["action_rating"].tolist() if safe_str(x) and safe_str(x) not in valid_actions}
            )
            if invalid_actions:
                errors.append(f"invalid_action_rating: {invalid_actions}")
        if {"action_rating", "entry_prerequisites", "post_entry_watch_items"}.issubset(df.columns):
            recommended = df["action_rating"].isin(["buy_now", "scale_in", "starter_position"])
            if recommended.any():
                missing_entry = recommended & df["entry_prerequisites"].astype(str).eq("")
                missing_watch = recommended & df["post_entry_watch_items"].astype(str).eq("")
                if missing_entry.any():
                    errors.append(f"missing_entry_prerequisites_for_action_rows={int(missing_entry.sum())}")
                if missing_watch.any():
                    errors.append(f"missing_post_entry_watch_items_for_action_rows={int(missing_watch.sum())}")
                misplaced_post_entry = recommended & df["entry_prerequisites"].astype(str).str.contains(
                    "next_monthly_revenue|next_tdcc_update", na=False
                )
                if misplaced_post_entry.any():
                    errors.append("post-entry monitoring items must not appear in entry_prerequisites")
        if {
            "original_category",
            "repeat_appear_label",
            "warrant_flow_signal",
            "downgrade_flags",
            "decision_priority",
        }.issubset(df.columns):
            stale_revenue_flag = df["downgrade_flags"].astype(str).str.contains(
                "revenue_no_warrant_stale_no_breakout|stale_no_warrant_no_breakout",
                na=False,
            )
            if stale_revenue_flag.any():
                errors.append("repeat/stale appearance must be tracked separately, not as a direct decision downgrade flag")

        case_2484 = df[df.get("stock_id", pd.Series(dtype=str)).astype(str).eq("2484")]
        if not case_2484.empty:
            tdcc_series = case_2484["tdcc_status"].astype(str) if "tdcc_status" in case_2484.columns else pd.Series("", index=case_2484.index)
            repeat_series = case_2484["repeat_appear_label"].astype(str) if "repeat_appear_label" in case_2484.columns else pd.Series("", index=case_2484.index)
            downgrade_series = case_2484["downgrade_flags"].astype(str) if "downgrade_flags" in case_2484.columns else pd.Series("", index=case_2484.index)
            priority_series = case_2484["decision_priority"].astype(str) if "decision_priority" in case_2484.columns else pd.Series("", index=case_2484.index)
            risky = case_2484[
                tdcc_series.eq("distribution_warning")
                | repeat_series.isin(["continued_overheated"])
                | downgrade_series.str.contains("overheated|priced_in|distribution", case=False, na=False)
            ]
            if not risky.empty and priority_series.loc[risky.index].isin(["A_priority_watch"]).any():
                errors.append("2484 risky latest row must not be A_priority_watch")

    all_candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    if not all_candidates.empty and not df.empty:
        required_merge_cols = {"source_row_index", "stock_id", "decision_priority"}
        if required_merge_cols.issubset(df.columns) and required_merge_cols.issubset(all_candidates.columns):
            left = df[["source_row_index", "stock_id", "decision_priority"]].rename(
                columns={"stock_id": "decision_stock_id", "decision_priority": "decision_priority_decision"}
            )
            right = all_candidates[["source_row_index", "stock_id", "decision_priority"]].rename(
                columns={"stock_id": "candidate_stock_id", "decision_priority": "decision_priority_candidates"}
            )
            merged = left.merge(right, on="source_row_index", how="inner")
            mismatched = merged[
                (merged["decision_stock_id"].astype(str) != merged["candidate_stock_id"].astype(str))
                | (merged["decision_priority_decision"].astype(str) != merged["decision_priority_candidates"].astype(str))
            ]
            if not mismatched.empty:
                errors.append(f"all_candidates decision merge mismatch rows={len(mismatched)}")
        else:
            warnings.append("all_candidates merge alignment check skipped because source_row_index/decision columns are missing")

    for path in [DECISION_MD, DECISION_PACKET]:
        if not path.exists():
            errors.append(f"missing_file: {path}")
        elif line_count(path) <= 5:
            errors.append(f"suspicious_single_line_or_empty_markdown: {path}")

    regression_status = "missing"
    if REGRESSION_2484_JSON.exists():
        try:
            data = json.loads(REGRESSION_2484_JSON.read_text(encoding="utf-8"))
            regression_status = safe_str(data.get("status", ""))
            if regression_status != "pass":
                errors.append(f"2484_regression_status={regression_status}")
        except Exception as exc:
            errors.append(f"failed_to_read_2484_regression_json: {exc}")
    else:
        warnings.append("2484 regression json missing")

    result = {
        "status": "pass" if not errors else "fail",
        "main_price_date": main_date,
        "decision_rows": 0 if df.empty else int(len(df)),
        "decision_md_lines": line_count(DECISION_MD),
        "decision_packet_lines": line_count(DECISION_PACKET),
        "regression_2484_status": regression_status,
        "errors": errors,
        "warnings": warnings,
    }
    return result, errors


def write_report(result: dict[str, object]) -> None:
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Daily Candidate Decision Layer Validation",
        "",
        f"- status: `{result['status']}`",
        f"- main_price_date: `{result['main_price_date']}`",
        f"- decision_rows: `{result['decision_rows']}`",
        f"- decision_md_lines: `{result['decision_md_lines']}`",
        f"- decision_packet_lines: `{result['decision_packet_lines']}`",
        f"- regression_2484_status: `{result['regression_2484_status']}`",
        "",
        "## Errors",
        "",
    ]
    errors = result.get("errors") or []
    if errors:
        lines.extend(f"- {err}" for err in errors)
    else:
        lines.append("- none")
    lines.extend(["", "## Warnings", ""])
    warnings = result.get("warnings") or []
    if warnings:
        lines.extend(f"- {warn}" for warn in warnings)
    else:
        lines.append("- none")
    lines.append("")
    VALIDATION_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    result, errors = validate()
    write_report(result)
    print(f"Saved: {VALIDATION_JSON}")
    print(f"Saved: {VALIDATION_MD}")
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1
    print("Daily candidate decision layer validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
