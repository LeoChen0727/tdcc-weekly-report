from __future__ import annotations

import csv
from pathlib import Path

import pytest

from scripts import validate_daily_pdf_contract_consumers as validator

LOW_VOLUME_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
MID_VOLUME_MODEL_ID = "volume_range_breakout_v2_mid_position_momentum_attack"
HIGH_VOLUME_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"


def model_row(model_id: str = LOW_VOLUME_MODEL_ID, approved: str = "true") -> dict[str, str]:
    return {
        "model_id": model_id,
        "approved_for_daily_pdf": approved,
        "pdf_visibility": "pdf_core_model",
    }


def event_row(
    field_name: str = "catalyst_summary",
    *,
    approved: str = "true",
    score_allowed: str = "false",
    ranking_allowed: str = "false",
    reason_text_allowed: str = "false",
    disclosure_only: str = "true",
    degraded_behavior: str = "force_disclosure_only_no_score_no_rank_no_reason",
    allowed_consumers: str = "daily_pdf;validator",
    source_file: str = "output/latest/all_candidates_latest.csv",
) -> dict[str, str]:
    return {
        "overlay_id": f"test_{field_name}",
        "source_layer": "daily_candidate_overlay",
        "source_file": source_file,
        "field_name": field_name,
        "allowed_effect": "disclosure_only",
        "allowed_consumers": allowed_consumers,
        "degraded_behavior": degraded_behavior,
        "score_allowed": score_allowed,
        "ranking_allowed": ranking_allowed,
        "reason_text_allowed": reason_text_allowed,
        "disclosure_only": disclosure_only,
        "requires_backtest": "false",
        "requires_human_review": "false",
        "approved_for_daily_pdf": approved,
        "approved_for_tdcc_weekly_pdf": "true",
        "approved_for_individual_pdf": "true",
        "effective_from": "2026-06-21",
        "deprecated_after": "",
        "change_reason": "test",
    }


def test_daily_pdf_contract_consumer_validator_passes() -> None:
    assert validator.main([]) == 0


def test_runtime_phase_runs_current_data_contracts_without_static_scans(
    tmp_path: Path,
    monkeypatch,
) -> None:
    stock_contract = tmp_path / "stock_model_contract_registry.csv"
    stock_contract.write_text("model_id,approved_for_daily_pdf,pdf_visibility\n", encoding="utf-8")
    monkeypatch.setattr(validator, "STOCK_MODEL_CONTRACT", stock_contract)
    monkeypatch.setattr(validator, "EVENT_CATALYST_CONTRACT", tmp_path / "missing_event_contract.csv")

    rows = {
        stock_contract: [model_row("runtime_model")],
        validator.DAILY_MODEL_REGISTRY: [
            {
                "model_id": "runtime_model",
                "model_registry_active": "true",
                "report_line_applicability": "both",
            }
        ],
        validator.DAILY_MODEL_PARAMETERS: [
            {"model_id": "runtime_model", "pdf_visibility": "pdf_core_model"}
        ],
        validator.DAILY_MODEL_READINESS: [
            {
                "model_id": "runtime_model",
                "presentation_allowed": "true",
                "pdf_integration_status": "pdf_integrated_daily_adapter",
            }
        ],
    }
    monkeypatch.setattr(validator, "load_csv_rows", lambda path: rows.get(path, []))
    monkeypatch.setattr(validator, "model_ids_from_report_outputs", lambda: {"runtime_model"})

    def forbidden(*args, **kwargs):
        raise AssertionError("runtime phase invoked a static source/AST/research scan")

    for name in (
        "discover_event_field_usages",
        "validate_event_field_usages",
        "validate_private_pdf_rules",
        "validate_renderer_fixed_model_table_contract",
        "validate_operation_row_metric_renderer_contract",
        "validate_research_recommendations_not_direct_pdf_inputs",
    ):
        monkeypatch.setattr(validator, name, forbidden)

    adapter_calls: list[bool] = []

    def validate_adapter(readiness_rows, **kwargs):
        assert readiness_rows == rows[validator.DAILY_MODEL_READINESS]
        adapter_calls.append(kwargs["require_renderer_contract"])
        return []

    monkeypatch.setattr(validator, "validate_pdf_integrated_operation_adapter_contract", validate_adapter)

    errors, used, required, usages, _, event_rows = validator.validate(
        validator.VALIDATION_PHASE_RUNTIME
    )

    assert errors == []
    assert used == {"runtime_model"}
    assert required == {"runtime_model"}
    assert usages == []
    assert event_rows == []
    assert adapter_calls == [False]
    assert validator.parse_args([]).phase == validator.VALIDATION_PHASE_FULL


