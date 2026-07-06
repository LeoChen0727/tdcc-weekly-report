from __future__ import annotations

from pathlib import Path
import json

from scripts.validate_chatgpt_daily_report_new_conversation_replay import (
    EXPECTED_PDF_ROLES,
    HIGHLIGHT_FULL_TEXT_FORBIDDEN_TEXT,
    HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT,
    HIGHLIGHT_LAYOUT_ROLES,
    HIGHLIGHT_STOCK_MODEL_SECTION_TEXT,
    RENDERED_MODEL_REGRESSION_CONTRACT,
    RUNTIME_MANIFEST_NAME,
    pdf_paths_from_stdout,
    read_rendered_model_regression_contract,
    role_to_pdf_paths_from_manifest,
    validate_highlight_layout_texts,
    validate_rendered_model_regression_texts,
    validate_runtime_manifest,
    validate_pdf_path_contract,
    validate_source_gate_echo,
)


ROOT = Path(__file__).resolve().parents[1]


def pdf_name(date: str, role: str) -> str:
    return f"{date}_requested_repo{date}_{role}_current_rules.pdf"


def pdf_outputs(paths: list[Path]) -> list[dict[str, object]]:
    return [
        {"pdf_role": role, "pdf_index": index, "path": str(path.resolve())}
        for index, (role, path) in enumerate(zip(EXPECTED_PDF_ROLES, paths), start=1)
    ]


def runtime_manifest(paths: list[Path], state: dict, *, main_price_date: str = "20260617") -> dict:
    return {
        "manifest_type": "chatgpt_daily_report_runtime_manifest",
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "clean_source_commit_sha": "a" * 40,
        "main_price_date": main_price_date,
        "freshness_path": state["freshness_path"],
        "readme_path": state["readme_path"],
        "packet_path": state["packet_path"],
        "pdf_count": len(paths),
        "output_dir": str(paths[0].parent),
        "pdf_paths": [str(path.resolve()) for path in paths],
        "pdf_outputs": pdf_outputs(paths),
    }


def test_replay_stdout_pdf_parser_deduplicates_entrypoint_output(tmp_path: Path) -> None:
    paths = [tmp_path / pdf_name("20260617", role) for role in EXPECTED_PDF_ROLES]
    stdout = "\n".join(
        [
            "official daily report source gate passed: source_ref=origin/main",
            *(str(path) for path in paths),
            "official ChatGPT-side daily PDF generation completed",
            *(str(path) for path in paths),
        ]
    )

    parsed = pdf_paths_from_stdout(stdout)

    assert parsed == [path.resolve() for path in paths]


def test_replay_pdf_path_contract_requires_exact_six_current_date_pdfs(tmp_path: Path) -> None:
    paths = [tmp_path / pdf_name("20260617", role) for role in EXPECTED_PDF_ROLES]

    errors = validate_pdf_path_contract(paths, tmp_path, "20260617")

    assert errors == []


def test_replay_pdf_path_contract_rejects_stale_or_wrong_date_pdfs(tmp_path: Path) -> None:
    paths = [
        tmp_path / pdf_name("20260617", EXPECTED_PDF_ROLES[0]),
        tmp_path / pdf_name("20260617", EXPECTED_PDF_ROLES[1]),
        tmp_path / pdf_name("20260617", EXPECTED_PDF_ROLES[2]),
        tmp_path / pdf_name("20260617", EXPECTED_PDF_ROLES[3]),
        tmp_path / pdf_name("20260617", EXPECTED_PDF_ROLES[4]),
        tmp_path / pdf_name("20260612", EXPECTED_PDF_ROLES[5]),
    ]

    errors = validate_pdf_path_contract(paths, tmp_path, "20260617")

    assert any("main_price_date=20260617" in error for error in errors)
    assert any("20260612_requested_repo20260612" in error for error in errors)


def test_replay_source_gate_echo_must_include_origin_main_state() -> None:
    state = {
        "source_commit_sha": "a" * 40,
        "main_price_date": "20260617",
    }
    stdout = (
        "official daily report source gate passed: "
        "source_ref=origin/main "
        f"source_commit_sha={state['source_commit_sha']} "
        "main_price_date=20260617 "
        "report_ready=True "
        "warrant_ready=True "
        "daily_pdf_ready=True\n"
        "official ChatGPT-side daily PDF generation completed\n"
    )

    errors = validate_source_gate_echo(stdout, state, "origin/main")

    assert errors == []


