from __future__ import annotations

import copy
import csv
import io
import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import validate_revenue_unreacted_range_anomaly_dispositions as validator  # noqa: E402


def _evidence_documents() -> list[dict[str, object]]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((ROOT / validator.EVIDENCE_ROOT).glob("*.json"))
    ]


def test_evidence_canonical_sha_binds_semantics_not_transport_provenance() -> None:
    document = _evidence_documents()[0]
    original = validator.evidence_canonical_sha256(document)

    provenance_only = copy.deepcopy(document)
    provenance_only["provenance"]["retrieved_at"] = "2099-01-01T00:00:00+08:00"
    provenance_only["provenance"]["raw_response_sha256"] = "not_persisted_diagnostic"
    assert validator.evidence_canonical_sha256(provenance_only) == original

    semantic_change = copy.deepcopy(document)
    semantic_change["semantic_payload"]["identity"]["entry_date"] = "20990101"
    assert validator.evidence_canonical_sha256(semantic_change) != original


def test_registry_canonical_sha_ignores_raw_blob_and_line_endings(tmp_path: Path) -> None:
    columns = [
        "operation_key",
        "realized_return_pct",
        "final_disposition",
        "anomaly_source_raw_file_sha256s",
    ]
    rows = [
        {
            "operation_key": "key-1",
            "realized_return_pct": "5.2740",
            "final_disposition": "verified_real_extreme",
            "anomaly_source_raw_file_sha256s": "raw-a",
        }
    ]

    def render(raw_value: str, return_value: str, line_ending: str) -> bytes:
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=columns, lineterminator=line_ending)
        writer.writeheader()
        writer.writerow(
            {
                **rows[0],
                "realized_return_pct": return_value,
                "anomaly_source_raw_file_sha256s": raw_value,
            }
        )
        return stream.getvalue().encode("utf-8")

    first = tmp_path / "first.csv"
    second = tmp_path / "second.csv"
    first.write_bytes(render("raw-a", "5.2740", "\n"))
    second.write_bytes(render("raw-b", "5.274", "\r\n"))

    assert validator.csv_semantic_sha256(
        first,
        excluded_columns=validator.REGISTRY_PROVENANCE_COLUMNS,
    ) == validator.csv_semantic_sha256(
        second,
        excluded_columns=validator.REGISTRY_PROVENANCE_COLUMNS,
    )
    assert validator.csv_semantic_sha256(first) != validator.csv_semantic_sha256(second)


def test_monthly_revenue_canonical_rows_replay_exact_registered_evidence() -> None:
    with (ROOT / validator.MONTHLY_REVENUE_PATH).open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    by_key = {
        (row["stock_id"].zfill(4), row["revenue_period"]): row
        for row in rows
    }

    event_count = 0
    for document in _evidence_documents():
        payload = document["semantic_payload"]
        stock_id = payload["identity"]["stock_id"]
        events = payload["root_checks"]["raw_source_lineage"]["monthly_revenue_events"]
        for event in events:
            event_count += 1
            row = by_key[(stock_id, event["period"])]
            assert (
                validator.monthly_revenue_row_canonical_sha256(row)
                == event["canonical_row_sha256"]
            )
    assert event_count >= 11


def test_evidence_never_claims_unpersisted_external_response_hashes() -> None:
    documents = _evidence_documents()
    assert len(documents) == 9
    for document in documents:
        serialized = json.dumps(document, ensure_ascii=False)
        assert "raw_response_sha256" not in serialized
        corroboration = document["semantic_payload"]["root_checks"][
            "independent_source_corroboration"
        ]
        assert corroboration["classification"] == (
            "independent_public_provider_corroboration"
        )
        assert corroboration["independent_underlying_measurement"] is False


def test_canonical_repository_bundle_has_no_effective_anomaly_blockers() -> None:
    result = validator.validate_bundle(ROOT, require_effective_nonblocking=True)
    assert result.errors == []
    assert result.effective_blockers == []
    assert len(result.rows) == 9


def _document_for_stock(stock_id: str) -> dict[str, object]:
    return next(
        document
        for document in _evidence_documents()
        if document["semantic_payload"]["identity"]["stock_id"] == stock_id
    )


def test_2478_uses_independent_public_provider_not_twse_as_corroboration() -> None:
    document = _document_for_stock("2478")
    corroboration = document["semantic_payload"]["root_checks"][
        "independent_source_corroboration"
    ]
    assert corroboration["classification"] == (
        "independent_public_provider_corroboration"
    )
    assert corroboration["independent_underlying_measurement"] is False
    assert corroboration["sources"] == [
        "https://goodinfo.tw/tw/ShowK_Chart.asp?CHT_CAT=DATE&STOCK_ID=2478"
    ]
    assert len(corroboration["observed_facts"]) == 2
    assert not any("twse.com.tw" in source for source in corroboration["sources"])


@pytest.mark.parametrize(
    ("stock_id", "field", "bad_value", "error_fragment"),
    (
        (
            "2408",
            "provider_reported_monthly_revenue_thousand_twd",
            "1",
            "does not match canonical row",
        ),
        (
            "2478",
            "provider_reported_close",
            "1",
            "does not match registered row",
        ),
    ),
)
def test_independent_corroboration_observed_fact_tamper_fails(
    stock_id: str,
    field: str,
    bad_value: str,
    error_fragment: str,
) -> None:
    document = copy.deepcopy(_document_for_stock(stock_id))
    corroboration = document["semantic_payload"]["root_checks"][
        "independent_source_corroboration"
    ]
    corroboration["observed_facts"][0][field] = bad_value
    case = next(case for case in validator.EXPECTED_CASES.values() if case.stock_id == stock_id)
    errors = validator._validate_independent_corroboration(
        ROOT,
        case,
        corroboration,
    )
    assert any(error_fragment in error for error in errors)