def test_runtime_phase_propagates_model_display_and_adapter_errors(
    tmp_path: Path,
    monkeypatch,
) -> None:
    stock_contract = tmp_path / "stock.csv"
    stock_contract.write_text("model_id\n", encoding="utf-8")
    monkeypatch.setattr(validator, "STOCK_MODEL_CONTRACT", stock_contract)
    monkeypatch.setattr(validator, "load_csv_rows", lambda path: [])
    monkeypatch.setattr(validator, "model_ids_from_report_outputs", lambda: set())
    monkeypatch.setattr(validator, "validate_model_ids", lambda *args: ["model approval sentinel"])
    monkeypatch.setattr(
        validator,
        "validate_required_display_model_coverage",
        lambda *args: ["display roster sentinel"],
    )

    def validate_adapter(*args, **kwargs):
        assert kwargs["require_renderer_contract"] is False
        return ["data adapter sentinel"]

    monkeypatch.setattr(validator, "validate_pdf_integrated_operation_adapter_contract", validate_adapter)

    errors, *_ = validator.validate(validator.VALIDATION_PHASE_RUNTIME)

    assert errors == [
        "model approval sentinel",
        "display roster sentinel",
        "data adapter sentinel",
    ]


def test_full_phase_keeps_event_renderer_and_research_scans(tmp_path: Path, monkeypatch) -> None:
    stock_contract = tmp_path / "stock.csv"
    event_contract = tmp_path / "event.csv"
    stock_contract.write_text("model_id\n", encoding="utf-8")
    event_contract.write_text("field_name\n", encoding="utf-8")
    monkeypatch.setattr(validator, "STOCK_MODEL_CONTRACT", stock_contract)
    monkeypatch.setattr(validator, "EVENT_CATALYST_CONTRACT", event_contract)
    monkeypatch.setattr(validator, "load_csv_rows", lambda path: [])
    monkeypatch.setattr(validator, "model_ids_from_report_outputs", lambda: set())
    monkeypatch.setattr(validator, "validate_model_ids", lambda *args: [])
    monkeypatch.setattr(validator, "validate_required_display_model_coverage", lambda *args: [])

    calls: list[str] = []
    monkeypatch.setattr(
        validator,
        "discover_event_field_usages",
        lambda rows: calls.append("discover_event") or [],
    )
    for name in (
        "validate_event_field_usages",
        "validate_private_pdf_rules",
        "validate_renderer_fixed_model_table_contract",
        "validate_operation_row_metric_renderer_contract",
        "validate_research_recommendations_not_direct_pdf_inputs",
    ):
        monkeypatch.setattr(
            validator,
            name,
            lambda *args, function_name=name: calls.append(function_name) or [],
        )
    monkeypatch.setattr(
        validator,
        "validate_pdf_integrated_operation_adapter_contract",
        lambda *args, **kwargs: calls.append(f"adapter:{kwargs['require_renderer_contract']}") or [],
    )

    errors, *_ = validator.validate(validator.VALIDATION_PHASE_FULL)

    assert errors == []
    assert calls == [
        "discover_event",
        "validate_event_field_usages",
        "validate_private_pdf_rules",
        "validate_renderer_fixed_model_table_contract",
        "validate_operation_row_metric_renderer_contract",
        "adapter:True",
        "validate_research_recommendations_not_direct_pdf_inputs",
    ]


def test_runtime_output_does_not_claim_skipped_event_or_private_scans(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        validator,
        "validate",
        lambda phase: ([], {"m"}, {"m"}, [], [model_row("m")], []),
    )

    assert validator.main(["--phase", "runtime"]) == 0
    output = capsys.readouterr().out

    assert "validation_phase=runtime" in output
    assert "event_catalyst_contract=" not in output
    assert "daily_event_contract_approved_rows=" not in output
    assert "daily_used_event_fields=" not in output
    assert "blocked_contract_fields=" not in output


def test_daily_pdf_model_ids_must_exist_and_be_approved() -> None:
    rows = [
        model_row("known_but_not_daily", approved="false"),
        model_row(LOW_VOLUME_MODEL_ID, approved="true"),
    ]

    assert validator.validate_model_ids([LOW_VOLUME_MODEL_ID], rows) == []

    errors = validator.validate_model_ids(["known_but_not_daily", "missing_model"], rows)
    assert any("not approved_for_daily_pdf=true" in error for error in errors)
    assert any("not in stock model contract" in error for error in errors)


