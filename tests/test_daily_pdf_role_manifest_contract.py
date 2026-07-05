from __future__ import annotations

from pathlib import Path

from scripts import validate_daily_pdf_role_manifest_contract as validator


def test_daily_pdf_role_manifest_contract_passes_current_repo() -> None:
    assert validator.validate() == []


def test_daily_pdf_role_manifest_contract_rejects_title_token_role_mapping(
    tmp_path: Path,
    monkeypatch,
) -> None:
    replay_copy = tmp_path / "validate_chatgpt_daily_report_new_conversation_replay.py"
    replay_copy.write_text(
        validator.REPLAY_VALIDATOR.read_text(encoding="utf-8")
        + "\nPDF_ROLE_TITLE_TOKENS = {'mainstream_highlight': '主流股每日推薦精華'}\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(validator, "REPLAY_VALIDATOR", replay_copy)

    errors = validator.validate_replay_manifest_contract()

    assert any("PDF_ROLE_TITLE_TOKENS" in error for error in errors)


def test_daily_pdf_role_manifest_contract_rejects_highlight_title_maps(
    tmp_path: Path,
    monkeypatch,
) -> None:
    replay_copy = tmp_path / "validate_chatgpt_daily_report_new_conversation_replay.py"
    replay_copy.write_text(
        validator.REPLAY_VALIDATOR.read_text(encoding="utf-8")
        + "\nHIGHLIGHT_LAYOUT_TITLES = ('主流股每日推薦精華',)\ntitle_to_pages = {}\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(validator, "REPLAY_VALIDATOR", replay_copy)

    errors = validator.validate_replay_manifest_contract()

    assert any("HIGHLIGHT_LAYOUT_TITLES" in error for error in errors)
    assert any("title_to_pages" in error for error in errors)


def test_daily_pdf_role_manifest_contract_rejects_entrypoint_role_order_drift(
    tmp_path: Path,
    monkeypatch,
) -> None:
    entrypoint_copy = tmp_path / "run_chatgpt_daily_report_entrypoint.py"
    text = validator.ENTRYPOINT.read_text(encoding="utf-8")
    entrypoint_copy.write_text(
        text.replace(
            '"mainstream_highlight",\n    "mainstream_full",',
            '"mainstream_full",\n    "mainstream_highlight",',
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(validator, "ENTRYPOINT", entrypoint_copy)

    errors = validator.validate_entrypoint_manifest_contract()

    assert any("PDF_OUTPUT_ROLES must be exactly" in error for error in errors)


def test_daily_pdf_role_manifest_contract_rejects_unknown_regression_role(
    tmp_path: Path,
    monkeypatch,
) -> None:
    contract_copy = tmp_path / "daily_pdf_rendered_model_regression_contract.csv"
    contract_copy.write_text(
        "contract_id,active,report_date,pdf_role,page_scope,model_id,required_stock_ids,forbidden_stock_ids,reason\n"
        "bad,true,*,mainstream,first_page,volume_range_breakout,6226,,bad role\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(validator, "REGRESSION_CONTRACT", contract_copy)

    errors = validator.validate_rendered_regression_contract_roles()

    assert any("unknown pdf_role='mainstream'" in error for error in errors)


def test_daily_pdf_role_manifest_contract_rejects_missing_required_regression_contract(
    tmp_path: Path,
    monkeypatch,
) -> None:
    contract_copy = tmp_path / "daily_pdf_rendered_model_regression_contract.csv"
    contract_copy.write_text(
        "contract_id,active,report_date,pdf_role,page_scope,model_id,required_stock_ids,forbidden_stock_ids,required_text_tokens,forbidden_text_tokens,reason\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(validator, "REGRESSION_CONTRACT", contract_copy)

    errors = validator.validate_rendered_regression_contract_roles()

    assert any(
        "missing required active contract_id='price_pullback_23ema_mainstream_highlight_structure'" in error
        for error in errors
    )


def test_daily_pdf_role_manifest_contract_rejects_23ema_dynamic_required_stock_ids(
    tmp_path: Path,
    monkeypatch,
) -> None:
    contract_copy = tmp_path / "daily_pdf_rendered_model_regression_contract.csv"
    contract_copy.write_text(
        "contract_id,active,report_date,pdf_role,page_scope,model_id,required_stock_ids,forbidden_stock_ids,required_text_tokens,forbidden_text_tokens,reason\n"
        "bad,true,20260703,non_mainstream_highlight,all_pages,price_pullback_23ema,2610|1102,2347,23EMA,,,dynamic rows\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(validator, "REGRESSION_CONTRACT", contract_copy)

    errors = validator.validate_rendered_regression_contract_roles()

    assert any("price_pullback_23ema date-specific regression rows must not require dynamic" in error for error in errors)
