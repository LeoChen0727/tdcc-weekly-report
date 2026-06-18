from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

SECTION_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
SECTION_MD = LATEST_DIR / "daily_volume_breakout_operation_section_latest.md"
EVIDENCE_AUDIT_CSV = LATEST_DIR / "daily_volume_breakout_operation_evidence_audit_latest.csv"
EVIDENCE_AUDIT_MD = LATEST_DIR / "daily_volume_breakout_operation_evidence_audit_latest.md"
TAXONOMY_CSV = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DAILY_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
FORMAL_SUMMARY_CSV = LATEST_DIR / "volume_breakout_formal_operation_backtest_latest.csv"
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

MODEL_ID = "volume_range_breakout"
LIFECYCLE_ADAPTER_SOURCE = "daily_candidate_model_signal_log+daily_published_model_snapshots+stock_price_history"
PDF_VIEWS = {"highlight", "full"}
PDF_SECTIONS = {
    "confirmed_operation",
    "confirmed_unranked_operation",
    "pending_confirmation",
    "active_operation",
}
HIGHLIGHT_HIDDEN_SECTIONS = {"confirmed_unranked_operation", "pending_confirmation"}
ROW_TYPES = {"data", "empty_state"}
SOURCE_STATUSES = {"ready"}
LINEAGE_LOOKBACK_CALENDAR_DAYS = 45

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
    "operation_status_zh",
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
    "median_return_zh",
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

    latest_volume = latest[latest["model_id"].astype(str).str.strip().eq(MODEL_ID)].copy()
    if latest_volume.empty:
        return
    if not MODEL_SIGNAL_LOG_CSV.exists():
        fail(f"missing formal model signal log: {MODEL_SIGNAL_LOG_CSV.relative_to(ROOT).as_posix()}")
    log = read_csv(MODEL_SIGNAL_LOG_CSV)
    missing_cols = sorted({"signal_date", "report_bucket", "stock_id", "model_id"} - set(log.columns))
    if missing_cols:
        fail(f"formal model signal log missing columns: {missing_cols}")
    log_volume = log[
        log["model_id"].astype(str).str.strip().eq(MODEL_ID)
        & log["signal_date"].map(normalize_date_text).eq(report_date)
    ].copy()

    def keyset(frame: pd.DataFrame) -> set[tuple[str, str, str, str]]:
        return {
            (
                normalize_date_text(row.get("signal_date")),
                str(row.get("report_bucket", "")).strip(),
                stock_id_text(row.get("stock_id")),
                str(row.get("model_id", "")).strip(),
            )
            for _, row in frame.iterrows()
        }

    latest_keys = keyset(latest_volume)
    log_keys = keyset(log_volume)
    missing = sorted(latest_keys - log_keys)
    extra = sorted(log_keys - latest_keys)
    if missing or extra:
        details: list[str] = []
        if missing:
            details.append("missing_from_signal_log=" + ", ".join(f"{date}/{bucket}/{stock}" for date, bucket, stock, _ in missing[:20]))
        if extra:
            details.append("extra_in_signal_log=" + ", ".join(f"{date}/{bucket}/{stock}" for date, bucket, stock, _ in extra[:20]))
        fail("latest volume_range_breakout signals and daily model signal log are out of sync: " + " | ".join(details))


def validate_selected_volume_breakout_model_lineage(section: pd.DataFrame) -> None:
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


def evidence_passes_buy_gate(evidence: pd.Series) -> bool:
    return (
        pd.to_numeric(pd.Series([evidence.get("sample_size", "")]), errors="coerce").iloc[0] >= 10
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
    if target.empty:
        return

    for _, row in target.iterrows():
        if str(row.get("evidence_match_status", "")).strip() != "positive_row_evidence":
            fail("confirmed/active rows must carry positive_row_evidence")
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
    included = audit[audit["included_in_daily_adapter"].astype(str).eq("True")].copy()
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

    bad_models = sorted(set(section["model_id"].astype(str)) - {MODEL_ID})
    if bad_models:
        fail(f"daily volume breakout operation section must not include other models: {bad_models}")

    bad_views = sorted(set(section["pdf_view"].astype(str)) - PDF_VIEWS)
    if bad_views:
        fail(f"invalid pdf_view values: {bad_views}")

    bad_sections = sorted(set(section["pdf_section"].astype(str)) - PDF_SECTIONS)
    if bad_sections:
        fail(f"invalid pdf_section values: {bad_sections}")
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
    if not eligible_triggers:
        fail("formal operation summary has no trigger passing the daily operation evidence gate")

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
        if not pending_data["entry_price_status_zh"].astype(str).str.contains("尚未確認").all():
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
        bad_quality = sorted(set(confirmed_data["quality_status_zh"].astype(str)) - {"正向證據"})
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
        bad_selected_trigger = sorted(set(confirmed_data["selected_trigger_id"].astype(str)) - eligible_triggers)
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
    if section["row_type"].astype(str).eq("empty_state").any() and "目前無資料" not in display_text:
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
        "VOLUME_OPERATION_HIGHLIGHT_LIMITS",
        '"confirmed_operation": 10',
        '"active_operation": 5',
        "confirmed_unranked_operation",
        "confirmed_not_buy_ranked",
        "build_volume_unranked_operation_table",
        "limit_volume_operation_rows_for_pdf_view",
        "VOLUME_TRIGGER_LABELS",
        "entry_date",
        "entry_price",
        "selected_trigger_id",
        "stop_loss_price",
        "final_rank_score",
    ]:
        if token not in source:
            fail(f"PDF generator must enforce structured volume operation rendering: {token}")
    forbidden = [
        "volume_breakout_operation_pdf_preview_latest.csv",
        "volume_breakout_confirmed_operation_rank_latest.csv",
        "volume_breakout_pending_operation_queue_latest.csv",
        "historical_pattern_operation_registry_latest.csv",
        "approved_operation_patterns_latest.csv",
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
        },
    )
    section = read_csv(SECTION_CSV)
    audit = read_csv(EVIDENCE_AUDIT_CSV)
    validate_shape(section, formal_summary, audit)
    validate_latest_signal_log_sync(section)
    validate_selected_volume_breakout_model_lineage(section)
    validate_display_text(section)
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
