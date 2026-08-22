from __future__ import annotations

from io import BytesIO
from itertools import product
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import subprocess

import pandas as pd

from revenue_unreacted_range_forward_confirmation_feature_audit import (
    OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
)
from revenue_unreacted_range_source_first_condition_audit import (
    ARTIFACT_ID as EXPECTED_SOURCE_ARTIFACT_ID,
    ARTIFACT_VERSION as EXPECTED_SOURCE_ARTIFACT_VERSION,
)
from revenue_unreacted_range_source_snapshot_projection import (
    LATEST_DETAIL_CSV as SOURCE_DETAIL_CSV,
    LATEST_MANIFEST_CSV as SOURCE_PROJECTION_MANIFEST_CSV,
    V1_PROJECTION_VERSION,
    V2_PROJECTION_VERSION,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    validate_projection_binding,
)
from revenue_unreacted_range_rearmed_operation_grid import (
    ANALYSIS_BASES,
    ARTIFACT_ID,
    ARTIFACT_VERSION,
    V2_ARTIFACT_VERSION,
    BASE_CONFIRMATION_RULE_ID,
    BASE_ENTRY_RULE_ID,
    BONUS_CONFIRMATION_RULE_ID,
    BONUS_ENTRY_RULE_ID,
    CONFIRMATION_SPECS,
    DETAIL_ARTIFACT_DROP_COLUMNS,
    DETAIL_CSV,
    DETAIL_MAX_BYTES,
    DOCS_CSV,
    DOCS_MD,
    DOCS_RETURN_REVIEW_CSV,
    FINANCIAL_STATEMENT_SCOPE,
    HISTORY_CSV,
    HISTORY_RETURN_REVIEW_CSV,
    HOLD_DAYS,
    LATEST_CSV,
    LATEST_MD,
    LIFECYCLE_SPECS,
    MODEL_ID,
    NO_STOP_POLICY_ID,
    OPERATION_RETURN_REVIEW_POLICY,
    PRICE_HISTORY_CUTOFF_DATE,
    PRIMARY_ANALYSIS_BASIS,
    RETURN_REVIEW_COLUMNS,
    RETURN_REVIEW_CSV,
    SENSITIVITY_ANALYSIS_BASIS,
    SOURCE_VARIANT_ID,
    STOP_POLICIES,
    STOP_POLICY_ID,
    STOP_RULE_ID,
    _grid_id,
    _overlap_pair_count,
)


ROOT = Path(__file__).resolve().parents[1]
PRICE_RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_price_comparability_resolution.csv"
)
PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
TRUSTED_SOURCE_REVISION = "b7ab7b6122b422e941efa3a3a1a915fbfcb59f4d"
SOURCE_DETAIL_RELATIVE_PATH = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
)
SOURCE_PROJECTION_MANIFEST_RELATIVE_PATH = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
PRICE_RESOLUTION_RELATIVE_PATH = (
    "config/revenue_unreacted_range_price_comparability_resolution.csv"
)
PRICE_HISTORY_RELATIVE_DIR = "data/stock_price_history"
PRICE_INPUT_COLUMNS = ("date", "open", "high", "low", "close", "volume", "volume_ratio")
CANONICAL_JSON_VERSION = "revenue_source_snapshot_projection_canonical_json_v1"

EXPECTED_V1_MANIFEST_DESCRIPTOR = {
    "model_id": "revenue_unreacted_range",
    "artifact_id": "revenue_unreacted_range_source_snapshot_projection",
    "artifact_version": "source_snapshot_projection_v1_20260731",
    "projection_id": "revenue_unreacted_range_source_snapshot_asof_20260713",
    "projection_version": "source_snapshot_projection_v1_20260731",
    "projection_policy_id": (
        "raw_source_and_price_truncated_before_source_first_episode_assembly_v1"
    ),
    "cutoff_date": "20260713",
    "full_source_artifact_id": EXPECTED_SOURCE_ARTIFACT_ID,
    "full_source_artifact_version": EXPECTED_SOURCE_ARTIFACT_VERSION,
    "projected_max_source_date": "20260617",
    "projected_max_trade_date": "20260629",
    "projected_max_episode_end_date": "20260713",
    "research_only": "True",
    "formal_model_use_allowed": "False",
    "approved_for_daily": "False",
    "production_change": "False",
}

_TRUSTED_TREE_CACHE: dict[str, dict[str, tuple[str, str, str]]] = {}
_TRUSTED_BLOB_CACHE: dict[tuple[str, str], bytes] = {}

ARTIFACT_VERSION_BY_PROJECTION = {
    V1_PROJECTION_VERSION: ARTIFACT_VERSION,
    V2_PROJECTION_VERSION: V2_ARTIFACT_VERSION,
}


def _expected_artifact_version(projection_version: object) -> str:
    version = str(projection_version).strip()
    try:
        return ARTIFACT_VERSION_BY_PROJECTION[version]
    except KeyError as exc:
        raise RuntimeError(
            f"unsupported canonical source projection version: {version or '<empty>'}"
        ) from exc


