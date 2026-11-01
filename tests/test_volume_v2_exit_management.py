from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_volume_breakout_operation_section as builder  # noqa: E402
import test_daily_volume_breakout_operation_section as existing_cases  # noqa: E402
import validate_daily_volume_breakout_operation_section as section_validator  # noqa: E402
from validate_daily_operation_adapter_protected_fields import validate_adapter_frame  # noqa: E402


MODEL_IDS = (
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
)
ENTRY_IDX = 2


def management_prices(holding_closes: list[float]) -> pd.DataFrame:
    closes = [100.0, 102.0, *holding_closes]
    return pd.DataFrame(
        {
            "date": pd.bdate_range("2026-06-01", periods=len(closes)).strftime("%Y%m%d"),
            "open": [100.0, 101.0, *([103.0] * len(holding_closes))],
            "high": [101.0, 103.0, *[max(value, 103.0) + 1 for value in holding_closes]],
            "low": [99.0, 100.0, *[min(value, 103.0) - 1 for value in holding_closes]],
            "close": closes,
            "volume": 1000.0,
            "ma20": 100.0,
            "ema23": 110.0,
            "ma60": 90.0,
            "ma120": 80.0,
        }
    )


def management_state(price: pd.DataFrame, holding_day: int) -> dict:
    return builder.v2_management_state(price, ENTRY_IDX, ENTRY_IDX + holding_day - 1)


def test_fourth_close_requires_next_open_even_when_no_future_row_exists() -> None:
    price = management_prices([95.0] * 4)

    state = management_state(price, 4)

    assert state["state"] == "stop_exit_pending_next_open"
    assert state["holding_days"] == 4
    assert state["stop_confirmed_days"] == 4
    assert state["stop_confirmation_idx"] == ENTRY_IDX + 3
    assert state["planned_exit_idx"] == ENTRY_IDX + 14
    assert state["stop_reference_price"] == pytest.approx(96.0)


def test_future_price_rows_do_not_turn_asof_stop_confirmation_into_an_exit() -> None:
    price = management_prices([95.0] * 4 + [150.0, 160.0])
    price.loc[ENTRY_IDX + 4, "open"] = 77.0
    price.loc[ENTRY_IDX + 4 :, "ma20"] = 300.0

    state = management_state(price, 4)

    assert state["state"] == "stop_exit_pending_next_open"
    assert state["holding_days"] == 4
    assert state["stop_confirmation_idx"] == ENTRY_IDX + 3
    assert state["stop_reference_price"] == pytest.approx(96.0)


def test_confirmed_stop_becomes_terminal_on_the_following_open() -> None:
    price = management_prices([95.0] * 4 + [150.0])
    price.loc[ENTRY_IDX + 4, "open"] = 77.0

    state = management_state(price, 5)

    assert state["state"] == "exited_stop_next_open"
    assert state["stop_confirmation_idx"] == ENTRY_IDX + 3
    assert state["exit_idx"] == ENTRY_IDX + 4
    assert price.iloc[state["exit_idx"]]["open"] == 77.0
    assert price.iloc[state["exit_idx"]]["close"] == 150.0


def test_counter_resets_instead_of_adding_nonconsecutive_below_days() -> None:
    price = management_prices([95.0, 95.0, 97.0, 95.0, 95.0, 95.0])

    state = management_state(price, 6)

    assert state["state"] == "active_operation"
    assert state["stop_confirmed_days"] == 3
    assert state["stop_confirmation_idx"] is None


def test_each_close_uses_that_days_reference_instead_of_the_last_reference() -> None:
    price = management_prices([95.0, 90.0, 95.0, 95.0, 95.0])
    price.loc[ENTRY_IDX + 1, "ma20"] = 90.0

    state = management_state(price, 5)

    assert state["state"] == "active_operation"
    assert state["stop_confirmed_days"] == 3
    assert state["stop_reference_price"] == pytest.approx(96.0)


def test_close_equal_to_the_daily_stop_reference_counts_as_below() -> None:
    price = management_prices([96.0] * 4)

    assert management_state(price, 4)["state"] == "stop_exit_pending_next_open"


def test_lower_of_the_two_valid_averages_is_the_reference() -> None:
    price = management_prices([95.0])
    price.loc[ENTRY_IDX, ["ma20", "ema23"]] = [110.0, 100.0]

    state = management_state(price, 1)

    assert state["stop_reference_price"] == pytest.approx(96.0)
    assert state["stop_confirmed_days"] == 1


