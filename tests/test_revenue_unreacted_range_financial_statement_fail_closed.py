from __future__ import annotations

import ast
import copy
import csv
import re
import sys
from pathlib import Path

import pandas as pd
import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_candidate_model_layer as model_layer  # noqa: E402
import validate_revenue_unreacted_range_financial_statement_fail_closed as guard  # noqa: E402


REVENUE_VALIDATOR_COMMAND = (
    "python scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py"
)
REVENUE_RUNTIME_COMMAND = f"{REVENUE_VALIDATOR_COMMAND} --phase runtime"
REVENUE_RUNTIME_STEP = "Validate revenue current artifact fail-closed contract"
REVENUE_INVOCATION_RE = re.compile(
    r"\bpython(?:3)?(?:\s+-[A-Za-z]+)*\s+scripts/"
    r"validate_revenue_unreacted_range_financial_statement_fail_closed\.py\b"
)
PRODUCTION_RUNTIME_CONTRACTS = (
    (
        ".github/workflows/daily_full_pipeline.yml",
        "daily-full-pipeline",
        "Build daily candidate model layer",
        "Build remaining daily model artifacts",
    ),
    (
        ".github/workflows/warrant_flow.yml",
        "warrant-flow",
        "Prepare warrant flow and formal model sync",
        "Build warrant downstream formal sync artifacts",
    ),
    (
        ".github/workflows/weekly_theme_review.yml",
        "weekly-theme-review",
        "Refresh theme mapping and catalyst performance",
        "Build weekly theme downstream formal sync artifacts",
    ),
)


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def _write_runtime_artifacts(root: Path, mutation: str = "") -> None:
    parameter = {
        "model_id": guard.MODEL_ID,
        "add_score_items": "核准的非財務事件類型",
        "forbidden_veto": "；".join(guard.FINANCIAL_FIELDS),
        "operation_guidance": "月營收與季／年財報維持獨立",
    }
    parity = {
        "model_id": guard.MODEL_ID,
        "parity_status": "warning_research_variant_only",
        "promotion_required": "True",
        "recommended_action": "do_not_promote",
    }
    readiness = {
        "model_id": guard.MODEL_ID,
        "approved_for_daily": "False",
        "presentation_allowed": "False",
        "operation_directive_level": "no_operation_directive",
    }
    candidate = {
        "source_row_index": "7",
        "stock_id": "1234",
        "event_catalyst_tags": "new_order;eps_surprise",
    }
    signal = {
        "model_id": guard.MODEL_ID,
        "source_row_index": "7.0",
        "stock_id": "1234",
        "score_components": guard.APPROVED_EVENT_COMPONENT,
    }
    if mutation == "parameter_financial_score":
        parameter["add_score_items"] += "；EPS"
    elif mutation == "parity_promotable":
        parity["parity_status"] = "pass"
    elif mutation == "readiness_presentable":
        readiness["presentation_allowed"] = "True"
    elif mutation == "untraceable_signal":
        signal["source_row_index"] = "8"
    elif mutation == "legacy_score_component":
        signal["score_components"] += ";EPS confirmation tag"
    elif mutation == "event_bonus_mismatch":
        signal["score_components"] = ""
    elif mutation:
        raise AssertionError(f"unknown runtime fixture mutation={mutation}")

    paths = {
        "daily_candidate_model_parameters_latest.csv": [parameter],
        "model_contract_parity_latest.csv": [parity],
        "model_operation_readiness_latest.csv": [readiness],
        "all_candidates_latest.csv": [candidate],
        "daily_candidate_model_signals_latest.csv": [signal],
    }
    for name, rows in paths.items():
        _write_csv(root / "output/latest" / name, rows)


def _normalized_run(run: object) -> str:
    if not isinstance(run, str):
        return ""
    return re.sub(r"\\\s*\n\s*", " ", run).replace("./scripts/", "scripts/")


