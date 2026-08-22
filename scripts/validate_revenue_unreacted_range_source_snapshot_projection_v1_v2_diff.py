from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
PROJECTION_ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
DIFF_ARTIFACT_ID = (
    "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff"
)
DIFF_ARTIFACT_VERSION = "source_snapshot_projection_v1_v2_diff_v1_20260822"
PROJECTION_ID = "revenue_unreacted_range_source_snapshot_asof_20260713"
V1_VERSION = "source_snapshot_projection_v1_20260731"
V2_VERSION = "source_snapshot_projection_v2_20260822"
V2_POLICY = (
    "raw_source_and_corrected_official_price_truncated_before_"
    "source_first_episode_assembly_v2"
)
V2_LINEAGE_CHANGE_REASON = (
    "corrected_official_pre_cutoff_price_history_lineage_rebaseline_20260822"
)
CANDIDATE_STATUS = "generated_pending_supersede_approval"
CUTOFF_DATE = "20260713"
V1_EXPECTED_MANIFEST_BYTES = 148157
V1_EXPECTED_MANIFEST_SHA256 = (
    "d2dde5a1f05bc2f15baf4d77f326a7ea90b481492178fa6d2fd6262bf316c79e"
)
V1_EXPECTED_DETAIL_BYTES = 26633382
V1_EXPECTED_DETAIL_SHA256 = (
    "b9784e4df2d2eba2c511b1c87f4255a6485a1fe1d7ac67490802e396614ee49a"
)
V1_EXPECTED_DETAIL_ROW_COUNT = 19569

V1_MANIFEST_CSV = ROOT / (
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v1_20260731.csv"
)
V1_DETAIL_CSV = ROOT / (
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v1_20260731.csv"
)
V2_MANIFEST_CSV = ROOT / (
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv"
)
V2_DETAIL_CSV = ROOT / (
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv"
)
DIFF_SUMMARY_CSV = ROOT / (
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_"
    "v1_20260731_to_v2_20260822_diff_summary.csv"
)
DIFF_DETAIL_CSV = ROOT / (
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_"
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
DETAIL_CAPTURE_FIELDS = {"generated_at", "monthly_revenue_history_blob_sha256"}
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
    return hashlib.sha256(
        "\n".join(
            (scope, identity_key, column, v1_value, v2_value, change_type)
        ).encode("utf-8")
    ).hexdigest()


def _expected_row(
    scope: str,
    identity_key: str,
    column: str,
    v1_value: str,
    v2_value: str,
    change_type: str,
    classification: str,
    evidence: str,
) -> dict[str, str]:
    return {
        "drift_id": _drift_id(
            scope, identity_key, column, v1_value, v2_value, change_type
        ),
        "drift_scope": scope,
        "identity_key": identity_key,
        "column_name": column,
        "v1_value": v1_value,
        "v2_value": v2_value,
        "change_type": change_type,
        "classification": classification,
        "source_evidence": evidence,
    }


def _classification(column: str) -> tuple[str, str]:
    if column in INVARIANT_MANIFEST_FIELDS:
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


def _price_map(value: object) -> dict[str, tuple[int, str]]:
    result: dict[str, tuple[int, str]] = {}
    for token in filter(None, _value(value).split("|")):
        parts = token.split(":")
        if len(parts) != 3 or not parts[1].isdigit() or len(parts[2]) != 64:
            raise RuntimeError(f"invalid cutoff price lineage token: {token}")
        if parts[0] in result:
            raise RuntimeError(f"duplicate cutoff price lineage stock: {parts[0]}")
        result[parts[0]] = (int(parts[1]), parts[2])
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


def _expected_diff(
    v1_manifest: pd.DataFrame,
    v1_detail: pd.DataFrame,
    v2_manifest: pd.DataFrame,
    v2_detail: pd.DataFrame,
) -> tuple[pd.DataFrame, dict[str, object]]:
    v1_row = v1_manifest.iloc[0]
    v2_row = v2_manifest.iloc[0]
    rows: list[dict[str, str]] = []
    for column in sorted(set(v1_manifest.columns) | set(v2_manifest.columns)):
        left = _value(v1_row.get(column, ""))
        right = _value(v2_row.get(column, ""))
        if left == right:
            continue
        classification, evidence = _classification(column)
        rows.append(
            _expected_row(
                "manifest",
                PROJECTION_ID,
                column,
                left,
                right,
                "added" if column not in v1_manifest.columns else "changed",
                classification,
                evidence,
            )
        )

    v1_by_key = v1_detail.set_index(v1_detail["episode_key"].astype(str), drop=False)
    v2_by_key = v2_detail.set_index(v2_detail["episode_key"].astype(str), drop=False)
    v1_keys = set(v1_by_key.index)
    v2_keys = set(v2_by_key.index)
    v1_price = _price_map(v1_row["cutoff_price_input_file_semantic_sha256s"])
    v2_price = _price_map(v2_row["cutoff_price_input_file_semantic_sha256s"])
    for key in sorted(v1_keys - v2_keys):
        stock_id = _value(v1_by_key.at[key, "stock_id"])
        classification, evidence = _episode_price_classification(
            stock_id=stock_id,
            v1_price=v1_price,
            v2_price=v2_price,
        )
        rows.append(
            _expected_row(
                "episode",
                key,
                "*",
                "present",
                "",
                "removed",
                classification,
                evidence,
            )
        )
    for key in sorted(v2_keys - v1_keys):
        stock_id = _value(v2_by_key.at[key, "stock_id"])
        classification, evidence = _episode_price_classification(
            stock_id=stock_id,
            v1_price=v1_price,
            v2_price=v2_price,
        )
        rows.append(
            _expected_row(
                "episode",
                key,
                "*",
                "",
                "present",
                "added",
                classification,
                evidence,
            )
        )
    changed_keys: set[str] = set()
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
            left = _value(v1_by_key.at[key, column])
            right = _value(v2_by_key.at[key, column])
            if left == right:
                continue
            changed_keys.add(key)
            if column in PRICE_DERIVED_DETAIL_FIELDS:
                classification = price_classification
                evidence = price_evidence
            else:
                classification = "unclassified_semantic_drift"
                evidence = "non-price episode field changed"
            rows.append(
                _expected_row(
                    "episode",
                    key,
                    column,
                    left,
                    right,
                    "changed",
                    classification,
                    evidence,
                )
            )
    detail = pd.DataFrame(rows, columns=list(DETAIL_COLUMNS))
    if not detail.empty:
        detail = detail.sort_values(
            ["drift_scope", "identity_key", "column_name", "drift_id"],
            kind="stable",
        ).reset_index(drop=True)
    episode = detail.loc[detail["drift_scope"].eq("episode")]
    manifest = detail.loc[detail["drift_scope"].eq("manifest")]
    changed_stocks = {
        stock_id
        for stock_id in set(v1_price) | set(v2_price)
        if v1_price.get(stock_id) != v2_price.get(stock_id)
    }
    metrics: dict[str, object] = {
        "added_episode_count": len(v2_keys - v1_keys),
        "removed_episode_count": len(v1_keys - v2_keys),
        "changed_episode_count": len(changed_keys),
        "changed_cell_count": len(episode),
        "changed_columns": sorted(set(episode["column_name"]) - {"*"}),
        "changed_stocks": changed_stocks,
        "manifest_changed_fields": sorted(manifest["column_name"]),
        "unclassified": int(
            detail["classification"].eq("unclassified_semantic_drift").sum()
        ),
    }
    return detail, metrics


def validate(
    *,
    v1_manifest_path: Path = V1_MANIFEST_CSV,
    v1_detail_path: Path = V1_DETAIL_CSV,
    v2_manifest_path: Path = V2_MANIFEST_CSV,
    v2_detail_path: Path = V2_DETAIL_CSV,
    summary_path: Path = DIFF_SUMMARY_CSV,
    detail_path: Path = DIFF_DETAIL_CSV,
    expected_v1_manifest_bytes: int = V1_EXPECTED_MANIFEST_BYTES,
    expected_v1_manifest_sha256: str = V1_EXPECTED_MANIFEST_SHA256,
    expected_v1_detail_bytes: int = V1_EXPECTED_DETAIL_BYTES,
    expected_v1_detail_sha256: str = V1_EXPECTED_DETAIL_SHA256,
    expected_v1_detail_row_count: int = V1_EXPECTED_DETAIL_ROW_COUNT,
) -> list[str]:
    errors: list[str] = []
    paths = {
        "v1 manifest": Path(v1_manifest_path),
        "v1 detail": Path(v1_detail_path),
        "v2 manifest": Path(v2_manifest_path),
        "v2 detail": Path(v2_detail_path),
        "diff summary": Path(summary_path),
        "diff detail": Path(detail_path),
    }
    missing = [f"{label}: {path}" for label, path in paths.items() if not path.is_file()]
    if missing:
        return [f"missing source projection v1/v2 diff artifact: {item}" for item in missing]
    try:
        v1_manifest = pd.read_csv(paths["v1 manifest"], dtype=str, keep_default_na=False)
        v1_detail = pd.read_csv(
            paths["v1 detail"], dtype=str, keep_default_na=False, low_memory=False
        )
        v2_manifest = pd.read_csv(paths["v2 manifest"], dtype=str, keep_default_na=False)
        v2_detail = pd.read_csv(
            paths["v2 detail"], dtype=str, keep_default_na=False, low_memory=False
        )
        summary = pd.read_csv(paths["diff summary"], dtype=str, keep_default_na=False)
        detail = pd.read_csv(paths["diff detail"], dtype=str, keep_default_na=False)
    except (OSError, pd.errors.ParserError) as exc:
        return [f"source projection v1/v2 diff cannot be parsed: {exc}"]
    if len(v1_manifest) != 1 or len(v2_manifest) != 1:
        return ["v1 and v2 manifests must each contain exactly one row"]
    if list(v1_detail.columns) != list(v2_detail.columns):
        return ["v1/v2 projection detail schema mismatch"]
    if "episode_key" not in v1_detail.columns:
        return ["projection detail is missing episode_key"]
    if v1_detail["episode_key"].duplicated().any() or v2_detail["episode_key"].duplicated().any():
        errors.append("v1/v2 projection detail repeats episode_key")
    if list(summary.columns) != list(SUMMARY_COLUMNS) or len(summary) != 1:
        errors.append("v1/v2 diff summary schema or row count mismatch")
        return errors
    if list(detail.columns) != list(DETAIL_COLUMNS):
        errors.append("v1/v2 diff detail schema mismatch")
        return errors
    row = summary.iloc[0]
    v1_row = v1_manifest.iloc[0]
    v2_row = v2_manifest.iloc[0]
    expected_identity = {
        "model_id": MODEL_ID,
        "artifact_id": PROJECTION_ARTIFACT_ID,
        "projection_id": PROJECTION_ID,
        "cutoff_date": CUTOFF_DATE,
    }
    for column, expected in expected_identity.items():
        for label, manifest_row in (("v1", v1_row), ("v2", v2_row)):
            if _value(manifest_row.get(column, "")) != expected:
                errors.append(f"{label} manifest {column} mismatch")
    expected_v2 = {
        "projection_version": V2_VERSION,
        "artifact_version": V2_VERSION,
        "projection_policy_id": V2_POLICY,
        "predecessor_projection_version": V1_VERSION,
        "lineage_change_reason": V2_LINEAGE_CHANGE_REASON,
        "candidate_status": CANDIDATE_STATUS,
    }
    for column, expected in expected_v2.items():
        if _value(v2_row.get(column, "")) != expected:
            errors.append(f"v2 manifest {column} mismatch")
    if _value(v1_row.get("projection_version", "")) != V1_VERSION:
        errors.append("v1 projection version mismatch")
    for column in INVARIANT_MANIFEST_FIELDS:
        if _value(v1_row.get(column, "")) != _value(v2_row.get(column, "")):
            errors.append(f"immutable v1/v2 manifest field changed: {column}")
    if _value(v1_row.get("cutoff_price_input_semantic_sha256", "")) == _value(
        v2_row.get("cutoff_price_input_semantic_sha256", "")
    ):
        errors.append("v2 candidate does not bind a changed official cutoff-price lineage")

    v1_manifest_payload = paths["v1 manifest"].read_bytes()
    v1_detail_payload = paths["v1 detail"].read_bytes()
    for label, actual, expected in (
        ("v1 manifest bytes", len(v1_manifest_payload), expected_v1_manifest_bytes),
        ("v1 manifest SHA-256", _sha256(v1_manifest_payload), expected_v1_manifest_sha256),
        ("v1 detail bytes", len(v1_detail_payload), expected_v1_detail_bytes),
        ("v1 detail SHA-256", _sha256(v1_detail_payload), expected_v1_detail_sha256),
        ("v1 detail row count", len(v1_detail), expected_v1_detail_row_count),
    ):
        if actual != expected:
            errors.append(f"immutable {label} mismatch: {actual}/{expected}")

    byte_bindings = (
        ("v1_manifest", paths["v1 manifest"]),
        ("v1_detail", paths["v1 detail"]),
        ("v2_manifest", paths["v2 manifest"]),
        ("v2_detail", paths["v2 detail"]),
    )
    for prefix, path in byte_bindings:
        payload = path.read_bytes()
        if _value(row[f"{prefix}_bytes"]) != str(len(payload)):
            errors.append(f"diff summary {prefix} bytes mismatch")
        if _value(row[f"{prefix}_sha256"]) != _sha256(payload):
            errors.append(f"diff summary {prefix} SHA-256 mismatch")
    v1_manifest_sha = _sha256(v1_manifest_payload)
    v1_detail_sha = _sha256(v1_detail_payload)
    if _value(v2_row.get("predecessor_manifest_bytes_sha256", "")) != v1_manifest_sha:
        errors.append("v2 predecessor manifest bytes SHA-256 mismatch")
    if _value(v2_row.get("predecessor_detail_bytes_sha256", "")) != v1_detail_sha:
        errors.append("v2 predecessor detail bytes SHA-256 mismatch")

    if _value(row["artifact_id"]) != DIFF_ARTIFACT_ID:
        errors.append("v1/v2 diff artifact id mismatch")
    if _value(row["artifact_version"]) != DIFF_ARTIFACT_VERSION:
        errors.append("v1/v2 diff artifact version mismatch")
    for column, expected in (
        ("model_id", MODEL_ID),
        ("projection_id", PROJECTION_ID),
        ("v1_projection_version", V1_VERSION),
        ("v2_projection_version", V2_VERSION),
        ("cutoff_date", CUTOFF_DATE),
        ("v1_episode_row_count", str(len(v1_detail))),
        ("v2_episode_row_count", str(len(v2_detail))),
    ):
        if _value(row[column]) != expected:
            errors.append(f"v1/v2 diff summary {column} mismatch")
    if detail["drift_id"].duplicated().any():
        errors.append("v1/v2 diff detail repeats drift_id")
    if detail["classification"].astype(str).str.strip().eq("").any():
        errors.append("v1/v2 diff detail has empty classification")
    if detail["source_evidence"].astype(str).str.strip().eq("").any():
        errors.append("v1/v2 diff detail has empty source evidence")

    try:
        expected_detail, metrics = _expected_diff(
            v1_manifest, v1_detail, v2_manifest, v2_detail
        )
    except (RuntimeError, KeyError, TypeError, ValueError) as exc:
        errors.append(f"independent v1/v2 diff reconstruction failed: {exc}")
        return errors
    actual_sorted = detail.sort_values(
        ["drift_scope", "identity_key", "column_name", "drift_id"], kind="stable"
    ).reset_index(drop=True)
    if not actual_sorted.equals(expected_detail):
        errors.append("v1/v2 diff detail does not match independent reconstruction")
    expected_counts = {
        "added_episode_count": metrics["added_episode_count"],
        "removed_episode_count": metrics["removed_episode_count"],
        "changed_episode_count": metrics["changed_episode_count"],
        "changed_cell_count": metrics["changed_cell_count"],
        "changed_column_count": len(metrics["changed_columns"]),
        "cutoff_price_input_changed_stock_count": len(metrics["changed_stocks"]),
        "manifest_changed_field_count": len(metrics["manifest_changed_fields"]),
        "unclassified_semantic_drift_count": metrics["unclassified"],
    }
    for column, expected in expected_counts.items():
        if _value(row[column]) != str(expected):
            errors.append(f"v1/v2 diff summary {column} mismatch")
    if _value(row["changed_columns"]) != (
        "|".join(metrics["changed_columns"]) or "none"
    ):
        errors.append("v1/v2 diff summary changed_columns mismatch")
    if _value(row["manifest_changed_fields"]) != (
        "|".join(metrics["manifest_changed_fields"]) or "none"
    ):
        errors.append("v1/v2 diff summary manifest_changed_fields mismatch")
    classified = len(expected_detail) - int(metrics["unclassified"])
    if _value(row["classified_semantic_drift_count"]) != str(classified):
        errors.append("v1/v2 diff summary classified count mismatch")
    if int(metrics["unclassified"]) != 0:
        errors.append("v1/v2 diff contains unclassified semantic drift")
    if _value(row["semantic_drift_status"]) != (
        "classified_corrected_official_cutoff_price_lineage"
    ):
        errors.append("v1/v2 diff semantic drift status mismatch")
    if not metrics["changed_stocks"]:
        errors.append("v1/v2 diff has no changed official cutoff-price stock lineage")
    if _value(row["cutoff_price_input_row_count_delta"]) != str(
        int(v2_row["cutoff_price_input_row_count"])
        - int(v1_row["cutoff_price_input_row_count"])
    ):
        errors.append("v1/v2 diff cutoff price row-count delta mismatch")
    if _value(row["research_only"]).lower() != "true":
        errors.append("v1/v2 diff research_only must be true")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if _value(row[column]).lower() != "false":
            errors.append(f"v1/v2 diff {column} must be false")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Independently validate the revenue source projection v1/v2 diff."
    )
    parser.add_argument("--v1-manifest", type=Path, default=V1_MANIFEST_CSV)
    parser.add_argument("--v1-detail", type=Path, default=V1_DETAIL_CSV)
    parser.add_argument("--v2-manifest", type=Path, default=V2_MANIFEST_CSV)
    parser.add_argument("--v2-detail", type=Path, default=V2_DETAIL_CSV)
    parser.add_argument("--diff-summary", type=Path, default=DIFF_SUMMARY_CSV)
    parser.add_argument("--diff-detail", type=Path, default=DIFF_DETAIL_CSV)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(
        v1_manifest_path=args.v1_manifest,
        v1_detail_path=args.v1_detail,
        v2_manifest_path=args.v2_manifest,
        v2_detail_path=args.v2_detail,
        summary_path=args.diff_summary,
        detail_path=args.diff_detail,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "revenue source snapshot projection v1/v2 diff validation passed: "
        "candidate_status=generated_pending_supersede_approval; "
        "unclassified_semantic_drift_count=0; formal_model_use_allowed=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
