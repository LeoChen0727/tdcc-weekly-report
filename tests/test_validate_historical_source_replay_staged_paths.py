from __future__ import annotations

from scripts import validate_historical_source_replay_staged_paths as staged


def test_exact_structured_source_and_warrant_flow_paths_are_allowed() -> None:
    paths = [
        "data/daily_price/daily_price_20260720.csv",
        "output/history/warrant_flow/warrant_flow_20260720.csv",
        "output/latest/warrant_flow_latest.csv",
        "output/latest/warrant_flow_latest.md",
        "output/history/historical_source_replay/github-run-123-1/20260720/structured_source_manifest.json",
    ]

    assert staged.validate(paths) == []


def test_candidate_model_and_pdf_paths_remain_forbidden() -> None:
    errors = staged.validate(
        [
            "output/latest/all_candidates_latest.csv",
            "output/latest/daily_model_snapshot_latest.csv",
            "output/history/reports/report.pdf",
        ]
    )

    assert len(errors) == 3
    assert all("forbidden artifact" in error for error in errors)


def test_any_staged_deletion_fails_closed_even_if_path_is_allowlisted() -> None:
    errors = staged.validate(
        ["data/daily_price/daily_price_20260720.csv"],
        deleted_paths=["data/daily_price/daily_price_20260720.csv"],
    )

    assert any("staged deletion is forbidden" in error for error in errors)


def test_rename_and_type_change_statuses_fail_closed() -> None:
    errors = staged.validate_changes(
        [
            ("R100", "data/daily_price/daily_price_20260720.csv"),
            ("R100", "data/daily_price/daily_price_20260721.csv"),
            ("T", "data/market_index_history.csv"),
        ],
        scope="staged",
    )

    assert sum("status is forbidden" in error for error in errors) == 3


def test_allowlisted_unstaged_and_untracked_paths_still_fail() -> None:
    errors = staged.validate_repository_state(
        [("M", "data/market_index_history.csv")],
        [("M", "data/market_index_ohlc_history.csv")],
        ["data/daily_price/daily_price_20260720.csv"],
    )

    assert any("unstaged worktree change" in error for error in errors)
    assert any("untracked worktree path" in error for error in errors)


def test_name_status_parser_keeps_both_rename_paths() -> None:
    changes = staged._parse_name_status_z(
        "R100\0data/daily_price/daily_price_20260720.csv\0"
        "data/daily_price/daily_price_20260721.csv\0M\0data/market_index_history.csv\0"
    )

    assert changes == [
        ("R100", "data/daily_price/daily_price_20260720.csv"),
        ("R100", "data/daily_price/daily_price_20260721.csv"),
        ("M", "data/market_index_history.csv"),
    ]
