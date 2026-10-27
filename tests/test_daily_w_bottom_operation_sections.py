from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_w_bottom_operation_sections as builder  # noqa: E402
import validate_daily_w_bottom_operation_sections as validator  # noqa: E402
import validate_daily_operation_adapter_protected_fields as protected_fields  # noqa: E402


def approval_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "w_bottom_right_side",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v2",
                "operation_module_id": "w_bottom_early_entry_operation_v2",
                "approval_version": "w_bottom_early_entry_operation_v2_20260629",
                "operation_directive_level": "approved_daily_operation_guidance",
                "buy_filter_id": "smooth_core_mainstream_right_rebound_5_20_bull",
                "best_evidence_sample_size": "31",
                "best_evidence_win_rate": "58.0645",
                "best_evidence_avg_return": "11.2532",
                "best_evidence_median_return": "6.2374",
                "approval_note_zh": "approved",
            },
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_module_id": "neckline_strict_45_signal_90_score_v1",
                "approval_version": "neckline_strict_45_signal_90_score_v1_20260629",
                "operation_directive_level": "approved_daily_operation_guidance",
                "buy_filter_id": "broad_45_non_bearish_with_90_warning",
                "best_evidence_sample_size": "51",
                "best_evidence_win_rate": "63.8889",
                "best_evidence_avg_return": "4.3784",
                "best_evidence_median_return": "4.4597",
                "approval_note_zh": "approved",
            },
        ]
    )


def signal_row(model_id: str, signal_date: str = "20260630") -> dict[str, str]:
    return {
        "model_id": model_id,
        "model_name_zh": "W bottom model",
        "signal_date": signal_date,
        "stock_id": "1234",
        "stock_name": "TestCo",
        "report_bucket": "mainstream",
        "report_line": "mainstream",
        "report_line_memberships": "mainstream",
        "display_rank": "1",
        "model_score": "70",
        "next_confirmation_zh": "follow approved rule",
    }


def test_current_signal_becomes_confirmed_buy_rows(monkeypatch) -> None:
    monkeypatch.setattr(builder, "signal_snapshot_paths", lambda _report_date: [])
    section, audit = builder.build_model_section(
        pd.DataFrame([signal_row("w_bottom_right_side")]),
        approval_frame(),
        builder.MODEL_CONFIGS["w_bottom_right_side"],
        "20260630",
        "2026-06-30 12:00:00 Asia/Taipei",
    )

    confirmed = section[
        section["row_type"].eq("data") & section["pdf_section"].eq("confirmed_operation")
    ]
    assert set(confirmed["pdf_view"]) == {"highlight", "full"}
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}
    assert set(confirmed["row_metric_status"]) == {"unavailable_no_approved_add_score_metric"}
    assert set(confirmed["row_metric_id"]) == {""}
    assert set(confirmed["row_metric_win_rate_zh"]) == {""}
    assert set(confirmed["entry_rule_id"]) == {"right_low_signal_next_open"}
    assert set(confirmed["exit_rule_id"]) == {"d20_gain10_else_d40_close"}
    assert "active_operation" in set(section["pdf_section"])
    assert not audit.empty


