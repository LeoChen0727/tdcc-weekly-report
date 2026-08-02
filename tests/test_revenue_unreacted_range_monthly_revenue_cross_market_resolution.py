from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_lag_strength_matrix as lag_strength  # noqa: E402
from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (  # noqa: E402
    BUSINESS_PAYLOAD_COLUMNS,
    CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS,
    CROSS_MARKET_RESOLUTION_REGISTRY_SORT_KEYS,
    RESOLUTION_CSV,
    canonical_monthly_revenue_history_table_sha256,
    canonical_monthly_revenue_raw_row_sha256,
    cross_market_resolution_registry_canonical_sha256,
    monthly_revenue_history_blob_sha256,
    resolve_monthly_revenue_cross_market_mirrors,
)
from revenue_unreacted_range_source_first_condition_audit import (  # noqa: E402
    load_revenue_history,
)
from revenue_unreacted_range_source_snapshot_projection import (  # noqa: E402
    load_cutoff_monthly_revenue_subset,
)
from revenue_unreacted_range_research_frame import (  # noqa: E402
    attach_revenue_unreacted_range_canonical_monthly_history,
)


def _row(
    *,
    market: str,
    source_market_name: str,
    source_table_date: str,
    stock_id: str = "5236",
    revenue_period: str = "202606",
    monthly_revenue: str = "192161",
) -> dict[str, str]:
    source_suffix = "L" if source_market_name == "TWSE" else "O"
    row = {column: "" for column in BUSINESS_PAYLOAD_COLUMNS}
    row.update(
        {
            "market": market,
            "source_market_name": source_market_name,
            "source_table_date": source_table_date,
            "source_kind": "official_mops_current_monthly_revenue_openapi",
            "source_url": (
                f"https://mopsfin.twse.com.tw/opendata/t187ap05_{source_suffix}.csv"
            ),
            "source_file": (
                "data/monthly_revenue_history/raw/"
                f"monthly_revenue_raw_{market}_{source_table_date}_{revenue_period}.csv"
            ),
            "stock_id": stock_id,
            "stock_name": "凌陽創新",
            "industry": "半導體業",
            "revenue_period": revenue_period,
            "revenue_period_roc": "11506",
            "monthly_revenue": monthly_revenue,
            "previous_month_revenue": "201026",
            "last_year_month_revenue": "170388",
            "month_over_month_pct": "-4.409877",
            "latest_revenue_yoy_pct": "12.778482",
            "cumulative_revenue": "1167421",
            "last_year_cumulative_revenue": "991235",
            "cumulative_revenue_yoy_pct": "17.774393",
            "note": "-",
            "revenue_positive_flag": "True",
            "revenue_strong_flag": "True",
            "revenue_numerical_anomaly_flag": "False",
            "revenue_numerical_anomaly_reason": "",
            "point_in_time_status": "ready_official_source_table_date",
            "research_join_allowed": "True",
            "allowed_for_formal_historical_model_use": "False",
            "formal_use_blocker": "blocked_until_sufficient_history_coverage_and_model_promotion",
            "coverage_note": (
                "full_market_current_monthly_revenue_saved_from_official_openapi; "
                "historical coverage starts at the first saved source table date unless "
                "separately backfilled"
            ),
        }
    )
    return row


def _registered_pair() -> pd.DataFrame:
    return pd.DataFrame(
        [
            _row(market="otc", source_market_name="TPEX", source_table_date="20260715"),
            _row(market="listed", source_market_name="TWSE", source_table_date="20260717"),
        ]
    )


def _registry() -> pd.DataFrame:
    return pd.read_csv(RESOLUTION_CSV, dtype=str, keep_default_na=False)


def test_registered_equal_payload_cross_market_mirror_keeps_earliest_official_row() -> None:
    resolved = resolve_monthly_revenue_cross_market_mirrors(_registered_pair())
    assert len(resolved) == 1
    assert resolved.iloc[0]["market"] == "otc"
    assert resolved.iloc[0]["source_market_name"] == "TPEX"
    assert resolved.iloc[0]["source_table_date"] == "20260715"
    assert (
        resolved.iloc[0]["cross_market_resolution_id"]
        == "revenue_unreacted_range_5236_202606_cross_market_mirror"
    )
    assert resolved.iloc[0]["source_row_canonical_sha256"] == (
        "49d69d892010c55067260fc105a0ef4ac3cb522135c46ca63d5267cf31f2973d"
    )
    assert resolved.iloc[0]["canonical_source_table_date"] == "20260715"


