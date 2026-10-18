from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import price_pullback_23ema_confirmed_history as history


@pytest.fixture(autouse=True)
def activated_reader_unit_fixture(monkeypatch):
    # Exercise the dormant reader independently of the capture-only deployment.
    monkeypatch.setattr(history, "CONFIRMATION_CONSUMER_ENABLED", True)
    monkeypatch.setattr(history, "CAPTURE_NOT_BEFORE_REPORT_DATE", "20261001")


def confirmation_rows(**changes: str) -> list[dict[str, str]]:
    row = {
        "model_id": history.MODEL_ID, "row_type": "data",
        "pdf_section": "confirmed_operation", "signal_date": "20261016",
        "operation_asof_date": "20261016", "stock_id": "1234",
        "report_line": "mainstream", "buy_rank_eligible": "True",
        "model_rank": "3", "display_rank": "4", "model_rank_overall": "5",
        "model_score": "70.0", "entry_date": "", "entry_price": "",
        "stock_name": "原確認", "adapter_note_zh": "",
        **changes,
    }
    return [{**row, "pdf_view": view} for view in ("highlight", "full")]


def write_snapshot(
    repository_root: Path,
    rows: list[dict[str, str]],
    *,
    revision: str = "r1",
    supersedes: str = "",
    legacy: bool = False,
    crlf: bool = False,
) -> tuple[Path, dict[str, str], bytes]:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]), lineterminator="\r\n" if crlf else "\n")
    writer.writeheader()
    writer.writerows(rows)
    payload = buffer.getvalue().encode("utf-8")
    sha = history.snapshot_payload_sha256(payload)
    stem = f"{history.SNAPSHOT_STEM}_20261016"
    name = f"{stem}.csv" if legacy else f"{stem}_{revision}_{sha[:12]}.csv"
    relative = history.SNAPSHOT_REPOSITORY_PATH / name
    path = repository_root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    entry = {
        "snapshot_report_date": "20261016", "artifact_id": history.ARTIFACT_ID,
        "snapshot_path": relative.as_posix(), "snapshot_sha256": sha,
        "snapshot_revision": revision, "supersedes_snapshot_sha256": supersedes,
        "revision_reason": "original_saved_confirmation" if revision == "r1" else "source_revision",
    }
    return path, entry, payload


def write_manifest(repository_root: Path, entries: list[dict[str, str]]) -> Path:
    directory = repository_root / history.SNAPSHOT_REPOSITORY_PATH
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / history.MANIFEST_NAME
    pd.DataFrame(entries).to_csv(path, index=False, encoding="utf-8")
    return path


def test_original_full_confirmation_binds_exact_string_row_and_original_ranks(tmp_path) -> None:
    rows = confirmation_rows()
    _, entry, payload = write_snapshot(tmp_path, rows)
    manifest = write_manifest(tmp_path, [entry])
    loaded = history.load_prior_confirmed_operations(
        "20261019", repository_root=tmp_path,
        snapshot_dir=manifest.parent, manifest_path=manifest,
    )
    assert len(loaded) == 1
    actual = loaded.iloc[0]
    raw_full = rows[1]
    independently_encoded = json.dumps(raw_full, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert actual["confirmation_row_sha256"] == hashlib.sha256(independently_encoded).hexdigest()
    assert actual["confirmation_source_sha256"] == hashlib.sha256(payload).hexdigest()
    assert actual["confirmation_source_artifact"] == entry["snapshot_path"]
    assert actual["confirmation_snapshot_revision"] == "r1"
    assert [actual[field] for field in history.RANK_COLUMNS] == ["3", "4", "5"]
    assert actual["entry_date"] == ""


@pytest.mark.parametrize("changes", [
    {"buy_rank_eligible": "False"},
    {"pdf_section": "confirmed_unranked_operation", "buy_rank_eligible": "False"},
    {"model_rank": ""}, {"display_rank": ""}, {"model_rank_overall": ""},
])
def test_original_unranked_or_missing_rank_cannot_be_upgraded_by_later_revision(tmp_path, changes) -> None:
    _, original, _ = write_snapshot(tmp_path, confirmation_rows(**changes))
    _, later, _ = write_snapshot(tmp_path, confirmation_rows(model_rank="1"), revision="r2", supersedes=original["snapshot_sha256"])
    write_manifest(tmp_path, [original, later])
    loaded = history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)
    assert loaded.empty
    assert len(loaded.attrs["rejected_confirmations"]) == 1


