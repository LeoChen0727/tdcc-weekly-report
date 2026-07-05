from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, markdown_table, now_text, read_csv, safe_str, to_number, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "volume_range_breakout"
OPERATION_MODULE_ID = "volume_breakout_confirmed_operation_v1"
APPROVAL_VERSION = "volume_breakout_operation_v1_20260615"
SOURCE_RESEARCH_ID = "volume_breakout_confirmed_operation"
ENTRY_RULE_ID = "confirmation_next_open"
STOP_LOSS_RULE_ID = "signal_low_stop"
EXIT_RULE_ID = "signal_low_stop_or_fixed_10d_close"
BUY_FILTER_ID = "positive_evidence_oos_rank_v1"

APPROVED_VOLUME_EVIDENCE_DIR = ROOT / "config" / "approved_operation_evidence"
CONFIRMED_SUMMARY_CSV = APPROVED_VOLUME_EVIDENCE_DIR / "volume_breakout_operation_v1_20260615_formal_operation_backtest.csv"
CONFIRMED_RANK_CSV = APPROVED_VOLUME_EVIDENCE_DIR / "volume_breakout_operation_v1_20260615_rank.csv"
OUT_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"
OUT_MD = LATEST_DIR / "approved_operation_patterns_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name

MIN_SAMPLE_SIZE = 10
MIN_WIN_RATE = 50.0
MIN_MEDIAN_RETURN = 0.0
MIN_RESEARCH_SCORE = 0.0

W_BOTTOM_MODEL_ID = "w_bottom_right_side"
W_BOTTOM_OPERATION_MODULE_ID = "w_bottom_early_entry_operation_v2"
W_BOTTOM_APPROVAL_VERSION = "w_bottom_early_entry_operation_v2_20260629"
W_BOTTOM_APPROVAL_STATUS = "approved_for_daily_v2"
W_BOTTOM_SOURCE_RESEARCH_ID = "w_bottom_early_entry_stop_loss_audit"
W_BOTTOM_ENTRY_RULE_ID = "right_low_signal_next_open"
W_BOTTOM_STOP_LOSS_RULE_ID = "w_structure_low_close_stop"
W_BOTTOM_EXIT_RULE_ID = "d20_gain10_else_d40_close"
W_BOTTOM_BUY_FILTER_ID = "smooth_core_mainstream_right_rebound_5_20_bull"
W_BOTTOM_SPEC_SOURCE = Path("docs/specs/w_bottom_right_side_early_entry_operation_spec.md")
W_BOTTOM_MIN_MATURE_SAMPLE_SIZE = 30
W_BOTTOM_MIN_POSITIVE_RETURN_RATE = 55.0

NECKLINE_MODEL_ID = "neckline_volume_breakout_confirmation"
NECKLINE_OPERATION_MODULE_ID = "neckline_strict_45_signal_90_score_v1"
NECKLINE_APPROVAL_VERSION = "neckline_strict_45_signal_90_score_v1_20260629"
NECKLINE_SOURCE_RESEARCH_ID = "neckline_strict_45_signal_90_score_operation_candidate"
NECKLINE_ENTRY_RULE_ID = "close_ge_1pct_within_3_sessions_next_open"
NECKLINE_STOP_LOSS_RULE_ID = "no_fixed_stop_loss_20d_operation_rule"
NECKLINE_EXIT_RULE_ID = "tp10_close_win_5pct_pullback_neutral_else_20d_close_loss"
NECKLINE_BUY_FILTER_ID = "broad_45_non_bearish_with_90_warning"
NECKLINE_SPEC_SOURCE = Path("docs/specs/neckline_volume_breakout_confirmation_model_change_spec.md")
NECKLINE_MIN_MATURE_SAMPLE_SIZE = 30
NECKLINE_MIN_PURE_WIN_RATE = 60.0
NECKLINE_MIN_NEUTRAL_INCLUSIVE_SUCCESS_RATE = 70.0

