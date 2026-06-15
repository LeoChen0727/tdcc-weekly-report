from __future__ import annotations

from pathlib import Path

from scripts import validate_chatgpt_side_pdf_contract as contract


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
GENERATOR = ROOT / "scripts" / "generate_daily_market_pdf.py"

PRODUCTION_RENDERERS = [
    "build_mainstream_daily_recommendation_highlight_pdf",
    "build_mainstream_full_candidate_list_pdf",
    "build_non_mainstream_daily_recommendation_highlight_pdf",
    "build_non_mainstream_full_candidate_list_pdf",
]


def _source(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _function_text(text: str, name: str) -> str:
    start = text.index(f"def {name}(")
    next_def = text.find("\ndef ", start + 1)
    end = len(text) if next_def == -1 else next_def
    return text[start:end]


def test_contract_validator_covers_six_formal_output_latest_pdfs() -> None:
    paths = {item.relative_path.as_posix() for item in contract.OFFICIAL_PDF_CONTRACTS}

    assert len(contract.OFFICIAL_PDF_CONTRACTS) == 6
    assert paths == {
        "output/latest/mainstream_daily_recommendation_highlight_latest.pdf",
        "output/latest/mainstream_full_candidate_list_latest.pdf",
        "output/latest/non_mainstream_daily_recommendation_highlight_latest.pdf",
        "output/latest/non_mainstream_full_candidate_list_latest.pdf",
        "output/latest/warrant_market_report_latest.pdf",
        "output/latest/market_risk_dashboard_latest.pdf",
    }
    assert all(path.startswith("output/latest/") for path in paths)
    assert all("preview" not in path.lower() for path in paths)


def test_contract_validator_has_highlight_full_boundary_rules() -> None:
    highlight_contracts = [item for item in contract.OFFICIAL_PDF_CONTRACTS if item.pdf_kind == "highlight"]
    full_contracts = [item for item in contract.OFFICIAL_PDF_CONTRACTS if item.pdf_kind == "full"]

    assert {item.report_family for item in highlight_contracts} == {"mainstream", "non_mainstream"}
    assert {item.report_family for item in full_contracts} == {"mainstream", "non_mainstream"}
    assert all(contract.REPRESENTATIVE_SECTION in item.required_all for item in highlight_contracts)
    assert all(contract.FULL_MODEL_LIST_SECTION in item.forbidden_all for item in highlight_contracts)
    assert all(contract.FULL_MODEL_LIST_SECTION in item.required_all for item in full_contracts)
    assert all(contract.REPRESENTATIVE_SECTION in item.forbidden_all for item in full_contracts)


def test_contract_validator_requires_new_and_consecutive_listing_sections() -> None:
    stock_contracts = [
        item
        for item in contract.OFFICIAL_PDF_CONTRACTS
        if item.report_family in {"mainstream", "non_mainstream"}
    ]

    assert len(stock_contracts) == 4
    for item in stock_contracts:
        assert contract.NEW_LISTED_TERMS in item.first_page_required_any
        assert contract.CONSECUTIVE_LISTED_TERMS in item.first_page_required_any
        assert (contract.SUMMARY_SECTION,) in item.first_page_required_any


def test_contract_validator_has_cross_report_pollution_titles() -> None:
    titles = contract.ALL_REPORT_TITLES

    assert len(titles) == 6
    assert len(set(titles)) == 6
    assert contract.WARRANT_TITLE in titles
    assert contract.MARKET_RISK_TITLE in titles


def test_daily_full_pipeline_runs_contract_validator_after_pdf_generation() -> None:
    workflow = _source(WORKFLOW)

    generator_call = "python scripts/generate_daily_market_pdf.py"
    legacy_validator_call = "python scripts/validate_daily_market_report.py"
    contract_validator_call = "python scripts/validate_chatgpt_side_pdf_contract.py"

    assert contract_validator_call in workflow
    assert workflow.index("python scripts/build_market_regime_dashboard.py") < workflow.index(contract_validator_call)
    assert workflow.index("python scripts/build_warrant_market_report.py") < workflow.index(contract_validator_call)
    assert workflow.index(generator_call) < workflow.index(contract_validator_call)
    assert workflow.index(legacy_validator_call) < workflow.index(contract_validator_call)


def test_production_model_line_pdfs_use_independent_renderer_entrypoints() -> None:
    text = _source(GENERATOR)
    main_text = _function_text(text, "main")

    for renderer in PRODUCTION_RENDERERS:
        assert f"def {renderer}(" in text
        assert f"{renderer}(" in main_text

    assert 'build_model_line_pdf("mainstream"' not in main_text
    assert 'build_model_line_pdf("non_mainstream"' not in main_text


def test_production_renderer_signatures_do_not_dispatch_by_line_or_full_flag() -> None:
    text = _source(GENERATOR)

    for renderer in PRODUCTION_RENDERERS:
        body = _function_text(text, renderer)
        signature = body.splitlines()[0]
        assert "report_line" not in signature
        assert "full:" not in signature
        assert "if report_line" not in body
        assert "if full" not in body
