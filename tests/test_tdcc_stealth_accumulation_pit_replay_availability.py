from __future__ import annotations

import ast
import csv
import hashlib
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

import audit_tdcc_stealth_accumulation_pit_replay_availability as audit  # noqa: E402
import validate_tdcc_stealth_accumulation_pit_replay_availability as validator  # noqa: E402


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


def _commit_all(root: Path, message: str) -> str:
    if not (root / ".git").exists():
        subprocess.run(
            ("git", "init"), cwd=root, check=True, capture_output=True
        )
        subprocess.run(
            ("git", "config", "user.email", "audit-test@example.invalid"),
            cwd=root,
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ("git", "config", "user.name", "Audit Test"),
            cwd=root,
            check=True,
            capture_output=True,
        )
    subprocess.run(("git", "add", "."), cwd=root, check=True, capture_output=True)
    subprocess.run(
        ("git", "commit", "-m", message),
        cwd=root,
        check=True,
        capture_output=True,
    )
    return subprocess.run(
        ("git", "rev-parse", "HEAD"),
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout.strip()


def _bind_artifact_to_commit(artifact: Path, commit: str) -> None:
    rows = _read_artifact(artifact)
    for row in rows:
        row["source_commit_sha"] = commit
    artifact.write_bytes(_csv_payload(audit.AUDIT_FIELDS, rows))


def _read_artifact(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _rewrite_manifest_snapshot_schema(
    root: Path,
    artifact_id: str,
    *,
    add_fields: tuple[str, ...] = (),
    remove_fields: tuple[str, ...] = (),
) -> None:
    manifest_path = root / audit.MANIFEST_PATH
    with manifest_path.open("r", encoding="utf-8", newline="") as handle:
        manifest_reader = csv.DictReader(handle)
        manifest_fields = list(manifest_reader.fieldnames or [])
        manifest_rows = list(manifest_reader)
    manifest_row = next(
        row for row in manifest_rows if row["artifact_id"] == artifact_id
    )
    snapshot_path = root / manifest_row["snapshot_path"]
    with snapshot_path.open("r", encoding="utf-8", newline="") as handle:
        snapshot_reader = csv.DictReader(handle)
        snapshot_fields = list(snapshot_reader.fieldnames or [])
        snapshot_rows = list(snapshot_reader)
    snapshot_fields = [
        field for field in snapshot_fields if field not in set(remove_fields)
    ]
    snapshot_fields.extend(add_fields)
    for row in snapshot_rows:
        for field in remove_fields:
            row.pop(field, None)
        for field in add_fields:
            row[field] = "1"
    snapshot_payload = _write_csv(snapshot_path, snapshot_fields, snapshot_rows)
    manifest_row["snapshot_sha256"] = hashlib.sha256(snapshot_payload).hexdigest()
    manifest_row["column_count"] = str(len(snapshot_fields))
    _write_csv(manifest_path, manifest_fields, manifest_rows)


def _rewrite_manifest_snapshot_value(
    root: Path,
    artifact_id: str,
    field: str,
    value: str,
) -> None:
    manifest_path = root / audit.MANIFEST_PATH
    with manifest_path.open("r", encoding="utf-8", newline="") as handle:
        manifest_reader = csv.DictReader(handle)
        manifest_fields = list(manifest_reader.fieldnames or [])
        manifest_rows = list(manifest_reader)
    manifest_row = next(
        row for row in manifest_rows if row["artifact_id"] == artifact_id
    )
    snapshot_path = root / manifest_row["snapshot_path"]
    with snapshot_path.open("r", encoding="utf-8", newline="") as handle:
        snapshot_reader = csv.DictReader(handle)
        snapshot_fields = list(snapshot_reader.fieldnames or [])
        snapshot_rows = list(snapshot_reader)
    snapshot_rows[0][field] = value
    snapshot_payload = _write_csv(snapshot_path, snapshot_fields, snapshot_rows)
    manifest_row["snapshot_sha256"] = hashlib.sha256(snapshot_payload).hexdigest()
    _write_csv(manifest_path, manifest_fields, manifest_rows)


def _fixture_repo(root: Path, *, published_target: bool) -> Path:
    selector_inputs = [f"selector_input_{index:02d}" for index in range(50)]
    snapshot_relative = (
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260828.csv"
    )
    snapshot_path = root / snapshot_relative
    snapshot_fields = ["signal_date", "stock_id", "model_id", *selector_inputs[:6]]
    snapshot_rows = [
        {
            "signal_date": "20260828",
            "stock_id": "2330",
            "model_id": (
                audit.MODEL_ID if published_target else "hot_theme_pullback"
            ),
        }
    ]
    snapshot_rows[0].update({field: "1" for field in selector_inputs[:6]})
    snapshot_payload = _write_csv(snapshot_path, snapshot_fields, snapshot_rows)
    snapshot_sha = hashlib.sha256(snapshot_payload).hexdigest()
    all_candidates_relative = (
        "output/history/daily_model_snapshots/all_candidates_20260828.csv"
    )
    all_candidates_fields = ["signal_date", "stock_id", *selector_inputs[:26]]
    all_candidates_rows = [
        {
            "signal_date": "20260828",
            "stock_id": "2330",
            **{field: "1" for field in selector_inputs[:26]},
        }
    ]
    all_candidates_payload = _write_csv(
        root / all_candidates_relative,
        all_candidates_fields,
        all_candidates_rows,
    )
    all_candidates_sha = hashlib.sha256(all_candidates_payload).hexdigest()
    manifest_fields = [
        "snapshot_report_date",
        "snapshot_revision",
        "artifact_id",
        "snapshot_path",
        "snapshot_sha256",
        "row_count",
        "column_count",
    ]
    _write_csv(
        root / audit.MANIFEST_PATH,
        manifest_fields,
        [
            {
                "snapshot_report_date": "20260828",
                "snapshot_revision": "r1",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": snapshot_relative,
                "snapshot_sha256": snapshot_sha,
                "row_count": "1",
                "column_count": str(len(snapshot_fields)),
            },
            {
                "snapshot_report_date": "20260828",
                "snapshot_revision": "r1",
                "artifact_id": "all_candidates_source_rows",
                "snapshot_path": all_candidates_relative,
                "snapshot_sha256": all_candidates_sha,
                "row_count": "1",
                "column_count": str(len(all_candidates_fields)),
            },
        ],
    )
    _write_csv(
        root / audit.LEGACY_SIGNAL_LOG_PATH,
        ["signal_date", "stock_id", "model_id"],
        [
            {
                "signal_date": "20260602",
                "stock_id": "2317",
                "model_id": audit.MODEL_ID,
            }
        ],
    )
    weekly_payloads: dict[str, bytes] = {}
    for date, stock in (("20260821", "2317"), ("20260828", "2330")):
        relative_path = f"output/history/tdcc/tdcc_holder_ratio_{date}.csv"
        payload = _csv_payload(
            ["date", "code", "over_400_pct"],
            [{"date": date, "code": stock, "over_400_pct": "55.0"}],
        )
        if date == "20260821":
            payload = b"\xef\xbb\xbf" + payload.replace(b"\n", b"\r\n")
        source_path = root / relative_path
        source_path.parent.mkdir(parents=True, exist_ok=True)
        source_path.write_bytes(payload)
        weekly_payloads[relative_path] = payload
    _write_csv(
        root / "output/history/tdcc/tdcc_latest_ratio_raw_20260828.csv",
        ["date", "code", "level", "ratio_pct"],
        [{"date": "20260828", "code": "2330", "level": "1", "ratio_pct": "1"}],
    )
    manifest_json = root / "output/history/tdcc/tdcc_dataset_manifest_20260828.json"
    manifest_json.parent.mkdir(parents=True, exist_ok=True)
    manifest_json.write_text(
        json.dumps({"signal_date": "20260828", "status": "pass"}),
        encoding="utf-8",
        newline="\n",
    )
    latest_manifest = root / audit.TDCC_LATEST_DATASET_MANIFEST_PATH
    latest_manifest.parent.mkdir(parents=True, exist_ok=True)
    latest_manifest.write_text(
        json.dumps(
            {
                "hash_mode": "utf8_text_lf_normalized_sha256",
                "snapshot_count": len(weekly_payloads),
                "required_dates": ["20260821", "20260828"],
                "history_dates": ["20260821", "20260828"],
                "current_stock_count": 2,
                "snapshots": [
                    {
                        "path": path,
                        "sha256": hashlib.sha256(
                            payload.decode("utf-8-sig")
                            .replace("\r\n", "\n")
                            .replace("\r", "\n")
                            .encode("utf-8")
                        ).hexdigest(),
                        "current_universe_missing_stock_ids": [],
                    }
                    for path, payload in sorted(weekly_payloads.items())
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
        newline="\n",
    )
    _write_csv(
        root / audit.TDCC_SIGNAL_SNAPSHOT_PATH,
        ["signal_date", "code", "signal_family"],
        [
            {
                "signal_date": "20260828",
                "code": "2330",
                "signal_family": "tdcc_normalized_accumulation",
            }
        ],
    )
    _write_csv(
        root / "data/tdcc_stock_history_raw/2330.csv",
        ["as_of_date", "code", "ratio_pct"],
        [{"as_of_date": "20260828", "code": "2330", "ratio_pct": "55"}],
    )
    _write_csv(
        root / "data/tdcc_stock_history/2330.csv",
        ["as_of_date", "stock_id", "over_400_pct"],
        [{"as_of_date": "20260828", "stock_id": "2330", "over_400_pct": "55"}],
    )
    _write_csv(
        root / "data/daily_price/20260828.csv",
        ["date", "ticker", "open", "close"],
        [{"date": "20260828", "ticker": "2330", "open": "100", "close": "101"}],
    )
    _write_csv(
        root / "data/stock_price_history/2330.csv",
        ["date", "stock_id", "open", "close"],
        [{"date": "20260828", "stock_id": "2330", "open": "100", "close": "101"}],
    )
    _write_csv(
        root / audit.STOCK_MODEL_CONTRACT_PATH,
        ["model_id", "input_columns"],
        [
            {
                "model_id": audit.MODEL_ID,
                "input_columns": ";".join(selector_inputs),
            }
        ],
    )
    _write_csv(
        root / audit.SEMANTIC_OWNERSHIP_PATH,
        ["model_id", "semantic_item_count", "semantic_sha256"],
        [
            {
                "model_id": audit.MODEL_ID,
                "semantic_item_count": "30",
                "semantic_sha256": "3" * 64,
            }
        ],
    )
    _write_csv(
        root / audit.SHARED_SEMANTIC_PATH,
        ["semantic_item", "consumer_models"],
        [
            {
                "semantic_item": f"shared_{index}",
                "consumer_models": (
                    audit.MODEL_ID if index < 28 else "hot_theme_pullback"
                ),
            }
            for index in range(29)
        ],
    )
    _commit_all(root, "fixture sources")
    artifact = root / "artifacts" / audit.ARTIFACT_NAME
    rows = audit.build_audit_rows(root, "HEAD")
    audit.write_audit(rows, artifact)
    return artifact


def test_audit_is_source_inventory_only_and_zero_sample_is_explicit(
    tmp_path: Path,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    rows = _read_artifact(artifact)

    assert tuple(rows[0]) == tuple(audit.AUDIT_FIELDS)
    assert [row["source_family"] for row in rows] == list(
        audit.SOURCE_FAMILY_ORDER
    )
    assert {row["availability_state"] for row in rows} == {
        audit.AVAILABILITY_STATE
    }
    assert {row["published_target_row_count"] for row in rows} == {"0"}
    by_family = {row["source_family"]: row for row in rows}
    assert by_family["published_all_candidates_snapshots"][
        "selector_present_input_count"
    ] == "26"
    assert by_family["published_all_candidates_snapshots"][
        "selector_missing_input_count"
    ] == "24"
    assert by_family["published_model_signal_snapshots"][
        "selector_present_input_count"
    ] == "6"
    assert by_family["published_model_signal_snapshots"][
        "selector_missing_input_count"
    ] == "44"
    assert by_family["tdcc_latest_dataset_manifest"]["source_file_count"] == "1"
    assert by_family["tdcc_per_stock_raw_history"]["source_unique_date_count"] == "1"
    assert by_family["tdcc_per_stock_normalized_history"][
        "source_unique_date_count"
    ] == "1"
    assert by_family["daily_price_date_snapshots"][
        "source_unique_stock_count"
    ] == "1"
    assert all(
        row["blockers"]
        == ";".join(audit.BASE_BLOCKERS + (audit.ZERO_SAMPLE_BLOCKER,))
        for row in rows
    )
    forbidden_fragments = ("event_id", "return", "win_rate", "entry_price", "exit_price")
    assert not any(
        fragment in field
        for field in audit.AUDIT_FIELDS
        for fragment in forbidden_fragments
    )
    assert validator.validate(
        repository_root=tmp_path,
        artifact_path=artifact,
    ) == []


def test_nonzero_published_membership_does_not_reuse_legacy_zero_sample_blocker(
    tmp_path: Path,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=True)
    rows = _read_artifact(artifact)

    assert {row["published_target_row_count"] for row in rows} == {"1"}
    assert all(audit.ZERO_SAMPLE_BLOCKER not in row["blockers"] for row in rows)
    assert validator.validate(
        repository_root=tmp_path,
        artifact_path=artifact,
    ) == []


def test_daily_price_inventory_uses_repo_supported_security_contract(
    tmp_path: Path,
) -> None:
    _write_csv(
        tmp_path / "data/daily_price/20260827.csv",
        ["date", "ticker", "close"],
        [
            {"date": "20260827", "ticker": "2330", "close": "100"},
            {"date": "20260827", "ticker": "030001", "close": "10"},
        ],
    )
    _write_csv(
        tmp_path / "data/daily_price/20260828.csv",
        ["date", "stock_id", "close"],
        [
            {"date": "20260828", "stock_id": "006208", "close": "101"},
            {"date": "20260828", "stock_id": "030001", "close": "11"},
        ],
    )

    for module in (audit, validator):
        metrics = module._daily_price_metrics(
            module.SourceAccess(tmp_path.resolve(), "")
        )

        assert metrics["stocks"] == {"2330", "006208"}
        assert "raw_unique_instrument_count=3" in metrics["coverage_detail"]
        assert "supported_security_count=2" in metrics["coverage_detail"]
        assert (
            "excluded_unsupported_instrument_count=1"
            in metrics["coverage_detail"]
        )
        assert "ticker_schema_file_count=1" in metrics["coverage_detail"]
        assert "stock_id_schema_file_count=1" in metrics["coverage_detail"]


@pytest.mark.parametrize(
    ("fields", "row", "error"),
    [
        (
            ["date", "close"],
            {"date": "20260828", "close": "100"},
            "exactly one security identifier field",
        ),
        (
            ["date", "ticker", "close"],
            {"date": "20260828", "ticker": "23A0", "close": "100"},
            "malformed security identifier",
        ),
    ],
)
def test_daily_price_inventory_fails_closed_on_identifier_schema_drift(
    tmp_path: Path,
    fields: list[str],
    row: dict[str, str],
    error: str,
) -> None:
    _write_csv(tmp_path / "data/daily_price/20260828.csv", fields, [row])

    for module in (audit, validator):
        with pytest.raises(RuntimeError, match=error):
            module._daily_price_metrics(module.SourceAccess(tmp_path.resolve(), ""))


@pytest.mark.parametrize(
    ("artifact_id", "extra_selector"),
    [
        (audit.ALL_CANDIDATES_ARTIFACT_ID, "selector_input_26"),
        (audit.MANIFEST_ARTIFACT_ID, "selector_input_06"),
    ],
)
def test_snapshot_selector_coverage_contract_fails_closed_on_schema_drift(
    tmp_path: Path,
    artifact_id: str,
    extra_selector: str,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    _rewrite_manifest_snapshot_schema(
        tmp_path, artifact_id, add_fields=(extra_selector,)
    )
    _bind_artifact_to_commit(artifact, _commit_all(tmp_path, "selector drift"))

    with pytest.raises(RuntimeError, match="selector input coverage drift"):
        audit.build_audit_rows(tmp_path, "")
    errors = validator.validate(repository_root=tmp_path, artifact_path=artifact)
    assert any("selector input coverage drift" in error for error in errors)


@pytest.mark.parametrize(
    ("artifact_id", "missing_field"),
    [
        (audit.MANIFEST_ARTIFACT_ID, "model_id"),
        (audit.MANIFEST_ARTIFACT_ID, "signal_date"),
        (audit.MANIFEST_ARTIFACT_ID, "stock_id"),
        (audit.ALL_CANDIDATES_ARTIFACT_ID, "signal_date"),
        (audit.ALL_CANDIDATES_ARTIFACT_ID, "stock_id"),
    ],
)
def test_published_snapshot_membership_schema_is_mandatory(
    tmp_path: Path,
    artifact_id: str,
    missing_field: str,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=True)
    _rewrite_manifest_snapshot_schema(
        tmp_path, artifact_id, remove_fields=(missing_field,)
    )
    _bind_artifact_to_commit(artifact, _commit_all(tmp_path, "membership drift"))

    with pytest.raises(RuntimeError, match="snapshot missing required columns"):
        audit.build_audit_rows(tmp_path, "")
    errors = validator.validate(repository_root=tmp_path, artifact_path=artifact)
    assert any("snapshot missing required columns" in error for error in errors)


@pytest.mark.parametrize(
    ("artifact_id", "field", "value"),
    [
        (audit.MANIFEST_ARTIFACT_ID, "model_id", ""),
        (audit.MANIFEST_ARTIFACT_ID, "signal_date", "2026-08-28"),
        (audit.MANIFEST_ARTIFACT_ID, "signal_date", "20260827"),
        (audit.MANIFEST_ARTIFACT_ID, "stock_id", ""),
        (audit.ALL_CANDIDATES_ARTIFACT_ID, "signal_date", ""),
        (audit.ALL_CANDIDATES_ARTIFACT_ID, "stock_id", ""),
    ],
)
def test_published_snapshot_membership_identity_values_are_mandatory(
    tmp_path: Path,
    artifact_id: str,
    field: str,
    value: str,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=True)
    _rewrite_manifest_snapshot_value(tmp_path, artifact_id, field, value)
    _bind_artifact_to_commit(artifact, _commit_all(tmp_path, "identity drift"))

    with pytest.raises(RuntimeError, match="snapshot identity"):
        audit.build_audit_rows(tmp_path, "")
    errors = validator.validate(repository_root=tmp_path, artifact_path=artifact)
    assert any("snapshot identity" in error for error in errors)


def test_published_snapshot_lf_crlf_transport_normalization_is_counted(
    tmp_path: Path,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    subprocess.run(
        ("git", "config", "core.autocrlf", "false"),
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    manifest_path = tmp_path / audit.MANIFEST_PATH
    with manifest_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        manifest_rows = list(reader)
    manifest_row = next(
        row
        for row in manifest_rows
        if row["artifact_id"] == audit.MANIFEST_ARTIFACT_ID
    )
    snapshot_path = tmp_path / manifest_row["snapshot_path"]
    canonical = snapshot_path.read_bytes()
    transported = canonical.replace(b"\n", b"\r\n")
    snapshot_path.write_bytes(transported)
    manifest_row["snapshot_sha256"] = hashlib.sha256(canonical).hexdigest()
    _write_csv(manifest_path, fields, manifest_rows)
    commit = _commit_all(tmp_path, "transport drift")

    rows = audit.build_audit_rows(tmp_path, "HEAD")
    audit.write_audit(rows, artifact)
    by_family = {row["source_family"]: row for row in rows}
    assert by_family["published_model_signal_snapshots"][
        "source_transport_normalized_hash_count"
    ] == "1"
    assert validator.validate(
        repository_root=tmp_path,
        artifact_path=artifact,
        source_ref=commit,
    ) == []


@pytest.mark.parametrize(
    ("field", "value", "error"),
    [
        ("hash_mode", "raw_sha256", "hash_mode is unsupported"),
        ("history_dates", ["2026-08-28"], "history_dates contains invalid dates"),
        ("required_dates", [""], "required_dates contains invalid dates"),
    ],
)
def test_latest_tdcc_manifest_contract_drift_fails_closed(
    tmp_path: Path,
    field: str,
    value: object,
    error: str,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    manifest_path = tmp_path / audit.TDCC_LATEST_DATASET_MANIFEST_PATH
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    payload[field] = value
    manifest_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    _bind_artifact_to_commit(artifact, _commit_all(tmp_path, "TDCC manifest drift"))

    with pytest.raises(RuntimeError, match=error):
        audit.build_audit_rows(tmp_path, "")
    errors = validator.validate(repository_root=tmp_path, artifact_path=artifact)
    assert any(error in item for item in errors)


def test_producer_cli_rejects_empty_source_ref() -> None:
    with pytest.raises(SystemExit) as exc_info:
        audit._parser().parse_args(["--source-ref", ""])

    assert exc_info.value.code == 2


@pytest.mark.parametrize("header_attack", ["missing", "extra", "reordered", "duplicate"])
def test_validator_rejects_every_header_and_order_drift(
    tmp_path: Path,
    header_attack: str,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    rows = _read_artifact(artifact)
    fields = list(audit.AUDIT_FIELDS)
    if header_attack == "missing":
        missing = fields.pop()
        for row in rows:
            row.pop(missing)
    elif header_attack == "extra":
        fields.append("unexpected")
        for row in rows:
            row["unexpected"] = "x"
    elif header_attack == "reordered":
        fields[0], fields[1] = fields[1], fields[0]
    else:
        fields.insert(1, fields[0])
    artifact.write_bytes(_csv_payload(fields, rows))

    errors = validator.validate(
        repository_root=tmp_path,
        artifact_path=artifact,
    )

    assert any("header/order mismatch" in error for error in errors)


def test_validator_rejects_hidden_trailing_artifact_cell(tmp_path: Path) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    lines = artifact.read_text(encoding="utf-8").splitlines()
    lines[1] += ",hidden_event_payload"
    artifact.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    errors = validator.validate(repository_root=tmp_path, artifact_path=artifact)

    assert any("row width mismatch" in error for error in errors)


@pytest.mark.parametrize(
    "payload",
    [b"first,second\n1\n", b"first,second\n1,2,hidden\n"],
)
def test_source_csv_parser_rejects_non_exact_row_width(payload: bytes) -> None:
    for module in (audit, validator):
        with pytest.raises(RuntimeError, match="row width mismatch"):
            module._read_csv_payload(payload, "synthetic.csv")


def test_validator_rejects_source_hash_and_coverage_tamper(tmp_path: Path) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    original = _read_artifact(artifact)

    hash_tamper = [dict(row) for row in original]
    weekly_index = next(
        index
        for index, row in enumerate(original)
        if row["source_family"] == "tdcc_weekly_holder_snapshots"
    )
    hash_tamper[weekly_index]["source_sha256"] = "0" * 64
    artifact.write_bytes(_csv_payload(audit.AUDIT_FIELDS, hash_tamper))
    hash_errors = validator.validate(
        repository_root=tmp_path,
        artifact_path=artifact,
    )
    assert any("source_sha256 mismatch" in error for error in hash_errors)

    coverage_tamper = [dict(row) for row in original]
    coverage_tamper[weekly_index]["source_file_count"] = "999"
    coverage_tamper[weekly_index]["source_unique_date_count"] = "999"
    artifact.write_bytes(_csv_payload(audit.AUDIT_FIELDS, coverage_tamper))
    coverage_errors = validator.validate(
        repository_root=tmp_path,
        artifact_path=artifact,
    )
    assert any("source_file_count mismatch" in error for error in coverage_errors)
    assert any("source_unique_date_count mismatch" in error for error in coverage_errors)


def test_validator_enforces_false_only_and_blocked_promotion(tmp_path: Path) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    rows = _read_artifact(artifact)
    for field in (
        "selector_replay_allowed",
        "performance_metrics_allowed",
        "formal_use",
        "trade_eligible",
        "promotion_evidence_allowed",
    ):
        rows[0][field] = "True"
    rows[0]["promotion_status"] = "approved"
    artifact.write_bytes(_csv_payload(audit.AUDIT_FIELDS, rows))

    errors = validator.validate(
        repository_root=tmp_path,
        artifact_path=artifact,
    )

    for field in (
        "selector_replay_allowed",
        "performance_metrics_allowed",
        "formal_use",
        "trade_eligible",
        "promotion_evidence_allowed",
    ):
        assert any(f"{field} must be False" in error for error in errors)
    assert any("promotion_status must be blocked" in error for error in errors)


def test_independent_validator_imports_no_audit_or_business_module() -> None:
    path = SCRIPTS / "validate_tdcc_stealth_accumulation_pit_replay_availability.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
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
        "fnmatch",
        "hashlib",
        "io",
        "json",
        "re",
        "subprocess",
        "pathlib",
        "typing",
    }
    assert imported - allowed == set()


def test_commit_bound_source_ref_ignores_uncommitted_physical_drift(
    tmp_path: Path,
) -> None:
    artifact = _fixture_repo(tmp_path, published_target=False)
    commands = (
        ("git", "init"),
        ("git", "config", "user.email", "audit-test@example.invalid"),
        ("git", "config", "user.name", "Audit Test"),
        ("git", "add", "."),
        ("git", "commit", "-m", "fixture"),
    )
    for command in commands:
        subprocess.run(
            command,
            cwd=tmp_path,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    commit = subprocess.run(
        ("git", "rev-parse", "HEAD"),
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout.strip()
    audit.write_audit(audit.build_audit_rows(tmp_path, "HEAD"), artifact)

    tracked_source = tmp_path / "data/daily_price/20260828.csv"
    tracked_source.write_text("physical drift must be ignored\n", encoding="utf-8")
    rows = _read_artifact(artifact)

    assert {row["source_commit_sha"] for row in rows} == {commit}
    assert validator.validate(
        repository_root=tmp_path,
        artifact_path=artifact,
        source_ref="HEAD",
    ) == []


def test_source_access_freezes_symbolic_ref_before_later_git_reads(
    tmp_path: Path,
) -> None:
    _fixture_repo(tmp_path, published_target=False)
    commands = (
        ("git", "init"),
        ("git", "config", "user.email", "audit-test@example.invalid"),
        ("git", "config", "user.name", "Audit Test"),
        ("git", "add", "."),
        ("git", "commit", "-m", "first"),
    )
    for command in commands:
        subprocess.run(command, cwd=tmp_path, check=True, capture_output=True)
    first_commit = subprocess.run(
        ("git", "rev-parse", "HEAD"),
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout.strip()
    tracked_path = "data/daily_price/20260828.csv"
    original_payload = (tmp_path / tracked_path).read_bytes()
    accesses = [
        module.SourceAccess(tmp_path.resolve(), "HEAD")
        for module in (audit, validator)
    ]
    assert {access.resolved_commit_sha() for access in accesses} == {first_commit}

    (tmp_path / tracked_path).write_text(
        "date,ticker,close\n20260828,2317,200\n",
        encoding="utf-8",
        newline="\n",
    )
    new_path = tmp_path / "data/daily_price/20260829.csv"
    new_path.write_text(
        "date,ticker,close\n20260829,2454,300\n",
        encoding="utf-8",
        newline="\n",
    )
    for command in (("git", "add", "."), ("git", "commit", "-m", "second")):
        subprocess.run(command, cwd=tmp_path, check=True, capture_output=True)

    for access in accesses:
        assert access.resolved_commit_sha() == first_commit
        assert access.read_bytes(tracked_path) == original_payload
        assert not access.exists("data/daily_price/20260829.csv")


def test_explicit_unresolvable_source_ref_fails_closed_inside_git_repo(
    tmp_path: Path,
) -> None:
    subprocess.run(("git", "init"), cwd=tmp_path, check=True, capture_output=True)

    for module in (audit, validator):
        with pytest.raises(RuntimeError, match="source_ref"):
            module.SourceAccess(
                tmp_path.resolve(), "definitely-missing-ref"
            ).resolved_commit_sha()


def test_nonempty_source_ref_never_downgrades_to_physical_non_git_mode(
    tmp_path: Path,
) -> None:
    for module in (audit, validator):
        with pytest.raises(RuntimeError, match="failed to resolve source_ref"):
            module.SourceAccess(tmp_path.resolve(), "HEAD").resolved_commit_sha()


@pytest.mark.parametrize("module", [audit, validator])
def test_explicit_source_ref_fails_closed_when_git_is_unavailable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    module: object,
) -> None:
    def unavailable(*_args: object, **_kwargs: object) -> object:
        raise OSError("git unavailable")

    monkeypatch.setattr(module.subprocess, "run", unavailable)

    with pytest.raises(RuntimeError, match="failed to resolve source_ref"):
        module.SourceAccess(tmp_path.resolve(), "HEAD").resolved_commit_sha()
