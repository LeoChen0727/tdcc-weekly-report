from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, markdown_table, now_text, read_csv, safe_str, to_number, write_csv  # noqa: E402
from formal_model_evidence import evidence_pin_for_model  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
V2_LOW_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
V2_MID_MODEL_ID = "volume_range_breakout_v2_mid_position_momentum_attack"
V2_HIGH_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"
V2_FORMAL_MODEL_IDS = (V2_LOW_MODEL_ID, V2_MID_MODEL_ID, V2_HIGH_MODEL_ID)
V2_ENTRY_RULE_ID = "confirmation_next_open"
V2_STOP_LOSS_RULE_ID = "sustained_close_below_lower_ma20_ema23_4pct_4d"
V2_EXIT_RULE_ID = "ema23_close_stop_or_fixed_15d_close"
V2_SOURCE_RESEARCH_ID = "volume_range_breakout_v2_candidate_bucket_contract"
V2_EVIDENCE_SOURCE = "output/latest/research_backtest/volume_range_breakout_v2_candidate_bucket_contract_latest.csv"
V2_APPROVAL_VERSION = "volume_range_breakout_v2_formal_operation_20260709"
V2_HIGH_SOURCE_RESEARCH_ID = "volume_range_breakout_v2_high_position_improvement_audit"
V2_HIGH_EVIDENCE_SOURCE = (
    "output/latest/research_backtest/volume_range_breakout_v2_high_position_improvement_audit_latest.csv"
)
V2_APPROVAL_METRICS = {
    V2_LOW_MODEL_ID: {
        "operation_module_id": "volume_range_breakout_v2_low_position_operation_v1",
        "buy_filter_id": "pos120_low_all_shapes_next_day_continuation_d15_stop",
        "model_name_zh": "低位放量攻擊",
        "best_evidence_sample_size": "26",
        "best_evidence_win_rate": "80.7692",
        "best_evidence_neutral_rate": "0.0000",
        "best_evidence_loss_rate": "19.2308",
        "best_evidence_median_return": "18.7857",
        "volume_v2_avg_return_pct": "28.7704",
        "win_count": "21",
        "neutral_count": "0",
        "loss_count": "5",
        "condition_zh": "120日位階 low_pos_le40，shape 可為 consolidation、non_consolidation 或 wide_range；確認為隔日續攻 close-only。",
    },
    V2_MID_MODEL_ID: {
        "operation_module_id": "volume_range_breakout_v2_mid_position_operation_v1",
        "buy_filter_id": "pos120_mid_non_consolidation_or_wide_next_day_continuation_d15_stop",
        "model_name_zh": "中位動能放量攻擊",
        "best_evidence_sample_size": "25",
        "best_evidence_win_rate": "80.0000",
        "best_evidence_neutral_rate": "0.0000",
        "best_evidence_loss_rate": "20.0000",
        "best_evidence_median_return": "14.6953",
        "volume_v2_avg_return_pct": "12.7599",
        "win_count": "20",
        "neutral_count": "0",
        "loss_count": "5",
        "condition_zh": "120日位階 mid_pos_40_75，shape 僅收 non_consolidation 或 wide_range；確認為隔日續攻 close-only。",
    },
    V2_HIGH_MODEL_ID: {
        "operation_module_id": "volume_range_breakout_v2_high_position_operation_v1",
        "approval_version": "volume_range_breakout_v2_high_position_operation_20260710",
        "source_research_id": V2_HIGH_SOURCE_RESEARCH_ID,
        "evidence_source": V2_HIGH_EVIDENCE_SOURCE,
        "evidence_source_kind": "volume_range_breakout_v2_high_position_improvement_audit",
        "buy_filter_id": "pos120_high_nonconsolidation_or_wide_ma60_gt_ma120_next_day_continuation_d15_stop",
        "model_name_zh": "高位階放量攻擊",
        "best_evidence_sample_size": "231",
        "best_evidence_win_rate": "62.3377",
        "best_evidence_neutral_rate": "0.0000",
        "best_evidence_loss_rate": "37.6623",
        "best_evidence_median_return": "6.6055",
        "volume_v2_avg_return_pct": "9.4824",
        "win_count": "144",
        "neutral_count": "0",
        "loss_count": "87",
        "condition_zh": (
            "120日位階 high_pos_gt75，shape 僅收 non_consolidation 或 wide_range，"
            "訊號日 MA60 > MA120；確認為隔日續攻 close-only。"
        ),
        "approval_note_zh": (
            "高位階放量攻擊升級為正式 daily operation model；模型條件加 close-only 確認就是買入 gate。"
            "單項加分可顯示其單項統計，多項命中只採真實重算且不變差的 combo 統計。"
        ),
        "risk_notes_zh": "目前不採扣分項；舊 v1 放量攻擊與高位階 v2 不得混用。",
    },
}

