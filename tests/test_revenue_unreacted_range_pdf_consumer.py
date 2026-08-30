from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import pytest
from reportlab.platypus import Table


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_chatgpt_side_daily_reports as renderer  # noqa: E402
import validate_revenue_unreacted_range_pdf_consumer_contract as validator  # noqa: E402


EMPTY_TEXT = {
    "confirmed_operation": renderer.MODEL_EMPTY_STATE_TEXT,
    "confirmed_unranked_operation": "目前無已確認但未列入買進排序列",
    "pending_confirmation": "目前無待確認列",
    "active_operation": renderer.OPERATION_ACTIVE_EMPTY_STATE_TEXT,
}


def readiness_row(
    *,
    presentation_allowed: bool = True,
    pdf_status: str = "pdf_integrated_daily_adapter",
    module_id: str = renderer.REVENUE_UNREACTED_RANGE_OPERATION_MODULE_ID,
) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": renderer.REVENUE_UNREACTED_RANGE_MODEL_ID,
                "formal_model_use_allowed": True,
                "approved_for_daily": True,
                "presentation_allowed": presentation_allowed,
                "production_allowed": True,
                "pdf_integration_status": pdf_status,
                "operation_module_id": module_id,
                "daily_adapter_sections": "|".join(
                    renderer.REVENUE_UNREACTED_RANGE_OPERATION_SECTIONS
                ),
            }
        ]
    )


def dormant_readiness() -> pd.DataFrame:
    row = readiness_row(
        presentation_allowed=False,
        pdf_status="not_started",
        module_id="revenue_unreacted_range_source_mid_falling_v2_operation_v1",
    )
    row.loc[:, "formal_model_use_allowed"] = False
    row.loc[:, "approved_for_daily"] = False
    row.loc[:, "production_allowed"] = False
    row.loc[:, "daily_adapter_sections"] = ""
    return row


def operation_row(
    *,
    pdf_view: str,
    pdf_section: str,
    display_order: int,
    stock_id: str = "2408",
    report_line: str = "mainstream",
    row_type: str = "data",
) -> dict[str, object]:
    action = {
        "confirmed_operation": "confirmed_buy_candidate",
        "confirmed_unranked_operation": "confirmed_not_buy_ranked",
        "pending_confirmation": "pending_confirmation",
        "active_operation": "active_operation",
    }[pdf_section]
    buy_rank_eligible = pdf_section == "confirmed_operation" and row_type == "data"
    empty = row_type == "empty_state"
    return {
        "model_id": renderer.REVENUE_UNREACTED_RANGE_MODEL_ID,
        "operation_module_id": renderer.REVENUE_UNREACTED_RANGE_OPERATION_MODULE_ID,
        "adapter_schema_version": renderer.REVENUE_UNREACTED_RANGE_ADAPTER_SCHEMA_VERSION,
        "lifecycle_contract_version": renderer.REVENUE_UNREACTED_RANGE_LIFECYCLE_CONTRACT_VERSION,
        "pdf_view": pdf_view,
        "pdf_section": pdf_section,
        "row_type": row_type,
        "display_order": display_order,
        "operation_asof_date": "20260828",
        "report_line": report_line,
        "report_line_memberships": report_line,
        "operation_status": "" if empty else pdf_section,
        "operation_status_zh": "" if empty else {
            "confirmed_operation": "已確認買入候選",
            "confirmed_unranked_operation": "已確認但未列入買進排序",
            "pending_confirmation": "待確認",
            "active_operation": "正式操作中",
        }[pdf_section],
        "row_action_status": "" if empty else action,
        "buy_rank_eligible": False if empty else buy_rank_eligible,
        "formal_model_use_allowed": True,
        "approved_for_daily": True,
        "presentation_allowed": True,
        "production_allowed": True,
        "stock_id": "" if empty else stock_id,
        "stock_name": "" if empty else f"測試{stock_id}",
        "stock_display": "" if empty else f"{stock_id} 測試",
        "signal_date": "" if empty else "20260825",
        "confirmation_date": "" if empty else "20260826",
        "entry_date": "" if empty else "20260827",
        "exit_date": "",
        "entry_basis_zh": "D+2開盤買入",
        "stop_basis_zh": "無停損規則",
        "exit_rule_zh": "D+30收盤固定出場",
        "planned_holding_days": "30",
        "operation_age_days": "2",
        "rank_reason_zh": "凍結條件通過",
        "risk_tags_zh": "provisional_backtest_supported_oos_unconfirmed",
        "empty_text_zh": EMPTY_TEXT[pdf_section] if empty else "",
        "row_metric_status": "not_applicable_empty_state" if empty else "ready",
        "row_metric_scope": "" if empty else "frozen_primary",
        "row_metric_id": "" if empty else "source_mid_falling_v2",
        "row_metric_label_zh": "" if empty else "凍結回測",
        "row_metric_matched_add_score_ids": "",
        "row_metric_sample_size": "" if empty else "53",
        "row_metric_win_rate_zh": "" if empty else "勝率77.36%",
        "row_metric_neutral_rate_zh": "" if empty else "和局0.00%",
        "row_metric_failure_rate_zh": "" if empty else "敗率22.64%",
        "row_metric_avg_return_zh": "" if empty else "平均報酬+14.90%",
        "row_metric_median_return_zh": "" if empty else "中位報酬+9.41%",
        "row_metric_source": "" if empty else "approved_operation_evidence_v2",
        "row_metric_selection_status": "" if empty else "fixed_no_tuning",
    }