PRICE_PULLBACK_MODEL_ID = "price_pullback_23ema"
PRICE_PULLBACK_OPERATION_MODULE_ID = "price_pullback_23ema_prev20_breakout_stop_v1"
PRICE_PULLBACK_APPROVAL_VERSION = "price_pullback_23ema_operation_v1_20260703"
PRICE_PULLBACK_SOURCE_RESEARCH_ID = "price_pullback_23ema_promotion_matrix"
PRICE_PULLBACK_ENTRY_RULE_ID = "signal_date_next_open"
PRICE_PULLBACK_STOP_LOSS_RULE_ID = "sustained_close_below_lower_ma20_ema23_4pct_4d"
PRICE_PULLBACK_EXIT_RULE_ID = "close_prev20_high_break_next_open"
PRICE_PULLBACK_BUY_FILTER_ID = "v1_gate_return20_tdcc_high_obv"
PRICE_PULLBACK_SPEC_SOURCE = Path("docs/specs/price_pullback_23ema_operation_candidate_spec.md")
PRICE_PULLBACK_MIN_MATURE_SAMPLE_SIZE = 1000
PRICE_PULLBACK_MIN_WIN_RATE = 60.0

PRICE_PULLBACK_APPROVAL_METRICS = {
    "surface_id": "price_pullback_23ema_v1",
    "selected_segment_id": PRICE_PULLBACK_BUY_FILTER_ID,
    "mature_sample_size": "1160",
    "accepted_trade_count": "1160",
    "win_count": "766",
    "neutral_count": "65",
    "failure_count": "329",
    "hard_stop_rate_pct": "9.14",
    "win_rate_pct": "66.03",
    "neutral_rate_pct": "5.60",
    "failure_rate_pct": "28.36",
    "avg_return_pct": "2.90",
    "technical_package_sample_size": "654",
    "technical_package_win_rate_pct": "75.54",
    "technical_package_neutral_rate_pct": "3.52",
    "technical_package_failure_rate_pct": "20.95",
    "technical_package_avg_return_pct": "2.96",
}

W_BOTTOM_APPROVAL_METRICS = {
    "surface_id": "w_bottom_right_low_early_entry",
    "selected_segment_id": W_BOTTOM_BUY_FILTER_ID,
    "sample_size": "44",
    "evaluated_sample_size": "31",
    "mature_sample_size": "31",
    "win_count": "18",
    "neutral_count": "0",
    "loss_count": "13",
    "incomplete_count": "13",
    "stop_count": "10",
    "positive_return_rate_pct": "58.0645",
    "neutral_inclusive_success_rate_pct": "58.0645",
    "avg_return_pct": "11.2532",
    "median_return_pct": "6.2374",
    "min_return_pct": "-12.7202",
    "unique_stock_count": "44",
}

NECKLINE_APPROVAL_METRICS = {
    "surface_id": "neckline_volume_breakout_confirmation",
    "selected_segment_id": "low_position_le60_market_bull",
    "source_candidate_count": "87",
    "confirmation_candidate_count": "51",
    "tradable_entry_count": "51",
    "incomplete_count": "0",
    "filter90_auto_bearish_source_count": "39",
    "filter90_auto_bearish_confirmed_count": "19",
    "score_adjustment_avg_points": "1.8627",
    "win_count": "23",
    "neutral_count": "15",
    "loss_count": "13",
    "pure_win_rate_pct": "63.8889",
    "neutral_inclusive_success_rate_pct": "74.5098",
    "avg_return_pct": "4.3784",
    "median_return_pct": "4.4597",
    "avg_max_close_return_pct": "8.5713",
    "avg_min_close_return_pct": "-6.2885",
    "unique_stock_count": "51",
}


def true_text(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "1.0", "yes", "y"}


def positive_rank_rows(rank: pd.DataFrame) -> pd.DataFrame:
    if rank.empty:
        return rank.copy()
    out = rank.copy()
    sample = out.get("evidence_sample_size", pd.Series(dtype=str)).map(to_number)
    win = out.get("evidence_win_rate", pd.Series(dtype=str)).map(to_number)
    median = out.get("evidence_median_return", pd.Series(dtype=str)).map(to_number)
    score = out.get("ranking_research_score", pd.Series(dtype=str)).map(to_number)
    oos = out.get("evidence_out_of_sample_pass", pd.Series(dtype=str)).map(true_text)
    return out[
        sample.ge(MIN_SAMPLE_SIZE)
        & win.ge(MIN_WIN_RATE)
        & median.gt(MIN_MEDIAN_RETURN)
        & score.gt(MIN_RESEARCH_SCORE)
        & oos
    ].copy()


