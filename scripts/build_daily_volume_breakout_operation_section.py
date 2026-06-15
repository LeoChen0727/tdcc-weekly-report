from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

SOURCE_PREVIEW_CSV = LATEST_DIR / "volume_breakout_operation_pdf_preview_latest.csv"
DAILY_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
APPROVAL_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"

OUT_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
OUT_MD = LATEST_DIR / "daily_volume_breakout_operation_section_latest.md"

MODEL_ID = "volume_range_breakout"
ADAPTER_SOURCE = "volume_breakout_operation_pdf_preview_latest.csv"
DAILY_SIGNAL_SOURCE = "daily_candidate_model_signals_for_report_latest.csv"
APPROVAL_SOURCE = "approved_operation_patterns_latest.csv"
PDF_VIEWS = ("highlight", "full")
PDF_SECTIONS = ("confirmed_operation", "pending_confirmation", "active_operation")

SECTION_ZH = {
    "confirmed_operation": "已確認操作",
    "pending_confirmation": "待確認",
    "active_operation": "操作中",
}

SECTION_EMPTY_NOTE_ZH = {
    "confirmed_operation": "目前沒有符合研究證據門檻的已確認操作列。",
    "pending_confirmation": "目前沒有待確認的放量攻擊訊號。",
    "active_operation": "目前 research artifact 尚未提供操作中追蹤列；正式 PDF 可保留空表格。",
}

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


def number_text(value: Any) -> float:
    text = safe_str(value).replace("%", "").replace("+", "").replace(",", "")
    if not text:
        return float("nan")
    try:
        return float(text)
    except Exception:
        return float("nan")


def normalize_date_text(value: Any) -> str:
    text = safe_str(value).replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""


def stock_id_key(value: Any) -> str:
    text = safe_str(value).replace(".0", "")
    return text.zfill(4) if text.isdigit() else text


def main_price_date() -> str:
    freshness = read_csv(DATA_FRESHNESS_CSV)
    if freshness.empty or "main_price_date" not in freshness.columns:
        return ""
    return normalize_date_text(freshness.iloc[0].get("main_price_date"))


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


def approved_confirmed_source_row(row: pd.Series) -> bool:
    quality = safe_str(row.get("quality_status_zh"))
    if quality:
        return quality == "正向證據"
    sample = number_text(row.get("sample_size"))
    win = number_text(row.get("win_rate_zh"))
    median = number_text(row.get("median_return_zh"))
    score = number_text(row.get("research_score"))
    return sample >= 10 and win >= 50 and median > 0 and score > 0


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


def pending_rows_from_daily_signals(
    signals: pd.DataFrame,
    daily_signal_date: str,
    daily_volume_count: int,
    approval: dict[str, str],
    generated_at: str,
    exclude_stock_ids: set[str] | None = None,
) -> list[dict[str, Any]]:
    volume = daily_volume_signal_rows(signals, daily_signal_date)
    rows: list[dict[str, Any]] = []
    if volume.empty:
        return rows
    excluded = {stock_id_key(value) for value in (exclude_stock_ids or set()) if stock_id_key(value)}
    for pdf_view in PDF_VIEWS:
        for idx, (_, signal) in enumerate(volume.iterrows(), start=1):
            stock_id = safe_str(signal.get("stock_id"))
            if stock_id_key(stock_id) in excluded:
                continue
            stock_name = safe_str(signal.get("stock_name"))
            display_order = safe_str(signal.get("display_rank") or signal.get("model_rank") or idx)
            record = {col: "" for col in OUTPUT_COLUMNS}
            record.update(
                {
                    "model_id": MODEL_ID,
                    "pdf_view": pdf_view,
                    "pdf_section": "pending_confirmation",
                    "pdf_section_zh": SECTION_ZH["pending_confirmation"],
                    "row_type": "data",
                    "operation_asof_date": daily_signal_date,
                    "operation_source_date_status": "ready",
                    "display_order": display_order,
                    "stock_id": stock_id,
                    "stock_name": stock_name,
                    "stock_display": f"{stock_id} {stock_name}".strip(),
                    "operation_status_zh": "待確認",
                    "quality_status_zh": "今日模型命中，尚未確認",
                    "trigger_zh": "",
                    "entry_basis_zh": "尚未確認，不列進場價",
                    "entry_price_status_zh": "尚未確認，不列進場價",
                    "stop_basis_zh": "尚未確認，不列停損價",
                    "exit_rule_zh": "待確認後才顯示操作規則",
                    "signal_date": daily_signal_date,
                    "confirmation_date": "",
                    "pending_age_zh": "今日訊號",
                    "pending_group_zh": signal_pending_group(signal),
                    "pending_confirmation_zh": signal_pending_text(signal),
                    "same_stock_pending_count": "1",
                    "tdcc_status_zh": safe_str(signal.get("tdcc_status_zh")),
                    "sample_size": safe_str(signal.get("recommended_sample_size")),
                    "win_rate_zh": safe_str(signal.get("best_close_win_rate_pct")),
                    "avg_return_zh": safe_str(signal.get("best_avg_close_return_pct")),
                    "median_return_zh": "",
                    "confidence_zh": safe_str(signal.get("recommended_sample_status")),
                    "research_score": safe_str(signal.get("model_score")),
                    "pdf_note_zh": safe_str(signal.get("risk_tags_zh") or signal.get("score_components_zh")),
                    "daily_signal_date": daily_signal_date,
                    "daily_volume_model_signal_count": daily_volume_count,
                    "adapter_source": DAILY_SIGNAL_SOURCE,
                    "adapter_source_status": "ready",
                    "row_action_status": "pending_confirmation",
                    "buy_rank_eligible": "False",
                    "adapter_note_zh": "今日放量攻擊模型命中，列入待確認；不列進場價，不列買入排名，不重新計算操作規則。",
                    "generated_at": generated_at,
                }
            )
            for col in APPROVAL_FIELDS:
                record[col] = approval[col]
            rows.append(record)
    return rows


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
    if source_status == "stale_research_source":
        adapter_note = f"{section_zh}：來源日期不符，今日不顯示舊操作列；不重新計算操作規則。"
    else:
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
        "operation_status_zh": section_zh,
        "quality_status_zh": "目前無資料",
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
        "adapter_source": ADAPTER_SOURCE,
        "adapter_source_status": source_status,
        **approval,
        "row_action_status": "empty_state",
        "buy_rank_eligible": "False",
        "adapter_note_zh": adapter_note,
        "generated_at": generated_at,
    }


