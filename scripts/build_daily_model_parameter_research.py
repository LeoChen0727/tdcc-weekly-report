from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from research_weekly_20pct_surge_volume import build_stock_day_frame  # noqa: E402
from research_weekly_surge_technical_grid import add_technical_features  # noqa: E402
from research_weekly_surge_theme_segments import attach_theme_labels  # noqa: E402
from build_daily_candidate_model_layer import build_parameter_table, build_specs  # noqa: E402
from build_approved_operation_patterns import (  # noqa: E402
    NECKLINE_APPROVAL_METRICS,
    NECKLINE_OPERATION_MODULE_ID,
    W_BOTTOM_APPROVAL_METRICS,
    W_BOTTOM_OPERATION_MODULE_ID,
)
from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, now_text, write_csv  # noqa: E402


HISTORY_DIR = Path("output/history/research")
OUT_CSV = LATEST_DIR / "daily_model_parameter_research_latest.csv"
OUT_MD = LATEST_DIR / "daily_model_parameter_research_latest.md"
OUT_DETAIL_CSV = LATEST_DIR / "daily_model_parameter_research_horizon_detail_latest.csv"
OUT_DETAIL_MD = LATEST_DIR / "daily_model_parameter_research_horizon_detail_latest.md"
OUT_PARITY_CSV = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.csv"
OUT_PARITY_MD = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.md"
HISTORY_CSV = HISTORY_DIR / "daily_model_parameter_research.csv"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name
DOCS_DETAIL_CSV = DOCS_LATEST_DIR / OUT_DETAIL_CSV.name
DOCS_DETAIL_MD = DOCS_LATEST_DIR / OUT_DETAIL_MD.name
DOCS_PARITY_CSV = DOCS_LATEST_DIR / OUT_PARITY_CSV.name
DOCS_PARITY_MD = DOCS_LATEST_DIR / OUT_PARITY_MD.name

HORIZONS = list(range(1, 11)) + [20]
MIN_OK_SAMPLE = 100
MIN_REVIEW_SAMPLE = 30


@dataclass(frozen=True)
class RuleSpec:
    model_id: str
    model_name_zh: str
    parameter_set_id: str
    parameter_summary: str
    pdf_visibility: str
    condition: Callable[[pd.DataFrame], pd.Series]
    notes: str
    parameter_role: str = "parameter_variant"
    production_parity_status: str = "variant_not_baseline"
    parity_blocker: str = ""
    variant_of: str = ""


def pct(num: float) -> str:
    if math.isnan(num):
        return "-"
    return f"{num:.2f}%"


def sample_status(n: int) -> str:
    if n >= MIN_OK_SAMPLE:
        return "ok_first_pass"
    if n >= MIN_REVIEW_SAMPLE:
        return "small_sample_review_only"
    return "insufficient_sample"


def bool_series(df: pd.DataFrame, value: bool = False) -> pd.Series:
    return pd.Series(value, index=df.index)


def between(series: pd.Series, low: float, high: float) -> pd.Series:
    return (series >= low) & (series <= high)


def trueish(series: pd.Series) -> pd.Series:
    if series.dtype == bool:
        return series.fillna(False)
    return series.astype(str).str.lower().isin(["true", "1", "yes"])


def add_price_structure_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.sort_values(["stock_id", "date"]).copy()
    groups = out.groupby("stock_id", group_keys=False)

    out["ema23_prev5"] = groups["ema23"].shift(5)
    out["ema23_slope_5d_pct"] = (out["ema23"] / out["ema23_prev5"] - 1.0) * 100.0
    out["previous_close"] = groups["close"].shift(1)
    out["signal_return_1d_pct"] = (out["close"] / out["previous_close"] - 1.0) * 100.0
    out["close_above_open"] = out["close"] > out["open"]
    out["bullish_attack_candle"] = (out["close"] > out["open"]) | (
        out["close"].eq(out["open"]) & (out["close"] > out["previous_close"])
    )
    candle_range = (out["high"] - out["low"]).replace(0, pd.NA)
    out["body_ratio"] = (out["close"] - out["open"]).abs() / candle_range
    out["upper_shadow_ratio"] = (out["high"] - out[["close", "open"]].max(axis=1)) / candle_range
    out["close_location"] = (out["close"] - out["low"]) / candle_range
    out["solid_red_candle"] = (
        (out["close"] > out["open"])
        & (out["body_ratio"] >= 0.25)
        & (out["upper_shadow_ratio"] <= 0.35)
        & (out["close_location"] >= 0.65)
    )

    # build_stock_day_frame already calculates this with a per-stock previous
    # 20-day denominator. Keep the alias local to this research script so the
    # parameter rules read consistently.
    out["volume_ratio_prev20"] = out["start_day_volume_ratio_vs_prev20"]
    volume_ma20 = (
        groups["volume"]
        .shift(1)
        .rolling(20, min_periods=10)
        .mean()
        .reset_index(level=0, drop=True)
    )
    # Some sources store raw shares, others store lots. Normalize only clearly
    # share-denominated values so the liquidity rule remains stable.
    out["volume_ma20_lots"] = volume_ma20.where(volume_ma20 < 100000, volume_ma20 / 1000.0)

    for window in [10, 20, 23, 30, 60]:
        high = groups["high"].shift(1).rolling(window, min_periods=max(5, min(window, 20))).max().reset_index(level=0, drop=True)
        low = groups["low"].shift(1).rolling(window, min_periods=max(5, min(window, 20))).min().reset_index(level=0, drop=True)
        out[f"range_high_{window}d_prev"] = high
        out[f"range_low_{window}d_prev"] = low
        out[f"range_width_{window}d_pct"] = (high / low - 1.0) * 100.0
        out[f"range_breakout_{window}d_pct"] = (out["close"] / high - 1.0) * 100.0
        out[f"distance_to_range_high_{window}d_pct"] = (out["close"] / high - 1.0) * 100.0

    range_pct = (out["high"] - out["low"]) / out["previous_close"].replace(0, pd.NA) * 100.0
    out["locked_limit_up_breakout"] = (
        (out["range_breakout_20d_pct"] >= 2.0)
        & (out["signal_return_1d_pct"] >= 9.0)
        & (out["close"] >= out["high"] * 0.995)
        & (out["open"] >= out["close"] * 0.995)
        & ((out["high"] == out["low"]) | (range_pct <= 1.0))
    )

    # A simple W-bottom proxy for research: the latest 35 trading days contain two
    # similar lows and the second low is higher, while price is back in the upper half.
    low_35 = groups["low"].shift(1).rolling(35, min_periods=25).min().reset_index(level=0, drop=True)
    low_18 = groups["low"].shift(1).rolling(18, min_periods=12).min().reset_index(level=0, drop=True)
    high_35 = groups["high"].shift(1).rolling(35, min_periods=25).max().reset_index(level=0, drop=True)
    out["w_bottom_proxy"] = (
        (low_18 >= low_35 * 0.98)
        & (low_18 <= low_35 * 1.12)
        & (out["close"] >= (low_35 + high_35) / 2)
        & (out["ema23_slope_5d_pct"] > 0)
    )
    return out


