from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import validate_revenue_unreacted_range_promotion_preparation as validator  # noqa: E402


SUMMARY_REPO_PATH = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv"
)
DETAIL_REPO_PATH = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv"
)
def _copy_csv(source: Path, target: Path) -> None:
    target.write_bytes(source.read_bytes())


def _git_blob(repo_path: str, target: Path, *, revision: str = "HEAD") -> None:
    result = subprocess.run(
        ["git", "--no-replace-objects", "show", f"{revision}:{repo_path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    target.write_bytes(result.stdout)


def _read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def _write_rows(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def _fixture_paths(tmp_path: Path) -> tuple[Path, Path, Path, Path]:
    decision = tmp_path / "decision.csv"
    anomalies = tmp_path / "anomalies.csv"
    summary = tmp_path / "summary.csv"
    detail = tmp_path / "detail.csv"
    _copy_csv(validator.DEFAULT_DECISION, decision)
    _copy_csv(validator.DEFAULT_ANOMALIES, anomalies)
    _git_blob(
        SUMMARY_REPO_PATH,
        summary,
        revision=validator.TRUSTED_V1_SOURCE_REVISION,
    )
    _git_blob(
        DETAIL_REPO_PATH,
        detail,
        revision=validator.TRUSTED_V1_SOURCE_REVISION,
    )
    return decision, anomalies, summary, detail


def _validate(paths: tuple[Path, Path, Path, Path]) -> list[str]:
    decision, anomalies, summary, detail = paths
    return validator.validate(
        decision_path=decision,
        anomaly_path=anomalies,
        summary_path=summary,
        detail_path=detail,
        require_source_artifacts=True,
    )


def _create_evidence_reference(
    repo_root: Path,
    *,
    relative_path: str = "docs/evidence/revenue_unreacted_range/case_2408.json",
) -> str:
    evidence_path = repo_root.joinpath(*relative_path.split("/"))
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    evidence_bytes = b'{"case":"2408","status":"verified"}\n'
    evidence_path.write_bytes(evidence_bytes)
    return (
        f"evidence_id=case_2408;path={relative_path};"
        f"sha256={hashlib.sha256(evidence_bytes).hexdigest()}"
    )


def _set_verified_row(
    row: dict[str, str],
    *,
    evidence_reference: str,
    disposition: str = "verified_real_extreme",
) -> None:
    handling, gate = validator.DISPOSITION_POLICIES[disposition]
    row["final_disposition"] = disposition
    row["primary_handling"] = handling
    row["promotion_gate_status"] = gate
    for column in validator.ROOT_CHECK_COLUMNS:
        row[column] = "pass"
    row["evidence_reference"] = evidence_reference
    row["approved_reason_reference"] = (
        evidence_reference if disposition == "verified_non_comparable" else ""
    )
    row["reviewed_at"] = "2026-08-12T12:00:00+08:00"


def test_migration_artifact_bindings_match_referenced_git_blobs() -> None:
    assert validator.validate_migration_artifact_bindings(
        dict(validator.EXPECTED_MIGRATION)
    ) == []


def test_migration_artifact_binding_reports_tampered_raw_blob_as_diagnostic(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original_git = validator._git
    target_spec = (
        f"{validator.TRUSTED_V2_SOURCE_REVISION}:"
        f"{validator.EXPECTED_MIGRATION['source_projection_diff_summary_path']}"
    )

    def tampered_git(*args: str) -> subprocess.CompletedProcess[bytes]:
        result = original_git(*args)
        if args == ("show", target_spec) and result.returncode == 0:
            return subprocess.CompletedProcess(
                result.args,
                result.returncode,
                stdout=result.stdout + b"tampered",
                stderr=result.stderr,
            )
        return result

    monkeypatch.setattr(validator, "_git", tampered_git)
    diagnostics: list[str] = []
    errors = validator.validate_migration_artifact_bindings(
        dict(validator.EXPECTED_MIGRATION),
        diagnostics=diagnostics,
    )
    assert errors == []
    assert any(
        "source_projection_diff_summary_sha256 raw identity differs" in diagnostic
        for diagnostic in diagnostics
    )


def test_default_validation_does_not_touch_trusted_git_or_source_artifacts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        validator,
        "_git",
        lambda *_args: pytest.fail("default validation touched unavailable Git history"),
    )
    monkeypatch.setattr(
        validator,
        "validate_summary",
        lambda *_args, **_kwargs: pytest.fail("default validation read source summary"),
    )
    monkeypatch.setattr(
        validator,
        "validate_detail",
        lambda *_args, **_kwargs: pytest.fail("default validation read source detail"),
    )

    assert validator.validate() == []


def test_explicit_historical_v1_source_audit_routes_to_trusted_git(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    trusted_payloads = {
        validator.DEFAULT_SUMMARY: b"trusted-v1-summary",
        validator.DEFAULT_DETAIL: b"trusted-v1-detail",
    }
    trusted_calls: list[Path] = []

    def trusted_blob(path: Path) -> bytes:
        trusted_calls.append(path)
        return trusted_payloads[path]

    def validate_summary(
        path: Path,
        *,
        payload: bytes | None = None,
        label: str | None = None,
        diagnostics: list[str] | None = None,
    ) -> tuple[dict[str, str], list[str]]:
        assert path == validator.DEFAULT_SUMMARY
        assert payload == trusted_payloads[path]
        assert label is not None and label.startswith("trusted Git ")
        return {}, []

    def validate_detail(
        path: Path,
        _anomaly_rows: list[dict[str, str]],
        *,
        payload: bytes | None = None,
        label: str | None = None,
    ) -> tuple[list[dict[str, str]], list[str]]:
        assert path == validator.DEFAULT_DETAIL
        assert payload == trusted_payloads[path]
        assert label is not None and label.startswith("trusted Git ")
        return [], []

    monkeypatch.setattr(validator, "_trusted_v1_source_blob", trusted_blob)
    monkeypatch.setattr(validator, "validate_summary", validate_summary)
    monkeypatch.setattr(validator, "validate_detail", validate_detail)

    assert validator.validate(historical_v1_source_audit=True) == []
    assert trusted_calls == [validator.DEFAULT_SUMMARY, validator.DEFAULT_DETAIL]


def test_explicit_historical_v1_source_audit_fails_closed_when_revision_unavailable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def unavailable_git(*args: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.CompletedProcess(args, 1, b"", b"shallow clone")

    monkeypatch.setattr(validator, "_git", unavailable_git)
    monkeypatch.setattr(
        validator,
        "validate_summary",
        lambda *_args, **_kwargs: pytest.fail("trusted Git failure reached summary"),
    )
    monkeypatch.setattr(
        validator,
        "validate_detail",
        lambda *_args, **_kwargs: pytest.fail("trusted Git failure reached detail"),
    )

    errors = validator.validate(historical_v1_source_audit=True)

    assert errors == ["trusted v1 promotion source revision is unavailable"]


def test_historical_v1_source_audit_rejects_explicit_source_pair(
    tmp_path: Path,
) -> None:
    errors = validator.validate(
        summary_path=tmp_path / "summary.csv",
        detail_path=tmp_path / "detail.csv",
        historical_v1_source_audit=True,
    )

    assert errors == [
        "historical v1 source audit cannot be combined with explicit summary/detail paths"
    ]


@pytest.mark.parametrize("provided", ["summary", "detail"])
def test_partial_explicit_source_pair_fails_closed(
    tmp_path: Path,
    provided: str,
) -> None:
    source_path = tmp_path / f"{provided}.csv"
    source_path.write_text("present\n", encoding="utf-8")

    errors = validator.validate(
        summary_path=source_path if provided == "summary" else None,
        detail_path=source_path if provided == "detail" else None,
    )

    assert any("complete summary/detail pair" in error for error in errors)


def test_malformed_explicit_source_pair_fails_closed_without_trusted_fallback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    summary_path = tmp_path / "summary.csv"
    detail_path = tmp_path / "detail.csv"
    summary_path.write_text("not,a,valid,summary\n", encoding="utf-8")
    detail_path.write_text("not,a,valid,detail\n", encoding="utf-8")
    monkeypatch.setattr(
        validator,
        "_trusted_v1_source_blob",
        lambda _path: pytest.fail("malformed explicit pair used trusted fallback"),
    )

    errors = validator.validate(
        summary_path=summary_path,
        detail_path=detail_path,
    )

    assert errors
    assert any("CSV is empty" in error for error in errors)


def test_explicit_source_pair_does_not_route_through_trusted_v1_git(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _fixture_paths(tmp_path)
    monkeypatch.setattr(
        validator,
        "_trusted_v1_source_blob",
        lambda _path: pytest.fail("explicit source pair reached trusted v1 routing"),
    )

    assert _validate(paths) == []


def test_exact_source_summary_detail_and_anomaly_set_pass(tmp_path: Path) -> None:
    assert _validate(_fixture_paths(tmp_path)) == []


def test_decision_metric_drift_fails_closed(tmp_path: Path) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[0])
    rows[0]["win_rate_pct"] = "99.0"
    _write_rows(paths[0], columns, rows)

    errors = _validate(paths)

    assert any("promotion preparation win_rate_pct mismatch" in error for error in errors)


def test_anomaly_operation_key_deletion_fails_closed(tmp_path: Path) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[1])
    _write_rows(paths[1], columns, rows[:-1])

    errors = _validate(paths)

    assert any("exact frozen 8 operation keys" in error for error in errors)
    assert any("exactly 8 rows" in error for error in errors)


def test_verified_disposition_without_eight_passes_and_evidence_fails_closed(
    tmp_path: Path,
) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[1])
    rows[0]["final_disposition"] = "verified_real_extreme"
    _write_rows(paths[1], columns, rows)

    errors = _validate(paths)

    assert any("verified disposition requires all eight root checks to pass" in error for error in errors)
    assert any("structured immutable evidence reference" in error for error in errors)
    assert any("verified disposition requires reviewed_at" in error for error in errors)


def test_5484_source_attribution_cannot_drift_to_latest_non_anomalous_source(
    tmp_path: Path,
) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[1])
    row = next(item for item in rows if item["stock_id"] == "5484")
    row["anomaly_source_event_periods"] = "202603"
    row["anomaly_source_available_dates"] = "20260417"
    row["anomaly_source_canonical_row_sha256s"] = (
        "be6be56baa5ea64517911874b21369f54af2e36bb2bcbdc5abf27345abe1fd4b"
    )
    _write_rows(paths[1], columns, rows)

    errors = _validate(paths)

    assert any("5484" in error and "anomaly_source_event_periods mismatch" in error for error in errors)
    assert any("5484" in error and "anomaly_source_canonical_row_sha256s mismatch" in error for error in errors)


def test_rule_formula_and_semantic_binding_mutations_fail_closed(tmp_path: Path) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[0])
    rows[0]["position_rule"] = "position_120d_pct<=75"
    rows[0]["rule_formula_canonical"] = rows[0]["rule_formula_canonical"].replace(
        "0..60", "0..90"
    )
    _write_rows(paths[0], columns, rows)
    summary_columns, summary_rows = _read_rows(paths[2])
    selected = next(row for row in summary_rows if validator._summary_matches(row))
    selected["position_shape_producer_semantic_sha256"] = "0" * 64
    _write_rows(paths[2], summary_columns, summary_rows)

    errors = _validate(paths)

    assert any("position_rule mismatch" in error for error in errors)
    assert any("rule_formula_canonical mismatch" in error for error in errors)
    assert any("rule_formula_sha256 does not bind" in error for error in errors)
    assert any("source summary position_shape_producer_semantic_sha256 mismatch" in error for error in errors)


def test_revenue_rule_threshold_drift_fails_even_with_self_consistent_formula_hash(
    tmp_path: Path,
) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[0])
    row = rows[0]
    row["revenue_rule"] = row["revenue_rule"].replace(">=30", ">=29", 1)
    row["rule_formula_canonical"] = row["rule_formula_canonical"].replace(
        ">=30", ">=29", 1
    )
    row["rule_formula_sha256"] = hashlib.sha256(
        row["rule_formula_canonical"].encode("utf-8")
    ).hexdigest()
    _write_rows(paths[0], columns, rows)

    errors = _validate(paths)

    assert any("revenue_rule mismatch" in error for error in errors)
    assert any("rule_formula_canonical mismatch" in error for error in errors)
    assert not any("rule_formula_sha256 does not bind" in error for error in errors)


