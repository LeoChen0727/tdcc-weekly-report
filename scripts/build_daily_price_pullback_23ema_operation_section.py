from __future__ import annotations

from datetime import datetime
import math
from pathlib import Path
import sys
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_candidate_model_layer import price_history_for_stock  # noqa: E402
from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, markdown_table, normalize_code, read_csv, safe_str, to_number, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
MODEL_SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"
MODEL_SIGNAL_LOG_CSV = ROOT / "output" / "history" / "daily_candidate_models" / "daily_candidate_model_signal_log.csv"

DAILY_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
APPROVAL_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"

OUT_CSV = LATEST_DIR / "daily_price_pullback_23ema_operation_section_latest.csv"
OUT_MD = LATEST_DIR / "daily_price_pullback_23ema_operation_section_latest.md"
AUDIT_CSV = LATEST_DIR / "daily_price_pullback_23ema_operation_evidence_audit_latest.csv"
AUDIT_MD = LATEST_DIR / "daily_price_pullback_23ema_operation_evidence_audit_latest.md"

MODEL_ID = "price_pullback_23ema"
MODEL_NAME_ZH = "23EMA回檔模型"
OPERATION_MODULE_ID = "price_pullback_23ema_prev20_breakout_stop_v1"
APPROVAL_VERSION = "price_pullback_23ema_operation_v1_20260703"
BUY_FILTER_ID = "v1_gate_return20_tdcc_high_obv"
FORMAL_SIGNAL_EFFECTIVE_FROM = "20260703"

ENTRY_RULE_ID = "signal_date_next_open"
STOP_LOSS_RULE_ID = "sustained_close_below_lower_ma20_ema23_4pct_4d"
EXIT_RULE_ID = "close_prev20_high_break_next_open"

ENTRY_BASIS_ZH = "本表股票為23EMA回檔模型通過候選，隔日開盤買入。"
EXIT_RULE_ZH = "收盤突破訊號日前20日高點後，隔日開盤賣出。"
STOP_BASIS_ZH = "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。"
WIN_DEFINITION_ZH = "勝：D+20內先觸發收盤突破訊號日前20日高點，且停損未先觸發。"
NEUTRAL_DEFINITION_ZH = "和：D+20內沒有賣出或停損，且D+20收盤報酬大於等於0%。"
FAILURE_DEFINITION_ZH = "敗：停損先觸發，或D+20內沒有賣出/停損但D+20收盤報酬小於0%。"

BASE_SAMPLE_SIZE = "1160"
BASE_WIN_RATE = "66.03%"
BASE_NEUTRAL_RATE = "5.60%"
BASE_FAILURE_RATE = "28.36%"
BASE_AVG_RETURN = "+2.90%"
TECHNICAL_SAMPLE_SIZE = "654"
TECHNICAL_WIN_RATE = "75.54%"
TECHNICAL_NEUTRAL_RATE = "3.52%"
TECHNICAL_FAILURE_RATE = "20.95%"
TECHNICAL_AVG_RETURN = "+2.96%"

PDF_VIEWS = ("highlight", "full")
PDF_SECTIONS = ("confirmed_operation", "active_operation")

SECTION_ZH = {
    "confirmed_operation": "本日可買 / 已確認買入候選",
    "active_operation": "操作中",
}
SECTION_EMPTY_NOTE_ZH = {
    "confirmed_operation": "本日無股票推薦",
    "active_operation": "目前無操作中追蹤列",
}

OUTPUT_COLUMNS = [
    "model_id",
    "model_name_zh",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "operation_asof_date",
    "operation_source_date_status",
    "report_line",
    "report_line_memberships",
    "display_order",
    "stock_id",
    "stock_name",
    "stock_display",
    "operation_status",
    "operation_status_zh",
    "operation_quality",
    "operation_quality_zh",
    "row_action_status",
    "buy_rank_eligible",
    "signal_date",
    "entry_rule_id",
    "entry_basis_zh",
    "entry_price_basis",
    "entry_date",
    "entry_price",
    "stop_loss_rule_id",
    "stop_loss_price",
    "stop_loss_label_zh",
    "stop_basis_zh",
    "exit_rule_id",
    "exit_rule_zh",
    "planned_holding_days",
    "operation_age_days",
    "target_price",
    "target_label_zh",
    "stop_confirmed_days",
    "realized_exit_date",
    "realized_exit_reason",
    "model_score",
    "reason_tags",
    "risk_tags_zh",
    "rank_reason_zh",
    "sample_size",
    "win_rate_zh",
    "neutral_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "technical_package_sample_size",
    "technical_package_win_rate_zh",
    "technical_package_neutral_rate_zh",
    "technical_package_failure_rate_zh",
    "technical_package_avg_return_zh",
    "win_definition_zh",
    "neutral_definition_zh",
    "failure_definition_zh",
    "daily_signal_date",
    "daily_model_signal_count",
    "adapter_source",
    "adapter_source_status",
    "approval_source",
    "approved_for_daily",
    "operation_module_approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "operation_directive_level",
    "buy_filter_id",
    "approval_note_zh",
    "pdf_note_zh",
    "adapter_note_zh",
    "generated_at",
]

