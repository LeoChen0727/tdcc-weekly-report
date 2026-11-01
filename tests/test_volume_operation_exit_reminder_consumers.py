from __future__ import annotations

from io import StringIO

import pandas as pd
import pytest

import build_chatgpt_daily_report_packet as packet
from scripts import generate_chatgpt_side_daily_reports as renderer


V2_MODELS = sorted(renderer.VOLUME_BREAKOUT_OPERATION_MODEL_IDS)
MANAGEMENT_COLUMNS = (
    "stop_reference_price", "stop_reference_date", "stop_confirmed_days",
    "holding_days", "planned_entry_date", "planned_exit_date",
    "planned_exit_date_status", "next_action_date", "next_action_date_status",
    "stop_confirmation_date", "next_action_zh",
)


def operation_row(model_id: str, **overrides) -> pd.Series:
    values = {
        "model_id": model_id,
        "pdf_view": "full",
        "pdf_section": "active_operation",
        "row_type": "data",
        "display_order": "1",
        "stock_id": "1234",
        "stock_display": "1234 測試股",
        "operation_status": "active_operation",
        "operation_status_zh": "操作中",
        "row_action_status": "stop_exit_pending_next_open",
        "buy_rank_eligible": "False",
        "entry_rule_id": "confirmation_next_open",
        "entry_date": "20261021",
        "entry_price": "20",
        "operation_age_days": "99",
        "holding_days": "3",
        "planned_holding_days": "15",
        "stop_reference_price": "9.8765",
        "stop_reference_date": "20261030",
        "stop_confirmed_days": "4",
        "stop_confirmation_date": "20261030",
        "stop_loss_price": "",
        "stop_loss_label_zh": "MA20/EMA23 4日收盤停損",
        "stop_basis_zh": "連續四日收盤確認後，隔日開盤停損。",
        "exit_rule_id": "ema23_close_stop_or_fixed_15d_close",
        "exit_rule_zh": "未觸發停損則第15個交易日收盤出場。",
        "planned_entry_date": "",
        "planned_exit_date": "20261120",
        "planned_exit_date_status": "scheduled_calendar_projection",
        "next_action_date": "20261103",
        "next_action_date_status": "scheduled_calendar_projection",
        "next_action_zh": "隔日開盤執行停損，成交價尚未產生。",
        "rank_reason_zh": "原排名原因",
        "adapter_note_zh": "原adapter備註",
    }
    values.update(overrides)
    return pd.Series(values)


@pytest.mark.parametrize("model_id", V2_MODELS)
def test_v2_labels_consume_supplied_values_without_recomputing(model_id: str) -> None:
    row = operation_row(model_id, ma20="999", ema23="888", close="777")
    before = row.to_dict()

    stop = renderer.volume_operation_stop_label(row, "active_operation")
    action = renderer.volume_operation_exit_label(row)

    assert "9.88" in stop
    assert "非成交價" in stop
    assert "4 / 4" in stop
    assert "停損已確認" in action
    assert "等待下一交易日開盤執行" in action
    assert "排定\n2026/11/3" in action
    assert "尚未產生" in action
    assert "已出場" not in action
    assert renderer.volume_operation_holding_label(row) == "3 / 15"
    assert row.to_dict() == before


@pytest.mark.parametrize("model_id", V2_MODELS)
def test_v2_confirmed_entry_dates_remain_scheduled_without_a_price(model_id: str) -> None:
    row = operation_row(
        model_id,
        pdf_section="confirmed_operation",
        row_action_status="confirmed_buy_candidate",
        buy_rank_eligible="True",
        entry_date="",
        entry_price="",
        planned_entry_date="20261102",
    )

    label = renderer.volume_operation_entry_label(row, "confirmed_operation")

    assert "排定\n2026/11/2" in label
    assert "開盤價尚未產生" in label
    assert row["entry_date"] == row["entry_price"] == ""
    assert "排定" in renderer.volume_operation_exit_label(row)


def test_v2_missing_future_date_is_not_inferred() -> None:
    row = operation_row(
        V2_MODELS[0],
        row_action_status="active_operation",
        planned_exit_date="",
        planned_exit_date_status="official_calendar_unavailable",
        next_action_date="",
        next_action_zh="",
        stop_confirmed_days="0",
    )

    assert "排定出場日待確認" in renderer.volume_operation_exit_label(row)
    assert renderer.volume_operation_action_label(row) == ""
    assert "0 / 4" in renderer.volume_operation_stop_label(row, "active_operation")


@pytest.mark.parametrize("model_id", V2_MODELS)
def test_v2_pending_stop_remains_active_with_existing_pdf_caps(model_id: str, monkeypatch) -> None:
    rows = pd.DataFrame([operation_row(model_id, stock_id=str(1000 + i)) for i in range(12)])
    monkeypatch.setattr(renderer, "volume_operation_all_rows_for_pdf", lambda *args: rows)

    full = renderer.selected_volume_operation_rows_for_pdf({}, model_id, "full", None, "active_operation")
    highlight = renderer.selected_volume_operation_rows_for_pdf({}, model_id, "highlight", None, "active_operation")
    confirmed = renderer.selected_volume_operation_rows_for_pdf({}, model_id, "full", None, "confirmed_operation")

    assert len(full) == 12
    assert len(highlight) == 10
    assert confirmed.empty
    assert full["operation_status"].eq("active_operation").all()
    rows["buy_rank_eligible"] = "True"
    assert renderer.selected_volume_operation_rows_for_pdf({}, model_id, "full", None, "active_operation").empty


