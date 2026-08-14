from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd
import pytest

from scripts import build_stock_price_history as history
from scripts import repair_daily_price_range as repair


def patch_history_paths(tmp_path: Path, monkeypatch) -> tuple[Path, Path, Path, Path]:
    daily_dir = tmp_path / "data" / "daily_price"
    stock_dir = tmp_path / "data" / "stock_price_history"
    latest_dir = tmp_path / "output" / "latest"
    docs_latest_dir = tmp_path / "docs" / "latest"
    for path in (daily_dir, stock_dir, latest_dir, docs_latest_dir):
        path.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(history, "DATA_DAILY_PRICE_DIR", daily_dir)
    monkeypatch.setattr(history, "STOCK_HISTORY_DIR", stock_dir)
    monkeypatch.setattr(history, "LATEST_DIR", latest_dir)
    monkeypatch.setattr(history, "DOCS_LATEST_DIR", docs_latest_dir)
    monkeypatch.setattr(history, "MANIFEST_CSV", latest_dir / "stock_price_history_manifest.csv")
    monkeypatch.setattr(history, "MANIFEST_JSON", latest_dir / "stock_price_history_manifest.json")
    monkeypatch.setattr(history, "MANIFEST_MD", latest_dir / "stock_price_history_manifest.md")
    monkeypatch.setattr(history, "DOCS_MANIFEST_CSV", docs_latest_dir / "stock_price_history_manifest.csv")
    monkeypatch.setattr(history, "DOCS_MANIFEST_JSON", docs_latest_dir / "stock_price_history_manifest.json")
    monkeypatch.setattr(history, "DOCS_MANIFEST_MD", docs_latest_dir / "stock_price_history_manifest.md")
    monkeypatch.setattr(history, "SOURCE_RECOVERY_JSON", latest_dir / "daily_price_source_recovery_latest.json")
    return daily_dir, stock_dir, latest_dir, docs_latest_dir


def write_daily_price(path: Path, date: str, close: float) -> None:
    pd.DataFrame(
        [
            {
                "date": date,
                "stock_id": "2330",
                "stock_name": "TSMC",
                "market": "TWSE",
                "open": close - 5,
                "high": close + 5,
                "low": close - 10,
                "close": close,
                "volume": 1000,
                "trading_value": 1000000,
                "source": "TEST",
            }
        ]
    ).to_csv(path, index=False, encoding="utf-8")


def write_existing_history(path: Path) -> None:
    pd.DataFrame(
        [
            {
                "date": "20260605",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "market": "TWSE",
                "open": 1000,
                "high": 1010,
                "low": 990,
                "close": 1005,
                "volume": 1000,
                "trading_value": 1000000,
                "source": "TEST",
                "source_file": "data/daily_price/daily_price_20260605.csv",
            }
        ]
    ).to_csv(path, index=False, encoding="utf-8")


def write_manifest_claiming_newer_history(path: Path) -> None:
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "stock_name": "TSMC",
                "market": "TWSE",
                "rows": 2,
                "start_date": "20260605",
                "end_date": "20260611",
                "latest_close": 1050,
                "latest_volume": 1000,
                "file_path": "data/stock_price_history/2330.csv",
                "raw_url": "https://example.invalid/2330.csv",
            }
        ]
    ).to_csv(path, index=False, encoding="utf-8")


def test_incremental_latest_updates_when_manifest_is_newer_than_actual_history(tmp_path, monkeypatch):
    daily_dir, stock_dir, latest_dir, _ = patch_history_paths(tmp_path, monkeypatch)
    write_daily_price(daily_dir / "daily_price_20260611.csv", "20260611", close=1050)
    write_existing_history(stock_dir / "2330.csv")
    write_manifest_claiming_newer_history(latest_dir / "stock_price_history_manifest.csv")

    manifest = history.build_history_files_incremental_latest()

    updated = pd.read_csv(stock_dir / "2330.csv", dtype=str)

    assert updated["date"].iloc[-1] == "20260611"
    assert manifest.loc[manifest["stock_id"].astype(str).eq("2330"), "end_date"].iloc[0] == "20260611"