def test_required_display_models_cannot_be_inferred_only_from_signal_rows() -> None:
    model_rows = [
        model_row("hot_theme_pullback"),
        model_row("w_bottom_right_side"),
        model_row("neckline_volume_breakout_confirmation"),
    ]
    registry_rows = [
        {
            "model_id": "hot_theme_pullback",
            "model_registry_active": "True",
            "report_line_applicability": "both",
        },
        {
            "model_id": "w_bottom_right_side",
            "model_registry_active": "True",
            "report_line_applicability": "both",
        },
        {
            "model_id": "neckline_volume_breakout_confirmation",
            "model_registry_active": "True",
            "report_line_applicability": "both",
        },
    ]
    parameter_rows = [
        {"model_id": "hot_theme_pullback", "pdf_visibility": "pdf_core_model"},
        {"model_id": "w_bottom_right_side", "pdf_visibility": "pdf_core_model"},
        {"model_id": "neckline_volume_breakout_confirmation", "pdf_visibility": "pdf_core_model"},
    ]

    errors = validator.validate_required_display_model_coverage(
        {"hot_theme_pullback"},
        model_rows,
        registry_rows,
        parameter_rows,
        [],
    )

    assert any("w_bottom_right_side" in error for error in errors)
    assert any("neckline_volume_breakout_confirmation" in error for error in errors)

    errors = validator.validate_required_display_model_coverage(
        {"hot_theme_pullback", "w_bottom_right_side", "neckline_volume_breakout_confirmation"},
        model_rows,
        registry_rows,
        parameter_rows,
        [],
    )
    assert errors == []


def test_contract_approved_display_model_must_be_in_daily_report_registry() -> None:
    model_rows = [
        model_row(LOW_VOLUME_MODEL_ID),
        model_row(HIGH_VOLUME_MODEL_ID),
    ]
    registry_rows = [
        {
            "model_id": LOW_VOLUME_MODEL_ID,
            "model_registry_active": "True",
            "report_line_applicability": "both",
        }
    ]
    parameter_rows = [
        {"model_id": LOW_VOLUME_MODEL_ID, "pdf_visibility": "pdf_core_model"},
        {"model_id": HIGH_VOLUME_MODEL_ID, "pdf_visibility": "pdf_core_model"},
    ]

    errors = validator.validate_required_display_model_coverage(
        {LOW_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID},
        model_rows,
        registry_rows,
        parameter_rows,
        [],
    )

    assert any("Daily PDF display registry missing required model_id" in error for error in errors)
    assert any(HIGH_VOLUME_MODEL_ID in error for error in errors)


def test_pdf_integrated_presentation_model_must_be_in_daily_report_registry() -> None:
    registry_rows = [
        {
            "model_id": LOW_VOLUME_MODEL_ID,
            "model_registry_active": "True",
            "report_line_applicability": "both",
        }
    ]
    parameter_rows = [
        {"model_id": LOW_VOLUME_MODEL_ID, "pdf_visibility": "pdf_core_model"},
        {"model_id": HIGH_VOLUME_MODEL_ID, "pdf_visibility": "pdf_core_model"},
    ]
    readiness_rows = [
        {
            "model_id": HIGH_VOLUME_MODEL_ID,
            "presentation_allowed": "True",
            "pdf_integration_status": "pdf_integrated_daily_adapter",
        }
    ]

    errors = validator.validate_required_display_model_coverage(
        {LOW_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID},
        [],
        registry_rows,
        parameter_rows,
        readiness_rows,
    )

    assert any("Daily PDF display registry missing required model_id" in error for error in errors)
    assert any(HIGH_VOLUME_MODEL_ID in error for error in errors)


def test_presentation_allowed_model_is_part_of_display_roster() -> None:
    registry_rows = [
        {
            "model_id": "w_bottom_right_side",
            "model_registry_active": "True",
            "report_line_applicability": "both",
        }
    ]
    readiness_rows = [{"model_id": "w_bottom_right_side", "presentation_allowed": "True"}]

    assert validator.display_roster_model_ids(registry_rows, [], readiness_rows) == {"w_bottom_right_side"}


def renderer_source_with_required_order() -> str:
    return (
        f'VOLUME_BREAKOUT_V2_LOW_MODEL_ID = "{LOW_VOLUME_MODEL_ID}"\n'
        f'VOLUME_BREAKOUT_V2_MID_MODEL_ID = "{MID_VOLUME_MODEL_ID}"\n'
        f'VOLUME_BREAKOUT_V2_HIGH_MODEL_ID = "{HIGH_VOLUME_MODEL_ID}"\n'
        'W_BOTTOM_RIGHT_SIDE_MODEL_ID = "w_bottom_right_side"\n'
        'W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID = "neckline_volume_breakout_confirmation"\n'
        'PRICE_PULLBACK_MODEL_ID = "price_pullback_23ema"\n'
        'MODEL_EMPTY_STATE_TEXT = "本日無股票推薦"\n'
        "PDF_PRESENTATION_MODEL_ORDER_OVERRIDES = {\n"
        "    VOLUME_BREAKOUT_V2_LOW_MODEL_ID: 1.0,\n"
        "    VOLUME_BREAKOUT_V2_MID_MODEL_ID: 1.05,\n"
        "    VOLUME_BREAKOUT_V2_HIGH_MODEL_ID: 1.08,\n"
        "    W_BOTTOM_RIGHT_SIDE_MODEL_ID: 1.1,\n"
        "    W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID: 1.2,\n"
        "    PRICE_PULLBACK_MODEL_ID: 1.3,\n"
        "}\n"
        "PDF_PRESENTATION_MODEL_ORDER_OVERRIDES[VOLUME_BREAKOUT_V2_HIGH_MODEL_ID] = 1.08\n"
    )