def test_unavailable_daily_averages_reset_the_existing_counter() -> None:
    price = management_prices([95.0] * 4)
    price.loc[ENTRY_IDX + 2, ["ma20", "ema23"]] = math.nan

    state = management_state(price, 4)

    assert state["state"] == "active_operation"
    assert state["stop_confirmed_days"] == 1


@pytest.mark.parametrize("missing_column", ["ma20", "ema23"])
def test_one_valid_average_retains_the_existing_stop_reference_policy(missing_column: str) -> None:
    price = management_prices([95.0])
    price.loc[ENTRY_IDX, ["ma20", "ema23"]] = 100.0
    price.loc[ENTRY_IDX, missing_column] = math.nan

    state = management_state(price, 1)

    assert state["stop_reference_price"] == pytest.approx(96.0)
    assert state["stop_confirmed_days"] == 1


def test_fourth_below_close_on_d14_exits_on_d15_open() -> None:
    price = management_prices([100.0] * 10 + [95.0] * 4 + [130.0])

    pending = management_state(price, 14)
    exited = management_state(price, 15)

    assert pending["state"] == "stop_exit_pending_next_open"
    assert pending["stop_confirmation_idx"] == ENTRY_IDX + 13
    assert exited["state"] == "exited_stop_next_open"
    assert exited["exit_idx"] == ENTRY_IDX + 14


def test_first_fourth_below_close_on_d15_retains_the_approved_fixed_close_exit() -> None:
    # The approved D15 source scans range(entry_idx, planned_exit_idx), excluding D15.
    price = management_prices([100.0] * 11 + [95.0] * 4)

    state = management_state(price, 15)

    assert state["state"] == "exited_fixed_15d_close"
    assert state["stop_confirmation_idx"] is None
    assert state["exit_idx"] == state["planned_exit_idx"] == ENTRY_IDX + 14


def test_below_days_after_d15_cannot_change_the_fixed_exit_reason() -> None:
    price = management_prices([100.0] * 12 + [95.0] * 4)

    state = management_state(price, 16)

    assert state["state"] == "exited_fixed_15d_close"
    assert state["stop_confirmation_idx"] is None
    assert state["exit_idx"] == ENTRY_IDX + 14


def test_d14_is_still_active_but_d15_is_terminal_without_a_stop() -> None:
    price = management_prices([100.0] * 15)

    before = management_state(price, 14)
    at_close = management_state(price, 15)

    assert before["state"] == "active_operation"
    assert before["holding_days"] == 14
    assert at_close["state"] == "exited_fixed_15d_close"
    assert at_close["exit_idx"] == ENTRY_IDX + 14


def test_actual_entry_day_is_holding_day_one() -> None:
    state = management_state(management_prices([100.0]), 1)

    assert state["state"] == "active_operation"
    assert state["holding_days"] == 1


def build_nonempty_management_rows(
    monkeypatch,
    tmp_path: Path,
    model_id: str,
    holding_days: int,
    *,
    confirmation_mode: str = "buy_ranked",
    price_frame: pd.DataFrame | None = None,
    extra_signal_dates: tuple[str, ...] = (),
):
    price = price_frame if price_frame is not None else management_prices([95.0] * holding_days)
    signal_date = str(price.iloc[0]["date"])
    confirmation_date = str(price.iloc[1]["date"])
    report_date = str(price.iloc[-1]["date"])
    snapshot_dir = existing_cases.patch_lifecycle_sources(
        monkeypatch, tmp_path, "1234", price.astype(str).to_dict("records")
    )
    if confirmation_mode == "buy_ranked":
        existing_cases.write_operation_snapshot(
            snapshot_dir, confirmation_date, signal_date, model_id=model_id
        )
    elif confirmation_mode == "unranked":
        existing_cases.write_operation_snapshot(
            snapshot_dir,
            confirmation_date,
            signal_date,
            model_id=model_id,
            pdf_section="confirmed_unranked_operation",
            row_action_status="confirmed_not_buy_ranked",
            buy_rank_eligible="False",
        )
    elif confirmation_mode == "prior_active_only":
        existing_cases.write_operation_snapshot(
            snapshot_dir,
            str(price.iloc[ENTRY_IDX]["date"]),
            signal_date,
            model_id=model_id,
            selected_confirmation_date=confirmation_date,
            pdf_section="active_operation",
            row_action_status="active_operation",
            buy_rank_eligible="False",
        )
    elif confirmation_mode != "missing":
        raise AssertionError(f"unknown confirmation fixture: {confirmation_mode}")
    signal = existing_cases.volume_signal("1234", signal_date, model_id=model_id)
    history = [
        signal,
        *[
            existing_cases.volume_signal("1234", date, model_id=model_id)
            for date in extra_signal_dates
        ],
    ]
    rows, audit = builder.build_lifecycle_rows(
        pd.DataFrame(),
        report_date,
        0,
        {model_id: existing_cases.model_approval_stub(model_id)},
        "2026-06-08 21:00:00 Asia/Taipei",
        existing_cases.formal_summary(model_id=model_id),
        signal_history=pd.DataFrame(history),
    )
    return pd.DataFrame(rows), pd.DataFrame(audit)


