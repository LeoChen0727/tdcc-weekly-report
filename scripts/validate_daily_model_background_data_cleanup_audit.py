from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_model_background_data_cleanup_audit import (  # noqa: E402
    DOCS_OUTPUT_CSV,
    DOCS_OUTPUT_MD,
    OUTPUT_CSV,
    OUTPUT_MD,
    REGISTRY,
    read_csv_rows,
)


REQUIRED_COLUMNS = {
    "generated_at",
    "data_family_id",
    "scope",
    "owner_lane",
    "cleanup_status",
    "retention_policy",
    "artifact_path",
    "artifact_match_count",
    "producer",
    "producer_exists",
    "validator",
    "validator_exists",
    "workflow_reference_count",
    "inventory_reference_count",
    "lineage_reference_count",
    "script_test_reference_count",
    "config_reference_count",
    "docs_reference_count",
    "deletion_decision",
    "deletion_allowed",
    "decision_reason",
    "required_next_step",
}

PROTECTED_DECISIONS = {
    "retain_historical_replay_evidence",
    "retain_shared_objective_source",
    "retain_latest_only_context",
    "retain_model_specific_semantics",
    "retain_model_research_evidence",
    "retain_registered_active_family",
    "not_applicable_missing_family",
    "blocked_deprecated_candidate_has_dependencies",
}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_docs_mirror(errors: list[str]) -> None:
    for output_path, docs_path in [(OUTPUT_CSV, DOCS_OUTPUT_CSV), (OUTPUT_MD, DOCS_OUTPUT_MD)]:
        if not output_path.exists():
            errors.append(f"missing cleanup audit artifact: {output_path.as_posix()}")
            continue
        if not docs_path.exists():
            errors.append(f"missing cleanup audit docs mirror: {docs_path.as_posix()}")
            continue
        if output_path.read_bytes() != docs_path.read_bytes():
            errors.append(f"cleanup audit docs mirror differs: {docs_path.as_posix()}")


def validate_audit(audit: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_COLUMNS - set(audit.columns)
    if missing:
        errors.append(f"cleanup audit missing columns: {sorted(missing)}")
        return errors
    if audit.empty:
        errors.append("cleanup audit is empty")
        return errors

    registry_ids = {row["data_family_id"] for row in read_csv_rows(REGISTRY)}
    audit_ids = set(audit["data_family_id"].astype(str))
    missing_ids = registry_ids - audit_ids
    extra_ids = audit_ids - registry_ids
    if missing_ids:
        errors.append(f"cleanup audit missing registry data families: {sorted(missing_ids)}")
    if extra_ids:
        errors.append(f"cleanup audit has unknown data families: {sorted(extra_ids)}")

    duplicated = audit.duplicated(["data_family_id"], keep=False)
    if duplicated.any():
        errors.append("cleanup audit must be unique by data_family_id")

    active_or_blocked = audit[~audit["cleanup_status"].eq("deprecated_candidate")]
    illegal_allowed = active_or_blocked[active_or_blocked["deletion_allowed"].str.lower().eq("true")]
    if not illegal_allowed.empty:
        errors.append("active or blocked data families must not have deletion_allowed=True")

    allowed = audit[audit["deletion_allowed"].str.lower().eq("true")]
    bad_allowed = allowed[~allowed["deletion_decision"].eq("eligible_for_cleanup_pr")]
    if not bad_allowed.empty:
        errors.append("deletion_allowed=True is permitted only for eligible_for_cleanup_pr")

    eligible = audit[audit["deletion_decision"].eq("eligible_for_cleanup_pr")]
    bad_eligible = eligible[~eligible["cleanup_status"].eq("deprecated_candidate")]
    if not bad_eligible.empty:
        errors.append("eligible_for_cleanup_pr requires cleanup_status=deprecated_candidate")

    protected = audit[audit["deletion_decision"].isin(PROTECTED_DECISIONS)]
    bad_protected = protected[protected["deletion_allowed"].str.lower().eq("true")]
    if not bad_protected.empty:
        errors.append("protected cleanup decisions must have deletion_allowed=False")

    revenue = audit[audit["data_family_id"].eq("monthly_revenue_point_in_time_panel")]
    if revenue.empty:
        errors.append("cleanup audit must include monthly_revenue_point_in_time_panel")
    elif set(revenue["deletion_decision"].astype(str)) != {"not_applicable_missing_family"}:
        errors.append("monthly_revenue_point_in_time_panel must remain not_applicable_missing_family")

    replay = audit[audit["scope"].isin(["shared_replay_evidence", "shared_replay_source"])]
    if not replay.empty and set(replay["deletion_decision"].astype(str)) != {"retain_historical_replay_evidence"}:
        errors.append("shared replay data families must retain historical replay evidence")

    return errors


def main() -> int:
    errors: list[str] = []
    validate_docs_mirror(errors)
    try:
        audit = read_csv(OUTPUT_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing cleanup audit artifact: {exc}")
        audit = pd.DataFrame()
    if not audit.empty:
        errors.extend(validate_audit(audit))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    deletion_allowed = int(audit["deletion_allowed"].astype(str).str.lower().eq("true").sum())
    print(f"validated_background_cleanup_audit_rows={len(audit)}")
    print(f"deletion_allowed_rows={deletion_allowed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
