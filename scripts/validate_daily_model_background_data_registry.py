from __future__ import annotations

import argparse
from pathlib import Path

from model_data_independence import strict_csv_rows, validate_data_sharing


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
    "price_pullback_23ema_research_outputs",
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

        if require_artifacts and artifact_path and not artifact_exists(artifact_path):
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
