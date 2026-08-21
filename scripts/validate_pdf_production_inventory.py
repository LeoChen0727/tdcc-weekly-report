from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "docs" / "pdf_production_inventory.md"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
PDF_PREBUILD_COMMAND = "python scripts/validate_pdf_production_inventory.py --phase prebuild"
PDF_RUNTIME_COMMAND = "python scripts/validate_pdf_production_inventory.py --phase runtime"
PUBLISHER = ROOT / "publish_chatgpt_report_readme_and_check.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
DAILY_MARKET_ARTIFACT_BUILDER = ROOT / "build_daily_market_report_artifacts.py"
ALIAS_ENSURER = ROOT / "ensure_report_aliases.py"
RULES_BUILDER = ROOT / "build_chatgpt_daily_report_rules.py"
DOCS_LATEST = ROOT / "docs" / "latest"
OUTPUT_LATEST = ROOT / "output" / "latest"
HISTORY_REPORTS = ROOT / "output" / "history" / "reports"
DATA_FRESHNESS = OUTPUT_LATEST / "data_freshness_latest.csv"
REPORT_MANIFEST_JSON = OUTPUT_LATEST / "report_manifest_latest.json"
REPORT_MANIFEST_MD = OUTPUT_LATEST / "report_manifest_latest.md"


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
            "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
            "scripts/validate_daily_pdf_completion_hard_gate.py",
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
    (
        "output/history/reports/YYYYMMDD_daily_market_summary.pdf",
        "canonical_history_pdf",
        "canonical_history_only",
    ),
    (
        "output/history/reports/YYYYMMDD_daily_market_full.pdf",
        "canonical_history_pdf",
        "canonical_history_only",
    ),
)

LEGACY_HISTORY_REFERENCE_FRAGMENTS = (
    "_每日全市場候選股監測報告_精華版.",
    "_完整候選股清單_完整版.",
    "_完整候選股清單_完整版表格.",
)

