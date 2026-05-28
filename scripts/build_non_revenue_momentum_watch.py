from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
DECISION_CSV = LATEST_DIR / "daily_candidate_decision_latest.csv"
VOLUME_ATTACK_STOCKS_CSV = LATEST_DIR / "volume_attack_theme_stocks_latest.csv"

OUT_CSV = LATEST_DIR / "non_revenue_momentum_watch_latest.csv"
OUT_MD = LATEST_DIR / "non_revenue_momentum_watch_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name

STRONG_THEME_STATUSES = {
    "mainstream_leader",
    "mainstream_follow_through",
    "emerging_theme",
}

STRONG_VOLUME_THEME_STATUSES = {
    "confirmed_volume_theme",
    "early_mainstream_candidate",
    "watch_volume_theme",
}

STRONG_VOLUME_TYPES = {
    "range_breakout_volume",
    "strict_high_breakout",
    "platform_volume_breakout",
    "neckline_volume_breakout",
}

WATCH_VOLUME_TYPES = {
    "range_breakout_watch",
    "ma_reclaim_volume_attack",
    "near_high_volume_watch",
    "right_side_volume_attack",
    "loose_ma_reclaim_volume_watch",
    "loose_right_side_volume_watch",
    "abnormal_volume_up",
    "volume_expansion_watch",
}

BULLISH_WARRANT_SIGNALS = {
    "call_strong_inflow",
    "call_inflow",
    "call_put_bullish",
    "low_float_call_spike",
}

TDCC_SUPPORT_SIGNALS = {
    "strong_accumulation",
    "mild_accumulation",
    "tdcc_strong",
    "tdcc_mild",
    "accumulation",
}

RISK_TERMS = {
    "distribution_warning",
    "failed_range_breakout_risk",
    "failed_volume_theme",
    "overheated_volume_theme",
    "mainstream_overheated",
    "continued_overheated",
    "overheated_after_tdcc",
    "price_leading_tdcc",
    "tdcc_price_divergence",
    "weak_theme",
}


def now_text() -> str:
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat"}:
        return ""
    return text


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return float("nan")
    try:
        return float(text)
    except Exception:
        return float("nan")


def truthy(value: Any) -> bool:
    return safe_str(value).lower() in {"1", "true", "yes", "y", "t"}


def row_text(row: pd.Series, cols: Iterable[str]) -> str:
    return " | ".join(safe_str(row.get(col, "")) for col in cols).lower()


def first_value(row: pd.Series, cols: Iterable[str]) -> str:
    for col in cols:
        value = safe_str(row.get(col, ""))
        if value:
            return value
    return ""


def append_note(existing: str, note: str) -> str:
    existing = safe_str(existing)
    if not existing:
        return note
    if note in existing:
        return existing
    return f"{existing}; {note}"


def read_main_price_date() -> str:
    readme = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
    if not readme.exists():
        return ""
    for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("main_price_date="):
            return line.split("=", 1)[1].strip()
    return ""


def merge_sources() -> pd.DataFrame:
    decision = read_csv(DECISION_CSV)
    all_candidates = read_csv(ALL_CANDIDATES_CSV)
    if decision.empty:
        return pd.DataFrame()

    base = decision.copy()
    if not all_candidates.empty and "source_row_index" in base.columns:
        all_source = all_candidates.drop(columns=["source_row_index"], errors="ignore")
        all_with_index = all_source.reset_index().rename(columns={"index": "source_row_index"})
        all_with_index["source_row_index"] = all_with_index["source_row_index"].astype(str)
        base["source_row_index"] = base["source_row_index"].astype(str)
        keep_cols = [
            "source_row_index",
            "category",
            "category_cn",
            "industry",
            "細分族群",
            "theme_group",
            "latest_revenue_yoy",
            "cumulative_revenue_yoy",
            "revenue_yoy_pct",
            "cumulative_yoy_pct",
            "revenue_warning",
            "revenue_acceleration_note",
            "already_priced_in",
            "priced_in_reason",
            "score",
            "rank",
            "volume_confirmed_breakout",
            "platform_breakout_flag",
            "neckline_breakout_flag",
            "platform_high",
            "previous_high",
            "previous_60d_high",
            "ema23",
            "ma20",
            "ma60",
        ]
        keep_cols = [col for col in keep_cols if col in all_with_index.columns]
        base = base.merge(
            all_with_index[keep_cols],
            on="source_row_index",
            how="left",
            suffixes=("", "_candidate"),
        )

    volume = read_csv(VOLUME_ATTACK_STOCKS_CSV)
    if not volume.empty and "stock_id" in volume.columns:
        volume = volume.drop_duplicates(subset=["stock_id"], keep="first")
        volume_cols = [
            "stock_id",
            "theme_name",
            "theme_final_status",
            "theme_volume_attack_status",
            "candidate_source_type",
            "candidate_line",
            "candidate_line_group",
            "volume_breakout_type",
            "volume_breakout_priority",
            "selection_status",
            "volume_breakout_score",
            "volume_breakout_notes",
            "volume_attack_bucket",
            "is_volume_attack_selected",
            "is_volume_attack_watch",
            "is_volume_attack_failed",
            "has_tdcc_distribution_warning",
            "has_bullish_warrant_signal",
            "warrant_flow_signal",
            "warrant_flow_warning",
            "range_high",
            "range_breakout_pct",
        ]
        volume_cols = [col for col in volume_cols if col in volume.columns]
        base = base.merge(volume[volume_cols], on="stock_id", how="left", suffixes=("", "_volume"))

    return base