AUDIT_COLUMNS = [
    "model_id",
    "operation_asof_date",
    "stock_id",
    "stock_name",
    "report_line",
    "signal_date",
    "entry_date",
    "operation_lifecycle_state",
    "audit_status",
    "included_in_daily_adapter",
    "exit_date",
    "exit_reason",
    "target_price",
    "stop_loss_price",
    "stop_confirmed_days",
    "reason",
    "generated_at",
]

DISPLAY_COLUMNS = [
    "pdf_view",
    "pdf_section_zh",
    "row_type",
    "report_line",
    "stock_display",
    "operation_quality_zh",
    "signal_date",
    "entry_basis_zh",
    "exit_rule_zh",
    "stop_basis_zh",
    "row_action_status",
    "buy_rank_eligible",
    "win_rate_zh",
    "neutral_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "rank_reason_zh",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def compact_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    text = text.replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""


def stock_id_key(value: Any) -> str:
    code = normalize_code(safe_str(value).replace(".0", ""))
    return code.zfill(4) if code.isdigit() else code


def true_text(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "1.0", "yes", "y"}


def format_price(value: Any) -> str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return f"{num:.2f}".rstrip("0").rstrip(".")


def main_price_date() -> str:
    freshness = read_csv(DATA_FRESHNESS_CSV, dtype=str).fillna("")
    if freshness.empty or "main_price_date" not in freshness.columns:
        return ""
    return compact_date(freshness.iloc[0].get("main_price_date"))


def approval_context(approval: pd.DataFrame) -> dict[str, str]:
    default = {
        "approval_source": APPROVAL_CSV.name,
        "approved_for_daily": "False",
        "operation_module_approved_for_daily": "False",
        "approval_status": "missing",
        "operation_module_id": "",
        "approval_version": "",
        "operation_directive_level": "no_operation_directive",
        "buy_filter_id": "",
        "approval_note_zh": "missing approved operation artifact",
    }
    if approval.empty or "model_id" not in approval.columns:
        return default
    part = approval[approval["model_id"].astype(str).eq(MODEL_ID)].copy()
    if part.empty:
        return default
    row = part.iloc[0]
    approved = true_text(row.get("approved_for_daily"))
    return {
        "approval_source": APPROVAL_CSV.name,
        "approved_for_daily": "True" if approved else "False",
        "operation_module_approved_for_daily": "True" if approved else "False",
        "approval_status": safe_str(row.get("approval_status")),
        "operation_module_id": safe_str(row.get("operation_module_id")),
        "approval_version": safe_str(row.get("approval_version")),
        "operation_directive_level": safe_str(row.get("operation_directive_level")) if approved else "no_operation_directive",
        "buy_filter_id": safe_str(row.get("buy_filter_id")),
        "approval_note_zh": safe_str(row.get("approval_note_zh")),
    }


def signal_dates(frame: pd.DataFrame) -> set[str]:
    if frame.empty or "signal_date" not in frame.columns:
        return set()
    return {date for date in frame["signal_date"].map(compact_date).tolist() if date}


def require_latest_signals_match_report_date(signals: pd.DataFrame, report_date: str) -> None:
    observed = signal_dates(signals)
    if observed and observed != {report_date}:
        raise RuntimeError(
            "price_pullback_23ema operation section requires same-date latest signals: "
            f"main_price_date={report_date or 'missing'} signal_dates={','.join(sorted(observed))}"
        )


def daily_model_signal_rows(signals: pd.DataFrame, report_date: str) -> pd.DataFrame:
    if signals.empty or "model_id" not in signals.columns:
        return pd.DataFrame()
    rows = signals[signals["model_id"].astype(str).eq(MODEL_ID)].copy()
    if rows.empty:
        return pd.DataFrame()
    rows["signal_date"] = rows.get("signal_date", pd.Series(dtype=str)).map(compact_date)
    rows["stock_id"] = rows.get("stock_id", pd.Series(dtype=str)).map(stock_id_key)
    rows = rows[(rows["signal_date"].eq(report_date)) & rows["stock_id"].ne("")].copy()
    if rows.empty:
        return pd.DataFrame()
    rows["_sort_report"] = rows.get("report_bucket", pd.Series([""] * len(rows))).astype(str)
    rows = rows.sort_values(["_sort_report", "stock_id"]).drop(columns=["_sort_report"], errors="ignore")
    return rows.reset_index(drop=True)


def signal_snapshot_paths(report_date: str) -> list[Path]:
    out: list[Path] = []
    for path in sorted(MODEL_SNAPSHOT_DIR.glob("daily_candidate_model_signals_for_report_*.csv")):
        snapshot_date = compact_date(path.stem.rsplit("_", 1)[-1])
        if snapshot_date and snapshot_date <= report_date:
            out.append(path)
    return out


def load_signal_history(current_signals: pd.DataFrame, report_date: str) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    log = read_csv(MODEL_SIGNAL_LOG_CSV, dtype=str).fillna("")
    if not log.empty and {"model_id", "signal_date"}.issubset(log.columns):
        part = log[log["model_id"].astype(str).eq(MODEL_ID)].copy()
        part["signal_date"] = part["signal_date"].map(compact_date)
        part = part[(part["signal_date"].ge(FORMAL_SIGNAL_EFFECTIVE_FROM)) & part["signal_date"].le(report_date)]
        if not part.empty:
            part["_source_priority"] = 1
            frames.append(part)
    for path in signal_snapshot_paths(report_date):
        frame = read_csv(path, dtype=str).fillna("")
        if frame.empty or "model_id" not in frame.columns:
            continue
        frame = frame[frame["model_id"].astype(str).eq(MODEL_ID)].copy()
        if frame.empty:
            continue
        frame["signal_date"] = frame.get("signal_date", pd.Series(dtype=str)).map(compact_date)
        frame = frame[(frame["signal_date"].ge(FORMAL_SIGNAL_EFFECTIVE_FROM)) & frame["signal_date"].le(report_date)]
        if frame.empty:
            continue
        frame["_source_priority"] = 2
        frames.append(frame)
    current = daily_model_signal_rows(current_signals, report_date)
    if not current.empty:
        current["_source_priority"] = 3
        frames.append(current)
    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames, ignore_index=True, sort=False)
    out["stock_id"] = out.get("stock_id", pd.Series(dtype=str)).map(stock_id_key)
    if "report_bucket" not in out.columns:
        out["report_bucket"] = ""
    out = out[(out["signal_date"] != "") & (out["stock_id"] != "")].copy()
    out["_source_priority"] = pd.to_numeric(out["_source_priority"], errors="coerce").fillna(0)
    out = out.sort_values(["signal_date", "stock_id", "report_bucket", "_source_priority"], ascending=[True, True, True, False])
    return out.drop_duplicates(["signal_date", "stock_id", "report_bucket"], keep="first").reset_index(drop=True)


