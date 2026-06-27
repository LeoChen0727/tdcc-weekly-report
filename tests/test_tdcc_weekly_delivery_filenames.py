from pathlib import Path

import pandas as pd
import pytest

from scripts import build_tdcc_weekly_candidate_reports as builder
from scripts import validate_tdcc_weekly_candidate_reports as validator


MODEL_CROSS_WEEKLY_SECTION = "model_cross_weekly_increase_tdcc_short_term_continuation_d5_d10"
MODEL_CROSS_CONSECUTIVE_SECTION = "model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10"


def _tdcc_manifest() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "section_order": 1,
                "section_id": "weekly_increase",
                "section_title_zh": "Weekly increase",
                "table_contract": "tdcc_ranking",
                "include_in_highlight": True,
                "highlight_limit": 10,
                "include_in_full": True,
                "full_limit": 50,
                "required": True,
                "enabled": True,
                "notes_zh": "",
            },
            {
                "section_order": 2,
                "section_id": "consecutive_accumulation",
                "section_title_zh": "Consecutive accumulation",
                "table_contract": "tdcc_ranking",
                "include_in_highlight": True,
                "highlight_limit": 10,
                "include_in_full": True,
                "full_limit": 50,
                "required": True,
                "enabled": True,
                "notes_zh": "",
            },
            {
                "section_order": 3,
                "section_id": MODEL_CROSS_WEEKLY_SECTION,
                "section_title_zh": "Weekly increase x model",
                "table_contract": "model_cross",
                "include_in_highlight": True,
                "highlight_limit": 10,
                "include_in_full": True,
                "full_limit": 50,
                "required": True,
                "enabled": True,
                "notes_zh": "",
            },
            {
                "section_order": 4,
                "section_id": MODEL_CROSS_CONSECUTIVE_SECTION,
                "section_title_zh": "Consecutive accumulation x model",
                "table_contract": "model_cross",
                "include_in_highlight": True,
                "highlight_limit": 10,
                "include_in_full": True,
                "full_limit": 50,
                "required": True,
                "enabled": True,
                "notes_zh": "",
            },
        ],
        columns=builder.SECTION_MANIFEST_COLUMNS,
    )


def _tdcc_report(section_ids: list[str], report_kind: str = "highlight") -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    stock_by_section = {
        "weekly_increase": "1001",
        "consecutive_accumulation": "1002",
        MODEL_CROSS_WEEKLY_SECTION: "1003",
        MODEL_CROSS_CONSECUTIVE_SECTION: "1004",
    }
    for index, section_id in enumerate(section_ids, start=1):
        row = {column: "" for column in builder.REPORT_COLUMNS}
        row.update(
            {
                "report_kind": report_kind,
                "section_id": section_id,
                "section_name_zh": section_id,
                "section_rank": "1",
                "tdcc_list_type": section_id,
                "signal_date": "20260626",
                "stock_id": stock_by_section[section_id],
                "stock_name": f"Stock {index}",
                "tdcc_score": "10",
                "tdcc_effective_increase_count": "1",
                "tdcc_high_pair_effective_streak_weeks": "2",
            }
        )
        if section_id.startswith("model_cross_"):
            row["model_id"] = "tdcc_short_term_continuation_d5_d10"
        rows.append(row)
    return builder.ensure_columns(pd.DataFrame(rows), builder.REPORT_COLUMNS)


def test_tdcc_weekly_delivery_pdf_paths_use_report_ready_signal_date() -> None:
    paths = builder.delivery_pdf_paths("20260612")

    assert paths["highlight"] == Path(
        "output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260612.pdf"
    )
    assert paths["full"] == Path(
        "output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260612.pdf"
    )
    assert validator.delivery_pdf_path("highlight", "20260612") == paths["highlight"]
    assert validator.delivery_pdf_path("full", "20260612") == paths["full"]


def test_tdcc_weekly_delivery_pdf_paths_reject_non_signal_date() -> None:
    with pytest.raises(RuntimeError, match="YYYYMMDD"):
        builder.delivery_pdf_path("highlight", "2026-06-12")

    with pytest.raises(RuntimeError, match="YYYYMMDD"):
        validator.delivery_pdf_path("full", "")


def test_tdcc_weekly_model_cross_empty_sections_do_not_fail_builder_validation() -> None:
    manifest = _tdcc_manifest()
    highlight = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "highlight")
    full = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "full")

    builder.validate_outputs(highlight, full, manifest)


def test_tdcc_weekly_core_required_sections_still_fail_when_empty() -> None:
    manifest = _tdcc_manifest()
    highlight = _tdcc_report(["consecutive_accumulation"], "highlight")
    full = _tdcc_report(["consecutive_accumulation"], "full")

    with pytest.raises(RuntimeError, match="weekly_increase"):
        builder.validate_outputs(highlight, full, manifest)


def test_tdcc_weekly_markdown_lists_empty_model_cross_sections(tmp_path: Path) -> None:
    manifest = _tdcc_manifest()
    report = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "highlight")
    path = tmp_path / "tdcc_weekly.md"

    builder.write_report_md(report, path, "TDCC weekly", manifest, "highlight", "20260626")

    text = path.read_text(encoding="utf-8")
    assert "## Consecutive accumulation x model" in text
    assert "本週無符合此模型交集條件" in text


def test_tdcc_weekly_validator_lists_empty_model_cross_sections_as_zero_count_warning() -> None:
    manifest = _tdcc_manifest()
    report = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "highlight")
    weekly_source = pd.DataFrame([{"stock_id": "1001"}])
    consecutive_source = pd.DataFrame([{"stock_id": "1002"}])
    errors: list[str] = []
    warnings: list[str] = []

    validator.validate_report(
        report,
        "highlight report-ready CSV",
        "highlight",
        "20260626",
        weekly_source,
        consecutive_source,
        manifest,
        errors,
        warnings,
    )

    assert errors == []
    assert any(MODEL_CROSS_CONSECUTIVE_SECTION in warning for warning in warnings)
    section_counts = validator.report_section_counts(report, manifest, "highlight")
    assert section_counts[MODEL_CROSS_WEEKLY_SECTION] == 0
    assert section_counts[MODEL_CROSS_CONSECUTIVE_SECTION] == 0