def attach_tdcc_features(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    tdcc_dir = Path("data/tdcc_stock_history")
    for path in sorted(tdcc_dir.glob("*.csv")):
        try:
            t = pd.read_csv(path, dtype={"stock_id": str}, keep_default_na=False)
        except Exception:
            continue
        if t.empty or "as_of_date" not in t.columns or "stock_id" not in t.columns:
            continue
        t = t.copy()
        t["stock_id"] = t["stock_id"].astype(str).str.extract(r"(\d+)")[0].str.zfill(4)
        t["tdcc_as_of_date"] = t["as_of_date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
        keep = [
            "stock_id",
            "tdcc_as_of_date",
            "tdcc_consecutive_up_weeks",
            "all_thresholds_up",
            "high_thresholds_up",
            "four_thresholds_sync_up",
            "over_400_change_1w",
            "over_800_change_1w",
            "over_1000_change_1w",
        ]
        for col in keep:
            if col not in t.columns:
                t[col] = ""
        rows.append(t[keep])
    if not rows:
        out = df.copy()
        out["tdcc_history_available"] = False
        return out

    tdcc = pd.concat(rows, ignore_index=True)
    tdcc["tdcc_date_dt"] = pd.to_datetime(tdcc["tdcc_as_of_date"], format="%Y%m%d", errors="coerce")
    for col in ["tdcc_consecutive_up_weeks", "over_400_change_1w", "over_800_change_1w", "over_1000_change_1w"]:
        tdcc[col] = pd.to_numeric(tdcc[col], errors="coerce")
    for col in ["all_thresholds_up", "high_thresholds_up", "four_thresholds_sync_up"]:
        tdcc[col] = tdcc[col].astype(str).str.lower().isin(["true", "1", "yes"])

    left = df.copy()
    left["price_date_dt"] = pd.to_datetime(left["date"].astype(str), format="%Y%m%d", errors="coerce")
    merged_parts: list[pd.DataFrame] = []
    for stock_id, price_part in left.groupby("stock_id", sort=False):
        tdcc_part = tdcc[tdcc["stock_id"].eq(stock_id)].sort_values("tdcc_date_dt")
        if tdcc_part.empty:
            p = price_part.copy()
            p["tdcc_history_available"] = False
            merged_parts.append(p)
            continue
        merged = pd.merge_asof(
            price_part.sort_values("price_date_dt"),
            tdcc_part.drop(columns=["stock_id"]).sort_values("tdcc_date_dt"),
            left_on="price_date_dt",
            right_on="tdcc_date_dt",
            direction="backward",
        )
        merged["tdcc_history_available"] = merged["tdcc_as_of_date"].notna()
        merged_parts.append(merged)
    out = pd.concat(merged_parts, ignore_index=True)
    return out


def build_research_frame() -> pd.DataFrame:
    df = build_stock_day_frame()
    if df.empty:
        return df
    df = add_technical_features(df)
    df = add_price_structure_features(df)
    df = attach_theme_labels(df)
    df = attach_tdcc_features(df)
    return df


def support_retest_mask(d: pd.DataFrame, low_col: str = "range_low_20d_prev") -> pd.Series:
    return (
        (d[low_col] > 0)
        & (d["close"] >= d[low_col] * 0.98)
        & (d["close"] <= d[low_col] * 1.08)
    )


def current_volume_range_breakout_baseline(d: pd.DataFrame) -> pd.Series:
    normal_volume = (
        (d["volume_ratio_prev20"] >= 2.0)
        & (d["range_breakout_20d_pct"] >= 2.0)
        & (d["volume_ma20_lots"] >= 1000)
        & d["bullish_attack_candle"]
    )
    return normal_volume | d["locked_limit_up_breakout"]


def current_price_pullback_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        (between(d["distance_ema23_pct"], -2.5, 5.0) | support_retest_mask(d))
        & (d["ema23_slope_5d_pct"] > 0)
    )


def current_hot_theme_pullback_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        d["strict_theme_status_group"].isin({"mainstream_supported", "mainstream_overheated"})
        & (between(d["distance_ema23_pct"], -2.5, 5.0) | support_retest_mask(d))
    )


