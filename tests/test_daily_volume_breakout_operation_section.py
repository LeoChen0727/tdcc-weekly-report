from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_volume_breakout_operation_section as builder  # noqa: E402
import build_model_operation_readiness as readiness_builder  # noqa: E402
import build_volume_breakout_confirmed_operation_backtest as operation_backtest  # noqa: E402
import generate_chatgpt_side_daily_reports as pdf_generator  # noqa: E402
import validate_daily_staged_paths as staged_path_validator  # noqa: E402
import validate_daily_pdf_contract_consumers as pdf_contract_validator  # noqa: E402
import validate_daily_volume_breakout_operation_section as section_validator  # noqa: E402
from daily_snapshot_revision_utils import snapshot_file_sha256  # noqa: E402

LOW_VOLUME_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
MID_VOLUME_MODEL_ID = "volume_range_breakout_v2_mid_position_momentum_attack"
HIGH_VOLUME_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"


def approval_stub(**updates: str) -> dict[str, str]:
    row = {
        "approval_source": "approved_operation_patterns_latest.csv",
        "approved_for_daily": "True",
        "operation_module_approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_module_id": "volume_range_breakout_v2_low_position_operation_v1",
        "approval_version": "volume_range_breakout_v2_formal_operation_20260709",
        "operation_directive_level": "approved_daily_operation_guidance",
        "row_action_status": "",
        "buy_rank_eligible": "False",
        "buy_filter_id": "pos120_low_all_shapes_next_day_continuation_d15_stop",
        "best_evidence_sample_size": "26",
        "best_evidence_win_rate": "80.7692",
        "best_evidence_median_return": "18.7857",
        "best_evidence_confidence_status": "approved",
        "best_evidence_out_of_sample_pass": "not_applicable",
        "volume_v2_neutral_rate_pct": "0.0000",
        "volume_v2_loss_rate_pct": "19.2308",
        "volume_v2_avg_return_pct": "28.7704",
        "approval_note_zh": "approved for test",
    }
    row.update(updates)
    return row


def model_approval_stub(model_id: str, **updates: str) -> dict[str, str]:
    model_updates = {
        LOW_VOLUME_MODEL_ID: {},
        MID_VOLUME_MODEL_ID: {
            "operation_module_id": "volume_range_breakout_v2_mid_position_operation_v1",
            "buy_filter_id": "pos120_mid_non_consolidation_or_wide_next_day_continuation_d15_stop",
            "best_evidence_sample_size": "25",
            "best_evidence_win_rate": "80.0000",
            "best_evidence_median_return": "14.6953",
            "volume_v2_neutral_rate_pct": "0.0000",
            "volume_v2_loss_rate_pct": "20.0000",
            "volume_v2_avg_return_pct": "12.7599",
        },
        HIGH_VOLUME_MODEL_ID: {
            "operation_module_id": "volume_range_breakout_v2_high_position_operation_v1",
            "approval_version": "volume_range_breakout_v2_high_position_operation_20260710",
            "buy_filter_id": "pos120_high_nonconsolidation_or_wide_ma60_gt_ma120_next_day_continuation_d15_stop",
            "best_evidence_sample_size": "231",
            "best_evidence_win_rate": "62.3377",
            "best_evidence_median_return": "6.6055",
            "volume_v2_neutral_rate_pct": "0.0000",
            "volume_v2_loss_rate_pct": "37.6623",
            "volume_v2_avg_return_pct": "9.4824",
        },
    }[model_id]
    model_updates.update(updates)
    return approval_stub(**model_updates)


def pdf_summary_approval_rows() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "entry_rule_zh": "確認日收盤後成立，下一個交易日開盤買入。",
                "exit_rule_zh": "若未觸發停損，固定第15個交易日收盤出場。",
                "stop_loss_rule_zh": "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。",
                "best_evidence_win_rate": "80.7692",
                "best_evidence_median_return": "18.7857",
            },
            {
                "model_id": MID_VOLUME_MODEL_ID,
                "entry_rule_zh": "確認日收盤後成立，下一個交易日開盤買入。",
                "exit_rule_zh": "若未觸發停損，固定第15個交易日收盤出場。",
                "stop_loss_rule_zh": "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。",
                "best_evidence_win_rate": "80.0000",
                "best_evidence_median_return": "14.6953",
            },
            {
                "model_id": HIGH_VOLUME_MODEL_ID,
                "entry_rule_zh": "確認日收盤後成立，下一個交易日開盤買入。",
                "exit_rule_zh": "收盤停損或 D+15 收盤出場。",
                "stop_loss_rule_zh": "收盤連續4天低於 MA20/EMA23 較低者 4%，隔日開盤停損。",
                "best_evidence_win_rate": "62.3377",
                "best_evidence_median_return": "6.6055",
            },
            {
                "model_id": "w_bottom_right_side",
                "entry_rule_zh": "右低點觀察訊號成立後，下一個交易日開盤買進。",
                "exit_rule_zh": "若 D+20 收盤報酬達 +10% 則 D+20 收盤出場；否則持有到 D+40 收盤。",
                "stop_loss_rule_zh": "收盤跌破 W 結構低點出場。",
                "w_bottom_mature_sample_size": "31",
                "w_bottom_neutral_count": "0",
                "w_bottom_loss_count": "13",
                "w_bottom_pure_win_rate_pct": "58.0645",
                "w_bottom_avg_return_pct": "11.2532",
            },
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "entry_rule_zh": "3個交易日內收盤相對原始回測進場價達+1%，下一個交易日開盤買進。",
                "exit_rule_zh": "20個交易日內收盤報酬先達+10%為勝；先達+5%後回落到<=+5%且未達+10%為和局；否則第20日收盤歸為操作規則敗。",
                "stop_loss_rule_zh": "v1不升級固定收盤停損；以20個交易日操作規則判定勝、和、敗。",
                "neckline_pure_win_rate_pct": "63.8889",
                "neckline_neutral_inclusive_success_rate_pct": "74.5098",
                "neckline_avg_return_pct": "4.3784",
            },
            {
                "model_id": "price_pullback_23ema",
                "entry_rule_zh": "確認日成立後隔日開盤買入。",
                "exit_rule_zh": "收盤突破訊號日前20日高點後，隔日開盤賣出。",
                "stop_loss_rule_zh": "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。",
                "price_pullback_win_rate_pct": "66.03",
                "price_pullback_neutral_rate_pct": "5.60",
                "price_pullback_failure_rate_pct": "28.36",
                "price_pullback_avg_return_pct": "2.90",
                "price_pullback_technical_package_win_rate_pct": "75.54",
                "price_pullback_technical_package_neutral_rate_pct": "3.52",
                "price_pullback_technical_package_failure_rate_pct": "20.95",
                "price_pullback_technical_package_avg_return_pct": "2.96",
            },
        ]
    ).fillna("")


def test_pdf_operation_model_summary_uses_standard_contract_tokens() -> None:
    inputs = {"approved_operation_patterns": pdf_summary_approval_rows()}

    for model_id in pdf_generator.OPERATION_TABLE_MODEL_IDS:
        summary = pdf_generator.operation_model_summary_text(inputs, model_id)
        for token in pdf_generator.OPERATION_MODEL_SUMMARY_REQUIRED_TOKENS:
            assert token in summary
        assert "下一個交易日" not in summary

    assert "勝率80.77%" in pdf_generator.operation_model_summary_text(inputs, LOW_VOLUME_MODEL_ID)
    assert "和局0.00%" in pdf_generator.operation_model_summary_text(inputs, "w_bottom_right_side")
    assert "含和局成功率74.51%" in pdf_generator.operation_model_summary_text(
        inputs,
        "neckline_volume_breakout_confirmation",
    )
    assert "技術強勢組合績效：勝率75.54%" in pdf_generator.operation_model_summary_text(
        inputs,
        "price_pullback_23ema",
    )


def test_pdf_operation_model_summary_renders_each_contract_token_as_own_line() -> None:
    inputs = {"approved_operation_patterns": pdf_summary_approval_rows()}

    lines = pdf_generator.operation_model_summary_lines(inputs, LOW_VOLUME_MODEL_ID)

    assert len(lines) == len(pdf_generator.OPERATION_MODEL_SUMMARY_REQUIRED_TOKENS)
    for line, token in zip(lines, pdf_generator.OPERATION_MODEL_SUMMARY_REQUIRED_TOKENS):
        assert line.startswith(token)
    for line, next_token in zip(lines, pdf_generator.OPERATION_MODEL_SUMMARY_REQUIRED_TOKENS[1:]):
        assert next_token not in line
    assert pdf_generator.OPERATION_MODEL_SAMPLING_TEXT in lines
    assert lines.count(pdf_generator.OPERATION_MODEL_SAMPLING_TEXT) == 1


def test_pdf_required_model_text_validation_does_not_infer_operation_empty_rows_from_candidates() -> None:
    inputs = {
        "model_registry": pd.DataFrame(
            [
                {
                    "model_id": LOW_VOLUME_MODEL_ID,
                    "model_name_zh": "Low Operation Model",
                    "model_registry_order": "1",
                    "model_registry_active": "True",
                    "report_line_applicability": "both",
                },
                {
                    "model_id": HIGH_VOLUME_MODEL_ID,
                    "model_name_zh": "High Operation Model",
                    "model_registry_order": "2",
                    "model_registry_active": "True",
                    "report_line_applicability": "both",
                },
                {
                    "model_id": "tdcc_stealth_accumulation",
                    "model_name_zh": "Non Operation Model",
                    "model_registry_order": "3",
                    "model_registry_active": "True",
                    "report_line_applicability": "both",
                },
            ]
        ),
        "model_parameters": pd.DataFrame(
            [
                {"model_id": LOW_VOLUME_MODEL_ID, "pdf_visibility": "pdf_core_model"},
                {"model_id": HIGH_VOLUME_MODEL_ID, "pdf_visibility": "pdf_core_model"},
                {"model_id": "tdcc_stealth_accumulation", "pdf_visibility": "pdf_core_model"},
            ]
        ),
        "model_readiness": pd.DataFrame(
            [
                {
                    "model_id": LOW_VOLUME_MODEL_ID,
                    "presentation_allowed": "True",
                    "pdf_integration_status": "pdf_integrated_daily_adapter",
                },
                {
                    "model_id": HIGH_VOLUME_MODEL_ID,
                    "presentation_allowed": "True",
                    "pdf_integration_status": "pdf_integrated_daily_adapter",
                },
            ]
        ),
        "model_signals": pd.DataFrame(
            columns=["model_id", "report_line", "stock_id", "model_rank", "display_rank", "model_score"]
        ),
    }
    text = (
        "Low Operation Model High Operation Model Non Operation Model "
        f"{pdf_generator.MODEL_EMPTY_STATE_TEXT}"
    )

    missing = pdf_generator.required_stock_model_text_missing(inputs, "mainstream", text)

    assert missing == []


def test_pdf_stock_model_summary_marks_numeric_tokens_red() -> None:
    markup = pdf_generator.stock_model_summary_markup(
        "v1 uses 10 trading days, win 58.06%, return +8.39%, watch D+20/D+40, model 23EMA"
    )

    assert f'<font color="{pdf_generator.PDF_RED}">v1</font>' in markup
    assert f'<font color="{pdf_generator.PDF_RED}">10</font>' in markup
    assert f'<font color="{pdf_generator.PDF_RED}">58.06%</font>' in markup
    assert f'<font color="{pdf_generator.PDF_RED}">+8.39%</font>' in markup
    assert f'<font color="{pdf_generator.PDF_RED}">D+20/D+40</font>' in markup
    assert "23EMA" in markup
    assert f'<font color="{pdf_generator.PDF_RED}">23</font>EMA' not in markup


def test_pdf_stock_model_sampling_sentence_is_fully_red() -> None:
    markup = pdf_generator.stock_model_summary_markup(pdf_generator.OPERATION_MODEL_SAMPLING_TEXT)

    assert markup == (
        f'<font color="{pdf_generator.PDF_RED}">'
        f"{pdf_generator.escape_html(pdf_generator.OPERATION_MODEL_SAMPLING_TEXT)}</font>"
    )


def test_pdf_stock_model_title_styles_are_blue() -> None:
    expected = pdf_generator.colors.HexColor(pdf_generator.PDF_MODEL_TITLE_BLUE)

    assert pdf_generator.MODEL_H1.textColor == expected
    assert pdf_generator.MODEL_H2.textColor == expected


def test_operation_section_label_helper_reserves_table_start_room_without_full_table_keep() -> None:
    table_flowable = object()
    story: list = []

    pdf_generator.append_section_label_with_table(story, pdf_generator.OPERATION_ACTIVE_TABLE_TITLE, table_flowable)

    assert isinstance(story[0], pdf_generator.CondPageBreak)
    assert getattr(story[0], "height", None) == pdf_generator.OPERATION_SECTION_TABLE_START_MIN_ROOM
    assert story[-1] is table_flowable
    assert getattr(story[1], "keepWithNext", 0) in (0, None, False)


def test_operation_section_label_helper_uses_short_room_for_empty_tables() -> None:
    table_flowable = pdf_generator.build_table([["TITLE"], ["HEADER"], ["EMPTY"]], [40 * pdf_generator.mm], 12.0)
    story: list = []

    pdf_generator.append_section_label_with_table(story, pdf_generator.OPERATION_ACTIVE_TABLE_TITLE, table_flowable)

    assert isinstance(story[0], pdf_generator.CondPageBreak)
    assert getattr(story[0], "height", None) == pdf_generator.OPERATION_SECTION_SHORT_TABLE_START_MIN_ROOM
    assert story[-1] is table_flowable


def volume_signal(
    stock_id: str = "1234",
    signal_date: str = "20260616",
    rank: str = "1",
    model_id: str = LOW_VOLUME_MODEL_ID,
) -> dict[str, str]:
    return {
        "model_id": model_id,
        "signal_date": signal_date,
        "stock_id": stock_id,
        "stock_name": "測試股",
        "display_rank": rank,
        "model_score": "70",
        "same_model_repeat_status_zh": "新進榜",
        "next_confirmation_zh": "等待隔日續強 / 回測 5MA / 回測 10MA",
        "risk_tags_zh": "依模型風險欄位管理",
    }


def formal_summary(
    trigger_id: str = "next_day_continuation_confirmed",
    tdcc_list_type: str = "no_tdcc",
    rank_bucket: str = "all",
    confluence_scope: str = "operation_trigger",
    confluence_id: str = "all_confirmed_volume_breakout",
    sample_size: str = "30",
    win_rate: str = "60",
    avg_return: str = "3.5",
    median_return: str = "2.5",
    score: str = "18",
    oos: str = "True",
    approved_for_daily: str = "True",
    risk_notes_zh: str = "approved formal daily evidence",
    model_id: str = LOW_VOLUME_MODEL_ID,
) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": model_id,
                "tdcc_list_type": tdcc_list_type,
                "rank_bucket": rank_bucket,
                "trigger_id": trigger_id,
                "confluence_scope": confluence_scope,
                "confluence_id": confluence_id,
                "sample_size": sample_size,
                "win_rate": win_rate,
                "avg_return": avg_return,
                "median_return": median_return,
                "ranking_research_score": score,
                "out_of_sample_pass": oos,
                "approved_for_daily": approved_for_daily,
                "risk_notes_zh": risk_notes_zh,
                "confidence_status": "中",
                "metric_sample_scope": "mature_selected_operation_only",
            }
        ]
    )


def refresh_legacy_snapshot_manifest(snapshot_dir: Path) -> None:
    specs = (
        (
            "daily_candidate_model_signals_for_report_*.csv",
            "daily_candidate_model_signals_for_report_",
            "model_signals_for_report",
        ),
        (
            "daily_volume_breakout_operation_section_*.csv",
            "daily_volume_breakout_operation_section_",
            "volume_breakout_operation_section",
        ),
        (
            "daily_volume_breakout_operation_evidence_audit_*.csv",
            "daily_volume_breakout_operation_evidence_audit_",
            "volume_breakout_operation_evidence_audit",
        ),
    )
    rows: list[dict[str, str]] = []
    for pattern, prefix, artifact_id in specs:
        for path in sorted(snapshot_dir.glob(pattern)):
            report_date = path.stem.removeprefix(prefix)
            if len(report_date) != 8 or not report_date.isdigit():
                continue
            rows.append(
                {
                    "snapshot_report_date": report_date,
                    "artifact_id": artifact_id,
                    "snapshot_path": path.as_posix(),
                    "snapshot_sha256": snapshot_file_sha256(path),
                }
            )
    pd.DataFrame(
        rows,
        columns=[
            "snapshot_report_date",
            "artifact_id",
            "snapshot_path",
            "snapshot_sha256",
        ],
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )


def patch_lifecycle_sources(monkeypatch, tmp_path: Path, stock_id: str, price_rows: list[dict[str, str]]) -> Path:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    signal_log = tmp_path / "output" / "history" / "daily_candidate_models" / "daily_candidate_model_signal_log.csv"
    price_dir = tmp_path / "data" / "stock_price_history"
    snapshot_dir.mkdir(parents=True)
    signal_log.parent.mkdir(parents=True)
    price_dir.mkdir(parents=True)
    pd.DataFrame(columns=["signal_date", "model_id", "stock_id", "stock_name"]).to_csv(signal_log, index=False)
    pd.DataFrame(price_rows).to_csv(price_dir / f"{stock_id}.csv", index=False)
    monkeypatch.setattr(builder, "MODEL_SNAPSHOT_DIR", snapshot_dir)
    monkeypatch.setattr(builder, "MODEL_SIGNAL_LOG_CSV", signal_log)
    monkeypatch.setattr(builder, "STOCK_PRICE_HISTORY_DIR", price_dir)
    original_signal_snapshot_paths = builder.signal_snapshot_paths

    def signal_snapshot_paths(report_date: str):
        refresh_legacy_snapshot_manifest(snapshot_dir)
        return original_signal_snapshot_paths(report_date)

    monkeypatch.setattr(builder, "signal_snapshot_paths", signal_snapshot_paths)
    return snapshot_dir


def write_operation_snapshot(
    snapshot_dir: Path,
    snapshot_date: str,
    signal_date: str,
    stock_id: str = "1234",
    pdf_section: str = "confirmed_operation",
    row_action_status: str = "confirmed_buy_candidate",
    buy_rank_eligible: str = "True",
    selected_confirmation_date: str | None = None,
    model_id: str = LOW_VOLUME_MODEL_ID,
) -> None:
    selected_confirmation_date = selected_confirmation_date or snapshot_date
    pd.DataFrame(
        [
            {
                "stock_id": stock_id,
                "model_id": model_id,
                "stock_name": "TestCo",
                "signal_date": signal_date,
                "selected_confirmation_date": selected_confirmation_date,
                "row_type": "data",
                "pdf_section": pdf_section,
                "row_action_status": row_action_status,
                "buy_rank_eligible": buy_rank_eligible,
            }
        ]
    ).to_csv(snapshot_dir / f"daily_volume_breakout_operation_section_{snapshot_date}.csv", index=False)
    refresh_legacy_snapshot_manifest(snapshot_dir)


