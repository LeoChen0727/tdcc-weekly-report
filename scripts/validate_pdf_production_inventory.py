from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "docs" / "pdf_production_inventory.md"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
PUBLISHER = ROOT / "publish_chatgpt_report_readme_and_check.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
RULES_BUILDER = ROOT / "build_chatgpt_daily_report_rules.py"
DOCS_LATEST = ROOT / "docs" / "latest"
OUTPUT_LATEST = ROOT / "output" / "latest"
DATA_FRESHNESS = OUTPUT_LATEST / "data_freshness_latest.csv"


@dataclass(frozen=True)
class PdfProducer:
    purpose: str
    producer_paths: tuple[str, ...]
    validator_paths: tuple[str, ...]
    publisher_paths: tuple[str, ...]


PDF_PRODUCERS: tuple[PdfProducer, ...] = (
    PdfProducer(
        purpose="ChatGPT-side daily",
        producer_paths=(
            "scripts/run_chatgpt_daily_report_entrypoint.py",
            "scripts/generate_chatgpt_side_daily_reports.py",
        ),
        validator_paths=(
            "scripts/validate_chatgpt_side_pdf_contract.py",
            "scripts/validate_daily_pdf_contract_consumers.py",
            "scripts/validate_chatgpt_side_pdf_layout_independence.py",
            "scripts/validate_chatgpt_side_volume_operation_pdf_integration.py",
        ),
        publisher_paths=(),
    ),
    PdfProducer(
        purpose="Daily repo market source artifact",
        producer_paths=("build_daily_market_report_artifacts.py",),
        validator_paths=(
            "scripts/validate_daily_production_boundaries.py",
            "scripts/validate_daily_report_source_preflight.py",
            "scripts/validate_daily_staged_paths.py",
        ),
        publisher_paths=(".github/workflows/daily_full_pipeline.yml",),
    ),
    PdfProducer(
        purpose="TDCC weekly",
        producer_paths=("scripts/build_tdcc_weekly_candidate_reports.py",),
        validator_paths=(
            "scripts/validate_tdcc_weekly_candidate_reports.py",
            "scripts/validate_pdf_facing_display_text.py",
        ),
        publisher_paths=(".github/workflows/tdcc_weekly.yml",),
    ),
    PdfProducer(
        purpose="Market risk/background",
        producer_paths=("scripts/build_market_regime_dashboard.py",),
        validator_paths=("scripts/validate_market_regime_dashboard.py",),
        publisher_paths=(),
    ),
    PdfProducer(
        purpose="Warrant market auxiliary",
        producer_paths=("scripts/build_warrant_market_report.py",),
        validator_paths=("tests/test_warrant_market_report_fallback.py",),
        publisher_paths=(),
    ),
    PdfProducer(
        purpose="Daily signal performance reports",
        producer_paths=("scripts/generate_daily_signal_performance_report.py",),
        validator_paths=("scripts/validate_daily_signal_performance.py",),
        publisher_paths=(".github/workflows/research_backtest_pipeline.yml",),
    ),
    PdfProducer(
        purpose="Individual stock report",
        producer_paths=("scripts/generate_individual_stock_report.py",),
        validator_paths=("scripts/validate_individual_stock_outputs.py",),
        publisher_paths=(
            ".github/workflows/individual_stock_report.yml",
            ".github/workflows/individual_stock_data_refresh.yml",
        ),
    ),
)


RETIRED_PRODUCER_PATHS = (
    "scripts/generate_daily_market_pdf.py",
    "scripts/validate_daily_market_report.py",
    "tests/test_daily_market_pdf_layout.py",
)

RETIRED_FIXED_DAILY_PDF_NAMES = (
    "daily_market_curated_report_latest.pdf",
    "daily_market_full_table_report_latest.pdf",
    "mainstream_daily_recommendation_highlight_latest.pdf",
    "mainstream_full_candidate_list_latest.pdf",
    "non_mainstream_daily_recommendation_highlight_latest.pdf",
    "non_mainstream_full_candidate_list_latest.pdf",
)

DAILY_MARKET_REPO_ARTIFACT_LIFECYCLE = (
    (
        "output/latest/daily_market_summary_latest.pdf",
        "compatibility_alias",
        "must_keep_until_packet_and_raw_health_consumers_move",
    ),
    (
        "output/latest/daily_market_full_latest.pdf",
        "compatibility_alias",
        "must_keep_until_packet_and_raw_health_consumers_move",
    ),
    (
        "output/latest/published_reports/daily_market/每日全市場候選股監測報告_精華版_YYYYMMDD.pdf",
        "published_human_pdf",
        "published_date_stamped_daily_market_pdf",
    ),
    (
        "output/latest/published_reports/daily_market/完整候選股清單_完整版_YYYYMMDD.pdf",
        "published_human_pdf",
        "published_date_stamped_daily_market_pdf",
    ),
)