def enabled_inputs(frame: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {
        "model_readiness": readiness_row(),
        renderer.REVENUE_UNREACTED_RANGE_OPERATION_INPUT_KEY: frame,
    }


def _cell_text(value: object) -> str:
    if hasattr(value, "getPlainText"):
        return value.getPlainText()
    return str(value)


def _table_text(table: Table) -> str:
    return " ".join(_cell_text(cell) for row in table._cellvalues for cell in row)


def test_missing_or_dormant_readiness_fails_closed_without_legacy_rendering() -> None:
    for inputs in ({}, {"model_readiness": dormant_readiness()}):
        story: list[object] = []
        with pytest.raises(RuntimeError, match="legacy generic fallback is forbidden"):
            renderer.revenue_unreacted_range_pdf_adapter_enabled(inputs)
        with pytest.raises(RuntimeError, match="legacy generic fallback is forbidden"):
            renderer.render_operation_model_summary_if_applicable(
                story, inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
            )
        with pytest.raises(RuntimeError, match="legacy generic fallback is forbidden"):
            renderer.render_model_operation_section_if_applicable(
                story,
                inputs,
                renderer.REVENUE_UNREACTED_RANGE_MODEL_ID,
                "highlight",
                "mainstream",
            )
        with pytest.raises(RuntimeError, match="legacy generic fallback is forbidden"):
            renderer.model_pdf_presentation_order(
                inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID, 6.0
            )
        with pytest.raises(RuntimeError, match="legacy generic fallback is forbidden"):
            renderer.should_render_highlight_model_description(
                inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
            )
        assert story == []
    assert renderer.REVENUE_UNREACTED_RANGE_MODEL_ID not in renderer.OPERATION_TABLE_MODEL_IDS
    assert renderer.REVENUE_UNREACTED_RANGE_MODEL_ID not in renderer.OPERATION_RENDERED_SECTIONS


def test_activated_readiness_suppresses_generic_legacy_revenue_description() -> None:
    inputs = enabled_inputs(
        pd.DataFrame(
            [
                operation_row(
                    pdf_view="highlight",
                    pdf_section="confirmed_operation",
                    display_order=1,
                )
            ]
        )
    )

    assert not renderer.should_render_highlight_model_description(
        inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
    )


@pytest.mark.parametrize(
    ("presentation_allowed", "pdf_status"),
    [(True, "not_started"), (False, "pdf_integrated_daily_adapter")],
)
def test_partial_readiness_activation_fails_closed(
    presentation_allowed: bool, pdf_status: str
) -> None:
    inputs = {
        "model_readiness": readiness_row(
            presentation_allowed=presentation_allowed,
            pdf_status=pdf_status,
        )
    }
    with pytest.raises(RuntimeError, match="partially activated"):
        renderer.revenue_unreacted_range_pdf_adapter_enabled(inputs)


def test_enabled_readiness_requires_exact_v2_sections_and_permissions() -> None:
    frame = pd.DataFrame(
        [
            operation_row(
                pdf_view="highlight",
                pdf_section="confirmed_operation",
                display_order=1,
            )
        ]
    )
    extra_section = readiness_row()
    extra_section.loc[:, "daily_adapter_sections"] += "|legacy_generic"
    with pytest.raises(RuntimeError, match="readiness sections mismatch"):
        renderer.revenue_unreacted_range_pdf_adapter_enabled(
            {
                "model_readiness": extra_section,
                renderer.REVENUE_UNREACTED_RANGE_OPERATION_INPUT_KEY: frame,
            }
        )

    disabled_permission = readiness_row()
    disabled_permission.loc[:, "approved_for_daily"] = False
    with pytest.raises(RuntimeError, match="readiness permission mismatch"):
        renderer.revenue_unreacted_range_pdf_adapter_enabled(
            {
                "model_readiness": disabled_permission,
                renderer.REVENUE_UNREACTED_RANGE_OPERATION_INPUT_KEY: frame,
            }
        )


def test_enabled_readiness_requires_dedicated_artifact() -> None:
    with pytest.raises(RuntimeError, match="dedicated PDF operation artifact is empty or missing"):
        renderer.revenue_unreacted_range_pdf_adapter_enabled(
            {"model_readiness": readiness_row()}
        )


def test_dedicated_artifact_rejects_schema_metadata_and_research_fallback() -> None:
    row = operation_row(
        pdf_view="highlight", pdf_section="confirmed_operation", display_order=1
    )
    bad_schema = pd.DataFrame([{**row, "adapter_schema_version": "schema_v1"}])
    with pytest.raises(RuntimeError, match="adapter_schema_version"):
        renderer.validate_revenue_unreacted_range_operation_artifact(bad_schema)

    fallback = pd.DataFrame([{**row, "source_artifact": "output/latest/research_backtest/model_signals.csv"}])
    with pytest.raises(RuntimeError, match="forbids research/model_signals fallback"):
        renderer.validate_revenue_unreacted_range_operation_artifact(fallback)


def test_highlight_confirmed_is_uncapped_and_active_is_capped_at_ten() -> None:
    rows = []
    for index in range(1, 13):
        rows.append(
            operation_row(
                pdf_view="highlight",
                pdf_section="confirmed_operation",
                display_order=index,
                stock_id=f"{2400 + index:04d}",
            )
        )
        rows.append(
            operation_row(
                pdf_view="highlight",
                pdf_section="active_operation",
                display_order=index,
                stock_id=f"{2500 + index:04d}",
            )
        )
    inputs = enabled_inputs(pd.DataFrame(rows))

    confirmed = renderer.selected_revenue_unreacted_range_operation_rows_for_pdf(
        inputs, "highlight", "mainstream", "confirmed_operation"
    )
    active = renderer.selected_revenue_unreacted_range_operation_rows_for_pdf(
        inputs, "highlight", "mainstream", "active_operation"
    )

    assert len(confirmed) == 12
    assert len(active) == 10
    assert active["stock_id"].tolist() == [f"{2500 + index:04d}" for index in range(1, 11)]


def test_full_view_keeps_unranked_pending_and_all_active_rows() -> None:
    rows = []
    for section, base in (
        ("confirmed_operation", 2400),
        ("confirmed_unranked_operation", 2500),
        ("pending_confirmation", 2600),
        ("active_operation", 2700),
    ):
        for index in range(1, 13):
            rows.append(
                operation_row(
                    pdf_view="full",
                    pdf_section=section,
                    display_order=index,
                    stock_id=f"{base + index:04d}",
                )
            )
    inputs = enabled_inputs(pd.DataFrame(rows))

    for section in renderer.REVENUE_UNREACTED_RANGE_OPERATION_SECTIONS:
        selected = renderer.selected_revenue_unreacted_range_operation_rows_for_pdf(
            inputs, "full", "mainstream", section
        )
        assert len(selected) == 12


def test_report_lines_are_filtered_only_from_dedicated_adapter_rows() -> None:
    frame = pd.DataFrame(
        [
            operation_row(
                pdf_view="highlight",
                pdf_section="confirmed_operation",
                display_order=1,
                stock_id="2408",
                report_line="mainstream",
            ),
            operation_row(
                pdf_view="highlight",
                pdf_section="confirmed_operation",
                display_order=1,
                stock_id="5483",
                report_line="non_mainstream",
            ),
        ]
    )
    inputs = enabled_inputs(frame)

    mainstream = renderer.selected_revenue_unreacted_range_operation_rows_for_pdf(
        inputs, "highlight", "mainstream", "confirmed_operation"
    )
    non_mainstream = renderer.selected_revenue_unreacted_range_operation_rows_for_pdf(
        inputs, "highlight", "non_mainstream", "confirmed_operation"
    )
    assert mainstream["stock_id"].tolist() == ["2408"]
    assert non_mainstream["stock_id"].tolist() == ["5483"]


def test_dedicated_empty_tables_use_exact_business_empty_states() -> None:
    confirmed = renderer.build_revenue_unreacted_range_confirmed_operation_table(
        pd.DataFrame()
    )
    active = renderer.build_revenue_unreacted_range_active_operation_table(
        pd.DataFrame()
    )
    assert renderer.MODEL_EMPTY_STATE_TEXT in _table_text(confirmed)
    assert renderer.OPERATION_ACTIVE_EMPTY_STATE_TEXT in _table_text(active)


def test_pending_and_active_tables_render_chinese_operation_status() -> None:
    pending_row = operation_row(
        pdf_view="full", pdf_section="pending_confirmation", display_order=1
    )
    active_row = operation_row(
        pdf_view="full", pdf_section="active_operation", display_order=1
    )

    pending_text = _table_text(
        renderer.build_revenue_unreacted_range_pending_operation_table(
            pd.DataFrame([pending_row])
        )
    )
    active_text = _table_text(
        renderer.build_revenue_unreacted_range_active_operation_table(
            pd.DataFrame([active_row])
        )
    )

    assert "待確認" in pending_text
    assert "pending_confirmation" not in pending_text
    assert "正式操作中" in active_text
    assert "active_operation" not in active_text


@pytest.mark.parametrize(("pdf_view", "expected_table_count"), [("highlight", 2), ("full", 4)])
def test_dedicated_renderer_uses_two_highlight_tables_and_four_full_tables(
    pdf_view: str,
    expected_table_count: int,
) -> None:
    sections = (
        ("confirmed_operation", "active_operation")
        if pdf_view == "highlight"
        else renderer.REVENUE_UNREACTED_RANGE_OPERATION_SECTIONS
    )
    frame = pd.DataFrame(
        [
            operation_row(
                pdf_view=pdf_view,
                pdf_section=section,
                display_order=1,
                row_type="empty_state",
            )
            for section in sections
        ]
    )
    story: list[object] = []
    renderer.render_revenue_unreacted_range_operation_section(
        story,
        enabled_inputs(frame),
        pdf_view,
        "mainstream",
    )
    tables = [flowable for flowable in story if isinstance(flowable, Table)]
    assert len(tables) == expected_table_count
    assert renderer.MODEL_EMPTY_STATE_TEXT in _table_text(tables[0])
    assert renderer.OPERATION_ACTIVE_EMPTY_STATE_TEXT in _table_text(tables[-1])


def test_activated_summary_uses_frozen_d2_d30_outcomes_and_sort_order() -> None:
    approval = pd.DataFrame(
        [
            {
                "model_id": renderer.REVENUE_UNREACTED_RANGE_MODEL_ID,
                "entry_rule_zh": "D+2開盤買入",
                "exit_rule_zh": "D+30收盤固定出場",
                "stop_loss_rule_zh": "無停損規則",
                "best_evidence_sample_size": "53",
                "best_evidence_win_rate": "77.3585",
                "best_evidence_median_return": "9.4077",
            }
        ]
    )
    inputs = {
        "model_readiness": readiness_row(),
        "approved_operation_patterns": approval,
        renderer.REVENUE_UNREACTED_RANGE_OPERATION_INPUT_KEY: pd.DataFrame(
            [
                operation_row(
                    pdf_view="highlight",
                    pdf_section="confirmed_operation",
                    display_order=1,
                )
            ]
        ),
    }
    summary = renderer.operation_model_summary_text(
        inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
    )

    assert "D+2開盤" in summary
    assert "D+30收盤固定出場" in summary
    assert "樣本數53" in summary
    assert "勝率77.36%" in summary
    assert renderer.model_pdf_presentation_order(
        inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID, 6.0
    ) == 1.25


def test_activated_operation_model_with_confirmed_data_is_not_misclassified_as_generic_zero_candidate() -> None:
    registry = pd.DataFrame(
        [
            {
                "model_id": renderer.REVENUE_UNREACTED_RANGE_MODEL_ID,
                "model_name_zh": "營收爆發但股價尚未反應模型",
                "model_registry_order": "6",
                "model_registry_active": True,
                "report_line_applicability": "both",
            }
        ]
    )
    enabled = {
        "model_readiness": readiness_row(),
        "model_registry": registry,
        "model_signals": pd.DataFrame(),
        renderer.REVENUE_UNREACTED_RANGE_OPERATION_INPUT_KEY: pd.DataFrame(
            [
                operation_row(
                    pdf_view="highlight",
                    pdf_section="confirmed_operation",
                    display_order=1,
                )
            ]
        ),
    }
    text = "營收爆發但股價尚未反應模型 2408 已確認買入候選"
    assert renderer.required_stock_model_text_missing(
        enabled, "mainstream", text
    ) == []

    dormant = {
        "model_readiness": dormant_readiness(),
        "model_registry": registry,
        "model_parameters": pd.DataFrame(
            [
                {
                    "model_id": renderer.REVENUE_UNREACTED_RANGE_MODEL_ID,
                    "pdf_visibility": "pdf_core_model",
                }
            ]
        ),
        "model_signals": pd.DataFrame(),
    }
    with pytest.raises(RuntimeError, match="legacy generic fallback is forbidden"):
        renderer.required_stock_model_text_missing(dormant, "mainstream", text)


def test_legacy_generic_revenue_rows_never_reach_generic_pdf_consumers() -> None:
    signals = pd.DataFrame(
        [
            {
                "model_id": renderer.REVENUE_UNREACTED_RANGE_MODEL_ID,
                "model_name_zh": "舊營收 generic 列",
                "stock_id": "5483",
                "report_line": "mainstream",
                "model_rank": "1",
                "display_rank": "1",
                "model_score": "99",
            },
            {
                "model_id": "other_model",
                "model_name_zh": "其他模型",
                "stock_id": "2408",
                "report_line": "mainstream",
                "model_rank": "2",
                "display_rank": "2",
                "model_score": "50",
            },
        ]
    )
    inputs = enabled_inputs(
        pd.DataFrame(
            [
                operation_row(
                    pdf_view="highlight",
                    pdf_section="confirmed_operation",
                    display_order=1,
                )
            ]
        )
    )
    inputs["model_signals"] = signals

    filtered = renderer.revenue_unreacted_range_generic_signal_rows_removed(inputs)
    assert filtered["model_id"].tolist() == ["other_model"]
    assert renderer.model_signal_rows(
        inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
    ) == []
    assert renderer.mainstream_curated_model_signal_rows(
        inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
    ) == []
    assert renderer.mainstream_full_model_signal_rows(
        inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
    ) == []
    assert renderer.non_mainstream_curated_model_signal_rows(
        inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
    ) == []
    assert renderer.non_mainstream_full_model_signal_rows(
        inputs, renderer.REVENUE_UNREACTED_RANGE_MODEL_ID
    ) == []
    assert renderer.preferred_model_label_for_stock(
        inputs, "2408", "mainstream"
    ) == "其他模型 #2"
    assert renderer.volume_operation_report_lines_for_stock(inputs, "5483") == set()


def test_legacy_generic_revenue_rows_cannot_bypass_missing_or_dormant_readiness() -> None:
    signals = pd.DataFrame(
        [{"model_id": renderer.REVENUE_UNREACTED_RANGE_MODEL_ID, "stock_id": "2408"}]
    )
    for inputs in (
        {"model_signals": signals},
        {"model_signals": signals, "model_readiness": dormant_readiness()},
    ):
        with pytest.raises(RuntimeError, match="legacy generic fallback is forbidden"):
            renderer.revenue_unreacted_range_generic_signal_rows_removed(inputs)


def test_semantic_manifest_adds_revenue_only_when_enabled_and_uses_dedicated_hash(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    rows = []
    for report_line in ("mainstream", "non_mainstream"):
        for pdf_view, sections in (
            ("highlight", ("confirmed_operation", "active_operation")),
            ("full", renderer.REVENUE_UNREACTED_RANGE_OPERATION_SECTIONS),
        ):
            for section in sections:
                rows.append(
                    operation_row(
                        pdf_view=pdf_view,
                        pdf_section=section,
                        display_order=1,
                        report_line=report_line,
                        row_type="empty_state",
                    )
                )
    frame = pd.DataFrame(rows)
    inputs = enabled_inputs(frame)
    repo = tmp_path / "repo"
    out = tmp_path / "out"
    source = repo / renderer.REVENUE_UNREACTED_RANGE_OPERATION_SOURCE_ARTIFACT
    source.parent.mkdir(parents=True)
    source.write_text("dedicated-revenue-adapter\n", encoding="utf-8")
    out.mkdir()
    monkeypatch.setattr(renderer, "REPO", repo)
    monkeypatch.setattr(renderer, "OUT", out)
    monkeypatch.setattr(renderer, "DATA_DATE", "20260828")
    monkeypatch.setattr(renderer, "REQUEST_DATE", "20260830")
    monkeypatch.setattr(renderer, "OPERATION_RENDERED_SECTIONS", {})

    with pytest.raises(RuntimeError, match="legacy generic fallback is forbidden"):
        renderer.operation_rendered_sections_for_inputs(
            {"model_readiness": dormant_readiness()}
        )
    paths = [out / f"report-{index}.pdf" for index in range(6)]
    manifest = renderer.write_pdf_semantic_manifest(paths, inputs)
    result = pd.read_csv(manifest, encoding="utf-8-sig")
    revenue = result[result["model_id"].eq(renderer.REVENUE_UNREACTED_RANGE_MODEL_ID)]

    assert not revenue.empty
    assert set(revenue["source_artifact"]) == {
        renderer.REVENUE_UNREACTED_RANGE_OPERATION_SOURCE_ARTIFACT
    }
    expected_hash = renderer.normalized_sha256_file(source)
    assert set(revenue["source_sha256"]) == {expected_hash}
    assert set(
        revenue[revenue["pdf_view"].eq("highlight")]["pdf_section"]
    ) == {"confirmed_operation", "active_operation"}


def test_independent_source_validator_passes_and_rejects_fallback_mutation(
    tmp_path: Path,
) -> None:
    assert validator.validate_renderer() == []
    source = renderer.__file__ and Path(renderer.__file__).read_text(encoding="utf-8")
    marker = (
        "def revenue_unreacted_range_operation_frame(\n"
        "    inputs: dict[str, pd.DataFrame],\n"
        "    pdf_view: str,\n"
        "    pdf_section: str,\n"
        ") -> pd.DataFrame:\n"
    )
    assert marker in source
    mutated = source.replace(
        marker,
        marker + '    inputs.get("model_signals", pd.DataFrame())\n',
        1,
    )
    path = tmp_path / "mutated_renderer.py"
    path.write_text(mutated, encoding="utf-8")

    errors = validator.validate_renderer(path)
    assert any("forbidden fallback dependency" in error for error in errors)

    summary_mutated = source.replace(
        marker,
        marker + '    inputs.get("model_summary", pd.DataFrame())\n',
        1,
    )
    summary_path = tmp_path / "mutated_summary_renderer.py"
    summary_path.write_text(summary_mutated, encoding="utf-8")
    summary_errors = validator.validate_renderer(summary_path)
    assert any("generic model_summary read" in error for error in summary_errors)