def revenue_status(row: pd.Series) -> tuple[str, str]:
    latest_yoy = safe_float(first_value(row, ["latest_revenue_yoy", "revenue_yoy_pct"]))
    cumulative_yoy = safe_float(first_value(row, ["cumulative_revenue_yoy", "cumulative_yoy_pct"]))
    text = row_text(
        row,
        [
            "revenue_warning",
            "revenue_acceleration_note",
            "downgrade_flags",
            "risk_tags",
            "why_downgraded",
            "why_selected",
            "next_confirmation",
        ],
    )
    unconfirmed = (
        "revenue_good_eps_unconfirmed" in text
        or "needs_eps_confirmation" in text
        or "eps" in text and "unconfirmed" in text
        or "毛利" in text and "未確認" in text
    )
    negative = False
    if latest_yoy == latest_yoy and latest_yoy < 0:
        negative = True
    if cumulative_yoy == cumulative_yoy and cumulative_yoy < 0:
        negative = True

    if negative and unconfirmed:
        return "negative_and_unconfirmed", "營收年增為負且 EPS/毛利或正式催化仍待確認"
    if negative:
        return "revenue_negative", "營收年增或累計年增為負"
    if unconfirmed:
        return "revenue_unconfirmed", "營收或題材尚未由 EPS/毛利/正式催化確認"
    if not first_value(row, ["latest_revenue_yoy", "revenue_yoy_pct", "cumulative_revenue_yoy", "cumulative_yoy_pct"]):
        return "revenue_data_missing", "缺少可用營收確認欄位"
    return "revenue_confirmed_or_not_weak", "營收未呈現負值或未標示待確認"


def has_price_volume_attack(row: pd.Series) -> bool:
    volume_type = safe_str(row.get("volume_breakout_type", ""))
    selection_status = safe_str(row.get("selection_status", ""))
    priority = safe_str(row.get("volume_breakout_priority", ""))
    volume_ratio = safe_float(row.get("volume_ratio", ""))
    return_5d = safe_float(row.get("return_5d", ""))

    if volume_type in STRONG_VOLUME_TYPES:
        return True
    if selection_status == "selected":
        return True
    if priority.startswith(("A_", "B_")):
        return True
    if truthy(row.get("volume_confirmed_breakout", "")):
        return True
    if truthy(row.get("platform_breakout_flag", "")) or truthy(row.get("neckline_breakout_flag", "")):
        return True
    if volume_ratio == volume_ratio and volume_ratio >= 1.5:
        return True
    if return_5d == return_5d and return_5d >= 8 and volume_ratio == volume_ratio and volume_ratio >= 1.2:
        return True
    return False


def has_watch_attack(row: pd.Series) -> bool:
    volume_type = safe_str(row.get("volume_breakout_type", ""))
    if volume_type in WATCH_VOLUME_TYPES:
        return True
    if truthy(row.get("is_volume_attack_watch", "")):
        return True
    if safe_str(row.get("selection_status", "")) == "watch":
        return True
    return False


def has_fund_or_theme_support(row: pd.Series) -> bool:
    theme_status = safe_str(row.get("theme_final_status", ""))
    volume_theme_status = safe_str(row.get("theme_volume_attack_status", ""))
    warrant = first_value(row, ["warrant_flow_signal", "warrant_flow_signal_volume"])
    tdcc = first_value(row, ["tdcc_status", "tdcc_judgement"])
    source_type = safe_str(row.get("candidate_source_type", ""))

    if theme_status in STRONG_THEME_STATUSES:
        return True
    if volume_theme_status in STRONG_VOLUME_THEME_STATUSES:
        return True
    if warrant in BULLISH_WARRANT_SIGNALS:
        return True
    if tdcc in TDCC_SUPPORT_SIGNALS or "accumulation" in tdcc:
        return True
    if "volume_attack_theme_candidate" in source_type or "early_mainstream_candidate" in source_type:
        return True
    return False