OUT_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"
OUT_MD = LATEST_DIR / "approved_operation_patterns_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name

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


def volume_v2_approval_row(model_id: str, generated_at: str) -> dict[str, Any]:
    metrics = V2_APPROVAL_METRICS[model_id]
    approval_version = metrics.get("approval_version", V2_APPROVAL_VERSION)
    evidence_pin = evidence_pin_for_model(model_id, approval_version)
    source_research_id = metrics.get("source_research_id", V2_SOURCE_RESEARCH_ID)
    evidence_source = metrics.get("evidence_source", V2_EVIDENCE_SOURCE)
    evidence_source_kind = metrics.get("evidence_source_kind", "volume_range_breakout_v2_candidate_bucket_contract")
    return {
        "generated_at": generated_at,
        "model_id": model_id,
        "operation_module_id": metrics["operation_module_id"],
        "approval_version": approval_version,
        "evidence_artifact_version": evidence_pin.evidence_version,
        "evidence_canonical_sha256": evidence_pin.canonical_sha256,
        "evidence_pin_source": evidence_pin.evidence_path,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": source_research_id,
        "entry_rule_id": V2_ENTRY_RULE_ID,
        "entry_rule_zh": "確認日收盤後成立，下一個交易日開盤買入。",
        "stop_loss_rule_id": V2_STOP_LOSS_RULE_ID,
        "stop_loss_rule_zh": "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。",
        "exit_rule_id": V2_EXIT_RULE_ID,
        "exit_rule_zh": "若未觸發停損，固定第15個交易日收盤出場。",
        "buy_filter_id": metrics["buy_filter_id"],
        "buy_filter_zh": metrics["condition_zh"],
        "pending_rule_zh": "訊號日後等待隔日續攻收盤確認；未確認前不列買入。",
        "min_sample_size": "0",
        "min_win_rate": "60.0",
        "min_median_return": "0.0",
        "require_out_of_sample_pass": "False",
        "min_research_score": "0.0",
        "evidence_summary_source": evidence_source,
        "evidence_rank_source": evidence_source,
        "evidence_source_kind": evidence_source_kind,
        "evidence_total_rank_rows": "",
        "evidence_positive_rank_rows": "",
        "best_evidence_scope": "model_contract",
        "best_evidence_id": model_id,
        "best_evidence_sample_size": metrics["best_evidence_sample_size"],
        "best_evidence_win_rate": metrics["best_evidence_win_rate"],
        "best_evidence_median_return": metrics["best_evidence_median_return"],
        "best_evidence_confidence_status": "research_validated_pending_post_merge_monitoring",
        "best_evidence_out_of_sample_pass": "not_applicable",
        "data_start_date": "",
        "data_end_date": "",
        "out_of_sample_start_date": "",
        "approval_note_zh": metrics.get("approval_note_zh") or (
            f"{metrics['model_name_zh']} 升級為正式 daily operation model；模型條件加 close-only 確認就是買入 gate，"
            "TDCC、MA60/MA120、EMA23 距離只可作分層或加分，不得作 hidden gate。"
        ),
        "risk_notes_zh": metrics.get("risk_notes_zh")
        or "樣本數不作否決理由；各 v2 模型語意獨立，舊 v1 放量攻擊不得回流 production。",
        "volume_v2_model_name_zh": metrics["model_name_zh"],
        "volume_v2_win_count": metrics["win_count"],
        "volume_v2_neutral_count": metrics["neutral_count"],
        "volume_v2_loss_count": metrics["loss_count"],
        "volume_v2_win_rate_pct": metrics["best_evidence_win_rate"],
        "volume_v2_neutral_rate_pct": metrics["best_evidence_neutral_rate"],
        "volume_v2_loss_rate_pct": metrics["best_evidence_loss_rate"],
        "volume_v2_avg_return_pct": metrics["volume_v2_avg_return_pct"],
        "volume_v2_median_return_pct": metrics["best_evidence_median_return"],
        "volume_v2_condition_zh": metrics["condition_zh"],
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

    evidence_pin = evidence_pin_for_model(W_BOTTOM_MODEL_ID, W_BOTTOM_APPROVAL_VERSION)
    return {
        "generated_at": generated_at,
        "model_id": W_BOTTOM_MODEL_ID,
        "operation_module_id": W_BOTTOM_OPERATION_MODULE_ID,
        "approval_version": W_BOTTOM_APPROVAL_VERSION,
        "evidence_artifact_version": evidence_pin.evidence_version,
        "evidence_canonical_sha256": evidence_pin.canonical_sha256,
        "evidence_pin_source": evidence_pin.evidence_path,
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

    evidence_pin = evidence_pin_for_model(NECKLINE_MODEL_ID, NECKLINE_APPROVAL_VERSION)
    return {
        "generated_at": generated_at,
        "model_id": NECKLINE_MODEL_ID,
        "operation_module_id": NECKLINE_OPERATION_MODULE_ID,
        "approval_version": NECKLINE_APPROVAL_VERSION,
        "evidence_artifact_version": evidence_pin.evidence_version,
        "evidence_canonical_sha256": evidence_pin.canonical_sha256,
        "evidence_pin_source": evidence_pin.evidence_path,
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

    evidence_pin = evidence_pin_for_model(PRICE_PULLBACK_MODEL_ID, PRICE_PULLBACK_APPROVAL_VERSION)
    return {
        "generated_at": generated_at,
        "model_id": PRICE_PULLBACK_MODEL_ID,
        "operation_module_id": PRICE_PULLBACK_OPERATION_MODULE_ID,
        "approval_version": PRICE_PULLBACK_APPROVAL_VERSION,
        "evidence_artifact_version": evidence_pin.evidence_version,
        "evidence_canonical_sha256": evidence_pin.canonical_sha256,
        "evidence_pin_source": evidence_pin.evidence_path,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": PRICE_PULLBACK_SOURCE_RESEARCH_ID,
        "entry_rule_id": PRICE_PULLBACK_ENTRY_RULE_ID,
        "entry_rule_zh": "訊號成立後隔日開盤買入。",
        "stop_loss_rule_id": PRICE_PULLBACK_STOP_LOSS_RULE_ID,
        "stop_loss_rule_zh": "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。",
        "exit_rule_id": PRICE_PULLBACK_EXIT_RULE_ID,
        "exit_rule_zh": "收盤突破訊號日前20日高點後，隔日開盤賣出。",
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
            "不作額外排序分。正式進出場只使用收盤確認與隔日開盤，不使用盤中高低點作報酬。"
        ),
    }


def build_approval(generated_at: str | None = None) -> pd.DataFrame:
    generated = generated_at or now_text()
    return pd.DataFrame(
        [
            volume_v2_approval_row(V2_LOW_MODEL_ID, generated),
            volume_v2_approval_row(V2_MID_MODEL_ID, generated),
            volume_v2_approval_row(V2_HIGH_MODEL_ID, generated),
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
    approval = build_approval()
    write_csv(approval, OUT_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(approval, DOCS_CSV)
    write_markdown(approval)
    print(f"Saved {OUT_CSV} rows={len(approval)}")
    print(f"Saved {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
