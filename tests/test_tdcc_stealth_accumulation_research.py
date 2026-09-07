from __future__ import annotations

import ast
import csv
import hashlib
import io
from datetime import date, timedelta
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_tdcc_stealth_accumulation_research as producer  # noqa: E402
import validate_tdcc_stealth_accumulation_research as validator  # noqa: E402


SIGNAL_FIELDS = [
    "signal_date",
    "report_line",
    "report_bucket",
    "stock_id",
    "stock_name",
    "model_id",
    "model_score",
    "model_rank",
    "display_rank",
    "selection_semantics",
    "entry_basis",
    "main_condition_met",
    "tdcc_price_phase",
    "tdcc_status",
]
MANIFEST_FIELDS = [
    "snapshot_report_date",
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
    "generated_at",
    "pipeline_commit_sha",
    "main_price_date",
    "report_ready",
    "warrant_ready",
    "warrant_source_status",
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
    "warrant_model_effect_allowed",
    "warrant_pdf_effect_allowed",
    "daily_pdf_ready",
    "artifact_id",
    "source_path",
    "snapshot_path",
    "source_sha256",
    "snapshot_sha256",
    "row_count",
    "column_count",
    "purpose",
]


def _csv_payload(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def _write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> bytes:
    payload = _csv_payload(fields, rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return payload


def _signal(
    signal_date: str,
    stock_id: str,
    model_id: str,
    *,
    report_line: str = "mainstream",
    report_bucket: str = "mainstream",
    model_score: str = "75.5",
) -> dict[str, str]:
    return {
        "signal_date": signal_date,
        "report_line": report_line,
        "report_bucket": report_bucket,
        "stock_id": stock_id,
        "stock_name": f"stock-{stock_id}",
        "model_id": model_id,
        "model_score": model_score,
        "model_rank": "1",
        "display_rank": "1",
        "selection_semantics": "actual_published_recommendation",
        "entry_basis": "signal_date_next_open",
        "main_condition_met": "True",
        "tdcc_price_phase": "tdcc_leading_price",
        "tdcc_status": "accumulation",
    }


def _snapshot(
    root: Path,
    report_date: str,
    revision: str,
    rows: list[dict[str, str]],
    *,
    supersedes: str = "",
) -> tuple[dict[str, str], Path]:
    payload = _csv_payload(SIGNAL_FIELDS, rows)
    sha = hashlib.sha256(payload).hexdigest()
    name = (
        f"daily_candidate_model_signals_for_report_{report_date}_{revision}_{sha[:12]}.csv"
    )
    relative = Path("output") / "history" / "daily_model_snapshots" / name
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    row = {
        "snapshot_report_date": report_date,
        "snapshot_revision": revision,
        "supersedes_snapshot_sha256": supersedes,
        "revision_reason": "fixture_initial" if revision == "r1" else "fixture_correction",
        "generated_at": f"{report_date} 18:00:00 Asia/Taipei",
        "pipeline_commit_sha": "a" * 40,
        "main_price_date": report_date,
        "report_ready": "True",
        "warrant_ready": "True",
        "warrant_source_status": "ok",
        "warrant_daily_publish_allowed": "True",
        "warrant_pdf_visibility": "visible",
        "warrant_model_effect_allowed": "True",
        "warrant_pdf_effect_allowed": "True",
        "daily_pdf_ready": "True",
        "artifact_id": "model_signals_for_report",
        "source_path": "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "snapshot_path": relative.as_posix(),
        "source_sha256": sha,
        "snapshot_sha256": sha,
        "row_count": str(len(rows)),
        "column_count": str(len(SIGNAL_FIELDS)),
        "purpose": "as_published_daily_model_snapshot",
    }
    return row, path


def _business_dates(start: str, count: int) -> list[str]:
    cursor = date.fromisoformat(f"{start[:4]}-{start[4:6]}-{start[6:]}")
    dates: list[str] = []
    while len(dates) < count:
        cursor += timedelta(days=1)
        if cursor.weekday() < 5:
            dates.append(cursor.strftime("%Y%m%d"))
    return dates


def _write_price(
    root: Path,
    stock_id: str,
    signal_date: str,
    d20_close: str,
    *,
    future_count: int = 25,
) -> None:
    fields = ["date", "stock_id", "open", "high", "low", "close", "volume"]
    rows = [
        {
            "date": signal_date,
            "stock_id": stock_id,
            "open": "99",
            "high": "100",
            "low": "98",
            "close": "99",
            "volume": "1000",
        }
    ]
    for index, trading_date in enumerate(
        _business_dates(signal_date, future_count), start=1
    ):
        close = "105" if index == 5 else "110" if index == 10 else d20_close if index == 20 else "101"
        rows.append(
            {
                "date": trading_date,
                "stock_id": stock_id,
                "open": "100",
                "high": close,
                "low": "99",
                "close": close,
                "volume": "1000",
            }
        )
    _write_csv(root / "data" / "stock_price_history" / f"{stock_id}.csv", fields, rows)


def _fixture_repo(
    tmp_path: Path,
    *,
    include_target: bool = True,
    duplicate_first_target: bool = False,
    first_snapshot_signal_date: str = "20260102",
) -> tuple[Path, Path, list[dict[str, str]], list[Path]]:
    root = tmp_path / "repo"
    other_model = "platform_strengthening"
    r1, r1_path = _snapshot(
        root,
        "20260102",
        "r1",
        [_signal(first_snapshot_signal_date, "9999", other_model)],
    )
    r2_rows = (
        [_signal("20260102", "2330", producer.MODEL_ID)]
        if include_target
        else [_signal("20260102", "2330", other_model)]
    )
    if duplicate_first_target and include_target:
        r2_rows.append(
            _signal(
                "20260102",
                "2330",
                producer.MODEL_ID,
                report_line="non_mainstream",
                report_bucket="non_mainstream",
            )
        )
    r2, r2_path = _snapshot(
        root,
        "20260102",
        "r2",
        r2_rows,
        supersedes=r1["snapshot_sha256"],
    )
    second_rows = [_signal("20260105", "2317", producer.MODEL_ID)] if include_target else [
        _signal("20260105", "2317", other_model)
    ]
    second, second_path = _snapshot(root, "20260105", "r1", second_rows)
    manifest_rows = [r1, r2, second]
    manifest_path = (
        root
        / "output"
        / "history"
        / "daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    _write_csv(manifest_path, MANIFEST_FIELDS, manifest_rows)
    if include_target:
        _write_price(root, "2330", "20260102", "200")
        _write_price(root, "2317", "20260105", "110")
    return root, manifest_path, manifest_rows, [r1_path, r2_path, second_path]


def _artifact_paths(tmp_path: Path) -> tuple[Path, Path]:
    artifact_dir = tmp_path / "artifacts"
    return (
        artifact_dir / producer.DETAIL_ARTIFACT_NAME,
        artifact_dir / producer.SUMMARY_ARTIFACT_NAME,
    )


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _read_fields(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return next(csv.reader(handle))


def test_exact_actual_recommendation_replay_uses_latest_revision_and_retains_anomaly(
    tmp_path: Path,
) -> None:
    root, manifest, _, _ = _fixture_repo(tmp_path)
    detail_path, summary_path = _artifact_paths(tmp_path)

    detail, summary = producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )

    assert [(row["signal_date"], row["stock_id"]) for row in detail] == [
        ("20260102", "2330"),
        ("20260105", "2317"),
    ]
    assert detail[0]["snapshot_revision"] == "r2"
    assert detail[0]["entry_date"] == "20260105"
    assert detail[0]["return_d5_pct"] == "5.000000"
    assert detail[0]["return_d10_pct"] == "10.000000"
    assert detail[0]["return_d20_pct"] == "100.000000"
    assert detail[0]["anomaly_candidate"] == "True"
    assert detail[0]["anomaly_disposition"] == "unresolved_anomaly_candidate"
    assert detail[0]["retained_in_primary"] == "True"
    assert all(len(detail[0][field]) == 64 for field in [
        "published_source_row_sha256",
        "snapshot_sha256",
        "snapshot_canonical_sha256",
        "price_source_sha256",
        "entry_price_row_sha256",
        "exit_d20_price_row_sha256",
    ])
    d20 = next(row for row in summary if row["horizon"] == "d20")
    assert d20["evaluated_count"] == "2"
    assert d20["average_return_pct"] == "55.000000"
    assert d20["unresolved_anomaly_candidate_count"] == "1"
    assert d20["primary_metric_basis"] == "including_unresolved_anomaly_candidates"
    assert d20["sensitivity_evaluated_count"] == "1"
    assert d20["sensitivity_excluded_anomaly_candidate_count"] == "1"
    assert d20["sensitivity_average_return_pct"] == "10.000000"
    assert d20["sensitivity_is_corrected_primary"] == "False"
    assert d20["formal_use"] == "False"
    assert d20["trade_eligible"] == "False"
    assert d20["promotion_evidence_allowed"] == "False"
    assert d20["promotion_status"] == "blocked"
    assert "phase_classifier_unresolved" in d20["promotion_blockers"]
    assert "formal_operation_decision_required" in d20["promotion_blockers"]
    assert validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    ) == []


def test_validate_rejects_non_exact_or_reordered_artifact_headers(tmp_path: Path) -> None:
    root, manifest, _, _ = _fixture_repo(tmp_path)
    detail_path, summary_path = _artifact_paths(tmp_path)
    producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    artifacts = {"detail": detail_path, "summary": summary_path}
    original_payloads = {path: path.read_bytes() for path in artifacts.values()}

    for label, artifact_path in artifacts.items():
        for mutation in ("missing", "extra", "reordered", "duplicate"):
            for path, payload in original_payloads.items():
                path.write_bytes(payload)
            fields = _read_fields(artifact_path)
            rows = _read_rows(artifact_path)
            if mutation == "missing":
                mutated_fields = fields[:-1]
            elif mutation == "extra":
                mutated_fields = [*fields, "unexpected_schema_column"]
            elif mutation == "reordered":
                mutated_fields = [fields[1], fields[0], *fields[2:]]
            elif mutation == "duplicate":
                mutated_fields = [fields[0], fields[0], *fields[1:]]
            else:  # pragma: no cover - mutation tuple is exhaustive
                raise AssertionError(mutation)
            projected_rows = [
                {field: row.get(field, "") for field in mutated_fields}
                for row in rows
            ]
            _write_csv(artifact_path, mutated_fields, projected_rows)

            errors = validator.validate(
                repository_root=root,
                manifest_path=manifest,
                price_dir=root / "data" / "stock_price_history",
                detail_path=detail_path,
                summary_path=summary_path,
            )

            assert (
                f"{label} schema does not exactly match v1 contract" in errors
            ), f"{label}/{mutation}: {errors}"


def test_cross_surface_duplicate_preserves_lineage_but_primary_is_deduped(
    tmp_path: Path,
) -> None:
    root, manifest, _, _ = _fixture_repo(
        tmp_path, duplicate_first_target=True
    )
    detail_path, summary_path = _artifact_paths(tmp_path)

    detail, summary = producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )

    assert len(detail) == 3
    duplicated = [row for row in detail if row["stock_id"] == "2330"]
    assert len(duplicated) == 2
    assert {row["signal_event_id"] for row in duplicated} == {
        duplicated[0]["signal_event_id"]
    }
    assert [row["source_presentation_ordinal"] for row in duplicated] == ["1", "2"]
    assert {row["source_presentation_count"] for row in duplicated} == {"2"}
    assert [row["primary_metric_included"] for row in duplicated] == ["True", "False"]
    assert [row["retained_in_primary"] for row in duplicated] == ["True", "False"]
    assert all(
        len(row["source_presentation_row_sha256s"].split(";")) == 2
        for row in duplicated
    )
    assert all(
        row["source_presentation_surfaces"]
        == "mainstream|mainstream;non_mainstream|non_mainstream"
        for row in duplicated
    )
    d20 = next(row for row in summary if row["horizon"] == "d20")
    assert d20["source_presentation_row_count"] == "3"
    assert d20["actual_recommendation_row_count"] == "2"
    assert d20["unique_signal_event_count"] == "2"
    assert d20["duplicate_source_presentation_count"] == "1"
    assert d20["evaluated_count"] == "2"
    assert d20["average_return_pct"] == "55.000000"
    assert validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    ) == []


