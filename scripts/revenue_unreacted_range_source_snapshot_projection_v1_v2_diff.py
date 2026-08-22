from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff"
ARTIFACT_VERSION = "source_snapshot_projection_v1_v2_diff_v1_20260822"
PROJECTION_ID = "revenue_unreacted_range_source_snapshot_asof_20260713"
V1_PROJECTION_VERSION = "source_snapshot_projection_v1_20260731"
V2_PROJECTION_VERSION = "source_snapshot_projection_v2_20260822"
CUTOFF_DATE = "20260713"

V1_MANIFEST_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v1_20260731.csv"
)
V1_DETAIL_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v1_20260731.csv"
)
V2_MANIFEST_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv"
)
V2_DETAIL_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv"
)
DIFF_SUMMARY_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_"
    "v1_20260731_to_v2_20260822_diff_summary.csv"
)
DIFF_DETAIL_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_"
    "v1_20260731_to_v2_20260822_diff_detail.csv"
)

SUMMARY_COLUMNS = (
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "projection_id",
    "v1_projection_version",
    "v2_projection_version",
    "cutoff_date",
    "v1_manifest_bytes",
    "v1_manifest_sha256",
    "v1_detail_bytes",
    "v1_detail_sha256",
    "v2_manifest_bytes",
    "v2_manifest_sha256",
    "v2_detail_bytes",
    "v2_detail_sha256",
    "v1_episode_row_count",
    "v2_episode_row_count",
    "added_episode_count",
    "removed_episode_count",
    "changed_episode_count",
    "changed_cell_count",
    "changed_column_count",
    "changed_columns",
    "cutoff_price_input_changed_stock_count",
    "cutoff_price_input_row_count_delta",
    "manifest_changed_field_count",
    "manifest_changed_fields",
    "classified_semantic_drift_count",
    "unclassified_semantic_drift_count",
    "semantic_drift_status",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "production_change",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
)

DETAIL_COLUMNS = (
    "drift_id",
    "drift_scope",
    "identity_key",
    "column_name",
    "v1_value",
    "v2_value",
    "change_type",
    "classification",
    "source_evidence",
)

UNCLASSIFIED_DIAGNOSTIC_FIELDS = (
    "drift_scope",
    "identity_key",
    "column_name",
    "change_type",
    "classification",
    "source_evidence",
)

INVARIANT_MANIFEST_FIELDS = {
    "model_id",
    "artifact_id",
    "projection_id",
    "cutoff_date",
    "full_source_artifact_id",
    "full_source_artifact_version",
    "cross_market_resolution_registry_canonical_sha256",
    "cutoff_revenue_subset_row_count",
    "cutoff_revenue_subset_semantic_sha256",
    "applied_monthly_resolution_count",
    "applied_monthly_resolution_ids",
    "applied_monthly_resolution_semantic_sha256",
    "applied_price_resolution_count",
    "applied_price_resolution_ids",
    "applied_price_resolution_semantic_sha256",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "production_change",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
}

VERSION_MANIFEST_FIELDS = {
    "artifact_version",
    "projection_version",
    "projection_policy_id",
    "predecessor_projection_version",
    "predecessor_manifest_bytes_sha256",
    "predecessor_detail_bytes_sha256",
    "lineage_change_reason",
    "candidate_status",
}

CAPTURE_MANIFEST_FIELDS = {
    "generated_at",
    "full_source_episode_row_count",
    "full_source_episode_semantic_sha256",
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
}

PRICE_MANIFEST_FIELDS = {
    "cutoff_price_input_stock_count",
    "cutoff_price_input_row_count",
    "cutoff_price_input_file_semantic_sha256s",
    "cutoff_price_input_semantic_sha256",
    "projected_episode_row_count",
    "projected_episode_semantic_sha256",
    "projected_max_source_date",
    "projected_max_trade_date",
    "projected_max_episode_end_date",
}

DETAIL_CAPTURE_FIELDS = {
    "generated_at",
    "monthly_revenue_history_blob_sha256",
}

