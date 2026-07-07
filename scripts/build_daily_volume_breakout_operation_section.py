from __future__ import annotations

from datetime import datetime
from functools import lru_cache
import math
import os
from pathlib import Path
import sys
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from volume_breakout_operation_utils import (  # noqa: E402
    TRIGGERS as SHARED_TRIGGERS,
    TRIGGER_MAP as SHARED_TRIGGER_MAP,
    TRIGGER_PRIORITY as SHARED_TRIGGER_PRIORITY,
    add_research_features,
    attach_tdcc_asof,
    event_payload as operation_event_payload,
    find_confirmation as shared_find_confirmation,
    best_evidence as best_row_evidence,
    load_market_regime_map,
    read_tdcc_events,
    signal_low_broken as shared_signal_low_broken,
    stop_hit_index as shared_stop_hit_index,
)


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

DAILY_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
APPROVAL_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"
APPROVED_FORMAL_SUMMARY_CSV = (
    ROOT
    / "config"
    / "approved_operation_evidence"
    / "volume_breakout_operation_v1_20260615_formal_operation_backtest.csv"
)
FORMAL_SUMMARY_CSV = APPROVED_FORMAL_SUMMARY_CSV
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
MODEL_SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"
MODEL_SIGNAL_LOG_CSV = ROOT / "output" / "history" / "daily_candidate_models" / "daily_candidate_model_signal_log.csv"
STOCK_PRICE_HISTORY_DIR = ROOT / "data" / "stock_price_history"

OUT_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
OUT_MD = LATEST_DIR / "daily_volume_breakout_operation_section_latest.md"
EVIDENCE_AUDIT_CSV = LATEST_DIR / "daily_volume_breakout_operation_evidence_audit_latest.csv"
EVIDENCE_AUDIT_MD = LATEST_DIR / "daily_volume_breakout_operation_evidence_audit_latest.md"
ALLOW_SNAPSHOT_REWRITE_ENV = "ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE"

MODEL_ID = "volume_range_breakout"
LIFECYCLE_ADAPTER_SOURCE = "daily_candidate_model_signal_log+daily_published_model_snapshots+stock_price_history"
APPROVAL_SOURCE = "approved_operation_patterns_latest.csv"
PDF_VIEWS = ("highlight", "full")
PDF_SECTIONS = (
    "confirmed_operation",
    "confirmed_unranked_operation",
    "pending_confirmation",
    "active_operation",
)
HIGHLIGHT_HIDDEN_SECTIONS = {
    "confirmed_unranked_operation",
    "pending_confirmation",
}
MAX_CONFIRM_DAYS = 10
MAX_HOLD_DAYS = 10

SECTION_ZH = {
    "confirmed_operation": "已確認操作",
    "confirmed_unranked_operation": "已確認但未通過買入排名門檻",
    "pending_confirmation": "待確認",
    "active_operation": "操作中",
}

SECTION_EMPTY_NOTE_ZH = {
    "confirmed_operation": "目前沒有符合研究證據門檻的已確認操作列。",
    "confirmed_unranked_operation": "目前沒有已確認但未通過買入排名門檻的股票。",
    "pending_confirmation": "目前沒有待確認的放量攻擊訊號。",
    "active_operation": "目前沒有操作中追蹤列。",
}


def section_allowed_for_pdf_view(pdf_view: str, pdf_section: str) -> bool:
    return not (pdf_view == "highlight" and pdf_section in HIGHLIGHT_HIDDEN_SECTIONS)

# Keep daily adapter trigger order in parity with the formal research backtest.
TRIGGERS = [
    {
        "trigger_id": spec.trigger_id,
        "trigger_zh": spec.trigger_name_zh,
        "confirmation_rule_zh": spec.confirmation_rule_zh,
        "max_confirm_days": spec.max_confirm_days,
        "ma_col": spec.ma_col,
    }
    for spec in SHARED_TRIGGERS
]
TRIGGER_PRIORITY = dict(SHARED_TRIGGER_PRIORITY)
TRIGGER_ZH = {item["trigger_id"]: item["trigger_zh"] for item in TRIGGERS}

OUTPUT_COLUMNS = [
    "model_id",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "operation_asof_date",
    "operation_source_date_status",
    "display_order",
    "stock_id",
    "stock_name",
    "stock_display",
    "operation_status",
    "operation_status_zh",
    "quality_status_zh",
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "trigger_zh",
    "entry_basis_zh",
    "entry_price_status_zh",
    "stop_basis_zh",
    "exit_rule_zh",
    "operation_score",
    "tdcc_score",
    "pattern_score",
    "risk_penalty",
    "final_rank_score",
    "rank_reason_zh",
    "entry_rule_id",
    "entry_price_basis",
    "entry_date",
    "entry_price",
    "stop_loss_rule_id",
    "stop_loss_price",
    "stop_loss_label_zh",
    "exit_rule_id",
    "planned_holding_days",
    "operation_age_days",
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
    "evidence_match_status",
    "evidence_tdcc_list_type",
    "evidence_rank_bucket",
    "evidence_confluence_scope",
    "evidence_confluence_id",
    "evidence_key",
    "evidence_out_of_sample_pass",
    "research_score",
    "pdf_note_zh",
    "daily_signal_date",
    "daily_volume_model_signal_count",
    "adapter_source",
    "adapter_source_status",
    "approval_source",
    "approved_for_daily",
    "operation_module_approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "operation_directive_level",
    "row_action_status",
    "buy_rank_eligible",
    "buy_filter_id",
    "approval_note_zh",
    "adapter_note_zh",
    "generated_at",
]

EVIDENCE_AUDIT_COLUMNS = [
    "model_id",
    "operation_asof_date",
    "stock_id",
    "stock_name",
    "signal_date",
    "selected_trigger_id",
    "selected_confirmation_date",
    "operation_lifecycle_state",
    "audit_status",
    "included_in_daily_adapter",
    "tdcc_list_type",
    "tdcc_rank",
    "rank_bucket",
    "classification_id",
    "attack_method",
    "price_position_type",
    "risk_type",
    "evidence_confluence_scope",
    "evidence_confluence_id",
    "evidence_sample_size",
    "evidence_win_rate",
    "evidence_avg_return",
    "evidence_median_return",
    "evidence_out_of_sample_pass",
    "ranking_research_score",
    "reason",
    "generated_at",
]

APPROVAL_FIELDS = [
    "approval_source",
    "approved_for_daily",
    "operation_module_approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "operation_directive_level",
    "buy_filter_id",
    "approval_note_zh",
]

OPERATION_SCORE_FIELDS = [
    "operation_score",
    "tdcc_score",
    "pattern_score",
    "risk_penalty",
    "final_rank_score",
    "rank_reason_zh",
]

_MARKET_REGIME_MAP: dict[str, str] | None = None
_TDCC_EVENTS: pd.DataFrame | None = None


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        print(f"WARNING: failed to read {path}: {exc}")
        return pd.DataFrame()


@lru_cache(maxsize=None)
def read_snapshot_csv_cached(path_text: str) -> pd.DataFrame:
    return read_csv(Path(path_text)).fillna("")


@lru_cache(maxsize=None)
def prior_operation_snapshot_paths(report_date: str) -> tuple[str, ...]:
    report_date = normalize_date_text(report_date)
    paths: list[tuple[str, str]] = []
    for path in MODEL_SNAPSHOT_DIR.glob("daily_volume_breakout_operation_section_*.csv"):
        snapshot_date = normalize_date_text(path.stem.rsplit("_", 1)[-1])
        if snapshot_date and snapshot_date < report_date:
            paths.append((snapshot_date, str(path)))
    return tuple(path for _snapshot_date, path in sorted(paths, reverse=True))


@lru_cache(maxsize=None)
def prior_active_snapshot_keys(report_date: str) -> frozenset[tuple[str, str, str]]:
    keys: set[tuple[str, str, str]] = set()
    for path_text in prior_operation_snapshot_paths(report_date):
        section = read_snapshot_csv_cached(path_text)
        if section.empty:
            continue
        active = section[
            section.get("pdf_section", pd.Series(dtype=str)).astype(str).eq("active_operation")
            & section.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
        ].copy()
        if active.empty:
            continue
        for _, row in active.iterrows():
            keys.add(
                (
                    stock_id_key(row.get("stock_id")),
                    normalize_date_text(row.get("signal_date")),
                    normalize_date_text(row.get("selected_confirmation_date")),
                )
            )
    return frozenset(keys)


def true_env(name: str) -> bool:
    return safe_str(os.environ.get(name)).lower() in {"1", "true", "yes", "y"}


def published_section_snapshot_path(report_date: str) -> Path:
    return MODEL_SNAPSHOT_DIR / f"daily_volume_breakout_operation_section_{normalize_date_text(report_date)}.csv"


def published_evidence_audit_snapshot_path(report_date: str) -> Path:
    return MODEL_SNAPSHOT_DIR / f"daily_volume_breakout_operation_evidence_audit_{normalize_date_text(report_date)}.csv"


