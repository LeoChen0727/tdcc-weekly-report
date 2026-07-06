from __future__ import annotations

from pathlib import Path

from scripts import validate_daily_pdf_completion_hard_gate as validator


ROOT = Path(__file__).resolve().parents[1]


def test_daily_pdf_completion_hard_gate_passes_current_repo() -> None:
    assert validator.validate() == []


def test_completion_gate_rejects_missing_runtime_manifest(tmp_path: Path) -> None:
    output_dir = tmp_path / "chatgpt_side_outputs"
    output_dir.mkdir()

    errors = validator.validate_output_dir(output_dir)

    assert any("runtime manifest" in error for error in errors)


def test_completion_gate_requires_operation_model_regression_contract() -> None:
    assert validator.validate_regression_contract() == []


def test_completion_gate_requires_operation_table_title_for_active_rows() -> None:
    rows = {
        "price_pullback_23ema": [
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "23EMA回檔模型",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "report_line": "both",
                "stock_display": "本日無股票推薦",
            },
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "23EMA回檔模型",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "data",
                "display_order": "1",
                "report_line": "mainstream",
                "operation_status": "active_operation",
                "buy_rank_eligible": "False",
                "stock_id": "1785",
                "stock_display": "1785 光洋科",
            },
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "23EMA回檔模型",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "report_line": "non_mainstream",
                "stock_display": "目前無操作中追蹤列",
            },
        ]
    }
    role_to_text = {
        "mainstream_highlight": validator.compact_text(
            "23EMA回檔模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
            "23EMA回檔模型 操作中 1785"
        ),
        "non_mainstream_highlight": validator.compact_text(
            "23EMA回檔模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
            "23EMA回檔模型 - 操作中 目前無操作中追蹤列"
        ),
    }

    errors = validator.validate_operation_adapter_pdf_text(
        role_to_text,
        rows,
        required_model_ids=["price_pullback_23ema"],
    )

    assert any(
        "missing operation table title for price_pullback_23ema/active_operation" in error
        for error in errors
    )


def test_completion_gate_accepts_operation_empty_state_tables() -> None:
    rows = {
        "neckline_volume_breakout_confirmation": [
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "report_line": "both",
                "stock_display": "本日無股票推薦",
            },
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "report_line": "both",
                "stock_display": "目前無操作中追蹤列",
            },
        ]
    }
    text = validator.compact_text(
        "W底頸線帶量突破確認模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
        "W底頸線帶量突破確認模型 - 操作中 目前無操作中追蹤列"
    )

    errors = validator.validate_operation_adapter_pdf_text(
        {
            "mainstream_highlight": text,
            "non_mainstream_highlight": text,
        },
        rows,
        required_model_ids=["neckline_volume_breakout_confirmation"],
    )

    assert errors == []


def test_completion_gate_requires_rendered_stock_ids_for_operation_rows() -> None:
    rows = {
        "price_pullback_23ema": [
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "23EMA回檔模型",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "report_line": "both",
                "stock_display": "本日無股票推薦",
            },
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "23EMA回檔模型",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "data",
                "display_order": "1",
                "report_line": "mainstream",
                "operation_status": "active_operation",
                "buy_rank_eligible": "False",
                "stock_id": "1785",
                "stock_display": "1785 光洋科",
            },
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "23EMA回檔模型",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "report_line": "non_mainstream",
                "stock_display": "目前無操作中追蹤列",
            },
        ]
    }
    role_to_text = {
        "mainstream_highlight": validator.compact_text(
            "23EMA回檔模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
            "23EMA回檔模型 - 操作中"
        ),
        "non_mainstream_highlight": validator.compact_text(
            "23EMA回檔模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
            "23EMA回檔模型 - 操作中 目前無操作中追蹤列"
        ),
    }

    errors = validator.validate_operation_adapter_pdf_text(
        role_to_text,
        rows,
        required_model_ids=["price_pullback_23ema"],
    )

    assert any("missing rendered stock_id=1785" in error for error in errors)


def test_completion_gate_uses_report_line_membership_for_line_agnostic_rows() -> None:
    rows = {
        "volume_range_breakout": [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "report_line": "both",
                "stock_display": "本日無股票推薦",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "data",
                "display_order": "1",
                "operation_status": "active_operation",
                "buy_rank_eligible": "False",
                "stock_id": "3055",
                "stock_display": "3055 蔚華科",
            },
        ]
    }
    role_to_text = {
        "mainstream_highlight": validator.compact_text(
            "放量攻擊模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
            "放量攻擊模型 - 操作中 3055"
        ),
        "non_mainstream_highlight": validator.compact_text(
            "放量攻擊模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
            "放量攻擊模型 - 操作中 目前無操作中追蹤列"
        ),
    }

    errors = validator.validate_operation_adapter_pdf_text(
        role_to_text,
        rows,
        required_model_ids=["volume_range_breakout"],
        stock_report_lines={"3055": {"mainstream"}},
    )

    assert errors == []


def test_completion_gate_rejects_pr_workflow_without_post_replay_gate(
    tmp_path: Path, monkeypatch
) -> None:
    full_workflow = tmp_path / "daily_full_pipeline.yml"
    pr_workflow = tmp_path / "daily_model_maintenance_pr_validation.yml"
    gate_file = tmp_path / "validate_daily_pdf_completion_hard_gate.py"
    replay_file = tmp_path / "validate_chatgpt_daily_report_new_conversation_replay.py"
    gate_file.write_text("# gate\n", encoding="utf-8")
    replay_file.write_text("# replay\n", encoding="utf-8")

    full_workflow.write_text(
        "\n".join(
            [
                *validator.REQUIRED_STATIC_VALIDATORS,
                validator.STATIC_COMPLETION_GATE_COMMAND,
                "- name: Replay ChatGPT-side daily PDF new conversation",
                validator.REPLAY_COMMAND,
                "PDF replay output_dir=chatgpt_side_outputs_new_conversation_replay",
                "--output-dir chatgpt_side_outputs_new_conversation_replay",
                validator.DAILY_FULL_OUTPUT_GATE_COMMAND,
                "- name: Dispatch and wait for GitHub Pages deploy",
            ]
        ),
        encoding="utf-8",
    )
    pr_workflow.write_text(
        "\n".join(
            [
                *validator.REQUIRED_PR_VALIDATORS,
                validator.STATIC_COMPLETION_GATE_COMMAND,
                "tests/test_daily_pdf_completion_hard_gate.py",
                "- name: Replay ChatGPT-side daily PDF new conversation",
                validator.REPLAY_COMMAND,
                "PDF replay output_dir=chatgpt_side_outputs_pr_validation",
                "--output-dir chatgpt_side_outputs_pr_validation",
                "- name: Upload PR daily PDF replay evidence",
                "chatgpt_side_outputs_pr_validation/*.pdf",
                "chatgpt_side_outputs_pr_validation/chatgpt_daily_report_runtime_manifest.json",
                "if-no-files-found: error",
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(validator, "DAILY_FULL_WORKFLOW", full_workflow)
    monkeypatch.setattr(validator, "DAILY_MODEL_PR_WORKFLOW", pr_workflow)
    monkeypatch.setattr(validator, "COMPLETION_GATE", gate_file)
    monkeypatch.setattr(validator, "REPLAY_VALIDATOR", replay_file)

    errors = validator.validate_workflow_gates()

    assert any(validator.PR_OUTPUT_GATE_COMMAND in error for error in errors)
