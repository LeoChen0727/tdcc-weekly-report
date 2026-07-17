from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

import merge_warrant_flow_into_candidates as warrant_merge


def _candidate_columns() -> list[str]:
    return [
        "date",
        "stock_id",
        "industry",
        *warrant_merge.WARRANT_OUTPUT_COLUMNS,
        "is_construction_recognition",
    ]


def _candidate_row() -> dict[str, object]:
    row: dict[str, object] = {
        "date": "20260716",
        "stock_id": "2330",
        "industry": "semiconductor",
        "is_construction_recognition": "False",
    }
    for column in warrant_merge.WARRANT_OUTPUT_COLUMNS:
        row[column] = "old"
    return row


def _configure_merge_paths(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> tuple[Path, Path]:
    candidate_path = tmp_path / "all_candidates_latest.csv"
    warrant_path = tmp_path / "warrant_flow_latest.csv"
    monkeypatch.setattr(warrant_merge, "ALL_CANDIDATES_CSV", candidate_path)
    monkeypatch.setattr(warrant_merge, "WARRANT_FLOW_CSV", warrant_path)
    monkeypatch.setattr(warrant_merge, "write_excel_and_md", lambda _df: None)
    monkeypatch.setattr(
        warrant_merge,
        "main_price_date_from_freshness",
        lambda: "20260716",
    )
    monkeypatch.setattr(
        warrant_merge,
        "normalize_report_candidate_dates",
        lambda frame, _date: frame,
    )
    return candidate_path, warrant_path


@pytest.mark.parametrize("warrant_case", ["usable", "empty", "no_stock_id"])
def test_merge_preserves_published_candidate_schema_in_every_output_branch(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    warrant_case: str,
) -> None:
    candidate_path, warrant_path = _configure_merge_paths(monkeypatch, tmp_path)
    original_columns = _candidate_columns()
    pd.DataFrame([_candidate_row()], columns=original_columns).to_csv(
        candidate_path,
        index=False,
        encoding="utf-8-sig",
    )

    if warrant_case == "usable":
        warrant_rows = [
            {
                "stock_id": "2330",
                "warrant_flow_signal": "call_inflow",
                "warrant_flow_score": "2",
                "note": "official",
            }
        ]
        pd.DataFrame(warrant_rows).to_csv(
            warrant_path,
            index=False,
            encoding="utf-8-sig",
        )
    elif warrant_case == "empty":
        pd.DataFrame(columns=["stock_id", "warrant_flow_signal"]).to_csv(
            warrant_path,
            index=False,
            encoding="utf-8-sig",
        )
    else:
        pd.DataFrame([{"ticker_without_contract": "2330"}]).to_csv(
            warrant_path,
            index=False,
            encoding="utf-8-sig",
        )

    merged, _status = warrant_merge.merge_warrant_flow()

    persisted = pd.read_csv(candidate_path, dtype=str)
    assert list(merged.columns) == original_columns
    assert list(persisted.columns) == original_columns
    assert len(persisted.columns) == len(set(persisted.columns))


def test_merge_is_idempotent_and_drops_only_stale_suffix_columns(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    candidate_path, warrant_path = _configure_merge_paths(monkeypatch, tmp_path)
    original_columns = [
        *_candidate_columns(),
        "call_turnover_warrant",
        "temporary_from_warrant",
    ]
    stale_row = _candidate_row()
    stale_row["call_turnover_warrant"] = "stale"
    stale_row["temporary_from_warrant"] = "stale"
    pd.DataFrame([stale_row], columns=original_columns).to_csv(
        candidate_path,
        index=False,
        encoding="utf-8-sig",
    )
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "warrant_flow_signal": "call_inflow",
                "warrant_flow_score": "2",
                "note": "official",
            }
        ]
    ).to_csv(
        warrant_path,
        index=False,
        encoding="utf-8-sig",
    )

    first, _status = warrant_merge.merge_warrant_flow()
    first_columns = list(first.columns)
    second, _status = warrant_merge.merge_warrant_flow()

    assert first_columns == _candidate_columns()
    assert list(second.columns) == first_columns
    assert len(second.columns) == len(set(second.columns))
    assert not any(column.endswith("_warrant") for column in second.columns)
    assert not any(column.endswith("_from_warrant") for column in second.columns)
