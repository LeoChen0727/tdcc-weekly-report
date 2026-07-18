from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_published_snapshot_ranking_backtest import (  # noqa: E402
    DOCS_CSV,
    DOCS_MD,
    EVENTS_CSV,
    MANIFEST_CSV,
    OUT_CSV,
    OUT_MD,
    REQUIRED_ARTIFACT_IDS,
    VOLUME_V2_EXACT_PAIRED_SOURCE_RESOLUTIONS,
    VOLUME_V2_MODEL_IDS,
    load_manifest,
)
from tracking_utils import read_csv, safe_str  # noqa: E402


SUMMARY_REQUIRED_COLUMNS = {
    "segment_type",
    "segment_value",
    "source_artifact",
    "model_id",
    "sample_size",
    "report_date_min",
    "report_date_max",
    "snapshot_report_count",
    "evaluated_d1_count",
    "win_rate_d1",
    "avg_return_d1",
    "median_return_d1",
    "evaluated_d3_count",
    "evaluated_d5_count",
    "evaluated_d10_count",
    "confidence_status",
    "lineage_excluded_count",
    "advisory_only",
    "generated_at",
}

EVENT_REQUIRED_COLUMNS = {
    "source_artifact",
    "snapshot_report_date",
    "stock_id",
    "model_id",
    "mainstream_segment",
    "rank_bucket",
    "score_decile",
    "anchor_date",
    "entry_date",
    "entry_open_price",
    "forward_window_status",
    "return_d1_close_pct",
    "return_d3_close_pct",
    "return_d5_close_pct",
    "return_d10_close_pct",
    "mfe_d10_pct",
    "mae_d10_pct",
    "ranking_evaluation_eligible",
    "trade_eligible",
    "lineage_gate_status",
    "lineage_formal_row_disposition",
    "lineage_evidence_status",
    "lineage_audit_source",
    "lineage_audit_source_sha256",
    "lineage_formal_row_sha256",
    "lineage_observed_formal_row_sha256",
    "lineage_formal_snapshot_sha256",
    "lineage_observed_formal_snapshot_sha256",
    "lineage_paired_source_resolution",
    "lineage_production_code_sha256",
    "lineage_watch_artifact_sha256",
    "lineage_candidate_artifact_sha256",
    "lineage_official_warrant_artifact_sha256",
    "summary_evidence_eligible",
    "lineage_gate_pass_for_promotion_evidence",
    "research_note",
}

LINEAGE_SOURCE_SHA_COLUMNS = (
    "lineage_audit_source_sha256",
    "lineage_production_code_sha256",
    "lineage_watch_artifact_sha256",
    "lineage_candidate_artifact_sha256",
    "lineage_official_warrant_artifact_sha256",
)

FORBIDDEN_SOURCE_NAMES = {
    "daily_candidate_model_signals_for_report_latest.csv",
    "daily_volume_breakout_operation_section_latest.csv",
    "volume_breakout_operation_pdf_preview_latest.csv",
    "historical_pattern_operation_registry_latest.csv",
    "approved_operation_patterns_latest.csv",
}


def compare_docs_copy() -> list[str]:
    errors: list[str] = []
    for output, docs in [(OUT_CSV, DOCS_CSV), (OUT_MD, DOCS_MD)]:
        if not output.exists():
            errors.append(f"missing output artifact: {output.as_posix()}")
            continue
        if not docs.exists():
            errors.append(f"missing docs/latest copy: {docs.as_posix()}")
            continue
        if output.read_text(encoding="utf-8") != docs.read_text(encoding="utf-8"):
            errors.append(f"docs/latest copy differs from output/latest: {docs.as_posix()}")
    return errors


def validate_summary() -> list[str]:
    errors: list[str] = []
    summary = read_csv(OUT_CSV, dtype=str).fillna("")
    if summary.empty:
        return [f"empty summary artifact: {OUT_CSV.as_posix()}"]
    missing = SUMMARY_REQUIRED_COLUMNS - set(summary.columns)
    if missing:
        errors.append(f"summary missing columns: {sorted(missing)}")
        return errors

    if set(summary["advisory_only"].astype(str)) != {"True"}:
        errors.append("summary must be advisory_only=True for every row")
    required_segment_types = {
        "model_overall",
        "model_mainstream_segment",
        "model_rank_bucket",
        "model_score_decile",
        "volume_operation_section",
    }
    observed_segment_types = set(summary["segment_type"].astype(str))
    missing_segments = sorted(required_segment_types - observed_segment_types)
    if missing_segments:
        errors.append(f"summary missing required segment types: {missing_segments}")

    volume_sections = summary[summary["segment_type"].astype(str).eq("volume_operation_section")]
    if volume_sections.empty:
        errors.append("summary must include volume_operation_section rows")
    else:
        joined_values = "\n".join(volume_sections["segment_value"].astype(str).tolist())
        for section in [
            "confirmed_operation",
            "confirmed_unranked_operation",
            "pending_confirmation",
            "active_operation",
        ]:
            if section not in joined_values:
                errors.append(f"summary must evaluate volume operation section separately: missing {section}")
    return errors