@pytest.mark.parametrize(
    ("disposition", "handling", "gate", "needs_reason"),
    [
        ("verified_real_extreme", "retain_in_primary_metrics", "eligible_only_after_all_other_model_gates", False),
        ("verified_data_error", "repair_source_and_rerun_old_metrics_forbidden", "blocked_until_repaired_rerun", False),
        ("verified_non_comparable", "exclude_only_with_approved_reason_and_rerun", "requires_model_governance_review", True),
    ],
)
def test_verified_disposition_requires_exact_global_policy_and_structured_evidence(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    disposition: str,
    handling: str,
    gate: str,
    needs_reason: bool,
) -> None:
    paths = _fixture_paths(tmp_path)
    repo_root = tmp_path / "validator-root"
    monkeypatch.setattr(validator, "ROOT", repo_root)
    columns, rows = _read_rows(paths[1])
    row = rows[0]
    evidence = _create_evidence_reference(repo_root)
    _set_verified_row(row, evidence_reference=evidence, disposition=disposition)
    assert bool(row["approved_reason_reference"]) is needs_reason
    _write_rows(paths[1], columns, rows)

    assert _validate(paths) == []

    row["primary_handling"] = "arbitrary_handling"
    _write_rows(paths[1], columns, rows)
    assert any("disposition policy mismatch" in error for error in _validate(paths))


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    [
        ("missing", "does not resolve to an existing file"),
        ("parent_escape", "must not contain dot segments"),
        ("absolute", "path must be repo-relative"),
        ("outside_allowed_root", "outside the allowed model-owned evidence roots"),
        ("sha_mismatch", "sha256 mismatch"),
    ],
)
def test_verified_evidence_reference_must_bind_real_allowed_repo_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
    expected_error: str,
) -> None:
    paths = _fixture_paths(tmp_path)
    repo_root = tmp_path / "validator-root"
    monkeypatch.setattr(validator, "ROOT", repo_root)
    reference = _create_evidence_reference(repo_root)
    prefix, _, valid_sha256 = reference.rpartition("sha256=")
    if mutation == "missing":
        reference = (
            "evidence_id=case_2408;"
            "path=docs/evidence/revenue_unreacted_range/missing.json;"
            f"sha256={valid_sha256}"
        )
    elif mutation == "parent_escape":
        reference = (
            "evidence_id=case_2408;"
            "path=docs/evidence/revenue_unreacted_range/../../escape.json;"
            f"sha256={valid_sha256}"
        )
    elif mutation == "absolute":
        reference = (
            "evidence_id=case_2408;path=C:/outside/case_2408.json;"
            f"sha256={valid_sha256}"
        )
    elif mutation == "outside_allowed_root":
        outside = repo_root / "config" / "case_2408.json"
        outside.parent.mkdir(parents=True, exist_ok=True)
        outside.write_bytes(b'{"case":"2408","status":"verified"}\n')
        reference = (
            "evidence_id=case_2408;path=config/case_2408.json;"
            f"sha256={valid_sha256}"
        )
    elif mutation == "sha_mismatch":
        reference = f"{prefix}sha256={'0' * 64}"
    else:  # pragma: no cover - parametrization is intentionally closed
        raise AssertionError(mutation)

    columns, rows = _read_rows(paths[1])
    _set_verified_row(rows[0], evidence_reference=reference)
    _write_rows(paths[1], columns, rows)

    assert any(expected_error in error for error in _validate(paths))


