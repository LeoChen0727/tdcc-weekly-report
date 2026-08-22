from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_daily_canonical_field_lineage as lineage  # noqa: E402
from daily_snapshot_revision_utils import snapshot_file_sha256  # noqa: E402


MIGRATION_ID = "volume_v2_warrant_canonical_field_lineage_20260718"
SCORE_RANK_MIGRATION_ID = "volume_v2_score_rank_canonical_field_lineage_20260718"
CONSUMER_HARDENING_MIGRATION_ID = "canonical_field_consumer_hardening_20260718"
CONSUMER_EXCLUSION_MIGRATION_ID = "canonical_field_consumer_exclusions_20260718"
RANKING_VALIDATOR_HISTORY_MIGRATION_ID = (
    "daily_published_ranking_validator_history_consumers_20260720"
)
SOURCE_IDENTITY_MIGRATION_ID = "volume_v2_candidate_projection_lineage_20260731"
FORMAL_OUTCOME_NUMERIC_MIGRATION_ID = (
    "volume_v2_formal_outcome_numeric_canonicalization_20260810"
)
PINNED_WATCH_LINEAGE_MIGRATION_ID = (
    "volume_v2_formal_current_pinned_watch_lineage_replay_20260815"
)
REPORT_SIGNAL_SCHEMA_CONSUMER_MIGRATION_ID = (
    "daily_pipeline_report_signal_schema_consumer_20260808"
)
RANKING_VALIDATOR_EXCLUSION_MIGRATION_ID = (
    "daily_published_ranking_validator_current_hash_exclusions_20260720"
)
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


def source_identity_fixture(
    root: Path,
    *,
    artifact: str,
    producer: str,
    stock_id: str = "2451",
) -> dict[str, str]:
    source_path = root / artifact
    write_csv(source_path, ["stock_id"], [{"stock_id": stock_id}])
    artifact_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    row_sha256 = hashlib.sha256(
        json.dumps(
            [["stock_id", stock_id]],
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    return {
        "stock_id": stock_id,
        "candidate_source_raw_stock_id": stock_id,
        "candidate_source_normalized_stock_id": stock_id,
        "candidate_source_identity_columns": "stock_id",
        "candidate_source_artifact": artifact,
        "candidate_source_producer": producer,
        "candidate_source_artifact_sha256": artifact_sha256,
        "candidate_source_record_number": "2",
        "candidate_source_row_sha256": row_sha256,
        "candidate_source_row_id": (
            f"{artifact}@{artifact_sha256}#2:{stock_id}:{row_sha256}"
        ),
    }


def test_all_candidates_source_identity_accepts_registered_unique_rows(
    tmp_path: Path,
) -> None:
    columns = ["stock_id", *lineage.SOURCE_IDENTITY_FIELDS]
    rows = [
        source_identity_fixture(
            tmp_path,
            artifact="output/latest/range_rebound_watch_latest.csv",
            producer="stock_daily_monitor.py",
        ),
        source_identity_fixture(
            tmp_path,
            artifact="output/latest/revenue_pullback_latest.csv",
            producer="stock_daily_monitor.py",
        ),
    ]
    write_csv(tmp_path / lineage.ALL_CANDIDATES_ARTIFACT, columns, rows)

    assert lineage._validate_all_candidates_source_identity(tmp_path) == []


def test_all_candidates_source_identity_accepts_cp950_literal_na_lineage(
    tmp_path: Path,
) -> None:
    artifact = "output/latest/range_rebound_watch_latest.csv"
    source_path = tmp_path / artifact
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_text = (
        "stock_id,note,literal_na,literal_n_a\r\n"
        "2451,測試,NA,N/A\r\n"
    )
    source_path.write_bytes(source_text.encode("cp950"))
    artifact_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    row_sha256 = hashlib.sha256(
        json.dumps(
            [
                ["stock_id", "2451"],
                ["note", "測試"],
                ["literal_na", "NA"],
                ["literal_n_a", "N/A"],
            ],
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    row = {
        "stock_id": "2451",
        "candidate_source_raw_stock_id": "2451",
        "candidate_source_normalized_stock_id": "2451",
        "candidate_source_identity_columns": "stock_id",
        "candidate_source_artifact": artifact,
        "candidate_source_producer": "stock_daily_monitor.py",
        "candidate_source_artifact_sha256": artifact_sha256,
        "candidate_source_record_number": "2",
        "candidate_source_row_sha256": row_sha256,
        "candidate_source_row_id": (
            f"{artifact}@{artifact_sha256}#2:2451:{row_sha256}"
        ),
    }
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        ["stock_id", *lineage.SOURCE_IDENTITY_FIELDS],
        [row],
    )

    assert lineage._validate_all_candidates_source_identity(tmp_path) == []


def test_all_candidates_source_identity_derives_every_nonblank_raw_alias(
    tmp_path: Path,
) -> None:
    artifact = "output/latest/range_rebound_watch_latest.csv"
    source_path = tmp_path / artifact
    write_csv(
        source_path,
        ["stock_id", "ticker"],
        [{"stock_id": "2451", "ticker": "2452"}],
    )
    artifact_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    row_sha256 = hashlib.sha256(
        json.dumps(
            [["stock_id", "2451"], ["ticker", "2452"]],
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    row = {
        "stock_id": "2451",
        "candidate_source_raw_stock_id": "2451",
        "candidate_source_normalized_stock_id": "2451",
        "candidate_source_identity_columns": "stock_id",
        "candidate_source_artifact": artifact,
        "candidate_source_producer": "stock_daily_monitor.py",
        "candidate_source_artifact_sha256": artifact_sha256,
        "candidate_source_record_number": "2",
        "candidate_source_row_sha256": row_sha256,
        "candidate_source_row_id": (
            f"{artifact}@{artifact_sha256}#2:2451:{row_sha256}"
        ),
    }
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        ["stock_id", *lineage.SOURCE_IDENTITY_FIELDS],
        [row],
    )

    errors = lineage._validate_all_candidates_source_identity(tmp_path)

    assert any(
        "source identity alias declaration mismatch" in error
        and "derived=['stock_id', 'ticker']" in error
        for error in errors
    )
    assert any(
        "raw source alias normalization mismatch" in error
        and "column=ticker" in error
        for error in errors
    )


def test_all_candidates_source_identity_uses_logical_records_across_blank_lines(
    tmp_path: Path,
) -> None:
    artifact = "output/latest/range_rebound_watch_latest.csv"
    source_path = tmp_path / artifact
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.write_bytes(b"\xef\xbb\xbfstock_id\r\n\r\n2451\r\n")
    artifact_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    row_sha256 = hashlib.sha256(
        json.dumps(
            [["stock_id", "2451"]],
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    row = {
        "stock_id": "2451",
        "candidate_source_raw_stock_id": "2451",
        "candidate_source_normalized_stock_id": "2451",
        "candidate_source_identity_columns": "stock_id",
        "candidate_source_artifact": artifact,
        "candidate_source_producer": "stock_daily_monitor.py",
        "candidate_source_artifact_sha256": artifact_sha256,
        "candidate_source_record_number": "2",
        "candidate_source_row_sha256": row_sha256,
        "candidate_source_row_id": (
            f"{artifact}@{artifact_sha256}#2:2451:{row_sha256}"
        ),
    }
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        ["stock_id", *lineage.SOURCE_IDENTITY_FIELDS],
        [row],
    )

    assert lineage._validate_all_candidates_source_identity(tmp_path) == []


def test_all_candidates_source_identity_fails_when_all_decoders_fail(
    tmp_path: Path,
) -> None:
    artifact = "output/latest/range_rebound_watch_latest.csv"
    source_path = tmp_path / artifact
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.write_bytes(b"stock_id,note\n2451,\x81")
    artifact_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    row_sha256 = "f" * 64
    row = {
        "stock_id": "2451",
        "candidate_source_raw_stock_id": "2451",
        "candidate_source_normalized_stock_id": "2451",
        "candidate_source_identity_columns": "stock_id",
        "candidate_source_artifact": artifact,
        "candidate_source_producer": "stock_daily_monitor.py",
        "candidate_source_artifact_sha256": artifact_sha256,
        "candidate_source_record_number": "2",
        "candidate_source_row_sha256": row_sha256,
        "candidate_source_row_id": (
            f"{artifact}@{artifact_sha256}#2:2451:{row_sha256}"
        ),
    }
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        ["stock_id", *lineage.SOURCE_IDENTITY_FIELDS],
        [row],
    )

    errors = lineage._validate_all_candidates_source_identity(tmp_path)

    assert any(
        "cannot be decoded with bounded encodings" in error for error in errors
    )


def test_all_candidates_source_identity_rejects_collapse_and_duplicate_lineage(
    tmp_path: Path,
) -> None:
    columns = ["stock_id", *lineage.SOURCE_IDENTITY_FIELDS]
    valid = source_identity_fixture(
        tmp_path,
        artifact="output/latest/range_rebound_watch_latest.csv",
        producer="stock_daily_monitor.py",
    )
    malformed = dict(valid)
    malformed["candidate_source_raw_stock_id"] = "2451A"
    malformed["candidate_source_normalized_stock_id"] = "2451A"
    collapsed = dict(valid)
    collapsed["candidate_source_raw_stock_id"] = "2451A"
    rows = [malformed, collapsed, dict(collapsed)]
    write_csv(tmp_path / lineage.ALL_CANDIDATES_ARTIFACT, columns, rows)

    errors = lineage._validate_all_candidates_source_identity(tmp_path)

    assert any("not a four-digit equity code" in error for error in errors)
    assert any("normalized identity parity mismatch" in error for error in errors)
    assert any("raw-to-normalized identity parity mismatch" in error for error in errors)
    assert any("source row id is duplicated" in error for error in errors)


def formal_resolution_row(
    source_rows: list[dict[str, str]],
    root: Path,
    *,
    report_surface: bool = False,
) -> dict[str, str]:
    ordered = sorted(source_rows, key=lambda row: row["candidate_source_row_id"])
    row = {
        "signal_date": "20260731",
        "report_bucket": "" if report_surface else "mainstream",
        "report_line": "mainstream" if report_surface else "",
        "source_row_index": "volume_breakout:0",
        "stock_id": "2451",
        "model_id": "volume_range_breakout_v2_mid_position_momentum_attack",
        "original_category": "volume_breakout",
        "candidate_source_row_ids": "|".join(
            row["candidate_source_row_id"] for row in ordered
        ),
        "candidate_source_row_sha256s": "|".join(
            row["candidate_source_row_sha256"] for row in ordered
        ),
        "candidate_source_categories": "|".join(
            row.get("original_category") or row.get("category") or "<blank>"
            for row in ordered
        ),
        "candidate_formal_outcome_sha256": "",
        "candidate_presentation_source_artifact": "",
        "candidate_presentation_source_artifact_sha256": "",
        "candidate_presentation_source_row_sha256": "",
    }
    row["candidate_formal_outcome_sha256"] = lineage._canonical_payload_sha256(
        lineage._formal_outcome_envelope(row)
    )
    row["candidate_presentation_source_row_sha256"] = (
        lineage._canonical_payload_sha256(
            lineage._formal_presentation_envelope(row)
        )
    )
    watch_path = root / lineage.VOLUME_WATCH_ARTIFACT
    watch_columns = ["signal_date", "stock_id", "volume_breakout_type"]
    watch_row = {
        "signal_date": "20260731",
        "stock_id": "2451",
        "volume_breakout_type": "bottom_volume_attack",
    }
    write_csv(watch_path, watch_columns, [watch_row])
    taxonomy_path = root / lineage.VOLUME_TAXONOMY_ARTIFACT
    taxonomy_columns = ["stock_id"]
    taxonomy_row = {"stock_id": "2451"}
    write_csv(taxonomy_path, taxonomy_columns, [taxonomy_row])
    descriptor = {
        "contract": lineage.FORMAL_PRESENTATION_PROJECTION_CONTRACT,
        "mode": "all_candidates",
        "candidate_source_row_ids": row["candidate_source_row_ids"].split("|"),
        "candidate_source_row_sha256s": row[
            "candidate_source_row_sha256s"
        ].split("|"),
        "candidate_source_categories": row["candidate_source_categories"].split(
            "|"
        ),
        "watch": {
            "artifact": lineage.VOLUME_WATCH_ARTIFACT,
            "artifact_sha256": lineage._canonical_text_sha256(
                watch_path.read_bytes()
            ),
            "record_number": 2,
            "row_sha256": lineage._ordered_row_sha256(watch_columns, watch_row),
        },
        "taxonomy": {
            "artifact": lineage.VOLUME_TAXONOMY_ARTIFACT,
            "artifact_sha256": lineage._canonical_text_sha256(
                taxonomy_path.read_bytes()
            ),
            "row_sha256": lineage._ordered_row_sha256(
                taxonomy_columns, taxonomy_row
            ),
        },
        "presentation_row_sha256": row[
            "candidate_presentation_source_row_sha256"
        ],
    }
    descriptor_text = json.dumps(
        descriptor,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    row["candidate_presentation_source_artifact"] = descriptor_text
    row["candidate_presentation_source_artifact_sha256"] = hashlib.sha256(
        descriptor_text.encode("utf-8")
    ).hexdigest()
    return row


def rehash_formal_resolution_row(row: dict[str, str]) -> None:
    row["candidate_formal_outcome_sha256"] = lineage._canonical_payload_sha256(
        lineage._formal_outcome_envelope(row)
    )
    row["candidate_presentation_source_row_sha256"] = (
        lineage._canonical_payload_sha256(
            lineage._formal_presentation_envelope(row)
        )
    )
    descriptor = json.loads(row["candidate_presentation_source_artifact"])
    for field_name in (
        "candidate_source_row_ids",
        "candidate_source_row_sha256s",
        "candidate_source_categories",
    ):
        field_value = row[field_name]
        descriptor[field_name] = field_value.split("|") if field_value else []
    descriptor["mode"] = (
        "all_candidates" if row["candidate_source_row_ids"] else "taxonomy"
    )
    descriptor["presentation_row_sha256"] = row[
        "candidate_presentation_source_row_sha256"
    ]
    descriptor_text = json.dumps(
        descriptor,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    row["candidate_presentation_source_artifact"] = descriptor_text
    row["candidate_presentation_source_artifact_sha256"] = hashlib.sha256(
        descriptor_text.encode("utf-8")
    ).hexdigest()


def write_current_formal_resolution_pair(
    root: Path,
) -> tuple[dict[str, str], dict[str, str]]:
    source_rows = [
        {
            **source_identity_fixture(
                root,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        }
    ]
    write_csv(
        root / lineage.ALL_CANDIDATES_ARTIFACT,
        list(source_rows[0]),
        source_rows,
    )
    raw = formal_resolution_row(source_rows, root)
    report = formal_resolution_row(source_rows, root, report_surface=True)
    columns = list(raw)
    write_csv(
        root / "output/latest/daily_candidate_model_signals_latest.csv",
        columns,
        [raw],
    )
    write_csv(
        root / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        columns,
        [report],
    )
    return raw, report


def test_formal_outcome_numeric_contract_is_stable_across_all_four_surfaces(
    tmp_path: Path,
) -> None:
    row = formal_resolution_row([], tmp_path)
    row.update(
        {
            "signal_date": "20260810",
            "stock_id": "6152",
            "model_id": "volume_range_breakout_v2_low_position_volume_attack",
            "candidate_source_row_ids": "",
            "candidate_source_row_sha256s": "",
            "candidate_source_categories": "",
            "warrant_flow_signal": "",
            "base_model_score": "60.0",
            "operation_score": "20.0",
            "tdcc_score": "12.0",
            "pattern_score": "8.0",
            "risk_penalty": "0.0",
            "final_rank_score": "100",
            "rank_reason_zh": "cap reached",
            "model_score": "100.0",
            "score_components": "base=60 | operation=20 | tdcc=12 | pattern=8",
            "risk_penalty_tags": "",
            "tdcc_status": "strong_accumulation",
            "next_confirmation": "confirm next close",
        }
    )
    rehash_formal_resolution_row(row)
    canonical_envelope = {
        "model_id": "volume_range_breakout_v2_low_position_volume_attack",
        "candidate_signal_date": "",
        "authoritative_warrant_signal": "",
        "base_model_score": "60.0",
        "operation_score": "20.0",
        "tdcc_score": "12.0",
        "pattern_score": "8.0",
        "risk_penalty": "0.0",
        "final_rank_score": "100.0",
        "rank_reason_zh": "cap reached",
        "model_score": "100.0",
        "score_components": "base=60 | operation=20 | tdcc=12 | pattern=8",
        "risk_penalty_tags": "",
        "tdcc_status": "strong_accumulation",
        "next_confirmation": "confirm next close",
    }
    row["candidate_formal_outcome_sha256"] = lineage._canonical_payload_sha256(
        canonical_envelope
    )

    labels = (
        "current_raw",
        "current_report",
        "formal_signal_log_20260810",
        "historical_pair_20260810",
    )
    for label in labels:
        errors = lineage._validate_formal_projection_hashes(row, label, 2)
        assert not any("formal outcome" in error for error in errors), errors

    drifted = dict(row)
    drifted["model_score"] = "99.9"
    for label in labels:
        errors = lineage._validate_formal_projection_hashes(drifted, label, 2)
        assert any(
            "formal outcome SHA-256 does not match the independent row projection"
            in error
            and f"artifact={label}" in error
            for error in errors
        )


@pytest.mark.parametrize("invalid", ["83.51", "NaN", "Infinity", "1e2", "bad"])
def test_formal_outcome_numeric_contract_rejects_invalid_values(
    tmp_path: Path,
    invalid: str,
) -> None:
    row = formal_resolution_row([], tmp_path)
    row["final_rank_score"] = invalid
    errors = lineage._validate_formal_projection_hashes(row, "current_raw", 2)
    assert any(
        "formal outcome numeric field is not canonicalizable" in error
        and "field=final_rank_score" in error
        for error in errors
    )


def test_formal_resolution_lineage_requires_exact_raw_report_pairing(
    tmp_path: Path,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        },
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/revenue_pullback_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "revenue_pullback",
        },
    ]
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        list(source_rows[0]),
        source_rows,
    )
    raw = formal_resolution_row(source_rows, tmp_path)
    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    columns = list(raw)
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_latest.csv",
        columns,
        [raw],
    )
    write_csv(
        tmp_path
        / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        columns,
        [report],
    )

    assert lineage._validate_formal_resolution_lineage(tmp_path) == []

    report["candidate_formal_outcome_sha256"] = "6" * 64
    report["candidate_source_row_sha256s"] = "1" * 64
    write_csv(
        tmp_path
        / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        columns,
        [report],
    )
    errors = lineage._validate_formal_resolution_lineage(tmp_path)

    assert any("source lineage arrays are not paired" in error for error in errors)
    assert any("raw/report resolution lineage mismatch" in error for error in errors)


def test_formal_resolution_lineage_rejects_synchronized_forged_source_rows(
    tmp_path: Path,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        }
    ]
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        list(source_rows[0]),
        source_rows,
    )
    forged_sha = "f" * 64
    forged_id = f"output/latest/forged.csv@{'e' * 64}#2:2451:{forged_sha}"
    raw = formal_resolution_row(source_rows, tmp_path)
    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    for row in (raw, report):
        row["candidate_source_row_ids"] = forged_id
        row["candidate_source_row_sha256s"] = forged_sha
        row["candidate_source_categories"] = "range_rebound"
    columns = list(raw)
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_latest.csv",
        columns,
        [raw],
    )
    write_csv(
        tmp_path
        / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        columns,
        [report],
    )

    errors = lineage._validate_formal_resolution_lineage(tmp_path)

    assert any("formal source crosswalk membership/order mismatch" in error for error in errors)
    assert any("references an unknown candidate row" in error for error in errors)