def build_rows_for_test(
    signals: pd.DataFrame,
    report_date: str,
    summary: pd.DataFrame,
    approval_overrides: dict[str, str] | None = None,
    model_id: str = LOW_VOLUME_MODEL_ID,
) -> pd.DataFrame:
    rows, _audit = build_rows_and_audit_for_test(
        signals,
        report_date,
        summary,
        approval_overrides,
        model_id,
    )
    return rows


def build_rows_and_audit_for_test(
    signals: pd.DataFrame,
    report_date: str,
    summary: pd.DataFrame,
    approval_overrides: dict[str, str] | None = None,
    model_id: str = LOW_VOLUME_MODEL_ID,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    approval = model_approval_stub(model_id, **(approval_overrides or {}))
    rows, audit = builder.build_lifecycle_rows(
        signals,
        report_date,
        int(signals["stock_id"].nunique()) if not signals.empty else 0,
        {model_id: approval},
        "2026-06-17 12:00:00 Asia/Taipei",
        summary,
    )
    return (
        pd.DataFrame(rows, columns=builder.OUTPUT_COLUMNS),
        pd.DataFrame(audit, columns=builder.EVIDENCE_AUDIT_COLUMNS),
    )


def complete_section_for_validator(rows: pd.DataFrame, report_date: str) -> pd.DataFrame:
    completed = rows.to_dict("records")
    existing = {
        (str(row.get("model_id", "")), str(row.get("pdf_view", "")), str(row.get("pdf_section", "")))
        for row in completed
        if str(row.get("row_type", "")) == "data"
    }
    for model_id in (LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID):
        approval = model_approval_stub(model_id)
        for pdf_view in builder.PDF_VIEWS:
            for pdf_section in builder.PDF_SECTIONS:
                if not builder.section_allowed_for_pdf_view(pdf_view, pdf_section):
                    continue
                if (model_id, pdf_view, pdf_section) in existing:
                    continue
                completed.append(
                    builder.empty_row(
                        model_id,
                        pdf_view,
                        pdf_section,
                        "ready",
                        report_date,
                        1,
                        approval,
                        "2026-06-17 12:00:00 Asia/Taipei",
                        report_date,
                    )
                )
    return pd.DataFrame(completed, columns=builder.OUTPUT_COLUMNS)


def high_position_price_rows() -> pd.DataFrame:
    dates = pd.date_range(end=pd.to_datetime("2026-06-17"), periods=120, freq="D").strftime("%Y%m%d")
    rows: list[dict[str, object]] = []
    for idx, date in enumerate(dates):
        close = 90.0 if idx < 60 else 100.0
        rows.append(
            {
                "date": date,
                "stock_id": "5678",
                "stock_name": "HighCo",
                "open": close,
                "high": close + 2,
                "low": close - 2,
                "close": close,
                "volume": 1000,
                "ma20": 100.0,
                "ma60": 99.0,
                "ema23": 100.0,
                "volume_ratio": 3.0,
                "previous_60d_high_calc": 104.0,
                "limit_up_like": "False",
            }
        )
    rows[-2].update({"open": 106.0, "high": 110.0, "low": 100.0, "close": 108.0})
    rows[-1].update({"open": 109.0, "high": 112.0, "low": 107.0, "close": 111.0})
    return pd.DataFrame(rows)


def test_high_position_confirmed_row_uses_exact_bonus_combo_metric(monkeypatch) -> None:
    monkeypatch.setattr(builder, "tdcc_events", lambda: pd.DataFrame())
    monkeypatch.setattr(builder, "market_regime_map", lambda: {})
    price = high_position_price_rows()
    signal_idx = len(price) - 2
    report_idx = len(price) - 1
    selected = {
        "trigger_id": "next_day_continuation_confirmed",
        "matched_trigger_ids": "next_day_continuation_confirmed",
        "confirmation_idx": report_idx,
        "confirmation_date": "20260617",
        "trigger_priority": 1,
        "trigger_zh": "隔日續攻",
    }
    signal = pd.Series(
        {
            "model_id": HIGH_VOLUME_MODEL_ID,
            "signal_date": "20260616",
            "stock_id": "5678",
            "stock_name": "HighCo",
            "display_rank": "1",
            "model_score": "88",
            "volume_position_bucket_120d": "high_pos_gt75",
            "volume_shape_bucket": "non_consolidation",
        }
    )
    approval = approval_stub(
        operation_module_id="volume_range_breakout_v2_high_position_operation_v1",
        approval_version="volume_range_breakout_v2_high_position_operation_20260710",
        buy_filter_id="pos120_high_nonconsolidation_or_wide_ma60_gt_ma120_next_day_continuation_d15_stop",
        best_evidence_sample_size="231",
        best_evidence_win_rate="62.3377",
        best_evidence_median_return="6.6055",
        volume_v2_neutral_rate_pct="0.0000",
        volume_v2_loss_rate_pct="37.6623",
        volume_v2_avg_return_pct="9.4824",
    )
    evidence, context, _audit = builder.model_level_evidence(signal, selected, approval)

    record = builder.confirmed_record(
        signal,
        selected,
        evidence,
        context,
        price,
        signal_idx,
        report_idx,
        approval,
        "2026-06-17 12:00:00 Asia/Taipei",
        "20260617",
        1,
        "1",
    )

    assert record["quality_status_zh"] == "正向證據"
    assert record["adapter_note_zh"] == (
        "由 v2 正式模型條件與 close-only 確認產生；不使用舊 v1 hidden evidence gate。"
    )
    assert record["sample_size"] == "231"
    assert record["win_rate_zh"] == "62.34%"
    assert record["neutral_rate_zh"] == "0.00%"
    assert record["loss_rate_zh"] == "37.66%"
    assert record["failure_rate_zh"] == "37.66%"
    assert record["avg_return_zh"] == "9.48%"
    assert record["pdf_bonus_combo_id"] == "pdf_combo__not_limit_up_like__breakout_2_5__signal_body_le3__close_location_le80"
    assert record["pdf_bonus_combo_source"] == "exact_combo_metric"
    assert record["pdf_bonus_combo_sample_size"] == "6"
    assert record["pdf_bonus_combo_win_rate_zh"] == "100.00%"
    assert record["pdf_bonus_combo_loss_rate_zh"] == "0.00%"
    assert record["pdf_bonus_combo_avg_return_zh"] == "+18.25%"
    assert record["row_metric_status"] == "ready"
    assert record["row_metric_scope"] == "exact_combo"
    assert record["row_metric_id"] == record["pdf_bonus_combo_id"]
    assert record["row_metric_win_rate_zh"] == record["pdf_bonus_combo_win_rate_zh"]
    assert record["row_metric_failure_rate_zh"] == record["pdf_bonus_combo_failure_rate_zh"]
    assert record["row_metric_avg_return_zh"] == record["pdf_bonus_combo_avg_return_zh"]


def output_row(**updates: str) -> dict[str, str]:
    row = {col: "" for col in builder.OUTPUT_COLUMNS}
    row.update(
        {
            "model_id": LOW_VOLUME_MODEL_ID,
            "pdf_view": "highlight",
            "pdf_section": "confirmed_operation",
            "row_type": "empty_state",
            "operation_asof_date": "20260615",
            "operation_source_date_status": "ready",
            "display_order": "0",
            "operation_status": "confirmed_operation",
            "row_action_status": "empty_state",
            "buy_rank_eligible": "False",
            "generated_at": "2026-06-16 08:00:00 Asia/Taipei",
        }
    )
    row.update(updates)
    return row


def audit_row(**updates: str) -> dict[str, str]:
    row = {col: "" for col in builder.EVIDENCE_AUDIT_COLUMNS}
    row.update(
        {
            "model_id": LOW_VOLUME_MODEL_ID,
            "operation_asof_date": "20260615",
            "stock_id": "1234",
            "signal_date": "20260615",
            "operation_lifecycle_state": "confirmed_operation",
            "audit_status": "candidate_evaluated",
            "included_in_daily_adapter": "False",
            "generated_at": "2026-06-16 08:00:00 Asia/Taipei",
        }
    )
    row.update(updates)
    return row


def lineage_audit_row(**updates: str) -> dict[str, str]:
    source_sha = "a" * 64
    row = {
        "snapshot_report_date": "20260716",
        "snapshot_revision": "r1",
        "signal_date": "20260716",
        "model_id": HIGH_VOLUME_MODEL_ID,
        "stock_id": "6505",
        "formal_row_disposition": "verified_clean",
        "evidence_status": "complete",
        "paired_source_resolution": "current_worktree_exact_source_files",
        "production_code_sha256": source_sha,
        "formal_snapshot_path": "formal.csv",
        "formal_snapshot_sha256": source_sha,
        "formal_row_number": "0",
        "formal_row_sha256": source_sha,
        "watch_artifact_sha256": source_sha,
        "candidate_artifact_sha256": source_sha,
        "official_warrant_artifact_sha256": source_sha,
        "candidate_row_present": "True",
        "canonical_warrant_source_type": "all_candidates_projection",
        "candidate_warrant_signal": "call_strong_inflow",
        "formal_warrant_signal": "call_strong_inflow",
        "impact_scope": "none",
    }
    row.update(updates)
    return row


def lineage_operation_section(**updates: str) -> pd.DataFrame:
    row = {
        "signal_date": "20260716",
        "model_id": HIGH_VOLUME_MODEL_ID,
        "stock_id": "6505",
        "row_type": "data",
        "pdf_section": "confirmed_operation",
    }
    row.update(updates)
    return pd.DataFrame([row])


def lineage_formal_signal_row(**updates: str) -> dict[str, str]:
    row = {
        "signal_date": "20260716",
        "report_line": "mainstream",
        "model_id": HIGH_VOLUME_MODEL_ID,
        "stock_id": "6505",
        "source_row_index": "volume_breakout:0",
        "warrant_flow_signal": "call_strong_inflow",
        "base_model_score": "72",
        "operation_score": "10",
        "tdcc_score": "4",
        "pattern_score": "6",
        "risk_penalty": "0",
        "final_rank_score": "92",
        "model_rank": "1",
    }
    row.update(updates)
    return row


def write_lineage_fixture(
    tmp_path: Path,
    *,
    formal_updates: dict[str, str] | None = None,
    audit_updates: dict[str, str] | None = None,
    source_relative_path: str = (
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260716.csv"
    ),
) -> tuple[Path, Path, pd.DataFrame]:
    source_path = tmp_path / source_relative_path
    source_path.parent.mkdir(parents=True, exist_ok=True)
    formal = pd.DataFrame([lineage_formal_signal_row(**(formal_updates or {}))])
    formal.to_csv(source_path, index=False)
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(
        [
            {
                "snapshot_report_date": "20260716",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "legacy_v1_manifest",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": source_relative_path.replace("\\", "/"),
                "snapshot_sha256": snapshot_file_sha256(source_path),
            }
        ]
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )
    resolved_audit_updates = {
        "formal_snapshot_path": source_relative_path.replace("\\", "/"),
        "formal_snapshot_sha256": builder.canonical_text_sha256(source_path.read_bytes()),
        "formal_row_number": "0",
        "formal_row_sha256": builder.canonical_row_sha256(formal.iloc[0]),
    }
    resolved_audit_updates.update(audit_updates or {})
    audit = lineage_audit_row(**resolved_audit_updates)
    audit_path = tmp_path / "lineage.csv"
    pd.DataFrame([audit]).to_csv(audit_path, index=False)
    return audit_path, source_path, formal


def write_20260807_2059_lineage_scope_fixture(
    tmp_path: Path,
) -> tuple[Path, pd.DataFrame, pd.DataFrame]:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    source_relative_path = (
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260807.csv"
    )
    source_path = tmp_path / source_relative_path
    formal = pd.DataFrame(
        [
            lineage_formal_signal_row(
                signal_date="20260807",
                stock_id="2059",
                source_row_index="volume_breakout:0",
                warrant_flow_signal="",
                final_rank_score="96",
                model_rank="1",
            ),
            lineage_formal_signal_row(
                signal_date="20260807",
                stock_id="6505",
                source_row_index="volume_breakout:1",
                model_rank="2",
            ),
        ]
    )
    formal.to_csv(source_path, index=False)
    snapshot_sha = snapshot_file_sha256(source_path)
    canonical_snapshot_sha = builder.canonical_text_sha256(source_path.read_bytes())
    pd.DataFrame(
        [
            {
                "snapshot_report_date": "20260807",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "legacy_v1_manifest",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": source_relative_path,
                "snapshot_sha256": snapshot_sha,
            }
        ]
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )
    audit_path = tmp_path / "lineage.csv"
    pd.DataFrame(
        [
            lineage_audit_row(
                snapshot_report_date="20260807",
                signal_date="20260807",
                stock_id="2059",
                formal_row_disposition="superseded",
                evidence_status="complete",
                paired_source_resolution=(
                    "published_snapshot_exact_current_sources_pending_commit"
                ),
                formal_snapshot_path=source_relative_path,
                formal_snapshot_sha256=canonical_snapshot_sha,
                formal_row_number="0",
                formal_row_sha256=builder.canonical_row_sha256(formal.iloc[0]),
                candidate_row_present="False",
                canonical_warrant_source_type=(
                    "negative_projection_no_candidate_row"
                ),
                candidate_warrant_signal="",
                formal_warrant_signal="",
                impact_scope="formal_warrant_lineage_superseded",
            ),
            lineage_audit_row(
                snapshot_report_date="20260807",
                signal_date="20260807",
                stock_id="6505",
                formal_row_disposition="verified_clean",
                evidence_status="complete",
                paired_source_resolution=(
                    "published_snapshot_exact_current_sources_pending_commit"
                ),
                formal_snapshot_path=source_relative_path,
                formal_snapshot_sha256=canonical_snapshot_sha,
                formal_row_number="1",
                formal_row_sha256=builder.canonical_row_sha256(formal.iloc[1]),
            ),
        ]
    ).to_csv(audit_path, index=False)
    section = pd.DataFrame(
        [
            output_row(
                model_id=HIGH_VOLUME_MODEL_ID,
                row_type="data",
                pdf_view="highlight",
                pdf_section="confirmed_operation",
                stock_id="2059",
                signal_date="20260807",
                display_order="1",
            ),
            output_row(
                model_id=HIGH_VOLUME_MODEL_ID,
                row_type="data",
                pdf_view="highlight",
                pdf_section="confirmed_operation",
                stock_id="6505",
                signal_date="20260807",
                display_order="2",
            ),
        ],
        columns=builder.OUTPUT_COLUMNS,
    )
    return audit_path, formal, section


def test_20260807_2059_negative_projection_is_excluded_before_formal_adapter(
    tmp_path: Path,
) -> None:
    audit_path, formal, section = write_20260807_2059_lineage_scope_fixture(
        tmp_path
    )

    scoped, excluded_keys = builder.filter_volume_v2_operation_lineage_scope(
        section,
        audit_path=audit_path,
        formal_signal_rows=formal,
        source_root=tmp_path,
    )

    assert excluded_keys == {
        ("20260807", HIGH_VOLUME_MODEL_ID, "2059")
    }
    assert scoped["stock_id"].tolist() == ["6505"]
    evidence = builder.require_verified_clean_volume_v2_lineage(
        scoped,
        audit_path=audit_path,
        formal_signal_rows=formal,
        source_root=tmp_path,
    )
    assert evidence["checked_rows"] == 1
    with pytest.raises(RuntimeError, match="stock_id.*2059|2059"):
        builder.require_verified_clean_volume_v2_lineage(
            section,
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )
    pdf_rows = pdf_generator.volume_operation_frame(
        {"volume_operation": scoped},
        HIGH_VOLUME_MODEL_ID,
        "highlight",
        "confirmed_operation",
    )
    assert pdf_rows["stock_id"].tolist() == ["6505"]


def test_20260807_candidate_present_superseded_row_still_fails_closed(
    tmp_path: Path,
) -> None:
    audit_path, formal, section = write_20260807_2059_lineage_scope_fixture(
        tmp_path
    )
    audit = pd.read_csv(audit_path, dtype=str, keep_default_na=False)
    audit.loc[0, "candidate_row_present"] = "True"
    audit.loc[0, "canonical_warrant_source_type"] = "all_candidates_projection"
    audit.to_csv(audit_path, index=False)

    scoped, excluded_keys = builder.filter_volume_v2_operation_lineage_scope(
        section,
        audit_path=audit_path,
        formal_signal_rows=formal,
        source_root=tmp_path,
    )

    assert excluded_keys == set()
    with pytest.raises(RuntimeError, match="superseded"):
        builder.require_verified_clean_volume_v2_lineage(
            scoped,
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


def test_20260807_old_negative_revision_does_not_override_verified_manifest_max(
    tmp_path: Path,
) -> None:
    audit_path, _r1_formal, section = write_20260807_2059_lineage_scope_fixture(
        tmp_path
    )
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    r2_formal = pd.DataFrame(
        [
            lineage_formal_signal_row(
                signal_date="20260807",
                stock_id="2059",
                source_row_index="volume_breakout:0",
                warrant_flow_signal="no_signal",
                final_rank_score="96",
                model_rank="1",
            ),
            lineage_formal_signal_row(
                signal_date="20260807",
                stock_id="6505",
                source_row_index="volume_breakout:1",
                model_rank="2",
            ),
        ]
    )
    staging = snapshot_dir / "model_signals_20260807_r2_staging.csv"
    r2_formal.to_csv(staging, index=False)
    r2_sha = snapshot_file_sha256(staging)
    r2_path = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_20260807_r2_{r2_sha[:12]}.csv"
    )
    staging.rename(r2_path)
    r2_relative = r2_path.relative_to(tmp_path).as_posix()
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    r1_sha = manifest.iloc[0]["snapshot_sha256"]
    manifest.loc[len(manifest)] = {
        "snapshot_report_date": "20260807",
        "snapshot_revision": "r2",
        "supersedes_snapshot_sha256": r1_sha,
        "revision_reason": "candidate_scope_correction",
        "artifact_id": "model_signals_for_report",
        "snapshot_path": r2_relative,
        "snapshot_sha256": r2_sha,
    }
    manifest.to_csv(manifest_path, index=False)
    canonical_r2_sha = builder.canonical_text_sha256(r2_path.read_bytes())
    audit = pd.read_csv(audit_path, dtype=str, keep_default_na=False)
    audit = pd.concat(
        [
            audit,
            pd.DataFrame(
                [
                    lineage_audit_row(
                        snapshot_report_date="20260807",
                        snapshot_revision="r2",
                        signal_date="20260807",
                        stock_id="2059",
                        formal_row_disposition="verified_clean",
                        formal_snapshot_path=r2_relative,
                        formal_snapshot_sha256=canonical_r2_sha,
                        formal_row_number="0",
                        formal_row_sha256=builder.canonical_row_sha256(
                            r2_formal.iloc[0]
                        ),
                        candidate_row_present="True",
                        canonical_warrant_source_type="all_candidates_projection",
                        candidate_warrant_signal="no_signal",
                        formal_warrant_signal="no_signal",
                        impact_scope="none",
                    ),
                    lineage_audit_row(
                        snapshot_report_date="20260807",
                        snapshot_revision="r2",
                        signal_date="20260807",
                        stock_id="6505",
                        formal_row_disposition="verified_clean",
                        formal_snapshot_path=r2_relative,
                        formal_snapshot_sha256=canonical_r2_sha,
                        formal_row_number="1",
                        formal_row_sha256=builder.canonical_row_sha256(
                            r2_formal.iloc[1]
                        ),
                    ),
                ]
            ),
        ],
        ignore_index=True,
    )
    audit.to_csv(audit_path, index=False)

    scoped, excluded_keys = builder.filter_volume_v2_operation_lineage_scope(
        section,
        audit_path=audit_path,
        formal_signal_rows=r2_formal,
        source_root=tmp_path,
    )

    assert excluded_keys == set()
    assert scoped["stock_id"].tolist() == ["2059", "6505"]
    evidence = builder.require_verified_clean_volume_v2_lineage(
        scoped,
        audit_path=audit_path,
        formal_signal_rows=r2_formal,
        source_root=tmp_path,
    )
    assert evidence["checked_rows"] == 2


def test_20260807_conflicting_manifest_max_audit_rows_fail_closed(
    tmp_path: Path,
) -> None:
    audit_path, formal, section = write_20260807_2059_lineage_scope_fixture(
        tmp_path
    )
    audit = pd.read_csv(audit_path, dtype=str, keep_default_na=False)
    conflicting = audit.iloc[0].copy()
    conflicting["candidate_row_present"] = "True"
    conflicting["canonical_warrant_source_type"] = "all_candidates_projection"
    conflicting["formal_row_disposition"] = "verified_clean"
    audit = pd.concat([audit, conflicting.to_frame().T], ignore_index=True)
    audit.to_csv(audit_path, index=False)

    with pytest.raises(
        RuntimeError,
        match="duplicate_manifest_max_negative_projection_evidence",
    ):
        builder.filter_volume_v2_operation_lineage_scope(
            section,
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


@pytest.mark.parametrize(
    ("field", "value", "error_text"),
    [
        ("evidence_status", "incomplete", "incomplete_negative_projection"),
        ("paired_source_resolution", "unknown", "incomplete_negative_projection"),
        ("watch_artifact_sha256", "", "incomplete_negative_projection"),
        ("formal_row_sha256", "b" * 64, "formal_row_exact_hash_mismatch"),
    ],
)
def test_20260807_negative_projection_exclusion_requires_complete_exact_lineage(
    tmp_path: Path,
    field: str,
    value: str,
    error_text: str,
) -> None:
    audit_path, formal, section = write_20260807_2059_lineage_scope_fixture(
        tmp_path
    )
    audit = pd.read_csv(audit_path, dtype=str, keep_default_na=False)
    audit.loc[0, field] = value
    audit.to_csv(audit_path, index=False)

    with pytest.raises(RuntimeError, match=error_text):
        builder.filter_volume_v2_operation_lineage_scope(
            section,
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


def test_restored_2059_operation_audit_is_not_marked_included(
    tmp_path: Path,
) -> None:
    audit_path, formal, section = write_20260807_2059_lineage_scope_fixture(
        tmp_path
    )
    only_2059 = section[section["stock_id"].eq("2059")].copy()
    scoped, excluded_keys = builder.filter_volume_v2_operation_lineage_scope(
        only_2059,
        audit_path=audit_path,
        formal_signal_rows=formal,
        source_root=tmp_path,
    )
    approvals = {
        model_id: builder.approval_context(pd.DataFrame(), model_id)
        for model_id in builder.FORMAL_MODEL_IDS
    }
    restored_section = builder.ensure_operation_section_empty_states(
        scoped,
        report_date="20260807",
        daily_signal_date="20260807",
        daily_volume_count=1,
        approvals_by_model=approvals,
        generated_at="2026-08-08 08:00:00 Asia/Taipei",
        metadata_source=only_2059,
    )
    operation_audit = pd.DataFrame(
        [
            audit_row(
                model_id=HIGH_VOLUME_MODEL_ID,
                signal_date="20260807",
                stock_id="2059",
                included_in_daily_adapter="True",
            ),
            audit_row(
                model_id=HIGH_VOLUME_MODEL_ID,
                signal_date="20260807",
                stock_id="6505",
                included_in_daily_adapter="True",
            ),
        ],
        columns=builder.EVIDENCE_AUDIT_COLUMNS,
    )

    restored_audit = builder.suppress_excluded_operation_audit_rows(
        operation_audit, excluded_keys
    )

    assert scoped.empty
    restored_target = restored_section[
        restored_section["model_id"].eq(HIGH_VOLUME_MODEL_ID)
        & restored_section["pdf_view"].eq("highlight")
        & restored_section["pdf_section"].eq("confirmed_operation")
    ]
    assert len(restored_target) == 1
    assert restored_target.iloc[0]["row_type"] == "empty_state"
    assert restored_target.iloc[0]["stock_id"] == ""
    assert not restored_section["stock_id"].eq("2059").any()
    assert restored_audit.set_index("stock_id").loc[
        "2059", "included_in_daily_adapter"
    ] == "False"
    assert restored_audit.set_index("stock_id").loc[
        "6505", "included_in_daily_adapter"
    ] == "True"


def test_formal_operation_lineage_gate_accepts_only_exact_verified_clean_row(tmp_path: Path) -> None:
    audit_path, _source_path, formal = write_lineage_fixture(tmp_path)

    evidence = builder.require_verified_clean_volume_v2_lineage(
        lineage_operation_section(),
        audit_path=audit_path,
        formal_signal_rows=formal,
        source_root=tmp_path,
    )

    assert evidence["checked_rows"] == 1
    assert len(evidence["audit_sha256"]) == 64
    assert evidence["formal_row_disposition"] == "verified_clean"
    assert evidence["evidence_status"] == "complete"


@pytest.mark.parametrize(
    "stock_id",
    ["6243", "6505"],
)
def test_formal_operation_lineage_gate_accepts_manifest_history_same_commit_sources(
    tmp_path: Path,
    stock_id: str,
) -> None:
    audit_path, _source_path, formal = write_lineage_fixture(
        tmp_path,
        formal_updates={"stock_id": stock_id},
        audit_updates={
            "stock_id": stock_id,
            "paired_source_resolution": (
                builder.MANIFEST_HISTORY_SAME_COMMIT_RESOLUTION
            ),
        },
    )

    evidence = builder.require_verified_clean_volume_v2_lineage(
        lineage_operation_section(stock_id=stock_id),
        audit_path=audit_path,
        formal_signal_rows=formal,
        source_root=tmp_path,
    )

    assert evidence["checked_rows"] == 1
    assert evidence["formal_row_disposition"] == "verified_clean"


@pytest.mark.parametrize(
    "source_resolution",
    ["unknown_resolution", "legacy_same_canonical_publication_fallback_incomplete"],
)
def test_formal_operation_lineage_gate_rejects_unapproved_source_resolution(
    tmp_path: Path,
    source_resolution: str,
) -> None:
    audit_path, _source_path, formal = write_lineage_fixture(
        tmp_path,
        audit_updates={"paired_source_resolution": source_resolution},
    )

    with pytest.raises(RuntimeError, match=source_resolution):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(),
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("formal_row_disposition", "quarantined"),
        ("evidence_status", "incomplete"),
        ("watch_artifact_sha256", ""),
    ],
)
def test_formal_operation_lineage_gate_rejects_invalid_same_commit_evidence(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    audit_path, _source_path, formal = write_lineage_fixture(
        tmp_path,
        audit_updates={
            "paired_source_resolution": (
                builder.MANIFEST_HISTORY_SAME_COMMIT_RESOLUTION
            ),
            field: value,
        },
    )

    with pytest.raises(RuntimeError, match="quarantined|incomplete|missing_or_invalid"):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(),
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


def test_formal_operation_lineage_gate_selects_manifest_max_same_day_revision(
    tmp_path: Path,
) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    r1 = snapshot_dir / "daily_candidate_model_signals_for_report_20260716.csv"
    r1_formal = pd.DataFrame(
        [lineage_formal_signal_row(final_rank_score="91")]
    )
    r1_formal.to_csv(r1, index=False)
    r1_sha = snapshot_file_sha256(r1)
    r2_staging = snapshot_dir / "model_signals_r2_staging.csv"
    r2_formal = pd.DataFrame([lineage_formal_signal_row()])
    r2_formal.to_csv(r2_staging, index=False)
    r2_sha = snapshot_file_sha256(r2_staging)
    r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_20260716_r2_{r2_sha[:12]}.csv"
    )
    r2_staging.rename(r2)
    r1_relative = r1.relative_to(tmp_path).as_posix()
    r2_relative = r2.relative_to(tmp_path).as_posix()
    pd.DataFrame(
        [
            {
                "snapshot_report_date": "20260716",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "legacy_v1_manifest",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": r1_relative,
                "snapshot_sha256": r1_sha,
            },
            {
                "snapshot_report_date": "20260716",
                "snapshot_revision": "r2",
                "supersedes_snapshot_sha256": r1_sha,
                "revision_reason": "same_day_correction",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": r2_relative,
                "snapshot_sha256": r2_sha,
            },
        ]
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )
    r1_canonical_sha = builder.canonical_text_sha256(r1.read_bytes())
    r2_canonical_sha = builder.canonical_text_sha256(r2.read_bytes())
    audit_path = tmp_path / "lineage.csv"
    pd.DataFrame(
        [
            lineage_audit_row(
                snapshot_revision="r2",
                formal_snapshot_path=r2_relative,
                formal_snapshot_sha256=r2_canonical_sha,
                formal_row_sha256=builder.canonical_row_sha256(r2_formal.iloc[0]),
            ),
            lineage_audit_row(
                snapshot_revision="r1",
                formal_row_disposition="superseded",
                formal_snapshot_path=r1_relative,
                formal_snapshot_sha256=r1_canonical_sha,
                formal_row_sha256=builder.canonical_row_sha256(r1_formal.iloc[0]),
            ),
            lineage_audit_row(
                audit_row_type="revision_coverage",
                snapshot_report_date="20260715",
                snapshot_revision="legacy_r1",
                signal_date="",
                model_id="",
                stock_id="",
                formal_row_disposition="not_applicable_revision_coverage",
            ),
        ]
    ).to_csv(audit_path, index=False)

    evidence = builder.require_verified_clean_volume_v2_lineage(
        lineage_operation_section(),
        audit_path=audit_path,
        formal_signal_rows=r2_formal,
        source_root=tmp_path,
    )

    assert evidence["checked_rows"] == 1
    assert evidence["formal_row_disposition"] == "verified_clean"


def write_20260804_r1_lineage_fixture_with_legacy_history(
    tmp_path: Path,
) -> tuple[Path, pd.DataFrame]:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    current_snapshot = (
        snapshot_dir / "daily_candidate_model_signals_for_report_20260804.csv"
    )
    formal = pd.DataFrame(
        [lineage_formal_signal_row(signal_date="20260804")]
    )
    formal.to_csv(current_snapshot, index=False)
    current_sha = snapshot_file_sha256(current_snapshot)
    current_relative = current_snapshot.relative_to(tmp_path).as_posix()
    pd.DataFrame(
        [
            {
                "snapshot_report_date": "20260804",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "legacy_v1_manifest",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": current_relative,
                "snapshot_sha256": current_sha,
            }
        ]
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )
    audit_path = tmp_path / "lineage.csv"
    pd.DataFrame(
        [
            lineage_audit_row(
                audit_row_type="revision_coverage",
                snapshot_report_date="20260717",
                snapshot_revision="legacy_r1",
                signal_date="",
                model_id="",
                stock_id="",
                formal_row_disposition="not_applicable_revision_coverage",
            ),
            lineage_audit_row(
                audit_row_type="revision_coverage",
                snapshot_report_date="20260717",
                snapshot_revision="legacy_r2",
                signal_date="",
                model_id="",
                stock_id="",
                formal_row_disposition="not_applicable_revision_coverage",
            ),
            lineage_audit_row(
                audit_row_type="revision_coverage",
                snapshot_report_date="20260717",
                snapshot_revision="legacy_r7",
                signal_date="",
                model_id="",
                stock_id="",
                formal_row_disposition="not_applicable_revision_coverage",
            ),
            lineage_audit_row(
                audit_row_type="formal_row",
                snapshot_report_date="20260804",
                snapshot_revision="r1",
                signal_date="20260804",
                formal_snapshot_path=current_relative,
                formal_snapshot_sha256=builder.canonical_text_sha256(
                    current_snapshot.read_bytes()
                ),
                formal_row_number="0",
                formal_row_sha256=builder.canonical_row_sha256(formal.iloc[0]),
            ),
        ]
    ).to_csv(audit_path, index=False)
    return audit_path, formal


def test_formal_operation_lineage_gate_accepts_20260804_r1_with_recovered_legacy_history(
    tmp_path: Path,
) -> None:
    audit_path, formal = write_20260804_r1_lineage_fixture_with_legacy_history(
        tmp_path
    )

    evidence = builder.require_verified_clean_volume_v2_lineage(
        lineage_operation_section(signal_date="20260804"),
        audit_path=audit_path,
        formal_signal_rows=formal,
        source_root=tmp_path,
    )

    assert evidence["checked_rows"] == 1
    assert evidence["formal_row_disposition"] == "verified_clean"


@pytest.mark.parametrize(
    "invalid_revision",
    [
        "",
        "legacy_r0",
        "legacy_r01",
        "legacy_r",
        "legacy_r1.0",
        "legacy_x1",
        "r0",
        "r01",
        "1",
    ],
)
def test_formal_operation_lineage_gate_rejects_malformed_audit_revision_namespace(
    tmp_path: Path,
    invalid_revision: str,
) -> None:
    audit_path, formal = write_20260804_r1_lineage_fixture_with_legacy_history(
        tmp_path
    )
    audit = pd.read_csv(audit_path, dtype=str, keep_default_na=False)
    audit.loc[0, "snapshot_revision"] = invalid_revision
    audit.to_csv(audit_path, index=False)

    with pytest.raises(RuntimeError, match="invalid snapshot_revision rows"):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(signal_date="20260804"),
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


def test_formal_operation_lineage_gate_does_not_treat_legacy_revision_as_manifest_r1(
    tmp_path: Path,
) -> None:
    audit_path, formal = write_20260804_r1_lineage_fixture_with_legacy_history(
        tmp_path
    )
    audit = pd.read_csv(audit_path, dtype=str, keep_default_na=False)
    audit.loc[3, "snapshot_revision"] = "legacy_r1"
    audit.to_csv(audit_path, index=False)

    with pytest.raises(RuntimeError, match="uncovered_manifest_max_lineage_evidence"):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(signal_date="20260804"),
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


@pytest.mark.parametrize("disposition", ["superseded", "quarantined", "unreplayable"])
def test_formal_operation_lineage_gate_rejects_non_clean_rows(
    tmp_path: Path,
    disposition: str,
) -> None:
    audit_path, _source_path, formal = write_lineage_fixture(
        tmp_path,
        audit_updates={"formal_row_disposition": disposition},
    )

    with pytest.raises(RuntimeError, match=disposition):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(),
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


def test_formal_operation_lineage_gate_rejects_uncovered_row(tmp_path: Path) -> None:
    audit_path, _source_path, formal = write_lineage_fixture(
        tmp_path,
        audit_updates={"stock_id": "6243"},
    )

    with pytest.raises(RuntimeError, match="uncovered"):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(),
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


def test_formal_operation_lineage_gate_rejects_incomplete_current_source_hashes(
    tmp_path: Path,
) -> None:
    audit_path, _source_path, formal = write_lineage_fixture(
        tmp_path,
        audit_updates={"watch_artifact_sha256": ""},
    )

    with pytest.raises(RuntimeError, match="missing_or_invalid"):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(),
            audit_path=audit_path,
            formal_signal_rows=formal,
            source_root=tmp_path,
        )


