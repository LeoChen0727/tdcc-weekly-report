from __future__ import annotations

import ast
import hashlib
from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (  # noqa: E402
    canonical_monthly_revenue_history_table_sha256,
    canonical_monthly_revenue_raw_row_sha256,
    cross_market_resolution_registry_canonical_sha256,
    load_canonical_monthly_revenue_history,
    monthly_revenue_history_blob_sha256,
)
from revenue_unreacted_range_source_snapshot_projection import (  # noqa: E402
    ARCHIVE_EVIDENCE_COLUMNS,
    ARTIFACT_ID,
    ARTIFACT_VERSION,
    CUTOFF_DATE,
    LATEST_DETAIL_CSV,
    LATEST_MANIFEST_CSV,
    MANIFEST_COLUMNS,
    MONTHLY_RESOLUTION_COLUMNS,
    PROJECTION_POLICY_ID,
    SOURCE_FIRST_ARTIFACT_ID,
    V1_EXPECTED_DETAIL_BYTES_SHA256,
    V1_EXPECTED_MANIFEST_BYTES_SHA256,
    V1_PROJECTION_VERSION,
    V2_CANDIDATE_STATUS,
    V2_LINEAGE_CHANGE_REASON,
    V2_MANIFEST_COLUMNS,
    V2_PROJECTION_POLICY_ID,
    V2_PROJECTION_VERSION,
    V2_SUPERSEDE_EVIDENCE_COLUMNS,
    archive_immutable_v1_projection,
    build_source_snapshot_projection_manifest,
    build_source_snapshot_projection_v2_manifest,
    canonical_projected_source_detail_semantic_sha256,
    cutoff_price_input_lineage,
    cutoff_price_input_stock_ids,
    load_cutoff_monthly_revenue_subset,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    supersede_source_snapshot_projection_v2_candidate,
    validate_projection_binding,
    write_source_snapshot_projection,
    write_source_snapshot_projection_v2_candidate,
)
from revenue_unreacted_range_source_first_condition_audit import (  # noqa: E402
    build_source_first_condition_audit,
)
import validate_revenue_unreacted_range_source_snapshot_projection as validator  # noqa: E402
import validate_revenue_unreacted_range_source_first_condition_audit as source_first_validator  # noqa: E402
import build_revenue_unreacted_range_research as orchestrator  # noqa: E402
import revenue_unreacted_range_source_snapshot_projection as projection  # noqa: E402


SOURCE_FIRST_EXACT7_PATH_CONSTANTS = (
    "V1_ARCHIVE_MANIFEST_CSV",
    "V1_ARCHIVE_DETAIL_CSV",
    "V1_ARCHIVE_EVIDENCE_CSV",
    "V2_MANIFEST_CSV",
    "V2_PROJECTED_DETAIL_CSV",
    "V1_V2_DIFF_SUMMARY_CSV",
    "V1_V2_DIFF_DETAIL_CSV",
)


def _bind_source_first_exact7_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for name in SOURCE_FIRST_EXACT7_PATH_CONSTANTS:
        path = tmp_path / f"{name}.csv"
        paths[name] = path
        monkeypatch.setattr(source_first_validator, name, path)
    return paths


def _bind_source_first_audit_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in ("LATEST_CSV", "DETAIL_CSV", "LATEST_MD"):
        path = tmp_path / f"{name}.txt"
        path.write_text("present\n", encoding="utf-8")
        monkeypatch.setattr(source_first_validator, name, path)


