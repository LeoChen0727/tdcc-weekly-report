from __future__ import annotations

from pathlib import Path
import json

from scripts.validate_chatgpt_daily_report_new_conversation_replay import (
    EXPECTED_TITLES,
    RUNTIME_MANIFEST_NAME,
    pdf_paths_from_stdout,
    validate_runtime_manifest,
    validate_pdf_path_contract,
    validate_source_gate_echo,
)


ROOT = Path(__file__).resolve().parents[1]


def pdf_name(date: str, title: str) -> str:
    return f"{date}_requested_repo{date}_{title}_current_rules.pdf"


def test_replay_stdout_pdf_parser_deduplicates_entrypoint_output(tmp_path: Path) -> None:
    paths = [tmp_path / pdf_name("20260617", title) for title in EXPECTED_TITLES]
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
    paths = [tmp_path / pdf_name("20260617", title) for title in EXPECTED_TITLES]

    errors = validate_pdf_path_contract(paths, tmp_path, "20260617")

    assert errors == []


def test_replay_pdf_path_contract_rejects_stale_or_missing_pdf_titles(tmp_path: Path) -> None:
    paths = [
        tmp_path / pdf_name("20260617", EXPECTED_TITLES[0]),
        tmp_path / pdf_name("20260617", EXPECTED_TITLES[1]),
        tmp_path / pdf_name("20260617", EXPECTED_TITLES[2]),
        tmp_path / pdf_name("20260617", EXPECTED_TITLES[3]),
        tmp_path / pdf_name("20260617", EXPECTED_TITLES[4]),
        tmp_path / pdf_name("20260612", EXPECTED_TITLES[5]),
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
    paths = [tmp_path / pdf_name("20260617", title) for title in EXPECTED_TITLES]
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "main_price_date": "20260617",
        "freshness_path": "origin/main:output/latest/data_freshness_latest.csv",
        "readme_path": "origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "packet_path": "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt",
    }
    (tmp_path / RUNTIME_MANIFEST_NAME).write_text(
        json.dumps(
            {
                "manifest_type": "chatgpt_daily_report_runtime_manifest",
                "source_ref": "origin/main",
                "source_commit_sha": "a" * 40,
                "clean_source_commit_sha": "a" * 40,
                "main_price_date": "20260617",
                "freshness_path": state["freshness_path"],
                "readme_path": state["readme_path"],
                "packet_path": state["packet_path"],
                "pdf_count": 6,
                "output_dir": str(tmp_path),
                "pdf_paths": [str(path) for path in paths],
            }
        ),
        encoding="utf-8",
    )

    errors = validate_runtime_manifest(paths, tmp_path, state)

    assert errors == []


def test_replay_runtime_manifest_rejects_wrong_date(tmp_path: Path) -> None:
    paths = [tmp_path / pdf_name("20260617", title) for title in EXPECTED_TITLES]
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "main_price_date": "20260617",
        "freshness_path": "origin/main:output/latest/data_freshness_latest.csv",
        "readme_path": "origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "packet_path": "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt",
    }
    (tmp_path / RUNTIME_MANIFEST_NAME).write_text(
        json.dumps(
            {
                "manifest_type": "chatgpt_daily_report_runtime_manifest",
                "source_ref": "origin/main",
                "source_commit_sha": "a" * 40,
                "clean_source_commit_sha": "a" * 40,
                "main_price_date": "20260612",
                "freshness_path": state["freshness_path"],
                "readme_path": state["readme_path"],
                "packet_path": state["packet_path"],
                "pdf_count": 6,
                "output_dir": str(tmp_path),
                "pdf_paths": [str(path) for path in paths],
            }
        ),
        encoding="utf-8",
    )

    errors = validate_runtime_manifest(paths, tmp_path, state)

    assert any("main_price_date" in error for error in errors)


def test_daily_workflow_runs_new_conversation_replay_gate() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8",
        errors="replace",
    )

    assert "Replay ChatGPT-side daily PDF new conversation" in workflow
    assert "python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in workflow
    assert "--output-dir chatgpt_side_outputs_new_conversation_replay" in workflow