def confirmation_snapshot_buy_ranked(signal: pd.Series, selected: dict[str, Any]) -> tuple[bool, str]:
    confirmation_date = normalize_date_text(selected.get("confirmation_date"))
    if not confirmation_date:
        return False, "missing_selected_confirmation_date"
    path = published_section_snapshot_path(confirmation_date)
    if not path.exists():
        return False, "missing_confirmation_operation_snapshot"
    section = read_snapshot_csv_cached(str(path))
    if section.empty:
        return False, "empty_confirmation_operation_snapshot"

    stock_id = stock_id_key(signal.get("stock_id"))
    signal_date = normalize_date_text(signal.get("signal_date"))
    matches = section[
        section.get("stock_id", pd.Series(dtype=str)).map(stock_id_key).eq(stock_id)
        & section.get("signal_date", pd.Series(dtype=str)).map(normalize_date_text).eq(signal_date)
        & section.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
    ].copy()
    if "selected_confirmation_date" in matches.columns:
        matches = matches[
            matches["selected_confirmation_date"].map(normalize_date_text).eq(confirmation_date)
        ].copy()
    if matches.empty:
        return False, "missing_confirmation_operation_snapshot_row"

    buy_ranked = matches[
        matches.get("pdf_section", pd.Series(dtype=str)).astype(str).eq("confirmed_operation")
        & matches.get("row_action_status", pd.Series(dtype=str)).astype(str).eq("confirmed_buy_candidate")
        & matches.get("buy_rank_eligible", pd.Series(dtype=str)).astype(str).eq("True")
    ]
    if buy_ranked.empty:
        return False, "confirmation_snapshot_not_buy_ranked_not_tracked_active"
    return True, "confirmation_snapshot_buy_ranked"


def prior_active_snapshot_tracked(signal: pd.Series, selected: dict[str, Any], report_date: str) -> tuple[bool, str]:
    confirmation_date = normalize_date_text(selected.get("confirmation_date"))
    key = (
        stock_id_key(signal.get("stock_id")),
        normalize_date_text(signal.get("signal_date")),
        confirmation_date,
    )
    if key in prior_active_snapshot_keys(report_date):
        return True, "prior_active_snapshot_tracked"
    return False, "missing_prior_active_snapshot"


def active_snapshot_backing(signal: pd.Series, selected: dict[str, Any], report_date: str) -> tuple[bool, str]:
    buy_ranked, buy_ranked_reason = confirmation_snapshot_buy_ranked(signal, selected)
    if buy_ranked:
        return True, buy_ranked_reason
    prior_active, _prior_reason = prior_active_snapshot_tracked(signal, selected, report_date)
    if prior_active:
        return False, f"{buy_ranked_reason}_despite_prior_active_snapshot"
    return False, buy_ranked_reason


def restore_published_snapshot(report_date: str) -> tuple[pd.DataFrame, pd.DataFrame] | None:
    if true_env(ALLOW_SNAPSHOT_REWRITE_ENV):
        return None
    section_path = published_section_snapshot_path(report_date)
    audit_path = published_evidence_audit_snapshot_path(report_date)
    if not section_path.exists():
        return None
    if not audit_path.exists():
        raise RuntimeError(
            "published volume breakout operation section snapshot exists without matching evidence audit snapshot: "
            f"{section_path.as_posix()} requires {audit_path.as_posix()}; set {ALLOW_SNAPSHOT_REWRITE_ENV}=1 only for an explicit correction run"
        )
    section = read_csv(section_path)
    audit = read_csv(audit_path)
    if section.empty:
        raise RuntimeError(f"published volume breakout operation section snapshot is empty: {section_path.as_posix()}")
    if audit.empty:
        raise RuntimeError(f"published volume breakout operation evidence audit snapshot is empty: {audit_path.as_posix()}")
    for col in OUTPUT_COLUMNS:
        if col not in section.columns:
            section[col] = ""
    for col in EVIDENCE_AUDIT_COLUMNS:
        if col not in audit.columns:
            audit[col] = ""
    return section[OUTPUT_COLUMNS].copy(), audit[EVIDENCE_AUDIT_COLUMNS].copy()


def number_text(value: Any) -> float:
    text = safe_str(value).replace("%", "").replace("+", "").replace(",", "")
    if not text:
        return float("nan")
    try:
        return float(text)
    except Exception:
        return float("nan")


def true_text(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "1.0", "yes", "y", "t"}


