from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path
import re

from model_data_independence import DATA_SHARING_COLUMNS, strict_csv_rows, validate_data_sharing


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config" / "daily_model_background_data_registry.csv"

REQUIRED_COLUMN_ORDER = (
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
REQUIRED_COLUMNS = set(REQUIRED_COLUMN_ORDER)

VALID_SCOPES = {
    "shared_objective",
    "shared_replay_evidence",
    "shared_replay_source",
    "latest_only_context",
    "model_specific",
    "model_research_output",
    "missing_shared_data_family",
}

VALID_OWNERS = {
    "daily_model_maintenance",
    "daily_production",
    "research_backtest",
    "official_price_data",
    "tdcc_weekly",
    "market_risk",
    "catalyst_event",
}

VALID_CLEANUP_STATUS = {
    "active",
    "blocked_missing_source_or_validator",
    "deprecated_candidate",
}

REQUIRED_FAMILIES = {
    "stock_price_history",
    "tdcc_stock_history",
    "market_index_history",
    "daily_model_signal_snapshots",
    "daily_all_candidates_snapshots",
    "daily_model_snapshot_revision_manifest",
    "daily_model_signal_background_feature_panel",
    "daily_model_background_feature_catalog",
    "monthly_revenue_history",
    "monthly_revenue_coverage_backfill_audit",
    "monthly_revenue_point_in_time_panel",
    "financial_statement_point_in_time_history",
    "financial_statement_source_manifest",
    "financial_statement_pit_coverage_audit",
    "revenue_unreacted_range_source_snapshot_projection",
    "hot_theme_pullback_published_signal_research_outputs",
    "pullback_short_reclaim_research_outputs",
    "tdcc_stealth_accumulation_published_signal_research_outputs",
    "tdcc_stealth_accumulation_pit_replay_availability_audit",
    "tdcc_stealth_accumulation_historical_selector_replay_outputs",
    "tdcc_short_term_continuation_d5_d10_research_outputs",
    "price_pullback_23ema_research_outputs",
    "price_pullback_23ema_operation_section",
    "neckline_context_interpretation",
    "w_bottom_shape_interpretation",
}

MODEL_SPECIFIC_FORBIDDEN_CONSUMERS = {"", "all_models"}


def split_list(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def load_registry(errors: list[str]) -> list[dict[str, str]]:
    return strict_csv_rows(REGISTRY, REQUIRED_COLUMN_ORDER, errors)


def artifact_exists(pattern: str) -> bool:
    if not pattern:
        return False
    normalized = pattern.replace("\\", "/")
    if "*" in normalized or "?" in normalized or "[" in normalized:
        return bool(list(ROOT.glob(normalized)))
    return (ROOT / normalized).exists()


def _strict_capture_date(value: str) -> str:
    if re.fullmatch(r"[0-9]{8}", value) is None:
        raise ValueError(f"invalid YYYYMMDD date: {value!r}")
    parsed = datetime.strptime(value, "%Y%m%d")
    if parsed.strftime("%Y%m%d") != value:
        raise ValueError(f"invalid YYYYMMDD date: {value!r}")
    return value


def _capture_csv_rows(path: Path, required_date_column: str) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        columns = reader.fieldnames or []
        if required_date_column not in columns or len(columns) != len(set(columns)):
            raise ValueError(f"missing or duplicate {required_date_column} column: {path}")
        rows = list(reader)
    if not rows or any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError(f"empty or malformed capture date CSV: {path}")
    return rows


def validate_price_pullback_forward_capture_registration(
    row: dict[str, str], *, require_artifacts: bool
) -> tuple[list[str], bool]:
    """Allow only the registered 23EMA pre-capture absence, never other families."""

    family = "price_pullback_23ema_operation_section"
    artifact_pattern = "output/history/daily_model_snapshots/daily_price_pullback_23ema_operation_section_*.csv"
    expected = {
        "data_family_id": family,
        "scope": "model_specific",
        "owner_lane": "daily_model_maintenance",
        "producer": "scripts/update_daily_published_model_snapshots.py",
        "artifact_path": artifact_pattern,
        "source_artifacts": "output/latest/daily_price_pullback_23ema_operation_section_latest.csv",
        "consumer_surfaces": "daily_production",
        "consumer_models": "price_pullback_23ema",
        "point_in_time_status": "forward_capture_not_before_20261019_consumer_enabled_not_full_PIT",
        "cleanup_status": "active",
    }
    errors = [
        f"{family}: forward capture metadata mismatch for {field}: expected={value!r} observed={row.get(field)!r}"
        for field, value in expected.items() if row.get(field) != value
    ]
    marker = re.fullmatch(
        r"forward_capture_not_before_([0-9]{8})_consumer_enabled_not_full_PIT",
        row.get("point_in_time_status", ""),
    )
    try:
        if marker is None:
            raise ValueError("expected a registered capture cutoff with consumer_enabled")
        capture_not_before = _strict_capture_date(marker.group(1))
    except ValueError as exc:
        errors.append(f"{family}: invalid forward capture registry marker: {exc}")
        return errors, False
    sharing = strict_csv_rows(
        ROOT / "config/daily_model_data_sharing_registry.csv", DATA_SHARING_COLUMNS, errors
    )
    registrations = [item for item in sharing if item["data_family_id"] == family]
    if len(registrations) != 1:
        errors.append(f"{family}: forward capture requires exactly one data-sharing registration")
    else:
        expected_sharing = {
            "ownership_mode": "model_owned_not_shared",
            "owner_model_or_family": "price_pullback_23ema",
            "registered_producers": expected["producer"],
            "producer_write_scope": artifact_pattern,
            "approved_consumer_models": "price_pullback_23ema",
            "consumer_access_mode": "owner_model_original_r1_confirmation_history_consumer_enabled",
        }
        for field, value in expected_sharing.items():
            if registrations[0].get(field) != value:
                errors.append(f"{family}: forward capture data-sharing metadata mismatch for {field}")
    if not require_artifacts:
        return errors, False

    freshness_path = ROOT / "output/latest/data_freshness_latest.csv"
    try:
        freshness = _capture_csv_rows(freshness_path, "main_price_date")
        if len(freshness) != 1:
            raise ValueError("freshness must contain exactly one authoritative row")
        report_date = _strict_capture_date(freshness[0]["main_price_date"])
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        errors.append(f"{family}: valid official data_freshness main_price_date is required: {exc}")
        return errors, False

    for path in ROOT.glob(artifact_pattern):
        try:
            if not path.is_file():
                raise ValueError("matching capture path must be a file")
            match = re.fullmatch(
                r"daily_price_pullback_23ema_operation_section_([0-9]{8})_r[1-9][0-9]*_[0-9a-f]{12}\.csv",
                path.name,
            )
            if match is None:
                raise ValueError("capture filename must identify an immutable dated revision")
            snapshot_date = _strict_capture_date(match.group(1))
            if snapshot_date < capture_not_before:
                raise ValueError("capture snapshot predates the permitted cutoff; historical backfill is forbidden")
            if snapshot_date > report_date:
                raise ValueError("capture snapshot date exceeds official main_price_date")
            snapshot_rows = _capture_csv_rows(path, "operation_asof_date")
            if any(_strict_capture_date(item["operation_asof_date"]) != snapshot_date for item in snapshot_rows):
                raise ValueError("capture operation_asof_date must match its immutable snapshot date")
        except (OSError, UnicodeError, ValueError, csv.Error) as exc:
            errors.append(f"{family}: invalid physical capture artifact {path}: {exc}")
    return errors, not errors and report_date < capture_not_before


def validate_registry(
    rows: list[dict[str, str]],
    *,
    require_artifacts: bool = True,
) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for idx, row in enumerate(rows, start=2):
        data_family_id = row["data_family_id"]
        scope = row["scope"]
        owner = row["owner_lane"]
        cleanup_status = row["cleanup_status"]
        artifact_path = row["artifact_path"]
        validator = row["validator"]
        consumer_models = set(split_list(row["consumer_models"]))
        allowed_use = row["allowed_use"].lower()
        forbidden_use = row["forbidden_use"].lower()

        if not data_family_id:
            errors.append(f"registry row {idx} has empty data_family_id")
            continue
        if data_family_id in seen:
            errors.append(f"duplicate data_family_id: {data_family_id}")
        seen.add(data_family_id)

        if scope not in VALID_SCOPES:
            errors.append(f"{data_family_id}: invalid scope {scope}")
        if owner not in VALID_OWNERS:
            errors.append(f"{data_family_id}: invalid owner_lane {owner}")
        if cleanup_status not in VALID_CLEANUP_STATUS:
            errors.append(f"{data_family_id}: invalid cleanup_status {cleanup_status}")

        if scope.startswith("shared") and "not a model-specific" not in forbidden_use and "do not" not in forbidden_use:
            errors.append(f"{data_family_id}: shared data family must explicitly forbid model-specific misuse")

        if scope in {"model_specific", "model_research_output"}:
            if consumer_models & MODEL_SPECIFIC_FORBIDDEN_CONSUMERS:
                errors.append(f"{data_family_id}: model-specific family must list specific consumer_models")
            if "do not" not in forbidden_use:
                errors.append(f"{data_family_id}: model-specific family must explicitly state forbidden_use")

        if scope == "latest_only_context" and "historical" not in forbidden_use:
            errors.append(f"{data_family_id}: latest_only_context must forbid historical point-in-time reuse")

        absent_before_capture = False
        if data_family_id == "price_pullback_23ema_operation_section":
            capture_errors, absent_before_capture = validate_price_pullback_forward_capture_registration(
                row, require_artifacts=require_artifacts
            )
            errors.extend(capture_errors)

        if scope == "missing_shared_data_family":
            if cleanup_status != "blocked_missing_source_or_validator":
                errors.append(f"{data_family_id}: missing data family must use cleanup_status=blocked_missing_source_or_validator")
            if artifact_path:
                errors.append(f"{data_family_id}: missing data family must not point to a real artifact_path")
            if validator != "not_implemented":
                errors.append(f"{data_family_id}: missing data family must use validator=not_implemented")
            if "none until" not in allowed_use:
                errors.append(f"{data_family_id}: missing data family allowed_use must block use until implementation")
            continue

        if require_artifacts and artifact_path and not artifact_exists(artifact_path) and not absent_before_capture:
            errors.append(f"{data_family_id}: artifact_path does not exist or match files: {artifact_path}")

        if validator and validator != "not_implemented" and validator.endswith(".py") and not (ROOT / validator).exists():
            errors.append(f"{data_family_id}: validator path missing: {validator}")

        if cleanup_status == "deprecated_candidate":
            if "delete" not in row["retention_policy"].lower() and "review" not in row["retention_policy"].lower():
                errors.append(f"{data_family_id}: deprecated_candidate must have explicit deletion/review retention_policy")

    missing_families = REQUIRED_FAMILIES - seen
    if missing_families:
        errors.append(f"registry missing required background data families: {sorted(missing_families)}")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the daily-model background data registry."
    )
    parser.add_argument(
        "--structure-only",
        action="store_true",
        help=(
            "Validate registry schema, ownership, contracts, migrations, producers, "
            "and validators without requiring not-yet-built artifact paths. A full "
            "validation is still required after the selected model producer runs."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    rows = load_registry(errors)
    if rows:
        errors.extend(
            validate_registry(rows, require_artifacts=not args.structure_only)
        )
    sharing_errors, _ = validate_data_sharing()
    errors.extend(sharing_errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    mode = "structure_only" if args.structure_only else "full_artifact"
    print(f"validated_daily_model_background_data_registry_rows={len(rows)}")
    print(f"validation_mode={mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
