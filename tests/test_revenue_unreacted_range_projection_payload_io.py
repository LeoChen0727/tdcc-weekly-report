from __future__ import annotations

import hashlib
from io import BytesIO
from pathlib import Path
import sys
from types import MappingProxyType

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_source_first_condition_audit as producer  # noqa: E402
from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (  # noqa: E402
    BUSINESS_PAYLOAD_COLUMNS,
    RESOLUTION_COLUMNS,
    canonical_monthly_revenue_raw_row_sha256,
)


REVENUE_KEY = "data/monthly_revenue_history/monthly_revenue_history.csv"
MONTHLY_RESOLUTION_KEY = (
    "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
)
PRICE_RESOLUTION_KEY = "config/revenue_unreacted_range_price_comparability_resolution.csv"
PRICE_PREFIX = "data/stock_price_history/"
CUTOFF = "20260713"


def _revenue_row(stock_id: str, source_date: str, *, later: bool = False) -> dict[str, str]:
    row = {column: "" for column in BUSINESS_PAYLOAD_COLUMNS}
    row.update(
        stock_id=stock_id,
        stock_name=f"Synthetic {stock_id}",
        revenue_period="202605" if stock_id == "1111" else "202606",
        revenue_period_roc="11505" if stock_id == "1111" else "11506",
        monthly_revenue="1000",
        previous_month_revenue="800",
        last_year_month_revenue="700",
        month_over_month_pct="25",
        latest_revenue_yoy_pct="40",
        cumulative_revenue="6000",
        last_year_cumulative_revenue="4500",
        cumulative_revenue_yoy_pct="33",
        revenue_positive_flag="True",
        revenue_strong_flag="True",
        revenue_numerical_anomaly_flag="False",
        point_in_time_status="ready_official_source_table_date",
        research_join_allowed="True",
        allowed_for_formal_historical_model_use="False",
        formal_use_blocker="synthetic_research_only",
        market="listed" if later else "otc",
        source_market_name="TWSE" if later else "TPEX",
        source_table_date=source_date,
        source_kind="synthetic_official_source",
        source_url=f"https://example.test/{stock_id}/{source_date}",
        source_file=f"data/monthly_revenue_history/raw/{stock_id}_{source_date}.csv",
    )
    return row


def _registry_row(earlier: dict[str, str], later: dict[str, str]) -> dict[str, str]:
    row = {column: "" for column in RESOLUTION_COLUMNS}
    earlier_sha = canonical_monthly_revenue_raw_row_sha256(earlier)
    row.update(
        resolution_id=f"synthetic_mirror_{earlier['stock_id']}",
        model_id="revenue_unreacted_range",
        stock_id=earlier["stock_id"],
        revenue_period=earlier["revenue_period"],
        official_market_transition_date=later["source_table_date"],
        canonical_source_table_date=earlier["source_table_date"],
        canonical_row_canonical_sha256=earlier_sha,
        resolution_status="registered_equal_payload_cross_market_mirror",
        canonicalization_policy="earliest_official_source_table_date",
        evidence_url="https://example.test/evidence",
        formal_model_use_allowed="False",
    )
    for side, source in (("earlier", earlier), ("later", later)):
        for column in (
            "market", "source_market_name", "source_table_date", "source_kind",
            "source_url", "source_file",
        ):
            row[f"{side}_{column}"] = source[column]
        row[f"{side}_raw_row_canonical_sha256"] = canonical_monthly_revenue_raw_row_sha256(source)
    return row


def _csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


@pytest.fixture
def source_inputs(tmp_path: Path):
    earlier = _revenue_row("2222", "20260708")
    later = _revenue_row("2222", "20260709", later=True)
    future_earlier = _revenue_row("3333", "20260714")
    future_later = _revenue_row("3333", "20260716", later=True)
    revenue = pd.DataFrame([
        _revenue_row("1111", "20260610"), earlier, later, future_earlier, future_later,
    ])
    registry = pd.DataFrame([
        _registry_row(earlier, later), _registry_row(future_earlier, future_later),
    ], columns=RESOLUTION_COLUMNS)
    resolutions = pd.DataFrame([
        {
            "stock_id": "1111", "resume_date": "20260714", "exchange_ratio": "0.5",
            "resolution_id": "future_price_scale", "root_cause_status": "verified_non_comparable_raw_price_scale",
        },
        {
            "stock_id": "2222", "resume_date": "20260515", "exchange_ratio": "0.25",
            "resolution_id": "past_price_scale", "root_cause_status": "verified_non_comparable_raw_price_scale",
        },
    ])
    prices = pd.DataFrame([
        {
            "date": day.strftime("%Y%m%d"),
            "open": 10,
            "high": 12.5 if day >= pd.Timestamp("2026-06-15") else 10.5,
            "low": 9.5,
            "close": 12.5 if day >= pd.Timestamp("2026-06-15") else 10,
            "volume": 2000000,
            "volume_ratio": 3.0 if day == pd.Timestamp("2026-06-15") else 1.0,
        }
        for day in pd.bdate_range("2026-05-01", "2026-08-31")
    ])
    payloads = {
        REVENUE_KEY: _csv_bytes(revenue),
        MONTHLY_RESOLUTION_KEY: _csv_bytes(registry),
        PRICE_RESOLUTION_KEY: _csv_bytes(resolutions),
        **{f"{PRICE_PREFIX}{stock_id}.csv": _csv_bytes(prices) for stock_id in ("1111", "2222", "3333")},
    }
    for key, payload in payloads.items():
        path = tmp_path / key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    return tmp_path, payloads