REPO_ARTIFACT_DAILY_PDF_NAMES = tuple(
    Path(path).name for path, _role, _status in DAILY_MARKET_REPO_ARTIFACT_LIFECYCLE
)

DAILY_MARKET_COMPATIBILITY_ALIAS_PATHS = (
    OUTPUT_LATEST / "daily_market_summary_latest.pdf",
    OUTPUT_LATEST / "daily_market_full_latest.pdf",
)

LEGACY_ROOT_DAILY_MARKET_PDF_PATHS = (
    OUTPUT_LATEST / "每日全市場候選股監測報告_精華版.pdf",
    OUTPUT_LATEST / "完整候選股清單_完整版表格.pdf",
)

LEGACY_ROOT_DAILY_MARKET_PDF_NAMES = tuple(
    path.name for path in LEGACY_ROOT_DAILY_MARKET_PDF_PATHS
)

AUXILIARY_INTERNAL_PDF_NAMES = (
    "warrant_market_report_latest.pdf",
    "market_risk_dashboard_latest.pdf",
)

FORBIDDEN_DOCS_LATEST_PDF_NAMES = (
    *RETIRED_FIXED_DAILY_PDF_NAMES,
    *REPO_ARTIFACT_DAILY_PDF_NAMES,
    *LEGACY_ROOT_DAILY_MARKET_PDF_NAMES,
    *AUXILIARY_INTERNAL_PDF_NAMES,
)

ALLOWED_DOCS_LATEST_ROOT_PDF_NAMES = {
    "daily_signal_performance_weekly_latest.pdf",
    "daily_signal_performance_monthly_latest.pdf",
    "tdcc_weekly_candidate_highlight_latest.pdf",
    "tdcc_weekly_candidate_full_latest.pdf",
}

PUBLIC_SURFACES = (
    DAILY_WORKFLOW,
    PUBLISHER,
    PACKET_BUILDER,
    RULES_BUILDER,
    OUTPUT_LATEST / "READ_ME_FIRST_DAILY_REPORT.txt",
    OUTPUT_LATEST / "READ_ME_FIRST_DAILY_REPORT_INDEX.txt",
    OUTPUT_LATEST / "chatgpt_daily_report_packet_latest.txt",
    DOCS_LATEST / "READ_ME_FIRST_DAILY_REPORT.txt",
    DOCS_LATEST / "READ_ME_FIRST_DAILY_REPORT_INDEX.txt",
    DOCS_LATEST / "chatgpt_daily_report_packet_latest.txt",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def current_main_price_date() -> str:
    if not DATA_FRESHNESS.exists():
        return ""
    with DATA_FRESHNESS.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        return ""
    return re.sub(r"[^0-9]", "", str(rows[0].get("main_price_date", "")))[:8]


def daily_market_published_pdf_paths(main_date: str) -> tuple[Path, ...]:
    date_text = re.sub(r"[^0-9]", "", str(main_date))[:8]
    if len(date_text) != 8:
        return ()
    published_dir = OUTPUT_LATEST / "published_reports" / "daily_market"
    return (
        published_dir / f"每日全市場候選股監測報告_精華版_{date_text}.pdf",
        published_dir / f"完整候選股清單_完整版_{date_text}.pdf",
    )


def validate_inventory_document(errors: list[str]) -> None:
    if not INVENTORY.exists():
        errors.append("missing PDF production inventory document: docs/pdf_production_inventory.md")
        return
    text = read_text(INVENTORY)
    required_markers = [
        "Official Producers",
        "Publisher Inventory",
        "Retired Daily PDF Paths",
        "Repo Artifact Daily PDFs",
        "Auxiliary Internal PDFs",
        "scripts/validate_pdf_production_inventory.py",
    ]
    for marker in required_markers:
        if marker not in text:
            errors.append(f"PDF production inventory missing marker: {marker}")
    for name, role, status in DAILY_MARKET_REPO_ARTIFACT_LIFECYCLE:
        for marker in (name, role, status):
            if marker not in text:
                errors.append(f"PDF production inventory missing daily market lifecycle marker: {marker}")
    for producer in PDF_PRODUCERS:
        if producer.purpose not in text:
            errors.append(f"PDF production inventory missing producer purpose: {producer.purpose}")
        for path in (*producer.producer_paths, *producer.validator_paths, *producer.publisher_paths):
            if path and path not in text:
                errors.append(f"PDF production inventory missing path: {path}")


def validate_paths_exist(errors: list[str]) -> None:
    for producer in PDF_PRODUCERS:
        for rel in (*producer.producer_paths, *producer.validator_paths, *producer.publisher_paths):
            path = ROOT / rel
            if not path.exists():
                errors.append(f"PDF production inventory path does not exist: {rel}")
    for rel in RETIRED_PRODUCER_PATHS:
        if (ROOT / rel).exists():
            errors.append(f"retired PDF producer/validator path still exists: {rel}")


def validate_output_latest(errors: list[str]) -> None:
    for name in RETIRED_FIXED_DAILY_PDF_NAMES:
        path = OUTPUT_LATEST / name
        if path.exists():
            errors.append(f"retired fixed daily PDF artifact still exists: {path.relative_to(ROOT).as_posix()}")
    for path in LEGACY_ROOT_DAILY_MARKET_PDF_PATHS:
        if path.exists():
            errors.append(f"legacy root daily market PDF still exists: {path.relative_to(ROOT).as_posix()}")
    for path in DAILY_MARKET_COMPATIBILITY_ALIAS_PATHS:
        if not path.exists():
            errors.append(f"daily market compatibility alias missing: {path.relative_to(ROOT).as_posix()}")
    main_date = current_main_price_date()
    if main_date:
        for path in daily_market_published_pdf_paths(main_date):
            if not path.exists():
                errors.append(f"published daily market PDF missing: {path.relative_to(ROOT).as_posix()}")


def validate_public_surface_text(errors: list[str]) -> None:
    for path in PUBLIC_SURFACES:
        if not path.exists():
            continue
        text = read_text(path)
        rel = path.relative_to(ROOT).as_posix()
        for name in RETIRED_FIXED_DAILY_PDF_NAMES:
            if name in text:
                errors.append(f"{rel} exposes retired fixed daily PDF name: {name}")
        for name in FORBIDDEN_DOCS_LATEST_PDF_NAMES:
            public_markers = (
                f"docs/latest/{name}",
                f"LeoChen0727.github.io/tdcc-weekly-report/latest/{name}",
            )
            if any(marker in text for marker in public_markers):
                errors.append(f"{rel} exposes forbidden docs/latest PDF path: {name}")


def validate_date_stamped_readmes(directory: Path, errors: list[str]) -> None:
    main_date = current_main_price_date()
    date_readme_re = re.compile(r"READ_ME_FIRST_DAILY_REPORT_(\d{8})\.txt$")
    for path in directory.glob("READ_ME_FIRST_DAILY_REPORT_*.txt"):
        match = date_readme_re.fullmatch(path.name)
        if not match:
            continue
        if main_date and match.group(1) != main_date:
            errors.append(
                "stale date-stamped daily README remains in latest directory: "
                f"{path.relative_to(ROOT).as_posix()}; current main_price_date={main_date}"
            )
        text = read_text(path)
        for name in FORBIDDEN_DOCS_LATEST_PDF_NAMES:
            if name in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} exposes forbidden PDF name: {name}")


