from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
import re
import shutil
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

VALIDATION_JSON = LATEST_DIR / "chatgpt_side_pdf_contract_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "chatgpt_side_pdf_contract_validation_latest.md"
DOCS_VALIDATION_MD = DOCS_LATEST_DIR / VALIDATION_MD.name

MAINSTREAM_HIGHLIGHT_TITLE = "\u4e3b\u6d41\u80a1\u6bcf\u65e5\u63a8\u85a6\u7cbe\u83ef"
MAINSTREAM_FULL_TITLE = "\u4e3b\u6d41\u80a1\u5b8c\u6574\u5019\u9078\u6e05\u55ae"
NON_MAINSTREAM_HIGHLIGHT_TITLE = "\u975e\u4e3b\u6d41\u80a1\u6bcf\u65e5\u63a8\u85a6\u7cbe\u83ef"
NON_MAINSTREAM_FULL_TITLE = "\u975e\u4e3b\u6d41\u80a1\u5b8c\u6574\u5019\u9078\u6e05\u55ae"
WARRANT_TITLE = "\u6b0a\u8b49\u5e02\u5834\u8f14\u52a9\u5206\u6790"
MARKET_RISK_TITLE = "\u5e02\u5834\u98a8\u96aa\u8207\u5927\u76e4\u671f\u6b0a\u80cc\u666f"

NEW_LISTED_TERMS = ("\u65b0\u9032\u699c", "\u65b0\u4e0a\u699c")
CONSECUTIVE_LISTED_TERMS = ("\u9023\u7e8c\u699c", "\u9023\u7e8c\u4e0a\u699c")
SUMMARY_SECTION = "\u5404\u6a21\u578b\u65b0\u9032\u699c / \u9023\u7e8c\u699c\u56fa\u5b9a\u6458\u8981"
REPRESENTATIVE_SECTION = "\u5404\u6a21\u578b\u4ee3\u8868\u80a1\u5206\u6790"
FULL_MODEL_LIST_SECTION = "\u5b8c\u6574\u6a21\u578b\u6e05\u55ae"
WARRANT_CALL_HEAT_SECTION = "\u8a8d\u8cfc\u71b1\u5ea6"
MARKET_INDEX_SECTION = "\u5927\u76e4\u6307\u6578\u7d50\u69cb"
FUTURES_OPTIONS_SECTION = "\u671f\u8ca8\u9078\u64c7\u6b0a\u90e8\u4f4d"
DATA_STATUS_SECTION = "\u8cc7\u6599\u72c0\u614b"


@dataclass(frozen=True)
class PdfContract:
    label: str
    relative_path: Path
    expected_title: str
    report_family: str
    pdf_kind: str
    min_pages: int
    max_pages: int
    min_text_chars: int
    first_page_required_any: tuple[tuple[str, ...], ...] = ()
    required_all: tuple[str, ...] = ()
    forbidden_all: tuple[str, ...] = ()