def normalize_date_text(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    text = text.replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""


def stock_id_key(value: Any) -> str:
    text = safe_str(value).replace(".0", "")
    return text.zfill(4) if text.isdigit() else text


def market_regime_map() -> dict[str, str]:
    global _MARKET_REGIME_MAP
    if _MARKET_REGIME_MAP is None:
        _MARKET_REGIME_MAP = load_market_regime_map()
    return _MARKET_REGIME_MAP


def tdcc_events() -> pd.DataFrame:
    global _TDCC_EVENTS
    if _TDCC_EVENTS is None:
        _TDCC_EVENTS = read_tdcc_events()
    return _TDCC_EVENTS.copy()


def main_price_date() -> str:
    freshness = read_csv(DATA_FRESHNESS_CSV)
    if freshness.empty or "main_price_date" not in freshness.columns:
        return ""
    return normalize_date_text(freshness.iloc[0].get("main_price_date"))


def signal_dates_in_frame(frame: pd.DataFrame) -> set[str]:
    if frame.empty or "signal_date" not in frame.columns:
        return set()
    return {
        date
        for date in frame["signal_date"].map(normalize_date_text).tolist()
        if date
    }


def require_latest_signals_match_report_date(signals: pd.DataFrame, report_date: str) -> None:
    report_date = normalize_date_text(report_date)
    dates = signal_dates_in_frame(signals)
    if not dates:
        return
    if dates != {report_date}:
        observed = ", ".join(sorted(dates))
        raise RuntimeError(
            "daily candidate model signals must be a same-date latest artifact before "
            "building volume breakout operations: "
            f"main_price_date={report_date or 'missing'} signal_dates={observed}"
        )


def approval_context(approval: pd.DataFrame) -> dict[str, str]:
    default = {
        "approval_source": APPROVAL_SOURCE,
        "approved_for_daily": "False",
        "operation_module_approved_for_daily": "False",
        "approval_status": "missing",
        "operation_module_id": "",
        "approval_version": "",
        "operation_directive_level": "no_operation_directive",
        "row_action_status": "empty_state",
        "buy_rank_eligible": "False",
        "buy_filter_id": "",
        "approval_note_zh": "尚未建立放量攻擊 approved operation artifact。",
    }
    if approval.empty or "model_id" not in approval.columns:
        return default
    part = approval[approval["model_id"].astype(str).str.strip().eq(MODEL_ID)].copy()
    if part.empty:
        return default
    row = part.iloc[0]
    approved = safe_str(row.get("approved_for_daily"))
    return {
        "approval_source": APPROVAL_SOURCE,
        "approved_for_daily": "True" if approved.lower() == "true" else "False",
        "operation_module_approved_for_daily": "True" if approved.lower() == "true" else "False",
        "approval_status": safe_str(row.get("approval_status")),
        "operation_module_id": safe_str(row.get("operation_module_id")),
        "approval_version": safe_str(row.get("approval_version")),
        "operation_directive_level": safe_str(row.get("operation_directive_level")),
        "row_action_status": "",
        "buy_rank_eligible": "False",
        "buy_filter_id": safe_str(row.get("buy_filter_id")),
        "approval_note_zh": safe_str(row.get("approval_note_zh")),
    }


def daily_signal_context(signals: pd.DataFrame, report_date: str = "") -> tuple[str, int]:
    report_date = normalize_date_text(report_date)
    if signals.empty or "model_id" not in signals.columns:
        return report_date, 0
    volume = signals[signals["model_id"].astype(str).str.strip().eq(MODEL_ID)].copy()
    if volume.empty:
        return report_date, 0
    if report_date and "signal_date" in volume.columns:
        volume = volume[volume["signal_date"].map(normalize_date_text).eq(report_date)].copy()
        unique_count = volume.get("stock_id", pd.Series(dtype=str)).astype(str).str.strip().replace("", pd.NA).dropna().nunique()
        return report_date, int(unique_count)
    signal_dates = sorted(
        {safe_str(value) for value in volume.get("signal_date", pd.Series(dtype=str)).tolist() if safe_str(value)}
    )
    signal_date = signal_dates[-1] if signal_dates else ""
    unique_count = volume.get("stock_id", pd.Series(dtype=str)).astype(str).str.strip().replace("", pd.NA).dropna().nunique()
    return signal_date, int(unique_count)


def daily_volume_signal_rows(signals: pd.DataFrame, daily_signal_date: str) -> pd.DataFrame:
    if signals.empty or "model_id" not in signals.columns:
        return pd.DataFrame()
    volume = signals[signals["model_id"].astype(str).str.strip().eq(MODEL_ID)].copy()
    if volume.empty:
        return pd.DataFrame()
    report_date = normalize_date_text(daily_signal_date)
    if report_date and "signal_date" in volume.columns:
        volume = volume[volume["signal_date"].map(normalize_date_text).eq(report_date)].copy()
    if volume.empty:
        return pd.DataFrame()
    if "display_rank" in volume.columns:
        volume["_display_order_num"] = pd.to_numeric(volume["display_rank"], errors="coerce")
    elif "model_rank" in volume.columns:
        volume["_display_order_num"] = pd.to_numeric(volume["model_rank"], errors="coerce")
    else:
        volume["_display_order_num"] = range(1, len(volume) + 1)
    volume["_display_order_num"] = volume["_display_order_num"].fillna(999999)
    return volume.sort_values(["_display_order_num", "stock_id"]).drop(columns=["_display_order_num"], errors="ignore")



def signal_pending_text(row: pd.Series) -> str:
    return (
        safe_str(row.get("next_confirmation_zh"))
        or safe_str(row.get("operation_reminder_zh"))
        or safe_str(row.get("recommended_usage_zh"))
        or "等待隔日確認；跌回突破區、量價失敗或 TDCC 轉弱則風險升高。"
    )


def signal_pending_group(row: pd.Series) -> str:
    return (
        safe_str(row.get("same_model_repeat_status_zh"))
        or safe_str(row.get("display_rank_new_signal"))
        or safe_str(row.get("display_rank_repeated_signal"))
        or "今日模型命中"
    )


def load_price_history(stock_id: str) -> pd.DataFrame:
    path = STOCK_PRICE_HISTORY_DIR / f"{stock_id_key(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = read_csv(path)
    if price.empty or not {"date", "open", "high", "low", "close"}.issubset(price.columns):
        return pd.DataFrame()
    out = price.copy()
    out["date"] = out["date"].map(normalize_date_text)
    out = out[out["date"].astype(str).str.len().eq(8)].copy()
    for col in ["open", "high", "low", "close", "volume"]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.dropna(subset=["open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)
    if "ma5" not in out.columns:
        out["ma5"] = out["close"].rolling(5, min_periods=1).mean()
    else:
        out["ma5"] = pd.to_numeric(out["ma5"], errors="coerce")
    if "ma10" not in out.columns:
        out["ma10"] = out["close"].rolling(10, min_periods=1).mean()
    else:
        out["ma10"] = pd.to_numeric(out["ma10"], errors="coerce")
    try:
        out = add_research_features(out)
    except Exception as exc:
        print(f"WARNING: failed to add volume breakout research features for {stock_id}: {exc}")
    return out


def price_at(row: pd.Series, col: str) -> float:
    value = row.get(col)
    try:
        num = float(value)
    except Exception:
        return math.nan
    return num if num > 0 else math.nan


def signal_low_broken(price: pd.DataFrame, signal_idx: int, through_idx: int, signal_low: float) -> bool:
    return shared_signal_low_broken(price, signal_idx, through_idx, signal_low)


def find_confirmation(price: pd.DataFrame, signal_idx: int, spec: dict[str, Any]) -> dict[str, Any] | None:
    signal = price.iloc[signal_idx]
    trigger_id = safe_str(spec.get("trigger_id"))
    signal_close = price_at(signal, "close")
    signal_high = price_at(signal, "high")
    signal_low = price_at(signal, "low")
    if any(math.isnan(value) for value in [signal_close, signal_high, signal_low]):
        return None

    if trigger_id == "next_day_break_signal_high_confirmed":
        shared_spec = SHARED_TRIGGER_MAP.get(trigger_id)
        return shared_find_confirmation(price, signal_idx, shared_spec) if shared_spec is not None else None

    if trigger_id == "next_day_continuation_confirmed":
        confirm_idx = signal_idx + 1
        if confirm_idx >= len(price) or signal_low_broken(price, signal_idx, confirm_idx, signal_low):
            return None
        row = price.iloc[confirm_idx]
        close = price_at(row, "close")
        if not math.isnan(close) and close > signal_close and close >= signal_high:
            return {"confirmation_idx": confirm_idx}
        return None

    ma_col = safe_str(spec.get("ma_col"))
    if ma_col:
        end_idx = min(len(price) - 1, signal_idx + int(spec.get("max_confirm_days", MAX_CONFIRM_DAYS)))
        for confirm_idx in range(signal_idx + 1, end_idx + 1):
            if signal_low_broken(price, signal_idx, confirm_idx, signal_low):
                return None
            row = price.iloc[confirm_idx]
            ma = price_at(row, ma_col)
            low = price_at(row, "low")
            close = price_at(row, "close")
            if any(math.isnan(value) for value in [ma, low, close]):
                continue
            if low <= ma and close >= ma:
                return {"confirmation_idx": confirm_idx}
    return None


def selected_confirmation(price: pd.DataFrame, signal_idx: int, report_idx: int) -> dict[str, Any] | None:
    matches: list[dict[str, Any]] = []
    for spec in TRIGGERS:
        found = find_confirmation(price, signal_idx, spec)
        if found is None:
            continue
        confirmation_idx = int(found["confirmation_idx"])
        if confirmation_idx > report_idx:
            continue
        trigger_id = safe_str(spec.get("trigger_id"))
        matches.append(
            {
                "trigger_id": trigger_id,
                "trigger_zh": safe_str(spec.get("trigger_zh")),
                "confirmation_idx": confirmation_idx,
                "confirmation_date": normalize_date_text(price.iloc[confirmation_idx].get("date")),
                "trigger_priority": TRIGGER_PRIORITY.get(trigger_id, 999),
            }
        )
    if not matches:
        return None
    matches = sorted(matches, key=lambda row: (row["confirmation_idx"], row["trigger_priority"], row["trigger_id"]))
    selected = dict(matches[0])
    selected["matched_trigger_ids"] = "|".join(dict.fromkeys(row["trigger_id"] for row in matches))
    return selected


def stop_hit_index(price: pd.DataFrame, entry_idx: int, through_idx: int, signal_low: float) -> int | None:
    return shared_stop_hit_index(price, entry_idx, through_idx, signal_low)


def signal_snapshot_paths(report_date: str) -> list[Path]:
    report_date = normalize_date_text(report_date)
    paths = sorted(MODEL_SNAPSHOT_DIR.glob("daily_candidate_model_signals_for_report_*.csv"))
    out: list[Path] = []
    for path in paths:
        date = normalize_date_text(path.stem.rsplit("_", 1)[-1])
        if date and (not report_date or date <= report_date):
            out.append(path)
    return out


def load_volume_signal_history(current_signals: pd.DataFrame, report_date: str) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    signal_log = read_csv(MODEL_SIGNAL_LOG_CSV)
    if not signal_log.empty and {"model_id", "signal_date"}.issubset(signal_log.columns):
        signal_log = signal_log[
            signal_log["model_id"].astype(str).str.strip().eq(MODEL_ID)
            & signal_log["signal_date"].map(normalize_date_text).le(report_date)
        ].copy()
        if not signal_log.empty:
            signal_log["snapshot_report_date"] = signal_log["signal_date"].map(normalize_date_text)
            signal_log["_source_priority"] = 1
            frames.append(signal_log)

    for path in signal_snapshot_paths(report_date):
        frame = read_csv(path)
        if frame.empty or "model_id" not in frame.columns:
            continue
        frame = frame[frame["model_id"].astype(str).str.strip().eq(MODEL_ID)].copy()
        if frame.empty:
            continue
        frame["snapshot_report_date"] = normalize_date_text(path.stem.rsplit("_", 1)[-1])
        frame["_source_priority"] = 2
        frames.append(frame)

    current = daily_volume_signal_rows(current_signals, report_date)
    if not current.empty:
        current = current.copy()
        current["snapshot_report_date"] = normalize_date_text(report_date)
        current["_source_priority"] = 3
        frames.append(current)

    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames, ignore_index=True, sort=False)
    if "signal_date" not in out.columns:
        out["signal_date"] = out["snapshot_report_date"]
    out["signal_date"] = out["signal_date"].map(normalize_date_text)
    out["stock_id"] = out.get("stock_id", pd.Series(dtype=str)).map(stock_id_key)
    out = out[(out["signal_date"] != "") & (out["stock_id"] != "")].copy()
    out = collapse_signal_history_rows(out)
    if "display_rank" in out.columns:
        out["_display_order_num"] = pd.to_numeric(out["display_rank"], errors="coerce")
    elif "model_rank" in out.columns:
        out["_display_order_num"] = pd.to_numeric(out["model_rank"], errors="coerce")
    else:
        out["_display_order_num"] = range(1, len(out) + 1)
    out["_display_order_num"] = out["_display_order_num"].fillna(999999)
    return out.sort_values(["signal_date", "_display_order_num", "stock_id"]).drop(
        columns=["_display_order_num"],
        errors="ignore",
    )


def collapse_signal_history_rows(out: pd.DataFrame) -> pd.DataFrame:
    if out.empty:
        return out
    work = out.copy()
    if "_source_priority" not in work.columns:
        work["_source_priority"] = 0
    if "display_rank" in work.columns:
        work["_display_order_num"] = pd.to_numeric(work["display_rank"], errors="coerce")
    elif "model_rank" in work.columns:
        work["_display_order_num"] = pd.to_numeric(work["model_rank"], errors="coerce")
    else:
        work["_display_order_num"] = math.nan
    work["_source_priority"] = pd.to_numeric(work["_source_priority"], errors="coerce").fillna(0)
    work["_display_order_num"] = work["_display_order_num"].fillna(999999)
    work = work.sort_values(
        ["signal_date", "stock_id", "model_id", "_source_priority", "_display_order_num"],
        ascending=[True, True, True, False, True],
    )

    rows: list[dict[str, Any]] = []
    for _, part in work.groupby(["signal_date", "stock_id", "model_id"], sort=False, dropna=False):
        record: dict[str, Any] = {}
        for col in work.columns:
            if col in {"_source_priority", "_display_order_num"}:
                continue
            values = [safe_str(value) for value in part[col].tolist() if safe_str(value)]
            record[col] = values[0] if values else ""
        for rank_col in ["display_rank", "model_rank"]:
            if rank_col in part.columns:
                nums = pd.to_numeric(part[rank_col], errors="coerce").dropna()
                if not nums.empty:
                    best = float(nums.min())
                    record[rank_col] = str(int(best)) if best.is_integer() else f"{best:g}"
        rows.append(record)
    return pd.DataFrame(rows)


def format_md_date(date: str) -> str:
    date = normalize_date_text(date)
    if not date:
        return ""
    return f"{int(date[4:6])}/{int(date[6:8])}"


def format_price(value: float) -> str:
    if math.isnan(value):
        return ""
    return f"{value:.2f}".rstrip("0").rstrip(".")


def evidence_rows_for_trigger(summary: pd.DataFrame, trigger_id: str) -> pd.DataFrame:
    if summary.empty or "trigger_id" not in summary.columns:
        return pd.DataFrame()
    out = summary[summary["trigger_id"].astype(str).eq(trigger_id)].copy()
    if out.empty:
        return out
    for col in ["sample_size", "win_rate", "median_return", "avg_return", "ranking_research_score"]:
        if col in out.columns:
            out[f"_{col}"] = pd.to_numeric(out[col], errors="coerce")
    oos = out.get("out_of_sample_pass", pd.Series(dtype=str)).astype(str).str.lower().isin({"true", "1", "1.0"})
    eligible = out[
        out.get("_sample_size", pd.Series(dtype=float)).ge(10)
        & out.get("_win_rate", pd.Series(dtype=float)).ge(50)
        & out.get("_median_return", pd.Series(dtype=float)).gt(0)
        & out.get("_ranking_research_score", pd.Series(dtype=float)).gt(0)
        & oos
    ].copy()
    if eligible.empty:
        return pd.DataFrame()
    return eligible.sort_values(["_ranking_research_score", "_sample_size"], ascending=[False, False])


def best_evidence_for_trigger(summary: pd.DataFrame, trigger_id: str) -> pd.Series | None:
    rows = evidence_rows_for_trigger(summary, trigger_id)
    if rows.empty:
        return None
    return rows.iloc[0]


def pct_display(value: Any) -> str:
    num = number_text(value)
    if math.isnan(num):
        return ""
    return f"{num:.2f}%"


def rank_bucket_for_context(row: pd.Series) -> str:
    list_type = safe_str(row.get("tdcc_list_type"))
    if list_type == "no_tdcc":
        return "all"
    rank = number_text(row.get("tdcc_rank"))
    if math.isnan(rank):
        return ""
    if rank <= 10:
        return "top_10"
    if rank <= 20:
        return "top_20"
    if rank <= 50:
        return "top_50"
    return ""


def evidence_passes_daily_gate(evidence: pd.Series | None) -> bool:
    if evidence is None:
        return False
    return (
        number_text(evidence.get("sample_size")) >= 10
        and number_text(evidence.get("win_rate")) >= 50
        and number_text(evidence.get("median_return")) > 0
        and number_text(evidence.get("ranking_research_score")) > 0
        and true_text(evidence.get("out_of_sample_pass"))
    )


def evidence_key(evidence: pd.Series | None) -> str:
    if evidence is None:
        return ""
    return "|".join(
        [
            safe_str(evidence.get("tdcc_list_type")),
            safe_str(evidence.get("rank_bucket")),
            safe_str(evidence.get("trigger_id")),
            safe_str(evidence.get("confluence_scope")),
            safe_str(evidence.get("confluence_id")),
        ]
    )


def operation_context_rows(
    price: pd.DataFrame,
    signal_idx: int,
    selected: dict[str, Any],
    signal: pd.Series | None = None,
) -> pd.DataFrame:
    confirmation_idx = int(selected["confirmation_idx"])
    payload = operation_event_payload(price, signal_idx, confirmation_idx, market_regime_map())
    source_signal = signal if signal is not None else pd.Series(dtype=object)
    payload.update(
        {
            "stock_id": stock_id_key(source_signal.get("stock_id")) or stock_id_key(payload.get("stock_id")),
            "stock_name": safe_str(source_signal.get("stock_name")) or safe_str(payload.get("stock_name")),
            "trigger_id": safe_str(selected.get("trigger_id")),
            "trigger_name_zh": safe_str(selected.get("trigger_zh")),
            "matched_trigger_ids": safe_str(selected.get("matched_trigger_ids")),
            "selected_trigger_id": safe_str(selected.get("trigger_id")),
            "selected_confirmation_date": safe_str(selected.get("confirmation_date")),
            "selected_trigger_priority": safe_str(selected.get("trigger_priority")),
        }
    )
    return attach_tdcc_asof(pd.DataFrame([payload]), tdcc_events(), "confirmation_date")


def select_row_evidence(
    price: pd.DataFrame,
    signal_idx: int,
    selected: dict[str, Any],
    formal_summary: pd.DataFrame,
    signal: pd.Series | None = None,
) -> tuple[pd.Series | None, pd.Series | None, bool, list[dict[str, Any]]]:
    contexts = operation_context_rows(price, signal_idx, selected, signal)
    audit_rows: list[dict[str, Any]] = []
    candidates: list[tuple[float, float, pd.Series, pd.Series]] = []
    evaluated: list[tuple[float, float, pd.Series, pd.Series]] = []
    if contexts.empty:
        return None, None, False, audit_rows

    for _, context in contexts.iterrows():
        evidence = best_row_evidence(context, formal_summary)
        audit = evidence_audit_payload(context, evidence, "candidate_evaluated", False, "")
        audit_rows.append(audit)
        if evidence is not None:
            score = number_text(evidence.get("ranking_research_score"))
            sample = number_text(evidence.get("sample_size"))
            evaluated.append((score, sample, context, evidence))
        if not evidence_passes_daily_gate(evidence):
            continue
        assert evidence is not None
        score = number_text(evidence.get("ranking_research_score"))
        sample = number_text(evidence.get("sample_size"))
        candidates.append((score, sample, context, evidence))

    if not candidates:
        if evaluated:
            evaluated.sort(key=lambda item: (item[0], item[1]), reverse=True)
            return evaluated[0][3], evaluated[0][2], False, audit_rows
        return None, contexts.iloc[0], False, audit_rows
    candidates.sort(key=lambda item: (item[0], item[1]), reverse=True)
    context = candidates[0][2]
    evidence = candidates[0][3]
    audit_rows.append(evidence_audit_payload(context, evidence, "positive_row_evidence", True, "selected"))
    return evidence, context, True, audit_rows


def evidence_audit_payload(
    context: pd.Series,
    evidence: pd.Series | None,
    audit_status: str,
    included: bool,
    reason: str,
) -> dict[str, Any]:
    bucket = safe_str(evidence.get("rank_bucket")) if evidence is not None else rank_bucket_for_context(context)
    return {
        "model_id": MODEL_ID,
        "operation_asof_date": "",
        "stock_id": stock_id_key(context.get("stock_id")),
        "stock_name": safe_str(context.get("stock_name")),
        "signal_date": normalize_date_text(context.get("signal_date")),
        "selected_trigger_id": safe_str(context.get("selected_trigger_id") or context.get("trigger_id")),
        "selected_confirmation_date": normalize_date_text(context.get("selected_confirmation_date") or context.get("confirmation_date")),
        "operation_lifecycle_state": "",
        "audit_status": audit_status,
        "included_in_daily_adapter": "True" if included else "False",
        "tdcc_list_type": safe_str(context.get("tdcc_list_type")),
        "tdcc_rank": safe_str(context.get("tdcc_rank")),
        "rank_bucket": bucket,
        "classification_id": safe_str(context.get("classification_id")),
        "attack_method": safe_str(context.get("attack_method")),
        "price_position_type": safe_str(context.get("price_position_type")),
        "risk_type": safe_str(context.get("risk_type")),
        "evidence_confluence_scope": "" if evidence is None else safe_str(evidence.get("confluence_scope")),
        "evidence_confluence_id": "" if evidence is None else safe_str(evidence.get("confluence_id")),
        "evidence_sample_size": "" if evidence is None else safe_str(evidence.get("sample_size")),
        "evidence_win_rate": "" if evidence is None else safe_str(evidence.get("win_rate")),
        "evidence_avg_return": "" if evidence is None else safe_str(evidence.get("avg_return")),
        "evidence_median_return": "" if evidence is None else safe_str(evidence.get("median_return")),
        "evidence_out_of_sample_pass": "" if evidence is None else safe_str(evidence.get("out_of_sample_pass")),
        "ranking_research_score": "" if evidence is None else safe_str(evidence.get("ranking_research_score")),
        "reason": reason,
        "generated_at": "",
    }


def apply_evidence_fields(
    record: dict[str, Any],
    evidence: pd.Series,
    context: pd.Series,
    match_status: str = "positive_row_evidence",
) -> None:
    record.update(
        {
            "evidence_match_status": match_status,
            "evidence_tdcc_list_type": safe_str(evidence.get("tdcc_list_type")),
            "evidence_rank_bucket": safe_str(evidence.get("rank_bucket")),
            "evidence_confluence_scope": safe_str(evidence.get("confluence_scope")),
            "evidence_confluence_id": safe_str(evidence.get("confluence_id")),
            "evidence_key": evidence_key(evidence),
            "evidence_out_of_sample_pass": safe_str(evidence.get("out_of_sample_pass")),
            "sample_size": safe_str(evidence.get("sample_size")),
            "win_rate_zh": pct_display(evidence.get("win_rate")),
            "avg_return_zh": pct_display(evidence.get("avg_return")),
            "median_return_zh": pct_display(evidence.get("median_return")),
            "confidence_zh": safe_str(evidence.get("confidence_status")),
            "tdcc_status_zh": (
                f"{safe_str(context.get('tdcc_list_type'))} rank {safe_str(context.get('tdcc_rank'))}".strip()
                if safe_str(context.get("tdcc_list_type")) != "no_tdcc"
                else "no_tdcc"
            ),
        }
    )


def apply_signal_operation_fields(record: dict[str, Any], signal: pd.Series) -> None:
    for col in OPERATION_SCORE_FIELDS:
        record[col] = safe_str(signal.get(col))


def lifecycle_base_record(
    signal: pd.Series,
    approval: dict[str, str],
    generated_at: str,
    report_date: str,
    daily_volume_count: int,
    pdf_section: str,
    display_order: str,
) -> dict[str, Any]:
    stock_id = stock_id_key(signal.get("stock_id"))
    stock_name = safe_str(signal.get("stock_name"))
    record = {col: "" for col in OUTPUT_COLUMNS}
    record.update(
        {
            "model_id": MODEL_ID,
            "pdf_section": pdf_section,
            "pdf_section_zh": SECTION_ZH[pdf_section],
            "row_type": "data",
            "operation_asof_date": report_date,
            "operation_source_date_status": "ready",
            "display_order": display_order,
            "stock_id": stock_id,
            "stock_name": stock_name,
            "stock_display": f"{stock_id} {stock_name}".strip(),
            "operation_status": pdf_section,
            "signal_date": normalize_date_text(signal.get("signal_date")),
            "same_stock_pending_count": "1",
            "tdcc_status_zh": safe_str(signal.get("tdcc_status_zh")),
            "research_score": safe_str(signal.get("model_score")),
            "pdf_note_zh": safe_str(signal.get("risk_tags_zh") or signal.get("score_components_zh")),
            "daily_signal_date": report_date,
            "daily_volume_model_signal_count": daily_volume_count,
            "adapter_source": LIFECYCLE_ADAPTER_SOURCE,
            "adapter_source_status": "ready",
            "adapter_note_zh": "由已發布模型快照與價格資料重建 D0-D10 操作狀態。",
            "generated_at": generated_at,
        }
    )
    for col in APPROVAL_FIELDS:
        record[col] = approval[col]
    apply_signal_operation_fields(record, signal)
    return record


def confirmed_record(
    signal: pd.Series,
    selected: dict[str, Any],
    evidence: pd.Series,
    context: pd.Series,
    price: pd.DataFrame,
    signal_idx: int,
    report_idx: int,
    approval: dict[str, str],
    generated_at: str,
    report_date: str,
    daily_volume_count: int,
    display_order: str,
) -> dict[str, Any]:
    signal_row = price.iloc[signal_idx]
    signal_low = price_at(signal_row, "low")
    signal_date = normalize_date_text(signal_row.get("date"))
    record = lifecycle_base_record(
        signal,
        approval,
        generated_at,
        report_date,
        daily_volume_count,
        "confirmed_operation",
        display_order,
    )
    record.update(
        {
            "operation_status_zh": "已確認操作",
            "quality_status_zh": "正向證據",
            "matched_trigger_ids": safe_str(selected.get("matched_trigger_ids")),
            "selected_trigger_id": safe_str(selected.get("trigger_id")),
            "selected_confirmation_date": safe_str(selected.get("confirmation_date")),
            "selected_trigger_priority": safe_str(selected.get("trigger_priority")),
            "trigger_zh": safe_str(selected.get("trigger_zh")),
            "entry_basis_zh": "確認日收盤後列入，下一個交易日開盤價進場。",
            "entry_price_status_zh": "下一個交易日開盤價尚未產生。",
            "stop_basis_zh": f"跌破 {format_md_date(signal_date)} 最低價 {format_price(signal_low)}",
            "exit_rule_zh": "先跌破停損基準出場，否則最多持有至第 10 個交易日收盤。",
            "entry_rule_id": "confirmation_next_open",
            "entry_price_basis": "next_open_after_confirmation",
            "entry_date": "",
            "entry_price": "",
            "stop_loss_rule_id": "signal_low_stop",
            "stop_loss_price": format_price(signal_low),
            "stop_loss_label_zh": f"{format_md_date(signal_date)}最低點",
            "exit_rule_id": "signal_low_stop_or_fixed_10d_close",
            "planned_holding_days": str(MAX_HOLD_DAYS),
            "operation_age_days": str(report_idx - signal_idx),
            "confirmation_date": safe_str(selected.get("confirmation_date")),
            "row_action_status": "confirmed_buy_candidate",
            "buy_rank_eligible": "True",
        }
    )
    apply_evidence_fields(record, evidence, context)
    return record


def confirmed_unranked_record(
    signal: pd.Series,
    selected: dict[str, Any],
    evidence: pd.Series | None,
    context: pd.Series | None,
    price: pd.DataFrame,
    signal_idx: int,
    report_idx: int,
    approval: dict[str, str],
    generated_at: str,
    report_date: str,
    daily_volume_count: int,
    display_order: str,
) -> dict[str, Any]:
    signal_row = price.iloc[signal_idx]
    signal_low = price_at(signal_row, "low")
    signal_date = normalize_date_text(signal_row.get("date"))
    record = lifecycle_base_record(
        signal,
        approval,
        generated_at,
        report_date,
        daily_volume_count,
        "confirmed_unranked_operation",
        display_order,
    )
    record.update(
        {
            "operation_status_zh": "已確認但未通過買入排名門檻",
            "quality_status_zh": "未通過買入排名門檻",
            "matched_trigger_ids": safe_str(selected.get("matched_trigger_ids")),
            "selected_trigger_id": safe_str(selected.get("trigger_id")),
            "selected_confirmation_date": safe_str(selected.get("confirmation_date")),
            "selected_trigger_priority": safe_str(selected.get("trigger_priority")),
            "trigger_zh": safe_str(selected.get("trigger_zh")),
            "entry_basis_zh": "已確認但未通過買入排名門檻，不列進場價。",
            "entry_price_status_zh": "未通過買入排名門檻，不列進場價。",
            "stop_basis_zh": "未列買入排名，不列停損價。",
            "exit_rule_zh": "未列買入排名，不列出場規則。",
            "entry_rule_id": "",
            "entry_price_basis": "",
            "entry_date": "",
            "entry_price": "",
            "stop_loss_rule_id": "",
            "stop_loss_price": "",
            "stop_loss_label_zh": "",
            "exit_rule_id": "",
            "planned_holding_days": "",
            "operation_age_days": str(report_idx - signal_idx),
            "confirmation_date": safe_str(selected.get("confirmation_date")),
            "row_action_status": "confirmed_not_buy_ranked",
            "buy_rank_eligible": "False",
            "rank_reason_zh": (
                "已確認，但該股所屬 TDCC/型態/確認方式的正式歷史證據未通過買入排名門檻。"
            ),
        }
    )
    if evidence is not None and context is not None:
        apply_evidence_fields(record, evidence, context, "row_level_evidence_not_buy_ranked")
    else:
        record["evidence_match_status"] = "no_matching_row_level_evidence"
    return record


def active_record(
    signal: pd.Series,
    selected: dict[str, Any],
    evidence: pd.Series,
    context: pd.Series,
    price: pd.DataFrame,
    signal_idx: int,
    entry_idx: int,
    report_idx: int,
    approval: dict[str, str],
    generated_at: str,
    report_date: str,
    daily_volume_count: int,
    display_order: str,
) -> dict[str, Any]:
    signal_row = price.iloc[signal_idx]
    entry = price.iloc[entry_idx]
    signal_low = price_at(signal_row, "low")
    signal_date = normalize_date_text(signal_row.get("date"))
    record = lifecycle_base_record(
        signal,
        approval,
        generated_at,
        report_date,
        daily_volume_count,
        "active_operation",
        display_order,
    )
    record.update(
        {
            "operation_status_zh": "操作中",
            "quality_status_zh": "已進場追蹤",
            "matched_trigger_ids": safe_str(selected.get("matched_trigger_ids")),
            "selected_trigger_id": safe_str(selected.get("trigger_id")),
            "selected_confirmation_date": safe_str(selected.get("confirmation_date")),
            "selected_trigger_priority": safe_str(selected.get("trigger_priority")),
            "trigger_zh": safe_str(selected.get("trigger_zh")),
            "entry_basis_zh": "確認日收盤後列入，下一個交易日開盤價進場。",
            "entry_price_status_zh": (
                f"已進場追蹤；進場日 {format_md_date(normalize_date_text(entry.get('date')))} "
                f"開盤價 {format_price(price_at(entry, 'open'))}"
            ),
            "stop_basis_zh": f"跌破 {format_md_date(signal_date)} 最低價 {format_price(signal_low)}",
            "exit_rule_zh": "先跌破停損基準出場，否則最多持有至第 10 個交易日收盤。",
            "entry_rule_id": "confirmation_next_open",
            "entry_price_basis": "next_open_after_confirmation",
            "entry_date": normalize_date_text(entry.get("date")),
            "entry_price": format_price(price_at(entry, "open")),
            "stop_loss_rule_id": "signal_low_stop",
            "stop_loss_price": format_price(signal_low),
            "stop_loss_label_zh": f"{format_md_date(signal_date)}最低點",
            "exit_rule_id": "signal_low_stop_or_fixed_10d_close",
            "planned_holding_days": str(MAX_HOLD_DAYS),
            "operation_age_days": str(report_idx - signal_idx),
            "confirmation_date": safe_str(selected.get("confirmation_date")),
            "row_action_status": "active_operation",
            "buy_rank_eligible": "False",
        }
    )
    apply_evidence_fields(record, evidence, context)
    return record


def pending_record(
    signal: pd.Series,
    signal_age: int,
    approval: dict[str, str],
    generated_at: str,
    report_date: str,
    daily_volume_count: int,
    display_order: str,
) -> dict[str, Any]:
    record = lifecycle_base_record(
        signal,
        approval,
        generated_at,
        report_date,
        daily_volume_count,
        "pending_confirmation",
        display_order,
    )
    age_text = "今日訊號" if signal_age <= 0 else f"D+{signal_age} 待確認"
    record.update(
        {
            "operation_status_zh": "待確認",
            "quality_status_zh": "模型已命中，尚未確認",
            "entry_basis_zh": "尚未確認，不列進場價",
            "entry_price_status_zh": "尚未確認，不列進場價",
            "stop_basis_zh": "尚未確認，不列停損價",
            "exit_rule_zh": "待確認後才顯示操作規則",
            "entry_rule_id": "pending_confirmation",
            "entry_price_basis": "",
            "entry_date": "",
            "entry_price": "",
            "stop_loss_rule_id": "signal_low_stop_after_confirmation",
            "stop_loss_price": "",
            "stop_loss_label_zh": "",
            "exit_rule_id": "signal_low_stop_or_fixed_10d_close",
            "planned_holding_days": str(MAX_HOLD_DAYS),
            "operation_age_days": str(signal_age),
            "pending_age_zh": age_text,
            "pending_group_zh": signal_pending_group(signal),
            "pending_confirmation_zh": (
                "模型已命中但尚未確認，不能列買入排名；若確認前跌破訊號日最低價或超過 10 個交易日，則不列操作。"
            ),
            "sample_size": safe_str(signal.get("recommended_sample_size")),
            "win_rate_zh": safe_str(signal.get("best_close_win_rate_pct")),
            "avg_return_zh": safe_str(signal.get("best_avg_close_return_pct")),
            "confidence_zh": safe_str(signal.get("recommended_sample_status")),
            "row_action_status": "pending_confirmation",
            "buy_rank_eligible": "False",
        }
    )
    return record


def source_gap_audit_payload(
    signal: pd.Series,
    report_date: str,
    reason: str,
    generated_at: str,
) -> dict[str, Any]:
    return {
        "model_id": MODEL_ID,
        "operation_asof_date": normalize_date_text(report_date),
        "stock_id": stock_id_key(signal.get("stock_id")),
        "stock_name": safe_str(signal.get("stock_name")),
        "signal_date": normalize_date_text(signal.get("signal_date")),
        "selected_trigger_id": "",
        "selected_confirmation_date": "",
        "operation_lifecycle_state": "source_gap",
        "audit_status": "source_gap",
        "included_in_daily_adapter": "False",
        "tdcc_list_type": "",
        "tdcc_rank": "",
        "rank_bucket": "",
        "classification_id": "",
        "attack_method": "",
        "price_position_type": "",
        "risk_type": "",
        "evidence_confluence_scope": "",
        "evidence_confluence_id": "",
        "evidence_sample_size": "",
        "evidence_win_rate": "",
        "evidence_avg_return": "",
        "evidence_median_return": "",
        "evidence_out_of_sample_pass": "",
        "ranking_research_score": "",
        "reason": reason,
        "generated_at": generated_at,
    }


def lifecycle_gate_audit_payload(
    signal: pd.Series,
    selected: dict[str, Any],
    report_date: str,
    reason: str,
    generated_at: str,
) -> dict[str, Any]:
    return {
        "model_id": MODEL_ID,
        "operation_asof_date": normalize_date_text(report_date),
        "stock_id": stock_id_key(signal.get("stock_id")),
        "stock_name": safe_str(signal.get("stock_name")),
        "signal_date": normalize_date_text(signal.get("signal_date")),
        "selected_trigger_id": safe_str(selected.get("trigger_id")),
        "selected_confirmation_date": normalize_date_text(selected.get("confirmation_date")),
        "operation_lifecycle_state": "active_operation_suppressed",
        "audit_status": "lifecycle_suppressed",
        "included_in_daily_adapter": "False",
        "tdcc_list_type": "",
        "tdcc_rank": "",
        "rank_bucket": "",
        "classification_id": "",
        "attack_method": "",
        "price_position_type": "",
        "risk_type": "",
        "evidence_confluence_scope": "",
        "evidence_confluence_id": "",
        "evidence_sample_size": "",
        "evidence_win_rate": "",
        "evidence_avg_return": "",
        "evidence_median_return": "",
        "evidence_out_of_sample_pass": "",
        "ranking_research_score": "",
        "reason": reason,
        "generated_at": generated_at,
    }


def lifecycle_suppression_audit_payload(
    record: dict[str, Any],
    winner: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    winner_state = safe_str(winner.get("pdf_section") or winner.get("operation_status"))
    return {
        "model_id": MODEL_ID,
        "operation_asof_date": normalize_date_text(record.get("operation_asof_date")),
        "stock_id": stock_id_key(record.get("stock_id")),
        "stock_name": safe_str(record.get("stock_name")),
        "signal_date": normalize_date_text(record.get("signal_date")),
        "selected_trigger_id": safe_str(record.get("selected_trigger_id")),
        "selected_confirmation_date": normalize_date_text(record.get("selected_confirmation_date")),
        "operation_lifecycle_state": safe_str(record.get("pdf_section") or record.get("operation_status")),
        "audit_status": "lifecycle_suppressed",
        "included_in_daily_adapter": "False",
        "tdcc_list_type": safe_str(record.get("evidence_tdcc_list_type")),
        "tdcc_rank": "",
        "rank_bucket": safe_str(record.get("evidence_rank_bucket")),
        "classification_id": "",
        "attack_method": "",
        "price_position_type": "",
        "risk_type": "",
        "evidence_confluence_scope": safe_str(record.get("evidence_confluence_scope")),
        "evidence_confluence_id": safe_str(record.get("evidence_confluence_id")),
        "evidence_sample_size": safe_str(record.get("sample_size")),
        "evidence_win_rate": safe_str(record.get("win_rate_zh")),
        "evidence_avg_return": safe_str(record.get("avg_return_zh")),
        "evidence_median_return": safe_str(record.get("median_return_zh")),
        "evidence_out_of_sample_pass": safe_str(record.get("evidence_out_of_sample_pass")),
        "ranking_research_score": "",
        "reason": f"same_stock_lifecycle_suppressed_by_{winner_state}",
        "generated_at": generated_at,
    }


def lifecycle_state_for_signal(
    signal: pd.Series,
    report_date: str,
    formal_summary: pd.DataFrame,
    approval: dict[str, str],
    generated_at: str,
    daily_volume_count: int,
) -> tuple[int, dict[str, Any] | None, list[dict[str, Any]]]:
    audit_rows: list[dict[str, Any]] = []
    stock_id = stock_id_key(signal.get("stock_id"))
    signal_date = normalize_date_text(signal.get("signal_date"))
    if not stock_id or not signal_date:
        audit_rows.append(source_gap_audit_payload(signal, report_date, "missing_signal_identity", generated_at))
        return 99, None, audit_rows
    price_path = STOCK_PRICE_HISTORY_DIR / f"{stock_id}.csv"
    price = load_price_history(stock_id)
    if price.empty:
        reason = "missing_stock_price_history_file" if not price_path.exists() else "unusable_stock_price_history"
        audit_rows.append(source_gap_audit_payload(signal, report_date, reason, generated_at))
        return 99, None, audit_rows
    signal_positions = price.index[price["date"].astype(str).eq(signal_date)].tolist()
    report_positions = price.index[price["date"].astype(str).eq(report_date)].tolist()
    if not signal_positions:
        audit_rows.append(
            source_gap_audit_payload(signal, report_date, "signal_date_missing_in_stock_price_history", generated_at)
        )
        return 99, None, audit_rows
    if not report_positions:
        audit_rows.append(
            source_gap_audit_payload(
                signal,
                report_date,
                "operation_asof_date_missing_in_stock_price_history",
                generated_at,
            )
        )
        return 99, None, audit_rows
    signal_idx = int(signal_positions[-1])
    report_idx = int(report_positions[-1])
    if signal_idx > report_idx:
        audit_rows.append(source_gap_audit_payload(signal, report_date, "signal_date_after_operation_asof_date", generated_at))
        return 99, None, audit_rows
    signal_age = report_idx - signal_idx
    display_order = safe_str(signal.get("display_rank") or signal.get("model_rank") or "999999")
    signal_low = price_at(price.iloc[signal_idx], "low")
    if math.isnan(signal_low):
        audit_rows.append(source_gap_audit_payload(signal, report_date, "signal_low_missing_in_stock_price_history", generated_at))
        return 99, None, audit_rows

    selected = selected_confirmation(price, signal_idx, report_idx)
    if selected is not None:
        confirmation_idx = int(selected["confirmation_idx"])
        entry_idx = confirmation_idx + 1
        if confirmation_idx < report_idx:
            active_backed_by_snapshot, snapshot_reason = active_snapshot_backing(signal, selected, report_date)
            if not active_backed_by_snapshot:
                audit_rows.append(
                    lifecycle_gate_audit_payload(signal, selected, report_date, snapshot_reason, generated_at)
                )
                return 90, None, audit_rows

        evidence, context, is_buy_rank_eligible, evidence_audit = select_row_evidence(
            price,
            signal_idx,
            selected,
            formal_summary,
            signal,
        )
        audit_rows.extend(evidence_audit)
        if confirmation_idx == report_idx:
            if is_buy_rank_eligible and evidence is not None and context is not None:
                record = confirmed_record(
                    signal,
                    selected,
                    evidence,
                    context,
                    price,
                    signal_idx,
                    report_idx,
                    approval,
                    generated_at,
                    report_date,
                    daily_volume_count,
                    display_order,
                )
                lifecycle_state = "confirmed_operation"
                priority = 1
            else:
                record = confirmed_unranked_record(
                    signal,
                    selected,
                    evidence,
                    context,
                    price,
                    signal_idx,
                    report_idx,
                    approval,
                    generated_at,
                    report_date,
                    daily_volume_count,
                    display_order,
                )
                lifecycle_state = "confirmed_unranked_operation"
                priority = 2
            for audit in audit_rows:
                audit["operation_asof_date"] = report_date
                audit["operation_lifecycle_state"] = lifecycle_state
                audit["generated_at"] = generated_at
                if not audit["reason"] and not is_buy_rank_eligible:
                    audit["reason"] = "confirmed_but_not_buy_ranked"
            return priority, record, audit_rows
        if not is_buy_rank_eligible or evidence is None or context is None:
            for audit in audit_rows:
                audit["operation_asof_date"] = report_date
                audit["operation_lifecycle_state"] = "confirmed_unranked_expired"
                audit["generated_at"] = generated_at
                if not audit["reason"]:
                    audit["reason"] = "confirmed_without_buy_rank_eligibility_not_tracked_active"
            return 90, None, audit_rows
        if entry_idx < len(price) and report_idx >= entry_idx:
            planned_exit_idx = entry_idx + MAX_HOLD_DAYS - 1
            stopped_idx = stop_hit_index(price, entry_idx, report_idx, signal_low)
            if stopped_idx is None and report_idx <= planned_exit_idx:
                record = active_record(
                    signal,
                    selected,
                    evidence,
                    context,
                    price,
                    signal_idx,
                    entry_idx,
                    report_idx,
                    approval,
                    generated_at,
                    report_date,
                    daily_volume_count,
                    display_order,
                )
                for audit in audit_rows:
                    audit["operation_asof_date"] = report_date
                    audit["operation_lifecycle_state"] = "active_operation"
                    audit["generated_at"] = generated_at
                return 0, record, audit_rows
        for audit in audit_rows:
            audit["operation_asof_date"] = report_date
            audit["operation_lifecycle_state"] = "expired"
            audit["included_in_daily_adapter"] = "False"
            audit["generated_at"] = generated_at
        return 90, None, audit_rows

    if signal_age <= MAX_CONFIRM_DAYS and not signal_low_broken(price, signal_idx, report_idx, signal_low):
        return 3, pending_record(signal, signal_age, approval, generated_at, report_date, daily_volume_count, display_order), audit_rows
    return 90, None, audit_rows


def build_lifecycle_rows(
    signals: pd.DataFrame,
    report_date: str,
    daily_volume_count: int,
    approval: dict[str, str],
    generated_at: str,
    formal_summary: pd.DataFrame,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    history = load_volume_signal_history(signals, report_date)
    if history.empty:
        return [], []

    candidates_by_stock: dict[str, list[tuple[int, int, dict[str, Any]]]] = {}
    audit_rows: list[dict[str, Any]] = []
    for seq, (_, signal) in enumerate(history.iterrows()):
        priority, record, signal_audit = lifecycle_state_for_signal(
            signal,
            report_date,
            formal_summary,
            approval,
            generated_at,
            daily_volume_count,
        )
        audit_rows.extend(signal_audit)
        if record is None:
            continue
        stock_id = stock_id_key(record.get("stock_id"))
        candidates_by_stock.setdefault(stock_id, []).append((priority, seq, record))

    best_by_stock: dict[str, tuple[int, dict[str, Any]]] = {}
    for stock_id, candidates in candidates_by_stock.items():
        candidates = sorted(candidates, key=lambda item: (item[0], item[1]))
        winner_priority, _winner_seq, winner = candidates[0]
        best_by_stock[stock_id] = (winner_priority, winner)
        for _priority, _seq, record in candidates[1:]:
            audit_rows.append(lifecycle_suppression_audit_payload(record, winner, generated_at))

    base_rows = [item[1] for item in sorted(best_by_stock.values(), key=lambda item: (item[0], number_text(item[1].get("display_order")), item[1].get("stock_id", "")))]
    selected_evidence_keys = {
        (
            stock_id_key(row.get("stock_id")),
            normalize_date_text(row.get("signal_date")),
            safe_str(row.get("selected_trigger_id")),
            safe_str(row.get("evidence_tdcc_list_type")),
            safe_str(row.get("evidence_rank_bucket")),
            safe_str(row.get("evidence_confluence_scope")),
            safe_str(row.get("evidence_confluence_id")),
        )
        for row in base_rows
        if safe_str(row.get("pdf_section")) in {"confirmed_operation", "active_operation"}
        and safe_str(row.get("evidence_match_status")) == "positive_row_evidence"
    }
    for audit in audit_rows:
        audit_key = (
            stock_id_key(audit.get("stock_id")),
            normalize_date_text(audit.get("signal_date")),
            safe_str(audit.get("selected_trigger_id")),
            safe_str(audit.get("tdcc_list_type")),
            safe_str(audit.get("rank_bucket")),
            safe_str(audit.get("evidence_confluence_scope")),
            safe_str(audit.get("evidence_confluence_id")),
        )
        audit["included_in_daily_adapter"] = (
            "True"
            if safe_str(audit.get("audit_status")) == "positive_row_evidence"
            and safe_str(audit.get("operation_lifecycle_state")) in {"confirmed_operation", "active_operation"}
            and audit_key in selected_evidence_keys
            else "False"
        )
    rows: list[dict[str, Any]] = []
    for pdf_view in PDF_VIEWS:
        for idx, row in enumerate(base_rows, start=1):
            if not section_allowed_for_pdf_view(pdf_view, safe_str(row.get("pdf_section"))):
                continue
            record = dict(row)
            record["pdf_view"] = pdf_view
            if not safe_str(record.get("display_order")) or safe_str(record.get("display_order")) == "999999":
                record["display_order"] = str(idx)
            rows.append(record)
    return rows, audit_rows


def empty_row(
    pdf_view: str,
    pdf_section: str,
    source_status: str,
    daily_signal_date: str,
    daily_volume_count: int,
    approval: dict[str, str],
    generated_at: str,
    operation_asof_date: str = "",
) -> dict[str, Any]:
    section_zh = SECTION_ZH[pdf_section]
    adapter_note = SECTION_EMPTY_NOTE_ZH[pdf_section]
    return {
        "model_id": MODEL_ID,
        "pdf_view": pdf_view,
        "pdf_section": pdf_section,
        "pdf_section_zh": section_zh,
        "row_type": "empty_state",
        "operation_asof_date": operation_asof_date,
        "operation_source_date_status": source_status,
        "display_order": 0,
        "stock_id": "",
        "stock_name": "",
        "stock_display": "目前無資料",
        "operation_status": pdf_section,
        "operation_status_zh": section_zh,
        "quality_status_zh": "目前無資料",
        "matched_trigger_ids": "",
        "selected_trigger_id": "",
        "selected_confirmation_date": "",
        "selected_trigger_priority": "",
        "trigger_zh": "",
        "entry_basis_zh": "",
        "entry_price_status_zh": "",
        "stop_basis_zh": "",
        "exit_rule_zh": "",
        "signal_date": "",
        "confirmation_date": "",
        "pending_age_zh": "",
        "pending_group_zh": "",
        "pending_confirmation_zh": "",
        "same_stock_pending_count": "",
        "tdcc_status_zh": "",
        "sample_size": "",
        "win_rate_zh": "",
        "avg_return_zh": "",
        "median_return_zh": "",
        "confidence_zh": "",
        "research_score": "",
        "pdf_note_zh": "",
        "daily_signal_date": daily_signal_date,
        "daily_volume_model_signal_count": daily_volume_count,
        "adapter_source": LIFECYCLE_ADAPTER_SOURCE,
        "adapter_source_status": source_status,
        **approval,
        "row_action_status": "empty_state",
        "buy_rank_eligible": "False",
        "adapter_note_zh": adapter_note,
        "generated_at": generated_at,
    }


def write_outputs(df: pd.DataFrame, source_rows: int, source_status: str) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")

    lines = [
        "# Daily Volume Breakout Operation Section",
        "",
        f"- generated_at: `{safe_str(df['generated_at'].iloc[0]) if not df.empty else now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        f"- source: `{LIFECYCLE_ADAPTER_SOURCE}`",
        f"- approval_source: `{safe_str(df['approval_source'].iloc[0]) if not df.empty else APPROVAL_SOURCE}`",
        f"- approved_for_daily: `{safe_str(df['approved_for_daily'].iloc[0]) if not df.empty else 'False'}`",
        f"- approval_version: `{safe_str(df['approval_version'].iloc[0]) if not df.empty else ''}`",
        f"- source_status: `{source_status}`",
        f"- source_rows: `{source_rows}`",
        "- purpose: production presentation adapter only; PDF/packet 必須讀取本 artifact，且不得重新計算進場、停損、出場或排名。",
        "- sections: confirmed_operation, confirmed_unranked_operation, pending_confirmation, active_operation.",
        "",
    ]
    for pdf_view in PDF_VIEWS:
        lines.extend([f"## {pdf_view}", ""])
        for section in PDF_SECTIONS:
            part = df[(df["pdf_view"].eq(pdf_view)) & (df["pdf_section"].eq(section))].copy()
            lines.extend([f"### {SECTION_ZH[section]}", ""])
            display_cols = [
                "display_order",
                "row_type",
                "stock_display",
                "trigger_zh",
                "entry_basis_zh",
                "stop_basis_zh",
                "exit_rule_zh",
                "pending_age_zh",
                "sample_size",
                "win_rate_zh",
                "median_return_zh",
                "approved_for_daily",
                "operation_module_approved_for_daily",
                "operation_directive_level",
                "row_action_status",
                "buy_rank_eligible",
                "adapter_note_zh",
            ]
            try:
                lines.append(part[display_cols].to_markdown(index=False))
            except Exception:
                lines.append(part[display_cols].to_string(index=False))
            lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8", newline="\n")

    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_LATEST_DIR / OUT_CSV.name).write_bytes(OUT_CSV.read_bytes())
    (DOCS_LATEST_DIR / OUT_MD.name).write_bytes(OUT_MD.read_bytes())


def write_evidence_audit(audit: pd.DataFrame) -> None:
    audit = audit.copy()
    if audit.empty:
        audit = pd.DataFrame(columns=EVIDENCE_AUDIT_COLUMNS)
    else:
        for col in EVIDENCE_AUDIT_COLUMNS:
            if col not in audit.columns:
                audit[col] = ""
        audit = audit[EVIDENCE_AUDIT_COLUMNS]
    EVIDENCE_AUDIT_CSV.parent.mkdir(parents=True, exist_ok=True)
    audit.to_csv(EVIDENCE_AUDIT_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")

    lines = [
        "# Daily Volume Breakout Operation Evidence Audit",
        "",
        f"- generated_at: `{safe_str(audit['generated_at'].iloc[0]) if not audit.empty else now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        "- purpose: row-level audit proving daily adapter evidence is attributed to each stock's own TDCC/trigger/pattern context.",
        "- rule: buy-ranked confirmed/active daily rows must use `positive_row_evidence`; confirmed rows without buy-ranking evidence are tracked separately as `confirmed_unranked_operation`.",
        "",
    ]
    if audit.empty:
        lines.append("_No evaluated confirmed or active operation rows._")
    else:
        display_cols = [
            "stock_id",
            "stock_name",
            "signal_date",
            "selected_trigger_id",
            "operation_lifecycle_state",
            "audit_status",
            "included_in_daily_adapter",
            "tdcc_list_type",
            "rank_bucket",
            "classification_id",
            "attack_method",
            "price_position_type",
            "evidence_confluence_scope",
            "evidence_confluence_id",
            "evidence_sample_size",
            "evidence_win_rate",
            "evidence_median_return",
            "evidence_out_of_sample_pass",
            "ranking_research_score",
            "reason",
        ]
        try:
            lines.append(audit[display_cols].to_markdown(index=False))
        except Exception:
            lines.append(audit[display_cols].to_string(index=False))
    EVIDENCE_AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_LATEST_DIR / EVIDENCE_AUDIT_CSV.name).write_bytes(EVIDENCE_AUDIT_CSV.read_bytes())
    (DOCS_LATEST_DIR / EVIDENCE_AUDIT_MD.name).write_bytes(EVIDENCE_AUDIT_MD.read_bytes())


def build() -> tuple[pd.DataFrame, pd.DataFrame]:
    signals = read_csv(DAILY_SIGNALS_CSV)
    approval = read_csv(APPROVAL_CSV)
    formal_summary = read_csv(FORMAL_SUMMARY_CSV)
    report_date = main_price_date()
    require_latest_signals_match_report_date(signals, report_date)
    daily_signal_date, daily_volume_count = daily_signal_context(signals, report_date)
    restored = restore_published_snapshot(daily_signal_date)
    if restored is not None:
        return restored
    generated_at = now_text()
    approval_info = approval_context(approval)
    rows, audit_rows = build_lifecycle_rows(
        signals,
        daily_signal_date,
        daily_volume_count,
        approval_info,
        generated_at,
        formal_summary,
    )
    existing = {
        (safe_str(row.get("pdf_view")), safe_str(row.get("pdf_section")))
        for row in rows
        if safe_str(row.get("row_type")) == "data"
    }
    for pdf_view in PDF_VIEWS:
        for pdf_section in PDF_SECTIONS:
            if not section_allowed_for_pdf_view(pdf_view, pdf_section):
                continue
            if (pdf_view, pdf_section) not in existing:
                rows.append(
                    empty_row(
                        pdf_view,
                        pdf_section,
                        "ready",
                        daily_signal_date,
                        daily_volume_count,
                        approval_info,
                        generated_at,
                        daily_signal_date,
                    )
                )
    out = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    out["_view_order"] = out["pdf_view"].map({"highlight": 0, "full": 1}).fillna(9)
    out["_section_order"] = out["pdf_section"].map(
        {
            "confirmed_operation": 0,
            "confirmed_unranked_operation": 1,
            "pending_confirmation": 2,
            "active_operation": 3,
        }
    ).fillna(9)
    out["_row_type_order"] = out["row_type"].map({"data": 0, "empty_state": 1}).fillna(9)
    out["_display_order_num"] = pd.to_numeric(out["display_order"], errors="coerce").fillna(999999)
    out = out.sort_values(["_view_order", "_section_order", "_row_type_order", "_display_order_num", "stock_id"])
    section = out.drop(columns=["_view_order", "_section_order", "_row_type_order", "_display_order_num"]).reset_index(drop=True)
    audit = pd.DataFrame(audit_rows, columns=EVIDENCE_AUDIT_COLUMNS)
    return section, audit


def main() -> int:
    out, audit = build()
    source_rows = int(out[out["row_type"].astype(str).eq("data")]["stock_id"].astype(str).replace("", pd.NA).dropna().nunique())
    write_outputs(out, source_rows, "ready")
    write_evidence_audit(audit)
    print(f"Saved: {OUT_CSV} rows={len(out)}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {EVIDENCE_AUDIT_CSV} rows={len(audit)}")
    print(f"Saved: {EVIDENCE_AUDIT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