def validate_docs_latest(errors: list[str]) -> None:
    if not DOCS_LATEST.exists():
        return

    for pdf in DOCS_LATEST.glob("*.pdf"):
        if pdf.name in FORBIDDEN_DOCS_LATEST_PDF_NAMES:
            errors.append(f"forbidden root PDF remains in docs/latest: {pdf.name}")
        elif pdf.name not in ALLOWED_DOCS_LATEST_ROOT_PDF_NAMES:
            errors.append(f"unclassified root PDF remains in docs/latest: {pdf.name}")

    validate_date_stamped_readmes(OUTPUT_LATEST, errors)
    validate_date_stamped_readmes(DOCS_LATEST, errors)


def validate_workflow_hooks(errors: list[str]) -> None:
    if not DAILY_WORKFLOW.exists():
        errors.append("missing Daily Full Pipeline workflow")
        return
    workflow = read_text(DAILY_WORKFLOW)
    required = "python scripts/validate_pdf_production_inventory.py"
    if workflow.count(required) < 2:
        errors.append("Daily Full Pipeline must run validate_pdf_production_inventory.py before and after publish")
    for name in FORBIDDEN_DOCS_LATEST_PDF_NAMES:
        if f"cp output/latest/{name} docs/latest/" in workflow:
            errors.append(f"Daily Full Pipeline copies forbidden PDF to docs/latest: {name}")
        if f"git add docs/latest/{name}" in workflow:
            errors.append(f"Daily Full Pipeline stages forbidden PDF in docs/latest: {name}")


def validate() -> list[str]:
    errors: list[str] = []
    validate_inventory_document(errors)
    validate_paths_exist(errors)
    validate_output_latest(errors)
    validate_public_surface_text(errors)
    validate_docs_latest(errors)
    validate_workflow_hooks(errors)
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PDF production inventory validation passed")
    for producer in PDF_PRODUCERS:
        print(f"validated_pdf_purpose={producer.purpose}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
