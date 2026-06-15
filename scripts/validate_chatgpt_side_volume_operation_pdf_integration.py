from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


CURATED_CANDIDATE_PDF_TITLE_PARTS = [
    "主流股每日推薦精華",
    "非主流股每日推薦精華",
]

FULL_CANDIDATE_PDF_TITLE_PARTS = [
    "主流股完整候選清單",
    "非主流股完整候選清單",
]

CANDIDATE_PDF_TITLE_PARTS = CURATED_CANDIDATE_PDF_TITLE_PARTS + FULL_CANDIDATE_PDF_TITLE_PARTS

MAINSTREAM_CURATED_REQUIRED_TEXT = [
    "放量攻擊模型",
]

REQUIRED_VOLUME_OPERATION_TEXT = [
    "放量攻擊模型",
    "已確認操作",
    "待確認",
    "操作中",
    "中位數報酬",
]

MAINSTREAM_CURATED_FORBIDDEN_TEXT = [
    "主流股觀察清單",
]

FORBIDDEN_RAW_TOKENS = [
    "buy_rank_eligible",
    "row_action_status",
    "confirmed_buy_candidate",
]

FORBIDDEN_DECISION_LAYER_TEXT = [
    "程式端操作評級",
    "程式端評級",
    "程式端建議買進",
    "建議買進",
]


def extract_text(path: Path) -> str:
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def compact_text(text: str) -> str:
    return "".join(text.split())


def find_pdf(output_dir: Path, title_part: str) -> Path | None:
    matches = sorted(output_dir.glob(f"*{title_part}*.pdf"))
    return matches[0] if matches else None


def validate_output_dir(output_dir: Path) -> list[str]:
    errors: list[str] = []
    pdfs = sorted(output_dir.glob("*.pdf"))
    if len(pdfs) < 6:
        errors.append(f"expected at least six ChatGPT-side PDFs in {output_dir}, got {len(pdfs)}")

    all_text: dict[Path, str] = {}
    for pdf in pdfs:
        try:
            all_text[pdf] = extract_text(pdf)
        except Exception as exc:
            errors.append(f"{pdf.name}: pypdf could not extract text: {exc}")

    for pdf, text in all_text.items():
        compact = compact_text(text)
        for token in FORBIDDEN_RAW_TOKENS:
            if token in text:
                errors.append(f"{pdf.name}: raw operation token leaked into PDF text: {token}")
        for token in FORBIDDEN_DECISION_LAYER_TEXT:
            if token in compact:
                errors.append(f"{pdf.name}: decision-layer buy text leaked into PDF text: {token}")

    for title_part in CANDIDATE_PDF_TITLE_PARTS:
        pdf = find_pdf(output_dir, title_part)
        if pdf is None:
            errors.append(f"missing candidate PDF matching title: {title_part}")
            continue
        text = all_text.get(pdf, "")
        compact = compact_text(text)
        required_text = (
            MAINSTREAM_CURATED_REQUIRED_TEXT
            if title_part == "主流股每日推薦精華"
            else REQUIRED_VOLUME_OPERATION_TEXT
        )
        for required in required_text:
            if required not in compact:
                errors.append(f"{pdf.name}: missing volume operation text {required!r}")

    mainstream_curated = find_pdf(output_dir, "主流股每日推薦精華")
    if mainstream_curated is not None:
        compact = compact_text(all_text.get(mainstream_curated, ""))
        for forbidden in MAINSTREAM_CURATED_FORBIDDEN_TEXT:
            if forbidden in compact:
                errors.append(f"{mainstream_curated.name}: mainstream curated PDF still contains obsolete front observation section {forbidden!r}")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate ChatGPT-side daily PDFs include the volume breakout operation adapter section."
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_output_dir(args.output_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"chatgpt-side volume operation PDF integration validation passed: {args.output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
