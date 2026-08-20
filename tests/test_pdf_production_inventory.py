from __future__ import annotations

import json
from pathlib import Path

import pytest

import ensure_report_aliases
from scripts import validate_pdf_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]


def _patch_runtime_inventory_paths(monkeypatch, tmp_path: Path) -> None:
    output_latest = tmp_path / "output" / "latest"
    docs_latest = tmp_path / "docs" / "latest"
    history_reports = tmp_path / "output" / "history" / "reports"
    output_latest.mkdir(parents=True)
    docs_latest.mkdir(parents=True)
    history_reports.mkdir(parents=True)

    monkeypatch.setattr(inventory, "ROOT", tmp_path)
    monkeypatch.setattr(inventory, "OUTPUT_LATEST", output_latest)
    monkeypatch.setattr(inventory, "DOCS_LATEST", docs_latest)
    monkeypatch.setattr(inventory, "HISTORY_REPORTS", history_reports)
    monkeypatch.setattr(inventory, "DATA_FRESHNESS", output_latest / "data_freshness_latest.csv")
    monkeypatch.setattr(
        inventory,
        "REPORT_MANIFEST_JSON",
        output_latest / "report_manifest_latest.json",
    )
    monkeypatch.setattr(
        inventory,
        "REPORT_MANIFEST_MD",
        output_latest / "report_manifest_latest.md",
    )
    monkeypatch.setattr(
        inventory,
        "DAILY_MARKET_COMPATIBILITY_ALIAS_PATHS",
        (
            output_latest / "daily_market_summary_latest.pdf",
            output_latest / "daily_market_full_latest.pdf",
        ),
    )
    monkeypatch.setattr(inventory, "LEGACY_ROOT_DAILY_MARKET_PDF_PATHS", ())
    monkeypatch.setattr(inventory, "STATIC_PUBLIC_SURFACES", ())
    monkeypatch.setattr(inventory, "RUNTIME_PUBLIC_SURFACES", ())
    for function_name in (
        "validate_inventory_document",
        "validate_paths_exist",
        "validate_daily_history_producer_contract",
        "validate_workflow_hooks",
    ):
        monkeypatch.setattr(inventory, function_name, lambda errors: None)


def _write_complete_runtime_inventory(main_date: str) -> None:
    inventory.DATA_FRESHNESS.write_text(
        f"main_price_date\n{main_date}\n",
        encoding="utf-8",
    )
    for path in inventory.DAILY_MARKET_COMPATIBILITY_ALIAS_PATHS:
        path.write_bytes(b"pdf")
    for path in inventory.daily_market_published_pdf_paths(main_date):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"pdf")

    expected = inventory.daily_market_canonical_history_paths(main_date)
    for path in expected.values():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"pdf" if path.suffix == ".pdf" else b"markdown")

    expected_rel = {field: path.relative_to(inventory.ROOT).as_posix() for field, path in expected.items()}
    manifest = {
        "main_price_date": main_date,
        "history_path_contract": "canonical_daily_market_history_only",
        **expected_rel,
        "history_summary_alias_md": expected_rel["history_summary_md"],
        "history_summary_alias_pdf": expected_rel["history_summary_pdf"],
        "history_full_alias_md": expected_rel["history_full_md"],
        "history_full_alias_pdf": expected_rel["history_full_pdf"],
    }
    for field, source_field in (
        ("history_summary_alias_md_raw_url", "history_summary_md"),
        ("history_summary_alias_pdf_raw_url", "history_summary_pdf"),
        ("history_full_alias_md_raw_url", "history_full_md"),
        ("history_full_alias_pdf_raw_url", "history_full_pdf"),
        ("summary_md_raw_url", "history_summary_md"),
        ("summary_pdf_raw_url", "history_summary_pdf"),
        ("full_md_raw_url", "history_full_md"),
        ("full_pdf_raw_url", "history_full_pdf"),
    ):
        manifest[field] = f"https://example.invalid/{expected_rel[source_field]}"
    inventory.REPORT_MANIFEST_JSON.write_text(
        json.dumps(manifest, ensure_ascii=False),
        encoding="utf-8",
    )
    inventory.REPORT_MANIFEST_MD.write_text(
        "\n".join(expected_rel.values()),
        encoding="utf-8",
    )


