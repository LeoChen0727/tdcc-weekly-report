from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import math
from pathlib import Path
import sys
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_candidate_model_layer import (  # noqa: E402
    detected_w_bottom_context,
    price_history_for_stock,
    normalize_code,
)
from daily_snapshot_revision_utils import (  # noqa: E402
    SnapshotRevision,
    select_latest_snapshot_revisions,
)
from tracking_utils import markdown_table, read_csv, safe_str, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
MODEL_SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"
MODEL_SIGNAL_LOG_CSV = ROOT / "output" / "history" / "daily_candidate_models" / "daily_candidate_model_signal_log.csv"

DAILY_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
APPROVAL_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"

ADAPTER_SOURCE = "daily_candidate_model_signal_log+daily_published_model_snapshots+production_w_bottom_detector+stock_price_history"
APPROVAL_SOURCE = "approved_operation_patterns_latest.csv"
PDF_VIEWS = ("highlight", "full")
PDF_SECTIONS = ("confirmed_operation", "active_operation")

W_BOTTOM_MODEL_ID = "w_bottom_right_side"
NECKLINE_MODEL_ID = "neckline_volume_breakout_confirmation"


@dataclass(frozen=True)
class ModelConfig:
    model_id: str
    output_prefix: str
    approved_operation_status: str
    entry_rule_id: str
    entry_basis_zh: str
    stop_loss_rule_id: str
    stop_basis_zh: str
    exit_rule_id: str
    exit_rule_zh: str
    planned_holding_days: int
    confirmed_status_zh: str
    active_status_zh: str


MODEL_CONFIGS = {
    W_BOTTOM_MODEL_ID: ModelConfig(
        model_id=W_BOTTOM_MODEL_ID,
        output_prefix="daily_w_bottom_right_side_operation_section",
        approved_operation_status="approved_operation_v2",
        entry_rule_id="right_low_signal_next_open",
        entry_basis_zh="右低點觀察訊號成立後，下一個交易日開盤買進。",
        stop_loss_rule_id="w_structure_low_close_stop",
        stop_basis_zh="收盤跌破 W 結構低點出場；W 結構低點為偵測到的左低點與右低點較低者。",
        exit_rule_id="d20_gain10_else_d40_close",
        exit_rule_zh="若 D+20 收盤報酬達 +10% 則 D+20 收盤出場；否則持有到 D+40 收盤，除非先觸發 W 結構低點收盤停損。",
        planned_holding_days=40,
        confirmed_status_zh="本日可買 / W底右低點早期進場候選",
        active_status_zh="操作中 / W底右低點早期進場追蹤",
    ),
    NECKLINE_MODEL_ID: ModelConfig(
        model_id=NECKLINE_MODEL_ID,
        output_prefix="daily_neckline_volume_breakout_confirmation_operation_section",
        approved_operation_status="approved_operation_v1",
        entry_rule_id="close_ge_1pct_within_3_sessions_next_open",
        entry_basis_zh="W底頸線帶量突破確認訊號成立後，下一個交易日開盤買進。",
        stop_loss_rule_id="no_fixed_stop_loss_20d_operation_rule",
        stop_basis_zh="v1 不升級固定收盤停損；以 20 個交易日操作規則判定勝、和、敗。",
        exit_rule_id="tp10_close_win_5pct_pullback_neutral_else_20d_close_loss",
        exit_rule_zh="20 個交易日內收盤報酬先達 +10% 為勝；先達 +5% 後回落到 <= +5% 且未達 +10% 為和局；否則第 20 日收盤歸為操作規則敗。",
        planned_holding_days=20,
        confirmed_status_zh="本日可買 / W底頸線帶量突破確認候選",
        active_status_zh="操作中 / W底頸線帶量突破確認追蹤",
    ),
}

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
    "quality_status_zh",
    "row_action_status",
    "buy_rank_eligible",
    "signal_date",
    "entry_rule_id",
    "entry_basis_zh",
    "entry_price_basis",
    "entry_date",
    "entry_price",
    "entry_price_status_zh",
    "stop_loss_rule_id",
    "stop_loss_price",
    "stop_loss_label_zh",
    "stop_basis_zh",
    "exit_rule_id",
    "exit_rule_zh",
    "planned_holding_days",
    "operation_age_days",
    "left_low_date",
    "right_low_date",
    "w_structure_low_price",
    "neckline_price",
    "neckline_distance_pct",
    "model_score",
    "operation_score",
    "tdcc_score",
    "pattern_score",
    "risk_penalty",
    "final_rank_score",
    "rank_reason_zh",
    "risk_tags_zh",
    "tdcc_status_zh",
    "sample_size",
    "win_rate_zh",
    "avg_return_zh",
    "median_return_zh",
    "row_metric_status",
    "row_metric_scope",
    "row_metric_id",
    "row_metric_label_zh",
    "row_metric_matched_add_score_ids",
    "row_metric_sample_size",
    "row_metric_win_rate_zh",
    "row_metric_neutral_rate_zh",
    "row_metric_failure_rate_zh",
    "row_metric_avg_return_zh",
    "row_metric_median_return_zh",
    "row_metric_source",
    "row_metric_selection_status",
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
    "stop_loss_price",
    "left_low_date",
    "right_low_date",
    "neckline_price",
    "reason",
    "adapter_source",
    "generated_at",
]

