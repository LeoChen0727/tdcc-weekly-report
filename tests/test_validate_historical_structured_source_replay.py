from __future__ import annotations

import json

import pandas as pd
import pytest

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


def test_freshness_rejects_mixed_tail_date_contract_drift() -> None:
    frame = pd.DataFrame(
        [
            {
                "main_price_date": "20260724",
                "main_price_date_source": "historical_replay_override",
                "historical_replay_main_price_date": "20260724",
                "expected_price_history_high_water_date": "20260728",
                "actual_stock_price_history_date": "20260724",
                "official_price_fetch_date": "20260728",
                "raw_official_price_fetch_date": "20260728",
                "report_ready": "false",
                "daily_pdf_ready": "false",
            }
        ]
    )

    errors = validator.validate_freshness_frame(frame, "20260724", "20260728")

    assert any("actual_stock_price_history_date mismatch" in error for error in errors)
    assert any("official_price_fetch_date mismatch" in error for error in errors)


def test_continuity_report_requires_exact_recomputed_calendar_and_replay_dates() -> None:
    report = {
        "status": "pass",
        "main_price_date": "20260724",
        "expected_trading_dates": ["20260720", "20260721", "20260724"],
    }

    assert validator.validate_continuity_report(
        report,
        "20260724",
        ["20260720", "20260721", "20260724"],
        ["20260720", "20260721", "20260724"],
    ) == []

    errors = validator.validate_continuity_report(
        report,
        "20260724",
        ["20260718", "20260720", "20260721", "20260724"],
        ["20260720", "20260721", "20260722", "20260723", "20260724"],
    )
    assert any("expected_trading_dates mismatch" in error for error in errors)
    assert any("omits replay trading dates" in error for error in errors)


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


def test_expected_manifest_paths_omit_optional_base_repair() -> None:
    assert validator.expected_replay_manifest_paths(
        "github-run-123-1",
        ["20260727", "20260728", "20260729"],
    ) == [
        "output/history/historical_source_replay/github-run-123-1/20260727/structured_source_manifest.json",
        "output/history/historical_source_replay/github-run-123-1/20260728/structured_source_manifest.json",
        "output/history/historical_source_replay/github-run-123-1/20260729/structured_source_manifest.json",
    ]


def test_expected_manifest_paths_include_explicit_base_repair_first() -> None:
    assert validator.expected_replay_manifest_paths(
        "github-run-123-1",
        ["20260720"],
        "20260717",
    ) == [
        "output/history/historical_source_replay/github-run-123-1/20260717/market_index_base_repair_manifest.json",
        "output/history/historical_source_replay/github-run-123-1/20260720/structured_source_manifest.json",
    ]


def test_recorded_baseline_rejects_wrong_required_tail_without_live_reads(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda *_, **__: pytest.fail("recorded baseline validation read live history"),
    )
    matrix = {
        "daily_price": "20260729",
        "stock_price_history": {"max_date": "20260729"},
        "market_index": {"TWSE": "20260724", "TPEX": "20260724"},
        "market_index_ohlc": {"TWSE": "20260724", "TPEX": "20260724"},
        "taifex": {"source": "20260724"},
        "warrant_daily": "20260724",
        "warrant_flow": "20260723",
    }

    errors = validator.validate_recorded_baseline(
        {"before_tail_matrix": matrix},
        "20260724",
        "20260729",
    )

    assert any("warrant_flow=20260723" in error for error in errors)


def _preserve_manifest_payload(expected_sha: str, fingerprints: dict) -> dict:
    target_date = "20260724"
    high_water = "20260728"
    output_sha = "d" * 64

    def source_row(source_id: str, accepted: list[dict], after_tail, **extra) -> dict:
        return {
            "source_id": source_id,
            "raw_sha256": "a" * 64,
            "normalized_sha256": "b" * 64,
            "output_sha256": output_sha,
            "requested_dates": [target_date],
            "observed_dates": [target_date],
            "fallback_used": False,
            "future_rows_used": False,
            "as_published": False,
            "validation_status": "pass",
            "pk_unique": True,
            "row_count": 1,
            "accepted_source_responses": accepted,
            "output_evidence": {"future_rows_excluded_from_slice": True},
            "before_tail": extra.pop("before_tail", "20260723"),
            "after_tail": after_tail,
            **extra,
        }

    exact_response = {
        "raw_sha256": "a" * 64,
        "normalized_sha256": "b" * 64,
        "observed_response_dates": [target_date],
        "exact_date_match": True,
    }
    warrant_responses = [
        {
            **exact_response,
            "source_name": "TWSE_WARRANT_STOCK_JSON",
            "logical_group": "mapping",
            "accepted": True,
            "accepted_rows": 1,
        },
        {
            **exact_response,
            "source_name": "TWSE_MI_INDEX_0999_JSON",
            "logical_group": "quote-0999",
            "accepted": True,
            "accepted_rows": 1,
        },
        {
            **exact_response,
            "source_name": "TWSE_MI_INDEX_0999P_JSON",
            "logical_group": "quote-0999P",
            "accepted": True,
            "accepted_rows": 1,
        },
    ]
    return {
        "schema_version": "historical_structured_source_replay_v1",
        "replay_id": "github-run-123-1",
        "report_date": target_date,
        "publication_status": "reconstructed_not_as_published",
        "as_published": False,
        "pipeline_commit_sha": expected_sha,
        "price_history_high_water_date": high_water,
        "protected_price_history_fingerprints": fingerprints,
        "after_tail_matrix": {
            "daily_price": high_water,
            "stock_price_history": {"max_date": high_water},
            "market_index": {"TWSE": target_date, "TPEX": target_date},
            "market_index_ohlc": {"TWSE": target_date, "TPEX": target_date},
            "taifex": {"a": target_date, "b": target_date},
            "warrant_daily": target_date,
            "warrant_flow": target_date,
        },
        "sources": [
            source_row(
                "official_daily_price",
                [exact_response],
                high_water,
                before_tail=high_water,
                price_history_high_water_date=high_water,
                preserved_target_slice_evidence={
                    "mode": "preserve_existing_price_history",
                    "price_history_high_water_date": high_water,
                    "fetched_target_slice_sha256": "e" * 64,
                    "preserved_daily_price_target_slice_sha256": {
                        f"data/daily_price/daily_price_{target_date}.csv": "e" * 64,
                        f"data/daily_price/{target_date}.csv": "e" * 64,
                    },
                    "preserved_stock_history_target_slice_manifest_sha256": "f" * 64,
                    "preserved_stock_history_target_slice_rows": 1,
                    "stock_history_coverage": {
                        "supported_stock_count": 1,
                        "missing_history_rows": 0,
                        "manifest_end_date_lower_bound": target_date,
                        "manifest_end_date_upper_bound": high_water,
                    },
                },
            ),
            source_row(
                "market_index",
                [exact_response],
                {"TWSE": target_date, "TPEX": target_date},
            ),
            source_row(
                "taifex_futures_options_vix",
                [exact_response],
                {"a": target_date, "b": target_date},
            ),
            source_row(
                "official_warrant_daily",
                warrant_responses,
                target_date,
            ),
        ],
    }