def test_pdf_production_inventory_prebuild_validator_passes() -> None:
    assert inventory.main(["--phase", "prebuild"]) == 0


def test_prebuild_allows_old_runtime_but_full_requires_completed_new_artifacts(
    monkeypatch, tmp_path: Path
) -> None:
    _patch_runtime_inventory_paths(monkeypatch, tmp_path)
    _write_complete_runtime_inventory("20260730")
    inventory.DATA_FRESHNESS.write_text(
        "main_price_date\n20260731\n",
        encoding="utf-8",
    )

    assert inventory.validate(inventory.VALIDATION_PHASE_PREBUILD) == []
    old_runtime_errors = inventory.validate()
    assert any("published daily market PDF missing" in error for error in old_runtime_errors)
    assert any("history_summary_md must equal canonical path" in error for error in old_runtime_errors)

    _write_complete_runtime_inventory("20260731")

    assert inventory.validate() == []


def test_pdf_production_inventory_cli_defaults_to_full(monkeypatch) -> None:
    observed_phases: list[str] = []

    def fake_validate(phase: str = inventory.VALIDATION_PHASE_FULL) -> list[str]:
        observed_phases.append(phase)
        return []

    monkeypatch.setattr(inventory, "validate", fake_validate)

    assert inventory.main([]) == 0
    assert observed_phases == [inventory.VALIDATION_PHASE_FULL]


def test_inventory_tracks_every_pdf_purpose() -> None:
    purposes = {producer.purpose for producer in inventory.PDF_PRODUCERS}

    assert purposes == {
        "ChatGPT-side daily",
        "Daily repo market source artifact",
        "TDCC weekly",
        "Market risk/background",
        "Warrant market auxiliary",
        "Daily signal performance reports",
        "Individual stock report",
    }


def test_daily_market_repo_artifact_lifecycle_is_explicit() -> None:
    lifecycle = inventory.DAILY_MARKET_REPO_ARTIFACT_LIFECYCLE
    paths = {path for path, _role, _status in lifecycle}

    assert paths == {
        "output/latest/daily_market_summary_latest.pdf",
        "output/latest/daily_market_full_latest.pdf",
        "output/latest/published_reports/daily_market/每日全市場候選股監測報告_精華版_YYYYMMDD.pdf",
        "output/latest/published_reports/daily_market/完整候選股清單_完整版_YYYYMMDD.pdf",
        "output/history/reports/YYYYMMDD_daily_market_summary.pdf",
        "output/history/reports/YYYYMMDD_daily_market_full.pdf",
    }
    assert inventory.REPO_ARTIFACT_DAILY_PDF_NAMES == tuple(
        Path(path).name for path, _role, _status in lifecycle
    )

    inventory_doc = (ROOT / "docs" / "pdf_production_inventory.md").read_text(
        encoding="utf-8"
    )
    lineage = (ROOT / "config" / "report_artifact_lineage.csv").read_text(
        encoding="utf-8-sig"
    )
    for path, role, status in lifecycle:
        assert path in inventory_doc
        assert role in inventory_doc
        assert status in inventory_doc
        assert path in lineage
    for path in inventory.LEGACY_ROOT_DAILY_MARKET_PDF_PATHS:
        rel = path.relative_to(ROOT).as_posix()
        assert rel not in lineage


def test_docs_latest_root_pdfs_are_classified() -> None:
    docs_latest = ROOT / "docs" / "latest"
    for path in docs_latest.glob("*.pdf"):
        assert path.name in inventory.ALLOWED_DOCS_LATEST_ROOT_PDF_NAMES
        assert path.name not in inventory.FORBIDDEN_DOCS_LATEST_PDF_NAMES


def test_retired_daily_pdf_paths_are_not_in_public_surfaces() -> None:
    for path in inventory.PUBLIC_SURFACES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for name in inventory.RETIRED_FIXED_DAILY_PDF_NAMES:
            assert name not in text, f"{path.relative_to(ROOT).as_posix()} exposes {name}"