def operation_asof_dates(source: pd.DataFrame) -> list[str]:
    if source.empty or "operation_asof_date" not in source.columns:
        return []
    return sorted(
        {normalize_date_text(value) for value in source["operation_asof_date"].tolist() if normalize_date_text(value)}
    )


def source_date_status(source: pd.DataFrame, daily_signal_date: str, source_status: str) -> tuple[str, str]:
    if source.empty or source_status != "ready":
        return source_status, ""
    dates = operation_asof_dates(source)
    daily_date = normalize_date_text(daily_signal_date)
    if len(dates) == 1 and dates[0] == daily_date:
        return "ready", dates[0]
    return "stale_research_source", "|".join(dates) if dates else "missing"


def normalize_source_rows(
    source: pd.DataFrame,
    source_status: str,
    daily_signal_date: str,
    daily_volume_count: int,
    approval: dict[str, str],
    generated_at: str,
    signals: pd.DataFrame | None = None,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    allowed = source.copy()
    effective_source_status, operation_asof_date = source_date_status(allowed, daily_signal_date, source_status)
    if effective_source_status == "stale_research_source":
        allowed = allowed.iloc[0:0].copy()
    if not allowed.empty:
        if "model_id" in allowed.columns:
            allowed = allowed[allowed["model_id"].astype(str).str.strip().eq(MODEL_ID)].copy()
        else:
            allowed = allowed.iloc[0:0].copy()
        if "pdf_section" in allowed.columns:
            allowed = allowed[allowed["pdf_section"].astype(str).str.strip().eq("confirmed_operation")].copy()
        else:
            allowed = allowed.iloc[0:0].copy()
        if "pdf_view" in allowed.columns:
            allowed = allowed[allowed["pdf_view"].astype(str).str.strip().isin(PDF_VIEWS)].copy()
        else:
            allowed = allowed.iloc[0:0].copy()
        if not allowed.empty:
            confirmed = allowed["pdf_section"].astype(str).str.strip().eq("confirmed_operation")
            approved_confirmed = allowed.apply(approved_confirmed_source_row, axis=1)
            allowed = allowed[(~confirmed) | approved_confirmed].copy()

    for _, row in allowed.iterrows():
        record = {col: safe_str(row.get(col)) for col in OUTPUT_COLUMNS}
        section = safe_str(row.get("pdf_section"))
        record["model_id"] = MODEL_ID
        record["pdf_view"] = safe_str(row.get("pdf_view"))
        record["pdf_section"] = section
        record["pdf_section_zh"] = SECTION_ZH.get(section, section)
        record["row_type"] = "data"
        record["operation_asof_date"] = normalize_date_text(row.get("operation_asof_date"))
        record["operation_source_date_status"] = effective_source_status
        record["daily_signal_date"] = daily_signal_date
        record["daily_volume_model_signal_count"] = daily_volume_count
        record["adapter_source"] = ADAPTER_SOURCE
        record["adapter_source_status"] = effective_source_status
        for col in APPROVAL_FIELDS:
            record[col] = approval[col]
        is_confirmed_buy = (
            section == "confirmed_operation"
            and approval["approved_for_daily"] == "True"
            and approval["operation_directive_level"] == "approved_daily_operation_guidance"
            and approved_confirmed_source_row(row)
        )
        if section == "confirmed_operation":
            record["row_action_status"] = "confirmed_buy_candidate" if is_confirmed_buy else "confirmed_not_buy_rank_eligible"
        elif section == "pending_confirmation":
            record["row_action_status"] = "pending_confirmation"
        else:
            record["row_action_status"] = "display_only"
        record["buy_rank_eligible"] = "True" if is_confirmed_buy else "False"
        record["adapter_note_zh"] = (
            "PDF 僅呈現 daily adapter 欄位，不重新計算進場、停損、出場或排名。"
            if approval["approved_for_daily"] == "True"
            else "PDF 僅呈現 research adapter 欄位，不重新計算進場、停損、出場或排名。"
        )
        record["generated_at"] = generated_at
        rows.append(record)

    confirmed_stock_ids = {
        stock_id_key(row.get("stock_id"))
        for row in rows
        if safe_str(row.get("pdf_section")) == "confirmed_operation"
        and safe_str(row.get("row_type")) == "data"
        and stock_id_key(row.get("stock_id"))
    }
    rows.extend(
        pending_rows_from_daily_signals(
            signals if signals is not None else pd.DataFrame(),
            daily_signal_date,
            daily_volume_count,
            approval,
            generated_at,
            confirmed_stock_ids,
        )
    )

    existing = {
        (safe_str(row.get("pdf_view")), safe_str(row.get("pdf_section")))
        for row in rows
        if safe_str(row.get("row_type")) == "data"
    }
    for pdf_view in PDF_VIEWS:
        for pdf_section in PDF_SECTIONS:
            if (pdf_view, pdf_section) not in existing:
                rows.append(
                    empty_row(
                        pdf_view,
                        pdf_section,
                        effective_source_status,
                        daily_signal_date,
                        daily_volume_count,
                        approval,
                        generated_at,
                        operation_asof_date,
                    )
                )

    out = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    out["_view_order"] = out["pdf_view"].map({"highlight": 0, "full": 1}).fillna(9)
    out["_section_order"] = out["pdf_section"].map(
        {"confirmed_operation": 0, "pending_confirmation": 1, "active_operation": 2}
    ).fillna(9)
    out["_row_type_order"] = out["row_type"].map({"data": 0, "empty_state": 1}).fillna(9)
    out["_display_order_num"] = pd.to_numeric(out["display_order"], errors="coerce").fillna(999999)
    out = out.sort_values(["_view_order", "_section_order", "_row_type_order", "_display_order_num", "stock_id"])
    return out.drop(columns=["_view_order", "_section_order", "_row_type_order", "_display_order_num"]).reset_index(drop=True)


def write_outputs(df: pd.DataFrame, source_rows: int, source_status: str) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")

    lines = [
        "# Daily Volume Breakout Operation Section",
        "",
        f"- generated_at: `{safe_str(df['generated_at'].iloc[0]) if not df.empty else now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        f"- source: `{ADAPTER_SOURCE}`",
        f"- approval_source: `{safe_str(df['approval_source'].iloc[0]) if not df.empty else APPROVAL_SOURCE}`",
        f"- approved_for_daily: `{safe_str(df['approved_for_daily'].iloc[0]) if not df.empty else 'False'}`",
        f"- approval_version: `{safe_str(df['approval_version'].iloc[0]) if not df.empty else ''}`",
        f"- source_status: `{source_status}`",
        f"- source_rows: `{source_rows}`",
        "- purpose: production presentation adapter only; PDF/packet 必須讀取本 artifact，且不得重新計算進場、停損、出場或排名。",
        "- sections: confirmed_operation, pending_confirmation, active_operation.",
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


def build() -> pd.DataFrame:
    source = read_csv(SOURCE_PREVIEW_CSV)
    signals = read_csv(DAILY_SIGNALS_CSV)
    approval = read_csv(APPROVAL_CSV)
    source_status = "ready" if not source.empty else "missing_or_empty_research_source"
    report_date = main_price_date()
    daily_signal_date, daily_volume_count = daily_signal_context(signals, report_date)
    return normalize_source_rows(
        source,
        source_status,
        daily_signal_date,
        daily_volume_count,
        approval_context(approval),
        now_text(),
        signals,
    )


def main() -> int:
    source = read_csv(SOURCE_PREVIEW_CSV)
    source_status = "ready" if not source.empty else "missing_or_empty_research_source"
    out = build()
    write_outputs(out, len(source), source_status)
    print(f"Saved: {OUT_CSV} rows={len(out)}")
    print(f"Saved: {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