@pytest.mark.parametrize("model_id", MODEL_IDS)
@pytest.mark.parametrize(
    ("holding_days", "expected_action"),
    [(2, "active_operation"), (4, "stop_exit_pending_next_open")],
)
def test_all_three_real_builders_keep_nonempty_management_rows_and_daily_fields(
    monkeypatch, tmp_path, model_id: str, holding_days: int, expected_action: str
) -> None:
    rows, _audit = build_nonempty_management_rows(monkeypatch, tmp_path, model_id, holding_days)

    assert len(rows) == 2
    assert set(rows["pdf_view"]) == {"highlight", "full"}
    assert set(rows["pdf_section"]) == {"active_operation"}
    assert set(rows["row_action_status"]) == {expected_action}
    assert set(rows["buy_rank_eligible"]) == {"False"}
    assert set(rows["operation_age_days"].astype(int)) == {holding_days}
    assert set(rows["stop_confirmed_days"].astype(int)) == {holding_days}
    assert rows["stop_loss_price"].astype(float).tolist() == pytest.approx([96.0, 96.0])


@pytest.mark.parametrize("model_id", MODEL_IDS)
@pytest.mark.parametrize("confirmation_mode", ["missing", "unranked", "prior_active_only"])
def test_stop_reminders_cannot_bypass_the_original_buy_ranked_confirmation_gate(
    monkeypatch, tmp_path, model_id: str, confirmation_mode: str
) -> None:
    if confirmation_mode == "missing":
        with pytest.raises(RuntimeError, match="requires the publisher manifest"):
            build_nonempty_management_rows(
                monkeypatch, tmp_path, model_id, 4, confirmation_mode=confirmation_mode
            )
        return
    rows, audit = build_nonempty_management_rows(
        monkeypatch, tmp_path, model_id, 4, confirmation_mode=confirmation_mode
    )

    assert rows.empty
    assert not audit.empty
    assert set(audit["included_in_daily_adapter"]) == {"False"}
    assert audit["reason"].str.contains("confirmation").all()


@pytest.mark.parametrize("model_id", MODEL_IDS)
def test_pending_stop_retains_same_stock_priority_over_a_new_confirmation(
    monkeypatch, tmp_path, model_id: str
) -> None:
    price = management_prices([95.0, 94.0, 94.0, 95.5])
    new_signal_idx = ENTRY_IDX + 2
    price.loc[new_signal_idx, ["open", "high", "low"]] = [94.5, 95.0, 93.0]
    price.loc[new_signal_idx + 1, ["open", "high", "low"]] = [95.0, 96.5, 94.5]
    old_signal_date = str(price.iloc[0]["date"])
    new_signal_date = str(price.iloc[new_signal_idx]["date"])

    rows, audit = build_nonempty_management_rows(
        monkeypatch,
        tmp_path,
        model_id,
        4,
        price_frame=price,
        extra_signal_dates=(new_signal_date,),
    )

    assert len(rows) == 2
    assert set(rows["signal_date"]) == {old_signal_date}
    assert set(rows["pdf_section"]) == {"active_operation"}
    assert set(rows["row_action_status"]) == {"stop_exit_pending_next_open"}
    suppressed = audit[audit["audit_status"].eq("lifecycle_suppressed")]
    assert not suppressed.empty
    assert new_signal_date in set(suppressed["signal_date"])


