from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_tdcc_chatgpt_tracking_outputs.py"
VALIDATOR = ROOT / "scripts" / "validate_tdcc_chatgpt_tracking_outputs.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_tracking_packet_builder_emits_validator_required_weekly_section() -> None:
    section = "## TDCC Weekly Increase and Consecutive Candidate Reports"

    assert section in read(VALIDATOR)
    assert section in read(BUILDER)


def test_tracking_packet_builder_upserts_weekly_report_readme_keys() -> None:
    source = read(BUILDER)
    required_keys = [
        "tdcc_weekly_increase_ranking_csv_raw_url",
        "tdcc_weekly_increase_ranking_md_raw_url",
        "tdcc_consecutive_accumulation_ranking_csv_raw_url",
        "tdcc_consecutive_accumulation_ranking_md_raw_url",
        "tdcc_weekly_model_cross_summary_csv_raw_url",
        "tdcc_weekly_model_cross_summary_md_raw_url",
        "tdcc_weekly_candidate_highlight_for_report_csv_raw_url",
        "tdcc_weekly_candidate_highlight_for_report_md_raw_url",
        "tdcc_weekly_candidate_full_for_report_csv_raw_url",
        "tdcc_weekly_candidate_full_for_report_md_raw_url",
        "tdcc_weekly_candidate_highlight_md_raw_url",
        "tdcc_weekly_candidate_full_md_raw_url",
        "tdcc_weekly_candidate_highlight_pdf_raw_url",
        "tdcc_weekly_candidate_full_pdf_raw_url",
        "tdcc_weekly_candidate_highlight_pdf_pages_url",
        "tdcc_weekly_candidate_full_pdf_pages_url",
    ]

    for key in required_keys:
        assert key in source