def _canonical_source_frames() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    current_manifest = load_source_snapshot_projection_manifest(
        SOURCE_PROJECTION_MANIFEST_CSV
    )
    projection_version = str(current_manifest.iloc[0]["projection_version"]).strip()
    _expected_artifact_version(projection_version)
    if projection_version == V1_PROJECTION_VERSION:
        return _trusted_source_frames()
    source = load_projected_source_detail(SOURCE_DETAIL_CSV)
    validate_projection_binding(current_manifest, source)
    if not PRICE_RESOLUTION_CSV.is_file():
        raise RuntimeError(
            f"canonical price comparability resolution is missing: {PRICE_RESOLUTION_CSV}"
        )
    resolutions = pd.read_csv(
        PRICE_RESOLUTION_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    return current_manifest, source, resolutions

def _current_price_frames(
    stock_ids: set[str], manifest: pd.DataFrame
) -> dict[str, pd.DataFrame]:
    projection_version = str(manifest.iloc[0]["projection_version"]).strip()
    _expected_artifact_version(projection_version)
    if projection_version == V1_PROJECTION_VERSION:
        return _trusted_price_frames(stock_ids, manifest)
    descriptors = _price_descriptors(manifest) if projection_version == V2_PROJECTION_VERSION else {}
    if projection_version == V2_PROJECTION_VERSION:
        missing_descriptors = sorted(stock_ids - set(descriptors))
        if missing_descriptors:
            raise RuntimeError(
                f"canonical v2 price descriptors omit stocks: {missing_descriptors[:5]}"
            )
    frames: dict[str, pd.DataFrame] = {}
    for stock_id in sorted(stock_ids):
        normalized = str(stock_id).strip()
        if re.fullmatch(r"\d{4,6}", normalized) is None:
            raise RuntimeError(f"canonical source has unsafe stock id: {stock_id!r}")
        path = PRICE_HISTORY_DIR / f"{normalized}.csv"
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"canonical price history is missing or unsafe: {path}")
        raw = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
        missing = sorted(set(PRICE_INPUT_COLUMNS) - set(raw.columns))
        if missing:
            raise RuntimeError(
                f"canonical price CSV is missing columns: {stock_id}: {missing}"
            )
        frame = raw.loc[:, list(PRICE_INPUT_COLUMNS)].copy()
        dates = frame["date"].astype(str).str.strip()
        numeric_export = dates.str.extract(r"^(\d{8})\.0+$", expand=False)
        dates = dates.where(dates.str.fullmatch(r"\d{8}"), numeric_export)
        if dates.isna().any():
            raise RuntimeError(f"canonical price CSV has invalid dates: {stock_id}")
        frame["date"] = dates
        frame = frame.loc[frame["date"].le(PRICE_HISTORY_CUTOFF_DATE)].copy()
        if frame.empty or frame["date"].duplicated().any():
            raise RuntimeError(
                f"canonical price CSV has empty or duplicate cutoff dates: {stock_id}"
            )
        frame = frame.sort_values("date", kind="mergesort").reset_index(drop=True)
        if projection_version == V2_PROJECTION_VERSION:
            rows = [
                [_payload_value(value) for value in values]
                for values in frame.loc[:, list(PRICE_INPUT_COLUMNS)].itertuples(
                    index=False, name=None
                )
            ]
            rows.sort()
            encoded = json.dumps(
                [CANONICAL_JSON_VERSION, list(PRICE_INPUT_COLUMNS), rows],
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
            expected_rows, expected_sha = descriptors[normalized]
            if len(frame) != expected_rows or hashlib.sha256(encoded).hexdigest() != expected_sha:
                raise RuntimeError(
                    f"canonical v2 price CSV descriptor drift: {normalized}"
                )
        frames[normalized] = frame
    return frames


def _git(*args: str, input_bytes: bytes | None = None) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "--no-replace-objects", "-C", str(ROOT), *args],
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def _safe_repo_path(relative_path: str) -> str:
    if "\\" in relative_path or not relative_path:
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
    return f"{PRICE_HISTORY_RELATIVE_DIR}/{normalized}.csv"


def _trusted_revision_preflight() -> None:
    revision = TRUSTED_SOURCE_REVISION
    if re.fullmatch(r"[0-9a-f]{40}", revision) is None:
        raise RuntimeError(f"trusted v1 revision is not a lowercase 40-character SHA: {revision}")
    resolved = _git("rev-parse", "--verify", f"{revision}^{{commit}}")
    if resolved.returncode != 0:
        detail = resolved.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"trusted v1 commit is unavailable: {revision}: {detail}")
    observed = resolved.stdout.decode("ascii", errors="strict").strip()
    if observed != revision:
        raise RuntimeError(
            f"trusted v1 revision does not resolve to its exact SHA: {observed} != {revision}"
        )
    ancestor = _git("merge-base", "--is-ancestor", revision, "HEAD")
    if ancestor.returncode != 0:
        detail = ancestor.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            f"trusted v1 revision is not an ancestor of HEAD: {revision}: {detail}"
        )


