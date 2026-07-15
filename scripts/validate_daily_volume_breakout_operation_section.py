from __future__ import annotations

from pathlib import Path

import pandas as pd

from validate_daily_operation_adapter_protected_fields import validate_adapter_frame


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
MODEL_SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"

SECTION_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
SECTION_MD = LATEST_DIR / "daily_volume_breakout_operation_section_latest.md"
EVIDENCE_AUDIT_CSV = LATEST_DIR / "daily_volume_breakout_operation_evidence_audit_latest.csv"
EVIDENCE_AUDIT_MD = LATEST_DIR / "daily_volume_breakout_operation_evidence_audit_latest.md"
TAXONOMY_CSV = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DAILY_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
APPROVED_FORMAL_SUMMARY_CSV = (
    ROOT
    / "config"
    / "approved_operation_evidence"
    / "volume_breakout_operation_v1_20260615_formal_operation_backtest.csv"
)
FORMAL_SUMMARY_CSV = APPROVED_FORMAL_SUMMARY_CSV
MODEL_SIGNAL_LOG_CSV = ROOT / "output" / "history" / "daily_candidate_models" / "daily_candidate_model_signal_log.csv"
DAILY_THEME_STATUS_HISTORY_CSVS = [
    ROOT / "output" / "history" / "daily_signals" / "daily_theme_status_history.csv",
    ROOT / "output" / "history" / "daily_candidates" / "daily_theme_status_history.csv",
]
DOCS_SECTION_CSV = DOCS_LATEST_DIR / SECTION_CSV.name
DOCS_SECTION_MD = DOCS_LATEST_DIR / SECTION_MD.name
DOCS_EVIDENCE_AUDIT_CSV = DOCS_LATEST_DIR / EVIDENCE_AUDIT_CSV.name
DOCS_EVIDENCE_AUDIT_MD = DOCS_LATEST_DIR / EVIDENCE_AUDIT_MD.name
PDF_GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
CONTRACT_MD = ROOT / "docs" / "specs" / "daily_volume_breakout_operation_section_contract.md"

LEGACY_MODEL_ID = "volume_range_breakout"
V2_LOW_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
V2_MID_MODEL_ID = "volume_range_breakout_v2_mid_position_momentum_attack"
V2_HIGH_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"
FORMAL_MODEL_IDS = {V2_LOW_MODEL_ID, V2_MID_MODEL_ID, V2_HIGH_MODEL_ID}
LIFECYCLE_ADAPTER_SOURCE = "daily_candidate_model_signal_log+daily_published_model_snapshots+stock_price_history"
REPORT_READY_BUCKETS = {"mainstream", "non_mainstream"}
PDF_VIEWS = {"highlight", "full"}
PDF_SECTIONS = {
    "confirmed_operation",
    "confirmed_unranked_operation",
    "pending_confirmation",
    "active_operation",
}
EXPECTED_OPERATION_STATUS = {
    "confirmed_operation": "confirmed_operation",
    "confirmed_unranked_operation": "confirmed_unranked_operation",
    "pending_confirmation": "pending_confirmation",
    "active_operation": "active_operation",
}
HIGHLIGHT_HIDDEN_SECTIONS = {"confirmed_unranked_operation", "pending_confirmation"}
ROW_TYPES = {"data", "empty_state"}
SOURCE_STATUSES = {"ready"}
CONFIRMED_QUALITY_STATUS_ZH = "正向證據"
LINEAGE_LOOKBACK_CALENDAR_DAYS = 45
AUDIT_STATUSES = {
    "candidate_evaluated",
    "positive_row_evidence",
    "positive_model_contract_evidence",
    "source_gap",
    "lifecycle_suppressed",
}
SOURCE_GAP_REASONS = {
    "missing_signal_identity",
    "missing_stock_price_history_file",
    "unusable_stock_price_history",
    "signal_date_missing_in_stock_price_history",
    "operation_asof_date_missing_in_stock_price_history",
    "signal_date_after_operation_asof_date",
    "signal_low_missing_in_stock_price_history",
}
LIFECYCLE_SUPPRESSION_STATES = PDF_SECTIONS | {"active_operation_suppressed"}
LIFECYCLE_SUPPRESSION_REASON_PREFIXES = (
    "same_stock_lifecycle_suppressed_by_",
    "confirmation_snapshot_",
    "missing_confirmation_",
    "empty_confirmation_",
)

REQUIRED_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "operation_asof_date",
    "operation_source_date_status",
    "display_order",
    "stock_id",
    "stock_display",
    "operation_status",
    "operation_status_zh",
    "quality_status_zh",
    "entry_basis_zh",
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
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "signal_date",
    "confirmation_date",
    "sample_size",
    "win_rate_zh",
    "neutral_rate_zh",
    "loss_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "median_return_zh",
    "pdf_bonus_combo_id",
    "pdf_bonus_combo_label_zh",
    "pdf_bonus_combo_sample_size",
    "pdf_bonus_combo_win_rate_zh",
    "pdf_bonus_combo_neutral_rate_zh",
    "pdf_bonus_combo_loss_rate_zh",
    "pdf_bonus_combo_failure_rate_zh",
    "pdf_bonus_combo_avg_return_zh",
    "pdf_bonus_combo_median_return_zh",
    "pdf_bonus_combo_source",
    "evidence_match_status",
    "evidence_tdcc_list_type",
    "evidence_rank_bucket",
    "evidence_confluence_scope",
    "evidence_confluence_id",
    "evidence_key",
    "evidence_out_of_sample_pass",
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
}

REQUIRED_AUDIT_COLUMNS = {
    "model_id",
    "operation_asof_date",
    "stock_id",
    "signal_date",
    "selected_trigger_id",
    "selected_confirmation_date",
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
    "evidence_avg_return",
    "evidence_median_return",
    "evidence_out_of_sample_pass",
    "ranking_research_score",
    "reason",
    "generated_at",
}

DISPLAY_COLUMNS = [
    "pdf_section_zh",
    "stock_display",
    "operation_status_zh",
    "quality_status_zh",
    "trigger_zh",
    "entry_basis_zh",
    "entry_price_status_zh",
    "stop_basis_zh",
    "exit_rule_zh",
    "pending_age_zh",
    "pending_group_zh",
    "pending_confirmation_zh",
    "tdcc_status_zh",
    "win_rate_zh",
    "avg_return_zh",
    "median_return_zh",
    "pdf_bonus_combo_id",
    "pdf_bonus_combo_win_rate_zh",
    "pdf_bonus_combo_loss_rate_zh",
    "pdf_bonus_combo_avg_return_zh",
    "pdf_bonus_combo_median_return_zh",
    "approved_for_daily",
    "operation_module_approved_for_daily",
    "approval_status",
    "approval_version",
    "operation_directive_level",
    "row_action_status",
    "buy_rank_eligible",
    "confidence_zh",
    "pdf_note_zh",
    "adapter_note_zh",
]

