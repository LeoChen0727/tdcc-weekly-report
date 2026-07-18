from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_daily_canonical_field_lineage as lineage  # noqa: E402


MIGRATION_ID = "volume_v2_warrant_canonical_field_lineage_20260718"
SCORE_RANK_MIGRATION_ID = "volume_v2_score_rank_canonical_field_lineage_20260718"
CONSUMER_HARDENING_MIGRATION_ID = "canonical_field_consumer_hardening_20260718"
CONSUMER_EXCLUSION_MIGRATION_ID = "canonical_field_consumer_exclusions_20260718"
COLLISION_MIGRATION_ID = "volume_v2_dispatcher_collision_registry_20260718"
APPROVAL = "user_requested_formal_lineage_hardening_20260718"
MODELS = ";".join(sorted(lineage.VOLUME_V2_MODELS))


def test_canonical_text_sha_is_bom_and_line_ending_independent() -> None:
    lf = b"field,value\nstock,1\n"
    crlf_with_bom = b"\xef\xbb\xbffield,value\r\nstock,1\r\n"
    cr = b"field,value\rstock,1\r"

    expected = lineage._canonical_text_sha256(lf)
    assert lineage._canonical_text_sha256(crlf_with_bom) == expected
    assert lineage._canonical_text_sha256(cr) == expected


