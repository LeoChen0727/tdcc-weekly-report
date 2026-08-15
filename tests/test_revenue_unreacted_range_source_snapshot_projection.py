from __future__ import annotations

import hashlib
from pathlib import Path
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
    ARTIFACT_ID,
    ARTIFACT_VERSION,
    CUTOFF_DATE,
    LATEST_DETAIL_CSV,
    LATEST_MANIFEST_CSV,
    MANIFEST_COLUMNS,
    MONTHLY_RESOLUTION_COLUMNS,
    PROJECTION_POLICY_ID,
    REBASELINE_ARTIFACT_VERSION,
    V1_PREDECESSOR_DETAIL_GIT_BLOB_RAW_SHA256,
    V1_PREDECESSOR_MANIFEST_GIT_BLOB_RAW_SHA256,
    SOURCE_FIRST_ARTIFACT_ID,
    build_source_snapshot_projection_manifest,
    canonical_projected_source_detail_semantic_sha256,
    cutoff_price_input_lineage,
    cutoff_price_input_stock_ids,
    load_cutoff_monthly_revenue_subset,
    load_committed_v1_projection_predecessor,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    projection_binding_errors,
    validate_projection_binding,
    write_source_snapshot_projection,
)
import revenue_unreacted_range_source_snapshot_projection as projection_producer  # noqa: E402
from revenue_unreacted_range_source_first_condition_audit import (  # noqa: E402
    build_source_first_condition_audit,
)
import validate_revenue_unreacted_range_source_snapshot_projection as validator  # noqa: E402
import build_revenue_unreacted_range_research as orchestrator  # noqa: E402


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


def test_v2_rebaseline_manifest_uses_separate_versioned_history_without_rewriting_v1(
    source_inputs: dict[str, object],
    tmp_path: Path,
) -> None:
    v1_manifest = _build(source_inputs)
    v2_manifest = build_source_snapshot_projection_manifest(
        source_inputs["full_detail"],
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
        generated_at="2026-08-14 00:00:00 Asia/Taipei",
        artifact_version=REBASELINE_ARTIFACT_VERSION,
    )
    assert v2_manifest.iloc[0]["artifact_version"] == REBASELINE_ARTIFACT_VERSION
    assert v2_manifest.iloc[0]["projection_version"] == REBASELINE_ARTIFACT_VERSION
    assert bool(v2_manifest.iloc[0]["research_only"])
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        assert not bool(v2_manifest.iloc[0][column])

    errors = validator.validate_frames(
        v2_manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
        expected_artifact_version=REBASELINE_ARTIFACT_VERSION,
    )
    assert errors == []
    forged_v1 = v2_manifest.copy()
    forged_v1.loc[0, "artifact_version"] = ARTIFACT_VERSION
    forged_v1.loc[0, "projection_version"] = ARTIFACT_VERSION
    assert "projection manifest artifact_version mismatch: " + (
        f"{ARTIFACT_VERSION}/{REBASELINE_ARTIFACT_VERSION}"
    ) in validator.validate_frames(
        forged_v1,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
        expected_artifact_version=REBASELINE_ARTIFACT_VERSION,
    )

    v1_manifest_path = tmp_path / "v1_manifest.csv"
    v1_detail_path = tmp_path / "v1_detail.csv"
    v1_history = tmp_path / "v1_history.csv"
    v1_docs = tmp_path / "v1_docs.csv"
    write_source_snapshot_projection(
        v1_manifest,
        source_inputs["projected_detail"],
        latest_manifest_path=v1_manifest_path,
        latest_detail_path=v1_detail_path,
        history_manifest_path=v1_history,
        docs_manifest_path=v1_docs,
        expected_artifact_version=ARTIFACT_VERSION,
    )
    v1_payloads_before = {
        path: path.read_bytes()
        for path in (v1_manifest_path, v1_detail_path, v1_history, v1_docs)
    }
    with pytest.raises(RuntimeError, match="dedicated transactional"):
        write_source_snapshot_projection(
            v2_manifest,
            source_inputs["projected_detail"],
            latest_manifest_path=tmp_path / "v2_manifest.csv",
            latest_detail_path=tmp_path / "v2_detail.csv",
            history_manifest_path=tmp_path / "v2_history.csv",
            docs_manifest_path=tmp_path / "v2_docs.csv",
            expected_artifact_version=REBASELINE_ARTIFACT_VERSION,
        )
    assert all(path.read_bytes() == payload for path, payload in v1_payloads_before.items())


