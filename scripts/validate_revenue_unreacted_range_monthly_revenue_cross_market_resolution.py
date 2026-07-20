from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_HISTORY_CSV = ROOT / "data/monthly_revenue_history/monthly_revenue_history.csv"
LATEST_MIRROR_CSV = (
    ROOT / "output/latest/research_backtest/monthly_revenue_history_latest.csv"
)
RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
)
MODEL_ID = "revenue_unreacted_range"
MONTHLY_REVENUE_LINEAGE_CANONICAL_JSON_VERSION = "canonical_json_v1"
VALIDATION_CLASSIFICATION = (
    "implementation_consistency_and_source_lineage_only_not_promotion_evidence"
)
EXPECTED_EVIDENCE_URL = (
    "https://investoredu.twse.com.tw/Mobile_Pages/..%2FFileSystem%2FFileUpload%2F"
    "0f3fc19b-38f3-4eb6-9613-702469baf46b.pdf"
)

KEY_COLUMNS = ("stock_id", "revenue_period")
SOURCE_IDENTITY_COLUMNS = (
    "market",
    "source_market_name",
    "source_table_date",
    "source_kind",
    "source_url",
    "source_file",
)
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
BUSINESS_PAYLOAD_COLUMNS = (
    "stock_id",
    "stock_name",
    "industry",
    "revenue_period",
    "revenue_period_roc",
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
    "note",
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_numerical_anomaly_flag",
    "revenue_numerical_anomaly_reason",
    "point_in_time_status",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
    "formal_use_blocker",
    "coverage_note",
)
RAW_ROW_CANONICAL_COLUMNS = SOURCE_IDENTITY_COLUMNS + BUSINESS_PAYLOAD_COLUMNS
RAW_ROW_NUMERIC_COLUMNS = (
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
)
RAW_ROW_BOOLEAN_COLUMNS = (
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_numerical_anomaly_flag",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
)
RESOLUTION_COLUMNS = (
    "resolution_id",
    "model_id",
    "stock_id",
    "revenue_period",
    "earlier_market",
    "earlier_source_market_name",
    "earlier_source_table_date",
    "earlier_source_kind",
    "earlier_source_url",
    "earlier_source_file",
    "earlier_raw_row_canonical_sha256",
    "later_market",
    "later_source_market_name",
    "later_source_table_date",
    "later_source_kind",
    "later_source_url",
    "later_source_file",
    "later_raw_row_canonical_sha256",
    "official_market_transition_date",
    "canonical_source_table_date",
    "canonical_row_canonical_sha256",
    "resolution_status",
    "canonicalization_policy",
    "evidence_url",
    "formal_model_use_allowed",
    "notes",
)
CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS = (
    "resolution_id",
    "model_id",
    "stock_id",
    "revenue_period",
    "earlier_market",
    "earlier_source_market_name",
    "earlier_source_table_date",
    "earlier_source_kind",
    "earlier_source_url",
    "earlier_source_file",
    "earlier_raw_row_canonical_sha256",
    "later_market",
    "later_source_market_name",
    "later_source_table_date",
    "later_source_kind",
    "later_source_url",
    "later_source_file",
    "later_raw_row_canonical_sha256",
    "official_market_transition_date",
    "canonical_source_table_date",
    "canonical_row_canonical_sha256",
    "resolution_status",
    "canonicalization_policy",
    "evidence_url",
    "formal_model_use_allowed",
)
CROSS_MARKET_RESOLUTION_REGISTRY_SORT_KEYS = (
    "model_id",
    "stock_id",
    "revenue_period",
    "resolution_id",
)
EXPECTED_5236 = {
    "resolution_id": "revenue_unreacted_range_5236_202606_cross_market_mirror",
    "model_id": MODEL_ID,
    "stock_id": "5236",
    "revenue_period": "202606",
    "earlier_market": "otc",
    "earlier_source_market_name": "TPEX",
    "earlier_source_table_date": "20260715",
    "earlier_source_kind": "official_mops_current_monthly_revenue_openapi",
    "earlier_source_url": "https://mopsfin.twse.com.tw/opendata/t187ap05_O.csv",
    "earlier_source_file": (
        "data/monthly_revenue_history/raw/"
        "monthly_revenue_raw_otc_20260715_202606.csv"
    ),
    "earlier_raw_row_canonical_sha256": (
        "49d69d892010c55067260fc105a0ef4ac3cb522135c46ca63d5267cf31f2973d"
    ),
    "later_market": "listed",
    "later_source_market_name": "TWSE",
    "later_source_table_date": "20260717",
    "later_source_kind": "official_mops_current_monthly_revenue_openapi",
    "later_source_url": "https://mopsfin.twse.com.tw/opendata/t187ap05_L.csv",
    "later_source_file": (
        "data/monthly_revenue_history/raw/"
        "monthly_revenue_raw_listed_20260717_202606.csv"
    ),
    "later_raw_row_canonical_sha256": (
        "b0c7b4b980c1e1fb8bc8e6c40a0aac09975fa657e3e4854a91c0b6504894d7bc"
    ),
    "official_market_transition_date": "20260716",
    "canonical_source_table_date": "20260715",
    "canonical_row_canonical_sha256": (
        "49d69d892010c55067260fc105a0ef4ac3cb522135c46ca63d5267cf31f2973d"
    ),
    "resolution_status": "registered_equal_payload_cross_market_mirror",
    "canonicalization_policy": "earliest_official_source_table_date",
    "evidence_url": EXPECTED_EVIDENCE_URL,
    "formal_model_use_allowed": "False",
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)