def _filesystem_build(root: Path, cutoff: str | None, **kwargs):
    return producer.build_source_first_condition_audit(
        root / REVENUE_KEY, root / PRICE_PREFIX, root / MONTHLY_RESOLUTION_KEY,
        root / PRICE_RESOLUTION_KEY, observation_cutoff_date=cutoff, **kwargs,
    )


@pytest.mark.parametrize("cutoff", [None, CUTOFF, "20260715", "20260831"])
def test_payload_build_matches_filesystem_without_io_monkeypatch(source_inputs, cutoff):
    root, payloads = source_inputs
    original = dict(payloads)
    expected = _filesystem_build(root, cutoff)
    # All physical paths deliberately do not exist. Only exact repo-relative
    # payload keys may provide source content and the price file inventory.
    actual = _filesystem_build(
        root / "does_not_exist", cutoff, source_payloads=MappingProxyType(payloads),
    )
    for expected_frame, actual_frame in zip(expected, actual):
        assert not expected_frame.empty
        pd.testing.assert_frame_equal(
            expected_frame.drop(columns="generated_at"),
            actual_frame.drop(columns="generated_at"),
        )
    assert payloads == original


def test_explicit_none_preserves_default_filesystem_behavior(source_inputs):
    root, _payloads = source_inputs
    default = _filesystem_build(root, CUTOFF)
    explicit_none = _filesystem_build(root, CUTOFF, source_payloads=None)
    for expected, actual in zip(default, explicit_none):
        pd.testing.assert_frame_equal(
            expected.drop(columns="generated_at"), actual.drop(columns="generated_at"),
        )
    missing_registry = producer._load_price_resolutions(root / "absent.csv", source_payloads=None)
    assert missing_registry.empty
    assert list(missing_registry.columns) == ["stock_id", "resume_date", "exchange_ratio", "resolution_id"]


@pytest.mark.parametrize("key", [REVENUE_KEY, MONTHLY_RESOLUTION_KEY, PRICE_RESOLUTION_KEY])
def test_required_payload_missing_never_falls_back_to_existing_files(source_inputs, key):
    root, payloads = source_inputs
    del payloads[key]
    with pytest.raises(RuntimeError, match="source payload is missing"):
        _filesystem_build(root, CUTOFF, source_payloads=payloads)


@pytest.mark.parametrize("value", [None, "csv text", bytearray(b"csv")])
def test_payload_must_be_immutable_bytes(source_inputs, value):
    root, payloads = source_inputs
    payloads[REVENUE_KEY] = value
    with pytest.raises(RuntimeError, match="source payload must be bytes"):
        _filesystem_build(root, CUTOFF, source_payloads=payloads)


def test_missing_stock_payload_does_not_read_existing_price_file(source_inputs):
    root, payloads = source_inputs
    key = f"{PRICE_PREFIX}1111.csv"
    del payloads[key]
    resolutions = producer._load_price_resolutions(source_payloads=payloads)
    with pytest.raises(RuntimeError, match="source payload is missing"):
        producer.load_stock_price("1111", root / key, resolutions, source_payloads=payloads)
    summary, detail = _filesystem_build(root, CUTOFF, source_payloads=payloads)
    assert not detail["stock_id"].eq("1111").any()
    assert summary["source_missing_price_history_event_count"].max() >= 1