def test_formal_operation_lineage_gate_does_not_reclassify_legacy_rows(tmp_path: Path) -> None:
    evidence = builder.require_verified_clean_volume_v2_lineage(
        lineage_operation_section(model_id=builder.LEGACY_MODEL_ID),
        audit_path=tmp_path / "missing.csv",
    )

    assert evidence["checked_rows"] == 0


@pytest.mark.parametrize(
    ("field", "changed_value"),
    [
        ("warrant_flow_signal", "watch_only_collision"),
        ("final_rank_score", "91"),
        ("model_rank", "2"),
    ],
)
def test_formal_operation_lineage_gate_rejects_same_key_changed_current_row(
    tmp_path: Path,
    field: str,
    changed_value: str,
) -> None:
    audit_path, _source_path, formal = write_lineage_fixture(tmp_path)
    changed = formal.copy()
    changed.loc[0, field] = changed_value

    with pytest.raises(RuntimeError, match="current_formal_row_exact_hash_mismatch"):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(),
            audit_path=audit_path,
            formal_signal_rows=changed,
            source_root=tmp_path,
        )


def test_formal_operation_lineage_gate_rejects_stale_formal_snapshot_source(
    tmp_path: Path,
) -> None:
    audit_path, source_path, formal = write_lineage_fixture(tmp_path)
    changed = formal.copy()
    changed.loc[0, "final_rank_score"] = "91"
    changed.to_csv(source_path, index=False)

    with pytest.raises(RuntimeError, match="daily snapshot SHA-256 mismatch"):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(),
            audit_path=audit_path,
            source_root=tmp_path,
        )


