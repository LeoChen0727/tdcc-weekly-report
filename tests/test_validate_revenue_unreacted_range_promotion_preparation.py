from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from pathlib import Path

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