def test_arbitrary_verified_evidence_string_fails_closed(tmp_path: Path) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[1])
    row = rows[0]
    row["final_disposition"] = "verified_real_extreme"
    row["primary_handling"] = "retain_in_primary_metrics"
    row["promotion_gate_status"] = "eligible_only_after_all_other_model_gates"
    for column in validator.ROOT_CHECK_COLUMNS:
        row[column] = "pass"
    row["evidence_reference"] = "looks good"
    row["reviewed_at"] = "2026-08-12"
    _write_rows(paths[1], columns, rows)

    assert any("structured immutable evidence reference" in error for error in _validate(paths))


def test_detail_return_mutation_breaks_recomputed_metrics_and_candidate_sha_binding(
    tmp_path: Path,
) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[3])
    selected = next(
        row
        for row in rows
        if row["operation_key"] in validator.EXPECTED_ANOMALIES
    )
    selected["realized_return_pct"] = "999.0"
    selected["candidate_detail_row_sha256"] = "0" * 64
    _write_rows(paths[3], columns, rows)

    errors = _validate(paths)

    assert any("recomputed avg_return_pct mismatch" in error for error in errors)
    assert any("candidate_detail_row_sha256 is not bound to source detail" in error for error in errors)


def test_detail_threshold_crossing_recomputes_both_return_rates(tmp_path: Path) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[3])
    selected_rows = [row for row in rows if validator._detail_matches(row)]
    next(row for row in selected_rows if -20.0 < float(row["realized_return_pct"]) < 20.0)[
        "realized_return_pct"
    ] = "-20.0"
    next(row for row in selected_rows if 0.0 < float(row["realized_return_pct"]) < 20.0)[
        "realized_return_pct"
    ] = "20.0"
    _write_rows(paths[3], columns, rows)

    errors = _validate(paths)

    assert any("recomputed return_ge20_rate_pct mismatch" in error for error in errors)
    assert any("recomputed return_le_minus20_rate_pct mismatch" in error for error in errors)


def test_detail_rule_and_timing_mutations_fail_closed(tmp_path: Path) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[3])
    row = next(item for item in rows if validator._detail_matches(item))
    row["source_position_120d_pct"] = "40.0"
    row["source_shape_return20_pct"] = "-5.0"
    row["latest_source_to_trigger_trading_days"] = "61"
    row["confirmation_index"] = row["trigger_index"]
    _write_rows(paths[3], columns, rows)

    errors = _validate(paths)

    assert any("violates 40<position_120d_pct<=75" in error for error in errors)
    assert any("violates the falling shape rule" in error for error in errors)
    assert any("violates the 0..60 source lag rule" in error for error in errors)
    assert any("violates D+1 confirmation timing" in error for error in errors)


def test_detail_formal_flag_true_fails_closed(tmp_path: Path) -> None:
    paths = _fixture_paths(tmp_path)
    columns, rows = _read_rows(paths[3])
    selected = next(row for row in rows if validator._detail_matches(row))
    selected["formal_model_use_allowed"] = "True"
    _write_rows(paths[3], columns, rows)

    errors = _validate(paths)

    assert any("formal_model_use_allowed mismatch" in error for error in errors)


