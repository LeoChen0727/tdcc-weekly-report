from __future__ import annotations

from pathlib import Path
import json
import subprocess
import pytest

from scripts import validate_chatgpt_daily_report_new_conversation_replay as replay
from scripts.validate_chatgpt_daily_report_new_conversation_replay import (
    EXPECTED_PDF_ROLES,
    HIGHLIGHT_FULL_TEXT_FORBIDDEN_TEXT,
    HIGHLIGHT_FULL_TEXT_REQUIRED_TEXT,
    HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT,
    HIGHLIGHT_LAYOUT_ROLES,
    HIGHLIGHT_STOCK_MODEL_SECTION_TEXT,
    RENDERED_MODEL_REGRESSION_CONTRACT,
    RUNTIME_MANIFEST_NAME,
    SEMANTIC_GOLDEN_CASES_CONTRACT,
    SEMANTIC_MANIFEST_NAME,
    pdf_paths_from_stdout,
    read_rendered_model_regression_contract,
    read_semantic_golden_cases,
    role_to_pdf_paths_from_manifest,
    validate_highlight_layout_texts,
    validate_rendered_model_regression_texts,
    validate_semantic_golden_cases,
    validate_semantic_manifest_schema,
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
        "semantic_manifest_path": str((paths[0].parent / SEMANTIC_MANIFEST_NAME).resolve()),
    }


def test_replay_zero_exit_without_completion_marker_reports_child_output() -> None:
    proc = subprocess.CompletedProcess(
        args=["python", "entrypoint.py"],
        returncode=0,
        stdout="休市，無新報告: market_status=closed_scheduled\n",
        stderr="",
    )

    try:
        replay.require_completed_replay(proc)
    except replay.ReplayValidationError as exc:
        text = str(exc)
        assert "returned exit code 0 without the official completion marker" in text
        assert "market_status=closed_scheduled" in text
    else:
        raise AssertionError("zero-output replay must not be treated as completed")


def test_replay_origin_main_date_must_match_source_freshness_contract() -> None:
    state = {
        "expected_main_price_date": "20260717",
        "main_price_date": "20260717",
    }

    assert (
        replay.resolve_validation_replay_date(state, "origin/main", "20260717")
        == "20260717"
    )

    try:
        replay.resolve_validation_replay_date(state, "origin/main", "20260716")
    except replay.ReplayValidationError as exc:
        assert "does not match the source freshness contract" in str(exc)
    else:
        raise AssertionError("mismatched workflow expected date must fail closed")


@pytest.mark.parametrize(
    ("market_session_date", "expected_main_price_date", "reason_code"),
    [
        ("20260718", "20260717", "weekend"),
        ("20260228", "20260227", "exchange_holiday"),
    ],
)
def test_replay_infers_exact_scheduled_closure_date_from_committed_status(
    tmp_path: Path,
    monkeypatch,
    market_session_date: str,
    expected_main_price_date: str,
    reason_code: str,
) -> None:
    monkeypatch.setattr(
        replay,
        "git_show_text",
        lambda repo_root, source_ref, repo_path: json.dumps(
            {
                "market_status": "closed_scheduled",
                "phase": "preflight",
                "market_session_date": market_session_date,
                "expected_main_price_date": expected_main_price_date,
                "should_run_daily_pipeline": False,
                "reason_code": reason_code,
            }
        ),
    )

    assert replay.infer_committed_closed_scheduled_replay_date(
        tmp_path,
        "pinned-replay/workflow-29677505156-1",
    ) == expected_main_price_date


def test_replay_open_session_does_not_enable_closed_validation_mode(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        replay,
        "git_show_text",
        lambda repo_root, source_ref, repo_path: json.dumps(
            {
                "market_status": "open_confirmed",
                "phase": "confirm",
                "market_session_date": "20260717",
                "expected_main_price_date": "20260717",
                "should_run_daily_pipeline": True,
            }
        ),
    )

    assert replay.infer_committed_closed_scheduled_replay_date(
        tmp_path,
        "pinned-replay/workflow-open",
    ) == ""


