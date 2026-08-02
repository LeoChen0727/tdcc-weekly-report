from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd
import pytest

import build_all_candidates_latest as candidates


def test_load_source_file_preserves_raw_and_normalized_identity(tmp_path: Path) -> None:
    source = tmp_path / "range_rebound_watch_latest.csv"
    pd.DataFrame(
        [
            {
                "date": "20260731",
                "ticker": "2451",
                "category": "range_rebound",
                "platform_high": "280",
            }
        ]
    ).to_csv(source, index=False, encoding="utf-8-sig")

    loaded = candidates.load_source_file(
        {
            "path": source,
            "producer": "stock_daily_monitor.py",
            "default_category": "range_rebound",
            "default_category_cn": "range rebound",
        }
    )

    assert len(loaded) == 1
    row = loaded.iloc[0]
    assert row["candidate_source_raw_stock_id"] == "2451"
    assert row["candidate_source_normalized_stock_id"] == "2451"
    assert row["stock_id"] == "2451"
    assert row["candidate_source_identity_columns"] == "ticker"
    assert row["candidate_source_artifact"] == source.as_posix()
    assert row["candidate_source_producer"] == "stock_daily_monitor.py"
    artifact_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
    source_payload = [
        ["date", "20260731"],
        ["ticker", "2451"],
        ["category", "range_rebound"],
        ["platform_high", "280"],
    ]
    row_sha256 = hashlib.sha256(
        json.dumps(
            source_payload,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    assert row["candidate_source_artifact_sha256"] == artifact_sha256
    assert row["candidate_source_record_number"] == "2"
    assert row["candidate_source_row_sha256"] == row_sha256
    assert row["candidate_source_row_id"] == (
        f"{source.as_posix()}@{artifact_sha256}#2:2451:{row_sha256}"
    )


def test_load_source_file_preserves_literal_na_and_cp950_lineage(
    tmp_path: Path,
) -> None:
    source = tmp_path / "range_rebound_watch_latest.csv"
    source_text = (
        "date,ticker,category,note,literal_na,literal_n_a\r\n"
        "20260731,2451,range_rebound,測試,NA,N/A\r\n"
    )
    source.write_bytes(source_text.encode("cp950"))

    loaded = candidates.load_source_file(
        {
            "path": source,
            "producer": "stock_daily_monitor.py",
            "default_category": "range_rebound",
            "default_category_cn": "range rebound",
        }
    )

    assert len(loaded) == 1
    row = loaded.iloc[0]
    assert row["note"] == "測試"
    assert row["literal_na"] == "NA"
    assert row["literal_n_a"] == "N/A"
    assert row["candidate_source_raw_stock_id"] == "2451"
    assert row["candidate_source_normalized_stock_id"] == "2451"
    assert row["candidate_source_identity_columns"] == "ticker"

    artifact_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
    row_payload = [
        ["date", "20260731"],
        ["ticker", "2451"],
        ["category", "range_rebound"],
        ["note", "測試"],
        ["literal_na", "NA"],
        ["literal_n_a", "N/A"],
    ]
    row_sha256 = hashlib.sha256(
        json.dumps(
            row_payload,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    assert row["candidate_source_artifact_sha256"] == artifact_sha256
    assert row["candidate_source_row_sha256"] == row_sha256
    assert row["candidate_source_row_id"] == (
        f"{source.as_posix()}@{artifact_sha256}#2:2451:{row_sha256}"
    )


def test_load_source_file_uses_logical_record_numbers_across_blank_lines(
    tmp_path: Path,
) -> None:
    source = tmp_path / "range_rebound_watch_latest.csv"
    source.write_bytes(
        b"\xef\xbb\xbfticker,category\r\n\r\n2451,range_rebound\r\n"
    )

    loaded = candidates.load_source_file(
        {
            "path": source,
            "producer": "stock_daily_monitor.py",
            "default_category": "range_rebound",
            "default_category_cn": "range rebound",
        }
    )

    assert len(loaded) == 1
    row = loaded.iloc[0]
    row_sha256 = hashlib.sha256(
        json.dumps(
            [["ticker", "2451"], ["category", "range_rebound"]],
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    artifact_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
    assert row["candidate_source_record_number"] == "2"
    assert row["candidate_source_row_sha256"] == row_sha256
    assert row["candidate_source_row_id"] == (
        f"{source.as_posix()}@{artifact_sha256}#2:2451:{row_sha256}"
    )


def test_builder_csv_reader_fails_when_all_decoders_fail(tmp_path: Path) -> None:
    source = tmp_path / "range_rebound_watch_latest.csv"
    source.write_bytes(b"ticker,note\n2451,\x81")

    with pytest.raises(
        RuntimeError,
        match="failed to decode CSV source with bounded encodings",
    ):
        candidates.read_csv(source)


def test_load_all_sources_keeps_distinct_category_source_lineage(tmp_path: Path) -> None:
    range_source = tmp_path / "range_rebound_watch_latest.csv"
    revenue_source = tmp_path / "revenue_pullback_latest.csv"
    pd.DataFrame(
        [
            {
                "date": "20260731",
                "ticker": "2451",
                "category": "range_rebound",
                "platform_high": "280",
            }
        ]
    ).to_csv(range_source, index=False, encoding="utf-8-sig")
    pd.DataFrame(
        [
            {
                "date": "20260731",
                "ticker": "2451",
                "category": "revenue_pullback",
                "revenue_yoy_pct": "381.55",
            }
        ]
    ).to_csv(revenue_source, index=False, encoding="utf-8-sig")

    original_sources = candidates.SOURCE_FILES
    candidates.SOURCE_FILES = [
        {
            "path": range_source,
            "producer": "stock_daily_monitor.py",
            "default_category": "range_rebound",
            "default_category_cn": "range rebound",
        },
        {
            "path": revenue_source,
            "producer": "stock_daily_monitor.py",
            "default_category": "revenue_pullback",
            "default_category_cn": "revenue pullback",
        },
    ]
    try:
        loaded = candidates.load_all_sources()
    finally:
        candidates.SOURCE_FILES = original_sources

    assert len(loaded) == 2
    assert set(loaded["category"]) == {"range_rebound", "revenue_pullback"}
    assert set(loaded["stock_id"]) == {"2451"}
    assert loaded["candidate_source_row_id"].is_unique
    assert set(loaded["candidate_source_artifact"]) == {
        range_source.as_posix(),
        revenue_source.as_posix(),
    }
    assert loaded["candidate_source_artifact_sha256"].str.fullmatch(
        r"[0-9a-f]{64}"
    ).all()
    assert loaded["candidate_source_row_sha256"].str.fullmatch(
        r"[0-9a-f]{64}"
    ).all()


def test_load_all_sources_preserves_exact_2451_duplicate_normalization_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    latest = tmp_path / "output/latest"
    latest.mkdir(parents=True)
    range_source = Path("output/latest/range_rebound_watch_latest.csv")
    revenue_source = Path("output/latest/revenue_pullback_latest.csv")
    columns = [
        "date",
        "stock_id",
        "ticker",
        "category",
        "platform_high",
        "short_platform_high",
        "platform_width_pct",
        "short_platform_width_pct",
        "false_breakout_risk",
        "revenue_yoy_pct",
        "cumulative_yoy_pct",
    ]
    pd.DataFrame(
        [
            {
                "date": "20260731",
                "stock_id": "2451",
                "ticker": "2451",
                "category": "range_rebound",
                "platform_high": "280",
                "short_platform_high": "280",
                "platform_width_pct": "29.63",
                "short_platform_width_pct": "29.63",
                "false_breakout_risk": "False",
                "revenue_yoy_pct": "381.5468504599",
                "cumulative_yoy_pct": "422.1697253819",
            }
        ],
        columns=columns,
    ).to_csv(tmp_path / range_source, index=False, encoding="utf-8-sig")
    pd.DataFrame(
        [
            {
                "date": "20260731",
                "stock_id": "2451",
                "ticker": "2451",
                "category": "revenue_pullback",
                "platform_high": "",
                "short_platform_high": "",
                "platform_width_pct": "",
                "short_platform_width_pct": "",
                "false_breakout_risk": "",
                "revenue_yoy_pct": "381.55",
                "cumulative_yoy_pct": "422.17",
            }
        ],
        columns=columns,
    ).to_csv(tmp_path / revenue_source, index=False, encoding="utf-8-sig")

    original_sources = candidates.SOURCE_FILES
    candidates.SOURCE_FILES = [
        {
            "path": range_source,
            "producer": "stock_daily_monitor.py",
            "default_category": "range_rebound",
            "default_category_cn": "range rebound",
        },
        {
            "path": revenue_source,
            "producer": "stock_daily_monitor.py",
            "default_category": "revenue_pullback",
            "default_category_cn": "revenue pullback",
        },
    ]
    monkeypatch.chdir(tmp_path)
    try:
        loaded = candidates.load_all_sources()
    finally:
        candidates.SOURCE_FILES = original_sources

    assert len(loaded) == 2
    assert set(loaded["stock_id"]) == {"2451"}
    assert set(loaded["candidate_source_raw_stock_id"]) == {"2451"}
    assert set(loaded["candidate_source_normalized_stock_id"]) == {"2451"}
    assert set(loaded["candidate_source_identity_columns"]) == {"stock_id;ticker"}
    assert set(loaded["candidate_source_artifact"]) == {
        range_source.as_posix(),
        revenue_source.as_posix(),
    }
    assert set(loaded["candidate_source_producer"]) == {"stock_daily_monitor.py"}
    assert loaded["candidate_source_row_id"].is_unique

    for _, row in loaded.iterrows():
        source_path = tmp_path / row["candidate_source_artifact"]
        source_frame = pd.read_csv(source_path, dtype=str, keep_default_na=False)
        source_payload = [
            [column, str(source_frame.iloc[0][column])]
            for column in source_frame.columns
        ]
        expected_row_sha256 = hashlib.sha256(
            json.dumps(
                source_payload,
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        expected_artifact_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
        assert row["candidate_source_artifact_sha256"] == expected_artifact_sha256
        assert row["candidate_source_record_number"] == "2"
        assert row["candidate_source_row_sha256"] == expected_row_sha256
        assert row["candidate_source_row_id"] == (
            f"{row['candidate_source_artifact']}@{expected_artifact_sha256}"
            f"#2:2451:{expected_row_sha256}"
        )

    by_category = loaded.set_index("category")
    assert by_category.loc["range_rebound", "platform_high"] == "280"
    assert by_category.loc["range_rebound", "short_platform_high"] == "280"
    assert by_category.loc["range_rebound", "platform_width_pct"] == "29.63"
    assert by_category.loc["range_rebound", "short_platform_width_pct"] == "29.63"
    assert by_category.loc["range_rebound", "false_breakout_risk"] == "False"
    assert by_category.loc["range_rebound", "revenue_yoy_pct"] == "381.5468504599"
    assert by_category.loc["range_rebound", "cumulative_yoy_pct"] == "422.1697253819"
    assert candidates.safe_str(by_category.loc["revenue_pullback", "platform_high"]) == ""
    assert (
        candidates.safe_str(by_category.loc["revenue_pullback", "short_platform_high"])
        == ""
    )
    assert (
        candidates.safe_str(by_category.loc["revenue_pullback", "platform_width_pct"])
        == ""
    )
    assert (
        candidates.safe_str(
            by_category.loc["revenue_pullback", "short_platform_width_pct"]
        )
        == ""
    )
    assert (
        candidates.safe_str(by_category.loc["revenue_pullback", "false_breakout_risk"])
        == ""
    )
    assert by_category.loc["revenue_pullback", "revenue_yoy_pct"] == "381.55"
    assert by_category.loc["revenue_pullback", "cumulative_yoy_pct"] == "422.17"


def test_deduplicate_candidates_rejects_same_grain_instead_of_keep_first() -> None:
    rows = pd.DataFrame(
        [
            {
                "date": "20260731",
                "category": "range_rebound",
                "stock_id": "2451",
                "score": "80",
                "rank": "1",
                "candidate_source_artifact": (
                    "output/latest/range_rebound_watch_latest.csv"
                ),
                "candidate_source_record_number": "2",
                "candidate_source_row_id": "source-row-a",
            },
            {
                "date": "20260731",
                "category": "range_rebound",
                "stock_id": "2451",
                "score": "79",
                "rank": "2",
                "candidate_source_artifact": (
                    "output/latest/range_rebound_watch_latest.csv"
                ),
                "candidate_source_record_number": "3",
                "candidate_source_row_id": "source-row-b",
            },
        ]
    )

    with pytest.raises(
        RuntimeError,
        match=(
            "duplicate source rows at the canonical "
            "date/category/stock_id grain"
        ),
    ):
        candidates.deduplicate_candidates(rows)


def test_load_source_file_rejects_conflicting_identity_aliases(tmp_path: Path) -> None:
    source = tmp_path / "range_rebound_watch_latest.csv"
    pd.DataFrame(
        [{"date": "20260731", "ticker": "2451", "stock_id": "2452"}]
    ).to_csv(source, index=False, encoding="utf-8-sig")

    try:
        candidates.load_source_file(
            {
                "path": source,
                "producer": "stock_daily_monitor.py",
                "default_category": "range_rebound",
                "default_category_cn": "range rebound",
            }
        )
    except RuntimeError as exc:
        assert "conflicting stock identity aliases" in str(exc)
    else:
        raise AssertionError("conflicting source identity aliases must fail closed")