def test_cli_requires_complete_source_pair(tmp_path: Path) -> None:
    errors = validator.validate(
        summary_path=tmp_path / "missing-summary.csv",
        detail_path=tmp_path / "missing-detail.csv",
        require_source_artifacts=True,
    )

    assert any("complete summary/detail pair" in error for error in errors)


@pytest.mark.parametrize("mutation", ["delete_v1", "reorder", "mutate_v1"])
def test_v1_v2_registry_prefix_is_exact_and_v3_is_append_only(
    tmp_path: Path,
    mutation: str,
) -> None:
    path = tmp_path / "decisions.csv"
    columns, rows = _read_rows(validator.DEFAULT_DECISION)
    if mutation == "delete_v1":
        rows = rows[1:]
    elif mutation == "reorder":
        rows = list(reversed(rows))
    else:
        rows[0]["operation_count"] = "53"
    _write_rows(path, columns, rows)

    _row, errors = validator.validate_decision(path)

    assert errors
    assert any(
        "exact v1 prefix" in error
        or "exact v1/v2 prefix" in error
        or "mismatch in v1" in error
        or "mismatch in v2" in error
        for error in errors
    )


def test_v2_trusted_git_audit_recomputes_exact_53_metrics() -> None:
    anomaly_rows, anomaly_errors = validator.validate_anomalies(
        validator.DEFAULT_ANOMALIES_V2,
        expected_anomalies=validator.EXPECTED_ANOMALIES_V2,
        version_label="v2",
    )
    assert anomaly_errors == []
    summary_payload = validator._trusted_v2_source_blob(validator.DEFAULT_SUMMARY)
    detail_payload = validator._trusted_v2_source_blob(validator.DEFAULT_DETAIL)

    selected_summary, summary_errors = validator.validate_summary(
        validator.DEFAULT_SUMMARY,
        payload=summary_payload,
        expected_summary=validator.SUMMARY_EXPECTED_V2,
    )
    selected_detail, detail_errors = validator.validate_detail(
        validator.DEFAULT_DETAIL,
        anomaly_rows,
        payload=detail_payload,
        expected_decision=validator.EXPECTED_DECISION_V2,
        expected_summary=validator.SUMMARY_EXPECTED_V2,
    )

    assert summary_errors == []
    assert detail_errors == []
    assert selected_summary is not None
    assert selected_summary["operation_count"] == "53"
    assert len(selected_detail) == 53


