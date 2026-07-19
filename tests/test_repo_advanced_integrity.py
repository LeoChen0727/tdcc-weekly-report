from __future__ import annotations

import csv
from pathlib import Path

from scripts import trace_runtime_file_lineage
from scripts import validate_repo_advanced_integrity as validator
from scripts.daily_snapshot_revision_utils import snapshot_file_sha256


ROOT = Path(__file__).resolve().parents[1]


def test_repo_advanced_integrity_validator_passes() -> None:
    assert validator.main() == 0


def test_advanced_integrity_gate_is_hooked_into_daily_pipeline() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    boundary = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_repo_advanced_integrity.py" in workflow
    assert "validate_repo_advanced_integrity.py" in boundary
    assert "validate(include_external_sources=False)" in boundary


def test_daily_pipeline_validates_external_sources_after_catalyst_refresh() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    refresh_idx = workflow.index("- name: Update catalyst data tables")
    freshness_idx = workflow.index(
        "- name: Refresh data freshness before external-source integrity gate"
    )
    freshness_build_idx = workflow.index("python build_data_freshness_latest.py", freshness_idx)
    freshness_validate_idx = workflow.index(
        "python scripts/validate_data_freshness_latest.py", freshness_idx
    )
    advanced_idx = workflow.index("python scripts/validate_repo_advanced_integrity.py")
    preflight_idx = workflow.index("- name: Validate Apps Script workflow triggers")
    install_idx = workflow.index("- name: Install dependencies")

    assert (
        preflight_idx
        < install_idx
        < refresh_idx
        < freshness_build_idx
        < freshness_validate_idx
        < advanced_idx
    )


def test_warrant_external_source_allows_legacy_ready_freshness(tmp_path: Path, monkeypatch) -> None:
    output_latest = tmp_path / "output" / "latest"
    output_latest.mkdir(parents=True)
    freshness = output_latest / "data_freshness_latest.csv"
    freshness.write_text(
        "main_price_date,warrant_flow_date,warrant_ready\n"
        "20260623,20260623,True\n",
        encoding="utf-8",
    )
    contract = tmp_path / "external_data_source_contract.csv"
    contract.write_text(
        "source_id,owner,status_artifact,freshness_date_column,readiness_column,require_matches_main_price_date,json_status_path,allowed_statuses,producer,validator\n"
        "warrant_flow,warrant,output/latest/data_freshness_latest.csv,warrant_flow_date,warrant_daily_publish_allowed,True,,,,\n",
        encoding="utf-8",
    )
    inventory = tmp_path / "repo_production_inventory.csv"
    inventory.write_text("path\n", encoding="utf-8")

    monkeypatch.setattr(validator, "ROOT", tmp_path)
    monkeypatch.setattr(validator, "EXTERNAL_SOURCE_CONTRACT", contract)
    monkeypatch.setattr(validator, "FRESHNESS_CSV", freshness)
    monkeypatch.setattr(validator, "INVENTORY_CSV", inventory)

    assert validator.validate_external_source_contract() == []


def test_warrant_external_source_rejects_present_false_publish_allowed(tmp_path: Path, monkeypatch) -> None:
    output_latest = tmp_path / "output" / "latest"
    output_latest.mkdir(parents=True)
    freshness = output_latest / "data_freshness_latest.csv"
    freshness.write_text(
        "main_price_date,warrant_flow_date,warrant_ready,warrant_daily_publish_allowed\n"
        "20260623,20260623,True,False\n",
        encoding="utf-8",
    )
    contract = tmp_path / "external_data_source_contract.csv"
    contract.write_text(
        "source_id,owner,status_artifact,freshness_date_column,readiness_column,require_matches_main_price_date,json_status_path,allowed_statuses,producer,validator\n"
        "warrant_flow,warrant,output/latest/data_freshness_latest.csv,warrant_flow_date,warrant_daily_publish_allowed,True,,,,\n",
        encoding="utf-8",
    )
    inventory = tmp_path / "repo_production_inventory.csv"
    inventory.write_text("path\n", encoding="utf-8")

    monkeypatch.setattr(validator, "ROOT", tmp_path)
    monkeypatch.setattr(validator, "EXTERNAL_SOURCE_CONTRACT", contract)
    monkeypatch.setattr(validator, "FRESHNESS_CSV", freshness)
    monkeypatch.setattr(validator, "INVENTORY_CSV", inventory)

    assert validator.validate_external_source_contract() == [
        "external source warrant_flow readiness warrant_daily_publish_allowed is not True"
    ]