def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def registry_rows() -> list[dict[str, str]]:
    common = {
        "field_name": "warrant_flow_signal",
        "last_migration_id": MIGRATION_ID,
        "approval_reference": APPROVAL,
        "required_validation_commands": (
            "python scripts/validate_daily_canonical_field_lineage.py;"
            "python scripts/validate_daily_warrant_formal_sync_scope.py;"
            "python -m pytest tests/test_daily_canonical_field_lineage.py"
        ),
    }
    rows = [
        {
            **common,
            "lineage_id": "warrant_flow_signal__official_current",
            "model_family": lineage.CURRENT_FAMILY,
            "artifact_path": "output/latest/warrant_flow_latest.csv",
            "artifact_role": "canonical",
            "producer": "build_warrant_flow_latest.py",
            "identity_columns": "date;stock_id",
            "as_of_columns": "date",
            "canonical_source_artifact": "output/latest/warrant_flow_latest.csv",
            "allowed_consumer_modules": (
                "merge_warrant_flow_into_candidates.py;"
                "scripts/build_daily_candidate_model_layer.py;"
                "scripts/build_volume_attack_theme_layer.py;"
                "scripts/validate_volume_attack_theme_layer.py;"
                "scripts/build_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_daily_warrant_formal_sync_scope.py;"
                "scripts/validate_daily_canonical_field_lineage.py"
            ),
            "allowed_use": "positive_projection_via_all_candidates_and_negative_absence_guard",
            "forbidden_use": "direct_positive_formal_use_outside_all_candidates",
            "collision_policy": "canonical_only",
            "parity_policy": "canonical_stock_date_unique",
            "notes": "Official current warrant signal is the only current canonical producer.",
        },
        {
            **common,
            "lineage_id": "warrant_flow_signal__all_candidates_current",
            "model_family": lineage.CURRENT_FAMILY,
            "artifact_path": "output/latest/all_candidates_latest.csv",
            "artifact_role": "canonical_projection",
            "producer": "merge_warrant_flow_into_candidates.py",
            "identity_columns": "signal_date;source_row_index;stock_id",
            "as_of_columns": "signal_date",
            "canonical_source_artifact": "output/latest/warrant_flow_latest.csv",
            "allowed_consumer_modules": (
                "scripts/build_daily_candidate_model_layer.py;"
                "scripts/build_volume_attack_theme_layer.py;"
                "scripts/validate_volume_attack_theme_layer.py;"
                "scripts/build_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_daily_warrant_formal_sync_scope.py;"
                "scripts/validate_daily_canonical_field_lineage.py"
            ),
            "allowed_use": "sole_positive_formal_projection_for_volume_v2",
            "forbidden_use": "watch_or_taxonomy_override",
            "collision_policy": "registered_projection_only",
            "parity_policy": "official_to_candidate_by_stock_and_date",
            "notes": "All volume-v2 positive warrant effects must enter through this projection.",
        },
        {
            **common,
            "lineage_id": "warrant_flow_signal__volume_watch_forbidden",
            "model_family": lineage.CURRENT_FAMILY,
            "artifact_path": "output/latest/volume_breakout_watch_latest.csv",
            "artifact_role": "forbidden_same_name",
            "producer": "scripts/build_volume_breakout_watch.py",
            "identity_columns": "signal_date;stock_id",
            "as_of_columns": "signal_date",
            "canonical_source_artifact": "output/latest/warrant_flow_latest.csv",
            "allowed_consumer_modules": "none",
            "allowed_use": "price_volume_and_model_owned_watch_fields_only",
            "forbidden_use": "warrant_flow_signal_and_warrant_derived_fields",
            "collision_policy": "column_must_be_absent",
            "parity_policy": "forbidden_same_name_no_value_parity",
            "notes": "The watch artifact must not mirror or override canonical warrant semantics.",
        },
        {
            **common,
            "lineage_id": "warrant_flow_signal__formal_raw_current",
            "model_family": lineage.CURRENT_FAMILY,
            "artifact_path": "output/latest/daily_candidate_model_signals_latest.csv",
            "artifact_role": "formal_projection",
            "producer": "scripts/build_daily_candidate_model_layer.py",
            "identity_columns": "signal_date;report_bucket;source_row_index;stock_id;model_id",
            "as_of_columns": "signal_date",
            "canonical_source_artifact": "output/latest/warrant_flow_latest.csv",
            "allowed_consumer_modules": (
                "scripts/build_daily_report_model_summary.py;"
                "scripts/validate_daily_warrant_formal_sync_scope.py;"
                "scripts/validate_daily_canonical_field_lineage.py"
            ),
            "allowed_use": "formal_volume_v2_signal_score_and_rank_projection",
            "forbidden_use": "watch_field_override_or_unregistered_consumer",
            "collision_policy": "registered_projection_only",
            "parity_policy": "candidate_to_raw_formal_by_exact_identity",
            "notes": "Only the three registered volume-v2 consumers are in scope.",
        },
        {
            **common,
            "lineage_id": "warrant_flow_signal__formal_report_current",
            "model_family": lineage.CURRENT_FAMILY,
            "artifact_path": "output/latest/daily_candidate_model_signals_for_report_latest.csv",
            "artifact_role": "formal_projection",
            "producer": "scripts/build_daily_candidate_model_layer.py",
            "identity_columns": "signal_date;report_line;source_row_index;stock_id;model_id",
            "as_of_columns": "signal_date",
            "canonical_source_artifact": "output/latest/warrant_flow_latest.csv",
            "allowed_consumer_modules": (
                "scripts/build_daily_report_model_summary.py;"
                "scripts/generate_chatgpt_side_daily_reports.py;"
                "scripts/build_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_daily_warrant_formal_sync_scope.py;"
                "scripts/validate_daily_canonical_field_lineage.py"
            ),
            "allowed_use": "formal_report_projection_for_registered_volume_v2_rows",
            "forbidden_use": "candidate_reconstruction_or_watch_fallback",
            "collision_policy": "registered_projection_only",
            "parity_policy": "raw_to_report_exact_warrant_score_rank_parity",
            "notes": "Report rows must preserve raw formal warrant semantics.",
        },
        {
            **common,
            "lineage_id": "warrant_flow_signal__volume_attack_theme_advisory",
            "model_family": lineage.CURRENT_FAMILY,
            "artifact_path": lineage.THEME_ADVISORY_ARTIFACT,
            "artifact_role": "advisory_projection",
            "producer": lineage.THEME_ADVISORY_PRODUCER,
            "identity_columns": "signal_date;stock_id",
            "as_of_columns": "warrant_flow_as_of",
            "canonical_source_artifact": "output/latest/warrant_flow_latest.csv",
            "allowed_consumer_modules": (
                "scripts/audit_daily_data_layer_consistency.py;"
                "scripts/build_chatgpt_indicator_usage_guide.py;"
                "scripts/build_non_revenue_momentum_watch.py;"
                "scripts/generate_chatgpt_side_daily_reports.py;"
                "scripts/update_daily_theme_status_history.py;"
                "scripts/validate_volume_attack_theme_layer.py;"
                "scripts/validate_daily_canonical_field_lineage.py"
            ),
            "allowed_use": "advisory_theme_context_with_pinned_canonical_lineage",
            "forbidden_use": "formal_model_gate_score_rank_or_candidate_reconstruction",
            "collision_policy": "registered_projection_only",
            "parity_policy": "candidate_to_theme_value_as_of_and_source_sha_parity",
            "notes": (
                "Theme warrant mirror is advisory and pins all_candidates plus official "
                "source lineage."
            ),
        },
        {
            **common,
            "lineage_id": "warrant_flow_signal__official_history",
            "model_family": lineage.HISTORY_FAMILY,
            "artifact_path": "output/history/warrant_flow/warrant_flow_*.csv",
            "artifact_role": "canonical",
            "producer": "build_warrant_flow_latest.py",
            "identity_columns": "date;stock_id",
            "as_of_columns": "date",
            "canonical_source_artifact": "output/history/warrant_flow/warrant_flow_*.csv",
            "allowed_consumer_modules": (
                "scripts/build_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_daily_warrant_formal_sync_scope.py;"
                "scripts/validate_daily_canonical_field_lineage.py"
            ),
            "allowed_use": "paired_historical_lineage_audit_only",
            "forbidden_use": "rewrite_or_reclassify_historical_rows",
            "collision_policy": "canonical_only",
            "parity_policy": "historical_canonical_stock_date_unique",
            "notes": "Historical source rows are immutable audit evidence.",
        },
        {
            **common,
            "lineage_id": "warrant_flow_signal__all_candidates_history",
            "model_family": lineage.HISTORY_FAMILY,
            "artifact_path": "output/history/daily_model_snapshots/all_candidates_*.csv",
            "artifact_role": "historical_projection",
            "producer": "scripts/update_daily_published_model_snapshots.py",
            "identity_columns": "signal_date;source_row_index;stock_id",
            "as_of_columns": "signal_date",
            "canonical_source_artifact": "output/history/warrant_flow/warrant_flow_*.csv",
            "allowed_consumer_modules": (
                "scripts/build_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_daily_warrant_formal_sync_scope.py;"
                "scripts/validate_daily_canonical_field_lineage.py"
            ),
            "allowed_use": "paired_historical_lineage_audit_only",
            "forbidden_use": "rewrite_historical_source_projection",
            "collision_policy": "registered_projection_only",
            "parity_policy": "historical_official_to_candidate_by_date_and_stock",
            "notes": "Historical candidate snapshots remain unchanged and are audited in place.",
        },
        {
            **common,
            "lineage_id": "warrant_flow_signal__formal_report_history",
            "model_family": lineage.HISTORY_FAMILY,
            "artifact_path": (
                "output/history/daily_model_snapshots/"
                "daily_candidate_model_signals_for_report_*.csv"
            ),
            "artifact_role": "historical_projection",
            "producer": "scripts/update_daily_published_model_snapshots.py",
            "identity_columns": "signal_date;report_line;source_row_index;stock_id;model_id",
            "as_of_columns": "signal_date",
            "canonical_source_artifact": "output/history/warrant_flow/warrant_flow_*.csv",
            "allowed_consumer_modules": (
                "scripts/build_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_volume_v2_warrant_lineage_history_audit.py;"
                "scripts/validate_daily_warrant_formal_sync_scope.py;"
                "scripts/validate_daily_canonical_field_lineage.py"
            ),
            "allowed_use": "paired_volume_v2_warrant_score_rank_audit_only",
            "forbidden_use": "rewrite_or_promote_from_superseded_history",
            "collision_policy": "registered_projection_only",
            "parity_policy": "historical_candidate_to_formal_warrant_score_rank_parity",
            "notes": "Legacy mismatches must be marked by audit rather than rewritten.",
        },
    ]
    for row in rows:
        row["contract_sha256"] = lineage.contract_sha256(row)
    with (ROOT / lineage.REGISTRY_PATH).open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        contract_rows = [dict(row) for row in csv.DictReader(handle)]
    assert len(contract_rows) == len(lineage.GOVERNED_FIELD_NODES)
    return contract_rows