FORBIDDEN_DISPLAY_TOKENS = [
    "signal_low",
    "next_open",
    "pullback_5ma_confirmed",
    "pullback_10ma_confirmed",
    "next_day_continuation_confirmed",
    "operation research source date",
    "PDF renders an empty section",
    "stale rows",
    "PDF 不重新計算",
    "must render only this model section",
    "must not recalculate operation rules",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def stock_id_text(value: object) -> str:
    text = str(value).strip().replace(".0", "")
    return text.zfill(4) if text.isdigit() else text


def normalize_date_text(value: object) -> str:
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    text = text.replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""


def normalize_report_bucket(value: object) -> str:
    return str(value).strip().replace("-", "_")


def pct_display(value: object) -> str:
    num = pd.to_numeric(pd.Series([str(value).replace("%", "").replace("+", "").replace(",", "")]), errors="coerce").iloc[0]
    if pd.isna(num):
        return ""
    return f"{float(num):.2f}%"


def split_memberships(value: object) -> set[str]:
    tokens = str(value).replace(";", "|").replace(",", "|").split("|")
    return {token.strip() for token in tokens if token.strip()}


def require_nonempty_csv(path: Path, required_columns: set[str]) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required source artifact: {path.relative_to(ROOT).as_posix()}")
    df = read_csv(path)
    if df.empty:
        fail(f"required source artifact is empty: {path.relative_to(ROOT).as_posix()}")
    missing = sorted(required_columns - set(df.columns))
    if missing:
        fail(f"{path.relative_to(ROOT).as_posix()} missing columns: {missing}")
    return df


def selected_volume_breakout_history(report_date: str) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for path in DAILY_THEME_STATUS_HISTORY_CSVS:
        if path.exists():
            frames.append(read_csv(path))
    if not frames:
        fail("missing selected volume breakout history sources")
    selected = pd.concat(frames, ignore_index=True, sort=False)
    for col in ["signal_date", "stock_id", "volume_breakout_type", "selection_status"]:
        if col not in selected.columns:
            selected[col] = ""
    selected["signal_date"] = selected["signal_date"].map(normalize_date_text)
    selected["stock_id"] = selected["stock_id"].map(stock_id_text)
    selected = selected[
        selected["signal_date"].astype(str).str.len().eq(8)
        & selected["stock_id"].astype(str).ne("")
        & selected["volume_breakout_type"].astype(str).str.strip().eq("bottom_volume_attack")
        & selected["selection_status"].astype(str).str.strip().eq("selected")
    ].copy()
    if selected.empty:
        return selected
    report_date = normalize_date_text(report_date)
    if report_date:
        cutoff = (
            pd.to_datetime(report_date, format="%Y%m%d") - pd.Timedelta(days=LINEAGE_LOOKBACK_CALENDAR_DAYS)
        ).strftime("%Y%m%d")
        selected = selected[
            selected["signal_date"].astype(str).ge(cutoff)
            & selected["signal_date"].astype(str).le(report_date)
        ].copy()
    return selected.drop_duplicates(["signal_date", "stock_id"], keep="last")


def report_date_from_section(section: pd.DataFrame) -> str:
    dates = sorted(
        {
            normalize_date_text(value)
            for value in section.get("daily_signal_date", pd.Series(dtype=str)).tolist()
            if normalize_date_text(value)
        }
    )
    if len(dates) != 1:
        fail(f"operation section must carry exactly one daily_signal_date, observed={dates}")
    return dates[0]


def validate_latest_signal_log_sync(section: pd.DataFrame) -> None:
    report_date = report_date_from_section(section)
    freshness = require_nonempty_csv(DATA_FRESHNESS_CSV, {"main_price_date", "report_ready", "warrant_ready", "daily_pdf_ready"})
    main_date = normalize_date_text(freshness.iloc[0].get("main_price_date"))
    if main_date != report_date:
        fail(f"operation daily_signal_date must match data freshness main_price_date: section={report_date} freshness={main_date}")

    latest = require_nonempty_csv(DAILY_SIGNALS_CSV, {"signal_date", "report_bucket", "stock_id", "model_id"})
    latest_dates = {
        normalize_date_text(value)
        for value in latest["signal_date"].tolist()
        if normalize_date_text(value)
    }
    if latest_dates != {report_date}:
        fail(f"latest daily model signals must contain exactly main_price_date={report_date}, observed={sorted(latest_dates)}")

    latest_volume = latest[latest["model_id"].astype(str).str.strip().isin(FORMAL_MODEL_IDS)].copy()
    if latest_volume.empty:
        return
    if not MODEL_SIGNAL_LOG_CSV.exists():
        fail(f"missing formal model signal log: {MODEL_SIGNAL_LOG_CSV.relative_to(ROOT).as_posix()}")
    log = read_csv(MODEL_SIGNAL_LOG_CSV)
    missing_cols = sorted({"signal_date", "report_bucket", "stock_id", "model_id"} - set(log.columns))
    if missing_cols:
        fail(f"formal model signal log missing columns: {missing_cols}")
    log_volume = log[
        log["model_id"].astype(str).str.strip().isin(FORMAL_MODEL_IDS)
        & log["signal_date"].map(normalize_date_text).eq(report_date)
    ].copy()
    report_ready_log_volume = log_volume[
        log_volume["report_bucket"].map(normalize_report_bucket).isin(REPORT_READY_BUCKETS)
    ].copy()

    def keyset(frame: pd.DataFrame) -> set[tuple[str, str, str, str]]:
        return {
            (
                normalize_date_text(row.get("signal_date")),
                normalize_report_bucket(row.get("report_bucket", "")),
                stock_id_text(row.get("stock_id")),
                str(row.get("model_id", "")).strip(),
            )
            for _, row in frame.iterrows()
        }

    latest_keys = keyset(latest_volume)
    log_keys = keyset(report_ready_log_volume)
    missing = sorted(latest_keys - log_keys)
    extra = sorted(log_keys - latest_keys)
    if missing or extra:
        details: list[str] = []
        if missing:
            details.append("missing_from_signal_log=" + ", ".join(f"{date}/{bucket}/{stock}" for date, bucket, stock, _ in missing[:20]))
        if extra:
            details.append("extra_in_signal_log=" + ", ".join(f"{date}/{bucket}/{stock}" for date, bucket, stock, _ in extra[:20]))
        fail("latest volume_range_breakout signals and daily model signal log are out of sync: " + " | ".join(details))

    latest_stocks = {
        stock_id_text(value)
        for value in latest_volume["stock_id"].tolist()
        if stock_id_text(value)
    }
    data_stocks = {
        stock_id_text(value)
        for value in section.loc[section["row_type"].astype(str).eq("data"), "stock_id"].tolist()
        if stock_id_text(value)
    }
    missing_stocks = sorted(latest_stocks - data_stocks)
    if missing_stocks:
        fail(f"latest volume_range_breakout stocks missing from operation section: {missing_stocks}")

    observed_counts = {
        str(value).strip()
        for value in section["daily_volume_model_signal_count"].tolist()
        if str(value).strip()
    }
    if observed_counts != {str(len(latest_stocks))}:
        fail(
            "daily_volume_model_signal_count must match latest volume_range_breakout stock count: "
            f"observed={sorted(observed_counts)} expected={len(latest_stocks)}"
        )


def validate_selected_volume_breakout_model_lineage(section: pd.DataFrame) -> None:
    # Legacy bottom_volume_attack selected-row lineage belonged to v1. The v2
    # formal adapter is backed by daily_candidate_model_signal_log rows whose
    # model_id is one of FORMAL_MODEL_IDS, validated in validate_latest_signal_log_sync().
    return
    report_date = report_date_from_section(section)
    selected = selected_volume_breakout_history(report_date)
    if selected.empty:
        return
    if not MODEL_SIGNAL_LOG_CSV.exists():
        fail(f"missing formal model signal log: {MODEL_SIGNAL_LOG_CSV.relative_to(ROOT).as_posix()}")
    model_log = read_csv(MODEL_SIGNAL_LOG_CSV)
    for col in ["signal_date", "stock_id", "model_id"]:
        if col not in model_log.columns:
            fail(f"formal model signal log missing column: {col}")
    formal = model_log[model_log["model_id"].astype(str).str.strip().eq(MODEL_ID)].copy()
    formal_keys = {
        (normalize_date_text(row.get("signal_date")), stock_id_text(row.get("stock_id")))
        for _, row in formal.iterrows()
    }
    missing = sorted(
        {
            (normalize_date_text(row.get("signal_date")), stock_id_text(row.get("stock_id")))
            for _, row in selected.iterrows()
        }
        - formal_keys
    )
    if missing:
        sample = ", ".join(f"{date}/{stock}" for date, stock in missing[:20])
        fail(
            "selected bottom_volume_attack rows missing formal volume_range_breakout model log lineage: "
            f"{sample}"
        )


def eligible_formal_triggers(formal_summary: pd.DataFrame) -> set[str]:
    if "metric_sample_scope" not in formal_summary.columns:
        fail("formal operation summary must expose metric_sample_scope")
    if set(formal_summary["metric_sample_scope"].astype(str)) != {"mature_selected_operation_only"}:
        fail("formal operation summary must be mature_selected_operation_only")
    out = formal_summary.copy()
    for col in ["sample_size", "win_rate", "median_return", "ranking_research_score"]:
        out[f"_{col}"] = pd.to_numeric(out[col], errors="coerce")
    oos = out["out_of_sample_pass"].astype(str).str.lower().isin({"true", "1", "1.0"})
    eligible = out[
        out["_sample_size"].ge(10)
        & out["_win_rate"].ge(50)
        & out["_median_return"].gt(0)
        & out["_ranking_research_score"].gt(0)
        & oos
        & out.apply(evidence_is_formally_approved, axis=1)
    ].copy()
    return {str(value).strip() for value in eligible["trigger_id"].tolist() if str(value).strip()}


def formal_evidence_row(formal_summary: pd.DataFrame, row: pd.Series) -> pd.Series | None:
    part = formal_summary[
        formal_summary["tdcc_list_type"].astype(str).eq(str(row.get("evidence_tdcc_list_type", "")).strip())
        & formal_summary["rank_bucket"].astype(str).eq(str(row.get("evidence_rank_bucket", "")).strip())
        & formal_summary["trigger_id"].astype(str).eq(str(row.get("selected_trigger_id", "")).strip())
        & formal_summary["confluence_scope"].astype(str).eq(str(row.get("evidence_confluence_scope", "")).strip())
        & formal_summary["confluence_id"].astype(str).eq(str(row.get("evidence_confluence_id", "")).strip())
    ].copy()
    if part.empty:
        return None
    return part.iloc[0]


def evidence_is_formally_approved(evidence: pd.Series) -> bool:
    approved = str(evidence.get("approved_for_daily", "")).strip().lower() in {"true", "1", "1.0"}
    risk_notes = str(evidence.get("risk_notes_zh", "")).strip().lower()
    return approved and "research only" not in risk_notes


def evidence_passes_buy_gate(evidence: pd.Series) -> bool:
    return (
        evidence_is_formally_approved(evidence)
        and pd.to_numeric(pd.Series([evidence.get("sample_size", "")]), errors="coerce").iloc[0] >= 10
        and pd.to_numeric(pd.Series([evidence.get("win_rate", "")]), errors="coerce").iloc[0] >= 50
        and pd.to_numeric(pd.Series([evidence.get("median_return", "")]), errors="coerce").iloc[0] > 0
        and pd.to_numeric(pd.Series([evidence.get("ranking_research_score", "")]), errors="coerce").iloc[0] > 0
        and str(evidence.get("out_of_sample_pass", "")).lower() in {"true", "1", "1.0"}
    )


def validate_row_level_evidence(section: pd.DataFrame, formal_summary: pd.DataFrame, audit: pd.DataFrame) -> None:
    target = section[
        section["row_type"].astype(str).eq("data")
        & section["pdf_section"].astype(str).isin({"confirmed_operation", "active_operation"})
    ].copy()
    included = audit[audit["included_in_daily_adapter"].astype(str).eq("True")].copy()
    if target.empty:
        if not included.empty:
            fail("evidence audit must not mark included rows when confirmed/active adapter rows are empty")
        return

    for _, row in target.iterrows():
        match_status = str(row.get("evidence_match_status", "")).strip()
        model_id = str(row.get("model_id", "")).strip()
        if model_id in FORMAL_MODEL_IDS and match_status != "positive_model_contract_evidence":
            fail("v2 volume breakout confirmed/active rows must use positive_model_contract_evidence")
        if match_status not in {
            "positive_row_evidence",
            "positive_model_contract_evidence",
        }:
            fail("confirmed/active rows must carry positive model evidence")
        if match_status == "positive_model_contract_evidence":
            if str(row.get("evidence_confluence_scope", "")).strip() != "model_contract":
                fail("v2 model-contract evidence rows must carry evidence_confluence_scope=model_contract")
            if str(row.get("evidence_confluence_id", "")).strip() not in FORMAL_MODEL_IDS:
                fail("v2 model-contract evidence rows must carry its formal model_id as evidence_confluence_id")
            continue
        evidence = formal_evidence_row(formal_summary, row)
        if evidence is None:
            fail(
                "daily adapter row references evidence not found in formal summary: "
                f"stock_id={row.get('stock_id')} key={row.get('evidence_key')}"
            )
        checks = {
            "sample_size": str(evidence.get("sample_size", "")).strip(),
            "win_rate_zh": pct_display(evidence.get("win_rate", "")),
            "avg_return_zh": pct_display(evidence.get("avg_return", "")),
            "median_return_zh": pct_display(evidence.get("median_return", "")),
            "evidence_out_of_sample_pass": str(evidence.get("out_of_sample_pass", "")).strip(),
        }
        for col, expected in checks.items():
            observed = str(row.get(col, "")).strip()
            if observed != expected:
                fail(
                    "daily adapter row evidence metric mismatch: "
                    f"stock_id={row.get('stock_id')} col={col} observed={observed} expected={expected}"
                )
        if not evidence_passes_buy_gate(evidence):
            fail(f"daily adapter row uses evidence that does not pass daily gate: stock_id={row.get('stock_id')}")

    if audit.empty:
        fail("evidence audit must not be empty when confirmed/active rows exist")
    missing = sorted(REQUIRED_AUDIT_COLUMNS - set(audit.columns))
    if missing:
        fail(f"evidence audit missing columns: {missing}")
    if included.empty:
        fail("evidence audit must include positive rows used by the daily adapter")
    target_keys = {
        (
            stock_id_text(row.get("stock_id")),
            normalize_date_text(row.get("signal_date")),
            str(row.get("selected_trigger_id", "")).strip(),
            str(row.get("evidence_tdcc_list_type", "")).strip(),
            str(row.get("evidence_rank_bucket", "")).strip(),
            str(row.get("evidence_confluence_scope", "")).strip(),
            str(row.get("evidence_confluence_id", "")).strip(),
        )
        for _, row in target.iterrows()
    }
    audit_keys = {
        (
            stock_id_text(row.get("stock_id")),
            normalize_date_text(row.get("signal_date")),
            str(row.get("selected_trigger_id", "")).strip(),
            str(row.get("tdcc_list_type", "")).strip(),
            str(row.get("rank_bucket", "")).strip(),
            str(row.get("evidence_confluence_scope", "")).strip(),
            str(row.get("evidence_confluence_id", "")).strip(),
        )
        for _, row in included.iterrows()
    }
    missing_audit = sorted(target_keys - audit_keys)
    if missing_audit:
        fail(f"daily adapter rows missing matching positive evidence audit rows: {missing_audit}")
    extra_included = sorted(audit_keys - target_keys)
    if extra_included:
        fail(f"evidence audit marks non-rendered rows as included_in_daily_adapter=True: {extra_included[:20]}")


def validate_high_position_bonus_metrics(section: pd.DataFrame) -> None:
    high_data = section[
        section["model_id"].astype(str).eq(V2_HIGH_MODEL_ID)
        & section["row_type"].astype(str).eq("data")
        & section["pdf_section"].astype(str).isin({"confirmed_operation", "active_operation"})
    ].copy()
    if high_data.empty:
        return
    baseline_expected = {
        "sample_size": "231",
        "win_rate_zh": "62.34%",
        "neutral_rate_zh": "0.00%",
        "loss_rate_zh": "37.66%",
        "failure_rate_zh": "37.66%",
        "avg_return_zh": "9.48%",
        "median_return_zh": "6.61%",
    }
    for col, expected in baseline_expected.items():
        bad = high_data[high_data[col].astype(str).str.strip().ne(expected)]
        if not bad.empty:
            fail(f"{V2_HIGH_MODEL_ID} data rows must retain baseline {col}={expected}")

    bonus = high_data[high_data["pdf_bonus_combo_id"].astype(str).str.strip().ne("")].copy()
    if bonus.empty:
        return
    required = [
        "pdf_bonus_combo_label_zh",
        "pdf_bonus_combo_sample_size",
        "pdf_bonus_combo_win_rate_zh",
        "pdf_bonus_combo_neutral_rate_zh",
        "pdf_bonus_combo_loss_rate_zh",
        "pdf_bonus_combo_failure_rate_zh",
        "pdf_bonus_combo_avg_return_zh",
        "pdf_bonus_combo_median_return_zh",
        "pdf_bonus_combo_source",
    ]
    for col in required:
        if bonus[col].astype(str).str.strip().eq("").any():
            fail(f"{V2_HIGH_MODEL_ID} bonus metric rows must populate {col}")
    bad_source = sorted(set(bonus["pdf_bonus_combo_source"].astype(str)) - {"single_bonus_metric", "exact_combo_metric"})
    if bad_source:
        fail(f"{V2_HIGH_MODEL_ID} bonus metric source must be single or exact combo: {bad_source}")
    for _, row in bonus.iterrows():
        bonus_win = pd.to_numeric(
            pd.Series([str(row.get("pdf_bonus_combo_win_rate_zh", "")).replace("%", "").replace("+", "")]),
            errors="coerce",
        ).iloc[0]
        bonus_avg = pd.to_numeric(
            pd.Series([str(row.get("pdf_bonus_combo_avg_return_zh", "")).replace("%", "").replace("+", "")]),
            errors="coerce",
        ).iloc[0]
        if pd.isna(bonus_win) or float(bonus_win) < 62.34:
            fail(f"{V2_HIGH_MODEL_ID} bonus metric must not display weaker win rate than baseline")
        if pd.isna(bonus_avg) or float(bonus_avg) <= 0:
            fail(f"{V2_HIGH_MODEL_ID} bonus metric must keep positive average return")


def validate_source_gap_audit(audit: pd.DataFrame) -> None:
    if audit.empty:
        return
    missing = sorted(REQUIRED_AUDIT_COLUMNS - set(audit.columns))
    if missing:
        fail(f"evidence audit missing columns: {missing}")
    bad_status = sorted(set(audit["audit_status"].astype(str)) - AUDIT_STATUSES)
    if bad_status:
        fail(f"evidence audit has unsupported audit_status values: {bad_status}")
    gaps = audit[audit["audit_status"].astype(str).eq("source_gap")].copy()
    if gaps.empty:
        return
    if gaps["included_in_daily_adapter"].astype(str).ne("False").any():
        fail("source_gap audit rows must never be included in the daily adapter")
    if gaps["operation_lifecycle_state"].astype(str).ne("source_gap").any():
        fail("source_gap audit rows must carry operation_lifecycle_state=source_gap")
    bad_reasons = sorted(set(gaps["reason"].astype(str)) - SOURCE_GAP_REASONS)
    if bad_reasons:
        fail(f"source_gap audit rows have unsupported reasons: {bad_reasons}")
    identity_required = gaps[~gaps["reason"].astype(str).eq("missing_signal_identity")].copy()
    missing_identity = identity_required[
        identity_required["stock_id"].astype(str).str.strip().eq("")
        | identity_required["signal_date"].astype(str).str.strip().eq("")
        | identity_required["operation_asof_date"].astype(str).str.strip().eq("")
    ]
    if not missing_identity.empty:
        fail("source_gap audit rows must preserve stock_id, signal_date, and operation_asof_date")


def validate_lifecycle_suppression_audit(audit: pd.DataFrame) -> None:
    if audit.empty:
        return
    suppressed = audit[audit["audit_status"].astype(str).eq("lifecycle_suppressed")].copy()
    if suppressed.empty:
        return
    if suppressed["included_in_daily_adapter"].astype(str).ne("False").any():
        fail("lifecycle_suppressed audit rows must never be included in the daily adapter")
    bad_states = sorted(set(suppressed["operation_lifecycle_state"].astype(str)) - LIFECYCLE_SUPPRESSION_STATES)
    if bad_states:
        fail(f"lifecycle_suppressed audit rows have invalid lifecycle states: {bad_states}")
    missing_identity = suppressed[
        suppressed["stock_id"].astype(str).str.strip().eq("")
        | suppressed["signal_date"].astype(str).str.strip().eq("")
        | suppressed["operation_asof_date"].astype(str).str.strip().eq("")
    ]
    if not missing_identity.empty:
        fail("lifecycle_suppressed audit rows must preserve stock_id, signal_date, and operation_asof_date")
    reason = suppressed["reason"].astype(str)
    allowed_reason = pd.Series(False, index=suppressed.index)
    for prefix in LIFECYCLE_SUPPRESSION_REASON_PREFIXES:
        allowed_reason = allowed_reason | reason.str.startswith(prefix)
    bad_reason = suppressed[~allowed_reason]
    if not bad_reason.empty:
        fail("lifecycle_suppressed audit rows must explain same-stock suppression or confirmation snapshot gating")


def published_section_snapshot_path(report_date: str) -> Path:
    return MODEL_SNAPSHOT_DIR / f"daily_volume_breakout_operation_section_{normalize_date_text(report_date)}.csv"


def matching_snapshot_rows(path: Path, row: pd.Series) -> pd.DataFrame:
    snapshot = read_csv(path).fillna("")
    stock_id = stock_id_text(row.get("stock_id"))
    signal_date = normalize_date_text(row.get("signal_date"))
    confirmation_date = normalize_date_text(row.get("selected_confirmation_date"))
    matches = snapshot[
        snapshot.get("stock_id", pd.Series(dtype=str)).map(stock_id_text).eq(stock_id)
        & snapshot.get("signal_date", pd.Series(dtype=str)).map(normalize_date_text).eq(signal_date)
        & snapshot.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
    ].copy()
    if "selected_confirmation_date" in matches.columns:
        matches = matches[
            matches["selected_confirmation_date"].map(normalize_date_text).eq(confirmation_date)
        ].copy()
    return matches


def active_backed_by_confirmation_snapshot(row: pd.Series) -> bool:
    confirmation_date = normalize_date_text(row.get("selected_confirmation_date"))
    path = published_section_snapshot_path(confirmation_date)
    if not path.exists():
        return False
    matches = matching_snapshot_rows(path, row)
    buy_ranked = matches[
        matches.get("pdf_section", pd.Series(dtype=str)).astype(str).eq("confirmed_operation")
        & matches.get("row_action_status", pd.Series(dtype=str)).astype(str).eq("confirmed_buy_candidate")
        & matches.get("buy_rank_eligible", pd.Series(dtype=str)).astype(str).eq("True")
    ]
    return not buy_ranked.empty


def validate_active_confirmation_snapshot_gate(active_data: pd.DataFrame) -> None:
    for _, row in active_data.iterrows():
        if active_backed_by_confirmation_snapshot(row):
            continue
        fail(
            "active_operation row is not backed by a confirmation-date buy-ranked row: "
            f"stock_id={stock_id_text(row.get('stock_id'))} "
            f"signal_date={normalize_date_text(row.get('signal_date'))} "
            f"confirmation_date={normalize_date_text(row.get('selected_confirmation_date'))}"
        )


def validate_file_presence() -> None:
    for path in [
        SECTION_CSV,
        SECTION_MD,
        EVIDENCE_AUDIT_CSV,
        EVIDENCE_AUDIT_MD,
        DOCS_SECTION_CSV,
        DOCS_SECTION_MD,
        DOCS_EVIDENCE_AUDIT_CSV,
        DOCS_EVIDENCE_AUDIT_MD,
        CONTRACT_MD,
        FORMAL_SUMMARY_CSV,
    ]:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT).as_posix()}")