def active_price_attack_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        current_volume_range_breakout_baseline(d)
        | (d["volume_ratio_prev20"] >= 2.5)
        | (d["return_5d_pct"] >= 8)
        | (d["return_20d_pct"] >= 20)
    ).fillna(False)


def current_revenue_unreacted_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    # Historical revenue feature panels are not yet complete in this research
    # frame, so this can only mirror the production price-range and not-started
    # parts. The parity artifact must keep this row marked as proxy-only.
    return (
        (d["close"] >= d["range_low_23d_prev"] * 0.95)
        & (d["close"] <= d["range_high_23d_prev"] * 1.05)
        & (~active_price_attack_proxy(d))
    )


def current_w_bottom_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return d["w_bottom_proxy"] & (d["range_breakout_20d_pct"] < 2.0)


def current_w_bottom_approved_operation_baseline(d: pd.DataFrame) -> pd.Series:
    """Anchor W-bottom parity to the approved operation artifact.

    The production detector itself is row/context based and too expensive for
    the generic parameter-grid builder. The formal daily operation contract is
    the approved operation artifact, while raw candidate rows remain
    research-only.
    """
    return current_w_bottom_baseline_proxy(d)


def current_neckline_volume_breakout_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        d["w_bottom_proxy"]
        & (
            ((d["range_breakout_20d_pct"] >= 0.0) & (d["volume_ratio_prev20"] >= 2.0) & d["bullish_attack_candle"])
            | d["locked_limit_up_breakout"]
        )
    )


def current_neckline_approved_operation_baseline(d: pd.DataFrame) -> pd.Series:
    """Anchor neckline parity to the approved operation v1 artifact.

    The formal daily operation contract is the approved operation artifact.
    Raw research rows remain advisory-only; production scoring/entry rules are
    synchronized through the operation module and contract metadata.
    """
    return current_neckline_volume_breakout_baseline_proxy(d)


def current_near_high_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        between(d["near_60d_high_pct"], -5.0, 0.0)
        & (d["volume_ratio_prev20"] >= 1.2)
        & (d["ema23_slope_5d_pct"] > 0)
        & (d["range_breakout_20d_pct"] < 2.0)
    )


def current_platform_strengthening_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        (d["range_width_20d_pct"] <= 18)
        & between(d["distance_to_range_high_20d_pct"], -5.0, 1.5)
        & (d["volume_ratio_prev20"] >= 1.2)
        & d["solid_red_candle"]
        & (d["range_breakout_20d_pct"] < 2.0)
    )


def current_pullback_short_reclaim_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        (d["return_20d_pct"] >= 5)
        & (between(d["distance_ema23_pct"], -1.0, 6.0) | (d["close_above_ma20"] & (d["ema23_slope_5d_pct"] > 0)))
        & (d["ema23_slope_5d_pct"] > 0)
    )


def current_tdcc_stealth_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        trueish(d["tdcc_history_available"])
        & (
            (d["tdcc_consecutive_up_weeks"] >= 1)
            | trueish(d["all_thresholds_up"])
            | trueish(d["high_thresholds_up"])
        )
        & (d["volume_ratio_prev20"] < 2.5)
        & (d["return_5d_pct"] < 8)
        & (d["return_20d_pct"] < 20)
        & (d["close"] >= d["range_low_23d_prev"] * 0.90)
        & (d["close"] <= d["range_high_23d_prev"] * 1.10)
        & (~current_volume_range_breakout_baseline(d))
    )


def current_tdcc_short_term_continuation_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        trueish(d["tdcc_history_available"])
        & (
            trueish(d["all_thresholds_up"])
            | trueish(d["high_thresholds_up"])
            | trueish(d["four_thresholds_sync_up"])
        )
        & between(d["return_5d_pct"], 10, 30)
        & (trueish(d["macd_hist_gt0"]) | trueish(d["kd_bullish_not_overheated"]))
    )