def test_summary_reports_per_horizon_right_censoring(tmp_path: Path) -> None:
    root, manifest, _, _ = _fixture_repo(tmp_path)
    _write_price(
        root,
        "2317",
        "20260105",
        "110",
        future_count=7,
    )
    detail_path, summary_path = _artifact_paths(tmp_path)
    _, summary = producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )

    by_horizon = {row["horizon"]: row for row in summary}
    assert by_horizon["d5"]["evaluated_count"] == "2"
    assert by_horizon["d5"]["right_censored_count"] == "0"
    assert by_horizon["d10"]["evaluated_count"] == "1"
    assert by_horizon["d10"]["right_censored_count"] == "1"
    assert by_horizon["d20"]["evaluated_count"] == "1"
    assert by_horizon["d20"]["right_censored_count"] == "1"
    assert {row["invalid_price_count"] for row in summary} == {"0"}
    assert validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    ) == []


def test_zero_target_snapshot_coverage_is_an_explicit_blocked_result(tmp_path: Path) -> None:
    root, manifest, _, _ = _fixture_repo(tmp_path, include_target=False)
    detail_path, summary_path = _artifact_paths(tmp_path)
    detail, summary = producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    assert detail == []
    assert len(summary) == 3
    assert {row["actual_recommendation_row_count"] for row in summary} == {"0"}
    assert {row["evidence_status"] for row in summary} == {"no_actual_recommendation_rows"}
    assert all("no_published_tdcc_stealth_signal_rows" in row["promotion_blockers"] for row in summary)
    assert validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    ) == []


