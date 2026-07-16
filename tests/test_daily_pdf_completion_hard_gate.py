from __future__ import annotations

from pathlib import Path

from scripts import validate_daily_pdf_completion_hard_gate as validator


ROOT = Path(__file__).resolve().parents[1]
LOW_VOLUME_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
LOW_VOLUME_MODEL_NAME = "低位放量攻擊模型"
OPERATION_SUMMARY_TEXT = (
    "買入：隔日開盤買入。"
    "賣出：依規則出場。"
    "停損：依規則停損。"
    "基礎模型績效：勝率1%。"
    "勝：測試勝。"
    "和：測試和。"
    "敗：測試敗。"
)


def compact_operation_pdf_text(text: str) -> str:
    return validator.compact_text(OPERATION_SUMMARY_TEXT + text)


def test_daily_pdf_completion_hard_gate_passes_current_repo() -> None:
    assert validator.validate() == []


def test_completion_gate_rejects_missing_runtime_manifest(tmp_path: Path) -> None:
    output_dir = tmp_path / "chatgpt_side_outputs"
    output_dir.mkdir()

    errors = validator.validate_output_dir(output_dir)

    assert any("runtime manifest" in error for error in errors)


def test_completion_gate_requires_operation_model_regression_contract() -> None:
    assert validator.validate_regression_contract() == []


def semantic_source_row(
    model_id: str,
    source_artifact: str,
    *,
    pdf_section: str = "confirmed_operation",
) -> dict[str, str]:
    return {
        "model_id": model_id,
        "pdf_section": pdf_section,
        "source_artifact": source_artifact,
    }


def test_completion_gate_accepts_semantic_manifest_dedicated_adapter_sources() -> None:
    rows = [
        semantic_source_row(
            "volume_range_breakout_v2_low_position_volume_attack",
            "output/latest/daily_volume_breakout_operation_section_latest.csv",
        ),
        semantic_source_row(
            "w_bottom_right_side",
            "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
            pdf_section="active_operation",
        ),
    ]

    errors = validator.validate_semantic_manifest_adapter_sources(rows)

    assert errors == []