def test_formal_operation_lineage_gate_rejects_stale_formal_row_hash(
    tmp_path: Path,
) -> None:
    audit_path, _source_path, _formal = write_lineage_fixture(
        tmp_path,
        audit_updates={"formal_row_sha256": "b" * 64},
    )

    with pytest.raises(RuntimeError, match="formal_row_exact_hash_mismatch"):
        builder.require_verified_clean_volume_v2_lineage(
            lineage_operation_section(),
            audit_path=audit_path,
            source_root=tmp_path,
        )


def test_restored_operation_snapshot_requires_exact_historical_formal_row(
    monkeypatch,
    tmp_path: Path,
) -> None:
    audit_path, source_path, _formal = write_lineage_fixture(
        tmp_path,
        source_relative_path=(
            "output/history/daily_model_snapshots/"
            "daily_candidate_model_signals_for_report_20260716.csv"
        ),
        audit_updates={
            "paired_source_resolution": "snapshot_history_exact_blob_fallback",
        },
    )
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    section_rows = [
        output_row(model_id=LOW_VOLUME_MODEL_ID),
        output_row(model_id=MID_VOLUME_MODEL_ID),
        output_row(
            model_id=HIGH_VOLUME_MODEL_ID,
            row_type="data",
            stock_id="6505",
            signal_date="20260716",
        ),
    ]
    pd.DataFrame(section_rows).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_section_20260716.csv",
        index=False,
    )
    pd.DataFrame(columns=builder.EVIDENCE_AUDIT_COLUMNS).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_evidence_audit_20260716.csv",
        index=False,
    )
    refresh_legacy_snapshot_manifest(snapshot_dir)
    monkeypatch.setattr(builder, "MODEL_SNAPSHOT_DIR", snapshot_dir)

    restored = builder.restore_published_snapshot("20260716")
    assert restored is not None
    evidence = builder.require_verified_clean_volume_v2_lineage(
        restored[0],
        audit_path=audit_path,
        source_root=tmp_path,
    )
    assert evidence["checked_rows"] == 1

    source_path.unlink()
    with pytest.raises(RuntimeError, match="daily snapshot file is missing"):
        builder.require_verified_clean_volume_v2_lineage(
            restored[0],
            audit_path=audit_path,
            source_root=tmp_path,
        )


def test_build_reuses_existing_published_operation_snapshot(monkeypatch, tmp_path) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    latest_dir.mkdir(parents=True)
    snapshot_dir.mkdir(parents=True)
    pd.DataFrame(
        [
            {
                "main_price_date": "20260615",
                "report_ready": "True",
                "daily_pdf_ready": "True",
            }
        ]
    ).to_csv(latest_dir / "data_freshness_latest.csv", index=False)
    pd.DataFrame([volume_signal("9999", "20260615")]).to_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
    )
    pd.DataFrame([{"model_id": LOW_VOLUME_MODEL_ID, **approval_stub()}]).to_csv(
        latest_dir / "approved_operation_patterns_latest.csv",
        index=False,
    )
    formal_summary().to_csv(latest_dir / "approved_formal_summary.csv", index=False)
    pd.DataFrame([output_row(stock_id="", stock_display="目前無資料")]).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_section_20260615.csv",
        index=False,
    )
    snapshot_rows = []
    for model_id in [LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID]:
        for pdf_view in builder.PDF_VIEWS:
            for pdf_section in builder.PDF_SECTIONS:
                if not builder.section_allowed_for_pdf_view(pdf_view, pdf_section):
                    continue
                snapshot_rows.append(
                    output_row(
                        model_id=model_id,
                        pdf_view=pdf_view,
                        pdf_section=pdf_section,
                        operation_status=pdf_section,
                    )
                )
    pd.DataFrame(snapshot_rows).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_section_20260615.csv",
        index=False,
    )
    pd.DataFrame([audit_row()]).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_evidence_audit_20260615.csv",
        index=False,
    )
    refresh_legacy_snapshot_manifest(snapshot_dir)

    monkeypatch.setattr(builder, "MODEL_SNAPSHOT_DIR", snapshot_dir)
    monkeypatch.setattr(builder, "DAILY_SIGNALS_CSV", latest_dir / "daily_candidate_model_signals_for_report_latest.csv")
    monkeypatch.setattr(builder, "APPROVAL_CSV", latest_dir / "approved_operation_patterns_latest.csv")
    monkeypatch.setattr(builder, "FORMAL_SUMMARY_CSV", latest_dir / "approved_formal_summary.csv")
    monkeypatch.setattr(builder, "DATA_FRESHNESS_CSV", latest_dir / "data_freshness_latest.csv")
    monkeypatch.delenv(builder.ALLOW_SNAPSHOT_REWRITE_ENV, raising=False)

    section, audit = builder.build()

    assert len(section) == len(snapshot_rows)
    assert set(section["model_id"]) == {LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID}
    assert set(section["stock_id"]) == {""}
    assert set(section["row_type"]) == {"empty_state"}
    assert audit["stock_id"].tolist() == ["1234"]


def test_build_allows_empty_published_operation_evidence_audit_snapshot(monkeypatch, tmp_path) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    latest_dir.mkdir(parents=True)
    snapshot_dir.mkdir(parents=True)
    pd.DataFrame(
        [
            {
                "main_price_date": "20260615",
                "report_ready": "True",
                "daily_pdf_ready": "True",
            }
        ]
    ).to_csv(latest_dir / "data_freshness_latest.csv", index=False)
    pd.DataFrame([volume_signal("9999", "20260615")]).to_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
    )
    pd.DataFrame([{"model_id": LOW_VOLUME_MODEL_ID, **approval_stub()}]).to_csv(
        latest_dir / "approved_operation_patterns_latest.csv",
        index=False,
    )
    formal_summary().to_csv(latest_dir / "approved_formal_summary.csv", index=False)
    snapshot_rows = []
    for model_id in [LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID]:
        for pdf_view in builder.PDF_VIEWS:
            for pdf_section in builder.PDF_SECTIONS:
                if not builder.section_allowed_for_pdf_view(pdf_view, pdf_section):
                    continue
                snapshot_rows.append(
                    output_row(
                        model_id=model_id,
                        pdf_view=pdf_view,
                        pdf_section=pdf_section,
                        operation_status=pdf_section,
                    )
                )
    pd.DataFrame(snapshot_rows).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_section_20260615.csv",
        index=False,
    )
    pd.DataFrame(columns=builder.EVIDENCE_AUDIT_COLUMNS).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_evidence_audit_20260615.csv",
        index=False,
    )
    refresh_legacy_snapshot_manifest(snapshot_dir)

    monkeypatch.setattr(builder, "MODEL_SNAPSHOT_DIR", snapshot_dir)
    monkeypatch.setattr(builder, "DAILY_SIGNALS_CSV", latest_dir / "daily_candidate_model_signals_for_report_latest.csv")
    monkeypatch.setattr(builder, "APPROVAL_CSV", latest_dir / "approved_operation_patterns_latest.csv")
    monkeypatch.setattr(builder, "FORMAL_SUMMARY_CSV", latest_dir / "approved_formal_summary.csv")
    monkeypatch.setattr(builder, "DATA_FRESHNESS_CSV", latest_dir / "data_freshness_latest.csv")
    monkeypatch.delenv(builder.ALLOW_SNAPSHOT_REWRITE_ENV, raising=False)

    section, audit = builder.build()

    assert len(section) == len(snapshot_rows)
    assert list(audit.columns) == builder.EVIDENCE_AUDIT_COLUMNS
    assert audit.empty


def backtest_lifecycle_state(stock_id: str, signal_date: str, report_date: str) -> str:
    price = builder.load_price_history(stock_id)
    signal_positions = price.index[price["date"].astype(str).eq(signal_date)].tolist()
    report_positions = price.index[price["date"].astype(str).eq(report_date)].tolist()
    assert signal_positions
    assert report_positions
    lifecycle = operation_backtest.lifecycle_state_for_signal(
        price,
        int(signal_positions[-1]),
        int(report_positions[-1]),
    )
    return str(lifecycle["operation_lifecycle_state"])


def test_lifecycle_keeps_unconfirmed_signal_pending(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.2", "high": "10.7", "low": "10.4", "close": "10.5", "volume": "900"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert pending["stock_id"].tolist() == ["1234"]
    assert pending["pdf_view"].tolist() == ["full"]
    assert set(pending["pending_age_zh"]) == {"D+1 待確認"}
    assert set(pending["row_action_status"]) == {"pending_confirmation"}
    assert set(pending["buy_rank_eligible"]) == {"False"}
    assert pending["selected_trigger_id"].eq("").all()
    assert backtest_lifecycle_state("1234", "20260616", "20260617") == "pending_confirmation"


def test_lifecycle_confirms_signal_on_report_date(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert confirmed["stock_id"].tolist() == ["1234", "1234"]
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}
    assert set(confirmed["selected_trigger_id"]) == {"next_day_continuation_confirmed"}
    assert set(confirmed["confirmation_date"]) == {"20260617"}
    assert pending.empty
    assert backtest_lifecycle_state("1234", "20260616", "20260617") == "confirmed_operation"


@pytest.mark.parametrize(
    "model_id",
    [LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID],
)
def test_each_v2_model_covers_pending_confirmed_active_lifecycle(monkeypatch, tmp_path, model_id: str) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {
                "date": "20260616",
                "open": "10",
                "high": "11",
                "low": "9",
                "close": "10",
                "volume": "1000",
                "ma20": "10",
                "ma60": "9",
                "ma120": "8",
                "ema23": "10",
            },
            {
                "date": "20260617",
                "open": "10.6",
                "high": "12",
                "low": "10.9",
                "close": "11.5",
                "volume": "1200",
                "ma20": "10.2",
                "ma60": "9.2",
                "ma120": "8.2",
                "ema23": "10.1",
            },
            {
                "date": "20260618",
                "open": "11.7",
                "high": "12.5",
                "low": "11.2",
                "close": "12",
                "volume": "1100",
                "ma20": "10.4",
                "ma60": "9.4",
                "ma120": "8.4",
                "ema23": "10.3",
            },
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616", model_id=model_id)]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )
    summary = formal_summary(model_id=model_id)

    pending_rows = build_rows_for_test(pd.DataFrame(), "20260616", summary, model_id=model_id)
    pending = pending_rows[
        pending_rows["pdf_section"].eq("pending_confirmation")
        & pending_rows["row_type"].eq("data")
    ]
    assert pending["stock_id"].tolist() == ["1234"]

    confirmed_rows = build_rows_for_test(pd.DataFrame(), "20260617", summary, model_id=model_id)
    confirmed = confirmed_rows[
        confirmed_rows["pdf_section"].eq("confirmed_operation")
        & confirmed_rows["row_type"].eq("data")
    ]
    assert confirmed["stock_id"].tolist() == ["1234", "1234"]
    assert set(confirmed["quality_status_zh"]) == {"正向證據"}
    assert set(confirmed["adapter_note_zh"]) == {
        "由 v2 正式模型條件與 close-only 確認產生；不使用舊 v1 hidden evidence gate。"
    }

    write_operation_snapshot(
        snapshot_dir,
        "20260617",
        "20260616",
        model_id=model_id,
    )
    active_rows = build_rows_for_test(pd.DataFrame(), "20260618", summary, model_id=model_id)
    active = active_rows[
        active_rows["pdf_section"].eq("active_operation")
        & active_rows["row_type"].eq("data")
    ]
    assert active["stock_id"].tolist() == ["1234", "1234"]
    assert set(active["entry_date"]) == {"20260618"}
    assert set(active["entry_price"]) == {"11.7"}


@pytest.mark.parametrize(
    "model_id",
    [LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID],
)
def test_builder_confirmed_rows_pass_complete_operation_artifact_validator(
    monkeypatch,
    tmp_path,
    capsys,
    model_id: str,
) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616", model_id=model_id)]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )
    summary = formal_summary(model_id=model_id)
    rows, audit = build_rows_and_audit_for_test(
        pd.DataFrame(),
        "20260617",
        summary,
        model_id=model_id,
    )
    section = complete_section_for_validator(rows, "20260617")
    taxonomy_path = tmp_path / "stock_theme_taxonomy_latest.csv"
    pd.DataFrame(
        [{"stock_id": "1234", "report_line_memberships": "mainstream|non_mainstream"}]
    ).to_csv(taxonomy_path, index=False)
    monkeypatch.setattr(section_validator, "TAXONOMY_CSV", taxonomy_path)

    section_validator.validate_operation_artifacts(section, summary, audit)

    invalid = section.copy()
    confirmed_mask = invalid["pdf_section"].eq("confirmed_operation") & invalid["row_type"].eq("data")
    invalid.loc[confirmed_mask, "quality_status_zh"] = "已通過 v2 模型條件與 close-only 確認"
    with pytest.raises(SystemExit):
        section_validator.validate_operation_artifacts(invalid, summary, audit)
    assert "confirmed operation rows must be positive evidence only" in capsys.readouterr().out


@pytest.mark.parametrize(
    "model_id",
    [LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID],
)
def test_builder_active_model_contract_rows_pass_complete_validator_without_legacy_trigger_evidence(
    monkeypatch,
    tmp_path,
    capsys,
    model_id: str,
) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260618", "open": "11.7", "high": "12.5", "low": "11.2", "close": "12", "volume": "1100"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616", model_id=model_id)]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )
    write_operation_snapshot(
        snapshot_dir,
        "20260617",
        "20260616",
        model_id=model_id,
    )

    producer_summary = formal_summary(model_id=model_id)
    rows, audit = build_rows_and_audit_for_test(
        pd.DataFrame(),
        "20260618",
        producer_summary,
        model_id=model_id,
    )
    section = complete_section_for_validator(rows, "20260618")
    taxonomy_path = tmp_path / "stock_theme_taxonomy_latest.csv"
    pd.DataFrame(
        [{"stock_id": "1234", "report_line_memberships": "mainstream|non_mainstream"}]
    ).to_csv(taxonomy_path, index=False)
    monkeypatch.setattr(section_validator, "TAXONOMY_CSV", taxonomy_path)
    monkeypatch.setattr(section_validator, "MODEL_SNAPSHOT_DIR", snapshot_dir)

    legacy_row_evidence = formal_summary(
        trigger_id="next_day_break_signal_high_confirmed",
        model_id=model_id,
    )
    section_validator.validate_operation_artifacts(section, legacy_row_evidence, audit)

    invalid = section.copy()
    active_mask = invalid["pdf_section"].eq("active_operation") & invalid["row_type"].eq("data")
    invalid.loc[active_mask, "evidence_match_status"] = "positive_row_evidence"
    with pytest.raises(SystemExit):
        section_validator.validate_operation_artifacts(invalid, legacy_row_evidence, audit)
    assert "active_operation rows use trigger without eligible formal evidence" in capsys.readouterr().out


def test_lifecycle_reads_published_signal_log_when_snapshot_is_missing(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    assert not (snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv").exists()
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        builder.MODEL_SIGNAL_LOG_CSV,
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert confirmed["stock_id"].tolist() == ["1234", "1234"]
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}


def test_lifecycle_does_not_read_selected_volume_history_as_adapter_source(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    assert not (snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv").exists()
    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    assert out.empty


def test_lifecycle_moves_prior_confirmed_signal_to_active(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "12.5", "low": "11.2", "close": "12", "volume": "1100"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260615")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        index=False,
    )
    write_operation_snapshot(snapshot_dir, "20260616", "20260615")

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert active["stock_id"].tolist() == ["1234", "1234"]
    assert confirmed.empty
    assert set(active["row_action_status"]) == {"active_operation"}
    assert set(active["buy_rank_eligible"]) == {"False"}
    assert set(active["selected_trigger_id"]) == {"next_day_continuation_confirmed"}
    assert set(active["confirmation_date"]) == {"20260616"}
    assert backtest_lifecycle_state("1234", "20260615", "20260617") == "active_operation"


def test_lifecycle_does_not_repromote_confirmation_day_unranked_signal_to_active(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "12.5", "low": "11.2", "close": "12", "volume": "1100"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260615")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        index=False,
    )
    write_operation_snapshot(
        snapshot_dir,
        "20260616",
        "20260615",
        pdf_section="confirmed_unranked_operation",
        row_action_status="confirmed_not_buy_ranked",
        buy_rank_eligible="False",
    )

    out, audit = build_rows_and_audit_for_test(pd.DataFrame(), "20260617", formal_summary())

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    assert active.empty
    suppressed = audit[audit["audit_status"].eq("lifecycle_suppressed")]
    assert suppressed["reason"].tolist() == ["confirmation_snapshot_not_buy_ranked_not_tracked_active"]
    assert suppressed["included_in_daily_adapter"].tolist() == ["False"]


def test_lifecycle_does_not_carry_forward_prior_active_without_buy_ranked_confirmation(
    monkeypatch,
    tmp_path,
) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "12.5", "low": "11.2", "close": "12", "volume": "1100"},
            {"date": "20260618", "open": "12.1", "high": "12.8", "low": "11.8", "close": "12.4", "volume": "1000"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260615")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        index=False,
    )
    write_operation_snapshot(
        snapshot_dir,
        "20260616",
        "20260615",
        pdf_section="confirmed_unranked_operation",
        row_action_status="confirmed_not_buy_ranked",
        buy_rank_eligible="False",
    )
    write_operation_snapshot(
        snapshot_dir,
        "20260617",
        "20260615",
        selected_confirmation_date="20260616",
        pdf_section="active_operation",
        row_action_status="active_operation",
        buy_rank_eligible="False",
    )

    out, audit = build_rows_and_audit_for_test(pd.DataFrame(), "20260618", formal_summary())

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    assert active.empty
    suppressed = audit[audit["audit_status"].eq("lifecycle_suppressed")]
    assert suppressed["reason"].tolist() == [
        "confirmation_snapshot_not_buy_ranked_not_tracked_active_despite_prior_active_snapshot"
    ]
    assert suppressed["included_in_daily_adapter"].tolist() == ["False"]


def test_lifecycle_does_not_carry_forward_snapshot_when_evidence_loses_formal_approval(
    monkeypatch,
    tmp_path,
) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "12.5", "low": "11.2", "close": "12", "volume": "1100"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260615")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        index=False,
    )
    write_operation_snapshot(
        snapshot_dir,
        "20260616",
        "20260615",
        pdf_section="confirmed_operation",
        row_action_status="confirmed_buy_candidate",
        buy_rank_eligible="True",
    )

    out, audit = build_rows_and_audit_for_test(
        pd.DataFrame(),
        "20260617",
        formal_summary(risk_notes_zh="approved formal daily evidence"),
        approval_overrides={
            "approved_for_daily": "False",
            "operation_module_approved_for_daily": "False",
            "approval_status": "research_only",
        },
    )

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    assert active.empty
    assert audit[audit["included_in_daily_adapter"].eq("True")].empty
    assert set(audit["reason"]) == {"confirmed_without_buy_rank_eligibility_not_tracked_active"}


def test_volume_operation_validator_rejects_prior_active_without_buy_ranked_confirmation(
    monkeypatch,
    tmp_path,
) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    write_operation_snapshot(
        snapshot_dir,
        "20260616",
        "20260615",
        pdf_section="confirmed_unranked_operation",
        row_action_status="confirmed_not_buy_ranked",
        buy_rank_eligible="False",
    )
    write_operation_snapshot(
        snapshot_dir,
        "20260617",
        "20260615",
        selected_confirmation_date="20260616",
        pdf_section="active_operation",
        row_action_status="active_operation",
        buy_rank_eligible="False",
    )
    monkeypatch.setattr(section_validator, "MODEL_SNAPSHOT_DIR", snapshot_dir)
    active_data = pd.DataFrame(
        [
            {
                "operation_asof_date": "20260618",
                "stock_id": "1234",
                "signal_date": "20260615",
                "selected_confirmation_date": "20260616",
                "row_type": "data",
                "pdf_section": "active_operation",
            }
        ]
    )

    with pytest.raises(SystemExit):
        section_validator.validate_active_confirmation_snapshot_gate(active_data)


def test_active_operation_wins_over_new_confirmed_signal_for_same_stock(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "13", "low": "11.6", "close": "12.8", "volume": "1300"},
        ],
    )
    pd.DataFrame(
        [
            volume_signal("1234", "20260615", "1"),
            volume_signal("1234", "20260616", "2"),
        ]
    ).to_csv(builder.MODEL_SIGNAL_LOG_CSV, index=False)
    write_operation_snapshot(snapshot_dir, "20260616", "20260615")

    out, audit = build_rows_and_audit_for_test(pd.DataFrame(), "20260617", formal_summary())

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert active["stock_id"].tolist() == ["1234", "1234"]
    assert confirmed.empty
    assert set(active["signal_date"]) == {"20260615"}
    assert set(active["confirmation_date"]) == {"20260616"}
    assert set(active["operation_status"]) == {"active_operation"}
    assert set(active["row_action_status"]) == {"active_operation"}
    included = audit[audit["included_in_daily_adapter"].eq("True")]
    assert included[["stock_id", "signal_date"]].drop_duplicates().to_dict("records") == [
        {"stock_id": "1234", "signal_date": "20260615"}
    ]
    suppressed = audit[
        audit["audit_status"].eq("positive_model_contract_evidence")
        & audit["stock_id"].eq("1234")
        & audit["signal_date"].eq("20260616")
    ]
    assert not suppressed.empty
    assert set(suppressed["included_in_daily_adapter"]) == {"False"}