def production_baseline_specs() -> list[RuleSpec]:
    return [
        RuleSpec(
            "volume_range_breakout",
            "放量攻擊模型",
            "production_current",
            "production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass",
            "pdf_core_model",
            current_volume_range_breakout_baseline,
            "Matches current production logic available in historical price fields, including locked-limit-up bypass without a volume-ratio gate.",
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "price_pullback_23ema",
            "股價回檔模型",
            "production_current_proxy",
            "production baseline proxy: near 23EMA/support + EMA23 slope proxy up",
            "pdf_core_model",
            current_price_pullback_baseline_proxy,
            "Production uses support/platform flags when available; research approximates support from historical 20d range low.",
            "production_baseline",
            "production_proxy",
            "support/platform entry flags are not fully backfilled in the historical research frame",
            "production_current",
        ),
        RuleSpec(
            "hot_theme_pullback",
            "熱門族群回檔模型",
            "production_current_proxy",
            "production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support",
            "pdf_core_model",
            current_hot_theme_pullback_baseline_proxy,
            "Production uses current model-layer hot theme labels; research uses strict historical no-lookahead theme state.",
            "production_baseline",
            "production_proxy",
            "daily hot-theme labels are not fully backfilled as point-in-time model-layer fields",
            "production_current",
        ),
        RuleSpec(
            "revenue_unreacted_range",
            "營收爆發但股價尚未反應模型",
            "production_current_proxy",
            "production baseline proxy: price still in 23d range and attack not started; revenue panel missing",
            "pdf_core_model",
            current_revenue_unreacted_baseline_proxy,
            "Revenue YoY/cumulative YoY history is not complete in this research frame, so this row is not production-parity.",
            "production_baseline",
            "proxy_only",
            "historical revenue panel is incomplete; strong_revenue gate cannot be replayed point-in-time",
            "production_current",
        ),
        RuleSpec(
            "w_bottom_right_side",
            "W底右側模型",
            W_BOTTOM_OPERATION_MODULE_ID,
            "approved operation baseline: right-low early entry, W-structure-low stop, D+20 gain10 else D+40 close exit",
            "pdf_core_model",
            current_w_bottom_approved_operation_baseline,
            (
                f"{W_BOTTOM_OPERATION_MODULE_ID} is the formal daily baseline through "
                "approved_operation_patterns_latest.csv; raw research candidate rows remain advisory-only."
            ),
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "neckline_volume_breakout_confirmation",
            "W底頸線帶量突破確認模型",
            NECKLINE_OPERATION_MODULE_ID,
            "approved operation baseline: W-bottom neckline signal, 45d non-bearish context, 90d score-only context, next-open entry and 20d operation-rule outcome",
            "pdf_core_model",
            current_neckline_approved_operation_baseline,
            (
                "W-bottom neckline volume breakout operation v1 is the formal daily baseline through "
                "approved_operation_patterns_latest.csv; other neckline subtypes remain outside this model."
            ),
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "pullback_short_reclaim",
            "回檔後短線轉強模型",
            "production_current_proxy",
            "production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up",
            "pdf_core_model",
            current_pullback_short_reclaim_baseline_proxy,
            "Production uses pullback/right-side/reclaim flags; research approximates with EMA and MA20 reclaim context.",
            "production_baseline",
            "production_proxy",
            "pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled",
            "production_current",
        ),
        RuleSpec(
            "tdcc_stealth_accumulation",
            "TDCC潛伏吸籌模型",
            "production_current_proxy",
            "production baseline proxy: TDCC positive, attack not started, low volume/return, still in range",
            "pdf_core_model",
            current_tdcc_stealth_baseline_proxy,
            "Production uses TDCC phase when available; research uses weekly TDCC history and range constraints.",
            "production_baseline",
            "production_proxy",
            "tdcc_price_phase is not fully available historically for every signal date",
            "production_current",
        ),
        RuleSpec(
            "tdcc_short_term_continuation_d5_d10",
            "TDCC短線延續模型 D+5/D+10",
            "production_current_proxy",
            "production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD",
            "pdf_core_model",
            current_tdcc_short_term_continuation_baseline_proxy,
            "This mirrors the daily specialty short-term continuation surface enough to serve as baseline before deeper grid variants.",
            "production_baseline",
            "production_proxy",
            "daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies",
            "production_current",
        ),
    ]


