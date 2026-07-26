from __future__ import annotations

import json

import pandas as pd

from scripts import replay_historical_structured_sources as replay
from scripts import validate_historical_structured_source_replay as validator


def test_manifest_rejects_wrong_replay_id_and_pipeline_sha(tmp_path) -> None:
    path = tmp_path / "structured_source_manifest.json"
    path.write_text(
        json.dumps(
            {
                "schema_version": "historical_structured_source_replay_v1",
                "replay_id": "wrong-run",
                "report_date": "20260720",
                "publication_status": "reconstructed_not_as_published",
                "as_published": False,
                "pipeline_commit_sha": "0" * 40,
                "sources": [],
            }
        ),
        encoding="utf-8",
    )

    errors = validator.validate_manifest(
        path,
        "20260720",
        "github-run-123-1",
        replay.git_output("rev-parse", "HEAD"),
    )

    assert any("replay_id mismatch" in error for error in errors)
    assert any("pipeline_commit_sha" in error for error in errors)


def test_context_latest_rejects_future_row(tmp_path) -> None:
    path = tmp_path / "context.csv"
    pd.DataFrame({"date": ["20260723", "20260725"], "value": [1, 2]}).to_csv(
        path,
        index=False,
    )

    errors = validator.validate_context_latest(path, "date", "20260724", minimum_rows=1)

    assert any("contains future rows" in error for error in errors)


def test_exact_dated_artifact_rejects_warrant_flow_gap(tmp_path) -> None:
    path = tmp_path / "warrant_flow_20260720.csv"
    pd.DataFrame({"date": ["20260721"], "stock_id": ["2330"]}).to_csv(path, index=False)

    errors = validator.validate_exact_dated_artifact(
        path,
        "20260720",
        "official warrant flow history",
    )

    assert any("date mismatch" in error for error in errors)


def test_freshness_rejects_daily_pdf_ready_true() -> None:
    frame = pd.DataFrame(
        [
            {
                "main_price_date": "20260724",
                "report_ready": "false",
                "daily_pdf_ready": "true",
            }
        ]
    )

    errors = validator.validate_freshness_frame(frame, "20260724")

    assert any("stale daily PDFs not ready" in error for error in errors)


def test_base_repair_rejects_twse_sha_drift() -> None:
    errors = validator.validate_base_twse_sha_payload(
        {
            "twse_base_row_sha256_before": {"data/market_index_history.csv": "a" * 64},
            "twse_base_row_sha256_after": {"data/market_index_history.csv": "b" * 64},
        }
    )

    assert errors == ["market index base repair TWSE row SHA preservation mismatch"]


def test_pipeline_sha_helper_accepts_exact_replay_base() -> None:
    sha = replay.git_output("rev-parse", "HEAD")

    assert validator.validate_pipeline_commit_sha({"pipeline_commit_sha": sha}, "day", sha) == []