def test_prior_signal_can_become_active_tracking_row(monkeypatch) -> None:
    price = pd.DataFrame(
        [
            {"date": "20260624", "open": 10.0, "high": 10.5, "low": 9.8, "close": 10.2},
            {"date": "20260625", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.5},
            {"date": "20260626", "open": 10.6, "high": 11.0, "low": 10.4, "close": 10.8},
            {"date": "20260629", "open": 10.9, "high": 11.2, "low": 10.7, "close": 11.0},
            {"date": "20260630", "open": 11.1, "high": 11.5, "low": 10.9, "close": 11.2},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    monkeypatch.setattr(
        builder,
        "build_structure_context",
        lambda _row, _price: {
            "left_low_date": "20260624",
            "right_low_date": "20260625",
            "w_structure_low_price": 9.8,
            "neckline_price": 12.0,
            "neckline_distance_pct": -6.67,
        },
    )
    monkeypatch.setattr(
        builder,
        "load_signal_history",
        lambda _signals, _config, _report_date: pd.DataFrame([signal_row("w_bottom_right_side", "20260624")]),
    )

    section, audit = builder.build_model_section(
        pd.DataFrame(columns=["model_id", "signal_date", "stock_id"]),
        approval_frame(),
        builder.MODEL_CONFIGS["w_bottom_right_side"],
        "20260630",
        "2026-06-30 12:00:00 Asia/Taipei",
    )

    active = section[section["row_type"].eq("data") & section["pdf_section"].eq("active_operation")]
    assert set(active["pdf_view"]) == {"highlight", "full"}
    assert set(active["row_action_status"]) == {"active_tracking"}
    assert set(active["buy_rank_eligible"]) == {"False"}
    assert set(active["entry_date"]) == {"20260625"}
    assert all(token in active.iloc[0]["exit_rule_zh"] for token in ("D+20", "+10%", "D+40"))
    assert "candidate_evaluated" in set(audit["audit_status"])


def test_validator_rejects_active_w_bottom_rows_without_exit_rule_tokens() -> None:
    active = pd.DataFrame(
        [
            {
                "pdf_view": "highlight",
                "report_line": "mainstream",
                "stock_id": "1234",
                "exit_rule_zh": "若 D+20 收盤報酬達 +10% 則 D+20 收盤出場。",
            }
        ]
    )

    errors = validator.validate_active_exit_rule_tokens(
        active,
        "daily_w_bottom_right_side_operation_section_latest.csv",
        "w_bottom_right_side",
    )

    assert any("missing tokens ['D+40']" in error for error in errors)

    active.loc[0, "exit_rule_zh"] = "若 D+20 收盤報酬達 +10% 則 D+20 收盤出場；否則持有到 D+40 收盤。"

    assert (
        validator.validate_active_exit_rule_tokens(
            active,
            "daily_w_bottom_right_side_operation_section_latest.csv",
            "w_bottom_right_side",
        )
        == []
    )


def test_current_w_bottom_signal_is_suppressed_when_same_stock_is_already_active(monkeypatch) -> None:
    price = pd.DataFrame(
        [
            {"date": "20260624", "open": 10.0, "high": 10.5, "low": 9.8, "close": 10.2},
            {"date": "20260625", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.5},
            {"date": "20260626", "open": 10.6, "high": 11.0, "low": 10.4, "close": 10.8},
            {"date": "20260629", "open": 10.9, "high": 11.2, "low": 10.7, "close": 11.0},
            {"date": "20260630", "open": 11.1, "high": 11.5, "low": 10.9, "close": 11.2},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    monkeypatch.setattr(
        builder,
        "build_structure_context",
        lambda _row, _price: {
            "left_low_date": "20260624",
            "right_low_date": "20260625",
            "w_structure_low_price": 9.8,
            "neckline_price": 12.0,
            "neckline_distance_pct": -6.67,
        },
    )
    monkeypatch.setattr(
        builder,
        "load_signal_history",
        lambda _signals, _config, _report_date: pd.DataFrame([signal_row("w_bottom_right_side", "20260624")]),
    )

    section, audit = builder.build_model_section(
        pd.DataFrame([signal_row("w_bottom_right_side", "20260630")]),
        approval_frame(),
        builder.MODEL_CONFIGS["w_bottom_right_side"],
        "20260630",
        "2026-06-30 12:00:00 Asia/Taipei",
    )

    confirmed = section[section["row_type"].eq("data") & section["pdf_section"].eq("confirmed_operation")]
    active = section[section["row_type"].eq("data") & section["pdf_section"].eq("active_operation")]
    assert confirmed.empty
    assert set(active["signal_date"]) == {"20260624"}
    assert set(active["stock_id"]) == {"1234"}
    suppressed = audit[audit["audit_status"].eq("lifecycle_suppressed")]
    assert suppressed[["stock_id", "signal_date", "reason"]].to_dict("records") == [
        {
            "stock_id": "1234",
            "signal_date": "20260630",
            "reason": "same_stock_already_active_operation",
        }
    ]
    assert set(suppressed["included_in_daily_adapter"]) == {"False"}


@pytest.mark.parametrize(
    "model_id",
    ["w_bottom_right_side", "neckline_volume_breakout_confirmation"],
)
def test_each_w_bottom_model_supported_states_pass_protected_contract(monkeypatch, model_id: str) -> None:
    config = builder.MODEL_CONFIGS[model_id]
    monkeypatch.setattr(builder, "load_signal_history", lambda *_args: pd.DataFrame())
    confirmed_section, confirmed_audit = builder.build_model_section(
        pd.DataFrame([signal_row(model_id, "20260630")]),
        approval_frame(),
        config,
        "20260630",
        "2026-06-30 12:00:00 Asia/Taipei",
    )

    price = pd.DataFrame(
        [
            {"date": "20260624", "open": 10.0, "high": 10.5, "low": 9.8, "close": 10.2},
            {"date": "20260625", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.5},
            {"date": "20260626", "open": 10.6, "high": 11.0, "low": 10.4, "close": 10.8},
            {"date": "20260629", "open": 10.9, "high": 11.2, "low": 10.7, "close": 11.0},
            {"date": "20260630", "open": 11.1, "high": 11.5, "low": 10.9, "close": 11.2},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    monkeypatch.setattr(
        builder,
        "build_structure_context",
        lambda _row, _price: {
            "left_low_date": "20260624",
            "right_low_date": "20260625",
            "w_structure_low_price": 9.8,
            "neckline_price": 12.0,
            "neckline_distance_pct": -6.67,
        },
    )
    monkeypatch.setattr(
        builder,
        "load_signal_history",
        lambda *_args: pd.DataFrame([signal_row(model_id, "20260624")]),
    )
    active_section, active_audit = builder.build_model_section(
        pd.DataFrame(columns=["model_id", "signal_date", "stock_id"]),
        approval_frame(),
        config,
        "20260630",
        "2026-06-30 12:00:00 Asia/Taipei",
    )

    combined = pd.concat([confirmed_section, active_section], ignore_index=True)
    assert protected_fields.validate_adapter_frame(
        combined,
        model_id,
        required_states={"confirmed", "active", "empty"},
    ) == []
    assert validator.validate_section(
        model_id,
        confirmed_section,
        confirmed_audit,
        expected_signal_count_override=1,
    ) == []
    assert validator.validate_section(
        model_id,
        active_section,
        active_audit,
        expected_signal_count_override=0,
    ) == []


def test_daily_full_pipeline_runs_w_bottom_operation_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")
    assert "python scripts/build_daily_w_bottom_operation_sections.py" in workflow
    assert "python scripts/validate_daily_w_bottom_operation_sections.py" in workflow
    assert "git add docs/latest/daily_w_bottom_right_side_operation_*_latest.*" in workflow
    assert "git add docs/latest/daily_neckline_volume_breakout_confirmation_operation_*_latest.*" in workflow


w_exit_root = Path(__file__).resolve().parents[1]



w_exit_fixture = json.loads(
    (w_exit_root / "tests" / "fixtures" / "w_bottom_exit_order_regression.json").read_text(encoding="utf-8")
)


def test_w_exit_real_case_fixture_is_explicitly_regression_only() -> None:
    assert w_exit_fixture["source_commit"] == "9b588342955e3e0d9aaadb0c240be3077224c5a6"
    assert w_exit_fixture["formal_performance_evidence_allowed"] is False
    assert w_exit_fixture["promotion_allowed"] is False
    assert "not_pit_or_performance_evidence" in w_exit_fixture["fixture_role"]
    assert {case["stock_id"] for case in w_exit_fixture["cases"]} == {
        "4943", "2482", "2431", "2363", "5269", "6237"
    }
    for case in w_exit_fixture["cases"]:
        assert len(case["bars"]) == case["old_late_stop_session"]
        assert case["bars"][0][0] == case["entry_date"]
        assert case["bars"][-1][0] == case["old_late_stop_date"]
        canonical_bars = json.dumps(case["bars"], separators=(",", ":")).encode()
        assert hashlib.sha256(canonical_bars).hexdigest() == case["source_bars_sha256"]


@pytest.mark.parametrize("case", w_exit_fixture["cases"], ids=lambda case: case["stock_id"])
def test_w_exit_real_w_bottom_terminal_exit_survives_later_stop(case: dict) -> None:
    """Use actual source rows; this is an event-order regression, not a backtest."""
    price = pd.DataFrame(case["bars"], columns=case["source_bar_columns"])
    terminal_idx = case["expected_terminal_session"] - 1
    expected = case["expected_exit"]

    at_terminal = builder.w_bottom_exit_state(
        price, 0, terminal_idx, case["entry_open"], case["stop_price"]
    )
    after_later_stop = builder.w_bottom_exit_state(
        price, 0, len(price) - 1, case["entry_open"], case["stop_price"]
    )

    assert at_terminal == expected
    assert after_later_stop == expected
    assert after_later_stop == at_terminal


def w_exit_synthetic_price(closes: list[float]) -> pd.DataFrame:
    """Synthetic session labels test boundaries; they are not market-calendar evidence."""
    return pd.DataFrame(
        {"date": [f"synthetic_session_{day:03d}" for day in range(1, len(closes) + 1)], "close": closes}
    )


def w_exit_assert_exit(price: pd.DataFrame, day: int, reason: str, *, stop: float = 90.0) -> None:
    assert builder.w_bottom_exit_state(price, 0, len(price) - 1, 100.0, stop) == {
        "state": "exited",
        "exit_date": price.iloc[day - 1]["date"],
        "exit_reason": reason,
    }


def test_w_exit_synthetic_entry_history_does_not_shift_holding_deadline() -> None:
    price = w_exit_synthetic_price([1.0] * 3 + [100.0] * 19 + [110.0] + [89.0] * 5)
    assert builder.w_bottom_exit_state(price, 3, len(price) - 1, 100.0, 90.0) == {
        "state": "exited",
        "exit_date": price.iloc[22]["date"],
        "exit_reason": "d20_gain10_close_exit",
    }


def test_w_exit_synthetic_stop_before_d20_remains_first_event() -> None:
    closes = [100.0] * 45
    closes[6] = 89.0
    closes[19] = 120.0
    w_exit_assert_exit(w_exit_synthetic_price(closes), 7, "w_structure_low_close_stop")


def test_w_exit_synthetic_equal_stop_does_not_change_strict_below_rule() -> None:
    closes = [100.0] * 45
    closes[6] = 90.0
    closes[19] = 120.0
    w_exit_assert_exit(w_exit_synthetic_price(closes), 20, "d20_gain10_close_exit")


def test_w_exit_synthetic_gain_before_d20_does_not_create_an_earlier_target() -> None:
    closes = [100.0] * 45
    closes[18] = 120.0
    closes[19] = 105.0
    w_exit_assert_exit(w_exit_synthetic_price(closes), 40, "d40_close_exit")


@pytest.mark.parametrize(
    ("d20_close", "expected_day", "expected_reason"),
    [(110.0, 20, "d20_gain10_close_exit"), (109.9999, 40, "d40_close_exit")],
)
def test_w_exit_synthetic_d20_threshold_is_inclusive(
    d20_close: float, expected_day: int, expected_reason: str
) -> None:
    closes = [100.0] * 45
    closes[19] = d20_close
    w_exit_assert_exit(w_exit_synthetic_price(closes), expected_day, expected_reason)


@pytest.mark.parametrize("session_count", [19, 39])
def test_w_exit_synthetic_incomplete_horizon_stays_active(session_count: int) -> None:
    price = w_exit_synthetic_price([100.0] * session_count)
    assert builder.w_bottom_exit_state(price, 0, len(price) - 1, 100.0, 90.0) == {
        "state": "active", "exit_date": "", "exit_reason": ""
    }


def test_w_exit_synthetic_same_day_d40_stop_has_priority() -> None:
    closes = [100.0] * 45
    closes[39] = 89.0
    w_exit_assert_exit(w_exit_synthetic_price(closes), 40, "w_structure_low_close_stop")


@pytest.mark.parametrize("d20_close", [100.0, 120.0])
def test_w_exit_synthetic_nan_stop_keeps_existing_time_exit_behavior(d20_close: float) -> None:
    closes = [100.0] * 45
    closes[19] = d20_close
    expected_day = 20 if d20_close >= 110.0 else 40
    expected_reason = "d20_gain10_close_exit" if expected_day == 20 else "d40_close_exit"
    w_exit_assert_exit(w_exit_synthetic_price(closes), expected_day, expected_reason, stop=float("nan"))


def test_w_exit_missing_asof_remains_an_existing_source_gap(monkeypatch) -> None:
    price = pd.DataFrame(
        [
            {"date": "20260105", "open": 100.0, "high": 101.0, "low": 99.0, "close": 100.0},
            {"date": "20260106", "open": 100.0, "high": 101.0, "low": 99.0, "close": 100.0},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    rows, audit = builder.active_data_row(
        pd.Series({"stock_id": "1234", "signal_date": "20260105"}),
        builder.MODEL_CONFIGS["w_bottom_right_side"],
        {},
        "20260107",
        0,
        "synthetic regression only",
        1,
    )
    assert rows == []
    assert audit["audit_status"] == "source_gap"
    assert audit["reason"] == "operation_asof_date_missing_in_stock_price_history"


NECKLINE_EXIT_ROOT = Path(__file__).resolve().parents[1]



NECKLINE_EXIT_FIXTURE = json.loads(
    (NECKLINE_EXIT_ROOT / "tests" / "fixtures" / "neckline_exit_order_regression.json").read_text(encoding="utf-8")
)


def neckline_exit_synthetic_price(closes: list[float]) -> pd.DataFrame:
    """Synthetic session ordinals for boundary tests, never market evidence."""
    return pd.DataFrame(
        {
            "date": pd.bdate_range("2026-06-01", periods=len(closes)).strftime("%Y%m%d"),
            "open": [100.0] * len(closes),
            "high": [max(100.0, close) for close in closes],
            "low": [min(100.0, close) for close in closes],
            "close": closes,
        }
    )


def neckline_exit_assert_exit(state: dict[str, str], date: str, reason: str) -> None:
    assert state == {"state": "exited", "exit_date": date, "exit_reason": reason}


@pytest.mark.parametrize("case", NECKLINE_EXIT_FIXTURE["cases"], ids=lambda case: case["case_id"])
def test_neckline_exit_actual_regression_windows_keep_the_formal_d20_exit(case: dict) -> None:
    # Only actual existing date/close rows are frozen here; there is no padding,
    # invented session, regenerated signal, or claim of a formal position/PIT.
    price = pd.DataFrame(case["prices"])
    expected = case["expected_formal"]
    assert price.iloc[0]["date"] == case["entry_date"]
    assert price["date"].is_unique
    assert price["date"].is_monotonic_increasing
    assert price.iloc[19]["date"] == expected["exit_date"]
    assert price.iloc[19]["close"] == expected["exit_price"]
    assert expected["holding_sessions"] == 20
    assert case["known_old_adapter"]["holding_sessions"] > 20
    assert len(case["source_raw_sha256"]) == 64

    state = builder.neckline_exit_state(price, 0, len(price) - 1, case["entry_price"])
    neckline_exit_assert_exit(state, expected["exit_date"], expected["exit_reason"])


@pytest.mark.parametrize("asof_idx", [18, 19, 20])
def test_neckline_exit_synthetic_d19_d20_d21_keep_the_same_deadline(asof_idx: int) -> None:
    price = neckline_exit_synthetic_price([100.0] * 20 + [112.0])
    state = builder.neckline_exit_state(price, 0, asof_idx, 100.0)
    if asof_idx == 18:
        assert state == {"state": "active", "exit_date": "", "exit_reason": ""}
    else:
        neckline_exit_assert_exit(state, price.iloc[19]["date"], "fixed_20d_close_without_tp10_or_neutral")


@pytest.mark.parametrize(
    ("prefix", "last_close", "reason"),
    [
        ([100.0] * 19, 110.0, "tp10_close_win"),
        ([106.0] + [106.0] * 18, 104.0, "pulled_back_to_5pct_after_plus5_without_tp10"),
    ],
)
def test_neckline_exit_synthetic_d20_event_precedes_deadline_fallback(prefix, last_close, reason) -> None:
    price = neckline_exit_synthetic_price(prefix + [last_close] + [120.0])
    neckline_exit_assert_exit(builder.neckline_exit_state(price, 0, 20, 100.0), price.iloc[19]["date"], reason)


@pytest.mark.parametrize(
    ("closes", "exit_idx", "reason"),
    [
        ([100.0, 106.0, 111.0], 2, "tp10_close_win"),
        ([100.0, 106.0, 104.0], 2, "pulled_back_to_5pct_after_plus5_without_tp10"),
    ],
)
def test_neckline_exit_synthetic_early_exit_is_stable_when_later_prices_are_appended(closes, exit_idx, reason) -> None:
    price = neckline_exit_synthetic_price(closes + [80.0] * 20 + [130.0])
    first = builder.neckline_exit_state(price, 0, exit_idx, 100.0)
    later = builder.neckline_exit_state(price, 0, len(price) - 1, 100.0)
    neckline_exit_assert_exit(first, price.iloc[exit_idx]["date"], reason)
    assert later == first


def test_neckline_exit_synthetic_nonzero_entry_index_counts_entry_as_day_one() -> None:
    price = neckline_exit_synthetic_price([120.0] * 3 + [100.0] * 20 + [112.0])
    state = builder.neckline_exit_state(price, 3, 23, 100.0)
    neckline_exit_assert_exit(state, price.iloc[22]["date"], "fixed_20d_close_without_tp10_or_neutral")


def test_neckline_exit_synthetic_asof_does_not_read_future_event_or_deadline() -> None:
    price = neckline_exit_synthetic_price([100.0] * 10 + [111.0] + [80.0] * 14)
    assert builder.neckline_exit_state(price, 0, 9, 100.0) == {
        "state": "active", "exit_date": "", "exit_reason": ""
    }


def test_neckline_exit_synthetic_exact_plus5_preserves_existing_if_elif_boundary() -> None:
    # Existing semantics intentionally preserved: a close exactly at +5% takes
    # the >=5 latch branch, rather than the subsequent elif neutral branch.
    price = neckline_exit_synthetic_price([106.0, 105.0, 104.0])
    assert builder.neckline_exit_state(price, 0, 1, 100.0) == {
        "state": "active", "exit_date": "", "exit_reason": ""
    }
    neckline_exit_assert_exit(
        builder.neckline_exit_state(price, 0, 2, 100.0),
        price.iloc[2]["date"],
        "pulled_back_to_5pct_after_plus5_without_tp10",
    )


def test_neckline_exit_synthetic_caller_keeps_expired_neckline_suppressed(monkeypatch) -> None:
    price = neckline_exit_synthetic_price([100.0] * 21 + [111.0] + [100.0] * 3)
    row = pd.Series(
        {
            "model_id": "neckline_volume_breakout_confirmation",
            "model_name_zh": "Synthetic test only",
            "signal_date": price.iloc[0]["date"],
            "stock_id": "1234",
            "stock_name": "Synthetic",
            "report_bucket": "mainstream",
            "report_line": "mainstream",
            "model_score": "70",
        }
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock: price)
    monkeypatch.setattr(builder, "build_structure_context", lambda _row, _price: {})
    config = builder.MODEL_CONFIGS["neckline_volume_breakout_confirmation"]
    before_rows, before_audit = builder.active_data_row(
        row, config, {}, price.iloc[20]["date"], 0, "synthetic", 1
    )
    later_rows, later_audit = builder.active_data_row(
        row, config, {}, price.iloc[-1]["date"], 0, "synthetic", 1
    )
    assert before_rows == later_rows == []
    for audit in (before_audit, later_audit):
        assert audit["audit_status"] == "lifecycle_suppressed"
        assert audit["included_in_daily_adapter"] == "False"
        assert audit["exit_date"] == price.iloc[20]["date"]
        assert audit["exit_reason"] == "fixed_20d_close_without_tp10_or_neutral"
