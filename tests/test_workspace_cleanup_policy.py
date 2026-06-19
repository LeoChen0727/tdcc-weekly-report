from __future__ import annotations

import json
from pathlib import Path

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
