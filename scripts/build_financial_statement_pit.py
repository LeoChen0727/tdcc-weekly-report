from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Iterable
from urllib.request import Request, urlopen

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import normalize_code, now_taipei, now_text, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTRY = ROOT / "config" / "daily_model_financial_statement_pit_sources.csv"
METRIC_MAPPING = ROOT / "config" / "daily_model_financial_statement_metric_mapping.csv"

DATA_FAMILY_ID = "financial_statement_point_in_time_history"
DATA_VERSION = "financial_statement_pit_v1"
MANIFEST_VERSION = "financial_statement_source_manifest_v1"
COVERAGE_AUDIT_ID = "financial_statement_pit_coverage_v1"

HISTORY_REL = Path("data/financial_statement_history/financial_statement_history.csv")
MANIFEST_REL = Path("data/financial_statement_history/financial_statement_source_manifest.csv")
COVERAGE_REL = Path("output/latest/research_backtest/financial_statement_pit_coverage_latest.csv")
COVERAGE_MD_REL = Path("output/latest/research_backtest/financial_statement_pit_coverage_latest.md")
DOCS_COVERAGE_REL = Path("docs/latest/financial_statement_pit_coverage_latest.csv")
DOCS_COVERAGE_MD_REL = Path("docs/latest/financial_statement_pit_coverage_latest.md")

OUTPUT_ALLOWLIST = {
    HISTORY_REL.as_posix(),
    MANIFEST_REL.as_posix(),
    COVERAGE_REL.as_posix(),
    COVERAGE_MD_REL.as_posix(),
    DOCS_COVERAGE_REL.as_posix(),
    DOCS_COVERAGE_MD_REL.as_posix(),
}

IDENTITY_ALIASES = {
    "source_table_date_raw": ("出表日期", "Date"),
    "fiscal_year_roc": ("年度", "Year"),
    "fiscal_quarter": ("季別", "Season"),
    "stock_id": ("公司代號", "SecuritiesCompanyCode"),
    "stock_name": ("公司名稱", "CompanyName"),
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


@dataclass(frozen=True)
class SourceCapture:
    source: dict[str, str]
    payload: bytes
    observed_at: str
    source_available_at: str
    availability_precision: str
    statement_scope: str
    period_basis: str
    raw_archive_ref: str
    archive_status: str
    fetch_status: str = "ok"
    declared_historical_pit_eligible: bool = False


def _bool_text(value: Any) -> str:
    return "True" if str(value or "").strip().lower() in {"true", "1", "yes"} else "False"


def _normalized_label(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or ""))
    return re.sub(r"\s+", "", text).strip()


def _normalized_row(row: dict[str, Any]) -> dict[str, tuple[str, str]]:
    return {
        _normalized_label(label): (str(label), "" if value is None else str(value).strip())
        for label, value in row.items()
    }


def _find_value(
    normalized_row: dict[str, tuple[str, str]], aliases: Iterable[str]
) -> tuple[str, str]:
    for alias in aliases:
        found = normalized_row.get(_normalized_label(alias))
        if found is not None:
            return found[1], found[0]
    return "", ""


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _safe_decimal(value: Any) -> Decimal | None:
    text = str(value or "").strip().replace(",", "").replace("％", "").replace("%", "")
    if text in {"", "-", "--", "N/A", "NA", "nan", "None"}:
        return None
    if text.startswith("(") and text.endswith(")"):
        text = f"-{text[1:-1]}"
    try:
        number = Decimal(text)
    except InvalidOperation:
        return None
    return number if number.is_finite() else None


def _decimal_text(value: Any) -> str:
    number = _safe_decimal(value)
    if number is None:
        return ""
    normalized = format(number, "f")
    if "." in normalized:
        normalized = normalized.rstrip("0").rstrip(".")
    return normalized or "0"


def _ratio_pct(numerator: Any, denominator: Any) -> str:
    top = _safe_decimal(numerator)
    bottom = _safe_decimal(denominator)
    if top is None or bottom is None or bottom == 0:
        return ""
    value = (top / bottom) * Decimal("100")
    return format(value.quantize(Decimal("0.0001")), "f")