@pytest.mark.parametrize("model_id", MODEL_IDS)
@pytest.mark.parametrize("exit_case", ["confirmed_stop", "fixed_d15", "fourth_below_on_d15"])
def test_real_builder_terminal_prices_remain_audit_only_for_all_three_models(
    monkeypatch, tmp_path, model_id: str, exit_case: str
) -> None:
    if exit_case == "confirmed_stop":
        closes = [95.0] * 4 + [150.0]
        price = management_prices(closes)
        price.loc[ENTRY_IDX + 4, ["open", "low"]] = [77.0, 76.0]
        expected_price = 77.0
        expected_reason = "sustained_close_below_lower_ma20_ema23_4pct_4d"
        expected_basis = "next_trading_day_open"
    else:
        closes = [100.0] * 15 if exit_case == "fixed_d15" else [100.0] * 11 + [95.0] * 4
        price = management_prices(closes)
        expected_price = closes[-1]
        expected_reason = "fixed_15d_close"
        expected_basis = "fixed_future_close"

    rows, audit = build_nonempty_management_rows(
        monkeypatch, tmp_path, model_id, len(closes), price_frame=price
    )

    assert rows.empty
    assert not audit.empty
    assert set(audit["included_in_daily_adapter"]) == {"False"}
    assert set(audit["exit_date"]) == {str(price.iloc[-1]["date"])}
    assert set(audit["exit_reason"]) == {expected_reason}
    assert set(audit["exit_price_basis"]) == {expected_basis}
    assert audit["exit_price"].astype(float).tolist() == pytest.approx([expected_price])


def official_calendar_fixture(monkeypatch, tmp_path: Path) -> tuple[Path, dict]:
    path = tmp_path / "market_session_status_latest.json"
    payload = {
        "official_sources": {
            "twse_annual_calendar": {
                "status": "ok",
                "sha256": "a" * 64,
                "covered_years": [2026],
            }
        },
        "scheduled_non_trading_days": ["20261026"],
        "exceptional_non_trading_days": ["20261023"],
    }
    path.write_text(json.dumps(payload), encoding="utf-8")
    monkeypatch.setattr(builder, "MARKET_SESSION_STATUS_JSON", path)
    return path, payload


def test_planned_d15_skips_weekends_and_both_registered_closure_types(monkeypatch, tmp_path) -> None:
    official_calendar_fixture(monkeypatch, tmp_path)

    dates = builder.v2_calendar_dates("20261021")

    assert dates == {
        "planned_entry_date": "20261021",
        "planned_exit_date": "20261112",
        "planned_exit_date_status": "scheduled_official_calendar",
    }


def test_confirmed_candidate_plans_next_open_and_counts_d15_from_that_entry(monkeypatch, tmp_path) -> None:
    official_calendar_fixture(monkeypatch, tmp_path)

    dates = builder.v2_calendar_dates("", "20261022")

    assert dates == {
        "planned_entry_date": "20261027",
        "planned_exit_date": "20261116",
        "planned_exit_date_status": "scheduled_official_calendar",
    }


def test_known_next_entry_survives_when_the_d15_year_is_not_covered(monkeypatch, tmp_path) -> None:
    official_calendar_fixture(monkeypatch, tmp_path)

    dates = builder.v2_calendar_dates("", "20261230")

    assert dates["planned_entry_date"] == "20261231"
    assert dates["planned_exit_date"] == ""
    assert dates["planned_exit_date_status"] == "unavailable_calendar"


def test_uncovered_next_entry_year_does_not_fall_back_to_a_weekday_guess(monkeypatch, tmp_path) -> None:
    official_calendar_fixture(monkeypatch, tmp_path)

    dates = builder.v2_calendar_dates("", "20261231")

    assert dates["planned_entry_date"] == ""
    assert dates["planned_exit_date"] == ""
    assert dates["planned_exit_date_status"] == "unavailable_calendar"