def renderer_source_with_operation_contract() -> str:
    return (
        renderer_source_with_required_order()
        + "W_BOTTOM_OPERATION_TABLE_MODEL_IDS = {W_BOTTOM_RIGHT_SIDE_MODEL_ID, W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID}\n"
        + "OPERATION_TABLE_MODEL_IDS = {VOLUME_BREAKOUT_V2_LOW_MODEL_ID, VOLUME_BREAKOUT_V2_MID_MODEL_ID, VOLUME_BREAKOUT_V2_HIGH_MODEL_ID, W_BOTTOM_RIGHT_SIDE_MODEL_ID, W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID, PRICE_PULLBACK_MODEL_ID}\n"
        + "W_BOTTOM_OPERATION_INPUT_KEYS = {\n"
        + "    W_BOTTOM_RIGHT_SIDE_MODEL_ID: 'w_bottom_right_side_operation',\n"
        + "    W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID: 'w_bottom_neckline_operation',\n"
        + "}\n"
        + "PRICE_PULLBACK_OPERATION_INPUT_KEY = 'price_pullback_operation'\n"
        + "\"daily_volume_breakout_operation_section_latest.csv\"\n"
        + "\"daily_w_bottom_right_side_operation_section_latest.csv\"\n"
        + "\"daily_neckline_volume_breakout_confirmation_operation_section_latest.csv\"\n"
        + "\"daily_price_pullback_23ema_operation_section_latest.csv\"\n"
        + "def w_bottom_operation_frame():\n"
        + "    return 'pdf_integrated_daily_adapter'\n"
        + "def render_w_bottom_operation_section():\n"
        + "    return 'adapter'\n"
        + "def price_pullback_operation_frame():\n"
        + "    return 'price_pullback_23ema adapter'\n"
        + "def render_price_pullback_operation_section():\n"
        + "    return 'adapter'\n"
        + "def render_volume_range_breakout_operation_section():\n"
        + "    return 'volume adapter'\n"
        + 'OPERATION_HIGHLIGHT_TABLE_CONTRACT = "confirmed_buy_then_active_only"\n'
        + "OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS = 10\n"
        + 'OPERATION_HIGHLIGHT_ROW_LIMITS = {"active_operation": OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS}\n'
        + "def operation_highlight_row_limit(pdf_section):\n"
        + "    return OPERATION_HIGHLIGHT_ROW_LIMITS.get(pdf_section)\n"
        + "def limit_operation_rows_for_pdf_view(rows, pdf_view, pdf_section):\n"
        + "    return rows\n"
        + "def selected_rows():\n"
        + "    return limit_operation_rows_for_pdf_view(selected, pdf_view, pdf_section)\n"
        + 'OPERATION_CONFIRMED_BUY_TABLE_TITLE = "本日可買 / 已確認買入候選"\n'
        + 'OPERATION_ACTIVE_TABLE_TITLE = "操作中"\n'
        + 'OPERATION_ACTIVE_EMPTY_STATE_TEXT = "目前無操作中追蹤列"\n'
        + 'OPERATION_MODEL_SAMPLING_TEXT = "取樣：已確認欄位股票精華版全部列出，操作中欄位股票精華版最多列出十檔股票。"\n'
        + "OPERATION_SECTION_TABLE_START_MIN_ROOM = 88 * mm\n"
        + "OPERATION_SECTION_SHORT_TABLE_START_MIN_ROOM = 48 * mm\n"
        + "OPERATION_SECTION_SHORT_TABLE_MAX_ROWS = 3\n"
        + "STOCK_MODEL_SECTION_TABLE_START_MIN_ROOM = 168 * mm\n"
        + "def append_stock_model_section_start(story, model_name, level):\n"
        + "    story.append(CondPageBreak(STOCK_MODEL_SECTION_TABLE_START_MIN_ROOM))\n"
        + "    append_stock_model_title(story, model_name, level=level)\n"
        + "append_stock_model_section_start(story, model_name, level=2)\n"
        + "def operation_section_table_start_min_room(table_flowable):\n"
        + "    return OPERATION_SECTION_SHORT_TABLE_START_MIN_ROOM\n"
        + "def append_section_label_with_table(\n"
        + "    story,\n"
        + "    label,\n"
        + "    table_flowable,\n"
        + "):\n"
        + "    story.append(CondPageBreak(operation_section_table_start_min_room(table_flowable)))\n"
        + "append_section_label_with_table(\n"
        + "        story,\n"
        + "        OPERATION_CONFIRMED_BUY_TABLE_TITLE,\n"
        + "        table_flowable,\n"
        + ")\n"
        + "append_section_label_with_table(\n"
        + "        story,\n"
        + "        OPERATION_ACTIVE_TABLE_TITLE,\n"
        + "        table_flowable,\n"
        + ")\n"
    )