def test_replay_pinned_branch_closed_date_must_match_source_freshness_contract() -> None:
    state = {
        "market_session_status": "closed_scheduled",
        "expected_main_price_date": "20260717",
        "main_price_date": "20260717",
    }

    assert replay.resolve_validation_replay_date(
        state,
        "pinned-replay/workflow-29677505156-1",
        "20260717",
    ) == "20260717"
    with pytest.raises(replay.ReplayValidationError, match="source freshness contract"):
        replay.resolve_validation_replay_date(
            state,
            "pinned-replay/workflow-29677505156-1",
            "20260716",
        )


def test_run_replay_passes_exact_origin_main_date_to_entrypoint(
    tmp_path: Path,
    monkeypatch,
) -> None:
    source_root = tmp_path / "clean-source"
    source_root.mkdir()
    stale_path = tmp_path / replay.STALE_RESIDUE_NAME
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "expected_main_price_date": "20260717",
        "main_price_date": "20260717",
    }
    commands: list[list[str]] = []
    resolver_calls: list[dict[str, object]] = []

    def fake_resolve_source_state(**kwargs: object) -> dict[str, object]:
        resolver_calls.append(kwargs)
        return dict(state)

    monkeypatch.setattr(
        replay,
        "resolve_daily_report_source_state",
        fake_resolve_source_state,
    )
    monkeypatch.setattr(replay, "create_stale_residue", lambda output_dir: stale_path)
    monkeypatch.setattr(
        replay,
        "add_clean_entrypoint_worktree",
        lambda *args, **kwargs: source_root,
    )
    monkeypatch.setattr(replay, "remove_clean_entrypoint_worktree", lambda *args: None)

    def fake_run_command(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
        commands.append(args)
        return subprocess.CompletedProcess(
            args=args,
            returncode=0,
            stdout="official ChatGPT-side daily PDF generation completed\n",
            stderr="",
        )

    monkeypatch.setattr(replay, "run_command", fake_run_command)

    replay.run_replay(
        tmp_path,
        "origin/main",
        tmp_path / "output",
        "20260717",
    )

    assert len(commands) == 1
    flag_index = commands[0].index("--validation-replay-main-price-date")
    assert commands[0][flag_index + 1] == "20260717"
    assert len(resolver_calls) == 2
    assert all(
        call["validation_replay_main_price_date"] == "20260717"
        for call in resolver_calls
    )


def test_run_replay_passes_committed_weekend_date_for_pinned_pr_source(
    tmp_path: Path,
    monkeypatch,
) -> None:
    source_root = tmp_path / "clean-source"
    source_root.mkdir()
    stale_path = tmp_path / replay.STALE_RESIDUE_NAME
    state = {
        "source_ref": "pinned-replay/workflow-29677505156-1",
        "source_commit_sha": "b" * 40,
        "market_session_status": "closed_scheduled",
        "expected_main_price_date": "20260717",
        "main_price_date": "20260717",
    }
    commands: list[list[str]] = []
    resolver_calls: list[dict[str, object]] = []

    monkeypatch.setattr(
        replay,
        "infer_committed_closed_scheduled_replay_date",
        lambda *args, **kwargs: "20260717",
    )

    def fake_resolve_source_state(**kwargs: object) -> dict[str, object]:
        resolver_calls.append(kwargs)
        return dict(state)

    monkeypatch.setattr(replay, "resolve_daily_report_source_state", fake_resolve_source_state)
    monkeypatch.setattr(replay, "create_stale_residue", lambda output_dir: stale_path)
    monkeypatch.setattr(replay, "add_clean_entrypoint_worktree", lambda *args, **kwargs: source_root)
    monkeypatch.setattr(replay, "remove_clean_entrypoint_worktree", lambda *args: None)

    def fake_run_command(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
        commands.append(args)
        return subprocess.CompletedProcess(
            args=args,
            returncode=0,
            stdout="official ChatGPT-side daily PDF generation completed\n",
            stderr="",
        )

    monkeypatch.setattr(replay, "run_command", fake_run_command)

    replay.run_replay(
        tmp_path,
        "pinned-replay/workflow-29677505156-1",
        tmp_path / "output",
    )

    flag_index = commands[0].index("--validation-replay-main-price-date")
    assert commands[0][flag_index + 1] == "20260717"
    assert all(
        call["validation_replay_main_price_date"] == "20260717"
        for call in resolver_calls
    )


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


def test_replay_runtime_manifest_requires_semantic_manifest_path(tmp_path: Path) -> None:
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
    manifest.pop("semantic_manifest_path")
    (tmp_path / RUNTIME_MANIFEST_NAME).write_text(json.dumps(manifest), encoding="utf-8")

    errors = validate_runtime_manifest(paths, tmp_path, state)

    assert any("semantic_manifest_path is missing" in error for error in errors)


def semantic_row(
    model_id: str,
    section: str,
    stock_id: str,
    *,
    pdf_role: str = "mainstream_highlight",
    main_price_date: str = "20260706",
    rendered_row_type: str = "data",
    empty_state_text: str = "",
) -> dict[str, str]:
    row_metric_status = (
        "not_applicable_empty_state"
        if rendered_row_type == "empty_state"
        else "unavailable_no_approved_add_score_metric"
    )
    return {
        "manifest_type": "chatgpt_daily_pdf_semantic_manifest",
        "main_price_date": main_price_date,
        "pdf_role": pdf_role,
        "pdf_view": "highlight",
        "report_line": "mainstream",
        "model_id": model_id,
        "pdf_section": section,
        "rendered_row_type": rendered_row_type,
        "rendered_order": "1",
        "stock_id": stock_id,
        "stock_name": stock_id,
        "pdf_path": "",
        "empty_state_text": empty_state_text,
        "operation_status": section,
        "row_action_status": "confirmed_buy_candidate" if section == "confirmed_operation" else "active_operation",
        "buy_rank_eligible": "True" if section == "confirmed_operation" else "False",
        "source_artifact": f"output/latest/daily_{model_id}_operation_section_latest.csv",
        "source_sha256": "a" * 64,
        "row_metric_status": row_metric_status,
        "row_metric_scope": "",
        "row_metric_id": "",
        "row_metric_label_zh": "",
        "row_metric_display_label_zh": "",
        "row_metric_sample_size": "",
        "row_metric_win_rate_zh": "",
        "row_metric_neutral_rate_zh": "",
        "row_metric_failure_rate_zh": "",
        "row_metric_avg_return_zh": "",
        "row_metric_selection_status": "",
        "row_metric_display_text": (
            "無核准加分績效"
            if rendered_row_type == "data" and section in {"confirmed_operation", "confirmed_unranked_operation"}
            else ""
        ),
    }


V2_LOW_VOLUME_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"


def test_semantic_manifest_schema_rejects_preview_source_artifact() -> None:
    row = semantic_row(V2_LOW_VOLUME_MODEL_ID, "confirmed_operation", "3055")
    row["source_artifact"] = "output/latest/volume_breakout_operation_pdf_preview_latest.csv"

    errors = validate_semantic_manifest_schema([row], "20260706")

    assert any("preview" in error for error in errors)


def test_semantic_manifest_schema_requires_ready_row_metric_display_to_match_payload() -> None:
    row = semantic_row(V2_LOW_VOLUME_MODEL_ID, "confirmed_operation", "3055")
    row.update(
        {
            "row_metric_status": "ready",
            "row_metric_scope": "single_add_score",
            "row_metric_id": "high_pos_base_plus_volume_lt2",
            "row_metric_label_zh": "量比 <= 2",
            "row_metric_display_label_zh": "量比 <= 2",
            "row_metric_sample_size": "31",
            "row_metric_win_rate_zh": "77.42%",
            "row_metric_neutral_rate_zh": "0.00%",
            "row_metric_failure_rate_zh": "22.58%",
            "row_metric_avg_return_zh": "+13.76%",
            "row_metric_selection_status": "single_add_score_metric",
            "row_metric_display_text": "錯誤地顯示基礎績效",
        }
    )

    errors = validate_semantic_manifest_schema([row], "20260706")

    assert any("row_metric_display_text does not match adapter payload" in error for error in errors)


def test_semantic_golden_cases_accept_known_20260706_accident_rows() -> None:
    rows = [
        semantic_row("w_bottom_right_side", "confirmed_operation", "6176"),
        semantic_row("w_bottom_right_side", "active_operation", "1618"),
        semantic_row("w_bottom_right_side", "active_operation", "3029"),
    ]
    case_ids = {
        "w_bottom_20260706_6176_confirmed_present",
        "w_bottom_20260706_1618_confirmed_absent",
        "w_bottom_20260706_1618_active_present",
        "w_bottom_20260706_3029_active_present",
        "w_bottom_20260706_6134_active_absent",
    }
    cases = [
        case
        for case in read_semantic_golden_cases(SEMANTIC_GOLDEN_CASES_CONTRACT)
        if case.get("case_id") in case_ids
    ]

    errors = validate_semantic_golden_cases(rows, "20260706", cases)

    assert errors == []


def test_semantic_golden_cases_reject_known_20260706_accident_drift() -> None:
    rows = [
        semantic_row("w_bottom_right_side", "confirmed_operation", "1618"),
        semantic_row("w_bottom_right_side", "active_operation", "1618"),
        semantic_row("w_bottom_right_side", "active_operation", "6134"),
    ]
    case_ids = {
        "w_bottom_20260706_6176_confirmed_present",
        "w_bottom_20260706_1618_confirmed_absent",
        "w_bottom_20260706_1618_active_present",
        "w_bottom_20260706_3029_active_present",
        "w_bottom_20260706_6134_active_absent",
    }
    cases = [
        case
        for case in read_semantic_golden_cases(SEMANTIC_GOLDEN_CASES_CONTRACT)
        if case.get("case_id") in case_ids
    ]

    errors = validate_semantic_golden_cases(rows, "20260706", cases)

    assert any("w_bottom_20260706_6176_confirmed_present" in error for error in errors)
    assert any("w_bottom_20260706_1618_confirmed_absent" in error for error in errors)
    assert any("w_bottom_20260706_3029_active_present" in error for error in errors)
    assert any("w_bottom_20260706_6134_active_absent" in error for error in errors)


def test_semantic_golden_cases_support_count_equals() -> None:
    rows = [
        semantic_row(V2_LOW_VOLUME_MODEL_ID, "confirmed_operation", "3055"),
        semantic_row(V2_LOW_VOLUME_MODEL_ID, "confirmed_operation", "4989"),
    ]
    cases = [
        {
            "case_id": "volume_confirmed_count",
            "active": "True",
            "report_date": "20260706",
            "pdf_role": "mainstream_highlight",
            "model_id": V2_LOW_VOLUME_MODEL_ID,
            "pdf_section": "confirmed_operation",
            "rendered_row_type": "data",
            "expectation": "count_equals",
            "expected_count": "2",
        }
    ]

    errors = validate_semantic_golden_cases(rows, "20260706", cases)

    assert errors == []


def test_semantic_golden_cases_count_equals_rejects_duplicate_stock() -> None:
    rows = [
        semantic_row("price_pullback_23ema", "confirmed_operation", "1802"),
        semantic_row("price_pullback_23ema", "confirmed_operation", "1802"),
    ]
    cases = [
        {
            "case_id": "price_pullback_1802_once",
            "active": "True",
            "report_date": "20260706",
            "pdf_role": "mainstream_highlight",
            "model_id": "price_pullback_23ema",
            "pdf_section": "confirmed_operation",
            "rendered_row_type": "data",
            "stock_id": "1802",
            "expectation": "count_equals",
            "expected_count": "1",
        }
    ]

    errors = validate_semantic_golden_cases(rows, "20260706", cases)

    assert any("price_pullback_1802_once" in error for error in errors)


def test_semantic_golden_cases_support_empty_state_rows() -> None:
    rows = [
        semantic_row(
            "neckline_volume_breakout_confirmation",
            "confirmed_operation",
            "",
            rendered_row_type="empty_state",
            empty_state_text="本日無股票推薦",
        )
    ]
    cases = [
        {
            "case_id": "neckline_empty_confirmed",
            "active": "True",
            "report_date": "20260706",
            "pdf_role": "mainstream_highlight",
            "model_id": "neckline_volume_breakout_confirmation",
            "pdf_section": "confirmed_operation",
            "rendered_row_type": "empty_state",
            "empty_state_text": "本日無股票推薦",
            "expectation": "present",
        }
    ]

    errors = validate_semantic_golden_cases(rows, "20260706", cases)

    assert errors == []


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
    full_required_text = "\n".join(HIGHLIGHT_FULL_TEXT_REQUIRED_TEXT)
    pages = {
        "mainstream_highlight": [f"mainstream highlight\n{required_text}", f"other content\n{full_required_text}"],
        "non_mainstream_highlight": [f"non-mainstream highlight\n{required_text}", f"other content\n{full_required_text}"],
    }

    assert validate_highlight_layout_texts(pages) == []

def test_replay_highlight_layout_allows_active_table_after_first_page() -> None:
    first_page_text = "\n".join(HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT)
    active_text = "\n".join(HIGHLIGHT_FULL_TEXT_REQUIRED_TEXT)
    pages = {
        "mainstream_highlight": [first_page_text, active_text],
        "non_mainstream_highlight": [first_page_text, active_text],
    }

    assert validate_highlight_layout_texts(pages) == []

def test_replay_highlight_layout_roles_are_machine_readable() -> None:
    assert HIGHLIGHT_LAYOUT_ROLES == ("mainstream_highlight", "non_mainstream_highlight")

def test_replay_highlight_layout_contract_rejects_reordered_first_page() -> None:
    required_text = "\n".join(HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT)
    full_required_text = "\n".join(HIGHLIGHT_FULL_TEXT_REQUIRED_TEXT)
    pages = {
        "mainstream_highlight": [HIGHLIGHT_STOCK_MODEL_SECTION_TEXT, f"{required_text}\n{full_required_text}"],
        "non_mainstream_highlight": [f"non-mainstream highlight\n{required_text}\n{full_required_text}"],
    }

    errors = validate_highlight_layout_texts(pages)

    assert any("first page missing required layout text" in error for error in errors)
    assert any("must not start with stock-model tables" in error for error in errors)

def test_replay_highlight_layout_contract_rejects_pending_operation_text() -> None:
    required_text = "\n".join(HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT)
    full_required_text = "\n".join(HIGHLIGHT_FULL_TEXT_REQUIRED_TEXT)
    forbidden_text = HIGHLIGHT_FULL_TEXT_FORBIDDEN_TEXT[0]
    pages = {
        "mainstream_highlight": [f"mainstream highlight\n{required_text}\n{full_required_text}\n{forbidden_text}"],
        "non_mainstream_highlight": [f"non-mainstream highlight\n{required_text}\n{full_required_text}"],
    }

    errors = validate_highlight_layout_texts(pages)

    assert any(f"forbidden operation-layer text: {forbidden_text}" in error for error in errors)

def test_replay_highlight_layout_contract_rejects_missing_active_table_text() -> None:
    required_text = "\n".join(HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT)
    pages = {
        "mainstream_highlight": [f"mainstream highlight\n{required_text}"],
        "non_mainstream_highlight": [f"non-mainstream highlight\n{required_text}"],
    }

    errors = validate_highlight_layout_texts(pages)

    assert any("full text missing required layout text" in error for error in errors)

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


def test_rendered_model_regression_contract_checks_formal_exit_rule_text_tokens() -> None:
    rows = [
        {
            "contract_id": "w_bottom_right_side_exit_rule_text",
            "active": "True",
            "report_date": "*",
            "pdf_role": "mainstream_highlight",
            "page_scope": "all_pages",
            "model_id": "w_bottom_right_side",
            "required_text_tokens": (
                "W底右側模型|若 D+20 收盤報酬達 +10%|D+20 收盤出場|"
                "D+40 收盤|W 結構低點收盤停損"
            ),
        },
        {
            "contract_id": "neckline_volume_breakout_confirmation_exit_rule_text",
            "active": "True",
            "report_date": "*",
            "pdf_role": "mainstream_highlight",
            "page_scope": "all_pages",
            "model_id": "neckline_volume_breakout_confirmation",
            "required_text_tokens": (
                "W底頸線帶量突破確認模型|20 個交易日內收盤報酬先達 +10%|"
                "先達 +5% 後回落到 <= +5%|否則第 20 日收盤歸為操作規則敗"
            ),
        },
    ]
    role_to_pages = {
        "mainstream_highlight": [
            (
                "W底右側模型\n"
                "賣出：若 D+20 收盤報酬達 +10% 則 D+20 收盤出場；"
                "否則持有到 D+40 收盤，除非先觸發 W 結構低點收盤停損。\n"
                "W底頸線帶量突破確認模型\n"
                "賣出：20 個交易日內收盤報酬先達 +10% 為勝；"
                "先達 +5% 後回落到 <= +5% 且未達 +10% 為和局；"
                "否則第 20 日收盤歸為操作規則敗。"
            )
        ]
    }

    assert validate_rendered_model_regression_texts(role_to_pages, "20260706", rows) == []

    role_to_pages["mainstream_highlight"][0] = (
        "W底右側模型\n"
        "賣出：若 D+20 收盤報酬達 +10% 則 D+20 收盤出場；"
        "W底頸線帶量突破確認模型\n"
        "賣出：20 個交易日內收盤報酬先達 +10% 為勝；"
        "先達 +5% 後回落到 <= +5% 且未達 +10% 為和局；"
        "否則第 20 日收盤歸為操作規則敗。"
    )

    errors = validate_rendered_model_regression_texts(role_to_pages, "20260706", rows)

    assert any("required text token='D+40 收盤' missing" in error for error in errors)
    assert any("required text token='W 結構低點收盤停損' missing" in error for error in errors)


def test_rendered_model_regression_contract_records_formal_operation_models() -> None:
    rows = read_rendered_model_regression_contract(RENDERED_MODEL_REGRESSION_CONTRACT)
    row_by_id = {row["contract_id"]: row for row in rows}
    sampling_sentence = "取樣：已確認欄位股票精華版全部列出，操作中欄位股票精華版最多列出十檔股票。"

    required_contracts = {
        "volume_range_breakout_v2_low_position_mainstream_highlight_structure",
        "volume_range_breakout_v2_low_position_non_mainstream_highlight_structure",
        "volume_range_breakout_v2_mid_position_mainstream_highlight_structure",
        "volume_range_breakout_v2_mid_position_non_mainstream_highlight_structure",
        "volume_range_breakout_v2_high_position_mainstream_highlight_structure",
        "volume_range_breakout_v2_high_position_non_mainstream_highlight_structure",
        "w_bottom_right_side_mainstream_highlight_structure",
        "w_bottom_right_side_non_mainstream_highlight_structure",
        "w_bottom_right_side_mainstream_highlight_confirmed_table_20260703",
        "w_bottom_right_side_mainstream_highlight_active_table_20260703",
        "w_bottom_right_side_mainstream_highlight_active_table_20260706",
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
    assert row_by_id["w_bottom_right_side_mainstream_highlight_active_table_20260703"]["required_stock_ids"]
    assert (
        row_by_id["w_bottom_right_side_mainstream_highlight_active_table_20260706"]["required_stock_ids"]
        == "3029"
    )
    for contract_id in (
        "volume_range_breakout_v2_low_position_mainstream_highlight_structure",
        "volume_range_breakout_v2_low_position_non_mainstream_highlight_structure",
        "volume_range_breakout_v2_mid_position_mainstream_highlight_structure",
        "volume_range_breakout_v2_mid_position_non_mainstream_highlight_structure",
        "volume_range_breakout_v2_high_position_mainstream_highlight_structure",
        "volume_range_breakout_v2_high_position_non_mainstream_highlight_structure",
        "w_bottom_right_side_mainstream_highlight_structure",
        "w_bottom_right_side_non_mainstream_highlight_structure",
        "neckline_volume_breakout_confirmation_mainstream_highlight_structure",
        "neckline_volume_breakout_confirmation_non_mainstream_highlight_structure",
        "price_pullback_23ema_mainstream_highlight_structure",
        "price_pullback_23ema_non_mainstream_highlight_structure",
    ):
        assert sampling_sentence in row_by_id[contract_id]["required_text_tokens"]
    assert row_by_id[
        "neckline_volume_breakout_confirmation_mainstream_highlight_active_empty_table_20260703"
    ]["required_text_tokens"]
    w_bottom_exit_tokens = (
        "若 D+20 收盤報酬達 +10%",
        "D+20 收盤出場",
        "D+40 收盤",
        "W 結構低點收盤停損",
    )
    for contract_id in (
        "w_bottom_right_side_mainstream_highlight_structure",
        "w_bottom_right_side_non_mainstream_highlight_structure",
    ):
        required_text_tokens = row_by_id[contract_id]["required_text_tokens"]
        for token in w_bottom_exit_tokens:
            assert token in required_text_tokens
    for contract_id in (
        "w_bottom_right_side_mainstream_highlight_active_table_20260703",
        "w_bottom_right_side_mainstream_highlight_active_table_20260706",
        "w_bottom_right_side_non_mainstream_highlight_active_table_20260703",
    ):
        required_text_tokens = row_by_id[contract_id]["required_text_tokens"]
        assert "D+20" in required_text_tokens
        assert "+10%" in required_text_tokens
        assert "D+40" in required_text_tokens
    neckline_exit_tokens = (
        "20 個交易日內收盤報酬先達 +10%",
        "先達 +5% 後回落到 <= +5%",
        "否則第 20 日收盤歸為操作規則敗",
    )
    for contract_id in (
        "neckline_volume_breakout_confirmation_mainstream_highlight_structure",
        "neckline_volume_breakout_confirmation_non_mainstream_highlight_structure",
    ):
        required_text_tokens = row_by_id[contract_id]["required_text_tokens"]
        for token in neckline_exit_tokens:
            assert token in required_text_tokens
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


def test_pdf_replay_stays_in_pr_validation_not_daily_full_runtime() -> None:
    daily_workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8",
        errors="replace",
    )
    pr_workflow = (
        ROOT / ".github" / "workflows" / "daily_pdf_replay_pr_validation.yml"
    ).read_text(
        encoding="utf-8",
        errors="replace",
    )

    assert "daily-pdf-dfkai-replay:" not in daily_workflow
    assert "Replay ChatGPT-side daily PDF new conversation" not in daily_workflow
    assert "chatgpt_side_outputs_new_conversation_replay" not in daily_workflow

    assert "daily-pdf-dfkai-replay:" in pr_workflow
    assert "Replay ChatGPT-side daily PDF new conversation" in pr_workflow
    assert "python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in pr_workflow
    assert "timeout-minutes: 20" in pr_workflow
    assert "timeout 20m python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in pr_workflow
    assert "PDF replay output_dir=chatgpt_side_outputs_pr_validation" in pr_workflow
    assert "--output-dir chatgpt_side_outputs_pr_validation" in pr_workflow