def test_calendar_degraded_external_source_requires_effect_guards() -> None:
    good = {
        "sources": {
            "twse_ex_right_ex_dividend": {
                "cached_rows": 1,
                "stale_max_trading_days": 3,
                "cache_age_trading_days_max": 1,
                "consecutive_live_failures": 1,
                "max_consecutive_live_failures": 2,
                "model_effect_allowed": False,
                "pdf_effect_allowed": False,
                "calendar_effect_allowed": False,
                "note": "cached stale reminder-only data",
            }
        }
    }
    assert validator.validate_degraded_external_source("calendar_sources", good, "stale_ok") == []

    bad = {
        "sources": {
            "twse_ex_right_ex_dividend": {
                "cached_rows": 1,
                "stale_max_trading_days": 3,
                "cache_age_trading_days_max": 1,
                "consecutive_live_failures": 1,
                "max_consecutive_live_failures": 2,
                "model_effect_allowed": True,
                "pdf_effect_allowed": False,
                "calendar_effect_allowed": False,
                "note": "cached stale reminder-only data",
            }
        }
    }
    errors = validator.validate_degraded_external_source("calendar_sources", bad, "stale_ok")
    assert any("model_effect_allowed=False" in error for error in errors)


def test_calendar_degraded_external_source_requires_cached_rows() -> None:
    bad = {
        "sources": {
            "twse_ex_right_ex_dividend": {
                "cached_rows": 0,
                "stale_max_trading_days": 3,
                "cache_age_trading_days_max": 1,
                "consecutive_live_failures": 1,
                "max_consecutive_live_failures": 2,
                "model_effect_allowed": False,
                "pdf_effect_allowed": False,
                "calendar_effect_allowed": False,
                "note": "cached stale reminder-only data",
            }
        }
    }
    errors = validator.validate_degraded_external_source("calendar_sources", bad, "stale_ok")
    assert any("cached_rows > 0" in error for error in errors)


def test_calendar_degraded_external_source_expires_after_consecutive_failures() -> None:
    bad = {
        "sources": {
            "twse_ex_right_ex_dividend": {
                "blocked_rows": 1,
                "cached_total_rows": 1,
                "consecutive_live_failures": 3,
                "max_consecutive_live_failures": 2,
                "model_effect_allowed": False,
                "pdf_effect_allowed": False,
                "calendar_effect_allowed": False,
                "note": "blocked-effect context cannot affect scoring",
            }
        }
    }
    errors = validator.validate_degraded_external_source("calendar_sources", bad, "degraded_blocked_effect")
    assert any("exceeds max" in error for error in errors)


def test_external_source_contract_runs_bounded_degradation_validator() -> None:
    text = (ROOT / "scripts" / "validate_repo_advanced_integrity.py").read_text(encoding="utf-8")
    assert "validate_degraded_external_source(source_id, data, str(observed_status))" in text


def _historical_replay_contract_row() -> dict[str, str]:
    return {
        "artifact_id": "model_signals_for_report",
        "artifact_glob": (
            "output/history/daily_model_snapshots/"
            "daily_candidate_model_signals_for_report_*.csv"
        ),
        "window_days": "60",
        "min_snapshots": "1",
        "required_columns": (
            "signal_date;stock_id;model_id;model_score;report_line;report_bucket;"
            "mainstream_report_eligible;non_mainstream_report_eligible"
        ),
        "forbidden_columns": "trade_decision",
        "allowed_report_lines": "mainstream;non_mainstream",
        "allowed_report_buckets": "mainstream;non_mainstream",
        "date_column": "signal_date",
        "file_date_regex": (
            r"daily_candidate_model_signals_for_report_(\d{8})"
            r"(?:_r[1-9][0-9]*_[0-9a-f]{12})?\.csv"
        ),
    }


