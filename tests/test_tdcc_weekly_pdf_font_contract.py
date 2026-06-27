from pathlib import Path

import pytest

from scripts import tdcc_weekly_pdf_font_contract as contract


def test_tdcc_weekly_repo_font_asset_registers() -> None:
    assert contract.TDCC_WEEKLY_PDF_FONT_PATH.exists()
    font_name = contract.register_tdcc_weekly_pdf_font()
    assert font_name == contract.TDCC_WEEKLY_PDF_FONT_NAME


def test_tdcc_weekly_font_contract_rejects_stsong_fallback(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    pdf = tmp_path / "tdcc_weekly.pdf"
    pdf.write_bytes(b"%PDF-" + b"x" * 10_000)

    monkeypatch.setattr(contract, "pdf_base_fonts", lambda path: {"/STSong-Light", "/Helvetica"})

    with pytest.raises(RuntimeError, match="STSong-Light"):
        contract.validate_tdcc_weekly_pdf_font_contract([pdf])


def test_tdcc_weekly_font_contract_requires_repo_font(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    pdf = tmp_path / "tdcc_weekly.pdf"
    pdf.write_bytes(b"%PDF-" + b"x" * 10_000)

    monkeypatch.setattr(contract, "pdf_base_fonts", lambda path: {"/Helvetica"})

    with pytest.raises(RuntimeError, match="TDCCSansTC-Regular"):
        contract.validate_tdcc_weekly_pdf_font_contract([pdf])


def test_tdcc_weekly_font_contract_accepts_subset_repo_font(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    pdf = tmp_path / "tdcc_weekly.pdf"
    pdf.write_bytes(b"%PDF-" + b"x" * 10_000)

    monkeypatch.setattr(contract, "pdf_base_fonts", lambda path: {"/AAAAAA+TDCCSansTC-Regular", "/Helvetica"})

    result = contract.validate_tdcc_weekly_pdf_font_contract([pdf])

    assert result