def _payload_value(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    return text


def _fixed_digits(value: object, length: int) -> str:
    text = _payload_value(value)
    exact = re.fullmatch(rf"\d{{{length}}}", text)
    if exact:
        return text
    numeric_export = re.fullmatch(rf"(\d{{{length}}})\.0+", text)
    if numeric_export:
        return numeric_export.group(1)
    raise RuntimeError(
        "independent monthly revenue date/period identity must be exact digits or an "
        f"equivalent numeric export: value={text!r}; digits={length}"
    )


def _canonical_json_sha256(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _canonical_numeric_value(value: object) -> str:
    text = _payload_value(value)
    if not text:
        return ""
    try:
        number = Decimal(text)
    except InvalidOperation as exc:
        raise RuntimeError(
            f"independent canonical numeric value is invalid: {text}"
        ) from exc
    if not number.is_finite():
        raise RuntimeError(f"independent canonical numeric value is non-finite: {text}")
    if number == 0:
        return "0"
    rendered = format(number.normalize(), "f")
    if "." in rendered:
        rendered = rendered.rstrip("0").rstrip(".")
    return rendered


def _canonical_raw_row_value(column: str, value: object) -> str:
    if column == "stock_id":
        text = _payload_value(value).replace(".0", "")
        return text.zfill(4) if text else ""
    if column == "revenue_period":
        return _fixed_digits(value, 6)
    if column == "source_table_date":
        return _fixed_digits(value, 8)
    if column == "market":
        return _payload_value(value).lower()
    if column == "source_market_name":
        return _payload_value(value).upper()
    if column in RAW_ROW_NUMERIC_COLUMNS:
        return _canonical_numeric_value(value)
    if column in RAW_ROW_BOOLEAN_COLUMNS:
        text = _payload_value(value).lower()
        if text not in {"true", "false"}:
            raise RuntimeError(
                f"independent canonical boolean value is invalid: {column}={text}"
            )
        return text
    return _payload_value(value)


def independent_monthly_revenue_raw_row_sha256(row: pd.Series) -> str:
    missing = sorted(set(RAW_ROW_CANONICAL_COLUMNS) - set(row.index))
    if missing:
        raise RuntimeError(
            f"independent raw-row canonical hash is missing columns: {missing}"
        )
    values = [
        _canonical_raw_row_value(column, row[column])
        for column in RAW_ROW_CANONICAL_COLUMNS
    ]
    return _canonical_json_sha256(
        [
            MONTHLY_REVENUE_LINEAGE_CANONICAL_JSON_VERSION,
            list(RAW_ROW_CANONICAL_COLUMNS),
            values,
        ]
    )


def _normalize_registry_semantics(registry: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(
        set(CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS)
        - set(registry.columns)
    )
    if missing:
        raise RuntimeError(
            f"independent registry canonical hash is missing columns: {missing}"
        )
    normalized = registry.loc[
        :, list(CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS)
    ].copy()
    for column in normalized.columns:
        normalized[column] = normalized[column].map(_payload_value)
    normalized["stock_id"] = normalized["stock_id"].str.replace(
        ".0", "", regex=False
    ).str.zfill(4)
    normalized["revenue_period"] = normalized["revenue_period"].map(
        lambda value: _fixed_digits(value, 6)
    )
    for column in (
        "earlier_source_table_date",
        "later_source_table_date",
        "official_market_transition_date",
        "canonical_source_table_date",
    ):
        normalized[column] = normalized[column].map(
            lambda value: _fixed_digits(value, 8)
        )
    for column in ("earlier_market", "later_market"):
        normalized[column] = normalized[column].str.lower()
    for column in ("earlier_source_market_name", "later_source_market_name"):
        normalized[column] = normalized[column].str.upper()
    normalized["formal_model_use_allowed"] = normalized[
        "formal_model_use_allowed"
    ].str.lower()
    return normalized.sort_values(
        list(CROSS_MARKET_RESOLUTION_REGISTRY_SORT_KEYS), kind="mergesort"
    ).reset_index(drop=True)


def independent_cross_market_resolution_registry_canonical_sha256(
    registry: pd.DataFrame,
) -> str:
    normalized = _normalize_registry_semantics(registry)
    rows = normalized.values.tolist()
    return _canonical_json_sha256(
        [
            MONTHLY_REVENUE_LINEAGE_CANONICAL_JSON_VERSION,
            list(CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS),
            rows,
        ]
    )


def _normalize_data(frame: pd.DataFrame) -> pd.DataFrame:
    output = frame.copy()
    output["stock_id"] = output["stock_id"].astype(str).str.replace(".0", "", regex=False).str.zfill(4)
    output["revenue_period"] = output["revenue_period"].map(
        lambda value: _fixed_digits(value, 6)
    )
    output["source_table_date"] = output["source_table_date"].map(
        lambda value: _fixed_digits(value, 8)
    )
    output["market"] = output["market"].astype(str).str.strip().str.lower()
    output["source_market_name"] = output["source_market_name"].astype(str).str.strip().str.upper()
    for column in ("source_kind", "source_url", "source_file"):
        output[column] = output[column].astype(str).str.strip()
    return output


def validate(
    data_path: Path = DATA_HISTORY_CSV,
    mirror_path: Path = LATEST_MIRROR_CSV,
    resolution_path: Path = RESOLUTION_CSV,
) -> list[str]:
    errors: list[str] = []
    for label, path in (
        ("data monthly revenue history", data_path),
        ("latest monthly revenue mirror", mirror_path),
        ("cross-market resolution registry", resolution_path),
    ):
        if not path.is_file():
            errors.append(f"missing {label}: {path}")
    if errors:
        return errors

    if _sha256(data_path) != _sha256(mirror_path):
        errors.append("monthly revenue data/latest mirror blob SHA-256 mismatch")
    data = _read(data_path)
    mirror = _read(mirror_path)
    if list(data.columns) != list(mirror.columns):
        errors.append("monthly revenue data/latest mirror column order mismatch")
    elif not data.equals(mirror):
        errors.append("monthly revenue data/latest mirror row or order mismatch")

    registry = _read(resolution_path)
    if tuple(registry.columns) != RESOLUTION_COLUMNS:
        errors.append(
            "cross-market resolution schema mismatch: "
            f"expected={list(RESOLUTION_COLUMNS)}; actual={list(registry.columns)}"
        )
        return errors
    if registry.duplicated(list(KEY_COLUMNS)).any():
        errors.append("cross-market resolution registry repeats a stock-period key")
    if registry["resolution_id"].duplicated().any():
        errors.append("cross-market resolution registry repeats a resolution ID")
    for column in (
        "earlier_raw_row_canonical_sha256",
        "later_raw_row_canonical_sha256",
        "canonical_row_canonical_sha256",
    ):
        if not registry[column].astype(str).str.lower().map(
            lambda value: bool(SHA256_PATTERN.fullmatch(value))
        ).all():
            errors.append(f"cross-market resolution registry has invalid {column}")
    try:
        registry_canonical_sha256 = (
            independent_cross_market_resolution_registry_canonical_sha256(registry)
        )
    except RuntimeError as exc:
        errors.append(str(exc))
        return errors
    if not SHA256_PATTERN.fullmatch(registry_canonical_sha256):
        errors.append("cross-market resolution registry canonical SHA-256 is invalid")

    target_registry = registry.loc[
        registry["stock_id"].astype(str).eq("5236")
        & registry["revenue_period"].astype(str).eq("202606")
    ]
    if len(target_registry) != 1:
        errors.append("cross-market resolution registry must contain exactly one 5236/202606 row")
        return errors
    target = target_registry.iloc[0]
    for column, expected in EXPECTED_5236.items():
        if str(target[column]) != expected:
            errors.append(
                f"5236/202606 resolution identity mismatch: {column}="
                f"{target[column]!r}; expected={expected!r}"
            )

    required_data = set(
        KEY_COLUMNS
        + SOURCE_IDENTITY_COLUMNS
        + BUSINESS_PAYLOAD_COLUMNS
    )
    missing = sorted(required_data - set(data.columns))
    if missing:
        errors.append(f"monthly revenue history missing lineage/payload columns: {missing}")
        return errors
    try:
        normalized = _normalize_data(data)
    except RuntimeError as exc:
        errors.append(str(exc))
        return errors
    duplicate_rows = normalized.loc[
        normalized.duplicated(list(KEY_COLUMNS), keep=False)
    ].copy()
    normalized_registry = _normalize_registry_semantics(registry)
    registered_keys = {
        (str(row.stock_id), str(row.revenue_period))
        for row in normalized_registry.itertuples(index=False)
    }
    duplicate_keys = {
        (str(row.stock_id), str(row.revenue_period))
        for row in duplicate_rows[list(KEY_COLUMNS)].drop_duplicates().itertuples(index=False)
    }
    unregistered = sorted(duplicate_keys - registered_keys)
    if unregistered:
        errors.append(f"monthly revenue history has unregistered duplicate keys: {unregistered}")
    missing_registered = sorted(registered_keys - duplicate_keys)
    if missing_registered:
        errors.append(f"registered cross-market mirrors are absent from monthly history: {missing_registered}")

    for registration in normalized_registry.itertuples(index=False):
        key_text = f"{registration.stock_id}/{registration.revenue_period}"
        rows = normalized.loc[
            normalized["stock_id"].eq(registration.stock_id)
            & normalized["revenue_period"].eq(registration.revenue_period)
        ].copy()
        if len(rows) != 2:
            errors.append(
                f"monthly revenue history must contain exactly two registered mirror rows: "
                f"{key_text}; actual_rows={len(rows)}"
            )
            continue
        if rows["market"].nunique(dropna=False) != 2:
            errors.append(f"{key_text} contains a forbidden same-market duplicate")
        if rows["source_market_name"].nunique(dropna=False) != 2:
            errors.append(f"{key_text} contains a forbidden same source-market duplicate")

        earlier_identity = (
            registration.earlier_market,
            registration.earlier_source_market_name,
            registration.earlier_source_table_date,
            registration.earlier_source_kind,
            registration.earlier_source_url,
            registration.earlier_source_file,
        )
        later_identity = (
            registration.later_market,
            registration.later_source_market_name,
            registration.later_source_table_date,
            registration.later_source_kind,
            registration.later_source_url,
            registration.later_source_file,
        )
        expected_identities = {earlier_identity, later_identity}
        actual_identities = {
            tuple(str(getattr(row, column)) for column in SOURCE_IDENTITY_COLUMNS)
            for row in rows.itertuples(index=False)
        }
        if actual_identities != expected_identities:
            errors.append(
                f"{key_text} source row identities mismatch: "
                f"actual={sorted(actual_identities)}; expected={sorted(expected_identities)}"
            )

        conflicts = [
            column
            for column in BUSINESS_PAYLOAD_COLUMNS
            if rows[column].map(_payload_value).nunique(dropna=False) != 1
        ]
        if conflicts:
            errors.append(f"{key_text} cross-market business payload conflict: {conflicts}")

        row_hashes: dict[tuple[str, ...], str] = {}
        for _, raw_row in rows.iterrows():
            identity = tuple(
                _payload_value(raw_row[column]) for column in SOURCE_IDENTITY_COLUMNS
            )
            row_hashes[identity] = independent_monthly_revenue_raw_row_sha256(raw_row)
        for side, identity, expected_hash in (
            (
                "earlier",
                earlier_identity,
                registration.earlier_raw_row_canonical_sha256,
            ),
            (
                "later",
                later_identity,
                registration.later_raw_row_canonical_sha256,
            ),
        ):
            actual_hash = row_hashes.get(identity, "")
            if actual_hash != expected_hash:
                errors.append(
                    f"{key_text} {side} raw-row canonical SHA-256 mismatch: "
                    f"actual={actual_hash}; expected={expected_hash}"
                )

        earliest = str(rows["source_table_date"].min())
        if registration.canonical_source_table_date != earliest:
            errors.append(
                f"{key_text} canonical date is not the earliest official source table date: "
                f"data_earliest={earliest}; registry={registration.canonical_source_table_date}"
            )
        transition = str(registration.official_market_transition_date)
        if not (
            registration.earlier_source_table_date
            < transition
            <= registration.later_source_table_date
        ):
            errors.append(f"{key_text} official market transition chronology is invalid")
        canonical_identity = (
            earlier_identity
            if registration.canonical_source_table_date
            == registration.earlier_source_table_date
            else later_identity
        )
        canonical_hash = row_hashes.get(canonical_identity, "")
        if canonical_hash != registration.canonical_row_canonical_sha256:
            errors.append(
                f"{key_text} canonical raw-row SHA-256 mismatch: "
                f"actual={canonical_hash}; expected={registration.canonical_row_canonical_sha256}"
            )
        if registration.canonical_row_canonical_sha256 not in {
            registration.earlier_raw_row_canonical_sha256,
            registration.later_raw_row_canonical_sha256,
        }:
            errors.append(f"{key_text} canonical raw-row hash is not bound to either raw side")
        if registration.model_id != MODEL_ID:
            errors.append(f"{key_text} has a foreign model owner")
        if registration.resolution_status != "registered_equal_payload_cross_market_mirror":
            errors.append(f"{key_text} has an invalid resolution status")
        if registration.canonicalization_policy != "earliest_official_source_table_date":
            errors.append(f"{key_text} has an invalid canonicalization policy")
        if not str(registration.evidence_url).startswith("https://"):
            errors.append(f"{key_text} evidence URL must use HTTPS")
        if str(registration.formal_model_use_allowed).lower() != "false":
            errors.append(
                f"{key_text} cross-market resolution must remain non-promotion research evidence"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate revenue_unreacted_range monthly revenue cross-market lineage."
    )
    parser.add_argument("--data", type=Path, default=DATA_HISTORY_CSV)
    parser.add_argument("--mirror", type=Path, default=LATEST_MIRROR_CSV)
    parser.add_argument("--resolution", type=Path, default=RESOLUTION_CSV)
    args = parser.parse_args()
    errors = validate(args.data, args.mirror, args.resolution)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    registry_sha256 = independent_cross_market_resolution_registry_canonical_sha256(
        _read(args.resolution)
    )
    print(
        "PASS: revenue_unreacted_range monthly revenue cross-market lineage; "
        f"classification={VALIDATION_CLASSIFICATION}; "
        f"registry_canonical_sha256={registry_sha256}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
