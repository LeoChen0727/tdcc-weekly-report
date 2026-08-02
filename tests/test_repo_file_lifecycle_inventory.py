from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

from scripts import validate_repo_file_lifecycle_inventory as validator


ROOT = Path(__file__).resolve().parents[1]


def run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.stdout.strip()


def test_repo_file_lifecycle_inventory_validator_passes() -> None:
    assert validator.main() == 0


def test_lifecycle_inventory_covers_existing_production_inventory() -> None:
    lifecycle_path = ROOT / "config" / "repo_file_lifecycle_inventory.csv"
    production_path = ROOT / "config" / "repo_production_inventory.csv"

    with lifecycle_path.open("r", encoding="utf-8-sig", newline="") as fh:
        lifecycle = {row["path"]: row for row in csv.DictReader(fh)}
    with production_path.open("r", encoding="utf-8-sig", newline="") as fh:
        production = {row["path"]: row for row in csv.DictReader(fh)}

    assert set(production) <= set(lifecycle)
    assert lifecycle["scripts/validate_repo_file_lifecycle_inventory.py"]["status"] == "active"
    assert "scripts/build_chip_flow_positive_streak.py" not in lifecycle


def test_lifecycle_inventory_has_no_pending_delete_or_deprecated_rows() -> None:
    lifecycle_path = ROOT / "config" / "repo_file_lifecycle_inventory.csv"

    with lifecycle_path.open("r", encoding="utf-8-sig", newline="") as fh:
        pending = [
            row["path"]
            for row in csv.DictReader(fh)
            if row["status"] in {"deprecated", "delete_candidate"}
        ]

    assert pending == []


def test_lifecycle_inventory_does_not_track_date_stamped_daily_readme_aliases() -> None:
    lifecycle_path = ROOT / "config" / "repo_file_lifecycle_inventory.csv"
    date_readme = re.compile(r"(?:^|/)READ_ME_FIRST_DAILY_REPORT_\d{8}\.txt$")
    reference_columns = [
        "called_by_workflow",
        "imported_by",
        "tested_by",
        "documented_by",
        "writes_artifact",
        "reads_artifact",
    ]

    with lifecycle_path.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    assert [row["path"] for row in rows if date_readme.search(row["path"])] == []
    offenders: list[tuple[str, str, str]] = []
    for row in rows:
        for column in reference_columns:
            for ref in row[column].split(";"):
                if date_readme.search(ref):
                    offenders.append((row["path"], column, ref))

    assert offenders == []


def test_active_guidance_does_not_point_to_retired_daily_pdf_artifacts() -> None:
    for path, row in validator.load_lifecycle_inventory([]).items():
        if row.type not in {"guidance_doc", "generated_guidance"} or row.status == "historical_artifact":
            continue
        text = validator.read_text(ROOT / path)
        assert "daily_market_curated_report_latest.pdf" not in text
        assert "daily_market_full_table_report_latest.pdf" not in text


def test_lifecycle_gate_is_hooked_into_daily_pipeline() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    boundary = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_repo_file_lifecycle_inventory.py" in workflow
    assert "validate_repo_file_lifecycle_inventory.py" in boundary


def test_read_text_reads_skip_worktree_file_from_head(tmp_path: Path, monkeypatch) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    run_git(repo, "init")
    run_git(repo, "config", "user.email", "tests@example.com")
    run_git(repo, "config", "user.name", "Lifecycle Tests")
    (repo / "scripts").mkdir()
    (repo / "scripts" / "keep.py").write_text("KEEP = True\n", encoding="utf-8")
    omitted = repo / "docs" / "latest" / "omitted.md"
    omitted.parent.mkdir(parents=True)
    omitted.write_text("canonical sparse text\n", encoding="utf-8")
    run_git(repo, "add", "-A")
    run_git(repo, "commit", "-m", "sparse source")

    sparse = tmp_path / "sparse"
    run_git(repo, "worktree", "add", "--no-checkout", "--detach", str(sparse), "HEAD")
    try:
        run_git(sparse, "sparse-checkout", "init", "--cone")
        run_git(sparse, "sparse-checkout", "set", "scripts")
        run_git(sparse, "reset", "--hard", "HEAD")
        assert not (sparse / "docs" / "latest" / "omitted.md").exists()

        monkeypatch.setattr(validator, "ROOT", sparse)
        assert validator.read_text(sparse / "docs" / "latest" / "omitted.md") == "canonical sparse text\n"
    finally:
        run_git(repo, "worktree", "remove", "--force", str(sparse))


def test_test_reference_matching_rejects_similar_validator_and_input_names() -> None:
    producer = "scripts/x.py"
    validator_path = "scripts/validate_x.py"

    assert validator.test_text_references_target(
        "python scripts/validate_x.py",
        validator_path,
    )
    assert not validator.test_text_references_target(
        "python scripts/validate_x.py",
        producer,
    )
    assert not validator.test_text_references_target(
        "run_x_chain_only = True",
        producer,
    )


def test_test_reference_matching_accepts_exact_path_import_and_module_references() -> None:
    target = "scripts/x.py"
    direct_references = [
        "python scripts/x.py",
        "from scripts.x import main",
        "import scripts.x",
        "scripts.x.main()",
        "entrypoint.x.main()",
        '(ROOT / "scripts" / "x.py").read_text()',
        'b\'      - "scripts/x.py"\\n\'',
    ]

    for text in direct_references:
        assert validator.test_text_references_target(text, target), text

    assert not validator.test_text_references_target(
        'artifact = "output/latest/x.csv"',
        target,
    )
    assert not validator.test_text_references_target(
        'workflow = ".github/workflows/x.yml"',
        target,
    )


def test_reference_column_validation_still_rejects_missing_tested_by(
    monkeypatch,
) -> None:
    target = "scripts/x.py"
    direct_test = "tests/test_x.py"
    lifecycle = {
        target: validator.LifecycleRow(
            path=target,
            type="python",
            owner="repo_infrastructure",
            status="active",
            called_by_workflow=(),
            imported_by=(),
            tested_by=(),
            documented_by=(),
            writes_artifact=(),
            reads_artifact=(),
            keep_reason="test fixture",
            delete_reason="",
            removal_risk="high",
        )
    }
    monkeypatch.setattr(validator, "workflow_invocations", lambda: {})
    monkeypatch.setattr(validator, "import_references", lambda _: {})
    monkeypatch.setattr(validator, "documentation_references", lambda _: {})
    monkeypatch.setattr(
        validator,
        "test_references",
        lambda _: {target: {direct_test}},
    )
    monkeypatch.setattr(validator, "lineage_artifacts", lambda: ({}, {}))

    errors = validator.validate_reference_columns(lifecycle)

    assert errors == [
        f"{target} lifecycle tested_by out of date: expected ['{direct_test}'], got []"
    ]
