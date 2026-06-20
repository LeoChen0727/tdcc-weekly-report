from __future__ import annotations

from pathlib import Path

from scripts import validate_individual_pdf_contract_consumers as validator


def model_row(model_id: str = "individual_model", approved: str = "true") -> dict[str, str]:
    return {
        "model_id": model_id,
        "approved_for_individual_pdf": approved,
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
    allowed_consumers: str = "individual_pdf;validator",
    source_file: str = "output/latest/individual_stock_reports/individual_stock_chatgpt_packet_index.csv",
) -> dict[str, str]:
    return {
        "overlay_id": f"test_{field_name}",
        "source_layer": "individual_pdf_fixture",
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
        "approved_for_daily_pdf": "true",
        "approved_for_tdcc_weekly_pdf": "true",
        "approved_for_individual_pdf": approved,
        "effective_from": "2026-06-21",
        "deprecated_after": "",
        "change_reason": "test",
    }


def test_individual_pdf_contract_consumer_validator_passes() -> None:
    assert validator.main() == 0


def test_individual_model_ids_must_exist_and_be_approved() -> None:
    rows = [
        model_row("known_but_not_individual", approved="false"),
        model_row("individual_model", approved="true"),
    ]

    assert validator.validate_model_ids(["individual_model"], rows) == []

    errors = validator.validate_model_ids(["known_but_not_individual", "missing_model"], rows)
    assert any("not approved_for_individual_pdf=true" in error for error in errors)
    assert any("not in stock model contract" in error for error in errors)


def test_model_id_discovery_reads_explicit_individual_output_columns(tmp_path: Path) -> None:
    output = tmp_path / "individual_index.csv"
    output.write_text("stock_id,model_id\n2330,individual_model\n2317,\n", encoding="utf-8")

    assert validator.model_ids_from_individual_outputs([output]) == {"individual_model"}


def test_unapproved_event_field_is_rejected_even_for_disclosure() -> None:
    usage = validator.EventFieldUsage(
        "catalyst_summary",
        "output/latest/individual_stock_reports/individual_stock_chatgpt_packet_index.csv",
        "csv_header",
    )

    errors = validator.validate_event_field_usages([usage], [event_row(approved="false")])

    assert any("not approved_for_individual_pdf=true" in error for error in errors)


def test_event_field_requires_individual_pdf_consumer_approval() -> None:
    usage = validator.EventFieldUsage(
        "catalyst_summary",
        "output/latest/individual_stock_reports/individual_stock_chatgpt_packet_index.csv",
        "csv_header",
    )

    errors = validator.validate_event_field_usages([usage], [event_row(allowed_consumers="daily_pdf")])

    assert any("lacks individual_pdf consumer approval" in error for error in errors)


def test_disclosure_only_event_field_cannot_enter_score_or_ranking_contexts() -> None:
    rows = [event_row("catalyst_strength_score")]
    score_usage = validator.EventFieldUsage(
        "catalyst_strength_score",
        "scripts/individual_pdf_fixture.py",
        "score",
        10,
        "pdf_score = catalyst_strength_score",
    )
    ranking_usage = validator.EventFieldUsage(
        "catalyst_strength_score",
        "scripts/individual_pdf_fixture.py",
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
        "scripts/individual_pdf_fixture.py",
        "reason",
        12,
        "action_summary_zh = catalyst_summary",
    )

    errors = validator.validate_event_field_usages([usage], [event_row()])

    assert any("reason text context" in error for error in errors)
    assert any("degraded event/catalyst source" in error for error in errors)


def test_source_context_detection_ignores_field_name_suffixes() -> None:
    contexts = validator.source_contexts("display_columns = ['catalyst_strength_score']", "catalyst_strength_score")
    assert contexts == {"source_reference"}

    contexts = validator.source_contexts("pdf_score = catalyst_strength_score", "catalyst_strength_score")
    assert contexts == {"score"}


def test_event_field_discovery_reads_individual_csv_header(tmp_path: Path) -> None:
    source = tmp_path / "renderer.py"
    source.write_text("columns = ['stock_id']\n", encoding="utf-8")
    output = tmp_path / "individual_stock_chatgpt_packet_index.csv"
    output.write_text("stock_id,catalyst_summary\n2330,ok\n", encoding="utf-8")

    usages = validator.discover_event_field_usages(
        [event_row("catalyst_summary", source_file=output.as_posix())],
        source_paths=[source],
        output_paths=[output],
    )

    assert usages == [validator.EventFieldUsage("catalyst_summary", output.as_posix(), "csv_header")]


def test_private_pdf_rule_detection_blocks_pdf_side_scoring(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text("pdf_side_score = catalyst_strength_score\n", encoding="utf-8")

    errors = validator.validate_private_pdf_rules([renderer])

    assert any("private PDF-side scoring" in error for error in errors)


def test_private_pdf_rule_detection_blocks_daily_pdf_output_consumption(tmp_path: Path) -> None:
    renderer = tmp_path / "renderer.py"
    renderer.write_text("path = 'chatgpt_side_outputs_official/mainstream.pdf'\n", encoding="utf-8")

    errors = validator.validate_private_pdf_rules([renderer])

    assert any("daily stock recommendation official PDF outputs" in error for error in errors)
