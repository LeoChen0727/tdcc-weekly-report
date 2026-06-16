from __future__ import annotations

from pathlib import Path

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
