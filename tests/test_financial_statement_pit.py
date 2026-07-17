from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Callable

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_financial_statement_pit import (  # noqa: E402
    APPROVED_HISTORICAL_SOURCE_VERIFIERS,
    HISTORY_COLUMNS,
    HISTORICAL_PROOF_MANIFEST_VERSION,
    HISTORICAL_REVISION_NORMALIZATION_ENABLED,
    MANIFEST_VERSION,
    ApprovedHistoricalSourceVerifier,
    ParsedHistoricalRevisionPayload,
    ParsedOfficialLineageEvidence,
    ParsedOfficialLineageRevision,
    REVISION_LINEAGE_COMPLETE,
    REVISION_LINEAGE_NO_PRIOR,
    REVISION_LINEAGE_PROOF_SCHEMA,
    SourceCapture,
    assign_revision_lineage,
    build_and_write,
    build_coverage,
    captures_from_manifest,
    load_metric_mapping,
    load_source_registry,
    normalize_capture,
)
from validate_financial_statement_pit import (  # noqa: E402
    _read_rows,
    validate,
    validate_historical_revision_normalization_gate,
    validate_historical_source_verifier_registry,
    validate_history,
    validate_manifest,
    validate_source_registry,
)


def payload_bytes(row: dict[str, str]) -> bytes:
    return json.dumps([row], ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def capture(
    source_id: str,
    row: dict[str, str],
    *,
    observed_at: str = "2026-07-16T10:00:00+08:00",
    source_available_at: str = "2026-07-16T10:00:00+08:00",
    availability_precision: str = "first_observed_at",
    statement_scope: str = "official_endpoint_reported_scope",
    historical_pit_eligible: bool = False,
    historical_source_fixture: bool = False,
) -> SourceCapture:
    payload = payload_bytes(row)
    source = load_source_registry()[source_id].copy()
    if historical_source_fixture:
        source.update(
            {
                "source_id": "mops_historical_fixture",
                "source_kind": "official_mops_xbrl_historical_filing",
                "source_url": "https://mops.twse.com.tw/mops/",
                "history_mode": "historical_point_in_time",
                "availability_semantics": "exact_company_filing_availability",
                "revision_lineage_semantics": (
                    "official_immutable_revision_payload_lineage_or_"
                    "authoritative_no_prior_revision_proof"
                ),
            }
        )
    return SourceCapture(
        source=source,
        payload=payload,
        observed_at=observed_at,
        source_available_at=source_available_at,
        availability_precision=availability_precision,
        statement_scope=statement_scope,
        period_basis="cumulative_ytd",
        raw_archive_ref=f"sha256://{hashlib.sha256(payload).hexdigest()}",
        archive_status="external_content_addressed_archive_verified",
        declared_historical_pit_eligible=historical_pit_eligible,
    )


def general_row(*, net_income: str = "150") -> dict[str, str]:
    return {
        "出表日期": "1150715",
        "年度": "115",
        "季別": "1",
        "公司代號": "2330",
        "公司名稱": "台積電",
        "營業收入": "1,000",
        "營業成本": "600",
        "營業毛利（毛損）淨額": "400",
        "營業費用": "180",
        "營業利益（損失）": "220",
        "營業外收入及支出": "20",
        "稅前淨利（淨損）": "240",
        "所得稅費用（利益）": "90",
        "本期淨利（淨損）": net_income,
        "淨利（淨損）歸屬於母公司業主": net_income,
        "基本每股盈餘（元）": "5.79",
    }


def normalize(one_capture: SourceCapture) -> tuple[pd.DataFrame, dict[str, object]]:
    aliases, required = load_metric_mapping()
    return normalize_capture(one_capture, aliases, required)


def parse_test_revision_payload(payload: bytes) -> ParsedHistoricalRevisionPayload:
    decoded = json.loads(payload.decode("utf-8"))
    if not isinstance(decoded, list) or not decoded:
        raise ValueError("test revision payload must contain rows")
    identities: set[tuple[str, str, str, str]] = set()
    for row in decoded:
        if not isinstance(row, dict):
            raise ValueError("test revision payload row must be an object")
        year = int(str(row["年度"]))
        if year < 1911:
            year += 1911
        identities.add(
            (
                str(row["公司代號"]),
                f"{year}Q{int(str(row['季別']))}",
                str(row["StatementScope"]),
                str(row["TaxonomyVersion"]),
            )
        )
    if len(identities) != 1:
        raise ValueError("test revision payload must identify one company/period/scope/taxonomy")
    company_id, fiscal_period, statement_scope, taxonomy_version = next(iter(identities))
    return ParsedHistoricalRevisionPayload(
        company_id=company_id,
        fiscal_period=fiscal_period,
        statement_scope=statement_scope,
        taxonomy_version=taxonomy_version,
    )


def parse_test_official_evidence(payload: bytes) -> ParsedOfficialLineageEvidence:
    try:
        decoded = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("test source official evidence contract mismatch") from exc
    expected_keys = {
        "schema_version",
        "source_id",
        "source_url",
        "official_evidence_url",
        "company_id",
        "fiscal_period",
        "statement_scope",
        "taxonomy_version",
        "assertion_type",
        "asserted_complete",
        "no_prior_revision_asserted",
        "official_assertion_id",
        "revisions",
    }
    if (
        not isinstance(decoded, dict)
        or set(decoded) != expected_keys
        or decoded["schema_version"] != "test_mops_lineage_evidence_v1"
        or not isinstance(decoded["revisions"], list)
    ):
        raise ValueError("test source official evidence contract mismatch")
    parsed_revisions: list[ParsedOfficialLineageRevision] = []
    for revision in decoded["revisions"]:
        if not isinstance(revision, dict) or set(revision) != {
            "revision_id",
            "supersedes_revision_id",
            "source_available_at",
            "payload_sha256",
        }:
            raise ValueError("test source official evidence revision contract mismatch")
        parsed_revisions.append(
            ParsedOfficialLineageRevision(
                revision_id=revision["revision_id"],
                supersedes_revision_id=revision["supersedes_revision_id"],
                source_available_at=revision["source_available_at"],
                payload_sha256=revision["payload_sha256"],
            )
        )
    return ParsedOfficialLineageEvidence(
        source_id=decoded["source_id"],
        source_url=decoded["source_url"],
        official_evidence_url=decoded["official_evidence_url"],
        company_id=decoded["company_id"],
        fiscal_period=decoded["fiscal_period"],
        statement_scope=decoded["statement_scope"],
        taxonomy_version=decoded["taxonomy_version"],
        assertion_type=decoded["assertion_type"],
        asserted_complete=decoded["asserted_complete"],
        no_prior_revision_asserted=decoded["no_prior_revision_asserted"],
        official_assertion_id=decoded["official_assertion_id"],
        revisions=tuple(parsed_revisions),
    )


def install_test_historical_verifier(
    monkeypatch: pytest.MonkeyPatch,
    source: dict[str, str],
) -> None:
    monkeypatch.setitem(
        APPROVED_HISTORICAL_SOURCE_VERIFIERS,
        source["source_id"],
        ApprovedHistoricalSourceVerifier(
            official_source_url=source["source_url"],
            parse_revision_payload=parse_test_revision_payload,
            parse_official_lineage_evidence=parse_test_official_evidence,
        ),
    )


def historical_manifest_fixture(
    tmp_path: Path,
    *,
    assertion_type: str = "complete_revision_history",
    proof_mutator: Callable[[dict[str, Any]], None] | None = None,
    proof_bytes: bytes | None = None,
    official_evidence_bytes: bytes | None = None,
    official_evidence_mutator: Callable[[dict[str, Any]], None] | None = None,
    source_url_override: str | None = None,
) -> tuple[Path, dict[str, str]]:
    source = capture(
        "twse_general",
        general_row(),
        historical_source_fixture=True,
    ).source
    if source_url_override is not None:
        source["source_url"] = source_url_override
    first_row = general_row(net_income="140")
    latest_row = general_row(net_income="150")
    for row in (first_row, latest_row):
        row["StatementScope"] = "consolidated"
        row["TaxonomyVersion"] = "tifrs-2025"
    first_payload = payload_bytes(first_row)
    latest_payload = payload_bytes(latest_row)
    first_path = tmp_path / "filing-v1.json"
    latest_path = tmp_path / "filing-v2.json"
    first_path.write_bytes(first_payload)
    latest_path.write_bytes(latest_payload)
    first_sha = hashlib.sha256(first_payload).hexdigest()
    latest_sha = hashlib.sha256(latest_payload).hexdigest()

    evidence_url = f"{source['source_url']}revision-completeness/2330/2026Q1"
    no_prior = assertion_type == "authoritative_no_prior_revision"
    evidence_revisions: list[dict[str, Any]] = [
        {
            "revision_id": "filing-v1",
            "supersedes_revision_id": None,
            "source_available_at": "2026-05-01T14:31:22+08:00",
            "payload_sha256": first_sha,
        },
        {
            "revision_id": "filing-v2",
            "supersedes_revision_id": "filing-v1",
            "source_available_at": "2026-05-15T14:31:22+08:00",
            "payload_sha256": latest_sha,
        },
    ]
    if no_prior:
        evidence_revisions = [
            evidence_revisions[-1] | {"supersedes_revision_id": None}
        ]
    if official_evidence_bytes is None:
        evidence_document: dict[str, Any] = {
            "schema_version": "test_mops_lineage_evidence_v1",
            "source_id": source["source_id"],
            "source_url": source["source_url"],
            "official_evidence_url": evidence_url,
            "company_id": "2330",
            "fiscal_period": "2026Q1",
            "statement_scope": "consolidated",
            "taxonomy_version": "tifrs-2025",
            "assertion_type": assertion_type,
            "asserted_complete": True,
            "no_prior_revision_asserted": no_prior,
            "official_assertion_id": "official-assertion-2026Q1-2330",
            "revisions": evidence_revisions,
        }
        if official_evidence_mutator is not None:
            official_evidence_mutator(evidence_document)
        official_evidence_bytes = json.dumps(
            evidence_document,
            separators=(",", ":"),
        ).encode("utf-8")
    official_evidence_path = tmp_path / "official-completeness-evidence.bin"
    official_evidence_path.write_bytes(official_evidence_bytes)
    official_evidence_sha = hashlib.sha256(official_evidence_bytes).hexdigest()
    revisions: list[dict[str, Any]] = [
        {
            "revision_id": "filing-v1",
            "supersedes_revision_id": None,
            "source_available_at": "2026-05-01T14:31:22+08:00",
            "payload": {
                "local_path": str(first_path),
                "sha256": first_sha,
                "byte_count": len(first_payload),
            },
        },
        {
            "revision_id": "filing-v2",
            "supersedes_revision_id": "filing-v1",
            "source_available_at": "2026-05-15T14:31:22+08:00",
            "payload": {
                "local_path": str(latest_path),
                "sha256": latest_sha,
                "byte_count": len(latest_payload),
            },
        },
    ]
    if no_prior:
        revisions = [revisions[-1] | {"supersedes_revision_id": None}]
    proof: dict[str, Any] = {
        "schema_version": REVISION_LINEAGE_PROOF_SCHEMA,
        "official_source": {
            "source_id": source["source_id"],
            "source_url": source["source_url"],
        },
        "company": {"stock_id": "2330"},
        "fiscal_period": "2026Q1",
        "statement_scope": "consolidated",
        "taxonomy_version": "tifrs-2025",
        "lineage_assertion": {
            "assertion_type": assertion_type,
            "asserted_complete": True,
            "no_prior_revision_asserted": no_prior,
            "official_assertion_id": "official-assertion-2026Q1-2330",
            "official_evidence": {
                "official_url": evidence_url,
                "local_path": str(official_evidence_path),
                "sha256": official_evidence_sha,
                "byte_count": len(official_evidence_bytes),
            },
        },
        "revisions": revisions,
    }
    if proof_mutator is not None:
        proof_mutator(proof)
    serialized_proof = (
        proof_bytes
        if proof_bytes is not None
        else json.dumps(proof, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    )
    proof_path = tmp_path / "revision-lineage-proof-v1.json"
    proof_path.write_bytes(serialized_proof)
    proof_sha = hashlib.sha256(serialized_proof).hexdigest()

    manifest_path = tmp_path / "capture-manifest.csv"
    pd.DataFrame(
        [
            {
                "source_id": source["source_id"],
                "local_raw_path": str(latest_path),
                "observed_at": "2026-05-16T10:00:00+08:00",
                "source_available_at": "2026-05-15T14:31:22+08:00",
                "availability_precision": "exact_company_filing_timestamp",
                "statement_scope": "consolidated",
                "period_basis": "cumulative_ytd",
                "raw_archive_ref": f"sha256://{latest_sha}",
                "archive_status": "external_content_addressed_archive_verified",
                "expected_sha256": latest_sha,
                "historical_pit_eligible": "True",
                "revision_lineage_proof_local_path": str(proof_path),
                "revision_lineage_proof_expected_sha256": proof_sha,
            }
        ]
    ).to_csv(manifest_path, index=False)
    return manifest_path, source


def synthetic_historical_validator_artifacts(
    *,
    proof_revision_count: int,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, str]]:
    history, manifest_row = normalize(capture("twse_general", general_row()))
    history = assign_revision_lineage(history)
    raw_sha = str(history.iloc[0]["raw_payload_sha256"])
    status = (
        REVISION_LINEAGE_NO_PRIOR
        if proof_revision_count == 1
        else REVISION_LINEAGE_COMPLETE
    )
    metadata_fields = (
        ("revision_lineage_proof_schema", REVISION_LINEAGE_PROOF_SCHEMA),
        ("revision_lineage_status", status),
        ("revision_lineage_proof_ref", f"sha256://{'a' * 64}"),
        ("revision_lineage_official_evidence_ref", f"sha256://{'b' * 64}"),
        ("revision_lineage_revision_count", str(proof_revision_count)),
        ("revision_lineage_latest_payload_sha256", raw_sha),
        ("revision_lineage_company_id", "2330"),
        ("revision_lineage_fiscal_period", "2026Q1"),
        ("revision_lineage_statement_scope", "consolidated"),
        ("revision_lineage_taxonomy_version", "tifrs-2025"),
        ("revision_lineage_latest_revision_id", f"filing-v{proof_revision_count}"),
    )

    def metadata(base: str) -> str:
        return ";".join([base, *(f"{key}={value}" for key, value in metadata_fields)])

    history.loc[0, "source_kind"] = "official_mops_xbrl_historical_filing"
    history.loc[0, "source_available_at"] = "2026-05-15T14:31:22+08:00"
    history.loc[0, "availability_precision"] = "exact_company_filing_timestamp"
    history.loc[0, "pit_status"] = (
        "historical_pit_exact_company_filing_and_revision_lineage_verified"
    )
    history.loc[0, "historical_pit_eligible"] = "True"
    history.loc[0, "statement_scope"] = "consolidated"
    history.loc[0, "provenance_status"] = metadata(
        "raw_payload_sha_and_source_row_sha_verified"
    )

    manifest_row["manifest_version"] = HISTORICAL_PROOF_MANIFEST_VERSION
    manifest_row["source_kind"] = "official_mops_xbrl_historical_filing"
    manifest_row["source_available_at"] = "2026-05-15T14:31:22+08:00"
    manifest_row["availability_precision"] = "exact_company_filing_timestamp"
    manifest_row["statement_scope"] = "consolidated"
    manifest_row["archive_status"] = metadata(
        "external_content_addressed_archive_verified"
    )
    manifest_row["historical_pit_eligible"] = "True"
    manifest_row["current_snapshot_only"] = "False"
    manifest = pd.DataFrame([manifest_row])
    source_semantics = {
        "twse_general": (
            "official_immutable_revision_payload_lineage_or_"
            "authoritative_no_prior_revision_proof"
        )
    }
    return history, manifest, source_semantics


def test_general_schema_builds_objective_metrics_and_cumulative_margins() -> None:
    history, manifest = normalize(capture("twse_general", general_row()))

    assert len(history) == 1
    row = history.iloc[0]
    assert row["fiscal_period"] == "2026Q1"
    assert row["source_table_date"] == "2026-07-15"
    assert row["operating_revenue"] == "1000"
    assert row["non_operating_income_expense"] == "20"
    assert row["basic_eps"] == "5.79"
    assert row["gross_margin_pct"] == "40.0000"
    assert row["operating_margin_pct"] == "22.0000"
    assert row["net_margin_pct"] == "15.0000"
    assert row["period_basis"] == "cumulative_ytd"
    assert row["pit_status"] == "current_snapshot_first_observed_only"
    assert row["historical_pit_eligible"] == "False"
    assert row["allowed_for_formal_model_use"] == "False"
    assert row["numerical_anomaly_candidate"] == "False"
    assert row["primary_metric_retained"] == "True"
    assert manifest["availability_precision"] == "first_observed_at"
    assert manifest["manifest_version"] == MANIFEST_VERSION
    assert MANIFEST_VERSION == "financial_statement_source_manifest_v1"
    assert manifest["normalized_row_count"] == 1
    assert manifest["dropped_invalid_identity_row_count"] == 0


def test_tpex_english_identity_fields_are_not_silently_dropped() -> None:
    row = general_row()
    row["Date"] = row.pop("出表日期")
    row["Year"] = row.pop("年度")
    row["Season"] = row.pop("季別")
    row["SecuritiesCompanyCode"] = row.pop("公司代號")
    row["CompanyName"] = row.pop("公司名稱")

    history, manifest = normalize(capture("tpex_general", row))

    assert len(history) == 1
    assert history.iloc[0]["stock_id"] == "2330"
    assert manifest["normalized_row_count"] == 1
    assert manifest["dropped_invalid_identity_row_count"] == 0


def test_banking_schema_never_inherits_general_margin_formulas() -> None:
    banking = {
        "出表日期": "1150715",
        "年度": "115",
        "季別": "1",
        "公司代號": "2882",
        "公司名稱": "國泰金",
        "淨收益": "1000",
        "營業費用": "500",
        "本期淨利（淨損）": "300",
        "基本每股盈餘（元）": "2.1",
    }
    history, _manifest = normalize(capture("twse_banking", banking))
    row = history.iloc[0]

    assert row["operating_revenue"] == "1000"
    assert row["net_income"] == "300"
    assert row["gross_margin_pct"] == ""
    assert row["operating_margin_pct"] == ""
    assert row["net_margin_pct"] == ""
    assert row["margin_derivation_status"] == "not_applicable_non_general_schema"


def test_revision_history_preserves_both_versions_and_links_lineage() -> None:
    first, _ = normalize(
        capture(
            "twse_general",
            general_row(net_income="150"),
            observed_at="2026-05-15T10:00:00+08:00",
            source_available_at="2026-05-15T10:00:00+08:00",
        )
    )
    revised, _ = normalize(
        capture(
            "twse_general",
            general_row(net_income="145"),
            observed_at="2026-06-20T10:00:00+08:00",
            source_available_at="2026-06-20T10:00:00+08:00",
        )
    )

    history = assign_revision_lineage(pd.concat([first, revised], ignore_index=True))

    assert len(history) == 2
    assert list(history["revision_number"]) == ["1", "2"]
    assert set(history["revision_count"]) == {"2"}
    assert history.iloc[1]["supersedes_revision_id"] == history.iloc[0]["revision_id"]
    assert list(history["is_latest_known_revision"]) == ["False", "True"]
    assert list(history["net_income"]) == ["150", "145"]


def test_global_table_date_change_does_not_create_false_financial_revision() -> None:
    first_row = general_row()
    second_row = general_row()
    second_row["出表日期"] = "1150716"
    first, _ = normalize(capture("twse_general", first_row))
    second, _ = normalize(
        capture(
            "twse_general",
            second_row,
            observed_at="2026-07-17T10:00:00+08:00",
            source_available_at="2026-07-17T10:00:00+08:00",
        )
    )

    history = assign_revision_lineage(pd.concat([first, second], ignore_index=True))

    assert len(history) == 1
    assert history.iloc[0]["revision_count"] == "1"


def test_current_snapshot_source_cannot_self_declare_historical_pit() -> None:
    with pytest.raises(ValueError, match="registry-owned historical source"):
        normalize(
            capture(
                "twse_general",
                general_row(),
                source_available_at="2026-05-15T14:31:22+08:00",
                availability_precision="exact_company_filing_timestamp",
                statement_scope="consolidated",
                historical_pit_eligible=True,
            )
        )


def test_exact_filed_at_without_revision_lineage_is_rejected() -> None:
    with pytest.raises(ValueError, match="complete official immutable revision payload lineage"):
        normalize(
            capture(
                "twse_general",
                general_row(),
                observed_at="2026-05-16T10:00:00+08:00",
                source_available_at="2026-05-15T14:31:22+08:00",
                availability_precision="exact_company_filing_timestamp",
                statement_scope="consolidated",
                historical_pit_eligible=True,
                historical_source_fixture=True,
            )
        )


def test_exact_filed_at_without_eligibility_declaration_remains_ineligible() -> None:
    historical, _ = normalize(
        capture(
            "twse_general",
            general_row(),
            observed_at="2026-05-16T10:00:00+08:00",
            source_available_at="2026-05-15T14:31:22+08:00",
            availability_precision="exact_company_filing_timestamp",
            statement_scope="consolidated",
            historical_pit_eligible=False,
            historical_source_fixture=True,
        )
    )

    assert historical.iloc[0]["historical_pit_eligible"] == "False"
    assert historical.iloc[0]["pit_status"] == "blocked_incomplete_filing_or_revision_lineage"
    assert historical.iloc[0]["allowed_for_formal_model_use"] == "False"


@pytest.mark.parametrize(
    ("assertion_type", "expected_status", "expected_revision_count"),
    [
        ("complete_revision_history", REVISION_LINEAGE_COMPLETE, 2),
        ("authoritative_no_prior_revision", REVISION_LINEAGE_NO_PRIOR, 1),
    ],
)
def test_valid_fixed_revision_lineage_proofs_are_derived_and_formal_use_remains_blocked(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    assertion_type: str,
    expected_status: str,
    expected_revision_count: int,
) -> None:
    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        assertion_type=assertion_type,
    )
    install_test_historical_verifier(monkeypatch, source)
    captures = captures_from_manifest(manifest_path, {source["source_id"]: source})
    assert len(captures) == 1
    assert captures[0].revision_lineage_status == expected_status
    assert captures[0].revision_lineage_revision_count == expected_revision_count
    assert captures[0].revision_lineage_evidence_verified is True
    assert HISTORICAL_REVISION_NORMALIZATION_ENABLED is False
    assert HISTORICAL_PROOF_MANIFEST_VERSION == "financial_statement_source_manifest_v2"
    with pytest.raises(ValueError, match="per-revision normalization is not implemented"):
        normalize(captures[0])