def test_v2_active_table_displays_holding_count_and_pending_action(monkeypatch) -> None:
    row = operation_row(V2_MODELS[0])
    monkeypatch.setattr(renderer, "build_table", lambda data, *args, **kwargs: data)

    table = renderer.build_volume_active_operation_table(pd.DataFrame([row]), V2_MODELS[0])

    assert table[2][2] == renderer.volume_operation_entry_label(row, "active_operation")
    assert table[2][4] == "3 / 15"
    assert "停損已確認" in table[2][5]
    assert "排定" in table[2][5]
    assert table[2][7] == row["rank_reason_zh"]


def test_legacy_volume_labels_and_selector_keep_their_original_behavior(monkeypatch) -> None:
    row = operation_row(
        renderer.LEGACY_VOLUME_BREAKOUT_MODEL_ID,
        stop_loss_label_zh="訊號低點",
        stop_loss_price="17.5",
        exit_rule_id="signal_low_stop_or_fixed_10d_close",
        planned_holding_days="10",
    )
    assert renderer.volume_operation_stop_label(row, "active_operation") == "訊號低點 17.5"
    assert renderer.volume_operation_holding_label(row) == "99 / 10"
    assert renderer.volume_operation_action_label(row) == ""
    assert "第 10 個交易日收盤" in renderer.volume_operation_exit_label(row)
    assert packet.volume_operation_execution_packet_suffix(row) == ""
    monkeypatch.setattr(renderer, "volume_operation_all_rows_for_pdf", lambda *args: pd.DataFrame([row]))
    assert renderer.selected_volume_operation_rows_for_pdf(
        {}, renderer.LEGACY_VOLUME_BREAKOUT_MODEL_ID, "full", None, "active_operation"
    ).empty


def test_volume_packet_exposes_adapter_fields_and_scheduled_dates(monkeypatch) -> None:
    active = operation_row(V2_MODELS[0])
    confirmed = operation_row(
        V2_MODELS[1],
        stock_id="5678",
        stock_display="5678 確認股",
        pdf_section="confirmed_operation",
        row_action_status="confirmed_buy_candidate",
        buy_rank_eligible="True",
        entry_date="",
        entry_price="",
        holding_days="",
        planned_entry_date="20261102",
        entry_price_status_zh="尚未到進場日，開盤價尚未產生。",
    )
    frame = pd.DataFrame([active, confirmed]).fillna("")
    before = frame.copy(deep=True)
    monkeypatch.setattr(
        packet,
        "safe_read_csv",
        lambda path: frame.copy() if path == packet.DAILY_VOLUME_BREAKOUT_OPERATION_SECTION_CSV else pd.DataFrame(),
    )

    text = "\n".join(packet.build_volume_operation_packet_lines())

    assert "planned_entry_date=排定 20261102" in text
    assert "planned_exit_date=排定 20261120" in text
    assert "next_action_date=排定 20261103" in text
    assert "stop_reference_price=9.8765（動態參考線，非成交價）" in text
    assert "stop_reference_date=20261030" in text
    assert "stop_confirmed_days=4" in text
    assert "stop_confirmation_date=20261030" in text
    assert "holding_days=3" in text
    assert "row_action_status=stop_exit_pending_next_open" in text
    assert "entry_price=20" in text
    confirmed_text = text.split("full_confirmed_operation:", 1)[1].split("full_pending_confirmation:", 1)[0]
    assert "entry_price=" not in confirmed_text
    pd.testing.assert_frame_equal(frame, before)


def pdf_adapter_frame(model_id: str) -> pd.DataFrame:
    frame = pd.DataFrame([operation_row(model_id)])
    for field in renderer.OPERATION_ROW_METRIC_REQUIRED_COLUMNS:
        if field not in frame:
            frame[field] = ""
    return frame