def _write_historical_replay_contract(
    path: Path,
    rows: list[dict[str, str]],
    *,
    fieldnames: tuple[str, ...] = validator.HISTORICAL_REPLAY_CONTRACT_COLUMNS,
) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_minimal_historical_replay_repo(tmp_path: Path, model_id: str) -> None:
    config_dir = tmp_path / "config"
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    config_dir.mkdir(parents=True, exist_ok=True)
    latest_dir.mkdir(parents=True, exist_ok=True)
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    (latest_dir / "data_freshness_latest.csv").write_text(
        "main_price_date\n20260630\n",
        encoding="utf-8",
    )
    _write_historical_replay_contract(
        config_dir / "historical_replay_semantic_contract.csv",
        [_historical_replay_contract_row()],
    )
    (latest_dir / "daily_candidate_model_parameters_latest.csv").write_text(
        "model_id\nneckline_volume_breakout_confirmation\n",
        encoding="utf-8",
    )
    (config_dir / "stock_model_contract_registry.csv").write_text(
        "model_id,effective_from,deprecated_after\n"
        "near_high_neckline_challenge,2026-06-21,2026-06-29\n"
        "platform_strengthening,2026-06-21,2026-06-29\n",
        encoding="utf-8",
    )
    parameter_snapshot = snapshot_dir / "daily_candidate_model_parameters_20260624.csv"
    parameter_snapshot.write_text(
        "model_id\nnear_high_neckline_challenge\nplatform_strengthening\n",
        encoding="utf-8",
    )
    signal_snapshot = snapshot_dir / "daily_candidate_model_signals_for_report_20260624.csv"
    signal_snapshot.write_text(
        "signal_date,stock_id,model_id,model_score,report_line,report_bucket,mainstream_report_eligible,non_mainstream_report_eligible\n"
        f"20260624,2330,{model_id},80,mainstream,mainstream,True,False\n",
        encoding="utf-8",
    )
    manifest = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "snapshot_report_date",
                "snapshot_revision",
                "supersedes_snapshot_sha256",
                "revision_reason",
                "artifact_id",
                "snapshot_path",
                "snapshot_sha256",
            ],
        )
        writer.writeheader()
        for artifact_id, path in (
            ("model_parameters", parameter_snapshot),
            ("model_signals_for_report", signal_snapshot),
        ):
            writer.writerow(
                {
                    "snapshot_report_date": "20260624",
                    "snapshot_revision": "r1",
                    "supersedes_snapshot_sha256": "",
                    "revision_reason": "legacy_v1_manifest",
                    "artifact_id": artifact_id,
                    "snapshot_path": path.relative_to(tmp_path).as_posix(),
                    "snapshot_sha256": snapshot_file_sha256(path),
                }
            )