def test_observation_cutoff_excludes_future_cross_market_mirror_without_rewriting_history() -> None:
    before_either_side = resolve_monthly_revenue_cross_market_mirrors(
        _registered_pair(),
        observation_cutoff_date="20260713",
    )
    after_earlier_side_only = resolve_monthly_revenue_cross_market_mirrors(
        _registered_pair(),
        observation_cutoff_date="20260716",
    )

    assert before_either_side.empty
    assert len(after_earlier_side_only) == 1
    assert after_earlier_side_only.iloc[0]["source_table_date"] == "20260715"
    assert after_earlier_side_only.iloc[0]["cross_market_resolution_id"] == ""
    assert after_earlier_side_only.iloc[0]["canonical_source_table_date"] == "20260715"


def test_observation_cutoff_requires_exact_yyyymmdd() -> None:
    with pytest.raises(RuntimeError, match="exactly YYYYMMDD"):
        resolve_monthly_revenue_cross_market_mirrors(
            _registered_pair(),
            observation_cutoff_date="2026-07-13",
        )


@pytest.mark.parametrize(
    ("column", "value"),
    (
        ("revenue_period", "2026069"),
        ("revenue_period", "202606x"),
        ("source_table_date", "202607159"),
        ("source_table_date", "20260715x"),
    ),
)
def test_date_and_period_identity_aliases_fail_closed(
    column: str,
    value: str,
) -> None:
    frame = _registered_pair()
    frame.loc[0, column] = value
    with pytest.raises(RuntimeError, match="must be exact digits"):
        resolve_monthly_revenue_cross_market_mirrors(frame)


def test_registered_mirror_resolution_is_independent_of_input_row_order() -> None:
    forward = resolve_monthly_revenue_cross_market_mirrors(_registered_pair())
    reverse = resolve_monthly_revenue_cross_market_mirrors(
        _registered_pair().iloc[::-1].reset_index(drop=True)
    )

    pd.testing.assert_frame_equal(forward, reverse)


def test_registered_cross_market_payload_conflict_fails_closed() -> None:
    frame = _registered_pair()
    frame.loc[1, "monthly_revenue"] = "192162"
    with pytest.raises(RuntimeError, match="payload conflict"):
        resolve_monthly_revenue_cross_market_mirrors(frame)


@pytest.mark.parametrize("missing_index", [0, 1])
def test_registered_mirror_missing_either_exact_raw_side_fails_closed(
    missing_index: int,
) -> None:
    frame = _registered_pair().drop(index=missing_index).reset_index(drop=True)
    with pytest.raises(RuntimeError, match="complete exact two-row raw pair"):
        resolve_monthly_revenue_cross_market_mirrors(frame)


@pytest.mark.parametrize("column", ["source_kind", "source_url", "source_file"])
def test_registered_cross_market_lineage_mutation_fails_closed(column: str) -> None:
    frame = _registered_pair()
    frame.loc[1, column] = f"mutated-{frame.loc[1, column]}"
    with pytest.raises(RuntimeError, match="source identities mismatch"):
        resolve_monthly_revenue_cross_market_mirrors(frame)


def test_registry_canonical_sha_binds_semantics_and_row_hashes_but_excludes_notes() -> None:
    registry = _registry()
    baseline = cross_market_resolution_registry_canonical_sha256(registry)
    semantic_mutation = registry.copy()
    semantic_mutation.loc[0, "evidence_url"] = "https://example.com/changed-evidence"
    assert cross_market_resolution_registry_canonical_sha256(semantic_mutation) != baseline
    hash_mutation = registry.copy()
    hash_mutation.loc[0, "later_raw_row_canonical_sha256"] = "0" * 64
    assert cross_market_resolution_registry_canonical_sha256(hash_mutation) != baseline
    notes_only = registry.copy()
    notes_only.loc[0, "notes"] = "excluded free-form note mutation"
    assert cross_market_resolution_registry_canonical_sha256(notes_only) == baseline
    assert "notes" not in CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS
    assert CROSS_MARKET_RESOLUTION_REGISTRY_SORT_KEYS == (
        "model_id",
        "stock_id",
        "revenue_period",
        "resolution_id",
    )


def test_raw_row_hash_is_stable_across_equivalent_numeric_dtypes() -> None:
    base = _registered_pair().iloc[0].copy()
    expected = canonical_monthly_revenue_raw_row_sha256(base)
    for monthly_revenue, stock_id, revenue_period, source_date in (
        (192161, 5236, 202606, 20260715),
        (192161.0, 5236.0, 202606.0, 20260715.0),
        ("192161", "5236", "202606", "20260715"),
    ):
        # pandas 3 rejects assigning numeric scalars into a string-inferred
        # Series.  Use an object fixture so this test exercises the canonical
        # hash normalizer, rather than pandas' assignment coercion policy.
        variant = base.astype(object).copy()
        variant["monthly_revenue"] = monthly_revenue
        variant["stock_id"] = stock_id
        variant["revenue_period"] = revenue_period
        variant["source_table_date"] = source_date
        assert canonical_monthly_revenue_raw_row_sha256(variant) == expected
    changed = base.astype(object).copy()
    changed["monthly_revenue"] = 192162
    assert canonical_monthly_revenue_raw_row_sha256(changed) != expected