DISPLAY_COLUMNS = [
    "pdf_view",
    "pdf_section_zh",
    "row_type",
    "report_line",
    "stock_display",
    "operation_status_zh",
    "entry_date",
    "entry_price",
    "stop_loss_price",
    "operation_age_days",
    "win_rate_zh",
    "avg_return_zh",
    "median_return_zh",
    "row_action_status",
    "buy_rank_eligible",
]

AUDIT_DISPLAY_COLUMNS = [
    "model_id",
    "operation_asof_date",
    "stock_id",
    "stock_name",
    "report_line",
    "signal_date",
    "entry_date",
    "audit_status",
    "included_in_daily_adapter",
    "operation_lifecycle_state",
    "exit_date",
    "exit_reason",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def normalize_date_text(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    text = text.replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""


def stock_id_key(value: Any) -> str:
    code = normalize_code(safe_str(value).replace(".0", ""))
    return code.zfill(4) if code.isdigit() else code


def number_text(value: Any) -> float:
    text = safe_str(value).replace("%", "").replace("+", "").replace(",", "")
    if not text:
        return math.nan
    try:
        return float(text)
    except Exception:
        return math.nan


def format_price(value: Any) -> str:
    num = number_text(value)
    if math.isnan(num):
        return ""
    return f"{num:.2f}".rstrip("0").rstrip(".")


def format_pct(value: Any) -> str:
    num = number_text(value)
    if math.isnan(num):
        return ""
    return f"{num:.2f}%"


def true_text(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "1.0", "yes", "y", "t"}


def output_paths(config: ModelConfig) -> tuple[Path, Path, Path, Path]:
    csv_path = LATEST_DIR / f"{config.output_prefix}_latest.csv"
    md_path = LATEST_DIR / f"{config.output_prefix}_latest.md"
    audit_csv_path = LATEST_DIR / f"{config.output_prefix.replace('operation_section', 'operation_evidence_audit')}_latest.csv"
    audit_md_path = LATEST_DIR / f"{config.output_prefix.replace('operation_section', 'operation_evidence_audit')}_latest.md"
    return csv_path, md_path, audit_csv_path, audit_md_path


def main_price_date() -> str:
    freshness = read_csv(DATA_FRESHNESS_CSV, dtype=str).fillna("")
    if freshness.empty or "main_price_date" not in freshness.columns:
        return ""
    return normalize_date_text(freshness.iloc[0].get("main_price_date"))


def signal_dates(frame: pd.DataFrame) -> set[str]:
    if frame.empty or "signal_date" not in frame.columns:
        return set()
    return {date for date in frame["signal_date"].map(normalize_date_text).tolist() if date}


def require_latest_signals_match_report_date(signals: pd.DataFrame, report_date: str) -> None:
    report_date = normalize_date_text(report_date)
    observed = signal_dates(signals)
    if not observed:
        return
    if observed != {report_date}:
        raise RuntimeError(
            "daily W-bottom operation sections require same-date latest signals: "
            f"main_price_date={report_date or 'missing'} signal_dates={','.join(sorted(observed))}"
        )


def approval_context(approval: pd.DataFrame, config: ModelConfig) -> dict[str, str]:
    default = {
        "approval_source": APPROVAL_SOURCE,
        "approved_for_daily": "False",
        "operation_module_approved_for_daily": "False",
        "approval_status": "missing",
        "operation_module_id": "",
        "approval_version": "",
        "operation_directive_level": "no_operation_directive",
        "buy_filter_id": "",
        "approval_note_zh": "missing approved operation artifact",
        "sample_size": "",
        "win_rate_zh": "",
        "avg_return_zh": "",
        "median_return_zh": "",
    }
    if approval.empty or "model_id" not in approval.columns:
        return default
    part = approval[approval["model_id"].astype(str).str.strip().eq(config.model_id)].copy()
    if part.empty:
        return default
    row = part.iloc[0]
    approved = true_text(row.get("approved_for_daily"))
    return {
        "approval_source": APPROVAL_SOURCE,
        "approved_for_daily": "True" if approved else "False",
        "operation_module_approved_for_daily": "True" if approved else "False",
        "approval_status": safe_str(row.get("approval_status")),
        "operation_module_id": safe_str(row.get("operation_module_id")),
        "approval_version": safe_str(row.get("approval_version")),
        "operation_directive_level": safe_str(row.get("operation_directive_level")) if approved else "no_operation_directive",
        "buy_filter_id": safe_str(row.get("buy_filter_id")),
        "approval_note_zh": safe_str(row.get("approval_note_zh")),
        "sample_size": safe_str(row.get("best_evidence_sample_size")),
        "win_rate_zh": format_pct(row.get("best_evidence_win_rate")),
        "avg_return_zh": format_pct(row.get("best_evidence_avg_return")),
        "median_return_zh": format_pct(row.get("best_evidence_median_return")),
    }


def daily_model_signal_rows(signals: pd.DataFrame, config: ModelConfig, report_date: str) -> pd.DataFrame:
    if signals.empty or "model_id" not in signals.columns:
        return pd.DataFrame()
    rows = signals[signals["model_id"].astype(str).str.strip().eq(config.model_id)].copy()
    if rows.empty:
        return pd.DataFrame()
    report_date = normalize_date_text(report_date)
    if report_date and "signal_date" in rows.columns:
        rows = rows[rows["signal_date"].map(normalize_date_text).eq(report_date)].copy()
    if rows.empty:
        return pd.DataFrame()
    if "display_rank" in rows.columns:
        rows["_display_order"] = pd.to_numeric(rows["display_rank"], errors="coerce")
    elif "model_rank" in rows.columns:
        rows["_display_order"] = pd.to_numeric(rows["model_rank"], errors="coerce")
    else:
        rows["_display_order"] = range(1, len(rows) + 1)
    rows["_display_order"] = rows["_display_order"].fillna(999999)
    rows["stock_id"] = rows["stock_id"].map(stock_id_key)
    return rows.sort_values(["_display_order", "stock_id"]).drop(columns=["_display_order"], errors="ignore")


def signal_snapshot_paths(report_date: str) -> list[SnapshotRevision]:
    return list(
        select_latest_snapshot_revisions(
            MODEL_SNAPSHOT_DIR,
            "model_signals_for_report",
            through_date=normalize_date_text(report_date),
            repository_root=ROOT,
        )
    )


def collapse_signal_history_rows(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return frame
    work = frame.copy()
    if "_source_priority" not in work.columns:
        work["_source_priority"] = 0
    if "display_rank" in work.columns:
        work["_display_order"] = pd.to_numeric(work["display_rank"], errors="coerce")
    elif "model_rank" in work.columns:
        work["_display_order"] = pd.to_numeric(work["model_rank"], errors="coerce")
    else:
        work["_display_order"] = math.nan
    work["_source_priority"] = pd.to_numeric(work["_source_priority"], errors="coerce").fillna(0)
    work["_display_order"] = work["_display_order"].fillna(999999)
    work = work.sort_values(
        ["signal_date", "stock_id", "model_id", "_source_priority", "_display_order"],
        ascending=[True, True, True, False, True],
    )

    rows: list[dict[str, Any]] = []
    for _, part in work.groupby(["signal_date", "stock_id", "model_id", "report_bucket"], sort=False, dropna=False):
        record: dict[str, Any] = {}
        for col in work.columns:
            if col in {"_source_priority", "_display_order"}:
                continue
            values = [safe_str(value) for value in part[col].tolist() if safe_str(value)]
            record[col] = values[0] if values else ""
        rows.append(record)
    return pd.DataFrame(rows)


def load_signal_history(current_signals: pd.DataFrame, config: ModelConfig, report_date: str) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    signal_log = read_csv(MODEL_SIGNAL_LOG_CSV, dtype=str).fillna("")
    if not signal_log.empty and {"model_id", "signal_date"}.issubset(signal_log.columns):
        signal_log = signal_log[
            signal_log["model_id"].astype(str).str.strip().eq(config.model_id)
            & signal_log["signal_date"].map(normalize_date_text).le(report_date)
        ].copy()
        if not signal_log.empty:
            signal_log["snapshot_report_date"] = signal_log["signal_date"].map(normalize_date_text)
            signal_log["_source_priority"] = 1
            frames.append(signal_log)

    for snapshot in signal_snapshot_paths(report_date):
        frame = read_csv(snapshot.path, dtype=str).fillna("")
        if frame.empty or "model_id" not in frame.columns:
            continue
        frame = frame[frame["model_id"].astype(str).str.strip().eq(config.model_id)].copy()
        if frame.empty:
            continue
        frame["snapshot_report_date"] = snapshot.report_date
        frame["_source_priority"] = 2
        frames.append(frame)

    current = daily_model_signal_rows(current_signals, config, report_date)
    if not current.empty:
        current = current.copy()
        current["snapshot_report_date"] = normalize_date_text(report_date)
        current["_source_priority"] = 3
        frames.append(current)

    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames, ignore_index=True, sort=False)
    out["signal_date"] = out.get("signal_date", pd.Series(dtype=str)).map(normalize_date_text)
    out["stock_id"] = out.get("stock_id", pd.Series(dtype=str)).map(stock_id_key)
    if "report_bucket" not in out.columns:
        out["report_bucket"] = ""
    out = out[(out["signal_date"] != "") & (out["stock_id"] != "")].copy()
    out = collapse_signal_history_rows(out)
    return out.sort_values(["signal_date", "stock_id", "report_bucket"]).reset_index(drop=True)


def price_for_stock(stock_id: str) -> pd.DataFrame:
    price = price_history_for_stock(stock_id_key(stock_id))
    if price.empty:
        return price
    out = price.copy()
    out["date"] = out["date"].map(normalize_date_text)
    out = out[out["date"].astype(str).str.len().eq(8)].copy()
    for col in ["open", "high", "low", "close"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    return out.dropna(subset=["open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)


def index_for_date(price: pd.DataFrame, date: str) -> int | None:
    matches = price.index[price["date"].astype(str).eq(normalize_date_text(date))].tolist()
    return int(matches[0]) if matches else None


def next_trading_index(price: pd.DataFrame, signal_idx: int) -> int | None:
    idx = signal_idx + 1
    return idx if idx < len(price) else None


def context_for_signal(row: pd.Series) -> dict[str, Any]:
    source = pd.Series(
        {
            "stock_id": stock_id_key(row.get("stock_id")),
            "signal_date": normalize_date_text(row.get("signal_date")),
            "date": normalize_date_text(row.get("signal_date")),
        }
    )
    return dict(detected_w_bottom_context(source))


def low_at_date(price: pd.DataFrame, date: str) -> float:
    idx = index_for_date(price, date)
    if idx is None:
        return math.nan
    return number_text(price.iloc[idx].get("low"))


def build_structure_context(row: pd.Series, price: pd.DataFrame) -> dict[str, Any]:
    context = context_for_signal(row)
    left_low_date = normalize_date_text(context.get("left_low_date"))
    right_low_date = normalize_date_text(context.get("right_low_date"))
    left_low = low_at_date(price, left_low_date)
    right_low = low_at_date(price, right_low_date)
    stop = math.nan
    if not math.isnan(left_low) and not math.isnan(right_low):
        stop = min(left_low, right_low)
    elif not math.isnan(left_low):
        stop = left_low
    elif not math.isnan(right_low):
        stop = right_low
    return {
        "context_available": bool(context.get("available")),
        "context_ok": bool(context.get("context_ok")),
        "left_low_date": left_low_date,
        "right_low_date": right_low_date,
        "w_structure_low_price": stop,
        "neckline_price": number_text(context.get("neckline_price")),
        "neckline_distance_pct": number_text(context.get("neckline_distance_pct")),
    }


def close_return_pct(close: float, entry_price: float) -> float:
    if entry_price <= 0 or math.isnan(close) or math.isnan(entry_price):
        return math.nan
    return (close / entry_price - 1.0) * 100.0


def w_bottom_exit_state(price: pd.DataFrame, entry_idx: int, asof_idx: int, entry_price: float, stop_price: float) -> dict[str, str]:
    for idx in range(entry_idx, asof_idx + 1):
        close = number_text(price.iloc[idx].get("close"))
        if not math.isnan(stop_price) and not math.isnan(close) and close < stop_price:
            return {
                "state": "exited",
                "exit_date": safe_str(price.iloc[idx].get("date")),
                "exit_reason": "w_structure_low_close_stop",
            }
    d20_idx = entry_idx + 19
    if d20_idx <= asof_idx and d20_idx < len(price):
        d20_close = number_text(price.iloc[d20_idx].get("close"))
        if close_return_pct(d20_close, entry_price) >= 10.0:
            return {
                "state": "exited",
                "exit_date": safe_str(price.iloc[d20_idx].get("date")),
                "exit_reason": "d20_gain10_close_exit",
            }
    d40_idx = entry_idx + 39
    if d40_idx <= asof_idx:
        exit_idx = min(d40_idx, len(price) - 1)
        return {
            "state": "exited",
            "exit_date": safe_str(price.iloc[exit_idx].get("date")),
            "exit_reason": "d40_close_exit",
        }
    return {"state": "active", "exit_date": "", "exit_reason": ""}


def neckline_exit_state(price: pd.DataFrame, entry_idx: int, asof_idx: int, entry_price: float) -> dict[str, str]:
    reached_plus5 = False
    for idx in range(entry_idx, asof_idx + 1):
        close = number_text(price.iloc[idx].get("close"))
        ret = close_return_pct(close, entry_price)
        if math.isnan(ret):
            continue
        if ret >= 10.0:
            return {
                "state": "exited",
                "exit_date": safe_str(price.iloc[idx].get("date")),
                "exit_reason": "tp10_close_win",
            }
        if ret >= 5.0:
            reached_plus5 = True
        elif reached_plus5 and ret <= 5.0:
            return {
                "state": "exited",
                "exit_date": safe_str(price.iloc[idx].get("date")),
                "exit_reason": "pulled_back_to_5pct_after_plus5_without_tp10",
            }
    d20_idx = entry_idx + 19
    if d20_idx <= asof_idx:
        exit_idx = min(d20_idx, len(price) - 1)
        return {
            "state": "exited",
            "exit_date": safe_str(price.iloc[exit_idx].get("date")),
            "exit_reason": "fixed_20d_close_without_tp10_or_neutral",
        }
    return {"state": "active", "exit_date": "", "exit_reason": ""}


def stock_display(row: pd.Series) -> str:
    stock_id = stock_id_key(row.get("stock_id"))
    stock_name = safe_str(row.get("stock_name"))
    return f"{stock_id} {stock_name}".strip()


def score_fields(row: pd.Series) -> dict[str, str]:
    return {
        "model_score": safe_str(row.get("model_score")),
        "operation_score": safe_str(row.get("operation_score")),
        "tdcc_score": safe_str(row.get("tdcc_score")),
        "pattern_score": safe_str(row.get("pattern_score")),
        "risk_penalty": safe_str(row.get("risk_penalty")),
        "final_rank_score": safe_str(row.get("final_rank_score")),
        "rank_reason_zh": safe_str(row.get("rank_reason_zh")),
    }


def common_row_fields(
    row: pd.Series,
    config: ModelConfig,
    approval: dict[str, str],
    report_date: str,
    daily_signal_count: int,
    generated_at: str,
    structure: dict[str, Any],
) -> dict[str, str]:
    report_line = safe_str(row.get("report_line")) or safe_str(row.get("report_bucket"))
    fields = {
        "model_id": config.model_id,
        "model_name_zh": safe_str(row.get("model_name_zh")),
        "operation_asof_date": report_date,
        "operation_source_date_status": "current_report_date",
        "report_line": report_line,
        "report_line_memberships": safe_str(row.get("report_line_memberships")) or report_line,
        "stock_id": stock_id_key(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "stock_display": stock_display(row),
        "signal_date": normalize_date_text(row.get("signal_date")),
        "entry_rule_id": config.entry_rule_id,
        "entry_basis_zh": config.entry_basis_zh,
        "entry_price_basis": "next_trading_open_after_signal_date",
        "stop_loss_rule_id": config.stop_loss_rule_id,
        "stop_loss_price": format_price(structure.get("w_structure_low_price")),
        "stop_loss_label_zh": "W 結構低點" if config.model_id == W_BOTTOM_MODEL_ID else "不使用固定停損",
        "stop_basis_zh": config.stop_basis_zh,
        "exit_rule_id": config.exit_rule_id,
        "exit_rule_zh": config.exit_rule_zh,
        "planned_holding_days": str(config.planned_holding_days),
        "left_low_date": safe_str(structure.get("left_low_date")),
        "right_low_date": safe_str(structure.get("right_low_date")),
        "w_structure_low_price": format_price(structure.get("w_structure_low_price")),
        "neckline_price": format_price(structure.get("neckline_price")),
        "neckline_distance_pct": format_pct(structure.get("neckline_distance_pct")),
        "risk_tags_zh": safe_str(row.get("risk_tags_zh")) or safe_str(row.get("risk_penalty_tags")),
        "tdcc_status_zh": safe_str(row.get("tdcc_status_zh")) or safe_str(row.get("tdcc_status")),
        "sample_size": safe_str(approval.get("sample_size")),
        "win_rate_zh": safe_str(approval.get("win_rate_zh")),
        "avg_return_zh": safe_str(approval.get("avg_return_zh")),
        "median_return_zh": safe_str(approval.get("median_return_zh")),
        "row_metric_status": "unavailable_no_approved_add_score_metric",
        "row_metric_scope": "",
        "row_metric_id": "",
        "row_metric_label_zh": "",
        "row_metric_matched_add_score_ids": "",
        "row_metric_sample_size": "",
        "row_metric_win_rate_zh": "",
        "row_metric_neutral_rate_zh": "",
        "row_metric_failure_rate_zh": "",
        "row_metric_avg_return_zh": "",
        "row_metric_median_return_zh": "",
        "row_metric_source": "",
        "row_metric_selection_status": "baseline_not_permitted_in_operation_row",
        "daily_signal_date": report_date,
        "daily_model_signal_count": str(daily_signal_count),
        "adapter_source": ADAPTER_SOURCE,
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
        "generated_at": generated_at,
    }
    fields.update(score_fields(row))
    return fields


def confirmed_data_row(
    row: pd.Series,
    config: ModelConfig,
    approval: dict[str, str],
    report_date: str,
    daily_signal_count: int,
    generated_at: str,
    display_order: int,
) -> list[dict[str, str]]:
    price = price_for_stock(row.get("stock_id"))
    structure = build_structure_context(row, price) if not price.empty else {}
    base = common_row_fields(row, config, approval, report_date, daily_signal_count, generated_at, structure)
    signal_idx = index_for_date(price, row.get("signal_date")) if not price.empty else None
    entry_idx = next_trading_index(price, signal_idx) if signal_idx is not None else None
    entry_date = safe_str(price.iloc[entry_idx].get("date")) if entry_idx is not None else ""
    entry_price = format_price(price.iloc[entry_idx].get("open")) if entry_idx is not None else ""
    rows: list[dict[str, str]] = []
    for pdf_view in PDF_VIEWS:
        out = {
            **base,
            "pdf_view": pdf_view,
            "pdf_section": "confirmed_operation",
            "pdf_section_zh": SECTION_ZH["confirmed_operation"],
            "row_type": "data",
            "display_order": str(display_order),
            "operation_status": "confirmed_operation",
            "operation_status_zh": config.confirmed_status_zh,
            "quality_status_zh": "approved operation guidance",
            "row_action_status": "confirmed_buy_candidate",
            "buy_rank_eligible": "True",
            "entry_date": entry_date,
            "entry_price": entry_price,
            "entry_price_status_zh": "下一個交易日開盤價" if entry_price else "下一個交易日開盤價待確認",
            "operation_age_days": "0",
            "pdf_note_zh": safe_str(row.get("operation_reminder_zh")) or safe_str(row.get("next_confirmation_zh")),
            "adapter_note_zh": "PDF may render this row as the model-owned buy/confirmed operation row; PDF must not recalculate lifecycle.",
        }
        rows.append(out)
    return rows


def active_data_row(
    row: pd.Series,
    config: ModelConfig,
    approval: dict[str, str],
    report_date: str,
    daily_signal_count: int,
    generated_at: str,
    display_order: int,
) -> tuple[list[dict[str, str]], dict[str, str]]:
    stock_id = stock_id_key(row.get("stock_id"))
    price = price_for_stock(stock_id)
    if price.empty:
        return [], audit_row(row, config, report_date, generated_at, "source_gap", "False", "missing_stock_price_history_file")
    signal_date = normalize_date_text(row.get("signal_date"))
    signal_idx = index_for_date(price, signal_date)
    asof_idx = index_for_date(price, report_date)
    if signal_idx is None:
        return [], audit_row(row, config, report_date, generated_at, "source_gap", "False", "signal_date_missing_in_stock_price_history")
    if asof_idx is None:
        return [], audit_row(row, config, report_date, generated_at, "source_gap", "False", "operation_asof_date_missing_in_stock_price_history")
    entry_idx = next_trading_index(price, signal_idx)
    if entry_idx is None:
        return [], audit_row(row, config, report_date, generated_at, "lifecycle_suppressed", "False", "next_trading_day_not_available_yet")
    if entry_idx > asof_idx:
        return [], audit_row(row, config, report_date, generated_at, "lifecycle_suppressed", "False", "entry_date_after_operation_asof_date")

    entry_price = number_text(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return [], audit_row(row, config, report_date, generated_at, "source_gap", "False", "invalid_entry_open_price")

    structure = build_structure_context(row, price)
    if config.model_id == W_BOTTOM_MODEL_ID:
        state = w_bottom_exit_state(price, entry_idx, asof_idx, entry_price, number_text(structure.get("w_structure_low_price")))
    else:
        state = neckline_exit_state(price, entry_idx, asof_idx, entry_price)

    if state["state"] != "active":
        audit = audit_row(
            row,
            config,
            report_date,
            generated_at,
            "lifecycle_suppressed",
            "False",
            state["exit_reason"],
        )
        audit["exit_date"] = state["exit_date"]
        audit["exit_reason"] = state["exit_reason"]
        return [], audit

    age = max(1, asof_idx - entry_idx + 1)
    base = common_row_fields(row, config, approval, report_date, daily_signal_count, generated_at, structure)
    rows: list[dict[str, str]] = []
    for pdf_view in PDF_VIEWS:
        rows.append(
            {
                **base,
                "pdf_view": pdf_view,
                "pdf_section": "active_operation",
                "pdf_section_zh": SECTION_ZH["active_operation"],
                "row_type": "data",
                "display_order": str(display_order),
                "operation_status": "active_operation",
                "operation_status_zh": config.active_status_zh,
                "quality_status_zh": "active by approved operation lifecycle",
                "row_action_status": "active_tracking",
                "buy_rank_eligible": "False",
                "entry_date": safe_str(price.iloc[entry_idx].get("date")),
                "entry_price": format_price(entry_price),
                "entry_price_status_zh": "已以訊號後下一個交易日開盤價追蹤",
                "operation_age_days": str(age),
                "pdf_note_zh": safe_str(row.get("operation_reminder_zh")) or safe_str(row.get("next_confirmation_zh")),
                "adapter_note_zh": "PDF may render this row as model-owned active operation tracking; PDF must not recalculate lifecycle.",
            }
        )
    audit = audit_row(row, config, report_date, generated_at, "candidate_evaluated", "True", "active_operation")
    audit["entry_date"] = safe_str(price.iloc[entry_idx].get("date"))
    return rows, audit


def audit_row(
    row: pd.Series,
    config: ModelConfig,
    report_date: str,
    generated_at: str,
    audit_status: str,
    included: str,
    reason: str,
) -> dict[str, str]:
    price = price_for_stock(row.get("stock_id"))
    structure = build_structure_context(row, price) if not price.empty else {}
    return {
        "model_id": config.model_id,
        "operation_asof_date": report_date,
        "stock_id": stock_id_key(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "report_line": safe_str(row.get("report_line")) or safe_str(row.get("report_bucket")),
        "signal_date": normalize_date_text(row.get("signal_date")),
        "entry_date": "",
        "operation_lifecycle_state": reason,
        "audit_status": audit_status,
        "included_in_daily_adapter": included,
        "exit_date": "",
        "exit_reason": "",
        "stop_loss_price": format_price(structure.get("w_structure_low_price")),
        "left_low_date": safe_str(structure.get("left_low_date")),
        "right_low_date": safe_str(structure.get("right_low_date")),
        "neckline_price": format_price(structure.get("neckline_price")),
        "reason": reason,
        "adapter_source": ADAPTER_SOURCE,
        "generated_at": generated_at,
    }


def empty_audit_row(config: ModelConfig, report_date: str, generated_at: str) -> dict[str, str]:
    return {
        "model_id": config.model_id,
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
        "stop_loss_price": "",
        "left_low_date": "",
        "right_low_date": "",
        "neckline_price": "",
        "reason": "no current confirmed rows and no active operation rows",
        "adapter_source": ADAPTER_SOURCE,
        "generated_at": generated_at,
    }


def empty_row(
    config: ModelConfig,
    pdf_view: str,
    pdf_section: str,
    report_date: str,
    daily_signal_count: int,
    approval: dict[str, str],
    generated_at: str,
) -> dict[str, str]:
    return {
        "model_id": config.model_id,
        "model_name_zh": "",
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
        "quality_status_zh": "empty_state",
        "row_action_status": "empty_state",
        "buy_rank_eligible": "False",
        "signal_date": "",
        "entry_rule_id": config.entry_rule_id,
        "entry_basis_zh": config.entry_basis_zh,
        "entry_price_basis": "",
        "entry_date": "",
        "entry_price": "",
        "entry_price_status_zh": "",
        "stop_loss_rule_id": config.stop_loss_rule_id,
        "stop_loss_price": "",
        "stop_loss_label_zh": "",
        "stop_basis_zh": config.stop_basis_zh,
        "exit_rule_id": config.exit_rule_id,
        "exit_rule_zh": config.exit_rule_zh,
        "planned_holding_days": str(config.planned_holding_days),
        "operation_age_days": "",
        "left_low_date": "",
        "right_low_date": "",
        "w_structure_low_price": "",
        "neckline_price": "",
        "neckline_distance_pct": "",
        "model_score": "",
        "operation_score": "",
        "tdcc_score": "",
        "pattern_score": "",
        "risk_penalty": "",
        "final_rank_score": "",
        "rank_reason_zh": "",
        "risk_tags_zh": "",
        "tdcc_status_zh": "",
        "sample_size": safe_str(approval.get("sample_size")),
        "win_rate_zh": safe_str(approval.get("win_rate_zh")),
        "avg_return_zh": safe_str(approval.get("avg_return_zh")),
        "median_return_zh": safe_str(approval.get("median_return_zh")),
        "row_metric_status": "not_applicable_empty_state",
        "row_metric_scope": "",
        "row_metric_id": "",
        "row_metric_label_zh": "",
        "row_metric_matched_add_score_ids": "",
        "row_metric_sample_size": "",
        "row_metric_win_rate_zh": "",
        "row_metric_neutral_rate_zh": "",
        "row_metric_failure_rate_zh": "",
        "row_metric_avg_return_zh": "",
        "row_metric_median_return_zh": "",
        "row_metric_source": "",
        "row_metric_selection_status": "empty_state",
        "daily_signal_date": report_date,
        "daily_model_signal_count": str(daily_signal_count),
        "adapter_source": ADAPTER_SOURCE,
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


def build_model_section(
    signals: pd.DataFrame,
    approval_frame: pd.DataFrame,
    config: ModelConfig,
    report_date: str,
    generated_at: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    current = daily_model_signal_rows(signals, config, report_date)
    history = load_signal_history(signals, config, report_date)
    approval = approval_context(approval_frame, config)
    daily_signal_count = int(current["stock_id"].nunique()) if not current.empty else 0
    rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []

    if history.empty or "signal_date" not in history.columns:
        active_candidates = pd.DataFrame()
    else:
        active_candidates = history[history["signal_date"].map(normalize_date_text).lt(report_date)].copy()
    active_rows_by_key: dict[tuple[str, str], tuple[str, list[dict[str, str]], dict[str, str]]] = {}
    for _, row in active_candidates.iterrows():
        active_rows, audit = active_data_row(
            row,
            config,
            approval,
            report_date,
            daily_signal_count,
            generated_at,
            display_order=len(active_rows_by_key) + 1,
        )
        audit_rows.append(audit)
        if not active_rows:
            continue
        key = (stock_id_key(row.get("stock_id")), safe_str(row.get("report_bucket")) or safe_str(row.get("report_line")))
        signal_date = normalize_date_text(row.get("signal_date"))
        existing = active_rows_by_key.get(key)
        if existing is None or signal_date >= existing[0]:
            active_rows_by_key[key] = (signal_date, active_rows, audit)

    for display_order, (_key, (_signal_date, active_rows, _audit)) in enumerate(sorted(active_rows_by_key.items()), start=1):
        for item in active_rows:
            item["display_order"] = str(display_order)
            rows.append(item)

    active_keys = set(active_rows_by_key)
    confirmed_order = 1
    for _, row in current.iterrows():
        key = (stock_id_key(row.get("stock_id")), safe_str(row.get("report_bucket")) or safe_str(row.get("report_line")))
        if key in active_keys:
            audit_rows.append(
                audit_row(
                    row,
                    config,
                    report_date,
                    generated_at,
                    "lifecycle_suppressed",
                    "False",
                    "same_stock_already_active_operation",
                )
            )
            continue
        rows.extend(
            confirmed_data_row(
                row,
                config,
                approval,
                report_date,
                daily_signal_count,
                generated_at,
                confirmed_order,
            )
        )
        audit_rows.append(audit_row(row, config, report_date, generated_at, "candidate_evaluated", "True", "confirmed_operation"))
        confirmed_order += 1

    existing = {(row["pdf_view"], row["pdf_section"]) for row in rows if row["row_type"] == "data"}
    for pdf_view in PDF_VIEWS:
        for section in PDF_SECTIONS:
            if (pdf_view, section) not in existing:
                rows.append(empty_row(config, pdf_view, section, report_date, daily_signal_count, approval, generated_at))
    if not audit_rows:
        audit_rows.append(empty_audit_row(config, report_date, generated_at))

    out = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    out["_view_order"] = out["pdf_view"].map({"highlight": 0, "full": 1}).fillna(9)
    out["_section_order"] = out["pdf_section"].map({"confirmed_operation": 0, "active_operation": 1}).fillna(9)
    out["_row_type_order"] = out["row_type"].map({"data": 0, "empty_state": 1}).fillna(9)
    out["_display_order_num"] = pd.to_numeric(out["display_order"], errors="coerce").fillna(999999)
    out = out.sort_values(["_view_order", "_section_order", "_row_type_order", "_display_order_num", "stock_id"])
    section = out.drop(columns=["_view_order", "_section_order", "_row_type_order", "_display_order_num"]).reset_index(drop=True)
    audit = pd.DataFrame(audit_rows, columns=AUDIT_COLUMNS)
    return section, audit


def write_model_outputs(config: ModelConfig, section: pd.DataFrame, audit: pd.DataFrame) -> None:
    csv_path, md_path, audit_csv_path, audit_md_path = output_paths(config)
    write_csv(section, csv_path)
    title = f"{config.model_id} Daily Operation Section"
    lines = [
        f"# {title}",
        "",
        "- Producer owner: `daily_model_maintenance`.",
        "- Consumer contract: PDF may render these rows; PDF must not infer buy/active lifecycle from candidate signals.",
        "- Digest/highlight view uses `confirmed_operation` and `active_operation` only.",
        "",
    ]
    lines.append(markdown_table(section, DISPLAY_COLUMNS, limit=120))
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    write_csv(audit, audit_csv_path)
    audit_lines = [
        f"# {config.model_id} Daily Operation Evidence Audit",
        "",
        "- Audit rows record model-side lifecycle decisions and suppressed rows.",
        "- Raw research variants are not consumed by this adapter.",
        "",
    ]
    audit_lines.append(markdown_table(audit, AUDIT_DISPLAY_COLUMNS, limit=160))
    audit_md_path.write_text("\n".join(audit_lines) + "\n", encoding="utf-8", newline="\n")

    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    for path in (csv_path, md_path, audit_csv_path, audit_md_path):
        (DOCS_LATEST_DIR / path.name).write_bytes(path.read_bytes())


def build_all() -> dict[str, tuple[pd.DataFrame, pd.DataFrame]]:
    signals = read_csv(DAILY_SIGNALS_CSV, dtype=str).fillna("")
    approval = read_csv(APPROVAL_CSV, dtype=str).fillna("")
    report_date = main_price_date()
    require_latest_signals_match_report_date(signals, report_date)
    generated_at = now_text()
    return {
        model_id: build_model_section(signals, approval, config, report_date, generated_at)
        for model_id, config in MODEL_CONFIGS.items()
    }


def main() -> int:
    built = build_all()
    for model_id, (section, audit) in built.items():
        config = MODEL_CONFIGS[model_id]
        write_model_outputs(config, section, audit)
        csv_path, md_path, audit_csv_path, audit_md_path = output_paths(config)
        print(f"Saved: {csv_path} rows={len(section)}")
        print(f"Saved: {md_path}")
        print(f"Saved: {audit_csv_path} rows={len(audit)}")
        print(f"Saved: {audit_md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
