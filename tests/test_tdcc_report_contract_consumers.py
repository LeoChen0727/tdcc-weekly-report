from __future__ import annotations

from scripts import validate_tdcc_report_contract_consumers as validator


def event_row(
    field_name: str = "catalyst_summary",
    *,
    approved: str = "true",
    score_allowed: str = "false",
    ranking_allowed: str = "false",
    reason_text_allowed: str = "false",
    disclosure_only: str = "true",
    degraded_behavior: str = "force_disclosure_only_no_score_no_rank_no_reason",
) -> dict[str, str]:
    return {
        "overlay_id": f"test_{field_name}",
        "source_layer": "daily_candidate_overlay",
        "source_file": "output/latest/all_candidates_latest.csv",
        "field_name": field_name,
        "allowed_effect": "disclosure_only",
        "allowed_consumers": "tdcc_weekly_pdf;validator",
        "degraded_behavior": degraded_behavior,
        "score_allowed": score_allowed,
        "ranking_allowed": ranking_allowed,
        "reason_text_allowed": reason_text_allowed,
        "disclosure_only": disclosure_only,
        "requires_backtest": "false",
        "requires_human_review": "false",
        "approved_for_daily_pdf": "true",
        "approved_for_tdcc_weekly_pdf": approved,
        "approved_for_individual_pdf": "true",
        "effective_from": "2026-06-21",
        "deprecated_after": "",
        "change_reason": "test",
    }


def test_tdcc_report_contract_consumer_validator_passes() -> None:
    assert validator.main() == 0


def test_tdcc_model_ids_must_exist_and_be_approved() -> None:
    rows = [
        {"model_id": "known_but_not_tdcc", "approved_for_tdcc_weekly_pdf": "false"},
        {"model_id": "tdcc_short_term_continuation_d5_d10", "approved_for_tdcc_weekly_pdf": "true"},
    ]

    assert validator.validate_model_ids(["tdcc_short_term_continuation_d5_d10"], rows) == []

    errors = validator.validate_model_ids(["known_but_not_tdcc", "missing_model"], rows)
    assert any("not approved for TDCC weekly PDF" in error for error in errors)
    assert any("not in stock model contract" in error for error in errors)


def test_unapproved_event_field_is_rejected_even_for_disclosure() -> None:
    usage = validator.EventFieldUsage("catalyst_summary", "output/latest/tdcc_weekly_report_latest.md", "markdown_text")

    errors = validator.validate_event_field_usages([usage], [event_row(approved="false")])

    assert any("not approved_for_tdcc_weekly_pdf=true" in error for error in errors)


def test_disclosure_only_event_field_cannot_enter_score_or_ranking_contexts() -> None:
    rows = [event_row("catalyst_strength_score")]
    score_usage = validator.EventFieldUsage(
        "catalyst_strength_score",
        "scripts/tdcc_report_fixture.py",
        "score",
        10,
        "tdcc_score = catalyst_strength_score",
    )
    ranking_usage = validator.EventFieldUsage(
        "catalyst_strength_score",
        "scripts/tdcc_report_fixture.py",
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
        "scripts/tdcc_report_fixture.py",
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

    contexts = validator.source_contexts("tdcc_score = catalyst_strength_score", "catalyst_strength_score")
    assert contexts == {"score"}


def test_generic_contract_names_are_not_detected_from_python_variable_names(tmp_path) -> None:
    source = tmp_path / "tdcc_source_fixture.py"
    source.write_text("top = summary.sort_values(['avg_return'])\n", encoding="utf-8")
    output = tmp_path / "tdcc_weekly_output.csv"
    output.write_text("summary,stock_id\nfoo,1234\n", encoding="utf-8")

    usages = validator.discover_event_field_usages(
        [event_row("summary")],
        source_paths=[source],
        output_paths=[output],
    )

    assert usages == [validator.EventFieldUsage("summary", output.as_posix(), "csv_header")]
