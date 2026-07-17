from __future__ import annotations

import csv
from pathlib import Path
import re
import subprocess

import yaml

from scripts.build_daily_candidate_model_layer import MODEL_SCORE_PROFILES
from scripts.validate_daily_warrant_formal_sync_scope import (
    ALLOWED_MUTABLE_MODEL_IDS,
    ALL_CANDIDATES_ARTIFACT,
    FORMAL_SIGNAL_ARTIFACTS,
    FRONTPAGE_UNIQUE_ARTIFACT,
    LATEST_SIGNAL_ARTIFACTS,
    MODEL_PARAMETERS_ARTIFACT,
    WARRANT_CANDIDATE_FIELDS,
    WARRANT_BONUS_BY_MODEL,
    WARRANT_FLOW_ARTIFACT,
    VOLUME_BREAKOUT_WATCH_ARTIFACT,
    STOCK_THEME_TAXONOMY_ARTIFACT,
    WARRANT_SOURCE_TO_CANDIDATE_FIELDS,
    BULLISH_WARRANT_SIGNALS,
    build_scope_snapshot,
    compare_scope_snapshots,
    validate_current_projection,
    validate_frontpage_uniqueness,
    validate_model_rank_contract,
    validate_staged_path_list,
    validate_warrant_bonus_parameter_contract,
)


ROOT = Path(__file__).resolve().parents[1]


