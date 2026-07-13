from __future__ import annotations

from pathlib import Path

import pytest

from scripts import generate_chatgpt_side_daily_reports as renderer
from scripts import validate_chatgpt_side_pdf_contract as contract


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
RENDERER = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
README_PUBLISHER = ROOT / "publish_chatgpt_report_readme_and_check.py"


def _source(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def test_contract_validator_passes() -> None:
    assert contract.main() == 0


def test_renderer_import_does_not_require_runtime_font_registration() -> None:
    assert renderer.FONT_NAME == contract.CHATGPT_DAILY_PDF_FONT_NAME
    assert renderer.Paragraph("標楷體繁體中文", renderer.BODY)


def test_renderer_setup_fonts_fails_closed_when_dfkai_is_missing(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    missing_font = tmp_path / "missing-kaiu.ttf"
    monkeypatch.setattr(renderer, "chatgpt_daily_dfkai_font_path", lambda: missing_font)

    with pytest.raises(RuntimeError, match="requires validated kaiu.ttf / DFKai-SB"):
        renderer.setup_fonts()


def test_contract_validator_tracks_six_chatgpt_side_builders() -> None:
    assert contract.CHATGPT_SIDE_BUILDERS == (
        "build_mainstream_curated_pdf",
        "build_mainstream_full_candidate_pdf",
        "build_non_mainstream_curated_pdf",
        "build_non_mainstream_full_candidate_pdf",
        "build_warrant_market_auxiliary_pdf",
        "build_market_risk_background_pdf",
    )

    renderer = _source(RENDERER)
    for builder in contract.CHATGPT_SIDE_BUILDERS:
        assert f"def {builder}(" in renderer


def test_daily_full_pipeline_does_not_generate_or_publish_retired_repo_pdfs() -> None:
    workflow = _source(WORKFLOW)

    for literal in contract.FORBIDDEN_WORKFLOW_LITERALS:
        assert literal not in workflow
    for filename in contract.RETIRED_PUBLIC_PDF_FILENAMES:
        assert f"docs/latest/{filename}" not in workflow


def test_packet_and_readme_do_not_expose_retired_repo_pdf_links() -> None:
    packet = _source(PACKET_BUILDER)
    readme = _source(README_PUBLISHER)

    for filename in contract.RETIRED_PUBLIC_PDF_FILENAMES:
        assert f"docs/latest/{filename}" not in packet
        assert f"docs/latest/{filename}" not in readme
    for filename in contract.RETIRED_FIXED_PDF_FILENAMES:
        assert f"output/latest/{filename}" not in packet
        assert f"output/latest/{filename}" not in readme
    for forbidden in (
        "daily_market_pdf_report_manifest_latest",
        "daily_market_report_validation_latest",
    ):
        assert forbidden not in packet
        assert forbidden not in readme


def _fake_font_path(tmp_path: Path) -> Path:
    path = tmp_path / "kaiu.ttf"
    path.write_bytes(b"x" * 1_000_001)
    return path


def _six_fake_pdfs(tmp_path: Path) -> list[Path]:
    paths = []
    for index in range(6):
        path = tmp_path / f"daily_{index}.pdf"
        path.write_bytes(b"%PDF-" + b"x" * 10_001)
        paths.append(path)
    return paths


def test_dfkai_font_path_uses_exact_daily_env_var(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = tmp_path / "kaiu.ttf"
    monkeypatch.setenv(contract.CHATGPT_DAILY_DFKAI_FONT_PATH_ENV, str(font_path))

    assert contract.chatgpt_daily_dfkai_font_path() == font_path


def test_dfkai_font_file_validation_fails_closed_when_path_missing(tmp_path: Path) -> None:
    missing_font = tmp_path / "missing-kaiu.ttf"

    errors = contract.dfkai_font_validation_errors(missing_font)

    assert any("font path does not exist" in error for error in errors)
    with pytest.raises(RuntimeError, match="font path does not exist"):
        contract.validate_dfkai_font_file(missing_font)


def test_dfkai_font_file_validation_requires_exact_name_table_token(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = _fake_font_path(tmp_path)
    monkeypatch.setattr(contract, "font_name_records", lambda path: {"NotDFKai-SB"})
    monkeypatch.setattr(
        contract,
        "font_cmap_codepoints",
        lambda path: {ord(char) for char in contract.TRADITIONAL_CHINESE_GLYPH_CANARY},
    )

    errors = contract.dfkai_font_validation_errors(font_path)

    assert any("required exact token" in error for error in errors)


def test_dfkai_font_file_validation_rejects_empty_name_table(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = _fake_font_path(tmp_path)
    monkeypatch.setattr(contract, "font_name_records", lambda path: set())
    monkeypatch.setattr(
        contract,
        "font_cmap_codepoints",
        lambda path: {ord(char) for char in contract.TRADITIONAL_CHINESE_GLYPH_CANARY},
    )

    errors = contract.dfkai_font_validation_errors(font_path)

    assert any("required exact token" in error for error in errors)


def test_dfkai_font_file_validation_accepts_exact_name_table_token(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = _fake_font_path(tmp_path)
    monkeypatch.setattr(contract, "font_name_records", lambda path: {"DFKai-SB"})
    monkeypatch.setattr(
        contract,
        "font_cmap_codepoints",
        lambda path: {ord(char) for char in contract.TRADITIONAL_CHINESE_GLYPH_CANARY},
    )

    assert contract.dfkai_font_validation_errors(font_path) == []


def test_daily_six_pdf_font_contract_rejects_substring_basefont(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+NotDFKai-SB", "/Identity-H", True, True)],
    )

    with pytest.raises(RuntimeError, match="missing required exact DFKai"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_rejects_generic_dfkai_basefont(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKai", "/Identity-H", True, True)],
    )

    with pytest.raises(RuntimeError, match="missing required exact DFKai"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_accepts_exact_subset_dfkai_basefont(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKai-SB", "/Identity-H", True, True)],
    )

    assert contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_rejects_exact_dfkai_without_embedding(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKai-SB", "/Identity-H", False, True)],
    )

    with pytest.raises(RuntimeError, match="not embedded"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_rejects_exact_dfkai_without_tounicode(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKai-SB", "/Identity-H", True, False)],
    )

    with pytest.raises(RuntimeError, match="missing ToUnicode"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_rejects_fallback_font(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/MSung-Light", "/UniGB-UCS2-H", False, False)],
    )

    with pytest.raises(RuntimeError, match="MSung-Light"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_requires_all_six_pdfs(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)[:5]
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKaiShu-SB-Estd-BF", "/Identity-H", True, True)],
    )

    with pytest.raises(RuntimeError, match="exactly 6 PDFs"):
        contract.validate_daily_six_pdf_font_contract(paths)