def best_evidence(summary: pd.DataFrame) -> pd.Series | None:
    if summary.empty:
        return None
    out = summary.copy()
    for col in ["sample_size", "win_rate", "median_return", "ranking_research_score"]:
        out[col] = pd.to_numeric(out.get(col), errors="coerce")
    eligible = out[
        out["sample_size"].ge(MIN_SAMPLE_SIZE)
        & out["win_rate"].ge(MIN_WIN_RATE)
        & out["median_return"].gt(MIN_MEDIAN_RETURN)
        & out["ranking_research_score"].gt(MIN_RESEARCH_SCORE)
        & out.get("out_of_sample_pass", pd.Series(dtype=str)).map(true_text)
    ].copy()
    if eligible.empty:
        return None
    eligible["_confidence_order"] = eligible.get("confidence_status", "").map({"high": 0, "medium": 1, "low": 2}).fillna(9)
    return eligible.sort_values(
        ["_confidence_order", "ranking_research_score", "sample_size"],
        ascending=[True, False, False],
    ).iloc[0]


def approval_row(summary: pd.DataFrame, rank: pd.DataFrame, generated_at: str) -> dict[str, Any]:
    positive = positive_rank_rows(rank)
    selected = best_evidence(summary)
    if selected is None:
        raise RuntimeError("volume breakout approval evidence has no eligible best evidence row")
    return {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "operation_module_id": OPERATION_MODULE_ID,
        "approval_version": APPROVAL_VERSION,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": SOURCE_RESEARCH_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "entry_rule_zh": "確認日收盤後列入，下一個交易日開盤價進場。",
        "stop_loss_rule_id": STOP_LOSS_RULE_ID,
        "stop_loss_rule_zh": "跌破訊號日期最低價停損。",
        "exit_rule_id": EXIT_RULE_ID,
        "exit_rule_zh": "先跌破停損基準出場，否則持有 10 個交易日收盤出場。",
        "buy_filter_id": BUY_FILTER_ID,
        "buy_filter_zh": (
            "正式買進排名只採用 evidence_sample_size>=10、evidence_win_rate>=50、"
            "evidence_median_return>0、evidence_out_of_sample_pass=True、ranking_research_score>0 的 confirmed rows。"
        ),
        "pending_rule_zh": "未確認股票只列入待確認；不得列買進價，確認後才啟動進場與出場規則。",
        "min_sample_size": MIN_SAMPLE_SIZE,
        "min_win_rate": MIN_WIN_RATE,
        "min_median_return": MIN_MEDIAN_RETURN,
        "require_out_of_sample_pass": "True",
        "min_research_score": MIN_RESEARCH_SCORE,
        "evidence_summary_source": CONFIRMED_SUMMARY_CSV.name,
        "evidence_rank_source": CONFIRMED_RANK_CSV.name,
        "evidence_total_rank_rows": len(rank),
        "evidence_positive_rank_rows": len(positive),
        "best_evidence_scope": selected.get("confluence_scope", ""),
        "best_evidence_id": selected.get("confluence_id", ""),
        "best_evidence_sample_size": selected.get("sample_size", ""),
        "best_evidence_win_rate": selected.get("win_rate", ""),
        "best_evidence_median_return": selected.get("median_return", ""),
        "best_evidence_confidence_status": selected.get("confidence_status", ""),
        "best_evidence_out_of_sample_pass": selected.get("out_of_sample_pass", ""),
        "data_start_date": selected.get("data_start_date", ""),
        "data_end_date": selected.get("data_end_date", ""),
        "out_of_sample_start_date": selected.get("out_of_sample_start_date", ""),
        "approval_note_zh": (
            "以目前 repo 可用歷史資料批准放量攻擊 v1 操作建議。"
            "後續固定 research/backtest 可用新版 approval_version 調整參數與條件。"
        ),
        "risk_notes_zh": (
            "這是模型化操作建議，不是無條件買進；confirmed rows 仍須通過正向證據過濾，"
            "pending rows 只追蹤確認，不列買進。"
        ),
    }


