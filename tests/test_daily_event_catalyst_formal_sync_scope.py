from __future__ import annotations

import csv
from pathlib import Path

from scripts.validate_daily_event_catalyst_formal_sync_scope import (
    ALLOWED_MUTABLE_MODEL_IDS,
    FORMAL_SIGNAL_ARTIFACTS,
    build_scope_snapshot,
    compare_scope_snapshots,
    validate_staged_path_list,
)


def _write_artifacts(root: Path, rows: list[dict[str, str]]) -> None:
    columns = ["signal_date", "stock_id", "model_id", "model_score", "display_rank"]
    for relative_path in FORMAL_SIGNAL_ARTIFACTS:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns)
            writer.writeheader()
            writer.writerows(rows)


def _baseline_rows() -> list[dict[str, str]]:
    return [
        {
            "signal_date": "20260716",
            "stock_id": "2330",
            "model_id": "revenue_unreacted_range",
            "model_score": "84",
            "display_rank": "1",
        },
        {
            "signal_date": "20260716",
            "stock_id": "1234",
            "model_id": "w_bottom_right_side",
            "model_score": "90",
            "display_rank": "1",
        },
    ]


def test_scope_allows_only_revenue_model_row_changes(tmp_path: Path) -> None:
    assert ALLOWED_MUTABLE_MODEL_IDS == {"revenue_unreacted_range"}
    _write_artifacts(tmp_path, _baseline_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _baseline_rows()
    after_rows[0]["model_score"] = "87"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert compare_scope_snapshots(before, after) == []
    assert before["aggregate_sha256"] == after["aggregate_sha256"]


def test_scope_fails_when_non_revenue_model_row_changes(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _baseline_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _baseline_rows()
    after_rows[1]["display_rank"] = "2"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    compare_errors = compare_scope_snapshots(before, after)
    assert len(compare_errors) == len(FORMAL_SIGNAL_ARTIFACTS)
    assert all("non-revenue formal signal hash drift" in error for error in compare_errors)


def test_scope_is_order_independent_for_protected_rows(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _baseline_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    _write_artifacts(tmp_path, list(reversed(_baseline_rows())))
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert compare_scope_snapshots(before, after) == []


def test_scope_requires_model_id_column(tmp_path: Path) -> None:
    for relative_path in FORMAL_SIGNAL_ARTIFACTS:
        path = tmp_path / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("stock_id,model_score\n2330,84\n", encoding="utf-8")

    _, errors = build_scope_snapshot(tmp_path)

    assert len(errors) == len(FORMAL_SIGNAL_ARTIFACTS)
    assert all("missing model_id" in error for error in errors)


def test_staged_path_allowlist_accepts_event_owned_formal_sync_outputs() -> None:
    assert validate_staged_path_list(
        [
            "data/event_catalysts/event_catalyst_log.csv",
            "output/latest/daily_candidate_model_signals_latest.csv",
            "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv",
            "output/history/daily_model_snapshots/all_candidates_20260716.csv",
            "docs/latest/daily_candidate_model_signals_latest.csv",
        ]
    ) == []


def test_staged_path_allowlist_rejects_mature_model_and_unowned_outputs() -> None:
    errors = validate_staged_path_list(
        [
            "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
            "output/history/daily_model_snapshots/daily_w_bottom_right_side_operation_section_20260716.csv",
            "docs/latest/unowned_artifact_latest.csv",
        ]
    )

    assert len(errors) == 3
    assert all("outside allowlist" in error for error in errors)