def test_registered_raw_hash_binding_mutation_fails_closed(tmp_path: Path) -> None:
    registry = _registry()
    registry.loc[0, "earlier_raw_row_canonical_sha256"] = "0" * 64
    registry.loc[0, "canonical_row_canonical_sha256"] = "0" * 64
    path = tmp_path / "resolution.csv"
    registry.to_csv(path, index=False, lineterminator="\n")
    with pytest.raises(RuntimeError, match="earlier raw-row canonical hash mismatch"):
        resolve_monthly_revenue_cross_market_mirrors(
            _registered_pair(), resolution_path=path
        )


def test_equal_payload_raw_content_mutation_fails_hash_binding() -> None:
    frame = _registered_pair()
    frame.loc[:, "monthly_revenue"] = "192162"
    with pytest.raises(RuntimeError, match="raw-row canonical hash mismatch"):
        resolve_monthly_revenue_cross_market_mirrors(frame)


def test_second_registration_is_resolved_and_registry_hash_is_key_order_stable(
    tmp_path: Path,
) -> None:
    second_pair = pd.DataFrame(
        [
            _row(
                market="otc",
                source_market_name="TPEX",
                source_table_date="20260710",
                stock_id="9999",
                revenue_period="202605",
                monthly_revenue="100",
            ),
            _row(
                market="listed",
                source_market_name="TWSE",
                source_table_date="20260712",
                stock_id="9999",
                revenue_period="202605",
                monthly_revenue="100",
            ),
        ]
    )
    second_pair.loc[:, "revenue_period_roc"] = "11505"
    earlier_hash = canonical_monthly_revenue_raw_row_sha256(second_pair.iloc[0])
    later_hash = canonical_monthly_revenue_raw_row_sha256(second_pair.iloc[1])
    registry = _registry()
    second = registry.iloc[0].copy()
    second.update(
        {
            "resolution_id": "revenue_unreacted_range_9999_202605_cross_market_mirror",
            "stock_id": "9999",
            "revenue_period": "202605",
            "earlier_source_table_date": "20260710",
            "earlier_source_file": (
                "data/monthly_revenue_history/raw/"
                "monthly_revenue_raw_otc_20260710_202605.csv"
            ),
            "earlier_raw_row_canonical_sha256": earlier_hash,
            "later_source_table_date": "20260712",
            "later_source_file": (
                "data/monthly_revenue_history/raw/"
                "monthly_revenue_raw_listed_20260712_202605.csv"
            ),
            "later_raw_row_canonical_sha256": later_hash,
            "official_market_transition_date": "20260711",
            "canonical_source_table_date": "20260710",
            "canonical_row_canonical_sha256": earlier_hash,
            "evidence_url": "https://example.com/9999-market-transition",
            "notes": "second registered fixture",
        }
    )
    registry = pd.concat([registry, second.to_frame().T], ignore_index=True)
    path = tmp_path / "resolution.csv"
    registry.to_csv(path, index=False, lineterminator="\n")

    frame = pd.concat([_registered_pair(), second_pair], ignore_index=True)
    resolved = resolve_monthly_revenue_cross_market_mirrors(frame, path)
    assert len(resolved) == 2
    second_canonical = resolved.loc[resolved["stock_id"].eq("9999")].iloc[0]
    assert second_canonical["source_table_date"] == "20260710"
    assert second_canonical["source_row_canonical_sha256"] == earlier_hash
    assert second_canonical["cross_market_resolution_id"] == second["resolution_id"]
    forward_sha = cross_market_resolution_registry_canonical_sha256(registry)
    reverse_sha = cross_market_resolution_registry_canonical_sha256(
        registry.iloc[::-1].reset_index(drop=True)
    )
    assert forward_sha == reverse_sha


