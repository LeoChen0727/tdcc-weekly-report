from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any

import pandas as pd
from pandas.errors import PerformanceWarning

from tracking_utils import (
    DOCS_LATEST_DIR,
    LATEST_DIR,
    STOCK_PRICE_HISTORY_DIR,
    fmt_pct,
    markdown_table,
    normalize_code,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


OUT_EVENTS = LATEST_DIR / "explosive_volume_up_events_latest.csv"
OUT_SUMMARY = LATEST_DIR / "explosive_volume_up_backtest_latest.csv"
OUT_POSITION_SUMMARY = LATEST_DIR / "explosive_volume_up_position_backtest_latest.csv"
OUT_MD = LATEST_DIR / "explosive_volume_up_backtest_latest.md"
HISTORY_EVENTS = Path("output/history/research/explosive_volume_up_events.csv")
HISTORY_SUMMARY = Path("output/history/research/explosive_volume_up_backtest.csv")
HISTORY_POSITION_SUMMARY = Path("output/history/research/explosive_volume_up_position_backtest.csv")
THEME_STATUS_HISTORY = LATEST_DIR / "daily_theme_status_history_latest.csv"
COMPANY_THEME_MAPPING = Path("data/theme_events/company_theme_mapping.csv")
STRUCTURAL_THEME_OVERRIDES = Path("data/theme_events/structural_theme_overrides.csv")

# Structural theme buckets are intentionally finer than industry.
# Example: 華通 remains PCB and 啟碁 remains networking, but both can still
# carry the low-earth-orbit satellite bucket when their theme tags say so.
STRUCTURAL_THEME_RULES = [
    (
        "low_earth_orbit_satellite_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        [
            "low earth orbit",
            "leo satellite",
            "leo",
            "satellite",
            "satellite communication",
            "space satellite",
            "starlink",
            "低軌",
            "低軌衛星",
            "太空衛星",
            "衛星",
            "星鏈",
        ],
    ),
    (
        "pcb_ccl_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["pcb", "ccl", "copper clad", "substrate", "printed circuit", "載板", "銅箔基板", "印刷電路板"],
    ),
    (
        "glass_fiber_ccl_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["glass fiber", "glass cloth", "fiberglass", "玻纖", "玻纖布", "玻纖紗", "銅箔基板", "高頻材料"],
    ),
    (
        "network_communication_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["network", "networking", "communication", "telecom", "網通", "通訊", "通訊設備"],
    ),
    (
        "optical_communication_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["optical", "fiber", "光通訊", "光纖"],
    ),
    (
        "cpo_silicon_photonics_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["cpo", "silicon photonics", "co-packaged optics", "矽光子", "共同封裝光學"],
    ),
    (
        "advanced_packaging_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["advanced packaging", "cowos", "soic", "foplp", "abf", "封裝", "先進封裝", "封測"],
    ),
    (
        "semiconductor_equipment_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["semiconductor equipment", "wafer equipment", "test equipment", "inspection", "probe", "半導體設備", "檢測", "探針"],
    ),
    (
        "semiconductor_materials_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["semiconductor material", "silicon wafer", "cmp", "photoresist", "mask", "specialty gas", "半導體材料", "矽晶圓", "光阻", "特用氣體", "光罩"],
    ),
    (
        "semiconductor_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["semiconductor", "ic design", "foundry", "advanced packaging", "equipment", "materials", "半導體", "先進封裝"],
    ),
    (
        "passive_component_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["passive", "mlcc", "capacitor", "resistor", "被動元件", "電容", "電阻"],
    ),
    (
        "ai_server_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["ai server", "server", "rack", "gpu", "伺服器"],
    ),
    (
        "power_thermal_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["cooling", "thermal", "power supply", "psu", "ups", "散熱", "電源", "電力", "不斷電"],
    ),
    (
        "connector_cable_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["connector", "cable", "wire harness", "連接器", "線材", "線束"],
    ),
    (
        "memory_hbm_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["memory", "hbm", "dram", "nand", "flash", "記憶體"],
    ),
    (
        "consumer_electronics_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["consumer electronics", "pc", "nb", "notebook", "gaming", "消費性電子", "電腦週邊"],
    ),
    (
        "robotics_automation_theme",
        "core_mainstream_theme",
        "mainstream_growth_theme",
        ["robot", "automation", "industrial computer", "motion control", "機器人", "自動化", "工業電腦", "控制器"],
    ),
    (
        "defense_industrial_theme",
        "non_mainstream_theme",
        "non_mainstream_rotation_theme",
        ["defense", "aerospace", "shipbuilding", "military", "防衛", "航太", "造船", "軍工"],
    ),
    (
        "ev_vehicle_theme",
        "non_mainstream_theme",
        "non_mainstream_rotation_theme",
        ["ev", "vehicle", "battery", "automotive", "車用", "電動車", "電池"],
    ),
    ("textile_theme", "non_mainstream_theme", "non_mainstream_rotation_theme", ["textile", "紡織", "成衣"]),
    ("financial_theme", "non_mainstream_theme", "non_mainstream_rotation_theme", ["financial", "finance", "bank", "insurance", "金融", "銀行", "保險"]),
    ("steel_theme", "non_mainstream_theme", "non_mainstream_rotation_theme", ["steel", "鋼鐵"]),
    ("shipping_theme", "non_mainstream_theme", "non_mainstream_rotation_theme", ["shipping", "航運"]),
    ("construction_theme", "non_mainstream_theme", "non_mainstream_rotation_theme", ["construction", "cement", "營建", "建材", "水泥"]),
    ("chemical_plastic_theme", "non_mainstream_theme", "non_mainstream_rotation_theme", ["chemical", "plastic", "化工", "塑膠"]),
    ("tourism_food_theme", "non_mainstream_theme", "non_mainstream_rotation_theme", ["tourism", "food", "觀光", "食品"]),
]