def _patch_preserve_manifest_recomputes(monkeypatch) -> None:
    monkeypatch.setattr(
        replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda target_date: {
            f"data/daily_price/daily_price_{target_date}.csv": "e" * 64,
            f"data/daily_price/{target_date}.csv": "e" * 64,
        },
    )
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda target_date, **kwargs: {
            "supported_stock_count": 1,
            "missing_history_rows": 0,
            "manifest_end_date_lower_bound": target_date,
            "manifest_end_date_upper_bound": "20260728",
        },
    )


def test_preserve_manifest_accepts_mixed_tail_and_exact_protected_fingerprints(
    tmp_path,
    monkeypatch,
) -> None:
    expected_sha = "1" * 40
    fingerprints = {
        "daily_price": {"path_count": 10, "aggregate_sha256": "2" * 64}
    }
    payload = _preserve_manifest_payload(expected_sha, fingerprints)
    path = tmp_path / "structured_source_manifest.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    def output_evidence(source_id, target_date, **kwargs):
        components = []
        if source_id == "official_daily_price":
            components = [
                {
                    "component_id": "stock_history_target_slices",
                    "slice_manifest_sha256": "f" * 64,
                    "row_count": 1,
                }
            ]
        return {
            "output_sha256": "d" * 64,
            "row_count": 1,
            "components": components,
        }

    monkeypatch.setattr(replay, "build_source_output_evidence", output_evidence)
    _patch_preserve_manifest_recomputes(monkeypatch)

    assert validator.validate_manifest(
        path,
        "20260724",
        "github-run-123-1",
        expected_sha,
        "20260728",
        fingerprints,
    ) == []


def test_preserve_manifest_rejects_unbound_fetched_target_sha(tmp_path, monkeypatch) -> None:
    expected_sha = "1" * 40
    fingerprints = {
        "daily_price": {"path_count": 10, "aggregate_sha256": "2" * 64}
    }
    payload = _preserve_manifest_payload(expected_sha, fingerprints)
    path = tmp_path / "structured_source_manifest.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    monkeypatch.setattr(
        replay,
        "build_source_output_evidence",
        lambda *args, **kwargs: {
            "output_sha256": "d" * 64,
            "row_count": 1,
            "components": [
                {
                    "component_id": "stock_history_target_slices",
                    "slice_manifest_sha256": "f" * 64,
                    "row_count": 1,
                }
            ],
        },
    )
    _patch_preserve_manifest_recomputes(monkeypatch)
    monkeypatch.setattr(
        replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda target_date: {
            f"data/daily_price/daily_price_{target_date}.csv": "c" * 64,
            f"data/daily_price/{target_date}.csv": "c" * 64,
        },
    )

    errors = validator.validate_manifest(
        path,
        "20260724",
        "github-run-123-1",
        expected_sha,
        "20260728",
        fingerprints,
    )

    assert any("not bound to committed target CSVs" in error for error in errors)


def test_preserve_manifest_rejects_protected_fingerprint_drift(tmp_path, monkeypatch) -> None:
    expected_sha = "1" * 40
    stored = {"daily_price": {"path_count": 10, "aggregate_sha256": "2" * 64}}
    current = {"daily_price": {"path_count": 10, "aggregate_sha256": "3" * 64}}
    payload = _preserve_manifest_payload(expected_sha, stored)
    path = tmp_path / "structured_source_manifest.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    monkeypatch.setattr(
        replay,
        "build_source_output_evidence",
        lambda *args, **kwargs: {
            "output_sha256": "d" * 64,
            "row_count": 1,
            "components": [
                {
                    "component_id": "stock_history_target_slices",
                    "slice_manifest_sha256": "f" * 64,
                    "row_count": 1,
                }
            ],
        },
    )
    _patch_preserve_manifest_recomputes(monkeypatch)

    errors = validator.validate_manifest(
        path,
        "20260724",
        "github-run-123-1",
        expected_sha,
        "20260728",
        current,
    )

    assert any("protected price/history fingerprint mismatch" in error for error in errors)
