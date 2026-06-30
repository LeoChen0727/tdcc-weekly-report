from __future__ import annotations

from pathlib import Path

from scripts import validate_daily_pdf_contract_consumers as validator


def model_row(model_id: str = "volume_range_breakout", approved: str = "true") -> dict[str, str]:
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
    assert validator.main() == 0


def test_daily_pdf_model_ids_must_exist_and_be_approved() -> None:
    rows = [
        model_row("known_but_not_daily", approved="false"),
        model_row("volume_range_breakout", approved="true"),
    ]

    assert validator.validate_model_ids(["volume_range_breakout"], rows) == []

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


def test_renderer_fixed_model_table_contract_blocks_zero_row_section_skip(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text(
        "MODEL_EMPTY_STATE_TEXT = '本日無股票推薦'\n"
        "if not ranked_rows:\n"
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