def test_v2_stale_raw_blob_literal_does_not_override_git_tree_semantics(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(
        validator.TRUSTED_V2_SOURCE_ARTIFACTS[validator.DEFAULT_SUMMARY],
        "blob",
        "0" * 40,
    )

    errors = validator.validate(source_audit="v2")

    assert errors == []


def test_v2_anomaly_registry_has_exact_9_and_6177_is_fail_closed() -> None:
    rows, errors = validator.validate_anomalies(
        validator.DEFAULT_ANOMALIES_V2,
        expected_anomalies=validator.EXPECTED_ANOMALIES_V2,
        version_label="v2",
    )

    assert errors == []
    assert len(rows) == 9
    row = next(item for item in rows.values() if item["stock_id"] == "6177")
    assert row["anomaly_attribution_mode"] == (
        "published_episode_level_source_flag_no_trigger_asof_event_requires_reconciliation"
    )
    assert row["anomaly_source_available_dates"] == (
        "not_applicable_pending_trigger_asof_reconciliation"
    )
    assert row["pit_calendar_continuity_status"] == "fail"
    assert row["raw_source_lineage_status"] == "fail"


def test_6177_future_event_cannot_be_backfilled_as_trigger_asof_attribution(
    tmp_path: Path,
) -> None:
    path = tmp_path / "anomalies-v2.csv"
    columns, rows = _read_rows(validator.DEFAULT_ANOMALIES_V2)
    row = next(item for item in rows if item["stock_id"] == "6177")
    row["anomaly_attribution_mode"] = "exact_anomaly_causing_qualifying_source_events"
    row["anomaly_source_event_periods"] = "202512"
    row["anomaly_source_available_dates"] = "20260117"
    row["anomaly_source_canonical_row_sha256s"] = (
        "d26bc6a94cf5869836e96f77b7af128b007b3159ae7680eb4e14030c7d19aae1"
    )
    row["anomaly_source_raw_file_sha256s"] = "0" * 64
    _write_rows(path, columns, rows)

    _rows, errors = validator.validate_anomalies(
        path,
        expected_anomalies=validator.EXPECTED_ANOMALIES_V2,
        version_label="v2",
    )

    assert any("available date is after trigger" in error for error in errors)
    assert any("6177 future-contaminated attribution must remain fail-closed" in error for error in errors)


def test_v1_v2_selected_operation_reconciliation_is_exact_46_7_6_and_2_rekeys() -> None:
    v1_anomalies, assert_v1 = validator.validate_anomalies(
        validator.DEFAULT_ANOMALIES,
        expected_anomalies=validator.EXPECTED_ANOMALIES_V1,
        version_label="v1",
    )
    v2_anomalies, assert_v2 = validator.validate_anomalies(
        validator.DEFAULT_ANOMALIES_V2,
        expected_anomalies=validator.EXPECTED_ANOMALIES_V2,
        version_label="v2",
    )
    migration, migration_errors = validator.validate_migration(validator.DEFAULT_MIGRATIONS)
    assert assert_v1 == []
    assert assert_v2 == []
    assert migration_errors == []
    assert migration is not None

    v1_rows, v1_errors = validator.validate_detail(
        validator.DEFAULT_DETAIL,
        v1_anomalies,
        payload=validator._trusted_v1_source_blob(validator.DEFAULT_DETAIL),
    )
    v2_rows, v2_errors = validator.validate_detail(
        validator.DEFAULT_DETAIL,
        v2_anomalies,
        payload=validator._trusted_v2_source_blob(validator.DEFAULT_DETAIL),
        expected_decision=validator.EXPECTED_DECISION_V2,
        expected_summary=validator.SUMMARY_EXPECTED_V2,
    )
    assert v1_errors == []
    assert v2_errors == []
    assert validator.validate_v1_v2_reconciliation(v1_rows, v2_rows, migration) == []
    assert migration["exact_common_operation_key_count"] == "46"
    assert migration["raw_added_operation_key_count"] == "7"
    assert migration["raw_removed_operation_key_count"] == "6"
    assert migration["episode_identity_rekey_count"] == "2"


def test_v1_v2_reconciliation_detects_extra_identity_rekey() -> None:
    v1_anomalies, _ = validator.validate_anomalies(validator.DEFAULT_ANOMALIES)
    v2_anomalies, _ = validator.validate_anomalies(
        validator.DEFAULT_ANOMALIES_V2,
        expected_anomalies=validator.EXPECTED_ANOMALIES_V2,
        version_label="v2",
    )
    migration, _ = validator.validate_migration(validator.DEFAULT_MIGRATIONS)
    assert migration is not None
    v1_rows, _ = validator.validate_detail(
        validator.DEFAULT_DETAIL,
        v1_anomalies,
        payload=validator._trusted_v1_source_blob(validator.DEFAULT_DETAIL),
    )
    v2_rows, _ = validator.validate_detail(
        validator.DEFAULT_DETAIL,
        v2_anomalies,
        payload=validator._trusted_v2_source_blob(validator.DEFAULT_DETAIL),
        expected_decision=validator.EXPECTED_DECISION_V2,
        expected_summary=validator.SUMMARY_EXPECTED_V2,
    )
    common_key = next(
        row["operation_key"]
        for row in v2_rows
        if row["operation_key"] in {item["operation_key"] for item in v1_rows}
    )
    next(row for row in v2_rows if row["operation_key"] == common_key)[
        "operation_key"
    ] = common_key + "|mutated"

    errors = validator.validate_v1_v2_reconciliation(v1_rows, v2_rows, migration)

    assert any("exact_common_operation_key_count mismatch" in error for error in errors)
    assert any("episode_identity_rekey_count mismatch" in error for error in errors)
def _write_mature_forward_holdout_manifest(
    path: Path,
    *,
    mature: int = 20,
    right_censored: int = 0,
    total_mature: int | None = None,
    total_right_censored: int | None = None,
) -> None:
    if total_mature is None:
        total_mature = mature
    if total_right_censored is None:
        total_right_censored = right_censored
    row = {
        "model_id": "revenue_unreacted_range",
        "artifact_id": "revenue_unreacted_range_forward_holdout_v2",
        "artifact_version": "forward_holdout_v2_20260828",
        "artifact_row_key": "manifest",
        "holdout_start_date": "20260831",
        "append_only_history": "True",
        "research_only": "True",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "presentation_allowed": "False",
        "production_change": "False",
        "primary_mature_count": str(mature),
        "primary_right_censored_count": str(right_censored),
        "holdout_event_count": str(total_mature + total_right_censored),
        "mature_event_count": str(total_mature),
        "bridge_excluded_signal_count": "3",
    }
    _write_rows(path, list(row), [row])


def _forward_holdout_evidence_fixture(
    tmp_path: Path,
    manifest_path: Path,
) -> tuple[dict[str, Path], Path, str]:
    paths: dict[str, Path] = {"manifest": manifest_path}
    for name in validator.DEFAULT_FORWARD_HOLDOUT_V2_EVIDENCE_PATHS:
        if name == "manifest":
            continue
        path = tmp_path / f"{name}.csv"
        path.write_text("placeholder\n", encoding="utf-8")
        paths[name] = path
    price_dir = tmp_path / "price-inputs"
    price_dir.mkdir()
    (price_dir / "2330.csv").write_text("date,open,close\n", encoding="utf-8")
    return paths, price_dir, "a" * 40


def _resolved_anomalies() -> dict[str, dict[str, str]]:
    return {
        f"case-{index}": {
            "final_disposition": "verified_real_extreme",
            "promotion_gate_status": "eligible_only_after_all_other_model_gates",
        }
        for index in range(9)
    }


def test_v5_disabled_adapter_history_remains_append_only_and_business_immutable() -> None:
    decision, decision_errors = validator.validate_decision(validator.DEFAULT_DECISION)
    migration, migration_errors = validator.validate_migration(
        validator.DEFAULT_MIGRATIONS
    )

    assert decision_errors == []
    assert migration_errors == []
    assert decision == validator.EXPECTED_DECISION_V6
    assert migration == validator.EXPECTED_MIGRATION_V1_TO_V2
    _decision_columns, decision_rows = _read_rows(validator.DEFAULT_DECISION)
    assert decision_rows[-3] == validator.EXPECTED_DECISION_V4
    assert decision_rows[-2] == validator.EXPECTED_DECISION_V5
    assert all(
        decision_rows[-3][column] == decision_rows[-2][column]
        for column in validator.V4_TO_V5_COMMON_DECISION_FIELDS
    )
    _migration_columns, migration_rows = _read_rows(validator.DEFAULT_MIGRATIONS)
    assert migration_rows[-3] == validator.EXPECTED_MIGRATION_V3_TO_V4
    assert migration_rows[-2] == validator.EXPECTED_MIGRATION_V4_TO_V5
    assert migration_rows[-2]["from_source_revision"] == migration_rows[-2]["to_source_revision"]
    assert migration_rows[-2]["from_source_artifact_version"] == migration_rows[-2]["to_source_artifact_version"]
    assert migration_rows[-2]["common_business_field_change_count"] == "0"
    assert migration_rows[-2]["v1_anomaly_count"] == "8"
    assert migration_rows[-2]["v2_anomaly_count"] == "8"
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_change",
    ):
        assert decision_rows[-2][column] == "False"
        assert migration_rows[-2][column] == "False"


def test_v6_provisional_activation_is_append_only_and_keeps_frozen_rule() -> None:
    decision, decision_errors = validator.validate_decision(validator.DEFAULT_DECISION)
    _migration, migration_errors = validator.validate_migration(
        validator.DEFAULT_MIGRATIONS
    )

    assert decision_errors == []
    assert migration_errors == []
    assert decision == validator.EXPECTED_DECISION_V6
    _decision_columns, decision_rows = _read_rows(validator.DEFAULT_DECISION)
    assert decision_rows[-2] == validator.EXPECTED_DECISION_V5
    assert decision_rows[-1] == validator.EXPECTED_DECISION_V6
    assert all(
        decision_rows[-2][column] == decision_rows[-1][column]
        for column in validator.V5_TO_V6_FROZEN_BUSINESS_FIELDS
    )
    assert decision_rows[-1]["forward_holdout_gate_policy"] == (
        "post_launch_monitoring_non_hard_no_tuning"
    )
    assert decision_rows[-1]["decision_status"] == (
        "provisional_backtest_supported_oos_unconfirmed"
    )
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_change",
    ):
        assert decision_rows[-1][column] == "True"

    _migration_columns, migration_rows = _read_rows(validator.DEFAULT_MIGRATIONS)
    assert migration_rows[-2] == validator.EXPECTED_MIGRATION_V4_TO_V5
    assert migration_rows[-1] == validator.EXPECTED_MIGRATION_V5_TO_V6
    assert migration_rows[-1]["from_source_revision"] == (
        migration_rows[-1]["to_source_revision"]
    )
    assert migration_rows[-1]["common_business_field_change_count"] == "0"
    assert migration_rows[-1]["research_only"] == "False"
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_change",
    ):
        assert migration_rows[-1][column] == "True"