def validate_shape(section: pd.DataFrame, formal_summary: pd.DataFrame, audit: pd.DataFrame) -> None:
    if section.empty:
        fail(f"{SECTION_CSV.relative_to(ROOT).as_posix()} has no rows")
    missing = sorted(REQUIRED_COLUMNS - set(section.columns))
    if missing:
        fail(f"daily volume breakout operation section missing columns: {missing}")

    models = set(section["model_id"].astype(str))
    if LEGACY_MODEL_ID in models:
        fail(f"legacy {LEGACY_MODEL_ID} must not appear in v2 operation section")
    bad_models = sorted(models - FORMAL_MODEL_IDS)
    if bad_models:
        fail(f"daily volume breakout operation section must not include other models: {bad_models}")

    bad_views = sorted(set(section["pdf_view"].astype(str)) - PDF_VIEWS)
    if bad_views:
        fail(f"invalid pdf_view values: {bad_views}")

    bad_sections = sorted(set(section["pdf_section"].astype(str)) - PDF_SECTIONS)
    if bad_sections:
        fail(f"invalid pdf_section values: {bad_sections}")
    bad_operation_status = section[
        section.apply(
            lambda row: str(row.get("operation_status", "")).strip()
            != EXPECTED_OPERATION_STATUS.get(str(row.get("pdf_section", "")).strip(), ""),
            axis=1,
        )
    ]
    if not bad_operation_status.empty:
        fail("operation_status must be a machine-readable mirror of pdf_section")
    hidden_highlight = section[
        section["pdf_view"].astype(str).eq("highlight")
        & section["pdf_section"].astype(str).isin(HIGHLIGHT_HIDDEN_SECTIONS)
    ]
    if not hidden_highlight.empty:
        fail("highlight PDF adapter rows must not include pending or unranked confirmation sections")

    bad_row_types = sorted(set(section["row_type"].astype(str)) - ROW_TYPES)
    if bad_row_types:
        fail(f"invalid row_type values: {bad_row_types}")

    bad_status = sorted(set(section["adapter_source_status"].astype(str)) - SOURCE_STATUSES)
    if bad_status:
        fail(f"invalid adapter_source_status values: {bad_status}")
    bad_date_status = sorted(set(section["operation_source_date_status"].astype(str)) - SOURCE_STATUSES)
    if bad_date_status:
        fail(f"invalid operation_source_date_status values: {bad_date_status}")

    if set(section["approved_for_daily"].astype(str)) != {"True"}:
        fail("daily volume breakout operation section must be approved_for_daily=True")
    if set(section["operation_module_approved_for_daily"].astype(str)) != {"True"}:
        fail("daily volume breakout operation section must carry operation_module_approved_for_daily=True")
    if set(section["approval_status"].astype(str)) != {"approved_for_daily_v1"}:
        fail("daily volume breakout operation section must carry approval_status=approved_for_daily_v1")
    if set(section["operation_directive_level"].astype(str)) != {"approved_daily_operation_guidance"}:
        fail("daily volume breakout operation section must carry approved daily operation guidance")
    if section["operation_module_id"].astype(str).str.strip().eq("").any():
        fail("daily volume breakout operation section must carry operation_module_id")
    if section["approval_version"].astype(str).str.strip().eq("").any():
        fail("daily volume breakout operation section must carry approval_version")
    if set(section["adapter_source"].astype(str)) != {LIFECYCLE_ADAPTER_SOURCE}:
        fail("daily volume breakout operation section must use the lifecycle adapter source only")
    eligible_triggers = eligible_formal_triggers(formal_summary)

    confirmed_data = section[
        section["pdf_section"].eq("confirmed_operation") & section["row_type"].eq("data")
    ].copy()
    data_rows = section[section["row_type"].eq("data")].copy()
    if not data_rows.empty:
        bad_dates = data_rows[
            data_rows["operation_asof_date"].astype(str).ne(data_rows["daily_signal_date"].astype(str))
        ]
        if not bad_dates.empty:
            fail("operation data rows must have operation_asof_date equal to daily_signal_date")
        duplicated_stock_rows = data_rows[
            data_rows.duplicated(["pdf_view", "stock_id"], keep=False)
        ]
        if not duplicated_stock_rows.empty:
            fail("operation section must keep only one lifecycle row per stock in each pdf_view")
        bad_data_status = data_rows[data_rows["adapter_source_status"].astype(str).ne("ready")]
        if not bad_data_status.empty:
            fail("operation data rows are allowed only when adapter_source_status=ready")
        duplicate_rows = data_rows[
            data_rows.duplicated(["pdf_view", "pdf_section", "stock_id"], keep=False)
        ]
        if not duplicate_rows.empty:
            fail("operation data rows must be unique by pdf_view/pdf_section/stock_id")
    pending_data = section[
        section["pdf_section"].eq("pending_confirmation") & section["row_type"].eq("data")
    ].copy()
    if not pending_data.empty:
        if pending_data["row_action_status"].astype(str).ne("pending_confirmation").any():
            fail("pending_confirmation data rows must carry row_action_status=pending_confirmation")
        if pending_data["buy_rank_eligible"].astype(str).ne("False").any():
            fail("pending_confirmation data rows must keep buy_rank_eligible=False")
        if pending_data["selected_trigger_id"].astype(str).str.strip().ne("").any():
            fail("pending_confirmation data rows must not carry a selected trigger")
        if pending_data["confirmation_date"].astype(str).str.strip().ne("").any():
            fail("pending_confirmation data rows must not carry a confirmation date")
        if pending_data["entry_date"].astype(str).str.strip().ne("").any():
            fail("pending_confirmation data rows must not carry an entry date")
        if pending_data["entry_price"].astype(str).str.strip().ne("").any():
            fail("pending_confirmation data rows must not carry an entry price")
        pending_text = pending_data["entry_price_status_zh"].astype(str)
        if not (pending_text.str.contains("等待").all() or pending_text.str.contains("未列買入").all()):
            fail("pending_confirmation data rows must clearly state that entry price is not available")
    confirmed_ids = {
        stock_id_text(value)
        for value in confirmed_data["stock_id"].tolist()
        if stock_id_text(value)
    }
    active_data = section[
        section["pdf_section"].eq("active_operation") & section["row_type"].eq("data")
    ].copy()
    active_ids = {
        stock_id_text(value)
        for value in active_data["stock_id"].tolist()
        if stock_id_text(value)
    }
    if not data_rows.empty:
        taxonomy = read_csv(TAXONOMY_CSV)
        if taxonomy.empty or "stock_id" not in taxonomy.columns:
            fail("stock_theme_taxonomy_latest.csv is required to validate operation row report routing")
        taxonomy_ids = {stock_id_text(value) for value in taxonomy["stock_id"].tolist() if stock_id_text(value)}
        missing_taxonomy = sorted(
            set(data_rows["stock_id"].map(stock_id_text).tolist()) - taxonomy_ids
        )
        if missing_taxonomy:
            fail(f"operation data rows missing stock taxonomy/basic industry source: {missing_taxonomy}")
        if "report_line_memberships" not in taxonomy.columns:
            fail("stock taxonomy must include report_line_memberships")
        taxonomy_membership = {
            stock_id_text(row.get("stock_id")): split_memberships(row.get("report_line_memberships"))
            for _, row in taxonomy.iterrows()
        }
        unrouted = sorted(
            {
                stock_id
                for stock_id in data_rows["stock_id"].map(stock_id_text).tolist()
                if not taxonomy_membership.get(stock_id)
                or bool(taxonomy_membership.get(stock_id, set()) - {"mainstream", "non_mainstream"})
            }
        )
        if unrouted:
            fail(f"operation data rows have invalid stock taxonomy report routing: {unrouted}")
    if not confirmed_data.empty:
        bad_quality = sorted(
            set(confirmed_data["quality_status_zh"].astype(str)) - {CONFIRMED_QUALITY_STATUS_ZH}
        )
        if bad_quality:
            fail(f"confirmed operation rows must be positive evidence only: {bad_quality}")
        if set(confirmed_data["row_action_status"].astype(str)) != {"confirmed_buy_candidate"}:
            fail("confirmed operation data rows must carry row_action_status=confirmed_buy_candidate")
        if set(confirmed_data["buy_rank_eligible"].astype(str)) != {"True"}:
            fail("confirmed operation data rows must be buy_rank_eligible=True")
        missing_selected = confirmed_data[
            confirmed_data["selected_trigger_id"].astype(str).str.strip().eq("")
            | confirmed_data["selected_confirmation_date"].astype(str).str.strip().eq("")
        ]
        if not missing_selected.empty:
            fail("confirmed operation data rows must carry selected trigger metadata")
        row_evidence_confirmed = confirmed_data[
            confirmed_data["evidence_match_status"].astype(str).str.strip().eq("positive_row_evidence")
        ]
        bad_selected_trigger = sorted(set(row_evidence_confirmed["selected_trigger_id"].astype(str)) - eligible_triggers)
        if bad_selected_trigger:
            fail(f"confirmed operation rows use trigger without eligible formal evidence: {bad_selected_trigger}")
        bad_confirm_date = confirmed_data[
            confirmed_data["confirmation_date"].map(normalize_date_text).ne(
                confirmed_data["daily_signal_date"].map(normalize_date_text)
            )
        ]
        if not bad_confirm_date.empty:
            fail("confirmed operation rows must be confirmed on the report date")

    unranked_data = section[
        section["pdf_section"].eq("confirmed_unranked_operation") & section["row_type"].eq("data")
    ].copy()
    if not unranked_data.empty:
        if set(unranked_data["row_action_status"].astype(str)) != {"confirmed_not_buy_ranked"}:
            fail("confirmed_unranked_operation rows must carry row_action_status=confirmed_not_buy_ranked")
        if set(unranked_data["buy_rank_eligible"].astype(str)) != {"False"}:
            fail("confirmed_unranked_operation rows must keep buy_rank_eligible=False")
        missing_selected = unranked_data[
            unranked_data["selected_trigger_id"].astype(str).str.strip().eq("")
            | unranked_data["selected_confirmation_date"].astype(str).str.strip().eq("")
        ]
        if not missing_selected.empty:
            fail("confirmed_unranked_operation rows must carry selected trigger metadata")
        bad_confirm_date = unranked_data[
            unranked_data["confirmation_date"].map(normalize_date_text).ne(
                unranked_data["daily_signal_date"].map(normalize_date_text)
            )
        ]
        if not bad_confirm_date.empty:
            fail("confirmed_unranked_operation rows must be confirmed on the report date")
        blocked_operation_fields = [
            "entry_rule_id",
            "entry_price_basis",
            "entry_date",
            "entry_price",
            "stop_loss_rule_id",
            "stop_loss_price",
            "exit_rule_id",
        ]
        for col in blocked_operation_fields:
            if unranked_data[col].astype(str).str.strip().ne("").any():
                fail(f"confirmed_unranked_operation rows must not carry operation field: {col}")
        if unranked_data["evidence_match_status"].astype(str).str.strip().eq("positive_row_evidence").any():
            fail("confirmed_unranked_operation rows must not carry positive_row_evidence")
        for _, row in unranked_data.iterrows():
            match_status = str(row.get("evidence_match_status", "")).strip()
            if match_status == "no_matching_row_level_evidence":
                continue
            if match_status == "model_contract_evidence_not_buy_ranked":
                if str(row.get("evidence_confluence_scope", "")).strip() != "model_contract":
                    fail("v2 unranked model-contract evidence rows must carry evidence_confluence_scope=model_contract")
                if str(row.get("evidence_confluence_id", "")).strip() not in FORMAL_MODEL_IDS:
                    fail("v2 unranked model-contract evidence rows must carry its formal model_id as evidence_confluence_id")
                continue
            if match_status != "row_level_evidence_not_buy_ranked":
                fail(f"invalid confirmed_unranked_operation evidence status: {match_status}")
            evidence = formal_evidence_row(formal_summary, row)
            if evidence is None:
                fail(
                    "confirmed_unranked_operation row references evidence not found in formal summary: "
                    f"stock_id={row.get('stock_id')} key={row.get('evidence_key')}"
                )
            if evidence_passes_buy_gate(evidence):
                fail(
                    "confirmed_unranked_operation row references buy-eligible evidence: "
                    f"stock_id={row.get('stock_id')} key={row.get('evidence_key')}"
                )

    buy_eligible = section[section["buy_rank_eligible"].astype(str).eq("True")]
    bad_buy = buy_eligible[
        ~(
            buy_eligible["pdf_section"].eq("confirmed_operation")
            & buy_eligible["row_type"].eq("data")
            & buy_eligible["row_action_status"].eq("confirmed_buy_candidate")
        )
    ]
    if not bad_buy.empty:
        fail("buy_rank_eligible=True is allowed only on confirmed_operation data rows")

    pending = section[section["pdf_section"].eq("pending_confirmation") & section["row_type"].eq("data")]
    bad_pending = pending[
        pending["buy_rank_eligible"].astype(str).ne("False")
        | pending["row_action_status"].astype(str).ne("pending_confirmation")
    ]
    if not bad_pending.empty:
        fail("pending_confirmation rows must stay buy_rank_eligible=False with row_action_status=pending_confirmation")

    for view in PDF_VIEWS:
        for section_id in PDF_SECTIONS:
            if view == "highlight" and section_id in HIGHLIGHT_HIDDEN_SECTIONS:
                continue
            part = section[section["pdf_view"].eq(view) & section["pdf_section"].eq(section_id)]
            if part.empty:
                fail(f"missing {view}/{section_id} section row")

    active = section[section["pdf_section"].eq("active_operation")]
    if active.empty:
        fail("active_operation section is required even when empty")
    if active["buy_rank_eligible"].astype(str).ne("False").any():
        fail("active_operation rows must not be buy_rank_eligible")
    active_data = active[active["row_type"].astype(str).eq("data")].copy()
    if not active_data.empty:
        if set(active_data["row_action_status"].astype(str)) != {"active_operation"}:
            fail("active_operation data rows must carry row_action_status=active_operation")
        missing_active_selected = active_data[
            active_data["selected_trigger_id"].astype(str).str.strip().eq("")
            | active_data["selected_confirmation_date"].astype(str).str.strip().eq("")
        ]
        if not missing_active_selected.empty:
            fail("active_operation data rows must carry selected trigger metadata")
        bad_active_trigger = sorted(set(active_data["selected_trigger_id"].astype(str)) - eligible_triggers)
        if bad_active_trigger:
            fail(f"active_operation rows use trigger without eligible formal evidence: {bad_active_trigger}")
        bad_active_dates = active_data[
            active_data["selected_confirmation_date"].map(normalize_date_text).gt(
                active_data["daily_signal_date"].map(normalize_date_text)
            )
        ]
        if not bad_active_dates.empty:
            fail("active_operation confirmation date cannot be after the report date")
        validate_active_confirmation_snapshot_gate(active_data)
        missing_active_entry = active_data[
            active_data["entry_date"].astype(str).str.strip().eq("")
            | active_data["entry_price"].astype(str).str.strip().eq("")
        ]
        if not missing_active_entry.empty:
            fail("active_operation data rows must carry structured entry_date and entry_price")
    active_empty = active[active["row_type"].astype(str).eq("empty_state")]
    if not active_empty.empty and active_empty["row_action_status"].astype(str).ne("empty_state").any():
        fail("active_operation empty rows must carry row_action_status=empty_state")
    if not active["adapter_note_zh"].astype(str).str.contains("操作中|D0-D10|追蹤", regex=True).any():
        fail("active_operation rows must explain operation-in-progress status")


    validate_high_position_bonus_metrics(section)
    validate_row_level_evidence(section, formal_summary, audit)


