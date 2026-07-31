from __future__ import annotations

from scripts import validate_historical_source_replay_staged_paths as staged


def test_exact_structured_source_and_warrant_flow_paths_are_allowed() -> None:
    paths = [
        "data/daily_price/daily_price_20260720.csv",
        "output/history/warrant_flow/warrant_flow_20260720.csv",
        "output/latest/warrant_flow_latest.csv",
        "output/latest/warrant_flow_latest.md",
        "output/latest/volume_attack_theme_layer_latest.csv",
        "output/latest/volume_attack_theme_stocks_latest.md",
        "output/latest/volume_attack_theme_layer_validation_latest.json",
        "docs/latest/volume_attack_theme_layer_latest.md",
        "docs/latest/volume_attack_theme_stocks_latest.csv",
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


def test_theme_near_misses_and_formal_model_artifacts_remain_forbidden() -> None:
    paths = [
        "output/latest/volume_attack_theme_layer_latest.json",
        "output/latest/volume_attack_theme_layer_validation_latest.csv",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "output/latest/daily_volume_breakout_operation_section_latest.csv",
        "output/latest/model_operation_readiness_latest.csv",
        "output/latest/volume_breakout_rank_latest.csv",
    ]

    errors = staged.validate(paths)

    assert len(errors) == len(paths)
    assert all(
        "forbidden artifact" in error or "not allowlisted" in error
        for error in errors
    )


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


def test_preserve_mode_reverse_forbids_raw_price_history_and_manifest_paths() -> None:
    protected = [
        "data/daily_price/daily_price_20260720.csv",
        "data/daily_price/20260720.csv",
        "data/stock_price_history/2330.csv",
        "output/latest/stock_price_history_manifest.csv",
        "docs/latest/stock_price_history_manifest.md",
    ]

    errors = staged.validate(
        protected,
        price_history_high_water_date="20260728",
    )

    assert len(errors) == len(protected)
    assert all("preserve mode forbids protected price/history path" in error for error in errors)


def test_preserve_mode_still_allows_formal_price_status_continuity_and_freshness() -> None:
    allowed = [
        "output/latest/official_daily_price_latest.csv",
        "output/latest/official_price_fetch_latest.json",
        "output/latest/official_price_fetch_latest.md",
        "output/latest/daily_price_history_continuity_latest.json",
        "output/latest/data_freshness_latest.csv",
    ]

    assert (
        staged.validate(
            allowed,
            price_history_high_water_date="20260728",
        )
        == []
    )


def test_legacy_mode_keeps_raw_price_history_paths_allowlisted() -> None:
    assert staged.validate(
        [
            "data/daily_price/daily_price_20260720.csv",
            "data/stock_price_history/2330.csv",
            "output/latest/stock_price_history_manifest.json",
        ],
        price_history_high_water_date="",
    ) == []