def test_non_mirror_rows_receive_self_lineage_and_run_hashes_are_stable(
    tmp_path: Path,
) -> None:
    ordinary = _row(
        market="otc",
        source_market_name="TPEX",
        source_table_date="20260617",
        stock_id="9999",
        revenue_period="202605",
        monthly_revenue="100",
    )
    ordinary["revenue_period_roc"] = "11505"
    raw = pd.concat([_registered_pair(), pd.DataFrame([ordinary])], ignore_index=True)
    resolved = resolve_monthly_revenue_cross_market_mirrors(raw)
    regular = resolved.loc[resolved["stock_id"].eq("9999")].iloc[0]
    assert regular["cross_market_resolution_id"] == ""
    assert regular["source_row_canonical_sha256"] == canonical_monthly_revenue_raw_row_sha256(
        pd.Series(ordinary)
    )
    assert regular["canonical_source_table_date"] == "20260617"
    assert canonical_monthly_revenue_history_table_sha256(resolved) == (
        canonical_monthly_revenue_history_table_sha256(
            resolved.iloc[::-1].reset_index(drop=True)
        )
    )
    blob = tmp_path / "history.csv"
    raw.to_csv(blob, index=False, lineterminator="\n")
    first_blob_sha = monthly_revenue_history_blob_sha256(blob)
    blob.write_bytes(blob.read_bytes() + b"\n")
    assert monthly_revenue_history_blob_sha256(blob) != first_blob_sha


def test_unregistered_cross_market_duplicate_fails_closed() -> None:
    frame = _registered_pair()
    frame["stock_id"] = "9999"
    with pytest.raises(RuntimeError, match="unregistered"):
        resolve_monthly_revenue_cross_market_mirrors(frame)


def test_same_market_duplicate_fails_closed() -> None:
    frame = _registered_pair()
    frame.loc[1, "market"] = "otc"
    frame.loc[1, "source_market_name"] = "TPEX"
    with pytest.raises(RuntimeError, match="same-market"):
        resolve_monthly_revenue_cross_market_mirrors(frame)


def test_source_first_and_lag_lookup_consume_the_same_cutoff_canonical_view(
    tmp_path: Path,
) -> None:
    previous = _row(
        market="otc",
        source_market_name="TPEX",
        source_table_date="20260617",
        revenue_period="202605",
        monthly_revenue="201026",
    )
    previous.update(
        {
            "revenue_period_roc": "11505",
            "latest_revenue_yoy_pct": "18.728996",
            "cumulative_revenue_yoy_pct": "18.811545",
        }
    )
    path = tmp_path / "monthly_revenue_history.csv"
    pd.concat([pd.DataFrame([previous]), _registered_pair()], ignore_index=True).to_csv(
        path, index=False
    )

    source_first = load_revenue_history(path)
    target = source_first.loc[
        source_first["stock_id"].eq("5236")
        & source_first["revenue_period"].eq("202606")
    ]
    assert len(target) == 1
    assert target.iloc[0]["source_table_date"] == "20260715"
    assert target.iloc[0]["previous_revenue_period"] == "202605"

    canonical_history = load_cutoff_monthly_revenue_subset(
        path,
        RESOLUTION_CSV,
        cutoff_date="20260716",
    )
    assert len(canonical_history) == 2
    lookup = lag_strength._monthly_history_lookup(canonical_history)
    assert lookup["5236"]["202606"]["source_table_date"] == "20260715"
    assert set(lookup["5236"]) == {"202605", "202606"}


def test_model_owned_research_frame_replaces_shared_duplicate_shift_view(
    tmp_path: Path,
) -> None:
    previous = _row(
        market="otc",
        source_market_name="TPEX",
        source_table_date="20260617",
        revenue_period="202605",
        monthly_revenue="201026",
    )
    previous.update(
        {
            "revenue_period_roc": "11505",
            "latest_revenue_yoy_pct": "18.728996",
            "cumulative_revenue_yoy_pct": "18.811545",
        }
    )
    history_path = tmp_path / "monthly_revenue_history.csv"
    pd.concat([pd.DataFrame([previous]), _registered_pair()], ignore_index=True).to_csv(
        history_path, index=False
    )
    shared_frame = pd.DataFrame(
        [
            {
                "stock_id": "5236",
                "date": date,
                "close": 100.0,
                "full_monthly_revenue_period": "202606",
                "full_monthly_revenue_source_table_date": "20260717",
                "full_monthly_revenue_prev1_period": "202606",
            }
            for date in ("20260714", "20260715", "20260717")
        ]
    )

    result = attach_revenue_unreacted_range_canonical_monthly_history(
        shared_frame, history_path
    )
    before = result.loc[result["date"].eq("20260714")].iloc[0]
    first_available = result.loc[result["date"].eq("20260715")].iloc[0]
    after_market_transfer = result.loc[result["date"].eq("20260717")].iloc[0]
    assert before["full_monthly_revenue_period"] == "202605"
    assert first_available["full_monthly_revenue_period"] == "202606"
    assert first_available["full_monthly_revenue_source_table_date"] == "20260715"
    assert after_market_transfer["full_monthly_revenue_source_table_date"] == "20260715"
    assert after_market_transfer["full_monthly_revenue_prev1_period"] == "202605"
    assert after_market_transfer["full_monthly_revenue_prev2_period"] == ""
    assert (
        after_market_transfer["full_monthly_revenue_source_artifact"]
        == "data/monthly_revenue_history/monthly_revenue_history.csv"
    )


