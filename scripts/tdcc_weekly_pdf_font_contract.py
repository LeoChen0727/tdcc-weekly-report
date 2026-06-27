from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
TDCC_WEEKLY_PDF_FONT_PATH = REPO_ROOT / "assets" / "fonts" / "TDCCSansTC-Regular.ttf"
TDCC_WEEKLY_PDF_FONT_NAME = "TDCCSansTC-Regular"
TDCC_WEEKLY_PDF_FONT_TOKEN = "TDCCSansTC-Regular"
TDCC_WEEKLY_PDF_FORBIDDEN_FONT_TOKENS = {
    "STSong-Light",
    "STSong",
}


def repo_relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def register_tdcc_weekly_pdf_font() -> str:
    if not TDCC_WEEKLY_PDF_FONT_PATH.exists():
        raise RuntimeError(
            "TDCC weekly PDF font asset is missing; refusing to render with a fallback font: "
            f"{repo_relative(TDCC_WEEKLY_PDF_FONT_PATH)}"
        )
    if TDCC_WEEKLY_PDF_FONT_PATH.stat().st_size < 1_000_000:
        raise RuntimeError(
            "TDCC weekly PDF font asset is unexpectedly small; refusing to render with a fallback font: "
            f"{repo_relative(TDCC_WEEKLY_PDF_FONT_PATH)}"
        )

    try:
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except Exception as exc:  # pragma: no cover - dependency gate
        raise RuntimeError(f"reportlab font registration unavailable for TDCC weekly PDF: {exc}") from exc

    try:
        pdfmetrics.registerFont(TTFont(TDCC_WEEKLY_PDF_FONT_NAME, str(TDCC_WEEKLY_PDF_FONT_PATH)))
    except Exception as exc:
        raise RuntimeError(
            "TDCC weekly PDF font registration failed; refusing to render with a fallback font: "
            f"{repo_relative(TDCC_WEEKLY_PDF_FONT_PATH)}: {exc}"
        ) from exc
    return TDCC_WEEKLY_PDF_FONT_NAME


def pdf_base_fonts(path: Path) -> set[str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency gate
        raise RuntimeError(f"pypdf unavailable for TDCC weekly font validation: {exc}") from exc

    if not path.exists() or path.stat().st_size < 10_000:
        raise RuntimeError(f"TDCC weekly PDF missing or too small for font validation: {repo_relative(path)}")

    fonts: set[str] = set()
    reader = PdfReader(str(path))
    for page in reader.pages:
        resources = page.get("/Resources") or {}
        collect_resource_fonts(resources, fonts)
    return fonts


def collect_resource_fonts(resources: object, fonts: set[str]) -> None:
    try:
        font_dict = resources.get("/Font") or {}
    except AttributeError:
        font_dict = {}
    for font_ref in font_dict.values():
        font = font_ref.get_object()
        base_font = font.get("/BaseFont")
        if base_font:
            fonts.add(str(base_font))

    try:
        xobjects = resources.get("/XObject") or {}
    except AttributeError:
        xobjects = {}
    for xobject_ref in xobjects.values():
        xobject = xobject_ref.get_object()
        nested_resources = xobject.get("/Resources")
        if nested_resources:
            collect_resource_fonts(nested_resources, fonts)


def normalized_font_name(font_name: str) -> str:
    return re.sub(r"^/[A-Z]{6}\+", "/", font_name)


def validate_tdcc_weekly_pdf_font_contract(paths: Iterable[Path]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    failures: list[str] = []
    for path in paths:
        fonts = sorted(pdf_base_fonts(path))
        result[repo_relative(path)] = fonts
        normalized = [normalized_font_name(font) for font in fonts]
        if not any(TDCC_WEEKLY_PDF_FONT_TOKEN in font for font in normalized):
            failures.append(
                f"{repo_relative(path)} missing required TDCC weekly PDF font token "
                f"{TDCC_WEEKLY_PDF_FONT_TOKEN}; fonts={fonts}"
            )
        forbidden_hits = [
            font
            for font in normalized
            for forbidden in TDCC_WEEKLY_PDF_FORBIDDEN_FONT_TOKENS
            if forbidden in font
        ]
        if forbidden_hits:
            failures.append(f"{repo_relative(path)} uses forbidden fallback fonts: {sorted(set(forbidden_hits))}")

    if failures:
        raise RuntimeError("TDCC weekly PDF font contract failed:\n" + "\n".join(failures))
    return result