def collision_registry_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for field_name in ("signal_date", "stock_id"):
        row = {
            "collision_id": f"volume_v2_dispatcher__{field_name}",
            "field_name": field_name,
            "model_family": lineage.COLLISION_MODEL_FAMILY,
            "canonical_artifact": lineage.ALL_CANDIDATES_ARTIFACT,
            "canonical_producer": lineage.ALL_CANDIDATES_PRODUCER,
            "allowed_mirror_artifact": lineage.VOLUME_WATCH_ARTIFACT,
            "allowed_mirror_producer": lineage.VOLUME_WATCH_PRODUCER,
            "dispatcher_consumer": lineage.VOLUME_DISPATCHER_CONSUMER,
            "collision_policy": lineage.COLLISION_CANONICAL_CANDIDATE_POLICY,
            "source_precedence": "candidate_preserved_watch_ignored",
            "value_parity_policy": "no_value_parity_watch_mirror_is_advisory",
            "last_migration_id": COLLISION_MIGRATION_ID,
            "approval_reference": APPROVAL,
            "required_validation_commands": (
                "python scripts/validate_daily_canonical_field_lineage.py;"
                "python -m pytest tests/test_daily_canonical_field_lineage.py"
            ),
            "notes": "Fixture collision remains canonical from all_candidates.",
        }
        row["contract_sha256"] = lineage.collision_contract_sha256(row)
        rows.append(row)
    return rows


def valid_model_source() -> str:
    return '''
VOLUME_V2_WATCH_OVERLAY_FIELDS = ("volume_ratio", "tdcc_status")
VOLUME_V2_WATCH_NON_AUTHORITATIVE_COLLISION_FIELDS = frozenset(
    {"signal_date", "stock_id", "warrant_flow_signal"}
)
VOLUME_V2_FORMAL_DISPATCH_FORBIDDEN_FIELDS = frozenset(
    {
        "score",
        "rank",
        "advisory_volume_breakout_score",
        "advisory_volume_breakout_rank",
        "volume_breakout_score",
        "volume_breakout_rank",
    }
)
VOLUME_V2_CANDIDATE_SCORE_FIELDS = ("tdcc_status", "volume_ratio")

def append_volume_breakout_signals(signals, candidates, signal_date):
    row = {"stock_id": "1617", "volume_ratio": "2"}
    v2_features = {"position_bucket_120d": "low_pos_le40"}
    authoritative_warrant_signal = "call_inflow"
    candidate_values = {"stock_id": "1617", "score": "12", "rank": "1"}
    score_source = {
        field: candidate_values[field]
        for field in VOLUME_V2_CANDIDATE_SCORE_FIELDS
        if field in candidate_values
    }
    watch_values = row.copy()
    overlapping_fields = set(score_source).intersection(watch_values)
    registered_collisions = set(VOLUME_V2_WATCH_OVERLAY_FIELDS).union(
        VOLUME_V2_WATCH_NON_AUTHORITATIVE_COLLISION_FIELDS
    )
    unregistered_collisions = sorted(overlapping_fields - registered_collisions)
    if unregistered_collisions:
        raise RuntimeError("unregistered same-name field collision")
    score_source.update(
        {
            field: row.get(field, "") for field in VOLUME_V2_WATCH_OVERLAY_FIELDS
        }
    )
    forbidden_dispatch_fields = set(score_source).intersection(
        VOLUME_V2_FORMAL_DISPATCH_FORBIDDEN_FIELDS
    )
    if forbidden_dispatch_fields:
        raise RuntimeError("formal-dispatch forbidden score/rank field")
    score_source["warrant_flow_signal"] = authoritative_warrant_signal
    score_source.update(v2_features)
    output = {"warrant_flow_signal": authoritative_warrant_signal}
    return output
'''


