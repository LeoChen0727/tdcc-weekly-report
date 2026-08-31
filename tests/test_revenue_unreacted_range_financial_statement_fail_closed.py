from __future__ import annotations

import ast
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_candidate_model_layer as model_layer  # noqa: E402
import validate_revenue_unreacted_range_financial_statement_fail_closed as guard  # noqa: E402


def _score(
    *,
    event_tags: str = "",
    fundamental_tags: str = "",
    extra_fields: dict[str, object] | None = None,
) -> tuple[float, list[str]]:
    values: dict[str, object] = {
        "event_catalyst_tags": event_tags,
        "fundamental_catalyst_tags": fundamental_tags,
    }
    values.update(extra_fields or {})
    row = pd.Series(values)
    score, components, _ = model_layer.score_revenue_unreacted(row)
    return score, components


def test_revenue_score_ignores_financial_and_unknown_catalyst_tags() -> None:
    baseline_score, baseline_components = _score()
    denied_event_tags = (
        "eps_surprise",
        "margin_improvement",
        "profit_turnaround",
        "material_information;new_order",
        "investor_conference;new_order",
        "shareholder_meeting",
        "unknown;new_order",
        "unapproved_event",
    )
    for event_tags in denied_event_tags:
        score, components = _score(event_tags=event_tags)
        assert score == pytest.approx(baseline_score), event_tags
        assert components == baseline_components, event_tags

    denied_fundamental_tags = (
        "eps_surprise",
        "gross_margin",
        "operating_margin;operating_income",
        "non_operating_income;net_income",
    )
    for fundamental_tags in denied_fundamental_tags:
        score, components = _score(fundamental_tags=fundamental_tags)
        assert score == pytest.approx(baseline_score), fundamental_tags
        assert components == baseline_components, fundamental_tags


def test_revenue_score_ignores_every_registered_financial_source_field() -> None:
    baseline_score, baseline_components = _score()
    for field in sorted(guard._financial_statement_source_fields(ROOT)):
        for source_field in (field, f"quarterly_{field}_ttm"):
            score, components = _score(extra_fields={source_field: 999})
            assert score == pytest.approx(baseline_score), source_field
            assert components == baseline_components, source_field


def test_revenue_score_allows_only_exact_first_token_non_financial_events() -> None:
    baseline_score, _ = _score()
    for event_type in sorted(guard.APPROVED_NON_FINANCIAL_EVENT_TYPES):
        score, components = _score(event_tags=f"{event_type};eps_surprise;theme_tag")
        assert score == pytest.approx(baseline_score + 3), event_type
        assert "核准非財務事件 +3" in components


def test_independent_repository_fail_closed_validator_passes() -> None:
    errors, metrics = guard.validate(ROOT)
    assert errors == []
    assert metrics["historical_pit_audit_rows"] == 68
    assert metrics["pre_v2_legacy_history_rows"] > 0
    assert metrics["quarantine_control_count"] == 5