def test_formal_resolution_lineage_rejects_descriptor_mode_source_mismatch(
    tmp_path: Path,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        }
    ]
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        list(source_rows[0]),
        source_rows,
    )
    raw = formal_resolution_row(source_rows, tmp_path)
    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    for row in (raw, report):
        descriptor = json.loads(row["candidate_presentation_source_artifact"])
        descriptor["mode"] = "taxonomy"
        descriptor_text = json.dumps(
            descriptor,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        row["candidate_presentation_source_artifact"] = descriptor_text
        row["candidate_presentation_source_artifact_sha256"] = hashlib.sha256(
            descriptor_text.encode("utf-8")
        ).hexdigest()
    columns = list(raw)
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_latest.csv",
        columns,
        [raw],
    )
    write_csv(
        tmp_path
        / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        columns,
        [report],
    )

    errors = lineage._validate_formal_resolution_lineage(tmp_path)

    assert any(
        "formal presentation descriptor mode/source mismatch" in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("field_name", "expected_error"),
    [
        (
            "candidate_formal_outcome_sha256",
            "formal outcome SHA-256 does not match the independent row projection",
        ),
        (
            "candidate_presentation_source_row_sha256",
            "formal presentation row SHA-256 does not match the independent row projection",
        ),
    ],
)
def test_formal_resolution_lineage_rejects_synchronized_derived_hash_tampering(
    tmp_path: Path,
    field_name: str,
    expected_error: str,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        }
    ]
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        list(source_rows[0]),
        source_rows,
    )
    raw = formal_resolution_row(source_rows, tmp_path)
    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    for row in (raw, report):
        row[field_name] = "f" * 64
    columns = list(raw)
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_latest.csv",
        columns,
        [raw],
    )
    write_csv(
        tmp_path
        / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        columns,
        [report],
    )

    errors = lineage._validate_formal_resolution_lineage(tmp_path)

    assert any(expected_error in error for error in errors)


def test_current_formal_resolution_rejects_self_consistent_wrong_watch_source(
    tmp_path: Path,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        }
    ]
    write_csv(
        tmp_path / lineage.ALL_CANDIDATES_ARTIFACT,
        list(source_rows[0]),
        source_rows,
    )
    raw = formal_resolution_row(source_rows, tmp_path)
    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    for row in (raw, report):
        descriptor = json.loads(row["candidate_presentation_source_artifact"])
        descriptor["watch"]["row_sha256"] = "f" * 64
        descriptor_text = json.dumps(
            descriptor,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        row["candidate_presentation_source_artifact"] = descriptor_text
        row["candidate_presentation_source_artifact_sha256"] = hashlib.sha256(
            descriptor_text.encode("utf-8")
        ).hexdigest()
    columns = list(raw)
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_latest.csv",
        columns,
        [raw],
    )
    write_csv(
        tmp_path
        / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        columns,
        [report],
    )

    errors = lineage._validate_formal_resolution_lineage(tmp_path)

    assert any(
        "formal presentation watch row SHA-256 mismatch" in error
        for error in errors
    )