def build_valid_repo(root: Path) -> None:
    rows = registry_rows()
    write_csv(root / lineage.REGISTRY_PATH, list(lineage.REGISTRY_COLUMNS), rows)
    migration = {
        "migration_id": MIGRATION_ID,
        "changed_lineage_ids": ";".join(row["lineage_id"] for row in rows),
        "previous_contract_sha256s": ";".join("NEW" for _ in rows),
        "new_contract_sha256s": ";".join(row["contract_sha256"] for row in rows),
        "affected_models": MODELS,
        "affected_consumers": (
            "build_warrant_flow_latest.py;merge_warrant_flow_into_candidates.py;"
            "scripts/build_daily_candidate_model_layer.py;"
            "scripts/build_volume_attack_theme_layer.py;"
            "scripts/build_volume_v2_warrant_lineage_history_audit.py;"
            "scripts/build_daily_report_model_summary.py;"
            "scripts/generate_chatgpt_side_daily_reports.py;"
            "scripts/validate_volume_attack_theme_layer.py;"
            "scripts/validate_volume_v2_warrant_lineage_history_audit.py;"
            "scripts/validate_daily_warrant_formal_sync_scope.py;"
            "scripts/validate_daily_canonical_field_lineage.py"
        ),
        "validation_commands": (
            "python scripts/validate_daily_canonical_field_lineage.py;"
            "python -m pytest tests/test_daily_canonical_field_lineage.py"
        ),
        "user_approval_reference": APPROVAL,
        "migration_status": lineage.VALID_MIGRATION_STATUS,
        "notes": "Initial user-approved volume-v2 warrant canonical field lineage contract.",
    }
    with (ROOT / lineage.MIGRATIONS_PATH).open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        contract_migrations = [dict(row) for row in csv.DictReader(handle)]
    assert [row["migration_id"] for row in contract_migrations] == [
        MIGRATION_ID,
        SCORE_RANK_MIGRATION_ID,
        CONSUMER_HARDENING_MIGRATION_ID,
    ]
    write_csv(
        root / lineage.MIGRATIONS_PATH,
        list(lineage.MIGRATION_COLUMNS),
        contract_migrations,
    )

    with (ROOT / lineage.CONSUMER_EXCLUSIONS_PATH).open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        consumer_exclusions = [dict(row) for row in csv.DictReader(handle)]
    write_csv(
        root / lineage.CONSUMER_EXCLUSIONS_PATH,
        list(lineage.CONSUMER_EXCLUSION_COLUMNS),
        consumer_exclusions,
    )
    with (ROOT / lineage.CONSUMER_EXCLUSION_MIGRATIONS_PATH).open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        consumer_exclusion_migrations = [
            dict(row) for row in csv.DictReader(handle)
        ]
    assert {row["migration_id"] for row in consumer_exclusion_migrations} == {
        CONSUMER_EXCLUSION_MIGRATION_ID,
        "canonical_field_consumer_theme_exclusions_20260718",
    }
    write_csv(
        root / lineage.CONSUMER_EXCLUSION_MIGRATIONS_PATH,
        list(lineage.CONSUMER_EXCLUSION_MIGRATION_COLUMNS),
        consumer_exclusion_migrations,
    )

    collision_rows = collision_registry_rows()
    write_csv(
        root / lineage.COLLISION_REGISTRY_PATH,
        list(lineage.COLLISION_REGISTRY_COLUMNS),
        collision_rows,
    )
    collision_migration = {
        "migration_id": COLLISION_MIGRATION_ID,
        "changed_collision_ids": ";".join(
            row["collision_id"] for row in collision_rows
        ),
        "previous_contract_sha256s": ";".join("NEW" for _ in collision_rows),
        "new_contract_sha256s": ";".join(
            row["contract_sha256"] for row in collision_rows
        ),
        "affected_models": MODELS,
        "affected_consumer": lineage.VOLUME_DISPATCHER_CONSUMER,
        "validation_commands": (
            "python scripts/validate_daily_canonical_field_lineage.py;"
            "python -m pytest tests/test_daily_canonical_field_lineage.py"
        ),
        "user_approval_reference": APPROVAL,
        "migration_status": lineage.COLLISION_MIGRATION_STATUS,
        "notes": "Initial fixture dispatcher collision registry.",
    }
    write_csv(
        root / lineage.COLLISION_MIGRATIONS_PATH,
        list(lineage.COLLISION_MIGRATION_COLUMNS),
        [collision_migration],
    )

    required_files = {
        "build_all_candidates_latest.py": "",
        "build_warrant_flow_latest.py": "",
        "merge_warrant_flow_into_candidates.py": "",
        "scripts/build_daily_candidate_model_layer.py": valid_model_source(),
        "scripts/build_volume_attack_theme_layer.py": "",
        "scripts/build_volume_v2_warrant_lineage_history_audit.py": "",
        "scripts/build_volume_breakout_watch.py": "",
        "scripts/build_daily_report_model_summary.py": "",
        "scripts/audit_daily_data_layer_consistency.py": "",
        "scripts/build_chatgpt_indicator_usage_guide.py": "",
        "scripts/build_non_revenue_momentum_watch.py": "",
        "scripts/generate_chatgpt_side_daily_reports.py": "",
        "scripts/update_daily_published_model_snapshots.py": "",
        "scripts/update_daily_theme_status_history.py": "",
        "scripts/validate_daily_warrant_formal_sync_scope.py": "",
        "scripts/validate_daily_canonical_field_lineage.py": "",
        "scripts/validate_volume_attack_theme_layer.py": "",
        "scripts/validate_volume_v2_warrant_lineage_history_audit.py": "",
    }
    for row in rows:
        required_files.setdefault(row["producer"], "")
        for consumer in row["allowed_consumer_modules"].split(";"):
            if consumer and consumer != "none":
                required_files.setdefault(consumer, "")
    for index, exclusion in enumerate(consumer_exclusions, start=1):
        module = exclusion["module"]
        required_files.setdefault(module, "")
        required_files[module] += (
            f'\n_EXCLUDED_FIELD_{index} = {exclusion["field_name"]!r}\n'
            f'_EXCLUDED_ARTIFACT_{index} = {exclusion["artifact_path"]!r}\n'
        )
    for relative, content in required_files.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    official = [{"date": "20260717", "stock_id": "1617", "warrant_flow_signal": "call_inflow"}]
    candidate = [
        {
            "signal_date": "20260717",
            "source_row_index": "1",
            "stock_id": "1617",
            "score": "71",
            "rank": "1",
            "warrant_flow_signal": "call_inflow",
        }
    ]
    formal = [
        {
            "signal_date": "20260717",
            "report_bucket": "mainstream",
            "report_line": "mainstream",
            "source_row_index": "1",
            "stock_id": "1617",
            "model_id": "volume_range_breakout_v2_low_position_volume_attack",
            "final_rank_score": "82",
            "model_score": "82",
            "model_rank": "1",
            "warrant_flow_signal": "call_inflow",
            "score_components": "base=80 | warrant bullish +2",
        }
    ]
    watch = [
        {
            "signal_date": "20260717",
            "stock_id": "1617",
            "volume_breakout_priority": "A_bottom_volume_attack",
            "advisory_volume_breakout_score": "71",
            "advisory_volume_breakout_rank": "1",
            "advisory_score_as_of": "20260717",
            "volume_ratio": "2.5",
        }
    ]
    write_csv(root / "output/latest/warrant_flow_latest.csv", list(official[0]), official)
    write_csv(root / "output/latest/all_candidates_latest.csv", list(candidate[0]), candidate)
    write_csv(
        root / "output/latest/volume_breakout_watch_latest.csv", list(watch[0]), watch
    )
    candidate_sha = lineage._canonical_text_sha256(
        (root / "output/latest/all_candidates_latest.csv").read_bytes()
    )
    official_sha = lineage._canonical_text_sha256(
        (root / "output/latest/warrant_flow_latest.csv").read_bytes()
    )
    watch_sha = lineage._canonical_text_sha256(
        (root / "output/latest/volume_breakout_watch_latest.csv").read_bytes()
    )
    theme = [
        {
            "signal_date": "20260717",
            "stock_id": "1617",
            "volume_breakout_score": "71",
            "volume_breakout_rank": "1",
            "volume_watch_as_of": "20260717",
            "volume_watch_source_artifact": lineage.VOLUME_WATCH_ARTIFACT,
            "volume_watch_source_sha256": watch_sha,
            "warrant_flow_signal": "call_inflow",
            "warrant_flow_as_of": "20260717",
            "warrant_flow_source_artifact": "output/latest/all_candidates_latest.csv",
            "warrant_flow_source_sha256": candidate_sha,
            "warrant_flow_official_source_artifact": "output/latest/warrant_flow_latest.csv",
            "warrant_flow_official_source_sha256": official_sha,
        }
    ]
    write_csv(
        root / lineage.THEME_ADVISORY_ARTIFACT,
        list(theme[0]),
        theme,
    )
    write_csv(
        root / "output/latest/daily_candidate_model_signals_latest.csv",
        list(formal[0]),
        formal,
    )
    write_csv(
        root / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        list(formal[0]),
        formal,
    )
    operation = [
        {
            "operation_date": "20260717",
            "operation_asof_date": "20260717",
            "pdf_view": "highlight",
            "report_line": "mainstream",
            "stock_id": "1617",
            "model_id": "volume_range_breakout_v2_low_position_volume_attack",
            "operation_section": "confirmed_operation",
            "pdf_section": "confirmed_operation",
            "row_type": "data",
            "final_rank_score": "82",
            "research_score": "82",
        }
    ]
    write_csv(
        root / "output/latest/daily_volume_breakout_operation_section_latest.csv",
        list(operation[0]),
        operation,
    )
    write_csv(
        root
        / "output/history/daily_model_snapshots/"
        "daily_volume_breakout_operation_section_20260717.csv",
        list(operation[0]),
        operation,
    )
    write_csv(
        root / "output/history/warrant_flow/warrant_flow_20260717.csv",
        list(official[0]),
        official,
    )
    write_csv(
        root / "output/history/daily_model_snapshots/all_candidates_20260717.csv",
        list(candidate[0]),
        candidate,
    )
    write_csv(
        root
        / "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260717.csv",
        list(formal[0]),
        formal,
    )


