from __future__ import annotations

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
    SOURCE_FIRST_ARTIFACT_ID,
    build_source_snapshot_projection_manifest,
    canonical_projected_source_detail_semantic_sha256,
    cutoff_price_input_lineage,
    cutoff_price_input_stock_ids,
    load_cutoff_monthly_revenue_subset,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    validate_projection_binding,
    write_source_snapshot_projection,
)
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
        source_inputs["full_detail"],
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
        source_inputs["full_detail"],
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
        source_inputs["full_detail"],
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
        source_inputs["full_detail"],
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
        source_inputs["full_detail"],
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
        source_inputs["full_detail"],
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


def test_post_cutoff_raw_changes_do_not_change_cutoff_input_hashes(
    source_inputs: dict[str, object],
) -> None:
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


def test_independent_validator_does_not_import_business_producers() -> None:
    source = Path(validator.__file__).read_text(encoding="utf-8")
    assert "import revenue_unreacted_range_source_snapshot_projection" not in source
    assert "from revenue_unreacted_range_source_snapshot_projection" not in source
    assert "import revenue_unreacted_range_source_first_condition_audit" not in source
    assert "from revenue_unreacted_range_source_first_condition_audit" not in source


def test_projection_stage_refreshes_full_source_before_writing_projection(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    full_summary = pd.DataFrame([{"view": "full"}])
    full_detail = pd.DataFrame([{"view": "full"}])
    projected_summary = pd.DataFrame([{"view": "projected"}])
    projected_detail = pd.DataFrame([{"view": "projected"}])
    manifest = pd.DataFrame([{"view": "manifest"}])
    calls: list[tuple[str, object, object]] = []

    def fake_build(*, observation_cutoff_date: str | None = None):
        if observation_cutoff_date is None:
            return full_summary, full_detail
        assert observation_cutoff_date == CUTOFF_DATE
        return projected_summary, projected_detail

    monkeypatch.setattr(orchestrator, "build_source_first_condition_audit", fake_build)
    monkeypatch.setattr(
        orchestrator,
        "build_source_snapshot_projection_manifest",
        lambda full, projected: (
            manifest
            if full is full_detail and projected is projected_detail
            else pytest.fail("projection stage used the wrong source frames")
        ),
    )
    monkeypatch.setattr(
        orchestrator,
        "write_source_first_condition_audit",
        lambda summary, detail: calls.append(("full", summary, detail)),
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
        ("full", full_summary, full_detail),
        ("projection", manifest, projected_detail),
    ]