def w_bottom_approval_row(generated_at: str) -> dict[str, Any]:
    if not W_BOTTOM_SPEC_SOURCE.exists():
        raise RuntimeError(f"missing W-bottom operation spec: {W_BOTTOM_SPEC_SOURCE}")

    mature_sample = to_number(W_BOTTOM_APPROVAL_METRICS["mature_sample_size"])
    positive_return_rate = to_number(W_BOTTOM_APPROVAL_METRICS["positive_return_rate_pct"])
    if mature_sample < W_BOTTOM_MIN_MATURE_SAMPLE_SIZE:
        raise RuntimeError("W-bottom approval evidence mature sample is below the v2 gate")
    if positive_return_rate < W_BOTTOM_MIN_POSITIVE_RETURN_RATE:
        raise RuntimeError("W-bottom approval evidence positive-return rate is below the v2 gate")

    return {
        "generated_at": generated_at,
        "model_id": W_BOTTOM_MODEL_ID,
        "operation_module_id": W_BOTTOM_OPERATION_MODULE_ID,
        "approval_version": W_BOTTOM_APPROVAL_VERSION,
        "approved_for_daily": "True",
        "approval_status": W_BOTTOM_APPROVAL_STATUS,
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": W_BOTTOM_SOURCE_RESEARCH_ID,
        "entry_rule_id": W_BOTTOM_ENTRY_RULE_ID,
        "entry_rule_zh": "右低點觀察訊號成立後，下一個交易日開盤買進。",
        "stop_loss_rule_id": W_BOTTOM_STOP_LOSS_RULE_ID,
        "stop_loss_rule_zh": "收盤跌破 W 結構低點出場；W 結構低點為偵測到的左低點與右低點較低者。",
        "exit_rule_id": W_BOTTOM_EXIT_RULE_ID,
        "exit_rule_zh": "若 D+20 收盤報酬達 +10% 則 D+20 收盤出場；否則持有到 D+40 收盤，除非先觸發 W 結構低點收盤停損。",
        "buy_filter_id": W_BOTTOM_BUY_FILTER_ID,
        "buy_filter_zh": "強勢或溫和多頭市場、核心主流族群、平滑圓弧 W 型態，且訊號收盤價已自右低點反彈 5% 到 20%。",
        "pending_rule_zh": "未成熟樣本保留揭露，不納入 D+20/D+40 操作正報酬率分母。",
        "min_sample_size": W_BOTTOM_MIN_MATURE_SAMPLE_SIZE,
        "min_win_rate": W_BOTTOM_MIN_POSITIVE_RETURN_RATE,
        "min_median_return": "",
        "require_out_of_sample_pass": "False",
        "min_research_score": "",
        "evidence_summary_source": str(W_BOTTOM_SPEC_SOURCE).replace("\\", "/"),
        "evidence_rank_source": str(W_BOTTOM_SPEC_SOURCE).replace("\\", "/"),
        "evidence_source_kind": "w_bottom_early_entry_operation_spec",
        "evidence_total_rank_rows": 1,
        "evidence_positive_rank_rows": 1,
        "best_evidence_scope": W_BOTTOM_APPROVAL_METRICS["surface_id"],
        "best_evidence_id": W_BOTTOM_APPROVAL_METRICS["selected_segment_id"],
        "best_evidence_sample_size": W_BOTTOM_APPROVAL_METRICS["mature_sample_size"],
        "best_evidence_win_rate": W_BOTTOM_APPROVAL_METRICS["positive_return_rate_pct"],
        "best_evidence_median_return": W_BOTTOM_APPROVAL_METRICS["median_return_pct"],
        "best_evidence_confidence_status": "approved_from_promoted_operation_spec_v2",
        "best_evidence_out_of_sample_pass": "not_applicable",
        "w_bottom_sample_size": W_BOTTOM_APPROVAL_METRICS["sample_size"],
        "w_bottom_evaluated_sample_size": W_BOTTOM_APPROVAL_METRICS["evaluated_sample_size"],
        "w_bottom_mature_sample_size": W_BOTTOM_APPROVAL_METRICS["mature_sample_size"],
        "w_bottom_win_count": W_BOTTOM_APPROVAL_METRICS["win_count"],
        "w_bottom_neutral_count": W_BOTTOM_APPROVAL_METRICS["neutral_count"],
        "w_bottom_loss_count": W_BOTTOM_APPROVAL_METRICS["loss_count"],
        "w_bottom_incomplete_count": W_BOTTOM_APPROVAL_METRICS["incomplete_count"],
        "w_bottom_stop_count": W_BOTTOM_APPROVAL_METRICS["stop_count"],
        "w_bottom_positive_return_rate_pct": W_BOTTOM_APPROVAL_METRICS["positive_return_rate_pct"],
        "w_bottom_pure_win_rate_pct": W_BOTTOM_APPROVAL_METRICS["positive_return_rate_pct"],
        "w_bottom_neutral_inclusive_success_rate_pct": W_BOTTOM_APPROVAL_METRICS[
            "neutral_inclusive_success_rate_pct"
        ],
        "w_bottom_avg_return_pct": W_BOTTOM_APPROVAL_METRICS["avg_return_pct"],
        "w_bottom_median_return_pct": W_BOTTOM_APPROVAL_METRICS["median_return_pct"],
        "w_bottom_min_return_pct": W_BOTTOM_APPROVAL_METRICS["min_return_pct"],
        "w_bottom_unique_stock_count": W_BOTTOM_APPROVAL_METRICS["unique_stock_count"],
        "data_start_date": "",
        "data_end_date": "",
        "out_of_sample_start_date": "",
        "approval_note_zh": (
            "W底右低點早期進場 v2 已批准為 daily operation guidance；"
            "raw research candidate rows 仍維持 research-only，正式 production 使用只能讀 approval artifact。"
        ),
        "risk_notes_zh": (
            "v2 只更新操作停損/出場與 evidence 口徑；不修改 w_bottom_right_side 的 production condition、scoring 或 ranking。"
        ),
    }


