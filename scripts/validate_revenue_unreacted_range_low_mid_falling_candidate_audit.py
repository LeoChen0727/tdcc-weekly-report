from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import hashlib
from io import BytesIO
import json
import math
import numbers
from pathlib import Path, PurePosixPath
import re
import subprocess

import numpy as np
import pandas as pd

V1_PROJECTION_VERSION = "source_snapshot_projection_v1_20260731"
V2_PROJECTION_VERSION = "source_snapshot_projection_v2_20260822"
PROJECTION_ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
PROJECTION_ID = "revenue_unreacted_range_source_snapshot_asof_20260713"
V1_PROJECTION_POLICY_ID = (
    "raw_source_and_price_truncated_before_source_first_episode_assembly_v1"
)
V2_PROJECTION_POLICY_ID = (
    "raw_source_and_corrected_official_price_truncated_before_source_first_episode_assembly_v2"
)
V2_LINEAGE_CHANGE_REASON = (
    "corrected_official_pre_cutoff_price_history_lineage_rebaseline_20260822"
)
V2_CANDIDATE_STATUS = "generated_pending_supersede_approval"
V1_PREDECESSOR_MANIFEST_SHA256 = (
    "d2dde5a1f05bc2f15baf4d77f326a7ea90b481492178fa6d2fd6262bf316c79e"
)
V1_PREDECESSOR_DETAIL_SHA256 = (
    "b9784e4df2d2eba2c511b1c87f4255a6485a1fe1d7ac67490802e396614ee49a"
)
PROJECTION_CANONICAL_JSON_VERSION = (
    "revenue_source_snapshot_projection_canonical_json_v1"
)
PROJECTION_CAPTURE_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
V1_PROJECTION_MANIFEST_COLUMNS = (
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "projection_id",
    "projection_version",
    "projection_policy_id",
    "cutoff_date",
    "full_source_artifact_id",
    "full_source_artifact_version",
    "full_source_episode_row_count",
    "full_source_episode_semantic_sha256",
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
    "cutoff_revenue_subset_row_count",
    "cutoff_revenue_subset_semantic_sha256",
    "cutoff_price_input_stock_count",
    "cutoff_price_input_row_count",
    "cutoff_price_input_file_semantic_sha256s",
    "cutoff_price_input_semantic_sha256",
    "applied_monthly_resolution_count",
    "applied_monthly_resolution_ids",
    "applied_monthly_resolution_semantic_sha256",
    "applied_price_resolution_count",
    "applied_price_resolution_ids",
    "applied_price_resolution_semantic_sha256",
    "projected_episode_row_count",
    "projected_episode_semantic_sha256",
    "projected_max_source_date",
    "projected_max_trade_date",
    "projected_max_episode_end_date",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "production_change",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
)
V2_PROJECTION_MANIFEST_COLUMNS = V1_PROJECTION_MANIFEST_COLUMNS + (
    "predecessor_projection_version",
    "predecessor_manifest_bytes_sha256",
    "predecessor_detail_bytes_sha256",
    "lineage_change_reason",
    "candidate_status",
)

ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_low_mid_falling_candidate_audit"
ARTIFACT_VERSION = "low_mid_falling_candidate_v1_20260720"
V2_ARTIFACT_VERSION = "low_mid_falling_candidate_v2_20260822"
EXPECTED_DATA_CONTRACT_SHA256 = (
    "4aff77863a07ba5fe7c574731ea84ac778b85daffbbfe7123d38cccd4cc61432"
)
SOURCE_FIRST_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
SOURCE_FIRST_ARTIFACT_VERSION = "source_first_condition_v3_20260720"
REARMED_ARTIFACT_ID = "revenue_unreacted_range_rearmed_operation_grid"
REARMED_ARTIFACT_VERSION = "rearmed_operation_grid_v1_20260713"
V2_REARMED_ARTIFACT_VERSION = "rearmed_operation_grid_v2_20260822"
POSITION_SHAPE_ARTIFACT_ID = (
    "revenue_unreacted_range_position_shape_transition_matrix"
)
POSITION_SHAPE_ARTIFACT_VERSION = "position_shape_transition_matrix_v1_20260717"
V2_POSITION_SHAPE_ARTIFACT_VERSION = "position_shape_transition_matrix_v2_20260822"
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
PRICE_HISTORY_CUTOFF_DATE = "20260713"
TRUSTED_SOURCE_REVISION = "b7ab7b6122b422e941efa3a3a1a915fbfcb59f4d"
EXPECTED_V1_MANIFEST_DESCRIPTOR = {
    "model_id": MODEL_ID,
    "artifact_id": "revenue_unreacted_range_source_snapshot_projection",
    "artifact_version": "source_snapshot_projection_v1_20260731",
    "projection_id": "revenue_unreacted_range_source_snapshot_asof_20260713",
    "projection_version": "source_snapshot_projection_v1_20260731",
    "projection_policy_id": (
        "raw_source_and_price_truncated_before_source_first_episode_assembly_v1"
    ),
    "cutoff_date": PRICE_HISTORY_CUTOFF_DATE,
    "full_source_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
    "full_source_artifact_version": SOURCE_FIRST_ARTIFACT_VERSION,
    "projected_max_source_date": "20260617",
    "projected_max_trade_date": "20260629",
    "projected_max_episode_end_date": PRICE_HISTORY_CUTOFF_DATE,
    "research_only": "True",
    "formal_model_use_allowed": "False",
    "approved_for_daily": "False",
    "production_change": "False",
}
_TRUSTED_TREE_CACHE: dict[str, dict[str, tuple[str, str, str]]] = {}
_TRUSTED_BLOB_CACHE: dict[tuple[str, str], bytes] = {}
VERSION_CONTRACT_BY_PROJECTION = {
    V1_PROJECTION_VERSION: (
        ARTIFACT_VERSION,
        REARMED_ARTIFACT_VERSION,
        POSITION_SHAPE_ARTIFACT_VERSION,
    ),
    V2_PROJECTION_VERSION: (
        V2_ARTIFACT_VERSION,
        V2_REARMED_ARTIFACT_VERSION,
        V2_POSITION_SHAPE_ARTIFACT_VERSION,
    ),
}


def _version_contract(projection_version: object) -> tuple[str, str, str]:
    version = str(projection_version).strip()
    try:
        return VERSION_CONTRACT_BY_PROJECTION[version]
    except KeyError as exc:
        raise RuntimeError(
            f"unsupported canonical source projection version: {version or '<empty>'}"
        ) from exc
WATCH_HORIZON_TRADING_DAYS = 60
HOLDING_DAYS = 30
NO_STOP_POLICY_ID = "none_no_stop_reference"
CANONICAL_LINEAGE_VERSION = "canonical_json_numeric_text_v1"
MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
HOLDING_SESSION_INDEX_OFFSET = HOLDING_DAYS - 1
HOLDING_SESSION_CONTRACT = "inclusive_entry_session_count_30_exit_offset_29"
PRODUCER_RELATIVE_PATH = (
    "scripts/revenue_unreacted_range_low_mid_falling_candidate_audit.py"
)
SOURCE_FIRST_PRODUCER_RELATIVE_PATH = (
    "scripts/revenue_unreacted_range_source_first_condition_audit.py"
)
REARMED_PRODUCER_RELATIVE_PATH = (
    "scripts/revenue_unreacted_range_rearmed_operation_grid.py"
)
POSITION_SHAPE_PRODUCER_RELATIVE_PATH = (
    "scripts/revenue_unreacted_range_position_shape_transition_matrix.py"
)
DATA_SHARING_REGISTRY_RELATIVE_PATH = "config/daily_model_data_sharing_registry.csv"
BACKGROUND_REGISTRY_RELATIVE_PATH = "config/daily_model_background_data_registry.csv"
BACKGROUND_CONTRACT_FIELDS = (
    "data_family_id",
    "scope",
    "owner_lane",
    "producer",
    "artifact_path",
    "source_artifacts",
    "consumer_surfaces",
    "consumer_models",
    "point_in_time_status",
    "allowed_use",
    "forbidden_use",
    "validator",
    "retention_policy",
    "cleanup_status",
    "notes",
)
PRICE_CANONICAL_COLUMNS = (
    "date",
    "analysis_open",
    "analysis_high",
    "analysis_low",
    "analysis_close",
)

PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = (
    "excluding_unresolved_anomaly_candidates_sensitivity"
)
ANALYSIS_BASES = (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS)
LIFECYCLE_POLICY_IDS = (
    "rearm_after_realized_exit_next_trade_day",
    "episode_first_match_once",
)
CONFIRMATION_VARIANT_IDS = (
    "base_close_confirmed",
    "delayed_next_close_continuation_bonus",
)
VARIANT_SPECS = (
    (10, "source_mid_falling", "mid_falling_member"),
    (20, "source_low_falling", "low_falling_member"),
    (30, "source_low_or_mid_falling_union", "low_or_mid_falling_union_member"),
)
FEATURE_SPECS = (
    (10, "source_position_120d_pct"),
    (20, "source_shape_return20_pct"),
    (30, "source_shape_range23_pct"),
    (40, "source_shape_ema23_slope5_pct"),
    (50, "latest_source_to_trigger_trading_days"),
)

FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
POSITION_POLICY = (
    "anchor adjusted close positioned within the adjusted analysis-high/analysis-low "
    "range of exactly 120 prior trading sessions, excluding the anchor"
)
SHAPE_POLICY = (
    "revenue-model-owned descriptive shape: adjusted close return from t-20 to anchor; "
    "adjusted-close range across the 23 sessions ending at anchor; EMA23 through anchor "
    "with five-session slope"
)
ANOMALY_POLICY = (
    "primary retains unresolved source price-path and operation-return review candidates; "
    "candidate exclusion is sensitivity only"
)
SAMPLE_POLICY = "sample_count_disclosed_not_used_as_automatic_rejection"
NON_OVERLAP_POLICY = (
    "same-stock entry must be after the prior realized exit within each lifecycle and "
    "confirmation variant"
)
PROMOTION_READINESS = "research_only_pending_holdout_validation"

SOURCE_RELATIVE_PATHS = {
    "projection_manifest": (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
    ),
    "source_first": (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
    ),
    "rearmed": (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_rearmed_operation_grid_detail_latest.csv"
    ),
    "price_dir": "data/stock_price_history",
    "resolution": "config/revenue_unreacted_range_price_comparability_resolution.csv",
}
ARTIFACT_RELATIVE_PATHS = {
    "summary": f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv",
    "detail": f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv",
    "paired": (
        f"output/latest/research_backtest/{ARTIFACT_ID}_paired_confirmation_latest.csv"
    ),
    "contrast": (
        f"output/latest/research_backtest/{ARTIFACT_ID}_feature_contrast_latest.csv"
    ),
    "markdown": f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md",
    "summary_history": f"output/history/research/{ARTIFACT_ID}.csv",
    "detail_history": f"output/history/research/{ARTIFACT_ID}_detail.csv",
    "paired_history": (
        f"output/history/research/{ARTIFACT_ID}_paired_confirmation.csv"
    ),
    "contrast_history": (
        f"output/history/research/{ARTIFACT_ID}_feature_contrast.csv"
    ),
    "summary_docs": f"docs/latest/{ARTIFACT_ID}_latest.csv",
    "detail_docs": f"docs/latest/{ARTIFACT_ID}_detail_latest.csv",
    "paired_docs": f"docs/latest/{ARTIFACT_ID}_paired_confirmation_latest.csv",
    "contrast_docs": f"docs/latest/{ARTIFACT_ID}_feature_contrast_latest.csv",
    "markdown_docs": f"docs/latest/{ARTIFACT_ID}_latest.md",
}


def _git(
    *args: str,
    input_bytes: bytes | None = None,
) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "--no-replace-objects", "-C", str(ROOT), *args],
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def _safe_repo_path(relative_path: str) -> str:
    if not relative_path or "\\" in relative_path or "\0" in relative_path:
        raise RuntimeError(f"trusted v1 unsafe Git path: {relative_path!r}")
    path = PurePosixPath(relative_path)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise RuntimeError(f"trusted v1 unsafe Git path: {relative_path!r}")
    normalized = path.as_posix()
    if normalized != relative_path:
        raise RuntimeError(f"trusted v1 unsafe Git path: {relative_path!r}")
    return normalized


def _trusted_stock_path(stock_id: object) -> str:
    normalized = str(stock_id).strip()
    if re.fullmatch(r"\d{4,6}", normalized) is None:
        raise RuntimeError(f"trusted v1 unsafe stock id: {stock_id!r}")
    return f"{SOURCE_RELATIVE_PATHS['price_dir']}/{normalized}.csv"


def _trusted_revision_preflight(
    revision: str = TRUSTED_SOURCE_REVISION,
) -> None:
    if re.fullmatch(r"[0-9a-f]{40}", revision) is None:
        raise RuntimeError(
            "trusted v1 revision is not a lowercase 40-character SHA: "
            f"{revision}"
        )
    resolved = _git("rev-parse", "--verify", f"{revision}^{{commit}}")
    if resolved.returncode != 0:
        detail = resolved.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"trusted v1 commit is unavailable: {revision}: {detail}")
    try:
        observed = resolved.stdout.decode("ascii", errors="strict").strip()
    except UnicodeDecodeError as exc:
        raise RuntimeError("trusted v1 commit identity is not ASCII") from exc
    if observed != revision:
        raise RuntimeError(
            "trusted v1 revision does not resolve to its exact SHA: "
            f"{observed} != {revision}"
        )
    object_type = _git("cat-file", "-t", revision)
    if object_type.returncode != 0 or object_type.stdout.strip() != b"commit":
        raise RuntimeError(f"trusted v1 revision is not a readable commit: {revision}")
    ancestor = _git("merge-base", "--is-ancestor", revision, "HEAD")
    if ancestor.returncode != 0:
        detail = ancestor.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            f"trusted v1 revision is not an ancestor of HEAD: {revision}: {detail}"
        )