HISTORY_PRODUCER_PATHS = (
    DAILY_MARKET_ARTIFACT_BUILDER,
    PACKET_BUILDER,
    ALIAS_ENSURER,
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

STATIC_PUBLIC_SURFACES = (
    DAILY_WORKFLOW,
    PUBLISHER,
    PACKET_BUILDER,
    RULES_BUILDER,
)

RUNTIME_PUBLIC_SURFACES = (
    OUTPUT_LATEST / "READ_ME_FIRST_DAILY_REPORT.txt",
    OUTPUT_LATEST / "READ_ME_FIRST_DAILY_REPORT_INDEX.txt",
    OUTPUT_LATEST / "chatgpt_daily_report_packet_latest.txt",
    DOCS_LATEST / "READ_ME_FIRST_DAILY_REPORT.txt",
    DOCS_LATEST / "READ_ME_FIRST_DAILY_REPORT_INDEX.txt",
    DOCS_LATEST / "chatgpt_daily_report_packet_latest.txt",
)

PUBLIC_SURFACES = (*STATIC_PUBLIC_SURFACES, *RUNTIME_PUBLIC_SURFACES)

VALIDATION_PHASE_FULL = "full"
VALIDATION_PHASE_PREBUILD = "prebuild"
VALIDATION_PHASE_RUNTIME = "runtime"
VALIDATION_PHASES = (
    VALIDATION_PHASE_FULL,
    VALIDATION_PHASE_PREBUILD,
    VALIDATION_PHASE_RUNTIME,
)
RUNTIME_VALIDATED_SURFACES = (
    "output_latest",
    "report_manifest_history",
    "runtime_public_surfaces",
    "docs_latest",
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


def daily_market_canonical_history_paths(main_date: str) -> dict[str, Path]:
    date_text = re.sub(r"[^0-9]", "", str(main_date))[:8]
    if len(date_text) != 8:
        return {}
    return {
        "history_summary_md": HISTORY_REPORTS / f"{date_text}_daily_market_summary.md",
        "history_summary_pdf": HISTORY_REPORTS / f"{date_text}_daily_market_summary.pdf",
        "history_full_md": HISTORY_REPORTS / f"{date_text}_daily_market_full.md",
        "history_full_pdf": HISTORY_REPORTS / f"{date_text}_daily_market_full.pdf",
    }


def contains_legacy_history_reference(text: str) -> bool:
    normalized = text.replace("\\", "/")
    if "output/history/reports/" not in normalized:
        return False
    return any(fragment in normalized for fragment in LEGACY_HISTORY_REFERENCE_FRAGMENTS)


def validate_daily_history_producer_contract(errors: list[str]) -> None:
    forbidden_literals = (
        "{main_date}_每日全市場候選股監測報告_精華版.md",
        "{main_date}_每日全市場候選股監測報告_精華版.pdf",
        "{main_date}_完整候選股清單_完整版.md",
        "{main_date}_完整候選股清單_完整版表格.pdf",
    )
    required_literals = (
        "{main_date}_daily_market_summary.pdf",
        "{main_date}_daily_market_full.pdf",
    )
    for path in HISTORY_PRODUCER_PATHS:
        if not path.exists():
            errors.append(f"missing daily history producer: {path.relative_to(ROOT).as_posix()}")
            continue
        source = read_text(path)
        rel = path.relative_to(ROOT).as_posix()
        for literal in forbidden_literals:
            if literal in source:
                errors.append(f"{rel} still generates retired Chinese history alias: {literal}")
        for literal in required_literals:
            if literal not in source:
                errors.append(f"{rel} missing canonical history artifact literal: {literal}")

    if ALIAS_ENSURER.exists():
        alias_source = read_text(ALIAS_ENSURER)
        for literal in (
            "published_summary_pdf(main_date)",
            "published_full_pdf(main_date)",
            "canonical_daily_market_history_only",
        ):
            if literal not in alias_source:
                errors.append(f"ensure_report_aliases.py missing history contract literal: {literal}")
        for literal in ("CHINESE_SUMMARY_PDF", "CHINESE_FULL_PDF"):
            if literal in alias_source:
                errors.append(f"ensure_report_aliases.py must not restore retired root PDF source: {literal}")


def validate_report_manifest_history_contract(errors: list[str]) -> None:
    if not REPORT_MANIFEST_JSON.exists():
        return

    try:
        manifest = json.loads(REPORT_MANIFEST_JSON.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"report manifest JSON is invalid: {exc}")
        return

    manifest_text = json.dumps(manifest, ensure_ascii=False)
    if contains_legacy_history_reference(manifest_text):
        errors.append("report_manifest_latest.json references retired Chinese history alias")

    main_date = current_main_price_date() or str(manifest.get("main_price_date", ""))
    expected = daily_market_canonical_history_paths(main_date)
    if not expected:
        errors.append("report manifest canonical history validation requires an 8-digit main_price_date")
        return

    if manifest.get("history_path_contract") != "canonical_daily_market_history_only":
        errors.append("report manifest missing canonical history_path_contract")

    alias_fields = {
        "history_summary_md": "history_summary_alias_md",
        "history_summary_pdf": "history_summary_alias_pdf",
        "history_full_md": "history_full_alias_md",
        "history_full_pdf": "history_full_alias_pdf",
    }
    for field, path in expected.items():
        expected_rel = path.relative_to(ROOT).as_posix()
        if str(manifest.get(field, "")).replace("\\", "/") != expected_rel:
            errors.append(f"report manifest {field} must equal canonical path: {expected_rel}")
        alias_field = alias_fields[field]
        if str(manifest.get(alias_field, "")).replace("\\", "/") != expected_rel:
            errors.append(f"report manifest {alias_field} must resolve to canonical path: {expected_rel}")

    raw_field_paths = {
        "history_summary_alias_md_raw_url": expected["history_summary_md"],
        "history_summary_alias_pdf_raw_url": expected["history_summary_pdf"],
        "history_full_alias_md_raw_url": expected["history_full_md"],
        "history_full_alias_pdf_raw_url": expected["history_full_pdf"],
        "summary_md_raw_url": expected["history_summary_md"],
        "summary_pdf_raw_url": expected["history_summary_pdf"],
        "full_md_raw_url": expected["history_full_md"],
        "full_pdf_raw_url": expected["history_full_pdf"],
    }
    for field, path in raw_field_paths.items():
        expected_rel = path.relative_to(ROOT).as_posix()
        value = str(manifest.get(field, "")).replace("\\", "/")
        if not value.endswith(expected_rel):
            errors.append(f"report manifest {field} must target canonical path: {expected_rel}")

    for field in ("history_summary_pdf", "history_full_pdf"):
        path = expected[field]
        if not path.exists():
            errors.append(f"canonical daily history PDF missing: {path.relative_to(ROOT).as_posix()}")

    if REPORT_MANIFEST_MD.exists():
        markdown = read_text(REPORT_MANIFEST_MD)
        if contains_legacy_history_reference(markdown):
            errors.append("report_manifest_latest.md references retired Chinese history alias")
        for path in expected.values():
            expected_rel = path.relative_to(ROOT).as_posix()
            if expected_rel not in markdown:
                errors.append(f"report_manifest_latest.md missing canonical history path: {expected_rel}")


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


def validate_public_surface_text(errors: list[str], paths: tuple[Path, ...] = PUBLIC_SURFACES) -> None:
    for path in paths:
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
    commands = [line.strip() for line in workflow.splitlines()]
    full_command = "python scripts/validate_pdf_production_inventory.py"
    if commands.count(PDF_PREBUILD_COMMAND) != 0:
        errors.append("Daily Full Pipeline must not run static PDF prebuild validation")
    if commands.count(full_command) != 0:
        errors.append("Daily Full Pipeline must not run mixed full PDF inventory validation")
    if commands.count(PDF_RUNTIME_COMMAND) != 2:
        errors.append(
            "Daily Full Pipeline must run exactly two runtime-only PDF inventory validations"
        )
    try:
        install_index = workflow.index("- name: Install dependencies")
        build_index = workflow.index("- name: Build daily market report artifacts", install_index)
        aliases_index = workflow.index("- name: Ensure English report aliases", build_index)
        post_build_runtime_index = workflow.index(PDF_RUNTIME_COMMAND, aliases_index)
        publish_index = workflow.index(
            "- name: Publish readme and multi-entry URL check",
            post_build_runtime_index,
        )
        post_publish_runtime_index = workflow.index(PDF_RUNTIME_COMMAND, publish_index)
        if not (
            install_index
            < build_index
            < aliases_index
            < post_build_runtime_index
            < publish_index
            < post_publish_runtime_index
        ):
            raise ValueError("invalid runtime PDF inventory ordering")
    except ValueError:
        errors.append(
            "Daily Full Pipeline must run runtime-only PDF inventory validation "
            "after both report build and publish"
        )
    deletion_aware_readme_staging = (
        'git add -A -- "output/latest/READ_ME_FIRST_DAILY_REPORT*.txt"',
        'git add -A -- "docs/latest/READ_ME_FIRST_DAILY_REPORT*.txt"',
    )
    for command in deletion_aware_readme_staging:
        if command not in workflow:
            errors.append(
                "Daily Full Pipeline must stage date-stamped daily README deletions with a quoted pathspec: "
                f"{command}"
            )
    for name in FORBIDDEN_DOCS_LATEST_PDF_NAMES:
        if f"cp output/latest/{name} docs/latest/" in workflow:
            errors.append(f"Daily Full Pipeline copies forbidden PDF to docs/latest: {name}")
        if f"git add docs/latest/{name}" in workflow:
            errors.append(f"Daily Full Pipeline stages forbidden PDF in docs/latest: {name}")


def validate(phase: str = VALIDATION_PHASE_FULL) -> list[str]:
    if phase not in VALIDATION_PHASES:
        raise ValueError(f"unsupported PDF production inventory validation phase: {phase}")

    errors: list[str] = []
    if phase != VALIDATION_PHASE_RUNTIME:
        validate_inventory_document(errors)
        validate_paths_exist(errors)
        validate_daily_history_producer_contract(errors)
        validate_public_surface_text(errors, STATIC_PUBLIC_SURFACES)
        validate_workflow_hooks(errors)
    if phase != VALIDATION_PHASE_PREBUILD:
        validate_output_latest(errors)
        validate_report_manifest_history_contract(errors)
        validate_public_surface_text(errors, RUNTIME_PUBLIC_SURFACES)
        validate_docs_latest(errors)
    return errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the PDF production inventory contract.")
    parser.add_argument(
        "--phase",
        choices=VALIDATION_PHASES,
        default=VALIDATION_PHASE_FULL,
        help=(
            "prebuild checks static contracts only; runtime checks current artifacts only; "
            "full checks both"
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args([] if argv is None else argv)
    errors = validate(args.phase)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PDF production inventory validation passed")
    print(f"validation_phase={args.phase}")
    if args.phase != VALIDATION_PHASE_RUNTIME:
        for producer in PDF_PRODUCERS:
            print(f"validated_pdf_purpose={producer.purpose}")
    if args.phase != VALIDATION_PHASE_PREBUILD:
        for surface in RUNTIME_VALIDATED_SURFACES:
            print(f"validated_runtime_surface={surface}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