def test_v5_business_field_drift_fails_closed(tmp_path: Path) -> None:
    path = tmp_path / "promotion.csv"
    columns, rows = _read_rows(validator.DEFAULT_DECISION)
    rows[-2]["position_rule"] = "40<position_120d_pct<=76"
    _write_rows(path, columns, rows)

    _row, errors = validator.validate_decision(path)

    assert any("position_rule mismatch in v5" in error for error in errors)
    assert any("changed frozen common decision fields" in error for error in errors)


def test_v5_permission_flip_fails_closed(tmp_path: Path) -> None:
    path = tmp_path / "promotion.csv"
    columns, rows = _read_rows(validator.DEFAULT_DECISION)
    rows[-2]["formal_model_use_allowed"] = "True"
    _write_rows(path, columns, rows)

    _row, errors = validator.validate_decision(path)

    assert any("formal_model_use_allowed mismatch in v5" in error for error in errors)


def test_v4_to_v5_common_business_change_count_tamper_fails(tmp_path: Path) -> None:
    path = tmp_path / "migrations.csv"
    columns, rows = _read_rows(validator.DEFAULT_MIGRATIONS)
    rows[-2]["common_business_field_change_count"] = "1"
    _write_rows(path, columns, rows)

    _row, errors = validator.validate_migration(path)

    assert any(
        "common_business_field_change_count mismatch in row 4" in error
        for error in errors
    )


def test_library_governance_validation_without_a_phase_remains_available() -> None:
    assert validator.validate() == []


def test_research_only_phase_requires_trusted_v2_source_contract() -> None:
    errors = validator.validate(phase="research-only")

    assert any("requires the trusted v2 PIT/lineage source contract" in error for error in errors)


def test_research_only_phase_accepts_trusted_v2_source_audit() -> None:
    assert validator.validate(phase="research-only", source_audit="v2") == []


