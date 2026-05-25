from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    TDCC_SIGNALS_DIR,
    main_price_date_from_freshness,
    markdown_table,
    normalize_code,
    now_text,
    raw_url,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


SNAPSHOT_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_snapshot.csv"
NORMALIZED_LOG_CSV = TDCC_SIGNALS_DIR / "tdcc_normalized_signal_log.csv"
PERFORMANCE_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_performance.csv"
ABM_HISTORY_CSV = TDCC_SIGNALS_DIR / "tdcc_pre_move_accumulation_history.csv"
ABM_LATEST_CSV = LATEST_DIR / "tdcc_pre_move_accumulation_latest.csv"
EFFECTIVENESS_CSV = LATEST_DIR / "tdcc_signal_effectiveness_latest.csv"
EFFECTIVENESS_MD = LATEST_DIR / "tdcc_signal_effectiveness_latest.md"
STOCK_THEME_MAP_CSV = Path("config/stock_theme_map.csv")
COMPANY_THEME_MAPPING_CSV = Path("data/theme_events/company_theme_mapping.csv")
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"

STRENGTH_MD = LATEST_DIR / "tdcc_strength_ranking_top_latest.md"
STRENGTH_CSV = LATEST_DIR / "tdcc_strength_ranking_top_latest.csv"
ABM_TOP_MD = LATEST_DIR / "tdcc_pre_move_abm_top_latest.md"
ABM_TOP_CSV = LATEST_DIR / "tdcc_pre_move_abm_top_latest.csv"
PHASE_MD = LATEST_DIR / "tdcc_phase_distribution_latest.md"
PHASE_CSV = LATEST_DIR / "tdcc_phase_distribution_latest.csv"
TOP_RISK_MD = LATEST_DIR / "tdcc_top_risk_list_latest.md"
TOP_RISK_CSV = LATEST_DIR / "tdcc_top_risk_list_latest.csv"
PACKET_MD = LATEST_DIR / "tdcc_chatgpt_tracking_packet_latest.md"

README_PATHS = [
    LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt",
    Path("docs/latest/READ_ME_FIRST_DAILY_REPORT.txt"),
]

TOP_N = 50
PACKET_N = 30
RISK_N = 20

REQUIRED_COLUMNS = [
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "tdcc_price_phase",
    "setup_type",
    "abm_score",
    "abm_rank",
    "price_return_5d",
    "price_return_20d",
    "distance_ma20_pct",
    "volume_ratio_20d",
    "theme_breadth_score",
    "relative_return_vs_benchmark",
]

THEME_DETAIL_COLUMNS = [
    "theme_mainstream_status",
    "theme_heat_level",
    "theme_momentum_score",
    "theme_tdcc_breadth_score",
    "theme_price_breadth_score",
    "theme_warrant_heat_score",
    "theme_relative_strength",
]

STRENGTH_COLUMNS = [
    "rank",
    "stock_id",
    "stock_name",
    "theme",
    "theme_mainstream_status",
    "theme_heat_level",
    "tdcc_strength_score",
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "tdcc_price_phase",
    "setup_type",
    "abm_score",
    "price_return_5d",
    "price_return_20d",
    "relative_return_vs_benchmark",
    "distance_ma20_pct",
    "volume_ratio_20d",
    "theme_breadth_score",
    "theme_momentum_score",
    "theme_tdcc_breadth_score",
    "theme_price_breadth_score",
    "theme_warrant_heat_score",
    "theme_relative_strength",
    "risk_label",
    "risk_bucket",
    "interpretation",
]

ABM_COLUMNS = [
    "abm_rank",
    "stock_id",
    "stock_name",
    "theme",
    "theme_mainstream_status",
    "theme_heat_level",
    "abm_score",
    "tdcc_strength_score",
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "tdcc_price_phase",
    "setup_type",
    "price_return_5d",
    "price_return_20d",
    "relative_return_vs_benchmark",
    "distance_ma20_pct",
    "volume_ratio_20d",
    "theme_breadth_score",
    "theme_momentum_score",
    "theme_tdcc_breadth_score",
    "theme_price_breadth_score",
    "theme_warrant_heat_score",
    "theme_relative_strength",
    "accumulation_label",
    "tracking_priority",
    "trigger_to_watch",
    "interpretation",
]

RISK_COLUMNS = [
    "stock_id",
    "stock_name",
    "theme",
    "theme_mainstream_status",
    "tdcc_strength_score",
    "tdcc_price_phase",
    "price_return_20d",
    "relative_return_vs_benchmark",
    "distance_ma20_pct",
    "volume_ratio_20d",
    "risk_bucket",
    "interpretation",
]

TOP_RISK_COLUMNS = ["risk_group"] + RISK_COLUMNS

PHASE_PERFORMANCE_COLUMNS = [
    "tdcc_price_phase",
    "mature_sample_d5",
    "avg_ret_d5",
    "avg_relative_ret_d5",
    "mature_sample_d10",
    "avg_ret_d10",
    "avg_relative_ret_d10",
    "mature_sample_d20",
    "avg_ret_d20",
    "avg_relative_ret_d20",
    "avg_mfe_d10",
    "avg_mae_d10",
]