def price_for_stock(stock_id: str) -> pd.DataFrame:
    price = price_history_for_stock(stock_id_key(stock_id))
    if price.empty:
        return price
    out = price.copy()
    out["date"] = out["date"].map(compact_date)
    for col in ["open", "high", "low", "close", "volume"]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.dropna(subset=["date", "open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)
    out["ma20"] = out["close"].rolling(20, min_periods=20).mean()
    out["ema23"] = out["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    return out


def index_for_date_or_before(price: pd.DataFrame, date: str) -> int | None:
    if price.empty:
        return None
    matches = price.index[price["date"].astype(str).le(compact_date(date))].tolist()
    return int(matches[-1]) if matches else None


def exact_index_for_date(price: pd.DataFrame, date: str) -> int | None:
    matches = price.index[price["date"].astype(str).eq(compact_date(date))].tolist()
    return int(matches[0]) if matches else None


def prev20_high_before_signal(price: pd.DataFrame, signal_idx: int) -> float:
    start = max(0, signal_idx - 20)
    window = price.iloc[start:signal_idx]
    if window.empty:
        return math.nan
    return to_number(window["high"].max())


def lower_ma_stop_price(price_row: pd.Series) -> float:
    ma20 = to_number(price_row.get("ma20"))
    ema23 = to_number(price_row.get("ema23"))
    refs = [value for value in [ma20, ema23] if not math.isnan(value) and value > 0]
    if not refs:
        return math.nan
    return min(refs) * 0.96


def operation_lifecycle(row: pd.Series, report_date: str) -> dict[str, Any]:
    price = price_for_stock(row.get("stock_id"))
    if price.empty:
        return {"state": "blocked_no_price_history", "included": False}
    signal_date = compact_date(row.get("signal_date"))
    signal_idx = exact_index_for_date(price, signal_date)
    asof_idx = index_for_date_or_before(price, report_date)
    if signal_idx is None or asof_idx is None:
        return {"state": "blocked_missing_signal_or_asof_price", "included": False}
    entry_idx = signal_idx + 1
    target_price = prev20_high_before_signal(price, signal_idx)
    if entry_idx >= len(price):
        return {
            "state": "pending_next_open_entry",
            "included": False,
            "target_price": target_price,
            "stop_price": math.nan,
        }
    if asof_idx < entry_idx:
        return {
            "state": "pending_next_open_entry",
            "included": False,
            "target_price": target_price,
            "entry_date": safe_str(price.iloc[entry_idx].get("date")),
            "entry_price": to_number(price.iloc[entry_idx].get("open")),
            "stop_price": math.nan,
        }

    stop_days = 0
    max_idx = min(asof_idx, entry_idx + 19)
    for idx in range(entry_idx, max_idx + 1):
        current = price.iloc[idx]
        close = to_number(current.get("close"))
        stop_price = lower_ma_stop_price(current)
        if not math.isnan(target_price) and not math.isnan(close) and close > target_price:
            return {
                "state": "target_exit_pending_next_open" if idx == asof_idx else "exited",
                "included": idx == asof_idx,
                "exit_date": safe_str(price.iloc[idx + 1].get("date")) if idx + 1 < len(price) else "",
                "exit_reason": "close_prev20_high_break_next_open",
                "target_price": target_price,
                "stop_price": stop_price,
                "stop_confirmed_days": stop_days,
                "entry_date": safe_str(price.iloc[entry_idx].get("date")),
                "entry_price": to_number(price.iloc[entry_idx].get("open")),
                "operation_age_days": idx - entry_idx + 1,
            }
        if not math.isnan(stop_price) and not math.isnan(close) and close <= stop_price:
            stop_days += 1
        else:
            stop_days = 0
        if stop_days >= 4:
            return {
                "state": "stop_exit_pending_next_open" if idx == asof_idx else "exited",
                "included": idx == asof_idx,
                "exit_date": safe_str(price.iloc[idx + 1].get("date")) if idx + 1 < len(price) else "",
                "exit_reason": "sustained_close_below_lower_ma20_ema23_4pct_4d",
                "target_price": target_price,
                "stop_price": stop_price,
                "stop_confirmed_days": stop_days,
                "entry_date": safe_str(price.iloc[entry_idx].get("date")),
                "entry_price": to_number(price.iloc[entry_idx].get("open")),
                "operation_age_days": idx - entry_idx + 1,
            }
    if asof_idx >= entry_idx + 19:
        return {
            "state": "expired_d20_no_active_tracking",
            "included": False,
            "target_price": target_price,
            "entry_date": safe_str(price.iloc[entry_idx].get("date")),
            "entry_price": to_number(price.iloc[entry_idx].get("open")),
        }
    current_stop = lower_ma_stop_price(price.iloc[asof_idx])
    return {
        "state": "active_operation",
        "included": True,
        "target_price": target_price,
        "stop_price": current_stop,
        "stop_confirmed_days": stop_days,
        "entry_date": safe_str(price.iloc[entry_idx].get("date")),
        "entry_price": to_number(price.iloc[entry_idx].get("open")),
        "operation_age_days": asof_idx - entry_idx + 1,
    }


def quality_status(row: pd.Series) -> tuple[str, str]:
    quality = safe_str(row.get("price_pullback_operation_quality")) or "base"
    if quality == "technical_strength":
        return "technical_strength", "技術強勢"
    return "base", "基礎"


def reason_text(row: pd.Series) -> str:
    quality, quality_zh = quality_status(row)
    reasons = ["20日漲幅0~25%", "TDCC高門檻增加", "OBV站上MA20"]
    if quality == "technical_strength":
        reasons.append("RSI>=60且MACD轉強")
    if "tdcc_all_thresholds_up" in safe_str(row.get("price_pullback_reason_tags")):
        reasons.append("籌碼全同步")
    return f"{quality_zh}；" + "、".join(reasons)


def risk_text(row: pd.Series) -> str:
    return "帶量紅K追價風險" if "volume_red_or_solid_red" in safe_str(row.get("price_pullback_risk_tags")) else ""


def base_row(
    row: pd.Series,
    approval: dict[str, str],
    report_date: str,
    daily_signal_count: int,
    generated_at: str,
    pdf_view: str,
    pdf_section: str,
) -> dict[str, str]:
    quality, quality_zh = quality_status(row)
    stock_id = stock_id_key(row.get("stock_id"))
    stock_name = safe_str(row.get("stock_name"))
    return {
        "model_id": MODEL_ID,
        "model_name_zh": MODEL_NAME_ZH,
        "pdf_view": pdf_view,
        "pdf_section": pdf_section,
        "pdf_section_zh": SECTION_ZH[pdf_section],
        "row_type": "data",
        "operation_asof_date": report_date,
        "operation_source_date_status": "current_report_date",
        "report_line": safe_str(row.get("report_bucket")) or safe_str(row.get("report_line")),
        "report_line_memberships": safe_str(row.get("report_line_memberships")) or safe_str(row.get("report_bucket")),
        "display_order": "",
        "stock_id": stock_id,
        "stock_name": stock_name,
        "stock_display": f"{stock_id} {stock_name}".strip(),
        "operation_status": pdf_section,
        "operation_status_zh": SECTION_ZH[pdf_section],
        "operation_quality": quality,
        "operation_quality_zh": quality_zh,
        "row_action_status": "",
        "buy_rank_eligible": "False",
        "signal_date": compact_date(row.get("signal_date")),
        "entry_rule_id": ENTRY_RULE_ID,
        "entry_basis_zh": ENTRY_BASIS_ZH,
        "entry_price_basis": "next_trading_day_open",
        "entry_date": "",
        "entry_price": "",
        "stop_loss_rule_id": STOP_LOSS_RULE_ID,
        "stop_loss_price": "",
        "stop_loss_label_zh": "",
        "stop_basis_zh": STOP_BASIS_ZH,
        "exit_rule_id": EXIT_RULE_ID,
        "exit_rule_zh": EXIT_RULE_ZH,
        "planned_holding_days": "20",
        "operation_age_days": "",
        "target_price": "",
        "target_label_zh": "訊號日前20日高點",
        "stop_confirmed_days": "",
        "realized_exit_date": "",
        "realized_exit_reason": "",
        "model_score": safe_str(row.get("model_score")),
        "reason_tags": safe_str(row.get("price_pullback_reason_tags")),
        "risk_tags_zh": risk_text(row),
        "rank_reason_zh": reason_text(row),
        "sample_size": BASE_SAMPLE_SIZE,
        "win_rate_zh": BASE_WIN_RATE,
        "neutral_rate_zh": BASE_NEUTRAL_RATE,
        "failure_rate_zh": BASE_FAILURE_RATE,
        "avg_return_zh": BASE_AVG_RETURN,
        "technical_package_sample_size": TECHNICAL_SAMPLE_SIZE,
        "technical_package_win_rate_zh": TECHNICAL_WIN_RATE,
        "technical_package_neutral_rate_zh": TECHNICAL_NEUTRAL_RATE,
        "technical_package_failure_rate_zh": TECHNICAL_FAILURE_RATE,
        "technical_package_avg_return_zh": TECHNICAL_AVG_RETURN,
        "win_definition_zh": WIN_DEFINITION_ZH,
        "neutral_definition_zh": NEUTRAL_DEFINITION_ZH,
        "failure_definition_zh": FAILURE_DEFINITION_ZH,
        "daily_signal_date": report_date,
        "daily_model_signal_count": str(daily_signal_count),
        "adapter_source": "daily_candidate_model_signal_log+daily_published_model_snapshots+stock_price_history",
        "adapter_source_status": "ready",
        "approval_source": safe_str(approval.get("approval_source")),
        "approved_for_daily": safe_str(approval.get("approved_for_daily")),
        "operation_module_approved_for_daily": safe_str(approval.get("operation_module_approved_for_daily")),
        "approval_status": safe_str(approval.get("approval_status")),
        "operation_module_id": safe_str(approval.get("operation_module_id")),
        "approval_version": safe_str(approval.get("approval_version")),
        "operation_directive_level": safe_str(approval.get("operation_directive_level")),
        "buy_filter_id": safe_str(approval.get("buy_filter_id")),
        "approval_note_zh": safe_str(approval.get("approval_note_zh")),
        "pdf_note_zh": "",
        "adapter_note_zh": "model-owned operation row; PDF must not infer lifecycle from candidate signals",
        "generated_at": generated_at,
    }


def confirmed_rows(row: pd.Series, approval: dict[str, str], report_date: str, count: int, generated_at: str) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for view in PDF_VIEWS:
        item = base_row(row, approval, report_date, count, generated_at, view, "confirmed_operation")
        item["row_action_status"] = "confirmed_buy_candidate"
        item["buy_rank_eligible"] = "True"
        item["pdf_note_zh"] = "買入：隔日開盤買入。"
        out.append(item)
    return out


def active_rows(row: pd.Series, approval: dict[str, str], report_date: str, count: int, generated_at: str) -> tuple[list[dict[str, str]], dict[str, str]]:
    state = operation_lifecycle(row, report_date)
    audit = audit_row(row, report_date, generated_at, safe_str(state.get("state")), "False", safe_str(state.get("state")))
    if not state.get("included"):
        audit["exit_date"] = safe_str(state.get("exit_date"))
        audit["exit_reason"] = safe_str(state.get("exit_reason"))
        audit["target_price"] = format_price(state.get("target_price"))
        audit["stop_loss_price"] = format_price(state.get("stop_price"))
        audit["stop_confirmed_days"] = safe_str(state.get("stop_confirmed_days"))
        return [], audit
    out: list[dict[str, str]] = []
    action = safe_str(state.get("state"))
    for view in PDF_VIEWS:
        item = base_row(row, approval, report_date, count, generated_at, view, "active_operation")
        item["row_action_status"] = action
        item["entry_date"] = safe_str(state.get("entry_date"))
        item["entry_price"] = format_price(state.get("entry_price"))
        item["target_price"] = format_price(state.get("target_price"))
        item["stop_loss_price"] = format_price(state.get("stop_price"))
        item["stop_loss_label_zh"] = "MA20/EMA23較低者向下4%"
        item["stop_confirmed_days"] = safe_str(state.get("stop_confirmed_days"))
        item["operation_age_days"] = safe_str(state.get("operation_age_days"))
        item["realized_exit_date"] = safe_str(state.get("exit_date"))
        item["realized_exit_reason"] = safe_str(state.get("exit_reason"))
        if action == "target_exit_pending_next_open":
            item["pdf_note_zh"] = "收盤突破訊號日前20日高點後，隔日開盤賣出。"
        elif action == "stop_exit_pending_next_open":
            item["pdf_note_zh"] = "停損條件已確認，隔日開盤停損。"
        else:
            item["pdf_note_zh"] = "操作中，依正式賣出/停損規則追蹤。"
        out.append(item)
    audit["included_in_daily_adapter"] = "True"
    audit["target_price"] = format_price(state.get("target_price"))
    audit["stop_loss_price"] = format_price(state.get("stop_price"))
    audit["stop_confirmed_days"] = safe_str(state.get("stop_confirmed_days"))
    audit["entry_date"] = safe_str(state.get("entry_date"))
    return out, audit


def audit_row(row: pd.Series, report_date: str, generated_at: str, audit_status: str, included: str, reason: str) -> dict[str, str]:
    return {
        "model_id": MODEL_ID,
        "operation_asof_date": report_date,
        "stock_id": stock_id_key(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "report_line": safe_str(row.get("report_bucket")) or safe_str(row.get("report_line")),
        "signal_date": compact_date(row.get("signal_date")),
        "entry_date": "",
        "operation_lifecycle_state": reason,
        "audit_status": audit_status,
        "included_in_daily_adapter": included,
        "exit_date": "",
        "exit_reason": "",
        "target_price": "",
        "stop_loss_price": "",
        "stop_confirmed_days": "",
        "reason": reason,
        "generated_at": generated_at,
    }


def empty_row(pdf_view: str, pdf_section: str, report_date: str, daily_signal_count: int, approval: dict[str, str], generated_at: str) -> dict[str, str]:
    return {
        "model_id": MODEL_ID,
        "model_name_zh": MODEL_NAME_ZH,
        "pdf_view": pdf_view,
        "pdf_section": pdf_section,
        "pdf_section_zh": SECTION_ZH[pdf_section],
        "row_type": "empty_state",
        "operation_asof_date": report_date,
        "operation_source_date_status": "current_report_date",
        "report_line": "both",
        "report_line_memberships": "mainstream|non_mainstream",
        "display_order": "999999",
        "stock_id": "",
        "stock_name": "",
        "stock_display": SECTION_EMPTY_NOTE_ZH[pdf_section],
        "operation_status": pdf_section,
        "operation_status_zh": SECTION_EMPTY_NOTE_ZH[pdf_section],
        "operation_quality": "empty_state",
        "operation_quality_zh": "",
        "row_action_status": "empty_state",
        "buy_rank_eligible": "False",
        "signal_date": "",
        "entry_rule_id": ENTRY_RULE_ID,
        "entry_basis_zh": ENTRY_BASIS_ZH,
        "entry_price_basis": "",
        "entry_date": "",
        "entry_price": "",
        "stop_loss_rule_id": STOP_LOSS_RULE_ID,
        "stop_loss_price": "",
        "stop_loss_label_zh": "",
        "stop_basis_zh": STOP_BASIS_ZH,
        "exit_rule_id": EXIT_RULE_ID,
        "exit_rule_zh": EXIT_RULE_ZH,
        "planned_holding_days": "20",
        "operation_age_days": "",
        "target_price": "",
        "target_label_zh": "訊號日前20日高點",
        "stop_confirmed_days": "",
        "realized_exit_date": "",
        "realized_exit_reason": "",
        "model_score": "",
        "reason_tags": "",
        "risk_tags_zh": "",
        "rank_reason_zh": "",
        "sample_size": BASE_SAMPLE_SIZE,
        "win_rate_zh": BASE_WIN_RATE,
        "neutral_rate_zh": BASE_NEUTRAL_RATE,
        "failure_rate_zh": BASE_FAILURE_RATE,
        "avg_return_zh": BASE_AVG_RETURN,
        "technical_package_sample_size": TECHNICAL_SAMPLE_SIZE,
        "technical_package_win_rate_zh": TECHNICAL_WIN_RATE,
        "technical_package_neutral_rate_zh": TECHNICAL_NEUTRAL_RATE,
        "technical_package_failure_rate_zh": TECHNICAL_FAILURE_RATE,
        "technical_package_avg_return_zh": TECHNICAL_AVG_RETURN,
        "win_definition_zh": WIN_DEFINITION_ZH,
        "neutral_definition_zh": NEUTRAL_DEFINITION_ZH,
        "failure_definition_zh": FAILURE_DEFINITION_ZH,
        "daily_signal_date": report_date,
        "daily_model_signal_count": str(daily_signal_count),
        "adapter_source": "daily_candidate_model_signal_log+daily_published_model_snapshots+stock_price_history",
        "adapter_source_status": "ready",
        "approval_source": safe_str(approval.get("approval_source")),
        "approved_for_daily": safe_str(approval.get("approved_for_daily")),
        "operation_module_approved_for_daily": safe_str(approval.get("operation_module_approved_for_daily")),
        "approval_status": safe_str(approval.get("approval_status")),
        "operation_module_id": safe_str(approval.get("operation_module_id")),
        "approval_version": safe_str(approval.get("approval_version")),
        "operation_directive_level": safe_str(approval.get("operation_directive_level")),
        "buy_filter_id": safe_str(approval.get("buy_filter_id")),
        "approval_note_zh": safe_str(approval.get("approval_note_zh")),
        "pdf_note_zh": SECTION_EMPTY_NOTE_ZH[pdf_section],
        "adapter_note_zh": "explicit model-owned empty state; PDF must not infer missing lifecycle rows",
        "generated_at": generated_at,
    }


def build_section(signals: pd.DataFrame, approval_frame: pd.DataFrame, report_date: str, generated_at: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    current = daily_model_signal_rows(signals, report_date)
    history = load_signal_history(signals, report_date)
    approval = approval_context(approval_frame)
    daily_signal_count = int(current["stock_id"].nunique()) if not current.empty else 0

    active_candidates = pd.DataFrame()
    if not history.empty:
        active_candidates = history[history["signal_date"].map(compact_date).lt(report_date)].copy()

    rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    active_by_key: dict[tuple[str, str], tuple[str, list[dict[str, str]], dict[str, str]]] = {}
    for _, row in active_candidates.iterrows():
        active, audit = active_rows(row, approval, report_date, daily_signal_count, generated_at)
        audit_rows.append(audit)
        if not active:
            continue
        key = (stock_id_key(row.get("stock_id")), safe_str(row.get("report_bucket")) or safe_str(row.get("report_line")))
        signal_date = compact_date(row.get("signal_date"))
        existing = active_by_key.get(key)
        if existing is None or signal_date >= existing[0]:
            active_by_key[key] = (signal_date, active, audit)

    active_keys = set(active_by_key)
    for display_order, (_key, (_signal_date, active, _audit)) in enumerate(sorted(active_by_key.items()), start=1):
        for item in active:
            item["display_order"] = str(display_order)
            rows.append(item)

    confirmed_order = 1
    for _, row in current.iterrows():
        key = (stock_id_key(row.get("stock_id")), safe_str(row.get("report_bucket")) or safe_str(row.get("report_line")))
        if key in active_keys:
            audit_rows.append(audit_row(row, report_date, generated_at, "suppressed_existing_active_position", "False", "same_stock_already_active"))
            continue
        for item in confirmed_rows(row, approval, report_date, daily_signal_count, generated_at):
            item["display_order"] = str(confirmed_order)
            rows.append(item)
        audit_rows.append(audit_row(row, report_date, generated_at, "candidate_evaluated", "True", "confirmed_operation"))
        confirmed_order += 1

    existing = {(row["pdf_view"], row["pdf_section"]) for row in rows if row["row_type"] == "data"}
    for view in PDF_VIEWS:
        for section in PDF_SECTIONS:
            if (view, section) not in existing:
                rows.append(empty_row(view, section, report_date, daily_signal_count, approval, generated_at))
    if not audit_rows:
        audit_rows.append(
            {
                "model_id": MODEL_ID,
                "operation_asof_date": report_date,
                "stock_id": "",
                "stock_name": "",
                "report_line": "both",
                "signal_date": "",
                "entry_date": "",
                "operation_lifecycle_state": "empty_state",
                "audit_status": "empty_state",
                "included_in_daily_adapter": "True",
                "exit_date": "",
                "exit_reason": "",
                "target_price": "",
                "stop_loss_price": "",
                "stop_confirmed_days": "",
                "reason": "no current confirmed rows and no active operation rows",
                "generated_at": generated_at,
            }
        )

    out = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    out["_view_order"] = out["pdf_view"].map({"highlight": 0, "full": 1}).fillna(9)
    out["_section_order"] = out["pdf_section"].map({"confirmed_operation": 0, "active_operation": 1}).fillna(9)
    out["_row_type_order"] = out["row_type"].map({"data": 0, "empty_state": 1}).fillna(9)
    out["_display_order_num"] = pd.to_numeric(out["display_order"], errors="coerce").fillna(999999)
    out = out.sort_values(["_view_order", "_section_order", "_row_type_order", "_display_order_num", "stock_id"])
    section = out.drop(columns=["_view_order", "_section_order", "_row_type_order", "_display_order_num"]).reset_index(drop=True)
    audit = pd.DataFrame(audit_rows, columns=AUDIT_COLUMNS)
    return section, audit


def write_outputs(section: pd.DataFrame, audit: pd.DataFrame) -> None:
    write_csv(section, OUT_CSV)
    lines = [
        "# price_pullback_23ema Daily Operation Section",
        "",
        "- Producer owner: `daily_model_maintenance`.",
        "- Digest/highlight view uses `confirmed_operation` and `active_operation` only.",
        "- This adapter does not rank stocks inside the model.",
        "",
        markdown_table(section, DISPLAY_COLUMNS, limit=160),
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8", newline="\n")

    write_csv(audit, AUDIT_CSV)
    audit_lines = [
        "# price_pullback_23ema Daily Operation Evidence Audit",
        "",
        "- Audit rows record model-side lifecycle decisions and suppressed duplicate active positions.",
        "",
        markdown_table(audit, AUDIT_COLUMNS, limit=200),
        "",
    ]
    AUDIT_MD.write_text("\n".join(audit_lines), encoding="utf-8", newline="\n")

    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    for path in (OUT_CSV, OUT_MD, AUDIT_CSV, AUDIT_MD):
        (DOCS_LATEST_DIR / path.name).write_bytes(path.read_bytes())


def main() -> int:
    signals = read_csv(DAILY_SIGNALS_CSV, dtype=str).fillna("")
    approval = read_csv(APPROVAL_CSV, dtype=str).fillna("")
    report_date = main_price_date()
    require_latest_signals_match_report_date(signals, report_date)
    section, audit = build_section(signals, approval, report_date, now_text())
    write_outputs(section, audit)
    print(f"Saved: {OUT_CSV} rows={len(section)}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {AUDIT_CSV} rows={len(audit)}")
    print(f"Saved: {AUDIT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