def has_risk(row: pd.Series) -> bool:
    text = row_text(
        row,
        [
            "theme_final_status",
            "theme_volume_attack_status",
            "volume_breakout_type",
            "downgrade_flags",
            "risk_tags",
            "why_downgraded",
            "must_not_overstate",
            "tdcc_status",
            "warrant_flow_warning",
        ],
    )
    if truthy(row.get("has_tdcc_distribution_warning", "")):
        return True
    if truthy(row.get("must_not_overstate", "")):
        return True
    return any(term in text for term in RISK_TERMS)


def classify_row(row: pd.Series, rev_status: str) -> tuple[bool, str, str, str]:
    price_attack = has_price_volume_attack(row)
    watch_attack = has_watch_attack(row)
    support = has_fund_or_theme_support(row)
    risk = has_risk(row)

    if rev_status == "revenue_confirmed_or_not_weak":
        return False, "", "", ""

    if rev_status == "revenue_data_missing" and not (price_attack and support):
        return False, "", "", ""

    if not (price_attack or watch_attack or support):
        return False, "", "", ""

    if risk:
        return (
            True,
            "D_overheated_or_failed_risk",
            "risk_watch_only",
            "題材或量價強，但風險/過熱/失敗突破警示存在，只能列風險觀察",
        )
    if price_attack and support:
        return (
            True,
            "A_fund_flow_confirmed_revenue_unconfirmed",
            "specialty_watch",
            "量價或族群資金已確認，但營收/EPS/毛利仍需補確認",
        )
    if support and watch_attack:
        return (
            True,
            "B_turnaround_theme_watch",
            "specialty_watch",
            "族群或資金有初步支持，量價仍屬接近發動觀察",
        )
    return (
        True,
        "C_hot_money_watch",
        "watch_only",
        "價格或題材有資金推動，但基本面確認不足，避免當主攻理由",
    )