def neckline_approval_row(generated_at: str) -> dict[str, Any]:
    if not NECKLINE_SPEC_SOURCE.exists():
        raise RuntimeError(f"missing neckline operation spec: {NECKLINE_SPEC_SOURCE}")

    mature_sample = to_number(NECKLINE_APPROVAL_METRICS["tradable_entry_count"])
    pure_win_rate = to_number(NECKLINE_APPROVAL_METRICS["pure_win_rate_pct"])
    inclusive_success = to_number(NECKLINE_APPROVAL_METRICS["neutral_inclusive_success_rate_pct"])
    if mature_sample < NECKLINE_MIN_MATURE_SAMPLE_SIZE:
        raise RuntimeError("neckline approval evidence mature sample is below the v1 gate")
    if pure_win_rate < NECKLINE_MIN_PURE_WIN_RATE:
        raise RuntimeError("neckline approval evidence pure win rate is below the v1 gate")
    if inclusive_success < NECKLINE_MIN_NEUTRAL_INCLUSIVE_SUCCESS_RATE:
        raise RuntimeError("neckline approval evidence inclusive success rate is below the v1 gate")

    return {
        "generated_at": generated_at,
        "model_id": NECKLINE_MODEL_ID,
        "operation_module_id": NECKLINE_OPERATION_MODULE_ID,
        "approval_version": NECKLINE_APPROVAL_VERSION,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": NECKLINE_SOURCE_RESEARCH_ID,
        "entry_rule_id": NECKLINE_ENTRY_RULE_ID,
        "entry_rule_zh": "45日非空頭頸線候選成立後，3個交易日內收盤相對原始回測進場價達+1%，下一個交易日開盤買進。",
        "stop_loss_rule_id": NECKLINE_STOP_LOSS_RULE_ID,
        "stop_loss_rule_zh": "v1不升級固定收盤停損；以20個交易日操作規則判定勝、和、敗。",
        "exit_rule_id": NECKLINE_EXIT_RULE_ID,
        "exit_rule_zh": "20個交易日內收盤報酬先達+10%為勝；先達+5%後回落到<=+5%且未達+10%為和局；否則第20日收盤歸為操作規則敗。",
        "buy_filter_id": NECKLINE_BUY_FILTER_ID,
        "buy_filter_zh": "45日 context 必須為 auto_non_bearish；90日 context 只當 score adjustment / risk warning，不作入選排除。",
        "pending_rule_zh": "純勝率與含和局成功率必須分開標示；正報酬但未達操作規則勝/和者仍可歸為操作規則敗。",
        "min_sample_size": NECKLINE_MIN_MATURE_SAMPLE_SIZE,
        "min_win_rate": NECKLINE_MIN_PURE_WIN_RATE,
        "min_median_return": "",
        "require_out_of_sample_pass": "False",
        "min_research_score": "",
        "evidence_summary_source": str(NECKLINE_SPEC_SOURCE).replace("\\", "/"),
        "evidence_rank_source": str(NECKLINE_SPEC_SOURCE).replace("\\", "/"),
        "evidence_source_kind": "neckline_strict_45_signal_90_score_operation_spec",
        "evidence_total_rank_rows": 1,
        "evidence_positive_rank_rows": 1,
        "best_evidence_scope": NECKLINE_APPROVAL_METRICS["surface_id"],
        "best_evidence_id": NECKLINE_APPROVAL_METRICS["selected_segment_id"],
        "best_evidence_sample_size": NECKLINE_APPROVAL_METRICS["tradable_entry_count"],
        "best_evidence_win_rate": NECKLINE_APPROVAL_METRICS["pure_win_rate_pct"],
        "best_evidence_median_return": NECKLINE_APPROVAL_METRICS["median_return_pct"],
        "best_evidence_confidence_status": "approved_from_promoted_operation_spec_v1",
        "best_evidence_out_of_sample_pass": "not_applicable",
        "neckline_source_candidate_count": NECKLINE_APPROVAL_METRICS["source_candidate_count"],
        "neckline_confirmation_candidate_count": NECKLINE_APPROVAL_METRICS["confirmation_candidate_count"],
        "neckline_tradable_entry_count": NECKLINE_APPROVAL_METRICS["tradable_entry_count"],
        "neckline_filter90_auto_bearish_confirmed_count": NECKLINE_APPROVAL_METRICS[
            "filter90_auto_bearish_confirmed_count"
        ],
        "neckline_win_count": NECKLINE_APPROVAL_METRICS["win_count"],
        "neckline_neutral_count": NECKLINE_APPROVAL_METRICS["neutral_count"],
        "neckline_loss_count": NECKLINE_APPROVAL_METRICS["loss_count"],
        "neckline_pure_win_rate_pct": NECKLINE_APPROVAL_METRICS["pure_win_rate_pct"],
        "neckline_neutral_inclusive_success_rate_pct": NECKLINE_APPROVAL_METRICS[
            "neutral_inclusive_success_rate_pct"
        ],
        "neckline_avg_return_pct": NECKLINE_APPROVAL_METRICS["avg_return_pct"],
        "neckline_avg_max_close_return_pct": NECKLINE_APPROVAL_METRICS["avg_max_close_return_pct"],
        "neckline_avg_min_close_return_pct": NECKLINE_APPROVAL_METRICS["avg_min_close_return_pct"],
        "neckline_unique_stock_count": NECKLINE_APPROVAL_METRICS["unique_stock_count"],
        "data_start_date": "",
        "data_end_date": "",
        "out_of_sample_start_date": "",
        "approval_note_zh": (
            "W底頸線帶量突破 v1 正式批准為 daily operation guidance；45日 context 是入選訊號，"
            "90日 context 只作分數與風險調整。其他頸線型態不混入此 v1，原始 research candidate rows 仍維持 research-only。"
        ),
        "risk_notes_zh": (
            "PDF標題下方必須標示操作規則勝率與含和局成功率；"
            "neckline_volume_breakout_confirmation v1 只代表 W-bottom subtype 的正式 confirmed-breakout surface，"
            "near_high_neckline_challenge 與 platform_strengthening 由 contract deprecation 停用。"
        ),
    }