def test_replay_runtime_manifest_must_match_source_and_pdf_paths(tmp_path: Path) -> None:
    paths = [tmp_path / pdf_name("20260617", role) for role in EXPECTED_PDF_ROLES]
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "main_price_date": "20260617",
        "freshness_path": "origin/main:output/latest/data_freshness_latest.csv",
        "readme_path": "origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "packet_path": "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt",
    }
    (tmp_path / RUNTIME_MANIFEST_NAME).write_text(
        json.dumps(runtime_manifest(paths, state)),
        encoding="utf-8",
    )

    errors = validate_runtime_manifest(paths, tmp_path, state)

    assert errors == []


def test_replay_runtime_manifest_rejects_wrong_date(tmp_path: Path) -> None:
    paths = [tmp_path / pdf_name("20260617", role) for role in EXPECTED_PDF_ROLES]
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "main_price_date": "20260617",
        "freshness_path": "origin/main:output/latest/data_freshness_latest.csv",
        "readme_path": "origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "packet_path": "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt",
    }
    (tmp_path / RUNTIME_MANIFEST_NAME).write_text(
        json.dumps(runtime_manifest(paths, state, main_price_date="20260612")),
        encoding="utf-8",
    )

    errors = validate_runtime_manifest(paths, tmp_path, state)

    assert any("main_price_date" in error for error in errors)


def test_replay_runtime_manifest_requires_pdf_outputs(tmp_path: Path) -> None:
    paths = [tmp_path / pdf_name("20260617", role) for role in EXPECTED_PDF_ROLES]
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "main_price_date": "20260617",
        "freshness_path": "origin/main:output/latest/data_freshness_latest.csv",
        "readme_path": "origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "packet_path": "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt",
    }
    manifest = runtime_manifest(paths, state)
    manifest.pop("pdf_outputs")
    (tmp_path / RUNTIME_MANIFEST_NAME).write_text(json.dumps(manifest), encoding="utf-8")

    errors = validate_runtime_manifest(paths, tmp_path, state)

    assert any("pdf_outputs must be a list" in error for error in errors)


def test_replay_runtime_manifest_role_mapping_uses_manifest_not_filename_tokens(tmp_path: Path) -> None:
    paths = [tmp_path / pdf_name("20260617", role) for role in EXPECTED_PDF_ROLES]
    manifest = {
        "pdf_outputs": [
            {"pdf_role": role, "pdf_index": index, "path": str(path.resolve())}
            for index, (role, path) in enumerate(zip(EXPECTED_PDF_ROLES, paths), start=1)
        ]
    }

    role_to_path, errors = role_to_pdf_paths_from_manifest(manifest, paths)

    assert errors == []
    assert role_to_path["mainstream_highlight"] == paths[0].resolve()
    assert role_to_path["non_mainstream_highlight"] == paths[2].resolve()


def test_replay_highlight_layout_contract_accepts_legacy_volume_first() -> None:
    required_text = "\n".join(HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT)
    pages = {
        "mainstream_highlight": [f"mainstream highlight\n{required_text}", "other content"],
        "non_mainstream_highlight": [f"non-mainstream highlight\n{required_text}", "other content"],
    }

    assert validate_highlight_layout_texts(pages) == []

def test_replay_highlight_layout_roles_are_machine_readable() -> None:
    assert HIGHLIGHT_LAYOUT_ROLES == ("mainstream_highlight", "non_mainstream_highlight")

def test_replay_highlight_layout_contract_rejects_reordered_first_page() -> None:
    required_text = "\n".join(HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT)
    pages = {
        "mainstream_highlight": [HIGHLIGHT_STOCK_MODEL_SECTION_TEXT, required_text],
        "non_mainstream_highlight": [f"non-mainstream highlight\n{required_text}"],
    }

    errors = validate_highlight_layout_texts(pages)

    assert any("first page missing required layout text" in error for error in errors)
    assert any("must not start with stock-model tables" in error for error in errors)

def test_replay_highlight_layout_contract_rejects_pending_operation_text() -> None:
    required_text = "\n".join(HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT)
    forbidden_text = HIGHLIGHT_FULL_TEXT_FORBIDDEN_TEXT[0]
    pages = {
        "mainstream_highlight": [f"mainstream highlight\n{required_text}\n{forbidden_text}"],
        "non_mainstream_highlight": [f"non-mainstream highlight\n{required_text}"],
    }

    errors = validate_highlight_layout_texts(pages)

    assert any(f"forbidden operation-layer text: {forbidden_text}" in error for error in errors)