def test_daily_workflow_uses_prebuild_once_and_keeps_two_full_validations() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    commands = [line.strip() for line in workflow.splitlines()]

    assert commands.count(
        "python scripts/validate_pdf_production_inventory.py --phase prebuild"
    ) == 1
    assert commands.count("python scripts/validate_pdf_production_inventory.py") >= 2

    prebuild_start = workflow.index(f"      - name: {inventory.PDF_PREBUILD_STEP_NAME}")
    prebuild_end = workflow.index("\n      - name:", prebuild_start + 1)
    assert workflow[prebuild_start:prebuild_end].rstrip() == inventory.PDF_PREBUILD_STEP

    build_index = workflow.index("- name: Build daily market report artifacts")
    post_build_full_index = workflow.index(
        "python scripts/validate_pdf_production_inventory.py",
        build_index,
    )
    publish_index = workflow.index(
        "- name: Publish readme and multi-entry URL check",
        post_build_full_index,
    )
    post_publish_full_index = workflow.index(
        "python scripts/validate_pdf_production_inventory.py",
        publish_index,
    )
    assert build_index < post_build_full_index < publish_index < post_publish_full_index


@pytest.mark.parametrize(
    "removed_command",
    (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_hidden_coupling_audit.py",
        "python scripts/validate_daily_model_background_data_registry.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_repo_code_isolation_policy.py",
        "python scripts/validate_model_research_workflow_isolation.py",
        "python scripts/validate_chatgpt_side_pdf_layout_independence.py",
        "python scripts/validate_daily_pdf_role_manifest_contract.py",
    ),
)
def test_daily_workflow_rejects_repo_static_command_in_pdf_prebuild_step(
    removed_command: str,
    monkeypatch,
) -> None:
    workflow = inventory.DAILY_WORKFLOW.read_text(encoding="utf-8")
    mutated = workflow.replace(
        inventory.PDF_PREBUILD_STEP,
        f"{inventory.PDF_PREBUILD_STEP}\n          {removed_command}",
        1,
    )
    original_read_text = inventory.read_text

    def read_mutated(path: Path) -> str:
        if path == inventory.DAILY_WORKFLOW:
            return mutated
        return original_read_text(path)

    monkeypatch.setattr(inventory, "read_text", read_mutated)
    errors: list[str] = []
    inventory.validate_workflow_hooks(errors)

    assert "Daily Full Pipeline PDF prebuild step must contain only the exact prebuild command" in errors


def test_daily_workflow_cleans_stale_readmes_before_pdf_inventory_validation() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    alias_step = workflow.index("python ensure_report_aliases.py")
    contract_validation = workflow.index(
        "python scripts/validate_pdf_production_inventory.py",
        alias_step,
    )

    assert alias_step < contract_validation


def test_daily_workflow_stages_readme_deletions_with_git_pathspecs() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert 'git add -A -- "output/latest/READ_ME_FIRST_DAILY_REPORT*.txt"' in workflow
    assert workflow.count('git add -A -- "docs/latest/READ_ME_FIRST_DAILY_REPORT*.txt"') >= 2
    assert "git add output/latest/READ_ME_FIRST_DAILY_REPORT*.txt" not in workflow
    assert "git add docs/latest/READ_ME_FIRST_DAILY_REPORT*.txt" not in workflow


def test_report_aliases_remove_stale_date_stamped_readmes(tmp_path: Path) -> None:
    current = tmp_path / "READ_ME_FIRST_DAILY_REPORT_20260617.txt"
    stale = tmp_path / "READ_ME_FIRST_DAILY_REPORT_20260616.txt"
    index = tmp_path / "READ_ME_FIRST_DAILY_REPORT_INDEX.txt"
    current.write_text("current", encoding="utf-8")
    stale.write_text("stale", encoding="utf-8")
    index.write_text("index", encoding="utf-8")

    ensure_report_aliases.remove_stale_date_stamped_readmes(tmp_path, "20260617")

    assert current.exists()
    assert not stale.exists()
    assert index.exists()