def price_pullback_approval_row(generated_at: str) -> dict[str, Any]:
    if not PRICE_PULLBACK_SPEC_SOURCE.exists():
        raise RuntimeError(f"missing price pullback operation spec: {PRICE_PULLBACK_SPEC_SOURCE}")

    mature_sample = to_number(PRICE_PULLBACK_APPROVAL_METRICS["mature_sample_size"])
    win_rate = to_number(PRICE_PULLBACK_APPROVAL_METRICS["win_rate_pct"])
    if mature_sample < PRICE_PULLBACK_MIN_MATURE_SAMPLE_SIZE:
        raise RuntimeError("price_pullback_23ema approval evidence mature sample is below the v1 gate")
    if win_rate < PRICE_PULLBACK_MIN_WIN_RATE:
        raise RuntimeError("price_pullback_23ema approval evidence win rate is below the v1 gate")

    return {
        "generated_at": generated_at,
        "model_id": PRICE_PULLBACK_MODEL_ID,
        "operation_module_id": PRICE_PULLBACK_OPERATION_MODULE_ID,
        "approval_version": PRICE_PULLBACK_APPROVAL_VERSION,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": PRICE_PULLBACK_SOURCE_RESEARCH_ID,
        "entry_rule_id": PRICE_PULLBACK_ENTRY_RULE_ID,
        "entry_rule_zh": "訊號成立後下一個交易日開盤買入。",
        "stop_loss_rule_id": PRICE_PULLBACK_STOP_LOSS_RULE_ID,
        "stop_loss_rule_zh": "收盤連續4天低於MA20/EMA23較低者4%，下一個交易日開盤停損。",
        "exit_rule_id": PRICE_PULLBACK_EXIT_RULE_ID,
        "exit_rule_zh": "收盤突破訊號日前20日高點後，下一個交易日開盤賣出。",
        "buy_filter_id": PRICE_PULLBACK_BUY_FILTER_ID,
        "buy_filter_zh": (
            "price_pullback_23ema訊號、20日漲幅0%到25%、TDCC高門檻籌碼增加、OBV站上OBV MA20。"
        ),
        "pending_rule_zh": (
            "本模型v1沒有待確認主表；精華版只提供本日可買/已確認候選與操作中。"
        ),
        "min_sample_size": PRICE_PULLBACK_MIN_MATURE_SAMPLE_SIZE,
        "min_win_rate": PRICE_PULLBACK_MIN_WIN_RATE,
        "min_median_return": "",
        "require_out_of_sample_pass": "False",
        "min_research_score": "",
        "evidence_summary_source": "output/latest/research_backtest/price_pullback_23ema_promotion_matrix_latest.csv",
        "evidence_rank_source": "output/latest/research_backtest/price_pullback_23ema_promotion_matrix_latest.csv",
        "evidence_source_kind": "price_pullback_23ema_promoted_operation_spec",
        "evidence_total_rank_rows": 1,
        "evidence_positive_rank_rows": 1,
        "best_evidence_scope": PRICE_PULLBACK_APPROVAL_METRICS["surface_id"],
        "best_evidence_id": PRICE_PULLBACK_APPROVAL_METRICS["selected_segment_id"],
        "best_evidence_sample_size": PRICE_PULLBACK_APPROVAL_METRICS["mature_sample_size"],
        "best_evidence_win_rate": PRICE_PULLBACK_APPROVAL_METRICS["win_rate_pct"],
        "best_evidence_median_return": "",
        "best_evidence_confidence_status": "approved_from_promoted_operation_spec_v1",
        "best_evidence_out_of_sample_pass": "not_applicable",
        "price_pullback_mature_sample_size": PRICE_PULLBACK_APPROVAL_METRICS["mature_sample_size"],
        "price_pullback_win_count": PRICE_PULLBACK_APPROVAL_METRICS["win_count"],
        "price_pullback_neutral_count": PRICE_PULLBACK_APPROVAL_METRICS["neutral_count"],
        "price_pullback_failure_count": PRICE_PULLBACK_APPROVAL_METRICS["failure_count"],
        "price_pullback_hard_stop_rate_pct": PRICE_PULLBACK_APPROVAL_METRICS["hard_stop_rate_pct"],
        "price_pullback_win_rate_pct": PRICE_PULLBACK_APPROVAL_METRICS["win_rate_pct"],
        "price_pullback_neutral_rate_pct": PRICE_PULLBACK_APPROVAL_METRICS["neutral_rate_pct"],
        "price_pullback_failure_rate_pct": PRICE_PULLBACK_APPROVAL_METRICS["failure_rate_pct"],
        "price_pullback_avg_return_pct": PRICE_PULLBACK_APPROVAL_METRICS["avg_return_pct"],
        "price_pullback_technical_package_sample_size": PRICE_PULLBACK_APPROVAL_METRICS[
            "technical_package_sample_size"
        ],
        "price_pullback_technical_package_win_rate_pct": PRICE_PULLBACK_APPROVAL_METRICS[
            "technical_package_win_rate_pct"
        ],
        "price_pullback_technical_package_neutral_rate_pct": PRICE_PULLBACK_APPROVAL_METRICS[
            "technical_package_neutral_rate_pct"
        ],
        "price_pullback_technical_package_failure_rate_pct": PRICE_PULLBACK_APPROVAL_METRICS[
            "technical_package_failure_rate_pct"
        ],
        "price_pullback_technical_package_avg_return_pct": PRICE_PULLBACK_APPROVAL_METRICS[
            "technical_package_avg_return_pct"
        ],
        "data_start_date": "",
        "data_end_date": "",
        "out_of_sample_start_date": "",
        "approval_note_zh": (
            "23EMA回檔模型 v1 正式批准為 daily operation guidance；營收、熱門族群、權證與高報酬結構分不進v1。"
        ),
        "risk_notes_zh": (
            "RSI>=60且MACD histogram>0只作技術強勢操作品質標籤；籌碼全同步與帶量紅K只作理由/風險標籤，"
            "不作額外排序分。正式進出場只使用收盤確認與下一交易日開盤，不使用盤中高低點作報酬。"
        ),
    }