@pytest.mark.parametrize("model_id", V2_MODELS)
def test_v2_pdf_csv_roundtrip_formats_nullable_integer_columns(model_id: str) -> None:
    active = pdf_adapter_frame(model_id)
    empty = active.copy()
    empty["row_type"] = "empty_state"
    fields = (
        "signal_date", "confirmation_date", "selected_confirmation_date", "entry_date",
        "stop_reference_date", "stop_confirmation_date", "planned_entry_date", "planned_exit_date",
        "next_action_date", "holding_days", "planned_holding_days", "operation_age_days", "stop_confirmed_days",
    )
    for field in fields:
        if field not in active:
            active[field] = "20261030" if field.endswith("date") else "3"
        empty[field] = ""
    raw = pd.read_csv(StringIO(pd.concat([active, empty], ignore_index=True).to_csv(index=False)))
    before = raw.copy(deep=True)
    assert raw.iloc[0]["holding_days"] == 3.0
    result = renderer.volume_operation_frame({"volume_operation": raw}, model_id, "full", "active_operation")
    row = result[result["row_type"].eq("data")].iloc[0]
    assert "2026/10/21" in renderer.volume_operation_entry_label(row, "active_operation")
    assert renderer.volume_operation_holding_label(row) == "3 / 15"
    stop = renderer.volume_operation_stop_label(row, "active_operation")
    assert "2026/10/30" in stop and "9.88" in stop and "4 / 4" in stop
    assert "排定\n2026/11/3" in renderer.volume_operation_exit_label(row)
    assert "20261030.0" not in stop
    pd.testing.assert_frame_equal(raw, before)


@pytest.mark.parametrize("model_id", V2_MODELS)
def test_v2_score_numbers_have_their_own_line(model_id: str) -> None:
    row = operation_row(model_id, operation_score="4", final_rank_score="93.4")
    assert renderer.volume_operation_score_label(row) == "操作\n4.00\n最終\n93.40"
    row["model_id"] = renderer.LEGACY_VOLUME_BREAKOUT_MODEL_ID
    assert renderer.volume_operation_score_label(row) == "操作 4.00 / 最終 93.40"


@pytest.mark.parametrize("model_id", V2_MODELS)
def test_v2_scheduled_dates_have_their_own_line(model_id: str) -> None:
    row = operation_row(
        model_id, row_action_status="active_operation", entry_date="", entry_price="",
        planned_entry_date="20261120", planned_exit_date="20261120", next_action_date="20261120",
    )
    before = row.to_dict()
    for label in (
        renderer.volume_operation_entry_label(row, "confirmed_operation"),
        renderer.volume_operation_exit_label(row),
        renderer.volume_operation_action_label(row),
    ):
        assert "2026/11/20" in label.splitlines()
        assert "排定\n2026/11/20" in label
    assert row.to_dict() == before


@pytest.mark.parametrize("model_id", V2_MODELS)
@pytest.mark.parametrize("missing_column", MANAGEMENT_COLUMNS)
def test_pdf_consumer_rejects_any_missing_v2_management_column(
    model_id: str, missing_column: str
) -> None:
    frame = pdf_adapter_frame(model_id).drop(columns=[missing_column])
    with pytest.raises(RuntimeError, match=missing_column):
        renderer.volume_operation_frame(
            {"volume_operation": frame}, model_id, "full", "active_operation"
        )


@pytest.mark.parametrize("model_id", V2_MODELS)
@pytest.mark.parametrize("missing_column", MANAGEMENT_COLUMNS)
def test_packet_consumer_rejects_any_missing_v2_management_column(
    monkeypatch, model_id: str, missing_column: str
) -> None:
    frame = pd.DataFrame([operation_row(model_id)]).drop(columns=[missing_column])
    monkeypatch.setattr(
        packet, "safe_read_csv",
        lambda path: frame.copy() if path == packet.DAILY_VOLUME_BREAKOUT_OPERATION_SECTION_CSV else pd.DataFrame(),
    )
    with pytest.raises(RuntimeError, match=missing_column):
        packet.build_volume_operation_packet_lines()


def test_complete_empty_state_schema_does_not_invent_operation_values(monkeypatch) -> None:
    frame = pdf_adapter_frame(V2_MODELS[0])
    frame["row_type"] = "empty_state"
    frame["row_action_status"] = "empty_state"
    for field in MANAGEMENT_COLUMNS:
        frame[field] = ""
    before = frame.copy(deep=True)
    result = renderer.volume_operation_frame(
        {"volume_operation": frame}, V2_MODELS[0], "full", "active_operation"
    )
    assert result[list(MANAGEMENT_COLUMNS)].eq("").all().all()
    monkeypatch.setattr(
        packet, "safe_read_csv",
        lambda path: frame.copy() if path == packet.DAILY_VOLUME_BREAKOUT_OPERATION_SECTION_CSV else pd.DataFrame(),
    )
    packet.build_volume_operation_packet_lines()
    pd.testing.assert_frame_equal(frame, before)


def test_legacy_consumer_schema_does_not_acquire_v2_requirements(monkeypatch) -> None:
    frame = pdf_adapter_frame(renderer.LEGACY_VOLUME_BREAKOUT_MODEL_ID).drop(columns=list(MANAGEMENT_COLUMNS))
    assert not renderer.volume_operation_frame(
        {"volume_operation": frame}, renderer.LEGACY_VOLUME_BREAKOUT_MODEL_ID, "full", "active_operation"
    ).empty
    monkeypatch.setattr(
        packet, "safe_read_csv",
        lambda path: frame.copy() if path == packet.DAILY_VOLUME_BREAKOUT_OPERATION_SECTION_CSV else pd.DataFrame(),
    )
    packet.build_volume_operation_packet_lines()
