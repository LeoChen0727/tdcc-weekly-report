from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, safe_str, to_number, write_csv  # noqa: E402


ROOT = Path(".")
RANK_CSV = LATEST_DIR / "volume_breakout_confirmed_operation_rank_latest.csv"
PENDING_CSV = LATEST_DIR / "volume_breakout_pending_operation_queue_latest.csv"
PREVIEW_CSV = LATEST_DIR / "volume_breakout_operation_pdf_preview_latest.csv"
PREVIEW_MD = LATEST_DIR / "volume_breakout_operation_pdf_preview_latest.md"

MODEL_ID = "volume_range_breakout"
HIGHLIGHT_CONFIRMED_LIMIT = 10

PREVIEW_COLUMNS = [
    "pdf_view",
    "pdf_section",
    "display_order",
    "stock_id",
    "stock_name",
    "stock_display",
    "operation_status_zh",
    "quality_status_zh",
    "trigger_zh",
    "entry_basis_zh",
    "entry_price_status_zh",
    "stop_basis_zh",
    "exit_rule_zh",
    "signal_date",
    "confirmation_date",
    "pending_age_zh",
    "pending_group_zh",
    "pending_confirmation_zh",
    "same_stock_pending_count",
    "tdcc_status_zh",
    "sample_size",
    "win_rate_zh",
    "avg_return_zh",
    "median_return_zh",
    "confidence_zh",
    "research_score",
    "pdf_note_zh",
]

TRIGGER_ZH = {
    "next_day_continuation_confirmed": "隔日續強確認",
    "pullback_5ma_confirmed": "回測 5MA 確認",
    "pullback_10ma_confirmed": "回測 10MA 確認",
}

CLASSIFICATION_ZH = {
    "locked_limit_up_breakout": "鎖量漲停突破",
    "limit_up_like_breakout": "類漲停突破",
    "long_base_low_position": "長盤整低位階突破",
    "low_position_breakout": "低位階突破",
    "high_position_breakout": "高位階突破",
    "wide_range_breakout": "寬區間突破",
    "standard_breakout": "一般突破",
}

ATTACK_ZH = {
    "locked_limit_up": "鎖量漲停",
    "volume_attack": "放量攻擊",
    "general_breakout": "一般突破",
}

POSITION_ZH = {
    "low_position": "低位階",
    "middle_position": "中位階",
    "high_position": "高位階",
    "unknown_position": "位階資料不足",
}

TDCC_ZH = {
    "weekly_increase": "TDCC 當週大戶增幅",
    "consecutive_accumulation": "TDCC 連續累積",
    "no_tdcc": "無 TDCC 疊加",
}

CONFIDENCE_ZH = {
    "low": "低",
    "medium": "中",
    "high": "高",
}


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def format_pct(value: Any, signed: bool = False) -> str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    sign = "+" if signed and num > 0 else ""
    return f"{sign}{num:.2f}%"


def format_date_short(value: Any) -> str:
    text = safe_str(value)
    if len(text) == 8 and text.isdigit():
        return f"{int(text[4:6])}/{int(text[6:8])}"
    return text


def format_price(value: Any) -> str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return f"{num:.2f}"


def stock_display(row: pd.Series) -> str:
    sid = safe_str(row.get("stock_id"))
    name = safe_str(row.get("stock_name"))
    return f"{sid} {name}".strip()


def stop_basis(signal_date: Any, stop_level: Any) -> str:
    date_text = format_date_short(signal_date)
    price_text = format_price(stop_level)
    if date_text and price_text:
        return f"跌破 {date_text} 最低價 {price_text}"
    if date_text:
        return f"跌破 {date_text} 最低價"
    return ""