PRICE_DERIVED_DETAIL_FIELDS = {
    "episode_start_trade_date",
    "episode_start_sequence_index",
    "latest_qualifying_trade_date",
    "latest_qualifying_sequence_index",
    "qualifying_trade_dates",
    "qualifying_sequence_indices",
    "episode_end_sequence_index",
    "episode_end_date",
    "episode_status",
    "source_price_unreacted_flag",
    "source_close",
    "source_return_5d_pct",
    "source_return_20d_pct",
    "source_volume_ratio",
    "source_range_width_23d_pct",
    "first_breakout_date",
    "first_breakout_lag_from_episode_start_days",
    "first_breakout_outcome",
    "first_breakout_d20_return_pct",
    "launch_date",
    "launch_lag_from_episode_start_days",
    "launch_lag_from_latest_source_days",
    "first_hit_20_day_offset",
    "launch_d20_return_pct",
    "launch_post_hit_min_return_pct",
    "price_path_threshold_candidate_flag",
    "price_path_resolution_ids",
    "unresolved_price_path_candidate_flag",
    "right_censored_flag",
    "retrospective_label_status",
}


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def _value(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value).strip()


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _drift_id(
    scope: str,
    identity_key: str,
    column: str,
    v1_value: str,
    v2_value: str,
    change_type: str,
) -> str:
    payload = "\n".join(
        (scope, identity_key, column, v1_value, v2_value, change_type)
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _detail_row(
    *,
    scope: str,
    identity_key: str,
    column: str,
    v1_value: str,
    v2_value: str,
    change_type: str,
    classification: str,
    source_evidence: str,
) -> dict[str, str]:
    return {
        "drift_id": _drift_id(
            scope,
            identity_key,
            column,
            v1_value,
            v2_value,
            change_type,
        ),
        "drift_scope": scope,
        "identity_key": identity_key,
        "column_name": column,
        "v1_value": v1_value,
        "v2_value": v2_value,
        "change_type": change_type,
        "classification": classification,
        "source_evidence": source_evidence,
    }


def _manifest_classification(column: str, equal: bool) -> tuple[str, str]:
    if column in INVARIANT_MANIFEST_FIELDS:
        if equal:
            return "", ""
        return (
            "unclassified_semantic_drift",
            "immutable cutoff/revenue/resolution/formal-use contract changed",
        )
    if column in VERSION_MANIFEST_FIELDS:
        return (
            "authorized_v2_candidate_metadata",
            "user_authorized_revenue_source_snapshot_projection_v2_bootstrap_20260822",
        )
    if column in CAPTURE_MANIFEST_FIELDS:
        return (
            "current_full_source_capture_refresh",
            "post-v1 full-source capture metadata; cutoff semantics remain invariant",
        )
    if column in PRICE_MANIFEST_FIELDS:
        return (
            "corrected_official_cutoff_price_lineage",
            "official pre-cutoff stock-price history repair",
        )
    return "unclassified_semantic_drift", "unsupported manifest field drift"


def _price_lineage_map(value: object) -> dict[str, tuple[int, str]]:
    result: dict[str, tuple[int, str]] = {}
    text = _value(value)
    if not text:
        return result
    for token in text.split("|"):
        parts = token.split(":")
        if len(parts) != 3 or not parts[1].isdigit():
            raise RuntimeError(f"invalid cutoff price lineage token: {token}")
        stock_id, rows, sha = parts
        if not stock_id or len(sha) != 64:
            raise RuntimeError(f"invalid cutoff price lineage token: {token}")
        if stock_id in result:
            raise RuntimeError(f"duplicate cutoff price lineage stock: {stock_id}")
        result[stock_id] = (int(rows), sha)
    return result


def _episode_price_classification(
    *,
    stock_id: str,
    v1_price: dict[str, tuple[int, str]],
    v2_price: dict[str, tuple[int, str]],
) -> tuple[str, str]:
    left = v1_price.get(stock_id)
    right = v2_price.get(stock_id)
    evidence = f"stock_id={stock_id}; cutoff_price_lineage:{left}->{right}"
    if stock_id and left != right:
        return "corrected_official_cutoff_price_lineage", evidence
    return "unclassified_semantic_drift", evidence


def build_diff_frames(
    v1_manifest: pd.DataFrame,
    v1_detail: pd.DataFrame,
    v2_manifest: pd.DataFrame,
    v2_detail: pd.DataFrame,
    *,
    v1_manifest_bytes: bytes,
    v1_detail_bytes: bytes,
    v2_manifest_bytes: bytes,
    v2_detail_bytes: bytes,
    generated_at: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    for label, frame in (("v1 manifest", v1_manifest), ("v2 manifest", v2_manifest)):
        if len(frame) != 1:
            raise RuntimeError(f"{label} must contain exactly one row")
    if list(v1_detail.columns) != list(v2_detail.columns):
        raise RuntimeError("v1/v2 projection detail schema mismatch")
    if "episode_key" not in v1_detail.columns:
        raise RuntimeError("projection detail is missing episode_key")
    for label, frame in (("v1 detail", v1_detail), ("v2 detail", v2_detail)):
        if frame["episode_key"].astype(str).duplicated().any():
            raise RuntimeError(f"{label} repeats episode_key")

    v1_row = v1_manifest.iloc[0]
    v2_row = v2_manifest.iloc[0]
    expected_identity = {
        "model_id": MODEL_ID,
        "artifact_id": "revenue_unreacted_range_source_snapshot_projection",
        "projection_id": PROJECTION_ID,
        "cutoff_date": CUTOFF_DATE,
    }
    for column, expected in expected_identity.items():
        if _value(v1_row.get(column, "")) != expected:
            raise RuntimeError(f"v1 manifest {column} mismatch")
        if _value(v2_row.get(column, "")) != expected:
            raise RuntimeError(f"v2 manifest {column} mismatch")
    if _value(v1_row.get("projection_version", "")) != V1_PROJECTION_VERSION:
        raise RuntimeError("v1 projection version mismatch")
    if _value(v2_row.get("projection_version", "")) != V2_PROJECTION_VERSION:
        raise RuntimeError("v2 projection version mismatch")
    if _value(v2_row.get("predecessor_projection_version", "")) != V1_PROJECTION_VERSION:
        raise RuntimeError("v2 predecessor projection version mismatch")
    if _value(v2_row.get("predecessor_manifest_bytes_sha256", "")) != _sha256(
        v1_manifest_bytes
    ):
        raise RuntimeError("v2 predecessor manifest bytes SHA-256 mismatch")
    if _value(v2_row.get("predecessor_detail_bytes_sha256", "")) != _sha256(
        v1_detail_bytes
    ):
        raise RuntimeError("v2 predecessor detail bytes SHA-256 mismatch")
    if _value(v2_row.get("candidate_status", "")) != (
        "generated_pending_supersede_approval"
    ):
        raise RuntimeError("v2 candidate status mismatch")

    drift_rows: list[dict[str, str]] = []
    manifest_columns = sorted(set(v1_manifest.columns) | set(v2_manifest.columns))
    for column in manifest_columns:
        v1_value = _value(v1_row.get(column, ""))
        v2_value = _value(v2_row.get(column, ""))
        if v1_value == v2_value:
            continue
        classification, evidence = _manifest_classification(column, False)
        drift_rows.append(
            _detail_row(
                scope="manifest",
                identity_key=PROJECTION_ID,
                column=column,
                v1_value=v1_value,
                v2_value=v2_value,
                change_type=(
                    "added" if column not in v1_manifest.columns else "changed"
                ),
                classification=classification,
                source_evidence=evidence,
            )
        )

    v1_by_key = v1_detail.set_index(v1_detail["episode_key"].astype(str), drop=False)
    v2_by_key = v2_detail.set_index(v2_detail["episode_key"].astype(str), drop=False)
    v1_keys = set(v1_by_key.index)
    v2_keys = set(v2_by_key.index)
    v1_price = _price_lineage_map(
        v1_row.get("cutoff_price_input_file_semantic_sha256s", "")
    )
    v2_price = _price_lineage_map(
        v2_row.get("cutoff_price_input_file_semantic_sha256s", "")
    )
    for key in sorted(v1_keys - v2_keys):
        stock_id = _value(v1_by_key.at[key, "stock_id"])
        classification, evidence = _episode_price_classification(
            stock_id=stock_id,
            v1_price=v1_price,
            v2_price=v2_price,
        )
        drift_rows.append(
            _detail_row(
                scope="episode",
                identity_key=key,
                column="*",
                v1_value="present",
                v2_value="",
                change_type="removed",
                classification=classification,
                source_evidence=evidence,
            )
        )
    for key in sorted(v2_keys - v1_keys):
        stock_id = _value(v2_by_key.at[key, "stock_id"])
        classification, evidence = _episode_price_classification(
            stock_id=stock_id,
            v1_price=v1_price,
            v2_price=v2_price,
        )
        drift_rows.append(
            _detail_row(
                scope="episode",
                identity_key=key,
                column="*",
                v1_value="",
                v2_value="present",
                change_type="added",
                classification=classification,
                source_evidence=evidence,
            )
        )

    changed_episode_keys: set[str] = set()
    for key in sorted(v1_keys & v2_keys):
        stock_id = _value(v2_by_key.at[key, "stock_id"])
        price_classification, price_evidence = _episode_price_classification(
            stock_id=stock_id,
            v1_price=v1_price,
            v2_price=v2_price,
        )
        for column in v1_detail.columns:
            if column in DETAIL_CAPTURE_FIELDS:
                continue
            v1_value = _value(v1_by_key.at[key, column])
            v2_value = _value(v2_by_key.at[key, column])
            if v1_value == v2_value:
                continue
            changed_episode_keys.add(key)
            if column in PRICE_DERIVED_DETAIL_FIELDS:
                classification = price_classification
                evidence = price_evidence
            else:
                classification = "unclassified_semantic_drift"
                evidence = "non-price episode field changed"
            drift_rows.append(
                _detail_row(
                    scope="episode",
                    identity_key=key,
                    column=column,
                    v1_value=v1_value,
                    v2_value=v2_value,
                    change_type="changed",
                    classification=classification,
                    source_evidence=evidence,
                )
            )

    detail = pd.DataFrame(drift_rows, columns=list(DETAIL_COLUMNS))
    if not detail.empty:
        detail = detail.sort_values(
            ["drift_scope", "identity_key", "column_name", "drift_id"],
            kind="stable",
        ).reset_index(drop=True)
    unclassified = int(
        detail["classification"].eq("unclassified_semantic_drift").sum()
    )
    classified = len(detail) - unclassified
    episode_changes = detail.loc[detail["drift_scope"].eq("episode")]
    changed_columns = sorted(
        set(episode_changes["column_name"].astype(str)) - {"*"}
    )
    manifest_changes = detail.loc[detail["drift_scope"].eq("manifest")]
    manifest_changed_fields = sorted(manifest_changes["column_name"].astype(str))
    changed_stocks = sorted(
        stock_id
        for stock_id in set(v1_price) | set(v2_price)
        if v1_price.get(stock_id) != v2_price.get(stock_id)
    )
    row_delta = int(v2_row["cutoff_price_input_row_count"]) - int(
        v1_row["cutoff_price_input_row_count"]
    )
    summary_row = {
        "generated_at": generated_at or _now_text(),
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "projection_id": PROJECTION_ID,
        "v1_projection_version": V1_PROJECTION_VERSION,
        "v2_projection_version": V2_PROJECTION_VERSION,
        "cutoff_date": CUTOFF_DATE,
        "v1_manifest_bytes": len(v1_manifest_bytes),
        "v1_manifest_sha256": _sha256(v1_manifest_bytes),
        "v1_detail_bytes": len(v1_detail_bytes),
        "v1_detail_sha256": _sha256(v1_detail_bytes),
        "v2_manifest_bytes": len(v2_manifest_bytes),
        "v2_manifest_sha256": _sha256(v2_manifest_bytes),
        "v2_detail_bytes": len(v2_detail_bytes),
        "v2_detail_sha256": _sha256(v2_detail_bytes),
        "v1_episode_row_count": len(v1_detail),
        "v2_episode_row_count": len(v2_detail),
        "added_episode_count": len(v2_keys - v1_keys),
        "removed_episode_count": len(v1_keys - v2_keys),
        "changed_episode_count": len(changed_episode_keys),
        "changed_cell_count": len(episode_changes),
        "changed_column_count": len(changed_columns),
        "changed_columns": "|".join(changed_columns) or "none",
        "cutoff_price_input_changed_stock_count": len(changed_stocks),
        "cutoff_price_input_row_count_delta": row_delta,
        "manifest_changed_field_count": len(manifest_changed_fields),
        "manifest_changed_fields": "|".join(manifest_changed_fields) or "none",
        "classified_semantic_drift_count": classified,
        "unclassified_semantic_drift_count": unclassified,
        "semantic_drift_status": (
            "classified_corrected_official_cutoff_price_lineage"
            if unclassified == 0
            else "unclassified_semantic_drift_blocked"
        ),
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "production_change": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
    }
    return pd.DataFrame([summary_row], columns=list(SUMMARY_COLUMNS)), detail


def build_diff_from_paths(
    *,
    v1_manifest_path: Path = V1_MANIFEST_CSV,
    v1_detail_path: Path = V1_DETAIL_CSV,
    v2_manifest_path: Path = V2_MANIFEST_CSV,
    v2_detail_path: Path = V2_DETAIL_CSV,
    generated_at: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    paths = (
        Path(v1_manifest_path),
        Path(v1_detail_path),
        Path(v2_manifest_path),
        Path(v2_detail_path),
    )
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise RuntimeError(f"missing v1/v2 projection artifact: {missing}")
    frames = (
        pd.read_csv(paths[0], dtype=str, keep_default_na=False),
        pd.read_csv(paths[1], dtype=str, keep_default_na=False, low_memory=False),
        pd.read_csv(paths[2], dtype=str, keep_default_na=False),
        pd.read_csv(paths[3], dtype=str, keep_default_na=False, low_memory=False),
    )
    return build_diff_frames(
        *frames,
        v1_manifest_bytes=paths[0].read_bytes(),
        v1_detail_bytes=paths[1].read_bytes(),
        v2_manifest_bytes=paths[2].read_bytes(),
        v2_detail_bytes=paths[3].read_bytes(),
        generated_at=generated_at,
    )


def _emit_unclassified_drift_diagnostics(
    detail: pd.DataFrame,
    *,
    unclassified_count: int,
) -> None:
    print(
        "v1_v2_diff_unclassified_semantic_drift_count="
        f"{unclassified_count}",
        file=sys.stderr,
        flush=True,
    )
    unclassified_rows = detail.loc[
        detail["classification"].eq("unclassified_semantic_drift")
    ].sort_values(
        ["drift_scope", "identity_key", "column_name", "drift_id"],
        kind="stable",
    )
    for _, row in unclassified_rows.iterrows():
        payload = {
            field: _value(row[field])
            for field in UNCLASSIFIED_DIAGNOSTIC_FIELDS
        }
        print(
            "v1_v2_diff_unclassified_semantic_drift_row="
            + json.dumps(
                payload,
                ensure_ascii=True,
                sort_keys=True,
                separators=(",", ":"),
            ),
            file=sys.stderr,
            flush=True,
        )


def write_diff_artifacts(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    *,
    summary_path: Path = DIFF_SUMMARY_CSV,
    detail_path: Path = DIFF_DETAIL_CSV,
) -> None:
    if list(summary.columns) != list(SUMMARY_COLUMNS) or len(summary) != 1:
        raise RuntimeError("v1/v2 diff summary schema or row count mismatch")
    if list(detail.columns) != list(DETAIL_COLUMNS):
        raise RuntimeError("v1/v2 diff detail schema mismatch")
    unclassified_count = int(
        summary.iloc[0]["unclassified_semantic_drift_count"]
    )
    if unclassified_count != 0:
        _emit_unclassified_drift_diagnostics(
            detail,
            unclassified_count=unclassified_count,
        )
        raise RuntimeError("v1/v2 diff contains unclassified semantic drift")
    for path in (Path(summary_path), Path(detail_path)):
        path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(summary_path, index=False)
    detail.to_csv(detail_path, index=False)