OFFICIAL_PDF_CONTRACTS: tuple[PdfContract, ...] = (
    PdfContract(
        label="mainstream_highlight",
        relative_path=Path("output/latest/mainstream_daily_recommendation_highlight_latest.pdf"),
        expected_title=MAINSTREAM_HIGHLIGHT_TITLE,
        report_family="mainstream",
        pdf_kind="highlight",
        min_pages=2,
        max_pages=220,
        min_text_chars=2_000,
        first_page_required_any=(NEW_LISTED_TERMS, CONSECUTIVE_LISTED_TERMS, (SUMMARY_SECTION,)),
        required_all=(REPRESENTATIVE_SECTION,),
        forbidden_all=(FULL_MODEL_LIST_SECTION,),
    ),
    PdfContract(
        label="mainstream_full",
        relative_path=Path("output/latest/mainstream_full_candidate_list_latest.pdf"),
        expected_title=MAINSTREAM_FULL_TITLE,
        report_family="mainstream",
        pdf_kind="full",
        min_pages=2,
        max_pages=220,
        min_text_chars=2_000,
        first_page_required_any=(NEW_LISTED_TERMS, CONSECUTIVE_LISTED_TERMS, (SUMMARY_SECTION,)),
        required_all=(FULL_MODEL_LIST_SECTION,),
        forbidden_all=(REPRESENTATIVE_SECTION,),
    ),
    PdfContract(
        label="non_mainstream_highlight",
        relative_path=Path("output/latest/non_mainstream_daily_recommendation_highlight_latest.pdf"),
        expected_title=NON_MAINSTREAM_HIGHLIGHT_TITLE,
        report_family="non_mainstream",
        pdf_kind="highlight",
        min_pages=2,
        max_pages=220,
        min_text_chars=2_000,
        first_page_required_any=(NEW_LISTED_TERMS, CONSECUTIVE_LISTED_TERMS, (SUMMARY_SECTION,)),
        required_all=(REPRESENTATIVE_SECTION,),
        forbidden_all=(FULL_MODEL_LIST_SECTION,),
    ),
    PdfContract(
        label="non_mainstream_full",
        relative_path=Path("output/latest/non_mainstream_full_candidate_list_latest.pdf"),
        expected_title=NON_MAINSTREAM_FULL_TITLE,
        report_family="non_mainstream",
        pdf_kind="full",
        min_pages=2,
        max_pages=220,
        min_text_chars=2_000,
        first_page_required_any=(NEW_LISTED_TERMS, CONSECUTIVE_LISTED_TERMS, (SUMMARY_SECTION,)),
        required_all=(FULL_MODEL_LIST_SECTION,),
        forbidden_all=(REPRESENTATIVE_SECTION,),
    ),
    PdfContract(
        label="warrant_market",
        relative_path=Path("output/latest/warrant_market_report_latest.pdf"),
        expected_title=WARRANT_TITLE,
        report_family="warrant",
        pdf_kind="auxiliary",
        min_pages=2,
        max_pages=80,
        min_text_chars=1_000,
        required_all=(DATA_STATUS_SECTION, WARRANT_CALL_HEAT_SECTION),
    ),
    PdfContract(
        label="market_risk",
        relative_path=Path("output/latest/market_risk_dashboard_latest.pdf"),
        expected_title=MARKET_RISK_TITLE,
        report_family="market_risk",
        pdf_kind="background",
        min_pages=2,
        max_pages=80,
        min_text_chars=1_000,
        required_all=(DATA_STATUS_SECTION, MARKET_INDEX_SECTION, FUTURES_OPTIONS_SECTION),
    ),
)

EXPECTED_CONTRACT_COUNT = 6
ALL_REPORT_TITLES = tuple(contract.expected_title for contract in OFFICIAL_PDF_CONTRACTS)


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def strip_report_date_prefix(line: str) -> str:
    text = line.strip()
    return re.sub(r"^\d{8}\s+", "", text)


def first_nonblank_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return ""


def page_texts(path: Path) -> tuple[int, list[str], str]:
    reader = PdfReader(str(path))
    texts: list[str] = []
    for page in reader.pages:
        texts.append(page.extract_text() or "")
    return len(reader.pages), texts, "\n".join(texts)


def title_lines(text: str) -> set[str]:
    found: set[str] = set()
    for line in text.splitlines():
        stripped = strip_report_date_prefix(line)
        if stripped in ALL_REPORT_TITLES:
            found.add(stripped)
    return found


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    haystack = compact(text)
    return any(compact(term) in haystack for term in terms)


def contains_all(text: str, terms: tuple[str, ...]) -> list[str]:
    haystack = compact(text)
    return [term for term in terms if compact(term) not in haystack]