DOCS_EVENTS = DOCS_LATEST_DIR / OUT_EVENTS.name
DOCS_SUMMARY = DOCS_LATEST_DIR / OUT_SUMMARY.name
DOCS_POSITION_SUMMARY = DOCS_LATEST_DIR / OUT_POSITION_SUMMARY.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name

VOLUME_RATIO_THRESHOLDS = [10, 8, 6, 5, 4, 3, 2]
MIN_SIGNAL_RETURNS = [0, 3, 5, 7]
HORIZONS = list(range(1, 21))
TARGETS = [5, 10, 20]

warnings.simplefilter("ignore", PerformanceWarning)


def load_price(path: Path) -> pd.DataFrame:
    df = read_csv(path, dtype=str)
    if df.empty:
        return df
    if "date" not in df.columns:
        return pd.DataFrame()
    for col in ["open", "high", "low", "close", "volume"]:
        if col not in df.columns:
            return pd.DataFrame()
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["date"] = df["date"].map(normalize_date)
    if "stock_id" not in df.columns:
        df["stock_id"] = normalize_code(path.stem)
    df["stock_id"] = df["stock_id"].map(normalize_code)
    if "stock_name" not in df.columns:
        df["stock_name"] = ""
    if "market" not in df.columns:
        df["market"] = ""
    df = df.dropna(subset=["open", "high", "low", "close", "volume"])
    df = df[df["date"].astype(str).str.len() == 8]
    return df.sort_values("date").reset_index(drop=True)