def test_later_revision_cannot_replace_original_rank(tmp_path) -> None:
    _, original, _ = write_snapshot(tmp_path, confirmation_rows())
    _, later, _ = write_snapshot(tmp_path, confirmation_rows(model_rank="1"), revision="r2", supersedes=original["snapshot_sha256"])
    write_manifest(tmp_path, [original, later])
    loaded = history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)
    assert loaded.iloc[0]["model_rank"] == "3"
    assert loaded.iloc[0]["confirmation_source_sha256"] == original["snapshot_sha256"]


def test_activated_consumer_fails_closed_without_history(tmp_path) -> None:
    with pytest.raises(RuntimeError, match="missing its manifest"):
        history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)
    assert list(tmp_path.iterdir()) == []


def test_only_manifest_registered_original_snapshot_is_consumed(tmp_path) -> None:
    write_snapshot(tmp_path, confirmation_rows())
    write_manifest(tmp_path, [{
        "snapshot_report_date": "20261016", "artifact_id": "model_signals_for_report",
        "snapshot_path": "not-read.csv", "snapshot_sha256": "a" * 64,
        "snapshot_revision": "r1", "supersedes_snapshot_sha256": "", "revision_reason": "fixture",
    }])
    with pytest.raises(RuntimeError, match="missing its history family"):
        history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)


@pytest.mark.parametrize("mismatch", ["model_rank", "buy_rank_eligible", "stock_name"])
def test_conflicting_full_highlight_original_rows_fail(tmp_path, mismatch) -> None:
    rows = confirmation_rows()
    rows[0][mismatch] = "different"
    _, entry, _ = write_snapshot(tmp_path, rows)
    write_manifest(tmp_path, [entry])
    with pytest.raises(RuntimeError, match="views conflict"):
        history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)


def test_tampered_original_snapshot_fails_before_position_creation(tmp_path) -> None:
    path, entry, payload = write_snapshot(tmp_path, confirmation_rows())
    write_manifest(tmp_path, [entry])
    path.write_bytes(payload.replace(b"70.0", b"90.0"))
    with pytest.raises(RuntimeError, match="SHA-256 mismatch"):
        history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)


@pytest.mark.parametrize("mode", ["missing_r1", "duplicate_r1", "missing_view", "different_signal_date"])
def test_original_confirmation_identity_cannot_be_substituted(tmp_path, mode) -> None:
    rows = confirmation_rows()
    if mode == "missing_view":
        rows = rows[:1]
    if mode == "different_signal_date":
        rows = confirmation_rows(signal_date="20261015")
    _, entry, _ = write_snapshot(tmp_path, rows, revision="r2" if mode == "missing_r1" else "r1")
    write_manifest(tmp_path, [entry, entry] if mode == "duplicate_r1" else [entry])
    with pytest.raises(RuntimeError):
        history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)


def test_same_day_and_future_confirmations_are_not_prior_positions(tmp_path) -> None:
    _, entry, _ = write_snapshot(tmp_path, confirmation_rows())
    write_manifest(tmp_path, [entry])
    assert history.load_prior_confirmed_operations("20261016", repository_root=tmp_path).empty
    assert history.load_prior_confirmed_operations("20261015", repository_root=tmp_path).empty


