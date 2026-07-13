from __future__ import annotations

from dataclasses import dataclass
import os
import re
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
RENDERER = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
README_PUBLISHER = ROOT / "publish_chatgpt_report_readme_and_check.py"
REPLAY_VALIDATOR = ROOT / "scripts" / "validate_chatgpt_daily_report_new_conversation_replay.py"

CHATGPT_DAILY_DFKAI_FONT_PATH_ENV = "CHATGPT_DAILY_DFKAI_FONT_PATH"
CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH = Path(r"C:\Windows\Fonts\kaiu.ttf")
CHATGPT_DAILY_PDF_FONT_NAME = "DFKai-SB"
TRADITIONAL_CHINESE_GLYPH_CANARY = "標楷體繁體中文測試買賣停損勝敗本日無股票推薦"
DFKAI_NAME_TABLE_TOKENS = {"DFKai-SB", "DFKaiShu-SB-Estd-BF"}
DFKAI_PDF_BASE_FONTS = {"/DFKai-SB", "/DFKaiShu-SB-Estd-BF"}
FORBIDDEN_DAILY_PDF_FONT_TOKENS = (
    "MSung-Light",
    "MSung",
    "STSong-Light",
    "STSong",
    "UniGB-UCS2-H",
    "UniGB",
    "TW-Kai",
)

CHATGPT_SIDE_BUILDERS = (
    "build_mainstream_curated_pdf",
    "build_mainstream_full_candidate_pdf",
    "build_non_mainstream_curated_pdf",
    "build_non_mainstream_full_candidate_pdf",
    "build_warrant_market_auxiliary_pdf",
    "build_market_risk_background_pdf",
)

RETIRED_FIXED_PDF_FILENAMES = (
    "daily_market_curated_report_latest.pdf",
    "daily_market_full_table_report_latest.pdf",
    "mainstream_daily_recommendation_highlight_latest.pdf",
    "mainstream_full_candidate_list_latest.pdf",
    "non_mainstream_daily_recommendation_highlight_latest.pdf",
    "non_mainstream_full_candidate_list_latest.pdf",
)

RETIRED_PUBLIC_PDF_FILENAMES = (
    *RETIRED_FIXED_PDF_FILENAMES,
    "warrant_market_report_latest.pdf",
    "market_risk_dashboard_latest.pdf",
)

FORBIDDEN_WORKFLOW_LITERALS = (
    "python scripts/generate_daily_market_pdf.py",
    "python scripts/validate_daily_market_report.py",
    "Generate fixed daily market PDF reports",
    "Validate fixed daily market PDF reports",
)


@dataclass(frozen=True)
class PdfFontRecord:
    base_font: str
    encoding: str
    embedded: bool
    to_unicode: bool


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def function_text(text: str, name: str) -> str:
    match = re.search(rf"^def {re.escape(name)}\(", text, flags=re.MULTILINE)
    if not match:
        raise ValueError(name)
    start = match.start()
    next_match = re.search(r"^def \w+\(", text[start + 1 :], flags=re.MULTILINE)
    if not next_match:
        return text[start:]
    return text[start : start + 1 + next_match.start()]


def chatgpt_daily_dfkai_font_path() -> Path:
    configured = os.environ.get(CHATGPT_DAILY_DFKAI_FONT_PATH_ENV, "").strip()
    if configured:
        return Path(configured).expanduser()
    return CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH


def font_name_records(font_path: Path) -> set[str]:
    try:
        from fontTools.ttLib import TTFont as FontToolsTTFont
    except Exception as exc:  # pragma: no cover - dependency gate
        raise RuntimeError(f"fontTools is required to validate DFKai font name tables: {exc}") from exc

    try:
        font = FontToolsTTFont(str(font_path), lazy=True)
    except Exception as exc:
        raise RuntimeError(f"cannot open DFKai font with fontTools: {font_path}: {exc}") from exc
    try:
        names: set[str] = set()
        name_table = font["name"]
        for record in name_table.names:
            try:
                text = record.toUnicode().strip()
            except Exception:
                continue
            if text:
                names.add(text)
        return names
    finally:
        font.close()