def rule_specs() -> list[RuleSpec]:
    specs: list[RuleSpec] = production_baseline_specs()

    for breakout_pct in [1.0, 2.0, 3.0]:
        for vol in [2.0, 3.0, 5.0]:
            for min_lots in [500, 1000, 2000]:
                specs.append(
                    RuleSpec(
                        "volume_range_breakout",
                        "放量攻擊模型",
                        f"prior20x{1 + breakout_pct / 100:.2f}_vol{vol:g}_minvol{min_lots}",
                        f"收盤突破前20日高點 {breakout_pct:g}% + 量比 >= {vol:g} + 20日均量 >= {min_lots}張 + 實體紅K",
                        "pdf_core_model",
                        lambda d, breakout_pct=breakout_pct, vol=vol, min_lots=min_lots: (
                            (d["volume_ratio_prev20"] >= vol)
                            & (d["range_breakout_20d_pct"] >= breakout_pct)
                            & (d["volume_ma20_lots"] >= min_lots)
                            & d["bullish_attack_candle"]
                        ),
                        "主條件是前20日高點突破、量能放大、流動性與實體紅K。漲幅、過熱、均線與60日高點不作為此模型否決條件。",
                    )
                )
    specs.append(
        RuleSpec(
            "volume_range_breakout",
            "放量攻擊模型",
            "locked_limit_up_breakout_no_volume_gate",
            "鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量",
            "pdf_core_model",
            lambda d: d["locked_limit_up_breakout"],
            "這是現行放量攻擊模型的鎖量漲停旁路；不是全面降低一般突破的量比門檻。",
        )
    )

    for low, high in [(-1.5, 3.0), (-2.5, 5.0), (-4.0, 7.0)]:
        for vol_max in [1.0, 1.2, 1.5]:
            specs.append(
                RuleSpec(
                    "price_pullback_23ema",
                    "股價回檔模型",
                    f"ema{low:g}_{high:g}_volmax{vol_max:g}",
                    f"距 23EMA {low:g}% 至 {high:g}% + 23EMA 向上 + 量比 <= {vol_max:g}",
                    "research_only_not_pdf_core",
                    lambda d, low=low, high=high, vol_max=vol_max: (
                        between(d["distance_ema23_pct"], low, high)
                        & (d["ema23_slope_5d_pct"] > 0)
                        & (d["volume_ratio_prev20"] <= vol_max)
                    ),
                    "回檔模型不要求突破；主軸是結構支撐與量縮回檔。",
                )
            )

    hot_theme_groups = {
        "strict_mainstream_any": {"mainstream_supported", "mainstream_overheated"},
        "strict_mainstream_supported": {"mainstream_supported"},
        "strict_mainstream_overheated": {"mainstream_overheated"},
    }
    for group_id, groups in hot_theme_groups.items():
        for low, high, support_high in [(-2.5, 5.0, 8.0), (-4.0, 7.0, 10.0)]:
            specs.append(
                RuleSpec(
                    "hot_theme_pullback",
                    "熱門族群回檔模型",
                    f"{group_id}_ema{low:g}_{high:g}_support{support_high:g}",
                    f"歷史熱門/主流族群狀態 {group_id} + 距 23EMA {low:g}% 至 {high:g}% 或接近20日支撐 {support_high:g}% 內",
                    "pdf_core_model",
                    lambda d, groups=groups, low=low, high=high, support_high=support_high: (
                        d["strict_theme_status_group"].isin(groups)
                        & (
                            between(d["distance_ema23_pct"], low, high)
                            | (
                                (d["range_low_20d_prev"] > 0)
                                & (d["close"] >= d["range_low_20d_prev"] * 0.98)
                                & (d["close"] <= d["range_low_20d_prev"] * (1 + support_high / 100))
                            )
                        )
                    ),
                    "使用 strict no-lookahead 歷史族群狀態近似每日熱門族群標籤；營收不作為必要條件。",
                )
            )

    for tolerance in [5, 10]:
        specs.append(
            RuleSpec(
                "revenue_unreacted_range",
                "營收爆發但股價尚未反應模型",
                f"range23_tol{tolerance}",
                f"股價位於 23 日區間上下 {tolerance}% 內；營收確認由每日模型層欄位提供",
                "pdf_core_model",
                lambda d, tolerance=tolerance: (
                    (d["close"] >= d["range_low_23d_prev"] * (1 - tolerance / 100))
                    & (d["close"] <= d["range_high_23d_prev"] * (1 + tolerance / 100))
                    & (d["range_width_23d_pct"] <= 20)
                ),
                "歷史營收 feature panel 尚未完整，這裡先用價格未反應區間作第一版近似條件。",
            )
        )

    for vol in [1.0, 1.2, 1.5]:
        specs.append(
            RuleSpec(
                "w_bottom_right_side",
                "W底右側模型",
                f"wproxy_vol{vol:g}",
                f"W底近似條件 + 右側結構墊高 + 量比 >= {vol:g}",
                "pdf_core_model",
                lambda d, vol=vol: d["w_bottom_proxy"] & (d["volume_ratio_prev20"] >= vol),
                "W底右側研究近似條件；正式升級仍需要圖形品質確認。",
            )
        )

    for dist in [3, 5]:
        for vol in [1.2, 1.5]:
            specs.append(
                RuleSpec(
                    "near_high_neckline_challenge",
                    "接近前高 / 頸線挑戰模型",
                    f"near{dist}_vol{vol:g}",
                    f"距 60 日高點下方 {dist}% 內 + 量比 >= {vol:g} + 23EMA 向上",
                    "research_only_not_pdf_core",
                    lambda d, dist=dist, vol=vol: (
                        between(d["near_60d_high_pct"], -dist, 0)
                        & (d["volume_ratio_prev20"] >= vol)
                        & (d["ema23_slope_5d_pct"] > 0)
                    ),
                    "用來提前 1 到 5 個交易日觀察突破前壓力挑戰；不是嚴格突破模型。",
                )
            )

    for window in [20, 30]:
        for near in [3, 5]:
            for vol in [1.2, 1.5]:
                specs.append(
                    RuleSpec(
                        "platform_strengthening",
                        "平台整理轉強模型",
                        f"w{window}_near{near}_vol{vol:g}",
                        f"{window}日區間寬度 <= 18% + 距區間上緣 {near}% 內 + 量比 >= {vol:g} + 實體紅K",
                        "research_only_not_pdf_core",
                        lambda d, window=window, near=near, vol=vol: (
                            (d[f"range_width_{window}d_pct"] <= 18)
                            & between(d[f"distance_to_range_high_{window}d_pct"], -near, 1.5)
                            & (d["volume_ratio_prev20"] >= vol)
                            & d["solid_red_candle"]
                        ),
                        "平台模型尋找波動收斂後、接近上緣時量能回升的型態。",
                    )
                )

    for vol in [1.0, 1.2, 1.5]:
        specs.append(
            RuleSpec(
                "pullback_short_reclaim",
                "回檔後短線轉強模型",
                f"prior20up_reclaim_vol{vol:g}",
                f"前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= {vol:g}",
                "pdf_core_model",
                lambda d, vol=vol: (
                    (d["return_20d_pct"] >= 10)
                    & between(d["distance_ema23_pct"], -1, 6)
                    & trueish(d["macd_hist_gt0"])
                    & (d["volume_ratio_prev20"] >= vol)
                ),
                "尋找前段上漲後回檔未破結構、並重新恢復短線動能的股票。",
            )
        )

    for consecutive in [1, 2, 3]:
        specs.append(
            RuleSpec(
                "tdcc_stealth_accumulation",
                "TDCC潛伏吸籌模型",
                f"tdcc_up{consecutive}_range10",
                f"TDCC 連續增加週數 >= {consecutive} + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20%",
                "pdf_core_model",
                lambda d, consecutive=consecutive: (
                    trueish(d["tdcc_history_available"])
                    & (d["tdcc_consecutive_up_weeks"] >= consecutive)
                    & (d["close"] >= d["range_low_23d_prev"] * 0.90)
                    & (d["close"] <= d["range_high_23d_prev"] * 1.10)
                    & (d["return_20d_pct"] <= 20)
                ),
                "目前使用本地 TDCC 歷史資料；完整歷史 phase panel 可用後再升級 phase 篩選。",
            )
        )

    specs.extend(
        [
            RuleSpec(
                "tdcc_short_term_continuation_d5_d10",
                "TDCC短線延續模型 D+5/D+10",
                "all_thresholds_up_ret5_10_30_macd",
                "四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0",
                "pdf_core_model",
                lambda d: (
                    trueish(d["tdcc_history_available"])
                    & trueish(d["all_thresholds_up"])
                    & between(d["return_5d_pct"], 10, 30)
                    & trueish(d["macd_hist_gt0"])
                ),
                "短線延續專項，不是低位吸籌模型。",
            ),
            RuleSpec(
                "tdcc_short_term_continuation_d5_d10",
                "TDCC短線延續模型 D+5/D+10",
                "high_thresholds_ret5_10_30_ret10_20_50_kd",
                "高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱",
                "pdf_core_model",
                lambda d: (
                    trueish(d["tdcc_history_available"])
                    & trueish(d["high_thresholds_up"])
                    & between(d["return_5d_pct"], 10, 30)
                    & between(d["return_10d_pct"], 20, 50)
                    & trueish(d["kd_bullish_not_overheated"])
                ),
                "短線延續研究；報酬統計使用訊號日隔天開盤到 D+1 至 D+10。",
            ),
            RuleSpec(
                "short_term_surge_d5_d10",
                "短線急漲 D+5/D+10 研究",
                "ret5_10_30_vol5_ge1_5_macd",
                "5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0",
                "research_only_not_pdf_core",
                lambda d: (
                    between(d["return_5d_pct"], 10, 30)
                    & (d["start_5d_avg_volume_ratio_vs_prev20"] >= 1.5)
                    & trueish(d["macd_hist_gt0"])
                ),
                "動能研究名單；進場假設必須使用訊號日後下一交易日開盤。",
            ),
        ]
    )

    for vol in [3.0, 5.0, 10.0]:
        specs.append(
            RuleSpec(
                "explosive_volume_red_candle",
                "爆天量紅K研究",
                f"vol{vol:g}_solid_red",
                f"量比 >= {vol:g} + 實體紅K + 上影線小 + 收盤接近日高",
                "research_only_not_pdf_core",
                lambda d, vol=vol: (d["volume_ratio_prev20"] >= vol) & d["solid_red_candle"],
                "研究用模型，參數驗證成熟前不納入核心 PDF 推薦模型。",
            )
        )

    return specs