def _prepare_v2_supersede_fixture(
    *,
    source_inputs: dict[str, object],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[dict[str, Path], dict[str, bytes]]:
    v1_manifest = _build(source_inputs)
    v1_detail = source_inputs["projected_detail"]
    v1_manifest_payload = v1_manifest.to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")
    v1_detail_payload = v1_detail.to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")
    v1_manifest_sha = hashlib.sha256(v1_manifest_payload).hexdigest()
    v1_detail_sha = hashlib.sha256(v1_detail_payload).hexdigest()
    monkeypatch.setattr(
        projection,
        "V1_EXPECTED_MANIFEST_BYTES",
        len(v1_manifest_payload),
    )
    monkeypatch.setattr(
        projection,
        "V1_EXPECTED_MANIFEST_BYTES_SHA256",
        v1_manifest_sha,
    )
    monkeypatch.setattr(
        projection,
        "V1_EXPECTED_DETAIL_BYTES",
        len(v1_detail_payload),
    )
    monkeypatch.setattr(
        projection,
        "V1_EXPECTED_DETAIL_BYTES_SHA256",
        v1_detail_sha,
    )

    v2_manifest = build_source_snapshot_projection_v2_manifest(
        source_inputs["full_detail"],
        source_inputs["projected_detail"],
        predecessor_manifest_bytes_sha256=v1_manifest_sha,
        predecessor_detail_bytes_sha256=v1_detail_sha,
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
        generated_at="2026-08-22 00:00:00 Asia/Taipei",
    )
    v2_manifest_payload = v2_manifest.to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")
    v2_detail_payload = v1_detail_payload
    paths = {
        name: tmp_path / f"{name}.csv"
        for name in (
            "evidence_path",
            "v1_manifest_path",
            "v1_detail_path",
            "candidate_manifest_path",
            "candidate_detail_path",
            "diff_summary_path",
            "diff_detail_path",
            "canonical_manifest_path",
            "canonical_detail_path",
            "history_manifest_path",
            "docs_manifest_path",
        )
    }
    for name in ("v1_manifest_path", "canonical_manifest_path", "history_manifest_path", "docs_manifest_path"):
        paths[name].write_bytes(v1_manifest_payload)
    for name in ("v1_detail_path", "canonical_detail_path"):
        paths[name].write_bytes(v1_detail_payload)
    paths["candidate_manifest_path"].write_bytes(v2_manifest_payload)
    paths["candidate_detail_path"].write_bytes(v2_detail_payload)
    diff_summary = pd.DataFrame(
        [
            {
                "v1_projection_version": V1_PROJECTION_VERSION,
                "v2_projection_version": V2_PROJECTION_VERSION,
                "v1_manifest_sha256": v1_manifest_sha,
                "v1_detail_sha256": v1_detail_sha,
                "v2_manifest_sha256": hashlib.sha256(v2_manifest_payload).hexdigest(),
                "v2_detail_sha256": hashlib.sha256(v2_detail_payload).hexdigest(),
                "unclassified_semantic_drift_count": "0",
                "semantic_drift_status": projection.V2_DIFF_CLASSIFIED_STATUS,
                "research_only": "true",
                "formal_model_use_allowed": "false",
                "approved_for_daily": "false",
                "production_change": "false",
                "promotion_evidence_allowed": "false",
                "ranking_consumption_allowed": "false",
                "pdf_consumption_allowed": "false",
            }
        ]
    )
    diff_summary.to_csv(paths["diff_summary_path"], index=False, lineterminator="\n")
    paths["diff_detail_path"].write_bytes(b"classified semantic drift\n")
    immutable = {
        "v1_manifest": v1_manifest_payload,
        "v1_detail": v1_detail_payload,
        "v2_manifest": v2_manifest_payload,
        "v2_detail": v2_detail_payload,
    }
    return paths, immutable


def _business_payload(stock_id: str, revenue_period: str) -> dict[str, object]:
    return {
        "stock_id": stock_id,
        "stock_name": f"Stock {stock_id}",
        "industry": "test",
        "revenue_period": revenue_period,
        "revenue_period_roc": "11506",
        "monthly_revenue": "1000",
        "previous_month_revenue": "900",
        "last_year_month_revenue": "800",
        "month_over_month_pct": "11.1111",
        "latest_revenue_yoy_pct": "25",
        "cumulative_revenue": "6000",
        "last_year_cumulative_revenue": "5000",
        "cumulative_revenue_yoy_pct": "20",
        "note": "-",
        "revenue_positive_flag": "True",
        "revenue_strong_flag": "True",
        "revenue_numerical_anomaly_flag": "False",
        "revenue_numerical_anomaly_reason": "",
        "point_in_time_status": "ready_official_source_table_date",
        "research_join_allowed": "True",
        "allowed_for_formal_historical_model_use": "False",
        "formal_use_blocker": "research_only",
        "coverage_note": "synthetic",
    }


def _raw_row(
    *,
    stock_id: str,
    revenue_period: str,
    market: str,
    market_name: str,
    source_date: str,
    source_file: str,
) -> dict[str, object]:
    return {
        "generated_at": "2026-07-31 00:00:00 Asia/Taipei",
        "history_id": "monthly_revenue_history",
        "history_version": "test_v1",
        "source_kind": "official_mops_test",
        "market": market,
        "source_market_name": market_name,
        **_business_payload(stock_id, revenue_period),
        "source_table_date": source_date,
        "source_table_date_raw": source_date,
        "fetch_date": "20260731",
        "fetch_timestamp": "2026-07-31 00:00:00 Asia/Taipei",
        "source_url": f"https://example.test/{source_file}",
        "source_file": source_file,
    }


def _monthly_registry_row(
    earlier: dict[str, object],
    later: dict[str, object],
    *,
    resolution_id: str,
    transition_date: str,
) -> dict[str, object]:
    earlier_hash = canonical_monthly_revenue_raw_row_sha256(pd.Series(earlier))
    later_hash = canonical_monthly_revenue_raw_row_sha256(pd.Series(later))
    return {
        "resolution_id": resolution_id,
        "model_id": "revenue_unreacted_range",
        "stock_id": earlier["stock_id"],
        "revenue_period": earlier["revenue_period"],
        "earlier_market": earlier["market"],
        "earlier_source_market_name": earlier["source_market_name"],
        "earlier_source_table_date": earlier["source_table_date"],
        "earlier_source_kind": earlier["source_kind"],
        "earlier_source_url": earlier["source_url"],
        "earlier_source_file": earlier["source_file"],
        "earlier_raw_row_canonical_sha256": earlier_hash,
        "later_market": later["market"],
        "later_source_market_name": later["source_market_name"],
        "later_source_table_date": later["source_table_date"],
        "later_source_kind": later["source_kind"],
        "later_source_url": later["source_url"],
        "later_source_file": later["source_file"],
        "later_raw_row_canonical_sha256": later_hash,
        "official_market_transition_date": transition_date,
        "canonical_source_table_date": earlier["source_table_date"],
        "canonical_row_canonical_sha256": earlier_hash,
        "resolution_status": "registered_equal_payload_cross_market_mirror",
        "canonicalization_policy": "earliest_official_source_table_date",
        "evidence_url": "https://example.test/evidence",
        "formal_model_use_allowed": "False",
        "notes": "future pair must not rewrite the cutoff snapshot",
    }


def _source_detail_row(
    *,
    stock_id: str,
    source_date: str,
    trade_date: str,
    end_date: str,
    monthly_blob_sha: str,
    monthly_table_sha: str,
    registry_sha: str,
) -> dict[str, object]:
    return {
        "generated_at": "2026-07-31 00:00:00 Asia/Taipei",
        "model_id": "revenue_unreacted_range",
        "artifact_id": SOURCE_FIRST_ARTIFACT_ID,
        "artifact_version": "source_first_condition_v3_20260720",
        "monthly_revenue_history_blob_sha256": monthly_blob_sha,
        "monthly_revenue_canonical_table_sha256": monthly_table_sha,
        "cross_market_resolution_registry_canonical_sha256": registry_sha,
        "condition_variant_id": "absolute_or_two_month_yoy_ge15",
        "episode_key": f"absolute_or_two_month_yoy_ge15|{stock_id}|{source_date}|1",
        "stock_id": stock_id,
        "episode_start_source_date": source_date,
        "latest_qualifying_source_date": source_date,
        "qualifying_source_dates": source_date,
        "episode_start_trade_date": trade_date,
        "latest_qualifying_trade_date": trade_date,
        "qualifying_trade_dates": trade_date,
        "episode_end_date": end_date,
        "episode_status": "right_censored_before_active_horizon",
        "approved_for_daily": False,
        "production_change": False,
    }


def _price_rows(*, active_attack_date: str = "") -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for timestamp in pd.bdate_range("2026-05-01", "2026-07-20"):
        date = timestamp.strftime("%Y%m%d")
        rows.append(
            {
                "date": date,
                "open": 10,
                "high": 10.5,
                "low": 9.5,
                "close": 10,
                "volume": 1000,
                "volume_ratio": 3.0 if date == active_attack_date else 1.0,
            }
        )
    return rows


@pytest.fixture()
def source_inputs(tmp_path: Path) -> dict[str, object]:
    ordinary = _raw_row(
        stock_id="1111",
        revenue_period="202606",
        market="listed",
        market_name="TWSE",
        source_date="20260710",
        source_file="data/monthly_revenue_history/raw/ordinary.csv",
    )
    future_earlier = _raw_row(
        stock_id="2222",
        revenue_period="202606",
        market="otc",
        market_name="TPEX",
        source_date="20260714",
        source_file="data/monthly_revenue_history/raw/future_earlier.csv",
    )
    future_later = _raw_row(
        stock_id="2222",
        revenue_period="202606",
        market="listed",
        market_name="TWSE",
        source_date="20260716",
        source_file="data/monthly_revenue_history/raw/future_later.csv",
    )
    cutoff_earlier = _raw_row(
        stock_id="4444",
        revenue_period="202606",
        market="otc",
        market_name="TPEX",
        source_date="20260708",
        source_file="data/monthly_revenue_history/raw/cutoff_earlier.csv",
    )
    cutoff_later = _raw_row(
        stock_id="4444",
        revenue_period="202606",
        market="listed",
        market_name="TWSE",
        source_date="20260709",
        source_file="data/monthly_revenue_history/raw/cutoff_later.csv",
    )
    no_episode = _raw_row(
        stock_id="5555",
        revenue_period="202606",
        market="listed",
        market_name="TWSE",
        source_date="20260710",
        source_file="data/monthly_revenue_history/raw/no_episode.csv",
    )
    revenue_path = tmp_path / "monthly_revenue_history.csv"
    pd.DataFrame(
        [
            ordinary,
            cutoff_earlier,
            cutoff_later,
            no_episode,
            future_earlier,
            future_later,
        ]
    ).to_csv(
        revenue_path,
        index=False,
    )
    monthly_registry_path = tmp_path / "monthly_resolution.csv"
    pd.DataFrame(
        [
            _monthly_registry_row(
                cutoff_earlier,
                cutoff_later,
                resolution_id="cutoff_cross_market_mirror",
                transition_date="20260709",
            ),
            _monthly_registry_row(
                future_earlier,
                future_later,
                resolution_id="future_cross_market_mirror",
                transition_date="20260715",
            ),
        ],
        columns=list(MONTHLY_RESOLUTION_COLUMNS),
    ).to_csv(monthly_registry_path, index=False)

    price_dir = tmp_path / "prices"
    price_dir.mkdir()
    pd.DataFrame(_price_rows()).to_csv(price_dir / "1111.csv", index=False)
    pd.DataFrame(_price_rows()).to_csv(price_dir / "2222.csv", index=False)
    pd.DataFrame(_price_rows()).to_csv(price_dir / "4444.csv", index=False)
    pd.DataFrame(_price_rows(active_attack_date="20260710")).to_csv(
        price_dir / "5555.csv",
        index=False,
    )
    price_registry_path = tmp_path / "price_resolution.csv"
    pd.DataFrame(
        [
            {
                "resolution_id": "price_before_cutoff",
                "model_id": "revenue_unreacted_range",
                "stock_id": "1111",
                "resume_date": "20260711",
                "exchange_ratio": "1",
                "root_cause_status": "verified_non_comparable_raw_price_scale",
                "notes": "applied",
            },
            {
                "resolution_id": "price_no_episode_before_cutoff",
                "model_id": "revenue_unreacted_range",
                "stock_id": "5555",
                "resume_date": "20260709",
                "exchange_ratio": "1",
                "root_cause_status": "verified_non_comparable_raw_price_scale",
                "notes": "applied even though no episode is emitted",
            },
            {
                "resolution_id": "price_after_cutoff",
                "model_id": "revenue_unreacted_range",
                "stock_id": "1111",
                "resume_date": "20260714",
                "exchange_ratio": "1",
                "root_cause_status": "verified_non_comparable_raw_price_scale",
                "notes": "not applied",
            },
        ]
    ).to_csv(price_registry_path, index=False)

    full_monthly = load_canonical_monthly_revenue_history(
        revenue_path,
        monthly_registry_path,
    )
    cutoff_monthly = load_cutoff_monthly_revenue_subset(
        revenue_path,
        monthly_registry_path,
    )
    monthly_blob_sha = monthly_revenue_history_blob_sha256(revenue_path)
    full_monthly_sha = canonical_monthly_revenue_history_table_sha256(full_monthly)
    cutoff_monthly_sha = canonical_monthly_revenue_history_table_sha256(cutoff_monthly)
    registry_sha = cross_market_resolution_registry_canonical_sha256(
        pd.read_csv(monthly_registry_path, dtype=str, keep_default_na=False)
    )
    _full_summary, full_detail = build_source_first_condition_audit(
        revenue_path,
        price_dir,
        monthly_registry_path,
        price_registry_path,
    )
    _projected_summary, projected_detail = build_source_first_condition_audit(
        revenue_path,
        price_dir,
        monthly_registry_path,
        price_registry_path,
        observation_cutoff_date=CUTOFF_DATE,
    )
    return {
        "revenue_path": revenue_path,
        "monthly_registry_path": monthly_registry_path,
        "price_dir": price_dir,
        "price_registry_path": price_registry_path,
        "full_detail": full_detail,
        "projected_detail": projected_detail,
        "cutoff_monthly_sha": cutoff_monthly_sha,
    }


def _build(inputs: dict[str, object]) -> pd.DataFrame:
    return build_source_snapshot_projection_manifest(
        inputs["full_detail"],
        inputs["projected_detail"],
        revenue_path=inputs["revenue_path"],
        price_dir=inputs["price_dir"],
        monthly_resolution_path=inputs["monthly_registry_path"],
        price_resolution_path=inputs["price_registry_path"],
        generated_at="2026-07-31 00:00:00 Asia/Taipei",
    )


def test_projection_manifest_binds_cutoff_inputs_and_round_trips(
    source_inputs: dict[str, object],
    tmp_path: Path,
) -> None:
    manifest = _build(source_inputs)
    row = manifest.iloc[0]
    assert list(manifest.columns) == list(MANIFEST_COLUMNS)
    assert row["artifact_id"] == ARTIFACT_ID
    assert row["artifact_version"] == ARTIFACT_VERSION
    assert row["projection_policy_id"] == PROJECTION_POLICY_ID
    assert row["cutoff_date"] == CUTOFF_DATE
    assert row["cutoff_revenue_subset_row_count"] == 3
    assert row["cutoff_revenue_subset_semantic_sha256"] == source_inputs[
        "cutoff_monthly_sha"
    ]
    assert row["applied_monthly_resolution_count"] == 1
    assert row["applied_monthly_resolution_ids"] == "cutoff_cross_market_mirror"
    assert row["cutoff_price_input_stock_count"] == 3
    assert cutoff_price_input_stock_ids(
        load_cutoff_monthly_revenue_subset(
            source_inputs["revenue_path"],
            source_inputs["monthly_registry_path"],
        ),
        source_inputs["price_dir"],
    ) == ["1111", "4444", "5555"]
    assert row["applied_price_resolution_count"] == 2
    assert row["applied_price_resolution_ids"] == (
        "price_before_cutoff|price_no_episode_before_cutoff"
    )
    assert row["projected_episode_row_count"] == len(
        source_inputs["projected_detail"]
    )
    assert row["projected_max_episode_end_date"] == CUTOFF_DATE
    assert bool(row["research_only"])
    assert not bool(row["formal_model_use_allowed"])

    errors = validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )
    assert errors == []

    latest_manifest = tmp_path / LATEST_MANIFEST_CSV.name
    latest_detail = tmp_path / LATEST_DETAIL_CSV.name
    history = tmp_path / "history.csv"
    docs = tmp_path / "docs.csv"
    write_source_snapshot_projection(
        manifest,
        source_inputs["projected_detail"],
        latest_manifest_path=latest_manifest,
        latest_detail_path=latest_detail,
        history_manifest_path=history,
        docs_manifest_path=docs,
    )
    loaded_manifest = load_source_snapshot_projection_manifest(latest_manifest)
    loaded_detail = load_projected_source_detail(latest_detail)
    validate_projection_binding(loaded_manifest, loaded_detail)
    assert canonical_projected_source_detail_semantic_sha256(loaded_detail) == row[
        "projected_episode_semantic_sha256"
    ]
    assert latest_manifest.read_bytes() == docs.read_bytes()

    rerun = manifest.copy()
    rerun.loc[0, "generated_at"] = "2026-07-31 01:00:00 Asia/Taipei"
    write_source_snapshot_projection(
        rerun,
        source_inputs["projected_detail"],
        latest_manifest_path=latest_manifest,
        latest_detail_path=latest_detail,
        history_manifest_path=history,
        docs_manifest_path=docs,
    )
    assert len(pd.read_csv(history)) == 1

    capture = rerun.copy()
    capture.loc[0, "generated_at"] = "2026-08-01 01:00:00 Asia/Taipei"
    capture.loc[0, "full_source_episode_row_count"] = int(
        capture.loc[0, "full_source_episode_row_count"]
    ) + 1
    capture.loc[0, "full_source_episode_semantic_sha256"] = "6" * 64
    capture.loc[0, "monthly_revenue_history_blob_sha256"] = "7" * 64
    capture.loc[0, "monthly_revenue_canonical_table_sha256"] = "8" * 64
    capture_detail = source_inputs["projected_detail"].copy()
    capture_detail["monthly_revenue_history_blob_sha256"] = "7" * 64
    assert canonical_projected_source_detail_semantic_sha256(capture_detail) == row[
        "projected_episode_semantic_sha256"
    ]
    write_source_snapshot_projection(
        capture,
        capture_detail,
        latest_manifest_path=latest_manifest,
        latest_detail_path=latest_detail,
        history_manifest_path=history,
        docs_manifest_path=docs,
    )
    assert len(pd.read_csv(history)) == 2

    drift = capture.copy()
    drift.loc[0, "cutoff_price_input_semantic_sha256"] = "0" * 64
    with pytest.raises(RuntimeError, match="immutable history key changed semantics"):
        write_source_snapshot_projection(
            drift,
            capture_detail,
            latest_manifest_path=latest_manifest,
            latest_detail_path=latest_detail,
            history_manifest_path=history,
            docs_manifest_path=docs,
        )


