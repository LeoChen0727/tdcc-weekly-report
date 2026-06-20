from pathlib import Path

import pytest

from scripts import build_tdcc_weekly_candidate_reports as builder
from scripts import validate_tdcc_weekly_candidate_reports as validator


def test_tdcc_weekly_delivery_pdf_paths_use_report_ready_signal_date() -> None:
    paths = builder.delivery_pdf_paths("20260612")

    assert paths["highlight"] == Path("output/latest/TDCC大戶籌碼週報_精華版_20260612.pdf")
    assert paths["full"] == Path("output/latest/TDCC大戶籌碼週報_完整版_20260612.pdf")
    assert validator.delivery_pdf_path("highlight", "20260612") == paths["highlight"]
    assert validator.delivery_pdf_path("full", "20260612") == paths["full"]


def test_tdcc_weekly_delivery_pdf_paths_reject_non_signal_date() -> None:
    with pytest.raises(RuntimeError, match="YYYYMMDD"):
        builder.delivery_pdf_path("highlight", "2026-06-12")

    with pytest.raises(RuntimeError, match="YYYYMMDD"):
        validator.delivery_pdf_path("full", "")