def test_ordinary_current_validation_accepts_uncommitted_rebuilt_formal_consumers(
    tmp_path: Path,
) -> None:
    raw, report = write_current_formal_resolution_pair(tmp_path)
    base_sha = initialize_git_fixture(tmp_path)
    watch_path = tmp_path / lineage.VOLUME_WATCH_ARTIFACT
    watch_columns, watch_rows = lineage._read_artifact(watch_path)
    watch_rows[0]["volume_breakout_type"] = "fresh_live_current_payload"
    write_csv(watch_path, watch_columns, watch_rows)
    watch_sha = lineage._canonical_text_sha256(watch_path.read_bytes())
    watch_row_sha = lineage._ordered_row_sha256(watch_columns, watch_rows[0])

    for row in (raw, report):
        descriptor = json.loads(row["candidate_presentation_source_artifact"])
        descriptor["watch"]["artifact_sha256"] = watch_sha
        descriptor["watch"]["row_sha256"] = watch_row_sha
        row["candidate_presentation_source_artifact"] = json.dumps(
            descriptor,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        rehash_formal_resolution_row(row)
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_latest.csv",
        list(raw),
        [raw],
    )
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        list(report),
        [report],
    )

    assert lineage._validate_formal_resolution_lineage(tmp_path) == []
    assert lineage._validate_formal_resolution_lineage(
        tmp_path,
        trusted_ref=base_sha,
    ) == []
    committed_refresh_errors = lineage._validate_formal_resolution_lineage(
        tmp_path,
        trusted_ref="HEAD",
        committed_refresh_mode=True,
    )
    assert any(
        "committed-refresh formal resolution consumer must match a committed payload"
        in error
        for error in committed_refresh_errors
    )


def test_current_formal_resolution_replays_pinned_watch_from_trusted_history(
    tmp_path: Path,
) -> None:
    write_current_formal_resolution_pair(tmp_path)
    consumer_revision = initialize_git_fixture(tmp_path)
    watch_path = tmp_path / lineage.VOLUME_WATCH_ARTIFACT
    watch_columns, watch_rows = lineage._read_artifact(watch_path)
    watch_rows[0]["volume_breakout_type"] = "advanced_after_consumer"
    write_csv(watch_path, watch_columns, watch_rows)
    subprocess.run(
        ["git", "add", lineage.VOLUME_WATCH_ARTIFACT],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "advance watch after formal consumers"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    trusted_ref = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    errors = lineage._validate_formal_resolution_lineage(
        tmp_path,
        trusted_ref=trusted_ref,
        committed_refresh_mode=True,
    )

    assert errors == []
    assert consumer_revision != trusted_ref


def test_committed_refresh_keeps_taxonomy_current_only_without_history_replay(
    tmp_path: Path,
) -> None:
    write_current_formal_resolution_pair(tmp_path)
    initialize_git_fixture(tmp_path)
    taxonomy_path = tmp_path / lineage.VOLUME_TAXONOMY_ARTIFACT
    taxonomy_columns, taxonomy_rows = lineage._read_artifact(taxonomy_path)
    taxonomy_columns.append("current_only_marker")
    taxonomy_rows[0]["current_only_marker"] = "advanced_after_consumer"
    write_csv(taxonomy_path, taxonomy_columns, taxonomy_rows)
    subprocess.run(
        ["git", "add", lineage.VOLUME_TAXONOMY_ARTIFACT],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "advance current taxonomy after formal consumers"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    errors = lineage._validate_formal_resolution_lineage(
        tmp_path,
        trusted_ref="HEAD",
        committed_refresh_mode=True,
    )

    assert any(
        "formal presentation taxonomy artifact SHA-256 mismatch" in error
        for error in errors
    )
    assert not any(
        "formal presentation watch" in error
        for error in errors
    )


def test_current_formal_resolution_rejects_pinned_source_later_than_consumer(
    tmp_path: Path,
) -> None:
    raw, report = write_current_formal_resolution_pair(tmp_path)
    initialize_git_fixture(tmp_path, empty_commit=True)
    watch_path = tmp_path / lineage.VOLUME_WATCH_ARTIFACT
    watch_columns, watch_rows = lineage._read_artifact(watch_path)
    original_watch_payload = watch_path.read_bytes()
    watch_rows[0]["volume_breakout_type"] = "future_source_revision"
    write_csv(watch_path, watch_columns, watch_rows)
    future_watch_payload = watch_path.read_bytes()
    future_watch_sha = lineage._canonical_text_sha256(future_watch_payload)
    future_watch_row_sha = lineage._ordered_row_sha256(
        watch_columns,
        watch_rows[0],
    )
    watch_path.write_bytes(original_watch_payload)

    for row in (raw, report):
        descriptor = json.loads(row["candidate_presentation_source_artifact"])
        descriptor["watch"]["artifact_sha256"] = future_watch_sha
        descriptor["watch"]["row_sha256"] = future_watch_row_sha
        descriptor_text = json.dumps(
            descriptor,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        row["candidate_presentation_source_artifact"] = descriptor_text
        row["candidate_presentation_source_artifact_sha256"] = hashlib.sha256(
            descriptor_text.encode("utf-8")
        ).hexdigest()
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_latest.csv",
        list(raw),
        [raw],
    )
    write_csv(
        tmp_path / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        list(report),
        [report],
    )
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "commit", "-m", "commit consumer with future source pin"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    watch_path.write_bytes(future_watch_payload)
    subprocess.run(
        ["git", "add", lineage.VOLUME_WATCH_ARTIFACT],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "publish pinned source too late"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    errors = lineage._validate_formal_resolution_lineage(
        tmp_path,
        trusted_ref="HEAD",
        committed_refresh_mode=True,
    )

    assert any(
        "formal presentation watch source revision is later than its committed "
        "consumer revision" in error
        for error in errors
    )


def test_historical_formal_source_crosswalk_rejects_forged_source_rows(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
            "warrant_flow_signal": "call_inflow",
        }
    ]
    forged_sha = "f" * 64
    forged_id = f"output/latest/forged.csv@{'e' * 64}#2:2451:{forged_sha}"
    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    report.update(
        {
            "candidate_source_row_ids": forged_id,
            "candidate_source_row_sha256s": forged_sha,
            "candidate_source_categories": "range_rebound",
            "warrant_flow_signal": "call_inflow",
        }
    )
    snapshot_dir = tmp_path / "output/history/daily_model_snapshots"
    candidate_path = snapshot_dir / "all_candidates_20260731.csv"
    report_path = snapshot_dir / "daily_candidate_model_signals_for_report_20260731.csv"
    official_path = tmp_path / "output/history/warrant_flow/warrant_flow_20260731.csv"
    write_csv(candidate_path, list(source_rows[0]), source_rows)
    write_csv(report_path, list(report), [report])
    write_csv(
        official_path,
        ["stock_id", "warrant_flow_signal"],
        [{"stock_id": "2451", "warrant_flow_signal": "call_inflow"}],
    )
    monkeypatch.setattr(
        lineage,
        "_manifest_dated_files",
        lambda _root, artifact_id: {
            "20260731": (
                candidate_path
                if artifact_id == "all_candidates_source_rows"
                else report_path
            )
        },
    )
    monkeypatch.setattr(
        lineage,
        "_dated_files",
        lambda _root, _pattern: {"20260731": official_path},
    )

    errors = lineage._validate_historical_projection(tmp_path)

    assert any(
        "formal source crosswalk membership/order mismatch" in error
        and "historical_pair_20260731" in error
        for error in errors
    )


def test_historical_formal_report_rejects_truncated_parallel_arrays_after_rehash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
            "warrant_flow_signal": "call_inflow",
        },
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/revenue_pullback_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "revenue_pullback",
            "warrant_flow_signal": "call_inflow",
        },
    ]
    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    report["candidate_source_row_sha256s"] = report[
        "candidate_source_row_sha256s"
    ].split("|")[0]
    rehash_formal_resolution_row(report)

    lifecycle = formal_resolution_row(source_rows, tmp_path)
    signal_log_path = tmp_path / lineage.FORMAL_SIGNAL_LOG_ARTIFACT
    write_csv(signal_log_path, list(lifecycle), [lifecycle])

    snapshot_dir = tmp_path / "output/history/daily_model_snapshots"
    candidate_path = snapshot_dir / "all_candidates_20260731.csv"
    report_path = snapshot_dir / "model_signals_for_report_20260731.csv"
    official_path = tmp_path / "output/history/warrant_flow/warrant_flow_20260731.csv"
    write_csv(candidate_path, list(source_rows[0]), source_rows)
    write_csv(report_path, list(report), [report])
    write_csv(
        official_path,
        ["stock_id", "warrant_flow_signal"],
        [{"stock_id": "2451", "warrant_flow_signal": "call_inflow"}],
    )
    monkeypatch.setattr(
        lineage,
        "_manifest_dated_files",
        lambda _root, artifact_id: {
            "20260731": (
                candidate_path
                if artifact_id == "all_candidates_source_rows"
                else report_path
            )
        },
    )
    monkeypatch.setattr(
        lineage,
        "_dated_files",
        lambda _root, _pattern: {"20260731": official_path},
    )

    errors = lineage._validate_historical_projection(tmp_path)

    assert any(
        "formal resolution source lineage arrays are not paired" in error
        and "artifact=historical_pair_20260731" in error
        for error in errors
    )


def test_historical_formal_signal_log_rejects_truncated_pairing_after_rehash(
    tmp_path: Path,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        },
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/revenue_pullback_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "revenue_pullback",
        },
    ]
    candidate_snapshot = (
        tmp_path
        / "output/history/daily_model_snapshots/all_candidates_20260731.csv"
    )
    write_csv(candidate_snapshot, list(source_rows[0]), source_rows)

    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    lifecycle = formal_resolution_row(source_rows, tmp_path)
    for row in (report, lifecycle):
        row["candidate_source_row_sha256s"] = "f" * 64
        rehash_formal_resolution_row(row)
    report_snapshot = (
        tmp_path
        / "output/history/daily_model_snapshots/model_signals_for_report_20260731.csv"
    )
    write_csv(report_snapshot, list(report), [report])
    signal_log_path = tmp_path / lineage.FORMAL_SIGNAL_LOG_ARTIFACT
    write_csv(signal_log_path, list(lifecycle), [lifecycle])

    errors = lineage._validate_historical_formal_signal_log(
        tmp_path,
        {"20260731": candidate_snapshot},
        {"20260731": report_snapshot},
    )

    assert any(
        "formal resolution source lineage arrays are not paired" in error
        and "artifact=formal_signal_log_20260731" in error
        for error in errors
    )
    assert any(
        "formal resolution source row ID/hash pairing mismatch" in error
        and "artifact=formal_signal_log_20260731" in error
        for error in errors
    )