def positive_evidence(row: pd.Series) -> bool:
    sample = to_number(row.get("evidence_sample_size"))
    win = to_number(row.get("evidence_win_rate"))
    median = to_number(row.get("evidence_median_return"))
    score = to_number(row.get("ranking_research_score"))
    return (
        not math.isnan(sample)
        and not math.isnan(win)
        and not math.isnan(median)
        and not math.isnan(score)
        and sample >= 10
        and win >= 50
        and median > 0
        and score > 0
    )


def quality_status(row: pd.Series) -> str:
    if positive_evidence(row):
        return "正向證據"
    sample = to_number(row.get("evidence_sample_size"))
    if math.isnan(sample) or sample < 10:
        return "樣本不足"
    return "證據偏弱"


def trigger_zh(row: pd.Series) -> str:
    return TRIGGER_ZH.get(safe_str(row.get("trigger_id")), safe_str(row.get("trigger_id")))


def tdcc_status_zh(row: pd.Series) -> str:
    list_type = safe_str(row.get("tdcc_list_type"))
    rank = safe_str(row.get("tdcc_rank"))
    base = TDCC_ZH.get(list_type, list_type)
    if list_type in {"weekly_increase", "consecutive_accumulation"} and rank:
        return f"{base} 第 {rank} 名"
    return base


def classification_note(row: pd.Series) -> str:
    parts = []
    for col, mapping in [
        ("classification_id", CLASSIFICATION_ZH),
        ("attack_method", ATTACK_ZH),
        ("price_position_type", POSITION_ZH),
    ]:
        value = safe_str(row.get(col))
        text = mapping.get(value, value)
        if text:
            parts.append(text)
    return " / ".join(dict.fromkeys(parts))