def _patch_historical_replay_paths(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(validator, "ROOT", tmp_path)
    monkeypatch.setattr(
        validator,
        "HISTORICAL_REPLAY_CONTRACT",
        tmp_path / "config" / "historical_replay_semantic_contract.csv",
    )
    monkeypatch.setattr(
        validator,
        "STOCK_MODEL_CONTRACT_REGISTRY",
        tmp_path / "config" / "stock_model_contract_registry.csv",
    )
    monkeypatch.setattr(
        validator,
        "MODEL_PARAMETERS_CSV",
        tmp_path / "output" / "latest" / "daily_candidate_model_parameters_latest.csv",
    )
    monkeypatch.setattr(
        validator,
        "DAILY_MODEL_SNAPSHOT_DIR",
        tmp_path / "output" / "history" / "daily_model_snapshots",
    )
    monkeypatch.setattr(
        validator,
        "FRESHNESS_CSV",
        tmp_path / "output" / "latest" / "data_freshness_latest.csv",
    )


def test_historical_replay_accepts_dated_deprecated_model_ids(tmp_path: Path, monkeypatch) -> None:
    _write_minimal_historical_replay_repo(tmp_path, "near_high_neckline_challenge")
    _patch_historical_replay_paths(tmp_path, monkeypatch)

    assert validator.validate_historical_replay_semantics() == []

    _write_minimal_historical_replay_repo(tmp_path, "platform_strengthening")
    assert validator.validate_historical_replay_semantics() == []


def test_historical_replay_rejects_never_registered_model_id(tmp_path: Path, monkeypatch) -> None:
    _write_minimal_historical_replay_repo(tmp_path, "not_a_registered_model")
    _patch_historical_replay_paths(tmp_path, monkeypatch)

    errors = validator.validate_historical_replay_semantics()

    assert any("historical replay unknown model_id 'not_a_registered_model'" in error for error in errors)


def test_historical_replay_contract_requires_exact_schema_without_crashing(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _write_minimal_historical_replay_repo(tmp_path, "near_high_neckline_challenge")
    _patch_historical_replay_paths(tmp_path, monkeypatch)
    wrong_order = (
        "artifact_glob",
        "artifact_id",
        *validator.HISTORICAL_REPLAY_CONTRACT_COLUMNS[2:],
    )
    _write_historical_replay_contract(
        validator.HISTORICAL_REPLAY_CONTRACT,
        [_historical_replay_contract_row()],
        fieldnames=wrong_order,
    )

    errors = validator.validate_historical_replay_semantics()

    assert any("schema drift" in error for error in errors)


def test_historical_replay_contract_rejects_duplicate_ids_and_globs(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _write_minimal_historical_replay_repo(tmp_path, "near_high_neckline_challenge")
    _patch_historical_replay_paths(tmp_path, monkeypatch)
    first = _historical_replay_contract_row()
    duplicate_id = dict(first)
    duplicate_id["artifact_glob"] = "output/history/other_*.csv"
    _write_historical_replay_contract(
        validator.HISTORICAL_REPLAY_CONTRACT,
        [first, duplicate_id],
    )
    id_errors = validator.validate_historical_replay_semantics()

    duplicate_glob = dict(first)
    duplicate_glob["artifact_id"] = "different_artifact"
    _write_historical_replay_contract(
        validator.HISTORICAL_REPLAY_CONTRACT,
        [first, duplicate_glob],
    )
    glob_errors = validator.validate_historical_replay_semantics()

    assert any("duplicate artifact_id" in error for error in id_errors)
    assert any("duplicate artifact_glob" in error for error in glob_errors)


def test_historical_replay_contract_hostile_values_return_errors_not_exceptions(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _write_minimal_historical_replay_repo(tmp_path, "near_high_neckline_challenge")
    _patch_historical_replay_paths(tmp_path, monkeypatch)
    cases = (
        ("file_date_regex", "(", "invalid file_date_regex"),
        ("file_date_regex", r"no_date_capture", "report-date capture group"),
        ("window_days", "0", "window_days must be a positive integer"),
        ("window_days", "not_an_integer", "window_days must be a positive integer"),
        (
            "window_days",
            str(validator.MAX_HISTORICAL_REPLAY_WINDOW_DAYS + 1),
            "window_days exceeds reasonable bound",
        ),
        (
            "window_days",
            "9" * 5000,
            "window_days is too large to parse",
        ),
        ("min_snapshots", "0", "min_snapshots must be a positive integer"),
        (
            "min_snapshots",
            "62",
            "min_snapshots exceeds the maximum calendar snapshots",
        ),
    )

    for field, value, expected in cases:
        hostile = _historical_replay_contract_row()
        hostile[field] = value
        _write_historical_replay_contract(
            validator.HISTORICAL_REPLAY_CONTRACT,
            [hostile],
        )

        errors = validator.validate_historical_replay_semantics()

        assert any(expected in error for error in errors), (field, value, errors)


def test_historical_replay_selects_same_day_max_signal_and_parameter_revisions(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _write_minimal_historical_replay_repo(tmp_path, "not_a_registered_model")
    _patch_historical_replay_paths(tmp_path, monkeypatch)
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    parameter_r1 = snapshot_dir / "daily_candidate_model_parameters_20260624.csv"
    parameter_r1.write_text(
        "model_id\nnear_high_neckline_challenge\n",
        encoding="utf-8",
    )
    parameter_r1_sha = snapshot_file_sha256(parameter_r1)
    signal_r1 = snapshot_dir / "daily_candidate_model_signals_for_report_20260624.csv"
    signal_r1_sha = snapshot_file_sha256(signal_r1)
    parameter_staging = snapshot_dir / "parameters-r2-staging.csv"
    parameter_staging.write_text(
        "model_id\nplatform_strengthening\n",
        encoding="utf-8",
    )
    parameter_r2_sha = snapshot_file_sha256(parameter_staging)
    parameter_r2 = snapshot_dir / (
        f"daily_candidate_model_parameters_20260624_r2_{parameter_r2_sha[:12]}.csv"
    )
    parameter_staging.rename(parameter_r2)
    signal_staging = snapshot_dir / "signals-r2-staging.csv"
    signal_staging.write_text(
        "signal_date,stock_id,model_id,model_score,report_line,report_bucket,mainstream_report_eligible,non_mainstream_report_eligible\n"
        "20260624,2330,platform_strengthening,80,mainstream,mainstream,True,False\n",
        encoding="utf-8",
    )
    signal_r2_sha = snapshot_file_sha256(signal_staging)
    signal_r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_20260624_r2_{signal_r2_sha[:12]}.csv"
    )
    signal_staging.rename(signal_r2)
    manifest = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
        fieldnames = list(rows[0])
    for row in rows:
        if row["artifact_id"] == "model_parameters":
            row["snapshot_sha256"] = parameter_r1_sha
    rows.extend(
        [
            {
                "snapshot_report_date": "20260624",
                "snapshot_revision": "r2",
                "supersedes_snapshot_sha256": parameter_r1_sha,
                "revision_reason": "same_day_contract_correction",
                "artifact_id": "model_parameters",
                "snapshot_path": parameter_r2.relative_to(tmp_path).as_posix(),
                "snapshot_sha256": parameter_r2_sha,
            },
            {
                "snapshot_report_date": "20260624",
                "snapshot_revision": "r2",
                "supersedes_snapshot_sha256": signal_r1_sha,
                "revision_reason": "same_day_signal_correction",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": signal_r2.relative_to(tmp_path).as_posix(),
                "snapshot_sha256": signal_r2_sha,
            },
        ]
    )
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    (tmp_path / "config" / "stock_model_contract_registry.csv").write_text(
        "model_id,effective_from,deprecated_after\n"
        "near_high_neckline_challenge,2026-06-21,2026-06-29\n"
        "platform_strengthening,2026-07-01,\n",
        encoding="utf-8",
    )

    assert validator.validate_historical_replay_semantics() == []


def test_advanced_integrity_contracts_exist() -> None:
    for path in validator.REQUIRED_CONFIGS:
        assert path.exists(), path


def test_pdf_golden_contract_has_six_formal_chatgpt_side_reports() -> None:
    with validator.PDF_GOLDEN_CONTRACT.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = {row["report_id"]: row for row in csv.DictReader(fh)}

    assert set(rows) == {
        "mainstream_daily_recommendation_highlight",
        "mainstream_full_candidate_list",
        "non_mainstream_daily_recommendation_highlight",
        "non_mainstream_full_candidate_list",
        "warrant_market_auxiliary",
        "market_risk_background",
    }


def test_runtime_file_lineage_tracer_records_read_and_write(tmp_path: Path) -> None:
    data = tmp_path / "sample.txt"
    tracer = trace_runtime_file_lineage.FileAccessTracer(repo_root=tmp_path)

    with tracer:
        data.write_text("ok", encoding="utf-8")
        assert data.read_text(encoding="utf-8") == "ok"

    events = {(event.operation, event.normalized_path) for event in tracer.iter_unique_events()}
    assert ("Path.write_text:write", "sample.txt") in events
    assert ("Path.read_text:read", "sample.txt") in events


def test_model_condition_spec_covers_registry_models() -> None:
    spec_rows = validator.read_csv_rows(validator.MODEL_CONDITION_SPEC)
    registry_rows = validator.read_csv_rows(validator.MODEL_REGISTRY_CSV)

    spec_models = {row["model_id"] for row in spec_rows}
    registry_models = {
        row["model_id"]
        for row in registry_rows
        if row.get("model_registry_active", "") == "True"
    }
    assert registry_models <= spec_models