def font_cmap_codepoints(font_path: Path) -> set[int]:
    try:
        from fontTools.ttLib import TTFont as FontToolsTTFont
    except Exception as exc:  # pragma: no cover - dependency gate
        raise RuntimeError(f"fontTools is required to validate DFKai cmap coverage: {exc}") from exc

    try:
        font = FontToolsTTFont(str(font_path), lazy=True)
    except Exception as exc:
        raise RuntimeError(f"cannot open DFKai font with fontTools: {font_path}: {exc}") from exc
    try:
        cmap = font.getBestCmap() or {}
        return {int(codepoint) for codepoint in cmap}
    finally:
        font.close()


def dfkai_font_validation_errors(font_path: Path | None = None) -> list[str]:
    path = font_path or chatgpt_daily_dfkai_font_path()
    errors: list[str] = []
    if not path.exists():
        return [
            "daily six-PDF renderer requires kaiu.ttf / DFKai-SB and refuses CJK fallback; "
            f"font path does not exist: {path}"
        ]
    if path.stat().st_size < 1_000_000:
        errors.append(f"DFKai font path is unexpectedly small and may be a fallback stub: {path}")

    try:
        names = font_name_records(path)
    except RuntimeError as exc:
        errors.append(str(exc))
        names = set()
    if not (names & DFKAI_NAME_TABLE_TOKENS):
        sample = ", ".join(sorted(names)[:12])
        errors.append(
            "DFKai font name table missing required exact token "
            f"{sorted(DFKAI_NAME_TABLE_TOKENS)}; font_path={path}; observed={sample}"
        )
    if names and any("TW-Kai" in name for name in names):
        errors.append(f"daily six-PDF renderer must not use TW-Kai for this contract: {path}")

    try:
        cmap_codepoints = font_cmap_codepoints(path)
    except RuntimeError as exc:
        errors.append(str(exc))
        cmap_codepoints = set()
    missing_glyphs = sorted({char for char in TRADITIONAL_CHINESE_GLYPH_CANARY if ord(char) not in cmap_codepoints})
    if missing_glyphs:
        errors.append(
            "DFKai font missing Traditional Chinese glyph canary coverage; "
            f"font_path={path}; missing={''.join(missing_glyphs)}"
        )
    return errors


def validate_dfkai_font_file(font_path: Path | None = None) -> Path:
    path = font_path or chatgpt_daily_dfkai_font_path()
    errors = dfkai_font_validation_errors(path)
    if errors:
        raise RuntimeError("ChatGPT-side daily six-PDF DFKai font validation failed:\n" + "\n".join(errors))
    return path


def _pdf_object(value: object) -> object:
    if hasattr(value, "get_object"):
        try:
            return value.get_object()
        except Exception:
            return value
    return value


def _pdf_has_embedded_font_file(descriptor: object) -> bool:
    descriptor = _pdf_object(descriptor)
    if not hasattr(descriptor, "get"):
        return False
    return any(descriptor.get(key) is not None for key in ("/FontFile", "/FontFile2", "/FontFile3"))


def _font_records_from_font(font_ref: object) -> list[PdfFontRecord]:
    font = _pdf_object(font_ref)
    if not hasattr(font, "get"):
        return []

    base_font = str(font.get("/BaseFont") or "")
    encoding = str(font.get("/Encoding") or "")
    to_unicode = font.get("/ToUnicode") is not None
    descriptor = font.get("/FontDescriptor")
    embedded = _pdf_has_embedded_font_file(descriptor) if descriptor is not None else False

    descendants = _pdf_object(font.get("/DescendantFonts") or [])
    records: list[PdfFontRecord] = []
    if descendants:
        for descendant_ref in descendants:
            descendant = _pdf_object(descendant_ref)
            if not hasattr(descendant, "get"):
                continue
            descendant_base = str(descendant.get("/BaseFont") or base_font)
            descendant_descriptor = descendant.get("/FontDescriptor")
            descendant_embedded = (
                _pdf_has_embedded_font_file(descendant_descriptor)
                if descendant_descriptor is not None
                else embedded
            )
            records.append(
                PdfFontRecord(
                    base_font=descendant_base,
                    encoding=encoding,
                    embedded=descendant_embedded,
                    to_unicode=to_unicode,
                )
            )
    else:
        records.append(
            PdfFontRecord(
                base_font=base_font,
                encoding=encoding,
                embedded=embedded,
                to_unicode=to_unicode,
            )
        )
    return records


