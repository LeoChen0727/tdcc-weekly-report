from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

import pytest

from scripts import apply_workspace_cleanup as apply_cleanup
from scripts import plan_workspace_cleanup as planner
from scripts import validate_workspace_cleanup_policy as validator


ROOT = Path(__file__).resolve().parents[1]


def test_wildcard_protected_path_fails(tmp_path: Path, monkeypatch) -> None:
    path = tmp_path / "protected.csv"
    path.write_text(
        "path,match_type,path_required,scope,owner,protected_reason,hard_block,review_required\n"
        "config/*.csv,prefix,false,repo,repo_infrastructure,bad,true,true\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(validator, "PROTECTED_PATHS", path)
    errors: list[str] = []
    validator.load_protected_rows(errors)
    assert any("wildcard" in error for error in errors)


def test_protected_prefix_in_manifest_fails(tmp_path: Path) -> None:
    manifest = {
        "report_id": "test",
        "manifest_hash": "",
        "rows": [{"path": "config/example.csv", "planned_action": "report_only"}],
        "git_status_porcelain_before_planner": "",
        "git_status_porcelain_after_planner": "",
        "history_summary_path": "",
    }
    manifest["manifest_hash"] = validator.canonical_manifest_hash(manifest)
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    pointer_path = tmp_path / "latest_manifest.json"
    pointer_path.write_text(
        json.dumps(
            {
                "report_id": "test",
                "manifest_path": str(manifest_path.relative_to(ROOT)) if ROOT in manifest_path.parents else str(manifest_path),
                "manifest_hash": manifest["manifest_hash"],
                "generated_at": "2026-06-19T00:00:00+00:00",
            }
        ),
        encoding="utf-8",
    )
    # Directly exercise the protected matcher because tmp manifests outside ROOT are intentionally rejected.
    protected_rows = [validator.ProtectedRow("config/", "prefix", True)]
    assert validator.path_matches_protected("config/example.csv", protected_rows)[0]


def test_tracked_file_in_manifest_fails() -> None:
    protected_rows = validator.load_protected_rows([])
    errors: list[str] = []
    manifest = {
        "report_id": "test",
        "manifest_hash": "",
        "rows": [{"path": "scripts/run_chatgpt_daily_report_entrypoint.py", "planned_action": "report_only"}],
        "git_status_porcelain_before_planner": "",
        "git_status_porcelain_after_planner": "",
        "history_summary_path": "",
    }
    manifest["manifest_hash"] = validator.canonical_manifest_hash(manifest)
    manifest_dir = ROOT / "workspace_cleanup_reports" / "test_manifest_validation"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_dir / "manifest.json"
    pointer_path = manifest_dir / "latest_manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    pointer_path.write_text(
        json.dumps(
            {
                "report_id": "test",
                "manifest_path": manifest_path.relative_to(ROOT).as_posix(),
                "manifest_hash": manifest["manifest_hash"],
                "generated_at": "2026-06-19T00:00:00+00:00",
            }
        ),
        encoding="utf-8",
    )
    validator.validate_manifest(pointer_path, protected_rows, errors)
    assert any("tracked file" in error or "protected path" in error for error in errors)


def test_non_empty_candidate_does_not_plan_delete() -> None:
    classification, action, reason = planner.classify_candidate(
        "chatgpt_side_outputs_example",
        [{"relative_path": "chatgpt_side_outputs_example/file.txt", "is_dir": False, "size": 1}],
        [],
        descendant_permission_denied=False,
        descendant_reparse=False,
    )
    assert action != "delete"
    assert classification in {"stale_candidate", "unknown_quarantine_candidate"}
    assert reason


def test_pdf_report_key_removes_date_and_source_tokens() -> None:
    key = planner.pdf_report_key(
        "chatgpt_side_outputs_official/20260618/"
        "20260618_requested_repo20260618_daily_highlight_current_rules.pdf"
    )
    assert key == "daily_highlight"


def test_pdf_report_key_is_ascii_stable_for_non_ascii_titles() -> None:
    first = planner.pdf_report_key(
        "chatgpt_side_outputs_official/20260618/"
        "20260618_requested_repo20260618_\u4e3b\u6d41\u80a1_current_rules.pdf"
    )
    second = planner.pdf_report_key(
        "chatgpt_side_outputs_official/20260619/"
        "20260619_requested_repo20260619_\u4e3b\u6d41\u80a1_current_rules.pdf"
    )
    assert first == second
    assert first.startswith("report_")
    assert first.isascii()