def test_single_byte_revision_lineage_proof_is_rejected(tmp_path: Path) -> None:
    manifest_path, source = historical_manifest_fixture(tmp_path, proof_bytes=b"x")

    with pytest.raises(ValueError, match="valid JSON using the fixed v1 schema"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


@pytest.mark.parametrize(
    "assertion_type",
    ["complete_revision_history", "authoritative_no_prior_revision"],
)
def test_production_without_source_specific_verifier_fails_closed(
    tmp_path: Path,
    assertion_type: str,
) -> None:
    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        assertion_type=assertion_type,
    )

    assert APPROVED_HISTORICAL_SOURCE_VERIFIERS == {}
    with pytest.raises(ValueError, match="has no approved source-specific verifier"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_fake_official_text_is_rejected_by_source_specific_evidence_parser(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        official_evidence_bytes=b"official complete no prior revisions",
    )
    install_test_historical_verifier(monkeypatch, source)

    with pytest.raises(ValueError, match="official evidence contract mismatch"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_wrong_old_revision_payload_identity_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def replace_old_payload_with_other_company(proof: dict[str, Any]) -> None:
        wrong_row = general_row(net_income="140")
        wrong_row["公司代號"] = "2317"
        wrong_row["StatementScope"] = "consolidated"
        wrong_row["TaxonomyVersion"] = "tifrs-2025"
        wrong_payload = payload_bytes(wrong_row)
        wrong_path = tmp_path / "wrong-company-old-revision.json"
        wrong_path.write_bytes(wrong_payload)
        proof["revisions"][0]["payload"] = {
            "local_path": str(wrong_path),
            "sha256": hashlib.sha256(wrong_payload).hexdigest(),
            "byte_count": len(wrong_payload),
        }

    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        proof_mutator=replace_old_payload_with_other_company,
    )
    install_test_historical_verifier(monkeypatch, source)

    with pytest.raises(ValueError, match=r"revisions\[0\] payload company"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_arbitrary_https_registered_url_is_not_an_approved_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        source_url_override="https://example.com/historical-financial-statements/",
    )
    monkeypatch.setitem(
        APPROVED_HISTORICAL_SOURCE_VERIFIERS,
        source["source_id"],
        ApprovedHistoricalSourceVerifier(
            official_source_url=source["source_url"],
            parse_revision_payload=parse_test_revision_payload,
            parse_official_lineage_evidence=parse_test_official_evidence,
        ),
    )

    with pytest.raises(ValueError, match="exact TWSE/TPEx allowlist"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_production_verifier_registry_is_empty_and_independently_validated() -> None:
    assert APPROVED_HISTORICAL_SOURCE_VERIFIERS == {}
    assert validate_historical_source_verifier_registry() == []
    assert HISTORICAL_REVISION_NORMALIZATION_ENABLED is False
    assert validate_historical_revision_normalization_gate() == []


def test_validator_rejects_arbitrary_https_source_registry_host() -> None:
    source_rows = _read_rows(
        ROOT / "config" / "daily_model_financial_statement_pit_sources.csv"
    )
    source_rows[0]["source_url"] = "https://example.com/financial-statements"

    errors = validate_source_registry(source_rows)

    assert any("source_url is not an approved official host" in error for error in errors)


def test_revision_lineage_proof_latest_must_be_current_capture_raw(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def use_old_payload_as_latest(proof: dict[str, Any]) -> None:
        unrelated_row = general_row(net_income="145")
        unrelated_row["StatementScope"] = "consolidated"
        unrelated_row["TaxonomyVersion"] = "tifrs-2025"
        unrelated_payload = payload_bytes(unrelated_row)
        unrelated_path = tmp_path / "filing-not-current.json"
        unrelated_path.write_bytes(unrelated_payload)
        proof["revisions"][-1]["payload"] = {
            "local_path": str(unrelated_path),
            "sha256": hashlib.sha256(unrelated_payload).hexdigest(),
            "byte_count": len(unrelated_payload),
        }

    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        proof_mutator=use_old_payload_as_latest,
    )
    install_test_historical_verifier(monkeypatch, source)

    with pytest.raises(ValueError, match="latest payload SHA does not match"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


@pytest.mark.parametrize(
    ("field", "bad_value", "error_text"),
    [
        ("company", {"stock_id": "2317"}, "payload company does not match proof"),
        ("fiscal_period", "2025Q4", "payload fiscal period does not match proof"),
        ("statement_scope", "individual", "statement_scope does not match capture manifest"),
    ],
)
def test_revision_lineage_proof_identity_and_scope_must_match_capture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    bad_value: object,
    error_text: str,
) -> None:
    def mutate(proof: dict[str, Any]) -> None:
        proof[field] = bad_value

    manifest_path, source = historical_manifest_fixture(tmp_path, proof_mutator=mutate)
    install_test_historical_verifier(monkeypatch, source)

    with pytest.raises(ValueError, match=error_text):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_false_no_prior_assertion_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def clear_no_prior_assertion(proof: dict[str, Any]) -> None:
        proof["lineage_assertion"]["no_prior_revision_asserted"] = False

    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        assertion_type="authoritative_no_prior_revision",
        proof_mutator=clear_no_prior_assertion,
    )
    install_test_historical_verifier(monkeypatch, source)

    with pytest.raises(ValueError, match="requires exactly one revision and a true no-prior"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_bad_revision_supersedes_chain_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def break_chain(proof: dict[str, Any]) -> None:
        proof["revisions"][1]["supersedes_revision_id"] = "unrelated-revision"

    manifest_path, source = historical_manifest_fixture(tmp_path, proof_mutator=break_chain)
    install_test_historical_verifier(monkeypatch, source)

    with pytest.raises(ValueError, match="supersedes chain is invalid"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_official_completeness_evidence_bytes_and_sha_must_match(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def forge_evidence_sha(proof: dict[str, Any]) -> None:
        proof["lineage_assertion"]["official_evidence"]["sha256"] = "0" * 64

    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        proof_mutator=forge_evidence_sha,
    )
    install_test_historical_verifier(monkeypatch, source)

    with pytest.raises(ValueError, match="official_evidence SHA-256 mismatch"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


@pytest.mark.parametrize(
    ("field", "forged_value"),
    [
        ("payload_sha256", "0" * 64),
        ("source_available_at", "2026-04-30T14:31:22+08:00"),
        ("supersedes_revision_id", "forged-prior-revision"),
    ],
)
def test_official_evidence_revision_lineage_must_exactly_match_proof(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    forged_value: str,
) -> None:
    def forge_old_revision(evidence: dict[str, Any]) -> None:
        evidence["revisions"][0][field] = forged_value

    manifest_path, source = historical_manifest_fixture(
        tmp_path,
        official_evidence_mutator=forge_old_revision,
    )
    install_test_historical_verifier(monkeypatch, source)

    with pytest.raises(
        ValueError,
        match="official completeness/no-prior evidence does not match the proof",
    ):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_capture_manifest_cannot_self_declare_revision_lineage_status(
    tmp_path: Path,
) -> None:
    manifest_path, source = historical_manifest_fixture(tmp_path)
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest["revision_lineage_status"] = REVISION_LINEAGE_COMPLETE
    manifest.to_csv(manifest_path, index=False)

    with pytest.raises(ValueError, match="must not self-declare revision-lineage status"):
        captures_from_manifest(manifest_path, {source["source_id"]: source})


def test_validator_rejects_revision_metadata_cross_artifact_drift(
) -> None:
    historical, manifest, source_semantics = synthetic_historical_validator_artifacts(
        proof_revision_count=1
    )
    historical.loc[0, "provenance_status"] = historical.loc[
        0, "provenance_status"
    ].replace("revision_lineage_company_id=2330", "revision_lineage_company_id=2317")

    errors = validate_history(
        historical.astype(str),
        manifest.astype(str),
        {"twse_general"},
        source_semantics,
    )

    assert any("proof company differs from history row" in error for error in errors)
    assert any("proof metadata disagree" in error for error in errors)


def test_validator_rejects_proof_revision_count_exceeding_normalized_lineage() -> None:
    historical, manifest, source_semantics = synthetic_historical_validator_artifacts(
        proof_revision_count=2
    )

    errors = validate_history(
        historical.astype(str),
        manifest.astype(str),
        {"twse_general"},
        source_semantics,
    )

    assert any(
        "proof revision count does not match normalized group lineage count" in error
        and "proof=2 normalized=1" in error
        for error in errors
    )


def test_current_snapshot_capture_manifest_keeps_base_schema_compatible(
    tmp_path: Path,
) -> None:
    raw_payload = payload_bytes(general_row())
    raw_path = tmp_path / "current.json"
    raw_path.write_bytes(raw_payload)
    raw_sha = hashlib.sha256(raw_payload).hexdigest()
    manifest_path = tmp_path / "current-capture-manifest.csv"
    pd.DataFrame(
        [
            {
                "source_id": "twse_general",
                "local_raw_path": str(raw_path),
                "observed_at": "2026-05-16T10:00:00+08:00",
                "source_available_at": "2026-05-16T10:00:00+08:00",
                "availability_precision": "first_observed_at",
                "statement_scope": "official_endpoint_reported_scope",
                "period_basis": "cumulative_ytd",
                "raw_archive_ref": f"sha256://{raw_sha}",
                "archive_status": "external_content_addressed_archive_verified",
                "expected_sha256": raw_sha,
                "historical_pit_eligible": "False",
            }
        ]
    ).to_csv(manifest_path, index=False)

    captures = captures_from_manifest(manifest_path, load_source_registry())

    assert len(captures) == 1
    assert captures[0].declared_historical_pit_eligible is False
    assert captures[0].revision_lineage_status == "not_available"
    assert captures[0].revision_lineage_proof_ref == ""
    assert captures[0].revision_lineage_evidence_verified is False


def test_validator_keeps_existing_v1_current_snapshot_manifest_compatible() -> None:
    _history, manifest_row = normalize(capture("twse_general", general_row()))
    manifest_row["manifest_version"] = "financial_statement_source_manifest_v1"

    assert validate_manifest(
        pd.DataFrame([manifest_row]).astype(str),
        set(load_source_registry()),
    ) == []


def test_validator_rejects_v2_on_current_snapshot_manifest() -> None:
    _history, manifest_row = normalize(capture("twse_general", general_row()))
    manifest_row["manifest_version"] = HISTORICAL_PROOF_MANIFEST_VERSION

    errors = validate_manifest(
        pd.DataFrame([manifest_row]).astype(str),
        set(load_source_registry()),
    )

    assert errors == ["manifest row 2: ineligible or current-snapshot rows must remain manifest v1"]


def test_numerical_extremes_are_unresolved_candidates_and_remain_primary() -> None:
    extreme = general_row(net_income="-107754")
    extreme["公司代號"] = "6919"
    extreme["營業收入"] = "2"
    extreme["營業成本"] = "1"
    extreme["營業毛利（毛損）淨額"] = "1"
    extreme["營業費用"] = "245832"
    extreme["營業利益（損失）"] = "-245831"
    extreme["基本每股盈餘（元）"] = "-0.07"
    history, _manifest = normalize(capture("twse_general", extreme))
    row = history.iloc[0]

    assert row["operating_margin_pct"] == "-12291550.0000"
    assert row["numerical_anomaly_candidate"] == "True"
    assert "operating_margin_abs_ge_500pct" in row["numerical_anomaly_triggers"]
    assert row["anomaly_disposition"] == "unresolved_anomaly_candidate"
    assert row["primary_metric_retained"] == "True"
    assert row["anomaly_evidence_status"].endswith("independent_corroboration_pending")


def test_validator_rejects_table_date_as_company_availability() -> None:
    history, manifest_row = normalize(capture("twse_general", general_row()))
    history = assign_revision_lineage(history)
    manifest = pd.DataFrame([manifest_row])
    history.loc[0, "availability_precision"] = "official_table_date"

    errors = validate_history(
        history.astype(str),
        manifest.astype(str),
        set(load_source_registry()),
    )

    assert any("global table date cannot become company filing availability" in error for error in errors)


def test_producer_write_allowlist_does_not_touch_mature_model_artifacts(tmp_path: Path) -> None:
    sentinel = tmp_path / "output" / "latest" / "daily_w_bottom_right_side_operation_section_latest.csv"
    sentinel.parent.mkdir(parents=True)
    sentinel.write_text("sentinel\n", encoding="utf-8")
    before = sentinel.read_bytes()

    paths = build_and_write([capture("twse_general", general_row())], tmp_path)

    assert sentinel.read_bytes() == before
    assert len(paths) == 6
    assert all(path.exists() for path in paths.values())


def test_complete_fixture_passes_independent_validator() -> None:
    history, manifest_row = normalize(capture("twse_general", general_row()))
    history = assign_revision_lineage(history)
    manifest = pd.DataFrame([manifest_row])
    coverage = build_coverage(history, manifest)
    source_rows = _read_rows(ROOT / "config" / "daily_model_financial_statement_pit_sources.csv")
    mapping_rows = _read_rows(ROOT / "config" / "daily_model_financial_statement_metric_mapping.csv")

    assert validate(
        history.astype(str),
        manifest.astype(str),
        coverage.astype(str),
        source_rows,
        mapping_rows,
    ) == []