def test_active_operation_audits_new_pending_same_stock_suppression(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "12.5", "low": "11.6", "close": "12", "volume": "1100"},
        ],
    )
    pd.DataFrame(
        [
            volume_signal("1234", "20260615", "1"),
            volume_signal("1234", "20260617", "2"),
        ]
    ).to_csv(builder.MODEL_SIGNAL_LOG_CSV, index=False)
    write_operation_snapshot(snapshot_dir, "20260616", "20260615")

    out, audit = build_rows_and_audit_for_test(pd.DataFrame(), "20260617", formal_summary())

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert set(active["signal_date"]) == {"20260615"}
    assert pending.empty
    suppressed = audit[audit["audit_status"].eq("lifecycle_suppressed")]
    assert suppressed[["stock_id", "signal_date", "operation_lifecycle_state"]].to_dict("records") == [
        {
            "stock_id": "1234",
            "signal_date": "20260617",
            "operation_lifecycle_state": "pending_confirmation",
        }
    ]
    assert set(suppressed["included_in_daily_adapter"]) == {"False"}
    assert set(suppressed["reason"]) == {"same_stock_lifecycle_suppressed_by_active_operation"}
    section_validator.validate_lifecycle_suppression_audit(audit)


def test_lifecycle_collapses_duplicate_signal_sources_without_last_row_overwrite(monkeypatch, tmp_path) -> None:
    patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.2", "high": "10.7", "low": "10.4", "close": "10.5", "volume": "900"},
        ],
    )
    pd.DataFrame(
        [
            {**volume_signal("1234", "20260616"), "report_bucket": "mainstream", "model_rank": "1", "display_rank": ""},
            {**volume_signal("1234", "20260616"), "report_bucket": "non_mainstream", "model_rank": "99", "display_rank": ""},
        ]
    ).to_csv(builder.MODEL_SIGNAL_LOG_CSV, index=False)

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert pending["stock_id"].tolist() == ["1234"]
    assert set(pending["display_order"]) == {"1"}
    assert set(pending["signal_date"]) == {"20260616"}


def test_lifecycle_audits_missing_report_date_price_gap(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.2", "high": "10.7", "low": "10.4", "close": "10.5", "volume": "900"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260615")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        index=False,
    )

    out, audit = build_rows_and_audit_for_test(pd.DataFrame(), "20260617", formal_summary())

    assert out.empty
    assert audit["audit_status"].tolist() == ["source_gap"]
    assert audit["operation_lifecycle_state"].tolist() == ["source_gap"]
    assert audit["included_in_daily_adapter"].tolist() == ["False"]
    assert audit["reason"].tolist() == ["operation_asof_date_missing_in_stock_price_history"]
    section_validator.validate_source_gap_audit(audit)


def test_lifecycle_expired_signal_matches_backtest_terminal_state(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "9.5", "high": "9.8", "low": "8.8", "close": "9.2", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    assert out.empty
    assert backtest_lifecycle_state("1234", "20260616", "20260617") == "expired"


def test_lifecycle_does_not_promote_confirmed_signal_without_positive_evidence(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out = build_rows_for_test(
        pd.DataFrame(),
        "20260617",
        formal_summary(),
        approval_overrides={
            "approved_for_daily": "False",
            "operation_module_approved_for_daily": "False",
            "approval_status": "research_only",
        },
    )

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    unranked = out[out["pdf_section"].eq("confirmed_unranked_operation") & out["row_type"].eq("data")]
    assert confirmed.empty
    assert unranked["stock_id"].tolist() == ["1234"]
    assert unranked["pdf_view"].tolist() == ["full"]
    assert set(unranked["row_action_status"]) == {"confirmed_not_buy_ranked"}
    assert set(unranked["buy_rank_eligible"]) == {"False"}
    assert set(unranked["entry_price"]) == {""}
    assert set(unranked["stop_loss_price"]) == {""}
    assert set(unranked["evidence_match_status"]) == {"model_contract_evidence_not_buy_ranked"}


def test_lifecycle_rejects_row_level_evidence_without_daily_approval(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out, audit = build_rows_and_audit_for_test(
        pd.DataFrame(),
        "20260617",
        formal_summary(risk_notes_zh="approved formal daily evidence"),
        approval_overrides={
            "approved_for_daily": "False",
            "operation_module_approved_for_daily": "False",
            "approval_status": "research_only",
        },
    )

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    unranked = out[out["pdf_section"].eq("confirmed_unranked_operation") & out["row_type"].eq("data")]
    assert confirmed.empty
    assert unranked["stock_id"].tolist() == ["1234"]
    assert set(unranked["row_action_status"]) == {"confirmed_not_buy_ranked"}
    assert set(unranked["buy_rank_eligible"]) == {"False"}
    assert set(unranked["evidence_match_status"]) == {"model_contract_evidence_not_buy_ranked"}
    assert audit[audit["included_in_daily_adapter"].eq("True")].empty


def test_lifecycle_rejects_research_only_row_level_evidence(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out, audit = build_rows_and_audit_for_test(
        pd.DataFrame(),
        "20260617",
        formal_summary(risk_notes_zh="research only; not approved for daily buy gate"),
        approval_overrides={
            "approved_for_daily": "False",
            "operation_module_approved_for_daily": "False",
            "approval_status": "research_only",
        },
    )

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    unranked = out[out["pdf_section"].eq("confirmed_unranked_operation") & out["row_type"].eq("data")]
    assert confirmed.empty
    assert unranked["stock_id"].tolist() == ["1234"]
    assert set(unranked["row_action_status"]) == {"confirmed_not_buy_ranked"}
    assert set(unranked["buy_rank_eligible"]) == {"False"}
    assert set(unranked["evidence_match_status"]) == {"model_contract_evidence_not_buy_ranked"}
    assert audit[audit["included_in_daily_adapter"].eq("True")].empty


def test_lifecycle_does_not_apply_tdcc_top10_evidence_to_no_tdcc_stock(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )
    tdcc_top10_only = formal_summary(
        tdcc_list_type="weekly_increase",
        rank_bucket="top_10",
        sample_size="10",
        win_rate="70",
        avg_return="22.68",
        median_return="21.09",
        score="32.78",
        oos="True",
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", tdcc_top10_only)

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert confirmed["stock_id"].tolist() == ["1234", "1234"]
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}
    assert set(confirmed["evidence_match_status"]) == {"positive_model_contract_evidence"}
    assert set(confirmed["evidence_tdcc_list_type"]) == {"model_level"}
    assert set(confirmed["evidence_confluence_scope"]) == {"model_contract"}
    assert set(confirmed["evidence_confluence_id"]) == {LOW_VOLUME_MODEL_ID}


def test_lifecycle_uses_exact_no_tdcc_row_level_evidence(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )
    summary = pd.concat(
        [
            formal_summary(
                tdcc_list_type="weekly_increase",
                rank_bucket="top_10",
                sample_size="10",
                win_rate="70",
                avg_return="22.68",
                median_return="21.09",
                score="32.78",
                oos="True",
            ),
            formal_summary(
                tdcc_list_type="no_tdcc",
                rank_bucket="all",
                sample_size="22",
                win_rate="55",
                avg_return="4.2",
                median_return="1.8",
                score="9.5",
                oos="True",
            ),
        ],
        ignore_index=True,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", summary)

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert confirmed["stock_id"].tolist() == ["1234", "1234"]
    assert set(confirmed["sample_size"]) == {"26"}
    assert set(confirmed["win_rate_zh"]) == {"80.77%"}
    assert set(confirmed["median_return_zh"]) == {"18.79%"}
    assert set(confirmed["evidence_match_status"]) == {"positive_model_contract_evidence"}
    assert set(confirmed["evidence_tdcc_list_type"]) == {"model_level"}
    assert set(confirmed["evidence_rank_bucket"]) == {"all"}
    assert set(confirmed["evidence_confluence_scope"]) == {"model_contract"}
    assert set(confirmed["evidence_confluence_id"]) == {LOW_VOLUME_MODEL_ID}


def test_daily_signal_context_uses_report_date_as_authority() -> None:
    signals = pd.DataFrame(
        [
            {"model_id": LOW_VOLUME_MODEL_ID, "signal_date": "20260612", "stock_id": "1111"},
            {"model_id": LOW_VOLUME_MODEL_ID, "signal_date": "20260615", "stock_id": "2222"},
            {"model_id": LOW_VOLUME_MODEL_ID, "signal_date": "20260615", "stock_id": "3333"},
        ]
    )

    signal_date, count = builder.daily_signal_context(signals, "20260615")

    assert signal_date == "20260615"
    assert count == 2


def test_daily_signal_context_does_not_promote_stale_model_signal_date() -> None:
    signals = pd.DataFrame(
        [
            {"model_id": LOW_VOLUME_MODEL_ID, "signal_date": "20260612", "stock_id": "1111"},
        ]
    )

    signal_date, count = builder.daily_signal_context(signals, "20260615")

    assert signal_date == "20260615"
    assert count == 0


def test_pdf_volume_operation_uses_taxonomy_for_report_line_fallback() -> None:
    rows = pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "1438",
                "stock_display": "1438 三地開發",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "display_order": "0",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )
    inputs = {
        "stock_theme_taxonomy": pd.DataFrame(
            [
                {
                    "stock_id": "1438",
                    "stock_name": "三地開發",
                    "industry": "建材營造",
                    "report_line_memberships": "non_mainstream",
                    "mainstream_report_eligible": "False",
                    "non_mainstream_report_eligible": "True",
                }
            ]
        )
    }

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "mainstream")
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "non_mainstream")

    assert "1438" not in set(mainstream["stock_id"].astype(str))
    assert "1438" in set(non_mainstream["stock_id"].astype(str))
    assert mainstream[mainstream["row_type"].eq("empty_state")]["stock_display"].tolist() == ["目前無資料"]


def test_pdf_volume_operation_does_not_guess_missing_taxonomy() -> None:
    rows = pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "9999",
                "stock_display": "9999 未分類",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            }
        ]
    )

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, {}, "mainstream")
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, {}, "non_mainstream")

    assert mainstream.empty
    assert non_mainstream.empty


def test_pdf_volume_operation_ignores_non_string_membership_values() -> None:
    rows = pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "6209",
                "stock_display": "6209 今國光",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "2",
                "stock_id": "6668",
                "stock_display": "6668 中揚光",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
        ]
    )
    inputs = {
        "stock_theme_taxonomy": pd.DataFrame(
            [
                {
                    "stock_id": "6209",
                    "report_line_memberships": float("nan"),
                    "taxonomy_report_line_memberships": 3.14,
                },
                {
                    "stock_id": "6668",
                    "report_line_memberships": "mainstream|non_mainstream",
                    "taxonomy_report_line_memberships": float("nan"),
                },
            ]
        )
    }

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "mainstream")
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "non_mainstream")

    assert set(mainstream["stock_id"].astype(str)) == {"6668"}
    assert set(non_mainstream["stock_id"].astype(str)) == {"6668"}


def test_daily_pipeline_runs_volume_breakout_operation_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")

    builder_command = "python scripts/build_daily_volume_breakout_operation_section.py"
    output_validator_command = (
        "python scripts/validate_daily_volume_breakout_operation_section.py --output-only"
    )
    full_validator_command = "python scripts/validate_daily_volume_breakout_operation_section.py"
    staged_path_command = "python scripts/validate_daily_staged_paths.py"
    artifact_names = (
        "daily_volume_breakout_operation_section_latest.csv",
        "daily_volume_breakout_operation_section_latest.md",
        "daily_volume_breakout_operation_evidence_audit_latest.csv",
        "daily_volume_breakout_operation_evidence_audit_latest.md",
    )
    copy_commands = [
        f"cp output/latest/{name} docs/latest/{name}" for name in artifact_names
    ]
    stage_lines = ["          git add -- \\"]
    for index, name in enumerate(artifact_names):
        suffix = " \\" if index < len(artifact_names) - 1 else ""
        stage_lines.append(f"            docs/latest/{name}{suffix}")
    exact_stage_block = "\n".join(stage_lines)

    builder_index = workflow.index(builder_command)
    output_validator_index = workflow.index(output_validator_command)
    copy_indices = [workflow.index(command) for command in copy_commands]
    stage_index = workflow.index(exact_stage_block)
    full_validator_index = workflow.index(full_validator_command, output_validator_index + 1)
    staged_path_index = workflow.index(staged_path_command, full_validator_index + 1)

    assert builder_index < output_validator_index < min(copy_indices)
    assert max(copy_indices) < stage_index < full_validator_index < staged_path_index
    assert workflow.count(output_validator_command) == 1
    assert workflow.count(full_validator_command) == 2
    for command in copy_commands:
        assert f"{command} || true" not in workflow
    assert f"{exact_stage_block} || true" not in workflow
    assert "git add docs/latest/daily_volume_breakout_operation_*" not in workflow


def test_volume_operation_builder_owns_output_only() -> None:
    source = (ROOT / "scripts" / "build_daily_volume_breakout_operation_section.py").read_text(
        encoding="utf-8"
    )

    assert "DOCS_LATEST_DIR" not in source
    assert "docs/latest" not in source


def test_volume_operation_staged_mirror_registry_is_complete() -> None:
    expected = {
        "daily_volume_breakout_operation_section_latest.csv",
        "daily_volume_breakout_operation_section_latest.md",
        "daily_volume_breakout_operation_evidence_audit_latest.csv",
        "daily_volume_breakout_operation_evidence_audit_latest.md",
    }

    assert expected <= set(staged_path_validator.DAILY_CANDIDATE_DOCS_MIRROR_FILES)