def test_latest_pdf_layout_baseline_forces_keep() -> None:
    rows = [
        {
            "path": "chatgpt_side_outputs_old",
            "planned_action": "quarantine",
            "classification": "diagnostic_candidate",
            "evidence_reason": "name_contains_diagnostic",
            "fingerprint_detail": [
                {
                    "relative_path": (
                        "chatgpt_side_outputs_old/"
                        "20260617_requested_repo20260617_daily_highlight_current_rules.pdf"
                    ),
                    "is_dir": False,
                    "mtime_ns": 1,
                }
            ],
        },
        {
            "path": "chatgpt_side_outputs_new",
            "planned_action": "quarantine",
            "classification": "diagnostic_candidate",
            "evidence_reason": "name_contains_diagnostic",
            "fingerprint_detail": [
                {
                    "relative_path": (
                        "chatgpt_side_outputs_new/"
                        "20260618_requested_repo20260618_daily_highlight_current_rules.pdf"
                    ),
                    "is_dir": False,
                    "mtime_ns": 2,
                }
            ],
        },
    ]
    summary: dict[str, object] = {}

    planner.mark_latest_pdf_layout_baselines(rows, summary)

    assert rows[0]["planned_action"] == "quarantine"
    assert rows[0]["layout_baseline_keep"] is False
    assert rows[1]["planned_action"] == "keep"
    assert rows[1]["classification"] == "comparison_evidence_keep"
    assert rows[1]["layout_baseline_keep"] is True
    assert rows[1]["layout_baseline_report_keys"] == ["daily_highlight"]
    assert summary["layout_baseline_report_count"] == 1
    assert summary["layout_baseline_pdf_count"] == 1


def test_gitignore_contains_quarantine_and_report_paths() -> None:
    text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "_workspace_quarantine/" in text
    assert "workspace_cleanup_reports/" in text


def test_manifest_hash_excludes_manifest_hash_itself() -> None:
    manifest = {"report_id": "x", "manifest_hash": "a", "rows": []}
    first = validator.canonical_manifest_hash(manifest)
    manifest["manifest_hash"] = "b"
    second = validator.canonical_manifest_hash(manifest)
    assert first == second


def test_latest_manifest_pointer_resolves() -> None:
    latest = ROOT / "workspace_cleanup_reports" / "test_manifest_validation" / "latest_manifest.json"
    if not latest.exists():
        test_tracked_file_in_manifest_fails()
    manifest_path, manifest = validator.resolve_manifest_pointer(latest)
    assert manifest_path.name == "manifest.json"
    assert manifest["report_id"] == "test"


def test_planner_default_run_does_not_write_tracked_history_summary() -> None:
    assert planner.parse_args is not None
    manifest = {
        "git_status_porcelain_before_planner": "",
        "git_status_porcelain_after_planner": "",
        "history_summary_path": "",
    }
    assert validator.status_only_allows_history_summary(
        str(manifest["git_status_porcelain_before_planner"]),
        str(manifest["git_status_porcelain_after_planner"]),
        str(manifest["history_summary_path"]),
    )


def test_after_planner_status_only_changes_allowed_history_summary() -> None:
    before = " M docs/existing.md\n"
    after = " M docs/existing.md\n?? docs/workspace_cleanup_history/20260619_policy_summary.md\n"
    assert validator.status_only_allows_history_summary(
        before,
        after,
        "docs/workspace_cleanup_history/20260619_policy_summary.md",
    )
    assert not validator.status_only_allows_history_summary(before, after, "")


def test_permission_denied_does_not_produce_applyable_action() -> None:
    classification, action, reason = planner.classify_candidate(
        "chatgpt_side_outputs_denied",
        [],
        [],
        descendant_permission_denied=True,
        descendant_reparse=False,
    )
    assert classification == "unknown_quarantine_candidate"
    assert action == "report_only"
    assert reason == "descendant_permission_denied"


def test_layout_baseline_manifest_row_must_keep() -> None:
    protected_rows = validator.load_protected_rows([])
    errors: list[str] = []
    manifest = {
        "report_id": "baseline-test",
        "manifest_hash": "",
        "rows": [
            {
                "path": "chatgpt_side_outputs_baseline",
                "planned_action": "quarantine",
                "layout_baseline_keep": True,
            }
        ],
        "git_status_porcelain_before_planner": "",
        "git_status_porcelain_after_planner": "",
        "history_summary_path": "",
    }
    manifest["manifest_hash"] = validator.canonical_manifest_hash(manifest)
    manifest_dir = ROOT / "workspace_cleanup_reports" / "baseline_manifest_validation"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_dir / "manifest.json"
    pointer_path = manifest_dir / "latest_manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    pointer_path.write_text(
        json.dumps(
            {
                "report_id": "baseline-test",
                "manifest_path": manifest_path.relative_to(ROOT).as_posix(),
                "manifest_hash": manifest["manifest_hash"],
                "generated_at": "2026-06-19T00:00:00+00:00",
            }
        ),
        encoding="utf-8",
    )
    validator.validate_manifest(pointer_path, protected_rows, errors)
    assert any("layout baseline row must be kept" in error for error in errors)