@pytest.mark.parametrize(
    ("phase", "contract", "condition", "surface", "parameter"),
    [
        (
            guard.REVENUE_LEGACY_PHASE,
            guard.REVENUE_LEGACY_CONTRACT_PHASE_FIELDS,
            guard.REVENUE_LEGACY_CONDITION_PHASE_FIELDS,
            guard.REVENUE_LEGACY_SURFACE_PHASE_FIELDS,
            guard.REVENUE_LEGACY_PARAMETER_PHASE_FIELDS,
        ),
        (
            guard.REVENUE_PREPARED_PHASE,
            guard.REVENUE_PREPARED_CONTRACT_PHASE_FIELDS,
            guard.REVENUE_PREPARED_CONDITION_PHASE_FIELDS,
            guard.REVENUE_PREPARED_SURFACE_PHASE_FIELDS,
            guard.REVENUE_PREPARED_PARAMETER_PHASE_FIELDS,
        ),
        (
            guard.REVENUE_ACTIVATED_PHASE,
            guard.REVENUE_ACTIVATED_CONTRACT_PHASE_FIELDS,
            guard.REVENUE_ACTIVATED_CONDITION_PHASE_FIELDS,
            guard.REVENUE_ACTIVATED_SURFACE_PHASE_FIELDS,
            guard.REVENUE_ACTIVATED_PARAMETER_PHASE_FIELDS,
        ),
    ],
)
def test_financial_guard_accepts_only_exact_revenue_formal_phases(
    phase: str,
    contract: dict[str, str],
    condition: dict[str, str],
    surface: dict[str, str],
    parameter: dict[str, str],
) -> None:
    assert guard._classify_revenue_formal_phase(
        {"model_id": guard.MODEL_ID, **contract},
        {"model_id": guard.MODEL_ID, **condition},
        {"surface_id": guard.MODEL_ID, **surface},
        {"model_id": guard.MODEL_ID, **parameter},
    ) == phase


@pytest.mark.parametrize("mixed_component", ["contract", "condition", "surface", "parameter"])
def test_financial_guard_rejects_prepared_activated_mixed_state(
    mixed_component: str,
) -> None:
    values = {
        "contract": dict(guard.REVENUE_ACTIVATED_CONTRACT_PHASE_FIELDS),
        "condition": dict(guard.REVENUE_ACTIVATED_CONDITION_PHASE_FIELDS),
        "surface": dict(guard.REVENUE_ACTIVATED_SURFACE_PHASE_FIELDS),
        "parameter": dict(guard.REVENUE_ACTIVATED_PARAMETER_PHASE_FIELDS),
    }
    prepared = {
        "contract": guard.REVENUE_PREPARED_CONTRACT_PHASE_FIELDS,
        "condition": guard.REVENUE_PREPARED_CONDITION_PHASE_FIELDS,
        "surface": guard.REVENUE_PREPARED_SURFACE_PHASE_FIELDS,
        "parameter": guard.REVENUE_PREPARED_PARAMETER_PHASE_FIELDS,
    }
    values[mixed_component] = dict(prepared[mixed_component])
    assert guard._classify_revenue_formal_phase(
        values["contract"],
        values["condition"],
        values["surface"],
        values["parameter"],
    ) is None


def test_activated_phase_keeps_exact_immutable_evidence_and_monthly_only_scope() -> None:
    assert guard.REVENUE_EXACT_EVIDENCE_PIN["canonical_sha256"] == (
        "4890147988797f8d0e7a27777d400514b423b679f108565675309ec2e83161fb"
    )
    registered = guard._financial_statement_source_fields(ROOT)
    for field in (
        "basic_eps",
        "gross_margin",
        "operating_margin",
        "operating_income",
        "non_operating_income_expense",
        "net_income",
    ):
        assert field in registered


def test_activated_readiness_identity_is_exact_and_lifecycle_aware() -> None:
    readiness = {
        "operation_module_status": (
            "approved_operation_v2_provisional_backtest_supported_oos_unconfirmed"
        ),
        "daily_adapter_status": "ready_empty_no_operation_rows",
        "formal_model_use_allowed": "True",
        "approved_for_daily": "True",
        "approval_status": "provisional_backtest_supported_oos_unconfirmed",
        "operation_module_id": (
            "revenue_unreacted_range_source_mid_falling_v2_operation_v2"
        ),
        "approval_version": (
            "revenue_unreacted_range_source_mid_falling_formal_operation_v2_20260830"
        ),
        "presentation_allowed": "True",
        "production_allowed": "True",
        "operation_directive_level": "approved_daily_operation_guidance",
        "pdf_integration_status": "pdf_integrated_daily_adapter",
        "packet_integration_status": "pending_packet_consumer",
        "daily_adapter_data_row_count": "0",
        "daily_adapter_sections": (
            "active_operation,confirmed_operation,"
            "confirmed_unranked_operation,pending_confirmation"
        ),
    }
    assert guard._activated_readiness_matches(readiness)

    with_rows = dict(readiness)
    with_rows["daily_adapter_data_row_count"] = "2"
    with_rows["daily_adapter_status"] = "ready_approved_operation_guidance"
    assert guard._activated_readiness_matches(with_rows)

    for field in (
        "operation_module_status",
        "approval_status",
        "approval_version",
        "operation_directive_level",
        "daily_adapter_sections",
    ):
        drifted = dict(readiness)
        drifted[field] = "drifted"
        assert not guard._activated_readiness_matches(drifted)