def validate_events() -> list[str]:
    errors: list[str] = []
    events = read_csv(EVENTS_CSV, dtype=str).fillna("")
    if events.empty:
        return [f"empty event artifact: {EVENTS_CSV.as_posix()}"]
    missing = EVENT_REQUIRED_COLUMNS - set(events.columns)
    if missing:
        errors.append(f"events missing columns: {sorted(missing)}")
        return errors

    source_artifacts = set(events["source_artifact"].astype(str))
    expected = {"model_signals_for_report", "volume_breakout_operation_section"}
    if not expected.issubset(source_artifacts):
        errors.append(f"events missing expected source_artifacts: {sorted(expected - source_artifacts)}")

    if events["research_note"].astype(str).str.contains("latest|pdf_preview|registry", case=False, regex=True).any():
        errors.append("events research_note must not reference latest/PDF/research registry sources")

    bad_dates = events[~events["snapshot_report_date"].astype(str).str.fullmatch(r"20\d{6}")]
    if not bad_dates.empty:
        errors.append("events contain invalid snapshot_report_date values")

    model_events = events[events["source_artifact"].astype(str).eq("model_signals_for_report")]
    if model_events.empty:
        errors.append("events must contain model_signals_for_report rows")
    else:
        bad_model_trade = model_events[model_events["trade_eligible"].astype(str).eq("True")]
        if not bad_model_trade.empty:
            errors.append("model_signals_for_report rows must not be trade_eligible=True")
        non_volume_v2 = model_events[
            ~model_events["model_id"].astype(str).isin(VOLUME_V2_MODEL_IDS)
        ]
        bad_model_ranking = non_volume_v2[
            ~non_volume_v2["ranking_evaluation_eligible"].astype(str).eq("True")
        ]
        if not bad_model_ranking.empty:
            errors.append(
                "non-volume-v2 model_signals_for_report rows must be "
                "ranking_evaluation_eligible=True"
            )

    operation = events[events["source_artifact"].astype(str).eq("volume_breakout_operation_section")]
    if operation.empty:
        errors.append("events must contain volume operation rows")
    else:
        confirmed = operation[operation["operation_section"].astype(str).eq("confirmed_operation")]
        if not confirmed.empty:
            eligible = confirmed[confirmed["trade_eligible"].astype(str).eq("True")]
            bad = eligible[~eligible["buy_rank_eligible"].astype(str).eq("True")]
            if not bad.empty:
                errors.append("confirmed trade_eligible rows must have buy_rank_eligible=True")
        pending = operation[operation["operation_section"].astype(str).eq("pending_confirmation")]
        bad_pending = pending[pending["trade_eligible"].astype(str).eq("True")]
        if not bad_pending.empty:
            errors.append("pending_confirmation rows must not be trade_eligible=True")
    return errors


def validate_volume_v2_lineage(events: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    if events.empty:
        return errors
    missing = EVENT_REQUIRED_COLUMNS - set(events.columns)
    if missing:
        return errors
    volume = events[events["model_id"].astype(str).isin(VOLUME_V2_MODEL_IDS)].copy()
    if volume.empty:
        return ["events contain no volume-v2 rows for formal-lineage validation"]

    allowed_status = {"verified_clean", "non_clean_excluded", "uncovered_fail_closed"}
    invalid_status = volume[~volume["lineage_gate_status"].astype(str).isin(allowed_status)]
    if not invalid_status.empty:
        errors.append("volume-v2 events contain invalid lineage_gate_status")

    clean = volume[volume["lineage_gate_status"].astype(str).eq("verified_clean")]
    if not clean.empty:
        required_true = (
            "summary_evidence_eligible",
            "lineage_gate_pass_for_promotion_evidence",
        )
        for field in required_true:
            if not clean[field].astype(str).eq("True").all():
                errors.append(f"verified_clean volume-v2 rows require {field}=True")
        clean_model_signals = clean[
            clean["source_artifact"].astype(str).eq("model_signals_for_report")
        ]
        if not clean_model_signals.empty and not clean_model_signals[
            "ranking_evaluation_eligible"
        ].astype(str).eq("True").all():
            errors.append(
                "verified_clean volume-v2 model signal rows require "
                "ranking_evaluation_eligible=True"
            )
        if not clean["lineage_formal_row_disposition"].astype(str).eq(
            "verified_clean"
        ).all():
            errors.append("verified_clean volume-v2 rows require verified_clean disposition")
        if not clean["lineage_evidence_status"].astype(str).eq("complete").all():
            errors.append("verified_clean volume-v2 rows require complete evidence")
        if not clean["lineage_paired_source_resolution"].astype(str).isin(
            VOLUME_V2_EXACT_PAIRED_SOURCE_RESOLUTIONS
        ).all():
            errors.append("verified_clean volume-v2 rows require exact paired source resolution")
        if not clean["lineage_formal_row_sha256"].astype(str).eq(
            clean["lineage_observed_formal_row_sha256"].astype(str)
        ).all():
            errors.append("verified_clean volume-v2 formal row SHA must match observed row SHA")
        if not clean["lineage_formal_snapshot_sha256"].astype(str).eq(
            clean["lineage_observed_formal_snapshot_sha256"].astype(str)
        ).all():
            errors.append(
                "verified_clean volume-v2 formal snapshot SHA must match observed snapshot SHA"
            )
        for field in (
            *LINEAGE_SOURCE_SHA_COLUMNS,
            "lineage_formal_row_sha256",
            "lineage_formal_snapshot_sha256",
        ):
            if not clean[field].astype(str).str.fullmatch(r"[0-9a-f]{64}").all():
                errors.append(f"verified_clean volume-v2 rows require canonical {field}")

    excluded = volume[
        volume["lineage_gate_status"].astype(str).isin(
            {"non_clean_excluded", "uncovered_fail_closed"}
        )
    ]
    if not excluded.empty:
        for field in (
            "summary_evidence_eligible",
            "lineage_gate_pass_for_promotion_evidence",
            "ranking_evaluation_eligible",
            "trade_eligible",
        ):
            if not excluded[field].astype(str).eq("False").all():
                errors.append(f"non-clean volume-v2 rows require {field}=False")
    return errors


def validate_manifest_source_contract() -> list[str]:
    errors: list[str] = []
    if not MANIFEST_CSV.exists():
        return [f"missing manifest: {MANIFEST_CSV.as_posix()}"]
    try:
        manifest = load_manifest(MANIFEST_CSV)
    except Exception as exc:
        return [str(exc)]

    current = manifest[manifest["artifact_id"].astype(str).isin(REQUIRED_ARTIFACT_IDS)]
    if current.empty:
        return ["manifest contains no required ranking snapshot artifacts"]
    for _, row in current.iterrows():
        source_path = safe_str(row.get("source_path", ""))
        snapshot_path = safe_str(row.get("snapshot_path", ""))
        snapshot_name = Path(snapshot_path).name
        if snapshot_name in FORBIDDEN_SOURCE_NAMES:
            errors.append(f"snapshot path must be date-stamped, not latest/PDF/research source: {snapshot_path}")
        if "output/latest/" in snapshot_path.replace("\\", "/"):
            errors.append(f"snapshot path must not point to output/latest: {snapshot_path}")
        if Path(source_path).name not in {
            "daily_candidate_model_signals_for_report_latest.csv",
            "daily_volume_breakout_operation_section_latest.csv",
        }:
            errors.append(f"unexpected source_path for ranking backtest snapshot: {source_path}")
    return errors


def main() -> int:
    events = read_csv(EVENTS_CSV, dtype=str).fillna("")
    errors = (
        compare_docs_copy()
        + validate_summary()
        + validate_events()
        + validate_volume_v2_lineage(events)
        + validate_manifest_source_contract()
    )
    if errors:
        print("ERROR: daily published snapshot ranking backtest validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    summary = read_csv(OUT_CSV, dtype=str).fillna("")
    print("daily published snapshot ranking backtest validation passed")
    print(f"summary_rows={len(summary)}")
    print(f"event_rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