def _collect_resource_font_records(resources_ref: object, records: list[PdfFontRecord]) -> None:
    resources = _pdf_object(resources_ref)
    if not hasattr(resources, "get"):
        return

    font_dict = _pdf_object(resources.get("/Font") or {})
    if hasattr(font_dict, "values"):
        for font_ref in font_dict.values():
            records.extend(_font_records_from_font(font_ref))

    xobjects = _pdf_object(resources.get("/XObject") or {})
    if hasattr(xobjects, "values"):
        for xobject_ref in xobjects.values():
            xobject = _pdf_object(xobject_ref)
            if hasattr(xobject, "get") and xobject.get("/Resources"):
                _collect_resource_font_records(xobject.get("/Resources"), records)


def pdf_font_records(path: Path) -> list[PdfFontRecord]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency gate
        raise RuntimeError(f"pypdf is required for daily six-PDF font validation: {exc}") from exc

    if not path.exists() or path.stat().st_size < 10_000:
        raise RuntimeError(f"daily PDF missing or too small for font validation: {path}")

    records: list[PdfFontRecord] = []
    reader = PdfReader(str(path))
    for page in reader.pages:
        _collect_resource_font_records(page.get("/Resources") or {}, records)
    return records


def normalized_pdf_font_name(font_name: str) -> str:
    return re.sub(r"^/[A-Z]{6}\+", "/", font_name)


def canonical_pdf_base_font_name(font_name: str) -> str:
    normalized = normalized_pdf_font_name(font_name)
    return normalized if normalized.startswith("/") else f"/{normalized}"


def validate_daily_six_pdf_font_contract(paths: Iterable[Path]) -> dict[str, list[dict[str, object]]]:
    pdf_paths = list(paths)
    errors: list[str] = []
    result: dict[str, list[dict[str, object]]] = {}
    if len(pdf_paths) != 6:
        errors.append(f"daily six-PDF font contract requires exactly 6 PDFs; observed={len(pdf_paths)}")

    for path in pdf_paths:
        try:
            records = pdf_font_records(path)
        except RuntimeError as exc:
            errors.append(str(exc))
            continue
        serializable = [
            {
                "base_font": record.base_font,
                "encoding": record.encoding,
                "embedded": record.embedded,
                "to_unicode": record.to_unicode,
            }
            for record in records
        ]
        result[str(path)] = serializable

        normalized_records = [
            PdfFontRecord(
                base_font=normalized_pdf_font_name(record.base_font),
                encoding=normalized_pdf_font_name(record.encoding),
                embedded=record.embedded,
                to_unicode=record.to_unicode,
            )
            for record in records
        ]
        all_font_text = " ".join(
            f"{record.base_font} {record.encoding}"
            for record in normalized_records
        )
        forbidden_hits = sorted(
            {
                token
                for token in FORBIDDEN_DAILY_PDF_FONT_TOKENS
                if token in all_font_text
            }
        )
        if forbidden_hits:
            errors.append(f"{path} uses forbidden daily PDF CJK fallback fonts: {forbidden_hits}")

        dfkai_records = [
            record
            for record in normalized_records
            if canonical_pdf_base_font_name(record.base_font) in DFKAI_PDF_BASE_FONTS
        ]
        if not dfkai_records:
            errors.append(
                f"{path} missing required exact DFKai/DFKaiShu BaseFont token {sorted(DFKAI_PDF_BASE_FONTS)}; "
                f"fonts={[record.base_font for record in normalized_records]}"
            )
            continue
        for record in dfkai_records:
            if not record.embedded:
                errors.append(f"{path} DFKai font is not embedded: {record.base_font}")
            if not record.to_unicode:
                errors.append(f"{path} DFKai font is missing ToUnicode mapping: {record.base_font}")

    if errors:
        raise RuntimeError("ChatGPT-side daily six-PDF font contract failed:\n" + "\n".join(errors))
    return result


