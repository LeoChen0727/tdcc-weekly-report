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
import validate_daily_price_pullback_23ema_operation_section as validator


def saved_confirmation(tmp_path: Path, **changes: str) -> tuple[pd.DataFrame, Path]:
    original = {
        "model_id": "price_pullback_23ema", "row_type": "data", "pdf_view": "full",
        "pdf_section": "confirmed_operation", "stock_id": "1234",
        "signal_date": "20261016", "operation_asof_date": "20261016",
        "report_line": "mainstream", "buy_rank_eligible": "True",
        "model_rank": "3", "display_rank": "4", "model_rank_overall": "5",
        "model_score": "70.0", "stock_name": "原始確認", "entry_price": "",
        **changes,
    }
    rows = [{**original, "pdf_view": view} for view in ("highlight", "full")]
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(original), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    payload = buffer.getvalue().encode("utf-8")
    sha = hashlib.sha256(payload).hexdigest()
    name = f"daily_price_pullback_23ema_operation_section_20261016_r1_{sha[:12]}.csv"
    relative = f"output/history/daily_model_snapshots/{name}"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_bytes(payload)
    pd.DataFrame([{
        "snapshot_report_date": "20261016", "artifact_id": "price_pullback_23ema_operation_section",
        "snapshot_path": relative, "snapshot_sha256": sha, "snapshot_revision": "r1",
        "supersedes_snapshot_sha256": "", "revision_reason": "initial_publish",
    }]).to_csv(path.parent / "daily_published_model_snapshot_manifest.csv", index=False)
    row_sha = hashlib.sha256(json.dumps(original, ensure_ascii=False, sort_keys=True,
                                       separators=(",", ":")).encode("utf-8")).hexdigest()
    active = {
        **original, "pdf_section": "active_operation", "operation_asof_date": "20261019",
        "buy_rank_eligible": "False", "entry_price": "100.00",
        "confirmation_source_artifact": relative, "confirmation_source_sha256": sha,
        "confirmation_row_sha256": row_sha, "confirmation_snapshot_revision": "r1",
        "confirmation_snapshot_report_date": "20261016",
    }
    return pd.DataFrame([active]), path


def test_independent_binding_accepts_saved_ranked_confirmation(tmp_path):
    frame, _ = saved_confirmation(tmp_path)
    assert validator.validate_confirmation_bindings(frame, repository_root=tmp_path) == []


@pytest.mark.parametrize("field,value,reason", [
    ("model_rank", "1", "frozen confirmation fields changed"),
    ("model_score", "99.0", "frozen confirmation fields changed"),
    ("confirmation_row_sha256", "0" * 64, "row SHA-256 mismatch"),
    ("confirmation_source_sha256", "0" * 64, "source SHA-256 mismatch"),
    ("confirmation_snapshot_revision", "r2", "original revision/date"),
    ("confirmation_source_artifact", "output/latest/fake.csv", "path/hash identity"),
    ("signal_date", "20261015", "original revision/date"),
])
def test_independent_binding_rejects_later_mutation(tmp_path, field, value, reason):
    frame, _ = saved_confirmation(tmp_path)
    frame.loc[0, field] = value
    errors = validator.validate_confirmation_bindings(frame, repository_root=tmp_path)
    assert any(reason in item for item in errors), errors


@pytest.mark.parametrize("changes", [
    {"buy_rank_eligible": "False"}, {"pdf_section": "confirmed_unranked_operation"},
    {"model_rank": ""},
])
def test_independent_binding_rejects_original_unranked_even_with_valid_hash(tmp_path, changes):
    frame, _ = saved_confirmation(tmp_path, **changes)
    frame.loc[0, "model_rank"] = "3"
    errors = validator.validate_confirmation_bindings(frame, repository_root=tmp_path)
    assert any("not buy-ranked" in item for item in errors), errors


def test_independent_binding_requires_manifest_and_untampered_original(tmp_path):
    frame, path = saved_confirmation(tmp_path)
    path.write_bytes(path.read_bytes().replace(b"70.0", b"80.0"))
    errors = validator.validate_confirmation_bindings(frame, repository_root=tmp_path)
    assert any("source SHA-256 mismatch" in item for item in errors)
    path.parent.joinpath("daily_published_model_snapshot_manifest.csv").unlink()
    errors = validator.validate_confirmation_bindings(frame, repository_root=tmp_path)
    assert any("cannot validate original confirmations" in item for item in errors)


def test_binding_row_hash_survives_crlf_checkout_with_quoted_multiline_cell(tmp_path):
    frame, path = saved_confirmation(tmp_path, stock_name="第一行\n第二行")
    path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
    assert validator.validate_confirmation_bindings(frame, repository_root=tmp_path) == []


def test_capture_only_rejects_active_even_when_original_binding_is_valid(tmp_path):
    frame, _ = saved_confirmation(tmp_path)
    assert validator.validate_confirmation_bindings(frame, repository_root=tmp_path) == []
    assert any("not activated" in error for error in validator.validate_capture_only_section(frame))


def test_capture_only_allows_confirmed_rows_and_empty_active_state(tmp_path):
    frame, _ = saved_confirmation(tmp_path)
    frame.loc[0, "pdf_section"] = "confirmed_operation"
    assert validator.validate_capture_only_section(frame) == []
    frame.loc[0, "pdf_section"] = "active_operation"
    frame.loc[0, "row_type"] = "empty_state"
    assert validator.validate_capture_only_section(frame) == []