def test_promotion_candidate_phase_requires_dispositions_and_mature_holdout(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    holdout = tmp_path / "holdout.csv"
    _write_mature_forward_holdout_manifest(holdout, mature=19)
    evidence_paths, price_dir, history_base_ref = _forward_holdout_evidence_fixture(
        tmp_path,
        holdout,
    )
    monkeypatch.setattr(
        validator,
        "_run_canonical_validator",
        lambda _label, _command: [],
    )
    monkeypatch.setattr(
        validator,
        "validate_current_anomaly_dispositions",
        lambda _root, *, require_effective_nonblocking: SimpleNamespace(
            errors=[
                "promotion-candidate anomaly gate remains blocked: "
                "operation_keys=['case-1']"
            ],
            diagnostics=[],
        ),
    )

    errors = validator.validate_phase_gates(
        "promotion-candidate",
        dict(validator.EXPECTED_DECISION_V5),
        {},
        source_contract_verified=True,
        forward_holdout_manifest_path=holdout,
        forward_holdout_evidence_paths=evidence_paths,
        forward_holdout_price_input_directory=price_dir,
        forward_holdout_history_base_ref=history_base_ref,
    )

    assert any("operation_keys=['case-1']" in error for error in errors)
    assert any("primary_mature_count=19; required=20" in error for error in errors)


def test_v6_promotion_candidate_keeps_holdout_integrity_without_maturity_gate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    holdout = tmp_path / "holdout.csv"
    _write_mature_forward_holdout_manifest(holdout, mature=0)
    evidence_paths, price_dir, history_base_ref = _forward_holdout_evidence_fixture(
        tmp_path,
        holdout,
    )
    commands: list[list[str]] = []

    def pass_canonical_validator(_label: str, command: list[str]) -> list[str]:
        commands.append(command)
        return []

    monkeypatch.setattr(validator, "_run_canonical_validator", pass_canonical_validator)
    monkeypatch.setattr(
        validator,
        "validate_current_anomaly_dispositions",
        lambda _root, *, require_effective_nonblocking: SimpleNamespace(
            errors=[],
            diagnostics=[],
        ),
    )

    assert validator.validate_phase_gates(
        "promotion-candidate",
        dict(validator.EXPECTED_DECISION_V6),
        _resolved_anomalies(),
        source_contract_verified=True,
        forward_holdout_manifest_path=holdout,
        forward_holdout_evidence_paths=evidence_paths,
        forward_holdout_price_input_directory=price_dir,
        forward_holdout_history_base_ref=history_base_ref,
    ) == []
    assert len(commands) == 1
    assert str(validator.FORWARD_HOLDOUT_V2_VALIDATOR) in commands[0]


def test_promotion_candidate_uses_primary_maturity_without_equating_challenger_totals(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    holdout = tmp_path / "holdout.csv"
    _write_mature_forward_holdout_manifest(
        holdout,
        mature=20,
        right_censored=2,
        total_mature=31,
        total_right_censored=7,
    )
    evidence_paths, price_dir, history_base_ref = _forward_holdout_evidence_fixture(
        tmp_path,
        holdout,
    )
    commands: list[list[str]] = []

    def pass_canonical_validator(_label: str, command: list[str]) -> list[str]:
        commands.append(command)
        return []

    monkeypatch.setattr(validator, "_run_canonical_validator", pass_canonical_validator)
    monkeypatch.setattr(
        validator,
        "validate_current_anomaly_dispositions",
        lambda _root, *, require_effective_nonblocking: SimpleNamespace(
            errors=[],
            diagnostics=[],
        ),
    )

    assert validator.validate_phase_gates(
        "promotion-candidate",
        dict(validator.EXPECTED_DECISION_V5),
        _resolved_anomalies(),
        source_contract_verified=True,
        forward_holdout_manifest_path=holdout,
        forward_holdout_evidence_paths=evidence_paths,
        forward_holdout_price_input_directory=price_dir,
        forward_holdout_history_base_ref=history_base_ref,
    ) == []
    assert len(commands) == 1
    assert str(validator.FORWARD_HOLDOUT_V2_VALIDATOR) in commands[0]
    assert "--source-detail" in commands[0]
    assert "--history-base-ref" in commands[0]


def test_minimal_forward_holdout_manifest_cannot_satisfy_promotion_gate(
    tmp_path: Path,
) -> None:
    holdout = tmp_path / "holdout.csv"
    _write_mature_forward_holdout_manifest(holdout)
    missing_evidence_paths = {
        name: tmp_path / f"missing-{name}.csv"
        for name in validator.DEFAULT_FORWARD_HOLDOUT_V2_EVIDENCE_PATHS
        if name != "manifest"
    }

    errors = validator.validate_phase_gates(
        "promotion-candidate",
        dict(validator.EXPECTED_DECISION_V5),
        _resolved_anomalies(),
        source_contract_verified=True,
        forward_holdout_manifest_path=holdout,
        forward_holdout_evidence_paths=missing_evidence_paths,
    )

    assert any("evidence is missing" in error for error in errors)
    assert any("explicit price_input_directory" in error for error in errors)
    assert any("immutable 40-character Git commit" in error for error in errors)


def test_production_pdf_phase_remains_blocked_by_disabled_adapter_contract(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    holdout = tmp_path / "holdout.csv"
    readiness = tmp_path / "readiness.csv"
    _write_mature_forward_holdout_manifest(holdout)
    evidence_paths, price_dir, history_base_ref = _forward_holdout_evidence_fixture(
        tmp_path,
        holdout,
    )
    monkeypatch.setattr(
        validator,
        "_run_canonical_validator",
        lambda _label, _command: [],
    )
    _write_rows(
        readiness,
        [
            "model_id",
            "approved_for_daily",
            "presentation_allowed",
            "daily_adapter_status",
            "pdf_integration_status",
        ],
        [
            {
                "model_id": "revenue_unreacted_range",
                "approved_for_daily": "True",
                "presentation_allowed": "True",
                "daily_adapter_status": "ready_approved_operation_guidance",
                "pdf_integration_status": "pdf_integrated_daily_adapter",
            }
        ],
    )
    resolved = {
        f"case-{index}": {
            "final_disposition": "verified_real_extreme",
            "promotion_gate_status": "eligible_only_after_all_other_model_gates",
        }
        for index in range(9)
    }

    errors = validator.validate_phase_gates(
        "production-pdf",
        dict(validator.EXPECTED_DECISION_V5),
        resolved,
        source_contract_verified=True,
        forward_holdout_manifest_path=holdout,
        forward_holdout_evidence_paths=evidence_paths,
        forward_holdout_price_input_directory=price_dir,
        forward_holdout_history_base_ref=history_base_ref,
        operation_readiness_path=readiness,
    )

    assert any("formal_model_use_allowed=True" in error for error in errors)
    assert any("disabled adapter preparation" in error for error in errors)


def _approved_production_decision() -> dict[str, str]:
    return dict(validator.EXPECTED_DECISION_V6)


def test_production_pdf_rejects_legacy_readiness_without_production_allowed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    holdout = tmp_path / "holdout.csv"
    readiness = tmp_path / "model_operation_readiness_latest.csv"
    _write_mature_forward_holdout_manifest(holdout)
    evidence_paths, price_dir, history_base_ref = _forward_holdout_evidence_fixture(
        tmp_path,
        holdout,
    )
    _write_rows(
        readiness,
        [
            "model_id",
            "approved_for_daily",
            "presentation_allowed",
            "daily_adapter_status",
            "pdf_integration_status",
        ],
        [
            {
                "model_id": "revenue_unreacted_range",
                "approved_for_daily": "True",
                "presentation_allowed": "True",
                "daily_adapter_status": "ready_approved_operation_guidance",
                "pdf_integration_status": "pdf_integrated_daily_adapter",
            }
        ],
    )
    monkeypatch.setattr(validator, "DEFAULT_OPERATION_READINESS", readiness)
    monkeypatch.setattr(
        validator,
        "_run_canonical_validator",
        lambda _label, _command: [],
    )

    errors = validator.validate_phase_gates(
        "production-pdf",
        _approved_production_decision(),
        _resolved_anomalies(),
        source_contract_verified=True,
        forward_holdout_manifest_path=holdout,
        forward_holdout_evidence_paths=evidence_paths,
        forward_holdout_price_input_directory=price_dir,
        forward_holdout_history_base_ref=history_base_ref,
        operation_readiness_path=readiness,
        formal_adapter_history_base_ref="b" * 40,
    )

    assert any("readiness schema is incomplete" in error for error in errors)
    assert any("production_allowed" in error for error in errors)


def test_production_pdf_delegates_to_model_adapter_readiness_and_pdf_validators(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_root = tmp_path / "repo"
    scripts = repo_root / "scripts"
    latest = repo_root / "output/latest"
    history = repo_root / "output/history/daily_model_snapshots"
    scripts.mkdir(parents=True)
    latest.mkdir(parents=True)
    history.mkdir(parents=True)
    holdout = tmp_path / "holdout.csv"
    _write_mature_forward_holdout_manifest(holdout)
    evidence_paths, price_dir, history_base_ref = _forward_holdout_evidence_fixture(
        tmp_path,
        holdout,
    )
    forward_validator = scripts / "validate_revenue_unreacted_range_forward_holdout_v2.py"
    module = scripts / "build_daily_revenue_unreacted_range_operation_section.py"
    adapter_validator = scripts / "validate_daily_revenue_unreacted_range_operation_section.py"
    readiness_validator = scripts / "validate_model_operation_readiness.py"
    revenue_pdf_validator = (
        scripts / "validate_revenue_unreacted_range_pdf_consumer_contract.py"
    )
    pdf_validator = scripts / "validate_daily_pdf_contract_consumers.py"
    artifact = latest / "daily_revenue_unreacted_range_operation_section_latest.csv"
    readiness = latest / "model_operation_readiness_latest.csv"
    for path in (
        forward_validator,
        module,
        adapter_validator,
        readiness_validator,
        revenue_pdf_validator,
        pdf_validator,
    ):
        path.write_text("placeholder\n", encoding="utf-8")
    _write_rows(artifact, ["generated_at"], [{"generated_at": "runtime-time"}])
    artifact_semantic = b'generated_at\n""\n'
    artifact_sha = hashlib.sha256(artifact_semantic).hexdigest()
    history_snapshot = history / (
        "daily_revenue_unreacted_range_operation_section_20260828_"
        f"{artifact_sha}.csv"
    )
    snapshot_path = (
        Path("\\\\?\\" + str(history_snapshot.resolve()))
        if sys.platform == "win32"
        else history_snapshot
    )
    snapshot_path.write_bytes(artifact_semantic)
    monkeypatch.setattr(validator, "ROOT", repo_root)
    monkeypatch.setattr(validator, "FORWARD_HOLDOUT_V2_VALIDATOR", forward_validator)
    monkeypatch.setattr(validator, "DEFAULT_OPERATION_READINESS", readiness)
    monkeypatch.setattr(validator, "FORMAL_ADAPTER_MODULE", module)
    monkeypatch.setattr(validator, "FORMAL_ADAPTER_VALIDATOR", adapter_validator)
    monkeypatch.setattr(validator, "FORMAL_ADAPTER_ARTIFACT", artifact)
    monkeypatch.setattr(validator, "FORMAL_ADAPTER_HISTORY_DIRECTORY", history)
    monkeypatch.setattr(validator, "MODEL_OPERATION_READINESS_VALIDATOR", readiness_validator)
    monkeypatch.setattr(
        validator,
        "FORMAL_ADAPTER_PDF_CONSUMER_VALIDATOR",
        revenue_pdf_validator,
    )
    monkeypatch.setattr(validator, "DAILY_PDF_CONSUMER_VALIDATOR", pdf_validator)
    row = {
        "model_id": "revenue_unreacted_range",
        "formal_model_use_allowed": "True",
        "approved_for_daily": "True",
        "presentation_allowed": "True",
        "production_allowed": "True",
        "approval_status": validator.FORMAL_ADAPTER_APPROVAL_STATUS,
        "approval_version": validator.FORMAL_ADAPTER_APPROVAL_VERSION,
        "operation_module_status": validator.FORMAL_ADAPTER_OPERATION_MODULE_STATUS,
        "operation_module_id": validator.FORMAL_ADAPTER_MODULE_ID,
        "operation_module_path": "scripts/build_daily_revenue_unreacted_range_operation_section.py",
        "operation_module_canonical_sha256": hashlib.sha256(b"placeholder\n").hexdigest(),
        "daily_adapter_status": "ready_empty_no_operation_rows",
        "adapter_artifact_id": validator.FORMAL_ADAPTER_ARTIFACT_ID,
        "adapter_artifact_version": validator.FORMAL_ADAPTER_APPROVAL_VERSION,
        "adapter_artifact_path": (
            "output/latest/daily_revenue_unreacted_range_operation_section_latest.csv"
        ),
        "adapter_artifact_canonical_sha256": artifact_sha,
        "adapter_schema_version": validator.FORMAL_ADAPTER_SCHEMA_VERSION,
        "lifecycle_contract_version": validator.FORMAL_ADAPTER_LIFECYCLE_VERSION,
        "daily_adapter_sections": ",".join(
            sorted(validator.FORMAL_ADAPTER_REQUIRED_SECTIONS)
        ),
        "operation_directive_level": "approved_daily_operation_guidance",
        "pdf_integration_status": "pdf_integrated_daily_adapter",
        "packet_integration_status": "pending_packet_consumer",
    }
    _write_rows(readiness, sorted(row), [row])
    calls: list[tuple[str, list[str]]] = []

    def pass_canonical_validator(label: str, command: list[str]) -> list[str]:
        calls.append((label, command))
        return []

    monkeypatch.setattr(validator, "_run_canonical_validator", pass_canonical_validator)
    monkeypatch.setattr(
        validator.subprocess,
        "run",
        lambda *_args, **_kwargs: SimpleNamespace(
            returncode=0,
            stdout="",
            stderr="",
        ),
    )
    monkeypatch.setattr(
        validator,
        "validate_current_anomaly_dispositions",
        lambda _root, *, require_effective_nonblocking: SimpleNamespace(
            errors=[],
            diagnostics=[],
        ),
    )

    errors = validator.validate_phase_gates(
        "production-pdf",
        _approved_production_decision(),
        _resolved_anomalies(),
        source_contract_verified=True,
        forward_holdout_manifest_path=holdout,
        forward_holdout_evidence_paths=evidence_paths,
        forward_holdout_price_input_directory=price_dir,
        forward_holdout_history_base_ref=history_base_ref,
        operation_readiness_path=readiness,
        formal_adapter_history_base_ref="b" * 40,
    )

    assert errors == []
    assert len(calls) == 5
    labels = [label for label, _command in calls]
    assert any("forward holdout v2" in label for label in labels)
    assert any("formal adapter" in label for label in labels)
    assert any("model operation readiness" in label for label in labels)
    assert any("model-owned revenue PDF consumer" in label for label in labels)
    assert any("PDF consumer" in label for label in labels)
    adapter_command = next(command for label, command in calls if "formal adapter" in label)
    assert "--source-module" in adapter_command
    assert "--history-snapshot" in adapter_command


def test_raw_monthly_blob_drift_is_diagnostic_but_canonical_drift_blocks(
    tmp_path: Path,
) -> None:
    summary = tmp_path / "summary.csv"
    _git_blob(
        SUMMARY_REPO_PATH,
        summary,
        revision=validator.TRUSTED_V2_SOURCE_REVISION,
    )
    columns, rows = _read_rows(summary)
    selected = next(
        row
        for row in rows
        if validator._summary_matches(row, validator.SUMMARY_EXPECTED_V2)
    )
    selected["monthly_revenue_history_blob_sha256"] = "0" * 64
    _write_rows(summary, columns, rows)
    diagnostics: list[str] = []

    _row, errors = validator.validate_summary(
        summary,
        expected_summary=validator.SUMMARY_EXPECTED_V2,
        diagnostics=diagnostics,
    )

    assert errors == []
    assert any("provenance value" in diagnostic for diagnostic in diagnostics)

    selected["monthly_revenue_canonical_table_sha256"] = "0" * 64
    _write_rows(summary, columns, rows)
    _row, errors = validator.validate_summary(
        summary,
        expected_summary=validator.SUMMARY_EXPECTED_V2,
    )
    assert any("monthly_revenue_canonical_table_sha256 mismatch" in error for error in errors)