def test_staged_mirror_validator_rejects_git_index_drift(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    output_dir = tmp_path / "output" / "latest"
    docs_dir = tmp_path / "docs" / "latest"
    output_dir.mkdir(parents=True)
    docs_dir.mkdir(parents=True)
    name = "daily_volume_breakout_operation_section_latest.csv"
    (output_dir / name).write_bytes(b"same-worktree\r\n")
    (docs_dir / name).write_bytes(b"same-worktree\r\n")
    indexed = {
        f"output/latest/{name}": b"canonical-index\n",
        f"docs/latest/{name}": b"stale-index\n",
    }

    monkeypatch.setattr(staged_path_validator, "LATEST_DIR", output_dir)
    monkeypatch.setattr(staged_path_validator, "DOCS_LATEST_DIR", docs_dir)
    monkeypatch.setattr(staged_path_validator, "DAILY_CANDIDATE_DOCS_MIRROR_FILES", (name,))
    monkeypatch.setattr(staged_path_validator, "INDICATOR_GUIDE_MIRROR_FILES", ())
    monkeypatch.setattr(
        staged_path_validator,
        "index_file_bytes",
        lambda relative_path: indexed.get(relative_path),
    )

    errors = staged_path_validator.validate_docs_latest_mirrors()

    assert errors == [
        "git index docs/latest mirror differs from git index output/latest: "
        f"docs/latest/{name}"
    ]


def test_output_only_presence_does_not_require_docs_mirrors(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_dir = tmp_path / "output" / "latest"
    docs_dir = tmp_path / "docs" / "latest"
    config_dir = tmp_path / "config"
    output_dir.mkdir(parents=True)
    config_dir.mkdir(parents=True)
    output_paths = [
        output_dir / "daily_volume_breakout_operation_section_latest.csv",
        output_dir / "daily_volume_breakout_operation_section_latest.md",
        output_dir / "daily_volume_breakout_operation_evidence_audit_latest.csv",
        output_dir / "daily_volume_breakout_operation_evidence_audit_latest.md",
    ]
    docs_paths = [docs_dir / path.name for path in output_paths]
    contract_path = config_dir / "contract.md"
    summary_path = config_dir / "summary.csv"
    for path in [*output_paths, contract_path, summary_path]:
        path.write_bytes(b"present\n")

    monkeypatch.setattr(section_validator, "ROOT", tmp_path)
    monkeypatch.setattr(section_validator, "SECTION_CSV", output_paths[0])
    monkeypatch.setattr(section_validator, "SECTION_MD", output_paths[1])
    monkeypatch.setattr(section_validator, "EVIDENCE_AUDIT_CSV", output_paths[2])
    monkeypatch.setattr(section_validator, "EVIDENCE_AUDIT_MD", output_paths[3])
    monkeypatch.setattr(section_validator, "DOCS_SECTION_CSV", docs_paths[0])
    monkeypatch.setattr(section_validator, "DOCS_SECTION_MD", docs_paths[1])
    monkeypatch.setattr(section_validator, "DOCS_EVIDENCE_AUDIT_CSV", docs_paths[2])
    monkeypatch.setattr(section_validator, "DOCS_EVIDENCE_AUDIT_MD", docs_paths[3])
    monkeypatch.setattr(section_validator, "CONTRACT_MD", contract_path)
    monkeypatch.setattr(section_validator, "FORMAL_SUMMARY_CSV", summary_path)

    section_validator.validate_file_presence(include_docs_mirrors=False)
    with pytest.raises(SystemExit) as exc_info:
        section_validator.validate_file_presence(include_docs_mirrors=True)

    assert exc_info.value.code == 1
    assert "missing required file: docs/latest" in capsys.readouterr().out


def test_volume_operation_docs_mirror_is_byte_exact(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_dir = tmp_path / "output" / "latest"
    docs_dir = tmp_path / "docs" / "latest"
    output_dir.mkdir(parents=True)
    docs_dir.mkdir(parents=True)
    names = (
        "daily_volume_breakout_operation_section_latest.csv",
        "daily_volume_breakout_operation_section_latest.md",
        "daily_volume_breakout_operation_evidence_audit_latest.csv",
        "daily_volume_breakout_operation_evidence_audit_latest.md",
    )
    output_paths = [output_dir / name for name in names]
    docs_paths = [docs_dir / name for name in names]
    for index, (output_path, docs_path) in enumerate(
        zip(output_paths, docs_paths, strict=True)
    ):
        content = f"artifact-{index}\n".encode()
        output_path.write_bytes(content)
        docs_path.write_bytes(content)

    monkeypatch.setattr(section_validator, "ROOT", tmp_path)
    monkeypatch.setattr(section_validator, "SECTION_CSV", output_paths[0])
    monkeypatch.setattr(section_validator, "SECTION_MD", output_paths[1])
    monkeypatch.setattr(section_validator, "EVIDENCE_AUDIT_CSV", output_paths[2])
    monkeypatch.setattr(section_validator, "EVIDENCE_AUDIT_MD", output_paths[3])
    monkeypatch.setattr(section_validator, "DOCS_SECTION_CSV", docs_paths[0])
    monkeypatch.setattr(section_validator, "DOCS_SECTION_MD", docs_paths[1])
    monkeypatch.setattr(
        section_validator,
        "DOCS_EVIDENCE_AUDIT_CSV",
        docs_paths[2],
    )
    monkeypatch.setattr(
        section_validator,
        "DOCS_EVIDENCE_AUDIT_MD",
        docs_paths[3],
    )

    section_validator.validate_docs_mirrors()
    for index, docs_path in enumerate(docs_paths):
        original = docs_path.read_bytes()
        docs_path.write_bytes(f"artifact-{index}\r\n".encode())

        with pytest.raises(SystemExit) as exc_info:
            section_validator.validate_docs_mirrors()

        assert exc_info.value.code == 1
        assert "docs mirror byte mismatch" in capsys.readouterr().out
        docs_path.write_bytes(original)


def test_current_volume_operation_docs_mirrors_match_output() -> None:
    section_validator.validate_docs_mirrors()


def test_volume_operation_validator_rejects_unsynced_model_signal_log(monkeypatch, tmp_path) -> None:
    latest_dir = tmp_path / "output" / "latest"
    history_dir = tmp_path / "output" / "history" / "daily_candidate_models"
    latest_dir.mkdir(parents=True)
    history_dir.mkdir(parents=True)

    freshness = latest_dir / "data_freshness_latest.csv"
    latest_signals = latest_dir / "daily_candidate_model_signals_for_report_latest.csv"
    signal_log = history_dir / "daily_candidate_model_signal_log.csv"

    pd.DataFrame(
        [
            {
                "main_price_date": "20260618",
                "report_ready": "True",
                "warrant_ready": "True",
                "daily_pdf_ready": "True",
            }
        ]
    ).to_csv(freshness, index=False)
    pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "report_bucket": "mainstream",
                "stock_id": "2061",
                "model_id": LOW_VOLUME_MODEL_ID,
            }
        ]
    ).to_csv(latest_signals, index=False)
    pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "report_bucket": "mainstream",
                "stock_id": "3002",
                "model_id": LOW_VOLUME_MODEL_ID,
            }
        ]
    ).to_csv(signal_log, index=False)

    monkeypatch.setattr(section_validator, "DATA_FRESHNESS_CSV", freshness)
    monkeypatch.setattr(section_validator, "DAILY_SIGNALS_CSV", latest_signals)
    monkeypatch.setattr(section_validator, "MODEL_SIGNAL_LOG_CSV", signal_log)

    section = pd.DataFrame([{"daily_signal_date": "20260618"}])
    with pytest.raises(SystemExit):
        section_validator.validate_latest_signal_log_sync(section)


def test_volume_operation_validator_allows_lineage_only_signal_log_rows(monkeypatch, tmp_path) -> None:
    latest_dir = tmp_path / "output" / "latest"
    history_dir = tmp_path / "output" / "history" / "daily_candidate_models"
    latest_dir.mkdir(parents=True)
    history_dir.mkdir(parents=True)

    freshness = latest_dir / "data_freshness_latest.csv"
    latest_signals = latest_dir / "daily_candidate_model_signals_for_report_latest.csv"
    signal_log = history_dir / "daily_candidate_model_signal_log.csv"

    pd.DataFrame(
        [
            {
                "main_price_date": "20260618",
                "report_ready": "True",
                "warrant_ready": "True",
                "daily_pdf_ready": "True",
            }
        ]
    ).to_csv(freshness, index=False)
    pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "report_bucket": "mainstream",
                "stock_id": "2061",
                "model_id": LOW_VOLUME_MODEL_ID,
            }
        ]
    ).to_csv(latest_signals, index=False)
    pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "report_bucket": "mainstream",
                "stock_id": "2061",
                "model_id": LOW_VOLUME_MODEL_ID,
            },
            {
                "signal_date": "20260618",
                "report_bucket": "",
                "stock_id": "5211",
                "model_id": LOW_VOLUME_MODEL_ID,
            },
        ]
    ).to_csv(signal_log, index=False)

    monkeypatch.setattr(section_validator, "DATA_FRESHNESS_CSV", freshness)
    monkeypatch.setattr(section_validator, "DAILY_SIGNALS_CSV", latest_signals)
    monkeypatch.setattr(section_validator, "MODEL_SIGNAL_LOG_CSV", signal_log)
    monkeypatch.setattr(
        section_validator,
        "filter_volume_v2_operation_lineage_scope",
        lambda frame, **_kwargs: (frame.copy(), set()),
    )

    section = pd.DataFrame(
        [
            {
                "daily_signal_date": "20260618",
                "row_type": "data",
                "stock_id": "2061",
                "daily_volume_model_signal_count": "1",
            }
        ]
    )
    section_validator.validate_latest_signal_log_sync(section)


def prepare_20260807_2059_completeness_fixture(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    audit_path, formal, section = write_20260807_2059_lineage_scope_fixture(
        tmp_path
    )
    formal = formal.copy()
    formal["report_bucket"] = "mainstream"

    audit = pd.read_csv(audit_path, dtype=str, keep_default_na=False)
    source_path = tmp_path / audit.iloc[0]["formal_snapshot_path"]
    formal.to_csv(source_path, index=False)
    manifest_path = (
        tmp_path
        / "output"
        / "history"
        / "daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[0, "snapshot_sha256"] = snapshot_file_sha256(source_path)
    manifest.to_csv(manifest_path, index=False)
    audit["formal_snapshot_sha256"] = builder.canonical_text_sha256(
        source_path.read_bytes()
    )
    audit.loc[0, "formal_row_sha256"] = builder.canonical_row_sha256(formal.iloc[0])
    audit.loc[1, "formal_row_sha256"] = builder.canonical_row_sha256(formal.iloc[1])
    audit.to_csv(audit_path, index=False)

    latest_dir = tmp_path / "output" / "latest"
    signal_log_dir = (
        tmp_path / "output" / "history" / "daily_candidate_models"
    )
    latest_dir.mkdir(parents=True, exist_ok=True)
    signal_log_dir.mkdir(parents=True, exist_ok=True)
    freshness_path = latest_dir / "data_freshness_latest.csv"
    latest_signals_path = (
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv"
    )
    signal_log_path = signal_log_dir / "daily_candidate_model_signal_log.csv"
    pd.DataFrame(
        [
            {
                "main_price_date": "20260807",
                "report_ready": "True",
                "warrant_ready": "True",
                "daily_pdf_ready": "True",
            }
        ]
    ).to_csv(freshness_path, index=False)
    formal.to_csv(latest_signals_path, index=False)
    formal.to_csv(signal_log_path, index=False)

    monkeypatch.setattr(section_validator, "ROOT", tmp_path)
    monkeypatch.setattr(section_validator, "DATA_FRESHNESS_CSV", freshness_path)
    monkeypatch.setattr(section_validator, "DAILY_SIGNALS_CSV", latest_signals_path)
    monkeypatch.setattr(section_validator, "MODEL_SIGNAL_LOG_CSV", signal_log_path)
    monkeypatch.setattr(
        section_validator,
        "VOLUME_V2_LINEAGE_AUDIT_CSV",
        audit_path,
        raising=False,
    )

    scoped, excluded_keys = builder.filter_volume_v2_operation_lineage_scope(
        section,
        audit_path=audit_path,
        formal_signal_rows=formal,
        source_root=tmp_path,
    )
    assert excluded_keys == {("20260807", HIGH_VOLUME_MODEL_ID, "2059")}
    scoped["daily_signal_date"] = "20260807"
    scoped["daily_volume_model_signal_count"] = "2"
    return formal, scoped


def test_20260807_operation_completeness_excludes_exact_superseded_noncandidate(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    _formal, scoped = prepare_20260807_2059_completeness_fixture(
        monkeypatch, tmp_path
    )

    section_validator.validate_latest_signal_log_sync(scoped)


def test_20260807_operation_completeness_keeps_raw_signal_count_and_log_lineage(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    _formal, scoped = prepare_20260807_2059_completeness_fixture(
        monkeypatch, tmp_path
    )
    wrong_count = scoped.copy()
    wrong_count["daily_volume_model_signal_count"] = "1"
    with pytest.raises(SystemExit):
        section_validator.validate_latest_signal_log_sync(wrong_count)
    assert (
        "daily_volume_model_signal_count must match latest volume_range_breakout "
        "stock count: observed=['1'] expected=2"
        in capsys.readouterr().out
    )

    signal_log = pd.read_csv(
        section_validator.MODEL_SIGNAL_LOG_CSV,
        dtype=str,
        keep_default_na=False,
    )
    signal_log = signal_log[signal_log["stock_id"].astype(str).ne("2059")]
    signal_log.to_csv(section_validator.MODEL_SIGNAL_LOG_CSV, index=False)
    with pytest.raises(SystemExit):
        section_validator.validate_latest_signal_log_sync(scoped)
    assert (
        "latest volume_range_breakout signals and daily model signal log are out of sync"
        in capsys.readouterr().out
    )


def test_20260807_operation_completeness_still_rejects_missing_real_candidate(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    _formal, scoped = prepare_20260807_2059_completeness_fixture(
        monkeypatch, tmp_path
    )
    without_verified_candidate = scoped.iloc[0:0].copy()
    empty = builder.empty_row(
        HIGH_VOLUME_MODEL_ID,
        "highlight",
        "confirmed_operation",
        "ready",
        "20260807",
        2,
        approval_stub(),
        "2026-08-08 08:00:00 Asia/Taipei",
        "20260807",
    )
    without_verified_candidate = pd.DataFrame(
        [empty], columns=builder.OUTPUT_COLUMNS
    )

    with pytest.raises(SystemExit):
        section_validator.validate_latest_signal_log_sync(
            without_verified_candidate
        )
    output = capsys.readouterr().out
    assert (
        "latest volume_range_breakout stocks missing from operation section: ['6505']"
        in output
    )
    assert "['2059']" not in output


def test_20260807_2059_scoped_adapter_passes_readiness_and_pdf_source_gate(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    _formal, scoped = prepare_20260807_2059_completeness_fixture(
        monkeypatch, tmp_path
    )
    approvals = {
        model_id: approval_stub(
            operation_module_id=f"{model_id}_operation_v1",
            buy_filter_id=f"{model_id}_buy_filter_v1",
        )
        for model_id in builder.FORMAL_MODEL_IDS
    }
    adapter = builder.ensure_operation_section_empty_states(
        scoped,
        report_date="20260807",
        daily_signal_date="20260807",
        daily_volume_count=2,
        approvals_by_model=approvals,
        generated_at="2026-08-08 08:00:00 Asia/Taipei",
    )
    adapter["approved_for_daily"] = "True"
    adapter["operation_directive_level"] = "approved_daily_operation_guidance"
    adapter["adapter_source_status"] = "ready"
    adapter.loc[
        adapter["row_type"].astype(str).eq("data"), "row_metric_status"
    ] = "unavailable_no_approved_add_score_metric"
    assert "2059" not in set(adapter["stock_id"].astype(str))
    assert "6505" in set(adapter["stock_id"].astype(str))

    readiness_rows: list[dict[str, str]] = []
    for model_id in sorted(builder.FORMAL_MODEL_IDS):
        summary = readiness_builder.summarize_volume_daily_adapter(
            adapter, model_id
        )
        assert str(summary["daily_adapter_status"]).startswith("ready_")
        readiness_rows.append(
            {
                "model_id": model_id,
                "pdf_integration_status": "pdf_integrated_daily_adapter",
                "daily_adapter_sections": str(summary["daily_adapter_sections"]),
            }
        )

    adapter_path = tmp_path / "daily_volume_breakout_operation_section_latest.csv"
    adapter.to_csv(adapter_path, index=False)
    artifact_paths = {
        model_id: adapter_path for model_id in builder.FORMAL_MODEL_IDS
    }
    errors = (
        pdf_contract_validator.validate_pdf_integrated_operation_adapter_contract(
            readiness_rows,
            source_paths=(),
            artifact_paths=artifact_paths,
            renderer_tokens={model_id: () for model_id in builder.FORMAL_MODEL_IDS},
            required_columns_by_model={
                model_id: set(adapter.columns)
                for model_id in builder.FORMAL_MODEL_IDS
            },
            allowed_sections_by_model={
                model_id: set(builder.PDF_SECTIONS)
                for model_id in builder.FORMAL_MODEL_IDS
            },
            required_model_ids=set(builder.FORMAL_MODEL_IDS),
        )
    )
    assert errors == []


def test_volume_operation_builder_rejects_latest_signal_date_mismatch() -> None:
    signals = pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "stock_id": "2061",
                "model_id": LOW_VOLUME_MODEL_ID,
            }
        ]
    )

    with pytest.raises(RuntimeError, match="main_price_date=20260617"):
        builder.require_latest_signals_match_report_date(signals, "20260617")


def test_daily_pdf_generator_does_not_read_research_operation_artifacts_directly() -> None:
    generator = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    if not generator.exists():
        return
    source = generator.read_text(encoding="utf-8", errors="replace")

    assert "daily_volume_breakout_operation_section_latest.csv" in source
    assert "render_volume_range_breakout_operation_section" in source
    assert "approved_operation_patterns_latest.csv" in source
    assert "volume_breakout_operation_pdf_preview_latest.csv" not in source
    assert "volume_breakout_confirmed_operation_rank_latest.csv" not in source
    assert "volume_breakout_pending_operation_queue_latest.csv" not in source


def test_daily_pdf_generator_omits_obsolete_volume_breakout_explanatory_text() -> None:
    generator = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    source = generator.read_text(encoding="utf-8", errors="replace")

    for token in [
        "放量攻擊模型操作參考",
        "以下僅呈現 daily adapter 已核准欄位",
        "PDF 不重新計算進場",
        "待確認列只作觀察",
    ]:
        assert token not in source
    assert 'DAILY_HIGHLIGHT_DESCRIPTION_POLICY = "program_side_non_volume"' in source
    assert "should_render_highlight_model_description(model_id)" in source



def test_volume_v2_pdf_validation_has_one_canonical_contract_path() -> None:
    stale_validator = ROOT / "scripts" / "validate_chatgpt_side_volume_operation_pdf_integration.py"
    assert not stale_validator.exists()

    stale_name = stale_validator.name
    for path in [
        ROOT / "config" / "repo_production_inventory.csv",
        ROOT / "config" / "repo_file_lifecycle_inventory.csv",
        ROOT / "docs" / "pdf_production_inventory.md",
    ]:
        assert stale_name not in path.read_text(encoding="utf-8-sig")

    workflow_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            ROOT / ".github" / "workflows" / "daily_full_pipeline.yml",
            ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml",
        ]
    )
    assert "validate_chatgpt_daily_report_new_conversation_replay.py" in workflow_text
    assert "validate_daily_pdf_completion_hard_gate.py" in workflow_text

    regression_contract = (
        ROOT / "config" / "daily_pdf_rendered_model_regression_contract.csv"
    ).read_text(encoding="utf-8-sig")
    for model_id in [LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID]:
        assert model_id in regression_contract
    for token in [
        "本日可買 / 已確認買入候選",
        "操作中",
        "低位放量攻擊模型",
        "中位動能放量攻擊模型",
        "高位階放量攻擊模型",
    ]:
        assert token in regression_contract


def test_pdf_chart_renderer_prefers_local_source_worktree_price_window(monkeypatch, tmp_path) -> None:
    calls: list[str] = []

    def fake_read_csv(path, **kwargs):
        calls.append(str(path))
        if str(path).startswith("https://"):
            raise AssertionError("raw GitHub price URL should not be used when local source data exists")
        return pd.DataFrame(
            [
                {"date": "2026-06-15", "open": "10", "high": "11", "low": "9", "close": "10.5", "volume": "1000"},
                {"date": "2026-06-16", "open": "10.5", "high": "12", "low": "10", "close": "11.5", "volume": "2000"},
                {"date": "2026-06-17", "open": "11.5", "high": "13", "low": "11", "close": "12.5", "volume": "3000"},
            ]
        )

    monkeypatch.setattr(pdf_generator, "read_csv", fake_read_csv)
    monkeypatch.setattr(pdf_generator, "LATEST", tmp_path / "output" / "latest")
    monkeypatch.setattr(pdf_generator, "CHARTS", tmp_path / "charts")
    monkeypatch.setitem(
        pdf_generator.REMOTE_README,
        "individual_stock_price_raw_url_template",
        "https://example.invalid/{stock_id}_price_window_180_latest.csv",
    )
    pdf_generator.CHARTS.mkdir(parents=True, exist_ok=True)

    chart = pdf_generator.plot_stock_chart("2330", "台積電", pd.Series(dtype=object))

    assert chart is not None
    assert chart.exists()
    assert calls == [
        str(
            tmp_path
            / "output"
            / "latest"
            / "individual_stock_reports"
            / "price_windows"
            / "2330_price_window_180_latest.csv"
        )
    ]


def test_daily_packet_builder_uses_daily_adapter_not_research_operation_artifacts() -> None:
    packet_builder = ROOT / "build_chatgpt_daily_report_packet.py"
    source = packet_builder.read_text(encoding="utf-8", errors="replace")

    assert "daily_volume_breakout_operation_section_latest.csv" in source
    assert "build_volume_operation_packet_lines" in source
    assert "volume_breakout_operation_pdf_preview_latest.csv" not in source
    assert "volume_breakout_confirmed_operation_rank_latest.csv" not in source
    assert "volume_breakout_pending_operation_queue_latest.csv" not in source
    assert "historical_pattern_operation_registry_latest.csv" not in source
    assert "approved_operation_patterns_latest.csv" not in source
    assert 'operation-row performance must consume row_metric_* only' in source
    for field in (
        "row_metric_status",
        "row_metric_scope",
        "row_metric_id",
        "row_metric_label_zh",
        "row_metric_sample_size",
        "row_metric_win_rate_zh",
        "row_metric_neutral_rate_zh",
        "row_metric_failure_rate_zh",
        "row_metric_avg_return_zh",
        "row_metric_median_return_zh",
        "row_metric_source",
        "row_metric_selection_status",
    ):
        assert field in source


def operation_rows_for_limit_test(
    pdf_section: str,
    count: int,
    pdf_view: str = "highlight",
    stock_start: int = 5000,
) -> pd.DataFrame:
    rows = []
    for index in range(count):
        rows.append(
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": pdf_view,
                "pdf_section": pdf_section,
                "row_type": "data",
                "display_order": str(index + 1),
                "stock_id": str(stock_start + index),
                "stock_display": f"{stock_start + index} Test",
                "row_action_status": (
                    "confirmed_buy_candidate"
                    if pdf_section == "confirmed_operation"
                    else "pending_confirmation"
                    if pdf_section == "pending_confirmation"
                    else "active_operation"
                ),
                "buy_rank_eligible": "True" if pdf_section == "confirmed_operation" else "False",
                "row_metric_status": (
                    "" if pdf_section == "pending_confirmation" else "unavailable_no_approved_add_score_metric"
                ),
                "row_metric_scope": "",
                "row_metric_id": "",
                "row_metric_label_zh": "",
                "row_metric_matched_add_score_ids": "",
                "row_metric_sample_size": "",
                "row_metric_win_rate_zh": "",
                "row_metric_neutral_rate_zh": "",
                "row_metric_failure_rate_zh": "",
                "row_metric_avg_return_zh": "",
                "row_metric_median_return_zh": "",
                "row_metric_source": "",
                "row_metric_selection_status": (
                    "" if pdf_section == "pending_confirmation" else "baseline_not_permitted_in_operation_row"
                ),
            }
        )
    return pd.DataFrame(rows)