def test_source_recovery_action_forces_full_history_rebuild(tmp_path, monkeypatch):
    daily_dir, stock_dir, latest_dir, _ = patch_history_paths(tmp_path, monkeypatch)
    write_daily_price(daily_dir / "daily_price_20260625.csv", "20260625", close=1040)
    write_daily_price(daily_dir / "daily_price_20260626.csv", "20260626", close=1050)
    (latest_dir / "daily_price_source_recovery_latest.json").write_text(
        (
            "{\n"
            '  "status": "repaired",\n'
            '  "actions": [{"date": "20260625", "action": "repair_daily_price_range"}]\n'
            "}\n"
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        history,
        "parse_args",
        lambda: argparse.Namespace(
            stock_id=None,
            incremental_latest=True,
            full_rebuild_if_source_recovered=True,
        ),
    )

    assert history.main() == 0

    updated = pd.read_csv(stock_dir / "2330.csv", dtype=str)

    assert list(updated["date"]) == ["20260625", "20260626"]
    assert history.source_recovery_has_repair_action()


def write_selected_daily_price(path: Path, date_text: str) -> None:
    pd.DataFrame(
        [
            {
                "date": date_text,
                "stock_id": "2330",
                "stock_name": "TSMC",
                "market": "TWSE",
                "open": 100,
                "high": 110,
                "low": 95,
                "close": 105,
                "volume": 1000,
                "trading_value": 100000,
                "source": "TWSE_TEST",
            },
            {
                "date": date_text,
                "stock_id": "00925",
                "stock_name": "ETF",
                "market": "TPEx",
                "open": 20,
                "high": 21,
                "low": 19,
                "close": 20.5,
                "volume": 2000,
                "trading_value": 40000,
                "source": "TPEX_TEST",
            },
        ]
    ).to_csv(path, index=False, encoding="utf-8-sig")


def write_base_history(path: Path, stock_id: str, dates: list[str]) -> None:
    rows = []
    for index, date_text in enumerate(dates):
        close = 80 + index
        rows.append(
            {
                "date": date_text,
                "stock_id": stock_id,
                "stock_name": f"Name {stock_id}",
                "market": "TWSE",
                "open": close - 1,
                "high": close + 1,
                "low": close - 2,
                "close": close,
                "volume": 500 + index,
                "trading_value": 50000 + index,
                "source": "TEST",
                "source_file": f"data/daily_price/daily_price_{date_text}.csv",
            }
        )
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8")


def write_selected_repair_contract_files(
    latest_dir: Path,
    docs_latest_dir: Path,
    stock_dir: Path,
    dates: list[str],
) -> None:
    daily_dir = latest_dir.parents[1] / "data" / "daily_price"
    manifest_rows = []
    for path in sorted(stock_dir.glob("*.csv")):
        frame = pd.read_csv(path, dtype=str).fillna("")
        stock_id = history.normalize_stock_id(path.stem)
        latest = frame.iloc[-1]
        manifest_rows.append(
            {
                "stock_id": stock_id,
                "stock_name": latest.get("stock_name", ""),
                "market": latest.get("market", ""),
                "rows": len(frame),
                "start_date": frame["date"].iloc[0],
                "end_date": frame["date"].iloc[-1],
                "latest_close": latest.get("close", ""),
                "latest_volume": latest.get("volume", ""),
                "file_path": f"data/stock_price_history/{stock_id}.csv",
                "raw_url": f"https://example.invalid/{stock_id}.csv",
            }
        )
    manifest = pd.DataFrame(manifest_rows)
    manifest.to_csv(latest_dir / "stock_price_history_manifest.csv", index=False, encoding="utf-8")
    manifest_json = {
        "generated_at": "before",
        "status": "generated",
        "stock_count": len(manifest),
        "daily_price_file_count": 0,
        "manifest_csv": "output/latest/stock_price_history_manifest.csv",
        "manifest_raw_url": "https://example.invalid/manifest.csv",
        "manifest_pages_url": "https://example.invalid/manifest-pages.csv",
        "history_dir": "data/stock_price_history",
    }
    (latest_dir / "stock_price_history_manifest.json").write_text(
        json.dumps(manifest_json), encoding="utf-8"
    )
    (latest_dir / "stock_price_history_manifest.md").write_text("before manifest\n", encoding="utf-8")
    for name in (
        "stock_price_history_manifest.csv",
        "stock_price_history_manifest.json",
        "stock_price_history_manifest.md",
    ):
        source = latest_dir / name
        (docs_latest_dir / name).write_bytes(source.read_bytes())
    (latest_dir / "repair_daily_price_range_latest.json").write_text(
        json.dumps(
            {
                "schema_version": "repair_daily_price_range_v2",
                "mode": "selected_dates",
                "source_base_sha": "a" * 40,
                "selected_dates": dates,
                "rows": [
                    {
                        "date": date_text,
                        "status": "repaired",
                        "twse_rows": 2,
                        "tpex_rows": 0,
                        "total_rows": 2,
                        "saved_files": (
                            f"data/daily_price/{date_text}.csv;"
                            f"data/daily_price/daily_price_{date_text}.csv"
                        ),
                        "canonical_path": f"data/daily_price/daily_price_{date_text}.csv",
                        "legacy_path": f"data/daily_price/{date_text}.csv",
                        "price_sha256": hashlib.sha256(
                            (daily_dir / f"daily_price_{date_text}.csv").read_bytes()
                        ).hexdigest(),
                        "fetch_response_provenance": [
                            {
                                "source_name": "TWSE_TEST",
                                "endpoint": "https://example.test/twse",
                                "attempt": 1,
                                "expected_response_date": date_text,
                                "exact_date_match": True,
                                "status_code": 200,
                                "raw_sha256": "a" * 64,
                                "normalized_sha256": "b" * 64,
                            },
                            {
                                "source_name": "TPEX_TEST",
                                "endpoint": "https://example.test/tpex",
                                "attempt": 1,
                                "expected_response_date": date_text,
                                "exact_date_match": True,
                                "status_code": 200,
                                "raw_sha256": "c" * 64,
                                "normalized_sha256": "d" * 64,
                            },
                        ],
                    }
                    for date_text in dates
                ],
                "check_rows": [],
            }
        ),
        encoding="utf-8",
    )
    (latest_dir / "repair_daily_price_range_latest.md").write_text(
        "# selected repair\n", encoding="utf-8"
    )


def setup_selected_history_case(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    daily_dir, stock_dir, latest_dir, docs_latest_dir = patch_history_paths(tmp_path, monkeypatch)
    dates = ["20250411", "20250521"]
    for date_text in dates:
        write_selected_daily_price(daily_dir / f"daily_price_{date_text}.csv", date_text)
        (daily_dir / f"{date_text}.csv").write_bytes(
            (daily_dir / f"daily_price_{date_text}.csv").read_bytes()
        )
    write_base_history(stock_dir / "2330.csv", "2330", ["20250410", "20250522"])
    write_base_history(stock_dir / "9999.csv", "9999", ["20250410", "20250522"])
    write_selected_repair_contract_files(latest_dir, docs_latest_dir, stock_dir, dates)
    return dates, daily_dir, stock_dir, latest_dir, docs_latest_dir


def test_selected_date_history_repair_injects_existing_creates_source_limited_and_preserves_outside(
    tmp_path: Path,
    monkeypatch,
):
    dates, _, stock_dir, latest_dir, _ = setup_selected_history_case(tmp_path, monkeypatch)
    before_existing = pd.read_csv(stock_dir / "2330.csv", dtype=str).fillna("")
    untouched_before = hashlib.sha256((stock_dir / "9999.csv").read_bytes()).hexdigest()

    manifest = history.build_history_files_selected_dates(
        dates,
        allowed_create_stock_ids={"00925"},
        expected_stock_union_count=2,
        expected_selected_row_count=4,
        expected_existing_history_count=1,
        expected_created_history_count=1,
        expected_untouched_history_count=1,
    )

    updated = pd.read_csv(stock_dir / "2330.csv", dtype=str).fillna("")
    created = pd.read_csv(stock_dir / "00925.csv", dtype=str).fillna("")
    assert list(updated["date"]) == ["20250410", "20250411", "20250521", "20250522"]
    assert list(created["date"]) == dates
    assert history.base_records_sha256(before_existing, excluded_dates=set(dates)) == history.base_records_sha256(
        updated, excluded_dates=set(dates)
    )
    assert hashlib.sha256((stock_dir / "9999.csv").read_bytes()).hexdigest() == untouched_before
    assert set(manifest["stock_id"].map(history.normalize_stock_id)) == {"00925", "2330", "9999"}

    report = json.loads(
        (latest_dir / "repair_daily_price_range_latest.json").read_text(encoding="utf-8")
    )["history_repair"]
    assert report["eligible_stock_union_count"] == 2
    assert report["eligible_stock_date_row_count"] == 4
    assert report["created_history_stock_ids"] == ["00925"]
    assert report["selected_rows_injected_existing_histories"] == 2
    assert report["selected_rows_created_histories"] == 2
    assert report["new_history_source_coverage"] == [
        {
            "stock_id": "00925",
            "new_history_source_coverage": "target_dates_only",
            "source_rows": 2,
            "outside_selected_date_source_rows": 0,
        }
    ]
    assert report["non_selected_base_before_sha256"] == report["non_selected_base_after_sha256"]
    assert (
        report["pre_repair_indicator_before_sha256"]
        == report["pre_repair_indicator_after_sha256"]
    )
    assert report["untouched_history_before_sha256"] == report["untouched_history_after_sha256"]


def test_selected_date_history_second_run_is_noop_and_preserves_manifest_timestamps(
    tmp_path: Path,
    monkeypatch,
):
    dates, _, stock_dir, latest_dir, docs_latest_dir = setup_selected_history_case(tmp_path, monkeypatch)
    history.build_history_files_selected_dates(
        dates,
        allowed_create_stock_ids={"00925"},
        expected_stock_union_count=2,
        expected_selected_row_count=4,
        expected_existing_history_count=1,
        expected_created_history_count=1,
        expected_untouched_history_count=1,
    )
    observed_paths = [
        stock_dir / "2330.csv",
        stock_dir / "00925.csv",
        latest_dir / "stock_price_history_manifest.csv",
        latest_dir / "stock_price_history_manifest.json",
        latest_dir / "stock_price_history_manifest.md",
        docs_latest_dir / "stock_price_history_manifest.csv",
        docs_latest_dir / "stock_price_history_manifest.json",
        docs_latest_dir / "stock_price_history_manifest.md",
        latest_dir / "repair_daily_price_range_latest.json",
        latest_dir / "repair_daily_price_range_latest.md",
    ]
    before = {path: path.read_bytes() for path in observed_paths}

    history.build_history_files_selected_dates(
        dates,
        allowed_create_stock_ids={"00925"},
        expected_stock_union_count=2,
        expected_selected_row_count=4,
        expected_existing_history_count=2,
        expected_untouched_history_count=1,
    )

    assert {path: path.read_bytes() for path in observed_paths} == before


def test_selected_date_history_missing_stock_with_older_source_row_fails_closed(
    tmp_path: Path,
    monkeypatch,
):
    dates, daily_dir, stock_dir, _, _ = setup_selected_history_case(tmp_path, monkeypatch)
    monkeypatch.setattr(
        history,
        "drop_stale_duplicate_dates",
        lambda frame, *args, **kwargs: frame.iloc[0:0].copy(),
    )
    pd.DataFrame(
        [
            {
                "date": "20250410",
                "stock_id": "00925",
                "stock_name": "ETF",
                "market": "TWSE",
                "open": 19,
                "high": 20,
                "low": 18,
                "close": 19.5,
                "volume": 100,
                "trading_value": 2000,
                "source": "TWSE_TEST",
            }
        ]
    ).to_csv(daily_dir / "daily_price_20250410.csv", index=False, encoding="utf-8-sig")

    with pytest.raises(ValueError, match="source rows outside selected dates"):
        history.build_history_files_selected_dates(
            dates,
            allowed_create_stock_ids={"00925"},
            expected_stock_union_count=2,
            expected_selected_row_count=4,
        )
    assert not (stock_dir / "00925.csv").exists()


def test_selected_date_history_expected_zero_created_count_is_enforced(
    tmp_path: Path,
    monkeypatch,
):
    dates, _, stock_dir, _, _ = setup_selected_history_case(tmp_path, monkeypatch)

    with pytest.raises(ValueError, match="missing-history count mismatch"):
        history.build_history_files_selected_dates(
            dates,
            allowed_create_stock_ids={"00925"},
            expected_stock_union_count=2,
            expected_selected_row_count=4,
            expected_created_history_count=0,
        )

    assert not (stock_dir / "00925.csv").exists()


@pytest.mark.parametrize("fail_after_replace", [2, 9])
def test_selected_date_history_transaction_rolls_back_histories_manifests_and_report(
    tmp_path: Path,
    monkeypatch,
    fail_after_replace: int,
):
    dates, _, stock_dir, latest_dir, docs_latest_dir = setup_selected_history_case(tmp_path, monkeypatch)
    real_replace = history.os.replace

    def same_volume_replace(source, target):
        assert Path(source).resolve().anchor == Path(target).resolve().anchor
        assert Path(source).resolve().is_relative_to(tmp_path.resolve())
        return real_replace(source, target)

    monkeypatch.setattr(history.os, "replace", same_volume_replace)
    observed_paths = [
        stock_dir / "2330.csv",
        stock_dir / "9999.csv",
        latest_dir / "stock_price_history_manifest.csv",
        latest_dir / "stock_price_history_manifest.json",
        latest_dir / "stock_price_history_manifest.md",
        docs_latest_dir / "stock_price_history_manifest.csv",
        docs_latest_dir / "stock_price_history_manifest.json",
        docs_latest_dir / "stock_price_history_manifest.md",
        latest_dir / "repair_daily_price_range_latest.json",
        latest_dir / "repair_daily_price_range_latest.md",
    ]
    before = {path: path.read_bytes() for path in observed_paths}

    with pytest.raises(OSError, match="injected selected history repair transaction failure"):
        history.build_history_files_selected_dates(
            dates,
            allowed_create_stock_ids={"00925"},
            expected_stock_union_count=2,
            expected_selected_row_count=4,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            fail_after_replace=fail_after_replace,
        )

    assert {path: path.read_bytes() for path in observed_paths} == before
    assert not (stock_dir / "00925.csv").exists()


@pytest.mark.parametrize("target_kind", ["canonical", "legacy"])
def test_selected_date_history_source_mutation_after_report_fails_closed(
    tmp_path: Path,
    monkeypatch,
    target_kind: str,
):
    dates, daily_dir, stock_dir, _, _ = setup_selected_history_case(tmp_path, monkeypatch)
    target = (
        daily_dir / "daily_price_20250411.csv"
        if target_kind == "canonical"
        else daily_dir / "20250411.csv"
    )
    target.write_bytes(target.read_bytes() + b"\n")
    before = (stock_dir / "2330.csv").read_bytes()

    with pytest.raises(
        ValueError, match="(source SHA-256|canonical/legacy payload) mismatch"
    ):
        history.build_history_files_selected_dates(
            dates,
            allowed_create_stock_ids={"00925"},
            expected_stock_union_count=2,
            expected_selected_row_count=4,
        )

    assert (stock_dir / "2330.csv").read_bytes() == before
    assert not (stock_dir / "00925.csv").exists()


def test_selected_date_history_accepts_failed_attempt_before_exact_market_successes(
    tmp_path: Path,
    monkeypatch,
):
    dates, _, _, latest_dir, _ = setup_selected_history_case(tmp_path, monkeypatch)
    report_path = latest_dir / "repair_daily_price_range_latest.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["rows"][0]["fetch_response_provenance"].insert(
        0,
        {
            "source_name": "TWSE_RWD_JSON_MI_INDEX",
            "endpoint": "https://example.test/twse-failed",
            "attempt": 1,
            "expected_response_date": dates[0],
            "exact_date_match": False,
            "status_code": 503,
            "raw_sha256": "e" * 64,
            "normalized_sha256": "f" * 64,
        },
    )
    report_path.write_text(json.dumps(report), encoding="utf-8")

    manifest = history.build_history_files_selected_dates(
        dates,
        allowed_create_stock_ids={"00925"},
        expected_stock_union_count=2,
        expected_selected_row_count=4,
    )

    assert set(manifest["stock_id"].map(history.normalize_stock_id)) == {
        "00925",
        "2330",
        "9999",
    }


def test_selected_date_history_pre_repair_indicator_drift_fails_closed(
    tmp_path: Path,
    monkeypatch,
):
    dates, _, stock_dir, latest_dir, docs_latest_dir = setup_selected_history_case(
        tmp_path, monkeypatch
    )
    prior_dates = [
        "20250403",
        "20250404",
        "20250407",
        "20250408",
        "20250409",
        "20250410",
        "20250522",
    ]
    write_base_history(stock_dir / "2330.csv", "2330", prior_dates)
    base = pd.read_csv(stock_dir / "2330.csv", dtype=str).fillna("")
    with_indicators = history.round_numeric_columns(
        history.add_indicators(history.normalize_base_frame(base))
    )
    with_indicators.loc[
        with_indicators["date"].eq("20250410"), "ma5"
    ] = 999.0
    with_indicators.to_csv(stock_dir / "2330.csv", index=False, encoding="utf-8")
    write_selected_repair_contract_files(
        latest_dir, docs_latest_dir, stock_dir, dates
    )
    before = (stock_dir / "2330.csv").read_bytes()

    with pytest.raises(ValueError, match="changed pre-repair indicators"):
        history.build_history_files_selected_dates(
            dates,
            allowed_create_stock_ids={"00925"},
            expected_stock_union_count=2,
            expected_selected_row_count=4,
        )

    assert (stock_dir / "2330.csv").read_bytes() == before
    assert not (stock_dir / "00925.csv").exists()


def selected_source_full_market_frame(date_text: str) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for offset in range(1300):
        market = "TWSE" if offset < 700 else "TPEx"
        price = 20.0 + offset / 100
        rows.append(
            {
                "date": date_text,
                "stock_id": str(1000 + offset),
                "stock_name": f"Stock {offset}",
                "market": market,
                "open": price,
                "high": price + 1,
                "low": price - 1,
                "close": price + 0.5,
                "volume": 1000 + offset,
                "trading_value": 100000 + offset,
                "source": f"{market}_TEST",
            }
        )
    return pd.DataFrame(rows)


def selected_source_args(dates: str) -> argparse.Namespace:
    date_values = [value for value in dates.split(",") if value]
    return argparse.Namespace(
        dates=dates,
        start_date="",
        end_date="",
        source_base_sha="a" * 40,
        max_days=10,
        retries=1,
        sleep_seconds=0.0,
        check_code="",
        expected_date_contract=[
            (
                f"{date_text}:"
                f"{hashlib.sha256(repair.dataframe_csv_bytes(selected_source_full_market_frame(date_text))).hexdigest()}:"
                "1300"
            )
            for date_text in date_values
        ],
        market_session_already_refreshed=False,
    )


def selected_source_fake_fetch(date_text: str, retries: int, sleep_seconds: float):
    del retries, sleep_seconds
    frame = selected_source_full_market_frame(date_text)
    return (
        frame,
        {
            "date": date_text,
            "full_market_ok": True,
            "twse_rows": 700,
            "tpex_rows": 600,
            "total_rows": 1300,
            "fetch_response_provenance": [
                {
                    "endpoint": f"https://example.test/{date_text}",
                    "raw_sha256": "a" * 64,
                    "normalized_sha256": "b" * 64,
                    "expected_response_date": date_text,
                    "exact_date_match": True,
                }
            ],
        },
        [f"test fetch {date_text}"],
    )


def test_selected_dates_publish_only_exact_files_and_hash_bound_report(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(repair, "_repository_head", lambda root: "a" * 40)
    marker = tmp_path / "data" / "daily_price" / "daily_price_20250101.csv"
    marker.parent.mkdir(parents=True)
    marker.write_bytes(b"unchanged")

    args = selected_source_args("20250411,20250521")
    args.expected_date_contract = [
        (
            f"{date_text}:"
            f"{hashlib.sha256(repair.dataframe_csv_bytes(selected_source_full_market_frame(date_text))).hexdigest()}:"
            "1300"
        )
        for date_text in ("20250411", "20250521")
    ]
    result = repair.run_selected_dates(
        args,
        fetch_func=selected_source_fake_fetch,
    )

    assert result == 0
    assert marker.read_bytes() == b"unchanged"
    for date_text in ("20250411", "20250521"):
        canonical = tmp_path / "data" / "daily_price" / f"daily_price_{date_text}.csv"
        legacy = tmp_path / "data" / "daily_price" / f"{date_text}.csv"
        assert canonical.read_bytes() == legacy.read_bytes()
        assert canonical.read_bytes().startswith(b"\xef\xbb\xbf")

    report = json.loads(
        (tmp_path / "output" / "latest" / "repair_daily_price_range_latest.json").read_text(
            encoding="utf-8"
        )
    )
    assert report["schema_version"] == "repair_daily_price_range_v2"
    assert report["mode"] == "selected_dates"
    assert report["selected_dates"] == ["20250411", "20250521"]
    assert len(report["expected_date_contracts"]) == 2
    assert len(report["rows"]) == 2
    for row in report["rows"]:
        payload = (tmp_path / row["canonical_path"]).read_bytes()
        assert row["price_sha256"] == hashlib.sha256(payload).hexdigest()
        assert row["fetch_response_provenance"][0]["exact_date_match"] is True


@pytest.mark.parametrize("fail_after_replace", [2, 5])
def test_selected_dates_transaction_rolls_back_every_replaced_target(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    fail_after_replace: int,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(repair, "_repository_head", lambda root: "a" * 40)
    real_replace = repair.os.replace

    def same_volume_replace(source, target):
        assert Path(source).resolve().anchor == Path(target).resolve().anchor
        assert Path(source).resolve().is_relative_to(tmp_path.resolve())
        return real_replace(source, target)

    monkeypatch.setattr(repair.os, "replace", same_volume_replace)
    expected: dict[Path, bytes] = {}
    for relative in (
        Path("data/daily_price/20250411.csv"),
        Path("data/daily_price/daily_price_20250411.csv"),
        Path("output/latest/repair_daily_price_range_latest.csv"),
        Path("output/latest/repair_daily_price_range_check_code_latest.csv"),
        Path("output/latest/repair_daily_price_range_latest.json"),
        Path("output/latest/repair_daily_price_range_latest.md"),
    ):
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = f"old:{relative.as_posix()}".encode("utf-8")
        path.write_bytes(payload)
        expected[path] = payload

    with pytest.raises(OSError, match="injected selected-date repair transaction failure"):
        repair.run_selected_dates(
            selected_source_args("20250411"),
            fetch_func=selected_source_fake_fetch,
            fail_after_replace=fail_after_replace,
        )

    for path, payload in expected.items():
        assert path.read_bytes() == payload


@pytest.mark.parametrize(
    "value,message",
    [
        ("20250521,20250411", "strictly ascending"),
        ("20250411,20250411", "duplicates"),
        ("20250230", "day is out of range"),
    ],
)
def test_selected_dates_fail_closed_on_invalid_identity(value: str, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        repair.parse_selected_dates(value)


def test_selected_dates_reject_range_arguments(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    args = selected_source_args("20250411")
    args.start_date = "20250411"
    with pytest.raises(ValueError, match="mutually exclusive"):
        repair.run_selected_dates(args, fetch_func=selected_source_fake_fetch)


def test_selected_dates_require_source_base_binding() -> None:
    args = selected_source_args("20250411")
    args.source_base_sha = ""

    with pytest.raises(ValueError, match="requires source_base_sha"):
        repair.run_selected_dates(args, fetch_func=selected_source_fake_fetch)


def test_selected_dates_require_expected_contracts() -> None:
    args = selected_source_args("20250411")
    args.expected_date_contract = None

    with pytest.raises(ValueError, match="requires expected date contracts"):
        repair.run_selected_dates(args, fetch_func=selected_source_fake_fetch)


def test_selected_dates_expected_contract_fails_before_any_publish(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(repair, "_repository_head", lambda root: "a" * 40)
    marker = tmp_path / "data/daily_price/daily_price_20250411.csv"
    marker.parent.mkdir(parents=True)
    marker.write_bytes(b"old canonical")
    args = selected_source_args("20250411")
    args.expected_date_contract = [f"20250411:{'0' * 64}:1300"]

    with pytest.raises(ValueError, match="normalized official source drift"):
        repair.run_selected_dates(args, fetch_func=selected_source_fake_fetch)

    assert marker.read_bytes() == b"old canonical"
    assert not (tmp_path / "output/latest/repair_daily_price_range_latest.json").exists()


def test_selected_dates_expected_contract_must_cover_exact_date_set() -> None:
    args = selected_source_args("20250411,20250521")
    args.expected_date_contract = [f"20250411:{'a' * 64}:1300"]

    with pytest.raises(ValueError, match="every and only selected date"):
        repair.run_selected_dates(args, fetch_func=selected_source_fake_fetch)


def test_selected_date_main_never_refreshes_current_market_session(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    args = selected_source_args("20250411")
    monkeypatch.setattr(repair, "parse_args", lambda: args)
    monkeypatch.setattr(repair, "run", lambda observed: 17 if observed is args else 99)
    monkeypatch.setattr(
        repair,
        "_refresh_range_market_session",
        lambda: pytest.fail("selected-date mode refreshed market session"),
    )

    assert repair.main() == 17


def test_legacy_range_main_uses_current_market_session_refresh_seam(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    args = selected_source_args("")
    observed: list[str] = []
    monkeypatch.setattr(repair, "parse_args", lambda: args)
    monkeypatch.setattr(repair, "run", lambda current: 17 if current is args else 99)
    monkeypatch.setattr(
        repair,
        "_refresh_range_market_session",
        lambda: observed.append("called") or {"market_status": "open_confirmed"},
    )

    assert repair.main() == 17
    assert observed == ["called"]