def _trusted_tree(revision: str = TRUSTED_SOURCE_REVISION) -> dict[str, tuple[str, str, str]]:
    cached = _TRUSTED_TREE_CACHE.get(revision)
    if cached is not None:
        return cached
    result = _git("ls-tree", "-r", "-z", revision)
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"trusted v1 Git tree is unreadable: {revision}: {detail}")
    entries: dict[str, tuple[str, str, str]] = {}
    for raw_entry in result.stdout.split(b"\0"):
        if not raw_entry:
            continue
        try:
            metadata, raw_path = raw_entry.split(b"\t", 1)
            mode, object_type, oid = metadata.decode("ascii", errors="strict").split(" ")
            repo_path = raw_path.decode("utf-8", errors="strict")
        except (ValueError, UnicodeDecodeError) as exc:
            raise RuntimeError("trusted v1 Git tree contains malformed metadata") from exc
        entries[repo_path] = (mode, object_type, oid)
    _TRUSTED_TREE_CACHE[revision] = entries
    return entries


def _trusted_blobs(
    relative_paths: set[str],
    *,
    revision: str = TRUSTED_SOURCE_REVISION,
) -> dict[str, bytes]:
    normalized_paths = {_safe_repo_path(path) for path in relative_paths}
    missing_paths = sorted(
        path for path in normalized_paths if (revision, path) not in _TRUSTED_BLOB_CACHE
    )
    if missing_paths:
        tree = _trusted_tree(revision)
        oids: list[str] = []
        for path in missing_paths:
            entry = tree.get(path)
            if entry is None:
                raise RuntimeError(f"trusted v1 Git blob is missing: {revision}:{path}")
            mode, object_type, oid = entry
            if (
                mode != "100644"
                or object_type != "blob"
                or re.fullmatch(r"[0-9a-f]{40}", oid) is None
            ):
                raise RuntimeError(
                    f"trusted v1 Git path is not a regular readable blob: {path}"
                )
            oids.append(oid)
        result = _git(
            "cat-file",
            "--batch",
            input_bytes=("\n".join(oids) + "\n").encode("ascii"),
        )
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(f"trusted v1 Git blobs are unreadable: {detail}")
        cursor = 0
        for path, expected_oid in zip(missing_paths, oids):
            newline = result.stdout.find(b"\n", cursor)
            if newline < 0:
                raise RuntimeError(f"trusted v1 Git blob header is missing: {path}")
            try:
                header = result.stdout[cursor:newline].decode("ascii", errors="strict").split(" ")
            except UnicodeDecodeError as exc:
                raise RuntimeError(f"trusted v1 Git blob header is invalid: {path}") from exc
            if len(header) != 3 or header[0] != expected_oid or header[1] != "blob":
                raise RuntimeError(f"trusted v1 Git blob header drift: {path}")
            try:
                size = int(header[2])
            except ValueError as exc:
                raise RuntimeError(f"trusted v1 Git blob size is invalid: {path}") from exc
            start = newline + 1
            end = start + size
            if end >= len(result.stdout) or result.stdout[end : end + 1] != b"\n":
                raise RuntimeError(f"trusted v1 Git blob payload is truncated: {path}")
            _TRUSTED_BLOB_CACHE[(revision, path)] = result.stdout[start:end]
            cursor = end + 1
        if cursor != len(result.stdout):
            raise RuntimeError("trusted v1 Git blob batch contains trailing bytes")
    return {
        path: _TRUSTED_BLOB_CACHE[(revision, path)] for path in normalized_paths
    }


def _read_csv_payload(payload: bytes, *, label: str, **kwargs: object) -> pd.DataFrame:
    try:
        return pd.read_csv(BytesIO(payload), **kwargs)
    except (UnicodeDecodeError, pd.errors.EmptyDataError, pd.errors.ParserError, ValueError) as exc:
        raise RuntimeError(f"trusted v1 CSV is unreadable: {label}: {exc}") from exc


def _validate_v1_manifest_descriptor(manifest: pd.DataFrame) -> None:
    if len(manifest) != 1:
        raise RuntimeError("trusted v1 projection manifest must contain exactly one row")
    missing = sorted(set(EXPECTED_V1_MANIFEST_DESCRIPTOR) - set(manifest.columns))
    if missing:
        raise RuntimeError(f"trusted v1 projection manifest is missing columns: {missing}")
    row = manifest.iloc[0]
    drift = {
        column: (str(row[column]), expected)
        for column, expected in EXPECTED_V1_MANIFEST_DESCRIPTOR.items()
        if str(row[column]) != expected
    }
    if drift:
        raise RuntimeError(f"trusted v1 projection manifest descriptor drift: {drift}")
    for column in (
        "cutoff_date",
        "projected_max_source_date",
        "projected_max_trade_date",
        "projected_max_episode_end_date",
    ):
        value = str(row[column])
        if re.fullmatch(r"\d{8}", value) is None or value > PRICE_HISTORY_CUTOFF_DATE:
            raise RuntimeError(
                f"trusted v1 projection manifest date/cutoff drift: {column}={value}"
            )


def _validate_trusted_date_values(
    frame: pd.DataFrame,
    columns: tuple[str, ...],
    *,
    label: str,
    pipe_delimited: bool = False,
) -> None:
    for column in columns:
        if column not in frame.columns:
            raise RuntimeError(f"trusted v1 {label} is missing date column: {column}")
        values = frame[column].astype(str).str.strip()
        if pipe_delimited:
            values = values.str.split("|").explode().astype(str).str.strip()
        if values.empty or not values.str.fullmatch(r"\d{8}").all():
            raise RuntimeError(f"trusted v1 {label} has invalid date: {column}")
        if values.gt(PRICE_HISTORY_CUTOFF_DATE).any():
            raise RuntimeError(f"trusted v1 {label} exceeds cutoff: {column}")


def _stock_id(value: object) -> str:
    text = str(value or "").strip()
    return text[:-2] if text.endswith(".0") and text[:-2].isdigit() else text


def _date_text(value: object) -> str:
    text = "".join(character for character in str(value or "") if character.isdigit())
    return text[:8] if len(text) >= 8 else ""


def _bool_value(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _same_number(
    observed: object,
    expected: object,
    *,
    tolerance: float = 0.00011,
) -> bool:
    observed_number = _number(observed)
    expected_number = _number(expected)
    if expected_number is None:
        return observed_number is None
    return observed_number is not None and math.isclose(
        observed_number, expected_number, abs_tol=tolerance
    )


def _split(value: object) -> list[str]:
    return [part.strip() for part in str(value).split("|") if part.strip()]


def _strict_integral(value: object, *, label: str) -> int:
    text = str(value).strip()
    try:
        number = Decimal(text)
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"{label} is not numeric: {text!r}") from exc
    if not number.is_finite() or number != number.to_integral_value():
        raise ValueError(f"{label} is not an integer: {text!r}")
    return int(number)


def _canonical_numeric_text(text: str) -> str | None:
    candidate = text.strip()
    if not re.fullmatch(
        r"[+-]?(?:(?:\d+(?:\.\d*)?)|(?:\.\d+))(?:[eE][+-]?\d+)?",
        candidate,
    ):
        return None
    unsigned = candidate.lstrip("+-")
    mantissa = re.split(r"[eE]", unsigned, maxsplit=1)[0]
    integer_part = mantissa.split(".", maxsplit=1)[0]
    if len(integer_part) > 1 and integer_part.startswith("0"):
        return None
    try:
        number = Decimal(candidate)
    except InvalidOperation:
        return None
    if not number.is_finite():
        return None
    if number == 0:
        return "0"
    rendered = format(number.normalize(), "f")
    return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered


def _canonical_value(value: object) -> str:
    if value is None or (
        not isinstance(value, (str, bytes)) and pd.isna(value)
    ):
        return ""
    if isinstance(value, (bool, np.bool_)):
        return "true" if bool(value) else "false"
    if isinstance(value, (numbers.Integral, numbers.Real, Decimal)):
        number = float(value)
        if not np.isfinite(number):
            return ""
        numeric = _canonical_numeric_text(str(value))
        if numeric is None:
            raise RuntimeError(f"canonical numeric value is invalid: {value!r}")
        return numeric
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    numeric = _canonical_numeric_text(text)
    return numeric if numeric is not None else text


def _require_sha256(value: object, *, label: str) -> str:
    digest = str(value).strip().lower()
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise RuntimeError(f"{label} is not a canonical SHA-256")
    return digest