def test_projection_binding_rejects_row_mutation_and_post_cutoff_date(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    mutated = source_inputs["projected_detail"].copy()
    mutated.loc[mutated.index[0], "episode_end_date"] = "20260714"
    with pytest.raises(RuntimeError, match="binding failed"):
        validate_projection_binding(manifest, mutated)


def test_independent_validator_rejects_price_lineage_and_formal_flag_mutation(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    price_path = source_inputs["price_dir"] / "1111.csv"
    price = pd.read_csv(price_path, dtype=str, keep_default_na=False)
    price.loc[price["date"].eq("20260709"), "close"] = "99"
    price.to_csv(price_path, index=False)
    errors = validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )
    assert any("cutoff_price_input" in error for error in errors)

    unsafe = manifest.copy()
    unsafe.loc[0, "formal_model_use_allowed"] = True
    errors = validator.validate_frames(
        unsafe,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )
    assert "formal_model_use_allowed must be false" in errors


def test_independent_validator_replays_rows_instead_of_trusting_rebound_manifest(
    source_inputs: dict[str, object],
) -> None:
    fabricated = source_inputs["projected_detail"].copy()
    fabricated.loc[fabricated.index[0], "episode_status"] = (
        "fabricated_not_from_raw_replay"
    )
    rebound_inputs = {**source_inputs, "projected_detail": fabricated}
    rebound_manifest = _build(rebound_inputs)
    validate_projection_binding(rebound_manifest, fabricated)

    errors = validator.validate_frames(
        rebound_manifest,
        fabricated,
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )

    assert any("independent replay" in error for error in errors)


def test_no_episode_stock_price_is_bound_and_independently_validated(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    assert "5555:" in str(
        manifest.iloc[0]["cutoff_price_input_file_semantic_sha256s"]
    )
    assert not source_inputs["projected_detail"]["stock_id"].astype(str).eq(
        "5555"
    ).any()

    price_path = source_inputs["price_dir"] / "5555.csv"
    price = pd.read_csv(price_path, dtype=str, keep_default_na=False)
    price.loc[price["date"].eq("20260709"), "close"] = "10.25"
    price.to_csv(price_path, index=False)
    errors = validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )

    assert any("cutoff_price_input" in error for error in errors)


def test_no_episode_stock_resolution_is_bound_and_independently_validated(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    registry = pd.read_csv(
        source_inputs["price_registry_path"],
        dtype=str,
        keep_default_na=False,
    )
    registry.loc[
        registry["resolution_id"].eq("price_no_episode_before_cutoff"),
        "exchange_ratio",
    ] = "2"
    registry.to_csv(source_inputs["price_registry_path"], index=False)

    errors = validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )

    assert any("applied_price_resolution_semantic_sha256" in error for error in errors)


def test_normalized_price_filename_collision_fails_closed(
    source_inputs: dict[str, object],
) -> None:
    duplicate = source_inputs["price_dir"] / "1111.0.csv"
    pd.read_csv(source_inputs["price_dir"] / "1111.csv").to_csv(
        duplicate,
        index=False,
    )
    cutoff_monthly = load_cutoff_monthly_revenue_subset(
        source_inputs["revenue_path"],
        source_inputs["monthly_registry_path"],
    )
    with pytest.raises(RuntimeError, match="repeats a normalized stock id"):
        cutoff_price_input_lineage(cutoff_monthly, source_inputs["price_dir"])


def test_duplicate_price_dates_fail_closed_in_producer_and_independent_validator(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    price_path = source_inputs["price_dir"] / "1111.csv"
    price = pd.read_csv(price_path, dtype=str, keep_default_na=False)
    conflicting = price.loc[price["date"].eq("20260709")].copy()
    conflicting.loc[:, "close"] = "99"
    pd.concat([price, conflicting], ignore_index=True).to_csv(price_path, index=False)

    cutoff_monthly = load_cutoff_monthly_revenue_subset(
        source_inputs["revenue_path"],
        source_inputs["monthly_registry_path"],
    )
    with pytest.raises(RuntimeError, match="repeats trading dates within cutoff"):
        cutoff_price_input_lineage(cutoff_monthly, source_inputs["price_dir"])

    errors = validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )
    assert any("repeats trading dates within cutoff" in error for error in errors)


def test_post_cutoff_raw_changes_do_not_change_cutoff_input_hashes(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    before_monthly = load_cutoff_monthly_revenue_subset(
        source_inputs["revenue_path"],
        source_inputs["monthly_registry_path"],
    )
    before_monthly_sha = canonical_monthly_revenue_history_table_sha256(before_monthly)
    before_price = cutoff_price_input_lineage(
        before_monthly,
        source_inputs["price_dir"],
    )

    raw = pd.read_csv(
        source_inputs["revenue_path"],
        dtype=str,
        keep_default_na=False,
    )
    future = _raw_row(
        stock_id="3333",
        revenue_period="202606",
        market="listed",
        market_name="TWSE",
        source_date="20260720",
        source_file="data/monthly_revenue_history/raw/future_only.csv",
    )
    pd.concat([raw, pd.DataFrame([future])], ignore_index=True).to_csv(
        source_inputs["revenue_path"],
        index=False,
    )
    price_path = source_inputs["price_dir"] / "1111.csv"
    price = pd.read_csv(price_path, dtype=str, keep_default_na=False)
    price.loc[price["date"].eq("20260714"), "close"] = "999"
    price.to_csv(price_path, index=False)
    pd.DataFrame(_price_rows()).to_csv(
        source_inputs["price_dir"] / "9999.csv",
        index=False,
    )

    after_monthly = load_cutoff_monthly_revenue_subset(
        source_inputs["revenue_path"],
        source_inputs["monthly_registry_path"],
    )
    after_price = cutoff_price_input_lineage(
        after_monthly,
        source_inputs["price_dir"],
    )
    assert canonical_monthly_revenue_history_table_sha256(after_monthly) == before_monthly_sha
    assert after_price == before_price

    _current_full_summary, current_full_detail = build_source_first_condition_audit(
        source_inputs["revenue_path"],
        source_inputs["price_dir"],
        source_inputs["monthly_registry_path"],
        source_inputs["price_registry_path"],
    )
    assert not current_full_detail.equals(source_inputs["full_detail"])
    assert validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    ) == []


def test_independent_validator_rejects_pre_cutoff_revenue_mutation(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    raw = pd.read_csv(
        source_inputs["revenue_path"],
        dtype=str,
        keep_default_na=False,
    )
    target = raw["stock_id"].eq("1111") & raw["source_table_date"].eq("20260710")
    assert int(target.sum()) == 1
    raw.loc[target, "monthly_revenue"] = "1001"
    raw.to_csv(source_inputs["revenue_path"], index=False)

    errors = validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )

    assert any(
        "cutoff_revenue_subset_semantic_sha256 source recomputation mismatch" in error
        for error in errors
    )


def test_independent_validator_ignores_post_cutoff_resolution_changes(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    monthly_registry = pd.read_csv(
        source_inputs["monthly_registry_path"],
        dtype=str,
        keep_default_na=False,
    )
    monthly_registry.loc[
        monthly_registry["resolution_id"].eq("future_cross_market_mirror"),
        "evidence_url",
    ] = "https://example.test/future-evidence-updated"
    monthly_registry.to_csv(source_inputs["monthly_registry_path"], index=False)

    price_registry = pd.read_csv(
        source_inputs["price_registry_path"],
        dtype=str,
        keep_default_na=False,
    )
    price_registry.loc[
        price_registry["resolution_id"].eq("price_after_cutoff"),
        "exchange_ratio",
    ] = "2"
    price_registry.to_csv(source_inputs["price_registry_path"], index=False)

    assert validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    ) == []


def test_independent_validator_rejects_pre_cutoff_monthly_resolution_mutation(
    source_inputs: dict[str, object],
) -> None:
    manifest = _build(source_inputs)
    registry = pd.read_csv(
        source_inputs["monthly_registry_path"],
        dtype=str,
        keep_default_na=False,
    )
    registry.loc[
        registry["resolution_id"].eq("cutoff_cross_market_mirror"),
        "evidence_url",
    ] = "https://example.test/cutoff-evidence-mutated"
    registry.to_csv(source_inputs["monthly_registry_path"], index=False)

    errors = validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )

    assert any(
        "applied_monthly_resolution_semantic_sha256 source recomputation mismatch"
        in error
        for error in errors
    )


def test_independent_validator_does_not_import_business_producers() -> None:
    source = Path(validator.__file__).read_text(encoding="utf-8")
    assert "import revenue_unreacted_range_source_snapshot_projection" not in source
    assert "from revenue_unreacted_range_source_snapshot_projection" not in source
    assert "import revenue_unreacted_range_source_first_condition_audit" not in source
    assert "from revenue_unreacted_range_source_first_condition_audit" not in source