def _trusted_tree() -> dict[str, tuple[str, str, str]]:
    cached = _TRUSTED_TREE_CACHE.get(TRUSTED_SOURCE_REVISION)
    if cached is not None:
        return cached
    result = _git("ls-tree", "-r", "-z", TRUSTED_SOURCE_REVISION)
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"trusted v1 Git tree is unreadable: {detail}")
    entries: dict[str, tuple[str, str, str]] = {}
    for raw_entry in result.stdout.split(b"\0"):
        if not raw_entry:
            continue
        try:
            metadata, raw_path = raw_entry.split(b"\t", 1)
            mode, object_type, oid = metadata.decode("ascii").split(" ")
            repo_path = raw_path.decode("utf-8", errors="strict")
        except (ValueError, UnicodeDecodeError) as exc:
            raise RuntimeError("trusted v1 Git tree contains malformed metadata") from exc
        entries[repo_path] = (mode, object_type, oid)
    _TRUSTED_TREE_CACHE[TRUSTED_SOURCE_REVISION] = entries
    return entries


def _trusted_blobs(relative_paths: set[str]) -> dict[str, bytes]:
    normalized_paths = {_safe_repo_path(path) for path in relative_paths}
    missing_from_cache = sorted(
        path
        for path in normalized_paths
        if (TRUSTED_SOURCE_REVISION, path) not in _TRUSTED_BLOB_CACHE
    )
    if missing_from_cache:
        tree = _trusted_tree()
        oids: list[str] = []
        for path in missing_from_cache:
            entry = tree.get(path)
            if entry is None:
                raise RuntimeError(
                    f"trusted v1 Git blob is missing: {TRUSTED_SOURCE_REVISION}:{path}"
                )
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
        result = _git("cat-file", "--batch", input_bytes=("\n".join(oids) + "\n").encode("ascii"))
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(f"trusted v1 Git blobs are unreadable: {detail}")
        cursor = 0
        for path, expected_oid in zip(missing_from_cache, oids):
            newline = result.stdout.find(b"\n", cursor)
            if newline < 0:
                raise RuntimeError(f"trusted v1 Git blob header is missing: {path}")
            header = result.stdout[cursor:newline].decode("ascii", errors="strict").split(" ")
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
            _TRUSTED_BLOB_CACHE[(TRUSTED_SOURCE_REVISION, path)] = result.stdout[start:end]
            cursor = end + 1
        if cursor != len(result.stdout):
            raise RuntimeError("trusted v1 Git blob batch contains trailing bytes")
    return {
        path: _TRUSTED_BLOB_CACHE[(TRUSTED_SOURCE_REVISION, path)]
        for path in normalized_paths
    }


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


def _payload_value(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value).strip()
    return text.lower() if text.lower() in {"true", "false"} else text


def _price_descriptors(manifest: pd.DataFrame) -> dict[str, tuple[int, str]]:
    row = manifest.iloc[0]
    required = {
        "cutoff_price_input_stock_count",
        "cutoff_price_input_row_count",
        "cutoff_price_input_file_semantic_sha256s",
    }
    missing = sorted(required - set(manifest.columns))
    if missing:
        raise RuntimeError(f"trusted v1 projection manifest is missing price lineage: {missing}")
    descriptors: dict[str, tuple[int, str]] = {}
    total_rows = 0
    for token in str(row["cutoff_price_input_file_semantic_sha256s"]).split("|"):
        fields = token.split(":")
        if len(fields) != 3:
            raise RuntimeError("trusted v1 price descriptor is malformed")
        stock_id, row_count_text, semantic_sha = fields
        _trusted_stock_path(stock_id)
        if stock_id in descriptors or re.fullmatch(r"\d+", row_count_text) is None:
            raise RuntimeError(f"trusted v1 price descriptor identity drift: {token}")
        if re.fullmatch(r"[0-9a-f]{64}", semantic_sha) is None:
            raise RuntimeError(f"trusted v1 price descriptor SHA-256 drift: {stock_id}")
        row_count = int(row_count_text)
        descriptors[stock_id] = (row_count, semantic_sha)
        total_rows += row_count
    if len(descriptors) != int(str(row["cutoff_price_input_stock_count"])):
        raise RuntimeError("trusted v1 price descriptor stock count drift")
    if total_rows != int(str(row["cutoff_price_input_row_count"])):
        raise RuntimeError("trusted v1 price descriptor row count drift")
    return descriptors