def test_payload_readers_are_fresh_and_lineage_uses_exact_payload_bytes(source_inputs):
    root, payloads = source_inputs
    first = producer.load_revenue_history(observation_cutoff_date=CUTOFF, source_payloads=payloads)
    second = producer.load_revenue_history(observation_cutoff_date=CUTOFF, source_payloads=payloads)
    pd.testing.assert_frame_equal(first, second)
    filesystem = producer.load_revenue_history(
        root / REVENUE_KEY, root / MONTHLY_RESOLUTION_KEY, observation_cutoff_date=CUTOFF,
    )
    expected = producer._monthly_revenue_run_lineage(
        filesystem, revenue_path=root / REVENUE_KEY, resolution_path=root / MONTHLY_RESOLUTION_KEY,
    )
    actual = producer._monthly_revenue_run_lineage(
        first, revenue_path=root / "absent.csv", resolution_path=root / "absent_registry.csv",
        source_payloads=payloads,
    )
    assert actual == expected
    assert actual["monthly_revenue_history_blob_sha256"] == hashlib.sha256(payloads[REVENUE_KEY]).hexdigest()
    assert first.loc[first["stock_id"].eq("2222"), "cross_market_resolution_id"].tolist() == ["synthetic_mirror_2222"]
    assert not first["stock_id"].eq("3333").any()


def test_payload_transport_changes_blob_not_canonical_lineage(source_inputs):
    root, payloads = source_inputs
    baseline = producer.load_revenue_history(observation_cutoff_date=CUTOFF, source_payloads=payloads)
    before = producer._monthly_revenue_run_lineage(
        baseline, revenue_path=root / REVENUE_KEY, resolution_path=root / MONTHLY_RESOLUTION_KEY,
        source_payloads=payloads,
    )
    for key in (REVENUE_KEY, MONTHLY_RESOLUTION_KEY):
        payloads[key] = b"\xef\xbb\xbf" + payloads[key].replace(b"\n", b"\r\n")
    transported = producer.load_revenue_history(observation_cutoff_date=CUTOFF, source_payloads=payloads)
    after = producer._monthly_revenue_run_lineage(
        transported, revenue_path=root / REVENUE_KEY, resolution_path=root / MONTHLY_RESOLUTION_KEY,
        source_payloads=payloads,
    )
    pd.testing.assert_frame_equal(baseline, transported)
    assert before.pop("monthly_revenue_history_blob_sha256") != after.pop("monthly_revenue_history_blob_sha256")
    assert before == after


def test_payload_prices_keep_original_adjustment_features_and_cutoff(source_inputs):
    root, payloads = source_inputs
    file_resolutions = producer._load_price_resolutions(root / PRICE_RESOLUTION_KEY)
    payload_resolutions = producer._load_price_resolutions(source_payloads=payloads)
    pd.testing.assert_frame_equal(file_resolutions, payload_resolutions)
    for stock_id in ("1111", "2222"):
        expected = producer.load_stock_price(
            stock_id, root / f"{PRICE_PREFIX}{stock_id}.csv", file_resolutions,
            observation_cutoff_date=CUTOFF,
        )
        actual = producer.load_stock_price(
            stock_id, root / "absent.csv", payload_resolutions,
            observation_cutoff_date=CUTOFF, source_payloads=payloads,
        )
        pd.testing.assert_frame_equal(expected, actual)
        assert actual["date"].max() == CUTOFF
        assert "future_price_scale" not in set(actual["price_resolution_ids_on_date"])
        if stock_id == "1111":
            assert actual["analysis_price_adjustment_factor"].eq(1).all()
        else:
            assert actual.loc[actual["date"].lt("20260515"), "analysis_price_adjustment_factor"].eq(4).all()


@pytest.mark.parametrize("mutation", ["registry_schema", "registry_owner", "mirror_payload", "mirror_missing"])
def test_payload_mode_preserves_resolver_fail_closed_contract(source_inputs, mutation):
    root, payloads = source_inputs
    key = MONTHLY_RESOLUTION_KEY if mutation.startswith("registry") else REVENUE_KEY
    frame = pd.read_csv(BytesIO(payloads[key]), dtype=str, keep_default_na=False)
    if mutation == "registry_schema":
        frame = frame.drop(columns="notes")
        expected = "schema mismatch"
    elif mutation == "registry_owner":
        frame.loc[0, "model_id"] = "foreign_model"
        expected = "foreign model owner"
    elif mutation == "mirror_payload":
        frame.loc[2, "monthly_revenue"] = "1001"
        expected = "payload conflict"
    else:
        frame = frame.drop(index=2)
        expected = "complete exact two-row raw pair"
    payloads[key] = _csv_bytes(frame)
    # Compare the same failure in both IO modes; neither mode weakens parsing.
    (root / key).write_bytes(payloads[key])
    with pytest.raises(RuntimeError, match=expected):
        producer.load_revenue_history(
            root / REVENUE_KEY, root / MONTHLY_RESOLUTION_KEY, observation_cutoff_date=CUTOFF,
        )
    with pytest.raises(RuntimeError, match=expected):
        producer.load_revenue_history(observation_cutoff_date=CUTOFF, source_payloads=payloads)