def summarize_rule(df: pd.DataFrame, spec: RuleSpec) -> tuple[dict[str, object], list[dict[str, object]]]:
    mask = spec.condition(df).fillna(False)
    picked = df[mask].copy()
    n = len(picked)
    unique_stocks = picked["stock_id"].nunique() if n else 0
    detail_rows: list[dict[str, object]] = []
    best_horizon = ""
    best_avg = -math.inf
    best_win = 0.0
    for h in HORIZONS:
        close_col = f"next_open_to_d{h}_close_return_pct"
        high_col = f"next_open_to_d{h}_high_return_pct"
        if close_col not in picked.columns:
            continue
        valid = picked.dropna(subset=[close_col])
        mature = len(valid)
        win = float((valid[close_col] > 0).mean() * 100.0) if mature else math.nan
        avg = float(valid[close_col].mean()) if mature else math.nan
        med = float(valid[close_col].median()) if mature else math.nan
        high_avg = float(valid[high_col].mean()) if mature and high_col in valid.columns else math.nan
        high_win_5 = float((valid[high_col] >= 5).mean() * 100.0) if mature and high_col in valid.columns else math.nan
        if mature and not math.isnan(avg) and avg > best_avg and h <= 10:
            best_avg = avg
            best_horizon = f"D+{h}"
            best_win = win
        detail_rows.append(
            {
                "model_id": spec.model_id,
                "model_name_zh": spec.model_name_zh,
                "parameter_set_id": spec.parameter_set_id,
                "horizon": f"D+{h}",
                "entry_basis": "signal_date_next_open",
                "exit_close_basis": f"D+{h}_close",
                "exit_high_basis": f"D+{h}_intraday_high",
                "mature_count": mature,
                "close_win_rate_pct": round(win, 2) if not math.isnan(win) else "",
                "avg_close_return_pct": round(avg, 2) if not math.isnan(avg) else "",
                "median_close_return_pct": round(med, 2) if not math.isnan(med) else "",
                "avg_high_return_pct": round(high_avg, 2) if not math.isnan(high_avg) else "",
                "high_5pct_hit_rate_pct": round(high_win_5, 2) if not math.isnan(high_win_5) else "",
            }
        )

    summary = {
        "generated_at": now_text(),
        "model_id": spec.model_id,
        "model_name_zh": spec.model_name_zh,
        "parameter_set_id": spec.parameter_set_id,
        "parameter_summary": spec.parameter_summary,
        "parameter_role": spec.parameter_role,
        "production_parity_status": spec.production_parity_status,
        "parity_blocker": spec.parity_blocker,
        "variant_of": spec.variant_of,
        "pdf_visibility": spec.pdf_visibility,
        "entry_basis": "signal_date_next_open",
        "selected_stock_days": n,
        "selected_unique_stocks": unique_stocks,
        "best_close_horizon_d1_d10": best_horizon,
        "best_close_win_rate_pct": round(best_win, 2) if best_horizon else "",
        "best_avg_close_return_pct": round(best_avg, 2) if best_horizon else "",
        "sample_status": sample_status(n),
        "apply_status": "candidate_parameter_review" if n >= MIN_REVIEW_SAMPLE else "do_not_apply_insufficient_sample",
        "notes": spec.notes,
    }
    for h in [1, 2, 3, 5, 10, 20]:
        row = next((r for r in detail_rows if r["horizon"] == f"D+{h}"), None)
        summary[f"d{h}_mature_count"] = row["mature_count"] if row else 0
        summary[f"d{h}_close_win_rate_pct"] = row["close_win_rate_pct"] if row else ""
        summary[f"d{h}_avg_close_return_pct"] = row["avg_close_return_pct"] if row else ""
        summary[f"d{h}_avg_high_return_pct"] = row["avg_high_return_pct"] if row else ""
    return summary, detail_rows