@pytest.mark.parametrize("defect", ["status", "sha256", "missing_years", "wrong_year", "scheduled_type", "exceptional_type", "invalid_date"])
def test_invalid_calendar_evidence_cannot_produce_a_planned_exit(monkeypatch, tmp_path, defect: str) -> None:
    path, payload = official_calendar_fixture(monkeypatch, tmp_path)
    annual = payload["official_sources"]["twse_annual_calendar"]
    if defect == "status":
        annual["status"] = "unavailable"
    elif defect == "sha256":
        annual["sha256"] = "unverified"
    elif defect == "missing_years":
        del annual["covered_years"]
    elif defect == "wrong_year":
        annual["covered_years"] = [2025]
    elif defect == "scheduled_type":
        payload["scheduled_non_trading_days"] = {}
    elif defect == "exceptional_type":
        payload["exceptional_non_trading_days"] = None
    else:
        payload["exceptional_non_trading_days"] = ["not-a-date"]
    path.write_text(json.dumps(payload), encoding="utf-8")

    dates = builder.v2_calendar_dates("", "20261022")

    assert dates["planned_entry_date"] == ""
    assert dates["planned_exit_date"] == ""
    assert dates["planned_exit_date_status"] == "unavailable_calendar"


def test_missing_calendar_file_does_not_produce_unverified_future_dates(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(builder, "MARKET_SESSION_STATUS_JSON", tmp_path / "absent-calendar.json")

    dates = builder.v2_calendar_dates("20261021")

    assert dates["planned_exit_date"] == ""
    assert dates["planned_exit_date_status"] == "unavailable_calendar"


@pytest.mark.parametrize("model_id", MODEL_IDS)
def test_pending_stop_actual_builder_passes_model_and_protected_validators(
    monkeypatch, tmp_path, model_id: str
) -> None:
    calendar_path, _payload = official_calendar_fixture(monkeypatch, tmp_path)
    rows, audit = build_nonempty_management_rows(monkeypatch, tmp_path, model_id, 4)
    report_date = str(rows.iloc[0]["operation_asof_date"])
    section = existing_cases.complete_section_for_validator(rows, report_date)
    audit = audit.reindex(columns=builder.EVIDENCE_AUDIT_COLUMNS, fill_value="").fillna("")
    taxonomy_path = tmp_path / "stock_theme_taxonomy_latest.csv"
    pd.DataFrame(
        [{"stock_id": "1234", "report_line_memberships": "mainstream|non_mainstream"}]
    ).to_csv(taxonomy_path, index=False)
    monkeypatch.setattr(section_validator, "TAXONOMY_CSV", taxonomy_path)
    monkeypatch.setattr(section_validator, "MODEL_SNAPSHOT_DIR", builder.MODEL_SNAPSHOT_DIR)
    monkeypatch.setattr(section_validator, "MARKET_SESSION_STATUS_JSON", calendar_path)

    assert len(rows) == 2
    assert set(rows["row_type"]) == {"data"}
    assert set(rows["row_action_status"]) == {"stop_exit_pending_next_open"}
    section_validator.validate_operation_artifacts(
        section, existing_cases.formal_summary(model_id=model_id), audit
    )
    assert validate_adapter_frame(section, model_id) == []


def test_actual_pending_builder_still_rejects_raw_next_open_in_visible_action_text(
    monkeypatch, tmp_path, capsys
) -> None:
    model_id = MODEL_IDS[0]
    calendar_path, _payload = official_calendar_fixture(monkeypatch, tmp_path)
    rows, audit = build_nonempty_management_rows(monkeypatch, tmp_path, model_id, 4)
    report_date = str(rows.iloc[0]["operation_asof_date"])
    section = existing_cases.complete_section_for_validator(rows, report_date)
    audit = audit.reindex(columns=builder.EVIDENCE_AUDIT_COLUMNS, fill_value="").fillna("")
    taxonomy_path = tmp_path / "stock_theme_taxonomy_latest.csv"
    pd.DataFrame(
        [{"stock_id": "1234", "report_line_memberships": "mainstream|non_mainstream"}]
    ).to_csv(taxonomy_path, index=False)
    monkeypatch.setattr(section_validator, "TAXONOMY_CSV", taxonomy_path)
    monkeypatch.setattr(section_validator, "MODEL_SNAPSHOT_DIR", builder.MODEL_SNAPSHOT_DIR)
    monkeypatch.setattr(section_validator, "MARKET_SESSION_STATUS_JSON", calendar_path)
    visible_rows = section["model_id"].eq(model_id) & section["row_type"].eq("data")
    section.loc[visible_rows, "next_action_zh"] = "next_open 停損；下一交易日開盤"

    with pytest.raises(SystemExit):
        section_validator.validate_operation_artifacts(
            section, existing_cases.formal_summary(model_id=model_id), audit
        )

    assert "forbidden raw display token leaked: next_open" in capsys.readouterr().out