def test_revision_chain_mismatch_fails_closed(tmp_path: Path) -> None:
    root, manifest, manifest_rows, _ = _fixture_repo(tmp_path)
    manifest_rows[1]["supersedes_snapshot_sha256"] = "f" * 64
    _write_csv(manifest, MANIFEST_FIELDS, manifest_rows)
    detail_path, summary_path = _artifact_paths(tmp_path)
    with pytest.raises(RuntimeError, match="supersedes_snapshot_sha256 mismatch"):
        producer.produce(
            repository_root=root,
            manifest_path=manifest,
            price_dir=root / "data" / "stock_price_history",
            detail_path=detail_path,
            summary_path=summary_path,
        )


@pytest.mark.parametrize("failure", ["snapshot_hash", "row_count"])
def test_snapshot_hash_and_row_count_fail_closed(tmp_path: Path, failure: str) -> None:
    root, manifest, manifest_rows, snapshot_paths = _fixture_repo(tmp_path)
    if failure == "snapshot_hash":
        snapshot_paths[1].write_bytes(snapshot_paths[1].read_bytes() + b"\n")
        expected = "snapshot SHA-256 mismatch"
    else:
        manifest_rows[1]["row_count"] = "999"
        _write_csv(manifest, MANIFEST_FIELDS, manifest_rows)
        expected = "snapshot row_count mismatch"
    detail_path, summary_path = _artifact_paths(tmp_path)
    with pytest.raises(RuntimeError, match=expected):
        producer.produce(
            repository_root=root,
            manifest_path=manifest,
            price_dir=root / "data" / "stock_price_history",
            detail_path=detail_path,
            summary_path=summary_path,
        )