def current_production_core_models() -> pd.DataFrame:
    current = build_parameter_table(build_specs()).copy()
    current = current[current["pdf_visibility"].eq("pdf_core_model")].copy()
    return current.drop_duplicates("model_id", keep="first").reset_index(drop=True)


def build_model_parity(summary: pd.DataFrame) -> pd.DataFrame:
    production = current_production_core_models()
    baseline = summary[summary["parameter_role"].eq("production_baseline")].copy()
    rows: list[dict[str, object]] = []
    for _, prod in production.iterrows():
        model_id = str(prod.get("model_id", ""))
        base_rows = baseline[baseline["model_id"].eq(model_id)].copy()
        variant_rows = summary[
            summary["model_id"].eq(model_id) & ~summary["parameter_role"].eq("production_baseline")
        ].copy()
        if base_rows.empty:
            status = "missing_production_baseline"
            baseline_ids = ""
            blockers = "research rule_specs() has no production_baseline row for this production core model"
            selected_days = ""
            unique_stocks = ""
        else:
            statuses = sorted(set(base_rows["production_parity_status"].astype(str)))
            if statuses == ["production_parity"]:
                status = "production_parity"
            elif "proxy_only" in statuses:
                status = "proxy_only"
            else:
                status = "production_proxy"
            baseline_ids = ",".join(base_rows["parameter_set_id"].astype(str))
            blockers = "; ".join(
                sorted(
                    {
                        str(value).strip()
                        for value in base_rows["parity_blocker"].fillna("")
                        if str(value).strip()
                    }
                )
            )
            if model_id == "w_bottom_right_side" and status == "production_parity":
                selected_days = int(W_BOTTOM_APPROVAL_METRICS["sample_size"])
                unique_stocks = int(W_BOTTOM_APPROVAL_METRICS["unique_stock_count"])
            elif model_id == "neckline_volume_breakout_confirmation" and status == "production_parity":
                selected_days = int(NECKLINE_APPROVAL_METRICS["tradable_entry_count"])
                unique_stocks = int(NECKLINE_APPROVAL_METRICS["unique_stock_count"])
            else:
                selected_days = int(pd.to_numeric(base_rows["selected_stock_days"], errors="coerce").fillna(0).sum())
                unique_stocks = int(pd.to_numeric(base_rows["selected_unique_stocks"], errors="coerce").fillna(0).max())
        rows.append(
            {
                "generated_at": now_text(),
                "model_id": model_id,
                "model_name_zh": prod.get("model_name_zh", ""),
                "production_pdf_visibility": prod.get("pdf_visibility", ""),
                "production_parameter_status": prod.get("parameter_status", ""),
                "production_main_conditions": prod.get("main_conditions", ""),
                "research_baseline_status": status,
                "research_baseline_parameter_set_id": baseline_ids,
                "research_variant_count": len(variant_rows),
                "baseline_selected_stock_days": selected_days,
                "baseline_selected_unique_stocks": unique_stocks,
                "parity_blocker": blockers,
                "completion_rule": (
                    "usable_as_exact_baseline"
                    if status == "production_parity"
                    else "usable_for_relative_research_only_until_blocker_resolved"
                ),
            }
        )
    return pd.DataFrame(rows)