def validate_contract(contract: PdfContract) -> tuple[dict[str, Any], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    path = ROOT / contract.relative_path
    info: dict[str, Any] = {
        "label": contract.label,
        "path": contract.relative_path.as_posix(),
        "exists": path.exists(),
        "size_bytes": path.stat().st_size if path.exists() else 0,
        "pages": 0,
        "text_chars": 0,
        "first_title": "",
        "report_family": contract.report_family,
        "pdf_kind": contract.pdf_kind,
    }

    if "preview" in contract.relative_path.name.lower():
        errors.append(f"{contract.label}: contract path points at a preview PDF")
    if contract.relative_path.parts[:2] != ("output", "latest"):
        errors.append(f"{contract.label}: contract path must use output/latest, got {contract.relative_path.as_posix()}")
    if not path.exists():
        errors.append(f"{contract.label}: missing PDF {contract.relative_path.as_posix()}")
        return info, errors, warnings

    try:
        pages, texts, text = page_texts(path)
    except Exception as exc:
        errors.append(f"{contract.label}: pypdf could not open/extract text: {exc}")
        return info, errors, warnings

    first_page_text = texts[0] if texts else ""
    first_title = strip_report_date_prefix(first_nonblank_line(text))
    info["pages"] = pages
    info["text_chars"] = len(compact(text))
    info["first_title"] = first_title

    if pages < contract.min_pages:
        errors.append(f"{contract.label}: page count {pages} below minimum {contract.min_pages}")
    if pages > contract.max_pages:
        warnings.append(f"{contract.label}: page count {pages} above expected range {contract.max_pages}")
    if len(compact(text)) < contract.min_text_chars:
        errors.append(f"{contract.label}: extracted text too short: {len(compact(text))}")
    if first_title != contract.expected_title:
        errors.append(f"{contract.label}: first title mismatch: got {first_title!r}, expected {contract.expected_title!r}")

    for terms in contract.first_page_required_any:
        if not contains_any(first_page_text, terms):
            errors.append(f"{contract.label}: first page missing required section marker from {list(terms)!r}")

    missing_required = contains_all(text, contract.required_all)
    for marker in missing_required:
        errors.append(f"{contract.label}: missing required marker {marker!r}")

    for forbidden in contract.forbidden_all:
        if compact(forbidden) in compact(text):
            errors.append(f"{contract.label}: forbidden marker appears {forbidden!r}")

    seen_titles = title_lines(text)
    wrong_titles = sorted(seen_titles - {contract.expected_title})
    if wrong_titles:
        errors.append(f"{contract.label}: other report title line(s) found: {wrong_titles!r}")

    return info, errors, warnings


def validate() -> tuple[dict[str, Any], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    pdf_results: list[dict[str, Any]] = []

    if len(OFFICIAL_PDF_CONTRACTS) != EXPECTED_CONTRACT_COUNT:
        errors.append(
            f"validator must cover exactly {EXPECTED_CONTRACT_COUNT} official daily production PDFs; "
            f"got {len(OFFICIAL_PDF_CONTRACTS)}"
        )

    labels = [contract.label for contract in OFFICIAL_PDF_CONTRACTS]
    if len(set(labels)) != len(labels):
        errors.append(f"duplicate PDF contract labels: {labels!r}")

    paths = [contract.relative_path.as_posix() for contract in OFFICIAL_PDF_CONTRACTS]
    if len(set(paths)) != len(paths):
        errors.append(f"duplicate PDF contract paths: {paths!r}")

    for contract in OFFICIAL_PDF_CONTRACTS:
        info, contract_errors, contract_warnings = validate_contract(contract)
        pdf_results.append(info)
        errors.extend(contract_errors)
        warnings.extend(contract_warnings)

    result = {
        "generated_at": now_text(),
        "status": "pass" if not errors else "fail",
        "contract_count": len(OFFICIAL_PDF_CONTRACTS),
        "expected_contract_count": EXPECTED_CONTRACT_COUNT,
        "pdfs": pdf_results,
        "checks": {
            "uses_output_latest_formal_pdfs": all(path.startswith("output/latest/") and "preview" not in path.lower() for path in paths),
            "covers_six_official_daily_pdfs": len(OFFICIAL_PDF_CONTRACTS) == EXPECTED_CONTRACT_COUNT,
            "has_highlight_full_boundary_rules": any(c.pdf_kind == "highlight" and c.forbidden_all for c in OFFICIAL_PDF_CONTRACTS)
            and any(c.pdf_kind == "full" and c.forbidden_all for c in OFFICIAL_PDF_CONTRACTS),
            "has_new_and_consecutive_section_rules": all(
                c.first_page_required_any for c in OFFICIAL_PDF_CONTRACTS if c.report_family in {"mainstream", "non_mainstream"}
            ),
            "has_cross_report_title_pollution_rules": True,
        },
        "errors": errors,
        "warnings": warnings,
    }
    return result, errors, warnings


def write_outputs(result: dict[str, Any]) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# ChatGPT-Side Daily PDF Contract Validation",
        "",
        f"- generated_at: `{result.get('generated_at', '')}`",
        f"- status: `{result.get('status', '')}`",
        f"- contract_count: `{result.get('contract_count', '')}`",
        "",
        "## PDF Files",
    ]
    for item in result.get("pdfs", []):
        lines.append(
            f"- {item['label']}: `{item['path']}` / pages `{item['pages']}` / "
            f"text_chars `{item['text_chars']}` / title `{item['first_title']}`"
        )
    lines.extend(["", "## Checks"])
    for key, value in result.get("checks", {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Errors"])
    if result.get("errors"):
        lines.extend(f"- {error}" for error in result["errors"])
    else:
        lines.append("- none")
    lines.extend(["", "## Warnings"])
    if result.get("warnings"):
        lines.extend(f"- {warning}" for warning in result["warnings"])
    else:
        lines.append("- none")
    lines.append("")
    VALIDATION_MD.write_text("\n".join(lines), encoding="utf-8")
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(VALIDATION_MD, DOCS_VALIDATION_MD)


def main() -> int:
    result, errors, _warnings = validate()
    write_outputs(result)
    print(f"Saved: {VALIDATION_JSON.relative_to(ROOT).as_posix()}")
    print(f"Saved: {VALIDATION_MD.relative_to(ROOT).as_posix()}")
    if errors:
        print("PDF contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PDF contract validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