def validate_display_text(section: pd.DataFrame) -> None:
    display_text = "\n".join(
        section[col].astype(str).str.cat(sep="\n") for col in DISPLAY_COLUMNS if col in section.columns
    )
    for token in FORBIDDEN_DISPLAY_TOKENS:
        if token in display_text:
            fail(f"forbidden raw display token leaked: {token}")
    if "median" in display_text.lower():
        fail("display text must use Chinese wording for median return, not raw 'median'")
    if section["row_type"].astype(str).eq("empty_state").any():
        for expected_empty_text in ["本日無股票推薦", "目前無操作中追蹤列"]:
            if expected_empty_text not in display_text:
                fail("empty-state display text must be present for PDF empty tables")


def validate_pdf_generator_boundary() -> None:
    if not PDF_GENERATOR.exists():
        return
    source = PDF_GENERATOR.read_text(encoding="utf-8", errors="replace")
    if "daily_volume_breakout_operation_section_latest.csv" not in source:
        fail("PDF generator must read the daily volume breakout operation adapter artifact")
    if "render_volume_range_breakout_operation_section" not in source:
        fail("PDF generator must expose an independent volume breakout operation renderer")
    for token in [
        "OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS = 10",
        "OPERATION_HIGHLIGHT_ROW_LIMITS",
        '"active_operation": OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS',
        "limit_operation_rows_for_pdf_view",
        "confirmed_unranked_operation",
        "confirmed_not_buy_ranked",
        "build_volume_unranked_operation_table",
        "VOLUME_TRIGGER_LABELS",
        "entry_date",
        "entry_price",
        "selected_trigger_id",
        "stop_loss_price",
        "final_rank_score",
    ]:
        if token not in source:
            fail(f"PDF generator must enforce structured volume operation rendering: {token}")
    for token in [
        "VOLUME_OPERATION_HIGHLIGHT_LIMITS",
        '"confirmed_operation": 10',
        '"active_operation": 5',
        '"active_operation": None',
    ]:
        if token in source:
            fail(f"PDF generator must not keep legacy highlight operation display caps: {token}")
    forbidden = [
        "volume_breakout_operation_pdf_preview_latest.csv",
        "volume_breakout_confirmed_operation_rank_latest.csv",
        "volume_breakout_pending_operation_queue_latest.csv",
        "historical_pattern_operation_registry_latest.csv",
    ]
    for token in forbidden:
        if token in source:
            fail(f"PDF generator must not read research artifact directly: {token}")


