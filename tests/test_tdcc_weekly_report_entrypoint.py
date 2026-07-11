import subprocess
from pathlib import Path
from types import SimpleNamespace

from scripts import run_tdcc_weekly_report_entrypoint as entrypoint


def test_entrypoint_allows_generated_latest_dirty_paths() -> None:
    assert entrypoint.is_generated_delivery_path("output/latest/tdcc_weekly_candidate_full_latest.pdf")
    assert entrypoint.is_generated_delivery_path(
        "output/latest/published_reports/tdcc_weekly/TDCC_report_20260703.pdf"
    )
    assert entrypoint.is_generated_delivery_path("docs/latest/tdcc_weekly_candidate_full_latest.pdf")


def test_entrypoint_rejects_non_generated_dirty_paths() -> None:
    assert not entrypoint.is_generated_delivery_path("scripts/build_tdcc_weekly_candidate_reports.py")
    assert not entrypoint.is_generated_delivery_path(".github/workflows/tdcc_weekly.yml")
    assert not entrypoint.is_generated_delivery_path("config/repo_file_lifecycle_inventory.csv")


def test_entrypoint_allows_only_untracked_codex_local_config() -> None:
    assert entrypoint.is_allowed_untracked_local_metadata("??", ".codex/config.toml")
    assert entrypoint.is_allowed_untracked_local_metadata("??", ".codex\\config.toml")
    assert not entrypoint.is_allowed_untracked_local_metadata(" M", ".codex/config.toml")
    assert not entrypoint.is_allowed_untracked_local_metadata("??", ".codex/other.toml")


def test_entrypoint_dirty_gate_ignores_only_codex_local_config(tmp_path: Path) -> None:
    subprocess.run(
        ["git", "init"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    )
    codex_dir = tmp_path / ".codex"
    codex_dir.mkdir()
    (codex_dir / "config.toml").write_text('approval_policy = "never"\n', encoding="utf-8")

    assert entrypoint.dirty_non_generated_paths(tmp_path) == []

    (codex_dir / "unexpected.toml").write_text("unexpected = true\n", encoding="utf-8")
    assert entrypoint.dirty_non_generated_paths(tmp_path) == [".codex/unexpected.toml"]


def test_repo_ignores_exact_codex_local_config_only() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    ignore_lines = {
        line.strip()
        for line in (repo_root / ".gitignore").read_text(encoding="utf-8").splitlines()
    }

    assert "/.codex/config.toml" in ignore_lines
    assert "/.codex/" not in ignore_lines


def test_entrypoint_does_not_apply_source_dirty_gate_to_delivery_root(
    tmp_path: Path,
    monkeypatch,
) -> None:
    repo_root = tmp_path / "automation-source"
    delivery_root = tmp_path / "fixed-delivery"
    repo_root.mkdir()
    delivery_root.mkdir()
    inspected_roots: list[Path] = []

    monkeypatch.setattr(
        entrypoint,
        "parse_args",
        lambda: SimpleNamespace(
            repo_root=repo_root,
            delivery_root=delivery_root,
            source_ref="origin/main",
            source_gate_only=True,
            keep_source_worktree=False,
        ),
    )
    monkeypatch.setattr(entrypoint, "fetch_source", lambda root: None)
    monkeypatch.setattr(entrypoint, "resolve_commit", lambda root, ref: "source-sha")

    def record_dirty_check(root: Path) -> list[str]:
        resolved = Path(root).resolve()
        inspected_roots.append(resolved)
        if resolved == delivery_root.resolve():
            return ["scripts/local_delivery_change.py"]
        return []

    def add_clean_source(root: Path, source_ref: str, temp_root: Path) -> Path:
        clean_source = temp_root / "clean-source"
        clean_source.mkdir()
        return clean_source

    monkeypatch.setattr(entrypoint, "dirty_non_generated_paths", record_dirty_check)
    monkeypatch.setattr(entrypoint, "add_source_worktree", add_clean_source)
    monkeypatch.setattr(entrypoint, "remove_source_worktree", lambda root, source: None)

    assert entrypoint.main() == 0
    assert repo_root.resolve() in inspected_roots
    assert delivery_root.resolve() not in inspected_roots


def test_entrypoint_delivery_paths_use_report_ready_signal_date() -> None:
    paths = entrypoint.delivery_pdf_paths("20260703")

    assert paths["highlight"].parent == Path("output/latest/published_reports/tdcc_weekly")
    assert paths["full"].parent == Path("output/latest/published_reports/tdcc_weekly")
    assert paths["highlight"].name.endswith("_20260703.pdf")
    assert paths["full"].name.endswith("_20260703.pdf")
    assert "20260704" not in paths["highlight"].name
    assert "20260704" not in paths["full"].name


def test_entrypoint_sync_outputs_copies_tdcc_artifacts_only(tmp_path: Path) -> None:
    source = tmp_path / "source"
    target = tmp_path / "target"
    for root in (source, target):
        (root / "output/latest/published_reports/tdcc_weekly").mkdir(parents=True)
        (root / "docs/latest/published_reports/tdcc_weekly").mkdir(parents=True)

    wanted = [
        "output/latest/tdcc_weekly_candidate_highlight_latest.pdf",
        "output/latest/published_reports/tdcc_weekly/TDCC_report_20260703.pdf",
        "docs/latest/tdcc_weekly_candidate_highlight_latest.pdf",
        "docs/latest/published_reports/tdcc_weekly/TDCC_report_20260703.pdf",
        "output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
    ]
    for rel in wanted:
        path = source / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rel, encoding="utf-8")

    ignored = source / "output/latest/daily_candidate_model_signals_for_report_latest.csv"
    ignored.parent.mkdir(parents=True, exist_ok=True)
    ignored.write_text("daily", encoding="utf-8")
    stale_root_pdf = target / "output/latest/TDCC_stale_20260626.pdf"
    stale_root_pdf.write_text("stale", encoding="utf-8")

    copied = entrypoint.sync_outputs(source, target)

    copied_text = {path.as_posix() for path in copied}
    assert set(wanted) <= copied_text
    assert not (target / ignored.relative_to(source)).exists()
    assert not stale_root_pdf.exists()
    for rel in wanted:
        assert (target / rel).read_text(encoding="utf-8") == rel


def test_entrypoint_load_validation_requires_report_ready_date_contract(tmp_path: Path) -> None:
    latest = tmp_path / "output/latest"
    latest.mkdir(parents=True)
    (latest / "tdcc_weekly_candidate_report_validation_latest.json").write_text(
        """
        {
          "status": "pass",
          "signal_date": "20260703",
          "date_contract": {
            "date_source": "report_ready_csv_signal_date",
            "report_date": "20260703"
          },
          "errors": []
        }
        """,
        encoding="utf-8",
    )

    data = entrypoint.load_validation(tmp_path)

    assert data["signal_date"] == "20260703"