def _trusted_price_frames(
    stock_ids: set[str], manifest: pd.DataFrame
) -> dict[str, pd.DataFrame]:
    descriptors = _price_descriptors(manifest)
    missing_descriptors = sorted(stock_ids - set(descriptors))
    if missing_descriptors:
        raise RuntimeError(
            f"trusted v1 price descriptors omit stocks: {missing_descriptors[:5]}"
        )
    paths = {_trusted_stock_path(stock_id) for stock_id in stock_ids}
    payloads = _trusted_blobs(paths)
    frames: dict[str, pd.DataFrame] = {}
    for stock_id in sorted(stock_ids):
        relative_path = _trusted_stock_path(stock_id)
        try:
            raw = pd.read_csv(
                BytesIO(payloads[relative_path]),
                dtype=str,
                keep_default_na=False,
                low_memory=False,
            )
        except (UnicodeDecodeError, pd.errors.ParserError) as exc:
            raise RuntimeError(
                f"trusted v1 price CSV is unreadable: {stock_id}: {exc}"
            ) from exc
        missing = sorted(set(PRICE_INPUT_COLUMNS) - set(raw.columns))
        if missing:
            raise RuntimeError(
                f"trusted v1 price CSV is missing columns: {stock_id}: {missing}"
            )
        frame = raw.loc[:, list(PRICE_INPUT_COLUMNS)].copy()
        dates = frame["date"].astype(str).str.strip()
        numeric_export = dates.str.extract(r"^(\d{8})\.0+$", expand=False)
        dates = dates.where(dates.str.fullmatch(r"\d{8}"), numeric_export)
        if dates.isna().any():
            raise RuntimeError(f"trusted v1 price CSV has invalid dates: {stock_id}")
        frame["date"] = dates
        frame = frame.loc[frame["date"].le(PRICE_HISTORY_CUTOFF_DATE)].copy()
        if frame.empty or frame["date"].duplicated().any():
            raise RuntimeError(
                f"trusted v1 price CSV has empty or duplicate cutoff dates: {stock_id}"
            )
        frame = frame.sort_values("date", kind="mergesort").reset_index(drop=True)
        rows = [
            [_payload_value(value) for value in values]
            for values in frame.loc[:, list(PRICE_INPUT_COLUMNS)].itertuples(
                index=False, name=None
            )
        ]
        rows.sort()
        encoded = json.dumps(
            [CANONICAL_JSON_VERSION, list(PRICE_INPUT_COLUMNS), rows],
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
        semantic_sha = hashlib.sha256(encoded).hexdigest()
        expected_rows, expected_sha = descriptors[stock_id]
        if len(frame) != expected_rows or semantic_sha != expected_sha:
            raise RuntimeError(
                "trusted v1 price CSV does not match its manifest descriptor: "
                f"{stock_id}"
            )
        frames[stock_id] = frame
    return frames


def _trusted_source_frames() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    _trusted_revision_preflight()
    payloads = _trusted_blobs(
        {
            SOURCE_DETAIL_RELATIVE_PATH,
            SOURCE_PROJECTION_MANIFEST_RELATIVE_PATH,
            PRICE_RESOLUTION_RELATIVE_PATH,
        }
    )
    try:
        source = pd.read_csv(
            BytesIO(payloads[SOURCE_DETAIL_RELATIVE_PATH]),
            dtype={"stock_id": str},
            keep_default_na=False,
            low_memory=False,
        )
        manifest = pd.read_csv(
            BytesIO(payloads[SOURCE_PROJECTION_MANIFEST_RELATIVE_PATH]),
            dtype=str,
            keep_default_na=False,
        )
        resolutions = pd.read_csv(
            BytesIO(payloads[PRICE_RESOLUTION_RELATIVE_PATH]),
            dtype={"stock_id": str},
            keep_default_na=False,
        )
    except (UnicodeDecodeError, pd.errors.ParserError) as exc:
        raise RuntimeError(f"trusted v1 source CSV is unreadable: {exc}") from exc
    _validate_v1_manifest_descriptor(manifest)
    return manifest, source, resolutions

def _source_lineage_errors(source: pd.DataFrame) -> list[str]:
    missing = sorted({"artifact_id", "artifact_version"} - set(source.columns))
    if missing:
        return [f"rearmed operation grid source lineage is missing columns: {missing}"]
    errors: list[str] = []
    if set(source["artifact_id"].astype(str)) != {EXPECTED_SOURCE_ARTIFACT_ID}:
        errors.append("rearmed operation grid source artifact id drift")
    if set(source["artifact_version"].astype(str)) != {
        EXPECTED_SOURCE_ARTIFACT_VERSION
    }:
        errors.append("rearmed operation grid source artifact version drift")
    return errors


SUMMARY_REQUIRED = {
    "model_id",
    "artifact_id",
    "artifact_version",
    "source_artifact_id",
    "source_variant_id",
    "analysis_basis",
    "grid_id",
    "lifecycle_policy_id",
    "confirmation_variant_id",
    "confirmation_information_cutoff",
    "entry_rule_id",
    "bonus_id",
    "bonus_timing_role",
    "holding_days",
    "stop_policy_id",
    "stop_rule_id",
    "stop_rule",
    "source_episode_count",
    "selected_operation_count",
    "mature_operation_count",
    "right_censored_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "realized_return_ge20_rate_pct",
    "strict_launch_success_rate_pct",
    "rearmed_operation_count",
    "same_stock_overlap_pair_count",
    "operation_return_review_candidate_count",
    "known_4916_trigger_dates",
    "known_1303_trigger_dates",
    "operation_return_review_policy",
    "same_stock_non_overlap_policy",
    "financial_statement_scope",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
}

DETAIL_REQUIRED = {
    "model_id",
    "artifact_id",
    "artifact_version",
    "source_artifact_id",
    "source_variant_id",
    "grid_id",
    "lifecycle_policy_id",
    "confirmation_variant_id",
    "confirmation_information_cutoff",
    "base_confirmation_rule_id",
    "bonus_id",
    "entry_rule_id",
    "holding_days",
    "stop_policy_id",
    "stop_rule_id",
    "episode_key",
    "stock_id",
    "stock_trade_sequence",
    "episode_trade_sequence",
    "rearmed_trade_flag",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "entry_price",
    "planned_exit_date",
    "exit_date",
    "exit_price",
    "exit_price_basis",
    "exit_reason",
    "stop_confirmation_date",
    "realized_return_pct",
    "return_outcome",
    "return_valid",
    "right_censored",
    "next_day_continuation_observed",
    "next_day_continuation_hit",
    "operation_return_review_candidate_flag",
    "source_anomaly_candidate_flag",
    "trigger_price_basis",
    "confirmation_price_basis",
    "entry_price_basis",
    "stop_confirmation_price_basis",
    "fixed_exit_price_basis",
    "intraday_operation_basis_used",
    "approved_for_daily",
    "production_change",
}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _expected_rate(count: int, total: int) -> float | None:
    return count / total * 100.0 if total else None


def _same_number(observed: object, expected: float | None, tolerance: float = 0.00011) -> bool:
    value = _number(observed)
    if expected is None:
        return value is None
    return value is not None and math.isclose(value, expected, abs_tol=tolerance)


def _governance(
    name: str,
    frame: pd.DataFrame,
    errors: list[str],
    *,
    expected_artifact_version: str = ARTIFACT_VERSION,
) -> None:
    if frame.empty:
        return
    if set(frame["model_id"].astype(str)) != {MODEL_ID}:
        errors.append(f"rearmed operation grid {name} model_id drift")
    if set(frame["artifact_id"].astype(str)) != {ARTIFACT_ID}:
        errors.append(f"rearmed operation grid {name} artifact_id drift")
    if set(frame["artifact_version"].astype(str)) != {expected_artifact_version}:
        errors.append(f"rearmed operation grid {name} artifact_version drift")
    if _boolish(frame["approved_for_daily"]).any():
        errors.append(f"rearmed operation grid {name} must remain research-only")
    if _boolish(frame["production_change"]).any():
        errors.append(f"rearmed operation grid {name} must not change production")


DateIndex = tuple[dict[str, int], tuple[str, ...]]


def _date_indices(
    stock_ids: set[str],
    *,
    manifest: pd.DataFrame,
) -> dict[str, DateIndex]:
    output: dict[str, DateIndex] = {}
    trusted_frames = _current_price_frames(stock_ids, manifest)
    for stock_id in sorted(stock_ids):
        dates = trusted_frames[stock_id]["date"]
        ordered_dates = tuple(dates.tolist())
        output[stock_id] = (
            {date: index for index, date in enumerate(ordered_dates)},
            ordered_dates,
        )
    return output


def _offset_date(index_data: DateIndex, date: str, offset: int) -> str:
    indices, dates = index_data
    if date not in indices:
        return ""
    target = indices[date] + offset
    return dates[target] if 0 <= target < len(dates) else ""


def _validate_timing(
    detail: pd.DataFrame,
    errors: list[str],
    *,
    manifest: pd.DataFrame,
) -> None:
    indices_by_stock = _date_indices(
        set(detail["stock_id"].astype(str)),
        manifest=manifest,
    )
    for row in detail.itertuples(index=False):
        stock_indices = indices_by_stock.get(str(row.stock_id), ({}, ()))
        trigger_date = str(row.trigger_date)
        if row.confirmation_variant_id == "base_close_confirmed":
            expected_confirmation = trigger_date
            expected_entry = _offset_date(stock_indices, trigger_date, 1)
            if row.entry_rule_id != BASE_ENTRY_RULE_ID:
                errors.append(f"rearmed operation grid base entry rule drift: {row.grid_id}")
        else:
            expected_confirmation = _offset_date(stock_indices, trigger_date, 1)
            expected_entry = _offset_date(stock_indices, trigger_date, 2)
            if row.entry_rule_id != BONUS_ENTRY_RULE_ID:
                errors.append(f"rearmed operation grid delayed entry rule drift: {row.grid_id}")
            if not bool(_boolish(pd.Series([row.next_day_continuation_hit])).iloc[0]):
                errors.append(
                    f"rearmed operation grid delayed bonus lacks next-close continuation: {row.stock_id}/{trigger_date}"
                )
        if str(row.confirmation_date) != expected_confirmation:
            errors.append(
                f"rearmed operation grid confirmation timing drift: {row.stock_id}/{trigger_date}/{row.confirmation_variant_id}"
            )
        observed_entry = str(row.entry_date)
        if observed_entry != expected_entry:
            errors.append(
                f"rearmed operation grid entry timing drift: {row.stock_id}/{trigger_date}/{row.confirmation_variant_id}"
            )
        if not bool(_boolish(pd.Series([row.return_valid])).iloc[0]):
            continue
        expected_planned_exit = _offset_date(
            stock_indices, observed_entry, int(row.holding_days) - 1
        )
        if str(row.planned_exit_date) != expected_planned_exit:
            errors.append(
                f"rearmed operation grid planned exit timing drift: {row.stock_id}/{observed_entry}/{row.holding_days}"
            )
        if row.exit_reason == STOP_RULE_ID:
            expected_stop_exit = _offset_date(
                stock_indices, str(row.stop_confirmation_date), 1
            )
            if str(row.exit_date) != expected_stop_exit:
                errors.append(
                    f"rearmed operation grid stop execution timing drift: {row.stock_id}/{row.stop_confirmation_date}"
                )
            if row.exit_price_basis != "next_trading_day_open_after_stop_close_confirmation":
                errors.append("rearmed operation grid stop exit price basis drift")
        elif str(row.exit_date) != expected_planned_exit or row.exit_price_basis != "fixed_future_close":
            errors.append(
                f"rearmed operation grid fixed exit timing or price basis drift: {row.stock_id}/{observed_entry}"
            )


def validate() -> list[str]:
    errors: list[str] = []
    paths = (
        LATEST_CSV,
        DETAIL_CSV,
        RETURN_REVIEW_CSV,
        LATEST_MD,
        HISTORY_CSV,
        HISTORY_RETURN_REVIEW_CSV,
        DOCS_CSV,
        DOCS_RETURN_REVIEW_CSV,
        DOCS_MD,
    )
    for path in paths:
        if not path.is_file():
            errors.append(f"rearmed operation grid artifact is missing: {path}")
    if errors:
        return errors
    if DETAIL_CSV.stat().st_size >= DETAIL_MAX_BYTES:
        errors.append("rearmed operation grid detail exceeds the Git-safe 50 MB policy")

    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={
            "stock_id": str,
            "episode_start_trade_date": str,
            "episode_end_date": str,
            "trigger_date": str,
            "confirmation_date": str,
            "entry_date": str,
            "planned_exit_date": str,
            "exit_date": str,
            "stop_confirmation_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )
    review = pd.read_csv(
        RETURN_REVIEW_CSV,
        dtype={"stock_id": str, "entry_date": str, "exit_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    try:
        source_projection_manifest, source, price_resolutions = _canonical_source_frames()
    except (RuntimeError, ValueError, KeyError, UnicodeDecodeError) as exc:
        return [str(exc)]
    try:
        validate_projection_binding(source_projection_manifest, source)
    except RuntimeError as exc:
        errors.append(str(exc))
    errors.extend(_source_lineage_errors(source))
    try:
        expected_artifact_version = _expected_artifact_version(
            source_projection_manifest.iloc[0]["projection_version"]
        )
    except (IndexError, KeyError, RuntimeError) as exc:
        errors.append(str(exc))
        return errors
    source = source.loc[source["condition_variant_id"].eq(SOURCE_VARIANT_ID)].copy()
    avision = price_resolutions.loc[
        price_resolutions["resolution_id"].eq(
            "2380_20260629_loss_offset_capital_reduction"
        )
    ]
    if len(avision) != 1:
        errors.append("rearmed operation grid 2380 capital-reduction resolution is missing")
    else:
        resolution = avision.iloc[0]
        ratio = pd.to_numeric(resolution["exchange_ratio"], errors="coerce")
        pre_close = pd.to_numeric(resolution["pre_event_close"], errors="coerce")
        reference = pd.to_numeric(resolution["resume_reference_price"], errors="coerce")
        if not pd.notna(ratio) or abs(pre_close / ratio - reference) > 0.005:
            errors.append("rearmed operation grid 2380 capital-reduction adjustment math drift")
        if resolution["approved_scope"] != "revenue_unreacted_range_model_owned_research_only":
            errors.append("rearmed operation grid 2380 resolution scope drift")

    for name, frame, required in (
        ("summary", summary, SUMMARY_REQUIRED),
        ("detail", detail, DETAIL_REQUIRED),
        ("operation return review", review, set(RETURN_REVIEW_COLUMNS)),
    ):
        missing = sorted(required - set(frame.columns))
        if missing:
            errors.append(f"rearmed operation grid {name} schema is missing columns: {missing}")
    if errors:
        return errors

    _governance(
        "summary", summary, errors,
        expected_artifact_version=expected_artifact_version,
    )
    _governance(
        "detail", detail, errors,
        expected_artifact_version=expected_artifact_version,
    )
    _governance(
        "operation return review", review, errors,
        expected_artifact_version=expected_artifact_version,
    )
    expected_grid_ids = {
        _grid_id(lifecycle, confirmation, hold_days, stop_policy)
        for lifecycle, confirmation, hold_days, stop_policy in product(
            LIFECYCLE_SPECS, CONFIRMATION_SPECS, HOLD_DAYS, STOP_POLICIES
        )
    }
    expected_summary = {
        (analysis_basis, grid_id)
        for analysis_basis, grid_id in product(ANALYSIS_BASES, expected_grid_ids)
    }
    if set(zip(summary["analysis_basis"], summary["grid_id"])) != expected_summary:
        errors.append("rearmed operation grid summary basis/grid coverage drift")
    if set(detail["grid_id"]) != expected_grid_ids:
        errors.append("rearmed operation grid detail grid coverage drift")
    if detail.duplicated(["grid_id", "stock_id", "episode_key", "trigger_date", "entry_date"]).any():
        errors.append("rearmed operation grid detail contains duplicate operations")
    if set(detail["base_confirmation_rule_id"]) != {BASE_CONFIRMATION_RULE_ID}:
        errors.append("rearmed operation grid base confirmation rule drift")
    if set(detail["source_variant_id"]) != {SOURCE_VARIANT_ID}:
        errors.append("rearmed operation grid source variant drift")
    if set(summary["financial_statement_scope"]) != {FINANCIAL_STATEMENT_SCOPE}:
        errors.append("rearmed operation grid monthly revenue and financial statement boundary drift")
    repeated_columns = sorted(set(DETAIL_ARTIFACT_DROP_COLUMNS) & set(detail.columns))
    if repeated_columns:
        errors.append(
            f"rearmed operation grid detail repeats summary/spec contract prose: {repeated_columns}"
        )
    if _boolish(detail["intraday_operation_basis_used"]).any():
        errors.append("rearmed operation grid uses intraday operation basis")
    for column, expected in (
        ("trigger_price_basis", "analysis_close"),
        ("confirmation_price_basis", "analysis_close"),
        ("entry_price_basis", "analysis_open"),
        ("stop_confirmation_price_basis", "analysis_close"),
        ("fixed_exit_price_basis", "analysis_close"),
    ):
        if set(detail[column].astype(str)) != {expected}:
            errors.append(f"rearmed operation grid price basis drift: {column}")
    if not summary["operation_return_review_policy"].eq(OPERATION_RETURN_REVIEW_POLICY).all():
        errors.append("rearmed operation grid return review policy drift")
    if _overlap_pair_count(detail) != 0:
        errors.append("rearmed operation grid contains same-stock overlapping operations")
    if not pd.to_numeric(
        summary["same_stock_overlap_pair_count"], errors="coerce"
    ).eq(0).all():
        errors.append("rearmed operation grid summary overlap count drift")

    benchmark = detail.loc[detail["lifecycle_policy_id"].eq("episode_first_match_once")]
    if benchmark.groupby(["grid_id", "stock_id", "episode_key"]).size().gt(1).any():
        errors.append("rearmed operation grid first-match benchmark selects more than once per episode")
    adopted = detail.loc[
        detail["lifecycle_policy_id"].eq("rearm_after_realized_exit_next_trade_day")
    ]
    for _, part in adopted.groupby(["grid_id", "stock_id"], sort=False):
        part = part.sort_values("stock_trade_sequence", kind="mergesort")
        expected_sequence = list(range(1, len(part) + 1))
        if list(pd.to_numeric(part["stock_trade_sequence"], errors="coerce")) != expected_sequence:
            errors.append("rearmed operation grid stock sequence is not contiguous")
        expected_flags = [sequence > 1 for sequence in expected_sequence]
        if list(_boolish(part["rearmed_trade_flag"])) != expected_flags:
            errors.append("rearmed operation grid rearmed flag drift")
        valid = part.loc[
            part["entry_date"].astype(str).str.fullmatch(r"\d{8}")
            & part["exit_date"].astype(str).str.fullmatch(r"\d{8}")
        ]
        previous_exit = ""
        for row in valid.itertuples(index=False):
            if previous_exit and str(row.entry_date) <= previous_exit:
                errors.append("rearmed operation grid starts before the prior realized exit")
            previous_exit = str(row.exit_date)

    try:
        _validate_timing(detail, errors, manifest=source_projection_manifest)
    except (RuntimeError, ValueError, KeyError, UnicodeDecodeError) as exc:
        errors.append(str(exc))

    source_anomaly = _boolish(source["qualifying_source_revenue_anomaly_candidate_flag"]) | _boolish(
        source["unresolved_price_path_candidate_flag"]
    )
    for row in summary.itertuples(index=False):
        part = detail.loc[detail["grid_id"].eq(row.grid_id)].copy()
        expected_source_count = len(source)
        if row.analysis_basis == SENSITIVITY_ANALYSIS_BASIS:
            part = part.loc[
                ~_boolish(part["source_anomaly_candidate_flag"])
                & ~_boolish(part["operation_return_review_candidate_flag"])
            ]
            expected_source_count = int((~source_anomaly).sum())
        mature = part.loc[_boolish(part["return_valid"])]
        outcomes = mature["return_outcome"].astype(str)
        counts = {
            "win": int(outcomes.eq("win").sum()),
            "neutral": int(outcomes.eq("neutral").sum()),
            "failure": int(outcomes.eq("failure").sum()),
        }
        if int(row.source_episode_count) != expected_source_count:
            errors.append(f"rearmed operation grid source count drift: {row.analysis_basis}/{row.grid_id}")
        if int(row.selected_operation_count) != len(part) or int(row.mature_operation_count) != len(mature):
            errors.append(f"rearmed operation grid operation count drift: {row.analysis_basis}/{row.grid_id}")
        for outcome, column in (
            ("win", "win_rate_pct"),
            ("neutral", "neutral_rate_pct"),
            ("failure", "failure_rate_pct"),
        ):
            if not _same_number(getattr(row, column), _expected_rate(counts[outcome], len(mature))):
                errors.append(
                    f"rearmed operation grid {outcome} rate drift: {row.analysis_basis}/{row.grid_id}"
                )
        returns = pd.to_numeric(mature["realized_return_pct"], errors="coerce").dropna()
        expected_average = float(returns.mean()) if len(returns) else None
        expected_median = float(returns.median()) if len(returns) else None
        if not _same_number(row.avg_return_pct, expected_average):
            errors.append(f"rearmed operation grid average return drift: {row.analysis_basis}/{row.grid_id}")
        if not _same_number(row.median_return_pct, expected_median):
            errors.append(f"rearmed operation grid median return drift: {row.analysis_basis}/{row.grid_id}")

    review_detail = detail.loc[_boolish(detail["operation_return_review_candidate_flag"])]
    expected_review_keys = set(
        zip(
            review_detail["stock_id"],
            review_detail["entry_date"],
            review_detail["exit_date"],
            review_detail["exit_price_basis"],
        )
    )
    observed_review_keys = set(
        zip(review["stock_id"], review["entry_date"], review["exit_date"], review["exit_price_basis"])
    )
    if expected_review_keys != observed_review_keys:
        errors.append("rearmed operation grid return review coverage drift")
    review_returns = pd.to_numeric(review["realized_return_pct"], errors="coerce")
    if review_returns.isna().any() or not review_returns.abs().ge(
        OPERATION_RETURN_REVIEW_THRESHOLD_PCT
    ).all():
        errors.append("rearmed operation grid return review threshold drift")
    replayed = pd.to_numeric(review["replayed_realized_return_pct"], errors="coerce")
    if replayed.isna().any() or not (replayed - review_returns).abs().le(0.0001).all():
        errors.append("rearmed operation grid return review replay drift")
    if not _boolish(review["included_in_primary_metrics"]).all():
        errors.append("rearmed operation grid review candidates must remain in primary metrics")
    if not _boolish(review["excluded_in_review_candidate_sensitivity"]).all():
        errors.append("rearmed operation grid review sensitivity exclusion drift")
    if not review["review_disposition"].eq(
        "unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly"
    ).all():
        errors.append("rearmed operation grid review candidates received an anomaly disposition")

    adopted_base = detail.loc[
        detail["lifecycle_policy_id"].eq("rearm_after_realized_exit_next_trade_day")
        & detail["confirmation_variant_id"].eq("base_close_confirmed")
        & detail["holding_days"].eq(20)
        & detail["stop_policy_id"].eq(NO_STOP_POLICY_ID)
    ]
    triggers_4916 = set(adopted_base.loc[adopted_base["stock_id"].eq("4916"), "trigger_date"])
    if not {"20251209", "20260518"}.issubset(triggers_4916):
        errors.append("rearmed operation grid does not preserve both known 4916 trigger episodes")
    if "20260527" not in set(
        adopted_base.loc[adopted_base["stock_id"].eq("1303"), "trigger_date"]
    ):
        errors.append("rearmed operation grid base confirmation omits known 1303 success")
    delayed = detail.loc[
        detail["lifecycle_policy_id"].eq("rearm_after_realized_exit_next_trade_day")
        & detail["confirmation_variant_id"].eq("delayed_next_close_continuation_bonus")
        & detail["holding_days"].eq(20)
        & detail["stop_policy_id"].eq(NO_STOP_POLICY_ID)
        & detail["stock_id"].eq("1303")
        & detail["trigger_date"].eq("20260527")
    ]
    if not delayed.empty:
        errors.append("rearmed operation grid incorrectly treats 1303 next-day continuation as a hard gate hit")

    if LATEST_CSV.read_bytes() != HISTORY_CSV.read_bytes() or LATEST_CSV.read_bytes() != DOCS_CSV.read_bytes():
        errors.append("rearmed operation grid summary mirrors drift")
    if RETURN_REVIEW_CSV.read_bytes() != HISTORY_RETURN_REVIEW_CSV.read_bytes() or RETURN_REVIEW_CSV.read_bytes() != DOCS_RETURN_REVIEW_CSV.read_bytes():
        errors.append("rearmed operation grid return review mirrors drift")
    if LATEST_MD.read_bytes() != DOCS_MD.read_bytes():
        errors.append("rearmed operation grid markdown mirror drift")
    markdown = LATEST_MD.read_text(encoding="utf-8")
    for token in (
        "重新武裝操作矩陣",
        "訊號日收盤首次突破前 20 日最高收盤，且 MA60 > MA120",
        "D+2 開盤進場",
        "同股操作不得重疊",
        "高低報酬只觸發查核，不直接判定異常",
        "EPS、毛利率、營益率、營業利益、業外、淨利均未納入",
    ):
        if token not in markdown:
            errors.append(f"rearmed operation grid markdown omits required rule: {token}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("revenue_unreacted_range rearmed operation grid validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
