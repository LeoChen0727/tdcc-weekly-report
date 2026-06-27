from pathlib import Path

import pytest

from scripts import tdcc_weekly_pdf_font_contract as contract


def test_tdcc_weekly_repo_kai_font_registers() -> None:
    assert contract.tdcc_weekly_kai_font_path().exists()
    font_name = contract.register_tdcc_weekly_pdf_font()
    assert font_name == contract.TDCC_WEEKLY_PDF_FONT_NAME


def test_tdcc_weekly_font_contract_rejects_stsong_fallback(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    pdf = tmp_path / "tdcc_weekly.pdf"
    pdf.write_bytes(b"%PDF-" + b"x" * 10_000)

    monkeypatch.setattr(contract, "pdf_base_fonts", lambda path: {"/STSong-Light", "/Helvetica"})

    with pytest.raises(RuntimeError, match="STSong-Light"):
        contract.validate_tdcc_weekly_pdf_font_contract([pdf])


def test_tdcc_weekly_font_contract_requires_kai_font(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    pdf = tmp_path / "tdcc_weekly.pdf"
    pdf.write_bytes(b"%PDF-" + b"x" * 10_000)

    monkeypatch.setattr(contract, "pdf_base_fonts", lambda path: {"/Helvetica"})

    with pytest.raises(RuntimeError, match="Kai font token"):
        contract.validate_tdcc_weekly_pdf_font_contract([pdf])


def test_tdcc_weekly_font_contract_rejects_noto_sans_fallback(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    pdf = tmp_path / "tdcc_weekly.pdf"
    pdf.write_bytes(b"%PDF-" + b"x" * 10_000)

    monkeypatch.setattr(contract, "pdf_base_fonts", lambda path: {"/AAAAAA+TDCCSansTC-Regular", "/Helvetica"})

    with pytest.raises(RuntimeError, match="TDCCSansTC"):
        contract.validate_tdcc_weekly_pdf_font_contract([pdf])


def test_tdcc_weekly_font_contract_accepts_subset_dfkai_font(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    pdf = tmp_path / "tdcc_weekly.pdf"
    pdf.write_bytes(b"%PDF-" + b"x" * 10_000)

    monkeypatch.setattr(contract, "pdf_base_fonts", lambda path: {"/AAAAAA+DFKaiShu-SB-Estd-BF", "/Helvetica"})

    result = contract.validate_tdcc_weekly_pdf_font_contract([pdf])

    assert result


def test_tdcc_weekly_font_contract_accepts_subset_tw_kai_font(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    pdf = tmp_path / "tdcc_weekly.pdf"
    pdf.write_bytes(b"%PDF-" + b"x" * 10_000)

    monkeypatch.setattr(contract, "pdf_base_fonts", lambda path: {"/AAAAAA+TW-Kai", "/Helvetica"})

    result = contract.validate_tdcc_weekly_pdf_font_contract([pdf])

    assert result


def test_tdcc_weekly_font_registration_fails_without_repo_kai(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    missing_font = tmp_path / "missing-tw-kai.ttf"
    monkeypatch.setenv(contract.TDCC_WEEKLY_PDF_FONT_PATH_ENV, str(missing_font))

    with pytest.raises(RuntimeError, match="requires the repo-controlled Traditional Chinese Kai font"):
        contract.register_tdcc_weekly_pdf_font()