def test_historical_formal_signal_log_rejects_blank_candidate_source_identity(
    tmp_path: Path,
) -> None:
    blank_candidate = {
        "stock_id": "2451",
        "category": "range_rebound",
        **{field_name: "" for field_name in lineage.SOURCE_IDENTITY_FIELDS},
    }
    candidate_snapshot = (
        tmp_path
        / "output/history/daily_model_snapshots/all_candidates_20260801.csv"
    )
    write_csv(candidate_snapshot, list(blank_candidate), [blank_candidate])

    report = formal_resolution_row([], tmp_path, report_surface=True)
    lifecycle = formal_resolution_row([], tmp_path)
    for row in (report, lifecycle):
        row["signal_date"] = "20260801"
        rehash_formal_resolution_row(row)
    report_snapshot = (
        tmp_path
        / "output/history/daily_model_snapshots/model_signals_for_report_20260801.csv"
    )
    write_csv(report_snapshot, list(report), [report])
    write_csv(
        tmp_path / lineage.FORMAL_SIGNAL_LOG_ARTIFACT,
        list(lifecycle),
        [lifecycle],
    )

    errors = lineage._validate_historical_formal_signal_log(
        tmp_path,
        {"20260801": candidate_snapshot},
        {"20260801": report_snapshot},
    )

    assert any(
        "candidate row is missing source identity" in error
        and "label=formal_signal_log_20260801" in error
        and "stock_id='2451'" in error
        for error in errors
    )


def test_historical_formal_signal_log_requires_crosswalk_and_unique_identity(
    tmp_path: Path,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        }
    ]
    candidate_snapshot = (
        tmp_path
        / "output/history/daily_model_snapshots/all_candidates_20260731.csv"
    )
    write_csv(candidate_snapshot, list(source_rows[0]), source_rows)
    formal = formal_resolution_row(source_rows, tmp_path)
    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    report_snapshot = (
        tmp_path
        / "output/history/daily_model_snapshots/model_signals_for_report_20260731.csv"
    )
    write_csv(report_snapshot, list(report), [report])
    signal_log_path = tmp_path / lineage.FORMAL_SIGNAL_LOG_ARTIFACT
    write_csv(signal_log_path, list(formal), [formal])

    assert lineage._validate_historical_formal_signal_log(
        tmp_path,
        {"20260731": candidate_snapshot},
        {"20260731": report_snapshot},
    ) == []

    forged = dict(formal)
    forged_sha = "f" * 64
    forged["candidate_source_row_ids"] = (
        f"output/latest/forged.csv@{'e' * 64}#2:2451:{forged_sha}"
    )
    forged["candidate_source_row_sha256s"] = forged_sha
    write_csv(signal_log_path, list(formal), [forged, dict(forged)])

    errors = lineage._validate_historical_formal_signal_log(
        tmp_path,
        {"20260731": candidate_snapshot},
        {"20260731": report_snapshot},
    )

    assert any("formal signal log has duplicate effective identity" in error for error in errors)
    assert any("formal source crosswalk membership/order mismatch" in error for error in errors)


def test_historical_formal_signal_log_rejects_report_parity_drift_after_self_rehash(
    tmp_path: Path,
) -> None:
    source_rows = [
        {
            **source_identity_fixture(
                tmp_path,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
            ),
            "category": "range_rebound",
        }
    ]
    candidate_snapshot = (
        tmp_path
        / "output/history/daily_model_snapshots/all_candidates_20260731.csv"
    )
    write_csv(candidate_snapshot, list(source_rows[0]), source_rows)

    report = formal_resolution_row(source_rows, tmp_path, report_surface=True)
    report_snapshot = (
        tmp_path
        / "output/history/daily_model_snapshots/model_signals_for_report_20260731.csv"
    )
    write_csv(report_snapshot, list(report), [report])

    lifecycle = formal_resolution_row(source_rows, tmp_path)
    lifecycle["rank_reason_zh"] = "tampered_but_self_consistent"
    lifecycle["candidate_formal_outcome_sha256"] = (
        lineage._canonical_payload_sha256(
            lineage._formal_outcome_envelope(lifecycle)
        )
    )
    signal_log_path = tmp_path / lineage.FORMAL_SIGNAL_LOG_ARTIFACT
    write_csv(signal_log_path, list(lifecycle), [lifecycle])

    errors = lineage._validate_historical_formal_signal_log(
        tmp_path,
        {"20260731": candidate_snapshot},
        {"20260731": report_snapshot},
    )

    assert not any(
        "formal outcome lineage hash mismatch" in error for error in errors
    )
    assert any(
        "formal signal log/report lineage mismatch" in error
        and "field=candidate_formal_outcome_sha256" in error
        for error in errors
    )


def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def initialize_git_fixture(root: Path, *, empty_commit: bool = False) -> str:
    subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "lineage-test@example.invalid"],
        cwd=root,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Lineage Test"],
        cwd=root,
        check=True,
    )
    if not empty_commit:
        subprocess.run(["git", "add", "."], cwd=root, check=True)
    command = ["git", "commit", "-m", "fixture"]
    if empty_commit:
        command.insert(2, "--allow-empty")
    subprocess.run(command, cwd=root, check=True, capture_output=True)
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


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
        RANKING_VALIDATOR_HISTORY_MIGRATION_ID,
        "theme_warrant_lineage_revision_contract_20260801",
        SOURCE_IDENTITY_MIGRATION_ID,
        REPORT_SIGNAL_SCHEMA_CONSUMER_MIGRATION_ID,
        FORMAL_OUTCOME_NUMERIC_MIGRATION_ID,
        PINNED_WATCH_LINEAGE_MIGRATION_ID,
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
        RANKING_VALIDATOR_EXCLUSION_MIGRATION_ID,
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
            **source_identity_fixture(
                root,
                artifact="output/latest/range_rebound_watch_latest.csv",
                producer="stock_daily_monitor.py",
                stock_id="1617",
            ),
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
    signal_log_row = dict(formal[0])
    for field_name in lineage.FORMAL_RESOLUTION_FIELDS:
        signal_log_row[field_name] = ""
    write_csv(
        root / lineage.FORMAL_SIGNAL_LOG_ARTIFACT,
        list(signal_log_row),
        [signal_log_row],
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
    snapshot_dir = root / "output/history/daily_model_snapshots"
    candidate_snapshot = snapshot_dir / "all_candidates_20260717.csv"
    report_snapshot = (
        snapshot_dir / "daily_candidate_model_signals_for_report_20260717.csv"
    )
    write_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv",
        [
            "snapshot_report_date",
            "snapshot_revision",
            "supersedes_snapshot_sha256",
            "revision_reason",
            "artifact_id",
            "snapshot_path",
            "snapshot_sha256",
        ],
        [
            {
                "snapshot_report_date": "20260717",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "legacy_v1_manifest",
                "artifact_id": "all_candidates_source_rows",
                "snapshot_path": candidate_snapshot.relative_to(root).as_posix(),
                "snapshot_sha256": snapshot_file_sha256(candidate_snapshot),
            },
            {
                "snapshot_report_date": "20260717",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "legacy_v1_manifest",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": report_snapshot.relative_to(root).as_posix(),
                "snapshot_sha256": snapshot_file_sha256(report_snapshot),
            },
        ],
    )


def refresh_current_theme_source_hashes(root: Path) -> None:
    theme_path = root / lineage.THEME_ADVISORY_ARTIFACT
    columns, rows = lineage._read_artifact(theme_path)
    source_hashes = {
        "volume_watch_source_sha256": lineage._canonical_text_sha256(
            (root / lineage.VOLUME_WATCH_ARTIFACT).read_bytes()
        ),
        "warrant_flow_source_sha256": lineage._canonical_text_sha256(
            (root / "output/latest/all_candidates_latest.csv").read_bytes()
        ),
        "warrant_flow_official_source_sha256": lineage._canonical_text_sha256(
            (root / "output/latest/warrant_flow_latest.csv").read_bytes()
        ),
    }
    for row in rows:
        row.update(source_hashes)
    write_csv(theme_path, columns, rows)


def set_current_candidate_warrant_projection(
    root: Path,
    *,
    candidate_signal: str,
    official_signal: str,
    theme_signal: str,
) -> None:
    for relative_path, signal in (
        ("output/latest/all_candidates_latest.csv", candidate_signal),
        ("output/latest/warrant_flow_latest.csv", official_signal),
        (lineage.THEME_ADVISORY_ARTIFACT, theme_signal),
    ):
        path = root / relative_path
        columns, rows = lineage._read_artifact(path)
        rows[0]["warrant_flow_signal"] = signal
        write_csv(path, columns, rows)

    score = "82" if candidate_signal in lineage.BULLISH_WARRANT_SIGNALS else "80"
    score_components = (
        "base=80 | warrant bullish +2"
        if candidate_signal in lineage.BULLISH_WARRANT_SIGNALS
        else "base=80"
    )
    for relative_path in (
        "output/latest/daily_candidate_model_signals_latest.csv",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    ):
        path = root / relative_path
        columns, rows = lineage._read_artifact(path)
        rows[0]["warrant_flow_signal"] = candidate_signal
        rows[0]["model_score"] = score
        rows[0]["final_rank_score"] = score
        rows[0]["score_components"] = score_components
        write_csv(path, columns, rows)

    refresh_current_theme_source_hashes(root)


