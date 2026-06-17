from __future__ import annotations

from pathlib import Path

import ensure_report_aliases
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


def test_daily_workflow_cleans_stale_readmes_before_pdf_inventory_validation() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    alias_step = workflow.index("python ensure_report_aliases.py")
    contract_validation = workflow.index(
        "python scripts/validate_pdf_production_inventory.py",
        alias_step,
    )

    assert alias_step < contract_validation


def test_report_aliases_remove_stale_date_stamped_readmes(tmp_path: Path) -> None:
    current = tmp_path / "READ_ME_FIRST_DAILY_REPORT_20260617.txt"
    stale = tmp_path / "READ_ME_FIRST_DAILY_REPORT_20260616.txt"
    index = tmp_path / "READ_ME_FIRST_DAILY_REPORT_INDEX.txt"
    current.write_text("current", encoding="utf-8")
    stale.write_text("stale", encoding="utf-8")
    index.write_text("index", encoding="utf-8")

    ensure_report_aliases.remove_stale_date_stamped_readmes(tmp_path, "20260617")

    assert current.exists()
    assert not stale.exists()
    assert index.exists()


def test_report_aliases_do_not_fall_back_to_wall_clock_date() -> None:
    text = (ROOT / "ensure_report_aliases.py").read_text(encoding="utf-8")
    start = text.index("def detect_main_date(")
    end = text.index("\n\nDATE_STAMPED_README_RE", start)
    body = text[start:end]

    assert 'datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")' not in body
    assert "wall-clock date fallback is forbidden" in text