def _write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def _read_csv_fixture(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        return columns, [
            {column: str(row.get(column) or "").strip() for column in columns}
            for row in reader
        ]


def _copy_tracked_artifact(relative_path: str, destination_root: Path) -> None:
    result = subprocess.run(
        ["git", "show", f"HEAD:{relative_path}"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    destination = destination_root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(result.stdout)


def _candidate_rows() -> list[dict[str, str]]:
    rows = [
        {"date": "20260716", "source_row_index": "1", "stock_id": "2330", "industry": "semi"},
        {"date": "20260716", "source_row_index": "2", "stock_id": "1234", "industry": "other"},
        {"date": "20260716", "source_row_index": "3", "stock_id": "5678", "industry": "other"},
        {"date": "20260716", "source_row_index": "4", "stock_id": "9012", "industry": "other"},
    ]
    signals = ["call_inflow", "no_signal", "call_inflow", "no_signal"]
    for row, signal in zip(rows, signals, strict=True):
        for column in WARRANT_CANDIDATE_FIELDS:
            row[column] = ""
        row["warrant_flow_signal"] = signal
    return rows


def _signal_rows() -> list[dict[str, str]]:
    return [
        {
            "signal_date": "20260716",
            "report_line": "mainstream",
            "source_row_index": "1",
            "stock_id": "2330",
            "model_id": "revenue_unreacted_range",
            "model_score": "87",
            "model_rank": "1",
            "warrant_flow_signal": "call_inflow",
        },
        {
            "signal_date": "20260716",
            "report_line": "mainstream",
            "source_row_index": "volume_breakout:0",
            "stock_id": "1234",
            "model_id": "volume_range_breakout_v2_high_position_volume_attack",
            "model_score": "70",
            "model_rank": "1",
            "warrant_flow_signal": "no_signal",
        },
        {
            "signal_date": "20260716",
            "report_line": "mainstream",
            "source_row_index": "3",
            "stock_id": "5678",
            "model_id": "w_bottom_right_side",
            "model_score": "88",
            "model_rank": "1",
            "warrant_flow_signal": "call_inflow",
        },
        {
            "signal_date": "20260716",
            "report_line": "mainstream",
            "source_row_index": "4",
            "stock_id": "9012",
            "model_id": "price_pullback_23ema",
            "model_score": "70",
            "model_rank": "1",
            "warrant_flow_signal": "no_signal",
        },
    ]


def _write_artifacts(root: Path, rows: list[dict[str, str]]) -> None:
    candidate_rows = _candidate_rows()
    _write_csv(root / ALL_CANDIDATES_ARTIFACT, list(candidate_rows[0]), candidate_rows)
    warrant_rows = [
        {
            "date": row["date"],
            "stock_id": row["stock_id"],
            "warrant_flow_signal": row["warrant_flow_signal"],
            "warrant_flow_score": row["warrant_flow_score"],
            "warrant_flow_warning": row["warrant_flow_warning"],
            "call_turnover": row["call_turnover"],
            "put_turnover": row["put_turnover"],
            "call_put_turnover_ratio": row["call_put_turnover_ratio"],
            "call_turnover_change_1d": row["call_turnover_change_1d"],
            "call_turnover_change_5d": row["call_turnover_change_5d"],
            "low_float_call_spike_count": row["low_float_call_spike_count"],
            "top_issuer": row["top_issuer"],
            "note": row["warrant_note"],
        }
        for row in candidate_rows
    ]
    _write_csv(
        root / WARRANT_FLOW_ARTIFACT,
        list(warrant_rows[0]),
        warrant_rows,
    )
    synthetic_rows: dict[int, dict[str, str]] = {}
    taxonomy_rows: dict[str, dict[str, str]] = {}
    for row in rows:
        match = re.fullmatch(r"volume_breakout:([0-9]+)", row.get("source_row_index", ""))
        if not match:
            continue
        index = int(match.group(1))
        stock_id = row["stock_id"]
        synthetic_rows[index] = {
            "stock_id": stock_id,
            "selection_status": "selected",
            "volume_breakout_type": "bottom_volume_attack",
        }
        taxonomy_rows[stock_id] = {
            "stock_id": stock_id,
            "industry": "fixture_industry",
        }
    watch_rows = [
        {
            "stock_id": "",
            "selection_status": "not_selected",
            "volume_breakout_type": "",
        }
        for _ in range(max(synthetic_rows, default=-1) + 1)
    ]
    for index, row in synthetic_rows.items():
        watch_rows[index] = row
    _write_csv(
        root / VOLUME_BREAKOUT_WATCH_ARTIFACT,
        ["stock_id", "selection_status", "volume_breakout_type"],
        watch_rows,
    )
    _write_csv(
        root / STOCK_THEME_TAXONOMY_ARTIFACT,
        ["stock_id", "industry"],
        list(taxonomy_rows.values()),
    )
    raw_signal_columns = [
        "signal_date",
        "report_bucket",
        "report_line",
        "source_row_index",
        "stock_id",
        "model_id",
        "model_group",
        "model_score",
        "model_rank",
        "base_model_score",
        "final_rank_score",
        "score_components",
        "warrant_flow_signal",
    ]
    signal_rows = []
    for row in rows:
        signal_row = dict(row)
        signal_row.setdefault("report_bucket", signal_row["report_line"])
        signal_row.setdefault("model_group", "pdf_core_model")
        signal_row.setdefault("same_model_repeat_status", "new_model_signal")
        signal_row.setdefault("same_model_consecutive_days", "1")
        signal_row.setdefault("same_model_appear_count_10d", "1")
        signal_row.setdefault("base_model_score", signal_row["model_score"])
        signal_row.setdefault("final_rank_score", signal_row["model_score"])
        bonus = WARRANT_BONUS_BY_MODEL.get(signal_row["model_id"])
        signal = signal_row.get("warrant_flow_signal", "")
        signal_row.setdefault(
            "score_components",
            f"warrant bullish +{bonus}"
            if bonus and signal in BULLISH_WARRANT_SIGNALS
            else "",
        )
        signal_rows.append(signal_row)

    winner_indexes: set[int] = set()
    grouped: dict[tuple[str, str], list[int]] = {}
    for index, row in enumerate(signal_rows):
        if (
            row["model_group"] == "pdf_core_model"
            and row["same_model_repeat_status"] != "repeated_same_model_signal"
        ):
            grouped.setdefault((row["report_bucket"], row["stock_id"]), []).append(index)
    for indexes in grouped.values():
        winner_indexes.add(
            sorted(
                indexes,
                key=lambda index: (
                    -float(signal_rows[index]["model_score"]),
                    float(signal_rows[index]["model_rank"]),
                    signal_rows[index]["model_id"],
                ),
            )[0]
        )
    for index, signal_row in enumerate(signal_rows):
        if signal_row["same_model_repeat_status"] == "repeated_same_model_signal":
            expected_allowed = "False"
            expected_reason = "same_model_repeat_moved_to_persistence_table"
            expected_reason_zh = "同模型重複進榜，移至延續表"
        elif signal_row["model_group"] != "pdf_core_model":
            expected_allowed = "False"
            expected_reason = "not_pdf_core_model"
            expected_reason_zh = "非PDF核心模型"
        elif index in winner_indexes:
            expected_allowed = "True"
            expected_reason = ""
            expected_reason_zh = ""
        else:
            expected_allowed = "False"
            expected_reason = "duplicate_stock_already_shown_on_frontpage"
            expected_reason_zh = "首頁已列示"
        signal_row.setdefault("frontpage_display_allowed", expected_allowed)
        signal_row.setdefault("frontpage_duplicate_reason", expected_reason)
        signal_row.setdefault("frontpage_duplicate_reason_zh", expected_reason_zh)

    status_groups: dict[tuple[str, str, str], list[int]] = {}
    for index, signal_row in enumerate(signal_rows):
        status_groups.setdefault(
            (
                signal_row["report_bucket"],
                signal_row["model_id"],
                signal_row["same_model_repeat_status"],
            ),
            [],
        ).append(index)
    for (bucket, model_id, status), indexes in status_groups.items():
        if status == "new_model_signal":
            ordered = sorted(
                indexes,
                key=lambda index: (
                    -float(signal_rows[index]["model_score"]),
                    float(signal_rows[index]["model_rank"]),
                    signal_rows[index]["stock_id"],
                ),
            )
            for rank, index in enumerate(ordered, start=1):
                signal_rows[index].setdefault("model_rank_new_signal", str(rank))
                signal_rows[index].setdefault("display_rank_new_signal", f"新進榜 #{rank}")
        elif status == "repeated_same_model_signal":
            ordered = sorted(
                indexes,
                key=lambda index: (
                    -float(signal_rows[index]["same_model_consecutive_days"]),
                    -float(signal_rows[index]["same_model_appear_count_10d"]),
                    -float(signal_rows[index]["model_score"]),
                    float(signal_rows[index]["model_rank"]),
                    signal_rows[index]["stock_id"],
                ),
            )
            for rank, index in enumerate(ordered, start=1):
                signal_rows[index].setdefault("model_rank_repeated_signal", str(rank))
                signal_rows[index].setdefault("display_rank_repeated_signal", f"連續榜 #{rank}")
    for signal_row in signal_rows:
        signal_row.setdefault("display_rank", signal_row["model_rank"])
        signal_row.setdefault("model_rank_overall", signal_row["model_rank"])
        signal_row.setdefault("model_rank_new_signal", "")
        signal_row.setdefault("model_rank_repeated_signal", "")
        signal_row.setdefault("display_rank_new_signal", "")
        signal_row.setdefault("display_rank_repeated_signal", "")

    _write_csv(
        root / LATEST_SIGNAL_ARTIFACTS[0],
        raw_signal_columns,
        [
            {column: row.get(column, "") for column in raw_signal_columns}
            for row in signal_rows
        ],
    )
    report_signal_columns = [
        *raw_signal_columns,
        "display_rank",
        "same_model_consecutive_days",
        "same_model_appear_count_10d",
        "same_model_repeat_status",
        "model_rank_overall",
        "model_rank_new_signal",
        "model_rank_repeated_signal",
        "display_rank_new_signal",
        "display_rank_repeated_signal",
        "frontpage_display_allowed",
        "frontpage_duplicate_reason",
        "frontpage_duplicate_reason_zh",
    ]
    _write_csv(
        root / LATEST_SIGNAL_ARTIFACTS[1],
        report_signal_columns,
        [
            {column: row.get(column, "") for column in report_signal_columns}
            for row in signal_rows
        ],
    )

    frontpage_rows = [
        {
            "signal_date": signal_rows[index]["signal_date"],
            "report_bucket": signal_rows[index]["report_bucket"],
            "stock_id": signal_rows[index]["stock_id"],
            "primary_model_id": signal_rows[index]["model_id"],
            "primary_model_score": signal_rows[index]["model_score"],
            "primary_model_rank": signal_rows[index]["model_rank"],
        }
        for index in sorted(winner_indexes)
    ]
    _write_csv(
        root / FRONTPAGE_UNIQUE_ARTIFACT,
        [
            "signal_date",
            "report_bucket",
            "stock_id",
            "primary_model_id",
            "primary_model_score",
            "primary_model_rank",
        ],
        frontpage_rows,
    )
    history_columns = [
        "signal_date",
        "report_bucket",
        "stock_id",
        "model_id",
        "base_model_score",
        "final_rank_score",
        "model_score",
        "model_rank",
    ]
    history_rows = [
        {
            "signal_date": row["signal_date"],
            "report_bucket": row.get("report_bucket", row["report_line"]),
            "stock_id": row["stock_id"],
            "model_id": row["model_id"],
            "base_model_score": row["model_score"],
            "final_rank_score": row["model_score"],
            "model_score": row["model_score"],
            "model_rank": row["model_rank"],
        }
        for row in rows
    ]
    _write_csv(root / FORMAL_SIGNAL_ARTIFACTS[2], history_columns, history_rows)
    parameter_rows = [
        {"model_id": model_id, "warrant_bullish_bonus": bonus}
        for model_id, bonus in WARRANT_BONUS_BY_MODEL.items()
    ]
    parameter_rows.extend(
        [
            {"model_id": "price_pullback_23ema", "warrant_bullish_bonus": "0"},
            {
                "model_id": "volume_range_breakout_v2_high_position_volume_attack",
                "warrant_bullish_bonus": "0",
            },
        ]
    )
    _write_csv(
        root / MODEL_PARAMETERS_ARTIFACT,
        ["model_id", "warrant_bullish_bonus"],
        parameter_rows,
    )


def test_mutable_scope_matches_nonzero_warrant_score_profiles() -> None:
    nonzero_profiles = {
        model_id
        for model_id, profile in MODEL_SCORE_PROFILES.items()
        if profile.warrant_bullish_bonus != 0
    }
    assert ALLOWED_MUTABLE_MODEL_IDS == nonzero_profiles
    assert "volume_range_breakout_v2_high_position_volume_attack" not in nonzero_profiles
    assert "price_pullback_23ema" not in nonzero_profiles


def test_tracked_formal_artifacts_match_real_scope_contract(
    tmp_path: Path,
) -> None:
    for relative_path in (
        ALL_CANDIDATES_ARTIFACT,
        MODEL_PARAMETERS_ARTIFACT,
        *FORMAL_SIGNAL_ARTIFACTS,
    ):
        _copy_tracked_artifact(relative_path, tmp_path)

    snapshot, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert snapshot["artifact_count"] == 1 + len(FORMAL_SIGNAL_ARTIFACTS)
    assert validate_warrant_bonus_parameter_contract(tmp_path) == []


def test_tracked_formal_rank_and_frontpage_contract(tmp_path: Path) -> None:
    for relative_path in (*LATEST_SIGNAL_ARTIFACTS, FRONTPAGE_UNIQUE_ARTIFACT):
        _copy_tracked_artifact(relative_path, tmp_path)

    raw_columns, raw_rows = _read_csv_fixture(tmp_path / LATEST_SIGNAL_ARTIFACTS[0])
    report_columns, report_rows = _read_csv_fixture(
        tmp_path / LATEST_SIGNAL_ARTIFACTS[1]
    )

    assert validate_model_rank_contract(
        raw_columns,
        raw_rows,
        LATEST_SIGNAL_ARTIFACTS[0],
        report_artifact=False,
    ) == []
    assert validate_model_rank_contract(
        report_columns,
        report_rows,
        LATEST_SIGNAL_ARTIFACTS[1],
        report_artifact=True,
    ) == []
    assert validate_frontpage_uniqueness(
        tmp_path,
        report_columns,
        report_rows,
    ) == []


def test_scope_allows_only_warrant_affected_model_changes(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[0]["warrant_flow_signal"] = "no_signal"
    after_rows[0]["model_score"] = "84"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert compare_scope_snapshots(before, after) == []
    assert before["aggregate_sha256"] == after["aggregate_sha256"]


def test_scope_rejects_same_warrant_state_score_drift_across_all_artifacts(
    tmp_path: Path,
) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[0]["model_score"] = "99"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert any(
        "warrant score delta mismatch" in error
        for error in compare_scope_snapshots(before, after)
    )


def test_scope_rejects_wrong_exact_bullish_bonus_delta(tmp_path: Path) -> None:
    rows = _signal_rows()
    rows[0]["warrant_flow_signal"] = "no_signal"
    rows[0]["model_score"] = "84"
    _write_artifacts(tmp_path, rows)
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[0]["model_score"] = "86.9"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert any(
        "warrant score delta mismatch" in error
        for error in compare_scope_snapshots(before, after)
    )


def test_scope_fails_closed_at_unprovable_lower_clamp_boundary(tmp_path: Path) -> None:
    rows = _signal_rows()
    rows[0]["warrant_flow_signal"] = "no_signal"
    rows[0]["model_score"] = "0"
    _write_artifacts(tmp_path, rows)
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[0]["model_score"] = "3"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert any(
        "not provable across lower clamp boundary" in error
        for error in compare_scope_snapshots(before, after)
    )


def test_scope_fails_closed_at_unprovable_upper_clamp_boundary(tmp_path: Path) -> None:
    rows = _signal_rows()
    rows[0]["model_score"] = "100"
    _write_artifacts(tmp_path, rows)
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[0]["warrant_flow_signal"] = "no_signal"
    after_rows[0]["model_score"] = "97"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert any(
        "not provable across upper clamp boundary" in error
        for error in compare_scope_snapshots(before, after)
    )


def test_scope_rejects_non_warrant_score_component_drift(tmp_path: Path) -> None:
    rows = _signal_rows()
    rows[0]["score_components"] = "base=50 | warrant bullish +3 | revenue strong +12"
    _write_artifacts(tmp_path, rows)
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[0]["score_components"] = "base=99 | warrant bullish +3 | revenue strong +12"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert any(
        "formal signal non-warrant semantic hash drift" in error
        or "non-warrant score components drift" in error
        for error in compare_scope_snapshots(before, after)
    )


def test_scope_fails_when_warrant_independent_model_changes(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[1]["model_score"] = "71"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    compare_errors = compare_scope_snapshots(before, after)
    assert len(compare_errors) == len(FORMAL_SIGNAL_ARTIFACTS)
    assert all("formal signal non-warrant semantic hash drift" in error for error in compare_errors)


def test_scope_allows_warrant_presentation_change_for_bonus_zero_model(
    tmp_path: Path,
) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[1]["warrant_flow_signal"] = "call_inflow"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert compare_scope_snapshots(before, after) == []


def test_scope_allows_frontpage_representative_cascade_for_bonus_zero_model(
    tmp_path: Path,
) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[3]["frontpage_display_allowed"] = "False"
    after_rows[3]["frontpage_duplicate_reason"] = "duplicate_stock_already_shown_on_frontpage"
    after_rows[3]["frontpage_duplicate_reason_zh"] = "首頁已列過同股票代表"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert compare_scope_snapshots(before, after) == []


def test_scope_fails_when_formal_signal_identity_membership_changes(
    tmp_path: Path,
) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    after_rows = _signal_rows()
    after_rows[0]["stock_id"] = "2331"
    _write_artifacts(tmp_path, after_rows)
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    compare_errors = compare_scope_snapshots(before, after)
    identity_errors = [
        error for error in compare_errors if "formal signal identity membership drift" in error
    ]
    assert len(identity_errors) == len(FORMAL_SIGNAL_ARTIFACTS)


def test_scope_protects_prior_date_score_history_for_mutable_model(
    tmp_path: Path,
) -> None:
    rows = _signal_rows()
    _write_artifacts(tmp_path, rows)
    history_path = tmp_path / FORMAL_SIGNAL_ARTIFACTS[2]
    history_columns = [
        "signal_date",
        "report_bucket",
        "stock_id",
        "model_id",
        "base_model_score",
        "final_rank_score",
        "model_score",
        "model_rank",
    ]
    prior_row = {
        "signal_date": "20260715",
        "report_bucket": "mainstream",
        "stock_id": "2330",
        "model_id": "revenue_unreacted_range",
        "base_model_score": "82",
        "final_rank_score": "82",
        "model_score": "82",
        "model_rank": "1",
    }
    current_history = [
        {
            "signal_date": row["signal_date"],
            "report_bucket": row["report_line"],
            "stock_id": row["stock_id"],
            "model_id": row["model_id"],
            "base_model_score": row["model_score"],
            "final_rank_score": row["model_score"],
            "model_score": row["model_score"],
            "model_rank": row["model_rank"],
        }
        for row in rows
    ]
    _write_csv(history_path, history_columns, [prior_row, *current_history])
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    prior_row["model_score"] = "99"
    _write_csv(history_path, history_columns, [prior_row, *current_history])
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert any(
        "formal signal non-warrant semantic hash drift" in error
        for error in compare_scope_snapshots(before, after)
    )


def test_scope_protects_prior_date_warrant_presentation_history(
    tmp_path: Path,
) -> None:
    rows = _signal_rows()
    _write_artifacts(tmp_path, rows)
    history_path = tmp_path / FORMAL_SIGNAL_ARTIFACTS[2]
    history_columns = [
        "signal_date",
        "report_bucket",
        "stock_id",
        "model_id",
        "base_model_score",
        "final_rank_score",
        "model_score",
        "model_rank",
        "warrant_flow_signal",
        "why_selected_human_zh",
    ]
    prior_row = {
        "signal_date": "20260715",
        "report_bucket": "mainstream",
        "stock_id": "2330",
        "model_id": "revenue_unreacted_range",
        "base_model_score": "82",
        "final_rank_score": "82",
        "model_score": "82",
        "model_rank": "1",
        "warrant_flow_signal": "no_signal",
        "why_selected_human_zh": "歷史正式理由",
    }
    current_history = [
        {
            "signal_date": row["signal_date"],
            "report_bucket": row["report_line"],
            "stock_id": row["stock_id"],
            "model_id": row["model_id"],
            "base_model_score": row["model_score"],
            "final_rank_score": row["model_score"],
            "model_score": row["model_score"],
            "model_rank": row["model_rank"],
            "warrant_flow_signal": row["warrant_flow_signal"],
            "why_selected_human_zh": "目前正式理由",
        }
        for row in rows
    ]
    _write_csv(history_path, history_columns, [prior_row, *current_history])
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    prior_row["warrant_flow_signal"] = "call_inflow"
    prior_row["why_selected_human_zh"] = "遭改寫的歷史理由"
    _write_csv(history_path, history_columns, [prior_row, *current_history])
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert any(
        "formal signal non-warrant semantic hash drift" in error
        for error in compare_scope_snapshots(before, after)
    )


def test_candidate_scope_allows_only_warrant_columns(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    candidate_rows = _candidate_rows()
    candidate_rows[0]["warrant_flow_score"] = "3"
    _write_csv(
        tmp_path / ALL_CANDIDATES_ARTIFACT,
        list(candidate_rows[0]),
        candidate_rows,
    )
    warrant_after, errors = build_scope_snapshot(tmp_path)
    assert errors == []
    assert compare_scope_snapshots(before, warrant_after) == []

    candidate_rows[0]["industry"] = "changed"
    _write_csv(
        tmp_path / ALL_CANDIDATES_ARTIFACT,
        list(candidate_rows[0]),
        candidate_rows,
    )
    non_warrant_after, errors = build_scope_snapshot(tmp_path)
    assert errors == []
    assert "all_candidates non-warrant content drift" in compare_scope_snapshots(
        before, non_warrant_after
    )


def test_projection_requires_candidate_raw_and_report_consistency(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    errors, metrics = validate_current_projection(tmp_path)

    assert errors == []
    assert metrics == {
        "candidate_rows": 4,
        "warrant_rows": 4,
        "raw_signal_rows": 4,
        "report_signal_rows": 4,
        "history_signal_rows": 4,
    }

    report_path = tmp_path / LATEST_SIGNAL_ARTIFACTS[1]
    report_rows = _signal_rows()
    report_rows[0]["warrant_flow_signal"] = "put_inflow"
    _write_csv(
        report_path,
        list(report_rows[0]),
        report_rows,
    )

    errors, _ = validate_current_projection(tmp_path)
    assert any("warrant projection mismatch" in error for error in errors)
    assert any("raw/report warrant formal sync mismatch" in error for error in errors)


def test_projection_allows_volume_v2_without_candidate_only_for_empty_official_projection(
    tmp_path: Path,
) -> None:
    rows = _signal_rows()
    rows[1]["source_row_index"] = "volume_breakout:999"
    rows[1]["stock_id"] = "9999"
    rows[1]["warrant_flow_signal"] = ""
    _write_artifacts(tmp_path, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert errors == []


def test_projection_rejects_volume_v2_without_candidate_when_official_warrant_exists(
    tmp_path: Path,
) -> None:
    rows = _signal_rows()
    rows[1]["source_row_index"] = "volume_breakout:999"
    rows[1]["stock_id"] = "9999"
    rows[1]["warrant_flow_signal"] = ""
    _write_artifacts(tmp_path, rows)

    warrant_path = tmp_path / WARRANT_FLOW_ARTIFACT
    columns, warrant_rows = _read_csv_fixture(warrant_path)
    official = {column: "" for column in columns}
    official.update(
        {
            "date": "20260716",
            "stock_id": "9999",
            "warrant_flow_signal": "call_inflow",
        }
    )
    _write_csv(warrant_path, columns, [*warrant_rows, official])

    errors, _ = validate_current_projection(tmp_path)

    assert any(
        "formal signal warrant projection mismatch" in error
        and "volume_range_breakout_v2_high_position_volume_attack" in error
        and "expected='call_inflow' actual=''" in error
        for error in errors
    )


def test_projection_rejects_volume_v2_without_candidate_or_taxonomy_lineage(
    tmp_path: Path,
) -> None:
    rows = _signal_rows()
    rows[1]["source_row_index"] = "volume_breakout:999"
    rows[1]["stock_id"] = "9999"
    rows[1]["warrant_flow_signal"] = ""
    _write_artifacts(tmp_path, rows)
    _write_csv(
        tmp_path / STOCK_THEME_TAXONOMY_ARTIFACT,
        ["stock_id", "industry"],
        [],
    )

    errors, _ = validate_current_projection(tmp_path)

    assert any(
        "formal volume signal has no canonical taxonomy lineage" in error
        and "volume_range_breakout_v2_high_position_volume_attack" in error
        for error in errors
    )


def test_projection_rejects_duplicate_volume_taxonomy_identity(tmp_path: Path) -> None:
    rows = _signal_rows()
    rows[1]["source_row_index"] = "volume_breakout:999"
    rows[1]["stock_id"] = "9999"
    rows[1]["warrant_flow_signal"] = ""
    _write_artifacts(tmp_path, rows)
    _write_csv(
        tmp_path / STOCK_THEME_TAXONOMY_ARTIFACT,
        ["stock_id", "industry"],
        [
            {"stock_id": "9999", "industry": "fixture_a"},
            {"stock_id": "9999", "industry": "fixture_b"},
        ],
    )

    errors, _ = validate_current_projection(tmp_path)

    assert any(
        "canonical taxonomy artifact has duplicate normalized stock_id: 9999" in error
        for error in errors
    )


def test_projection_rejects_volume_v2_non_synthetic_source_key_fallback(
    tmp_path: Path,
) -> None:
    rows = _signal_rows()
    rows[1]["source_row_index"] = "stale-general-source"
    _write_artifacts(tmp_path, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any(
        "formal signal row has no all_candidates warrant source" in error
        and "stale-general-source" in error
        for error in errors
    )


def test_projection_rejects_candidate_warrant_drift_from_official_source(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    candidate_rows = _candidate_rows()
    candidate_rows[0]["warrant_flow_signal"] = "put_inflow"
    _write_csv(
        tmp_path / ALL_CANDIDATES_ARTIFACT,
        list(candidate_rows[0]),
        candidate_rows,
    )

    errors, _ = validate_current_projection(tmp_path)

    assert any("all_candidates warrant projection mismatch" in error for error in errors)


def test_projection_rejects_empty_official_projection(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    warrant_columns = ["date", "stock_id", *WARRANT_SOURCE_TO_CANDIDATE_FIELDS]
    _write_csv(
        tmp_path / WARRANT_FLOW_ARTIFACT,
        warrant_columns,
        [],
    )

    errors, _ = validate_current_projection(tmp_path)

    assert "official warrant projection has no rows" in errors
    assert any(
        "official warrant projection must have exactly one valid date" in error
        for error in errors
    )


def test_projection_rejects_missing_candidate_formal_date(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    candidate_rows = _candidate_rows()
    for row in candidate_rows:
        row["date"] = ""
    _write_csv(
        tmp_path / ALL_CANDIDATES_ARTIFACT,
        list(candidate_rows[0]),
        candidate_rows,
    )

    errors, _ = validate_current_projection(tmp_path)

    assert any(
        "all_candidates must have exactly one valid formal date" in error
        for error in errors
    )


def test_projection_rejects_non_signal_warrant_field_drift(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    candidate_rows = _candidate_rows()
    candidate_rows[0]["call_turnover"] = "999"
    _write_csv(
        tmp_path / ALL_CANDIDATES_ARTIFACT,
        list(candidate_rows[0]),
        candidate_rows,
    )

    errors, _ = validate_current_projection(tmp_path)

    assert any(
        "all_candidates warrant projection mismatch" in error
        and "column=call_turnover" in error
        for error in errors
    )


def test_projection_rejects_wrong_warrant_bonus_marker(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    raw_path = tmp_path / LATEST_SIGNAL_ARTIFACTS[0]
    with raw_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        rows = list(reader)
    rows[0]["score_components"] = "warrant bullish +5"
    _write_csv(raw_path, columns, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any("formal signal warrant bonus marker mismatch" in error for error in errors)


def test_projection_rejects_warrant_bonus_parameter_drift(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    parameter_path = tmp_path / MODEL_PARAMETERS_ARTIFACT
    with parameter_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        rows = list(reader)
    for row in rows:
        if row["model_id"] == "revenue_unreacted_range":
            row["warrant_bullish_bonus"] = "4"
    _write_csv(parameter_path, columns, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any("formal model warrant bonus parameter mismatch" in error for error in errors)


def test_projection_rejects_wrong_frontpage_representative_fields(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    report_path = tmp_path / LATEST_SIGNAL_ARTIFACTS[1]
    with report_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        rows = list(reader)
    rows[0]["frontpage_display_allowed"] = "False"
    rows[0]["frontpage_duplicate_reason"] = "duplicate_stock_already_shown_on_frontpage"
    rows[0]["frontpage_duplicate_reason_zh"] = "首頁已列示"
    _write_csv(report_path, columns, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any("report frontpage representative mismatch" in error for error in errors)


def test_projection_rejects_frontpage_consumer_primary_model_drift(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    frontpage_path = tmp_path / FRONTPAGE_UNIQUE_ARTIFACT
    with frontpage_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        rows = list(reader)
    rows[0]["primary_model_id"] = "wrong_model"
    _write_csv(frontpage_path, columns, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any("frontpage consumer primary model mismatch" in error for error in errors)


def test_projection_rejects_synchronized_wrong_model_rank(tmp_path: Path) -> None:
    rows = _signal_rows()
    rows[0]["model_rank"] = "2"
    _write_artifacts(tmp_path, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any("formal model rank mismatch" in error for error in errors)


def test_projection_normalizes_equivalent_numeric_warrant_fields(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    candidate_rows = _candidate_rows()
    candidate_rows[0]["warrant_flow_score"] = "2"
    _write_csv(
        tmp_path / ALL_CANDIDATES_ARTIFACT,
        list(candidate_rows[0]),
        candidate_rows,
    )
    warrant_path = tmp_path / WARRANT_FLOW_ARTIFACT
    with warrant_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        warrant_columns = list(reader.fieldnames or [])
        warrant_rows = list(reader)
    warrant_rows[0]["warrant_flow_score"] = "2.0"
    _write_csv(warrant_path, warrant_columns, warrant_rows)

    errors, _ = validate_current_projection(tmp_path)

    assert errors == []


def test_projection_rejects_conflicting_same_stock_candidate_warrant(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    candidate_rows = _candidate_rows()
    conflicting = dict(candidate_rows[1])
    conflicting["source_row_index"] = "5"
    conflicting["warrant_flow_signal"] = "call_inflow"
    candidate_rows.append(conflicting)
    _write_csv(
        tmp_path / ALL_CANDIDATES_ARTIFACT,
        list(candidate_rows[0]),
        candidate_rows,
    )

    errors, _ = validate_current_projection(tmp_path)

    assert any("inconsistent warrant signals for stock_id=1234" in error for error in errors)


def test_projection_rejects_current_history_score_drift(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    history_path = tmp_path / FORMAL_SIGNAL_ARTIFACTS[2]
    with history_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        rows = list(reader)
    rows[0]["model_score"] = "999"
    _write_csv(history_path, columns, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any("report/history formal signal mismatch" in error for error in errors)


def test_projection_rejects_raw_report_final_rank_score_drift(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    report_path = tmp_path / LATEST_SIGNAL_ARTIFACTS[1]
    with report_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        rows = list(reader)
    rows[0]["final_rank_score"] = "999"
    _write_csv(report_path, columns, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any(
        "raw/report warrant formal sync mismatch" in error
        and "column=final_rank_score" in error
        for error in errors
    )


def test_projection_rejects_formal_signal_date_mismatch(tmp_path: Path) -> None:
    rows = _signal_rows()
    for row in rows:
        row["signal_date"] = "20260715"
    _write_artifacts(tmp_path, rows)

    errors, _ = validate_current_projection(tmp_path)

    assert any(
        "raw formal signals date must equal formal warrant/candidate date 20260716"
        in error
        for error in errors
    )
    assert any(
        "report formal signals date must equal formal warrant/candidate date 20260716"
        in error
        for error in errors
    )


def test_warrant_formal_sync_staged_paths_are_positive_allowlisted() -> None:
    assert validate_staged_path_list(
        [
            "output/latest/warrant_flow_latest.csv",
            "output/history/daily_model_snapshots/data_freshness_20260716.csv",
            "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv",
            "docs/latest/daily_candidate_model_signals_latest.csv",
        ]
    ) == []

    errors = validate_staged_path_list(
        [
            "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
            "output/history/daily_model_snapshots/daily_w_bottom_right_side_operation_section_20260716.csv",
            "output/latest/research_backtest/volume_range_breakout_v2_research_latest.csv",
        ]
    )
    assert len(errors) == 3
    assert all("outside allowlist" in error for error in errors)


def test_scope_is_order_independent_for_protected_rows(tmp_path: Path) -> None:
    _write_artifacts(tmp_path, _signal_rows())
    before, errors = build_scope_snapshot(tmp_path)
    assert errors == []

    _write_artifacts(tmp_path, list(reversed(_signal_rows())))
    after, errors = build_scope_snapshot(tmp_path)

    assert errors == []
    assert compare_scope_snapshots(before, after) == []


def test_warrant_workflow_rebuilds_formal_consumers_and_fails_closed() -> None:
    workflow = (ROOT / ".github" / "workflows" / "warrant_flow.yml").read_text(
        encoding="utf-8"
    )
    parsed_workflow = yaml.safe_load(workflow)

    assert parsed_workflow["name"] == "Warrant Flow"
    assert "group: daily-full-pipeline-${{ github.ref }}" in workflow
    assert "cancel-in-progress: false" in workflow
    assert "fetch-depth: 0" in workflow
    assert "ref: main" in workflow
    assert "Enforce main-only mutation" in workflow
    assert "refs/heads/main" in workflow
    assert "REQUESTED_DATE: ${{ github.event.inputs.date || '' }}" in workflow
    assert '[[ ! "$REQUESTED_DATE" =~ ^[0-9]{8}$ ]]' in workflow
    assert '--date "${{ github.event.inputs.date }}"' not in workflow
    assert "python scripts/validate_daily_warrant_formal_sync_scope.py" in workflow
    assert '--write-snapshot "$warrant_formal_sync_scope_before"' in workflow
    assert '--compare-snapshot "$warrant_formal_sync_scope_before"' in workflow
    assert 'capture_mature_sentinels "$mature_sentinel_before"' in workflow
    assert 'capture_mature_sentinels "$mature_sentinel_after"' in workflow
    assert 'cmp --silent "$mature_sentinel_before" "$mature_sentinel_after"' in workflow
    for protected_static_artifact in (
        "output/latest/daily_candidate_model_parameters_latest.csv",
        "output/latest/daily_candidate_model_parameters_latest.md",
        "docs/latest/daily_candidate_model_parameters_latest.csv",
        "docs/latest/daily_candidate_model_parameters_latest.md",
        "output/latest/daily_report_model_registry_latest.csv",
        "output/latest/daily_report_model_registry_latest.md",
        "docs/latest/daily_report_model_registry_latest.csv",
        "docs/latest/daily_report_model_registry_latest.md",
    ):
        assert protected_static_artifact in workflow
    assert "python scripts/validate_warrant_source_status.py" in workflow
    assert "validate_warrant_source_status.py --allow-noncritical-grace" not in workflow
    assert "fetch_official_warrant_daily.py --require-current-usable" in workflow
    assert "--require-formal-current" in workflow
    for artifact_id in (
        "data_freshness",
        "model_signals_for_report",
        "all_candidates_source_rows",
        "model_summary_for_report",
    ):
        assert f"--artifact-id {artifact_id}" in workflow
    assert "daily_volume_breakout_operation_section_*.csv" in workflow
    assert "manifest:" in workflow

    expected_order = [
        "python merge_warrant_flow_into_candidates.py",
        "python build_data_freshness_latest.py",
        "python scripts/validate_data_freshness_latest.py",
        "python scripts/build_daily_candidate_model_layer.py",
        "python scripts/validate_daily_candidate_model_layer.py",
        "python scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py",
        "python scripts/build_daily_report_model_summary.py",
        "python scripts/audit_daily_candidate_model_selection_correctness.py",
        "python scripts/audit_daily_candidate_pipeline_integrity.py",
        "python scripts/build_theme_event_watch.py",
        "python scripts/update_daily_published_model_snapshots.py",
        "python scripts/validate_daily_published_model_snapshots.py",
        "python scripts/build_chatgpt_indicator_usage_guide.py",
    ]
    indexes = [workflow.index(command) for command in expected_order]
    assert indexes == sorted(indexes)

    for forbidden_builder in (
        "build_approved_operation_patterns.py",
        "build_daily_volume_breakout_operation_section.py",
        "build_daily_w_bottom_operation_sections.py",
        "build_daily_neckline_volume_breakout_confirmation_operation_section.py",
        "build_daily_price_pullback_23ema_operation_section.py",
        "build_model_operation_readiness.py",
    ):
        assert forbidden_builder not in workflow

    commit_block = workflow[
        workflow.index("- name: Commit warrant flow and formal sync outputs") :
        workflow.index("- name: Dispatch and wait for warrant Pages deploy")
    ]
    assert "if git diff --cached --quiet; then" in commit_block
    assert 'git commit -m "Update official warrant flow and formal model sync"' in commit_block
    assert 'git commit -m "Update official warrant flow and formal model sync" ||' not in commit_block
    assert "bash scripts/ci_push_with_retry.sh" not in commit_block
    assert "git fetch origin main" in commit_block
    assert 'current_origin_main="$(git rev-parse origin/main)"' in commit_block
    assert 'if [ "$current_origin_main" != "$BUILD_BASE_SHA" ]; then' in commit_block
    assert "git push origin HEAD:main" in commit_block
    assert "--validate-staged" in commit_block
    assert "git add output/history/daily_model_snapshots/ || true" not in commit_block
    assert "git add output/history/daily_candidate_models/ || true" not in commit_block
    assert 'test -z "$(git status --porcelain)"' in commit_block
    assert 'echo "PUSHED_ARTIFACT_SHA=$pushed_artifact_sha" >> "$GITHUB_ENV"' in commit_block
    assert "git add docs/latest/theme_event_watch_latest.*" in commit_block
    assert "git add docs/latest/chatgpt_indicator_usage_guide_latest.md" in commit_block
    assert "git add docs/latest/CHATGPT_INDICATOR_USAGE_GUIDE.txt" in commit_block

    pages_block = workflow[workflow.index("- name: Dispatch and wait for warrant Pages deploy") :]
    assert "env.ARTIFACT_COMMIT_CREATED == 'true'" in pages_block
    assert 'target_sha="$PUSHED_ARTIFACT_SHA"' in pages_block
    assert "git fetch origin main" in pages_block
    assert 'if [ "$current_origin_main" != "$target_sha" ]; then' in pages_block
    assert "previous_pages_run_id=" in pages_block
    assert "gh workflow run pages.yml --ref main" in pages_block
    assert "--event workflow_dispatch" in pages_block
    assert '--commit "$target_sha"' in pages_block
    assert 'pages_run_id" != "$previous_pages_run_id"' in pages_block
    assert 'pages_head_sha" != "$target_sha"' in pages_block
    assert 'pages_event" != "workflow_dispatch"' in pages_block
    assert 'pages_head_branch" != "main"' in pages_block
    assert "pages_deploy_attempts" not in pages_block