def test_legacy_manifest_and_crlf_hash_remain_compatible(tmp_path) -> None:
    _, entry, payload = write_snapshot(tmp_path, confirmation_rows(), legacy=True, crlf=True)
    entry["snapshot_sha256"] = hashlib.sha256(payload).hexdigest()
    for field in ("snapshot_revision", "supersedes_snapshot_sha256", "revision_reason"):
        del entry[field]
    write_manifest(tmp_path, [entry])
    loaded = history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)
    assert len(loaded) == 1
    assert loaded.iloc[0]["confirmation_source_sha256"] == history.snapshot_payload_sha256(payload)


def test_git_crlf_checkout_of_quoted_multiline_fields_keeps_row_identity(tmp_path) -> None:
    rows = confirmation_rows(stock_name="原確認\n股票", adapter_note_zh="保留空格 \n 第二行\t")
    path, entry, payload = write_snapshot(tmp_path, rows)
    write_manifest(tmp_path, [entry])
    original = history.load_prior_confirmed_operations("20261019", repository_root=tmp_path).iloc[0]
    # Git checkout conversion also changes newlines inside quoted CSV fields.
    checkout_payload = payload.replace(b"\n", b"\r\n")
    assert '"原確認\r\n股票"'.encode("utf-8") in checkout_payload
    path.write_bytes(checkout_payload)
    checked_out = history.load_prior_confirmed_operations("20261019", repository_root=tmp_path).iloc[0]
    assert checked_out["confirmation_source_sha256"] == original["confirmation_source_sha256"]
    assert checked_out["confirmation_row_sha256"] == original["confirmation_row_sha256"]
    assert checked_out["stock_name"] == original["stock_name"] == "原確認\n股票"
    assert checked_out["adapter_note_zh"] == original["adapter_note_zh"] == "保留空格 \n 第二行\t"


def test_partial_revision_schema_remains_invalid(tmp_path) -> None:
    _, entry, _ = write_snapshot(tmp_path, confirmation_rows())
    del entry["revision_reason"]
    write_manifest(tmp_path, [entry])
    with pytest.raises(RuntimeError, match="partial revision schema"):
        history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)


def test_same_stock_dual_report_membership_preserves_both_original_keys(tmp_path) -> None:
    rows = confirmation_rows() + confirmation_rows(report_line="non_mainstream", model_rank="8")
    _, entry, _ = write_snapshot(tmp_path, rows)
    write_manifest(tmp_path, [entry])
    loaded = history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)
    assert len(loaded) == 2
    assert set(loaded["report_line"]) == {"mainstream", "non_mainstream"}
    assert set(loaded["model_rank"]) == {"3", "8"}


def test_capture_only_never_consumes_even_a_saved_ranked_confirmation(tmp_path, monkeypatch) -> None:
    _, entry, _ = write_snapshot(tmp_path, confirmation_rows())
    write_manifest(tmp_path, [entry])
    monkeypatch.setattr(history, "CONFIRMATION_CONSUMER_ENABLED", False)
    loaded = history.load_prior_confirmed_operations("20261019", repository_root=tmp_path)
    assert loaded.empty
    assert loaded.attrs["history_status"] == "capture_only_consumer_disabled"


def test_capture_not_started_is_distinct_from_missing_activated_history(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(history, "CONFIRMATION_CONSUMER_ENABLED", False)
    monkeypatch.setattr(history, "CAPTURE_NOT_BEFORE_REPORT_DATE", "20261019")
    loaded = history.load_prior_confirmed_operations("20261018", repository_root=tmp_path)
    assert loaded.empty
    assert loaded.attrs["history_status"] == "capture_not_started"


def test_activated_consumer_cannot_import_pre_capture_snapshot(tmp_path, monkeypatch) -> None:
    _, entry, _ = write_snapshot(tmp_path, confirmation_rows())
    write_manifest(tmp_path, [entry])
    monkeypatch.setattr(history, "CAPTURE_NOT_BEFORE_REPORT_DATE", "20261019")
    with pytest.raises(RuntimeError, match="predates forward capture start"):
        history.load_prior_confirmed_operations("20261020", repository_root=tmp_path)