def test_independent_validator_rejects_tampered_return(tmp_path: Path) -> None:
    root, manifest, _, _ = _fixture_repo(tmp_path)
    detail_path, summary_path = _artifact_paths(tmp_path)
    producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    detail_rows = _read_rows(detail_path)
    detail_rows[0]["return_d5_pct"] = "999.000000"
    _write_csv(detail_path, producer.DETAIL_FIELDS, detail_rows)
    errors = validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    assert any("return_d5_pct mismatch" in error for error in errors)


def test_validator_rejects_cross_surface_lineage_and_anomaly_tamper(
    tmp_path: Path,
) -> None:
    root, manifest, _, _ = _fixture_repo(
        tmp_path, duplicate_first_target=True
    )
    detail_path, summary_path = _artifact_paths(tmp_path)
    producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    original = _read_rows(detail_path)

    lineage = [dict(row) for row in original]
    lineage[0]["snapshot_revision"] = "r1"
    lineage[0]["published_source_row_sha256"] = "0" * 64
    lineage[0]["source_presentation_count"] = "99"
    _write_csv(detail_path, producer.DETAIL_FIELDS, lineage)
    lineage_errors = validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    assert any("snapshot_revision mismatch" in error for error in lineage_errors)
    assert any("published_source_row_sha256 mismatch" in error for error in lineage_errors)
    assert any("source_presentation_count mismatch" in error for error in lineage_errors)

    anomaly = [dict(row) for row in original]
    candidate_index = next(
        index
        for index, row in enumerate(anomaly)
        if row["stock_id"] == "2330" and row["primary_metric_included"] == "True"
    )
    anomaly[candidate_index]["anomaly_candidate"] = "False"
    anomaly[candidate_index]["anomaly_trigger_codes"] = ""
    anomaly[candidate_index]["anomaly_disposition"] = "not_anomaly_candidate"
    _write_csv(detail_path, producer.DETAIL_FIELDS, anomaly)
    anomaly_errors = validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    assert any("anomaly_candidate mismatch" in error for error in anomaly_errors)
    assert any("anomaly_trigger_codes mismatch" in error for error in anomaly_errors)


