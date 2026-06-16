from __future__ import annotations

from pathlib import Path

from scripts import validate_pdf_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]


def test_pdf_production_inventory_validator_passes() -> None:
    assert inventory.main() == 0


def test_inventory_tracks_every_pdf_purpose() -> None:
    purposes = {producer.purpose for producer in inventory.PDF_PRODUCERS}

    assert purposes == {
        "ChatGPT-side daily",
        "Daily repo market source artifact",
        "TDCC weekly",
        "Market risk/background",
        "Warrant market auxiliary",
        "Daily signal performance reports",
        "Individual stock report",
    }


def test_docs_latest_root_pdfs_are_classified() -> None:
    docs_latest = ROOT / "docs" / "latest"
    for path in docs_latest.glob("*.pdf"):
        assert path.name in inventory.ALLOWED_DOCS_LATEST_ROOT_PDF_NAMES
        assert path.name not in inventory.FORBIDDEN_DOCS_LATEST_PDF_NAMES


def test_retired_daily_pdf_paths_are_not_in_public_surfaces() -> None:
    for path in inventory.PUBLIC_SURFACES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for name in inventory.RETIRED_FIXED_DAILY_PDF_NAMES:
            assert name not in text, f"{path.relative_to(ROOT).as_posix()} exposes {name}"


def test_daily_workflow_runs_inventory_validator_twice() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert workflow.count("python scripts/validate_pdf_production_inventory.py") >= 2