def _production_runtime_contract_errors(
    workflow: dict[object, object],
    *,
    job_id: str,
    build_step_name: str,
    downstream_step_name: str,
) -> list[str]:
    errors: list[str] = []
    jobs = workflow.get("jobs", {})
    if not isinstance(jobs, dict) or not isinstance(jobs.get(job_id), dict):
        return [f"missing expected job {job_id}"]
    job = jobs[job_id]
    steps = job.get("steps", [])
    if not isinstance(steps, list):
        return [f"invalid steps for job {job_id}"]
    targets = [
        step
        for step in steps
        if isinstance(step, dict) and step.get("name") == REVENUE_RUNTIME_STEP
    ]
    if len(targets) != 1:
        return ["dedicated revenue runtime step must occur exactly once"]
    target = targets[0]
    if "continue-on-error" in job and job["continue-on-error"] is not False:
        errors.append("production runtime job must remain fail closed")
    if target.get("run") != REVENUE_RUNTIME_COMMAND:
        errors.append("dedicated revenue runtime step must be the exact single command")
    if any(key in target for key in ("if", "continue-on-error", "shell")):
        errors.append("dedicated revenue runtime step must be unconditional and use default shell")
    for scope, defaults in (
        ("workflow", workflow.get("defaults", {})),
        ("job", job.get("defaults", {})),
    ):
        if (
            isinstance(defaults, dict)
            and isinstance(defaults.get("run"), dict)
            and "shell" in defaults["run"]
        ):
            errors.append(f"{scope} defaults.run.shell must remain unset")

    all_runs = "\n".join(
        _normalized_run(step.get("run"))
        for candidate_job in jobs.values()
        if isinstance(candidate_job, dict)
        for step in candidate_job.get("steps", [])
        if isinstance(step, dict)
    )
    if len(REVENUE_INVOCATION_RE.findall(all_runs)) != 1:
        errors.append("workflow must contain exactly one logical revenue validator invocation")

    def named_step_indexes(name: str) -> list[int]:
        return [
            index
            for index, step in enumerate(steps)
            if isinstance(step, dict) and step.get("name") == name
        ]

    target_index = steps.index(target)
    build_indexes = named_step_indexes(build_step_name)
    summary_indexes = named_step_indexes(downstream_step_name)
    if len(build_indexes) != 1 or build_indexes[0] >= target_index:
        errors.append("current artifact build must precede the dedicated runtime step")
    if len(summary_indexes) != 1 or summary_indexes[0] <= target_index:
        errors.append("summary/downstream step must follow the dedicated runtime step")
    return errors


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