def test_legacy_signal_log_exception_is_exactly_one_immutable_archive() -> None:
    lineage_rows = guard._read_rows(ROOT / "config/report_artifact_lineage.csv")
    revenue_lineage = [
        row
        for row in lineage_rows
        if guard.LEGACY_SIGNAL_LOG in row.get("source_artifacts", "")
        and guard.MODEL_ID in " ".join(row.values())
    ]
    archive_script = ROOT / guard.LEGACY_ARCHIVE_PRODUCER
    assert guard._legacy_archive_quarantine_errors(
        ROOT,
        revenue_lineage,
        [archive_script],
    ) == []

    unexpected_lineage = dict(revenue_lineage[0])
    unexpected_lineage["artifact_path"] = "output/latest/forbidden_runtime_consumer.csv"
    errors = guard._legacy_archive_quarantine_errors(
        ROOT,
        [*revenue_lineage, unexpected_lineage],
        [archive_script],
    )
    assert any("limited to the immutable legacy archive" in error for error in errors)

    errors = guard._legacy_archive_quarantine_errors(
        ROOT,
        revenue_lineage,
        [archive_script, ROOT / "scripts/forbidden_revenue_runtime_consumer.py"],
    )
    assert any(
        "only the immutable legacy archive producer" in error for error in errors
    )


def test_independent_validator_does_not_import_production_business_module() -> None:
    source = (ROOT / "scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py").read_text(
        encoding="utf-8"
    )
    assert "import build_daily_candidate_model_layer" not in source


@pytest.mark.parametrize(
    "financial_field", sorted(guard._financial_statement_source_fields(ROOT))
)
def test_reachable_semantic_guard_rejects_condition_side_financial_bypass(
    financial_field: str,
) -> None:
    source = (ROOT / "scripts/build_daily_candidate_model_layer.py").read_text(
        encoding="utf-8"
    )
    original = "return strong_revenue(row) and in_recent_range(row, 5) and not active_attack"
    assert original in source
    for source_field in (financial_field, f"quarterly_{financial_field}_ttm"):
        replacement = (
            f'return strong_revenue(row) and num(row, "{source_field}") > 0 '
            "and in_recent_range(row, 5) and not active_attack"
        )
        mutated_tree = ast.parse(source.replace(original, replacement, 1))
        hits = guard._financial_reference_hits(
            mutated_tree,
            ("cond_revenue_unreacted", "score_revenue_unreacted"),
            guard._financial_statement_source_fields(ROOT),
        )
        assert any(source_field in hit for hit in hits)


def test_event_bonus_ast_guard_rejects_or_bypass() -> None:
    source = (ROOT / "scripts/build_daily_candidate_model_layer.py").read_text(
        encoding="utf-8"
    )
    original = "if event_type in approved_non_financial_event_types:"
    replacement = (
        'if event_type in approved_non_financial_event_types or event_type == "unapproved_event":'
    )
    assert original in source
    mutated_tree = ast.parse(source.replace(original, replacement, 1))
    function = guard._function_node(mutated_tree, "score_revenue_unreacted")
    assert function is not None
    assert guard._strict_event_bonus_errors(function)