def build_rows(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, row in df.iterrows():
        rev_status, rev_note = revenue_status(row)
        include, momentum_type, action_status, interpretation = classify_row(row, rev_status)
        if not include:
            continue

        next_confirmation = safe_str(row.get("next_confirmation", ""))
        next_confirmation = append_note(
            next_confirmation,
            "等待 EPS/毛利/正式催化或下一期營收確認；若量價失敗則降級。",
        )
        if momentum_type.startswith("A_"):
            next_confirmation = append_note(
                next_confirmation,
                "若放量突破後隔日仍守住突破區，才可維持短線高優先觀察。",
            )
        elif momentum_type.startswith("D_"):
            next_confirmation = append_note(
                next_confirmation,
                "若出現長上影、跌回突破區或 TDCC 轉弱，排除主攻。",
            )

        rows.append(
            {
                "signal_date": first_value(row, ["signal_date", "date"]),
                "stock_id": safe_str(row.get("stock_id", "")),
                "stock_name": safe_str(row.get("stock_name", "")),
                "category": first_value(row, ["original_category", "category"]),
                "category_cn": first_value(row, ["original_category_cn", "category_cn"]),
                "theme_name": first_value(row, ["theme_name", "theme_group", "細分族群", "industry"]),
                "decision_priority": safe_str(row.get("decision_priority", "")),
                "decision_score": safe_str(row.get("decision_score", "")),
                "decision_rank_in_category": safe_str(row.get("decision_rank_in_category", "")),
                "revenue_confirmation_status": rev_status,
                "revenue_confirmation_note": rev_note,
                "non_revenue_momentum_flag": "True",
                "non_revenue_momentum_type": momentum_type,
                "non_revenue_action_status": action_status,
                "fundamental_confirmation_needed": "True",
                "theme_final_status": safe_str(row.get("theme_final_status", "")),
                "theme_volume_attack_status": safe_str(row.get("theme_volume_attack_status", "")),
                "candidate_source_type": safe_str(row.get("candidate_source_type", "")),
                "volume_breakout_type": safe_str(row.get("volume_breakout_type", "")),
                "volume_breakout_priority": safe_str(row.get("volume_breakout_priority", "")),
                "selection_status": safe_str(row.get("selection_status", "")),
                "volume_ratio": safe_str(row.get("volume_ratio", "")),
                "return_5d": safe_str(row.get("return_5d", "")),
                "return_20d": safe_str(row.get("return_20d", "")),
                "tdcc_status": safe_str(row.get("tdcc_status", "")),
                "warrant_flow_signal": first_value(row, ["warrant_flow_signal", "warrant_flow_signal_volume"]),
                "must_not_overstate": safe_str(row.get("must_not_overstate", "")),
                "downgrade_flags": safe_str(row.get("downgrade_flags", "")),
                "risk_tags": safe_str(row.get("risk_tags", "")),
                "why_selected": safe_str(row.get("why_selected", "")),
                "why_downgraded": safe_str(row.get("why_downgraded", "")),
                "next_confirmation": next_confirmation,
                "interpretation": interpretation,
            }
        )

    out = pd.DataFrame(rows)
    if out.empty:
        return out

    type_order = {
        "A_fund_flow_confirmed_revenue_unconfirmed": 1,
        "B_turnaround_theme_watch": 2,
        "C_hot_money_watch": 3,
        "D_overheated_or_failed_risk": 4,
    }
    priority_order = {"A": 1, "B": 2, "C": 3, "D": 4}
    out["_type_order"] = out["non_revenue_momentum_type"].map(type_order).fillna(99)
    out["_priority_order"] = out["decision_priority"].astype(str).str[0].map(priority_order).fillna(9)
    out["_score"] = pd.to_numeric(out["decision_score"], errors="coerce").fillna(-999)
    out["_volume_ratio"] = pd.to_numeric(out["volume_ratio"], errors="coerce").fillna(-999)
    out = out.sort_values(
        ["_type_order", "_priority_order", "_score", "_volume_ratio"],
        ascending=[True, True, False, False],
    )
    return out.drop(columns=["_type_order", "_priority_order", "_score", "_volume_ratio"])


def md_table(headers: Iterable[str], rows: Iterable[Iterable[Any]]) -> list[str]:
    headers = [str(h) for h in headers]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        values = [safe_str(v).replace("\n", " ").replace("|", "/") for v in row]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def write_outputs(out: pd.DataFrame) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT_CSV, index=False, encoding="utf-8", lineterminator="\n")
    out.to_csv(DOCS_CSV, index=False, encoding="utf-8", lineterminator="\n")

    lines: list[str] = []
    lines.append("# Non-Revenue Momentum Watch")
    lines.append("")
    lines.append("## Metadata")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append(f"- main_price_date: `{read_main_price_date()}`")
    lines.append("- section_type: `specialty_section_not_core_category`")
    lines.append("- model_effect_allowed: `False`")
    lines.append("- allowed_use: `reporting_priority_and_follow_up_only`")
    lines.append("- rule: This is not a seventh core daily category. It is a specialty overlay for stocks where price/theme/fund flow is moving before revenue confirmation.")
    lines.append("")
    lines.append("## Interpretation Rules")
    lines.append("- `A_fund_flow_confirmed_revenue_unconfirmed`: price/volume or theme support is present, but EPS/gross margin/revenue confirmation is still required.")
    lines.append("- `B_turnaround_theme_watch`: theme or fund-flow support is emerging, but price confirmation is incomplete.")
    lines.append("- `C_hot_money_watch`: hot-money or technical movement exists, but fundamentals are not confirmed.")
    lines.append("- `D_overheated_or_failed_risk`: risk, overheated, distribution, or failed-breakout warning exists; do not promote to main attack list.")
    lines.append("- These rows should be discussed separately from the six fixed categories and must not be used as core weight changes.")
    lines.append("")

    if out.empty:
        lines.append("## Current Rows")
        lines.extend(md_table(["status", "note"], [["empty", "No rows matched the non-revenue momentum watch conditions."]]))
    else:
        lines.append("## Type Counts")
        counts = out["non_revenue_momentum_type"].value_counts().reset_index()
        counts.columns = ["non_revenue_momentum_type", "count"]
        lines.extend(md_table(counts.columns, counts.values.tolist()))
        lines.append("")

        display_cols = [
            "non_revenue_momentum_type",
            "stock_id",
            "stock_name",
            "theme_name",
            "decision_priority",
            "decision_score",
            "revenue_confirmation_status",
            "theme_final_status",
            "theme_volume_attack_status",
            "volume_breakout_type",
            "volume_ratio",
            "tdcc_status",
            "warrant_flow_signal",
            "interpretation",
            "next_confirmation",
        ]
        display_cols = [col for col in display_cols if col in out.columns]
        lines.append("## Current Watch List")
        lines.extend(md_table(display_cols, out[display_cols].head(40).values.tolist()))

    text = "\n".join(lines) + "\n"
    OUT_MD.write_text(text, encoding="utf-8")
    DOCS_MD.write_text(text, encoding="utf-8")


def main() -> int:
    base = merge_sources()
    out = build_rows(base) if not base.empty else pd.DataFrame()
    write_outputs(out)
    print(f"Saved: {OUT_CSV} rows={len(out)}")
    print(f"Saved: {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