def test_default_and_explicit_full_phase_keep_every_existing_gate(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    calls: list[str] = []

    def recorded(name: str, result: object):
        def call(root: Path):
            calls.append(name)
            return result

        return call

    replacements = {
        "_static_semantic_errors": ("static", []),
        "_current_parameter_errors": ("parameters", []),
        "_historical_pit_errors": ("pit", ([], 68)),
        "_current_signal_errors": ("signals", ([], 11)),
        "_history_classification_errors": ("history", ([], 7, 3)),
        "_legacy_history_quarantine_errors": ("consumers", ([], 5)),
    }
    for function_name, (label, result) in replacements.items():
        monkeypatch.setattr(guard, function_name, recorded(label, result))

    expected_calls = ["static", "parameters", "pit", "signals", "history", "consumers"]
    for phase in (None, guard.VALIDATION_PHASE_FULL):
        calls.clear()
        if phase is None:
            errors, metrics = guard.validate(tmp_path)
        else:
            errors, metrics = guard.validate(tmp_path, phase=phase)
        assert errors == []
        assert calls == expected_calls
        assert metrics == {
            "current_revenue_signal_rows": 11,
            "pre_v2_legacy_history_rows": 7,
            "post_v2_history_rows": 3,
            "historical_pit_audit_rows": 68,
            "quarantine_control_count": 5,
        }


def test_runtime_phase_reads_only_current_artifacts(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    def reject_static(root: Path):
        raise AssertionError(f"runtime reached a static/history gate: {root}")

    for function_name in (
        "_static_semantic_errors",
        "_historical_pit_errors",
        "_history_classification_errors",
        "_legacy_history_quarantine_errors",
    ):
        monkeypatch.setattr(guard, function_name, reject_static)
    _write_runtime_artifacts(tmp_path)

    errors, metrics = guard.validate(tmp_path, phase=guard.VALIDATION_PHASE_RUNTIME)

    assert errors == []
    assert metrics == {
        "current_revenue_signal_rows": 1,
        "pre_v2_legacy_history_rows": 0,
        "post_v2_history_rows": 0,
        "historical_pit_audit_rows": 0,
        "quarantine_control_count": 2,
    }


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    (
        ("parameter_financial_score", "parameter artifact still exposes"),
        ("parity_promotable", "revenue parity must remain research-only"),
        ("readiness_presentable", "operation readiness must remain non-formal"),
        ("untraceable_signal", "cannot be traced to all_candidates source_row_index"),
        ("legacy_score_component", "retains legacy component"),
        ("event_bonus_mismatch", "event bonus does not match"),
    ),
)
def test_runtime_phase_fails_closed_on_each_current_gate(
    tmp_path: Path, mutation: str, expected_error: str
) -> None:
    _write_runtime_artifacts(tmp_path, mutation)
    errors, _ = guard.validate(tmp_path, phase=guard.VALIDATION_PHASE_RUNTIME)
    assert any(expected_error in error for error in errors)


def test_runtime_cli_reports_executed_and_skipped_scopes_truthfully(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    metrics = {
        "current_revenue_signal_rows": 4,
        "pre_v2_legacy_history_rows": 0,
        "post_v2_history_rows": 0,
        "historical_pit_audit_rows": 0,
        "quarantine_control_count": 2,
    }
    monkeypatch.setattr(guard, "validate", lambda root, *, phase: ([], metrics))

    assert guard.main(["--repo-root", str(tmp_path), "--phase", "runtime"]) == 0
    stdout = capsys.readouterr().out
    assert "validation_phase=runtime" in stdout
    assert "runtime_scope=current_parameters,current_parity,current_readiness," in stdout
    assert "current_signal_trace,current_score_event" in stdout
    assert "skipped=static_ast,static_config,historical_pit,full_history," in stdout
    assert "history_consumer_scan" in stdout
    assert "pre_v2_history_quarantined=" not in stdout


def test_production_workflows_use_one_dedicated_runtime_step_in_order() -> None:
    for (
        relative_path,
        job_id,
        build_step_name,
        downstream_step_name,
    ) in PRODUCTION_RUNTIME_CONTRACTS:
        workflow = yaml.safe_load((ROOT / relative_path).read_text(encoding="utf-8"))
        assert _production_runtime_contract_errors(
            workflow,
            job_id=job_id,
            build_step_name=build_step_name,
            downstream_step_name=downstream_step_name,
        ) == [], relative_path


@pytest.mark.parametrize(
    "mutation",
    (
        "rename",
        "step_if",
        "continue_on_error",
        "step_shell",
        "job_default_shell",
        "workflow_default_shell",
        "job_continue_true",
        "job_continue_dynamic",
        "alternate_path",
        "masked",
        "duplicate_bare",
        "wrong_order",
    ),
)
@pytest.mark.parametrize(
    ("relative_path", "job_id", "build_step_name", "downstream_step_name"),
    PRODUCTION_RUNTIME_CONTRACTS,
)
def test_dedicated_runtime_step_contract_rejects_representative_mutations(
    mutation: str,
    relative_path: str,
    job_id: str,
    build_step_name: str,
    downstream_step_name: str,
) -> None:
    workflow = yaml.safe_load(
        (ROOT / relative_path).read_text(encoding="utf-8")
    )
    mutated = copy.deepcopy(workflow)
    job = mutated["jobs"][job_id]
    steps = job["steps"]
    target = next(step for step in steps if step.get("name") == REVENUE_RUNTIME_STEP)
    if mutation == "rename":
        target["name"] = "Renamed revenue validator"
    elif mutation == "step_if":
        target["if"] = "always()"
    elif mutation == "continue_on_error":
        target["continue-on-error"] = True
    elif mutation == "step_shell":
        target["shell"] = "bash {0}"
    elif mutation == "job_default_shell":
        job["defaults"] = {"run": {"shell": "bash {0}"}}
    elif mutation == "workflow_default_shell":
        mutated["defaults"] = {"run": {"shell": "bash {0}"}}
    elif mutation == "job_continue_true":
        job["continue-on-error"] = True
    elif mutation == "job_continue_dynamic":
        job["continue-on-error"] = "${{ always() }}"
    elif mutation == "alternate_path":
        target["run"] = target["run"].replace(" scripts/", " ./scripts/")
    elif mutation == "masked":
        target["run"] += " || true"
    elif mutation == "duplicate_bare":
        other = next(step for step in steps if isinstance(step.get("run"), str) and step is not target)
        other["run"] += f"\n{REVENUE_VALIDATOR_COMMAND}"
    else:
        steps.remove(target)
        summary_index = next(
            index
            for index, step in enumerate(steps)
            if isinstance(step, dict) and step.get("name") == downstream_step_name
        )
        steps.insert(summary_index + 1, target)

    assert _production_runtime_contract_errors(
        mutated,
        job_id=job_id,
        build_step_name=build_step_name,
        downstream_step_name=downstream_step_name,
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