def build_approval(summary: pd.DataFrame, rank: pd.DataFrame, generated_at: str | None = None) -> pd.DataFrame:
    generated = generated_at or now_text()
    if summary.empty:
        raise RuntimeError(f"missing confirmed operation summary: {CONFIRMED_SUMMARY_CSV}")
    if rank.empty:
        raise RuntimeError(f"missing confirmed operation rank: {CONFIRMED_RANK_CSV}")
    return pd.DataFrame(
        [
            approval_row(summary, rank, generated),
            w_bottom_approval_row(generated),
            neckline_approval_row(generated),
            price_pullback_approval_row(generated),
        ]
    )


def write_markdown(df: pd.DataFrame) -> None:
    lines = [
        "# Approved Operation Patterns",
        "",
        f"- generated_at: `{now_text()}`",
        "- purpose: explicit promotion gate from research/backtest evidence to daily operation guidance",
        "- rule: raw research backtest rows can remain research-only; this artifact is the explicit approval layer",
        "",
        markdown_table(
            df,
            [
                "model_id",
                "operation_module_id",
                "approval_version",
                "approved_for_daily",
                "operation_directive_level",
                "entry_rule_id",
                "stop_loss_rule_id",
                "exit_rule_id",
                "buy_filter_id",
                "evidence_positive_rank_rows",
                "best_evidence_sample_size",
                "best_evidence_win_rate",
                "best_evidence_median_return",
                "evidence_source_kind",
                "approval_note_zh",
            ],
            limit=20,
        ),
        "",
    ]
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_MD.write_text(OUT_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def main() -> int:
    summary = read_csv(CONFIRMED_SUMMARY_CSV, dtype=str).fillna("")
    rank = read_csv(CONFIRMED_RANK_CSV, dtype=str).fillna("")
    approval = build_approval(summary, rank)
    write_csv(approval, OUT_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(approval, DOCS_CSV)
    write_markdown(approval)
    print(f"Saved {OUT_CSV} rows={len(approval)}")
    print(f"Saved {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