def test_valid_canonical_field_lineage_contract_passes(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    assert lineage.validate(tmp_path) == []


def test_source_identity_registry_requires_every_in_place_writer_mirror(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.REGISTRY_PATH
    columns, rows = lineage._read_artifact(path)
    row = next(
        item
        for item in rows
        if item["lineage_id"] == "candidate_source_row_id__all_candidates_current"
    )
    removed = "scripts/build_candidate_repeat_appearance.py"
    row["allowed_consumer_modules"] = ";".join(
        consumer
        for consumer in row["allowed_consumer_modules"].split(";")
        if consumer != removed
    )
    row["contract_sha256"] = lineage.contract_sha256(row)
    write_csv(path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "all_candidates source identity lineage omits registered in-place writer mirrors"
        in error
        and "candidate_source_row_id__all_candidates_current" in error
        and removed in error
        for error in errors
    )


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


def test_global_official_warrant_row_without_candidate_is_not_a_formal_projection() -> None:
    formal = {
        "signal_date": "20260807",
        "report_line": "mainstream",
        "source_row_index": "volume_breakout:3",
        "stock_id": "2059",
        "model_id": "volume_range_breakout_v2_high_position_volume_attack",
        "final_rank_score": "70",
        "model_score": "70",
        "model_rank": "1",
        "warrant_flow_signal": "",
        "score_components": "base=70",
    }

    errors, indexed = lineage._validate_projection_set(
        [{"stock_id": "2059", "warrant_flow_signal": "call_inflow"}],
        [],
        [formal],
        "current_raw",
    )

    assert errors == []
    assert len(indexed) == 1


def test_candidate_scoped_official_warrant_mismatch_still_fails_closed() -> None:
    candidate = {
        "source_row_index": "1",
        "stock_id": "6505",
        "warrant_flow_signal": "call_inflow",
    }
    formal = {
        "signal_date": "20260807",
        "report_line": "mainstream",
        "source_row_index": "1",
        "stock_id": "6505",
        "model_id": "volume_range_breakout_v2_high_position_volume_attack",
        "final_rank_score": "72",
        "model_score": "72",
        "model_rank": "1",
        "warrant_flow_signal": "call_inflow",
        "score_components": "base=70 | warrant bullish +2",
    }

    errors, _ = lineage._validate_projection_set(
        [{"stock_id": "6505", "warrant_flow_signal": "no_signal"}],
        [candidate],
        [formal],
        "current_raw",
    )

    assert any(
        "official/all_candidates warrant projection mismatch" in error
        and "stock_id=6505" in error
        for error in errors
    )


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


def test_theme_official_lineage_resolves_pinned_revision_after_latest_advances(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    columns, rows = lineage._read_artifact(official_path)
    rows.append(
        {
            "date": "20260717",
            "stock_id": "9999",
            "warrant_flow_signal": "call_inflow",
        }
    )
    write_csv(official_path, columns, rows)
    old_official_sha = lineage._canonical_text_sha256(official_path.read_bytes())
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    theme_columns, theme_rows = lineage._read_artifact(theme_path)
    theme_rows[0]["warrant_flow_official_source_sha256"] = old_official_sha
    write_csv(theme_path, theme_columns, theme_rows)
    base_sha = initialize_git_fixture(tmp_path)
    rows[0]["date"] = "20260730"
    rows[1]["date"] = "20260730"
    rows[1]["warrant_flow_signal"] = "put_inflow"
    write_csv(official_path, columns, rows)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "commit", "-m", "advance mutable warrant latest"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    assert lineage.validate(tmp_path, base_ref=base_sha) == []
    payload, revision = lineage._resolve_pinned_canonical_source_revision(
        tmp_path,
        "output/latest/warrant_flow_latest.csv",
        old_official_sha,
        trusted_ref=base_sha,
        allow_live=False,
    )
    _, resolved_rows = lineage._read_csv_payload(payload)
    resolved = {row["stock_id"]: row["warrant_flow_signal"] for row in resolved_rows}
    assert resolved["9999"] == "call_inflow"
    assert revision == base_sha


def test_theme_official_lineage_rejects_unreconstructable_revision(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    initialize_git_fixture(tmp_path)
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    columns, rows = lineage._read_artifact(theme_path)
    rows[0]["warrant_flow_official_source_sha256"] = "f" * 64
    write_csv(theme_path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "theme advisory official warrant source revision cannot be validated" in error
        and "not reconstructable" in error
        for error in errors
    )


def test_theme_same_revision_signal_mismatch_still_fails_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    columns, rows = lineage._read_artifact(theme_path)
    rows[0]["warrant_flow_signal"] = "no_signal"
    write_csv(theme_path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "theme advisory warrant projection differs from official warrant" in error
        for error in errors
    )


def test_theme_allows_2059_global_only_official_no_signal_projection(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)

    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    official_columns, official_rows = lineage._read_artifact(official_path)
    official_rows.append(
        {
            "date": "20260717",
            "stock_id": "2059",
            "warrant_flow_signal": "no_signal",
        }
    )
    write_csv(official_path, official_columns, official_rows)

    watch_path = tmp_path / lineage.VOLUME_WATCH_ARTIFACT
    watch_columns, watch_rows = lineage._read_artifact(watch_path)
    watch_2059 = dict(watch_rows[0])
    watch_2059.update(
        {
            "stock_id": "2059",
            "advisory_volume_breakout_rank": "2",
        }
    )
    watch_rows.append(watch_2059)
    write_csv(watch_path, watch_columns, watch_rows)

    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    theme_columns, theme_rows = lineage._read_artifact(theme_path)
    theme_2059 = dict(theme_rows[0])
    theme_2059.update(
        {
            "stock_id": "2059",
            "volume_breakout_rank": "2",
            "warrant_flow_signal": "",
        }
    )
    theme_rows.append(theme_2059)
    write_csv(theme_path, theme_columns, theme_rows)
    refresh_current_theme_source_hashes(tmp_path)

    assert lineage.validate(tmp_path) == []


def test_theme_candidate_blank_exact_official_parity_passes(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    set_current_candidate_warrant_projection(
        tmp_path,
        candidate_signal="",
        official_signal="",
        theme_signal="",
    )

    assert lineage._validate_current_projection(tmp_path) == []


def test_theme_candidate_blank_official_no_signal_mismatch_fails_closed(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    set_current_candidate_warrant_projection(
        tmp_path,
        candidate_signal="",
        official_signal="no_signal",
        theme_signal="",
    )

    errors = lineage._validate_current_projection(tmp_path)

    assert any(
        "theme advisory warrant projection differs from official warrant" in error
        and "stock_id=1617" in error
        and "official='no_signal' actual=''" in error
        for error in errors
    )


def test_theme_pinned_official_duplicate_rows_fail_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    columns, rows = lineage._read_artifact(official_path)
    rows.append(dict(rows[0]))
    write_csv(official_path, columns, rows)
    refresh_current_theme_source_hashes(tmp_path)

    errors = lineage._validate_current_projection(tmp_path)

    assert any(
        "theme advisory pinned official warrant revision has duplicate stock_id rows: "
        "stock_id=1617" in error
        for error in errors
    )


def test_theme_conflicting_candidate_duplicate_rows_fail_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    candidate_path = tmp_path / "output/latest/all_candidates_latest.csv"
    columns, rows = lineage._read_artifact(candidate_path)
    conflicting = dict(rows[0])
    conflicting.update(
        {
            "source_row_index": "2",
            "warrant_flow_signal": "no_signal",
        }
    )
    rows.append(conflicting)
    write_csv(candidate_path, columns, rows)
    refresh_current_theme_source_hashes(tmp_path)

    errors = lineage._validate_current_projection(tmp_path)

    assert any(
        "current_theme has inconsistent warrant projection by stock" in error
        and "stock_id=1617" in error
        for error in errors
    )


def test_theme_mixed_official_revisions_fail_closed(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    columns, rows = lineage._read_artifact(theme_path)
    mixed = dict(rows[0])
    mixed["stock_id"] = "9999"
    mixed["warrant_flow_signal"] = ""
    mixed["warrant_flow_official_source_sha256"] = "f" * 64
    rows.append(mixed)
    write_csv(theme_path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "theme advisory official warrant source revision is not singular" in error
        for error in errors
    )


def test_theme_positive_signal_requires_row_in_pinned_official_revision(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    write_csv(
        official_path,
        ["date", "stock_id", "warrant_flow_signal"],
        [{"date": "20260717", "stock_id": "9999", "warrant_flow_signal": ""}],
    )
    official_sha = lineage._canonical_text_sha256(official_path.read_bytes())
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    columns, rows = lineage._read_artifact(theme_path)
    rows[0]["warrant_flow_official_source_sha256"] = official_sha
    write_csv(theme_path, columns, rows)

    errors = lineage.validate(tmp_path)

    assert any(
        "theme advisory positive warrant projection lacks pinned official row" in error
        and "stock_id=1617" in error
        for error in errors
    )


def test_theme_rejects_source_revision_committed_after_consumer(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    official_payload = official_path.read_bytes()
    official_path.unlink()
    initialize_git_fixture(tmp_path)
    official_path.parent.mkdir(parents=True, exist_ok=True)
    official_path.write_bytes(official_payload)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "commit", "-m", "add source after theme"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    errors = lineage._validate_current_projection(tmp_path, trusted_ref="HEAD")

    assert any(
        "official warrant revision is not available before the consumer artifact"
        in error
        for error in errors
    )


def test_theme_rejects_branch_committed_pair_outside_trusted_ref(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    trusted_base = initialize_git_fixture(tmp_path)
    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    official_columns, official_rows = lineage._read_artifact(official_path)
    official_rows.append(
        {
            "date": official_rows[0]["date"],
            "stock_id": "9999",
            "warrant_flow_signal": "",
        }
    )
    write_csv(official_path, official_columns, official_rows)
    branch_source_sha = lineage._canonical_text_sha256(official_path.read_bytes())
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    theme_columns, theme_rows = lineage._read_artifact(theme_path)
    for row in theme_rows:
        row["warrant_flow_official_source_sha256"] = branch_source_sha
    write_csv(theme_path, theme_columns, theme_rows)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "commit", "-m", "branch-only theme source pair"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    errors = lineage._validate_current_projection(
        tmp_path,
        trusted_ref=trusted_base,
    )

    assert any(
        "committed theme artifact revision is outside trusted ref ancestry"
        in error
        for error in errors
    )


def test_pr_safe_base_history_replays_only_unrelated_pr_changes(tmp_path: Path) -> None:
    write_current_formal_resolution_pair(tmp_path)
    unrelated = tmp_path / "tests/test_repo_production_inventory.py"
    unrelated.parent.mkdir(parents=True, exist_ok=True)
    unrelated.write_text("base control test\n", encoding="utf-8")
    initialize_git_fixture(tmp_path)
    watch_path = tmp_path / lineage.VOLUME_WATCH_ARTIFACT
    watch_columns, watch_rows = lineage._read_artifact(watch_path)
    watch_rows[0]["volume_breakout_type"] = "base_watch_v2"
    write_csv(watch_path, watch_columns, watch_rows)
    subprocess.run(
        ["git", "add", lineage.VOLUME_WATCH_ARTIFACT], cwd=tmp_path, check=True
    )
    subprocess.run(
        ["git", "commit", "-m", "advance watch at PR base"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    base_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    unrelated.write_text("PR control test\n", encoding="utf-8")
    subprocess.run(
        ["git", "add", "tests/test_repo_production_inventory.py"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "unrelated PR change"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    assert any(
        "formal presentation watch artifact SHA-256 mismatch" in error
        for error in lineage._validate_formal_resolution_lineage(tmp_path)
    )
    assert any(
        "formal presentation watch artifact SHA-256 mismatch" in error
        for error in lineage._validate_formal_resolution_lineage(
            tmp_path, trusted_ref=base_sha
        )
    )
    resolved, replay, evidence, errors = lineage._select_pr_safe_base_history(
        tmp_path, base_sha
    )
    assert errors == []
    assert replay is True
    assert resolved == base_sha
    assert "selected_mode=pr_safe_base_history" in evidence
    assert (
        lineage._validate_formal_resolution_lineage(
            tmp_path,
            trusted_ref=resolved,
            committed_refresh_mode=True,
        )
        == []
    )


def test_pr_safe_base_history_falls_back_for_governed_changes(tmp_path: Path) -> None:
    write_current_formal_resolution_pair(tmp_path)
    base_sha = initialize_git_fixture(tmp_path)
    raw_path = tmp_path / lineage.FORMAL_RAW_ARTIFACT
    raw_path.write_bytes(raw_path.read_bytes() + b"\n")
    subprocess.run(
        ["git", "add", lineage.FORMAL_RAW_ARTIFACT], cwd=tmp_path, check=True
    )
    subprocess.run(
        ["git", "commit", "-m", "change governed formal consumer"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    resolved, replay, evidence, errors = lineage._select_pr_safe_base_history(
        tmp_path, base_sha
    )
    assert errors == []
    assert replay is False
    assert resolved == base_sha
    assert "selected_mode=strict_current" in evidence
    assert any(lineage.FORMAL_RAW_ARTIFACT in item for item in evidence)


def test_pr_safe_base_history_rejects_governed_rename_and_delete(tmp_path: Path) -> None:
    write_current_formal_resolution_pair(tmp_path)
    base_sha = initialize_git_fixture(tmp_path)
    subprocess.run(
        [
            "git",
            "mv",
            lineage.FORMAL_REPORT_ARTIFACT,
            "output/latest/renamed_report.csv",
        ],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "rename governed consumer"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    _, replay, evidence, errors = lineage._select_pr_safe_base_history(
        tmp_path, base_sha
    )
    assert errors == []
    assert replay is False
    assert any("D:" + lineage.FORMAL_REPORT_ARTIFACT in item for item in evidence)
    assert any("A:output/latest/renamed_report.csv" in item for item in evidence)


def test_pr_safe_changed_path_parser_is_nul_safe_and_fail_closed() -> None:
    changes, errors = lineage._parse_pr_safe_changed_paths(
        b"M\0tests/ok.py\0T\0output/latest/volume_breakout_watch_latest.csv\0"
    )
    assert errors == []
    assert changes == [
        ("M", "tests/ok.py"),
        ("T", lineage.VOLUME_WATCH_ARTIFACT),
    ]
    for malformed in (
        b"M\0tests/unterminated.py",
        b"M\0",
        b"R100\0old.py\0new.py\0",
        b"M\0../escape.py\0",
        b"M\0bad\\path.py\0",
        b"M\0bad\xff.py\0",
    ):
        _, malformed_errors = lineage._parse_pr_safe_changed_paths(malformed)
        assert malformed_errors


@pytest.mark.parametrize("residue", ["staged", "unstaged", "untracked"])
def test_pr_safe_base_history_rejects_dirty_checkout(
    tmp_path: Path, residue: str
) -> None:
    write_current_formal_resolution_pair(tmp_path)
    base_sha = initialize_git_fixture(tmp_path)
    residue_path = tmp_path / "tests/residue.txt"
    residue_path.parent.mkdir(parents=True, exist_ok=True)
    residue_path.write_text("residue\n", encoding="utf-8")
    if residue == "staged":
        subprocess.run(["git", "add", "tests/residue.txt"], cwd=tmp_path, check=True)
    elif residue == "unstaged":
        subprocess.run(
            ["git", "add", "tests/residue.txt"], cwd=tmp_path, check=True
        )
        subprocess.run(
            ["git", "commit", "-m", "track residue"],
            cwd=tmp_path,
            check=True,
            capture_output=True,
        )
        residue_path.write_text("changed\n", encoding="utf-8")

    _, replay, _, errors = lineage._select_pr_safe_base_history(tmp_path, base_sha)
    assert replay is False
    assert any("staged, unstaged, or untracked residue" in error for error in errors)


def test_pr_safe_base_history_rejects_invalid_base_and_mode_combinations(
    tmp_path: Path,
) -> None:
    for base_ref in (None, "", "HEAD", "f" * 39, "G" * 40):
        _, replay, _, errors = lineage._select_pr_safe_base_history(tmp_path, base_ref)
        assert replay is False
        assert errors
    write_current_formal_resolution_pair(tmp_path)
    initialize_git_fixture(tmp_path)
    _, replay, _, errors = lineage._select_pr_safe_base_history(tmp_path, "f" * 40)
    assert replay is False
    assert any("unable to resolve" in error for error in errors)
    assert any(
        "mutually exclusive" in error
        for error in lineage.validate(
            tmp_path,
            base_ref="a" * 40,
            trusted_ref="b" * 40,
            pr_safe_base_history=True,
        )
    )


def test_pr_safe_base_history_rejects_nonancestor_base(tmp_path: Path) -> None:
    write_current_formal_resolution_pair(tmp_path)
    initialize_git_fixture(tmp_path)
    branch = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    subprocess.run(
        ["git", "checkout", "-b", "side"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "side commit"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    side_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    subprocess.run(
        ["git", "checkout", branch], cwd=tmp_path, check=True, capture_output=True
    )
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "main commit"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    _, replay, _, errors = lineage._select_pr_safe_base_history(tmp_path, side_sha)
    assert replay is False
    assert any("ancestor of HEAD" in error for error in errors)


def test_pr_safe_tree_entry_parser_rejects_type_and_identity_drift() -> None:
    path = "tests/test_repo_production_inventory.py"
    entry, errors = lineage._parse_pr_safe_tree_entry(
        f"100644 blob {'a' * 40}\t{path}\0".encode(), path
    )
    assert errors == []
    assert entry == ("100644", "blob", "a" * 40)
    for malformed in (
        f"120000 blob {'a' * 40}\t{path}\0".encode(),
        f"160000 commit {'a' * 40}\t{path}\0".encode(),
        f"100644 blob {'a' * 40}\ttests/wrong.py\0".encode(),
        f"100644 blob not-a-sha\t{path}\0".encode(),
        f"100644 blob {'a' * 40}\t{path}".encode(),
    ):
        parsed, malformed_errors = lineage._parse_pr_safe_tree_entry(malformed, path)
        if parsed is not None:
            assert parsed[:2] != ("100644", "blob")
        else:
            assert malformed_errors


def test_pr_safe_base_history_rejects_mode_drift_on_safe_path(tmp_path: Path) -> None:
    write_current_formal_resolution_pair(tmp_path)
    safe_path = tmp_path / "tests/test_repo_production_inventory.py"
    safe_path.parent.mkdir(parents=True, exist_ok=True)
    safe_path.write_text("control test\n", encoding="utf-8")
    base_sha = initialize_git_fixture(tmp_path)
    subprocess.run(
        ["git", "config", "core.filemode", "false"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "update-index", "--chmod=+x", "tests/test_repo_production_inventory.py"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "change safe path mode"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    _, replay, evidence, errors = lineage._select_pr_safe_base_history(
        tmp_path, base_sha
    )
    assert errors == []
    assert replay is False
    assert any("non_regular_blob" in item for item in evidence)


def test_pr_safe_base_history_rejects_replace_refs_and_grafts(tmp_path: Path) -> None:
    replace_root = tmp_path / "replace"
    write_current_formal_resolution_pair(replace_root)
    base_sha = initialize_git_fixture(replace_root)
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "replacement target"],
        cwd=replace_root,
        check=True,
        capture_output=True,
    )
    replacement_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=replace_root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    subprocess.run(
        ["git", "update-ref", f"refs/replace/{base_sha}", replacement_sha],
        cwd=replace_root,
        check=True,
    )
    _, replay, _, errors = lineage._select_pr_safe_base_history(
        replace_root, base_sha
    )
    assert replay is False
    assert any("refs/replace" in error for error in errors)

    graft_root = tmp_path / "graft"
    write_current_formal_resolution_pair(graft_root)
    graft_sha = initialize_git_fixture(graft_root)
    git_dir = subprocess.run(
        ["git", "rev-parse", "--git-dir"],
        cwd=graft_root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    graft_file = graft_root / git_dir / "info/grafts"
    graft_file.parent.mkdir(parents=True, exist_ok=True)
    graft_file.write_text(graft_sha + "\n", encoding="utf-8")
    _, replay, _, errors = lineage._select_pr_safe_base_history(graft_root, graft_sha)
    assert replay is False
    assert any("graft state" in error for error in errors)


def test_pr_safe_base_history_propagates_git_failure_and_malformed_output(
    tmp_path: Path, monkeypatch,
) -> None:
    original = lineage._run_git

    def failed_diff(root, args, *, operation):
        if operation == "collect PR-safe base-history changed paths":
            return subprocess.CompletedProcess(args, 1, b"", b"failed"), []
        return original(root, args, operation=operation)

    write_current_formal_resolution_pair(tmp_path)
    base_sha = initialize_git_fixture(tmp_path)
    monkeypatch.setattr(lineage, "_run_git", failed_diff)
    _, replay, _, errors = lineage._select_pr_safe_base_history(tmp_path, base_sha)
    assert replay is False
    assert any("cannot collect changed paths" in error for error in errors)

    def malformed_diff(root, args, *, operation):
        if operation == "collect PR-safe base-history changed paths":
            return subprocess.CompletedProcess(args, 0, b"M\0bad\xff.py\0", b""), []
        return original(root, args, operation=operation)

    monkeypatch.setattr(lineage, "_run_git", malformed_diff)
    _, replay, _, errors = lineage._select_pr_safe_base_history(tmp_path, base_sha)
    assert replay is False
    assert any("not valid UTF-8" in error for error in errors)


def test_pr_safe_base_history_propagates_git_timeout(tmp_path: Path, monkeypatch) -> None:
    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired(cmd="git", timeout=15)

    monkeypatch.setattr(lineage.subprocess, "run", timeout)
    _, replay, _, errors = lineage._select_pr_safe_base_history(tmp_path, "a" * 40)
    assert replay is False
    assert any("timed out" in error for error in errors)


def test_cli_forwards_pr_safe_mode_and_prints_selection(
    monkeypatch, tmp_path: Path, capsys
) -> None:
    observed = {}

    def fake_validate(
        root,
        *,
        base_ref,
        trusted_ref,
        pr_safe_base_history,
        runtime_scope,
        mode_evidence,
    ):
        observed.update(
            root=root,
            base_ref=base_ref,
            trusted_ref=trusted_ref,
            pr_safe_base_history=pr_safe_base_history,
            runtime_scope=runtime_scope,
        )
        mode_evidence.extend(
            ("resolved_base_sha=" + "a" * 40, "selected_mode=pr_safe_base_history")
        )
        return []

    monkeypatch.setattr(lineage, "validate", fake_validate)
    monkeypatch.setattr(
        "sys.argv",
        [
            "validate_daily_canonical_field_lineage.py",
            "--repo-root",
            str(tmp_path),
            "--base-ref",
            "a" * 40,
            "--pr-safe-base-history",
        ],
    )
    assert lineage.main() == 0
    assert observed == {
        "root": tmp_path,
        "base_ref": "a" * 40,
        "trusted_ref": None,
        "pr_safe_base_history": True,
        "runtime_scope": None,
    }
    assert "selected_mode=pr_safe_base_history" in capsys.readouterr().out


def test_cli_existing_modes_do_not_enable_pr_safe_history(
    monkeypatch, tmp_path: Path
) -> None:
    observed = []

    def fake_validate(
        root,
        *,
        base_ref,
        trusted_ref,
        pr_safe_base_history,
        runtime_scope,
        mode_evidence,
    ):
        observed.append((base_ref, trusted_ref, pr_safe_base_history, runtime_scope))
        return []

    monkeypatch.setattr(lineage, "validate", fake_validate)
    for argv in (
        ["validator", "--repo-root", str(tmp_path)],
        ["validator", "--repo-root", str(tmp_path), "--base-ref", "a" * 40],
        [
            "validator",
            "--repo-root",
            str(tmp_path),
            "--base-ref",
            "a" * 40,
            "--trusted-ref",
            "b" * 40,
        ],
    ):
        monkeypatch.setattr("sys.argv", argv)
        assert lineage.main() == 0
    assert observed == [
        (None, None, False, None),
        ("a" * 40, None, False, None),
        ("a" * 40, "b" * 40, False, None),
    ]


def test_runtime_scope_node_partitions_are_exact() -> None:
    assert len(lineage.GOVERNED_FIELD_NODES) == 65
    assert len(lineage.CURRENT_LINEAGE_NODES) == 42
    assert len(lineage.AUDIT_SOURCE_CURRENT_LINEAGE_NODES) == 41
    assert len(lineage.HISTORY_LINEAGE_NODES) == 23
    assert len(lineage.SNAPSHOT_HISTORY_LINEAGE_NODES) == 16
    assert len(lineage.LIFECYCLE_HISTORY_LINEAGE_NODES) == 7
    assert lineage.CURRENT_LINEAGE_NODES.isdisjoint(lineage.HISTORY_LINEAGE_NODES)
    assert (
        lineage.CURRENT_LINEAGE_NODES | lineage.HISTORY_LINEAGE_NODES
        == set(lineage.GOVERNED_FIELD_NODES)
    )
    assert (
        lineage.SNAPSHOT_HISTORY_LINEAGE_NODES
        | lineage.LIFECYCLE_HISTORY_LINEAGE_NODES
        == lineage.HISTORY_LINEAGE_NODES
    )
    assert lineage.OPERATION_CURRENT_NODE in lineage.CURRENT_LINEAGE_NODES
    assert lineage.OPERATION_CURRENT_NODE not in lineage.AUDIT_SOURCE_CURRENT_LINEAGE_NODES


@pytest.mark.parametrize("runtime_scope", ["audit-sources", "complete-current"])
def test_runtime_scopes_skip_historical_and_static_validators(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    runtime_scope: str,
) -> None:
    build_valid_repo(tmp_path)

    def forbidden(*_args, **_kwargs):
        raise AssertionError("historical/static validator must not run in runtime scope")

    for name in (
        "validate_migration_ledgers_append_only",
        "_validate_reverse_current_consumers",
        "_validate_migrations",
        "_validate_consumer_exclusion_migrations",
        "_validate_collision_migrations",
        "_validate_dispatcher_ast",
        "_validate_historical_projection",
        "_dispatcher_collision_field_sets",
    ):
        monkeypatch.setattr(lineage, name, forbidden)

    assert lineage.validate(tmp_path, runtime_scope=runtime_scope) == []


def test_no_arg_full_mode_still_calls_historical_and_static_validators(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    observed: set[str] = set()

    def record(name: str):
        def validator(*_args, **_kwargs):
            observed.add(name)
            return []

        return validator

    for name in (
        "_validate_reverse_current_consumers",
        "_validate_migrations",
        "_validate_collision_migrations",
        "_validate_dispatcher_ast",
        "_validate_historical_projection",
    ):
        monkeypatch.setattr(lineage, name, record(name))

    assert lineage.validate(tmp_path) == []
    assert observed == {
        "_validate_reverse_current_consumers",
        "_validate_migrations",
        "_validate_collision_migrations",
        "_validate_dispatcher_ast",
        "_validate_historical_projection",
    }


@pytest.mark.parametrize(
    "relative_path",
    [
        "output/history/warrant_flow/warrant_flow_20260717.csv",
        "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv",
        lineage.FORMAL_SIGNAL_LOG_ARTIFACT,
        lineage.MIGRATIONS_PATH.as_posix(),
    ],
)
def test_runtime_scopes_ignore_corrupt_historical_only_inputs(
    tmp_path: Path,
    relative_path: str,
) -> None:
    build_valid_repo(tmp_path)
    (tmp_path / relative_path).write_text("corrupt\n", encoding="utf-8")

    assert lineage.validate(tmp_path, runtime_scope="audit-sources") == []
    assert lineage.validate(tmp_path, runtime_scope="complete-current") == []
    assert lineage.validate(tmp_path)


@pytest.mark.parametrize(
    "mutation",
    [
        "registry_hash",
        "current_header",
        "source_row",
        "raw_report",
        "pinned_source",
        "collision",
    ],
)
def test_runtime_scopes_fail_closed_on_current_lineage_drift(
    tmp_path: Path,
    mutation: str,
) -> None:
    build_valid_repo(tmp_path)
    if mutation == "registry_hash":
        path = tmp_path / lineage.REGISTRY_PATH
        columns, rows = lineage._read_artifact(path)
        current = next(
            row for row in rows if row["artifact_path"].startswith("output/latest/")
        )
        current["contract_sha256"] = "0" * 64
        write_csv(path, columns, rows)
    elif mutation == "current_header":
        path = tmp_path / "output/latest/warrant_flow_latest.csv"
        columns, rows = lineage._read_artifact(path)
        columns.remove(lineage.FIELD_NAME)
        for row in rows:
            row.pop(lineage.FIELD_NAME, None)
        write_csv(path, columns, rows)
    elif mutation == "source_row":
        path = tmp_path / lineage.ALL_CANDIDATES_ARTIFACT
        columns, rows = lineage._read_artifact(path)
        rows[0]["candidate_source_row_sha256"] = "0" * 64
        write_csv(path, columns, rows)
    elif mutation == "raw_report":
        path = tmp_path / lineage.FORMAL_REPORT_ARTIFACT
        columns, rows = lineage._read_artifact(path)
        row = next(row for row in rows if row["model_id"] in lineage.VOLUME_V2_MODELS)
        row[lineage.FIELD_NAME] = "put_inflow"
        write_csv(path, columns, rows)
    elif mutation == "pinned_source":
        path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
        columns, rows = lineage._read_artifact(path)
        rows[0]["warrant_flow_official_source_sha256"] = "0" * 64
        write_csv(path, columns, rows)
    else:
        for relative in (lineage.ALL_CANDIDATES_ARTIFACT, lineage.VOLUME_WATCH_ARTIFACT):
            path = tmp_path / relative
            columns, rows = lineage._read_artifact(path)
            columns.append("runtime_collision_drift")
            for row in rows:
                row["runtime_collision_drift"] = "drift"
            write_csv(path, columns, rows)

    assert lineage.validate(tmp_path, runtime_scope="audit-sources")
    assert lineage.validate(tmp_path, runtime_scope="complete-current")


def test_operation_drift_only_blocks_complete_current_runtime_scope(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / "output/latest/daily_volume_breakout_operation_section_latest.csv"
    columns, rows = lineage._read_artifact(path)
    rows[0]["final_rank_score"] = "999"
    write_csv(path, columns, rows)

    assert lineage.validate(tmp_path, runtime_scope="audit-sources") == []
    errors = lineage.validate(tmp_path, runtime_scope="complete-current")
    assert any("current_operation" in error for error in errors)


def test_runtime_audit_requires_selected_current_file_in_worktree(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    (tmp_path / "output/latest/warrant_flow_latest.csv").unlink()

    errors = lineage.validate(tmp_path, runtime_scope="audit-sources")
    assert "runtime selected current artifact is missing: output/latest/warrant_flow_latest.csv" in errors


def test_runtime_audit_rejects_unreadable_selected_current_file(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    target = tmp_path / "output/latest/warrant_flow_latest.csv"
    original_open = Path.open

    def deny_binary_read(path: Path, mode: str = "r", *args, **kwargs):
        if path == target and mode == "rb":
            raise PermissionError("blocked by regression")
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", deny_binary_read)
    errors = lineage.validate(tmp_path, runtime_scope="audit-sources")
    assert any(
        "runtime selected current artifact is unreadable: "
        "output/latest/warrant_flow_latest.csv" in error
        for error in errors
    )


def test_runtime_complete_requires_operation_file_but_audit_does_not(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    operation_path = (
        tmp_path / "output/latest/daily_volume_breakout_operation_section_latest.csv"
    )
    operation_path.unlink()

    assert lineage.validate(tmp_path, runtime_scope="audit-sources") == []
    errors = lineage.validate(tmp_path, runtime_scope="complete-current")
    assert any(
        "runtime selected current artifact is missing: "
        "output/latest/daily_volume_breakout_operation_section_latest.csv" in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("runtime_scope", "expected_missing"),
    [("audit-sources", 41), ("complete-current", 42)],
)
def test_runtime_scope_rejects_header_only_zero_row_registry(
    tmp_path: Path,
    runtime_scope: str,
    expected_missing: int,
) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.REGISTRY_PATH
    columns, _rows = lineage._read_artifact(path)
    write_csv(path, columns, [])

    errors = lineage.validate(tmp_path, runtime_scope=runtime_scope)
    node_error = next(
        error
        for error in errors
        if "canonical field registry governed volume-v2 node set mismatch" in error
    )
    assert node_error.count("(") >= expected_missing


@pytest.mark.parametrize("runtime_scope", ["audit-sources", "complete-current"])
def test_runtime_scope_rejects_header_only_zero_row_collision_registry(
    tmp_path: Path,
    runtime_scope: str,
) -> None:
    build_valid_repo(tmp_path)
    path = tmp_path / lineage.COLLISION_REGISTRY_PATH
    columns, _rows = lineage._read_artifact(path)
    write_csv(path, columns, [])

    errors = lineage.validate(tmp_path, runtime_scope=runtime_scope)
    assert any(
        "unregistered volume-v2 dispatcher same-name collision" in error
        for error in errors
    )


def test_cli_runtime_scope_is_forwarded_and_mutually_exclusive(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    observed: list[str | None] = []

    def fake_validate(
        root,
        *,
        base_ref,
        trusted_ref,
        pr_safe_base_history,
        runtime_scope,
        mode_evidence,
    ):
        observed.append(runtime_scope)
        return []

    monkeypatch.setattr(lineage, "validate", fake_validate)
    monkeypatch.setattr(
        "sys.argv",
        [
            "validator",
            "--repo-root",
            str(tmp_path),
            "--runtime-scope",
            "audit-sources",
        ],
    )
    assert lineage.main() == 0
    assert observed == ["audit-sources"]
    assert "scope=runtime_audit_sources governed_nodes=41" in capsys.readouterr().out

    for extra in (
        ["--base-ref", "a" * 40],
        ["--trusted-ref", "a" * 40],
        ["--pr-safe-base-history"],
    ):
        monkeypatch.setattr(
            "sys.argv",
            ["validator", "--runtime-scope", "complete-current", *extra],
        )
        with pytest.raises(SystemExit):
            lineage.main()


def test_theme_accepts_true_uncommitted_live_source_pair(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    trusted_base = initialize_git_fixture(tmp_path)
    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    official_columns, official_rows = lineage._read_artifact(official_path)
    official_rows.append(
        {
            "date": official_rows[0]["date"],
            "stock_id": "9999",
            "warrant_flow_signal": "",
        }
    )
    write_csv(official_path, official_columns, official_rows)
    live_source_sha = lineage._canonical_text_sha256(official_path.read_bytes())
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    theme_columns, theme_rows = lineage._read_artifact(theme_path)
    for row in theme_rows:
        row["warrant_flow_official_source_sha256"] = live_source_sha
    write_csv(theme_path, theme_columns, theme_rows)

    assert (
        lineage._validate_current_projection(
            tmp_path,
            trusted_ref=trusted_base,
        )
        == []
    )


def test_theme_rejects_live_consumer_with_branch_committed_untrusted_source(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    trusted_base = initialize_git_fixture(tmp_path)
    official_path = tmp_path / "output/latest/warrant_flow_latest.csv"
    official_columns, official_rows = lineage._read_artifact(official_path)
    official_rows.append(
        {
            "date": official_rows[0]["date"],
            "stock_id": "9999",
            "warrant_flow_signal": "",
        }
    )
    write_csv(official_path, official_columns, official_rows)
    branch_source_sha = lineage._canonical_text_sha256(official_path.read_bytes())
    subprocess.run(
        ["git", "add", "output/latest/warrant_flow_latest.csv"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "branch-only official source"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    theme_path = tmp_path / lineage.THEME_ADVISORY_ARTIFACT
    theme_columns, theme_rows = lineage._read_artifact(theme_path)
    for row in theme_rows:
        row["warrant_flow_official_source_sha256"] = branch_source_sha
    write_csv(theme_path, theme_columns, theme_rows)

    errors = lineage._validate_current_projection(
        tmp_path,
        trusted_ref=trusted_base,
    )

    assert any(
        "theme advisory official warrant source revision cannot be validated"
        in error
        and "not reconstructable" in error
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
    manifest_path = (
        tmp_path
        / "output/history/daily_model_snapshots/"
        "daily_published_model_snapshot_manifest.csv"
    )
    columns, rows = lineage._read_artifact(manifest_path)
    write_csv(
        manifest_path,
        columns,
        [row for row in rows if row["artifact_id"] != "model_signals_for_report"],
    )

    errors = lineage.validate(tmp_path)

    assert "historical parity has no formal report snapshots" in errors


def test_historical_parity_selects_same_day_manifest_max_revisions(
    tmp_path: Path,
) -> None:
    build_valid_repo(tmp_path)
    snapshot_dir = tmp_path / "output/history/daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    candidate_r1 = snapshot_dir / "all_candidates_20260717.csv"
    report_r1 = snapshot_dir / "daily_candidate_model_signals_for_report_20260717.csv"
    for path in (candidate_r1, report_r1):
        columns, rows = lineage._read_artifact(path)
        rows[0]["warrant_flow_signal"] = "no_signal"
        write_csv(path, columns, rows)
    candidate_r1_sha = snapshot_file_sha256(candidate_r1)
    report_r1_sha = snapshot_file_sha256(report_r1)
    candidate_columns, candidate_rows = lineage._read_artifact(
        tmp_path / "output/latest/all_candidates_latest.csv"
    )
    candidate_staging = snapshot_dir / "candidate-r2-staging.csv"
    write_csv(candidate_staging, candidate_columns, candidate_rows)
    candidate_r2_sha = snapshot_file_sha256(candidate_staging)
    candidate_r2 = snapshot_dir / (
        f"all_candidates_20260717_r2_{candidate_r2_sha[:12]}.csv"
    )
    candidate_staging.rename(candidate_r2)
    report_columns, report_rows = lineage._read_artifact(
        tmp_path / "output/latest/daily_candidate_model_signals_for_report_latest.csv"
    )
    report_staging = snapshot_dir / "report-r2-staging.csv"
    write_csv(report_staging, report_columns, report_rows)
    report_r2_sha = snapshot_file_sha256(report_staging)
    report_r2 = snapshot_dir / (
        "daily_candidate_model_signals_for_report_"
        f"20260717_r2_{report_r2_sha[:12]}.csv"
    )
    report_staging.rename(report_r2)
    columns, manifest_rows = lineage._read_artifact(manifest_path)
    for row in manifest_rows:
        if row["artifact_id"] == "all_candidates_source_rows":
            row["snapshot_sha256"] = candidate_r1_sha
        elif row["artifact_id"] == "model_signals_for_report":
            row["snapshot_sha256"] = report_r1_sha
    manifest_rows.extend(
        [
            {
                "snapshot_report_date": "20260717",
                "snapshot_revision": "r2",
                "supersedes_snapshot_sha256": candidate_r1_sha,
                "revision_reason": "same_day_candidate_correction",
                "artifact_id": "all_candidates_source_rows",
                "snapshot_path": candidate_r2.relative_to(tmp_path).as_posix(),
                "snapshot_sha256": candidate_r2_sha,
            },
            {
                "snapshot_report_date": "20260717",
                "snapshot_revision": "r2",
                "supersedes_snapshot_sha256": report_r1_sha,
                "revision_reason": "same_day_report_correction",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": report_r2.relative_to(tmp_path).as_posix(),
                "snapshot_sha256": report_r2_sha,
            },
        ]
    )
    write_csv(manifest_path, columns, manifest_rows)

    assert lineage.validate(tmp_path) == []


@pytest.mark.parametrize(
    ("relative_path", "tamper"),
    [
        (lineage.MIGRATIONS_PATH, "rewrite_notes"),
        (
            lineage.CONSUMER_EXCLUSION_MIGRATIONS_PATH,
            "rewrite_validation_commands",
        ),
        (lineage.MIGRATIONS_PATH, "reorder"),
        (lineage.COLLISION_MIGRATIONS_PATH, "delete"),
    ],
)
def test_migration_ledgers_reject_base_row_tampering(
    tmp_path: Path,
    relative_path: Path,
    tamper: str,
) -> None:
    build_valid_repo(tmp_path)
    base_sha = initialize_git_fixture(tmp_path)
    path = tmp_path / relative_path
    columns, rows = lineage._read_artifact(path)
    if tamper == "rewrite_notes":
        rows[0]["notes"] = "tampered historical migration note"
    elif tamper == "rewrite_validation_commands":
        rows[0]["validation_commands"] = "python tampered_validator.py"
    elif tamper == "reorder":
        rows[0], rows[1] = rows[1], rows[0]
    elif tamper == "delete":
        rows.pop(0)
    else:  # pragma: no cover - the parametrization is the contract.
        raise AssertionError(f"unsupported test tamper: {tamper}")
    write_csv(path, columns, rows)

    errors = lineage.validate_migration_ledgers_append_only(tmp_path, base_sha)

    assert any(
        f"{relative_path.as_posix()} is append-only" in error for error in errors
    )


def test_append_only_validation_accepts_ledgers_absent_from_real_base_tree(
    tmp_path: Path,
) -> None:
    base_sha = initialize_git_fixture(tmp_path, empty_commit=True)
    build_valid_repo(tmp_path)

    assert lineage.validate_migration_ledgers_append_only(tmp_path, base_sha) == []


def test_append_only_validation_rejects_unresolvable_base_ref(tmp_path: Path) -> None:
    build_valid_repo(tmp_path)
    initialize_git_fixture(tmp_path)

    errors = lineage.validate_migration_ledgers_append_only(
        tmp_path,
        "missing-base-ref",
    )

    assert any(
        "cannot resolve append-only migration validation base" in error
        for error in errors
    )


def test_explicit_trusted_ref_accepts_one_clean_direct_child(tmp_path: Path) -> None:
    base_sha = initialize_git_fixture(tmp_path, empty_commit=True)
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "bounded refresh"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    trusted_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    resolved, errors = lineage._validate_explicit_trusted_ref_boundary(
        tmp_path,
        base_sha,
        trusted_sha,
    )

    assert errors == []
    assert resolved == trusted_sha


def test_explicit_trusted_ref_rejects_non_direct_child(tmp_path: Path) -> None:
    base_sha = initialize_git_fixture(tmp_path, empty_commit=True)
    for message in ("bounded refresh", "unexpected extra commit"):
        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", message],
            cwd=tmp_path,
            check=True,
            capture_output=True,
        )

    resolved, errors = lineage._validate_explicit_trusted_ref_boundary(
        tmp_path,
        base_sha,
        "HEAD",
    )

    assert resolved is None
    assert any("direct single-parent child" in error for error in errors)
    assert any("exactly one committed revision" in error for error in errors)


def test_explicit_trusted_ref_rejects_uncommitted_residue(tmp_path: Path) -> None:
    base_sha = initialize_git_fixture(tmp_path, empty_commit=True)
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "bounded refresh"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    (tmp_path / "untracked-residue.txt").write_text("not committed\n", encoding="utf-8")

    resolved, errors = lineage._validate_explicit_trusted_ref_boundary(
        tmp_path,
        base_sha,
        "HEAD",
    )

    assert resolved is None
    assert any("forbids staged, unstaged, or untracked residue" in error for error in errors)


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
    hashes[0] = "0" * 64
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

    daily_full = contents["daily_full"]
    audit_validation = f"{canonical_validation} --runtime-scope audit-sources"
    complete_validation = f"{canonical_validation} --runtime-scope complete-current"
    operation_artifact_name = Path(lineage.OPERATION_CURRENT_NODE[1]).name
    operation_build = (
        "python scripts/build_"
        f"{operation_artifact_name.removesuffix('_latest.csv')}.py"
    )
    assert daily_full.count(audit_validation) == 1
    assert daily_full.count(complete_validation) == 1
    assert daily_full.index(model_build) < daily_full.index(audit_validation)
    assert daily_full.index(audit_validation) < daily_full.index(operation_build)
    assert daily_full.index(operation_build) < daily_full.index(complete_validation)
    assert contents["warrant_flow"].count("--runtime-scope") == 0

    theme_build = "python scripts/build_volume_attack_theme_layer.py"
    warrant_workflow = contents["warrant_flow"]
    assert warrant_workflow.count(theme_build) == 1
    assert warrant_workflow.index(theme_build) < warrant_workflow.index(model_build)
def test_pr_safe_base_history_safe_paths_reject_near_misses() -> None:
    import hashlib

    from scripts import validate_daily_canonical_field_lineage as lineage

    safe_paths = lineage.PR_SAFE_BASE_HISTORY_SAFE_CONTROL_PATHS
    safe_path_identity = ("\n".join(sorted(safe_paths)) + "\n").encode("utf-8")
    assert len(safe_paths) == 16
    assert hashlib.sha256(safe_path_identity).hexdigest() == (
        "b37d1ee652dde9424b2bbbe422060bd33532b90a1256005b0a18a5ebe5625fe0"
    )
    retired_ledger_path = (
        "config/daily_model_pr_safe_self_"
        "migration_authorizations.csv"
    )
    assert retired_ledger_path not in safe_paths
    for path in sorted(safe_paths):
        near_misses = {
            f"{path}.bak",
            f"{path}/child",
            path.swapcase(),
            path.replace("/", "\\"),
        }
        assert path not in near_misses
        for near_miss in near_misses:
            assert near_miss not in safe_paths
            assert lineage._is_pr_safe_base_history_governed_path(near_miss)


def test_all_validator_git_subprocesses_disable_replace_objects() -> None:
    import ast
    from pathlib import Path

    source_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "validate_daily_canonical_field_lineage.py"
    )
    tree = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
    subprocess_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "subprocess"
        and node.func.attr == "run"
    ]

    assert len(subprocess_calls) == 10
    for call in subprocess_calls:
        assert call.args
        command = call.args[0]
        assert isinstance(command, (ast.List, ast.Tuple))
        assert len(command.elts) >= 2
        assert isinstance(command.elts[0], ast.Constant)
        assert command.elts[0].value == "git"
        assert isinstance(command.elts[1], ast.Constant)
        assert command.elts[1].value == "--no-replace-objects"
