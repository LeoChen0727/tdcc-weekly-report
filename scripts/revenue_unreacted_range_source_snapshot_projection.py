from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo

import pandas as pd

from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (
    BUSINESS_PAYLOAD_COLUMNS,
    RESOLUTION_COLUMNS as MONTHLY_RESOLUTION_COLUMNS,
    SOURCE_IDENTITY_COLUMNS,
    canonical_monthly_revenue_history_table_sha256,
    cross_market_resolution_registry_canonical_sha256,
    load_canonical_monthly_revenue_history,
    load_cross_market_resolutions,
    monthly_revenue_history_blob_sha256,
    resolve_monthly_revenue_cross_market_mirrors,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
ARTIFACT_VERSION = "source_snapshot_projection_v1_20260731"
PROJECTION_ID = "revenue_unreacted_range_source_snapshot_asof_20260713"
PROJECTION_VERSION = ARTIFACT_VERSION
PROJECTION_POLICY_ID = (
    "raw_source_and_price_truncated_before_source_first_episode_assembly_v1"
)
CUTOFF_DATE = "20260713"
SOURCE_FIRST_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"

REVENUE_HISTORY_CSV = ROOT / "data/monthly_revenue_history/monthly_revenue_history.csv"
PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
MONTHLY_RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
)
PRICE_RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_price_comparability_resolution.csv"
)
FULL_SOURCE_DETAIL_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_first_condition_audit_detail_latest.csv"
)
LATEST_MANIFEST_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
LATEST_DETAIL_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
)
HISTORY_MANIFEST_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest.csv"
)
DOCS_MANIFEST_CSV = (
    ROOT
    / "docs/latest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)

CANONICAL_JSON_VERSION = "revenue_source_snapshot_projection_canonical_json_v1"
PRICE_INPUT_COLUMNS = (
    "date",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "volume_ratio",
)
MONTHLY_CANONICAL_BINDING_COLUMNS = (
    "stock_id",
    "revenue_period",
    "source_row_canonical_sha256",
    "cross_market_resolution_id",
    "canonical_source_table_date",
)
MONTHLY_RAW_REQUIRED_COLUMNS = SOURCE_IDENTITY_COLUMNS + BUSINESS_PAYLOAD_COLUMNS
PRICE_RESOLUTION_REQUIRED_COLUMNS = (
    "resolution_id",
    "model_id",
    "stock_id",
    "resume_date",
    "exchange_ratio",
    "root_cause_status",
)
MANIFEST_COLUMNS = (
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
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
NO_RESOLUTION_ID = "none"
PROJECTED_CAPTURE_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def _payload_value(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    return text


def _canonical_json_sha256(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _normalize_stock_id(value: object) -> str:
    text = _payload_value(value).replace(".0", "")
    return text.zfill(4) if text else ""


def _digits(value: object, length: int, *, label: str) -> str:
    text = _payload_value(value)
    exact = re.fullmatch(rf"\d{{{length}}}", text)
    if exact:
        return text
    numeric_export = re.fullmatch(rf"(\d{{{length}}})\.0+", text)
    if numeric_export:
        return numeric_export.group(1)
    raise RuntimeError(f"{label} must contain exactly {length} digits: {text!r}")


def _canonical_frame_sha256(
    frame: pd.DataFrame,
    *,
    columns: tuple[str, ...] | list[str] | None = None,
    excluded_columns: tuple[str, ...] = (),
) -> str:
    selected = (
        list(columns)
        if columns is not None
        else [column for column in frame.columns if column not in excluded_columns]
    )
    missing = sorted(set(selected) - set(frame.columns))
    if missing:
        raise RuntimeError(f"canonical frame is missing columns: {missing}")
    rows = [
        [_payload_value(value) for value in row]
        for row in frame.loc[:, selected].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _canonical_json_sha256([CANONICAL_JSON_VERSION, selected, rows])


def canonical_source_detail_semantic_sha256(frame: pd.DataFrame) -> str:
    return _canonical_frame_sha256(frame, excluded_columns=("generated_at",))


def canonical_projected_source_detail_semantic_sha256(frame: pd.DataFrame) -> str:
    return _canonical_frame_sha256(
        frame,
        excluded_columns=("generated_at", *PROJECTED_CAPTURE_LINEAGE_COLUMNS),
    )


def _constant(frame: pd.DataFrame, column: str, *, label: str) -> str:
    if column not in frame.columns:
        raise RuntimeError(f"{label} is missing column: {column}")
    values = sorted({_payload_value(value) for value in frame[column]})
    if len(values) != 1 or not values[0]:
        raise RuntimeError(f"{label} must have one non-empty {column}: {values}")
    return values[0]


def _read_raw_monthly_revenue(path: Path, cutoff_date: str | None) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing monthly revenue history: {path}")
    frame = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    missing = sorted(set(MONTHLY_RAW_REQUIRED_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(f"monthly revenue history is missing columns: {missing}")
    dates = frame["source_table_date"].map(
        lambda value: _digits(value, 8, label="monthly source_table_date")
    )
    frame = frame.copy()
    frame["source_table_date"] = dates
    if cutoff_date is not None:
        frame = frame.loc[frame["source_table_date"].le(cutoff_date)].copy()
    return frame.reset_index(drop=True)


def load_cutoff_monthly_revenue_subset(
    revenue_path: Path = REVENUE_HISTORY_CSV,
    monthly_resolution_path: Path = MONTHLY_RESOLUTION_CSV,
    *,
    cutoff_date: str = CUTOFF_DATE,
) -> pd.DataFrame:
    cutoff = _digits(cutoff_date, 8, label="projection cutoff_date")
    raw = _read_raw_monthly_revenue(Path(revenue_path), cutoff)
    return resolve_monthly_revenue_cross_market_mirrors(
        raw,
        Path(monthly_resolution_path),
        observation_cutoff_date=cutoff,
    )


def _price_file_projection(path: Path, stock_id: str, cutoff_date: str) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing projected stock price history: {path}")
    frame = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    missing = sorted(set(PRICE_INPUT_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(f"price history {stock_id} is missing columns: {missing}")
    frame = frame.loc[:, list(PRICE_INPUT_COLUMNS)].copy()
    frame["date"] = frame["date"].map(
        lambda value: _digits(value, 8, label=f"price date for {stock_id}")
    )
    frame = (
        frame.loc[frame["date"].le(cutoff_date)]
        .sort_values("date", kind="mergesort")
        .drop_duplicates("date", keep="last")
        .reset_index(drop=True)
    )
    return frame


def _price_paths_by_stock(price_dir: Path) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for path in sorted(Path(price_dir).glob("*.csv")):
        stock_id = _normalize_stock_id(path.stem)
        if not stock_id:
            continue
        if stock_id in paths:
            raise RuntimeError(
                "price history directory repeats a normalized stock id: "
                f"{stock_id}/{paths[stock_id].name}/{path.name}"
            )
        paths[stock_id] = path
    return paths


def cutoff_price_input_stock_ids(
    cutoff_revenue: pd.DataFrame,
    price_dir: Path = PRICE_HISTORY_DIR,
) -> list[str]:
    if "stock_id" not in cutoff_revenue.columns:
        raise RuntimeError("cutoff canonical monthly revenue is missing stock_id")
    revenue_stock_ids = {
        _normalize_stock_id(value)
        for value in cutoff_revenue["stock_id"]
        if _normalize_stock_id(value)
    }
    return sorted(revenue_stock_ids & set(_price_paths_by_stock(Path(price_dir))))


def cutoff_price_input_lineage(
    cutoff_revenue: pd.DataFrame,
    price_dir: Path = PRICE_HISTORY_DIR,
    *,
    cutoff_date: str = CUTOFF_DATE,
) -> dict[str, object]:
    cutoff = _digits(cutoff_date, 8, label="projection cutoff_date")
    price_paths = _price_paths_by_stock(Path(price_dir))
    descriptors: list[list[object]] = []
    total_rows = 0
    for stock_id in cutoff_price_input_stock_ids(cutoff_revenue, Path(price_dir)):
        frame = _price_file_projection(price_paths[stock_id], stock_id, cutoff)
        semantic_sha = _canonical_frame_sha256(
            frame,
            columns=list(PRICE_INPUT_COLUMNS),
        )
        total_rows += len(frame)
        descriptors.append([stock_id, len(frame), semantic_sha])
    descriptor_text = "|".join(
        f"{stock_id}:{row_count}:{semantic_sha}"
        for stock_id, row_count, semantic_sha in descriptors
    )
    return {
        "stock_count": len(descriptors),
        "row_count": total_rows,
        "file_semantic_sha256s": descriptor_text,
        "semantic_sha256": _canonical_json_sha256(
            [CANONICAL_JSON_VERSION, "cutoff_price_input_set", descriptors]
        ),
    }


def _read_registry(path: Path, *, label: str) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing {label}: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def _resolution_subset_sha256(frame: pd.DataFrame) -> str:
    columns = tuple(column for column in frame.columns if column != "notes")
    return _canonical_frame_sha256(frame, columns=columns)


def _applied_monthly_resolutions(
    cutoff_revenue: pd.DataFrame,
    monthly_registry: pd.DataFrame,
    cutoff_date: str,
) -> tuple[list[str], str]:
    required = {"cross_market_resolution_id"}
    missing = sorted(required - set(cutoff_revenue.columns))
    if missing:
        raise RuntimeError(f"cutoff monthly revenue is missing columns: {missing}")
    ids = sorted(
        {
            _payload_value(value)
            for value in cutoff_revenue["cross_market_resolution_id"]
            if _payload_value(value) not in {"", NO_RESOLUTION_ID}
        }
    )
    if tuple(monthly_registry.columns) != tuple(MONTHLY_RESOLUTION_COLUMNS):
        raise RuntimeError("monthly resolution registry schema mismatch")
    eligible = monthly_registry.copy()
    for column in ("earlier_source_table_date", "later_source_table_date"):
        eligible[column] = eligible[column].map(
            lambda value: _digits(value, 8, label=f"monthly resolution {column}")
        )
    eligible = eligible.loc[
        eligible["resolution_id"].isin(ids)
        & eligible["earlier_source_table_date"].le(cutoff_date)
        & eligible["later_source_table_date"].le(cutoff_date)
    ].copy()
    if sorted(eligible["resolution_id"].tolist()) != ids:
        raise RuntimeError("cutoff monthly resolution ids are not fully eligible")
    return ids, _resolution_subset_sha256(eligible)


def _applied_price_resolutions(
    price_input_stock_ids: list[str],
    price_registry: pd.DataFrame,
    cutoff_date: str,
) -> tuple[list[str], str]:
    missing = sorted(set(PRICE_RESOLUTION_REQUIRED_COLUMNS) - set(price_registry.columns))
    if missing:
        raise RuntimeError(f"price resolution registry is missing columns: {missing}")
    stock_ids = set(price_input_stock_ids)
    normalized = price_registry.copy()
    normalized["stock_id"] = normalized["stock_id"].map(_normalize_stock_id)
    normalized["resume_date"] = normalized["resume_date"].map(
        lambda value: _digits(value, 8, label="price resolution resume_date")
    )
    eligible = normalized.loc[
        normalized["stock_id"].isin(stock_ids)
        & normalized["resume_date"].le(cutoff_date)
        & normalized["root_cause_status"].eq(
            "verified_non_comparable_raw_price_scale"
        )
    ].copy()
    foreign_models = sorted(
        set(eligible.loc[~eligible["model_id"].eq(MODEL_ID), "model_id"])
    )
    if foreign_models:
        raise RuntimeError(
            "cutoff source-first price inputs contain foreign-model resolutions: "
            f"{foreign_models}"
        )
    applied = eligible.loc[eligible["model_id"].eq(MODEL_ID)].copy()
    ids = sorted(applied["resolution_id"].astype(str).tolist())
    return ids, _resolution_subset_sha256(applied)


def _date_tokens(frame: pd.DataFrame, columns: tuple[str, ...]) -> list[str]:
    tokens: list[str] = []
    for column in columns:
        if column not in frame.columns:
            raise RuntimeError(f"projected source detail is missing date column: {column}")
        for value in frame[column]:
            for token in _payload_value(value).split("|"):
                token = token.strip()
                if token:
                    tokens.append(_digits(token, 8, label=column))
    return tokens


def _max_projected_dates(projected_detail: pd.DataFrame) -> tuple[str, str, str]:
    source_dates = _date_tokens(
        projected_detail,
        (
            "episode_start_source_date",
            "latest_qualifying_source_date",
            "qualifying_source_dates",
        ),
    )
    trade_dates = _date_tokens(
        projected_detail,
        (
            "episode_start_trade_date",
            "latest_qualifying_trade_date",
            "qualifying_trade_dates",
        ),
    )
    end_dates = _date_tokens(projected_detail, ("episode_end_date",))
    return (
        max(source_dates, default=""),
        max(trade_dates, default=""),
        max(end_dates, default=""),
    )


def _require_source_identity(
    full_source_detail: pd.DataFrame,
    projected_detail: pd.DataFrame,
) -> tuple[str, str]:
    source_artifact_id = _constant(
        full_source_detail,
        "artifact_id",
        label="full source detail",
    )
    source_artifact_version = _constant(
        full_source_detail,
        "artifact_version",
        label="full source detail",
    )
    if source_artifact_id != SOURCE_FIRST_ARTIFACT_ID:
        raise RuntimeError(f"unexpected full source artifact_id: {source_artifact_id}")
    if _constant(projected_detail, "artifact_id", label="projected source detail") != source_artifact_id:
        raise RuntimeError("projected detail artifact_id differs from full source")
    if (
        _constant(projected_detail, "artifact_version", label="projected source detail")
        != source_artifact_version
    ):
        raise RuntimeError("projected detail artifact_version differs from full source")
    if list(projected_detail.columns) != list(full_source_detail.columns):
        raise RuntimeError("projected detail must preserve the full source detail schema")
    return source_artifact_id, source_artifact_version


def build_source_snapshot_projection_manifest(
    full_source_detail: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    revenue_path: Path = REVENUE_HISTORY_CSV,
    price_dir: Path = PRICE_HISTORY_DIR,
    monthly_resolution_path: Path = MONTHLY_RESOLUTION_CSV,
    price_resolution_path: Path = PRICE_RESOLUTION_CSV,
    cutoff_date: str = CUTOFF_DATE,
    generated_at: str | None = None,
) -> pd.DataFrame:
    cutoff = _digits(cutoff_date, 8, label="projection cutoff_date")
    if cutoff != CUTOFF_DATE:
        raise RuntimeError(f"projection cutoff drift: {cutoff}/{CUTOFF_DATE}")
    source_artifact_id, source_artifact_version = _require_source_identity(
        full_source_detail,
        projected_detail,
    )
    cutoff_revenue = load_cutoff_monthly_revenue_subset(
        Path(revenue_path),
        Path(monthly_resolution_path),
        cutoff_date=cutoff,
    )
    full_revenue = load_canonical_monthly_revenue_history(
        Path(revenue_path),
        Path(monthly_resolution_path),
    )
    monthly_registry = load_cross_market_resolutions(Path(monthly_resolution_path))
    price_registry = _read_registry(
        Path(price_resolution_path),
        label="price resolution registry",
    )
    monthly_ids, monthly_resolution_sha = _applied_monthly_resolutions(
        cutoff_revenue,
        monthly_registry,
        cutoff,
    )
    price_input_stock_ids = cutoff_price_input_stock_ids(
        cutoff_revenue,
        Path(price_dir),
    )
    price_ids, price_resolution_sha = _applied_price_resolutions(
        price_input_stock_ids,
        price_registry,
        cutoff,
    )
    price_lineage = cutoff_price_input_lineage(
        cutoff_revenue,
        Path(price_dir),
        cutoff_date=cutoff,
    )
    max_source_date, max_trade_date, max_end_date = _max_projected_dates(
        projected_detail
    )
    if any(value and value > cutoff for value in (max_source_date, max_trade_date, max_end_date)):
        raise RuntimeError(
            "projected source detail exceeds cutoff: "
            f"source={max_source_date}; trade={max_trade_date}; end={max_end_date}; cutoff={cutoff}"
        )
    monthly_blob_sha = monthly_revenue_history_blob_sha256(Path(revenue_path))
    monthly_table_sha = canonical_monthly_revenue_history_table_sha256(full_revenue)
    cutoff_monthly_table_sha = canonical_monthly_revenue_history_table_sha256(
        cutoff_revenue
    )
    monthly_registry_sha = cross_market_resolution_registry_canonical_sha256(
        monthly_registry
    )
    for frame, label in (
        (full_source_detail, "full source detail"),
        (projected_detail, "projected source detail"),
    ):
        for column, expected in (
            ("monthly_revenue_history_blob_sha256", monthly_blob_sha),
            ("cross_market_resolution_registry_canonical_sha256", monthly_registry_sha),
        ):
            if _constant(frame, column, label=label) != expected:
                raise RuntimeError(f"{label} {column} does not match current raw lineage")
    if (
        _constant(
            full_source_detail,
            "monthly_revenue_canonical_table_sha256",
            label="full source detail",
        )
        != monthly_table_sha
    ):
        raise RuntimeError("full source detail canonical monthly lineage mismatch")
    if (
        _constant(
            projected_detail,
            "monthly_revenue_canonical_table_sha256",
            label="projected source detail",
        )
        != cutoff_monthly_table_sha
    ):
        raise RuntimeError("projected source detail cutoff monthly lineage mismatch")
    row = {
        "generated_at": generated_at or _now_text(),
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "projection_id": PROJECTION_ID,
        "projection_version": PROJECTION_VERSION,
        "projection_policy_id": PROJECTION_POLICY_ID,
        "cutoff_date": cutoff,
        "full_source_artifact_id": source_artifact_id,
        "full_source_artifact_version": source_artifact_version,
        "full_source_episode_row_count": len(full_source_detail),
        "full_source_episode_semantic_sha256": canonical_source_detail_semantic_sha256(
            full_source_detail
        ),
        "monthly_revenue_history_blob_sha256": monthly_blob_sha,
        "monthly_revenue_canonical_table_sha256": monthly_table_sha,
        "cross_market_resolution_registry_canonical_sha256": monthly_registry_sha,
        "cutoff_revenue_subset_row_count": len(cutoff_revenue),
        "cutoff_revenue_subset_semantic_sha256": cutoff_monthly_table_sha,
        "cutoff_price_input_stock_count": price_lineage["stock_count"],
        "cutoff_price_input_row_count": price_lineage["row_count"],
        "cutoff_price_input_file_semantic_sha256s": price_lineage[
            "file_semantic_sha256s"
        ],
        "cutoff_price_input_semantic_sha256": price_lineage["semantic_sha256"],
        "applied_monthly_resolution_count": len(monthly_ids),
        "applied_monthly_resolution_ids": "|".join(monthly_ids) or NO_RESOLUTION_ID,
        "applied_monthly_resolution_semantic_sha256": monthly_resolution_sha,
        "applied_price_resolution_count": len(price_ids),
        "applied_price_resolution_ids": "|".join(price_ids) or NO_RESOLUTION_ID,
        "applied_price_resolution_semantic_sha256": price_resolution_sha,
        "projected_episode_row_count": len(projected_detail),
        "projected_episode_semantic_sha256": (
            canonical_projected_source_detail_semantic_sha256(projected_detail)
        ),
        "projected_max_source_date": max_source_date,
        "projected_max_trade_date": max_trade_date,
        "projected_max_episode_end_date": max_end_date,
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "production_change": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
    }
    manifest = pd.DataFrame([row], columns=list(MANIFEST_COLUMNS))
    validate_projection_binding(manifest, projected_detail)
    return manifest


def projection_binding_errors(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    expected_cutoff_date: str = CUTOFF_DATE,
) -> list[str]:
    errors: list[str] = []
    if list(manifest.columns) != list(MANIFEST_COLUMNS):
        errors.append(
            "projection manifest schema mismatch: "
            f"expected={list(MANIFEST_COLUMNS)}; actual={list(manifest.columns)}"
        )
        return errors
    if len(manifest) != 1:
        errors.append(f"projection manifest must have exactly one row: {len(manifest)}")
        return errors
    row = manifest.iloc[0]
    expected_constants = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "projection_id": PROJECTION_ID,
        "projection_version": PROJECTION_VERSION,
        "projection_policy_id": PROJECTION_POLICY_ID,
        "cutoff_date": expected_cutoff_date,
        "full_source_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
    }
    for column, expected in expected_constants.items():
        if _payload_value(row[column]) != expected:
            errors.append(
                f"projection manifest {column} mismatch: {_payload_value(row[column])}/{expected}"
            )
    try:
        detail_artifact_id = _constant(
            projected_detail,
            "artifact_id",
            label="projected source detail",
        )
        detail_artifact_version = _constant(
            projected_detail,
            "artifact_version",
            label="projected source detail",
        )
        if detail_artifact_id != _payload_value(row["full_source_artifact_id"]):
            errors.append("projected detail artifact_id is not bound to manifest")
        if detail_artifact_version != _payload_value(row["full_source_artifact_version"]):
            errors.append("projected detail artifact_version is not bound to manifest")
        actual_sha = canonical_projected_source_detail_semantic_sha256(projected_detail)
        if actual_sha != _payload_value(row["projected_episode_semantic_sha256"]):
            errors.append("projected detail semantic SHA-256 is not bound to manifest")
        if len(projected_detail) != int(row["projected_episode_row_count"]):
            errors.append("projected detail row count is not bound to manifest")
        for column, manifest_column in (
            ("monthly_revenue_history_blob_sha256", "monthly_revenue_history_blob_sha256"),
            (
                "monthly_revenue_canonical_table_sha256",
                "cutoff_revenue_subset_semantic_sha256",
            ),
            (
                "cross_market_resolution_registry_canonical_sha256",
                "cross_market_resolution_registry_canonical_sha256",
            ),
        ):
            if _constant(
                projected_detail,
                column,
                label="projected source detail",
            ) != _payload_value(row[manifest_column]):
                errors.append(f"projected detail {column} is not bound to manifest")
        max_source, max_trade, max_end = _max_projected_dates(projected_detail)
        for column, actual in (
            ("projected_max_source_date", max_source),
            ("projected_max_trade_date", max_trade),
            ("projected_max_episode_end_date", max_end),
        ):
            if _payload_value(row[column]) != actual:
                errors.append(f"projected detail {column} is not bound to manifest")
            if actual and actual > expected_cutoff_date:
                errors.append(f"projected detail {column} exceeds cutoff: {actual}")
    except (RuntimeError, TypeError, ValueError) as exc:
        errors.append(str(exc))
    if _payload_value(row["research_only"]) != "true":
        errors.append("projection manifest research_only must be true")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if _payload_value(row[column]) != "false":
            errors.append(f"projection manifest {column} must be false")
    for column in (
        "full_source_episode_semantic_sha256",
        "monthly_revenue_history_blob_sha256",
        "monthly_revenue_canonical_table_sha256",
        "cross_market_resolution_registry_canonical_sha256",
        "cutoff_revenue_subset_semantic_sha256",
        "cutoff_price_input_semantic_sha256",
        "applied_monthly_resolution_semantic_sha256",
        "applied_price_resolution_semantic_sha256",
        "projected_episode_semantic_sha256",
    ):
        if not SHA256_PATTERN.fullmatch(_payload_value(row[column])):
            errors.append(f"projection manifest {column} is not a SHA-256")
    return errors


def validate_projection_binding(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    expected_cutoff_date: str = CUTOFF_DATE,
) -> None:
    errors = projection_binding_errors(
        manifest,
        projected_detail,
        expected_cutoff_date=expected_cutoff_date,
    )
    if errors:
        raise RuntimeError("source snapshot projection binding failed: " + "; ".join(errors))


def write_source_snapshot_projection(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    latest_manifest_path: Path = LATEST_MANIFEST_CSV,
    latest_detail_path: Path = LATEST_DETAIL_CSV,
    history_manifest_path: Path = HISTORY_MANIFEST_CSV,
    docs_manifest_path: Path = DOCS_MANIFEST_CSV,
) -> None:
    validate_projection_binding(manifest, projected_detail)
    for path in (
        latest_manifest_path,
        latest_detail_path,
        history_manifest_path,
        docs_manifest_path,
    ):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
    if Path(history_manifest_path).is_file():
        history = pd.read_csv(history_manifest_path, dtype=str, keep_default_na=False)
        if list(history.columns) != list(MANIFEST_COLUMNS):
            raise RuntimeError("source snapshot projection history schema mismatch")
        key_columns = ("projection_id", "projection_version", "cutoff_date")
        key_mask = pd.Series(True, index=history.index)
        for column in key_columns:
            key_mask &= history[column].eq(_payload_value(manifest.iloc[0][column]))
        matching = history.loc[key_mask]
        if not matching.empty:
            capture_columns = {
                "generated_at",
                "full_source_episode_row_count",
                "full_source_episode_semantic_sha256",
                "monthly_revenue_history_blob_sha256",
                "monthly_revenue_canonical_table_sha256",
                "cross_market_resolution_registry_canonical_sha256",
            }
            immutable_columns = [
                column for column in MANIFEST_COLUMNS if column not in capture_columns
            ]
            current_immutable_sha = _canonical_frame_sha256(
                manifest,
                columns=immutable_columns,
            )
            prior_immutable_shas = {
                _canonical_frame_sha256(
                    matching.loc[[index]],
                    columns=immutable_columns,
                )
                for index in matching.index
            }
            if prior_immutable_shas != {current_immutable_sha}:
                raise RuntimeError(
                    "source snapshot projection immutable history key changed semantics"
                )
            capture_identity_columns = [
                column for column in MANIFEST_COLUMNS if column != "generated_at"
            ]
            current_capture_sha = _canonical_frame_sha256(
                manifest,
                columns=capture_identity_columns,
            )
            prior_capture_shas = {
                _canonical_frame_sha256(
                    matching.loc[[index]],
                    columns=capture_identity_columns,
                )
                for index in matching.index
            }
            if current_capture_sha not in prior_capture_shas:
                history = pd.concat([history, manifest], ignore_index=True)
        else:
            history = pd.concat([history, manifest], ignore_index=True)
    else:
        history = manifest.copy()
    manifest.to_csv(latest_manifest_path, index=False)
    projected_detail.to_csv(latest_detail_path, index=False)
    manifest.to_csv(docs_manifest_path, index=False)
    history.to_csv(history_manifest_path, index=False)


def load_source_snapshot_projection_manifest(
    path: Path = LATEST_MANIFEST_CSV,
) -> pd.DataFrame:
    if not Path(path).is_file():
        raise RuntimeError(f"missing source snapshot projection manifest: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def load_projected_source_detail(path: Path = LATEST_DETAIL_CSV) -> pd.DataFrame:
    if not Path(path).is_file():
        raise RuntimeError(f"missing projected source detail: {path}")
    return pd.read_csv(
        path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