def test_report_aliases_do_not_fall_back_to_wall_clock_date() -> None:
    text = (ROOT / "ensure_report_aliases.py").read_text(encoding="utf-8")
    start = text.index("def detect_main_date(")
    end = text.index("\n\nDATE_STAMPED_README_RE", start)
    body = text[start:end]

    assert 'datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")' not in body
    assert "wall-clock date fallback is forbidden" in text


def test_daily_history_producers_use_only_canonical_history_names() -> None:
    for path in inventory.HISTORY_PRODUCER_PATHS:
        source = path.read_text(encoding="utf-8")
        for literal in inventory.LEGACY_HISTORY_REFERENCE_FRAGMENTS:
            assert f'{{main_date}}{literal}' not in source
        assert "{main_date}_daily_market_summary.pdf" in source
        assert "{main_date}_daily_market_full.pdf" in source


def test_report_aliases_rewrite_manifest_to_canonical_history_paths(
    monkeypatch, tmp_path: Path
) -> None:
    monkeypatch.chdir(tmp_path)
    latest = Path("output/latest")
    history = Path("output/history/reports")
    published = latest / "published_reports" / "daily_market"
    latest.mkdir(parents=True)
    history.mkdir(parents=True)
    published.mkdir(parents=True)

    main_date = "20260717"
    (latest / "data_freshness_latest.csv").write_text(
        f"main_price_date,report_ready\n{main_date},True\n",
        encoding="utf-8",
    )
    (latest / "每日全市場候選股監測報告_精華版.md").write_text(
        "summary", encoding="utf-8"
    )
    (latest / "完整候選股清單_完整版.md").write_text("full", encoding="utf-8")
    (published / f"每日全市場候選股監測報告_精華版_{main_date}.pdf").write_bytes(
        b"summary-pdf"
    )
    (published / f"完整候選股清單_完整版_{main_date}.pdf").write_bytes(b"full-pdf")

    legacy_summary = (
        f"output/history/reports/{main_date}_每日全市場候選股監測報告_精華版.pdf"
    )
    legacy_full = f"output/history/reports/{main_date}_完整候選股清單_完整版表格.pdf"
    (latest / "report_manifest_latest.json").write_text(
        json.dumps(
            {
                "main_price_date": main_date,
                "history_summary_pdf": legacy_summary,
                "history_full_pdf": legacy_full,
                "recommended_read_order": [legacy_summary, legacy_full],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (latest / "report_manifest_latest.md").write_text(
        "# Daily manifest\n\n"
        "5. 日期版英文 MD / PDF\n"
        "6. 中文檔名僅作人類閱讀備援\n\n"
        "## 英文 alias raw URLs\n\n"
        f"- history summary pdf: {legacy_summary}\n"
        f"- history full pdf: {legacy_full}\n",
        encoding="utf-8",
    )

    assert ensure_report_aliases.main() == 0

    manifest = json.loads((latest / "report_manifest_latest.json").read_text(encoding="utf-8"))
    expected_summary = f"output/history/reports/{main_date}_daily_market_summary.pdf"
    expected_full = f"output/history/reports/{main_date}_daily_market_full.pdf"
    assert manifest["history_path_contract"] == "canonical_daily_market_history_only"
    assert manifest["history_summary_pdf"] == expected_summary
    assert manifest["history_summary_alias_pdf"] == expected_summary
    assert manifest["history_full_pdf"] == expected_full
    assert manifest["history_full_alias_pdf"] == expected_full
    assert not ensure_report_aliases.contains_legacy_history_reference(
        json.dumps(manifest, ensure_ascii=False)
    )
    manifest_md = (latest / "report_manifest_latest.md").read_text(encoding="utf-8")
    assert expected_summary in manifest_md
    assert expected_full in manifest_md
    assert "5. canonical history MD / PDF" in manifest_md
    assert "6. 中文 PDF 檔名僅保留於 published human-delivery surface" in manifest_md
    assert not ensure_report_aliases.contains_legacy_history_reference(manifest_md)
    assert (history / f"{main_date}_daily_market_summary.pdf").read_bytes() == b"summary-pdf"
    assert (history / f"{main_date}_daily_market_full.pdf").read_bytes() == b"full-pdf"