def test_renderer_fixed_model_table_contract_blocks_zero_row_section_skip(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract()
        + "if not ranked_rows:\n"
        "    continue\n",
        encoding="utf-8",
    )

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("must not skip a model section" in error for error in errors)


def test_renderer_fixed_model_table_contract_requires_empty_state_text(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text("def render():\n    return 'empty'\n", encoding="utf-8")

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("missing zero-candidate text" in error for error in errors)


def test_renderer_contract_blocks_technical_model_status_summary_table(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract()
        + "append_model_status_table(story, inputs, spec, 0, line_label)\n",
        encoding="utf-8",
    )

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("must not render technical model/PDF integration status summary tables" in error for error in errors)


def test_renderer_contract_requires_w_bottom_order_after_volume_attack(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text("MODEL_EMPTY_STATE_TEXT = '本日無股票推薦'\n", encoding="utf-8")

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("W-bottom model sections immediately after volume attack" in error for error in errors)


def test_renderer_contract_requires_operation_oriented_highlight_tables(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(renderer_source_with_required_order(), encoding="utf-8")

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("operation-oriented model highlight tables" in error for error in errors)


def test_renderer_contract_blocks_legacy_confirmed_operation_highlight_cap(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract()
        + 'BROKEN_OPERATION_HIGHLIGHT_LIMITS = {"confirmed_operation": 10, "active_operation": 10}\n',
        encoding="utf-8",
    )

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("must not cap highlight confirmed_operation rows" in error for error in errors)


def test_renderer_contract_blocks_active_operation_highlight_cap_below_10(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract()
        + 'BROKEN_OPERATION_HIGHLIGHT_LIMITS = {"active_operation": 5}\n',
        encoding="utf-8",
    )

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("active_operation rows at exactly 10" in error for error in errors)


def test_renderer_contract_blocks_active_operation_highlight_uncapped(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract()
        + 'BROKEN_OPERATION_HIGHLIGHT_LIMITS = {"active_operation": None}\n',
        encoding="utf-8",
    )

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("active_operation rows uncapped" in error for error in errors)


def test_renderer_contract_blocks_old_operation_empty_state_policy(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract()
        + "DAILY_HIGHLIGHT_VOLUME_EMPTY_CONFIRMED_POLICY = 'text_empty_state'\n"
        + "story.append(para('目前無已確認操作。', BODY_SMALL))\n",
        encoding="utf-8",
    )

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("empty states inside the two main tables" in error for error in errors)


def test_renderer_contract_requires_operation_label_table_start_helper(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract().replace("def append_section_label_with_table(", "def append_label("),
        encoding="utf-8",
    )

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("section-label-with-table helper" in error for error in errors)


def test_renderer_contract_blocks_direct_operation_label_append(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract()
        + "story.append(Paragraph(OPERATION_ACTIVE_TABLE_TITLE, H2))\n",
        encoding="utf-8",
    )

    errors = validator.validate_renderer_fixed_model_table_contract([renderer])

    assert any("must not be appended separately" in error for error in errors)


def test_unapproved_event_field_is_rejected_even_for_disclosure() -> None:
    usage = validator.EventFieldUsage("catalyst_summary", "output/latest/all_candidates_latest.csv", "csv_header")

    errors = validator.validate_event_field_usages([usage], [event_row(approved="false")])

    assert any("not approved_for_daily_pdf=true" in error for error in errors)


def test_event_field_requires_daily_pdf_consumer_approval() -> None:
    usage = validator.EventFieldUsage("catalyst_summary", "output/latest/all_candidates_latest.csv", "csv_header")

    errors = validator.validate_event_field_usages([usage], [event_row(allowed_consumers="tdcc_weekly_pdf")])

    assert any("lacks daily_pdf consumer approval" in error for error in errors)


def test_disclosure_only_event_field_cannot_enter_score_or_ranking_contexts() -> None:
    rows = [event_row("catalyst_strength_score")]
    score_usage = validator.EventFieldUsage(
        "catalyst_strength_score",
        "scripts/daily_pdf_fixture.py",
        "score",
        10,
        "daily_score = catalyst_strength_score",
    )
    ranking_usage = validator.EventFieldUsage(
        "catalyst_strength_score",
        "scripts/daily_pdf_fixture.py",
        "ranking",
        11,
        "sort_values(['catalyst_strength_score'])",
    )

    errors = validator.validate_event_field_usages([score_usage, ranking_usage], rows)

    assert any("score context" in error for error in errors)
    assert any("ranking context" in error for error in errors)


def test_degraded_disclosure_field_cannot_strengthen_reason_text() -> None:
    usage = validator.EventFieldUsage(
        "catalyst_summary",
        "scripts/daily_pdf_fixture.py",
        "reason",
        12,
        "why_selected_zh = catalyst_summary",
    )

    errors = validator.validate_event_field_usages([usage], [event_row()])

    assert any("reason text context" in error for error in errors)
    assert any("degraded event/catalyst source" in error for error in errors)


def test_source_context_detection_ignores_field_name_suffixes() -> None:
    contexts = validator.source_contexts("display_columns = ['catalyst_strength_score']", "catalyst_strength_score")
    assert contexts == {"source_reference"}

    contexts = validator.source_contexts("daily_score = catalyst_strength_score", "catalyst_strength_score")
    assert contexts == {"score"}


def test_daily_event_field_discovery_reads_candidate_csv_header(tmp_path: Path) -> None:
    source = tmp_path / "renderer.py"
    source.write_text("columns = ['stock_id']\n", encoding="utf-8")
    output = tmp_path / "all_candidates_latest.csv"
    output.write_text("stock_id,catalyst_summary\n1234,ok\n", encoding="utf-8")

    usages = validator.discover_event_field_usages(
        [event_row("catalyst_summary", source_file=output.as_posix())],
        source_paths=[source],
        output_paths=[output],
    )

    assert usages == [validator.EventFieldUsage("catalyst_summary", output.as_posix(), "csv_header")]


def test_private_pdf_rule_detection_blocks_research_direct_inputs(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text("path = 'daily_model_parameter_recommendations_latest.csv'\n", encoding="utf-8")

    errors = validator.validate_private_pdf_rules([renderer])

    assert any("research recommendation outputs" in error for error in errors)


def test_operation_row_metric_renderer_contract_passes_current_renderer() -> None:
    assert validator.validate_operation_row_metric_renderer_contract() == []


def test_operation_row_metric_renderer_contract_rejects_baseline_fallback(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        "def operation_row_performance_label(row):\n"
        "    return row.get('win_rate_zh', '-')\n",
        encoding="utf-8",
    )

    errors = validator.validate_operation_row_metric_renderer_contract(renderer)

    assert any("model-owned row_metric contract" in error for error in errors)
    assert any("baseline or legacy metric prefixes" in error for error in errors)


def write_w_bottom_adapter(path: Path, model_id: str, extra_section: str | None = None) -> None:
    columns = sorted(validator.W_BOTTOM_OPERATION_REQUIRED_COLUMNS)
    rows: list[dict[str, str]] = []
    for pdf_view in sorted(validator.W_BOTTOM_OPERATION_REQUIRED_VIEWS):
        for pdf_section in sorted(validator.W_BOTTOM_OPERATION_REQUIRED_SECTIONS):
            rows.append(
                {
                    column: {
                        "model_id": model_id,
                        "pdf_view": pdf_view,
                        "pdf_section": pdf_section,
                        "row_type": "empty_state",
                        "display_order": "1",
                        "operation_asof_date": "20260630",
                        "report_line": "both",
                        "report_line_memberships": "mainstream|non_mainstream",
                        "operation_status": pdf_section,
                        "row_action_status": "empty_state",
                        "buy_rank_eligible": "False",
                    }.get(column, "test")
                    for column in columns
                }
            )
    if extra_section:
        row = {column: "test" for column in columns}
        row.update(
            {
                "model_id": model_id,
                "pdf_view": "highlight",
                "pdf_section": extra_section,
                "row_type": "data",
                "display_order": "2",
                "operation_asof_date": "20260630",
                "report_line": "both",
                "report_line_memberships": "mainstream|non_mainstream",
                "operation_status": extra_section,
                "row_action_status": extra_section,
                "buy_rank_eligible": "False",
            }
        )
        rows.append(row)
    lines = [",".join(columns)]
    lines.extend(",".join(row[column] for column in columns) for row in rows)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_price_pullback_adapter(path: Path, extra_column_drop: str | None = None) -> None:
    columns = sorted(validator.PRICE_PULLBACK_OPERATION_REQUIRED_COLUMNS - ({extra_column_drop} if extra_column_drop else set()))
    rows: list[dict[str, str]] = []
    for pdf_view in sorted(validator.PDF_OPERATION_REQUIRED_VIEWS):
        for pdf_section in sorted(validator.PDF_OPERATION_REQUIRED_SECTIONS):
            rows.append(
                {
                    column: {
                        "model_id": "price_pullback_23ema",
                        "pdf_view": pdf_view,
                        "pdf_section": pdf_section,
                        "row_type": "empty_state",
                        "display_order": "1",
                        "operation_asof_date": "20260703",
                        "report_line": "both",
                        "report_line_memberships": "mainstream|non_mainstream",
                        "operation_status": pdf_section,
                        "operation_status_zh": "empty",
                        "operation_quality_zh": "基礎",
                        "row_action_status": "empty_state",
                        "buy_rank_eligible": "False",
                        "signal_date": "20260703",
                        "entry_rule_id": "signal_date_next_open",
                        "entry_basis_zh": "隔日開盤買入",
                        "stop_loss_rule_id": "sustained_close_below_lower_ma20_ema23_4pct_4d",
                        "stop_basis_zh": "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。",
                        "exit_rule_id": "close_prev20_high_break_next_open",
                        "exit_rule_zh": "收盤突破訊號日前20日高點後，隔日開盤賣出。",
                        "planned_holding_days": "20",
                        "operation_age_days": "",
                        "sample_size": "1160",
                        "win_rate_zh": "66.03%",
                        "neutral_rate_zh": "5.60%",
                        "failure_rate_zh": "28.36%",
                        "avg_return_zh": "+2.90%",
                        "technical_package_win_rate_zh": "75.54%",
                        "technical_package_neutral_rate_zh": "3.52%",
                        "technical_package_failure_rate_zh": "20.95%",
                        "technical_package_avg_return_zh": "+2.96%",
                        "rank_reason_zh": "基礎",
                        "risk_tags_zh": "",
                    }.get(column, "test")
                    for column in columns
                }
            )
    lines = [",".join(columns)]
    lines.extend(",".join(row[column] for column in columns) for row in rows)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    (
        ("valid", None),
        ("missing_file", "missing PDF operation adapter artifact"),
        ("missing_column", "row_metric_status"),
        ("empty_rows", "has no rows"),
        ("wrong_model", "mixes model_ids"),
        ("missing_section", "missing required sections"),
        ("missing_view", "missing required pdf_view"),
        ("incomplete_metric", "incomplete row_metric payload"),
        ("missing_readiness", "readiness row missing"),
    ),
)
def test_data_only_operation_adapter_keeps_csv_contract_without_renderer_scan(
    tmp_path: Path,
    monkeypatch,
    mutation: str,
    expected_error: str | None,
) -> None:
    model_id = "price_pullback_23ema"
    adapter = tmp_path / "daily_price_pullback_23ema_operation_section_latest.csv"
    if mutation != "missing_file":
        write_price_pullback_adapter(
            adapter,
            extra_column_drop="row_metric_status" if mutation == "missing_column" else None,
        )

    if adapter.exists() and mutation not in {"valid", "missing_column"}:
        with adapter.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            fieldnames = list(reader.fieldnames or [])
            rows = list(reader)
        if mutation == "empty_rows":
            rows = []
        elif mutation == "wrong_model":
            for row in rows:
                row["model_id"] = "wrong_model"
        elif mutation == "missing_section":
            rows = [row for row in rows if row["pdf_section"] != "active_operation"]
        elif mutation == "missing_view":
            rows = [row for row in rows if row["pdf_view"] != "highlight"]
        elif mutation == "incomplete_metric":
            rows[0]["row_type"] = "data"
            rows[0]["row_metric_status"] = "ready"
            rows[0]["row_metric_label_zh"] = ""
        with adapter.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def forbidden_renderer_scan(*args, **kwargs):
        raise AssertionError("data-only adapter validation read renderer source")

    monkeypatch.setattr(validator, "renderer_text_for_operation_contract", forbidden_renderer_scan)
    readiness_rows = [] if mutation == "missing_readiness" else [
        {
            "model_id": model_id,
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "daily_adapter_sections": "confirmed_operation,active_operation",
        }
    ]
    errors = validator.validate_pdf_integrated_operation_adapter_contract(
        readiness_rows,
        source_paths=[tmp_path / "missing_renderer.py"],
        artifact_paths={model_id: adapter},
        renderer_tokens={model_id: ("must_not_be_read",)},
        required_columns_by_model={model_id: validator.PRICE_PULLBACK_OPERATION_REQUIRED_COLUMNS},
        allowed_sections_by_model={model_id: validator.PDF_OPERATION_REQUIRED_SECTIONS},
        required_model_ids={model_id},
        require_renderer_contract=False,
    )

    if expected_error is None:
        assert errors == []
    else:
        assert any(expected_error in error for error in errors)


def test_w_bottom_operation_adapter_contract_requires_integrated_readiness_and_sections(
    tmp_path: Path,
    monkeypatch,
) -> None:
    model_id = "w_bottom_right_side"
    adapter = tmp_path / "daily_w_bottom_right_side_operation_section_latest.csv"
    write_w_bottom_adapter(adapter, model_id)
    monkeypatch.setattr(validator, "W_BOTTOM_OPERATION_ARTIFACTS", {model_id: adapter})

    readiness_rows = [
        {
            "model_id": model_id,
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "daily_adapter_sections": "confirmed_operation,active_operation",
        }
    ]

    assert validator.validate_w_bottom_operation_adapter_contract(readiness_rows) == []

    readiness_rows[0]["pdf_integration_status"] = "pending_pdf_renderer"
    errors = validator.validate_w_bottom_operation_adapter_contract(readiness_rows)
    assert any("pdf_integrated_daily_adapter" in error for error in errors)


def test_w_bottom_operation_adapter_contract_rejects_pdf_forbidden_sections(
    tmp_path: Path,
    monkeypatch,
) -> None:
    model_id = "neckline_volume_breakout_confirmation"
    adapter = tmp_path / "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv"
    write_w_bottom_adapter(adapter, model_id, extra_section="pending_confirmation")
    monkeypatch.setattr(validator, "W_BOTTOM_OPERATION_ARTIFACTS", {model_id: adapter})
    readiness_rows = [
        {
            "model_id": model_id,
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "daily_adapter_sections": "confirmed_operation,active_operation,pending_confirmation",
        }
    ]

    errors = validator.validate_w_bottom_operation_adapter_contract(readiness_rows)

    assert any("PDF-forbidden sections" in error and "pending_confirmation" in error for error in errors)


def test_pdf_integrated_operation_adapter_must_be_consumed_by_renderer(tmp_path: Path) -> None:
    adapter = tmp_path / "daily_price_pullback_23ema_operation_section_latest.csv"
    write_price_pullback_adapter(adapter)
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        renderer_source_with_operation_contract().replace(
            '"daily_price_pullback_23ema_operation_section_latest.csv"\n',
            "",
        ),
        encoding="utf-8",
    )
    readiness_rows = [
        {
            "model_id": "price_pullback_23ema",
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "daily_adapter_sections": "confirmed_operation,active_operation",
        }
    ]

    errors = validator.validate_pdf_integrated_operation_adapter_contract(
        readiness_rows,
        source_paths=[renderer],
        artifact_paths={"price_pullback_23ema": adapter},
        renderer_tokens={
            "price_pullback_23ema": (
                "PRICE_PULLBACK_MODEL_ID",
                "daily_price_pullback_23ema_operation_section_latest.csv",
                "render_price_pullback_operation_section",
            )
        },
        required_columns_by_model={"price_pullback_23ema": validator.PRICE_PULLBACK_OPERATION_REQUIRED_COLUMNS},
        allowed_sections_by_model={"price_pullback_23ema": validator.PDF_OPERATION_REQUIRED_SECTIONS},
    )

    assert any("not consumed from its dedicated adapter" in error for error in errors)


def test_price_pullback_operation_adapter_contract_requires_pdf_safe_columns(tmp_path: Path) -> None:
    adapter = tmp_path / "daily_price_pullback_23ema_operation_section_latest.csv"
    write_price_pullback_adapter(adapter, extra_column_drop="row_metric_status")
    renderer = tmp_path / "renderer.py"
    renderer.write_text(renderer_source_with_operation_contract(), encoding="utf-8")
    readiness_rows = [
        {
            "model_id": "price_pullback_23ema",
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "daily_adapter_sections": "confirmed_operation,active_operation",
        }
    ]

    errors = validator.validate_pdf_integrated_operation_adapter_contract(
        readiness_rows,
        source_paths=[renderer],
        artifact_paths={"price_pullback_23ema": adapter},
        renderer_tokens={
            "price_pullback_23ema": (
                "PRICE_PULLBACK_MODEL_ID",
                "daily_price_pullback_23ema_operation_section_latest.csv",
                "render_price_pullback_operation_section",
            )
        },
        required_columns_by_model={"price_pullback_23ema": validator.PRICE_PULLBACK_OPERATION_REQUIRED_COLUMNS},
        allowed_sections_by_model={"price_pullback_23ema": validator.PDF_OPERATION_REQUIRED_SECTIONS},
    )

    assert any("row_metric_status" in error for error in errors)