def _canonical_mapping_sha256(
    values: dict[str, object],
    *,
    excluded_columns: frozenset[str] = frozenset({"generated_at"}),
) -> str:
    payload = [
        [str(column), _canonical_value(value)]
        for column, value in sorted(values.items(), key=lambda item: str(item[0]))
        if str(column) not in excluded_columns
    ]
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _canonical_table_sha256(
    frame: pd.DataFrame,
    *,
    excluded_columns: frozenset[str] = frozenset({"generated_at"}),
) -> str:
    columns = sorted(
        str(column)
        for column in frame.columns
        if str(column) not in excluded_columns
    )
    rows = sorted(
        [
            [_canonical_value(row[column]) for column in columns]
            for _, row in frame.loc[:, columns].iterrows()
        ]
    )
    payload = {
        "canonical_lineage_version": CANONICAL_LINEAGE_VERSION,
        "columns": columns,
        "rows": rows,
    }
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _projection_payload_value(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    if isinstance(value, (bool, np.bool_)):
        return "true" if bool(value) else "false"
    text = str(value).strip()
    return text.lower() if text.lower() in {"true", "false"} else text


def _projection_detail_semantic_sha256(frame: pd.DataFrame) -> str:
    columns = [
        column
        for column in frame.columns
        if column not in {"generated_at", *PROJECTION_CAPTURE_LINEAGE_COLUMNS}
    ]
    rows = [
        [_projection_payload_value(value) for value in row]
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    ]
    rows.sort()
    payload = [PROJECTION_CANONICAL_JSON_VERSION, columns, rows]
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _projection_constant(frame: pd.DataFrame, column: str) -> str:
    if column not in frame.columns:
        raise RuntimeError(f"projected detail is missing column: {column}")
    values = sorted({_projection_payload_value(value) for value in frame[column]})
    if len(values) != 1 or not values[0]:
        raise RuntimeError(
            f"projected detail must have one non-empty {column}: {values}"
        )
    return values[0]


def _projection_date_token(value: object, *, column: str) -> str:
    text = _projection_payload_value(value)
    exact = re.fullmatch(r"\d{8}", text)
    if exact:
        return text
    numeric_export = re.fullmatch(r"(\d{8})\.0+", text)
    if numeric_export:
        return numeric_export.group(1)
    raise RuntimeError(
        f"projected detail {column} must contain exactly eight digits: {text!r}"
    )


def _projection_max_date(frame: pd.DataFrame, columns: tuple[str, ...]) -> str:
    tokens: list[str] = []
    for column in columns:
        if column not in frame.columns:
            raise RuntimeError(f"projected detail is missing date column: {column}")
        for value in frame[column]:
            for token in _projection_payload_value(value).split("|"):
                if token.strip():
                    tokens.append(_projection_date_token(token, column=column))
    return max(tokens, default="")


def _projection_binding_errors(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
) -> list[str]:
    errors: list[str] = []
    columns = tuple(manifest.columns)
    if columns not in (
        V1_PROJECTION_MANIFEST_COLUMNS,
        V2_PROJECTION_MANIFEST_COLUMNS,
    ):
        return ["projection manifest schema mismatch"]
    if len(manifest) != 1:
        return [f"projection manifest must have exactly one row: {len(manifest)}"]
    row = manifest.iloc[0]
    version = _projection_payload_value(row["projection_version"])
    if version == V1_PROJECTION_VERSION:
        expected_policy = V1_PROJECTION_POLICY_ID
        if columns != V1_PROJECTION_MANIFEST_COLUMNS:
            errors.append("v1 projection manifest schema mismatch")
    elif version == V2_PROJECTION_VERSION:
        expected_policy = V2_PROJECTION_POLICY_ID
        if columns != V2_PROJECTION_MANIFEST_COLUMNS:
            errors.append("v2 projection manifest schema mismatch")
        for column, expected in {
            "predecessor_projection_version": V1_PROJECTION_VERSION,
            "predecessor_manifest_bytes_sha256": V1_PREDECESSOR_MANIFEST_SHA256,
            "predecessor_detail_bytes_sha256": V1_PREDECESSOR_DETAIL_SHA256,
            "lineage_change_reason": V2_LINEAGE_CHANGE_REASON,
            "candidate_status": V2_CANDIDATE_STATUS,
        }.items():
            if _projection_payload_value(row[column]) != expected:
                errors.append(f"projection manifest {column} mismatch")
    else:
        expected_policy = ""
        errors.append(f"unsupported projection version: {version}")
    for column, expected in {
        "model_id": MODEL_ID,
        "artifact_id": PROJECTION_ARTIFACT_ID,
        "artifact_version": version,
        "projection_id": PROJECTION_ID,
        "projection_version": version,
        "projection_policy_id": expected_policy,
        "cutoff_date": PRICE_HISTORY_CUTOFF_DATE,
        "full_source_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
    }.items():
        if _projection_payload_value(row[column]) != expected:
            errors.append(f"projection manifest {column} mismatch")
    try:
        if _projection_constant(projected_detail, "artifact_id") != _projection_payload_value(
            row["full_source_artifact_id"]
        ):
            errors.append("projected detail artifact_id binding mismatch")
        if _projection_constant(
            projected_detail, "artifact_version"
        ) != _projection_payload_value(row["full_source_artifact_version"]):
            errors.append("projected detail artifact_version binding mismatch")
        if len(projected_detail) != int(row["projected_episode_row_count"]):
            errors.append("projected detail row-count binding mismatch")
        if _projection_detail_semantic_sha256(
            projected_detail
        ) != _projection_payload_value(row["projected_episode_semantic_sha256"]):
            errors.append("projected detail semantic SHA-256 binding mismatch")
        for detail_column, manifest_column in (
            ("monthly_revenue_history_blob_sha256", "monthly_revenue_history_blob_sha256"),
            ("monthly_revenue_canonical_table_sha256", "cutoff_revenue_subset_semantic_sha256"),
            (
                "cross_market_resolution_registry_canonical_sha256",
                "cross_market_resolution_registry_canonical_sha256",
            ),
        ):
            if _projection_constant(
                projected_detail, detail_column
            ) != _projection_payload_value(row[manifest_column]):
                errors.append(f"projected detail {detail_column} lineage mismatch")
        maxima = (
            _projection_max_date(
                projected_detail,
                (
                    "episode_start_source_date",
                    "latest_qualifying_source_date",
                    "qualifying_source_dates",
                ),
            ),
            _projection_max_date(
                projected_detail,
                (
                    "episode_start_trade_date",
                    "latest_qualifying_trade_date",
                    "qualifying_trade_dates",
                ),
            ),
            _projection_max_date(projected_detail, ("episode_end_date",)),
        )
        for column, actual in zip(
            (
                "projected_max_source_date",
                "projected_max_trade_date",
                "projected_max_episode_end_date",
            ),
            maxima,
        ):
            if _projection_payload_value(row[column]) != actual:
                errors.append(f"projected detail {column} binding mismatch")
            if actual and actual > PRICE_HISTORY_CUTOFF_DATE:
                errors.append(f"projected detail {column} exceeds cutoff")
    except (RuntimeError, TypeError, ValueError) as exc:
        errors.append(str(exc))
    if _projection_payload_value(row["research_only"]) != "true":
        errors.append("research_only must be true")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if _projection_payload_value(row[column]) != "false":
            errors.append(f"{column} must be false")
    return errors


def _canonical_frame_sha256(frame: pd.DataFrame) -> str:
    missing = sorted(set(PRICE_CANONICAL_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(f"canonical price history is missing columns: {missing}")
    canonical = frame.loc[:, list(PRICE_CANONICAL_COLUMNS)].copy()
    canonical["date"] = canonical["date"].map(_date_text)
    canonical = canonical.loc[
        canonical["date"].str.fullmatch(r"\d{8}")
        & canonical["date"].le(PRICE_HISTORY_CUTOFF_DATE)
    ].sort_values("date", kind="mergesort").reset_index(drop=True)
    if canonical.empty or canonical["date"].duplicated().any():
        raise RuntimeError("canonical price history is empty or date-duplicated")
    columns = list(PRICE_CANONICAL_COLUMNS)
    rows = [
        [[column, _canonical_value(row[column])] for column in columns]
        for _, row in canonical.loc[:, columns].iterrows()
    ]
    payload = {
        "canonical_lineage_version": CANONICAL_LINEAGE_VERSION,
        "columns": columns,
        "rows": rows,
    }
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _source_payload(
    source_root: Path,
    relative_path: str,
    *,
    trusted_revision: str | None = None,
) -> bytes:
    if trusted_revision is not None:
        return _trusted_blobs(
            {_safe_repo_path(relative_path)},
            revision=trusted_revision,
        )[_safe_repo_path(relative_path)]
    path = source_root / relative_path
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"lineage source is missing or unsafe: {path}")
    return path.read_bytes()

def _normalized_file_sha256(
    source_root: Path,
    relative_path: str,
    *,
    trusted_revision: str | None = None,
) -> str:
    payload = _source_payload(
        source_root,
        relative_path,
        trusted_revision=trusted_revision,
    ).replace(b"\r\n", b"\n")
    return hashlib.sha256(payload).hexdigest()

def _registered_data_contract_sha256(
    source_root: Path,
    *,
    trusted_revision: str | None = None,
) -> str:
    registry_payload = _source_payload(
        source_root,
        DATA_SHARING_REGISTRY_RELATIVE_PATH,
        trusted_revision=trusted_revision,
    )
    if trusted_revision is not None:
        registry = _read_csv_payload(
            registry_payload,
            label=DATA_SHARING_REGISTRY_RELATIVE_PATH,
            keep_default_na=False,
            low_memory=False,
        )
    else:
        registry = pd.read_csv(
            BytesIO(registry_payload), keep_default_na=False, low_memory=False
        )
    required = {
        "data_family_id",
        "ownership_mode",
        "owner_model_or_family",
        "registered_producers",
        "producer_write_scope",
        "consumer_access_mode",
        "approved_consumer_models",
        "data_contract_sha256",
    }
    missing = sorted(required - set(registry.columns))
    if missing:
        raise RuntimeError(f"data-sharing registry is missing columns: {missing}")
    rows = registry.loc[registry["data_family_id"].astype(str).eq(ARTIFACT_ID)]
    if len(rows) != 1:
        raise RuntimeError(
            f"data-sharing registry must contain exactly one {ARTIFACT_ID} row"
        )
    row = rows.iloc[0]
    expected = {
        "ownership_mode": "model_owned_not_shared",
        "owner_model_or_family": MODEL_ID,
        "registered_producers": "scripts/build_revenue_unreacted_range_research.py",
        "producer_write_scope": ARTIFACT_RELATIVE_PATHS["summary"],
        "consumer_access_mode": "owner_model_research_only",
        "approved_consumer_models": MODEL_ID,
    }
    drift = [column for column, value in expected.items() if str(row[column]) != value]
    if drift:
        raise RuntimeError(f"data-sharing registry governance drift: {drift}")
    digest = str(row["data_contract_sha256"]).strip().lower()
    if len(digest) != 64 or any(character not in "0123456789abcdef" for character in digest):
        raise RuntimeError("registered data contract is not a canonical SHA-256")
    if digest != EXPECTED_DATA_CONTRACT_SHA256:
        raise RuntimeError(
            "registered low/mid falling data contract SHA-256 drift: "
            f"observed={digest}; expected={EXPECTED_DATA_CONTRACT_SHA256}"
        )

    background_payload = _source_payload(
        source_root,
        BACKGROUND_REGISTRY_RELATIVE_PATH,
        trusted_revision=trusted_revision,
    )
    if trusted_revision is not None:
        background = _read_csv_payload(
            background_payload,
            label=BACKGROUND_REGISTRY_RELATIVE_PATH,
            keep_default_na=False,
            low_memory=False,
        )
    else:
        background = pd.read_csv(
            BytesIO(background_payload), keep_default_na=False, low_memory=False
        )
    missing_background = sorted(set(BACKGROUND_CONTRACT_FIELDS) - set(background.columns))
    if missing_background:
        raise RuntimeError(
            f"background data registry is missing columns: {missing_background}"
        )
    background_rows = background.loc[
        background["data_family_id"].astype(str).eq(ARTIFACT_ID)
    ]
    if len(background_rows) != 1:
        raise RuntimeError(
            f"background data registry must contain exactly one {ARTIFACT_ID} row"
        )
    background_row = background_rows.iloc[0]
    payload = "\n".join(
        f"{field}={background_row[field]}" for field in BACKGROUND_CONTRACT_FIELDS
    )
    computed = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    if computed != digest:
        raise RuntimeError(
            "background data contract SHA-256 drift from data-sharing registry pin: "
            f"computed={computed}; registered={digest}"
        )
    return computed


def _lineage_set_sha256(frame: pd.DataFrame, column: str) -> str:
    values = sorted(set(frame[column].astype(str).str.strip().str.lower()))
    if not values or any(
        len(value) != 64 or any(character not in "0123456789abcdef" for character in value)
        for value in values
    ):
        raise RuntimeError(f"invalid canonical lineage SHA-256 set: {column}")
    payload = json.dumps(
        values,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator * 100.0 if denominator else None


def _stat(values: pd.Series, method: str) -> float | None:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return None
    if method == "mean":
        return float(numeric.mean())
    if method == "median":
        return float(numeric.median())
    if method == "p10":
        return float(numeric.quantile(0.10))
    if method == "p90":
        return float(numeric.quantile(0.90))
    if method == "min":
        return float(numeric.min())
    if method == "max":
        return float(numeric.max())
    raise ValueError(method)


def _top_abs_share(values: pd.Series, count: int) -> float | None:
    numeric = pd.to_numeric(values, errors="coerce").dropna().abs()
    denominator = float(numeric.sum())
    if numeric.empty or denominator <= 0:
        return None
    return float(numeric.nlargest(count).sum()) / denominator * 100.0


def _standardized_mean_difference(
    high: pd.Series, low: pd.Series
) -> float | None:
    a = pd.to_numeric(high, errors="coerce").dropna()
    b = pd.to_numeric(low, errors="coerce").dropna()
    if len(a) < 2 or len(b) < 2:
        return None
    denominator = len(a) + len(b) - 2
    variance = (
        (len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)
    ) / denominator
    if not np.isfinite(variance) or variance <= 0:
        return None
    return float((a.mean() - b.mean()) / math.sqrt(variance))


def _load_resolutions(
    path: Path,
    *,
    trusted_revision: str | None = None,
) -> pd.DataFrame:
    columns = ["stock_id", "resume_date", "exchange_ratio", "resolution_id"]
    if trusted_revision is not None:
        relative = SOURCE_RELATIVE_PATHS["resolution"]
        payload = _trusted_blobs({relative}, revision=trusted_revision)[relative]
        frame = _read_csv_payload(
            payload,
            label=relative,
            dtype={"stock_id": str},
            keep_default_na=False,
        )
    else:
        if not path.is_file():
            return pd.DataFrame(columns=columns)
        frame = pd.read_csv(path, dtype={"stock_id": str}, keep_default_na=False)
    required = {*columns, "root_cause_status"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"price resolution is missing columns: {missing}")
    frame = frame.loc[
        frame["root_cause_status"].astype(str).eq(
            "verified_non_comparable_raw_price_scale"
        )
    ].copy()
    frame["stock_id"] = frame["stock_id"].map(_stock_id)
    if trusted_revision is not None:
        raw_dates = frame["resume_date"].astype(str).str.strip()
        if (
            not raw_dates.str.fullmatch(r"\d{8}").all()
            or raw_dates.gt(PRICE_HISTORY_CUTOFF_DATE).any()
        ):
            raise RuntimeError("trusted v1 price resolution date/cutoff drift")
        frame["resume_date"] = raw_dates
    else:
        frame["resume_date"] = frame["resume_date"].map(_date_text)
    frame["exchange_ratio"] = pd.to_numeric(
        frame["exchange_ratio"], errors="coerce"
    )
    if frame["exchange_ratio"].isna().any() or frame["exchange_ratio"].le(0).any():
        raise RuntimeError("price resolution exchange ratio is invalid")
    return frame


def _load_adjusted_price(
    stock_id: str,
    price_dir: Path,
    resolutions: pd.DataFrame,
    *,
    trusted_revision: str | None = None,
) -> pd.DataFrame:
    if trusted_revision is not None:
        relative = _trusted_stock_path(stock_id)
        payload = _trusted_blobs({relative}, revision=trusted_revision)[relative]
        frame = _read_csv_payload(payload, label=relative, low_memory=False)
    else:
        path = price_dir / f"{stock_id}.csv"
        if not path.is_file():
            raise RuntimeError(f"price history is missing: {path}")
        frame = pd.read_csv(path, low_memory=False)
    required = {"date", "open", "high", "low", "close"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"price history {stock_id} is missing columns: {missing}")
    if trusted_revision is not None:
        raw_dates = frame["date"].astype(str).str.strip()
        if raw_dates.empty or not raw_dates.str.fullmatch(r"\d{8}").all():
            raise RuntimeError(f"trusted v1 price history has invalid dates: {stock_id}")
        frame["date"] = raw_dates
    else:
        frame["date"] = frame["date"].map(_date_text)
    frame = frame.loc[
        frame["date"].str.fullmatch(r"\d{8}")
        & frame["date"].le(PRICE_HISTORY_CUTOFF_DATE)
    ].copy()
    if trusted_revision is not None and frame["date"].duplicated().any():
        raise RuntimeError(f"trusted v1 price history has duplicate dates: {stock_id}")
    frame = frame.sort_values("date", kind="mergesort").drop_duplicates(
        "date", keep="last"
    )
    for column in ("open", "high", "low", "close"):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.dropna(subset=["close"]).reset_index(drop=True)
    frame["adjustment_factor"] = 1.0
    for event in resolutions.loc[resolutions["stock_id"].eq(stock_id)].itertuples(
        index=False
    ):
        frame.loc[frame["date"].lt(str(event.resume_date)), "adjustment_factor"] *= (
            1.0 / float(event.exchange_ratio)
        )
    for column in ("open", "high", "low", "close"):
        frame[f"analysis_{column}"] = frame[column] * frame["adjustment_factor"]
    frame["analysis_ema23"] = frame["analysis_close"].ewm(
        span=23, adjust=False, min_periods=23
    ).mean()
    frame["sequence_index"] = np.arange(len(frame), dtype=int)
    if frame.empty or frame["date"].duplicated().any():
        raise RuntimeError(f"adjusted price history is empty or duplicated: {stock_id}")
    return frame


def _anchor_features(price: pd.DataFrame, index: int) -> dict[str, object]:
    close = _number(price.at[index, "analysis_close"])
    close_value = float(close) if close is not None else math.nan
    prior = price.iloc[max(0, index - 120) : index]
    prior_high = pd.to_numeric(prior["analysis_high"], errors="coerce")
    prior_low = pd.to_numeric(prior["analysis_low"], errors="coerce")
    position_observed = bool(
        len(prior) == 120
        and prior_high.notna().all()
        and prior_low.notna().all()
        and np.isfinite(close_value)
    )
    high = float(prior_high.max()) if position_observed else math.nan
    low = float(prior_low.min()) if position_observed else math.nan
    position_observed = bool(
        position_observed
        and np.isfinite(high)
        and np.isfinite(low)
        and high > low
    )
    position = (
        (close_value - low) / (high - low) * 100.0
        if position_observed
        else math.nan
    )
    if not position_observed:
        position_bucket = "insufficient_history"
    elif position <= 40:
        position_bucket = "low_pos_le40"
    elif position <= 75:
        position_bucket = "mid_pos_40_75"
    else:
        position_bucket = "high_pos_gt75"

    return20 = math.nan
    range23 = math.nan
    ema_slope5 = math.nan
    if index >= 20:
        close20 = _number(price.at[index - 20, "analysis_close"])
        if close20 is not None and close20 > 0 and np.isfinite(close_value):
            return20 = (close_value / close20 - 1.0) * 100.0
    recent = pd.to_numeric(
        price.iloc[max(0, index - 22) : index + 1]["analysis_close"],
        errors="coerce",
    )
    if len(recent) == 23 and recent.notna().all() and float(recent.min()) > 0:
        range23 = (float(recent.max()) / float(recent.min()) - 1.0) * 100.0
    if index >= 5:
        ema_now = _number(price.at[index, "analysis_ema23"])
        ema_prior = _number(price.at[index - 5, "analysis_ema23"])
        if ema_now is not None and ema_prior is not None and ema_prior > 0:
            ema_slope5 = (ema_now / ema_prior - 1.0) * 100.0
    shape_observed = bool(
        np.isfinite(return20) and np.isfinite(range23) and np.isfinite(ema_slope5)
    )
    if not shape_observed:
        shape_bucket = "insufficient_history"
    elif return20 > 5 and ema_slope5 > 0:
        shape_bucket = "rising"
    elif return20 < -5 and ema_slope5 < 0:
        shape_bucket = "falling"
    elif abs(return20) <= 5 and range23 <= 15:
        shape_bucket = "consolidation"
    else:
        shape_bucket = "mixed_or_turn"
    classification_observed = position_observed and shape_observed
    cell_id = (
        f"{position_bucket}__{shape_bucket}"
        if classification_observed
        else "insufficient_history"
    )
    return {
        "source_position_120d_pct": round(position, 4) if np.isfinite(position) else "",
        "source_shape_return20_pct": (
            round(return20, 4) if np.isfinite(return20) else ""
        ),
        "source_shape_range23_pct": (
            round(range23, 4) if np.isfinite(range23) else ""
        ),
        "source_shape_ema23_slope5_pct": (
            round(ema_slope5, 4) if np.isfinite(ema_slope5) else ""
        ),
        "source_position_bucket": position_bucket,
        "source_shape_bucket": shape_bucket,
        "source_position_shape_cell_id": cell_id,
        "source_classification_observed": classification_observed,
    }


def _read_sources(
    source_root: Path,
    *,
    projection_version: str = V1_PROJECTION_VERSION,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    _version_contract(projection_version)
    if source_root.resolve() == ROOT and projection_version == V1_PROJECTION_VERSION:
        revision = TRUSTED_SOURCE_REVISION
        _trusted_revision_preflight(revision)
        relative_paths = {
            name: SOURCE_RELATIVE_PATHS[name]
            for name in ("projection_manifest", "source_first", "rearmed")
        }
        payloads = _trusted_blobs(set(relative_paths.values()), revision=revision)
        source = _read_csv_payload(
            payloads[relative_paths["source_first"]],
            label=relative_paths["source_first"],
            dtype={"stock_id": str},
            keep_default_na=False,
            low_memory=False,
        )
        rearmed = _read_csv_payload(
            payloads[relative_paths["rearmed"]],
            label=relative_paths["rearmed"],
            dtype={"stock_id": str},
            keep_default_na=False,
            low_memory=False,
        )
        projection_manifest = _read_csv_payload(
            payloads[relative_paths["projection_manifest"]],
            label=relative_paths["projection_manifest"],
            dtype=str,
            keep_default_na=False,
        )
        _validate_v1_manifest_descriptor(projection_manifest)
        _validate_trusted_date_values(
            source,
            (
                "episode_start_source_date",
                "episode_start_canonical_source_table_date",
                "episode_start_trade_date",
                "latest_qualifying_source_date",
                "latest_qualifying_canonical_source_table_date",
                "latest_qualifying_trade_date",
                "episode_end_date",
            ),
            label="source-first detail",
        )
        _validate_trusted_date_values(
            source,
            (
                "qualifying_source_dates",
                "qualifying_canonical_source_table_dates",
                "qualifying_trade_dates",
            ),
            label="source-first detail",
            pipe_delimited=True,
        )
        rearmed_slice_columns = {
            "lifecycle_policy_id",
            "confirmation_variant_id",
            "holding_days",
            "stop_policy_id",
            "return_valid",
        }
        if not rearmed_slice_columns.issubset(rearmed.columns):
            raise RuntimeError(
                "trusted v1 rearmed detail is missing selected-slice columns"
            )
        rearmed_dates = rearmed.loc[
            rearmed["lifecycle_policy_id"].astype(str).isin(LIFECYCLE_POLICY_IDS)
            & rearmed["confirmation_variant_id"].astype(str).isin(
                CONFIRMATION_VARIANT_IDS
            )
            & pd.to_numeric(rearmed["holding_days"], errors="coerce").eq(
                HOLDING_DAYS
            )
            & rearmed["stop_policy_id"].astype(str).eq(NO_STOP_POLICY_ID)
            & _boolish(rearmed["return_valid"])
        ]
        if rearmed_dates.empty:
            raise RuntimeError("trusted v1 rearmed selected valid slice is empty")
        _validate_trusted_date_values(
            rearmed_dates,
            (
                "trigger_date",
                "confirmation_date",
                "entry_date",
                "planned_exit_date",
                "exit_date",
            ),
            label="rearmed selected valid detail",
        )
        return projection_manifest, source, rearmed
    paths = {
        name: source_root / SOURCE_RELATIVE_PATHS[name]
        for name in ("projection_manifest", "source_first", "rearmed")
    }
    missing_paths = [str(path) for path in paths.values() if not path.is_file()]
    if missing_paths:
        raise RuntimeError(f"source artifacts are missing: {missing_paths}")
    source = pd.read_csv(
        paths["source_first"],
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    rearmed = pd.read_csv(
        paths["rearmed"],
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    projection_manifest = pd.read_csv(
        paths["projection_manifest"],
        dtype=str,
        keep_default_na=False,
    )
    return projection_manifest, source, rearmed

def _prepare_source(source: pd.DataFrame) -> pd.DataFrame:
    required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "condition_variant_id",
        "episode_key",
        "stock_id",
        "stock_name",
        "episode_start_revenue_period",
        "episode_start_source_date",
        "episode_start_cross_market_resolution_id",
        "episode_start_source_row_canonical_sha256",
        "episode_start_canonical_source_table_date",
        "episode_start_trade_date",
        "episode_start_sequence_index",
        "latest_qualifying_revenue_period",
        "latest_qualifying_source_date",
        "latest_qualifying_cross_market_resolution_id",
        "latest_qualifying_source_row_canonical_sha256",
        "latest_qualifying_canonical_source_table_date",
        "latest_qualifying_trade_date",
        "latest_qualifying_sequence_index",
        "qualifying_update_count",
        "qualifying_revenue_periods",
        "qualifying_source_dates",
        "qualifying_cross_market_resolution_ids",
        "qualifying_source_row_canonical_sha256s",
        "qualifying_canonical_source_table_dates",
        "qualifying_trade_dates",
        "qualifying_sequence_indices",
        *MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS,
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise RuntimeError(f"source-first detail is missing columns: {missing}")
    expected = {
        "model_id": MODEL_ID,
        "artifact_id": SOURCE_FIRST_ARTIFACT_ID,
        "artifact_version": SOURCE_FIRST_ARTIFACT_VERSION,
    }
    for column, value in expected.items():
        if set(source[column].astype(str)) != {value}:
            raise RuntimeError(f"source-first governance drift: {column}")
    for column in MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS:
        values = set(source[column].astype(str).str.strip().str.lower())
        if len(values) != 1:
            raise RuntimeError(f"source-first run lineage is not constant: {column}")
        digest = next(iter(values))
        if len(digest) != 64 or any(
            character not in "0123456789abcdef" for character in digest
        ):
            raise RuntimeError(f"source-first run lineage is not SHA-256: {column}")
    source = source.loc[
        source["condition_variant_id"].astype(str).eq(SOURCE_VARIANT_ID)
    ].copy()
    if source.empty:
        raise RuntimeError("source-first selected condition is empty")
    if set(source["condition_variant_id"].astype(str)) != {SOURCE_VARIANT_ID}:
        raise RuntimeError("source-first selected condition governance drift")
    source["stock_id"] = source["stock_id"].map(_stock_id)
    if source["episode_key"].astype(str).duplicated().any():
        raise RuntimeError("source-first detail has duplicate episode keys")
    selected_slice_sha = _canonical_table_sha256(source)
    source["source_first_canonical_row_sha256"] = source.apply(
        lambda row: _canonical_mapping_sha256(row.to_dict()), axis=1
    )
    source["source_first_selected_slice_canonical_sha256"] = selected_slice_sha
    return source.set_index("episode_key", drop=False)


def _prepare_operations(
    rearmed: pd.DataFrame,
    *,
    expected_artifact_version: str = REARMED_ARTIFACT_VERSION,
) -> pd.DataFrame:
    required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "source_artifact_id",
        "source_variant_id",
        "grid_id",
        "lifecycle_policy_id",
        "confirmation_variant_id",
        "holding_days",
        "stop_policy_id",
        "return_valid",
        "episode_key",
        "stock_id",
        "stock_name",
        "trigger_date",
        "confirmation_date",
        "entry_index",
        "entry_date",
        "entry_price",
        "planned_exit_index",
        "planned_exit_date",
        "exit_index",
        "exit_date",
        "exit_price",
        "entry_price_basis",
        "fixed_exit_price_basis",
        "exit_price_basis",
        "exit_reason",
        "intraday_operation_basis_used",
        "realized_return_pct",
        "return_outcome",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        "operation_return_review_candidate_flag",
    }
    missing = sorted(required - set(rearmed.columns))
    if missing:
        raise RuntimeError(f"rearmed detail is missing columns: {missing}")
    expected_all = {
        "model_id": MODEL_ID,
        "artifact_id": REARMED_ARTIFACT_ID,
        "artifact_version": expected_artifact_version,
        "source_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
        "source_variant_id": SOURCE_VARIANT_ID,
        "entry_price_basis": "analysis_open",
    }
    for column, value in expected_all.items():
        if set(rearmed[column].astype(str)) != {value}:
            raise RuntimeError(f"rearmed governance or price-basis drift: {column}")
    if _boolish(rearmed["intraday_operation_basis_used"]).any():
        raise RuntimeError("rearmed operation uses intraday price basis")
    holding_all = pd.to_numeric(rearmed["holding_days"], errors="coerce")
    if holding_all.isna().any() or not np.isclose(
        holding_all, holding_all.round()
    ).all():
        raise RuntimeError("rearmed holding-days contract is invalid")
    expected_grid = (
        rearmed["lifecycle_policy_id"].astype(str)
        + "|"
        + rearmed["confirmation_variant_id"].astype(str)
        + "|d"
        + holding_all.round().astype("int64").astype(str)
        + "|"
        + rearmed["stop_policy_id"].astype(str)
    )
    if not rearmed["grid_id"].astype(str).eq(expected_grid).all():
        raise RuntimeError("rearmed grid contract drift")

    selected = rearmed.loc[
        rearmed["lifecycle_policy_id"].astype(str).isin(LIFECYCLE_POLICY_IDS)
        & rearmed["confirmation_variant_id"].astype(str).isin(
            CONFIRMATION_VARIANT_IDS
        )
        & pd.to_numeric(rearmed["holding_days"], errors="coerce").eq(HOLDING_DAYS)
        & rearmed["stop_policy_id"].astype(str).eq(NO_STOP_POLICY_ID)
        & _boolish(rearmed["return_valid"])
    ].copy()
    if selected.empty:
        raise RuntimeError("rearmed selected operation slice is empty")
    expected_selected = {
        "entry_price_basis": "analysis_open",
        "fixed_exit_price_basis": "analysis_close",
        "exit_price_basis": "fixed_future_close",
        "exit_reason": "fixed_d30_close",
        "stop_policy_id": NO_STOP_POLICY_ID,
    }
    for column, value in expected_selected.items():
        if set(selected[column].astype(str)) != {value}:
            raise RuntimeError(f"rearmed governance or price-basis drift: {column}")
    selected["stock_id"] = selected["stock_id"].map(_stock_id)
    for column in ("trigger_date", "confirmation_date", "entry_date", "exit_date"):
        selected[column] = selected[column].map(_date_text)
        if selected[column].eq("").any():
            raise RuntimeError(f"rearmed operation has invalid {column}")
    selected["realized_return_pct"] = pd.to_numeric(
        selected["realized_return_pct"], errors="coerce"
    )
    if selected["realized_return_pct"].isna().any():
        raise RuntimeError("rearmed operation has invalid realized return")
    duplicate_columns = [
        "grid_id",
        "stock_id",
        "episode_key",
        "trigger_date",
        "entry_date",
    ]
    if selected.duplicated(duplicate_columns).any():
        raise RuntimeError("rearmed selected slice contains duplicate operations")
    first_match = selected.loc[
        selected["lifecycle_policy_id"].eq("episode_first_match_once")
    ]
    if first_match.duplicated(
        ["confirmation_variant_id", "stock_id", "episode_key"]
    ).any():
        raise RuntimeError(
            "rearmed episode_first_match_once has multiple operations per episode"
        )
    if _overlap_pair_count(selected):
        raise RuntimeError("rearmed selected slice contains same-stock overlap")
    selected_slice_sha = _canonical_table_sha256(selected)
    selected["rearmed_operation_canonical_row_sha256"] = selected.apply(
        lambda row: _canonical_mapping_sha256(row.to_dict()), axis=1
    )
    selected["rearmed_d30_no_stop_slice_canonical_sha256"] = selected_slice_sha
    return selected.sort_values(
        [
            "lifecycle_policy_id",
            "confirmation_variant_id",
            "stock_id",
            "entry_date",
            "episode_key",
        ],
        kind="mergesort",
    ).reset_index(drop=True)


def _asof_source(
    episode: pd.Series,
    price: pd.DataFrame,
    trigger_index: int,
) -> dict[str, object]:
    periods = _split(episode["qualifying_revenue_periods"])
    source_dates = [
        _date_text(value) for value in _split(episode["qualifying_source_dates"])
    ]
    resolution_ids = [
        _canonical_value(value)
        for value in _split(episode["qualifying_cross_market_resolution_ids"])
    ]
    source_row_sha256s = [
        _require_sha256(value, label="qualifying source-row lineage")
        for value in _split(episode["qualifying_source_row_canonical_sha256s"])
    ]
    canonical_source_table_dates = [
        _date_text(value)
        for value in _split(episode["qualifying_canonical_source_table_dates"])
    ]
    trade_dates = [
        _date_text(value) for value in _split(episode["qualifying_trade_dates"])
    ]
    try:
        sequence_indices = [
            _strict_integral(value, label="qualifying sequence index")
            for value in _split(episode["qualifying_sequence_indices"])
        ]
        update_count = _strict_integral(
            episode["qualifying_update_count"],
            label="qualifying update count",
        )
    except ValueError as exc:
        raise RuntimeError(
            f"source-first qualifying lineage is invalid: {episode['episode_key']}"
        ) from exc
    lengths = {
        len(periods),
        len(source_dates),
        len(resolution_ids),
        len(source_row_sha256s),
        len(canonical_source_table_dates),
        len(trade_dates),
        len(sequence_indices),
        update_count,
    }
    if len(lengths) != 1 or not periods:
        raise RuntimeError(
            f"source-first qualifying lineage is not aligned: {episode['episode_key']}"
        )
    if any(
        not value
        for value in (
            source_dates
            + resolution_ids
            + canonical_source_table_dates
            + trade_dates
        )
    ):
        raise RuntimeError(
            f"source-first qualifying lineage contains an invalid date: "
            f"{episode['episode_key']}"
        )
    if sequence_indices != sorted(sequence_indices) or len(set(sequence_indices)) != len(
        sequence_indices
    ):
        raise RuntimeError(
            f"source-first qualifying sequence is not strictly ordered: "
            f"{episode['episode_key']}"
        )
    for label, values in (
        ("revenue periods", periods),
        ("source dates", source_dates),
        ("trade dates", trade_dates),
    ):
        if values != sorted(values) or len(set(values)) != len(values):
            raise RuntimeError(
                f"source-first qualifying {label} are not strictly ordered: "
                f"{episode['episode_key']}"
            )
    scalar_lineage = {
        "episode_start_revenue_period": periods[0],
        "episode_start_source_date": source_dates[0],
        "episode_start_cross_market_resolution_id": resolution_ids[0],
        "episode_start_source_row_canonical_sha256": source_row_sha256s[0],
        "episode_start_canonical_source_table_date": (
            canonical_source_table_dates[0]
        ),
        "episode_start_trade_date": trade_dates[0],
        "episode_start_sequence_index": sequence_indices[0],
        "latest_qualifying_revenue_period": periods[-1],
        "latest_qualifying_source_date": source_dates[-1],
        "latest_qualifying_cross_market_resolution_id": resolution_ids[-1],
        "latest_qualifying_source_row_canonical_sha256": source_row_sha256s[-1],
        "latest_qualifying_canonical_source_table_date": (
            canonical_source_table_dates[-1]
        ),
        "latest_qualifying_trade_date": trade_dates[-1],
        "latest_qualifying_sequence_index": sequence_indices[-1],
    }
    for column, expected in scalar_lineage.items():
        observed = episode[column]
        if column.endswith("sequence_index"):
            equal = _same_number(observed, expected, tolerance=0.0)
        elif column.endswith("source_row_canonical_sha256"):
            equal = _require_sha256(observed, label=column) == expected
        elif column.endswith("source_date") or column.endswith("table_date"):
            equal = _date_text(observed) == expected
        else:
            equal = str(observed) == str(expected)
        if not equal:
            raise RuntimeError(
                f"source-first scalar/array lineage drift: "
                f"{episode['episode_key']}/{column}"
            )
    date_index = {str(date): int(index) for index, date in price["date"].items()}
    normalized_dates = list(date_index)
    for source_date, trade_date, sequence_index in zip(
        source_dates, trade_dates, sequence_indices
    ):
        if trade_date not in date_index:
            raise RuntimeError(
                f"source-first qualifying trade date is absent from price history: "
                f"{episode['episode_key']}/{trade_date}"
            )
        if source_date > trade_date:
            raise RuntimeError(
                f"source-first source date is after its mapped trade date: "
                f"{episode['episode_key']}"
            )
        mapped = next((date for date in normalized_dates if date >= source_date), "")
        if trade_date != mapped:
            raise RuntimeError(
                f"source-first trade-date mapping is not first date on/after source: "
                f"{episode['episode_key']}/{source_date}/{trade_date}/{mapped}"
            )
        if sequence_index != date_index[trade_date]:
            raise RuntimeError(
                f"source-first sequence/date lineage drift: {episode['episode_key']}"
            )
    known_positions = [
        position
        for position, sequence_index in enumerate(sequence_indices)
        if sequence_index <= trigger_index
    ]
    if not known_positions:
        raise RuntimeError(
            f"operation has no qualifying source known by trigger: "
            f"{episode['episode_key']}"
        )
    position = known_positions[-1]
    source_index = sequence_indices[position]
    return {
        "asof_latest_qualifying_revenue_period": periods[position],
        "asof_latest_qualifying_source_date": source_dates[position],
        "asof_latest_qualifying_cross_market_resolution_id": (
            resolution_ids[position]
        ),
        "asof_latest_qualifying_source_row_canonical_sha256": (
            source_row_sha256s[position]
        ),
        "asof_latest_qualifying_canonical_source_table_date": (
            canonical_source_table_dates[position]
        ),
        "asof_latest_qualifying_trade_date": trade_dates[position],
        "asof_latest_qualifying_sequence_index": source_index,
        "latest_source_to_trigger_trading_days": trigger_index - source_index,
        "future_qualifying_update_ignored_count": len(periods) - position - 1,
        "source_index": source_index,
    }


def _overlap_pair_count(detail: pd.DataFrame) -> int:
    count = 0
    if detail.empty:
        return count
    group_columns = ["lifecycle_policy_id", "confirmation_variant_id", "stock_id"]
    for _keys, part in detail.groupby(group_columns, sort=False, dropna=False):
        prior_exit = ""
        for row in part.sort_values("entry_date", kind="mergesort").itertuples(
            index=False
        ):
            if prior_exit and str(row.entry_date) <= prior_exit:
                count += 1
            prior_exit = max(prior_exit, str(row.exit_date))
    return count


def _expected_detail(
    source: pd.DataFrame,
    operations: pd.DataFrame,
    source_root: Path,
    price_stock_ids: set[str],
    *,
    trusted_revision: str | None = None,
) -> pd.DataFrame:
    price_dir = source_root / SOURCE_RELATIVE_PATHS["price_dir"]
    resolutions = _load_resolutions(
        source_root / SOURCE_RELATIVE_PATHS["resolution"],
        trusted_revision=trusted_revision,
    )
    producer_sha = _normalized_file_sha256(
        source_root,
        PRODUCER_RELATIVE_PATH,
        trusted_revision=trusted_revision,
    )
    source_first_producer_sha = _normalized_file_sha256(
        source_root,
        SOURCE_FIRST_PRODUCER_RELATIVE_PATH,
        trusted_revision=trusted_revision,
    )
    rearmed_producer_sha = _normalized_file_sha256(
        source_root,
        REARMED_PRODUCER_RELATIVE_PATH,
        trusted_revision=trusted_revision,
    )
    position_shape_producer_sha = _normalized_file_sha256(
        source_root,
        POSITION_SHAPE_PRODUCER_RELATIVE_PATH,
        trusted_revision=trusted_revision,
    )
    data_contract_sha = _registered_data_contract_sha256(
        source_root,
        trusted_revision=trusted_revision,
    )
    price_cache: dict[str, pd.DataFrame] = {}
    price_hash_cache: dict[str, str] = {}
    normalized_price_stock_ids = sorted(
        {_stock_id(value) for value in price_stock_ids if _stock_id(value)}
    )
    if trusted_revision is not None:
        _trusted_blobs(
            {_trusted_stock_path(stock_id) for stock_id in normalized_price_stock_ids},
            revision=trusted_revision,
        )
    for stock_id in normalized_price_stock_ids:
        price_cache[stock_id] = _load_adjusted_price(
            stock_id,
            price_dir,
            resolutions,
            trusted_revision=trusted_revision,
        )
        price_hash_cache[stock_id] = _canonical_frame_sha256(price_cache[stock_id])
    price_manifest_sha = _canonical_table_sha256(
        pd.DataFrame(
            [
                {
                    "stock_id": stock_id,
                    "price_history_canonical_sha256": digest,
                }
                for stock_id, digest in sorted(price_hash_cache.items())
            ]
        )
    )
    rows: list[dict[str, object]] = []
    for operation in operations.itertuples(index=False):
        episode_key = str(operation.episode_key)
        if episode_key not in source.index:
            raise RuntimeError(f"source-first episode is missing: {episode_key}")
        episode = source.loc[episode_key]
        stock_id = str(operation.stock_id)
        if str(episode["stock_id"]) != stock_id:
            raise RuntimeError(f"source-first stock lineage drift: {episode_key}")
        if stock_id not in price_cache:
            raise RuntimeError(
                f"operation stock is absent from source-first price manifest: {stock_id}"
            )
        price = price_cache[stock_id]
        date_index = {str(date): int(index) for index, date in price["date"].items()}
        named_dates = {
            "trigger": str(operation.trigger_date),
            "confirmation": str(operation.confirmation_date),
            "entry": str(operation.entry_date),
            "exit": str(operation.exit_date),
        }
        missing = [name for name, date in named_dates.items() if date not in date_index]
        if missing:
            raise RuntimeError(
                f"operation dates are absent from price history: "
                f"{stock_id}/{episode_key}/{missing}"
            )
        indices = {name: date_index[date] for name, date in named_dates.items()}
        delayed = (
            str(operation.confirmation_variant_id)
            == "delayed_next_close_continuation_bonus"
        )
        if indices["confirmation"] != indices["trigger"] + (1 if delayed else 0):
            raise RuntimeError(
                f"confirmation offset drift: {stock_id}/{episode_key}/"
                f"{operation.confirmation_variant_id}"
            )
        if indices["entry"] != indices["confirmation"] + 1:
            raise RuntimeError(
                f"entry offset drift: {stock_id}/{episode_key}/"
                f"{operation.confirmation_variant_id}"
            )
        if indices["exit"] != indices["entry"] + HOLDING_DAYS - 1:
            raise RuntimeError(
                f"D30 exit offset drift: {stock_id}/{episode_key}/"
                f"{operation.confirmation_variant_id}"
            )
        recorded_indices = {
            "entry": operation.entry_index,
            "planned_exit": operation.planned_exit_index,
            "exit": operation.exit_index,
        }
        for name, value in recorded_indices.items():
            expected_index = indices["exit"] if name == "planned_exit" else indices[name]
            if not _same_number(value, expected_index, tolerance=0.0):
                raise RuntimeError(
                    f"recorded operation index drift: {stock_id}/{episode_key}/{name}"
                )
        if _date_text(operation.planned_exit_date) != str(operation.exit_date):
            raise RuntimeError(
                f"recorded planned exit date drift: {stock_id}/{episode_key}"
            )
        if delayed:
            trigger_close = _number(price.at[indices["trigger"], "analysis_close"])
            confirmation_close = _number(
                price.at[indices["confirmation"], "analysis_close"]
            )
            if not (
                trigger_close is not None
                and confirmation_close is not None
                and confirmation_close > trigger_close
            ):
                raise RuntimeError(
                    f"delayed confirmation lacks continuation: {stock_id}/{episode_key}"
                )
        entry_open = _number(price.at[indices["entry"], "analysis_open"])
        exit_close = _number(price.at[indices["exit"], "analysis_close"])
        if not (
            entry_open is not None
            and entry_open > 0
            and exit_close is not None
            and exit_close > 0
        ):
            raise RuntimeError(
                f"operation price basis is invalid: {stock_id}/{episode_key}"
            )
        replayed_return = (exit_close / entry_open - 1.0) * 100.0
        if not _same_number(operation.entry_price, entry_open, tolerance=0.00000001):
            raise RuntimeError(
                f"recorded entry price drift: {stock_id}/{episode_key}"
            )
        if not _same_number(operation.exit_price, exit_close, tolerance=0.00000001):
            raise RuntimeError(
                f"recorded exit price drift: {stock_id}/{episode_key}"
            )
        if not _same_number(
            operation.realized_return_pct, replayed_return, tolerance=0.00011
        ):
            raise RuntimeError(
                f"D30 open-to-close replay drift: {stock_id}/{episode_key}/"
                f"{operation.confirmation_variant_id}"
            )
        expected_outcome = (
            "win"
            if replayed_return > 1e-9
            else "failure"
            if replayed_return < -1e-9
            else "neutral"
        )
        if str(operation.return_outcome) != expected_outcome:
            raise RuntimeError(f"return outcome drift: {stock_id}/{episode_key}")

        asof = _asof_source(episode, price, indices["trigger"])
        lag = int(asof["latest_source_to_trigger_trading_days"])
        if lag < 0:
            raise RuntimeError(f"source is after trigger: {stock_id}/{episode_key}")
        if lag > WATCH_HORIZON_TRADING_DAYS:
            continue
        features = _anchor_features(price, int(asof["source_index"]))
        low_member = (
            features["source_position_bucket"] == "low_pos_le40"
            and features["source_shape_bucket"] == "falling"
        )
        mid_member = (
            features["source_position_bucket"] == "mid_pos_40_75"
            and features["source_shape_bucket"] == "falling"
        )
        union_member = low_member or mid_member
        if not union_member:
            continue
        source_candidate = _bool_value(operation.source_anomaly_candidate_flag)
        price_candidate = _bool_value(
            operation.unresolved_price_path_candidate_flag
        )
        return_candidate = _bool_value(
            operation.operation_return_review_candidate_flag
        )
        combined_candidate = source_candidate or price_candidate or return_candidate
        operation_key = "|".join(
            (
                str(operation.lifecycle_policy_id),
                str(operation.confirmation_variant_id),
                stock_id,
                episode_key,
                str(operation.trigger_date),
                str(operation.entry_date),
            )
        )
        rows.append(
            {
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                "canonical_lineage_version": CANONICAL_LINEAGE_VERSION,
                "data_contract_sha256": data_contract_sha,
                "producer_semantic_sha256": producer_sha,
                "source_first_producer_semantic_sha256": source_first_producer_sha,
                "rearmed_producer_semantic_sha256": rearmed_producer_sha,
                "position_shape_producer_semantic_sha256": (
                    position_shape_producer_sha
                ),
                "source_first_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
                "source_first_artifact_version": SOURCE_FIRST_ARTIFACT_VERSION,
                "source_variant_id": SOURCE_VARIANT_ID,
                **{
                    column: str(episode[column]).strip().lower()
                    for column in MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS
                },
                "source_first_canonical_row_sha256": str(
                    episode["source_first_canonical_row_sha256"]
                ),
                "source_first_selected_slice_canonical_sha256": str(
                    episode["source_first_selected_slice_canonical_sha256"]
                ),
                "rearmed_artifact_id": REARMED_ARTIFACT_ID,
                "rearmed_artifact_version": REARMED_ARTIFACT_VERSION,
                "rearmed_grid_id": str(operation.grid_id),
                "rearmed_operation_canonical_row_sha256": str(
                    operation.rearmed_operation_canonical_row_sha256
                ),
                "rearmed_d30_no_stop_slice_canonical_sha256": str(
                    operation.rearmed_d30_no_stop_slice_canonical_sha256
                ),
                "price_history_canonical_sha256": price_hash_cache[stock_id],
                "price_history_manifest_canonical_sha256": price_manifest_sha,
                "operation_key": operation_key,
                "paired_trigger_key": "|".join(
                    (
                        str(operation.lifecycle_policy_id),
                        stock_id,
                        episode_key,
                        str(operation.trigger_date),
                    )
                ),
                "lifecycle_policy_id": str(operation.lifecycle_policy_id),
                "confirmation_variant_id": str(operation.confirmation_variant_id),
                "holding_days": HOLDING_DAYS,
                "stop_policy_id": NO_STOP_POLICY_ID,
                "episode_key": episode_key,
                "stock_id": stock_id,
                "stock_name": str(operation.stock_name),
                **{key: value for key, value in asof.items() if key != "source_index"},
                "trigger_date": str(operation.trigger_date),
                "confirmation_date": str(operation.confirmation_date),
                "trigger_index": indices["trigger"],
                "confirmation_index": indices["confirmation"],
                "entry_index": indices["entry"],
                "entry_date": str(operation.entry_date),
                "entry_price": round(float(operation.entry_price), 8),
                "planned_exit_index": indices["exit"],
                "planned_exit_date": _date_text(operation.planned_exit_date),
                "exit_index": indices["exit"],
                "exit_date": str(operation.exit_date),
                "exit_price": round(float(operation.exit_price), 8),
                "entry_price_basis": "analysis_open",
                "fixed_exit_price_basis": "analysis_close",
                "exit_price_basis": "fixed_future_close",
                "exit_reason": "fixed_d30_close",
                "holding_session_index_offset": HOLDING_SESSION_INDEX_OFFSET,
                "holding_session_contract": HOLDING_SESSION_CONTRACT,
                "intraday_operation_basis_used": False,
                "realized_return_pct": round(replayed_return, 4),
                "return_outcome": expected_outcome,
                "realized_return_ge20": replayed_return >= 20.0,
                "realized_return_le_minus20": replayed_return <= -20.0,
                "source_anchor_date": str(asof["asof_latest_qualifying_trade_date"]),
                **features,
                "mid_falling_member": mid_member,
                "low_falling_member": low_member,
                "low_or_mid_falling_union_member": union_member,
                "source_anomaly_candidate_flag": source_candidate,
                "unresolved_price_path_candidate_flag": price_candidate,
                "operation_return_review_candidate_flag": return_candidate,
                "combined_exclusion_candidate_flag": combined_candidate,
                "primary_included": True,
                "sensitivity_included": not combined_candidate,
                "same_stock_non_overlap_applied": True,
                "watch_horizon_trading_days": WATCH_HORIZON_TRADING_DAYS,
                "watch_horizon_passed": True,
                "position_policy": POSITION_POLICY,
                "shape_policy": SHAPE_POLICY,
                "anomaly_policy": ANOMALY_POLICY,
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "approved_for_daily": False,
                "presentation_allowed": False,
                "formal_model_use_allowed": False,
                "production_change": False,
                "promotion_readiness": PROMOTION_READINESS,
            }
        )
    if not rows:
        raise RuntimeError("independent low/mid falling candidate slice is empty")
    detail = pd.DataFrame(rows).sort_values(
        [
            "lifecycle_policy_id",
            "confirmation_variant_id",
            "stock_id",
            "entry_date",
        ],
        kind="mergesort",
    ).reset_index(drop=True)
    if detail["operation_key"].duplicated().any():
        raise RuntimeError("independent replay contains duplicate operation keys")
    first = detail.loc[detail["lifecycle_policy_id"].eq("episode_first_match_once")]
    if first.duplicated(
        ["confirmation_variant_id", "stock_id", "episode_key"]
    ).any():
        raise RuntimeError(
            "episode_first_match_once contains multiple operations per episode"
        )
    overlaps = _overlap_pair_count(detail)
    if overlaps:
        raise RuntimeError(f"independent replay contains same-stock overlap: {overlaps}")
    detail["candidate_detail_row_sha256"] = detail.apply(
        lambda row: _canonical_mapping_sha256(row.to_dict()), axis=1
    )
    detail["detail_artifact_canonical_sha256"] = _canonical_table_sha256(detail)
    for source_column, set_column in (
        (
            "source_first_canonical_row_sha256",
            "source_first_canonical_row_set_sha256",
        ),
        (
            "rearmed_operation_canonical_row_sha256",
            "rearmed_operation_canonical_row_set_sha256",
        ),
        (
            "price_history_canonical_sha256",
            "price_history_canonical_set_sha256",
        ),
        (
            "candidate_detail_row_sha256",
            "candidate_detail_row_set_sha256",
        ),
    ):
        detail[set_column] = _lineage_set_sha256(detail, source_column)
    return detail

def _artifact_lineage(detail: pd.DataFrame) -> dict[str, str]:
    first = detail.iloc[0]
    return {
        "canonical_lineage_version": str(first["canonical_lineage_version"]),
        "data_contract_sha256": str(first["data_contract_sha256"]),
        "producer_semantic_sha256": str(first["producer_semantic_sha256"]),
        "source_first_producer_semantic_sha256": str(
            first["source_first_producer_semantic_sha256"]
        ),
        "rearmed_producer_semantic_sha256": str(
            first["rearmed_producer_semantic_sha256"]
        ),
        "position_shape_producer_semantic_sha256": str(
            first["position_shape_producer_semantic_sha256"]
        ),
        "source_first_artifact_id": str(first["source_first_artifact_id"]),
        "source_first_artifact_version": str(first["source_first_artifact_version"]),
        **{
            column: str(first[column])
            for column in MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS
        },
        "rearmed_artifact_id": str(first["rearmed_artifact_id"]),
        "rearmed_artifact_version": str(first["rearmed_artifact_version"]),
        "source_first_selected_slice_canonical_sha256": str(
            first["source_first_selected_slice_canonical_sha256"]
        ),
        "rearmed_d30_no_stop_slice_canonical_sha256": str(
            first["rearmed_d30_no_stop_slice_canonical_sha256"]
        ),
        "price_history_manifest_canonical_sha256": str(
            first["price_history_manifest_canonical_sha256"]
        ),
        "detail_artifact_canonical_sha256": str(
            first["detail_artifact_canonical_sha256"]
        ),
        "source_first_canonical_row_set_sha256": str(
            first["source_first_canonical_row_set_sha256"]
        ),
        "rearmed_operation_canonical_row_set_sha256": str(
            first["rearmed_operation_canonical_row_set_sha256"]
        ),
        "price_history_canonical_set_sha256": str(
            first["price_history_canonical_set_sha256"]
        ),
        "candidate_detail_row_set_sha256": str(
            first["candidate_detail_row_set_sha256"]
        ),
    }


def _governance_errors(
    frame: pd.DataFrame,
    name: str,
    expected_lineage: dict[str, str] | None = None,
    *,
    expected_artifact_version: str = ARTIFACT_VERSION,
) -> list[str]:
    errors: list[str] = []
    expected = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": expected_artifact_version,
        "source_variant_id": SOURCE_VARIANT_ID,
        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
        "promotion_readiness": PROMOTION_READINESS,
        **(expected_lineage or {}),
    }
    if frame.empty:
        return [f"{name} is empty"]
    for column, value in expected.items():
        if column not in frame.columns:
            errors.append(f"{name} is missing governance column: {column}")
        elif set(frame[column].astype(str)) != {value}:
            errors.append(f"{name} governance drift: {column}")
    for column in (
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
    ):
        if column not in frame.columns:
            errors.append(f"{name} is missing formal-use flag: {column}")
        elif _boolish(frame[column]).any():
            errors.append(f"{name} must keep {column}=False")
    if (
        "generated_at" not in frame.columns
        or frame["generated_at"].astype(str).nunique() != 1
        or not str(frame["generated_at"].iloc[0]).strip()
    ):
        errors.append(f"{name} must contain one non-mutable generated_at value")
    return errors


def _compare_detail(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    *,
    expected_artifact_version: str = ARTIFACT_VERSION,
) -> list[str]:
    errors = _governance_errors(
        actual,
        "detail",
        _artifact_lineage(expected),
        expected_artifact_version=expected_artifact_version,
    )
    required = set(expected.columns)
    missing = sorted(required - set(actual.columns))
    if missing:
        errors.append(f"detail is missing independently replayed columns: {missing}")
        return errors
    if actual["operation_key"].astype(str).duplicated().any():
        errors.append("detail contains duplicate operation keys")
        return errors
    left = actual.copy()
    left["stock_id"] = left["stock_id"].map(_stock_id)
    joined = expected.merge(
        left,
        on="operation_key",
        how="outer",
        suffixes=("_expected", "_actual"),
        indicator=True,
        validate="one_to_one",
    )
    if not joined["_merge"].eq("both").all():
        errors.append("detail membership differs from independent source replay")
        return errors
    bool_columns = {
        "intraday_operation_basis_used",
        "realized_return_ge20",
        "realized_return_le_minus20",
        "source_classification_observed",
        "mid_falling_member",
        "low_falling_member",
        "low_or_mid_falling_union_member",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        "operation_return_review_candidate_flag",
        "combined_exclusion_candidate_flag",
        "primary_included",
        "sensitivity_included",
        "same_stock_non_overlap_applied",
        "watch_horizon_passed",
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
    }
    numeric_columns = {
        "holding_days",
        "trigger_index",
        "confirmation_index",
        "entry_index",
        "entry_price",
        "planned_exit_index",
        "exit_index",
        "exit_price",
        "holding_session_index_offset",
        "asof_latest_qualifying_sequence_index",
        "latest_source_to_trigger_trading_days",
        "future_qualifying_update_ignored_count",
        "realized_return_pct",
        "source_position_120d_pct",
        "source_shape_return20_pct",
        "source_shape_range23_pct",
        "source_shape_ema23_slope5_pct",
        "watch_horizon_trading_days",
    }
    string_columns = required - bool_columns - numeric_columns - {"operation_key"}
    for column in sorted(string_columns):
        expected_values = joined[f"{column}_expected"].fillna("").astype(str)
        actual_values = joined[f"{column}_actual"].fillna("").astype(str)
        mismatches = int((~expected_values.eq(actual_values)).sum())
        if mismatches:
            errors.append(f"detail {column} drift rows={mismatches}")
    for column in sorted(bool_columns):
        mismatches = int(
            (~_boolish(joined[f"{column}_expected"]).eq(
                _boolish(joined[f"{column}_actual"])
            )).sum()
        )
        if mismatches:
            errors.append(f"detail {column} drift rows={mismatches}")
    for column in sorted(numeric_columns):
        mismatches = sum(
            not _same_number(observed, expected_value)
            for observed, expected_value in zip(
                joined[f"{column}_actual"], joined[f"{column}_expected"]
            )
        )
        if mismatches:
            errors.append(f"detail {column} drift rows={mismatches}")
    if not _boolish(left["primary_included"]).all():
        errors.append("detail primary must retain every candidate row")
    expected_sensitivity = ~_boolish(left["combined_exclusion_candidate_flag"])
    if not _boolish(left["sensitivity_included"]).eq(expected_sensitivity).all():
        errors.append("detail sensitivity inclusion is not candidate exclusion only")
    low = _boolish(left["low_falling_member"])
    mid = _boolish(left["mid_falling_member"])
    union = _boolish(left["low_or_mid_falling_union_member"])
    if (low & mid).any() or not union.eq(low | mid).all() or not union.all():
        errors.append("detail low/mid/union membership drift")
    if _overlap_pair_count(left):
        errors.append("detail contains same-stock overlap within lifecycle/confirmation")
    first = left.loc[left["lifecycle_policy_id"].eq("episode_first_match_once")]
    if first.duplicated(
        ["confirmation_variant_id", "stock_id", "episode_key"]
    ).any():
        errors.append("detail episode_first_match_once is not one operation per episode")
    return errors


def _performance_metrics(part: pd.DataFrame) -> dict[str, float | int | None]:
    returns = pd.to_numeric(part["realized_return_pct"], errors="coerce")
    outcomes = part["return_outcome"].astype(str)
    count = len(part)
    wins = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    failures = int(outcomes.eq("failure").sum())
    ge20 = int(returns.ge(20.0).sum())
    le_minus20 = int(returns.le(-20.0).sum())
    return {
        "operation_count": count,
        "unique_stock_count": int(part["stock_id"].nunique()),
        "unique_episode_count": int(part["episode_key"].nunique()),
        "win_count": wins,
        "neutral_count": neutral,
        "failure_count": failures,
        "win_rate_pct": _rate(wins, count),
        "neutral_rate_pct": _rate(neutral, count),
        "failure_rate_pct": _rate(failures, count),
        "avg_return_pct": _stat(returns, "mean"),
        "median_return_pct": _stat(returns, "median"),
        "p10_return_pct": _stat(returns, "p10"),
        "p90_return_pct": _stat(returns, "p90"),
        "min_return_pct": _stat(returns, "min"),
        "max_return_pct": _stat(returns, "max"),
        "return_ge20_count": ge20,
        "return_ge20_rate_pct": _rate(ge20, count),
        "return_le_minus20_count": le_minus20,
        "return_le_minus20_rate_pct": _rate(le_minus20, count),
        "top1_abs_return_share_pct": _top_abs_share(returns, 1),
        "top5_abs_return_share_pct": _top_abs_share(returns, 5),
        "source_anomaly_candidate_count": int(
            _boolish(part["source_anomaly_candidate_flag"]).sum()
        ),
        "unresolved_price_path_candidate_count": int(
            _boolish(part["unresolved_price_path_candidate_flag"]).sum()
        ),
        "operation_return_review_candidate_count": int(
            _boolish(part["operation_return_review_candidate_flag"]).sum()
        ),
        "combined_exclusion_candidate_count": int(
            _boolish(part["combined_exclusion_candidate_flag"]).sum()
        ),
        "same_stock_overlap_pair_count": _overlap_pair_count(part),
    }


def _validate_metrics(
    row: object,
    expected: dict[str, float | int | None],
    label: str,
    errors: list[str],
) -> None:
    for column, value in expected.items():
        if not hasattr(row, column):
            errors.append(f"{label} is missing metric: {column}")
        elif not _same_number(getattr(row, column), value):
            errors.append(f"{label} metric drift: {column}")


def _compare_summary(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    *,
    expected_artifact_version: str = ARTIFACT_VERSION,
) -> list[str]:
    errors = _governance_errors(
        summary,
        "summary",
        _artifact_lineage(detail),
        expected_artifact_version=expected_artifact_version,
    )
    required_keys = {
        (basis, lifecycle, confirmation, variant_id)
        for basis in ANALYSIS_BASES
        for lifecycle in LIFECYCLE_POLICY_IDS
        for confirmation in CONFIRMATION_VARIANT_IDS
        for _order, variant_id, _member in VARIANT_SPECS
    }
    required_columns = {
        "analysis_basis",
        "lifecycle_order",
        "lifecycle_policy_id",
        "confirmation_order",
        "confirmation_variant_id",
        "candidate_variant_order",
        "candidate_variant_id",
        "candidate_member_column",
        "holding_days",
        "stop_policy_id",
        "watch_horizon_trading_days",
        "sample_policy",
        "anomaly_policy",
        "same_stock_non_overlap_policy",
    }
    missing = sorted(required_columns - set(summary.columns))
    if missing:
        errors.append(f"summary is missing contract columns: {missing}")
        return errors
    observed_keys = set(
        zip(
            summary["analysis_basis"].astype(str),
            summary["lifecycle_policy_id"].astype(str),
            summary["confirmation_variant_id"].astype(str),
            summary["candidate_variant_id"].astype(str),
        )
    )
    if observed_keys != required_keys or summary.duplicated(
        [
            "analysis_basis",
            "lifecycle_policy_id",
            "confirmation_variant_id",
            "candidate_variant_id",
        ]
    ).any():
        errors.append("summary grid membership differs from the exact 2x2x2x3 contract")
        return errors
    parts = {
        PRIMARY_ANALYSIS_BASIS: detail,
        SENSITIVITY_ANALYSIS_BASIS: detail.loc[
            _boolish(detail["sensitivity_included"])
        ],
    }
    variant_meta = {
        variant_id: (order, member)
        for order, variant_id, member in VARIANT_SPECS
    }
    for row in summary.itertuples(index=False):
        lifecycle = str(row.lifecycle_policy_id)
        confirmation = str(row.confirmation_variant_id)
        variant = str(row.candidate_variant_id)
        basis = parts[str(row.analysis_basis)]
        grid = basis.loc[
            basis["lifecycle_policy_id"].eq(lifecycle)
            & basis["confirmation_variant_id"].eq(confirmation)
        ]
        order, member = variant_meta[variant]
        part = grid.loc[_boolish(grid[member])]
        label = f"summary {row.analysis_basis}/{lifecycle}/{confirmation}/{variant}"
        _validate_metrics(row, _performance_metrics(part), label, errors)
        expected_lifecycle_order = (LIFECYCLE_POLICY_IDS.index(lifecycle) + 1) * 10
        expected_confirmation_order = (
            CONFIRMATION_VARIANT_IDS.index(confirmation) + 1
        ) * 10
        exact = {
            "lifecycle_order": expected_lifecycle_order,
            "confirmation_order": expected_confirmation_order,
            "candidate_variant_order": order,
            "candidate_member_column": member,
            "holding_days": HOLDING_DAYS,
            "stop_policy_id": NO_STOP_POLICY_ID,
            "watch_horizon_trading_days": WATCH_HORIZON_TRADING_DAYS,
            "sample_policy": SAMPLE_POLICY,
            "anomaly_policy": ANOMALY_POLICY,
            "same_stock_non_overlap_policy": NON_OVERLAP_POLICY,
        }
        for column, expected_value in exact.items():
            if str(getattr(row, column)) != str(expected_value):
                errors.append(f"{label} contract drift: {column}")
    for basis in ANALYSIS_BASES:
        for lifecycle in LIFECYCLE_POLICY_IDS:
            for confirmation in CONFIRMATION_VARIANT_IDS:
                rows = summary.loc[
                    summary["analysis_basis"].eq(basis)
                    & summary["lifecycle_policy_id"].eq(lifecycle)
                    & summary["confirmation_variant_id"].eq(confirmation)
                ].set_index("candidate_variant_id")
                low_count = int(rows.at["source_low_falling", "operation_count"])
                mid_count = int(rows.at["source_mid_falling", "operation_count"])
                union_count = int(
                    rows.at["source_low_or_mid_falling_union", "operation_count"]
                )
                if union_count != low_count + mid_count:
                    errors.append(
                        f"summary union does not conserve disjoint low+mid rows: "
                        f"{basis}/{lifecycle}/{confirmation}"
                    )
    return errors


def _expected_paired(
    detail: pd.DataFrame,
    *,
    expected_artifact_version: str = ARTIFACT_VERSION,
) -> pd.DataFrame:
    key_columns = ["lifecycle_policy_id", "stock_id", "episode_key", "trigger_date"]
    common_columns = [
        *key_columns,
        "stock_name",
        "source_first_canonical_row_sha256",
        "price_history_canonical_sha256",
        "asof_latest_qualifying_source_date",
        "asof_latest_qualifying_trade_date",
        "latest_source_to_trigger_trading_days",
        "source_position_120d_pct",
        "source_shape_return20_pct",
        "source_shape_range23_pct",
        "source_shape_ema23_slope5_pct",
        "source_position_bucket",
        "source_shape_bucket",
        "source_position_shape_cell_id",
        "mid_falling_member",
        "low_falling_member",
        "low_or_mid_falling_union_member",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
    ]
    tail_columns = [
        "confirmation_date",
        "entry_date",
        "exit_date",
        "realized_return_pct",
        "rearmed_operation_canonical_row_sha256",
        "candidate_detail_row_sha256",
        "operation_return_review_candidate_flag",
        "combined_exclusion_candidate_flag",
    ]
    base = detail.loc[
        detail["confirmation_variant_id"].eq("base_close_confirmed"),
        [*common_columns, *tail_columns],
    ].copy()
    delayed = detail.loc[
        detail["confirmation_variant_id"].eq(
            "delayed_next_close_continuation_bonus"
        ),
        [*common_columns, *tail_columns],
    ].copy()
    if base.duplicated(key_columns).any() or delayed.duplicated(key_columns).any():
        raise RuntimeError("independent paired keys are duplicated")
    joined = base.merge(
        delayed,
        on=key_columns,
        how="inner",
        suffixes=("_base", "_delayed"),
        validate="one_to_one",
    )
    rows: list[dict[str, object]] = []
    for pair in joined.itertuples(index=False):
        for column in common_columns[4:]:
            base_value = getattr(pair, f"{column}_base")
            delayed_value = getattr(pair, f"{column}_delayed")
            if column.startswith("source_") and column.endswith("_pct"):
                equal = _same_number(base_value, delayed_value)
            else:
                equal = str(base_value) == str(delayed_value)
            if not equal:
                raise RuntimeError(f"paired source replay drift: {column}")
        base_candidate = _bool_value(
            pair.combined_exclusion_candidate_flag_base
        )
        delayed_candidate = _bool_value(
            pair.combined_exclusion_candidate_flag_delayed
        )
        rows.append(
            {
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": expected_artifact_version,
                **_artifact_lineage(detail),
                "source_variant_id": SOURCE_VARIANT_ID,
                **{column: getattr(pair, column) for column in key_columns},
                **{
                    column: getattr(pair, f"{column}_base")
                    for column in common_columns[4:]
                },
                "base_confirmation_date": pair.confirmation_date_base,
                "base_entry_date": pair.entry_date_base,
                "base_exit_date": pair.exit_date_base,
                "base_realized_return_pct": pair.realized_return_pct_base,
                "base_rearmed_operation_canonical_row_sha256": (
                    pair.rearmed_operation_canonical_row_sha256_base
                ),
                "base_candidate_detail_row_sha256": (
                    pair.candidate_detail_row_sha256_base
                ),
                "delayed_confirmation_date": pair.confirmation_date_delayed,
                "delayed_entry_date": pair.entry_date_delayed,
                "delayed_exit_date": pair.exit_date_delayed,
                "delayed_realized_return_pct": pair.realized_return_pct_delayed,
                "delayed_rearmed_operation_canonical_row_sha256": (
                    pair.rearmed_operation_canonical_row_sha256_delayed
                ),
                "delayed_candidate_detail_row_sha256": (
                    pair.candidate_detail_row_sha256_delayed
                ),
                "delayed_minus_base_return_pct_points": (
                    float(pair.realized_return_pct_delayed)
                    - float(pair.realized_return_pct_base)
                ),
                "base_operation_return_review_candidate_flag": _bool_value(
                    pair.operation_return_review_candidate_flag_base
                ),
                "delayed_operation_return_review_candidate_flag": _bool_value(
                    pair.operation_return_review_candidate_flag_delayed
                ),
                "paired_combined_exclusion_candidate_flag": (
                    base_candidate or delayed_candidate
                ),
                "paired_sensitivity_included": not (
                    base_candidate or delayed_candidate
                ),
                "paired_comparison_role": (
                    "same_trigger_distinct_information_cutoff_not_independent_operations"
                ),
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "approved_for_daily": False,
                "presentation_allowed": False,
                "formal_model_use_allowed": False,
                "production_change": False,
                "promotion_readiness": PROMOTION_READINESS,
            }
        )
    if not rows:
        raise RuntimeError("independent paired confirmation slice is empty")
    return pd.DataFrame(rows)


def _compare_paired(
    paired: pd.DataFrame,
    expected: pd.DataFrame,
    *,
    expected_artifact_version: str = ARTIFACT_VERSION,
) -> list[str]:
    errors = _governance_errors(
        paired,
        "paired",
        _artifact_lineage(expected),
        expected_artifact_version=expected_artifact_version,
    )
    required = set(expected.columns)
    missing = sorted(required - set(paired.columns))
    if missing:
        errors.append(f"paired artifact is missing replayed columns: {missing}")
        return errors
    keys = ["lifecycle_policy_id", "stock_id", "episode_key", "trigger_date"]
    if paired.duplicated(keys).any():
        errors.append("paired artifact contains duplicate trigger keys")
        return errors
    left = paired.copy()
    left["stock_id"] = left["stock_id"].map(_stock_id)
    left["trigger_date"] = left["trigger_date"].map(_date_text)
    left["lifecycle_policy_id"] = left["lifecycle_policy_id"].astype(str)
    left["episode_key"] = left["episode_key"].astype(str)
    joined = expected.merge(
        left,
        on=keys,
        how="outer",
        suffixes=("_expected", "_actual"),
        indicator=True,
        validate="one_to_one",
    )
    if not joined["_merge"].eq("both").all():
        errors.append("paired membership differs from independent replay")
        return errors
    bool_columns = {
        "mid_falling_member",
        "low_falling_member",
        "low_or_mid_falling_union_member",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        "base_operation_return_review_candidate_flag",
        "delayed_operation_return_review_candidate_flag",
        "paired_combined_exclusion_candidate_flag",
        "paired_sensitivity_included",
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
    }
    numeric_columns = {
        "latest_source_to_trigger_trading_days",
        "source_position_120d_pct",
        "source_shape_return20_pct",
        "source_shape_range23_pct",
        "source_shape_ema23_slope5_pct",
        "base_realized_return_pct",
        "delayed_realized_return_pct",
        "delayed_minus_base_return_pct_points",
    }
    string_columns = required - bool_columns - numeric_columns - set(keys)
    for column in sorted(string_columns):
        mismatches = int(
            (~joined[f"{column}_expected"].fillna("").astype(str).eq(
                joined[f"{column}_actual"].fillna("").astype(str)
            )).sum()
        )
        if mismatches:
            errors.append(f"paired {column} drift rows={mismatches}")
    for column in sorted(bool_columns):
        mismatches = int(
            (~_boolish(joined[f"{column}_expected"]).eq(
                _boolish(joined[f"{column}_actual"])
            )).sum()
        )
        if mismatches:
            errors.append(f"paired {column} drift rows={mismatches}")
    for column in sorted(numeric_columns):
        mismatches = sum(
            not _same_number(observed, expected_value)
            for observed, expected_value in zip(
                joined[f"{column}_actual"], joined[f"{column}_expected"]
            )
        )
        if mismatches:
            errors.append(f"paired {column} drift rows={mismatches}")
    return errors


def _compare_feature_contrast(
    contrast: pd.DataFrame,
    detail: pd.DataFrame,
    *,
    expected_artifact_version: str = ARTIFACT_VERSION,
) -> list[str]:
    errors = _governance_errors(
        contrast,
        "feature_contrast",
        _artifact_lineage(detail),
        expected_artifact_version=expected_artifact_version,
    )
    required_columns = {
        "analysis_basis",
        "lifecycle_policy_id",
        "confirmation_variant_id",
        "candidate_variant_order",
        "candidate_variant_id",
        "feature_order",
        "feature_id",
        "high_return_definition",
        "low_return_definition",
        "high_return_operation_count",
        "low_return_operation_count",
        "high_observed_count",
        "low_observed_count",
        "high_mean",
        "high_median",
        "low_mean",
        "low_median",
        "high_minus_low_mean",
        "standardized_mean_difference",
        "contrast_scope",
        "sample_policy",
        "anomaly_policy",
    }
    missing = sorted(required_columns - set(contrast.columns))
    if missing:
        errors.append(f"feature contrast is missing contract columns: {missing}")
        return errors
    required_keys = {
        (basis, lifecycle, confirmation, variant_id, feature_id)
        for basis in ANALYSIS_BASES
        for lifecycle in LIFECYCLE_POLICY_IDS
        for confirmation in CONFIRMATION_VARIANT_IDS
        for _variant_order, variant_id, _member in VARIANT_SPECS
        for _feature_order, feature_id in FEATURE_SPECS
    }
    observed_keys = set(
        zip(
            contrast["analysis_basis"].astype(str),
            contrast["lifecycle_policy_id"].astype(str),
            contrast["confirmation_variant_id"].astype(str),
            contrast["candidate_variant_id"].astype(str),
            contrast["feature_id"].astype(str),
        )
    )
    key_columns = [
        "analysis_basis",
        "lifecycle_policy_id",
        "confirmation_variant_id",
        "candidate_variant_id",
        "feature_id",
    ]
    if observed_keys != required_keys or contrast.duplicated(key_columns).any():
        errors.append("feature contrast grid differs from exact replay contract")
        return errors
    parts = {
        PRIMARY_ANALYSIS_BASIS: detail,
        SENSITIVITY_ANALYSIS_BASIS: detail.loc[
            _boolish(detail["sensitivity_included"])
        ],
    }
    variant_meta = {
        variant_id: (order, member)
        for order, variant_id, member in VARIANT_SPECS
    }
    feature_meta = {feature_id: order for order, feature_id in FEATURE_SPECS}
    for row in contrast.itertuples(index=False):
        basis = parts[str(row.analysis_basis)]
        lifecycle = str(row.lifecycle_policy_id)
        confirmation = str(row.confirmation_variant_id)
        variant = str(row.candidate_variant_id)
        feature = str(row.feature_id)
        variant_order, member = variant_meta[variant]
        part = basis.loc[
            basis["lifecycle_policy_id"].eq(lifecycle)
            & basis["confirmation_variant_id"].eq(confirmation)
            & _boolish(basis[member])
        ]
        returns = pd.to_numeric(part["realized_return_pct"], errors="coerce")
        high = part.loc[returns.ge(20.0)]
        low = part.loc[returns.le(0.0)]
        high_values = pd.to_numeric(high[feature], errors="coerce").dropna()
        low_values = pd.to_numeric(low[feature], errors="coerce").dropna()
        high_mean = _stat(high_values, "mean")
        low_mean = _stat(low_values, "mean")
        expected_metrics = {
            "high_return_operation_count": len(high),
            "low_return_operation_count": len(low),
            "high_observed_count": len(high_values),
            "low_observed_count": len(low_values),
            "high_mean": high_mean,
            "high_median": _stat(high_values, "median"),
            "low_mean": low_mean,
            "low_median": _stat(low_values, "median"),
            "high_minus_low_mean": (
                high_mean - low_mean
                if high_mean is not None and low_mean is not None
                else None
            ),
            "standardized_mean_difference": _standardized_mean_difference(
                high_values, low_values
            ),
        }
        label = (
            f"feature contrast {row.analysis_basis}/{lifecycle}/{confirmation}/"
            f"{variant}/{feature}"
        )
        _validate_metrics(row, expected_metrics, label, errors)
        exact = {
            "candidate_variant_order": variant_order,
            "feature_order": feature_meta[feature],
            "high_return_definition": "realized_return_pct>=20",
            "low_return_definition": "realized_return_pct<=0",
            "contrast_scope": (
                "descriptive_same_operation_contract_not_promotion_evidence"
            ),
            "sample_policy": SAMPLE_POLICY,
            "anomaly_policy": ANOMALY_POLICY,
        }
        for column, expected_value in exact.items():
            if str(getattr(row, column)) != str(expected_value):
                errors.append(f"{label} contract drift: {column}")
    return errors


def _validate_mirrors_and_markdown(paths: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    for name, path in paths.items():
        if not path.is_file():
            errors.append(f"artifact is missing: {name}={path}")
    if errors:
        return errors
    for family in ("summary", "detail", "paired", "contrast"):
        if not (
            paths[family].read_bytes()
            == paths[f"{family}_history"].read_bytes()
            == paths[f"{family}_docs"].read_bytes()
        ):
            errors.append(f"{family} latest/history/docs byte mirrors drift")
    if paths["markdown"].read_bytes() != paths["markdown_docs"].read_bytes():
        errors.append("markdown latest/docs byte mirrors drift")
    try:
        markdown = paths["markdown"].read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"markdown is not UTF-8: {exc}")
        return errors
    for token in (
        "research_only",
        "0～60",
        "D+1",
        "D+2",
        "anomaly candidates",
        "EPS",
    ):
        if token not in markdown:
            errors.append(f"markdown omits required explanation: {token}")
    return errors


def validate(
    *,
    artifact_root: Path = ROOT,
    source_root: Path = ROOT,
) -> list[str]:
    artifact_root = artifact_root.resolve()
    source_root = source_root.resolve()
    paths = {
        name: artifact_root / relative
        for name, relative in ARTIFACT_RELATIVE_PATHS.items()
    }
    errors = _validate_mirrors_and_markdown(paths)
    if errors:
        return errors
    try:
        current_manifest_path = source_root / SOURCE_RELATIVE_PATHS["projection_manifest"]
        if current_manifest_path.is_symlink() or not current_manifest_path.is_file():
            raise RuntimeError(
                f"canonical projection manifest is missing or unsafe: {current_manifest_path}"
            )
        current_manifest = pd.read_csv(
            current_manifest_path,
            dtype=str,
            keep_default_na=False,
        )
        if len(current_manifest) != 1 or "projection_version" not in current_manifest.columns:
            raise RuntimeError(
                "canonical projection manifest must have one row and projection_version"
            )
        projection_version = str(
            current_manifest.iloc[0]["projection_version"]
        ).strip()
        (
            expected_artifact_version,
            expected_rearmed_artifact_version,
            expected_position_shape_artifact_version,
        ) = _version_contract(projection_version)
        projection_manifest, source_raw, rearmed_raw = _read_sources(
            source_root,
            projection_version=projection_version,
        )
        errors.extend(_projection_binding_errors(projection_manifest, source_raw))
        if errors:
            return errors
        source = _prepare_source(source_raw)
        operations = _prepare_operations(
            rearmed_raw,
            expected_artifact_version=expected_rearmed_artifact_version,
        )
        if "stock_id" not in source_raw.columns:
            raise RuntimeError("source-first detail is missing stock_id for price manifest")
        expected_detail = _expected_detail(
            source,
            operations,
            source_root,
            {_stock_id(value) for value in source_raw["stock_id"]},
            trusted_revision=(
                TRUSTED_SOURCE_REVISION
                if source_root == ROOT
                and projection_version == V1_PROJECTION_VERSION
                else None
            ),
        )
        expected_detail.loc[:, "artifact_version"] = expected_artifact_version
        if "rearmed_artifact_version" in expected_detail.columns:
            expected_detail.loc[:, "rearmed_artifact_version"] = (
                expected_rearmed_artifact_version
            )
        if "position_shape_artifact_version" in expected_detail.columns:
            expected_detail.loc[:, "position_shape_artifact_version"] = (
                expected_position_shape_artifact_version
            )
        expected_paired = _expected_paired(
            expected_detail,
            expected_artifact_version=expected_artifact_version,
        )
        summary = pd.read_csv(
            paths["summary"], keep_default_na=False, low_memory=False
        )
        detail = pd.read_csv(
            paths["detail"],
            dtype={"stock_id": str},
            keep_default_na=False,
            low_memory=False,
        )
        paired = pd.read_csv(
            paths["paired"],
            dtype={"stock_id": str},
            keep_default_na=False,
            low_memory=False,
        )
        contrast = pd.read_csv(
            paths["contrast"], keep_default_na=False, low_memory=False
        )
        errors.extend(
            _compare_detail(
                detail,
                expected_detail,
                expected_artifact_version=expected_artifact_version,
            )
        )
        errors.extend(
            _compare_summary(
                summary,
                expected_detail,
                expected_artifact_version=expected_artifact_version,
            )
        )
        errors.extend(
            _compare_paired(
                paired,
                expected_paired,
                expected_artifact_version=expected_artifact_version,
            )
        )
        errors.extend(
            _compare_feature_contrast(
                contrast,
                expected_detail,
                expected_artifact_version=expected_artifact_version,
            )
        )
    except (
        RuntimeError,
        ValueError,
        KeyError,
        AttributeError,
        pd.errors.ParserError,
    ) as exc:
        errors.append(str(exc))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Independently validate the revenue low/mid falling candidate audit."
        )
    )
    parser.add_argument(
        "--artifact-root",
        type=Path,
        default=ROOT,
        help="Repository root containing generated candidate artifacts.",
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        default=ROOT,
        help="Repository root containing source-first/rearmed data and price history.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(artifact_root=args.artifact_root, source_root=args.source_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "revenue_unreacted_range low/mid falling candidate audit validation passed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