def test_rendered_model_regression_contract_accepts_as_published_volume_rows() -> None:
    rows = [
        {
            "contract_id": "volume_range_breakout_mainstream_highlight_20260703",
            "active": "True",
            "report_date": "20260703",
            "pdf_role": "mainstream_highlight",
            "page_scope": "first_page",
            "model_id": "volume_range_breakout",
            "required_stock_ids": "6226|2483|6742",
            "forbidden_stock_ids": "3055|1515|2342",
        }
    ]
    role_to_pages = {
        "mainstream_highlight": [
            "2026/7/3 main daily digest\nvolume_range_breakout\n6226 光鼎\n2483 百容\n6742 澤米"
        ]
    }

    assert validate_rendered_model_regression_texts(role_to_pages, "20260703", rows) == []


def test_rendered_model_regression_contract_checks_required_and_forbidden_text_tokens() -> None:
    rows = [
        {
            "contract_id": "price_pullback_23ema_highlight_structure",
            "active": "True",
            "report_date": "*",
            "pdf_role": "mainstream_highlight",
            "page_scope": "all_pages",
            "model_id": "price_pullback_23ema",
            "required_text_tokens": "23EMA回檔模型|MA20/EMA23|66.03%|5.60%|28.36%|+2.90%",
            "forbidden_text_tokens": "盤中過前高收盤賣",
        }
    ]
    role_to_pages = {
        "mainstream_highlight": [
            "第1頁",
            "23EMA回檔模型\n停損：收盤連續 4 天低於 MA20/EMA23 較低者的 4%\n"
            "基礎 66.03% / 5.60% / 28.36% / +2.90%",
        ]
    }

    assert validate_rendered_model_regression_texts(role_to_pages, "20260706", rows) == []

    role_to_pages["mainstream_highlight"][1] = "23EMA回檔模型\n盤中過前高收盤賣\n基礎 66.03%"
    errors = validate_rendered_model_regression_texts(role_to_pages, "20260706", rows)

    assert any("required text token='MA20/EMA23' missing" in error for error in errors)
    assert any("forbidden text token='盤中過前高收盤賣' appeared" in error for error in errors)


def test_rendered_model_regression_contract_rejects_volume_snapshot_drift() -> None:
    rows = [
        {
            "contract_id": "volume_range_breakout_mainstream_highlight_20260703",
            "active": "True",
            "report_date": "20260703",
            "pdf_role": "mainstream_highlight",
            "page_scope": "first_page",
            "model_id": "volume_range_breakout",
            "required_stock_ids": "6226|2483|6742",
            "forbidden_stock_ids": "3055|1515|2342",
        }
    ]
    role_to_pages = {
        "mainstream_highlight": [
            "2026/7/3 main daily digest\nvolume_range_breakout\n3055 蔚華科\n1515 力山\n2342 茂矽"
        ]
    }

    errors = validate_rendered_model_regression_texts(role_to_pages, "20260703", rows)

    assert any("required stock_id=6226 missing" in error for error in errors)
    assert any("forbidden stock_id=3055 appeared" in error for error in errors)
    assert any("forbidden stock_id=2342 appeared" in error for error in errors)


def test_rendered_model_regression_contract_records_20260703_volume_guard() -> None:
    rows = read_rendered_model_regression_contract(RENDERED_MODEL_REGRESSION_CONTRACT)
    row_by_id = {row["contract_id"]: row for row in rows}

    guard = row_by_id["volume_range_breakout_mainstream_highlight_20260703"]

    assert guard["active"] == "True"
    assert guard["report_date"] == "20260703"
    assert guard["pdf_role"] == "mainstream_highlight"
    assert guard["page_scope"] == "first_page"
    assert guard["model_id"] == "volume_range_breakout"
    assert guard["required_stock_ids"] == "6226|2483|6742"
    assert guard["forbidden_stock_ids"] == "3055|1515|2342"
    assert "放量攻擊模型" in guard["required_text_tokens"]