def test_model_owned_research_frame_combines_raw_and_resolution_formal_flags(
    tmp_path: Path,
) -> None:
    registered = _registered_pair()
    registered.loc[:, "allowed_for_formal_historical_model_use"] = "True"
    ordinary = _row(
        market="otc",
        source_market_name="TPEX",
        source_table_date="20260617",
        stock_id="9999",
        revenue_period="202605",
        monthly_revenue="100",
    )
    ordinary.update(
        {
            "revenue_period_roc": "11505",
            "allowed_for_formal_historical_model_use": "True",
        }
    )
    history_path = tmp_path / "monthly_revenue_history.csv"
    pd.concat([registered, pd.DataFrame([ordinary])], ignore_index=True).to_csv(
        history_path,
        index=False,
        lineterminator="\n",
    )

    registry = _registry()
    earlier_hash = canonical_monthly_revenue_raw_row_sha256(registered.iloc[0])
    later_hash = canonical_monthly_revenue_raw_row_sha256(registered.iloc[1])
    registry.loc[0, "earlier_raw_row_canonical_sha256"] = earlier_hash
    registry.loc[0, "later_raw_row_canonical_sha256"] = later_hash
    registry.loc[0, "canonical_row_canonical_sha256"] = earlier_hash
    resolution_path = tmp_path / "resolution.csv"
    registry.to_csv(resolution_path, index=False, lineterminator="\n")

    result = attach_revenue_unreacted_range_canonical_monthly_history(
        pd.DataFrame(
            [
                {"stock_id": "5236", "date": "20260718", "close": 100.0},
                {"stock_id": "9999", "date": "20260718", "close": 100.0},
            ]
        ),
        history_path,
        resolution_path,
    ).set_index("stock_id")

    registered_result = result.loc["5236"]
    assert registered_result["full_monthly_revenue_cross_market_resolution_id"] == (
        "revenue_unreacted_range_5236_202606_cross_market_mirror"
    )
    assert registered_result["full_monthly_revenue_source_row_canonical_sha256"] == (
        earlier_hash
    )
    assert (
        registered_result["full_monthly_revenue_canonical_source_table_date"]
        == "20260715"
    )
    assert not bool(
        registered_result["full_monthly_revenue_formal_model_use_allowed"]
    )

    ordinary_result = result.loc["9999"]
    assert ordinary_result["full_monthly_revenue_cross_market_resolution_id"] == ""
    assert ordinary_result["full_monthly_revenue_source_row_canonical_sha256"] == (
        canonical_monthly_revenue_raw_row_sha256(pd.Series(ordinary))
    )
    assert (
        ordinary_result["full_monthly_revenue_canonical_source_table_date"]
        == "20260617"
    )
    assert bool(ordinary_result["full_monthly_revenue_formal_model_use_allowed"])


def test_model_owned_research_frame_preserves_missing_stock_vs_missing_asof_status(
    tmp_path: Path,
) -> None:
    previous = _row(
        market="otc",
        source_market_name="TPEX",
        source_table_date="20260617",
        revenue_period="202605",
        monthly_revenue="201026",
    )
    history_path = tmp_path / "monthly_revenue_history.csv"
    pd.concat([pd.DataFrame([previous]), _registered_pair()], ignore_index=True).to_csv(
        history_path, index=False
    )
    frame = pd.DataFrame(
        [
            {"stock_id": "5236", "date": "20260616", "close": 100.0},
            {"stock_id": "9999", "date": "20260717", "close": 100.0},
        ]
    )

    result = attach_revenue_unreacted_range_canonical_monthly_history(
        frame, history_path
    )
    by_stock = result.set_index("stock_id")
    assert (
        by_stock.loc["5236", "full_monthly_revenue_data_status"]
        == "missing_asof_revenue_on_or_before_signal_date"
    )
    assert (
        by_stock.loc["9999", "full_monthly_revenue_data_status"]
        == "missing_stock_in_full_monthly_revenue_history"
    )
    assert set(result["full_monthly_revenue_source_artifact"]) == {
        "data/monthly_revenue_history/monthly_revenue_history.csv"
    }