def test_valid_canonical_field_lineage_contract_passes(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    assert lineage.validate(tmp_path) == []


def test_unregistered_direct_advisory_field_consumer_fails_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    consumer = tmp_path / "scripts/unregistered_theme_score_consumer.py"
    consumer.write_text(
        'ARTIFACT = "output/latest/volume_attack_theme_stocks_latest.csv"\n'
        'FIELD = "volume_breakout_score"\n',
        encoding="utf-8",
    )

    errors = lineage.validate(tmp_path)

    assert any(
        "unregistered current canonical field consumer collision" in error
        and "module=scripts/unregistered_theme_score_consumer.py" in error
        and "field=volume_breakout_score" in error
        for error in errors
    )


def test_unregistered_direct_formal_field_consumer_fails_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    consumer = tmp_path / "build_unregistered_formal_packet.py"
    consumer.write_text(
        'ARTIFACT = "output/latest/daily_candidate_model_signals_for_report_latest.csv"\n'
        'FIELD = "model_score"\n',
        encoding="utf-8",
    )

    errors = lineage.validate(tmp_path)

    assert any(
        "unregistered current canonical field consumer collision" in error
        and "module=build_unregistered_formal_packet.py" in error
        and "field=model_score" in error
        for error in errors
    )


def test_unregistered_generic_candidate_score_consumer_fails_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    consumer = tmp_path / "scripts/unregistered_candidate_score_consumer.py"
    consumer.write_text(
        'ARTIFACT = "output/latest/all_candidates_latest.csv"\n'
        'FIELD = "score"\n',
        encoding="utf-8",
    )

    errors = lineage.validate(tmp_path)

    assert any(
        "unregistered current canonical field consumer collision" in error
        and "lineage_id=score__all_candidates_current" in error
        and "module=scripts/unregistered_candidate_score_consumer.py" in error
        for error in errors
    )


def test_stale_consumer_exclusion_fails_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    module = tmp_path / "generate_candidate_charts.py"
    module.write_text(
        module.read_text(encoding="utf-8").replace("'score'", "'not_score'"),
        encoding="utf-8",
    )

    errors = lineage.validate(tmp_path)

    assert any(
        "stale canonical consumer exclusion" in error
        and "candidate_score_chart_local_field" not in error
        and "lineage_id=score__all_candidates_current" in error
        and "module=generate_candidate_charts.py" in error
        for error in errors
    )


def test_watch_advisory_registry_requires_explicit_as_of_column(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.REGISTRY_PATH
    columns, rows = lineage._read_artifact(path)
    row = next(
        item
        for item in rows
        if item["lineage_id"]
        == "advisory_volume_breakout_score__volume_watch_current"
    )
    row["as_of_columns"] = "signal_date"
    write_csv(path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "watch advisory lineage must register advisory_score_as_of" in error
        for error in errors
    )


def test_non_revenue_watch_does_not_consume_theme_advisory_score() -> None:
    source = (ROOT / "scripts/build_non_revenue_momentum_watch.py").read_text(
        encoding="utf-8-sig"
    )
    assert "volume_breakout_score" not in source


def test_watch_same_name_field_collision_fails_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    write_csv(
        tmp_path / "output/latest/volume_breakout_watch_latest.csv",
        ["signal_date", "stock_id", "warrant_flow_signal"],
        [
            {
                "signal_date": "20260717",
                "stock_id": "1617",
                "warrant_flow_signal": "no_signal",
            }
        ],
    )
    errors = lineage.validate(tmp_path)
    assert any("forbidden same-name field collision" in error for error in errors)


def test_overlay_tuple_rejects_warrant_and_warrant_count_fields(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    source = valid_model_source().replace(
        '("volume_ratio", "tdcc_status")',
        '("stock_id", "warrant_flow_signal", "call_warrant_count")',
    )
    (tmp_path / lineage.MODEL_SOURCE_PATH).write_text(source, encoding="utf-8")
    errors = lineage.validate(tmp_path)
    assert any(
        "contains forbidden warrant fields: call_warrant_count,warrant_flow_signal" in error
        for error in errors
    )


def test_generic_row_dict_update_is_rejected(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    source = valid_model_source().replace(
        "    forbidden_dispatch_fields = set(score_source).intersection(",
        "    score_source.update(row.to_dict())\n"
        "    forbidden_dispatch_fields = set(score_source).intersection(",
    )
    (tmp_path / lineage.MODEL_SOURCE_PATH).write_text(source, encoding="utf-8")
    errors = lineage.validate(tmp_path)
    assert any("unregistered score_source.update source" in error for error in errors)


@pytest.mark.parametrize(
    "injected_write,expected_error",
    [
        (
            "    score_source.update(watch_values)\n",
            "unregistered score_source.update source",
        ),
        (
            "    score_source.update(candidate_values)\n",
            "unregistered score_source.update source",
        ),
        (
            "    score_source |= watch_values\n",
            "must not use augmented score_source mutation",
        ),
        (
            '    score_source["future_semantic"] = watch_values["future_semantic"]\n',
            "unregistered score_source subscript write",
        ),
        (
            "    score_source_alias = score_source\n"
            "    score_source_alias.update(watch_values)\n",
            "unregistered load context",
        ),
    ],
)
def test_dispatcher_rejects_score_source_write_bypasses(
    tmp_path: Path, injected_write: str, expected_error: str
) -> None:
    build_valid_repo(tmp_path)
    source = valid_model_source().replace(
        "    forbidden_dispatch_fields = set(score_source).intersection(",
        injected_write
        + "    forbidden_dispatch_fields = set(score_source).intersection(",
    )
    (tmp_path / lineage.MODEL_SOURCE_PATH).write_text(source, encoding="utf-8")

    errors = lineage.validate(tmp_path)

    assert any(expected_error in error for error in errors)


def test_formal_projection_mismatch_fails_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    report_path = (
        tmp_path / "output/latest/daily_candidate_model_signals_for_report_latest.csv"
    )
    columns, rows = lineage._read_artifact(report_path)
    rows[0]["warrant_flow_signal"] = "no_signal"
    rows[0]["score_components"] = "base=80"
    write_csv(report_path, columns, rows)
    errors = lineage.validate(tmp_path)
    assert any("formal volume warrant projection mismatch current_report" in error for error in errors)
    assert any("current raw/report volume v2 parity mismatch" in error for error in errors)


def test_theme_advisory_warrant_projection_and_source_sha_fail_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    columns, rows = lineage._read_artifact(theme_path)
    rows[0]["warrant_flow_signal"] = "no_signal"
    rows[0]["warrant_flow_source_sha256"] = "0" * 64
    write_csv(theme_path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "theme advisory warrant projection differs from all_candidates" in error
        for error in errors
    )
    assert any(
        "theme advisory warrant lineage metadata mismatch" in error
        and "warrant_flow_source_sha256" in error
        for error in errors
    )


def test_dispatcher_rejects_formal_score_rank_field_in_watch_overlay(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    source = valid_model_source().replace(
        '("volume_ratio", "tdcc_status")',
        '("volume_ratio", "tdcc_status", "volume_breakout_score")',
    )
    (tmp_path / lineage.MODEL_SOURCE_PATH).write_text(source, encoding="utf-8")

    errors = lineage.validate(tmp_path)

    assert any(
        "contains formal-dispatch forbidden score/rank fields: "
        "volume_breakout_score" in error
        for error in errors
    )


def test_dispatcher_requires_formal_score_rank_filter_guard(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    source = valid_model_source().replace(
        "VOLUME_V2_FORMAL_DISPATCH_FORBIDDEN_FIELDS\n    )",
        "frozenset()\n    )",
    )
    (tmp_path / lineage.MODEL_SOURCE_PATH).write_text(source, encoding="utf-8")

    errors = lineage.validate(tmp_path)

    assert any(
        "must enforce VOLUME_V2_FORMAL_DISPATCH_FORBIDDEN_FIELDS" in error
        for error in errors
    )


def test_dispatcher_requires_candidate_score_allowlist(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    source = valid_model_source().replace(
        "for field in VOLUME_V2_CANDIDATE_SCORE_FIELDS",
        "for field in candidate_values",
    )
    (tmp_path / lineage.MODEL_SOURCE_PATH).write_text(source, encoding="utf-8")

    errors = lineage.validate(tmp_path)

    assert any(
        f"dict comprehension over {lineage.CANDIDATE_SCORE_GLOBAL}" in error
        for error in errors
    )


def test_theme_watch_score_rank_and_source_sha_fail_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    columns, rows = lineage._read_artifact(theme_path)
    rows[0]["volume_breakout_score"] = "70"
    rows[0]["volume_breakout_rank"] = "2"
    rows[0]["volume_watch_source_sha256"] = "0" * 64
    write_csv(theme_path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "theme advisory watch score/rank parity mismatch" in error
        and "source_column=advisory_volume_breakout_score" in error
        and "projection_column=volume_breakout_score" in error
        for error in errors
    )
    assert any(
        "theme advisory watch score/rank parity mismatch" in error
        and "source_column=advisory_volume_breakout_rank" in error
        and "projection_column=volume_breakout_rank" in error
        for error in errors
    )
    assert any(
        "theme advisory warrant lineage metadata mismatch" in error
        and "column=volume_watch_source_sha256" in error
        for error in errors
    )


def test_positive_candidate_signal_without_official_row_fails_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    columns, _ = lineage._read_artifact(official_path)
    write_csv(official_path, columns, [])

    errors = lineage.validate(tmp_path)

    assert any(
        "positive all_candidates warrant projection lacks official canonical row"
        in error
        and "stock_id=1617" in error
        for error in errors
    )


def test_formal_model_score_must_equal_final_rank_score(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    for relative in (
        "output/latest/daily_candidate_model_signals_latest.csv",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    ):
        path = tmp_path / relative
        columns, rows = lineage._read_artifact(path)
        rows[0]["model_score"] = "81"
        write_csv(path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "volume v2 formal score direct-mirror mismatch current_raw" in error
        for error in errors
    )
    assert any(
        "volume v2 formal score direct-mirror mismatch current_report" in error
        for error in errors
    )


@pytest.mark.parametrize("bad_rank", ["", "2"])
def test_formal_model_rank_must_be_present_and_exact(
    tmp_path: Path, bad_rank: str
) -> None:
    build_valid_repo(tmp_path)
    for relative in (
        "output/latest/daily_candidate_model_signals_latest.csv",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    ):
        path = tmp_path / relative
        columns, rows = lineage._read_artifact(path)
        rows[0]["model_rank"] = bad_rank
        write_csv(path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "volume v2 rank parity mismatch current_raw" in error for error in errors
    )
    assert any(
        "volume v2 rank parity mismatch current_report" in error for error in errors
    )


def test_registry_missing_score_rank_field_artifact_node_fails_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.REGISTRY_PATH
    columns, rows = lineage._read_artifact(path)
    rows = [
        row
        for row in rows
        if row["lineage_id"] != "final_rank_score__operation_current"
    ]
    write_csv(path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "canonical field registry governed volume-v2 node set mismatch" in error
        and "final_rank_score" in error
        and "daily_volume_breakout_operation_section_latest.csv" in error
        for error in errors
    )


def test_registry_missing_operation_history_final_rank_node_fails_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.REGISTRY_PATH
    columns, rows = lineage._read_artifact(path)
    rows = [
        row
        for row in rows
        if row["lineage_id"] != "final_rank_score__operation_history"
    ]
    write_csv(path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "canonical field registry governed volume-v2 node set mismatch" in error
        and "final_rank_score" in error
        and "daily_volume_breakout_operation_section_*.csv" in error
        for error in errors
    )


def test_historical_volume_v2_date_requires_official_and_candidate_pair(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    (
        tmp_path / "output/history/warrant_flow/warrant_flow_20260717.csv"
    ).unlink()

    errors = lineage.validate(tmp_path)

    assert any(
        "historical volume v2 dates missing official warrant snapshots: 20260717"
        in error
        for error in errors
    )
    assert any(
        "historical volume v2 parity validated zero complete snapshot pairs" in error
        for error in errors
    )


def test_historical_volume_v2_zero_pair_fails_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    (
        tmp_path
        / "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260717.csv"
    ).unlink()

    errors = lineage.validate(tmp_path)

    assert "historical parity has no formal report snapshots" in errors


def test_sparse_historical_artifacts_are_read_from_head(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "lineage-test@example.invalid"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Lineage Test"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "commit", "-m", "fixture"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    for relative in (
        "output/history/warrant_flow/warrant_flow_20260717.csv",
        "output/history/daily_model_snapshots/all_candidates_20260717.csv",
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260717.csv",
    ):
        (tmp_path / relative).unlink()

    assert lineage.validate(tmp_path) == []


def test_migration_tip_must_pin_current_contract(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.MIGRATIONS_PATH
    columns, rows = lineage._read_artifact(path)
    hashes = rows[-1]["new_contract_sha256s"].split(";")
    hashes[2] = "0" * 64
    rows[-1]["new_contract_sha256s"] = ";".join(hashes)
    write_csv(path, columns, rows)
    errors = lineage.validate(tmp_path)
    assert any("migration tip does not pin current field contract" in error for error in errors)


def test_consumer_exclusion_contract_hash_is_fail_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.CONSUMER_EXCLUSIONS_PATH
    columns, rows = lineage._read_artifact(path)
    rows[0]["notes"] = "changed without migration"
    write_csv(path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "canonical consumer exclusion contract SHA mismatch" in error
        for error in errors
    )


def test_consumer_exclusion_migration_tip_must_pin_contract(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.CONSUMER_EXCLUSION_MIGRATIONS_PATH
    columns, rows = lineage._read_artifact(path)
    hashes = rows[0]["new_contract_sha256s"].split(";")
    hashes[0] = "0" * 64
    rows[0]["new_contract_sha256s"] = ";".join(hashes)
    write_csv(path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "canonical consumer exclusion migration tip does not pin contract" in error
        for error in errors
    )


def test_unregistered_actual_dispatcher_collision_fails_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    for relative in (
        lineage.ALL_CANDIDATES_ARTIFACT,
        lineage.VOLUME_WATCH_ARTIFACT,
    ):
        path = tmp_path / relative
        columns, rows = lineage._read_artifact(path)
        columns.append("new_shared_field")
        for row in rows:
            row["new_shared_field"] = "collision"
        write_csv(path, columns, rows)
    errors = lineage.validate(tmp_path)
    assert any(
        "unregistered volume-v2 dispatcher same-name collision: new_shared_field"
        in error
        for error in errors
    )


def test_registry_policy_must_match_dispatcher_ast_global(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.COLLISION_REGISTRY_PATH
    columns, rows = lineage._read_artifact(path)
    rows[0]["collision_policy"] = lineage.COLLISION_WATCH_OVERLAY_POLICY
    write_csv(path, columns, rows)
    errors = lineage.validate(tmp_path)
    assert any(
        f"watch-overlay collision is absent from {lineage.OVERLAY_GLOBAL}: signal_date"
        in error
        for error in errors
    )


def test_registered_collision_must_remain_in_ast_global(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    source = valid_model_source().replace('    {"signal_date", ', "    {")
    (tmp_path / lineage.MODEL_SOURCE_PATH).write_text(source, encoding="utf-8")
    errors = lineage.validate(tmp_path)
    assert any(
        "candidate-preserved collision is absent from "
        f"{lineage.NON_AUTHORITATIVE_GLOBAL}: signal_date" in error
        for error in errors
    )


def test_dispatcher_collision_migration_tip_must_pin_contract(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.COLLISION_MIGRATIONS_PATH
    columns, rows = lineage._read_artifact(path)
    hashes = rows[0]["new_contract_sha256s"].split(";")
    hashes[0] = "0" * 64
    rows[0]["new_contract_sha256s"] = ";".join(hashes)
    write_csv(path, columns, rows)
    errors = lineage.validate(tmp_path)
    assert any(
        "dispatcher collision migration tip does not pin current contract" in error
        for error in errors
    )


def test_workflows_run_canonical_lineage_after_model_build() -> None:
    model_build = "python scripts/build_daily_candidate_model_layer.py"
    canonical_validation = (
        "python scripts/validate_daily_canonical_field_lineage.py"
    )
    snapshot_update = "python scripts/update_daily_published_model_snapshots.py"
    snapshot_validation = "python scripts/validate_daily_published_model_snapshots.py"
    workflows = {
        "daily_full": ROOT / ".github/workflows/daily_full_pipeline.yml",
        "warrant_flow": ROOT / ".github/workflows/warrant_flow.yml",
    }
    contents: dict[str, str] = {}
    for name, path in workflows.items():
        text = path.read_text(encoding="utf-8")
        contents[name] = text
        assert text.count(model_build) == 1
        assert text.count(canonical_validation) == 2
        canonical_positions = [
            index
            for index in range(len(text))
            if text.startswith(canonical_validation, index)
        ]
        assert text.index(model_build) < canonical_positions[0]
        snapshot_update_position = text.index(snapshot_update)
        post_update_snapshot_validation = text.index(
            snapshot_validation,
            snapshot_update_position,
        )
        assert snapshot_update_position < post_update_snapshot_validation
        assert post_update_snapshot_validation < canonical_positions[1]

    theme_build = "python scripts/build_volume_attack_theme_layer.py"
    warrant_workflow = contents["warrant_flow"]
    assert warrant_workflow.count(theme_build) == 1
    assert warrant_workflow.index(theme_build) < warrant_workflow.index(model_build)
