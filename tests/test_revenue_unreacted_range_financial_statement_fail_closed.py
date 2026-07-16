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
    assert metrics["historical_pit_audit_rows"] == 62
    assert metrics["pre_v2_legacy_history_rows"] > 0
    assert metrics["quarantine_control_count"] == 5


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