def _numerical_anomaly_fields(
    metric_values: dict[str, str],
    gross_margin: str,
    operating_margin: str,
    net_margin: str,
) -> tuple[str, str, str, str, str]:
    triggers: list[str] = []
    eps = _safe_decimal(metric_values.get("basic_eps", ""))
    if eps is not None and abs(eps) >= Decimal("50"):
        triggers.append("basic_eps_abs_ge_50")
    for label, value in (
        ("gross_margin_abs_ge_500pct", gross_margin),
        ("operating_margin_abs_ge_500pct", operating_margin),
        ("net_margin_abs_ge_500pct", net_margin),
    ):
        number = _safe_decimal(value)
        if number is not None and abs(number) >= Decimal("500"):
            triggers.append(label)
    if triggers:
        return (
            "True",
            ";".join(triggers),
            "unresolved_anomaly_candidate",
            "True",
            "source_payload_and_formula_traced_independent_corroboration_pending",
        )
    return "False", "", "not_triggered", "True", "not_required"


def _parse_roc_date(value: Any) -> str:
    digits = re.sub(r"\D", "", str(value or ""))
    if len(digits) == 7:
        year = int(digits[:3]) + 1911
        month = int(digits[3:5])
        day = int(digits[5:7])
    elif len(digits) == 8:
        year = int(digits[:4])
        month = int(digits[4:6])
        day = int(digits[6:8])
    else:
        return ""
    try:
        return datetime(year, month, day).date().isoformat()
    except ValueError:
        return ""


def _parse_fiscal_year(value: Any) -> tuple[str, str]:
    digits = re.sub(r"\D", "", str(value or ""))
    if not digits:
        return "", ""
    raw = str(int(digits))
    year = int(raw)
    if year < 1911:
        year += 1911
    if year < 1990 or year > 2200:
        return "", raw
    return str(year), raw


def _parse_quarter(value: Any) -> str:
    match = re.search(r"([1-4])", str(value or ""))
    return match.group(1) if match else ""