def test_pdf_operation_highlight_display_limits_are_section_specific() -> None:
    confirmed = operation_rows_for_limit_test("confirmed_operation", 12)
    pending = operation_rows_for_limit_test("pending_confirmation", 8)
    active = operation_rows_for_limit_test("active_operation", 7)
    active_many = operation_rows_for_limit_test("active_operation", 12)

    assert len(pdf_generator.limit_operation_rows_for_pdf_view(confirmed, "highlight", "confirmed_operation")) == 12
    assert len(pdf_generator.limit_operation_rows_for_pdf_view(pending, "highlight", "pending_confirmation")) == 8
    assert len(pdf_generator.limit_operation_rows_for_pdf_view(active, "highlight", "active_operation")) == 7
    assert len(pdf_generator.limit_operation_rows_for_pdf_view(active_many, "highlight", "active_operation")) == 10

    assert len(pdf_generator.limit_operation_rows_for_pdf_view(confirmed, "full", "confirmed_operation")) == 12
    assert len(pdf_generator.limit_operation_rows_for_pdf_view(pending, "full", "pending_confirmation")) == 8
    assert len(pdf_generator.limit_operation_rows_for_pdf_view(active, "full", "active_operation")) == 7
    assert len(pdf_generator.limit_operation_rows_for_pdf_view(active_many, "full", "active_operation")) == 12


def test_pdf_operation_highlight_display_limits_apply_after_report_line_filter() -> None:
    rows = operation_rows_for_limit_test("active_operation", 8)
    taxonomy = []
    for index, stock_id in enumerate(rows["stock_id"].astype(str).tolist()):
        taxonomy.append(
            {
                "stock_id": stock_id,
                "report_line_memberships": "mainstream" if index < 6 else "non_mainstream",
                "mainstream_report_eligible": "True" if index < 6 else "False",
                "non_mainstream_report_eligible": "False" if index < 6 else "True",
            }
        )
    inputs = {
        "volume_operation": rows,
        "stock_theme_taxonomy": pd.DataFrame(taxonomy),
    }

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(
        pdf_generator.volume_operation_frame(inputs, LOW_VOLUME_MODEL_ID, "highlight", "active_operation"),
        inputs,
        "mainstream",
    )
    mainstream = pdf_generator.limit_operation_rows_for_pdf_view(
        mainstream,
        "highlight",
        "active_operation",
    )
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(
        pdf_generator.volume_operation_frame(inputs, LOW_VOLUME_MODEL_ID, "highlight", "active_operation"),
        inputs,
        "non_mainstream",
    )
    non_mainstream = pdf_generator.limit_operation_rows_for_pdf_view(
        non_mainstream,
        "highlight",
        "active_operation",
    )

    assert len(mainstream) == 6
    assert len(non_mainstream) == 2


def test_pdf_operation_renderer_uses_row_level_buy_eligibility(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    rows = pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "operation_asof_date": "20260612",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "1111",
                "stock_display": "1111 測試A",
                "trigger_zh": "舊確認方式不可出現",
                "entry_basis_zh": "舊買入方式不可出現",
                "entry_price_status_zh": "舊進場價狀態不可出現",
                "stop_basis_zh": "舊停損基準不可出現",
                "exit_rule_zh": "舊出場規則不可出現",
                    "selected_trigger_id": "next_day_continuation_confirmed",
                "selected_confirmation_date": "20260612",
                "confirmation_date": "20260612",
                "entry_rule_id": "confirmation_next_open",
                "entry_price_basis": "next_open_after_confirmation",
                "entry_date": "",
                "entry_price": "",
                "stop_loss_rule_id": "signal_low_stop",
                "stop_loss_price": "10.00",
                "stop_loss_label_zh": "6/11最低點",
                "exit_rule_id": "signal_low_stop_or_fixed_10d_close",
                "planned_holding_days": "10",
                "operation_age_days": "1",
                "operation_score": "12.3",
                "tdcc_score": "1.0",
                "pattern_score": "2.0",
                "risk_penalty": "0",
                "final_rank_score": "88.8",
                "rank_reason_zh": "正式分數理由",
                "sample_size": "12",
                "win_rate_zh": "66.67%",
                "avg_return_zh": "+21.67%",
                "median_return_zh": "+21.09%",
                "row_metric_status": "unavailable_no_approved_add_score_metric",
                "row_metric_scope": "",
                "row_metric_id": "",
                "row_metric_label_zh": "",
                "row_metric_matched_add_score_ids": "",
                "row_metric_sample_size": "",
                "row_metric_win_rate_zh": "",
                "row_metric_neutral_rate_zh": "",
                "row_metric_failure_rate_zh": "",
                "row_metric_avg_return_zh": "",
                "row_metric_median_return_zh": "",
                "row_metric_source": "",
                "row_metric_selection_status": "baseline_not_permitted_in_operation_row",
                "confidence_zh": "低",
                "operation_status_zh": "已確認",
                "row_action_status": "confirmed_buy_candidate",
                "buy_rank_eligible": "True",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "operation_asof_date": "20260612",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "2222",
                "stock_display": "2222 測試B",
                "pending_age_zh": "D+1，剩 9 個交易日",
                "pending_group_zh": "D+0-D+1 等隔日續強",
                "pending_confirmation_zh": "等待隔日續強 / 回測 5MA / 回測 10MA",
                "entry_basis_zh": "舊待確認進場欄位不可出現",
                "entry_price_status_zh": "舊待確認進場狀態不可出現",
                "stop_basis_zh": "舊待確認停損欄位不可出現",
                "operation_score": "4.0",
                "final_rank_score": "77.6",
                "rank_reason_zh": "待確認分數理由",
                "operation_status_zh": "待確認",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "operation_asof_date": "20260612",
                "row_type": "empty_state",
                "display_order": "0",
                "stock_id": "",
                "stock_display": "目前無資料",
                "operation_status_zh": "操作中",
                "adapter_note_zh": "目前無操作中追蹤列。",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )

    story: list = []
    pdf_generator.render_volume_range_breakout_operation_section(
        story,
        {"volume_operation": rows},
        LOW_VOLUME_MODEL_ID,
        "highlight",
    )

    story_text = "\n".join(
        flowable.getPlainText()
        for flowable in story
        if hasattr(flowable, "getPlainText")
    )
    for token in [
        "放量攻擊模型操作參考",
        "以下僅呈現 daily adapter 已核准欄位",
        "PDF 不重新計算進場",
        "待確認列只作觀察",
    ]:
        assert token not in story_text

    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == pdf_generator.operation_table_title(
        pdf_generator.operation_model_display_name(LOW_VOLUME_MODEL_ID),
        pdf_generator.OPERATION_CONFIRMED_BUY_TABLE_TITLE,
    )
    assert confirmed[1] == [
        "排名",
        "股票",
        "確認方式",
        "確認日",
        "買入方式",
        "停損基準",
        "出場規則",
        "操作 / 最終分數",
        "加分勝/和/敗/報酬",
        "排名原因",
    ]
    assert confirmed[2][1] == "1111 測試A"
    assert confirmed[2][2] == pdf_generator.VOLUME_TRIGGER_LABELS["next_day_continuation_confirmed"]
    assert confirmed[2][3] == "2026/6/12"
    assert confirmed[2][4] == "確認後下一交易日開盤，尚未產生"
    assert confirmed[2][5] == "6/11最低點 10.00"
    assert confirmed[2][6] == "跌破停損基準，否則最多第 10 個交易日收盤"
    assert confirmed[2][7] == "操作 12.30 / 最終 88.80"
    assert confirmed[2][8] == pdf_generator.OPERATION_ROW_METRIC_UNAVAILABLE_TEXT
    assert confirmed[2][9] == "正式分數理由"
    assert "2222 測試B" not in " ".join(str(cell) for row in confirmed for cell in row)
    assert active[0][0] == pdf_generator.operation_table_title(
        pdf_generator.operation_model_display_name(LOW_VOLUME_MODEL_ID),
        pdf_generator.OPERATION_ACTIVE_TABLE_TITLE,
    )
    assert active[1] == ["股票", "確認方式", "進場日 / 價", "停損基準", "持有天數", "出場規則", "操作 / 最終分數", "備註"]
    assert active[2][7] == "目前無操作中追蹤列"

    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "2222 測試B" not in visible
    assert "待確認分數理由" not in visible
    assert "buy_rank_eligible" not in visible
    assert "row_action_status" not in visible
    assert "confirmed_buy_candidate" not in visible
    assert "舊確認方式不可出現" not in visible
    assert "舊買入方式不可出現" not in visible
    assert "舊進場價狀態不可出現" not in visible
    assert "舊停損基準不可出現" not in visible
    assert "舊出場規則不可出現" not in visible


def test_pdf_operation_renderer_full_shows_confirmed_unranked(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    rows = pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "full",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "full",
                "pdf_section": "confirmed_unranked_operation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "3333",
                "stock_display": "3333 測試C",
                    "selected_trigger_id": "next_day_continuation_confirmed",
                "selected_confirmation_date": "20260612",
                "confirmation_date": "20260612",
                "rank_reason_zh": "已確認但證據未過門檻",
                "sample_size": "2098",
                "win_rate_zh": "38.13%",
                "median_return_zh": "-3.28%",
                "row_metric_status": "unavailable_no_approved_add_score_metric",
                "row_metric_scope": "",
                "row_metric_id": "",
                "row_metric_label_zh": "",
                "row_metric_matched_add_score_ids": "",
                "row_metric_sample_size": "",
                "row_metric_win_rate_zh": "",
                "row_metric_neutral_rate_zh": "",
                "row_metric_failure_rate_zh": "",
                "row_metric_avg_return_zh": "",
                "row_metric_median_return_zh": "",
                "row_metric_source": "",
                "row_metric_selection_status": "baseline_not_permitted_in_operation_row",
                "evidence_match_status": "row_level_evidence_not_buy_ranked",
                "row_action_status": "confirmed_not_buy_ranked",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "full",
                "pdf_section": "pending_confirmation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "full",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )

    story: list = []
    pdf_generator.render_volume_range_breakout_operation_section(
        story,
        {"volume_operation": rows},
        LOW_VOLUME_MODEL_ID,
        "full",
    )

    assert len(captured_tables) == 4
    _, unranked, _, _ = captured_tables
    assert unranked[0][0] == pdf_generator.operation_table_title(
        pdf_generator.operation_model_display_name(LOW_VOLUME_MODEL_ID),
        "已確認但未通過買入排名門檻",
    )
    assert unranked[1] == ["股票", "確認方式", "確認日", "未列排名原因", "加分勝/和/敗/報酬", "證據狀態"]
    assert unranked[2][0] == "3333 測試C"
    assert unranked[2][3] == "已確認但證據未過門檻"
    assert unranked[2][4] == pdf_generator.OPERATION_ROW_METRIC_UNAVAILABLE_TEXT
    assert unranked[2][5] == "歷史證據未過門檻"
    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "confirmed_not_buy_ranked" not in visible
    assert "row_level_evidence_not_buy_ranked" not in visible


def test_pdf_operation_renderer_keeps_highlight_empty_tables(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    rows = pd.DataFrame(
        [
            output_row(
                pdf_view="highlight",
                pdf_section="confirmed_operation",
                stock_display="目前無資料",
                adapter_note_zh="已確認操作：來源日期不符，今日不顯示舊操作列；不重新計算操作規則。",
                row_metric_status="not_applicable_empty_state",
            ),
            output_row(
                pdf_view="highlight",
                pdf_section="pending_confirmation",
                stock_display="目前無資料",
                adapter_note_zh="待確認：來源日期不符，今日不顯示舊操作列；不重新計算操作規則。",
                row_metric_status="not_applicable_empty_state",
            ),
            output_row(
                pdf_view="highlight",
                pdf_section="active_operation",
                stock_display="目前無資料",
                adapter_note_zh="操作中：來源日期不符，今日不顯示舊操作列；不重新計算操作規則。",
                row_metric_status="not_applicable_empty_state",
            ),
        ]
    )

    story: list = []
    pdf_generator.render_volume_range_breakout_operation_section(
        story,
        {"volume_operation": rows},
        LOW_VOLUME_MODEL_ID,
        "highlight",
    )

    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == pdf_generator.operation_table_title(
        pdf_generator.operation_model_display_name(LOW_VOLUME_MODEL_ID),
        pdf_generator.OPERATION_CONFIRMED_BUY_TABLE_TITLE,
    )
    assert confirmed[1][:2] == ["排名", "股票"]
    assert confirmed[2][9] == "本日無股票推薦"
    assert active[0][0] == pdf_generator.operation_table_title(
        pdf_generator.operation_model_display_name(LOW_VOLUME_MODEL_ID),
        pdf_generator.OPERATION_ACTIVE_TABLE_TITLE,
    )
    assert active[1][:2] == ["股票", "確認方式"]
    story_text = "\n".join(
        flowable.getPlainText()
        for flowable in story
        if hasattr(flowable, "getPlainText")
    )
    assert "本日可買 / 已確認買入候選" in story_text
    assert "操作中" in story_text
    assert "待確認" not in story_text
    assert "今日沒有可顯示的放量攻擊操作列。" not in story_text
def w_bottom_readiness(model_id: str, status: str = "pdf_integrated_daily_adapter") -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": model_id,
                "pdf_integration_status": status,
                "daily_adapter_sections": "confirmed_operation,active_operation",
            }
        ]
    )


def w_bottom_operation_row(
    model_id: str,
    pdf_section: str,
    row_type: str = "data",
    stock_id: str = "1111",
    stock_display: str = "1111 WBuy",
    report_line: str = "mainstream",
    row_action_status: str = "confirmed_buy_candidate",
    buy_rank_eligible: str = "True",
) -> dict[str, str]:
    row_metric_status = (
        "not_applicable_empty_state" if row_type == "empty_state" else "unavailable_no_approved_add_score_metric"
    )
    return {
        "model_id": model_id,
        "model_name_zh": model_id,
        "pdf_view": "highlight",
        "pdf_section": pdf_section,
        "pdf_section_zh": pdf_section,
        "row_type": row_type,
        "operation_asof_date": "20260630",
        "operation_source_date_status": "current_report_date",
        "report_line": report_line,
        "report_line_memberships": "mainstream|non_mainstream" if report_line == "both" else report_line,
        "display_order": "1",
        "stock_id": stock_id,
        "stock_name": stock_display,
        "stock_display": stock_display,
        "operation_status": pdf_section,
        "operation_status_zh": pdf_section,
        "quality_status_zh": "adapter evidence",
        "row_action_status": row_action_status,
        "buy_rank_eligible": buy_rank_eligible,
        "signal_date": "20260630",
        "entry_rule_id": "test_entry_rule",
        "entry_basis_zh": "adapter entry basis",
        "entry_date": "20260701" if row_type == "data" else "",
        "entry_price": "10.5" if row_type == "data" else "",
        "stop_loss_rule_id": "test_stop_rule",
        "stop_loss_price": "9.8",
        "stop_loss_label_zh": "adapter stop",
        "exit_rule_id": "test_exit_rule",
        "exit_rule_zh": "adapter exit",
        "planned_holding_days": "20",
        "operation_age_days": "2",
        "sample_size": "31",
        "win_rate_zh": "58.06%",
        "median_return_zh": "6.24%",
        "row_metric_status": row_metric_status,
        "row_metric_scope": "",
        "row_metric_id": "",
        "row_metric_label_zh": "",
        "row_metric_matched_add_score_ids": "",
        "row_metric_sample_size": "",
        "row_metric_win_rate_zh": "",
        "row_metric_neutral_rate_zh": "",
        "row_metric_failure_rate_zh": "",
        "row_metric_avg_return_zh": "",
        "row_metric_median_return_zh": "",
        "row_metric_source": "",
        "row_metric_selection_status": (
            "" if row_type == "empty_state" else "baseline_not_permitted_in_operation_row"
        ),
        "pdf_note_zh": "model-owned adapter row",
        "adapter_note_zh": "PDF must not infer lifecycle",
    }