def test_validator_rejects_formal_promotion_and_sensitivity_tamper(
    tmp_path: Path,
) -> None:
    root, manifest, _, _ = _fixture_repo(tmp_path)
    detail_path, summary_path = _artifact_paths(tmp_path)
    producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    detail = _read_rows(detail_path)
    summary = _read_rows(summary_path)
    detail[0]["formal_use"] = "True"
    detail[0]["trade_eligible"] = "True"
    detail[0]["promotion_evidence_allowed"] = "True"
    detail[0]["operation_decision_status"] = "approved"
    summary[0]["formal_use"] = "True"
    summary[0]["trade_eligible"] = "True"
    summary[0]["promotion_evidence_allowed"] = "True"
    summary[0]["operation_decision_status"] = "approved"
    summary[0]["promotion_status"] = "approved"
    summary[0]["sensitivity_is_corrected_primary"] = "True"
    _write_csv(detail_path, producer.DETAIL_FIELDS, detail)
    _write_csv(summary_path, producer.SUMMARY_FIELDS, summary)

    errors = validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )

    assert any("formal_use" in error for error in errors)
    assert any("trade_eligible" in error for error in errors)
    assert any("promotion_evidence_allowed" in error for error in errors)
    assert any("operation_decision_status" in error for error in errors)
    assert any("promotion_status" in error for error in errors)
    assert any("corrected primary" in error for error in errors)


def test_repo_internal_attacker_manifest_is_rejected_by_producer_and_validator(
    tmp_path: Path,
) -> None:
    root, manifest, _, _ = _fixture_repo(tmp_path)
    detail_path, summary_path = _artifact_paths(tmp_path)
    producer.produce(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    attacker_manifest = root / "attacker" / manifest.name
    _write_csv(attacker_manifest, MANIFEST_FIELDS, _read_rows(manifest))

    with pytest.raises(RuntimeError, match="canonical daily snapshot manifest"):
        producer.produce(
            repository_root=root,
            manifest_path=attacker_manifest,
            price_dir=root / "data" / "stock_price_history",
            detail_path=detail_path,
            summary_path=summary_path,
        )
    errors = validator.validate(
        repository_root=root,
        manifest_path=attacker_manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    assert any("canonical daily snapshot manifest" in error for error in errors)


@pytest.mark.parametrize(
    "attack_surface",
    [
        "snapshot_report_date",
        "main_price_date",
        "non_target_signal_date",
        "price_date",
        "duplicate_price_date",
    ],
)
def test_impossible_or_duplicate_dates_fail_closed_across_all_sources(
    tmp_path: Path,
    attack_surface: str,
) -> None:
    root, manifest, _, _ = _fixture_repo(
        tmp_path,
        first_snapshot_signal_date=(
            "20261340" if attack_surface == "non_target_signal_date" else "20260102"
        ),
    )
    if attack_surface in {"snapshot_report_date", "main_price_date"}:
        manifest_rows = _read_rows(manifest)
        manifest_rows[0][attack_surface] = "20261340"
        _write_csv(manifest, MANIFEST_FIELDS, manifest_rows)
    elif attack_surface in {"price_date", "duplicate_price_date"}:
        price_path = root / "data" / "stock_price_history" / "2330.csv"
        price_rows = _read_rows(price_path)
        price_rows[1]["date"] = (
            "20261340"
            if attack_surface == "price_date"
            else price_rows[0]["date"]
        )
        _write_csv(
            price_path,
            ["date", "stock_id", "open", "high", "low", "close", "volume"],
            price_rows,
        )

    detail_path, summary_path = _artifact_paths(tmp_path)
    with pytest.raises(RuntimeError, match="date"):
        producer.produce(
            repository_root=root,
            manifest_path=manifest,
            price_dir=root / "data" / "stock_price_history",
            detail_path=detail_path,
            summary_path=summary_path,
        )
    _write_csv(detail_path, producer.DETAIL_FIELDS, [])
    _write_csv(summary_path, producer.SUMMARY_FIELDS, [])
    errors = validator.validate(
        repository_root=root,
        manifest_path=manifest,
        price_dir=root / "data" / "stock_price_history",
        detail_path=detail_path,
        summary_path=summary_path,
    )
    assert any("date" in error for error in errors)


def test_validator_imports_are_limited_to_independent_standard_library_modules() -> None:
    validator_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "validate_tdcc_stealth_accumulation_research.py"
    )
    tree = ast.parse(validator_path.read_text(encoding="utf-8"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)
    allowed = {
        "__future__",
        "argparse",
        "csv",
        "datetime",
        "decimal",
        "hashlib",
        "io",
        "json",
        "pathlib",
        "re",
        "typing",
    }
    unexpected = sorted(imported - allowed)
    assert unexpected == []


def test_cli_write_is_wrapped_by_model_owned_artifact_guard() -> None:
    producer_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "build_tdcc_stealth_accumulation_research.py"
    )
    tree = ast.parse(producer_path.read_text(encoding="utf-8"))
    main = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "main"
    )
    guard_with = [
        node
        for node in ast.walk(main)
        if isinstance(node, ast.With)
        and any(
            isinstance(item.context_expr, ast.Call)
            and isinstance(item.context_expr.func, ast.Name)
            and item.context_expr.func.id == "model_owned_artifact_guard"
            for item in node.items
        )
    ]
    assert len(guard_with) == 1
    preflight_statement = next(
        node
        for node in main.body
        if isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name)
        and node.value.func.id == "_preflight_model_owned_outputs"
    )
    guard_statement = next(node for node in main.body if node is guard_with[0])
    assert main.body.index(preflight_statement) < main.body.index(guard_statement)


def test_cli_without_registered_ownership_leaves_no_output(tmp_path: Path) -> None:
    detail_path = (
        tmp_path
        / "output"
        / "research"
        / producer.MODEL_ID
        / producer.DETAIL_ARTIFACT_NAME
    )
    summary_path = detail_path.with_name(producer.SUMMARY_ARTIFACT_NAME)
    with pytest.raises(
        RuntimeError, match="missing model research artifact ownership registry"
    ):
        producer.main(
            [
                "--repository-root",
                str(tmp_path),
                "--detail-output",
                str(detail_path),
                "--summary-output",
                str(summary_path),
            ]
        )
    assert not detail_path.exists()
    assert not summary_path.exists()
    assert not detail_path.parent.exists()