def test_rendered_model_regression_contract_records_formal_operation_models() -> None:
    rows = read_rendered_model_regression_contract(RENDERED_MODEL_REGRESSION_CONTRACT)
    row_by_id = {row["contract_id"]: row for row in rows}

    required_contracts = {
        "volume_range_breakout_mainstream_highlight_structure",
        "volume_range_breakout_non_mainstream_highlight_empty_20260703",
        "volume_range_breakout_mainstream_highlight_confirmed_empty_table_20260703",
        "volume_range_breakout_mainstream_highlight_active_table_20260703",
        "volume_range_breakout_non_mainstream_highlight_empty_tables_20260703",
        "w_bottom_right_side_mainstream_highlight_structure",
        "w_bottom_right_side_non_mainstream_highlight_structure",
        "w_bottom_right_side_mainstream_highlight_confirmed_table_20260703",
        "w_bottom_right_side_mainstream_highlight_active_table_20260703",
        "w_bottom_right_side_non_mainstream_highlight_confirmed_table_20260703",
        "w_bottom_right_side_non_mainstream_highlight_active_table_20260703",
        "neckline_volume_breakout_confirmation_mainstream_highlight_structure",
        "neckline_volume_breakout_confirmation_non_mainstream_highlight_structure",
        "neckline_volume_breakout_confirmation_mainstream_highlight_confirmed_empty_table_20260703",
        "neckline_volume_breakout_confirmation_mainstream_highlight_active_empty_table_20260703",
        "neckline_volume_breakout_confirmation_non_mainstream_highlight_confirmed_empty_table_20260703",
        "neckline_volume_breakout_confirmation_non_mainstream_highlight_active_empty_table_20260703",
        "price_pullback_23ema_mainstream_highlight_structure",
        "price_pullback_23ema_non_mainstream_highlight_structure",
        "price_pullback_23ema_mainstream_highlight_20260703",
        "price_pullback_23ema_non_mainstream_highlight_20260703",
        "price_pullback_23ema_mainstream_highlight_confirmed_table_20260703",
        "price_pullback_23ema_mainstream_highlight_active_empty_table_20260703",
        "price_pullback_23ema_non_mainstream_highlight_confirmed_table_20260703",
        "price_pullback_23ema_non_mainstream_highlight_active_empty_table_20260703",
    }

    assert required_contracts <= set(row_by_id)
    assert row_by_id["price_pullback_23ema_mainstream_highlight_structure"]["report_date"] == "*"
    assert row_by_id["price_pullback_23ema_mainstream_highlight_20260703"]["required_stock_ids"] == ""
    assert row_by_id["price_pullback_23ema_non_mainstream_highlight_20260703"]["required_stock_ids"] == ""
    assert row_by_id["price_pullback_23ema_mainstream_highlight_20260703"]["forbidden_stock_ids"]
    assert row_by_id["price_pullback_23ema_non_mainstream_highlight_20260703"]["forbidden_stock_ids"]
    assert row_by_id["volume_range_breakout_mainstream_highlight_confirmed_empty_table_20260703"][
        "required_text_tokens"
    ]
    assert row_by_id["w_bottom_right_side_mainstream_highlight_active_table_20260703"]["required_stock_ids"]
    assert row_by_id[
        "neckline_volume_breakout_confirmation_mainstream_highlight_active_empty_table_20260703"
    ]["required_text_tokens"]
    assert (
        row_by_id["price_pullback_23ema_mainstream_highlight_confirmed_table_20260703"]["required_stock_ids"]
        == ""
    )
    assert "23EMA回檔模型" in row_by_id["price_pullback_23ema_mainstream_highlight_structure"][
        "required_text_tokens"
    ]
    price_pullback_tokens = row_by_id["price_pullback_23ema_mainstream_highlight_structure"][
        "required_text_tokens"
    ]
    assert "買入：本表股票為23EMA回檔模型通過候選，隔日開盤買入。" in price_pullback_tokens
    assert "賣出：收盤突破訊號日前20日高點後，隔日開盤賣出。" in price_pullback_tokens
    assert "停損：收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。" in price_pullback_tokens
    assert "基礎模型績效：勝率66.03%" in price_pullback_tokens
    assert "技術強勢組合績效：勝率75.54%" in price_pullback_tokens
    assert "勝：D+20內先觸發收盤突破訊號日前20日高點" in price_pullback_tokens
    assert "和：D+20內沒有賣出或停損" in price_pullback_tokens
    assert "敗：停損先觸發" in price_pullback_tokens
    price_pullback_forbidden = row_by_id["price_pullback_23ema_mainstream_highlight_structure"][
        "forbidden_text_tokens"
    ]
    assert "下一個交易日開盤買入" in price_pullback_forbidden
    assert "下一個交易日開盤賣出" in price_pullback_forbidden
    assert "下一個交易日開盤停損" in price_pullback_forbidden
    assert "W底頸線帶量突破確認模型" in row_by_id[
        "neckline_volume_breakout_confirmation_mainstream_highlight_structure"
    ]["required_text_tokens"]


def test_daily_workflow_runs_new_conversation_replay_gate() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8",
        errors="replace",
    )

    assert "Replay ChatGPT-side daily PDF new conversation" in workflow
    assert "python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in workflow
    assert "timeout-minutes: 20" in workflow
    assert "timeout 20m python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in workflow
    assert "PDF replay output_dir=chatgpt_side_outputs_new_conversation_replay" in workflow
    assert "--output-dir chatgpt_side_outputs_new_conversation_replay" in workflow