def as_bool(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def numeric_series(df: pd.DataFrame, column: str, default: float = math.nan) -> pd.Series:
    if column not in df.columns:
        return pd.Series(default, index=df.index, dtype="float64")
    return pd.to_numeric(df[column], errors="coerce")


def bool_series(df: pd.DataFrame, column: str) -> pd.Series:
    if column not in df.columns:
        return pd.Series(False, index=df.index)
    return df[column].map(as_bool)


def fmt_num(value: Any, digits: int = 2) -> str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return f"{num:.{digits}f}"


def standard_theme_from_text(*values: Any) -> str:
    text = " ".join(safe_str(v) for v in values if safe_str(v)).lower()
    if not text:
        return ""
    rules = [
        ("optical communication/CPO", ["optical", "cpo", "光通訊", "光通", "光纖"]),
        ("semiconductor equipment/materials", ["semiconductor_equipment", "wafer reclaim", "equipment", "material", "半導體設備", "設備", "材料"]),
        ("memory", ["memory", "dram", "flash", "記憶"]),
        ("passive components", ["passive", "mlcc", "capacitor", "resistor", "inductor", "被動", "電容", "電阻", "電感"]),
        ("PCB/CCL", ["pcb_ccl", "pcb", "ccl", "printed circuit", "玻纖", "銅箔", "電路板"]),
        ("power discrete/diodes", ["power_discrete", "mosfet", "diode", "diodes", "二極體", "功率"]),
        ("AI server supply chain", ["ai_server", "ai server", "server", "伺服器", "ipc"]),
        ("networking", ["networking", "wireless", "communications", "通信", "網通"]),
        ("EV/auto electronics", ["auto", "vehicle", "automotive", "汽車", "車用"]),
        ("green energy", ["green", "energy", "solar", "battery", "storage", "綠能", "電池", "儲能", "太陽能"]),
        ("biotechnology", ["biotech", "medical", "生技", "醫療"]),
        ("finance", ["finance", "bank", "insurance", "金融", "銀行", "保險"]),
        ("semiconductor", ["semiconductor", "ic design", "foundry", "半導體", "晶圓", "ic"]),
        ("consumer electronics", ["consumer", "panel", "display", "optoelectronics", "光電", "面板"]),
        ("traditional industries", ["cement", "food", "textile", "chemical", "plastic", "steel", "shipping", "tourism", "construction", "水泥", "食品", "紡織", "化學", "塑膠", "鋼鐵", "航運", "觀光", "營建", "建材", "不動產"]),
        ("other electronics", ["electronics", "electronic", "computer", "電機", "電子", "電腦", "資訊"]),
    ]
    for theme, keywords in rules:
        if any(keyword in text for keyword in keywords):
            return theme
    return ""


def fallback_theme_from_code(stock_id: Any, stock_name: Any = "") -> str:
    code = normalize_code(stock_id)
    name = safe_str(stock_name)
    if not code:
        return "other"
    if any(token in name for token in ["銀行", "金控", "保", "證"]):
        return "finance"
    if any(token in name for token in ["藥", "生", "醫", "寶齡", "杏輝", "逸達", "正瀚", "五鼎"]):
        return "biotechnology"
    if any(token in name for token in ["營", "建", "地產", "開發", "工"]):
        return "traditional industries"
    prefix2 = code[:2]
    prefix3 = code[:3]
    if prefix2 in {"28", "58"}:
        return "finance"
    if prefix2 in {"17", "65", "84"}:
        return "biotechnology"
    if prefix2 in {"13", "14", "18", "19", "20", "21", "22", "25", "26", "27", "29", "55", "56"}:
        return "traditional industries"
    if prefix3 in {"300", "301", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329"}:
        return "semiconductor"
    if prefix2 in {"30", "31", "32", "33", "34", "35", "36", "37"}:
        return "other electronics"
    if prefix2 in {"15", "16", "23", "24", "49", "52", "53", "54", "61", "62", "64", "66", "67", "80", "81", "82"}:
        return "other electronics"
    return "other"


def first_existing_value(row: pd.Series, columns: list[str]) -> str:
    for col in columns:
        if col in row.index:
            value = safe_str(row.get(col))
            if value:
                return value
    return ""


def load_theme_lookup() -> tuple[dict[str, str], dict[str, Any]]:
    lookup: dict[str, str] = {}
    source_counts = {"config": 0, "company_theme_mapping": 0, "all_candidates": 0}

    all_candidates = read_csv(ALL_CANDIDATES_CSV, dtype=str)
    if not all_candidates.empty:
        for _, row in all_candidates.iterrows():
            code = normalize_code(first_existing_value(row, ["stock_id", "code", "ticker"]))
            if not code:
                continue
            theme = first_existing_value(row, ["theme_group", "primary_theme", "細分族群", "industry", "sector", "sub_theme"])
            standard = standard_theme_from_text(theme)
            if standard:
                lookup[code] = standard
                source_counts["all_candidates"] += 1

    company_mapping = read_csv(COMPANY_THEME_MAPPING_CSV, dtype=str)
    if not company_mapping.empty:
        for _, row in company_mapping.iterrows():
            code = normalize_code(row.get("stock_id"))
            if not code:
                continue
            standard = standard_theme_from_text(row.get("theme_tags"), row.get("industry"), row.get("theme_summary"))
            if standard:
                lookup[code] = standard
                source_counts["company_theme_mapping"] += 1

    config_map = read_csv(STOCK_THEME_MAP_CSV, dtype=str)
    if not config_map.empty:
        for _, row in config_map.iterrows():
            code = normalize_code(row.get("code"))
            if not code:
                continue
            theme = safe_str(row.get("primary_theme"))
            standard = standard_theme_from_text(theme, row.get("secondary_theme"), row.get("industry"), row.get("concept_tags")) or theme
            if standard:
                lookup[code] = standard
                source_counts["config"] += 1

    return lookup, source_counts


def apply_theme_lookup(df: pd.DataFrame, meta: dict[str, Any]) -> None:
    if df.empty:
        meta["theme_lookup_rows"] = 0
        meta["theme_other_pct"] = 0
        return
    lookup, source_counts = load_theme_lookup()
    if "theme" not in df.columns:
        df["theme"] = ""
    before_other = df["theme"].astype(str).str.lower().isin(["", "other", "nan", "none"]).sum()
    for idx, row in df.iterrows():
        current = safe_str(row.get("theme"))
        if current and current.lower() not in {"other", "nan", "none"}:
            standard = standard_theme_from_text(current)
            if standard:
                df.at[idx, "theme"] = standard
            continue
        code = normalize_code(first_existing_value(row, ["stock_id", "code", "ticker"]))
        theme = lookup.get(code, "")
        if not theme:
            theme = standard_theme_from_text(row.get("industry"), row.get("secondary_theme"), row.get("stock_name"), row.get("name"))
        if not theme:
            theme = fallback_theme_from_code(code, first_existing_value(row, ["stock_name", "name"]))
        df.at[idx, "theme"] = theme or "other"
    after_other = df["theme"].astype(str).str.lower().isin(["", "other", "nan", "none"]).sum()
    meta["theme_lookup_rows"] = len(lookup)
    meta["theme_lookup_sources"] = source_counts
    meta["theme_other_before"] = int(before_other)
    meta["theme_other_after"] = int(after_other)
    meta["theme_other_pct"] = round(after_other / max(len(df), 1) * 100, 2)


def latest_date(df: pd.DataFrame) -> str:
    if df.empty or "signal_date" not in df.columns:
        return ""
    dates = [safe_str(v) for v in df["signal_date"].dropna().tolist()]
    return max(dates) if dates else ""


def signal_id_frame(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if out.empty:
        return out
    if "code" not in out.columns and "stock_id" in out.columns:
        out["code"] = out["stock_id"]
    if "stock_id" not in out.columns and "code" in out.columns:
        out["stock_id"] = out["code"]
    if "name" not in out.columns and "stock_name" in out.columns:
        out["name"] = out["stock_name"]
    if "stock_name" not in out.columns and "name" in out.columns:
        out["stock_name"] = out["name"]
    if "signal_date" not in out.columns and "signal_trade_date" in out.columns:
        out["signal_date"] = out["signal_trade_date"]
    if "signal_date" not in out.columns:
        out["signal_date"] = ""
    if "signal_id" not in out.columns:
        out["signal_id"] = out["signal_date"].astype(str) + "_" + out.get("code", "").astype(str) + "_normalized"
    else:
        empty = out["signal_id"].astype(str).isin(["", "nan", "None", "<NA>"])
        out.loc[empty, "signal_id"] = (
            out.loc[empty, "signal_date"].astype(str)
            + "_"
            + out.loc[empty, "code"].astype(str)
            + "_normalized"
        )
    return out


def combine_prefer_left(left: pd.Series, right: pd.Series) -> pd.Series:
    left_text = left.astype(str)
    empty = left.isna() | left_text.isin(["", "nan", "None", "<NA>"])
    return left.where(~empty, right)


def add_strength_fields(df: pd.DataFrame) -> None:
    all_up = bool_series(df, "all_thresholds_up")
    high_up = bool_series(df, "high_thresholds_up")
    weeks = numeric_series(df, "tdcc_consecutive_up_weeks", 0).fillna(0)
    breadth = numeric_series(df, "theme_breadth_score", 0).fillna(0)
    over_1000_up = bool_series(df, "has_1000")
    over_800_up = bool_series(df, "has_800")
    if "tdcc_1w_change_1000" in df.columns:
        over_1000_up = over_1000_up | (numeric_series(df, "tdcc_1w_change_1000", 0) > 0)
    if "tdcc_1w_change_800" in df.columns:
        over_800_up = over_800_up | (numeric_series(df, "tdcc_1w_change_800", 0) > 0)
    df["tdcc_strength_score"] = (
        all_up.astype(int) * 30
        + high_up.astype(int) * 20
        + weeks * 10
        + breadth * 10
        + over_1000_up.astype(int) * 10
        + over_800_up.astype(int) * 5
    ).round(2)


def derive_theme_fields(df: pd.DataFrame) -> None:
    if df.empty:
        for col in THEME_DETAIL_COLUMNS:
            df[col] = ""
        return
    if "theme" not in df.columns:
        df["theme"] = df.get("primary_theme", "")
    df["theme"] = df["theme"].astype(str).replace({"nan": "", "None": ""}).str.strip()
    df.loc[df["theme"].eq(""), "theme"] = "other"
    if "theme_breadth_score" not in df.columns:
        df["theme_breadth_score"] = ""

    work = df.copy()
    work["_theme"] = work["theme"].astype(str)
    work["_leading"] = work["tdcc_price_phase"].astype(str).eq("tdcc_leading_price")
    work["_confirmed"] = work["tdcc_price_phase"].astype(str).eq("tdcc_price_confirmed")
    work["_late"] = work["tdcc_price_phase"].astype(str).eq("price_leading_tdcc")
    work["_overheated"] = work["tdcc_price_phase"].astype(str).eq("overheated_after_tdcc") | work["setup_type"].astype(str).eq("overheated")
    work["_divergent"] = work["tdcc_price_phase"].astype(str).isin(["tdcc_price_divergence", "failed_after_tdcc"])
    work["_strength"] = numeric_series(work, "tdcc_strength_score", 0).fillna(0)
    work["_abm"] = numeric_series(work, "abm_score", 0).fillna(0)
    work["_breadth"] = numeric_series(work, "theme_breadth_score", 0).fillna(0)
    work["_rel"] = numeric_series(work, "relative_return_vs_benchmark", 0).fillna(0)
    stats = work.groupby("_theme", dropna=False).agg(
        theme_signal_count=("stock_id", "count"),
        leading_count=("_leading", "sum"),
        confirmed_count=("_confirmed", "sum"),
        late_count=("_late", "sum"),
        overheated_count=("_overheated", "sum"),
        divergent_count=("_divergent", "sum"),
        avg_strength=("_strength", "mean"),
        avg_abm=("_abm", "mean"),
        max_breadth=("_breadth", "max"),
        avg_relative=("_rel", "mean"),
    )

    def classify_theme(theme: str) -> str:
        row = stats.loc[theme]
        total = int(row["theme_signal_count"])
        leading = int(row["leading_count"])
        confirmed = int(row["confirmed_count"])
        late = int(row["late_count"])
        overheated = int(row["overheated_count"])
        divergent = int(row["divergent_count"])
        breadth = float(row["max_breadth"] or 0)
        avg_abm = float(row["avg_abm"] or 0)
        avg_rel = float(row["avg_relative"] or 0)
        active = leading + confirmed
        theme_l = theme.lower()
        if total <= 1 or theme_l in {"", "other", "nan", "none"}:
            return "single_name_signal"
        if divergent >= max(2, total * 0.35) and avg_rel < 0:
            return "weak_theme"
        if overheated >= max(2, total * 0.35) or late >= max(2, total * 0.4):
            return "mainstream_overheated"
        if total >= 5 and active >= 3 and breadth >= 2:
            return "mainstream_leader"
        if total >= 3 and active >= 2:
            return "mainstream_follow_through"
        if total >= 2 and leading >= 1 and avg_abm >= 60:
            return "emerging_theme"
        if total >= 2:
            return "non_mainstream_watch"
        return "single_name_signal"

    status_map = {theme: classify_theme(theme) for theme in stats.index}
    heat_map: dict[str, str] = {}
    momentum_map: dict[str, float] = {}
    price_breadth_map: dict[str, float] = {}
    rel_map: dict[str, float] = {}
    for theme, row in stats.iterrows():
        total = max(int(row["theme_signal_count"]), 1)
        active = int(row["leading_count"]) + int(row["confirmed_count"])
        overheated = int(row["overheated_count"])
        if overheated / total >= 0.35:
            heat = "overheated"
        elif active >= 3:
            heat = "high"
        elif active >= 1:
            heat = "medium"
        else:
            heat = "low"
        heat_map[theme] = heat
        momentum_map[theme] = round(active * 10 + int(row["late_count"]) * 3 + float(row["avg_relative"] or 0), 2)
        price_breadth_map[theme] = float(active + int(row["late_count"]))
        rel_map[theme] = round(float(row["avg_relative"] or 0), 2)

    df["theme_mainstream_status"] = df["theme"].map(status_map).fillna("single_name_signal")
    df["theme_heat_level"] = df["theme"].map(heat_map).fillna("low")
    df["theme_momentum_score"] = df["theme"].map(momentum_map).fillna(0)
    df["theme_tdcc_breadth_score"] = numeric_series(df, "theme_breadth_score", 0).fillna(0)
    df["theme_price_breadth_score"] = df["theme"].map(price_breadth_map).fillna(0)
    if "theme_warrant_heat_score" not in df.columns:
        df["theme_warrant_heat_score"] = numeric_series(df, "warrant_sector_heat_score", 0).fillna(0)
    df["theme_relative_strength"] = df["theme"].map(rel_map).fillna(0)


def prepare_latest_frame() -> tuple[pd.DataFrame, dict[str, Any]]:
    snapshot = signal_id_frame(read_csv(SNAPSHOT_CSV, dtype=str))
    abm = signal_id_frame(read_csv(ABM_LATEST_CSV, dtype=str))
    meta: dict[str, Any] = {
        "snapshot_rows": len(snapshot),
        "abm_latest_rows": len(abm),
        "ranking_quality": "complete",
        "missing_columns": [],
        "latest_signal_date": "",
        "benchmark_available": "unknown",
        "theme_data_available": "unknown",
        "theme_lookup_rows": 0,
        "theme_other_pct": 100,
    }
    if snapshot.empty and abm.empty:
        meta["ranking_quality"] = "no_data"
        return pd.DataFrame(), meta

    if snapshot.empty:
        base = abm.copy()
    else:
        signal_date = latest_date(snapshot)
        base = snapshot[snapshot["signal_date"].astype(str) == signal_date].copy()
        if not abm.empty:
            merge_cols = [
                "signal_id",
                "abm_score",
                "abm_rank",
                "setup_type",
                "priority_group",
                "tdcc_price_phase",
                "price_return_5d",
                "price_return_20d",
                "distance_ma20_pct",
                "volume_ratio_20d",
                "relative_ret_2w",
                "theme_breadth_score",
            ]
            keep = [c for c in merge_cols if c in abm.columns]
            if keep:
                base = base.merge(
                    abm[keep].drop_duplicates("signal_id", keep="last"),
                    on="signal_id",
                    how="left",
                    suffixes=("", "_abm"),
                )
                for col in merge_cols:
                    alt = f"{col}_abm"
                    if alt in base.columns:
                        current = base[col] if col in base.columns else pd.Series("", index=base.index)
                        base[col] = combine_prefer_left(current, base[alt])
                        base = base.drop(columns=[alt])

    if "stock_id" not in base.columns:
        base["stock_id"] = base.get("code", "")
    if "stock_name" not in base.columns:
        base["stock_name"] = base.get("name", "")
    if "theme" not in base.columns:
        base["theme"] = base.get("primary_theme", "")
    if "relative_return_vs_benchmark" not in base.columns:
        base["relative_return_vs_benchmark"] = base["relative_ret_2w"] if "relative_ret_2w" in base.columns else ""
    if "all_thresholds_up" not in base.columns:
        base["all_thresholds_up"] = base.get("is_all_thresholds", "")
    if "high_thresholds_up" not in base.columns:
        high = bool_series(base, "has_800") | bool_series(base, "has_1000")
        base["high_thresholds_up"] = high.map(lambda v: "True" if v else "False")

    for col in REQUIRED_COLUMNS:
        if col not in base.columns:
            base[col] = ""
            meta["missing_columns"].append(col)

    base = base.drop_duplicates("signal_id", keep="last").reset_index(drop=True)
    add_strength_fields(base)
    apply_theme_lookup(base, meta)
    derive_theme_fields(base)
    meta["latest_signal_date"] = latest_date(base)
    meta["benchmark_available"] = "yes" if numeric_series(base, "relative_return_vs_benchmark").notna().any() else "no"
    meta["theme_data_available"] = "yes" if meta.get("theme_other_pct", 100) < 80 else "partial"
    if meta["missing_columns"]:
        meta["ranking_quality"] = "partial"
    return base, meta


def risk_label(phase: Any) -> str:
    return {
        "tdcc_leading_price": "potential_accumulation",
        "tdcc_price_confirmed": "confirmed_move",
        "price_leading_tdcc": "late_or_chasing_risk",
        "overheated_after_tdcc": "overheated",
        "tdcc_price_divergence": "divergence_failed_watch",
        "failed_after_tdcc": "divergence_failed_watch",
        "insufficient_price_context": "insufficient_data",
        "insufficient_tdcc_history": "insufficient_data",
        "neutral_or_unclear": "neutral",
    }.get(safe_str(phase), "neutral")


def risk_bucket(phase: Any) -> str:
    return {
        "tdcc_leading_price": "strong_but_pre_move",
        "tdcc_price_confirmed": "strong_confirmed",
        "price_leading_tdcc": "strong_but_late",
        "overheated_after_tdcc": "strong_but_overheated",
        "tdcc_price_divergence": "strong_but_divergent",
        "failed_after_tdcc": "strong_but_divergent",
        "insufficient_price_context": "insufficient_data",
        "insufficient_tdcc_history": "insufficient_data",
    }.get(safe_str(phase), "insufficient_data" if "insufficient" in safe_str(phase) else "neutral")


def phase_interpretation(phase: Any) -> str:
    return {
        "tdcc_leading_price": "籌碼持續改善，但股價尚未明顯反應。",
        "tdcc_price_confirmed": "籌碼改善且股價已開始確認。",
        "price_leading_tdcc": "股價已先漲，TDCC 訊號可能偏晚。",
        "overheated_after_tdcc": "籌碼強但股價已過熱，需防追高。",
        "tdcc_price_divergence": "TDCC 增加但股價轉弱，需防訊號失效。",
        "failed_after_tdcc": "訊號後價格轉弱，列為失效觀察。",
        "insufficient_price_context": "價格或 benchmark 資料不足，不列入強弱判斷。",
        "insufficient_tdcc_history": "TDCC 歷史不足，不列入強弱判斷。",
        "neutral_or_unclear": "訊號不明確，僅保留觀察。",
    }.get(safe_str(phase), "資料不足或訊號不明確。")


def accumulation_label(row: pd.Series) -> str:
    phase = safe_str(row.get("tdcc_price_phase"))
    setup = safe_str(row.get("setup_type"))
    abm = to_number(row.get("abm_score"), 0)
    if phase == "tdcc_leading_price" and setup == "quiet_accumulation" and abm >= 80:
        return "prime_pre_move"
    if phase == "tdcc_leading_price" and abm >= 60:
        return "watch_pre_move"
    if phase == "tdcc_price_confirmed":
        return "confirmed_not_pre_move"
    if phase in {"price_leading_tdcc", "overheated_after_tdcc"}:
        return "not_pre_move_overheated"
    if phase in {"tdcc_price_divergence", "failed_after_tdcc"}:
        return "divergence_risk"
    if phase in {"insufficient_price_context", "insufficient_tdcc_history"}:
        return "insufficient_data"
    return "watch_only"


def tracking_priority(row: pd.Series) -> str:
    phase = safe_str(row.get("tdcc_price_phase"))
    setup = safe_str(row.get("setup_type"))
    label = safe_str(row.get("accumulation_label"))
    abm = to_number(row.get("abm_score"), 0)
    weeks = to_number(row.get("tdcc_consecutive_up_weeks"), 0)
    price20 = to_number(row.get("price_return_20d"))
    dist20 = to_number(row.get("distance_ma20_pct"))
    vol20 = to_number(row.get("volume_ratio_20d"))
    rel = to_number(row.get("relative_return_vs_benchmark"))
    theme_status = safe_str(row.get("theme_mainstream_status"))
    strong_theme = {"emerging_theme", "mainstream_follow_through", "mainstream_leader"}
    if phase in {"insufficient_price_context", "insufficient_tdcc_history"} or math.isnan(rel) or not theme_status:
        return "D_insufficient_data"
    if (
        phase == "tdcc_leading_price"
        and setup == "quiet_accumulation"
        and label == "prime_pre_move"
        and abm >= 90
        and weeks >= 2
        and not math.isnan(price20)
        and -3 <= price20 <= 8
        and not math.isnan(dist20)
        and dist20 <= 6
        and not math.isnan(vol20)
        and vol20 <= 1.5
        and rel >= 0
        and theme_status in strong_theme
    ):
        return "A_prime_watch"
    if phase == "tdcc_leading_price" and label in {"prime_pre_move", "watch_pre_move"} and abm >= 80:
        if (
            theme_status in {"single_name_signal", "weak_theme"}
            or (not math.isnan(price20) and price20 < -10)
            or rel < -5
            or (not math.isnan(price20) and price20 > 20)
        ):
            return "C_weak_or_discounted"
        return "B_confirm_needed"
    if phase == "tdcc_leading_price":
        return "C_weak_or_discounted"
    return "D_insufficient_data" if "insufficient" in phase else "C_weak_or_discounted"


def trigger_to_watch(row: pd.Series) -> str:
    priority = safe_str(row.get("tracking_priority"))
    rel = to_number(row.get("relative_return_vs_benchmark"))
    price20 = to_number(row.get("price_return_20d"))
    dist20 = to_number(row.get("distance_ma20_pct"))
    vol20 = to_number(row.get("volume_ratio_20d"))
    phase = safe_str(row.get("tdcc_price_phase"))
    theme_status = safe_str(row.get("theme_mainstream_status"))
    triggers: list[str] = []
    if priority == "A_prime_watch":
        triggers.extend(["量縮守住 MA20", "相對 benchmark 維持轉強", "避免爆量長上影"])
    else:
        if math.isnan(rel) or rel < 0:
            triggers.append("相對 benchmark 轉正")
        if math.isnan(dist20) or dist20 < 0:
            triggers.append("站回 MA20")
        elif dist20 <= 6:
            triggers.append("量縮守住 MA20")
        else:
            triggers.append("等待乖離收斂到 MA20 附近")
        if not math.isnan(vol20) and vol20 > 1.5:
            triggers.append("避免爆量長上影")
        else:
            triggers.append("放量站上 5 日 / 10 日均線")
        if not math.isnan(price20) and price20 < -3:
            triggers.append("價格止跌並重新轉強")
        if theme_status in {"single_name_signal", "non_mainstream_watch"}:
            triggers.append("等待第二檔 / 第三檔同族群股票同步轉強")
        if phase in {"tdcc_price_divergence", "failed_after_tdcc"}:
            triggers.append("確認 TDCC 背離是否解除")
    return "；".join(dict.fromkeys(triggers[:4]))


def format_numeric_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    numeric_cols = [
        "tdcc_strength_score",
        "abm_score",
        "price_return_5d",
        "price_return_20d",
        "relative_return_vs_benchmark",
        "distance_ma20_pct",
        "volume_ratio_20d",
        "theme_breadth_score",
        "theme_momentum_score",
        "theme_tdcc_breadth_score",
        "theme_price_breadth_score",
        "theme_warrant_heat_score",
        "theme_relative_strength",
    ]
    for col in numeric_cols:
        if col in out.columns:
            out[col] = out[col].map(lambda v: fmt_num(v, 2))
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    return out[columns]


def write_strength_top(df: pd.DataFrame, meta: dict[str, Any]) -> pd.DataFrame:
    if df.empty:
        out = pd.DataFrame(columns=STRENGTH_COLUMNS)
        write_csv(out, STRENGTH_CSV)
        STRENGTH_MD.write_text("# TDCC Strength Ranking Top\n\n目前沒有可用資料。\n", encoding="utf-8")
        return out
    top = df.copy()
    top["risk_label"] = top["tdcc_price_phase"].map(risk_label)
    top["risk_bucket"] = top["tdcc_price_phase"].map(risk_bucket)
    top["interpretation"] = top["tdcc_price_phase"].map(phase_interpretation)
    top = top.sort_values(["tdcc_strength_score", "tdcc_consecutive_up_weeks", "stock_id"], ascending=[False, False, True])
    top = top.head(TOP_N).copy()
    top["rank"] = range(1, len(top) + 1)
    out = format_numeric_columns(top, STRENGTH_COLUMNS)
    write_csv(out, STRENGTH_CSV)
    lines = [
        "# TDCC Strength Ranking Top",
        "",
        f"- generated_at: {now_text()}",
        f"- latest_signal_date: {meta.get('latest_signal_date', '')}",
        f"- ranking_quality: {meta.get('ranking_quality', '')}",
        f"- missing_columns: {','.join(meta.get('missing_columns', [])) or 'none'}",
        "",
        "注意：這是籌碼強弱榜，不等於潛伏吸籌榜。price_leading_tdcc / overheated_after_tdcc 不可解讀成潛伏吸籌。",
        "",
        markdown_table(out, STRENGTH_COLUMNS),
        "",
    ]
    STRENGTH_MD.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_abm_top(df: pd.DataFrame, meta: dict[str, Any]) -> tuple[pd.DataFrame, bool]:
    if df.empty:
        out = pd.DataFrame(columns=ABM_COLUMNS)
        write_csv(out, ABM_TOP_CSV)
        ABM_TOP_MD.write_text("# TDCC Pre-Move Accumulation / ABM Top\n\n目前沒有可用資料。\n", encoding="utf-8")
        return out, False
    work = df.copy()
    work["accumulation_label"] = work.apply(accumulation_label, axis=1)
    work["tracking_priority"] = work.apply(tracking_priority, axis=1)
    work["trigger_to_watch"] = work.apply(trigger_to_watch, axis=1)
    work["interpretation"] = work["tdcc_price_phase"].map(phase_interpretation)
    strict = (
        work["tdcc_price_phase"].astype(str).eq("tdcc_leading_price")
        & (numeric_series(work, "abm_score", 0) >= 60)
        & (numeric_series(work, "tdcc_consecutive_up_weeks", 0) >= 2)
        & (numeric_series(work, "distance_ma20_pct", 999) <= 15)
        & (numeric_series(work, "volume_ratio_20d", 999) <= 1.8)
        & (numeric_series(work, "price_return_20d", 999) <= 25)
        & (numeric_series(work, "relative_return_vs_benchmark", 0) >= -5)
    )
    filtered = work[strict].copy()
    relaxed = False
    if len(filtered) < 10:
        relaxed = True
        relaxed_mask = (
            work["tdcc_price_phase"].astype(str).isin(["tdcc_leading_price", "tdcc_price_confirmed"])
            | work["setup_type"].astype(str).eq("quiet_accumulation")
            | (numeric_series(work, "abm_score", 0) >= 60)
        )
        filtered = work[
            relaxed_mask
            & (numeric_series(work, "price_return_20d", 999) <= 30)
            & (numeric_series(work, "distance_ma20_pct", 999) <= 20)
        ].copy()
    priority_order = {"A_prime_watch": 0, "B_confirm_needed": 1, "C_weak_or_discounted": 2, "D_insufficient_data": 3}
    label_order = {
        "prime_pre_move": 0,
        "watch_pre_move": 1,
        "confirmed_not_pre_move": 2,
        "watch_only": 3,
        "divergence_risk": 4,
        "insufficient_data": 5,
        "not_pre_move_overheated": 6,
    }
    theme_order = {
        "emerging_theme": 0,
        "mainstream_follow_through": 1,
        "mainstream_leader": 2,
        "non_mainstream_watch": 3,
        "single_name_signal": 4,
        "weak_theme": 5,
        "mainstream_overheated": 6,
    }
    filtered["_priority_order"] = filtered["tracking_priority"].map(priority_order).fillna(9)
    filtered["_label_order"] = filtered["accumulation_label"].map(label_order).fillna(9)
    filtered["_theme_order"] = filtered["theme_mainstream_status"].map(theme_order).fillna(9)
    filtered = filtered.sort_values(
        ["_priority_order", "_label_order", "_theme_order", "abm_score", "tdcc_strength_score", "stock_id"],
        ascending=[True, True, True, False, False, True],
    ).head(TOP_N)
    filtered["abm_rank"] = range(1, len(filtered) + 1)
    out = format_numeric_columns(filtered, ABM_COLUMNS)
    write_csv(out, ABM_TOP_CSV)
    lines = [
        "# TDCC Pre-Move Accumulation / ABM Top",
        "",
        f"- generated_at: {now_text()}",
        f"- latest_signal_date: {meta.get('latest_signal_date', '')}",
        f"- relaxed_filter: {relaxed}",
        f"- ranking_quality: {meta.get('ranking_quality', '')}",
        f"- missing_columns: {','.join(meta.get('missing_columns', [])) or 'none'}",
        "",
        "注意：這份名單才是潛伏吸籌追蹤清單。ABM 高不等於買進，仍需看 trigger_to_watch。price_leading_tdcc / overheated_after_tdcc 不列為 prime_pre_move。",
        "",
        markdown_table(out, ABM_COLUMNS),
        "",
    ]
    ABM_TOP_MD.write_text("\n".join(lines), encoding="utf-8")
    return out, relaxed


def normalize_performance(perf: pd.DataFrame) -> pd.DataFrame:
    perf = signal_id_frame(perf)
    if perf.empty:
        return perf
    value_cols = [col for col in perf.columns if col != "signal_id"]
    return perf.groupby("signal_id", as_index=False).agg({col: "last" for col in value_cols})


def merge_snapshot_performance(snapshot: pd.DataFrame) -> pd.DataFrame:
    perf = normalize_performance(read_csv(PERFORMANCE_CSV, dtype=str))
    if snapshot.empty:
        return pd.DataFrame()
    base = signal_id_frame(snapshot.copy())
    if perf.empty:
        return base
    keep_cols = [
        c
        for c in perf.columns
        if c == "signal_id"
        or c.startswith(("d", "mature_", "relative_", "max_", "min_"))
        or c in {"status"}
    ]
    perf = perf[keep_cols].drop_duplicates("signal_id", keep="last")
    return base.merge(perf, on="signal_id", how="left", suffixes=("", "_perf"))


def maturity_mask(df: pd.DataFrame, horizon: int) -> pd.Series:
    col = f"mature_d{horizon}"
    ret_col = f"d{horizon}_return_pct"
    if col in df.columns:
        return df[col].map(as_bool)
    if ret_col in df.columns:
        return numeric_series(df, ret_col).notna()
    return pd.Series(False, index=df.index)


def avg_col(df: pd.DataFrame, col: str) -> str:
    if df.empty or col not in df.columns:
        return ""
    value = pd.to_numeric(df[col], errors="coerce").mean()
    if math.isnan(value):
        return ""
    return f"{value:.2f}"


def phase_mature_counts(phase_table: pd.DataFrame) -> dict[str, int]:
    performance = phase_table[phase_table.get("section", "") == "phase_performance"] if not phase_table.empty else pd.DataFrame()
    out: dict[str, int] = {}
    for horizon in [5, 10, 20]:
        col = f"mature_sample_d{horizon}"
        out[f"phase_mature_d{horizon}_count"] = (
            int(pd.to_numeric(performance[col], errors="coerce").fillna(0).sum()) if col in performance.columns else 0
        )
    return out


def write_phase_distribution(latest_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    total = len(latest_df)
    if not latest_df.empty:
        phase_counts = latest_df["tdcc_price_phase"].fillna("").replace("", "unknown").value_counts().reset_index()
        phase_counts.columns = ["tdcc_price_phase", "sample_count"]
        for _, row in phase_counts.iterrows():
            count = int(row["sample_count"])
            rows.append(
                {
                    "section": "phase_distribution",
                    "tdcc_price_phase": row["tdcc_price_phase"],
                    "sample_count": count,
                    "pct_of_total": f"{(count / total * 100) if total else 0:.2f}",
                }
            )
        weeks_phase = latest_df.groupby(["tdcc_consecutive_up_weeks", "tdcc_price_phase"], dropna=False).size().reset_index(name="signal_count")
        for _, row in weeks_phase.iterrows():
            rows.append(
                {
                    "section": "consecutive_weeks_x_phase",
                    "tdcc_consecutive_up_weeks": safe_str(row.get("tdcc_consecutive_up_weeks")),
                    "tdcc_price_phase": safe_str(row.get("tdcc_price_phase")) or "unknown",
                    "signal_count": int(row["signal_count"]),
                }
            )
        conditions = {
            "all_thresholds_up": bool_series(latest_df, "all_thresholds_up"),
            "high_thresholds_up": bool_series(latest_df, "high_thresholds_up"),
            "over_800_or_above": bool_series(latest_df, "has_800") | bool_series(latest_df, "has_1000"),
            "over_1000_only": bool_series(latest_df, "has_1000") & ~bool_series(latest_df, "has_800"),
            "consecutive_2w": numeric_series(latest_df, "tdcc_consecutive_up_weeks", 0) >= 2,
            "consecutive_3w": numeric_series(latest_df, "tdcc_consecutive_up_weeks", 0) >= 3,
            "quiet_accumulation": latest_df["setup_type"].astype(str).eq("quiet_accumulation"),
            "early_breakout": latest_df["setup_type"].astype(str).eq("early_breakout"),
            "strong_momentum": latest_df["setup_type"].astype(str).eq("strong_momentum"),
            "overheated": latest_df["setup_type"].astype(str).eq("overheated") | latest_df["tdcc_price_phase"].astype(str).eq("overheated_after_tdcc"),
        }
        for name, mask in conditions.items():
            counts = latest_df[mask]["tdcc_price_phase"].fillna("").replace("", "unknown").value_counts()
            if counts.empty:
                rows.append({"section": "condition_x_phase", "condition_name": name, "tdcc_price_phase": "none", "signal_count": 0})
            for phase, count in counts.items():
                rows.append({"section": "condition_x_phase", "condition_name": name, "tdcc_price_phase": phase, "signal_count": int(count)})

    all_snapshot = signal_id_frame(read_csv(SNAPSHOT_CSV, dtype=str))
    perf_base = merge_snapshot_performance(all_snapshot)
    if not perf_base.empty and "tdcc_price_phase" in perf_base.columns:
        for phase, group in perf_base.groupby("tdcc_price_phase", dropna=False):
            row: dict[str, Any] = {"section": "phase_performance", "tdcc_price_phase": safe_str(phase) or "unknown"}
            for horizon in [5, 10, 20]:
                mature = group[maturity_mask(group, horizon)].copy()
                row[f"mature_sample_d{horizon}"] = len(mature)
                row[f"avg_ret_d{horizon}"] = avg_col(mature, f"d{horizon}_return_pct")
                row[f"avg_relative_ret_d{horizon}"] = avg_col(mature, f"relative_return_vs_benchmark_d{horizon}")
            row["avg_mfe_d10"] = avg_col(group[maturity_mask(group, 10)], "max_return_10d")
            row["avg_mae_d10"] = avg_col(group[maturity_mask(group, 10)], "max_drawdown_10d")
            rows.append(row)

    out = pd.DataFrame(rows)
    write_csv(out, PHASE_CSV)
    phase_dist = out[out["section"] == "phase_distribution"] if not out.empty else pd.DataFrame()
    weeks_phase = out[out["section"] == "consecutive_weeks_x_phase"] if not out.empty else pd.DataFrame()
    condition_phase = out[out["section"] == "condition_x_phase"] if not out.empty else pd.DataFrame()
    performance = out[out["section"] == "phase_performance"] if not out.empty else pd.DataFrame()
    counts = phase_mature_counts(out)
    pending_notes = []
    for horizon in [5, 10, 20]:
        if counts[f"phase_mature_d{horizon}_count"] == 0:
            pending_notes.append(f"- phase-level D+{horizon} 尚未成熟，不可做 phase 勝率結論。")
    lines = [
        "# TDCC Phase Distribution",
        "",
        f"- generated_at: {now_text()}",
        f"- latest_signal_count: {total}",
        f"- phase_mature_d5_count: {counts['phase_mature_d5_count']}",
        f"- phase_mature_d10_count: {counts['phase_mature_d10_count']}",
        f"- phase_mature_d20_count: {counts['phase_mature_d20_count']}",
        "",
        "## Phase 分布",
        "",
        markdown_table(phase_dist, ["tdcc_price_phase", "sample_count", "pct_of_total"]),
        "",
        "## 連續週數 x Phase",
        "",
        markdown_table(weeks_phase, ["tdcc_consecutive_up_weeks", "tdcc_price_phase", "signal_count"]),
        "",
        "## TDCC 條件 x Phase",
        "",
        markdown_table(condition_phase, ["condition_name", "tdcc_price_phase", "signal_count"]),
        "",
        "## Phase 後續成熟績效",
        "",
        "\n".join(pending_notes),
        "",
        markdown_table(performance, PHASE_PERFORMANCE_COLUMNS),
        "",
    ]
    PHASE_MD.write_text("\n".join(lines), encoding="utf-8")
    return out


def count_mature(perf: pd.DataFrame, horizon: int) -> int:
    if perf.empty:
        return 0
    normalized = normalize_performance(perf)
    return int(maturity_mask(normalized, horizon).sum())


def count_pending(perf: pd.DataFrame) -> int:
    if perf.empty:
        return 0
    normalized = normalize_performance(perf)
    mature_any = pd.Series(False, index=normalized.index)
    for horizon in [5, 10, 20]:
        mature_any = mature_any | maturity_mask(normalized, horizon)
    return int((~mature_any).sum())


def file_ok(path: Path) -> str:
    return "yes" if path.exists() and path.stat().st_size > 0 else "no"


def build_risk_lists(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    result: dict[str, pd.DataFrame] = {}
    work = df.copy()
    if not work.empty:
        work["risk_bucket"] = work["tdcc_price_phase"].map(risk_bucket)
        work["interpretation"] = work["tdcc_price_phase"].map(phase_interpretation)
    for phase in ["price_leading_tdcc", "overheated_after_tdcc", "tdcc_price_divergence"]:
        if work.empty:
            part = pd.DataFrame(columns=RISK_COLUMNS)
        else:
            part = work[work["tdcc_price_phase"].astype(str).eq(phase)].copy()
            part = part.sort_values(["tdcc_strength_score", "price_return_20d", "stock_id"], ascending=[False, False, True]).head(RISK_N)
        result[phase] = format_numeric_columns(part, RISK_COLUMNS)
    return result


def phase_join_quality(overall_counts: dict[str, int], phase_counts: dict[str, int]) -> str:
    notes: list[str] = []
    for horizon in [5, 10, 20]:
        overall = overall_counts[f"overall_mature_d{horizon}_count"]
        phase = phase_counts[f"phase_mature_d{horizon}_count"]
        if overall > 0 and phase == 0:
            notes.append(f"D+{horizon}: overall mature exists but phase-level mature is zero; phase field may be newly added or join key is incomplete")
        elif overall != phase:
            notes.append(f"D+{horizon}: overall={overall}, phase={phase}")
    return "ok" if not notes else "; ".join(notes)


def sample_status(overall_counts: dict[str, int], phase_counts: dict[str, int]) -> str:
    if phase_counts["phase_mature_d5_count"] == 0:
        if overall_counts["overall_mature_d5_count"] > 0:
            return "overall_mature_available_but_phase_level_not_ready"
        return "no_mature_phase_samples"
    if phase_counts["phase_mature_d10_count"] == 0 or phase_counts["phase_mature_d20_count"] == 0:
        return "phase_d5_available_longer_horizons_pending"
    return "phase_samples_available"


def theme_section_table(df: pd.DataFrame, status_values: set[str], columns: list[str], limit: int = 20) -> pd.DataFrame:
    if df.empty or "theme_mainstream_status" not in df.columns:
        return pd.DataFrame(columns=columns)
    part = df[df["theme_mainstream_status"].astype(str).isin(status_values)].copy()
    if part.empty:
        return pd.DataFrame(columns=columns)
    return part.head(limit)[columns]


def build_theme_summary(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "theme",
        "theme_mainstream_status",
        "signal_count",
        "leading_count",
        "confirmed_count",
        "late_or_overheated_count",
        "divergence_count",
        "avg_tdcc_strength_score",
        "avg_abm_score",
        "representative_codes",
    ]
    if df.empty or "theme" not in df.columns:
        return pd.DataFrame(columns=columns)
    work = df.copy()
    work["_leading"] = work["tdcc_price_phase"].astype(str).eq("tdcc_leading_price")
    work["_confirmed"] = work["tdcc_price_phase"].astype(str).eq("tdcc_price_confirmed")
    work["_late_or_overheated"] = work["tdcc_price_phase"].astype(str).isin(["price_leading_tdcc", "overheated_after_tdcc"])
    work["_divergence"] = work["tdcc_price_phase"].astype(str).isin(["tdcc_price_divergence", "failed_after_tdcc"])
    rows: list[dict[str, Any]] = []
    for theme, group in work.groupby("theme", dropna=False):
        theme_text = safe_str(theme) or "other"
        codes = group.sort_values("tdcc_strength_score", ascending=False)["stock_id"].astype(str).head(5).tolist()
        rows.append(
            {
                "theme": theme_text,
                "theme_mainstream_status": group["theme_mainstream_status"].astype(str).mode().iloc[0] if "theme_mainstream_status" in group.columns and not group.empty else "",
                "signal_count": len(group),
                "leading_count": int(group["_leading"].sum()),
                "confirmed_count": int(group["_confirmed"].sum()),
                "late_or_overheated_count": int(group["_late_or_overheated"].sum()),
                "divergence_count": int(group["_divergence"].sum()),
                "avg_tdcc_strength_score": fmt_num(numeric_series(group, "tdcc_strength_score").mean(), 2),
                "avg_abm_score": fmt_num(numeric_series(group, "abm_score").mean(), 2),
                "representative_codes": "|".join(codes),
            }
        )
    out = pd.DataFrame(rows, columns=columns)
    if out.empty:
        return out
    return out.sort_values(["signal_count", "leading_count", "confirmed_count"], ascending=[False, False, False]).head(30)


def write_top_risk_list(risk_lists: dict[str, pd.DataFrame]) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for phase, part in risk_lists.items():
        tmp = part.copy()
        tmp.insert(0, "risk_group", phase)
        frames.append(tmp)
    out = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=TOP_RISK_COLUMNS)
    for col in TOP_RISK_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    out = out[TOP_RISK_COLUMNS]
    write_csv(out, TOP_RISK_CSV)
    lines = [
        "# TDCC Top Risk List",
        "",
        f"- generated_at: {now_text()}",
        "- purpose: identify TDCC-strong names that are late, overheated, or divergent; do not treat these as pre-move accumulation.",
        "",
        "## price_leading_tdcc Top 20",
        "",
        markdown_table(risk_lists.get("price_leading_tdcc", pd.DataFrame(columns=RISK_COLUMNS)), RISK_COLUMNS),
        "",
        "## overheated_after_tdcc Top 20",
        "",
        markdown_table(risk_lists.get("overheated_after_tdcc", pd.DataFrame(columns=RISK_COLUMNS)), RISK_COLUMNS),
        "",
        "## tdcc_price_divergence Top 20",
        "",
        markdown_table(risk_lists.get("tdcc_price_divergence", pd.DataFrame(columns=RISK_COLUMNS)), RISK_COLUMNS),
        "",
    ]
    TOP_RISK_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return out


def write_packet(meta: dict[str, Any], strength_top: pd.DataFrame, abm_top: pd.DataFrame, phase_table: pd.DataFrame, latest_df: pd.DataFrame) -> None:
    perf = read_csv(PERFORMANCE_CSV, dtype=str)
    overall_counts = {
        "overall_mature_d5_count": count_mature(perf, 5),
        "overall_mature_d10_count": count_mature(perf, 10),
        "overall_mature_d20_count": count_mature(perf, 20),
    }
    phase_counts = phase_mature_counts(phase_table)
    pending_count = count_pending(perf)
    join_quality = phase_join_quality(overall_counts, phase_counts)
    status = sample_status(overall_counts, phase_counts)
    insufficient_count = 0
    if not phase_table.empty and "tdcc_price_phase" in phase_table.columns:
        sample_col = phase_table.get("sample_count", pd.Series(dtype=float))
        insufficient_count = int(
            phase_table[
                (phase_table.get("section", "") == "phase_distribution")
                & phase_table["tdcc_price_phase"].astype(str).isin(["insufficient_price_context", "insufficient_tdcc_history"])
            ]
            .get("sample_count", pd.Series(dtype=float))
            .astype(float)
            .sum()
        )

    phase_dist = phase_table[phase_table.get("section", "") == "phase_distribution"] if not phase_table.empty else pd.DataFrame()
    weeks_phase = phase_table[phase_table.get("section", "") == "consecutive_weeks_x_phase"] if not phase_table.empty else pd.DataFrame()
    performance = phase_table[phase_table.get("section", "") == "phase_performance"] if not phase_table.empty else pd.DataFrame()
    risk_lists = build_risk_lists(latest_df)
    write_top_risk_list(risk_lists)
    theme_summary = build_theme_summary(latest_df)
    mature_notes: list[str] = []
    for horizon in [5, 10, 20]:
        phase_count = phase_counts[f"phase_mature_d{horizon}_count"]
        overall_count = overall_counts[f"overall_mature_d{horizon}_count"]
        if phase_count == 0:
            mature_notes.append(f"- phase-level D+{horizon} 尚未成熟，不可做 phase 勝率結論。")
        if overall_count > 0 and phase_count == 0:
            mature_notes.append(
                f"- overall_mature_d{horizon}_count={overall_count} 但 phase_mature_d{horizon}_count=0；原因通常是 phase 欄位為新加、舊樣本未補 phase，或 performance join key 不完整。"
            )

    theme_cols = ["stock_id", "stock_name", "theme", "theme_mainstream_status", "tdcc_price_phase", "abm_score", "tracking_priority", "risk_bucket", "interpretation"]
    strength_theme_cols = ["stock_id", "stock_name", "theme", "theme_mainstream_status", "tdcc_strength_score", "tdcc_price_phase", "risk_bucket", "interpretation"]
    abm_theme_cols = ["stock_id", "stock_name", "theme", "theme_mainstream_status", "abm_score", "tracking_priority", "tdcc_price_phase", "trigger_to_watch"]
    strength_for_theme = strength_top.copy()
    abm_for_theme = abm_top.copy()

    lines = [
        "# TDCC CHATGPT TRACKING PACKET",
        "",
        "## Metadata",
        f"- generated_at: {now_text()}",
        f"- main_price_date: {main_price_date_from_freshness()}",
        f"- latest_tdcc_signal_date: {meta.get('latest_signal_date', '')}",
        "- source_files: tdcc_signal_snapshot.csv, tdcc_normalized_signal_log.csv, tdcc_signal_performance.csv, tdcc_pre_move_accumulation_latest.csv, tdcc_signal_effectiveness_latest.md",
        f"- overall_mature_d5_count: {overall_counts['overall_mature_d5_count']}",
        f"- phase_mature_d5_count: {phase_counts['phase_mature_d5_count']}",
        f"- overall_mature_d10_count: {overall_counts['overall_mature_d10_count']}",
        f"- phase_mature_d10_count: {phase_counts['phase_mature_d10_count']}",
        f"- overall_mature_d20_count: {overall_counts['overall_mature_d20_count']}",
        f"- phase_mature_d20_count: {phase_counts['phase_mature_d20_count']}",
        f"- pending_count: {pending_count}",
        f"- insufficient_sample_count: {insufficient_count}",
        f"- ranking_quality: {meta.get('ranking_quality', '')}",
        f"- phase_mature_join_quality: {join_quality}",
        f"- benchmark_available: {meta.get('benchmark_available', 'unknown')}",
        f"- theme_data_available: {meta.get('theme_data_available', 'unknown')}",
        f"- theme_lookup_rows: {meta.get('theme_lookup_rows', 0)}",
        f"- theme_other_pct: {meta.get('theme_other_pct', '')}",
        f"- sample_status: {status}",
        f"- relaxed_filter: {meta.get('relaxed_filter', '')}",
        f"- missing_columns: {','.join(meta.get('missing_columns', [])) or 'none'}",
        "",
        "## Data Availability",
        f"- tdcc_signal_snapshot.csv: {file_ok(SNAPSHOT_CSV)}",
        f"- tdcc_normalized_signal_log.csv: {file_ok(NORMALIZED_LOG_CSV)}",
        f"- tdcc_signal_performance.csv: {file_ok(PERFORMANCE_CSV)}",
        f"- tdcc_pre_move_accumulation_history.csv: {file_ok(ABM_HISTORY_CSV)}",
        f"- tdcc_pre_move_accumulation_latest.csv: {file_ok(ABM_LATEST_CSV)}",
        f"- tdcc_signal_effectiveness_latest.csv: {file_ok(EFFECTIVENESS_CSV)}",
        f"- tdcc_signal_effectiveness_latest.md: {file_ok(EFFECTIVENESS_MD)}",
        "",
        "## Data Quality Notes",
        f"- missing_columns: {','.join(meta.get('missing_columns', [])) or 'none'}",
        f"- ranking_quality: {meta.get('ranking_quality', '')}",
        f"- phase_mature_join_quality: {join_quality}",
        f"- benchmark_available: {meta.get('benchmark_available', 'unknown')}",
        f"- theme_data_available: {meta.get('theme_data_available', 'unknown')}",
        f"- theme_lookup_rows: {meta.get('theme_lookup_rows', 0)}",
        f"- theme_lookup_sources: {meta.get('theme_lookup_sources', {})}",
        f"- theme_other_before: {meta.get('theme_other_before', '')}",
        f"- theme_other_after: {meta.get('theme_other_after', '')}",
        f"- theme_other_pct: {meta.get('theme_other_pct', '')}",
        f"- sample_status: {status}",
        f"- relaxed_filter: {meta.get('relaxed_filter', '')}",
        "- packet_generated_from: snapshot + ABM latest + normalized performance + phase distribution",
        "",
        "## Mature Sample Status",
        "",
        f"- overall_mature_d5_count: {overall_counts['overall_mature_d5_count']}",
        f"- phase_mature_d5_count: {phase_counts['phase_mature_d5_count']}",
        f"- overall_mature_d10_count: {overall_counts['overall_mature_d10_count']}",
        f"- phase_mature_d10_count: {phase_counts['phase_mature_d10_count']}",
        f"- overall_mature_d20_count: {overall_counts['overall_mature_d20_count']}",
        f"- phase_mature_d20_count: {phase_counts['phase_mature_d20_count']}",
        f"- pending_count: {pending_count}",
        f"- insufficient_sample_count: {insufficient_count}",
        f"- phase_mature_join_quality: {join_quality}",
        f"- sample_status: {status}",
        "",
        "\n".join(mature_notes) if mature_notes else "- phase-level mature sample 已可使用。",
        "",
        "## TDCC Strength Ranking Top 30",
        "",
        markdown_table(strength_top.head(PACKET_N), STRENGTH_COLUMNS),
        "",
        "## Pre-Move Accumulation / ABM Top 30",
        "",
        markdown_table(abm_top.head(PACKET_N), ABM_COLUMNS),
        "",
        "## Theme Mainstream Summary",
        "",
        markdown_table(theme_summary, list(theme_summary.columns) if not theme_summary.empty else [
            "theme",
            "theme_mainstream_status",
            "signal_count",
            "leading_count",
            "confirmed_count",
            "late_or_overheated_count",
            "divergence_count",
            "avg_tdcc_strength_score",
            "avg_abm_score",
            "representative_codes",
        ]),
        "",
        "## TDCC Strength Ranking by Theme Mainstream Status",
        "",
        markdown_table(strength_for_theme.head(PACKET_N), strength_theme_cols),
        "",
        "## Pre-Move / ABM Ranking by Theme Mainstream Status",
        "",
        markdown_table(abm_for_theme.head(PACKET_N), abm_theme_cols),
        "",
        "## 主流潛伏吸籌名單",
        "",
        markdown_table(theme_section_table(abm_for_theme, {"emerging_theme", "mainstream_follow_through", "mainstream_leader"}, abm_theme_cols), abm_theme_cols),
        "",
        "## 非主流但值得觀察名單",
        "",
        markdown_table(theme_section_table(abm_for_theme, {"non_mainstream_watch"}, abm_theme_cols), abm_theme_cols),
        "",
        "## 孤單訊號 / 非主流降權名單",
        "",
        markdown_table(theme_section_table(abm_for_theme, {"single_name_signal", "weak_theme"}, abm_theme_cols), abm_theme_cols),
        "",
        "## 主流過熱風險名單",
        "",
        markdown_table(theme_section_table(strength_for_theme, {"mainstream_overheated"}, strength_theme_cols), strength_theme_cols),
        "",
        "## TDCC 背離 + 弱族群名單",
        "",
        markdown_table(
            latest_df[
                latest_df["tdcc_price_phase"].astype(str).isin(["tdcc_price_divergence", "failed_after_tdcc"])
                & latest_df["theme_mainstream_status"].astype(str).isin(["weak_theme", "single_name_signal"])
            ].assign(risk_bucket=lambda d: d["tdcc_price_phase"].map(risk_bucket), interpretation=lambda d: d["tdcc_price_phase"].map(phase_interpretation)).pipe(format_numeric_columns, strength_theme_cols),
            strength_theme_cols,
        ),
        "",
        "## Top Risk List",
        "",
        "- price_leading_tdcc: 股價已先漲，TDCC 訊號可能偏晚。",
        "- overheated_after_tdcc: 籌碼強但股價已過熱。",
        "- tdcc_price_divergence: TDCC 增加但股價轉弱，需列為失效觀察。",
        "",
        "## Top Risk List - price_leading_tdcc Top 20",
        "",
        markdown_table(risk_lists["price_leading_tdcc"], RISK_COLUMNS),
        "",
        "## Top Risk List - overheated_after_tdcc Top 20",
        "",
        markdown_table(risk_lists["overheated_after_tdcc"], RISK_COLUMNS),
        "",
        "## Top Risk List - tdcc_price_divergence Top 20",
        "",
        markdown_table(risk_lists["tdcc_price_divergence"], RISK_COLUMNS),
        "",
        "## Phase Distribution",
        "",
        markdown_table(phase_dist, ["tdcc_price_phase", "sample_count", "pct_of_total"]),
        "",
        "## Consecutive Weeks x Phase",
        "",
        markdown_table(weeks_phase, ["tdcc_consecutive_up_weeks", "tdcc_price_phase", "signal_count"]),
        "",
        "## Mature Performance Summary",
        "",
        "只使用 mature_dN=True 的資料。pending 不可視為正面或負面。",
        "",
        "\n".join(mature_notes) if mature_notes else "- phase-level mature sample 已可使用。",
        "",
        markdown_table(performance, PHASE_PERFORMANCE_COLUMNS),
        "",
        "## Model Tuning Recommendation",
        "",
        "- tuning_status: not_ready",
        "- reason: insufficient mature D+10 / D+20 samples",
        "- allowed_changes: reporting_priority_only",
        "- forbidden_changes: core_weight_change",
        "- threshold_for_review: each major phase mature_d10 >= 30, or overall mature_d20 >= 100 with at least 3-4 weeks of data",
        "- note: 目前可以調整追蹤優先級與報告分層，但不可調整核心 TDCC / ABM 權重。",
        "",
        "## Interpretation Rules",
        "- pending 不可視為正面或負面。",
        "- same stock_id + signal_date 只能算一筆 normalized signal。",
        "- TDCC Strength Ranking 找籌碼最強，不等於潛伏吸籌。",
        "- Pre-Move / ABM Ranking 才是找潛伏吸籌。",
        "- price_leading_tdcc / overheated_after_tdcc 不可寫成潛伏吸籌。",
        "- tdcc_price_divergence 要列為失效觀察。",
        "- 必須同時看絕對報酬與相對 TWSE / TPEx benchmark。",
        "- 在 tuning_status=not_ready 前，不可調整核心模型權重。",
        "",
    ]
    PACKET_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def upsert_readme_fields() -> None:
    fields = {
        "tdcc_strength_ranking_top_md_raw_url": raw_url(STRENGTH_MD),
        "tdcc_strength_ranking_top_csv_raw_url": raw_url(STRENGTH_CSV),
        "tdcc_pre_move_abm_top_md_raw_url": raw_url(ABM_TOP_MD),
        "tdcc_pre_move_abm_top_csv_raw_url": raw_url(ABM_TOP_CSV),
        "tdcc_phase_distribution_md_raw_url": raw_url(PHASE_MD),
        "tdcc_phase_distribution_csv_raw_url": raw_url(PHASE_CSV),
        "tdcc_top_risk_list_md_raw_url": raw_url(TOP_RISK_MD),
        "tdcc_top_risk_list_csv_raw_url": raw_url(TOP_RISK_CSV),
        "tdcc_chatgpt_tracking_packet_raw_url": raw_url(PACKET_MD),
    }
    for path in README_PATHS:
        existing_lines = path.read_text(encoding="utf-8", errors="replace").splitlines() if path.exists() else []
        seen = set(fields)
        new_lines: list[str] = []
        inserted = False
        for line in existing_lines:
            key = line.split("=", 1)[0] if "=" in line else ""
            if key in fields:
                new_lines.append(f"{key}={fields[key]}")
                seen.discard(key)
            elif line == "RULES:" and not inserted:
                for missing_key, value in fields.items():
                    if missing_key in seen:
                        new_lines.append(f"{missing_key}={value}")
                seen.clear()
                inserted = True
                new_lines.append(line)
            else:
                new_lines.append(line)
        if not existing_lines:
            new_lines = [f"{key}={value}" for key, value in fields.items()]
        elif seen:
            for key, value in fields.items():
                if key in seen:
                    new_lines.append(f"{key}={value}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(new_lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    latest_df, meta = prepare_latest_frame()
    strength_top = write_strength_top(latest_df, meta)
    abm_top, relaxed = write_abm_top(latest_df, meta)
    meta["relaxed_filter"] = relaxed
    phase_table = write_phase_distribution(latest_df)
    write_packet(meta, strength_top, abm_top, phase_table, latest_df)
    upsert_readme_fields()
    print(f"Saved: {STRENGTH_MD}")
    print(f"Saved: {STRENGTH_CSV}")
    print(f"Saved: {ABM_TOP_MD}")
    print(f"Saved: {ABM_TOP_CSV}")
    print(f"Saved: {PHASE_MD}")
    print(f"Saved: {PHASE_CSV}")
    print(f"Saved: {TOP_RISK_MD}")
    print(f"Saved: {TOP_RISK_CSV}")
    print(f"Saved: {PACKET_MD}")
    print(f"ranking_quality={meta.get('ranking_quality')}")
    print(f"missing_columns={','.join(meta.get('missing_columns', [])) or 'none'}")
    print(f"theme_other_pct={meta.get('theme_other_pct')}")


if __name__ == "__main__":
    main()