def confirmed_row(row: pd.Series, pdf_view: str, pdf_section: str, display_order: int) -> dict[str, Any]:
    return {
        "pdf_view": pdf_view,
        "pdf_section": pdf_section,
        "display_order": display_order,
        "stock_id": safe_str(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "stock_display": stock_display(row),
        "operation_status_zh": "已確認",
        "quality_status_zh": quality_status(row),
        "trigger_zh": trigger_zh(row),
        "entry_basis_zh": "確認後下一交易日開盤",
        "entry_price_status_zh": "進場價待下一交易日開盤",
        "stop_basis_zh": stop_basis(row.get("signal_date"), row.get("stop_loss_level")),
        "exit_rule_zh": "先跌破停損基準出場，否則進場後第 10 個交易日收盤出場",
        "signal_date": safe_str(row.get("signal_date")),
        "confirmation_date": safe_str(row.get("confirmation_date")),
        "pending_age_zh": "",
        "pending_group_zh": "",
        "pending_confirmation_zh": "",
        "same_stock_pending_count": "",
        "tdcc_status_zh": tdcc_status_zh(row),
        "sample_size": safe_str(row.get("evidence_sample_size")),
        "win_rate_zh": format_pct(row.get("evidence_win_rate")),
        "avg_return_zh": format_pct(row.get("evidence_avg_return"), signed=True),
        "median_return_zh": format_pct(row.get("evidence_median_return"), signed=True),
        "confidence_zh": CONFIDENCE_ZH.get(safe_str(row.get("evidence_confidence_status")), safe_str(row.get("evidence_confidence_status"))),
        "research_score": safe_str(row.get("ranking_research_score")),
        "pdf_note_zh": classification_note(row),
    }


def pending_group(age: int) -> str:
    if age <= 1:
        return "D+0-D+1 等隔日續強"
    if age <= 5:
        return "D+2-D+5 等回測 5MA/10MA"
    return "D+6-D+10 接近過期"


def pending_age_zh(age_value: Any) -> str:
    age = int(to_number(age_value, 0))
    remaining = max(0, 10 - age)
    return f"D+{age}，剩 {remaining} 個交易日"


def pending_row(row: pd.Series, pdf_view: str, pdf_section: str, display_order: int, count: int) -> dict[str, Any]:
    age = int(to_number(row.get("signal_age_trading_days"), 0))
    return {
        "pdf_view": pdf_view,
        "pdf_section": pdf_section,
        "display_order": display_order,
        "stock_id": safe_str(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "stock_display": stock_display(row),
        "operation_status_zh": "待確認",
        "quality_status_zh": "尚未確認",
        "trigger_zh": "",
        "entry_basis_zh": "尚未確認，不列進場價",
        "entry_price_status_zh": "",
        "stop_basis_zh": stop_basis(row.get("signal_date"), row.get("stop_loss_level")),
        "exit_rule_zh": "尚未成立；確認後才啟動進場與出場規則",
        "signal_date": safe_str(row.get("signal_date")),
        "confirmation_date": "",
        "pending_age_zh": pending_age_zh(age),
        "pending_group_zh": pending_group(age),
        "pending_confirmation_zh": "等待隔日續強 / 回測 5MA / 回測 10MA",
        "same_stock_pending_count": count,
        "tdcc_status_zh": "",
        "sample_size": "",
        "win_rate_zh": "",
        "avg_return_zh": "",
        "median_return_zh": "",
        "confidence_zh": "",
        "research_score": "",
        "pdf_note_zh": classification_note(row),
    }


def sort_rank(rank: pd.DataFrame) -> pd.DataFrame:
    if rank.empty:
        return rank
    out = rank.copy()
    out["_operation_rank"] = pd.to_numeric(out.get("operation_rank"), errors="coerce").fillna(999999)
    out["_score"] = pd.to_numeric(out.get("ranking_research_score"), errors="coerce").fillna(-999999)
    return out.sort_values(["_operation_rank", "_score", "stock_id"], ascending=[True, False, True])


def dedupe_pending(pending: pd.DataFrame) -> pd.DataFrame:
    if pending.empty:
        return pending
    out = pending.copy()
    out["_age"] = pd.to_numeric(out.get("signal_age_trading_days"), errors="coerce").fillna(999)
    out["_signal_date"] = out.get("signal_date", "").astype(str)
    out["_same_stock_pending_count"] = out.groupby("stock_id")["stock_id"].transform("size")
    out = out.sort_values(["stock_id", "_signal_date", "_age"], ascending=[True, False, True])
    out = out.drop_duplicates("stock_id", keep="first")
    out = out.sort_values(["_age", "_signal_date", "stock_id"], ascending=[True, False, True]).reset_index(drop=True)
    return out


def build_preview(rank: pd.DataFrame, pending: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    rank_sorted = sort_rank(rank)
    positive = rank_sorted[rank_sorted.apply(positive_evidence, axis=1)].head(HIGHLIGHT_CONFIRMED_LIMIT)
    for idx, (_, row) in enumerate(positive.iterrows(), start=1):
        rows.append(confirmed_row(row, "highlight", "confirmed_operation", idx))
    for idx, (_, row) in enumerate(rank_sorted.iterrows(), start=1):
        rows.append(confirmed_row(row, "full", "confirmed_operation", idx))

    pending_unique = dedupe_pending(pending)
    highlight_pending = pending_unique.head(10)
    for idx, (_, row) in enumerate(highlight_pending.iterrows(), start=1):
        rows.append(pending_row(row, "highlight", "pending_confirmation", idx, int(to_number(row.get("_same_stock_pending_count"), 1))))
    for idx, (_, row) in enumerate(pending_unique.iterrows(), start=1):
        rows.append(pending_row(row, "full", "pending_confirmation", idx, int(to_number(row.get("_same_stock_pending_count"), 1))))

    return pd.DataFrame(rows, columns=PREVIEW_COLUMNS)


MARKDOWN_HEADERS = {
    "display_order": "排序",
    "model_id": "模型ID",
    "model_name_zh": "模型",
    "pdf_visibility": "PDF 層級",
    "recommended_usage": "研究用途",
    "research_status_zh": "操作研究狀態",
    "stock_display": "股票",
    "operation_status_zh": "狀態",
    "quality_status_zh": "研究品質",
    "trigger_zh": "觸發型態",
    "entry_basis_zh": "買進基準",
    "stop_basis_zh": "停損基準",
    "sample_size": "樣本數",
    "win_rate_zh": "勝率",
    "avg_return_zh": "平均報酬",
    "median_return_zh": "中位數報酬",
    "confidence_zh": "信心",
    "pending_age_zh": "待確認天數",
    "pending_group_zh": "待確認分組",
    "holding_age_zh": "操作天數",
    "planned_exit_zh": "預定出場",
    "same_stock_pending_count": "同股待確認筆數",
    "pdf_note_zh": "PDF 備註",
    "research_score": "研究分數",
}


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 120) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    headers = [MARKDOWN_HEADERS.get(col, col) for col in columns]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.head(limit).iterrows():
        values = [safe_str(row.get(col)).replace("|", "/").replace("\n", " ")[:160] for col in columns]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def write_markdown(preview: pd.DataFrame, rank: pd.DataFrame, pending: pd.DataFrame) -> None:
    highlight_confirmed = preview[(preview["pdf_view"] == "highlight") & (preview["pdf_section"] == "confirmed_operation")]
    full_confirmed = preview[(preview["pdf_view"] == "full") & (preview["pdf_section"] == "confirmed_operation")]
    highlight_pending = preview[(preview["pdf_view"] == "highlight") & (preview["pdf_section"] == "pending_confirmation")]
    full_pending = preview[(preview["pdf_view"] == "full") & (preview["pdf_section"] == "pending_confirmation")]
    lines = [
        "# Volume Breakout Operation PDF Preview",
        "",
        f"- generated_at: `{now_text()}`",
        f"- source_confirmed_rows: `{len(rank)}`",
        f"- source_pending_rows: `{len(pending)}`",
        f"- preview_full_pending_unique_stocks: `{len(full_pending)}`",
        "- rule: preview only; PDF should not rebuild these display fields itself.",
        "- wording: PDF text uses `日期最低價` and `中位數報酬`; internal column ids stay in CSV only.",
        "",
        "## 精華版 已確認操作排名",
        "",
        *markdown_table(
            highlight_confirmed,
            [
                "display_order",
                "stock_display",
                "operation_status_zh",
                "trigger_zh",
                "entry_basis_zh",
                "stop_basis_zh",
                "sample_size",
                "win_rate_zh",
                "avg_return_zh",
                "median_return_zh",
                "confidence_zh",
            ],
        ),
        "",
        "## 精華版 待確認",
        "",
        *markdown_table(
            highlight_pending,
            [
                "display_order",
                "stock_display",
                "operation_status_zh",
                "pending_age_zh",
                "pending_group_zh",
                "stop_basis_zh",
                "same_stock_pending_count",
                "pdf_note_zh",
            ],
        ),
        "",
        "## 完整版 已確認操作排名",
        "",
        *markdown_table(
            full_confirmed,
            [
                "display_order",
                "stock_display",
                "quality_status_zh",
                "trigger_zh",
                "stop_basis_zh",
                "sample_size",
                "win_rate_zh",
                "median_return_zh",
                "research_score",
            ],
        ),
        "",
        "## 完整版 待確認",
        "",
        *markdown_table(
            full_pending,
            [
                "display_order",
                "stock_display",
                "pending_age_zh",
                "pending_group_zh",
                "stop_basis_zh",
                "same_stock_pending_count",
                "pdf_note_zh",
            ],
        ),
    ]
    PREVIEW_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    rank = read_csv(RANK_CSV)
    pending = read_csv(PENDING_CSV)
    preview = build_preview(rank, pending)
    write_csv(preview, PREVIEW_CSV)
    write_markdown(preview, rank, pending)
    print(f"Saved: {PREVIEW_CSV} rows={len(preview)}")
    print(f"Saved: {PREVIEW_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