def validate_packet_builder_boundary() -> None:
    if not PACKET_BUILDER.exists():
        return
    source = PACKET_BUILDER.read_text(encoding="utf-8", errors="replace")
    if "daily_volume_breakout_operation_section_latest.csv" not in source:
        fail("packet builder must read the daily volume breakout operation adapter artifact")
    if "build_volume_operation_packet_lines" not in source:
        fail("packet builder must render the volume breakout operation adapter section")
    forbidden = [
        "volume_breakout_operation_pdf_preview_latest.csv",
        "volume_breakout_confirmed_operation_rank_latest.csv",
        "volume_breakout_pending_operation_queue_latest.csv",
        "historical_pattern_operation_registry_latest.csv",
        "approved_operation_patterns_latest.csv",
    ]
    for token in forbidden:
        if token in source:
            fail(f"packet builder must not read research artifact directly: {token}")


def validate_operation_artifacts(
    section: pd.DataFrame,
    formal_summary: pd.DataFrame,
    audit: pd.DataFrame,
) -> None:
    """Run the complete row-level contract shared by production and regression tests."""
    validate_shape(section, formal_summary, audit)
    validate_source_gap_audit(audit)
    validate_lifecycle_suppression_audit(audit)
    validate_display_text(section)
    for model_id in sorted(FORMAL_MODEL_IDS):
        protected_errors = validate_adapter_frame(section, model_id)
        if protected_errors:
            fail("; ".join(protected_errors))


def main() -> int:
    validate_file_presence()
    formal_summary = require_nonempty_csv(
        FORMAL_SUMMARY_CSV,
        {
            "model_id",
            "tdcc_list_type",
            "rank_bucket",
            "trigger_id",
            "confluence_scope",
            "confluence_id",
            "sample_size",
            "win_rate",
            "median_return",
            "ranking_research_score",
            "out_of_sample_pass",
            "metric_sample_scope",
            "approved_for_daily",
            "risk_notes_zh",
        },
    )
    section = read_csv(SECTION_CSV)
    audit = read_csv(EVIDENCE_AUDIT_CSV)
    validate_operation_artifacts(section, formal_summary, audit)
    validate_latest_signal_log_sync(section)
    validate_selected_volume_breakout_model_lineage(section)
    validate_pdf_generator_boundary()
    validate_packet_builder_boundary()
    print(
        "daily volume breakout operation section validation passed "
        f"rows={len(section)} "
        f"data_rows={(section['row_type'].astype(str) == 'data').sum()} "
        f"empty_rows={(section['row_type'].astype(str) == 'empty_state').sum()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