def test_completion_gate_rejects_semantic_manifest_candidate_signal_source() -> None:
    rows = [
        semantic_source_row(
            "volume_range_breakout_v2_low_position_volume_attack",
            "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        )
    ]

    errors = validator.validate_semantic_manifest_adapter_sources(rows)

    assert any("must use dedicated adapter" in error for error in errors)


def test_completion_gate_rejects_semantic_manifest_unknown_operation_model() -> None:
    rows = [
        semantic_source_row(
            "future_operation_model",
            "output/latest/daily_future_operation_model_operation_section_latest.csv",
        )
    ]

    errors = validator.validate_semantic_manifest_adapter_sources(rows)

    assert any("without a formal PDF operation adapter contract" in error for error in errors)


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
        "mainstream_highlight": compact_operation_pdf_text(
            "23EMA回檔模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
            "23EMA回檔模型 操作中 1785"
        ),
        "non_mainstream_highlight": compact_operation_pdf_text(
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


def test_completion_gate_uses_volume_v2_display_name_fallback() -> None:
    assert (
        validator.model_display_name(
            "volume_range_breakout_v2_low_position_volume_attack",
            [{"model_name_zh": ""}],
        )
        == "低位放量攻擊模型"
    )
    assert (
        validator.model_display_name(
            "volume_range_breakout_v2_mid_position_momentum_attack",
            [{"model_name_zh": ""}],
        )
        == "中位動能放量攻擊模型"
    )
    assert (
        validator.model_display_name(
            "volume_range_breakout_v2_high_position_volume_attack",
            [{"model_name_zh": ""}],
        )
        == "高位階放量攻擊模型"
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
    text = compact_operation_pdf_text(
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


def test_completion_gate_requires_operation_summary_tokens() -> None:
    rows = {
        LOW_VOLUME_MODEL_ID: [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "model_name_zh": LOW_VOLUME_MODEL_NAME,
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "report_line": "both",
                "stock_display": "本日無股票推薦",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "model_name_zh": LOW_VOLUME_MODEL_NAME,
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "report_line": "both",
                "stock_display": "目前無操作中追蹤列",
            },
        ]
    }
    text = validator.compact_text(
        f"{LOW_VOLUME_MODEL_NAME} - 本日可買 / 已確認買入候選 本日無股票推薦 "
        f"{LOW_VOLUME_MODEL_NAME} - 操作中 目前無操作中追蹤列"
    )

    errors = validator.validate_operation_adapter_pdf_text(
        {
            "mainstream_highlight": text,
            "non_mainstream_highlight": text,
        },
        rows,
        required_model_ids=[LOW_VOLUME_MODEL_ID],
    )

    assert any("missing operation model summary token" in error for error in errors)


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
        "mainstream_highlight": compact_operation_pdf_text(
            "23EMA回檔模型 - 本日可買 / 已確認買入候選 本日無股票推薦 "
            "23EMA回檔模型 - 操作中"
        ),
        "non_mainstream_highlight": compact_operation_pdf_text(
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
        LOW_VOLUME_MODEL_ID: [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "report_line": "both",
                "stock_display": "本日無股票推薦",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
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
        "mainstream_highlight": compact_operation_pdf_text(
            f"{LOW_VOLUME_MODEL_NAME} - 本日可買 / 已確認買入候選 本日無股票推薦 "
            f"{LOW_VOLUME_MODEL_NAME} - 操作中 3055"
        ),
        "non_mainstream_highlight": compact_operation_pdf_text(
            f"{LOW_VOLUME_MODEL_NAME} - 本日可買 / 已確認買入候選 本日無股票推薦 "
            f"{LOW_VOLUME_MODEL_NAME} - 操作中 目前無操作中追蹤列"
        ),
    }

    errors = validator.validate_operation_adapter_pdf_text(
        role_to_text,
        rows,
        required_model_ids=[LOW_VOLUME_MODEL_ID],
        stock_report_lines={"3055": {"mainstream"}},
    )

    assert errors == []


def test_completion_gate_rejects_pr_workflow_without_post_replay_gate(
    tmp_path: Path, monkeypatch
) -> None:
    full_workflow = tmp_path / "daily_full_pipeline.yml"
    pr_workflow = tmp_path / "daily_model_maintenance_pr_validation.yml"
    pdf_replay_workflow = tmp_path / "daily_pdf_replay_pr_validation.yml"
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
            ]
        ),
        encoding="utf-8",
    )
    pdf_replay_workflow.write_text(
        "\n".join(
            [
                "python scripts/validate_repo_production_inventory.py",
                "python scripts/validate_daily_pdf_contract_consumers.py",
                "python scripts/validate_daily_pdf_shared_path_isolation.py",
                "python scripts/validate_daily_production_boundaries.py",
                validator.STATIC_COMPLETION_GATE_COMMAND,
                "- name: Replay ChatGPT-side daily PDF new conversation",
                validator.REPLAY_COMMAND,
                "PDF replay output_dir=chatgpt_side_outputs_pr_validation",
                "--output-dir chatgpt_side_outputs_pr_validation",
                "- name: Upload PR daily PDF replay evidence",
                "chatgpt_side_outputs_pr_validation/*.pdf",
                "chatgpt_side_outputs_pr_validation/chatgpt_daily_report_runtime_manifest.json",
                "chatgpt_side_outputs_pr_validation/chatgpt_daily_pdf_semantic_manifest.csv",
                "if-no-files-found: error",
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(validator, "DAILY_FULL_WORKFLOW", full_workflow)
    monkeypatch.setattr(validator, "DAILY_MODEL_PR_WORKFLOW", pr_workflow)
    monkeypatch.setattr(validator, "DAILY_PDF_REPLAY_PR_WORKFLOW", pdf_replay_workflow)
    monkeypatch.setattr(validator, "COMPLETION_GATE", gate_file)
    monkeypatch.setattr(validator, "REPLAY_VALIDATOR", replay_file)

    errors = validator.validate_workflow_gates()

    assert any(validator.PR_OUTPUT_GATE_COMMAND in error for error in errors)