def _timestamp_now() -> str:
    return now_taipei().isoformat(timespec="seconds")


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [
            {str(key): str(value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(handle)
        ]


def load_source_registry(path: Path = SOURCE_REGISTRY) -> dict[str, dict[str, str]]:
    rows = _read_csv_rows(path)
    by_id: dict[str, dict[str, str]] = {}
    for row in rows:
        source_id = row["source_id"]
        if source_id in by_id:
            raise ValueError(f"duplicate source_id: {source_id}")
        by_id[source_id] = row
    return by_id


def load_metric_mapping(
    path: Path = METRIC_MAPPING,
) -> tuple[dict[str, dict[str, tuple[str, ...]]], dict[str, set[str]]]:
    rows = _read_csv_rows(path)
    aliases: dict[str, dict[str, tuple[str, ...]]] = {}
    required: dict[str, set[str]] = {}
    for row in rows:
        schema = row["industry_schema"]
        metric = row["canonical_metric"]
        schema_map = aliases.setdefault(schema, {})
        if metric in schema_map:
            raise ValueError(f"duplicate metric mapping: {schema}/{metric}")
        schema_map[metric] = tuple(
            part.strip() for part in row["source_label_aliases"].split(";") if part.strip()
        )
        if _bool_text(row["required_for_schema"]) == "True":
            required.setdefault(schema, set()).add(metric)
    return aliases, required


def _decode_payload(payload: bytes) -> list[dict[str, Any]]:
    decoded = json.loads(payload.decode("utf-8-sig"))
    if isinstance(decoded, dict):
        for key in ("data", "rows", "result"):
            if isinstance(decoded.get(key), list):
                decoded = decoded[key]
                break
    if not isinstance(decoded, list):
        raise ValueError("financial statement source payload must be a JSON row list")
    return [row for row in decoded if isinstance(row, dict)]


def _capture_historical_eligible(capture: SourceCapture) -> bool:
    if capture.declared_historical_pit_eligible and (
        capture.source.get("history_mode") != "historical_point_in_time"
        or capture.source.get("availability_semantics")
        != "exact_company_filing_availability"
        or capture.source.get("source_kind") == "official_openapi_current_snapshot"
    ):
        raise ValueError(
            "historical PIT eligibility requires a registry-owned historical source; "
            f"current source_id={capture.source.get('source_id', '')} cannot self-declare it"
        )
    return (
        capture.declared_historical_pit_eligible
        and capture.availability_precision
        in {"exact_company_filing_timestamp", "exact_company_filing_date"}
        and bool(capture.source_available_at)
        and capture.statement_scope
        not in {"", "unknown", "official_endpoint_reported_scope"}
    )


def normalize_capture(
    capture: SourceCapture,
    metric_aliases: dict[str, dict[str, tuple[str, ...]]],
    required_metrics: dict[str, set[str]],
) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows = _decode_payload(capture.payload)
    payload_sha = _sha256_bytes(capture.payload)
    source = capture.source
    schema = source["industry_schema"]
    schema_aliases = metric_aliases.get(schema, {})
    generated_at = now_text()
    historical_eligible = _capture_historical_eligible(capture)
    output_rows: list[dict[str, Any]] = []

    for raw_row in rows:
        normalized = _normalized_row(raw_row)
        identity: dict[str, str] = {}
        for field, aliases in IDENTITY_ALIASES.items():
            identity[field] = _find_value(normalized, aliases)[0]
        fiscal_year, fiscal_year_roc = _parse_fiscal_year(identity["fiscal_year_roc"])
        fiscal_quarter = _parse_quarter(identity["fiscal_quarter"])
        stock_id = normalize_code(identity["stock_id"])
        if not stock_id or not fiscal_year or not fiscal_quarter:
            continue

        metric_values = {metric: "" for metric in CANONICAL_METRICS}
        source_labels: list[str] = []
        for metric, aliases in schema_aliases.items():
            value, label = _find_value(normalized, aliases)
            metric_values[metric] = _decimal_text(value)
            if label:
                source_labels.append(f"{metric}={label}")

        row_payload = _canonical_json_bytes(raw_row)
        row_sha = _sha256_bytes(row_payload)
        revision_metric_sha = _sha256_bytes(_canonical_json_bytes(metric_values))
        revision_key = "|".join(
            [
                source["market"],
                stock_id,
                fiscal_year,
                fiscal_quarter,
                capture.statement_scope,
                capture.period_basis,
                schema,
                revision_metric_sha,
            ]
        )
        revision_id = hashlib.sha256(revision_key.encode("utf-8")).hexdigest()
        required = required_metrics.get(schema, set())
        missing_required = sorted(metric for metric in required if not metric_values.get(metric, ""))
        pit_status = (
            "historical_pit_exact_company_filing_available"
            if historical_eligible
            else "current_snapshot_first_observed_only"
            if capture.availability_precision == "first_observed_at"
            else "blocked_incomplete_filing_availability"
        )
        if schema == "general":
            gross_margin = _ratio_pct(metric_values["gross_profit"], metric_values["operating_revenue"])
            operating_margin = _ratio_pct(
                metric_values["operating_income"], metric_values["operating_revenue"]
            )
            net_margin = _ratio_pct(metric_values["net_income"], metric_values["operating_revenue"])
            margin_status = (
                "general_schema_ratios_derived_from_cumulative_reported_values"
                if any((gross_margin, operating_margin, net_margin))
                else "general_schema_missing_or_zero_revenue"
            )
        else:
            gross_margin = operating_margin = net_margin = ""
            margin_status = "not_applicable_non_general_schema"
        (
            anomaly_candidate,
            anomaly_triggers,
            anomaly_disposition,
            primary_retained,
            anomaly_evidence_status,
        ) = _numerical_anomaly_fields(
            metric_values,
            gross_margin,
            operating_margin,
            net_margin,
        )

        output_rows.append(
            {
                "generated_at": generated_at,
                "data_family_id": DATA_FAMILY_ID,
                "data_version": DATA_VERSION,
                "source_id": source["source_id"],
                "source_kind": source["source_kind"],
                "market": source["market"],
                "industry_schema": schema,
                "source_url": source["source_url"],
                "raw_archive_ref": capture.raw_archive_ref,
                "raw_payload_sha256": payload_sha,
                "source_row_sha256": row_sha,
                "source_table_date": _parse_roc_date(identity["source_table_date_raw"]),
                "source_table_date_raw": identity["source_table_date_raw"],
                "observed_at": capture.observed_at,
                "first_observed_at": capture.observed_at,
                "source_available_at": capture.source_available_at,
                "availability_precision": capture.availability_precision,
                "pit_status": pit_status,
                "historical_pit_eligible": _bool_text(historical_eligible),
                "research_asof_join_allowed": _bool_text(bool(capture.source_available_at)),
                "allowed_for_formal_model_use": "False",
                "fiscal_year": fiscal_year,
                "fiscal_year_roc": fiscal_year_roc,
                "fiscal_quarter": fiscal_quarter,
                "fiscal_period": f"{fiscal_year}Q{fiscal_quarter}",
                "statement_scope": capture.statement_scope,
                "period_basis": capture.period_basis,
                "monetary_unit": source["monetary_unit"],
                "per_share_unit": source["per_share_unit"],
                "stock_id": stock_id,
                "stock_name": identity["stock_name"],
                "revision_id": revision_id,
                "revision_number": "",
                "revision_count": "",
                "supersedes_revision_id": "",
                "is_latest_known_revision": "",
                **metric_values,
                "gross_margin_pct": gross_margin,
                "operating_margin_pct": operating_margin,
                "net_margin_pct": net_margin,
                "margin_derivation_status": margin_status,
                "metric_completeness_status": (
                    "required_metrics_complete"
                    if not missing_required
                    else f"missing_required_metrics:{';'.join(missing_required)}"
                ),
                "source_metric_labels": ";".join(source_labels),
                "provenance_status": "raw_payload_sha_and_source_row_sha_verified",
                "numerical_anomaly_candidate": anomaly_candidate,
                "numerical_anomaly_triggers": anomaly_triggers,
                "anomaly_disposition": anomaly_disposition,
                "primary_metric_retained": primary_retained,
                "anomaly_evidence_status": anomaly_evidence_status,
                "coverage_note": (
                    "Exact company filing availability is registered and usable for research as-of joins; "
                    "formal model use still requires historical coverage validation and a separate promotion."
                    if historical_eligible
                    else "Current OpenAPI rows are usable only from first_observed_at forward and are not historical PIT. "
                    "Exact company filing availability plus historical coverage validation is required before model use."
                ),
            }
        )

    history = pd.DataFrame(output_rows, columns=HISTORY_COLUMNS)
    manifest = {
        "generated_at": generated_at,
        "manifest_version": MANIFEST_VERSION,
        "source_id": source["source_id"],
        "source_kind": source["source_kind"],
        "market": source["market"],
        "industry_schema": schema,
        "source_url": source["source_url"],
        "observed_at": capture.observed_at,
        "source_available_at": capture.source_available_at,
        "availability_precision": capture.availability_precision,
        "statement_scope": capture.statement_scope,
        "period_basis": capture.period_basis,
        "monetary_unit": source["monetary_unit"],
        "per_share_unit": source["per_share_unit"],
        "raw_archive_ref": capture.raw_archive_ref,
        "raw_payload_sha256": payload_sha,
        "raw_byte_count": len(capture.payload),
        "source_row_count": len(rows),
        "normalized_row_count": len(history),
        "dropped_invalid_identity_row_count": len(rows) - len(history),
        "fetch_status": capture.fetch_status,
        "archive_status": capture.archive_status,
        "historical_pit_eligible": _bool_text(historical_eligible),
        "current_snapshot_only": _bool_text(source["history_mode"] == "current_snapshot_only"),
        "notes": source["notes"],
    }
    return history, manifest


def _is_inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def fetch_current_sources(
    raw_archive_dir: Path,
    sources: dict[str, dict[str, str]],
    *,
    timeout_seconds: int = 60,
) -> list[SourceCapture]:
    if _is_inside(raw_archive_dir, ROOT):
        raise ValueError("raw archive directory must be outside the repository")
    raw_archive_dir.mkdir(parents=True, exist_ok=True)
    observed_at = _timestamp_now()
    captures: list[SourceCapture] = []
    for source_id, source in sources.items():
        if _bool_text(source["enabled"]) != "True":
            continue
        request = Request(
            source["source_url"],
            headers={"User-Agent": "taiwan-stock-recommendation-financial-statement-pit/1.0"},
        )
        with urlopen(request, timeout=timeout_seconds) as response:
            payload = response.read()
        _decode_payload(payload)
        payload_sha = _sha256_bytes(payload)
        stamp = re.sub(r"\D", "", observed_at)[:14]
        raw_path = raw_archive_dir / f"{stamp}_{source_id}_{payload_sha[:16]}.json"
        if not raw_path.exists():
            raw_path.write_bytes(payload)
        if _sha256_bytes(raw_path.read_bytes()) != payload_sha:
            raise RuntimeError(f"raw archive SHA mismatch: {raw_path}")
        captures.append(
            SourceCapture(
                source=source,
                payload=payload,
                observed_at=observed_at,
                source_available_at=observed_at,
                availability_precision="first_observed_at",
                statement_scope=source["statement_scope"],
                period_basis=source["period_basis"],
                raw_archive_ref=f"sha256://{payload_sha}",
                archive_status="external_content_addressed_archive_verified",
                declared_historical_pit_eligible=False,
            )
        )
    return captures


def captures_from_manifest(
    manifest_path: Path,
    sources: dict[str, dict[str, str]],
) -> list[SourceCapture]:
    required = {
        "source_id",
        "local_raw_path",
        "observed_at",
        "source_available_at",
        "availability_precision",
        "statement_scope",
        "period_basis",
        "raw_archive_ref",
        "archive_status",
        "expected_sha256",
        "historical_pit_eligible",
    }
    rows = _read_csv_rows(manifest_path)
    captures: list[SourceCapture] = []
    for row in rows:
        missing = required - set(row)
        if missing:
            raise ValueError(f"capture manifest missing columns: {sorted(missing)}")
        source_id = row["source_id"]
        if source_id not in sources:
            raise ValueError(f"capture manifest has unknown source_id: {source_id}")
        raw_path = Path(row["local_raw_path"])
        payload = raw_path.read_bytes()
        payload_sha = _sha256_bytes(payload)
        if payload_sha != row["expected_sha256"]:
            raise ValueError(f"capture manifest SHA mismatch: {raw_path}")
        captures.append(
            SourceCapture(
                source=sources[source_id],
                payload=payload,
                observed_at=row["observed_at"],
                source_available_at=row["source_available_at"],
                availability_precision=row["availability_precision"],
                statement_scope=row["statement_scope"],
                period_basis=row["period_basis"],
                raw_archive_ref=row["raw_archive_ref"],
                archive_status=row["archive_status"],
                declared_historical_pit_eligible=(
                    _bool_text(row["historical_pit_eligible"]) == "True"
                ),
            )
        )
    return captures


def _read_existing(path: Path, columns: tuple[str, ...]) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=columns)
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    missing = set(columns) - set(frame.columns)
    if missing:
        raise ValueError(f"existing artifact has incompatible schema: {path}; missing={sorted(missing)}")
    return frame[list(columns)].copy()


def assign_revision_lineage(history: pd.DataFrame) -> pd.DataFrame:
    if history.empty:
        return pd.DataFrame(columns=HISTORY_COLUMNS)
    out = history.copy().fillna("")
    out = out.sort_values(
        ["source_available_at", "observed_at", "source_row_sha256", "revision_id"]
    ).drop_duplicates("revision_id", keep="first")
    group_columns = [
        "market",
        "stock_id",
        "fiscal_year",
        "fiscal_quarter",
        "statement_scope",
        "period_basis",
    ]
    parts: list[pd.DataFrame] = []
    for _key, part in out.groupby(group_columns, sort=False, dropna=False):
        ordered = part.sort_values(
            ["source_available_at", "observed_at", "source_row_sha256", "revision_id"]
        ).copy()
        revisions = list(ordered["revision_id"].astype(str))
        ordered["revision_number"] = [str(index + 1) for index in range(len(ordered))]
        ordered["revision_count"] = str(len(ordered))
        ordered["supersedes_revision_id"] = ["", *revisions[:-1]]
        ordered["is_latest_known_revision"] = [
            "True" if index == len(ordered) - 1 else "False"
            for index in range(len(ordered))
        ]
        parts.append(ordered)
    combined = pd.concat(parts, ignore_index=True)
    return combined.sort_values(
        ["market", "stock_id", "fiscal_year", "fiscal_quarter", "revision_number"]
    )[list(HISTORY_COLUMNS)].reset_index(drop=True)


def merge_history(existing: pd.DataFrame, new_rows: pd.DataFrame) -> pd.DataFrame:
    old = existing.copy()
    old["_new_priority"] = 0
    new = new_rows.copy()
    new["_new_priority"] = 1
    combined = pd.concat([old, new], ignore_index=True)
    combined = combined.where(pd.notna(combined), "")
    if combined.empty:
        return pd.DataFrame(columns=HISTORY_COLUMNS)
    earliest_first = combined.groupby("revision_id")["first_observed_at"].min().to_dict()
    earliest_observed = combined.groupby("revision_id")["observed_at"].min().to_dict()
    combined = combined.sort_values(["revision_id", "_new_priority"])
    combined = combined.drop_duplicates("revision_id", keep="last")
    combined["first_observed_at"] = combined["revision_id"].map(earliest_first)
    first_observed_mask = combined["availability_precision"].astype(str).eq("first_observed_at")
    combined.loc[first_observed_mask, "source_available_at"] = combined.loc[
        first_observed_mask, "revision_id"
    ].map(earliest_first)
    combined.loc[first_observed_mask, "observed_at"] = combined.loc[
        first_observed_mask, "revision_id"
    ].map(earliest_observed)
    combined = combined.drop(columns=["_new_priority"])
    return assign_revision_lineage(combined)


def merge_manifest(existing: pd.DataFrame, new_rows: pd.DataFrame) -> pd.DataFrame:
    old = existing.copy()
    old["_new_priority"] = 0
    new = new_rows.copy()
    new["_new_priority"] = 1
    combined = pd.concat([old, new], ignore_index=True)
    combined = combined.where(pd.notna(combined), "")
    if combined.empty:
        return pd.DataFrame(columns=MANIFEST_COLUMNS)
    key = ["source_id", "raw_payload_sha256"]
    earliest_observed = combined.groupby(key)["observed_at"].min().to_dict()
    combined = combined.sort_values(["source_id", "raw_payload_sha256", "_new_priority"])
    combined = combined.drop_duplicates(key, keep="last")
    combined["observed_at"] = [
        earliest_observed[(row["source_id"], row["raw_payload_sha256"])]
        for _, row in combined.iterrows()
    ]
    first_observed_mask = combined["availability_precision"].astype(str).eq("first_observed_at")
    combined.loc[first_observed_mask, "source_available_at"] = combined.loc[
        first_observed_mask, "observed_at"
    ]
    combined = combined.drop(columns=["_new_priority"])
    return combined[list(MANIFEST_COLUMNS)].reset_index(drop=True)


def _coverage_pct(frame: pd.DataFrame, column: str) -> str:
    if frame.empty:
        return "0.0000"
    present = frame[column].astype(str).str.strip().ne("").sum()
    return f"{present / len(frame) * 100:.4f}"


def build_coverage(history: pd.DataFrame, manifest: pd.DataFrame | None = None) -> pd.DataFrame:
    generated_at = now_text()
    if manifest is None:
        manifest = history[["source_id", "market", "industry_schema"]].drop_duplicates().copy()
        manifest["source_row_count"] = 1
        manifest["dropped_invalid_identity_row_count"] = 0
    latest_manifest = manifest.sort_values("observed_at" if "observed_at" in manifest else "source_id")
    latest_manifest = latest_manifest.drop_duplicates("source_id", keep="last")
    group_keys = sorted(
        {
            (str(row["market"]), str(row["industry_schema"]))
            for _, row in latest_manifest.iterrows()
        }
    )
    grouped: list[tuple[str, str, pd.DataFrame, pd.DataFrame]] = [
        ("ALL", "ALL", history, latest_manifest)
    ]
    for market, schema in group_keys:
        history_part = history[
            history["market"].astype(str).eq(market)
            & history["industry_schema"].astype(str).eq(schema)
        ].copy()
        manifest_part = latest_manifest[
            latest_manifest["market"].astype(str).eq(market)
            & latest_manifest["industry_schema"].astype(str).eq(schema)
        ].copy()
        grouped.append((market, schema, history_part, manifest_part))
    rows: list[dict[str, Any]] = []
    for market, schema, part, manifest_part in grouped:
        exact_rows = int(
            part["historical_pit_eligible"].astype(str).eq("True").sum()
        ) if not part.empty else 0
        current_rows = int(
            part["pit_status"].astype(str).eq("current_snapshot_first_observed_only").sum()
        ) if not part.empty else 0
        if part.empty:
            pit_status = "current_snapshot_empty_placeholder"
        elif exact_rows == 0:
            pit_status = "current_snapshot_only_not_historical_pit"
        elif exact_rows < len(part):
            pit_status = "partial_historical_pit_coverage"
        else:
            pit_status = "historical_pit_rows_present_promotion_gate_closed"
        periods = sorted(value for value in part["fiscal_period"].astype(str) if value)
        rows.append(
            {
                "generated_at": generated_at,
                "audit_id": COVERAGE_AUDIT_ID,
                "row_type": "total" if market == "ALL" else "market_schema",
                "market": market,
                "industry_schema": schema,
                "captured_source_count": int(manifest_part["source_id"].nunique()),
                "captured_raw_row_count": int(
                    pd.to_numeric(manifest_part["source_row_count"], errors="coerce").fillna(0).sum()
                ),
                "normalized_history_row_count": len(part),
                "dropped_invalid_identity_row_count": int(
                    pd.to_numeric(
                        manifest_part["dropped_invalid_identity_row_count"], errors="coerce"
                    ).fillna(0).sum()
                ),
                "unique_stock_count": int(part["stock_id"].nunique()) if not part.empty else 0,
                "fiscal_period_min": periods[0] if periods else "",
                "fiscal_period_max": periods[-1] if periods else "",
                "exact_filing_available_rows": exact_rows,
                "current_snapshot_only_rows": current_rows,
                "research_asof_join_allowed_rows": int(
                    part["research_asof_join_allowed"].astype(str).eq("True").sum()
                ) if not part.empty else 0,
                "formal_model_allowed_rows": int(
                    part["allowed_for_formal_model_use"].astype(str).eq("True").sum()
                ) if not part.empty else 0,
                "operating_revenue_coverage_pct": _coverage_pct(part, "operating_revenue"),
                "gross_profit_coverage_pct": _coverage_pct(part, "gross_profit"),
                "operating_income_coverage_pct": _coverage_pct(part, "operating_income"),
                "non_operating_income_expense_coverage_pct": _coverage_pct(
                    part, "non_operating_income_expense"
                ),
                "net_income_coverage_pct": _coverage_pct(part, "net_income"),
                "basic_eps_coverage_pct": _coverage_pct(part, "basic_eps"),
                "gross_margin_coverage_pct": _coverage_pct(part, "gross_margin_pct"),
                "operating_margin_coverage_pct": _coverage_pct(part, "operating_margin_pct"),
                "numerical_anomaly_candidate_rows": int(
                    part["numerical_anomaly_candidate"].astype(str).eq("True").sum()
                ) if not part.empty else 0,
                "unresolved_anomaly_candidate_rows": int(
                    part["anomaly_disposition"].astype(str).eq("unresolved_anomaly_candidate").sum()
                ) if not part.empty else 0,
                "primary_metric_retained_rows": int(
                    part["primary_metric_retained"].astype(str).eq("True").sum()
                ) if not part.empty else 0,
                "pit_coverage_status": pit_status,
                "formal_model_use_allowed": "False",
                "blocker": (
                    "exact_company_filing_availability_and_historical_coverage_not_complete;"
                    "unresolved_numerical_anomaly_candidates_require_bottom_level_disposition;"
                    "separate_model_research_and_promotion_approval_required"
                ),
            }
        )
    return pd.DataFrame(rows, columns=COVERAGE_COLUMNS)


def _write_coverage_markdown(coverage: pd.DataFrame, path: Path) -> None:
    total = coverage[coverage["row_type"].astype(str).eq("total")]
    total_row = total.iloc[0].to_dict() if not total.empty else {}
    lines = [
        "# Financial Statement Point-In-Time Coverage",
        "",
        f"- generated_at: `{now_text()}`",
        f"- audit_id: `{COVERAGE_AUDIT_ID}`",
        f"- captured_sources: `{total_row.get('captured_source_count', 0)}`",
        f"- captured_raw_rows: `{total_row.get('captured_raw_row_count', 0)}`",
        f"- normalized_history_rows: `{total_row.get('normalized_history_row_count', 0)}`",
        f"- unique_stocks: `{total_row.get('unique_stock_count', 0)}`",
        f"- fiscal_period_range: `{total_row.get('fiscal_period_min', '')}` to `{total_row.get('fiscal_period_max', '')}`",
        f"- unresolved_numerical_anomaly_candidates: `{total_row.get('unresolved_anomaly_candidate_rows', 0)}`; all remain in primary data.",
        f"- pit_coverage_status: `{total_row.get('pit_coverage_status', 'missing')}`",
        "- formal_model_use_allowed: `False`",
        "- boundary: current TWSE/TPEX OpenAPI data is recorded from `first_observed_at` forward. The global table date is not treated as a company filing date.",
        "- historical requirement: exact company filing availability, revision-preserving MOPS/XBRL history, and coverage validation must pass before any model may consume EPS, margins, operating income, non-operating income, or net income as formal evidence.",
        "",
        "## Coverage Rows",
        "",
        "| market | industry_schema | rows | stocks | EPS coverage | net income coverage | PIT status |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for _, row in coverage.iterrows():
        lines.append(
            "| {market} | {schema} | {rows} | {stocks} | {eps}% | {net}% | {status} |".format(
                market=row["market"],
                schema=row["industry_schema"],
                rows=row["normalized_history_row_count"],
                stocks=row["unique_stock_count"],
                eps=row["basic_eps_coverage_pct"],
                net=row["net_income_coverage_pct"],
                status=row["pit_coverage_status"],
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def _output_paths(output_root: Path) -> dict[str, Path]:
    paths = {
        relative.as_posix(): output_root / relative
        for relative in (
            HISTORY_REL,
            MANIFEST_REL,
            COVERAGE_REL,
            COVERAGE_MD_REL,
            DOCS_COVERAGE_REL,
            DOCS_COVERAGE_MD_REL,
        )
    }
    if set(paths) != OUTPUT_ALLOWLIST:
        raise RuntimeError("financial statement producer output allowlist drift")
    return paths


def build_and_write(captures: list[SourceCapture], output_root: Path = ROOT) -> dict[str, Path]:
    if not captures:
        raise ValueError("no financial statement source captures supplied")
    aliases, required = load_metric_mapping()
    history_frames: list[pd.DataFrame] = []
    manifest_rows: list[dict[str, Any]] = []
    for capture in captures:
        history, manifest = normalize_capture(capture, aliases, required)
        history_frames.append(history)
        manifest_rows.append(manifest)
    new_history = (
        pd.concat(history_frames, ignore_index=True)
        if history_frames
        else pd.DataFrame(columns=HISTORY_COLUMNS)
    )
    if new_history.empty:
        raise RuntimeError("official financial statement captures contained no valid company rows")

    paths = _output_paths(output_root)
    existing_history = _read_existing(paths[HISTORY_REL.as_posix()], HISTORY_COLUMNS)
    existing_manifest = _read_existing(paths[MANIFEST_REL.as_posix()], MANIFEST_COLUMNS)
    history = merge_history(existing_history, new_history)
    manifest = merge_manifest(
        existing_manifest,
        pd.DataFrame(manifest_rows, columns=MANIFEST_COLUMNS),
    )
    coverage = build_coverage(history, manifest)

    write_csv(history, paths[HISTORY_REL.as_posix()])
    write_csv(manifest, paths[MANIFEST_REL.as_posix()])
    write_csv(coverage, paths[COVERAGE_REL.as_posix()])
    write_csv(coverage, paths[DOCS_COVERAGE_REL.as_posix()])
    _write_coverage_markdown(coverage, paths[COVERAGE_MD_REL.as_posix()])
    paths[DOCS_COVERAGE_MD_REL.as_posix()].parent.mkdir(parents=True, exist_ok=True)
    paths[DOCS_COVERAGE_MD_REL.as_posix()].write_bytes(
        paths[COVERAGE_MD_REL.as_posix()].read_bytes()
    )
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the independent financial-statement PIT data layer")
    parser.add_argument("--fetch-current", action="store_true")
    parser.add_argument("--raw-archive-dir", type=Path)
    parser.add_argument("--capture-manifest", type=Path)
    parser.add_argument("--output-root", type=Path, default=ROOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    sources = load_source_registry()
    captures: list[SourceCapture] = []
    if args.fetch_current:
        if args.raw_archive_dir is None:
            raise ValueError("--raw-archive-dir outside the repository is required with --fetch-current")
        captures.extend(fetch_current_sources(args.raw_archive_dir, sources))
    if args.capture_manifest is not None:
        captures.extend(captures_from_manifest(args.capture_manifest, sources))
    paths = build_and_write(captures, args.output_root)
    print(f"financial_statement_pit_history={paths[HISTORY_REL.as_posix()]}")
    print(f"financial_statement_source_manifest={paths[MANIFEST_REL.as_posix()]}")
    print(f"financial_statement_pit_coverage={paths[COVERAGE_REL.as_posix()]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