def validate() -> list[str]:
    errors: list[str] = []

    for path in (WORKFLOW, ENTRYPOINT, RENDERER, PACKET_BUILDER, README_PUBLISHER, REPLAY_VALIDATOR):
        if not path.exists():
            errors.append(f"missing required ChatGPT-side contract file: {path.relative_to(ROOT).as_posix()}")

    if errors:
        return errors

    workflow = read_text(WORKFLOW)
    entrypoint = read_text(ENTRYPOINT)
    renderer = read_text(RENDERER)
    packet = read_text(PACKET_BUILDER)
    readme = read_text(README_PUBLISHER)
    replay_validator = read_text(REPLAY_VALIDATOR)

    for literal in (
        "resolve_daily_report_source_state",
        '"worktree", "add", "--detach"',
        "CHATGPT_DAILY_REPORT_ENTRYPOINT",
        "CHATGPT_DAILY_OUTPUT_DIR",
    ):
        if literal not in entrypoint:
            errors.append(f"official entrypoint missing required source gate literal: {literal}")

    for name in CHATGPT_SIDE_BUILDERS:
        if f"def {name}(" not in renderer:
            errors.append(f"missing ChatGPT-side PDF builder: {name}")
    try:
        main_body = function_text(renderer, "main")
    except ValueError:
        errors.append("ChatGPT-side renderer missing main()")
        main_body = ""
    if "setup_fonts()" not in main_body:
        errors.append("ChatGPT-side renderer main() must validate and register DFKai before rendering")
    for name in CHATGPT_SIDE_BUILDERS:
        if f"{name}(" not in main_body:
            errors.append(f"ChatGPT-side renderer main() does not call builder: {name}")

    for literal in FORBIDDEN_WORKFLOW_LITERALS:
        if literal in workflow:
            errors.append(f"daily_full_pipeline must not run retired fixed PDF path: {literal}")

    for literal in (
        "CHATGPT_DAILY_DFKAI_FONT_PATH_ENV",
        "validate_dfkai_font_file",
        "TTFont(CHATGPT_DAILY_PDF_FONT_NAME",
    ):
        if literal not in renderer:
            errors.append(f"ChatGPT-side daily PDF renderer missing DFKai fail-closed literal: {literal}")
    for forbidden in (
        "UnicodeCIDFont",
        "MSung-Light",
        "STSong-Light",
        "UniGB-UCS2-H",
    ):
        if forbidden in renderer:
            errors.append(f"ChatGPT-side daily PDF renderer must not contain fallback font literal: {forbidden}")
    if "validate_daily_six_pdf_font_contract(paths)" not in replay_validator:
        errors.append("new-conversation replay validator must run daily six-PDF font contract")

    for name in RETIRED_PUBLIC_PDF_FILENAMES:
        docs_copy = f"docs/latest/{name}"
        if docs_copy in workflow:
            errors.append(f"daily_full_pipeline must not publish retired repo PDF artifact: {docs_copy}")
        if docs_copy in packet:
            errors.append(f"packet builder must not expose retired repo PDF artifact: {docs_copy}")
        if docs_copy in readme:
            errors.append(f"README publisher must not expose retired repo PDF artifact: {docs_copy}")

    for name in RETIRED_FIXED_PDF_FILENAMES:
        output_path = f"output/latest/{name}"
        if output_path in packet:
            errors.append(f"packet builder must not expose retired fixed PDF artifact: {output_path}")
        if output_path in readme:
            errors.append(f"README publisher must not expose retired fixed PDF artifact: {output_path}")

    if "daily_market_pdf_report_manifest_latest" in packet:
        errors.append("packet builder must not read retired fixed PDF manifest")
    if "daily_market_report_validation_latest" in packet:
        errors.append("packet builder must not read retired fixed PDF validation")
    if "daily_market_pdf_report_manifest_latest" in readme:
        errors.append("README publisher must not read retired fixed PDF manifest")
    if "daily_market_report_validation_latest" in readme:
        errors.append("README publisher must not read retired fixed PDF validation")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("ChatGPT-side daily PDF contract validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