def numbered_w_bottom_operation_row(
    model_id: str,
    pdf_section: str,
    stock_id: str,
    display_order: int,
    *,
    stock_display: str | None = None,
    report_line: str = "mainstream",
    row_action_status: str | None = None,
    buy_rank_eligible: str | None = None,
) -> dict[str, str]:
    if row_action_status is None:
        row_action_status = "confirmed_buy_candidate" if pdf_section == "confirmed_operation" else "active_tracking"
    if buy_rank_eligible is None:
        buy_rank_eligible = "True" if pdf_section == "confirmed_operation" else "False"
    row = w_bottom_operation_row(
        model_id,
        pdf_section,
        stock_id=stock_id,
        stock_display=stock_display or f"{stock_id} TestStock",
        report_line=report_line,
        row_action_status=row_action_status,
        buy_rank_eligible=buy_rank_eligible,
    )
    row["display_order"] = str(display_order)
    return row


def price_pullback_operation_row(
    pdf_section: str,
    row_type: str = "data",
    stock_id: str = "3333",
    stock_display: str = "3333 PricePullback",
    operation_quality: str = "technical_strength",
    report_line: str = "mainstream",
    row_action_status: str = "confirmed_buy_candidate",
    buy_rank_eligible: str = "True",
) -> dict[str, str]:
    row_metric_ready = row_type == "data" and operation_quality == "technical_strength"
    row_metric_status = (
        "not_applicable_empty_state"
        if row_type == "empty_state"
        else "ready" if row_metric_ready else "unavailable_no_approved_add_score_metric"
    )
    return {
        "model_id": pdf_generator.PRICE_PULLBACK_MODEL_ID,
        "model_name_zh": "23EMA回檔模型",
        "pdf_view": "highlight",
        "pdf_section": pdf_section,
        "pdf_section_zh": pdf_section,
        "row_type": row_type,
        "operation_asof_date": "20260703",
        "operation_source_date_status": "current_report_date",
        "report_line": report_line,
        "report_line_memberships": "mainstream|non_mainstream" if report_line == "both" else report_line,
        "display_order": "1",
        "stock_id": stock_id,
        "stock_name": stock_display,
        "stock_display": stock_display,
        "operation_status": pdf_section,
        "operation_status_zh": pdf_section,
        "operation_quality": operation_quality,
        "operation_quality_zh": "技術強勢" if operation_quality == "technical_strength" else "基礎",
        "row_action_status": row_action_status,
        "buy_rank_eligible": buy_rank_eligible,
        "signal_date": "20260703",
        "entry_rule_id": "signal_date_next_open",
        "entry_basis_zh": "本表股票為23EMA回檔模型通過候選，隔日開盤買入。",
        "stop_loss_rule_id": "sustained_close_below_lower_ma20_ema23_4pct_4d",
        "stop_basis_zh": "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。",
        "exit_rule_id": "close_prev20_high_break_next_open",
        "exit_rule_zh": "收盤突破訊號日前20日高點後，隔日開盤賣出。",
        "planned_holding_days": "20",
        "operation_age_days": "2" if row_type == "data" else "",
        "sample_size": "1160",
        "win_rate_zh": "66.03%",
        "neutral_rate_zh": "5.60%",
        "failure_rate_zh": "28.36%",
        "avg_return_zh": "+2.90%",
        "technical_package_win_rate_zh": "75.54%",
        "technical_package_neutral_rate_zh": "3.52%",
        "technical_package_failure_rate_zh": "20.95%",
        "technical_package_avg_return_zh": "+2.96%",
        "row_metric_status": row_metric_status,
        "row_metric_scope": "exact_combo" if row_metric_ready else "",
        "row_metric_id": "price_pullback_23ema__technical_strength_rsi60_macd_positive" if row_metric_ready else "",
        "row_metric_label_zh": "RSI14 >= 60 + MACD histogram > 0" if row_metric_ready else "",
        "row_metric_matched_add_score_ids": "rsi14_ge60|macd_hist_gt0" if row_metric_ready else "",
        "row_metric_sample_size": "654" if row_metric_ready else "",
        "row_metric_win_rate_zh": "75.54%" if row_metric_ready else "",
        "row_metric_neutral_rate_zh": "3.52%" if row_metric_ready else "",
        "row_metric_failure_rate_zh": "20.95%" if row_metric_ready else "",
        "row_metric_avg_return_zh": "+2.96%" if row_metric_ready else "",
        "row_metric_median_return_zh": "",
        "row_metric_source": "price_pullback_23ema_feature_confirmation_research_latest.csv" if row_metric_ready else "",
        "row_metric_selection_status": (
            "exact_recomputed_combo_metric"
            if row_metric_ready
            else "" if row_type == "empty_state" else "baseline_not_permitted_in_operation_row"
        ),
        "rank_reason_zh": "技術強勢；20日漲幅0~25%、TDCC高門檻增加、OBV站上MA20",
        "risk_tags_zh": "",
    }


def test_price_pullback_pdf_renderer_uses_model_owned_adapter_rows(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    operation_rows = pd.DataFrame(
        [
            price_pullback_operation_row("confirmed_operation"),
            price_pullback_operation_row(
                "active_operation",
                row_type="empty_state",
                stock_id="",
                stock_display=pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT,
                report_line="both",
                row_action_status="empty_state",
                buy_rank_eligible="False",
            ),
        ]
    )
    candidate_signals = pd.DataFrame(
        [
            {
                "model_id": pdf_generator.PRICE_PULLBACK_MODEL_ID,
                "stock_id": "9999",
                "stock_name": "CandidateLeak",
                "report_line": "mainstream",
                "same_model_repeat_status_zh": "新上榜",
            }
        ]
    )

    story: list = []
    rendered = pdf_generator.render_model_operation_section_if_applicable(
        story,
        {
            "model_readiness": w_bottom_readiness(pdf_generator.PRICE_PULLBACK_MODEL_ID),
            pdf_generator.PRICE_PULLBACK_OPERATION_INPUT_KEY: operation_rows,
            "model_signals": candidate_signals,
        },
        pdf_generator.PRICE_PULLBACK_MODEL_ID,
        "highlight",
        "mainstream",
    )

    assert rendered is True
    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == "23EMA回檔模型 - 本日可買 / 已確認買入候選"
    assert confirmed[1] == ["股票", "操作品質", "訊號日", "買入", "賣出", "停損", "勝/和/敗/報酬", "理由 / 風險"]
    assert "排名" not in confirmed[1]
    assert confirmed[2][0] == "3333 PricePullback"
    assert confirmed[2][1] == "技術強勢"
    assert "隔日開盤買入" in confirmed[2][3]
    assert "隔日開盤賣出" in confirmed[2][4]
    assert "下一個交易日" not in confirmed[2][3]
    assert "下一個交易日" not in confirmed[2][4]
    assert "66.03%" not in confirmed[2][6]
    assert "+2.90%" not in confirmed[2][6]
    assert "75.54%" in confirmed[2][6]
    assert "+2.96%" in confirmed[2][6]
    assert active[0][0] == "23EMA回檔模型 - 操作中"
    assert active[2][6] == pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT
    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "9999" not in visible
    assert "CandidateLeak" not in visible


def test_operation_row_performance_label_uses_model_owned_row_metric_only() -> None:
    row = pd.Series(
        {
            "win_rate_zh": "50.00%",
            "neutral_rate_zh": "1.00%",
            "failure_rate_zh": "49.00%",
            "avg_return_zh": "+1.00%",
            "pdf_bonus_combo_win_rate_zh": "80.00%",
            "pdf_bonus_combo_neutral_rate_zh": "0.00%",
            "pdf_bonus_combo_loss_rate_zh": "20.00%",
            "pdf_bonus_combo_avg_return_zh": "+4.10%",
            "row_metric_status": "ready",
            "row_metric_scope": "exact_combo",
            "row_metric_id": "pdf_combo__breakout_2_5__signal_body_le3",
            "row_metric_label_zh": "突破 2%~5% + K棒實體 <= 3%",
            "row_metric_sample_size": "5",
            "row_metric_win_rate_zh": "80.00%",
            "row_metric_neutral_rate_zh": "0.00%",
            "row_metric_failure_rate_zh": "20.00%",
            "row_metric_avg_return_zh": "+4.10%",
        }
    )

    label = pdf_generator.operation_row_performance_label(row)

    assert label == "突破 2%~5% + K棒實體 <= 3% | 樣本數 5 | 80.00% / 0.00% / 20.00% / +4.10%"
    assert "50.00%" not in label
    assert "+1.00%" not in label


def test_price_pullback_metrics_label_prefers_technical_package_over_baseline() -> None:
    label = pdf_generator.price_pullback_metrics_label(pd.Series(price_pullback_operation_row("confirmed_operation")))

    assert label == "RSI14 >= 60 + MACD histogram > 0 | 樣本數 654 | 75.54% / 3.52% / 20.95% / +2.96%"
    assert "66.03%" not in label
    assert "+2.90%" not in label


def test_price_pullback_metrics_label_blocks_baseline_for_base_rows() -> None:
    row = pd.Series(price_pullback_operation_row("confirmed_operation", operation_quality="base"))

    label = pdf_generator.price_pullback_metrics_label(row)

    assert label == pdf_generator.OPERATION_ROW_METRIC_UNAVAILABLE_TEXT
    assert "66.03%" not in label
    assert "+2.90%" not in label
    assert "75.54%" not in label
    assert "+2.96%" not in label


def test_w_bottom_pdf_renderer_uses_model_owned_adapter_rows(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    model_id = pdf_generator.W_BOTTOM_RIGHT_SIDE_MODEL_ID
    operation_rows = pd.DataFrame(
        [
            w_bottom_operation_row(model_id, "confirmed_operation", stock_id="1111", stock_display="1111 WBuy"),
            w_bottom_operation_row(
                model_id,
                "active_operation",
                stock_id="2222",
                stock_display="2222 WActive",
                row_action_status="active_tracking",
                buy_rank_eligible="False",
            ),
        ]
    )
    candidate_signals = pd.DataFrame(
        [
            {
                "model_id": model_id,
                "stock_id": "9999",
                "stock_name": "CandidateLeak",
                "report_line": "mainstream",
                "same_model_repeat_status_zh": "新上榜",
            }
        ]
    )

    story: list = []
    pdf_generator.render_w_bottom_operation_section(
        story,
        {
            "model_readiness": w_bottom_readiness(model_id),
            "w_bottom_right_side_operation": operation_rows,
            "model_signals": candidate_signals,
        },
        model_id,
        "highlight",
        "mainstream",
    )

    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == "W底右側模型 - 本日可買 / 已確認買入候選"
    assert confirmed[2][1] == "1111 WBuy"
    assert confirmed[2][8] == pdf_generator.OPERATION_ROW_METRIC_UNAVAILABLE_TEXT
    assert "58.06%" not in confirmed[2][8]
    assert active[0][0] == "W底右側模型 - 操作中"
    assert active[2][0] == "2222 WActive"
    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "9999" not in visible
    assert "CandidateLeak" not in visible
    story_text = "\n".join(
        flowable.getPlainText()
        for flowable in story
        if hasattr(flowable, "getPlainText")
    )
    assert pdf_generator.OPERATION_CONFIRMED_BUY_TABLE_TITLE in story_text
    assert pdf_generator.OPERATION_ACTIVE_TABLE_TITLE in story_text
    assert "新上榜" not in story_text
    assert "重複上榜" not in story_text


def test_operation_highlight_limit_helper_keeps_confirmed_all_and_active_max_10() -> None:
    rows = pd.DataFrame(
        [
            {"row_type": "data", "stock_id": f"{idx:04d}", "display_order": str(idx)}
            for idx in range(1, 13)
        ]
    )

    confirmed = pdf_generator.limit_operation_rows_for_pdf_view(
        rows,
        "highlight",
        "confirmed_operation",
    )
    active = pdf_generator.limit_operation_rows_for_pdf_view(
        rows,
        "highlight",
        "active_operation",
    )

    assert len(confirmed) == 12
    assert len(active) == pdf_generator.OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS
    assert "0006" in set(active["stock_id"].astype(str))
    assert "0011" not in set(active["stock_id"].astype(str))


def test_w_bottom_highlight_confirmed_operation_rows_are_not_capped(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    model_id = pdf_generator.W_BOTTOM_RIGHT_SIDE_MODEL_ID
    confirmed_rows = [
        numbered_w_bottom_operation_row(model_id, "confirmed_operation", f"{idx:04d}", idx)
        for idx in range(1, 13)
    ]
    active_empty = w_bottom_operation_row(
        model_id,
        "active_operation",
        row_type="empty_state",
        stock_id="",
        stock_display=pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT,
        report_line="both",
        row_action_status="empty_state",
        buy_rank_eligible="False",
    )

    pdf_generator.render_w_bottom_operation_section(
        [],
        {
            "model_readiness": w_bottom_readiness(model_id),
            "w_bottom_right_side_operation": pd.DataFrame([*confirmed_rows, active_empty]),
        },
        model_id,
        "highlight",
        "mainstream",
    )

    confirmed_table = captured_tables[0]
    visible = "\n".join(str(cell) for row in confirmed_table for cell in row)
    for idx in range(1, 13):
        assert f"{idx:04d}" in visible


def test_w_bottom_highlight_active_operation_caps_at_10_and_keeps_3029(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    model_id = pdf_generator.W_BOTTOM_RIGHT_SIDE_MODEL_ID
    confirmed_empty = w_bottom_operation_row(
        model_id,
        "confirmed_operation",
        row_type="empty_state",
        stock_id="",
        stock_display=pdf_generator.MODEL_EMPTY_STATE_TEXT,
        report_line="both",
        row_action_status="empty_state",
        buy_rank_eligible="False",
    )
    active_stock_ids = [
        "1590",
        "1609",
        "1618",
        "2301",
        "2323",
        "2331",
        "2374",
        "3029",
        "3596",
        "5469",
        "6134",
        "6153",
    ]
    active_rows = [
        numbered_w_bottom_operation_row(
            model_id,
            "active_operation",
            stock_id,
            display_order,
            stock_display=f"{stock_id} 零壹" if stock_id == "3029" else f"{stock_id} Active",
        )
        for display_order, stock_id in enumerate(active_stock_ids, start=1)
    ]

    pdf_generator.render_w_bottom_operation_section(
        [],
        {
            "model_readiness": w_bottom_readiness(model_id),
            "w_bottom_right_side_operation": pd.DataFrame([confirmed_empty, *active_rows]),
        },
        model_id,
        "highlight",
        "mainstream",
    )

    active_table = captured_tables[1]
    visible = "\n".join(str(cell) for row in active_table for cell in row)
    visible_stock_count = sum(1 for stock_id in active_stock_ids if stock_id in visible)
    assert visible_stock_count == pdf_generator.OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS
    assert "3029 零壹" in visible
    assert "6134 Active" not in visible


def test_w_bottom_pdf_renderer_sanitizes_pending_entry_price_text(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    model_id = pdf_generator.W_BOTTOM_RIGHT_SIDE_MODEL_ID
    confirmed = w_bottom_operation_row(model_id, "confirmed_operation")
    confirmed.update(
        {
            "entry_basis_zh": "",
            "entry_rule_id": "",
            "entry_price_status_zh": "下一個交易日開盤價待確認",
            "entry_date": "",
            "entry_price": "",
        }
    )
    active_empty = w_bottom_operation_row(
        model_id,
        "active_operation",
        row_type="empty_state",
        stock_id="",
        stock_display=pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT,
        report_line="both",
        row_action_status="empty_state",
        buy_rank_eligible="False",
    )

    pdf_generator.render_w_bottom_operation_section(
        [],
        {
            "model_readiness": w_bottom_readiness(model_id),
            "w_bottom_right_side_operation": pd.DataFrame([confirmed, active_empty]),
        },
        model_id,
        "highlight",
        "mainstream",
    )

    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "待確認" not in visible
    assert "確認價未定" in visible


def test_w_bottom_pdf_renderer_fails_closed_without_integrated_readiness() -> None:
    model_id = pdf_generator.W_BOTTOM_RIGHT_SIDE_MODEL_ID
    operation_rows = pd.DataFrame([w_bottom_operation_row(model_id, "confirmed_operation")])

    with pytest.raises(RuntimeError, match="pdf_integrated_daily_adapter"):
        pdf_generator.render_w_bottom_operation_section(
            [],
            {
                "model_readiness": w_bottom_readiness(model_id, status="pending_pdf_renderer"),
                "w_bottom_right_side_operation": operation_rows,
            },
            model_id,
            "highlight",
            "mainstream",
        )


def test_w_bottom_pdf_renderer_keeps_model_owned_empty_state_inside_tables(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    model_id = pdf_generator.W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID
    operation_rows = pd.DataFrame(
        [
            w_bottom_operation_row(
                model_id,
                "confirmed_operation",
                row_type="empty_state",
                stock_id="",
                stock_display=pdf_generator.MODEL_EMPTY_STATE_TEXT,
                report_line="both",
                row_action_status="empty_state",
                buy_rank_eligible="False",
            ),
            w_bottom_operation_row(
                model_id,
                "active_operation",
                row_type="empty_state",
                stock_id="",
                stock_display=pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT,
                report_line="both",
                row_action_status="empty_state",
                buy_rank_eligible="False",
            ),
        ]
    )

    pdf_generator.render_w_bottom_operation_section(
        [],
        {
            "model_readiness": w_bottom_readiness(model_id),
            "w_bottom_neckline_operation": operation_rows,
        },
        model_id,
        "highlight",
        "mainstream",
    )

    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == "W底頸線帶量突破確認模型 - 本日可買 / 已確認買入候選"
    assert confirmed[2][-1] == pdf_generator.MODEL_EMPTY_STATE_TEXT
    assert active[0][0] == "W底頸線帶量突破確認模型 - 操作中"
    assert active[2][-1] == pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT
