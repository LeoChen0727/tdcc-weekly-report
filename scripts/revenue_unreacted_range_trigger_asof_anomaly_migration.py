from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from typing import Iterable

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from build_daily_model_parameter_research import (
    _attach_revenue_signal_market_regime,
    _revenue_unreacted_timing_prepared_frame,
)
from revenue_unreacted_range_forward_confirmation_feature_audit import (
    prepare_daily_by_stock,
)
from revenue_unreacted_range_low_mid_falling_candidate_audit import (
    V3_ARTIFACT_VERSION as LOW_MID_V3_VERSION,
    _candidate_detail_artifact_sha256,
    _candidate_detail_row_sha256,
    _v3_provenance_excluded_mapping_sha256,
    _v3_provenance_excluded_table_sha256,
    build_low_mid_falling_candidate_audit,
)
from revenue_unreacted_range_operation_lag_bucket_audit import (
    V3_ARTIFACT_VERSION as OPERATION_LAG_V3_VERSION,
    build_operation_lag_bucket_audit,
)
from revenue_unreacted_range_position_shape_transition_matrix import (
    V3_ARTIFACT_VERSION as POSITION_SHAPE_V3_VERSION,
    build_position_shape_transition_matrix,
)
from revenue_unreacted_range_rearmed_operation_grid import (
    DETAIL_ARTIFACT_DROP_COLUMNS,
    PRICE_HISTORY_CUTOFF_DATE,
    TRIGGER_ASOF_ANOMALY_POLICY_ID,
    V3_ARTIFACT_VERSION as REARMED_V3_VERSION,
    build_rearmed_operation_grid,
)
from revenue_unreacted_range_research_frame import (
    build_revenue_unreacted_range_research_frame,
)
from revenue_unreacted_range_source_first_condition_audit import (
    ARTIFACT_ID as SOURCE_FIRST_ARTIFACT_ID,
    ARTIFACT_VERSION as SOURCE_FIRST_ARTIFACT_VERSION,
    PRIMARY_VARIANT_ID,
    attach_qualifying_event_anomaly_flags,
    load_revenue_history,
)
from revenue_unreacted_range_source_snapshot_projection import (
    V2_PROJECTION_VERSION,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    validate_projection_binding,
)


MODEL_ID = "revenue_unreacted_range"
MIGRATION_ID = (
    "revenue_unreacted_range_6177_trigger_asof_anomaly_attribution_"
    "repair_v1_20260829"
)
GENERATED_AT = "2026-08-29 00:00:00 Asia/Taipei"
SOURCE_EVENT_ARTIFACT_ID = (
    "revenue_unreacted_range_source_first_condition_qualifying_event_anomaly"
)
SOURCE_EVENT_ARTIFACT_VERSION = (
    "source_first_qualifying_event_anomaly_v1_20260829"
)
MIGRATION_ARTIFACT_VERSION = "trigger_asof_anomaly_migration_v1_20260829"
HISTORY_ROOT = ROOT / "output/history/research"


@dataclass(frozen=True)
class ArtifactSpec:
    artifact_id: str
    artifact_version: str
    path: Path


ARTIFACT_SPECS = {
    "source_event": ArtifactSpec(
        SOURCE_EVENT_ARTIFACT_ID,
        SOURCE_EVENT_ARTIFACT_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_source_first_condition_qualifying_event_"
            "anomaly_v1_20260829.csv"
        ),
    ),
    "rearmed_summary": ArtifactSpec(
        "revenue_unreacted_range_rearmed_operation_grid",
        REARMED_V3_VERSION,
        HISTORY_ROOT / "revenue_unreacted_range_rearmed_operation_grid_v3_20260829.csv",
    ),
    "rearmed_detail": ArtifactSpec(
        "revenue_unreacted_range_rearmed_operation_grid_detail",
        REARMED_V3_VERSION,
        HISTORY_ROOT
        / "revenue_unreacted_range_rearmed_operation_grid_detail_v3_20260829.csv",
    ),
    "rearmed_review": ArtifactSpec(
        "revenue_unreacted_range_rearmed_operation_grid_operation_return_review",
        REARMED_V3_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_rearmed_operation_grid_operation_return_"
            "review_v3_20260829.csv"
        ),
    ),
    "operation_lag_summary": ArtifactSpec(
        "revenue_unreacted_range_operation_lag_bucket_audit",
        OPERATION_LAG_V3_VERSION,
        HISTORY_ROOT
        / "revenue_unreacted_range_operation_lag_bucket_audit_v3_20260829.csv",
    ),
    "operation_lag_detail": ArtifactSpec(
        "revenue_unreacted_range_operation_lag_bucket_audit_detail",
        OPERATION_LAG_V3_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_operation_lag_bucket_audit_detail_"
            "v3_20260829.csv"
        ),
    ),
    "position_shape_summary": ArtifactSpec(
        "revenue_unreacted_range_position_shape_transition_matrix",
        POSITION_SHAPE_V3_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_position_shape_transition_matrix_"
            "v3_20260829.csv"
        ),
    ),
    "position_shape_detail": ArtifactSpec(
        "revenue_unreacted_range_position_shape_transition_matrix_detail",
        POSITION_SHAPE_V3_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_position_shape_transition_matrix_detail_"
            "v3_20260829.csv"
        ),
    ),
    "position_shape_transition": ArtifactSpec(
        "revenue_unreacted_range_position_shape_transition_matrix_transition",
        POSITION_SHAPE_V3_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_position_shape_transition_matrix_transition_"
            "v3_20260829.csv"
        ),
    ),
    "low_mid_summary": ArtifactSpec(
        "revenue_unreacted_range_low_mid_falling_candidate_audit",
        LOW_MID_V3_VERSION,
        HISTORY_ROOT
        / "revenue_unreacted_range_low_mid_falling_candidate_audit_v3_20260829.csv",
    ),
    "low_mid_detail": ArtifactSpec(
        "revenue_unreacted_range_low_mid_falling_candidate_audit_detail",
        LOW_MID_V3_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_"
            "v3_20260829.csv"
        ),
    ),
    "low_mid_paired": ArtifactSpec(
        "revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation",
        LOW_MID_V3_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_low_mid_falling_candidate_audit_paired_"
            "confirmation_v3_20260829.csv"
        ),
    ),
    "low_mid_contrast": ArtifactSpec(
        "revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast",
        LOW_MID_V3_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_low_mid_falling_candidate_audit_feature_"
            "contrast_v3_20260829.csv"
        ),
    ),
    "diff_detail": ArtifactSpec(
        "revenue_unreacted_range_trigger_asof_anomaly_migration_diff_detail",
        MIGRATION_ARTIFACT_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_trigger_asof_anomaly_migration_diff_detail_"
            "v1_20260829.csv"
        ),
    ),
    "candidate_rows": ArtifactSpec(
        "revenue_unreacted_range_trigger_asof_selected_anomaly_candidate_rows",
        MIGRATION_ARTIFACT_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_trigger_asof_selected_anomaly_candidate_"
            "rows_v1_20260829.csv"
        ),
    ),
    "validation_summary": ArtifactSpec(
        "revenue_unreacted_range_trigger_asof_anomaly_migration_validation_summary",
        MIGRATION_ARTIFACT_VERSION,
        HISTORY_ROOT
        / (
            "revenue_unreacted_range_trigger_asof_anomaly_migration_validation_"
            "summary_v1_20260829.csv"
        ),
    ),
}
MANIFEST_PATH = (
    HISTORY_ROOT
    / "revenue_unreacted_range_trigger_asof_anomaly_migration_manifest_v1_20260829.csv"
)

V2_PATHS = {
    "rearmed_detail": ROOT
    / "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_detail_latest.csv",
    "operation_lag_detail": ROOT
    / "output/latest/research_backtest/revenue_unreacted_range_operation_lag_bucket_audit_detail_latest.csv",
    "position_shape_detail": ROOT
    / "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_detail_latest.csv",
    "low_mid_detail": ROOT
    / "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv",
    "low_mid_summary": ROOT
    / "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
}

EXPECTED_FAMILY_DIFF_COUNTS = {
    "rearmed_detail": 1259,
    "operation_lag_detail": 36,
    "position_shape_detail": 108,
    "low_mid_detail": 9,
}
KEY_COLUMNS = {
    "rearmed_detail": (
        "grid_id",
        "stock_id",
        "episode_key",
        "trigger_date",
        "entry_date",
    ),
    "operation_lag_detail": (
        "grid_id",
        "stock_id",
        "episode_key",
        "trigger_date",
        "entry_date",
    ),
    "position_shape_detail": (
        "operation_key",
        "anchor_id",
    ),
    "low_mid_detail": ("operation_key",),
}

SELECTED_FILTER = {
    "lifecycle_policy_id": "rearm_after_realized_exit_next_trade_day",
    "confirmation_variant_id": "delayed_next_close_continuation_bonus",
    "holding_days": "30",
    "stop_policy_id": "none_no_stop_reference",
}
SELECTED_BUSINESS_COLUMNS = (
    "operation_key",
    "stock_id",
    "episode_key",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "entry_price",
    "exit_date",
    "exit_price",
    "realized_return_pct",
    "return_outcome",
    "source_anchor_date",
    "source_position_120d_pct",
    "source_shape_return20_pct",
    "source_shape_range23_pct",
    "source_shape_ema23_slope5_pct",
    "source_position_bucket",
    "source_shape_bucket",
    "mid_falling_member",
)
PRIMARY_METRIC_COLUMNS = (
    "operation_count",
    "unique_stock_count",
    "unique_episode_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
    "min_return_pct",
    "max_return_pct",
    "return_ge20_count",
    "return_ge20_rate_pct",
    "return_le_minus20_count",
    "return_le_minus20_rate_pct",
)
ANOMALY_ATTRIBUTION_COLUMNS = (
    "operation_key",
    "source_anomaly_candidate_flag",
    "unresolved_price_path_candidate_flag",
    "operation_return_review_candidate_flag",
    "combined_exclusion_candidate_flag",
    "primary_included",
    "sensitivity_included",
)


def _bool_value(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8-sig")


def _csv_roundtrip(frame: pd.DataFrame) -> pd.DataFrame:
    return pd.read_csv(
        io.StringIO(frame.to_csv(index=False, lineterminator="\n")),
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )


def _canonical_records_sha256(
    frame: pd.DataFrame,
    columns: Iterable[str],
    *,
    row_set: bool,
) -> str:
    selected = _csv_roundtrip(frame).loc[:, list(columns)]
    records = [
        json.dumps(
            {column: str(row[column]) for column in selected.columns},
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        for _, row in selected.iterrows()
    ]
    if row_set:
        records.sort()
    payload = ("\n".join(records) + "\n").encode("utf-8")
    return _sha256(payload)


def _is_diagnostic_provenance_column(column: object) -> bool:
    name = str(column).strip().lower()
    return (
        name == "generated_at"
        or name == "byte_sha256"
        or name.startswith("raw_")
        or "blob_sha256" in name
        or "crlf" in name
    )


def canonical_table_semantic_sha256(frame: pd.DataFrame) -> str:
    columns = [
        column
        for column in frame.columns
        if not _is_diagnostic_provenance_column(column)
    ]
    return _canonical_records_sha256(frame, columns, row_set=False)


def validate_raw_provenance_hash_invariance() -> None:
    base = pd.DataFrame(
        [
            {
                "generated_at": GENERATED_AT,
                "artifact_version": LOW_MID_V3_VERSION,
                "operation_key": "raw-provenance-invariance-probe",
                "trigger_date": "20251204",
                "monthly_revenue_history_blob_sha256": "a" * 64,
                "raw_source_file": "raw-a.csv",
                "raw_source_sha256": "b" * 64,
            }
        ]
    )
    raw_mutation = base.copy()
    raw_mutation.loc[0, "generated_at"] = "2026-08-29 00:01:00 Asia/Taipei"
    raw_mutation.loc[0, "monthly_revenue_history_blob_sha256"] = "c" * 64
    raw_mutation.loc[0, "raw_source_file"] = "raw-b-crlf.csv"
    raw_mutation.loc[0, "raw_source_sha256"] = "d" * 64

    def envelope(frame: pd.DataFrame) -> tuple[str, str, str, str, str, str]:
        row = frame.iloc[0].to_dict()
        candidate_row_sha = _candidate_detail_row_sha256(
            row,
            artifact_version=LOW_MID_V3_VERSION,
        )
        detail = frame.copy()
        detail["candidate_detail_row_sha256"] = candidate_row_sha
        return (
            _v3_provenance_excluded_mapping_sha256(row),
            _v3_provenance_excluded_table_sha256(frame),
            candidate_row_sha,
            _candidate_detail_artifact_sha256(
                detail,
                artifact_version=LOW_MID_V3_VERSION,
            ),
            _canonical_records_sha256(
                detail,
                ("candidate_detail_row_sha256",),
                row_set=True,
            ),
            canonical_table_semantic_sha256(detail),
        )

    baseline_envelope = envelope(base)
    if envelope(raw_mutation) != baseline_envelope:
        raise RuntimeError(
            "v3 raw/blob/CRLF diagnostic mutation changed a canonical promotion hash"
        )
    business_mutation = raw_mutation.copy()
    business_mutation.loc[0, "trigger_date"] = "20251205"
    if any(
        before == after
        for before, after in zip(
            baseline_envelope,
            envelope(business_mutation),
            strict=True,
        )
    ):
        raise RuntimeError(
            "v3 business/PIT mutation did not change every canonical promotion hash"
        )


def _write_append_only(
    path: Path,
    payload: bytes,
    *,
    expected_semantic_sha256: str | None = None,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_bytes()
        if existing != payload:
            if expected_semantic_sha256 is None:
                raise RuntimeError(
                    "append-only v3 artifact already exists with different bytes "
                    f"and no semantic identity: {path}"
                )
            try:
                existing_frame = pd.read_csv(
                    io.BytesIO(existing),
                    dtype=str,
                    keep_default_na=False,
                    low_memory=False,
                )
            except Exception as exc:
                raise RuntimeError(
                    f"append-only v3 artifact cannot be parsed for semantic identity: {path}"
                ) from exc
            existing_semantic_sha256 = canonical_table_semantic_sha256(
                existing_frame
            )
            if existing_semantic_sha256 != expected_semantic_sha256:
                raise RuntimeError(
                    "append-only v3 artifact canonical semantic drift: "
                    f"{path}/{existing_semantic_sha256}/{expected_semantic_sha256}"
                )
        return
    path.write_bytes(payload)


def _pipe_tokens(value: object) -> list[str]:
    return [token.strip() for token in str(value).split("|") if token.strip()]


def build_source_event_anomaly_detail(source_detail: pd.DataFrame) -> pd.DataFrame:
    enriched = attach_qualifying_event_anomaly_flags(
        source_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    selected = enriched.loc[
        enriched["condition_variant_id"].astype(str).eq(PRIMARY_VARIANT_ID)
    ].copy()
    revenue = load_revenue_history(observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE)
    revenue_by_sha = revenue.set_index("source_row_canonical_sha256", drop=False)
    rows: list[dict[str, object]] = []
    for episode in selected.itertuples(index=False):
        parallel = {
            "revenue_period": _pipe_tokens(episode.qualifying_revenue_periods),
            "source_date": _pipe_tokens(episode.qualifying_source_dates),
            "trade_date": _pipe_tokens(episode.qualifying_trade_dates),
            "sequence_index": _pipe_tokens(episode.qualifying_sequence_indices),
            "source_row_canonical_sha256": _pipe_tokens(
                episode.qualifying_source_row_canonical_sha256s
            ),
            "source_revenue_anomaly_candidate_flag": _pipe_tokens(
                episode.qualifying_source_revenue_anomaly_candidate_flags
            ),
        }
        lengths = {len(values) for values in parallel.values()}
        if len(lengths) != 1 or not next(iter(lengths)):
            raise RuntimeError(
                f"source event anomaly detail is not parallel: {episode.episode_key}"
            )
        for event_offset, values in enumerate(zip(*parallel.values()), start=1):
            event = dict(zip(parallel, values))
            canonical_row_sha = event["source_row_canonical_sha256"]
            if canonical_row_sha not in revenue_by_sha.index:
                raise RuntimeError(
                    "source event anomaly canonical row is missing from cutoff history: "
                    f"{canonical_row_sha}"
                )
            source_row = revenue_by_sha.loc[canonical_row_sha]
            source_path = ROOT / str(source_row["source_file"])
            if not source_path.is_file():
                raise RuntimeError(
                    f"source event anomaly raw source file is missing: {source_path}"
                )
            rows.append(
                {
                    "generated_at": GENERATED_AT,
                    "model_id": MODEL_ID,
                    "artifact_id": SOURCE_EVENT_ARTIFACT_ID,
                    "artifact_version": SOURCE_EVENT_ARTIFACT_VERSION,
                    "source_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
                    "source_artifact_version": SOURCE_FIRST_ARTIFACT_VERSION,
                    "source_projection_version": V2_PROJECTION_VERSION,
                    "condition_variant_id": PRIMARY_VARIANT_ID,
                    "episode_key": str(episode.episode_key),
                    "stock_id": str(episode.stock_id),
                    "event_order": event_offset,
                    **event,
                    "raw_source_file": str(source_row["source_file"]),
                    "raw_source_sha256": _sha256(source_path.read_bytes()),
                    "episode_source_revenue_anomaly_candidate_flag": _bool_value(
                        episode.qualifying_source_revenue_anomaly_candidate_flag
                    ),
                    "attribution_policy_id": TRIGGER_ASOF_ANOMALY_POLICY_ID,
                }
            )
    detail = pd.DataFrame(rows)
    duplicate_key = ["episode_key", "event_order"]
    if detail.empty or detail.duplicated(duplicate_key).any():
        raise RuntimeError("source event anomaly detail is empty or duplicated")
    return detail.sort_values(
        ["stock_id", "episode_key", "event_order"], kind="mergesort"
    ).reset_index(drop=True)


def _load_csv(path: Path) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"required immutable v2 artifact is missing: {path}")
    return pd.read_csv(
        path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )


def _row_keys(frame: pd.DataFrame, columns: tuple[str, ...]) -> pd.Series:
    text = _csv_roundtrip(frame)
    missing = sorted(set(columns) - set(text.columns))
    if missing:
        raise RuntimeError(f"migration key columns are missing: {missing}")
    return text.loc[:, list(columns)].astype(str).agg("|".join, axis=1)


def _business_compare_columns(old: pd.DataFrame, new: pd.DataFrame) -> list[str]:
    allowed_exact = {
        "generated_at",
        "artifact_version",
        "source_anomaly_candidate_flag",
        "combined_exclusion_candidate_flag",
        "sensitivity_included",
        "candidate_detail_row_sha256",
        "detail_artifact_canonical_sha256",
        "source_first_canonical_row_set_sha256",
        "rearmed_operation_canonical_row_set_sha256",
        "price_history_canonical_set_sha256",
        "candidate_detail_row_set_sha256",
        "source_operation_artifact_version",
        "source_operation_lag_artifact_version",
        "source_rearmed_artifact_version",
        "rearmed_artifact_version",
        "position_shape_artifact_version",
    }
    columns = []
    for column in old.columns:
        if column not in new.columns or column in allowed_exact:
            continue
        if "sha256" in column:
            continue
        columns.append(column)
    return columns


def compare_family_attribution(
    family: str,
    old: pd.DataFrame,
    new: pd.DataFrame,
) -> pd.DataFrame:
    key_columns = KEY_COLUMNS[family]
    old_text = _csv_roundtrip(old)
    new_text = _csv_roundtrip(new)
    old_text["_migration_row_key"] = _row_keys(old_text, key_columns)
    new_text["_migration_row_key"] = _row_keys(new_text, key_columns)
    if old_text["_migration_row_key"].duplicated().any():
        raise RuntimeError(f"immutable v2 {family} has duplicate migration keys")
    if new_text["_migration_row_key"].duplicated().any():
        raise RuntimeError(f"v3 {family} has duplicate migration keys")
    old_text = old_text.set_index("_migration_row_key", drop=False).sort_index()
    new_text = new_text.set_index("_migration_row_key", drop=False).sort_index()
    if old_text.index.tolist() != new_text.index.tolist():
        raise RuntimeError(f"v3 {family} changed operation identity")
    compare_columns = _business_compare_columns(old_text, new_text)
    changed_business = old_text[compare_columns].ne(new_text[compare_columns])
    if changed_business.any().any():
        first_key, first_column = changed_business.stack().loc[lambda value: value].index[0]
        raise RuntimeError(
            f"v3 {family} changed business projection: {first_key}/{first_column}"
        )
    old_flags = old_text["source_anomaly_candidate_flag"].map(_bool_value)
    new_flags = new_text["source_anomaly_candidate_flag"].map(_bool_value)
    changed = old_flags.ne(new_flags)
    expected = EXPECTED_FAMILY_DIFF_COUNTS[family]
    if int(changed.sum()) != expected:
        raise RuntimeError(
            f"v3 {family} attribution diff count drift: {int(changed.sum())}/{expected}"
        )
    rows = []
    for row_key in old_text.index[changed]:
        before = old_text.loc[row_key]
        after = new_text.loc[row_key]
        rows.append(
            {
                "generated_at": GENERATED_AT,
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_SPECS["diff_detail"].artifact_id,
                "artifact_version": MIGRATION_ARTIFACT_VERSION,
                "migration_id": MIGRATION_ID,
                "artifact_family": family,
                "row_key": row_key,
                "stock_id": str(after.get("stock_id", "")),
                "episode_key": str(after.get("episode_key", "")),
                "trigger_date": str(after.get("trigger_date", "")),
                "entry_date": str(after.get("entry_date", "")),
                "before_source_anomaly_candidate_flag": bool(old_flags.loc[row_key]),
                "after_source_anomaly_candidate_flag": bool(new_flags.loc[row_key]),
                "business_projection_unchanged": True,
                "change_reason": (
                    "future qualifying monthly-revenue anomaly excluded by trigger-as-of cutoff"
                ),
            }
        )
    return pd.DataFrame(rows)


def _selected_detail(detail: pd.DataFrame) -> pd.DataFrame:
    selected = detail.copy()
    for column, expected in SELECTED_FILTER.items():
        selected = selected.loc[selected[column].astype(str).eq(expected)]
    selected = selected.loc[selected["mid_falling_member"].map(_bool_value)].copy()
    return selected.sort_values("operation_key", kind="mergesort").reset_index(drop=True)


def _selected_primary_summary(summary: pd.DataFrame) -> pd.DataFrame:
    selected = summary.loc[
        summary["analysis_basis"].astype(str).eq("primary_candidate_retaining")
        & summary["candidate_variant_id"].astype(str).eq("source_mid_falling")
    ].copy()
    for column, expected in SELECTED_FILTER.items():
        selected = selected.loc[selected[column].astype(str).eq(expected)]
    if len(selected) != 1:
        raise RuntimeError(
            f"v3 selected primary summary must have exactly one row; found {len(selected)}"
        )
    return selected.reset_index(drop=True)


def build_candidate_rows(old_detail: pd.DataFrame, new_detail: pd.DataFrame) -> pd.DataFrame:
    old_selected = _selected_detail(old_detail)
    new_selected = _selected_detail(new_detail)
    old_candidates = old_selected.loc[
        old_selected["combined_exclusion_candidate_flag"].map(_bool_value)
    ].copy()
    if len(old_candidates) != 9:
        raise RuntimeError(
            f"immutable v2 selected candidate row count drift: {len(old_candidates)}/9"
        )
    new_by_key = new_selected.set_index("operation_key", drop=False)
    rows = []
    for before in old_candidates.itertuples(index=False):
        operation_key = str(before.operation_key)
        if operation_key not in new_by_key.index:
            raise RuntimeError(f"v3 selected operation is missing: {operation_key}")
        after = new_by_key.loc[operation_key]
        rows.append(
            {
                "generated_at": GENERATED_AT,
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_SPECS["candidate_rows"].artifact_id,
                "artifact_version": MIGRATION_ARTIFACT_VERSION,
                "migration_id": MIGRATION_ID,
                "operation_key": operation_key,
                "stock_id": str(after["stock_id"]),
                "trigger_date": str(after["trigger_date"]),
                "entry_date": str(after["entry_date"]),
                "exit_date": str(after["exit_date"]),
                "realized_return_pct": str(after["realized_return_pct"]),
                "before_candidate_detail_row_sha256": str(
                    before.candidate_detail_row_sha256
                ),
                "after_candidate_detail_row_sha256": str(
                    after["candidate_detail_row_sha256"]
                ),
                "before_source_anomaly_candidate_flag": bool(
                    _bool_value(before.source_anomaly_candidate_flag)
                ),
                "after_source_anomaly_candidate_flag": bool(
                    _bool_value(after["source_anomaly_candidate_flag"])
                ),
                "operation_return_review_candidate_flag": bool(
                    _bool_value(after["operation_return_review_candidate_flag"])
                ),
                "after_combined_exclusion_candidate_flag": bool(
                    _bool_value(after["combined_exclusion_candidate_flag"])
                ),
                "primary_included": bool(_bool_value(after["primary_included"])),
                "business_projection_unchanged": True,
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["stock_id", "trigger_date", "entry_date"], kind="mergesort"
    ).reset_index(drop=True)


def build_validation_summary(
    old_low_mid: pd.DataFrame,
    old_low_mid_summary: pd.DataFrame,
    new_low_mid: pd.DataFrame,
    new_low_mid_summary: pd.DataFrame,
    diff_detail: pd.DataFrame,
) -> pd.DataFrame:
    old_selected = _selected_detail(old_low_mid)
    new_selected = _selected_detail(new_low_mid)
    old_business_hash = _canonical_records_sha256(
        old_selected, SELECTED_BUSINESS_COLUMNS, row_set=True
    )
    new_business_hash = _canonical_records_sha256(
        new_selected, SELECTED_BUSINESS_COLUMNS, row_set=True
    )
    if old_business_hash != new_business_hash:
        raise RuntimeError("v3 selected 53-operation business projection changed")
    old_primary = _selected_primary_summary(old_low_mid_summary)
    new_primary = _selected_primary_summary(new_low_mid_summary)
    old_primary_metrics_sha = _canonical_records_sha256(
        old_primary, PRIMARY_METRIC_COLUMNS, row_set=False
    )
    new_primary_metrics_sha = _canonical_records_sha256(
        new_primary, PRIMARY_METRIC_COLUMNS, row_set=False
    )
    if old_primary_metrics_sha != new_primary_metrics_sha:
        raise RuntimeError("v3 selected primary metric semantics changed")
    old_anomaly_row_set_sha = _canonical_records_sha256(
        old_selected, ANOMALY_ATTRIBUTION_COLUMNS, row_set=True
    )
    new_anomaly_row_set_sha = _canonical_records_sha256(
        new_selected, ANOMALY_ATTRIBUTION_COLUMNS, row_set=True
    )
    if old_anomaly_row_set_sha == new_anomaly_row_set_sha:
        raise RuntimeError("v3 anomaly attribution row set did not change")
    returns = pd.to_numeric(new_selected["realized_return_pct"], errors="raise")
    outcomes = new_selected["return_outcome"].astype(str)
    source_candidate_count = int(
        new_selected["source_anomaly_candidate_flag"].map(_bool_value).sum()
    )
    return_candidate_count = int(
        new_selected["operation_return_review_candidate_flag"].map(_bool_value).sum()
    )
    combined_candidate_count = int(
        new_selected["combined_exclusion_candidate_flag"].map(_bool_value).sum()
    )
    sensitivity = new_selected.loc[
        new_selected["sensitivity_included"].map(_bool_value)
    ].copy()
    sensitivity_returns = pd.to_numeric(
        sensitivity["realized_return_pct"], errors="raise"
    )
    sensitivity_outcomes = sensitivity["return_outcome"].astype(str)
    values = {
        "generated_at": GENERATED_AT,
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_SPECS["validation_summary"].artifact_id,
        "artifact_version": MIGRATION_ARTIFACT_VERSION,
        "migration_id": MIGRATION_ID,
        "source_projection_version": V2_PROJECTION_VERSION,
        "anomaly_attribution_policy_id": TRIGGER_ASOF_ANOMALY_POLICY_ID,
        "rearmed_artifact_version": REARMED_V3_VERSION,
        "operation_lag_artifact_version": OPERATION_LAG_V3_VERSION,
        "position_shape_artifact_version": POSITION_SHAPE_V3_VERSION,
        "low_mid_artifact_version": LOW_MID_V3_VERSION,
        "rearmed_attribution_changed_row_count": int(
            diff_detail["artifact_family"].eq("rearmed_detail").sum()
        ),
        "operation_lag_attribution_changed_row_count": int(
            diff_detail["artifact_family"].eq("operation_lag_detail").sum()
        ),
        "position_shape_attribution_changed_row_count": int(
            diff_detail["artifact_family"].eq("position_shape_detail").sum()
        ),
        "low_mid_attribution_changed_row_count": int(
            diff_detail["artifact_family"].eq("low_mid_detail").sum()
        ),
        "selected_operation_count": len(new_selected),
        "selected_unique_stock_count": int(new_selected["stock_id"].nunique()),
        "selected_unique_episode_count": int(new_selected["episode_key"].nunique()),
        "selected_win_count": int(outcomes.eq("win").sum()),
        "selected_neutral_count": int(outcomes.eq("neutral").sum()),
        "selected_failure_count": int(outcomes.eq("failure").sum()),
        "selected_avg_return_pct": round(float(returns.mean()), 4),
        "selected_median_return_pct": round(float(returns.median()), 4),
        "selected_source_anomaly_candidate_count": source_candidate_count,
        "selected_operation_return_review_candidate_count": return_candidate_count,
        "selected_combined_exclusion_candidate_count": combined_candidate_count,
        "sensitivity_operation_count": len(sensitivity),
        "sensitivity_win_count": int(sensitivity_outcomes.eq("win").sum()),
        "sensitivity_failure_count": int(sensitivity_outcomes.eq("failure").sum()),
        "sensitivity_avg_return_pct": round(float(sensitivity_returns.mean()), 4),
        "sensitivity_median_return_pct": round(
            float(sensitivity_returns.median()), 4
        ),
        "operation_business_field_change_count": 0,
        "primary_metric_rerun_completed": True,
        "raw_only_mutation_canonical_hashes_unchanged": True,
        "business_pit_mutation_canonical_hashes_changed": True,
        "selected_operation_business_row_set_sha256_before": old_business_hash,
        "selected_operation_business_row_set_sha256_after": new_business_hash,
        "primary_metrics_semantic_sha256_before": old_primary_metrics_sha,
        "primary_metrics_semantic_sha256_after": new_primary_metrics_sha,
        "anomaly_attribution_row_set_sha256_before": old_anomaly_row_set_sha,
        "anomaly_attribution_row_set_sha256_after": new_anomaly_row_set_sha,
        "business_projection_row_set_sha256": new_business_hash,
        "primary_metrics_semantic_sha256": new_primary_metrics_sha,
        "anomaly_attribution_row_set_sha256": new_anomaly_row_set_sha,
        "selected_53_business_projection_unchanged": True,
        "primary_metrics_unchanged": True,
        "v1_v2_artifacts_written": False,
        "approved_for_daily": False,
        "presentation_allowed": False,
        "formal_model_use_allowed": False,
        "production_change": False,
    }
    expected = {
        "selected_operation_count": 53,
        "selected_unique_stock_count": 48,
        "selected_unique_episode_count": 48,
        "selected_win_count": 41,
        "selected_neutral_count": 0,
        "selected_failure_count": 12,
        "selected_avg_return_pct": 14.895,
        "selected_median_return_pct": 9.4077,
        "selected_source_anomaly_candidate_count": 7,
        "selected_operation_return_review_candidate_count": 1,
        "selected_combined_exclusion_candidate_count": 8,
        "sensitivity_operation_count": 45,
        "sensitivity_win_count": 35,
        "sensitivity_failure_count": 10,
        "sensitivity_avg_return_pct": 14.1697,
        "sensitivity_median_return_pct": 9.3306,
    }
    drift = {
        key: (values[key], expected_value)
        for key, expected_value in expected.items()
        if values[key] != expected_value
    }
    if drift:
        raise RuntimeError(f"v3 selected operation metrics drift: {drift}")
    return pd.DataFrame([values])


def build_v3_chain() -> dict[str, pd.DataFrame]:
    validate_raw_provenance_hash_invariance()
    manifest = load_source_snapshot_projection_manifest()
    source_detail = load_projected_source_detail()
    validate_projection_binding(
        manifest,
        source_detail,
        expected_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    if str(manifest.iloc[0]["projection_version"]).strip() != V2_PROJECTION_VERSION:
        raise RuntimeError("trigger-as-of migration requires canonical source projection v2")
    enriched_source = attach_qualifying_event_anomaly_flags(
        source_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    frame = build_revenue_unreacted_range_research_frame()
    if frame.empty:
        raise RuntimeError("trigger-as-of migration has no research price frame")
    prepared = _attach_revenue_signal_market_regime(
        _revenue_unreacted_timing_prepared_frame(frame)
    )
    daily_by_stock = prepare_daily_by_stock(
        prepared,
        source_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    rearmed_summary, rearmed_detail, rearmed_review = build_rearmed_operation_grid(
        source_detail=source_detail,
        daily_by_stock=daily_by_stock,
        source_projection_manifest=manifest,
        anomaly_attribution_policy_id=TRIGGER_ASOF_ANOMALY_POLICY_ID,
        generated_at=GENERATED_AT,
    )
    operation_lag_summary, operation_lag_detail = build_operation_lag_bucket_audit(
        operation_detail=rearmed_detail,
        source_detail=source_detail,
        source_projection_manifest=manifest,
        generated_at=GENERATED_AT,
    )
    position_summary, position_detail, position_transition = (
        build_position_shape_transition_matrix(
            operation_lag_detail=operation_lag_detail,
            rearmed_detail=rearmed_detail,
            daily_by_stock=daily_by_stock,
            generated_at=GENERATED_AT,
            enforce_pinned_baseline=False,
        )
    )
    low_mid_summary, low_mid_detail, low_mid_paired, low_mid_contrast = (
        build_low_mid_falling_candidate_audit(
            source_detail,
            rearmed_detail,
            daily_by_stock,
            generated_at=GENERATED_AT,
        )
    )
    frames = {
        "source_event": build_source_event_anomaly_detail(enriched_source),
        "rearmed_summary": rearmed_summary,
        "rearmed_detail": rearmed_detail.drop(
            columns=list(DETAIL_ARTIFACT_DROP_COLUMNS), errors="raise"
        ),
        "rearmed_review": rearmed_review,
        "operation_lag_summary": operation_lag_summary,
        "operation_lag_detail": operation_lag_detail,
        "position_shape_summary": position_summary,
        "position_shape_detail": position_detail,
        "position_shape_transition": position_transition,
        "low_mid_summary": low_mid_summary,
        "low_mid_detail": low_mid_detail,
        "low_mid_paired": low_mid_paired,
        "low_mid_contrast": low_mid_contrast,
    }
    diffs = []
    for family in EXPECTED_FAMILY_DIFF_COUNTS:
        diffs.append(
            compare_family_attribution(family, _load_csv(V2_PATHS[family]), frames[family])
        )
    diff_detail = pd.concat(diffs, ignore_index=True)
    frames["diff_detail"] = diff_detail
    old_low_mid = _load_csv(V2_PATHS["low_mid_detail"])
    frames["candidate_rows"] = build_candidate_rows(
        old_low_mid, frames["low_mid_detail"]
    )
    frames["validation_summary"] = build_validation_summary(
        old_low_mid,
        _load_csv(V2_PATHS["low_mid_summary"]),
        frames["low_mid_detail"],
        frames["low_mid_summary"],
        diff_detail,
    )
    return frames


def write_v3_chain(frames: dict[str, pd.DataFrame]) -> pd.DataFrame:
    missing = sorted(set(ARTIFACT_SPECS) - set(frames))
    if missing:
        raise RuntimeError(f"v3 chain is missing frames: {missing}")
    manifest_rows = []
    for key, spec in ARTIFACT_SPECS.items():
        frame = frames[key]
        payload = _csv_bytes(frame)
        semantic_sha256 = canonical_table_semantic_sha256(frame)
        _write_append_only(
            spec.path,
            payload,
            expected_semantic_sha256=semantic_sha256,
        )
        manifest_rows.append(
            {
                "generated_at": GENERATED_AT,
                "model_id": MODEL_ID,
                "migration_id": MIGRATION_ID,
                "artifact_key": key,
                "artifact_id": spec.artifact_id,
                "artifact_version": spec.artifact_version,
                "path": spec.path.relative_to(ROOT).as_posix(),
                "row_count": len(frame),
                "byte_sha256": _sha256(spec.path.read_bytes()),
                "canonical_semantic_sha256": semantic_sha256,
                "append_only": True,
                "production_change": False,
            }
        )
    manifest = pd.DataFrame(manifest_rows)
    _write_append_only(
        MANIFEST_PATH,
        _csv_bytes(manifest),
        expected_semantic_sha256=canonical_table_semantic_sha256(manifest),
    )
    return manifest


def validate_committed_v3_chain() -> list[str]:
    errors = []
    for key, spec in ARTIFACT_SPECS.items():
        if not spec.path.is_file():
            errors.append(f"missing append-only v3 artifact: {spec.path}")
    if not MANIFEST_PATH.is_file():
        errors.append(f"missing append-only v3 manifest: {MANIFEST_PATH}")
    if errors:
        return errors
    manifest = _load_csv(MANIFEST_PATH)
    if len(manifest) != len(ARTIFACT_SPECS):
        errors.append(
            f"v3 manifest row count drift: {len(manifest)}/{len(ARTIFACT_SPECS)}"
        )
        return errors
    by_key = manifest.set_index("artifact_key", drop=False)
    for key, spec in ARTIFACT_SPECS.items():
        if key not in by_key.index:
            errors.append(f"v3 manifest missing artifact key: {key}")
            continue
        row = by_key.loc[key]
        payload = spec.path.read_bytes()
        frame = _load_csv(spec.path)
        if str(row["path"]) != spec.path.relative_to(ROOT).as_posix():
            errors.append(f"v3 manifest path drift: {key}")
        if not re.fullmatch(r"[0-9a-f]{64}", str(row["byte_sha256"])):
            errors.append(f"v3 manifest diagnostic byte SHA-256 format drift: {key}")
        if str(row["canonical_semantic_sha256"]) != canonical_table_semantic_sha256(
            frame
        ):
            errors.append(f"v3 manifest semantic SHA-256 drift: {key}")
        if int(row["row_count"]) != len(frame):
            errors.append(f"v3 manifest row count drift: {key}")
    validation = _load_csv(ARTIFACT_SPECS["validation_summary"].path)
    if len(validation) != 1:
        errors.append("v3 validation summary must contain exactly one row")
    elif not (
        _bool_value(validation.iloc[0]["selected_53_business_projection_unchanged"])
        and _bool_value(validation.iloc[0]["primary_metrics_unchanged"])
        and _bool_value(
            validation.iloc[0]["raw_only_mutation_canonical_hashes_unchanged"]
        )
        and _bool_value(
            validation.iloc[0]["business_pit_mutation_canonical_hashes_changed"]
        )
        and not _bool_value(validation.iloc[0]["v1_v2_artifacts_written"])
    ):
        errors.append("v3 validation summary did not preserve immutable business semantics")
    candidates = _load_csv(ARTIFACT_SPECS["candidate_rows"].path)
    if len(candidates) != 9:
        errors.append(f"v3 candidate closure row count drift: {len(candidates)}/9")
    repaired_6177 = candidates.loc[
        candidates["stock_id"].astype(str).eq("6177")
        & candidates["entry_date"].astype(str).eq("20251208")
    ]
    if len(repaired_6177) != 1:
        errors.append("v3 candidate closure is missing the exact 6177 operation")
    elif _bool_value(
        repaired_6177.iloc[0]["after_source_anomaly_candidate_flag"]
    ):
        errors.append("6177 trigger-as-of source anomaly attribution remains true")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Build or validate the append-only revenue trigger-as-of anomaly v3 chain."
        )
    )
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if not args.validate_only:
        frames = build_v3_chain()
        write_v3_chain(frames)
    errors = validate_committed_v3_chain()
    if errors:
        print("FAIL: revenue trigger-as-of anomaly v3 migration")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "PASS: revenue trigger-as-of anomaly v3 migration validated; "
        "v1/v2 immutable, selected 53 operation business projection unchanged"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
