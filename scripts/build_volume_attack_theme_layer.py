from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import pandas as pd

from tracking_utils import (
    DOCS_LATEST_DIR,
    LATEST_DIR,
    main_price_date_from_freshness,
    now_text,
    pages_url,
    raw_url,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


VOLUME_WATCH_CSV = LATEST_DIR / "volume_breakout_watch_latest.csv"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
THEME_LEADERSHIP_CSV = LATEST_DIR / "daily_theme_leadership_latest.csv"
TWO_LINE_VIEW_CSV = LATEST_DIR / "daily_candidate_two_line_view_latest.csv"

THEME_LAYER_CSV = LATEST_DIR / "volume_attack_theme_layer_latest.csv"
THEME_LAYER_MD = LATEST_DIR / "volume_attack_theme_layer_latest.md"
STOCK_LAYER_CSV = LATEST_DIR / "volume_attack_theme_stocks_latest.csv"
STOCK_LAYER_MD = LATEST_DIR / "volume_attack_theme_stocks_latest.md"

DOCS_THEME_LAYER_CSV = DOCS_LATEST_DIR / THEME_LAYER_CSV.name
DOCS_THEME_LAYER_MD = DOCS_LATEST_DIR / THEME_LAYER_MD.name
DOCS_STOCK_LAYER_CSV = DOCS_LATEST_DIR / STOCK_LAYER_CSV.name
DOCS_STOCK_LAYER_MD = DOCS_LATEST_DIR / STOCK_LAYER_MD.name

MAINSTREAM_STATUSES = {"mainstream_leader", "mainstream_follow_through", "emerging_theme"}
RISK_THEME_STATUSES = {"weak_theme", "mainstream_overheated"}
GENERIC_THEME_VALUES = {"", "other", "unknown", "nan", "none", "mainstream_growth", "unclassified", "twse", "tpex"}
THEME_NAME_COLUMNS = ["theme_name", "蝝啣??黎", "sub_theme", "sector", "industry", "concept", "theme_group"]

SELECTED_TYPES = {"strict_60d_volume_breakout", "platform_volume_breakout", "neckline_volume_breakout"}
WATCH_TYPES = {
    "right_side_volume_attack",
    "abnormal_volume_up",
    "volume_expansion_watch",
    "loose_platform_volume_watch",
    "loose_ma_reclaim_volume_watch",
    "loose_right_side_volume_watch",
}
FAILED_TYPES = {"failed_range_breakout_risk"}
BULLISH_WARRANT_SIGNALS = {"call_inflow", "call_strong_inflow", "call_put_bullish", "low_float_call_spike"}


def first_text(row: pd.Series, columns: list[str]) -> str:
    for col in columns:
        if col in row.index:
            text = safe_str(row.get(col, ""))
            if text:
                return text
    return ""


def num(value: Any, default: float = math.nan) -> float:
    return to_number(value, default=default)


def theme_name_of(row: pd.Series) -> str:
    for col in THEME_NAME_COLUMNS:
        value = safe_str(row.get(col, ""))
        if value and value.lower() not in GENERIC_THEME_VALUES:
            return value
    return "other"


def normalize_status(value: Any) -> str:
    text = safe_str(value)
    return text if text else "single_name_signal"


def is_distribution_warning(row: pd.Series) -> bool:
    text = " ".join(
        safe_str(row.get(col, "")).lower()
        for col in ["tdcc_status", "risk_flags", "risk_tags", "downgrade_flags", "why_downgraded"]
    )
    return "distribution" in text or "overheated" in text or "continued_overheated" in text


def is_bullish_warrant(row: pd.Series) -> bool:
    return safe_str(row.get("warrant_flow_signal", "")).lower() in BULLISH_WARRANT_SIGNALS


def is_selected_row(row: pd.Series) -> bool:
    event_type = safe_str(row.get("volume_breakout_type", ""))
    selection = safe_str(row.get("selection_status", "")).lower()
    priority = safe_str(row.get("volume_breakout_priority", ""))
    if event_type in SELECTED_TYPES:
        return True
    if selection.startswith("selected") and priority in {"A_valid_breakout_watch", "B_confirm_needed"}:
        return True
    return False


def is_watch_row(row: pd.Series) -> bool:
    event_type = safe_str(row.get("volume_breakout_type", ""))
    selection = safe_str(row.get("selection_status", "")).lower()
    if event_type in WATCH_TYPES:
        return True
    return "watch" in selection


def is_failed_row(row: pd.Series) -> bool:
    event_type = safe_str(row.get("volume_breakout_type", ""))
    if event_type in FAILED_TYPES:
        return True
    if safe_str(row.get("false_breakout_risk", "")).lower() in {"true", "1", "yes", "y"}:
        return True
    risk_text = " ".join(safe_str(row.get(col, "")).lower() for col in ["risk_flags", "risk_tags"])
    return "failed" in risk_text or "long_upper_shadow" in risk_text or "gap_up_failed" in risk_text


def volume_type_bucket(event_type: Any) -> str:
    text = safe_str(event_type)
    if text == "strict_60d_volume_breakout":
        return "strict_high_breakout"
    if text in {"platform_volume_breakout", "neckline_volume_breakout"}:
        return "range_breakout_volume"
    if text in {"right_side_volume_attack", "abnormal_volume_up", "volume_expansion_watch"}:
        return "right_side_or_volume_attack"
    if text.startswith("loose_"):
        return "early_watch"
    if text in FAILED_TYPES:
        return "failed_breakout_risk"
    return text or "unknown"


def build_lookup_by_theme(theme_df: pd.DataFrame) -> dict[str, dict[str, Any]]:
    if theme_df.empty or "theme_name" not in theme_df.columns:
        return {}
    lookup: dict[str, dict[str, Any]] = {}
    for _, row in theme_df.iterrows():
        theme = safe_str(row.get("theme_name", ""))
        if theme:
            lookup[theme] = row.to_dict()
    return lookup


def build_lookup_by_stock(df: pd.DataFrame) -> dict[str, dict[str, Any]]:
    if df.empty or "stock_id" not in df.columns:
        return {}
    lookup: dict[str, dict[str, Any]] = {}
    for _, row in df.iterrows():
        stock_id = safe_str(row.get("stock_id", ""))
        if not stock_id:
            continue
        row_dict = row.to_dict()
        row_theme = theme_name_of(row)
        if stock_id not in lookup:
            lookup[stock_id] = row_dict
            continue
        old_theme = theme_name_of(pd.Series(lookup[stock_id]))
        if old_theme == "other" and row_theme != "other":
            lookup[stock_id] = row_dict
    return lookup


def enrich_stocks(watch: pd.DataFrame, theme_df: pd.DataFrame, two_line: pd.DataFrame, candidates: pd.DataFrame) -> pd.DataFrame:
    if watch.empty:
        return pd.DataFrame()

    theme_lookup = build_lookup_by_theme(theme_df)
    two_line_lookup = build_lookup_by_stock(two_line)
    candidate_lookup = build_lookup_by_stock(candidates)
    rows: list[dict[str, Any]] = []

    for _, row in watch.iterrows():
        source = row.to_dict()
        stock_id = safe_str(source.get("stock_id", ""))
        theme_name = theme_name_of(row)
        theme_info = theme_lookup.get(theme_name, {})
        stock_info = two_line_lookup.get(stock_id, {})
        candidate_info = candidate_lookup.get(stock_id, {})

        if theme_name == "other":
            candidate_theme = theme_name_of(pd.Series(candidate_info)) if candidate_info else ""
            if candidate_theme and candidate_theme != "other":
                theme_name = candidate_theme
                theme_info = theme_lookup.get(theme_name, {})
        if not theme_info and stock_info:
            stock_theme = theme_name_of(pd.Series(stock_info))
            if stock_theme and stock_theme != "other":
                theme_name = stock_theme
                theme_info = theme_lookup.get(theme_name, {})
        if not theme_info and candidate_info:
            candidate_theme = theme_name_of(pd.Series(candidate_info))
            if candidate_theme and candidate_theme != "other":
                theme_name = candidate_theme
                theme_info = theme_lookup.get(theme_name, {})

        theme_final_status = normalize_status(
            theme_info.get("theme_final_status")
            or stock_info.get("theme_final_status")
            or candidate_info.get("theme_final_status")
            or source.get("theme_final_status")
        )
        theme_structural_status = normalize_status(
            theme_info.get("theme_structural_status")
            or stock_info.get("theme_structural_status")
            or candidate_info.get("theme_structural_status")
            or source.get("theme_structural_status")
        )
        theme_mainstream_label = normalize_status(
            theme_info.get("theme_mainstream_label")
            or stock_info.get("theme_mainstream_label")
            or candidate_info.get("theme_mainstream_label")
            or source.get("theme_mainstream_label")
        )
        candidate_source_type = safe_str(stock_info.get("candidate_source_type", source.get("candidate_source_type", "")))
        candidate_line_group = safe_str(stock_info.get("candidate_line_group", source.get("candidate_line_group", "")))
        candidate_line = safe_str(stock_info.get("candidate_line", source.get("candidate_line", "")))

        event_type = safe_str(source.get("volume_breakout_type", ""))
        bucket = volume_type_bucket(event_type)
        selected = is_selected_row(pd.Series(source))
        watch_row = is_watch_row(pd.Series(source))
        failed = is_failed_row(pd.Series(source))
        distribution = is_distribution_warning(pd.Series(source))

        rows.append(
            {
                **source,
                "theme_name": theme_name,
                "theme_final_status": theme_final_status,
                "theme_structural_status": theme_structural_status,
                "theme_mainstream_label": theme_mainstream_label,
                "theme_breadth_score": safe_str(theme_info.get("theme_breadth_score", "")),
                "theme_strength_score": safe_str(theme_info.get("theme_strength_score", "")),
                "theme_risk_score": safe_str(theme_info.get("theme_risk_score", "")),
                "theme_leader_stock_id": safe_str(theme_info.get("theme_leader_stock_id", "")),
                "theme_leader_stock_name": safe_str(theme_info.get("theme_leader_stock_name", "")),
                "candidate_source_type": candidate_source_type,
                "candidate_line_group": candidate_line_group,
                "candidate_line": candidate_line,
                "volume_attack_bucket": bucket,
                "is_volume_attack_selected": "True" if selected else "False",
                "is_volume_attack_watch": "True" if watch_row else "False",
                "is_volume_attack_failed": "True" if failed else "False",
                "has_tdcc_distribution_warning": "True" if distribution else "False",
                "has_bullish_warrant_signal": "True" if is_bullish_warrant(pd.Series(source)) else "False",
            }
        )

    out = pd.DataFrame(rows)
    return out.fillna("")


def status_for_theme(part: pd.DataFrame, theme_final_status: str, theme_name: str = "", theme_structural_status: str = "") -> str:
    total = len(part)
    selected_count = int((part["is_volume_attack_selected"] == "True").sum())
    watch_count = int((part["is_volume_attack_watch"] == "True").sum())
    failed_count = int((part["is_volume_attack_failed"] == "True").sum())
    distribution_count = int((part["has_tdcc_distribution_warning"] == "True").sum())
    bullish_warrant_count = int((part["has_bullish_warrant_signal"] == "True").sum())

    if total == 0:
        return "insufficient_data"
    if safe_str(theme_name).lower() in GENERIC_THEME_VALUES or safe_str(theme_name) == "other":
        return "theme_status_missing"
    if failed_count >= max(2, total // 2):
        return "failed_volume_theme"
    if theme_final_status == "mainstream_overheated" or distribution_count >= max(2, total // 2):
        return "overheated_volume_theme"
    is_core_mainstream = safe_str(theme_structural_status) == "core_mainstream_theme"
    if theme_final_status in MAINSTREAM_STATUSES and is_core_mainstream and selected_count >= 2:
        return "confirmed_volume_theme"
    if theme_final_status in MAINSTREAM_STATUSES and is_core_mainstream and total >= 3 and (selected_count + watch_count) >= 3:
        return "early_mainstream_candidate"
    if theme_final_status in MAINSTREAM_STATUSES and is_core_mainstream and (selected_count + watch_count) >= 1:
        return "watch_volume_theme"
    if theme_final_status in MAINSTREAM_STATUSES and not is_core_mainstream:
        return "non_mainstream_volume_watch"
    if selected_count + watch_count == 1:
        return "single_stock_volume_attack"
    if theme_final_status in RISK_THEME_STATUSES:
        return "failed_volume_theme" if failed_count else "weak_or_non_mainstream_volume_watch"
    if bullish_warrant_count or selected_count:
        return "single_stock_volume_attack"
    return "non_mainstream_volume_watch"


def interpretation_for_status(status: str) -> str:
    mapping = {
        "confirmed_volume_theme": "multiple volume breakouts with theme support; can be reviewed as mainstream-funding line, still needs stock-level confirmation",
        "early_mainstream_candidate": "theme-level volume attack is spreading early; use as early mainstream candidate, not as confirmed breakout",
        "watch_volume_theme": "theme has volume attack evidence but breadth is still thin; wait for follow-through",
        "single_stock_volume_attack": "single-stock volume attack only; keep in individual line unless theme broadens",
        "overheated_volume_theme": "volume is active but overheat/distribution risk is high; downgrade chase entries",
        "failed_volume_theme": "multiple failed or risky volume attacks; move to risk list",
        "weak_or_non_mainstream_volume_watch": "non-mainstream or weak theme; observation only unless stock confirms strongly",
        "non_mainstream_volume_watch": "volume activity without mainstream support; keep separate from mainstream-funding line",
        "theme_status_missing": "theme mapping missing; do not classify as mainstream or non-mainstream until theme mapping is fixed",
        "insufficient_data": "insufficient data",
    }
    return mapping.get(status, "observe only")


def build_theme_layer(stocks: pd.DataFrame) -> pd.DataFrame:
    if stocks.empty:
        return pd.DataFrame()

    rows: list[dict[str, Any]] = []
    for theme_name, part in stocks.groupby("theme_name", dropna=False):
        part = part.copy()
        theme_final_status = safe_str(part["theme_final_status"].replace("", pd.NA).dropna().iloc[0]) if not part["theme_final_status"].replace("", pd.NA).dropna().empty else "single_name_signal"
        theme_structural_status = safe_str(part["theme_structural_status"].replace("", pd.NA).dropna().iloc[0]) if "theme_structural_status" in part.columns and not part["theme_structural_status"].replace("", pd.NA).dropna().empty else ""
        theme_mainstream_label = safe_str(part["theme_mainstream_label"].replace("", pd.NA).dropna().iloc[0]) if "theme_mainstream_label" in part.columns and not part["theme_mainstream_label"].replace("", pd.NA).dropna().empty else ""
        status = status_for_theme(part, theme_final_status, safe_str(theme_name), theme_structural_status)
        volume_ratio = pd.to_numeric(part.get("volume_ratio", ""), errors="coerce")
        score = pd.to_numeric(part.get("volume_breakout_score", ""), errors="coerce").fillna(0)
        leader = part.assign(_score=score).sort_values("_score", ascending=False).iloc[0]

        rows.append(
            {
                "theme_name": safe_str(theme_name) or "other",
                "theme_final_status": theme_final_status,
                "theme_structural_status": theme_structural_status,
                "theme_mainstream_label": theme_mainstream_label,
                "theme_volume_attack_status": status,
                "theme_stock_count": int(part["stock_id"].nunique()) if "stock_id" in part.columns else int(len(part)),
                "volume_attack_count": int(len(part)),
                "range_breakout_volume_count": int(part["volume_breakout_type"].isin(["platform_volume_breakout", "neckline_volume_breakout"]).sum()),
                "range_breakout_watch_count": int(part["volume_breakout_type"].isin(["loose_platform_volume_watch"]).sum()),
                "ma_reclaim_volume_attack_count": int(part["volume_breakout_type"].isin(["loose_ma_reclaim_volume_watch"]).sum()),
                "near_high_volume_watch_count": int(part["volume_breakout_type"].isin(["right_side_volume_attack", "loose_right_side_volume_watch"]).sum()),
                "strict_high_breakout_count": int((part["volume_breakout_type"] == "strict_60d_volume_breakout").sum()),
                "failed_range_breakout_risk_count": int((part["is_volume_attack_failed"] == "True").sum()),
                "avg_volume_ratio": round(float(volume_ratio.mean()), 4) if not volume_ratio.dropna().empty else "",
                "median_volume_ratio": round(float(volume_ratio.median()), 4) if not volume_ratio.dropna().empty else "",
                "volume_ratio_above_1_5_count": int((volume_ratio >= 1.5).sum()) if not volume_ratio.dropna().empty else 0,
                "volume_ratio_above_2_0_count": int((volume_ratio >= 2.0).sum()) if not volume_ratio.dropna().empty else 0,
                "tdcc_accumulation_count": int(part.get("tdcc_status", pd.Series(dtype=str)).astype(str).str.contains("accumulation", case=False, na=False).sum()) if "tdcc_status" in part.columns else 0,
                "tdcc_distribution_warning_count": int((part["has_tdcc_distribution_warning"] == "True").sum()),
                "warrant_bullish_count": int((part["has_bullish_warrant_signal"] == "True").sum()),
                "leader_stock_id": safe_str(leader.get("stock_id", "")),
                "leader_stock_name": safe_str(leader.get("stock_name", "")),
                "leader_volume_attack_type": safe_str(leader.get("volume_breakout_type", "")),
                "leader_confirmed": "True" if safe_str(leader.get("is_volume_attack_selected", "")) == "True" else "False",
                "theme_breadth_score": safe_str(leader.get("theme_breadth_score", "")),
                "theme_strength_score": safe_str(leader.get("theme_strength_score", "")),
                "theme_risk_score": safe_str(leader.get("theme_risk_score", "")),
                "interpretation": interpretation_for_status(status),
            }
        )

    out = pd.DataFrame(rows)
    order = {
        "confirmed_volume_theme": 1,
        "early_mainstream_candidate": 2,
        "watch_volume_theme": 3,
        "single_stock_volume_attack": 4,
        "non_mainstream_volume_watch": 5,
        "weak_or_non_mainstream_volume_watch": 6,
        "overheated_volume_theme": 10,
        "failed_volume_theme": 11,
        "insufficient_data": 99,
        "theme_status_missing": 98,
    }
    out["_order"] = out["theme_volume_attack_status"].map(order).fillna(50)
    out["_count"] = pd.to_numeric(out["volume_attack_count"], errors="coerce").fillna(0)
    out["_avg_volume"] = pd.to_numeric(out["avg_volume_ratio"], errors="coerce").fillna(0)
    out = out.sort_values(["_order", "_count", "_avg_volume"], ascending=[True, False, False])
    return out.drop(columns=["_order", "_count", "_avg_volume"]).reset_index(drop=True)


def apply_theme_status_to_stocks(stocks: pd.DataFrame, theme_layer: pd.DataFrame) -> pd.DataFrame:
    if stocks.empty or theme_layer.empty:
        return stocks
    status = theme_layer[["theme_name", "theme_volume_attack_status", "interpretation"]].copy()
    out = stocks.drop(columns=[col for col in ["theme_volume_attack_status", "volume_attack_theme_interpretation"] if col in stocks.columns])
    out = out.merge(status, on="theme_name", how="left")
    out = out.rename(columns={"interpretation": "volume_attack_theme_interpretation"})

    def source_type(row: pd.Series) -> str:
        existing = safe_str(row.get("candidate_source_type", ""))
        status_text = safe_str(row.get("theme_volume_attack_status", ""))
        if status_text in {"confirmed_volume_theme", "early_mainstream_candidate", "watch_volume_theme"}:
            if existing and "volume_attack_theme_candidate" in existing:
                return existing
            return "volume_attack_theme_candidate" if status_text != "early_mainstream_candidate" else "early_mainstream_candidate"
        if existing:
            return existing
        if status_text in {"overheated_volume_theme", "failed_volume_theme"}:
            return "risk_downgraded_candidate"
        return "individual_quality_candidate"

    out["candidate_source_type"] = out.apply(source_type, axis=1)
    return out.fillna("")


def md_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> str:
    if df.empty:
        return "_No rows._"
    cols = [col for col in columns if col in df.columns]
    if not cols:
        return "_No matching columns._"
    return df[cols].head(limit).to_markdown(index=False)


def write_markdown(theme_layer: pd.DataFrame, stock_layer: pd.DataFrame, main_date: str) -> None:
    theme_cols = [
        "theme_name",
        "theme_final_status",
        "theme_structural_status",
        "theme_mainstream_label",
        "theme_volume_attack_status",
        "volume_attack_count",
        "range_breakout_volume_count",
        "range_breakout_watch_count",
        "ma_reclaim_volume_attack_count",
        "near_high_volume_watch_count",
        "strict_high_breakout_count",
        "tdcc_accumulation_count",
        "tdcc_distribution_warning_count",
        "warrant_bullish_count",
        "leader_stock_id",
        "leader_stock_name",
        "leader_volume_attack_type",
        "interpretation",
    ]
    stock_cols = [
        "stock_id",
        "stock_name",
        "theme_name",
        "theme_final_status",
        "theme_structural_status",
        "theme_mainstream_label",
        "theme_volume_attack_status",
        "volume_breakout_type",
        "volume_breakout_priority",
        "selection_status",
        "candidate_source_type",
        "volume_ratio",
        "tdcc_status",
        "warrant_flow_signal",
        "next_volume_breakout_confirmation",
    ]

    lines = [
        "# Volume Attack Theme Layer",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_date: `{main_date}`",
        f"- source_watch: `{VOLUME_WATCH_CSV.as_posix()}`",
        f"- source_theme: `{THEME_LEADERSHIP_CSV.as_posix()}`",
        "- rule: Volume-attack sections must show `theme_final_status`, `theme_structural_status`, `theme_mainstream_label`, and `theme_volume_attack_status`; do not show only the theme name.",
        "",
        "## Status Rules",
        "",
        "- confirmed_volume_theme: multiple volume breakouts with mainstream/emerging theme support.",
        "- early_mainstream_candidate: at least three volume attack/watch rows in a mainstream/emerging theme, but not fully confirmed.",
        "- watch_volume_theme: theme has volume attack evidence but breadth is still thin.",
        "- single_stock_volume_attack: stock-level signal only; do not place in mainstream-funding front section.",
        "- non_mainstream_volume_watch / weak_or_non_mainstream_volume_watch: observation only unless the stock confirms strongly.",
        "- overheated_volume_theme / failed_volume_theme: downgrade chase entries and list as risk.",
        "- theme_status_missing: source rows have no reliable stock theme; do not infer mainstream/non-mainstream from memory.",
        "",
        "## Theme Volume Attack Matrix",
        "",
        md_table(theme_layer, theme_cols, 100),
        "",
        "## Stock-Level Volume Attack With Theme Status",
        "",
        md_table(stock_layer, stock_cols, 120),
        "",
        "## Read Order For ChatGPT",
        "",
        "1. Read `daily_candidate_two_line_view_latest.md/csv` for mainstream vs individual lines.",
        "2. Read this file for the volume-attack theme layer.",
        "3. Read `volume_breakout_watch_latest.md/csv` only for detailed price/volume fields.",
        "4. If a row lacks `theme_final_status` or `theme_volume_attack_status`, mark `theme_status_missing` instead of guessing.",
        "",
    ]
    text = "\n".join(lines) + "\n"
    THEME_LAYER_MD.write_text(text, encoding="utf-8")
    DOCS_THEME_LAYER_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_THEME_LAYER_MD.write_text(text, encoding="utf-8")

    stock_lines = [
        "# Volume Attack Theme Stocks",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_date: `{main_date}`",
        "- rule: Every volume attack stock row carries explicit mainstream/non-mainstream status.",
        "",
        md_table(stock_layer, stock_cols, 250),
        "",
    ]
    stock_text = "\n".join(stock_lines) + "\n"
    STOCK_LAYER_MD.write_text(stock_text, encoding="utf-8")
    DOCS_STOCK_LAYER_MD.write_text(stock_text, encoding="utf-8")


def write_outputs(theme_layer: pd.DataFrame, stock_layer: pd.DataFrame, main_date: str) -> None:
    write_csv(theme_layer, THEME_LAYER_CSV)
    write_csv(stock_layer, STOCK_LAYER_CSV)
    write_csv(theme_layer, DOCS_THEME_LAYER_CSV)
    write_csv(stock_layer, DOCS_STOCK_LAYER_CSV)
    write_markdown(theme_layer, stock_layer, main_date)


def main() -> int:
    main_date = main_price_date_from_freshness()
    watch = read_csv(VOLUME_WATCH_CSV, dtype=str, keep_default_na=False)
    candidates = read_csv(ALL_CANDIDATES_CSV, dtype=str, keep_default_na=False)
    theme_df = read_csv(THEME_LEADERSHIP_CSV, dtype=str, keep_default_na=False)
    two_line = read_csv(TWO_LINE_VIEW_CSV, dtype=str, keep_default_na=False)

    if watch.empty:
        stock_layer = pd.DataFrame()
        theme_layer = pd.DataFrame()
    else:
        stock_layer = enrich_stocks(watch, theme_df, two_line, candidates)
        theme_layer = build_theme_layer(stock_layer)
        stock_layer = apply_theme_status_to_stocks(stock_layer, theme_layer)

    write_outputs(theme_layer, stock_layer, main_date)
    print(f"Saved: {THEME_LAYER_CSV} rows={len(theme_layer)}")
    print(f"Saved: {THEME_LAYER_MD}")
    print(f"Saved: {STOCK_LAYER_CSV} rows={len(stock_layer)}")
    print(f"Saved: {STOCK_LAYER_MD}")
    print(f"Pages: {pages_url(DOCS_THEME_LAYER_MD)}")
    print(f"Raw: {raw_url(THEME_LAYER_MD)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