def build_stock_events(path: Path) -> pd.DataFrame:
    price = load_price(path)
    if len(price) < 45:
        return pd.DataFrame()

    price["prev_close"] = price["close"].shift(1)
    price["signal_return_1d_pct"] = (price["close"] / price["prev_close"] - 1) * 100
    price["intraday_return_pct"] = (price["close"] / price["open"] - 1) * 100
    day_range = price["high"] - price["low"]
    red_body = price["close"] - price["open"]
    upper_shadow = price["high"] - price[["open", "close"]].max(axis=1)
    price["real_body_pct_of_range"] = (red_body / day_range) * 100
    price["upper_shadow_pct_of_range"] = (upper_shadow / day_range) * 100
    price["close_location_pct"] = ((price["close"] - price["low"]) / day_range) * 100
    price["is_red_candle"] = price["close"].gt(price["open"])
    price["strict_red_close_near_high"] = (
        price["is_red_candle"]
        & price["real_body_pct_of_range"].ge(40)
        & price["upper_shadow_pct_of_range"].le(25)
        & price["close_location_pct"].ge(75)
    )
    price["relaxed_red_small_upper_shadow"] = (
        price["is_red_candle"]
        & price["real_body_pct_of_range"].ge(25)
        & price["upper_shadow_pct_of_range"].le(35)
        & price["close_location_pct"].ge(65)
    )
    price["signal_quality_bucket"] = "not_red_or_failed_close"
    price.loc[day_range.le(0) | day_range.isna(), "signal_quality_bucket"] = "invalid_intraday_range"
    price.loc[price["is_red_candle"], "signal_quality_bucket"] = "red_candle_but_not_strong_close"
    price.loc[price["relaxed_red_small_upper_shadow"], "signal_quality_bucket"] = "relaxed_red_small_upper_shadow"
    price.loc[price["strict_red_close_near_high"], "signal_quality_bucket"] = "strict_red_close_near_high"
    price["prev20_volume_avg"] = price["volume"].shift(1).rolling(20, min_periods=10).mean()
    price["prev5_volume_avg"] = price["volume"].shift(1).rolling(5, min_periods=3).mean()
    price["volume_ratio_vs_prev20"] = price["volume"] / price["prev20_volume_avg"]
    price["volume_ratio_vs_prev5"] = price["volume"] / price["prev5_volume_avg"]
    price["prev_day_volume_ratio_vs_prev20"] = price["volume"].shift(1) / price["prev20_volume_avg"]
    price["next_open"] = price["open"].shift(-1)
    price["high_60"] = price["high"].shift(1).rolling(60, min_periods=30).max()
    price["low_60"] = price["low"].shift(1).rolling(60, min_periods=30).min()
    price["high_120"] = price["high"].shift(1).rolling(120, min_periods=60).max()
    price["low_120"] = price["low"].shift(1).rolling(120, min_periods=60).min()
    price["ma20"] = price["close"].rolling(20, min_periods=20).mean()
    price["ema23"] = price["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    price["return_20d_before_signal_pct"] = (price["close"].shift(1) / price["close"].shift(21) - 1) * 100
    price["return_60d_before_signal_pct"] = (price["close"].shift(1) / price["close"].shift(61) - 1) * 100
    price["distance_to_60d_high_pct"] = (price["close"] / price["high_60"] - 1) * 100
    price["distance_to_60d_low_pct"] = (price["close"] / price["low_60"] - 1) * 100
    price["distance_to_120d_high_pct"] = (price["close"] / price["high_120"] - 1) * 100
    price["distance_to_120d_low_pct"] = (price["close"] / price["low_120"] - 1) * 100
    price["distance_to_ema23_pct"] = (price["close"] / price["ema23"] - 1) * 100
    pct_60 = (price["close"] - price["low_60"]) / (price["high_60"] - price["low_60"])
    pct_120 = (price["close"] - price["low_120"]) / (price["high_120"] - price["low_120"])
    price["price_position_bucket"] = "mid_range_volume_attack"
    price.loc[pct_60.isna() | price["high_60"].le(price["low_60"]), "price_position_bucket"] = "insufficient_position_history"
    price.loc[pct_60.le(0.35) & price["return_20d_before_signal_pct"].le(10), "price_position_bucket"] = "bottom_or_low_zone_volume_reversal"
    price.loc[
        pct_60.gt(0.35)
        & pct_60.le(0.50)
        & price["distance_to_ema23_pct"].ge(0)
        & price["return_20d_before_signal_pct"].le(15),
        "price_position_bucket",
    ] = "low_to_mid_reclaim_volume_attack"
    price.loc[pct_60.ge(0.70), "price_position_bucket"] = "near_high_volume_attack"
    price.loc[pct_60.ge(0.80) & price["return_20d_before_signal_pct"].ge(20), "price_position_bucket"] = "high_zone_extension_or_chase"
    price.loc[
        price["price_position_bucket"].eq("mid_range_volume_attack")
        & pct_120.le(0.35)
        & price["return_20d_before_signal_pct"].le(15),
        "price_position_bucket",
    ] = "long_base_low_zone_volume_reversal"

    for horizon in HORIZONS:
        window_high = price["high"].shift(-1).rolling(horizon, min_periods=horizon).max().shift(-(horizon - 1))
        window_low = price["low"].shift(-1).rolling(horizon, min_periods=horizon).min().shift(-(horizon - 1))
        d_close = price["close"].shift(-horizon)
        price[f"mature_d{horizon}"] = price["next_open"].notna() & d_close.notna()
        price[f"next_open_to_d{horizon}_close_return_pct"] = (d_close / price["next_open"] - 1) * 100
        price[f"next_open_to_d{horizon}_max_high_return_pct"] = (window_high / price["next_open"] - 1) * 100
        price[f"next_open_to_d{horizon}_max_low_return_pct"] = (window_low / price["next_open"] - 1) * 100

    mask = (
        price["volume_ratio_vs_prev20"].ge(min(VOLUME_RATIO_THRESHOLDS))
        & price["signal_return_1d_pct"].ge(min(MIN_SIGNAL_RETURNS))
        & price["next_open"].notna()
    )
    out = price.loc[mask].copy()
    if out.empty:
        return pd.DataFrame()
    keep = [
        "date",
        "stock_id",
        "stock_name",
        "market",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "prev20_volume_avg",
        "prev5_volume_avg",
        "volume_ratio_vs_prev20",
        "volume_ratio_vs_prev5",
        "prev_day_volume_ratio_vs_prev20",
        "signal_return_1d_pct",
        "intraday_return_pct",
        "real_body_pct_of_range",
        "upper_shadow_pct_of_range",
        "close_location_pct",
        "is_red_candle",
        "strict_red_close_near_high",
        "relaxed_red_small_upper_shadow",
        "signal_quality_bucket",
        "next_open",
        "high_60",
        "low_60",
        "high_120",
        "low_120",
        "ma20",
        "ema23",
        "return_20d_before_signal_pct",
        "return_60d_before_signal_pct",
        "distance_to_60d_high_pct",
        "distance_to_60d_low_pct",
        "distance_to_120d_high_pct",
        "distance_to_120d_low_pct",
        "distance_to_ema23_pct",
        "price_position_bucket",
    ]
    for horizon in HORIZONS:
        keep += [
            f"mature_d{horizon}",
            f"next_open_to_d{horizon}_close_return_pct",
            f"next_open_to_d{horizon}_max_high_return_pct",
            f"next_open_to_d{horizon}_max_low_return_pct",
        ]
    return out[keep]


def classify_signal_quality(row: pd.Series) -> str:
    if to_number(row.get("high")) <= to_number(row.get("low")):
        return "invalid_intraday_range"
    if bool(row.get("strict_red_close_near_high")):
        return "strict_red_close_near_high"
    if bool(row.get("relaxed_red_small_upper_shadow")):
        return "relaxed_red_small_upper_shadow"
    if bool(row.get("is_red_candle")):
        return "red_candle_but_not_strong_close"
    return "not_red_or_failed_close"


def classify_price_position(row: pd.Series) -> str:
    close = to_number(row.get("close"))
    high_60 = to_number(row.get("high_60"))
    low_60 = to_number(row.get("low_60"))
    high_120 = to_number(row.get("high_120"))
    low_120 = to_number(row.get("low_120"))
    ret20 = to_number(row.get("return_20d_before_signal_pct"))
    dist_ema23 = to_number(row.get("distance_to_ema23_pct"))
    if pd.isna(close) or pd.isna(high_60) or pd.isna(low_60) or high_60 <= low_60:
        return "insufficient_position_history"
    pct_60 = (close - low_60) / (high_60 - low_60)
    pct_120 = (close - low_120) / (high_120 - low_120) if high_120 > low_120 else pd.NA
    if pct_60 <= 0.35 and ret20 <= 10:
        return "bottom_or_low_zone_volume_reversal"
    if pct_60 <= 0.50 and dist_ema23 >= 0 and ret20 <= 15:
        return "low_to_mid_reclaim_volume_attack"
    if pct_60 >= 0.80 and ret20 >= 20:
        return "high_zone_extension_or_chase"
    if pct_60 >= 0.70:
        return "near_high_volume_attack"
    if pd.notna(pct_120) and pct_120 <= 0.35 and ret20 <= 15:
        return "long_base_low_zone_volume_reversal"
    return "mid_range_volume_attack"


def load_theme_status_history() -> pd.DataFrame:
    df = read_csv(THEME_STATUS_HISTORY, dtype=str)
    if df.empty or not {"signal_date", "stock_id"}.issubset(df.columns):
        return pd.DataFrame()
    df = df.copy()
    df["date"] = df["signal_date"].map(normalize_date)
    df["stock_id"] = df["stock_id"].map(normalize_code)
    keep = [
        "date",
        "stock_id",
        "theme_name",
        "industry",
        "theme_final_status",
        "theme_status_group",
        "theme_structural_status",
        "structural_theme_bucket",
        "theme_mainstream_label",
        "static_structural_theme_bucket",
        "static_theme_mainstream_label",
        "theme_volume_attack_status",
        "candidate_source_type",
        "candidate_line_group",
    ]
    existing = [col for col in keep if col in df.columns]
    return df[existing].drop_duplicates(["date", "stock_id"], keep="last")


def classify_structural_theme(text: str) -> tuple[str, str, str]:
    value = safe_str(text).lower()
    for bucket, structural_status, mainstream_label, keywords in STRUCTURAL_THEME_RULES:
        if any(keyword in value for keyword in keywords):
            return structural_status, bucket, mainstream_label
    if value:
        return "uncategorized_theme", "uncategorized_theme", "uncategorized_theme"
    return "theme_context_unavailable", "theme_context_unavailable", "theme_context_unavailable"


def load_company_theme_map() -> pd.DataFrame:
    df = read_csv(COMPANY_THEME_MAPPING, dtype=str)
    if df.empty or "stock_id" not in df.columns:
        return pd.DataFrame()
    df = df.copy()
    df["stock_id"] = df["stock_id"].map(normalize_code)
    for col in ["industry", "theme_tags", "theme_summary"]:
        if col not in df.columns:
            df[col] = ""
    combined = (df["industry"].fillna("") + " " + df["theme_tags"].fillna("") + " " + df["theme_summary"].fillna(""))
    classified = combined.map(classify_structural_theme)
    df["static_theme_structural_status"] = classified.map(lambda x: x[0])
    df["static_structural_theme_bucket"] = classified.map(lambda x: x[1])
    df["static_theme_mainstream_label"] = classified.map(lambda x: x[2])
    keep = [
        "stock_id",
        "industry",
        "theme_tags",
        "theme_summary",
        "static_theme_structural_status",
        "static_structural_theme_bucket",
        "static_theme_mainstream_label",
    ]
    mapped = df[keep].drop_duplicates("stock_id", keep="last")
    overrides = load_structural_theme_overrides()
    if overrides.empty:
        return mapped
    out = mapped.merge(overrides, on="stock_id", how="outer", suffixes=("", "_override"))
    for col in ["industry", "theme_tags", "theme_summary"]:
        if col not in out.columns:
            out[col] = ""
        out[col] = out[col].fillna("")
    if "override_industry" in out.columns:
        out["industry"] = out["industry"].where(
            out["industry"].ne(""),
            out["override_industry"].fillna(""),
        )
    for target, override_col in [
        ("static_theme_structural_status", "override_theme_structural_status"),
        ("static_structural_theme_bucket", "override_structural_theme_bucket"),
        ("static_theme_mainstream_label", "override_theme_mainstream_label"),
    ]:
        out[target] = out[target].fillna("")
        out[target] = out[override_col].fillna("").where(out[override_col].fillna("").ne(""), out[target])
    if "override_stock_name" in out.columns:
        out["theme_summary"] = out["theme_summary"].where(
            out["theme_summary"].ne(""),
            out["override_stock_name"].fillna("") + " " + out["override_theme_note"].fillna(""),
        )
    return out[keep].drop_duplicates("stock_id", keep="last")


def load_structural_theme_overrides() -> pd.DataFrame:
    df = read_csv(STRUCTURAL_THEME_OVERRIDES, dtype=str)
    if df.empty or "stock_id" not in df.columns:
        return pd.DataFrame()
    df = df.copy()
    df["stock_id"] = df["stock_id"].map(normalize_code)
    rename = {
        "stock_name": "override_stock_name",
        "primary_industry_hint": "override_industry",
        "structural_theme_bucket": "override_structural_theme_bucket",
        "theme_structural_status": "override_theme_structural_status",
        "theme_mainstream_label": "override_theme_mainstream_label",
        "theme_note": "override_theme_note",
    }
    for src in rename:
        if src not in df.columns:
            df[src] = ""
    keep = ["stock_id", *rename.values()]
    return df.rename(columns=rename)[keep].drop_duplicates("stock_id", keep="last")


def assign_market_theme_group(out: pd.DataFrame) -> pd.DataFrame:
    """Use investable theme buckets before legacy industry buckets."""
    unavailable = {
        "",
        "unknown",
        "theme_context_unavailable",
        "uncategorized_theme",
        "insufficient_data",
    }
    for col in ["structural_theme_bucket", "theme_name", "industry"]:
        if col not in out.columns:
            out[col] = ""
        out[col] = out[col].fillna("").astype(str).str.strip()

    out["market_theme_group"] = out["structural_theme_bucket"]
    out["theme_group_source"] = "structural_theme_bucket"

    use_theme_name = out["market_theme_group"].isin(unavailable)
    out.loc[use_theme_name, "market_theme_group"] = out.loc[use_theme_name, "theme_name"]
    out.loc[use_theme_name, "theme_group_source"] = "theme_name"

    use_industry = out["market_theme_group"].isin(unavailable)
    out.loc[use_industry, "market_theme_group"] = out.loc[use_industry, "industry"]
    out.loc[use_industry, "theme_group_source"] = "industry"

    still_missing = out["market_theme_group"].isin(unavailable)
    out.loc[still_missing, "market_theme_group"] = "theme_context_unavailable"
    out.loc[still_missing, "theme_group_source"] = "unavailable"
    return out


def enrich_theme_context(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return events
    theme = load_theme_status_history()
    out = events.copy()
    if not theme.empty:
        out = out.merge(theme, on=["date", "stock_id"], how="left")
    static_theme = load_company_theme_map()
    if not static_theme.empty:
        out = out.merge(static_theme, on="stock_id", how="left", suffixes=("", "_static"))
        for target, static_col in [
            ("industry", "industry_static"),
            ("theme_tags", "theme_tags_static"),
            ("theme_summary", "theme_summary_static"),
        ]:
            if target not in out.columns:
                out[target] = ""
            if static_col in out.columns:
                out[target] = out[target].fillna("")
                out[target] = out[target].where(out[target].ne(""), out[static_col].fillna(""))
    for col in [
        "theme_name",
        "theme_final_status",
        "theme_status_group",
        "theme_structural_status",
        "structural_theme_bucket",
        "theme_mainstream_label",
        "theme_volume_attack_status",
        "candidate_source_type",
        "candidate_line_group",
        "industry",
        "theme_tags",
        "theme_summary",
        "static_theme_structural_status",
        "static_structural_theme_bucket",
        "static_theme_mainstream_label",
        "market_theme_group",
        "theme_group_source",
    ]:
        if col not in out.columns:
            out[col] = ""
        out[col] = out[col].fillna("")
    out["theme_structural_status"] = out["theme_structural_status"].where(
        out["theme_structural_status"].ne(""),
        out["static_theme_structural_status"],
    )
    out["theme_mainstream_label"] = out["theme_mainstream_label"].where(
        out["theme_mainstream_label"].ne(""),
        out["static_theme_mainstream_label"],
    )
    out["structural_theme_bucket"] = out["structural_theme_bucket"].where(
        out["structural_theme_bucket"].ne(""),
        out["static_structural_theme_bucket"],
    )
    out["theme_mainstream_label"] = out["theme_mainstream_label"].replace("", "theme_context_unavailable")
    out["theme_structural_status"] = out["theme_structural_status"].replace("", "theme_context_unavailable")
    out["structural_theme_bucket"] = out["structural_theme_bucket"].replace("", "theme_context_unavailable")
    out["theme_status_group"] = out["theme_status_group"].replace("", "theme_context_unavailable")
    return assign_market_theme_group(out)


def summarize_rule(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if events.empty:
        return pd.DataFrame()
    for volume_threshold in VOLUME_RATIO_THRESHOLDS:
        for min_return in MIN_SIGNAL_RETURNS:
            part = events[
                events["volume_ratio_vs_prev20"].ge(volume_threshold)
                & events["signal_return_1d_pct"].ge(min_return)
            ].copy()
            if part.empty:
                continue
            rule_name = f"volume_ratio_prev20_ge_{volume_threshold}x_signal_return_ge_{min_return}pct"
            unique_stock_days = part[["date", "stock_id"]].drop_duplicates().shape[0]
            unique_stocks = part["stock_id"].nunique()
            for horizon in HORIZONS:
                mature_col = f"mature_d{horizon}"
                close_col = f"next_open_to_d{horizon}_close_return_pct"
                high_col = f"next_open_to_d{horizon}_max_high_return_pct"
                low_col = f"next_open_to_d{horizon}_max_low_return_pct"
                matured = part[part[mature_col].astype(bool)].copy()
                row: dict[str, Any] = {
                    "rule_name": rule_name,
                    "volume_ratio_threshold": volume_threshold,
                    "min_signal_return_pct": min_return,
                    "horizon": f"D+{horizon}",
                    "selected_stock_days": unique_stock_days,
                    "selected_stocks": unique_stocks,
                    "mature_count": len(matured),
                    "sample_status": sample_status(len(matured)),
                }
                if matured.empty:
                    rows.append(row)
                    continue
                close_ret = pd.to_numeric(matured[close_col], errors="coerce")
                high_ret = pd.to_numeric(matured[high_col], errors="coerce")
                low_ret = pd.to_numeric(matured[low_col], errors="coerce")
                row.update(
                    {
                        "close_win_rate_pct": round(close_ret.gt(0).mean() * 100, 2),
                        "avg_close_return_pct": round(close_ret.mean(), 2),
                        "median_close_return_pct": round(close_ret.median(), 2),
                        "avg_mfe_pct": round(high_ret.mean(), 2),
                        "median_mfe_pct": round(high_ret.median(), 2),
                        "avg_mae_pct": round(low_ret.mean(), 2),
                        "median_mae_pct": round(low_ret.median(), 2),
                    }
                )
                for target in TARGETS:
                    row[f"hit_rate_high_ge_{target}pct"] = round(high_ret.ge(target).mean() * 100, 2)
                    row[f"close_hit_rate_ge_{target}pct"] = round(close_ret.ge(target).mean() * 100, 2)
                rows.append(row)
    return pd.DataFrame(rows).sort_values(
        ["volume_ratio_threshold", "min_signal_return_pct", "horizon"],
        ascending=[False, True, True],
    )


def summarize_position_segments(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if events.empty or "price_position_bucket" not in events.columns:
        return pd.DataFrame()
    group_cols = [
        "signal_quality_bucket",
        "price_position_bucket",
        "market_theme_group",
        "theme_group_source",
        "theme_structural_status",
        "structural_theme_bucket",
        "theme_mainstream_label",
        "theme_status_group",
    ]
    grouped_events = events.copy()
    for col in group_cols:
        if col not in grouped_events.columns:
            grouped_events[col] = "unknown"
        grouped_events[col] = grouped_events[col].fillna("unknown").replace("", "unknown")
    for group_key, bucket_df in grouped_events.groupby(group_cols, dropna=False):
        (
            signal_quality,
            bucket,
            market_theme_group,
            theme_group_source,
            theme_structural_status,
            structural_theme_bucket,
            theme_mainstream_label,
            theme_status_group,
        ) = group_key
        for volume_threshold in VOLUME_RATIO_THRESHOLDS:
            for min_return in MIN_SIGNAL_RETURNS:
                part = bucket_df[
                    bucket_df["volume_ratio_vs_prev20"].ge(volume_threshold)
                    & bucket_df["signal_return_1d_pct"].ge(min_return)
                ].copy()
                if part.empty:
                    continue
                unique_stock_days = part[["date", "stock_id"]].drop_duplicates().shape[0]
                unique_stocks = part["stock_id"].nunique()
                for horizon in HORIZONS:
                    mature_col = f"mature_d{horizon}"
                    close_col = f"next_open_to_d{horizon}_close_return_pct"
                    high_col = f"next_open_to_d{horizon}_max_high_return_pct"
                    low_col = f"next_open_to_d{horizon}_max_low_return_pct"
                    matured = part[part[mature_col].astype(bool)].copy()
                    row: dict[str, Any] = {
                            "signal_quality_bucket": signal_quality,
                            "price_position_bucket": bucket,
                            "market_theme_group": market_theme_group,
                            "theme_group_source": theme_group_source,
                            "theme_structural_status": theme_structural_status,
                            "structural_theme_bucket": structural_theme_bucket,
                            "theme_mainstream_label": theme_mainstream_label,
                            "theme_status_group": theme_status_group,
                        "volume_ratio_threshold": volume_threshold,
                        "min_signal_return_pct": min_return,
                        "horizon": f"D+{horizon}",
                        "selected_stock_days": unique_stock_days,
                        "selected_stocks": unique_stocks,
                        "mature_count": len(matured),
                        "sample_status": sample_status(len(matured)),
                    }
                    if matured.empty:
                        rows.append(row)
                        continue
                    close_ret = pd.to_numeric(matured[close_col], errors="coerce")
                    high_ret = pd.to_numeric(matured[high_col], errors="coerce")
                    low_ret = pd.to_numeric(matured[low_col], errors="coerce")
                    row.update(
                        {
                            "close_win_rate_pct": round(close_ret.gt(0).mean() * 100, 2),
                            "avg_close_return_pct": round(close_ret.mean(), 2),
                            "median_close_return_pct": round(close_ret.median(), 2),
                            "avg_mfe_pct": round(high_ret.mean(), 2),
                            "median_mfe_pct": round(high_ret.median(), 2),
                            "avg_mae_pct": round(low_ret.mean(), 2),
                            "median_mae_pct": round(low_ret.median(), 2),
                        }
                    )
                    for target in TARGETS:
                        row[f"hit_rate_high_ge_{target}pct"] = round(high_ret.ge(target).mean() * 100, 2)
                        row[f"close_hit_rate_ge_{target}pct"] = round(close_ret.ge(target).mean() * 100, 2)
                    rows.append(row)
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows).sort_values(
        ["horizon", "signal_quality_bucket", "price_position_bucket", "hit_rate_high_ge_10pct", "close_win_rate_pct", "mature_count"],
        ascending=[True, True, True, False, False, False],
    )


def sample_status(mature_count: int) -> str:
    if mature_count >= 100:
        return "ok"
    if mature_count >= 30:
        return "small_sample"
    if mature_count > 0:
        return "insufficient_sample"
    return "pending_or_no_mature"


def fmt_num(value: Any, digits: int = 2) -> str:
    num = to_number(value)
    if pd.isna(num):
        return "-"
    return f"{num:.{digits}f}"


def best_tables(summary: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    if summary.empty:
        return pd.DataFrame(), pd.DataFrame()
    d10 = summary[summary["horizon"].eq("D+10")].copy()
    d20 = summary[summary["horizon"].eq("D+20")].copy()
    rank_cols = ["hit_rate_high_ge_10pct", "close_win_rate_pct", "mature_count"]
    d10 = d10.sort_values(rank_cols, ascending=[False, False, False]).head(20)
    d20 = d20.sort_values(rank_cols, ascending=[False, False, False]).head(20)
    return d10, d20


def build_markdown(events: pd.DataFrame, summary: pd.DataFrame, position_summary: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Explosive Volume Up Backtest")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append("- signal_definition: signal day volume / previous 20 trading day average volume >= threshold, and signal day close-to-close return >= minimum return.")
    lines.append("- entry_basis: next trading day open.")
    lines.append("- close_return: next open to D+N close.")
    lines.append("- high_hit_rate: after next-open entry, the highest high during the holding window reaches target return. This is performance labeling, not intraday signal entry.")
    lines.append("- strict_candle_quality: red candle, real body >= 40% of intraday range, upper shadow <= 25%, close location >= 75%.")
    lines.append("- relaxed_candle_quality: red candle, real body >= 25% of intraday range, upper shadow <= 35%, close location >= 65%.")
    lines.append("- purpose: research only; do not mix into daily candidate core ranking until sample and regime tests mature.")
    lines.append("")
    if events.empty or summary.empty:
        lines.append("_No mature events._")
        return "\n".join(lines) + "\n"

    lines.append("## Data Summary")
    lines.append("")
    lines.append(f"- total_event_rows: `{len(events)}`")
    lines.append(f"- unique_stock_days: `{events[['date', 'stock_id']].drop_duplicates().shape[0]}`")
    lines.append(f"- date_range: `{events['date'].min()}` to `{events['date'].max()}`")
    lines.append("")

    display_cols = [
        "rule_name",
        "horizon",
        "selected_stock_days",
        "mature_count",
        "close_win_rate_pct",
        "avg_close_return_pct",
        "median_close_return_pct",
        "hit_rate_high_ge_10pct",
        "hit_rate_high_ge_20pct",
        "avg_mfe_pct",
        "avg_mae_pct",
        "sample_status",
    ]

    for title, part in [("D+10 Highest +10% Hit Rate", best_tables(summary)[0]), ("D+20 Highest +10% Hit Rate", best_tables(summary)[1])]:
        lines.append(f"## {title}")
        lines.append("")
        lines.append(markdown_table(part, display_cols, limit=20))
        lines.append("")

    lines.append("## Threshold Matrix: D+10")
    lines.append("")
    d10 = summary[summary["horizon"].eq("D+10")].copy()
    lines.append(markdown_table(d10, display_cols, limit=80))
    lines.append("")

    lines.append("## Threshold Matrix: D+20")
    lines.append("")
    d20 = summary[summary["horizon"].eq("D+20")].copy()
    lines.append(markdown_table(d20, display_cols, limit=80))
    lines.append("")

    if not position_summary.empty:
        seg_cols = [
            "signal_quality_bucket",
            "price_position_bucket",
            "market_theme_group",
            "theme_group_source",
            "theme_structural_status",
            "structural_theme_bucket",
            "theme_mainstream_label",
            "theme_status_group",
            "volume_ratio_threshold",
            "min_signal_return_pct",
            "horizon",
            "selected_stock_days",
            "mature_count",
            "close_win_rate_pct",
            "avg_close_return_pct",
            "median_close_return_pct",
            "hit_rate_high_ge_10pct",
            "hit_rate_high_ge_20pct",
            "sample_status",
        ]
        lines.append("## Price Position Segments: D+10")
        lines.append("")
        seg_d10 = position_summary[position_summary["horizon"].eq("D+10")].copy()
        seg_d10 = seg_d10.sort_values(["hit_rate_high_ge_10pct", "mature_count"], ascending=[False, False])
        lines.append(markdown_table(seg_d10, seg_cols, limit=80))
        lines.append("")

        lines.append("## Price Position Segments: D+20")
        lines.append("")
        seg_d20 = position_summary[position_summary["horizon"].eq("D+20")].copy()
        seg_d20 = seg_d20.sort_values(["hit_rate_high_ge_10pct", "mature_count"], ascending=[False, False])
        lines.append(markdown_table(seg_d20, seg_cols, limit=80))
        lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    lines.append("- If a high volume-ratio threshold has very few mature samples, the hit rate is unstable even if it looks high.")
    lines.append("- If lowering the threshold increases sample size but hit rate falls toward 50%, volume alone is not discriminative enough.")
    lines.append("- This module should next be segmented by theme/mainstream status, TDCC phase, market regime, and technical position.")
    lines.append("")
    return "\n".join(lines) + "\n"


def compact_events(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return events
    keep = [
        "date",
        "stock_id",
        "stock_name",
        "industry",
        "market",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "prev20_volume_avg",
        "volume_ratio_vs_prev20",
        "volume_ratio_vs_prev5",
        "prev_day_volume_ratio_vs_prev20",
        "signal_return_1d_pct",
        "intraday_return_pct",
        "real_body_pct_of_range",
        "upper_shadow_pct_of_range",
        "close_location_pct",
        "is_red_candle",
        "strict_red_close_near_high",
        "relaxed_red_small_upper_shadow",
        "signal_quality_bucket",
        "next_open",
        "theme_name",
        "theme_final_status",
        "theme_status_group",
        "market_theme_group",
        "theme_group_source",
        "theme_structural_status",
        "structural_theme_bucket",
        "theme_mainstream_label",
        "static_structural_theme_bucket",
        "theme_volume_attack_status",
        "candidate_source_type",
        "candidate_line_group",
        "return_20d_before_signal_pct",
        "return_60d_before_signal_pct",
        "distance_to_60d_high_pct",
        "distance_to_60d_low_pct",
        "distance_to_120d_high_pct",
        "distance_to_120d_low_pct",
        "distance_to_ema23_pct",
        "price_position_bucket",
    ]
    for horizon in [1, 5, 10, 20]:
        keep += [
            f"mature_d{horizon}",
            f"next_open_to_d{horizon}_close_return_pct",
            f"next_open_to_d{horizon}_max_high_return_pct",
            f"next_open_to_d{horizon}_max_low_return_pct",
        ]
    existing = [col for col in keep if col in events.columns]
    out = events[existing].copy()
    return out.sort_values(["date", "volume_ratio_vs_prev20"], ascending=[False, False]).reset_index(drop=True)


def mirror_to_docs(paths: list[Path]) -> None:
    for path in paths:
        target = DOCS_LATEST_DIR / path.name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())


def main() -> int:
    rows: list[pd.DataFrame] = []
    for path in sorted(STOCK_PRICE_HISTORY_DIR.glob("*.csv")):
        events = build_stock_events(path)
        if not events.empty:
            rows.append(events)

    all_events = pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()
    all_events = enrich_theme_context(all_events)
    summary = summarize_rule(all_events)
    position_summary = summarize_position_segments(all_events)
    event_output = compact_events(all_events)

    write_csv(event_output, OUT_EVENTS)
    write_csv(summary, OUT_SUMMARY)
    write_csv(position_summary, OUT_POSITION_SUMMARY)
    write_csv(event_output, HISTORY_EVENTS)
    write_csv(summary, HISTORY_SUMMARY)
    write_csv(position_summary, HISTORY_POSITION_SUMMARY)
    OUT_MD.write_text(build_markdown(event_output, summary, position_summary), encoding="utf-8", newline="\n")
    mirror_to_docs([OUT_EVENTS, OUT_SUMMARY, OUT_POSITION_SUMMARY, OUT_MD])

    print(f"Saved: {OUT_EVENTS} rows={len(event_output)}")
    print(f"Saved: {OUT_SUMMARY} rows={len(summary)}")
    print(f"Saved: {OUT_POSITION_SUMMARY} rows={len(position_summary)}")
    print(f"Saved: {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