def test_independent_corroboration_missing_facts_fails() -> None:
    document = copy.deepcopy(_document_for_stock("6177"))
    corroboration = document["semantic_payload"]["root_checks"][
        "independent_source_corroboration"
    ]
    corroboration["observed_facts"] = []
    case = next(case for case in validator.EXPECTED_CASES.values() if case.stock_id == "6177")
    errors = validator._validate_independent_corroboration(ROOT, case, corroboration)
    assert any("corroboration facts missing" in error for error in errors)


def test_repair_closure_raw_diagnostics_do_not_change_semantic_dependency() -> None:
    original = (ROOT / validator.REPAIR_CLOSURE_PATH).read_bytes()
    raw_mutation = original.replace(
        b"4eba010d3afeb2b50f3b6e88a60fb699bfad9d34b1e991c0cc8b898775b1231f",
        b"0" * 64,
    )
    canonical_mutation = original.replace(
        b"1cb88da0fb389f1e4775c6ae2c05d1c4813d7c584e9e2fc0ba7183d4bf7e1e71",
        b"0" * 64,
    )
    semantic = lambda payload: validator.csv_bytes_semantic_sha256(
        payload,
        excluded_columns=validator.REPAIR_CLOSURE_PROVENANCE_COLUMNS,
        source_name="repair-closure",
    )
    assert semantic(raw_mutation) == semantic(original)
    assert semantic(canonical_mutation) != semantic(original)


def test_v3_artifact_semantic_hash_ignores_transport_but_binds_business() -> None:
    original = (
        b"generated_at,raw_source_sha256,operation_key,trigger_date\r\n"
        b"2026-08-29,a,key-1,20251204\r\n"
    )
    raw_mutation = (
        b"generated_at,raw_source_sha256,operation_key,trigger_date\n"
        b"2099-01-01,b,key-1,20251204\n"
    )
    business_mutation = raw_mutation.replace(b"20251204", b"20251205")
    semantic = lambda payload: validator.artifact_bytes_semantic_sha256(
        payload,
        source_name="probe.csv",
    )
    assert semantic(raw_mutation) == semantic(original)
    assert semantic(business_mutation) != semantic(original)


def test_full_v3_artifact_pin_catches_nonselected_row_mutation() -> None:
    original = (ROOT / validator.V3_CANDIDATE_SUMMARY_PATH).read_bytes()
    mutated = original.replace(
        b"research_only_pending_holdout_validation",
        b"research_only_pending_holdout_validatioX",
        1,
    )
    assert mutated != original
    assert validator.artifact_bytes_semantic_sha256(
        original,
        source_name="v3-summary",
    ) != validator.artifact_bytes_semantic_sha256(
        mutated,
        source_name="v3-summary-mutated",
    )


def test_immutable_v2_reader_disables_git_replace_objects(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[list[str]] = []

    def fake_run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append(command)
        if "rev-parse" in command:
            return subprocess.CompletedProcess(command, 0, validator.V2_CANDIDATE_BASELINE_COMMIT.encode() + b"\n", b"")
        if "merge-base" in command:
            return subprocess.CompletedProcess(command, 0, b"", b"")
        return subprocess.CompletedProcess(command, 0, b"payload", b"")

    monkeypatch.setattr(validator.subprocess, "run", fake_run)
    assert validator._read_git_blob(
        ROOT,
        commit_sha=validator.V2_CANDIDATE_BASELINE_COMMIT,
        logical_path=validator.V2_CANDIDATE_SUMMARY_PATH,
    ) == b"payload"
    assert calls
    assert all("--no-replace-objects" in command for command in calls)


def test_price_row_canonical_hash_tamper_fails_replay() -> None:
    document = copy.deepcopy(_document_for_stock("2408"))
    replay = document["semantic_payload"]["root_checks"]["formal_operation_replay"]
    replay["price_row_canonical_sha256s"]["entry_open"] = "0" * 64
    case = next(case for case in validator.EXPECTED_CASES.values() if case.stock_id == "2408")

    errors = validator._validate_price_replay(ROOT, case, replay)

    assert any("entry_open canonical price-row SHA drifted" in error for error in errors)


def test_6177_future_source_cannot_be_backdated_into_trigger_asof() -> None:
    document = copy.deepcopy(_document_for_stock("6177"))
    lineage = document["semantic_payload"]["root_checks"]["raw_source_lineage"]
    future_event = next(
        event for event in lineage["monthly_revenue_events"] if event["period"] == "202512"
    )
    future_event["available_date"] = "20251204"
    case = validator.EXPECTED_CASES[validator.REPAIR_OPERATION_KEY]
    diagnostics: list[str] = []

    errors = validator._validate_monthly_lineage(ROOT, case, lineage, diagnostics)

    assert any("event identity drifted" in error for error in errors)
    assert any("trade-aligned available date drifted" in error for error in errors)


def test_immutable_v2_baseline_must_be_ancestor(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        if "rev-parse" in command:
            return subprocess.CompletedProcess(
                command,
                0,
                validator.V2_CANDIDATE_BASELINE_COMMIT.encode() + b"\n",
                b"",
            )
        return subprocess.CompletedProcess(command, 1, b"", b"not ancestor")

    monkeypatch.setattr(validator.subprocess, "run", fake_run)
    with pytest.raises(ValueError, match="not an ancestor"):
        validator._read_git_blob(
            ROOT,
            commit_sha=validator.V2_CANDIDATE_BASELINE_COMMIT,
            logical_path=validator.V2_CANDIDATE_SUMMARY_PATH,
        )