def test_v1_archive_preflight_uses_exact_committed_git_blob_bytes() -> None:
    manifest, detail, manifest_payload, detail_payload = (
        load_committed_v1_projection_predecessor()
    )
    assert len(manifest) == 1
    assert not detail.empty
    assert hashlib.sha256(manifest_payload).hexdigest() == (
        V1_PREDECESSOR_MANIFEST_GIT_BLOB_RAW_SHA256
    )
    assert hashlib.sha256(detail_payload).hexdigest() == (
        V1_PREDECESSOR_DETAIL_GIT_BLOB_RAW_SHA256
    )


def test_v1_archive_preflight_fails_closed_when_pinned_blob_is_unavailable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        projection_producer,
        "_git_blob_bytes",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            RuntimeError("injected missing predecessor blob")
        ),
    )
    with pytest.raises(RuntimeError, match="missing predecessor blob"):
        load_committed_v1_projection_predecessor()


def test_projection_rejects_unregistered_rebaseline_version(
    source_inputs: dict[str, object],
) -> None:
    with pytest.raises(
        RuntimeError,
        match="unsupported source snapshot projection artifact version",
    ):
        build_source_snapshot_projection_manifest(
            source_inputs["full_detail"],
            source_inputs["projected_detail"],
            revenue_path=source_inputs["revenue_path"],
            price_dir=source_inputs["price_dir"],
            monthly_resolution_path=source_inputs["monthly_registry_path"],
            price_resolution_path=source_inputs["price_registry_path"],
            artifact_version="source_snapshot_projection_unregistered",
        )

    manifest = _build(source_inputs)
    manifest.loc[0, "artifact_version"] = "source_snapshot_projection_unregistered"
    manifest.loc[0, "projection_version"] = "source_snapshot_projection_unregistered"
    assert projection_binding_errors(
        manifest,
        source_inputs["projected_detail"],
    ) == [
        "projection manifest artifact_version is not registered: "
        "source_snapshot_projection_unregistered"
    ]
    independent_errors = validator.validate_frames(
        manifest,
        source_inputs["projected_detail"],
        revenue_path=source_inputs["revenue_path"],
        price_dir=source_inputs["price_dir"],
        monthly_resolution_path=source_inputs["monthly_registry_path"],
        price_resolution_path=source_inputs["price_registry_path"],
    )
    assert (
        "projection manifest artifact_version is not registered: "
        "source_snapshot_projection_unregistered"
    ) in independent_errors


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
    monkeypatch.setattr(
        orchestrator,
        "build_source_snapshot_projection_manifest",
        lambda *_args, **_kwargs: pytest.fail(
            "projection replay stage built a replacement immutable capture"
        ),
    )
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


def test_projection_rebaseline_stage_has_exact_thirteen_path_contract() -> None:
    allowed = list(
        orchestrator.SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS
    )
    assert len(allowed) == 13
    assert orchestrator.validate_source_snapshot_projection_rebaseline_stage_changed_paths(
        allowed,
        existing_paths=allowed,
    ) == []
    extra_errors = orchestrator.validate_source_snapshot_projection_rebaseline_stage_changed_paths(
        [*allowed, "output/latest/model_operation_readiness_latest.csv"],
        existing_paths=allowed,
    )
    assert extra_errors == [
        "source snapshot projection rebaseline stage artifact allowlist violation: "
        "output/latest/model_operation_readiness_latest.csv"
    ]
    for missing_path in allowed:
        existing = [path for path in allowed if path != missing_path]
        errors = orchestrator.validate_source_snapshot_projection_rebaseline_stage_changed_paths(
            existing,
            existing_paths=existing,
        )
        assert errors == [
            "source snapshot projection rebaseline stage expected artifact unchanged: "
            + missing_path,
            "source snapshot projection rebaseline stage required artifact missing: "
            + missing_path,
        ]


def _seed_transaction_bundle(temp_root: Path, target_root: Path) -> dict[str, bytes]:
    prior: dict[str, bytes] = {}
    for index, relative_path in enumerate(
        orchestrator.SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS
    ):
        prior_payload = f"prior-{index}".encode()
        replacement_payload = f"replacement-{index}".encode()
        prior[relative_path] = prior_payload
        target = target_root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(prior_payload)
        staged = temp_root / relative_path
        staged.parent.mkdir(parents=True, exist_ok=True)
        staged.write_bytes(replacement_payload)
    return prior


@pytest.mark.parametrize("failure_index", range(13))
def test_projection_rebaseline_transaction_rolls_back_each_replace_failure(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    failure_index: int,
) -> None:
    target_root = tmp_path / f"target-{failure_index}"
    temp_root = tmp_path / f"temp-{failure_index}"
    prior = _seed_transaction_bundle(temp_root, target_root)
    call_count = 0

    def injected_replace(source: Path, destination: Path) -> None:
        nonlocal call_count
        current = call_count
        call_count += 1
        if current == failure_index:
            raise OSError(f"injected replace failure {failure_index}")
        source.replace(destination)

    monkeypatch.setattr(orchestrator, "_replace_rebaseline_path", injected_replace)
    with pytest.raises(OSError, match="injected replace failure"):
        orchestrator._publish_rebaseline_temp_bundle(temp_root, root=target_root)
    for relative_path, payload in prior.items():
        assert (target_root / relative_path).read_bytes() == payload