def test_event_bonus_ast_guard_rejects_unlabeled_second_event_branch() -> None:
    source = (ROOT / "scripts/build_daily_candidate_model_layer.py").read_text(
        encoding="utf-8"
    )
    original = '        comps.append("核准非財務事件 +3")\n'
    replacement = (
        original
        + '    if event_type == "financial_results":\n'
        + "        score += 3\n"
    )
    assert original in source
    mutated_tree = ast.parse(source.replace(original, replacement, 1))
    function = guard._function_node(mutated_tree, "score_revenue_unreacted")
    assert function is not None
    assert guard._strict_event_bonus_errors(function)


def test_reachable_event_source_guard_rejects_helper_bypass() -> None:
    source = (ROOT / "scripts/build_daily_candidate_model_layer.py").read_text(
        encoding="utf-8"
    )
    helper = (
        "def revenue_event_bypass(row: pd.Series) -> float:\n"
        '    return 3.0 if text(row, "event_catalyst_tags") == "financial_results" else 0.0\n\n\n'
    )
    score_marker = "def score_revenue_unreacted(row: pd.Series)"
    assert score_marker in source
    mutated = source.replace(score_marker, helper + score_marker, 1)
    score_line = (
        '    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["revenue_unreacted_range"])\n'
    )
    assert score_line in mutated
    mutated = mutated.replace(
        score_line, score_line + "    score += revenue_event_bypass(row)\n", 1
    )
    mutated_tree = ast.parse(mutated)
    reachable = guard._reachable_function_nodes(
        mutated_tree, ("cond_revenue_unreacted", "score_revenue_unreacted")
    )
    assert guard._reachable_event_source_locations(reachable) != [
        "score_revenue_unreacted"
    ]


def test_module_literal_aliases_cannot_bypass_event_or_financial_guards() -> None:
    source = (ROOT / "scripts/build_daily_candidate_model_layer.py").read_text(
        encoding="utf-8"
    )
    helper = (
        'EVENT_FIELD_ALIAS = "event_" + "catalyst_tags"\n'
        'FIN_FIELD_ALIAS = "gross_" + "profit"\n\n'
        "def hidden_alias_bonus(row: pd.Series) -> float:\n"
        '    event_bonus = 3.0 if text(row, EVENT_FIELD_ALIAS) == "financial_results" else 0.0\n'
        "    return event_bonus + num(row, FIN_FIELD_ALIAS)\n\n\n"
    )
    score_marker = "def score_revenue_unreacted(row: pd.Series)"
    assert score_marker in source
    mutated = source.replace(score_marker, helper + score_marker, 1)
    score_line = (
        '    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["revenue_unreacted_range"])\n'
    )
    assert score_line in mutated
    mutated = mutated.replace(
        score_line, score_line + "    score += hidden_alias_bonus(row)\n", 1
    )
    mutated_tree = ast.parse(mutated)
    aliases = guard._module_literal_string_aliases(mutated_tree)
    assert aliases["EVENT_FIELD_ALIAS"] == "event_catalyst_tags"
    assert aliases["FIN_FIELD_ALIAS"] == "gross_profit"
    roots = ("cond_revenue_unreacted", "score_revenue_unreacted")
    reachable = guard._reachable_function_nodes(mutated_tree, roots)
    assert guard._reachable_event_source_locations(reachable, aliases) != [
        "score_revenue_unreacted"
    ]
    hits = guard._financial_reference_hits(
        mutated_tree, roots, guard._financial_statement_source_fields(ROOT)
    )
    assert any("gross_profit" in hit for hit in hits)


def test_history_date_classifier_allows_valid_post_v2_rows_and_rejects_bad_dates() -> None:
    pre_v2, post_v2, errors = guard._classify_history_dates(
        [
            {"signal_date": "20260715"},
            {"signal_date": "20260716"},
            {"signal_date": "2026-07-17"},
            {"signal_date": "20260230"},
        ]
    )
    assert pre_v2 == 1
    assert post_v2 == 1
    assert len(errors) == 2
