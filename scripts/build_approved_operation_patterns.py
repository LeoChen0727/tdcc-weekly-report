from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, markdown_table, now_text, read_csv, safe_str, to_number, write_csv  # noqa: E402


MODEL_ID = "volume_range_breakout"
OPERATION_MODULE_ID = "volume_breakout_confirmed_operation_v1"
APPROVAL_VERSION = "volume_breakout_operation_v1_20260615"
SOURCE_RESEARCH_ID = "volume_breakout_confirmed_operation"
ENTRY_RULE_ID = "confirmation_next_open"
STOP_LOSS_RULE_ID = "signal_low_stop"
EXIT_RULE_ID = "signal_low_stop_or_fixed_10d_close"
BUY_FILTER_ID = "positive_evidence_oos_rank_v1"

CONFIRMED_SUMMARY_CSV = LATEST_DIR / "volume_breakout_formal_operation_backtest_latest.csv"
CONFIRMED_RANK_CSV = LATEST_DIR / "volume_breakout_confirmed_operation_rank_latest.csv"
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
    best = best_evidence(summary)
    source = summary if not summary.empty else rank
    data_start = safe_str(source.get("data_start_date", pd.Series(dtype=str)).min()) if "data_start_date" in source.columns else ""
    data_end = safe_str(source.get("data_end_date", pd.Series(dtype=str)).max()) if "data_end_date" in source.columns else ""
    split = (
        safe_str(source.get("out_of_sample_start_date", pd.Series(dtype=str)).max())
        if "out_of_sample_start_date" in source.columns
        else ""
    )

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
        "best_evidence_scope": "" if best is None else safe_str(best.get("confluence_scope")),
        "best_evidence_id": "" if best is None else safe_str(best.get("confluence_id")),
        "best_evidence_sample_size": "" if best is None else safe_str(best.get("sample_size")),
        "best_evidence_win_rate": "" if best is None else safe_str(best.get("win_rate")),
        "best_evidence_median_return": "" if best is None else safe_str(best.get("median_return")),
        "best_evidence_confidence_status": "" if best is None else safe_str(best.get("confidence_status")),
        "best_evidence_out_of_sample_pass": "" if best is None else safe_str(best.get("out_of_sample_pass")),
        "data_start_date": data_start,
        "data_end_date": data_end,
        "out_of_sample_start_date": split,
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


def build_approval(summary: pd.DataFrame, rank: pd.DataFrame, generated_at: str | None = None) -> pd.DataFrame:
    generated = generated_at or now_text()
    if summary.empty:
        raise RuntimeError(f"missing confirmed operation summary: {CONFIRMED_SUMMARY_CSV}")
    if rank.empty:
        raise RuntimeError(f"missing confirmed operation rank: {CONFIRMED_RANK_CSV}")
    return pd.DataFrame([approval_row(summary, rank, generated), w_bottom_approval_row(generated)])


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
