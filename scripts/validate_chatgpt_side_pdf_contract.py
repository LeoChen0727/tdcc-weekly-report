from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
RENDERER = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
README_PUBLISHER = ROOT / "publish_chatgpt_report_readme_and_check.py"

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


def validate() -> list[str]:
    errors: list[str] = []

    for path in (WORKFLOW, ENTRYPOINT, RENDERER, PACKET_BUILDER, README_PUBLISHER):
        if not path.exists():
            errors.append(f"missing required ChatGPT-side contract file: {path.relative_to(ROOT).as_posix()}")

    if errors:
        return errors

    workflow = read_text(WORKFLOW)
    entrypoint = read_text(ENTRYPOINT)
    renderer = read_text(RENDERER)
    packet = read_text(PACKET_BUILDER)
    readme = read_text(README_PUBLISHER)

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
    for name in CHATGPT_SIDE_BUILDERS:
        if f"{name}(" not in main_body:
            errors.append(f"ChatGPT-side renderer main() does not call builder: {name}")

    for literal in FORBIDDEN_WORKFLOW_LITERALS:
        if literal in workflow:
            errors.append(f"daily_full_pipeline must not run retired fixed PDF path: {literal}")

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