def test_projection_rebaseline_transaction_publishes_exact_bundle(
    tmp_path: Path,
) -> None:
    target_root = tmp_path / "target"
    temp_root = tmp_path / "temp"
    _seed_transaction_bundle(temp_root, target_root)
    orchestrator._publish_rebaseline_temp_bundle(temp_root, root=target_root)
    for index, relative_path in enumerate(
        orchestrator.SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS
    ):
        assert (target_root / relative_path).read_bytes() == f"replacement-{index}".encode()


@pytest.mark.parametrize("mutation", ["missing", "extra", "renamed"])
def test_projection_rebaseline_transaction_rejects_non_exact_bundle(
    tmp_path: Path,
    mutation: str,
) -> None:
    target_root = tmp_path / f"target-{mutation}"
    temp_root = tmp_path / f"temp-{mutation}"
    prior = _seed_transaction_bundle(temp_root, target_root)
    first = orchestrator.SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS[0]
    if mutation == "missing":
        (temp_root / first).unlink()
    elif mutation == "extra":
        extra = temp_root / "output/latest/research_backtest/unregistered.csv"
        extra.parent.mkdir(parents=True, exist_ok=True)
        extra.write_text("extra", encoding="utf-8")
    else:
        source = temp_root / first
        source.rename(source.with_name(source.name + ".renamed"))
    with pytest.raises(RuntimeError, match="exact-set validation failed"):
        orchestrator._publish_rebaseline_temp_bundle(temp_root, root=target_root)
    for relative_path, payload in prior.items():
        assert (target_root / relative_path).read_bytes() == payload


@pytest.mark.parametrize(
    "validator_name",
    [
        "validate_source_first_condition_audit_independently",
        "validate_source_snapshot_projection_independently",
        "validate_source_snapshot_projection_diff_independently",
    ],
)
def test_projection_rebaseline_independent_validator_failure_stops_before_publish(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    validator_name: str,
) -> None:
    for name in (
        "validate_source_first_condition_audit_independently",
        "validate_source_snapshot_projection_independently",
        "validate_source_snapshot_projection_diff_independently",
    ):
        monkeypatch.setattr(
            orchestrator,
            name,
            (lambda *args, **kwargs: ["injected validator failure"])
            if name == validator_name
            else (lambda *args, **kwargs: []),
        )
    with pytest.raises(RuntimeError, match="injected validator failure"):
        orchestrator._validate_rebaseline_temp_bundle(
            temp_root=tmp_path,
            v1_manifest_path=tmp_path / "v1-manifest.csv",
            v1_detail_path=tmp_path / "v1-detail.csv",
            v2_manifest_path=tmp_path / "v2-manifest.csv",
            v2_detail_path=tmp_path / "v2-detail.csv",
        )


def test_projection_rebaseline_guard_rolls_back_allowed_paths_on_failure(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    allowed = list(
        orchestrator.SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS
    )
    prior_payloads: dict[str, bytes] = {}
    for index, relative_path in enumerate(allowed):
        payload = f"prior-{index}".encode()
        prior_payloads[relative_path] = payload
        path = tmp_path / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)

    monkeypatch.setattr(orchestrator, "_dirty_snapshot", lambda _root: {})
    monkeypatch.setattr(
        orchestrator,
        "changed_during_run",
        lambda _root, _before: allowed,
    )
    with pytest.raises(RuntimeError, match="injected publish failure"):
        with orchestrator.source_snapshot_projection_rebaseline_stage_artifact_guard(
            root=tmp_path,
        ):
            (tmp_path / allowed[0]).write_bytes(b"replacement")
            (tmp_path / allowed[1]).unlink()
            raise RuntimeError("injected publish failure")

    for relative_path, prior_payload in prior_payloads.items():
        assert (tmp_path / relative_path).read_bytes() == prior_payload


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
    monkeypatch.setattr(
        orchestrator,
        "build_source_snapshot_projection_manifest",
        lambda *_args, **_kwargs: pytest.fail(
            "projection chain built a replacement immutable capture"
        ),
    )
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

    def fake_low_mid(
        source,
        rearmed,
        daily,
        *,
        source_projection_manifest,
        source_projection_artifact_version,
    ):
        assert source is frames["projected_detail"]
        assert rearmed is frames["rearmed_detail"]
        assert daily is projected_daily
        assert source_projection_manifest is frames["manifest"]
        assert source_projection_artifact_version == ARTIFACT_VERSION
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