def test_projection_stage_reuses_immutable_capture_without_current_source_rebuild(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    projected_detail = pd.DataFrame([{"view": "projected"}])
    manifest = pd.DataFrame([{"view": "manifest"}])
    calls: list[tuple[str, object, object]] = []

    monkeypatch.setattr(
        orchestrator,
        "load_immutable_source_snapshot_projection",
        lambda: (manifest, projected_detail),
    )
    monkeypatch.setattr(
        orchestrator,
        "build_source_first_condition_audit",
        lambda *_args, **_kwargs: pytest.fail(
            "projection stage rebuilt the mutable current source"
        ),
    )
    assert not hasattr(orchestrator, "build_source_snapshot_projection_manifest")
    monkeypatch.setattr(
        orchestrator,
        "write_source_first_condition_audit",
        lambda *_args, **_kwargs: pytest.fail(
            "projection stage rewrote the mutable current-source audit"
        ),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_source_snapshot_projection",
        lambda bound_manifest, detail: calls.append(
            ("projection", bound_manifest, detail)
        ),
    )

    orchestrator.build_and_write_source_snapshot_projection()

    assert calls == [
        ("projection", manifest, projected_detail),
    ]


def test_projection_chain_stage_rebuilds_cutoff_consumers_in_dependency_order(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    frames = {
        name: pd.DataFrame([{"view": name}])
        for name in (
            "fixed_detail",
            "projected_detail",
            "manifest",
            "lag_strength_summary",
            "lag_strength_detail",
            "launch_summary",
            "launch_detail",
            "launch_feature",
            "forward_summary",
            "forward_detail",
            "forward_events",
            "forward_feature",
            "forward_review",
            "rearmed_summary",
            "rearmed_detail",
            "rearmed_review",
            "lag_summary",
            "lag_detail",
            "position_summary",
            "position_detail",
            "position_transition",
            "low_mid_summary",
            "low_mid_detail",
            "low_mid_paired",
            "low_mid_contrast",
        )
    }
    prepared = pd.DataFrame([{"prepared": True}])
    projected_daily = {"1111": pd.DataFrame([{"date": CUTOFF_DATE}])}
    writes: list[str] = []

    monkeypatch.setattr(
        orchestrator,
        "load_immutable_source_snapshot_projection",
        lambda: (frames["manifest"], frames["projected_detail"]),
    )
    monkeypatch.setattr(
        orchestrator,
        "build_source_first_condition_audit",
        lambda *_args, **_kwargs: pytest.fail(
            "projection chain rebuilt the mutable current source"
        ),
    )
    assert not hasattr(orchestrator, "build_source_snapshot_projection_manifest")
    monkeypatch.setattr(
        orchestrator,
        "build_revenue_unreacted_range_research_frame",
        lambda: pd.DataFrame([{"frame": True}]),
    )
    monkeypatch.setattr(
        orchestrator,
        "_revenue_unreacted_timing_prepared_frame",
        lambda _frame: prepared,
    )
    monkeypatch.setattr(
        orchestrator,
        "_attach_revenue_signal_market_regime",
        lambda value: value,
    )
    monkeypatch.setattr(
        orchestrator.pd,
        "read_csv",
        lambda path, **_kwargs: (
            frames["fixed_detail"]
            if path == orchestrator.FIXED_CONFIRMATION_DETAIL_CSV
            else pytest.fail(f"projection chain read an unexpected CSV: {path}")
        ),
    )

    def fake_lag_strength(
        fixed_detail,
        *,
        source_projection_manifest,
        projected_source_detail,
    ):
        assert fixed_detail is frames["fixed_detail"]
        assert source_projection_manifest is frames["manifest"]
        assert projected_source_detail is frames["projected_detail"]
        return frames["lag_strength_summary"], frames["lag_strength_detail"]

    monkeypatch.setattr(orchestrator, "build_lag_strength_matrix", fake_lag_strength)

    def fake_launch(
        _prepared,
        lag_strength_detail,
        *,
        observation_cutoff_date=None,
    ):
        assert _prepared is prepared
        assert lag_strength_detail is frames["lag_strength_detail"]
        assert observation_cutoff_date == CUTOFF_DATE
        return (
            frames["launch_summary"],
            frames["launch_detail"],
            frames["launch_feature"],
        )

    monkeypatch.setattr(
        orchestrator,
        "build_launch_timing_feature_audit",
        fake_launch,
    )

    def fake_prepare(_prepared, source, *, observation_cutoff_date=None):
        assert _prepared is prepared
        assert source is frames["projected_detail"]
        assert observation_cutoff_date == CUTOFF_DATE
        return projected_daily

    monkeypatch.setattr(orchestrator, "prepare_daily_by_stock", fake_prepare)

    def fake_forward(*, source_detail, daily_by_stock, source_projection_manifest):
        assert source_detail is frames["projected_detail"]
        assert daily_by_stock is projected_daily
        assert source_projection_manifest is frames["manifest"]
        return (
            frames["forward_summary"],
            frames["forward_detail"],
            frames["forward_events"],
            frames["forward_feature"],
            frames["forward_review"],
        )

    monkeypatch.setattr(
        orchestrator,
        "build_forward_confirmation_feature_audit",
        fake_forward,
    )

    def fake_rearmed(*, source_detail, daily_by_stock, source_projection_manifest):
        assert source_detail is frames["projected_detail"]
        assert daily_by_stock is projected_daily
        assert source_projection_manifest is frames["manifest"]
        return (
            frames["rearmed_summary"],
            frames["rearmed_detail"],
            frames["rearmed_review"],
        )

    monkeypatch.setattr(orchestrator, "build_rearmed_operation_grid", fake_rearmed)

    def fake_lag(*, operation_detail, source_detail, source_projection_manifest):
        assert operation_detail is frames["rearmed_detail"]
        assert source_detail is frames["projected_detail"]
        assert source_projection_manifest is frames["manifest"]
        return frames["lag_summary"], frames["lag_detail"]

    monkeypatch.setattr(orchestrator, "build_operation_lag_bucket_audit", fake_lag)

    def fake_low_mid(source, rearmed, daily):
        assert source is frames["projected_detail"]
        assert rearmed is frames["rearmed_detail"]
        assert daily is projected_daily
        return (
            frames["low_mid_summary"],
            frames["low_mid_detail"],
            frames["low_mid_paired"],
            frames["low_mid_contrast"],
        )

    monkeypatch.setattr(
        orchestrator,
        "build_low_mid_falling_candidate_audit",
        fake_low_mid,
    )
    monkeypatch.setattr(
        orchestrator,
        "write_source_first_condition_audit",
        lambda *_args, **_kwargs: pytest.fail(
            "projection chain rewrote the mutable current-source audit"
        ),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_source_snapshot_projection",
        lambda *_args, **_kwargs: pytest.fail(
            "projection chain rewrote the pinned source projection"
        ),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_lag_strength_matrix",
        lambda summary, detail: (
            writes.append("lag_strength")
            if summary is frames["lag_strength_summary"]
            and detail is frames["lag_strength_detail"]
            else pytest.fail("projection chain wrote the wrong lag-strength frames")
        ),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_launch_timing_feature_audit",
        lambda summary, detail, feature: (
            writes.append("launch")
            if summary is frames["launch_summary"]
            and detail is frames["launch_detail"]
            and feature is frames["launch_feature"]
            else pytest.fail("projection chain wrote the wrong launch frames")
        ),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_forward_confirmation_feature_audit",
        lambda *_args: writes.append("forward"),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_rearmed_operation_grid",
        lambda *_args: writes.append("rearmed"),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_operation_lag_bucket_audit",
        lambda *_args: writes.append("lag"),
    )

    def fake_position():
        assert writes == [
            "lag_strength",
            "launch",
            "forward",
            "rearmed",
            "lag",
        ]
        return (
            frames["position_summary"],
            frames["position_detail"],
            frames["position_transition"],
        )

    monkeypatch.setattr(orchestrator, "build_position_shape_transition_matrix", fake_position)
    monkeypatch.setattr(
        orchestrator,
        "write_position_shape_transition_matrix",
        lambda *_args: writes.append("position_shape"),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_low_mid_falling_candidate_audit",
        lambda *_args: writes.append("low_mid"),
    )
    orchestrator.build_and_write_source_snapshot_projection_chain()

    assert writes == [
        "lag_strength",
        "launch",
        "forward",
        "rearmed",
        "lag",
        "position_shape",
        "low_mid",
    ]


def test_v2_manifest_is_predecessor_bound_and_pending_supersede(
    source_inputs: dict[str, object],
    tmp_path: Path,
) -> None:
    manifest = build_source_snapshot_projection_v2_manifest(
        source_inputs["full_detail"],
        source_inputs["projected_detail"],
        predecessor_manifest_bytes_sha256=V1_EXPECTED_MANIFEST_BYTES_SHA256,
        predecessor_detail_bytes_sha256=V1_EXPECTED_DETAIL_BYTES_SHA256,
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
        generated_at="2026-08-22 00:00:00 Asia/Taipei",
    )

    row = manifest.iloc[0]
    assert list(manifest.columns) == list(V2_MANIFEST_COLUMNS)
    assert row["artifact_version"] == V2_PROJECTION_VERSION
    assert row["projection_version"] == V2_PROJECTION_VERSION
    assert row["projection_policy_id"] == V2_PROJECTION_POLICY_ID
    assert row["predecessor_projection_version"] == V1_PROJECTION_VERSION
    assert (
        row["predecessor_manifest_bytes_sha256"]
        == V1_EXPECTED_MANIFEST_BYTES_SHA256
    )
    assert row["predecessor_detail_bytes_sha256"] == V1_EXPECTED_DETAIL_BYTES_SHA256
    assert row["lineage_change_reason"] == V2_LINEAGE_CHANGE_REASON
    assert row["candidate_status"] == V2_CANDIDATE_STATUS
    assert validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    ) == []
    manifest_path = tmp_path / "v2_manifest.csv"
    manifest.to_csv(manifest_path, index=False)
    lineage, row_count, semantic_sha = (
        source_first_validator._pinned_monthly_revenue_lineage(manifest_path)
    )
    assert lineage["monthly_revenue_history_blob_sha256"] == str(
        row["monthly_revenue_history_blob_sha256"]
    )
    assert row_count == int(row["cutoff_revenue_subset_row_count"])
    assert semantic_sha == row["cutoff_revenue_subset_semantic_sha256"]

    drift = manifest.copy()
    drift.loc[0, "lineage_change_reason"] = "partial_date_list"
    drift.to_csv(manifest_path, index=False)
    with pytest.raises(RuntimeError, match="lineage_change_reason drift"):
        source_first_validator._pinned_monthly_revenue_lineage(manifest_path)


def test_source_first_default_manifest_routes_zero_to_canonical_and_full_to_v2(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exact7 = _bind_source_first_exact7_paths(tmp_path, monkeypatch)
    canonical_manifest = tmp_path / "canonical_v1_manifest.csv"
    canonical_manifest.write_text("projection_version\nv1\n", encoding="utf-8")
    monkeypatch.setattr(
        source_first_validator,
        "SOURCE_SNAPSHOT_PROJECTION_MANIFEST_CSV",
        canonical_manifest,
    )
    _bind_source_first_audit_outputs(tmp_path, monkeypatch)
    routed: list[Path] = []

    def stop_after_binding(path: Path):
        routed.append(path)
        raise RuntimeError("routing probe stop")

    monkeypatch.setattr(
        source_first_validator,
        "_pinned_monthly_revenue_lineage",
        stop_after_binding,
    )

    assert source_first_validator.validate() == [
        "source-first current monthly revenue lineage cannot be verified: "
        "routing probe stop"
    ]
    assert routed == [canonical_manifest]

    for path in exact7.values():
        path.write_text("present\n", encoding="utf-8")
    assert source_first_validator.validate() == [
        "source-first current monthly revenue lineage cannot be verified: "
        "routing probe stop"
    ]
    assert routed == [canonical_manifest, exact7["V2_MANIFEST_CSV"]]


def test_source_first_default_manifest_partial_exact7_fails_without_replay(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exact7 = _bind_source_first_exact7_paths(tmp_path, monkeypatch)
    exact7["V1_ARCHIVE_MANIFEST_CSV"].write_text("present\n", encoding="utf-8")
    monkeypatch.setattr(
        source_first_validator,
        "_pinned_monthly_revenue_lineage",
        lambda *_args, **_kwargs: pytest.fail("partial exact7 replayed canonical v1"),
    )
    monkeypatch.setattr(
        source_first_validator,
        "_current_monthly_revenue_lineage",
        lambda *_args, **_kwargs: pytest.fail("partial exact7 replayed current source"),
    )

    errors = source_first_validator.validate()

    assert len(errors) == 6
    assert all(
        "versioned source projection exact7 closure is incomplete or unsafe"
        in error
        for error in errors
    )
    assert all("missing_or_non_file" in error for error in errors)


@pytest.mark.parametrize(
    ("unsafe_kind", "expected_state"),
    (
        ("missing", "missing_or_non_file"),
        ("directory", "directory_not_allowed"),
        ("symlink", "symlink_not_allowed"),
    ),
)
def test_source_first_default_manifest_rejects_nonfile_exact7_entries(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    unsafe_kind: str,
    expected_state: str,
) -> None:
    exact7 = _bind_source_first_exact7_paths(tmp_path, monkeypatch)
    for path in exact7.values():
        path.write_text("present\n", encoding="utf-8")
    unsafe_path = exact7["V2_PROJECTED_DETAIL_CSV"]
    if unsafe_kind == "missing":
        unsafe_path.unlink()
    elif unsafe_kind == "directory":
        unsafe_path.unlink()
        unsafe_path.mkdir()
    else:
        original_is_symlink = Path.is_symlink
        monkeypatch.setattr(
            Path,
            "is_symlink",
            lambda path: path == unsafe_path or original_is_symlink(path),
        )

    routed, errors = source_first_validator._resolve_default_projection_manifest_path()

    assert routed is None
    assert len(errors) == 1
    assert str(unsafe_path) in errors[0]
    assert expected_state in errors[0]


def test_source_first_projection_manifest_cli_default_and_explicit_bypass(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    explicit_manifest = tmp_path / "explicit_manifest.csv"
    explicit_manifest.write_text("projection_version\nv1\n", encoding="utf-8")
    assert source_first_validator.parse_args([]).projection_manifest is None
    assert source_first_validator.parse_args(
        ["--projection-manifest", str(explicit_manifest)]
    ).projection_manifest == explicit_manifest

    exact7 = _bind_source_first_exact7_paths(tmp_path, monkeypatch)
    exact7["V1_ARCHIVE_MANIFEST_CSV"].write_text("present\n", encoding="utf-8")
    _bind_source_first_audit_outputs(tmp_path, monkeypatch)
    routed: list[Path] = []
    monkeypatch.setattr(
        source_first_validator,
        "_resolve_default_projection_manifest_path",
        lambda: pytest.fail("explicit projection manifest entered default routing"),
    )

    def stop_after_binding(path: Path):
        routed.append(path)
        raise RuntimeError("explicit routing probe stop")

    monkeypatch.setattr(
        source_first_validator,
        "_pinned_monthly_revenue_lineage",
        stop_after_binding,
    )

    assert source_first_validator.validate(
        projection_manifest_path=explicit_manifest
    ) == [
        "source-first current monthly revenue lineage cannot be verified: "
        "explicit routing probe stop"
    ]
    assert routed == [explicit_manifest]


def test_archive_v1_preserves_canonical_raw_bytes(
    source_inputs: dict[str, object],
    tmp_path: Path,
) -> None:
    manifest = _build(source_inputs)
    detail = source_inputs["projected_detail"]
    canonical_manifest = tmp_path / "canonical_manifest.csv"
    canonical_detail = tmp_path / "canonical_detail.csv"
    archive_manifest = tmp_path / "archive_manifest.csv"
    archive_detail = tmp_path / "archive_detail.csv"
    evidence_path = tmp_path / "archive_evidence.csv"
    manifest.to_csv(canonical_manifest, index=False)
    detail.to_csv(canonical_detail, index=False)
    manifest_bytes = canonical_manifest.read_bytes()
    detail_bytes = canonical_detail.read_bytes()
    manifest_sha = projection._file_sha256(canonical_manifest)
    detail_sha = projection._file_sha256(canonical_detail)
    detail_semantic_sha = canonical_projected_source_detail_semantic_sha256(detail)

    evidence = archive_immutable_v1_projection(
        canonical_manifest_path=canonical_manifest,
        canonical_detail_path=canonical_detail,
        archive_manifest_path=archive_manifest,
        archive_detail_path=archive_detail,
        evidence_path=evidence_path,
        expected_manifest_bytes=len(manifest_bytes),
        expected_manifest_bytes_sha256=manifest_sha,
        expected_detail_bytes=len(detail_bytes),
        expected_detail_bytes_sha256=detail_sha,
        expected_detail_row_count=len(detail),
        expected_detail_semantic_sha256=detail_semantic_sha,
    )

    assert list(evidence.columns) == list(ARCHIVE_EVIDENCE_COLUMNS)
    assert archive_manifest.read_bytes() == manifest_bytes
    assert archive_detail.read_bytes() == detail_bytes
    assert canonical_manifest.read_bytes() == manifest_bytes
    assert canonical_detail.read_bytes() == detail_bytes
    assert str(evidence.iloc[0]["immutable_copy_verified"]).lower() == "true"

    archive_manifest.write_bytes(b"different")
    with pytest.raises(RuntimeError, match="different bytes"):
        archive_immutable_v1_projection(
            canonical_manifest_path=canonical_manifest,
            canonical_detail_path=canonical_detail,
            archive_manifest_path=archive_manifest,
            archive_detail_path=archive_detail,
            evidence_path=evidence_path,
            expected_manifest_bytes=len(manifest_bytes),
            expected_manifest_bytes_sha256=manifest_sha,
            expected_detail_bytes=len(detail_bytes),
            expected_detail_bytes_sha256=detail_sha,
            expected_detail_row_count=len(detail),
            expected_detail_semantic_sha256=detail_semantic_sha,
        )


def test_v2_candidate_writer_never_touches_canonical_latest(
    source_inputs: dict[str, object],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest = build_source_snapshot_projection_v2_manifest(
        source_inputs["full_detail"],
        source_inputs["projected_detail"],
        predecessor_manifest_bytes_sha256=V1_EXPECTED_MANIFEST_BYTES_SHA256,
        predecessor_detail_bytes_sha256=V1_EXPECTED_DETAIL_BYTES_SHA256,
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
        generated_at="2026-08-22 00:00:00 Asia/Taipei",
    )
    canonical_manifest = tmp_path / "canonical_latest_manifest.csv"
    canonical_detail = tmp_path / "canonical_latest_detail.csv"
    canonical_manifest.write_bytes(b"immutable canonical manifest")
    canonical_detail.write_bytes(b"immutable canonical detail")
    predecessor_manifest = tmp_path / "v1_manifest.csv"
    predecessor_detail = tmp_path / "v1_detail.csv"
    predecessor_manifest.write_bytes(b"archive manifest")
    predecessor_detail.write_bytes(b"archive detail")

    def fake_file_sha(path: Path) -> str:
        if Path(path) == predecessor_manifest:
            return V1_EXPECTED_MANIFEST_BYTES_SHA256
        if Path(path) == predecessor_detail:
            return V1_EXPECTED_DETAIL_BYTES_SHA256
        return pytest.fail(f"unexpected SHA path: {path}")

    monkeypatch.setattr(projection, "_file_sha256", fake_file_sha)
    candidate_manifest = tmp_path / "candidate_manifest.csv"
    candidate_detail = tmp_path / "candidate_detail.csv"
    write_source_snapshot_projection_v2_candidate(
        manifest,
        source_inputs["projected_detail"],
        manifest_path=candidate_manifest,
        detail_path=candidate_detail,
        predecessor_manifest_path=predecessor_manifest,
        predecessor_detail_path=predecessor_detail,
    )

    assert candidate_manifest.is_file()
    assert candidate_detail.is_file()
    assert canonical_manifest.read_bytes() == b"immutable canonical manifest"
    assert canonical_detail.read_bytes() == b"immutable canonical detail"


def test_v2_candidate_writer_enforces_exact_repository_destinations(
    source_inputs: dict[str, object],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest = build_source_snapshot_projection_v2_manifest(
        source_inputs["full_detail"],
        source_inputs["projected_detail"],
        predecessor_manifest_bytes_sha256=V1_EXPECTED_MANIFEST_BYTES_SHA256,
        predecessor_detail_bytes_sha256=V1_EXPECTED_DETAIL_BYTES_SHA256,
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
        generated_at="2026-08-22 00:00:00 Asia/Taipei",
    )
    repository_root = tmp_path / "repository"
    allowed_manifest = repository_root / "history" / "candidate_v2_manifest.csv"
    allowed_detail = repository_root / "history" / "candidate_v2_detail.csv"
    monkeypatch.setattr(projection, "ROOT", repository_root)
    monkeypatch.setattr(projection, "V2_CANDIDATE_MANIFEST_CSV", allowed_manifest)
    monkeypatch.setattr(projection, "V2_CANDIDATE_DETAIL_CSV", allowed_detail)
    forbidden = (
        repository_root / "output/latest/canonical_manifest.csv",
        repository_root / "output/latest/canonical_detail.csv",
        repository_root / "output/history/canonical_manifest.csv",
        repository_root / "docs/latest/canonical_manifest.csv",
        repository_root / "output/latest/alias/../canonical_manifest.csv",
    )

    outside_manifest = tmp_path / "outside_repository_manifest.csv"
    outside_detail = tmp_path / "outside_repository_detail.csv"
    for destination in forbidden:
        for destination_role in ("manifest", "detail"):
            with pytest.raises(
                RuntimeError,
                match="refuses a non-versioned repository destination",
            ):
                write_source_snapshot_projection_v2_candidate(
                    manifest,
                    source_inputs["projected_detail"],
                    manifest_path=(
                        destination
                        if destination_role == "manifest"
                        else outside_manifest
                    ),
                    detail_path=(
                        destination
                        if destination_role == "detail"
                        else outside_detail
                    ),
                    predecessor_manifest_path=tmp_path / "missing_v1_manifest.csv",
                    predecessor_detail_path=tmp_path / "missing_v1_detail.csv",
                )

    assert not repository_root.exists()
    assert not outside_manifest.exists()
    assert not outside_detail.exists()

    predecessor_manifest = tmp_path / "v1_manifest.csv"
    predecessor_detail = tmp_path / "v1_detail.csv"
    predecessor_manifest.write_bytes(b"immutable v1 manifest")
    predecessor_detail.write_bytes(b"immutable v1 detail")

    def fake_file_sha(path: Path) -> str:
        if Path(path) == predecessor_manifest:
            return V1_EXPECTED_MANIFEST_BYTES_SHA256
        if Path(path) == predecessor_detail:
            return V1_EXPECTED_DETAIL_BYTES_SHA256
        return pytest.fail(f"unexpected SHA path: {path}")

    monkeypatch.setattr(projection, "_file_sha256", fake_file_sha)
    write_source_snapshot_projection_v2_candidate(
        manifest,
        source_inputs["projected_detail"],
        manifest_path=allowed_manifest,
        detail_path=allowed_detail,
        predecessor_manifest_path=predecessor_manifest,
        predecessor_detail_path=predecessor_detail,
    )

    assert allowed_manifest.read_bytes() == manifest.to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")
    assert allowed_detail.read_bytes() == source_inputs["projected_detail"].to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")


def test_v2_supersede_copies_exact3_and_appends_history_without_losing_v1(
    source_inputs: dict[str, object],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths, immutable = _prepare_v2_supersede_fixture(
        source_inputs=source_inputs,
        tmp_path=tmp_path,
        monkeypatch=monkeypatch,
    )
    candidate_manifest_before = paths["candidate_manifest_path"].read_bytes()
    candidate_detail_before = paths["candidate_detail_path"].read_bytes()
    v1_manifest_before = paths["v1_manifest_path"].read_bytes()
    v1_detail_before = paths["v1_detail_path"].read_bytes()

    evidence = supersede_source_snapshot_projection_v2_candidate(
        superseded_at="2026-08-22 12:34:56 Asia/Taipei",
        **paths,
    )

    assert list(evidence.columns) == list(V2_SUPERSEDE_EVIDENCE_COLUMNS)
    assert paths["canonical_manifest_path"].read_bytes() == immutable["v2_manifest"]
    assert paths["canonical_detail_path"].read_bytes() == immutable["v2_detail"]
    assert paths["docs_manifest_path"].read_bytes() == immutable["v2_manifest"]
    history = pd.read_csv(
        paths["history_manifest_path"],
        dtype=str,
        keep_default_na=False,
    )
    assert list(history.columns) == list(V2_MANIFEST_COLUMNS)
    assert history["projection_version"].tolist() == [
        V1_PROJECTION_VERSION,
        V2_PROJECTION_VERSION,
    ]
    assert history.iloc[0][list(projection.V2_MANIFEST_EXTENSION_COLUMNS)].eq("").all()
    assert history.iloc[[1]].reset_index(drop=True).equals(
        pd.read_csv(
            paths["candidate_manifest_path"],
            dtype=str,
            keep_default_na=False,
        )
    )
    evidence_row = pd.read_csv(
        paths["evidence_path"],
        dtype=str,
        keep_default_na=False,
    ).iloc[0]
    assert evidence_row["canonical_history_preimage_row_count"] == "1"
    assert evidence_row["canonical_history_postimage_row_count"] == "2"
    assert evidence_row["canonical_history_postimage_v1_row_count"] == "1"
    assert evidence_row["canonical_history_postimage_v2_row_count"] == "1"
    assert evidence_row["canonical_history_append_only_verified"].lower() == "true"
    assert evidence_row["forward_holdout_refreshed"].lower() == "false"
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        assert evidence_row[column].lower() == "false"
    assert paths["candidate_manifest_path"].read_bytes() == candidate_manifest_before
    assert paths["candidate_detail_path"].read_bytes() == candidate_detail_before
    assert paths["v1_manifest_path"].read_bytes() == v1_manifest_before
    assert paths["v1_detail_path"].read_bytes() == v1_detail_before
    assert validator._validate_canonical_v2_supersede(
        canonical_manifest_path=paths["canonical_manifest_path"],
        canonical_detail_path=paths["canonical_detail_path"],
        history_manifest_path=paths["history_manifest_path"],
        docs_manifest_path=paths["docs_manifest_path"],
        evidence_path=paths["evidence_path"],
        v1_manifest_path=paths["v1_manifest_path"],
        v1_detail_path=paths["v1_detail_path"],
        v2_manifest_path=paths["candidate_manifest_path"],
        v2_detail_path=paths["candidate_detail_path"],
        diff_summary_path=paths["diff_summary_path"],
        diff_detail_path=paths["diff_detail_path"],
    ) == []

    postimage = {path: path.read_bytes() for path in paths.values()}
    supersede_source_snapshot_projection_v2_candidate(**paths)
    assert {path: path.read_bytes() for path in paths.values()} == postimage


def test_v2_supersede_fails_closed_before_writes_on_unclassified_drift(
    source_inputs: dict[str, object],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths, _immutable = _prepare_v2_supersede_fixture(
        source_inputs=source_inputs,
        tmp_path=tmp_path,
        monkeypatch=monkeypatch,
    )
    diff_summary = pd.read_csv(
        paths["diff_summary_path"],
        dtype=str,
        keep_default_na=False,
    )
    diff_summary.loc[0, "unclassified_semantic_drift_count"] = "1"
    diff_summary.to_csv(paths["diff_summary_path"], index=False, lineterminator="\n")
    preimage = {
        name: path.read_bytes()
        for name, path in paths.items()
        if name != "evidence_path"
    }

    with pytest.raises(RuntimeError, match="unclassified_semantic_drift_count"):
        supersede_source_snapshot_projection_v2_candidate(
            superseded_at="2026-08-22 12:34:56 Asia/Taipei",
            **paths,
        )

    assert not paths["evidence_path"].exists()
    assert {
        name: path.read_bytes()
        for name, path in paths.items()
        if name != "evidence_path"
    } == preimage


def test_v2_supersede_rolls_back_exact_outputs_on_postimage_validation_failure(
    source_inputs: dict[str, object],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths, _immutable = _prepare_v2_supersede_fixture(
        source_inputs=source_inputs,
        tmp_path=tmp_path,
        monkeypatch=monkeypatch,
    )
    preimage = {
        name: path.read_bytes()
        for name, path in paths.items()
        if name != "evidence_path"
    }
    monkeypatch.setattr(
        projection,
        "validate_source_snapshot_projection_v2_supersede",
        lambda **_kwargs: (_ for _ in ()).throw(
            RuntimeError("forced postimage validation failure")
        ),
    )

    with pytest.raises(RuntimeError, match="forced postimage validation failure"):
        supersede_source_snapshot_projection_v2_candidate(
            superseded_at="2026-08-22 12:34:56 Asia/Taipei",
            **paths,
        )

    assert not paths["evidence_path"].exists()
    assert {
        name: path.read_bytes()
        for name, path in paths.items()
        if name != "evidence_path"
    } == preimage


def test_legacy_canonical_writer_rejects_v2_before_changing_any_bytes(
    source_inputs: dict[str, object],
    tmp_path: Path,
) -> None:
    manifest = build_source_snapshot_projection_v2_manifest(
        source_inputs["full_detail"],
        source_inputs["projected_detail"],
        predecessor_manifest_bytes_sha256=V1_EXPECTED_MANIFEST_BYTES_SHA256,
        predecessor_detail_bytes_sha256=V1_EXPECTED_DETAIL_BYTES_SHA256,
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
        generated_at="2026-08-22 00:00:00 Asia/Taipei",
    )
    canonical_paths = {
        "latest_manifest_path": tmp_path / "canonical_manifest.csv",
        "latest_detail_path": tmp_path / "canonical_detail.csv",
        "history_manifest_path": tmp_path / "canonical_history.csv",
        "docs_manifest_path": tmp_path / "canonical_docs.csv",
    }
    original_bytes: dict[Path, bytes] = {}
    for index, path in enumerate(canonical_paths.values(), start=1):
        payload = f"immutable canonical payload {index}".encode()
        path.write_bytes(payload)
        original_bytes[path] = payload

    with pytest.raises(RuntimeError, match="legacy canonical.*accepts only"):
        write_source_snapshot_projection(
            manifest,
            source_inputs["projected_detail"],
            **canonical_paths,
        )

    assert {
        path: path.read_bytes() for path in canonical_paths.values()
    } == original_bytes


def test_canonical_projection_loader_rejects_v2_without_supersede_closure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        orchestrator,
        "load_source_snapshot_projection_manifest",
        lambda: pd.DataFrame(
            [{"projection_version": V2_PROJECTION_VERSION}]
        ),
    )
    monkeypatch.setattr(
        orchestrator,
        "load_projected_source_detail",
        lambda: pytest.fail("canonical v2 detail reached a downstream consumer"),
    )
    monkeypatch.setattr(
        orchestrator,
        "validate_source_snapshot_projection",
        lambda: ["missing supersede evidence"],
    )
    monkeypatch.setattr(
        orchestrator,
        "validate_projection_binding",
        lambda *_args, **_kwargs: pytest.fail(
            "canonical v2 reached downstream binding validation"
        ),
    )

    with pytest.raises(RuntimeError, match="supersede closure failed.*missing supersede evidence"):
        orchestrator.load_immutable_source_snapshot_projection()


def test_canonical_projection_loader_accepts_only_validated_v2(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest = pd.DataFrame([{"projection_version": V2_PROJECTION_VERSION}])
    detail = pd.DataFrame([{"stock_id": "1111"}])
    calls: list[str] = []
    monkeypatch.setattr(
        orchestrator,
        "load_source_snapshot_projection_manifest",
        lambda: manifest,
    )
    monkeypatch.setattr(
        orchestrator,
        "validate_source_snapshot_projection",
        lambda: calls.append("independent_supersede_closure") or [],
    )
    monkeypatch.setattr(
        orchestrator,
        "load_projected_source_detail",
        lambda: calls.append("load_detail") or detail,
    )

    def fake_binding(actual_manifest, actual_detail, **kwargs):
        assert actual_manifest is manifest
        assert actual_detail is detail
        assert kwargs["expected_cutoff_date"] == orchestrator.PRICE_HISTORY_CUTOFF_DATE
        calls.append("bind_detail")

    monkeypatch.setattr(orchestrator, "validate_projection_binding", fake_binding)

    assert orchestrator.load_immutable_source_snapshot_projection() == (manifest, detail)
    assert calls == [
        "independent_supersede_closure",
        "load_detail",
        "bind_detail",
    ]


def test_supersede_and_chain_stage_orders_selection_before_consumers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[str] = []
    monkeypatch.setattr(
        orchestrator,
        "supersede_source_snapshot_projection_v2_candidate",
        lambda: calls.append("supersede"),
    )
    monkeypatch.setattr(
        orchestrator,
        "build_and_write_source_snapshot_projection_chain",
        lambda: calls.append("chain"),
    )

    orchestrator.build_and_write_source_snapshot_projection_supersede_and_chain()

    assert calls == ["supersede", "chain"]


def test_rebaseline_stage_builds_only_candidate_archive_source_first_and_diff(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import revenue_unreacted_range_source_snapshot_projection_v1_v2_diff as diff

    canonical_manifest = tmp_path / "canonical_manifest.csv"
    canonical_detail = tmp_path / "canonical_detail.csv"
    canonical_manifest.write_bytes(b"canonical manifest")
    canonical_detail.write_bytes(b"canonical detail")
    monkeypatch.setattr(
        orchestrator,
        "SOURCE_SNAPSHOT_V1_CANONICAL_MANIFEST_CSV",
        canonical_manifest,
    )
    monkeypatch.setattr(
        orchestrator,
        "SOURCE_SNAPSHOT_V1_CANONICAL_DETAIL_CSV",
        canonical_detail,
    )
    calls: list[str] = []
    evidence = pd.DataFrame(
        [
            {
                "canonical_manifest_sha256": V1_EXPECTED_MANIFEST_BYTES_SHA256,
                "canonical_detail_sha256": V1_EXPECTED_DETAIL_BYTES_SHA256,
            }
        ]
    )
    monkeypatch.setattr(
        orchestrator,
        "archive_immutable_v1_projection",
        lambda: calls.append("archive") or evidence,
    )
    full_summary = pd.DataFrame([{"view": "full_summary"}])
    full_detail = pd.DataFrame([{"view": "full_detail"}])
    projected_detail = pd.DataFrame([{"view": "projected_detail"}])

    def fake_source_first(*_args, observation_cutoff_date=None, **_kwargs):
        if observation_cutoff_date is None:
            calls.append("source_first_full")
            return full_summary, full_detail
        assert observation_cutoff_date == CUTOFF_DATE
        calls.append("source_first_cutoff")
        return pd.DataFrame([{"view": "projected_summary"}]), projected_detail

    monkeypatch.setattr(
        orchestrator,
        "build_source_first_condition_audit",
        fake_source_first,
    )
    candidate_manifest = pd.DataFrame([{"view": "candidate"}])

    def fake_manifest(full, projected, **kwargs):
        assert full is full_detail
        assert projected is projected_detail
        assert (
            kwargs["predecessor_manifest_bytes_sha256"]
            == V1_EXPECTED_MANIFEST_BYTES_SHA256
        )
        assert (
            kwargs["predecessor_detail_bytes_sha256"]
            == V1_EXPECTED_DETAIL_BYTES_SHA256
        )
        calls.append("candidate_manifest")
        return candidate_manifest

    monkeypatch.setattr(
        orchestrator,
        "build_source_snapshot_projection_v2_manifest",
        fake_manifest,
    )
    monkeypatch.setattr(
        orchestrator,
        "write_source_first_condition_audit",
        lambda summary, detail: (
            calls.append("write_source_first")
            if summary is full_summary and detail is full_detail
            else pytest.fail("rebaseline wrote the cutoff source-first frame")
        ),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_source_snapshot_projection_v2_candidate",
        lambda manifest, detail: (
            calls.append("write_candidate")
            if manifest is candidate_manifest and detail is projected_detail
            else pytest.fail("rebaseline wrote the wrong candidate")
        ),
    )
    diff_summary = pd.DataFrame([{"view": "diff_summary"}])
    diff_detail = pd.DataFrame([{"view": "diff_detail"}])
    monkeypatch.setattr(
        diff,
        "build_diff_from_paths",
        lambda: calls.append("build_diff") or (diff_summary, diff_detail),
    )
    monkeypatch.setattr(
        diff,
        "write_diff_artifacts",
        lambda summary, detail: (
            calls.append("write_diff")
            if summary is diff_summary and detail is diff_detail
            else pytest.fail("rebaseline wrote the wrong diff")
        ),
    )

    orchestrator.build_and_write_source_snapshot_projection_rebaseline()

    assert calls == [
        "archive",
        "source_first_full",
        "source_first_cutoff",
        "candidate_manifest",
        "write_source_first",
        "write_candidate",
        "build_diff",
        "write_diff",
    ]
    assert canonical_manifest.read_bytes() == b"canonical manifest"
    assert canonical_detail.read_bytes() == b"canonical detail"


def test_default_validator_versioned_closure_is_optional_then_fail_closed(
    tmp_path: Path,
) -> None:
    paths = {
        "v1_manifest_path": tmp_path / "v1_manifest.csv",
        "v1_detail_path": tmp_path / "v1_detail.csv",
        "v1_evidence_path": tmp_path / "v1_evidence.csv",
        "v2_manifest_path": tmp_path / "v2_manifest.csv",
        "v2_detail_path": tmp_path / "v2_detail.csv",
        "diff_summary_path": tmp_path / "diff_summary.csv",
        "diff_detail_path": tmp_path / "diff_detail.csv",
    }
    replay = {
        "revenue_path": tmp_path / "revenue.csv",
        "price_dir": tmp_path / "prices",
        "monthly_resolution_path": tmp_path / "monthly_resolution.csv",
        "price_resolution_path": tmp_path / "price_resolution.csv",
    }
    assert validator._validate_versioned_v2_closure(**replay, **paths) == []

    paths["v2_manifest_path"].mkdir()
    errors = validator._validate_versioned_v2_closure(**replay, **paths)
    assert len(errors) == 7
    assert all("missing versioned source projection closure artifact" in error for error in errors)
    paths["v2_manifest_path"].rmdir()

    paths["v2_manifest_path"].write_text("projection_version\nvalue\n", encoding="utf-8")
    errors = validator._validate_versioned_v2_closure(**replay, **paths)
    assert len(errors) == 6
    assert all("missing versioned source projection closure artifact" in error for error in errors)


def test_code_only_default_validation_preserves_existing_current_source_replay(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest_path = tmp_path / "canonical_v1_manifest.csv"
    detail_path = tmp_path / "canonical_v1_detail.csv"
    pd.DataFrame([{"projection_version": V1_PROJECTION_VERSION}]).to_csv(
        manifest_path,
        index=False,
    )
    pd.DataFrame([{"stock_id": "1111"}]).to_csv(detail_path, index=False)
    replay_paths = [tmp_path / name for name in ("revenue.csv", "monthly.csv", "price.csv")]
    for path in replay_paths:
        path.write_text("value\npresent\n", encoding="utf-8")
    price_dir = tmp_path / "prices"
    price_dir.mkdir()
    monkeypatch.setattr(validator, "MANIFEST_CSV", manifest_path)
    monkeypatch.setattr(validator, "PROJECTED_DETAIL_CSV", detail_path)
    for name in (
        "V1_ARCHIVE_MANIFEST_CSV",
        "V1_ARCHIVE_DETAIL_CSV",
        "V1_ARCHIVE_EVIDENCE_CSV",
        "V2_MANIFEST_CSV",
        "V2_PROJECTED_DETAIL_CSV",
        "V1_V2_DIFF_SUMMARY_CSV",
        "V1_V2_DIFF_DETAIL_CSV",
    ):
        monkeypatch.setattr(validator, name, tmp_path / f"missing_{name}.csv")
    calls: list[str] = []
    monkeypatch.setattr(
        validator,
        "_validate_immutable_v1_files",
        lambda *_args, **_kwargs: pytest.fail("code-only PR reinterpreted immutable v1"),
    )
    monkeypatch.setattr(
        validator,
        "validate_frames",
        lambda *_args, **_kwargs: calls.append("current_source_replay") or ["drift"],
    )

    assert validator.validate(
        manifest_path=manifest_path,
        projected_detail_path=detail_path,
        revenue_path=replay_paths[0],
        price_dir=price_dir,
        monthly_resolution_path=replay_paths[1],
        price_resolution_path=replay_paths[2],
    ) == ["drift"]
    assert calls == ["current_source_replay"]


def test_default_validator_versioned_closure_calls_v2_and_diff_validators(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = {
        "v1_manifest_path": tmp_path / "v1_manifest.csv",
        "v1_detail_path": tmp_path / "v1_detail.csv",
        "v1_evidence_path": tmp_path / "v1_evidence.csv",
        "v2_manifest_path": tmp_path / "v2_manifest.csv",
        "v2_detail_path": tmp_path / "v2_detail.csv",
        "diff_summary_path": tmp_path / "diff_summary.csv",
        "diff_detail_path": tmp_path / "diff_detail.csv",
    }
    for path in paths.values():
        pd.DataFrame([{"value": "present"}]).to_csv(path, index=False)
    replay = {
        "revenue_path": tmp_path / "revenue.csv",
        "price_dir": tmp_path / "prices",
        "monthly_resolution_path": tmp_path / "monthly_resolution.csv",
        "price_resolution_path": tmp_path / "price_resolution.csv",
    }
    for key in (
        "revenue_path",
        "monthly_resolution_path",
        "price_resolution_path",
    ):
        replay[key].write_text("value\npresent\n", encoding="utf-8")
    replay["price_dir"].mkdir()
    calls: list[str] = []
    monkeypatch.setattr(
        validator,
        "_validate_v1_archive_evidence",
        lambda **_kwargs: calls.append("archive") or [],
    )
    monkeypatch.setattr(
        validator,
        "validate_frames",
        lambda *_args, **_kwargs: calls.append("v2") or [],
    )

    def fake_diff(**kwargs):
        assert kwargs["v1_manifest_path"] == paths["v1_manifest_path"]
        assert kwargs["v2_manifest_path"] == paths["v2_manifest_path"]
        assert kwargs["diff_summary_path"] == paths["diff_summary_path"]
        assert kwargs["diff_detail_path"] == paths["diff_detail_path"]
        calls.append("diff")
        return []

    monkeypatch.setattr(
        validator,
        "_validate_projection_v1_v2_diff_subprocess",
        fake_diff,
    )
    assert validator._validate_versioned_v2_closure(**replay, **paths) == []
    assert calls == ["archive", "v2", "diff"]


def test_source_projection_validator_runs_diff_validator_as_exact_isolated_cli(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = {
        name: tmp_path / f"{name}.csv"
        for name in (
            "v1_manifest_path",
            "v1_detail_path",
            "v2_manifest_path",
            "v2_detail_path",
            "diff_summary_path",
            "diff_detail_path",
        )
    }
    observed: dict[str, object] = {}

    def fake_run(argv, **kwargs):
        observed["argv"] = list(argv)
        observed["kwargs"] = dict(kwargs)
        return subprocess.CompletedProcess(
            argv,
            0,
            stdout=validator.V1_V2_DIFF_VALIDATOR_SUCCESS + "\n",
            stderr="",
        )

    monkeypatch.setattr(validator.subprocess, "run", fake_run)

    assert validator._validate_projection_v1_v2_diff_subprocess(**paths) == []
    assert observed["argv"] == [
        sys.executable,
        "-I",
        str(validator.V1_V2_DIFF_VALIDATOR),
        "--v1-manifest",
        str(paths["v1_manifest_path"]),
        "--v1-detail",
        str(paths["v1_detail_path"]),
        "--v2-manifest",
        str(paths["v2_manifest_path"]),
        "--v2-detail",
        str(paths["v2_detail_path"]),
        "--diff-summary",
        str(paths["diff_summary_path"]),
        "--diff-detail",
        str(paths["diff_detail_path"]),
    ]
    kwargs = observed["kwargs"]
    assert kwargs["cwd"] == validator.ROOT
    assert kwargs["stdin"] == subprocess.DEVNULL
    assert kwargs["stdout"] == subprocess.PIPE
    assert kwargs["stderr"] == subprocess.PIPE
    assert kwargs["check"] is False
    assert kwargs["shell"] is False
    assert kwargs["timeout"] == validator.V1_V2_DIFF_VALIDATOR_TIMEOUT_SECONDS


@pytest.mark.parametrize(
    ("returncode", "stdout", "stderr"),
    (
        (1, "ERROR: unclassified semantic drift\n", ""),
        (0, "unexpected success text\n", ""),
        (0, validator.V1_V2_DIFF_VALIDATOR_SUCCESS + "\n", "warning"),
    ),
)
def test_source_projection_diff_cli_rejects_failure_or_nonexact_success(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    returncode: int,
    stdout: str,
    stderr: str,
) -> None:
    paths = {
        name: tmp_path / f"{name}.csv"
        for name in (
            "v1_manifest_path",
            "v1_detail_path",
            "v2_manifest_path",
            "v2_detail_path",
            "diff_summary_path",
            "diff_detail_path",
        )
    }
    monkeypatch.setattr(
        validator.subprocess,
        "run",
        lambda argv, **_kwargs: subprocess.CompletedProcess(
            argv,
            returncode,
            stdout=stdout,
            stderr=stderr,
        ),
    )

    errors = validator._validate_projection_v1_v2_diff_subprocess(**paths)

    assert len(errors) == 1
    assert "v1/v2 diff independent validator failed" in errors[0]


@pytest.mark.parametrize(
    ("failure", "expected"),
    (
        (
            subprocess.TimeoutExpired(["python", "validator.py"], 300),
            "timed out",
        ),
        (OSError("cannot execute"), "could not execute"),
    ),
)
def test_source_projection_diff_cli_fails_closed_on_execution_boundary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure: BaseException,
    expected: str,
) -> None:
    paths = {
        name: tmp_path / f"{name}.csv"
        for name in (
            "v1_manifest_path",
            "v1_detail_path",
            "v2_manifest_path",
            "v2_detail_path",
            "diff_summary_path",
            "diff_detail_path",
        )
    }

    def fail_run(*_args, **_kwargs):
        raise failure

    monkeypatch.setattr(validator.subprocess, "run", fail_run)

    errors = validator._validate_projection_v1_v2_diff_subprocess(**paths)

    assert len(errors) == 1
    assert expected in errors[0]


def test_source_projection_validator_does_not_import_diff_validator_python_code() -> None:
    tree = ast.parse(Path(validator.__file__).read_text(encoding="utf-8"))
    forbidden = (
        "validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff"
    )
    imported_modules = {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    imported_modules.update(
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    )

    assert forbidden not in imported_modules


def test_default_canonical_validator_routes_complete_exact7_to_closure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest_path = tmp_path / "canonical_v1_manifest.csv"
    detail_path = tmp_path / "canonical_v1_detail.csv"
    pd.DataFrame([{"projection_version": V1_PROJECTION_VERSION}]).to_csv(
        manifest_path,
        index=False,
    )
    pd.DataFrame([{"stock_id": "1111"}]).to_csv(detail_path, index=False)
    monkeypatch.setattr(validator, "MANIFEST_CSV", manifest_path)
    monkeypatch.setattr(validator, "PROJECTED_DETAIL_CSV", detail_path)
    monkeypatch.setattr(
        validator,
        "V2_SUPERSEDE_EVIDENCE_CSV",
        tmp_path / "absent_v2_supersede_evidence.csv",
    )
    exact7_names = (
        "V1_ARCHIVE_MANIFEST_CSV",
        "V1_ARCHIVE_DETAIL_CSV",
        "V1_ARCHIVE_EVIDENCE_CSV",
        "V2_MANIFEST_CSV",
        "V2_PROJECTED_DETAIL_CSV",
        "V1_V2_DIFF_SUMMARY_CSV",
        "V1_V2_DIFF_DETAIL_CSV",
    )
    exact7_paths: dict[str, Path] = {}
    for name in exact7_names:
        path = tmp_path / f"{name}.csv"
        path.write_text("value\npresent\n", encoding="utf-8")
        exact7_paths[name] = path
        monkeypatch.setattr(validator, name, path)
    calls: list[str] = []
    monkeypatch.setattr(
        validator,
        "_validate_immutable_v1_files",
        lambda *_args, **_kwargs: calls.append("immutable_v1") or [],
    )

    def fake_closure(**kwargs):
        assert kwargs["v1_manifest_path"] == exact7_paths["V1_ARCHIVE_MANIFEST_CSV"]
        assert kwargs["v1_detail_path"] == exact7_paths["V1_ARCHIVE_DETAIL_CSV"]
        assert kwargs["v1_evidence_path"] == exact7_paths["V1_ARCHIVE_EVIDENCE_CSV"]
        assert kwargs["v2_manifest_path"] == exact7_paths["V2_MANIFEST_CSV"]
        assert kwargs["v2_detail_path"] == exact7_paths["V2_PROJECTED_DETAIL_CSV"]
        assert kwargs["diff_summary_path"] == exact7_paths["V1_V2_DIFF_SUMMARY_CSV"]
        assert kwargs["diff_detail_path"] == exact7_paths["V1_V2_DIFF_DETAIL_CSV"]
        calls.append("v1_v2_closure")
        return ["closure evidence"]

    monkeypatch.setattr(validator, "_validate_versioned_v2_closure", fake_closure)
    monkeypatch.setattr(
        validator,
        "validate_frames",
        lambda *_args, **_kwargs: pytest.fail(
            "complete exact7 fell through to current-source replay"
        ),
    )

    assert validator.validate(
        manifest_path=manifest_path,
        projected_detail_path=detail_path,
        revenue_path=tmp_path / "revenue.csv",
        price_dir=tmp_path / "prices",
        monthly_resolution_path=tmp_path / "monthly.csv",
        price_resolution_path=tmp_path / "price.csv",
    ) == ["closure evidence"]
    assert calls == ["immutable_v1", "v1_v2_closure"]


def test_default_canonical_validator_treats_nonfile_exact7_as_started(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest_path = tmp_path / "canonical_v1_manifest.csv"
    detail_path = tmp_path / "canonical_v1_detail.csv"
    pd.DataFrame([{"projection_version": V1_PROJECTION_VERSION}]).to_csv(
        manifest_path,
        index=False,
    )
    pd.DataFrame([{"stock_id": "1111"}]).to_csv(detail_path, index=False)
    monkeypatch.setattr(validator, "MANIFEST_CSV", manifest_path)
    monkeypatch.setattr(validator, "PROJECTED_DETAIL_CSV", detail_path)
    monkeypatch.setattr(
        validator,
        "V2_SUPERSEDE_EVIDENCE_CSV",
        tmp_path / "absent_v2_supersede_evidence.csv",
    )
    exact7_names = (
        "V1_ARCHIVE_MANIFEST_CSV",
        "V1_ARCHIVE_DETAIL_CSV",
        "V1_ARCHIVE_EVIDENCE_CSV",
        "V2_MANIFEST_CSV",
        "V2_PROJECTED_DETAIL_CSV",
        "V1_V2_DIFF_SUMMARY_CSV",
        "V1_V2_DIFF_DETAIL_CSV",
    )
    for name in exact7_names:
        monkeypatch.setattr(validator, name, tmp_path / f"{name}.csv")
    validator.V2_MANIFEST_CSV.mkdir()
    monkeypatch.setattr(
        validator,
        "_validate_immutable_v1_files",
        lambda *_args, **_kwargs: [],
    )
    monkeypatch.setattr(
        validator,
        "validate_frames",
        lambda *_args, **_kwargs: pytest.fail(
            "non-file exact7 entry fell through to current-source replay"
        ),
    )

    errors = validator.validate(
        manifest_path=manifest_path,
        projected_detail_path=detail_path,
        revenue_path=tmp_path / "revenue.csv",
        price_dir=tmp_path / "prices",
        monthly_resolution_path=tmp_path / "monthly.csv",
        price_resolution_path=tmp_path / "price.csv",
    )

    assert len(errors) == 7
    assert all("missing versioned source projection closure artifact" in error for error in errors)


def test_explicit_v2_validation_does_not_reenter_default_closure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest_path = tmp_path / "v2_manifest.csv"
    detail_path = tmp_path / "v2_detail.csv"
    pd.DataFrame([{"projection_version": V2_PROJECTION_VERSION}]).to_csv(
        manifest_path,
        index=False,
    )
    pd.DataFrame([{"stock_id": "1111"}]).to_csv(detail_path, index=False)
    replay_paths = [tmp_path / name for name in ("revenue.csv", "monthly.csv", "price.csv")]
    for path in replay_paths:
        path.write_text("value\npresent\n", encoding="utf-8")
    price_dir = tmp_path / "prices"
    price_dir.mkdir()
    monkeypatch.setattr(
        validator,
        "_validate_versioned_v2_closure",
        lambda **_kwargs: pytest.fail("explicit v2 validation re-entered default closure"),
    )
    monkeypatch.setattr(validator, "validate_frames", lambda *_args, **_kwargs: [])

    assert validator.validate(
        manifest_path=manifest_path,
        projected_detail_path=detail_path,
        revenue_path=replay_paths[0],
        price_dir=price_dir,
        monthly_resolution_path=replay_paths[1],
        price_resolution_path=replay_paths[2],
    ) == []


def test_default_canonical_validator_requires_v2_closure_and_supersede_evidence(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest_path = tmp_path / "canonical_manifest_latest.csv"
    detail_path = tmp_path / "canonical_detail_latest.csv"
    pd.DataFrame([{"projection_version": V2_PROJECTION_VERSION}]).to_csv(
        manifest_path,
        index=False,
    )
    pd.DataFrame([{"stock_id": "1111"}]).to_csv(detail_path, index=False)
    monkeypatch.setattr(validator, "MANIFEST_CSV", manifest_path)
    monkeypatch.setattr(validator, "PROJECTED_DETAIL_CSV", detail_path)
    monkeypatch.setattr(
        validator,
        "validate_frames",
        lambda *_args, **_kwargs: pytest.fail(
            "canonical v2 fell through to ordinary frame validation"
        ),
    )
    calls: list[str] = []
    monkeypatch.setattr(
        validator,
        "_validate_versioned_v2_closure",
        lambda **_kwargs: calls.append("immutable_v1_v2_diff_closure")
        or ["closure evidence"],
    )
    monkeypatch.setattr(
        validator,
        "_validate_canonical_v2_supersede",
        lambda **_kwargs: calls.append("canonical_supersede_evidence")
        or ["selection evidence"],
    )

    errors = validator.validate(
        manifest_path=manifest_path,
        projected_detail_path=detail_path,
        revenue_path=tmp_path / "missing_revenue.csv",
        price_dir=tmp_path / "missing_prices",
        monthly_resolution_path=tmp_path / "missing_monthly.csv",
        price_resolution_path=tmp_path / "missing_price_resolution.csv",
    )

    assert errors == ["closure evidence", "selection evidence"]
    assert calls == [
        "immutable_v1_v2_diff_closure",
        "canonical_supersede_evidence",
    ]
