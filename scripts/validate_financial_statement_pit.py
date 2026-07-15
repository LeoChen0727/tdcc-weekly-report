from __future__ import annotations

import csv
import re
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTRY = ROOT / "config" / "daily_model_financial_statement_pit_sources.csv"
METRIC_MAPPING = ROOT / "config" / "daily_model_financial_statement_metric_mapping.csv"
HISTORY_PATH = ROOT / "data" / "financial_statement_history" / "financial_statement_history.csv"
MANIFEST_PATH = ROOT / "data" / "financial_statement_history" / "financial_statement_source_manifest.csv"
COVERAGE_PATH = ROOT / "output" / "latest" / "research_backtest" / "financial_statement_pit_coverage_latest.csv"
COVERAGE_MD_PATH = ROOT / "output" / "latest" / "research_backtest" / "financial_statement_pit_coverage_latest.md"
DOCS_COVERAGE_PATH = ROOT / "docs" / "latest" / "financial_statement_pit_coverage_latest.csv"
DOCS_COVERAGE_MD_PATH = ROOT / "docs" / "latest" / "financial_statement_pit_coverage_latest.md"

EXPECTED_SCHEMAS = {
    "general",
    "banking",
    "securities",
    "financial_holding",
    "insurance",
    "other",
}
EXPECTED_SOURCE_IDS = {
    f"{market}_{schema}"
    for market in ("twse", "tpex")
    for schema in EXPECTED_SCHEMAS
}
CANONICAL_METRICS = (
    "operating_revenue",
    "operating_cost",
    "gross_profit",
    "operating_expenses",
    "operating_income",
    "non_operating_income_expense",
    "pretax_income",
    "income_tax_expense",
    "net_income",
    "parent_net_income",
    "basic_eps",
)
HISTORY_COLUMNS = (
    "generated_at",
    "data_family_id",
    "data_version",
    "source_id",
    "source_kind",
    "market",
    "industry_schema",
    "source_url",
    "raw_archive_ref",
    "raw_payload_sha256",
    "source_row_sha256",
    "source_table_date",
    "source_table_date_raw",
    "observed_at",
    "first_observed_at",
    "source_available_at",
    "availability_precision",
    "pit_status",
    "historical_pit_eligible",
    "research_asof_join_allowed",
    "allowed_for_formal_model_use",
    "fiscal_year",
    "fiscal_year_roc",
    "fiscal_quarter",
    "fiscal_period",
    "statement_scope",
    "period_basis",
    "monetary_unit",
    "per_share_unit",
    "stock_id",
    "stock_name",
    "revision_id",
    "revision_number",
    "revision_count",
    "supersedes_revision_id",
    "is_latest_known_revision",
    *CANONICAL_METRICS,
    "gross_margin_pct",
    "operating_margin_pct",
    "net_margin_pct",
    "margin_derivation_status",
    "metric_completeness_status",
    "source_metric_labels",
    "provenance_status",
    "numerical_anomaly_candidate",
    "numerical_anomaly_triggers",
    "anomaly_disposition",
    "primary_metric_retained",
    "anomaly_evidence_status",
    "coverage_note",
)
MANIFEST_COLUMNS = (
    "generated_at",
    "manifest_version",
    "source_id",
    "source_kind",
    "market",
    "industry_schema",
    "source_url",
    "observed_at",
    "source_available_at",
    "availability_precision",
    "statement_scope",
    "period_basis",
    "monetary_unit",
    "per_share_unit",
    "raw_archive_ref",
    "raw_payload_sha256",
    "raw_byte_count",
    "source_row_count",
    "normalized_row_count",
    "dropped_invalid_identity_row_count",
    "fetch_status",
    "archive_status",
    "historical_pit_eligible",
    "current_snapshot_only",
    "notes",
)
COVERAGE_COLUMNS = (
    "generated_at",
    "audit_id",
    "row_type",
    "market",
    "industry_schema",
    "captured_source_count",
    "captured_raw_row_count",
    "normalized_history_row_count",
    "dropped_invalid_identity_row_count",
    "unique_stock_count",
    "fiscal_period_min",
    "fiscal_period_max",
    "exact_filing_available_rows",
    "current_snapshot_only_rows",
    "research_asof_join_allowed_rows",
    "formal_model_allowed_rows",
    "operating_revenue_coverage_pct",
    "gross_profit_coverage_pct",
    "operating_income_coverage_pct",
    "non_operating_income_expense_coverage_pct",
    "net_income_coverage_pct",
    "basic_eps_coverage_pct",
    "gross_margin_coverage_pct",
    "operating_margin_coverage_pct",
    "numerical_anomaly_candidate_rows",
    "unresolved_anomaly_candidate_rows",
    "primary_metric_retained_rows",
    "pit_coverage_status",
    "formal_model_use_allowed",
    "blocker",
)
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [
            {str(key): str(value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(handle)
        ]


def _read_frame(path: Path, expected_columns: tuple[str, ...], errors: list[str]) -> pd.DataFrame:
    if not path.exists():
        errors.append(f"missing artifact: {path.relative_to(ROOT).as_posix()}")
        return pd.DataFrame(columns=expected_columns)
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    if tuple(frame.columns) != expected_columns:
        errors.append(
            f"{path.relative_to(ROOT).as_posix()}: exact schema mismatch; "
            f"expected={list(expected_columns)}; actual={list(frame.columns)}"
        )
        return pd.DataFrame(columns=expected_columns)
    return frame


def _parse_timestamp(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def _decimal(value: str) -> Decimal | None:
    if str(value).strip() == "":
        return None
    try:
        number = Decimal(str(value))
    except InvalidOperation:
        return None
    return number if number.is_finite() else None


def validate_source_registry(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    source_ids = [row.get("source_id", "") for row in rows]
    if set(source_ids) != EXPECTED_SOURCE_IDS or len(source_ids) != len(EXPECTED_SOURCE_IDS):
        errors.append(
            "financial statement source registry must contain exactly TWSE/TPEX x six industry schemas"
        )
    for row in rows:
        source_id = row.get("source_id", "<missing>")
        host = urlparse(row.get("source_url", "")).hostname or ""
        if host not in {"openapi.twse.com.tw", "www.tpex.org.tw"}:
            errors.append(f"{source_id}: source_url is not an approved official host")
        if row.get("history_mode") != "current_snapshot_only":
            errors.append(f"{source_id}: current OpenAPI must remain current_snapshot_only")
        if row.get("availability_semantics") != "first_observed_at_not_company_filing_time":
            errors.append(f"{source_id}: table date must not be relabeled as company filing time")
        if row.get("raw_archive_policy") != "external_content_addressed_archive_required":
            errors.append(f"{source_id}: raw archive must remain external and content-addressed")
        if row.get("period_basis") != "cumulative_ytd":
            errors.append(f"{source_id}: income statement period basis must remain cumulative_ytd")
    return errors


def validate_metric_mapping(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    seen: set[tuple[str, str]] = set()
    schemas = {row.get("industry_schema", "") for row in rows}
    if schemas != EXPECTED_SCHEMAS:
        errors.append(f"financial statement metric mapping schema set drift: {sorted(schemas)}")
    for row in rows:
        key = (row.get("industry_schema", ""), row.get("canonical_metric", ""))
        if key in seen:
            errors.append(f"duplicate financial statement metric mapping: {key}")
        seen.add(key)
        if key[1] not in CANONICAL_METRICS:
            errors.append(f"unsupported canonical financial metric: {key[1]}")
        if not row.get("source_label_aliases", ""):
            errors.append(f"{key}: source_label_aliases is empty")
        if row.get("derive_ratio_from_revenue") == "True" and key[0] != "general":
            errors.append(f"{key}: non-general schemas must not inherit general margin formulas")
    required_general = {
        ("general", metric)
        for metric in (
            "operating_revenue",
            "gross_profit",
            "operating_income",
            "non_operating_income_expense",
            "net_income",
            "basic_eps",
        )
    }
    if not required_general <= seen:
        errors.append("general schema is missing one or more required canonical metrics")
    return errors


def validate_manifest(
    manifest: pd.DataFrame,
    source_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    if manifest.empty:
        return ["financial statement source manifest is empty"]
    if manifest.duplicated(["source_id", "raw_payload_sha256"], keep=False).any():
        errors.append("source manifest must be unique by source_id + raw_payload_sha256")
    for index, row in manifest.iterrows():
        label = f"manifest row {index + 2}"
        if row["source_id"] not in source_ids:
            errors.append(f"{label}: unknown source_id={row['source_id']}")
        if not SHA_RE.fullmatch(row["raw_payload_sha256"]):
            errors.append(f"{label}: invalid raw_payload_sha256")
        if row["raw_archive_ref"] != f"sha256://{row['raw_payload_sha256']}":
            errors.append(f"{label}: raw_archive_ref must be content-addressed by the exact payload SHA")
        if re.match(r"^[A-Za-z]:[\\/]", row["raw_archive_ref"]):
            errors.append(f"{label}: local raw archive paths must not be committed")
        observed = _parse_timestamp(row["observed_at"])
        available = _parse_timestamp(row["source_available_at"])
        if observed is None or available is None:
            errors.append(f"{label}: observed_at and source_available_at must be ISO timestamps")
        elif available > observed:
            errors.append(f"{label}: source_available_at cannot be after observed_at")
        if row["availability_precision"] == "official_table_date":
            errors.append(f"{label}: global table date cannot be used as company filing availability")
        if row["source_kind"] == "official_openapi_current_snapshot":
            if row["availability_precision"] != "first_observed_at":
                errors.append(f"{label}: current snapshot must use first_observed_at")
            if row["historical_pit_eligible"] != "False":
                errors.append(f"{label}: current snapshot cannot claim historical PIT eligibility")
            if row["current_snapshot_only"] != "True":
                errors.append(f"{label}: current source must be marked current_snapshot_only")
        if row["archive_status"] != "external_content_addressed_archive_verified":
            errors.append(f"{label}: archive_status must prove external content-addressed retention")
        try:
            source_count = int(row["source_row_count"])
            normalized_count = int(row["normalized_row_count"])
            dropped_count = int(row["dropped_invalid_identity_row_count"])
        except ValueError:
            errors.append(f"{label}: source and normalized row counts must be integers")
            continue
        if normalized_count + dropped_count != source_count:
            errors.append(f"{label}: normalized + dropped rows must equal source_row_count")
        if source_count > 1 and normalized_count == 0:
            errors.append(f"{label}: multi-row source was silently dropped by identity mapping")
        if source_count > 1 and dropped_count > 0:
            errors.append(f"{label}: multi-row source contains invalid identity rows")
    return errors


def _validate_margin(
    row: pd.Series,
    numerator_column: str,
    output_column: str,
    errors: list[str],
    label: str,
) -> None:
    revenue = _decimal(row["operating_revenue"])
    numerator = _decimal(row[numerator_column])
    actual = _decimal(row[output_column])
    if revenue is None or revenue == 0 or numerator is None:
        if actual is not None:
            errors.append(f"{label}: {output_column} must be blank without a valid denominator")
        return
    expected = (numerator / revenue * Decimal("100")).quantize(Decimal("0.0001"))
    if actual is None or abs(actual - expected) > Decimal("0.0001"):
        errors.append(f"{label}: {output_column} formula mismatch")


def _expected_anomaly_triggers(row: pd.Series) -> list[str]:
    triggers: list[str] = []
    eps = _decimal(row["basic_eps"])
    if eps is not None and abs(eps) >= Decimal("50"):
        triggers.append("basic_eps_abs_ge_50")
    for trigger, column in (
        ("gross_margin_abs_ge_500pct", "gross_margin_pct"),
        ("operating_margin_abs_ge_500pct", "operating_margin_pct"),
        ("net_margin_abs_ge_500pct", "net_margin_pct"),
    ):
        value = _decimal(row[column])
        if value is not None and abs(value) >= Decimal("500"):
            triggers.append(trigger)
    return triggers


def validate_history(
    history: pd.DataFrame,
    manifest: pd.DataFrame,
    source_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    if history.empty:
        return ["financial statement history is empty"]
    required_nonblank = (
        "source_id",
        "market",
        "industry_schema",
        "raw_payload_sha256",
        "source_row_sha256",
        "observed_at",
        "first_observed_at",
        "source_available_at",
        "fiscal_year",
        "fiscal_quarter",
        "fiscal_period",
        "stock_id",
        "revision_id",
    )
    for column in required_nonblank:
        if history[column].astype(str).str.strip().eq("").any():
            errors.append(f"financial statement history has blank required column: {column}")
    if history.duplicated("revision_id", keep=False).any():
        errors.append("financial statement history revision_id must be unique")
    manifest_shas = set(manifest["raw_payload_sha256"].astype(str))
    for index, row in history.iterrows():
        label = f"history row {index + 2} stock={row['stock_id']} period={row['fiscal_period']}"
        if row["source_id"] not in source_ids:
            errors.append(f"{label}: unknown source_id={row['source_id']}")
        for column in ("raw_payload_sha256", "source_row_sha256", "revision_id"):
            if not SHA_RE.fullmatch(row[column]):
                errors.append(f"{label}: invalid {column}")
        if row["raw_payload_sha256"] not in manifest_shas:
            errors.append(f"{label}: raw payload SHA is absent from source manifest")
        if row["raw_archive_ref"] != f"sha256://{row['raw_payload_sha256']}":
            errors.append(f"{label}: raw archive reference does not match payload SHA")
        observed = _parse_timestamp(row["observed_at"])
        first_observed = _parse_timestamp(row["first_observed_at"])
        available = _parse_timestamp(row["source_available_at"])
        if None in {observed, first_observed, available}:
            errors.append(f"{label}: invalid ISO point-in-time timestamp")
        else:
            assert observed is not None and first_observed is not None and available is not None
            if first_observed > observed:
                errors.append(f"{label}: first_observed_at cannot be after observed_at")
            if available > observed:
                errors.append(f"{label}: source_available_at cannot be after observed_at")
        if row["availability_precision"] == "official_table_date":
            errors.append(f"{label}: global table date cannot become company filing availability")
        if row["pit_status"] == "current_snapshot_first_observed_only":
            if row["availability_precision"] != "first_observed_at":
                errors.append(f"{label}: current snapshot PIT status requires first_observed_at")
            if row["historical_pit_eligible"] != "False":
                errors.append(f"{label}: current snapshot cannot be historical PIT eligible")
        if row["historical_pit_eligible"] == "True":
            if row["availability_precision"] not in {
                "exact_company_filing_timestamp",
                "exact_company_filing_date",
            }:
                errors.append(f"{label}: historical PIT eligibility requires exact filing availability")
            if row["statement_scope"] in {"", "unknown", "official_endpoint_reported_scope"}:
                errors.append(f"{label}: historical PIT eligibility requires explicit statement_scope")
            if row["pit_status"] != "historical_pit_exact_company_filing_available":
                errors.append(f"{label}: historical PIT row has inconsistent pit_status")
        if row["research_asof_join_allowed"] != "True":
            errors.append(f"{label}: row with source_available_at should allow research as-of joins")
        if row["allowed_for_formal_model_use"] != "False":
            errors.append(f"{label}: data-layer PR must not authorize formal model use")
        if row["period_basis"] != "cumulative_ytd":
            errors.append(f"{label}: period_basis must remain cumulative_ytd")
        if row["provenance_status"] != "raw_payload_sha_and_source_row_sha_verified":
            errors.append(f"{label}: provenance_status drift")
        expected_triggers = _expected_anomaly_triggers(row)
        actual_triggers = [
            value for value in row["numerical_anomaly_triggers"].split(";") if value
        ]
        if actual_triggers != expected_triggers:
            errors.append(f"{label}: numerical anomaly trigger drift")
        if expected_triggers:
            if row["numerical_anomaly_candidate"] != "True":
                errors.append(f"{label}: threshold trigger must remain an anomaly candidate")
            if row["anomaly_disposition"] != "unresolved_anomaly_candidate":
                errors.append(f"{label}: threshold trigger cannot receive a final disposition")
            if row["anomaly_evidence_status"] != (
                "source_payload_and_formula_traced_independent_corroboration_pending"
            ):
                errors.append(f"{label}: anomaly evidence status must disclose missing corroboration")
        else:
            if row["numerical_anomaly_candidate"] != "False":
                errors.append(f"{label}: non-triggered row cannot claim a threshold anomaly")
            if row["anomaly_disposition"] != "not_triggered":
                errors.append(f"{label}: non-triggered row has unexpected anomaly disposition")
        if row["primary_metric_retained"] != "True":
            errors.append(f"{label}: numerical candidates must remain in primary data")
        if row["industry_schema"] == "general":
            _validate_margin(row, "gross_profit", "gross_margin_pct", errors, label)
            _validate_margin(row, "operating_income", "operating_margin_pct", errors, label)
            _validate_margin(row, "net_income", "net_margin_pct", errors, label)
        else:
            for column in ("gross_margin_pct", "operating_margin_pct", "net_margin_pct"):
                if row[column] != "":
                    errors.append(f"{label}: non-general schema must not derive {column}")

    group_columns = [
        "market",
        "stock_id",
        "fiscal_year",
        "fiscal_quarter",
        "statement_scope",
        "period_basis",
    ]
    for key, part in history.groupby(group_columns, dropna=False):
        ordered = part.sort_values("revision_number")
        numbers = [int(value) for value in ordered["revision_number"]]
        expected = list(range(1, len(ordered) + 1))
        if numbers != expected:
            errors.append(f"revision sequence is not continuous for {key}: {numbers}")
        if set(ordered["revision_count"].astype(str)) != {str(len(ordered))}:
            errors.append(f"revision_count mismatch for {key}")
        latest = ordered[ordered["is_latest_known_revision"].astype(str).eq("True")]
        if len(latest) != 1 or latest.iloc[0]["revision_number"] != str(len(ordered)):
            errors.append(f"exactly the final revision must be latest for {key}")
        revisions = list(ordered["revision_id"].astype(str))
        expected_supersedes = ["", *revisions[:-1]]
        if list(ordered["supersedes_revision_id"].astype(str)) != expected_supersedes:
            errors.append(f"supersedes_revision_id chain mismatch for {key}")
    return errors


def validate_coverage(
    coverage: pd.DataFrame,
    history: pd.DataFrame,
    manifest: pd.DataFrame,
) -> list[str]:
    errors: list[str] = []
    if coverage.empty:
        return ["financial statement PIT coverage audit is empty"]
    total = coverage[coverage["row_type"].astype(str).eq("total")]
    if len(total) != 1:
        return ["financial statement PIT coverage must contain exactly one total row"]
    row = total.iloc[0]
    latest_manifest = manifest.sort_values("observed_at").drop_duplicates("source_id", keep="last")
    if int(row["captured_source_count"]) != latest_manifest["source_id"].nunique():
        errors.append("coverage total captured_source_count does not match manifest")
    if int(row["captured_raw_row_count"]) != int(
        pd.to_numeric(latest_manifest["source_row_count"], errors="coerce").fillna(0).sum()
    ):
        errors.append("coverage total captured_raw_row_count does not match manifest")
    if int(row["normalized_history_row_count"]) != len(history):
        errors.append("coverage total normalized_history_row_count does not match history")
    if int(row["dropped_invalid_identity_row_count"]) != int(
        pd.to_numeric(
            latest_manifest["dropped_invalid_identity_row_count"], errors="coerce"
        ).fillna(0).sum()
    ):
        errors.append("coverage total dropped_invalid_identity_row_count does not match manifest")
    if int(row["unique_stock_count"]) != history["stock_id"].nunique():
        errors.append("coverage total unique_stock_count does not match history")
    exact_count = int(history["historical_pit_eligible"].astype(str).eq("True").sum())
    if int(row["exact_filing_available_rows"]) != exact_count:
        errors.append("coverage exact_filing_available_rows does not match history")
    anomaly_count = int(history["numerical_anomaly_candidate"].astype(str).eq("True").sum())
    unresolved_count = int(
        history["anomaly_disposition"].astype(str).eq("unresolved_anomaly_candidate").sum()
    )
    if int(row["numerical_anomaly_candidate_rows"]) != anomaly_count:
        errors.append("coverage numerical_anomaly_candidate_rows does not match history")
    if int(row["unresolved_anomaly_candidate_rows"]) != unresolved_count:
        errors.append("coverage unresolved_anomaly_candidate_rows does not match history")
    if int(row["primary_metric_retained_rows"]) != len(history):
        errors.append("coverage primary_metric_retained_rows must equal all history rows")
    if row["formal_model_use_allowed"] != "False" or int(row["formal_model_allowed_rows"]) != 0:
        errors.append("financial statement coverage must keep formal model use blocked")
    if "separate_model_research_and_promotion_approval_required" not in row["blocker"]:
        errors.append("coverage blocker must require separate model research and promotion approval")
    if anomaly_count and "unresolved_numerical_anomaly_candidates" not in row["blocker"]:
        errors.append("coverage blocker must retain unresolved numerical anomaly candidates")
    if exact_count == 0 and row["pit_coverage_status"] != "current_snapshot_only_not_historical_pit":
        errors.append("current snapshot-only history must report current_snapshot_only_not_historical_pit")
    return errors


def validate_mirrors() -> list[str]:
    errors: list[str] = []
    for source, mirror in (
        (COVERAGE_PATH, DOCS_COVERAGE_PATH),
        (COVERAGE_MD_PATH, DOCS_COVERAGE_MD_PATH),
    ):
        if not source.exists() or not mirror.exists():
            errors.append(f"missing coverage mirror pair: {source.name}")
        elif source.read_bytes() != mirror.read_bytes():
            errors.append(f"coverage docs mirror differs: {mirror.relative_to(ROOT).as_posix()}")
    raw_dir = ROOT / "data" / "financial_statement_history" / "raw"
    if raw_dir.exists() and any(path.is_file() for path in raw_dir.rglob("*")):
        errors.append("raw financial statement archives must not be committed inside the repository")
    return errors


def validate(
    history: pd.DataFrame,
    manifest: pd.DataFrame,
    coverage: pd.DataFrame,
    source_rows: list[dict[str, str]],
    mapping_rows: list[dict[str, str]],
) -> list[str]:
    errors = validate_source_registry(source_rows)
    errors.extend(validate_metric_mapping(mapping_rows))
    source_ids = {row["source_id"] for row in source_rows}
    errors.extend(validate_manifest(manifest, source_ids))
    errors.extend(validate_history(history, manifest, source_ids))
    errors.extend(validate_coverage(coverage, history, manifest))
    return errors


def main() -> int:
    errors: list[str] = []
    source_rows = _read_rows(SOURCE_REGISTRY)
    mapping_rows = _read_rows(METRIC_MAPPING)
    history = _read_frame(HISTORY_PATH, HISTORY_COLUMNS, errors)
    manifest = _read_frame(MANIFEST_PATH, MANIFEST_COLUMNS, errors)
    coverage = _read_frame(COVERAGE_PATH, COVERAGE_COLUMNS, errors)
    if not errors:
        errors.extend(validate(history, manifest, coverage, source_rows, mapping_rows))
        errors.extend(validate_mirrors())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_financial_statement_history_rows={len(history)}")
    print(f"validated_financial_statement_manifest_rows={len(manifest)}")
    print(f"validated_financial_statement_coverage_rows={len(coverage)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