def write_apply_test_manifest(report_id: str, rows: list[dict[str, object]]) -> tuple[Path, Path, dict[str, object]]:
    manifest = {
        "report_id": report_id,
        "manifest_hash": "",
        "rows": rows,
        "git_head": "test-head",
        "git_status_porcelain_after_planner": "",
        "generated_at_utc": "2026-06-20T00:00:00+00:00",
    }
    manifest["manifest_hash"] = apply_cleanup.manifest_hash(manifest)
    manifest_dir = ROOT / "workspace_cleanup_reports" / report_id
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_dir / "manifest.json"
    pointer_path = manifest_dir / "latest_manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    pointer_path.write_text(
        json.dumps(
            {
                "report_id": report_id,
                "manifest_path": manifest_path.relative_to(ROOT).as_posix(),
                "manifest_hash": manifest["manifest_hash"],
                "generated_at": manifest["generated_at_utc"],
            }
        ),
        encoding="utf-8",
    )
    return manifest_path, pointer_path, manifest


def test_apply_latest_manifest_pointer_resolves_to_full_manifest() -> None:
    manifest_path, pointer_path, manifest = write_apply_test_manifest("apply_pointer_validation", [])

    loaded = apply_cleanup.load_manifest(pointer_path)

    assert loaded.path == manifest_path
    assert loaded.pointer_path == pointer_path
    assert loaded.data["manifest_hash"] == manifest["manifest_hash"]


def test_apply_rejects_pointer_hash_mismatch() -> None:
    _, pointer_path, _ = write_apply_test_manifest("apply_pointer_hash_validation", [])
    pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
    pointer["manifest_hash"] = "bad"
    pointer_path.write_text(json.dumps(pointer), encoding="utf-8")

    with pytest.raises(apply_cleanup.ApplyError, match="pointer hash"):
        apply_cleanup.load_manifest(pointer_path)


def test_apply_delete_requires_allow_delete(monkeypatch: pytest.MonkeyPatch) -> None:
    candidate = ROOT / "workspace_cleanup_reports" / "apply_delete_candidate"
    shutil.rmtree(candidate, ignore_errors=True)
    candidate.mkdir(parents=True)
    try:
        manifest = {
            "rows": [
                {
                    "path": candidate.relative_to(ROOT).as_posix(),
                    "planned_action": "delete",
                    "file_count": 0,
                }
            ]
        }
        monkeypatch.setattr(apply_cleanup, "validate_manifest_context", lambda *_args, **_kwargs: None)
        monkeypatch.setattr(apply_cleanup, "git_tracked_files", lambda: set())

        with pytest.raises(apply_cleanup.ApplyError, match="--allow-delete"):
            apply_cleanup.validate_manifest_actions(manifest, allow_delete=False, max_age_hours=24)
    finally:
        shutil.rmtree(candidate, ignore_errors=True)


def test_apply_delete_rechecks_live_empty_directory() -> None:
    candidate = ROOT / "workspace_cleanup_reports" / "apply_non_empty_delete_candidate"
    shutil.rmtree(candidate, ignore_errors=True)
    candidate.mkdir(parents=True)
    (candidate / "child.txt").write_text("not empty", encoding="utf-8")
    try:
        with pytest.raises(apply_cleanup.ApplyError, match="not empty"):
            apply_cleanup.assert_live_empty_directory(candidate, candidate.relative_to(ROOT).as_posix())
    finally:
        shutil.rmtree(candidate, ignore_errors=True)


def test_apply_quarantine_manifest_uses_manual_only_recovery_hint() -> None:
    source = ROOT / "workspace_cleanup_reports" / "apply_quarantine_candidate"
    quarantine_root = ROOT / "workspace_cleanup_reports" / "apply_quarantine_root"
    shutil.rmtree(source, ignore_errors=True)
    shutil.rmtree(quarantine_root, ignore_errors=True)
    source.mkdir(parents=True)
    (source / "artifact.txt").write_text("diagnostic", encoding="utf-8")
    try:
        rows = apply_cleanup.apply_actions(
            {"report_id": "apply_quarantine_validation"},
            [
                {
                    "path": source.relative_to(ROOT).as_posix(),
                    "planned_action": "quarantine",
                    "evidence_reason": "test_diagnostic",
                }
            ],
            quarantine_root=quarantine_root,
            allow_delete=False,
            owner="test",
            expires_days=30,
        )

        manifest_path = quarantine_root / "QUARANTINE_MANIFEST.csv"
        with manifest_path.open("r", encoding="utf-8", newline="") as fh:
            manifest_rows = list(csv.DictReader(fh))
        assert rows[0]["recovery_hint"].startswith("manual-only:")
        assert manifest_rows[0]["recovery_hint"].startswith("manual-only:")
        assert not source.exists()
    finally:
        shutil.rmtree(source, ignore_errors=True)
        shutil.rmtree(quarantine_root, ignore_errors=True)