def write_model_parity(parity: pd.DataFrame) -> None:
    write_csv(parity, OUT_PARITY_CSV)
    write_csv(parity, DOCS_PARITY_CSV)
    counts = (
        parity["research_baseline_status"].value_counts().reset_index()
        if not parity.empty
        else pd.DataFrame(columns=["research_baseline_status", "count"])
    )
    if not counts.empty:
        counts.columns = ["research_baseline_status", "count"]
    lines = [
        "# Daily Model Research Baseline Parity",
        "",
        f"- generated_at: `{now_text()}`",
        "- purpose: verify that every daily production core model has a research production-baseline row before parameter variants are compared",
        "- production_parity: historical research fields can replay the production baseline directly",
        "- production_proxy / proxy_only: baseline exists, but one or more production fields are not fully available point-in-time in the research frame",
        "- rule: variants must compare against the production_baseline row of the same model_id; proxy rows cannot be promoted without resolving blockers",
        "",
        "## Status Summary",
        "",
        markdown_table(counts, counts.columns.tolist()) if not counts.empty else "No parity rows.",
        "",
        "## Model Parity Detail",
        "",
        markdown_table(
            parity,
            [
                "model_id",
                "research_baseline_status",
                "research_baseline_parameter_set_id",
                "research_variant_count",
                "baseline_selected_stock_days",
                "baseline_selected_unique_stocks",
                "parity_blocker",
                "completion_rule",
            ],
            limit=80,
        ),
    ]
    OUT_PARITY_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PARITY_MD.write_text(OUT_PARITY_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, coverage: dict[str, object]) -> None:
    summary_sorted = summary.sort_values(
        ["model_id", "sample_status", "best_avg_close_return_pct"],
        ascending=[True, True, False],
    ).reset_index(drop=True)
    review = summary_sorted[summary_sorted["selected_stock_days"] >= MIN_REVIEW_SAMPLE].copy()
    top = review.sort_values(["best_avg_close_return_pct", "selected_stock_days"], ascending=[False, False]).head(30)
    lines = [
        "# Daily Model Parameter Research",
        "",
        f"- generated_at: `{now_text()}`",
        f"- price_history_files: `{coverage.get('price_history_files')}`",
        f"- max_price_rows: `{coverage.get('max_price_rows')}`",
        f"- data_range: `{coverage.get('date_min')}` ~ `{coverage.get('date_max')}`",
        "- entry_basis: `signal_date_next_open`",
        "- close_return_definition: `(D+n close / next trading day open - 1)`",
        "- high_return_definition: `(max intraday high through D+n / next trading day open - 1)`",
        "",
        "## Data Quality",
        "",
        "- This is first-pass parameter research using the current repo price history.",
        "- If sample_status is `small_sample_review_only` or `insufficient_sample`, do not treat the parameter as a final model weight.",
        "- Revenue historical panel is not complete in price history, so the revenue-unreacted research row only validates the price-range component.",
        "",
        "## Top Parameter Sets By Avg Close Return",
        "",
        markdown_table(
            top,
            [
                "model_id",
                "parameter_set_id",
                "parameter_role",
                "production_parity_status",
                "selected_stock_days",
                "selected_unique_stocks",
                "best_close_horizon_d1_d10",
                "best_close_win_rate_pct",
                "best_avg_close_return_pct",
                "sample_status",
                "parameter_summary",
            ],
            limit=30,
        ),
        "",
        "## All Model Parameter Summary",
        "",
        markdown_table(
            summary_sorted,
            [
                "model_id",
                "parameter_set_id",
                "parameter_role",
                "production_parity_status",
                "selected_stock_days",
                "d1_close_win_rate_pct",
                "d3_close_win_rate_pct",
                "d5_close_win_rate_pct",
                "d10_close_win_rate_pct",
                "d5_avg_close_return_pct",
                "d10_avg_close_return_pct",
                "sample_status",
                "parameter_summary",
            ],
            limit=200,
        ),
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_MD.write_text(OUT_MD.read_text(encoding="utf-8"), encoding="utf-8")

    focus = detail[detail["horizon"].isin(["D+1", "D+2", "D+3", "D+4", "D+5", "D+6", "D+7", "D+8", "D+9", "D+10"])].copy()
    lines2 = [
        "# Daily Model Parameter Research - Horizon Detail",
        "",
        f"- generated_at: `{now_text()}`",
        "- entry_basis: `signal_date_next_open`",
        "",
        markdown_table(
            focus,
            [
                "model_id",
                "parameter_set_id",
                "horizon",
                "mature_count",
                "close_win_rate_pct",
                "avg_close_return_pct",
                "median_close_return_pct",
                "avg_high_return_pct",
                "high_5pct_hit_rate_pct",
            ],
            limit=300,
        ),
    ]
    OUT_DETAIL_MD.write_text("\n".join(lines2) + "\n", encoding="utf-8")
    DOCS_DETAIL_MD.write_text(OUT_DETAIL_MD.read_text(encoding="utf-8"), encoding="utf-8")


def coverage_stats() -> dict[str, object]:
    rows = []
    for path in Path("data/stock_price_history").glob("*.csv"):
        try:
            df = pd.read_csv(path, usecols=["date"])
        except Exception:
            continue
        if df.empty:
            continue
        rows.append((len(df), str(df["date"].min()), str(df["date"].max())))
    if not rows:
        return {"price_history_files": 0, "max_price_rows": 0, "date_min": "", "date_max": ""}
    return {
        "price_history_files": len(rows),
        "max_price_rows": max(r[0] for r in rows),
        "date_min": min(r[1] for r in rows),
        "date_max": max(r[2] for r in rows),
    }


def main() -> int:
    df = build_research_frame()
    if df.empty:
        raise RuntimeError("No price history available for model parameter research")

    summaries: list[dict[str, object]] = []
    details: list[dict[str, object]] = []
    for spec in rule_specs():
        summary, detail_rows = summarize_rule(df, spec)
        summaries.append(summary)
        details.extend(detail_rows)

    summary_df = pd.DataFrame(summaries)
    detail_df = pd.DataFrame(details)
    coverage = coverage_stats()
    parity_df = build_model_parity(summary_df)

    write_csv(summary_df, OUT_CSV)
    write_csv(detail_df, OUT_DETAIL_CSV)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(summary_df, HISTORY_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(summary_df, DOCS_CSV)
    write_csv(detail_df, DOCS_DETAIL_CSV)
    write_markdown(summary_df, detail_df, coverage)
    write_model_parity(parity_df)

    print(f"Saved {OUT_CSV} rows={len(summary_df)}")
    print(f"Saved {OUT_DETAIL_CSV} rows={len(detail_df)}")
    print(f"Saved {OUT_PARITY_CSV} rows={len(parity_df)}")
    print(f"Saved {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

