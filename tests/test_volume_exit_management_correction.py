from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

import pytest
import yaml

from scripts import prepare_volume_v2_exit_management_correction as correction


def test_workflow_defers_runner_temp_until_step_execution() -> None:
    import yaml

    workflow = yaml.safe_load((correction.ROOT / ".github/workflows/volume_v2_exit_management_correction.yml").read_text(encoding="utf-8"))
    job = workflow["jobs"]["prepare-volume-v2-exit-management-correction"]
    assert not any("runner." in str(value) for value in job["env"].values())
    prepare = job["steps"][0]
    assert prepare["shell"] == "bash"
    assert "$RUNNER_TEMP/" in prepare["run"] and '>> "$GITHUB_ENV"' in prepare["run"]


def write_rows(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def local_git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def commit_fixture(root: Path) -> str:
    local_git(root, "add", "--all")
    local_git(root, "-c", "commit.gpgsign=false", "commit", "-qm", "fixture")
    return local_git(root, "rev-parse", "HEAD")


@pytest.fixture
def source_repo(tmp_path: Path, monkeypatch):
    root = tmp_path / "repo"
    root.mkdir()
    local_git(root, "init", "-q")
    local_git(root, "config", "user.name", "Correction Test")
    local_git(root, "config", "user.email", "correction@example.invalid")
    latest = root / "output/latest"
    headers = [
        "model_id", "pdf_view", "pdf_section", "row_type", "stock_id", "signal_date",
        "entry_date", "entry_price", "display_order", "operation_status", "row_action_status",
        "buy_rank_eligible", "operation_age_days", "planned_holding_days", "stop_loss_price",
        "stop_loss_label_zh", "operation_score", "rank_reason_zh", "sample_size", "win_rate_zh",
        "risk_flags", "generated_at",
    ]
    rows = []
    for section, identities in (
        ("confirmed_operation", correction.EXPECTED_CONFIRMED),
        ("active_operation", correction.EXPECTED_ACTIVE),
    ):
        for index, (model, stock) in enumerate(sorted(identities), 1):
            active = section == "active_operation"
            rows.append({
                "model_id": model, "pdf_view": "full", "pdf_section": section, "row_type": "data",
                "stock_id": stock, "signal_date": "20261029", "entry_date": "20261030" if active else "",
                "entry_price": "20" if active else "", "display_order": str(index),
                "operation_status": section, "row_action_status": "active_operation" if active else "confirmed_buy_candidate",
                "buy_rank_eligible": "False" if active else "True", "operation_age_days": "2",
                "planned_holding_days": "15", "stop_loss_price": "", "stop_loss_label_zh": "old reference",
                "operation_score": "71.5", "rank_reason_zh": "original rank", "sample_size": "26",
                "win_rate_zh": "80.7692%", "risk_flags": "unchanged", "generated_at": "old",
            })
    write_rows(latest / "daily_volume_breakout_operation_section_latest.csv", headers, rows)
    audit_headers = ["model_id", "stock_id", "signal_date", "included_in_daily_adapter", "audit_status", "generated_at"]
    audit_rows = [{
        "model_id": row["model_id"], "stock_id": row["stock_id"], "signal_date": row["signal_date"],
        "included_in_daily_adapter": "True", "audit_status": "positive_model_contract_evidence", "generated_at": "old",
    } for row in rows]
    write_rows(latest / "daily_volume_breakout_operation_evidence_audit_latest.csv", audit_headers, audit_rows)
    write_rows(latest / "data_freshness_latest.csv", ["main_price_date", "report_ready", "daily_pdf_ready"], [{
        "main_price_date": "20261030", "report_ready": "True", "daily_pdf_ready": "True",
    }])
    manifest_headers = [
        "snapshot_report_date", "artifact_id", "snapshot_revision", "snapshot_path", "snapshot_sha256",
        "source_sha256", "supersedes_snapshot_sha256", "revision_reason",
    ]
    manifest_rows = []
    hashes = {}
    for artifact, stem in correction.ARTIFACTS.items():
        source = latest / f"{stem}_latest.csv"
        digest = correction.sha256(source)
        hashes[artifact] = digest
        relative = f"{correction.SNAPSHOT_ROOT}/{stem}_20261030_r1_{digest[:12]}.csv"
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        manifest_rows.append({
            "snapshot_report_date": "20261030", "artifact_id": artifact, "snapshot_revision": "r1",
            "snapshot_path": relative, "snapshot_sha256": digest, "source_sha256": digest,
            "supersedes_snapshot_sha256": "", "revision_reason": "initial_publish",
        })
        (latest / f"{stem}_latest.md").write_text("original metadata\n", encoding="utf-8")
    other_digest = hashlib.sha256(b"preserved\n").hexdigest()
    other_relative = f"{correction.SNAPSHOT_ROOT}/daily_candidate_model_summary_for_report_20261029_r1_{other_digest[:12]}.csv"
    (root / other_relative).write_bytes(b"preserved\n")
    manifest_rows.append({
        "snapshot_report_date": "20261029", "artifact_id": "model_summary_for_report", "snapshot_revision": "r1",
        "snapshot_path": other_relative, "snapshot_sha256": other_digest, "source_sha256": other_digest,
        "supersedes_snapshot_sha256": "", "revision_reason": "initial_publish",
    })
    write_rows(root / correction.MANIFEST, manifest_headers, manifest_rows)
    for relative in correction.LATEST_PATHS:
        if relative.startswith("docs/"):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(latest / target.name, target)
    (latest / "other_model_statistics.csv").write_text("primary metrics retained\n", encoding="utf-8")
    monkeypatch.setattr(correction, "EXPECTED_R1_HASHES", hashes)
    source_sha = commit_fixture(root)
    return root, source_sha, tmp_path / "package"


class PreparationRunner:
    """Synthetic writer boundary; never run production producers in these tests."""

    def __init__(self, fault: str = ""):
        self.fault = fault
        self.commands = []
        self.rebuild_environment = []

    def __call__(self, args: list[str], root: Path, env: dict[str, str]) -> None:
        self.commands.append(args)
        if args[0] == "git":
            correction.execute(args, root, env)
            return
        script = Path(args[2]).name
        if script == "build_daily_volume_breakout_operation_section.py":
            self.rebuild_environment.append(env.get("ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE"))
            for artifact, stem in correction.ARTIFACTS.items():
                path = root / "output/latest" / f"{stem}_latest.csv"
                headers, rows = correction.read_rows(path)
                for field in sorted(correction.MANAGEMENT_COLUMNS):
                    if field not in headers:
                        headers.append(field)
                for row in rows:
                    row.update({field: "" for field in correction.MANAGEMENT_COLUMNS})
                    row["generated_at"] = "new"
                    if artifact.endswith("section"):
                        row.update({
                            "stop_reference_price": "12.3456", "stop_reference_date": "20261030",
                            "planned_entry_date": row["entry_date"] or "20261102", "planned_exit_date": "20261120",
                            "planned_exit_date_status": "scheduled_official_calendar", "next_action_zh": "approved management reminder",
                        })
                        if row["pdf_section"] == "active_operation":
                            row.update({"holding_days": "1", "operation_age_days": "1", "stop_confirmed_days": "0",
                                        "stop_loss_price": "12.3456", "stop_loss_label_zh": "dynamic reference"})
                        if row["stock_id"] == "4960":
                            row.update({"row_action_status": "stop_exit_pending_next_open", "stop_confirmed_days": "4",
                                        "stop_confirmation_date": "20261030", "next_action_date": "20261102",
                                        "next_action_date_status": "scheduled_official_calendar"})
                        if self.fault == "score":
                            row["operation_score"] = "999"
                        if self.fault == "flag":
                            row["risk_flags"] = "changed"
                write_rows(path, headers, rows)
                (root / "output/latest" / f"{stem}_latest.md").write_text("new management metadata\n", encoding="utf-8")
            if self.fault == "snapshot":
                path = next((root / correction.SNAPSHOT_ROOT).glob("*_r1_*.csv"))
                path.write_bytes(path.read_bytes() + b"changed\n")
            if self.fault == "outside":
                (root / "output/latest/other_model_statistics.csv").write_text("changed primary metric\n", encoding="utf-8")
        elif script == "update_daily_published_model_snapshots.py":
            headers, rows = correction.read_rows(root / correction.MANIFEST)
            for artifact, stem in correction.ARTIFACTS.items():
                source = root / "output/latest" / f"{stem}_latest.csv"
                digest = correction.sha256(source)
                relative = f"{correction.SNAPSHOT_ROOT}/{stem}_20261030_r2_{digest[:12]}.csv"
                shutil.copyfile(source, root / relative)
                rows.append({
                    "snapshot_report_date": "20261030", "artifact_id": artifact, "snapshot_revision": "r2",
                    "snapshot_path": relative, "snapshot_sha256": digest, "source_sha256": digest,
                    "supersedes_snapshot_sha256": correction.EXPECTED_R1_HASHES[artifact],
                    "revision_reason": correction.REVISION_REASON,
                })
            unrelated = next(row for row in rows if row["artifact_id"] not in correction.ARTIFACTS)
            if self.fault == "manifest_drift":
                unrelated["revision_reason"] = "changed_other_family"
            elif self.fault == "manifest_delete":
                rows.remove(unrelated)
            elif self.fault == "manifest_extra":
                rows.append({**unrelated, "snapshot_report_date": "20261030", "artifact_id": "model_registry", "snapshot_revision": "r2"})
            elif self.fault == "manifest_reorder":
                rows.reverse()
            write_rows(root / correction.MANIFEST, headers, rows)
        elif script == "stage_daily_published_snapshot_revisions.py":
            paths = correction.selected_snapshot_paths(root, require_r2=True)
            local_git(root, "add", "--", correction.MANIFEST, *paths.values())
        else:
            assert script in {"validate_daily_volume_breakout_operation_section.py", "validate_daily_published_model_snapshots.py"}
            assert "ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE" not in env
            if self.fault == "reuse_manifest_drift" and script == "validate_daily_published_model_snapshots.py":
                headers, rows = correction.read_rows(root / correction.MANIFEST)
                next(row for row in rows if row["artifact_id"] not in correction.ARTIFACTS)["revision_reason"] = "changed_on_reuse"
                write_rows(root / correction.MANIFEST, headers, rows)


def prepare(source_repo, runner: PreparationRunner) -> dict:
    root, source_sha, output = source_repo
    return correction.prepare_correction(
        repo_root=root, expected_source_sha=source_sha, expected_report_date="20261030",
        output_dir=output, runner=runner,
    )


def test_missing_schema_prepares_only_r2_and_exact_reviewable_payload(source_repo) -> None:
    root, source_sha, output = source_repo
    before = correction.immutable_snapshot_hashes(root)
    runner = PreparationRunner()

    receipt = prepare(source_repo, runner)

    assert receipt["status"] == "reviewable_metadata_package"
    assert receipt["source_sha"] == source_sha == local_git(root, "rev-parse", "HEAD")
    assert receipt["mode"] == "prepared_corrected_r2"
    assert receipt["original_manifest_rows_preserved"] is True
    assert len(receipt["manifest_delta"]["added_revision_identities"]) == 2
    assert receipt["confirmed_count"] == 2 and receipt["active_count"] == 7
    assert runner.rebuild_environment == ["1"]
    assert len(receipt["allowed_paths"]) == len(receipt["payload"]) == 11
    assert set(receipt["changed_paths"]).issubset(receipt["allowed_paths"])
    correction.assert_immutable_snapshots(root, before)
    archive = Path(receipt["archive_path"])
    with zipfile.ZipFile(archive) as bundle:
        assert set(bundle.namelist()) == set(receipt["allowed_paths"])
        assert not any("_r1_" in path for path in bundle.namelist())
    assert json.loads((output / "volume_v2_exit_management_correction_receipt.json").read_text(encoding="utf-8"))["archive_sha256"] == correction.sha256(archive)
    publication = next(args for args in runner.commands if "scripts/update_daily_published_model_snapshots.py" in args)
    assert publication.count("--artifact-id") == 2
    assert publication[-2:] == ["--revision-reason", correction.REVISION_REASON]
    assert not any("push" in args or "fetch" in args or "build_chatgpt_daily_report_packet.py" in args for args in runner.commands)


def test_existing_complete_r2_is_reused_without_rebuilding_or_r3(source_repo) -> None:
    first = prepare(source_repo, PreparationRunner())
    root, _, output = source_repo
    source_sha = commit_fixture(root)
    runner = PreparationRunner()

    receipt = prepare((root, source_sha, output.parent / "reused-package"), runner)

    assert receipt["mode"] == "reused_corrected_r2"
    assert receipt["r2_paths"] == first["r2_paths"]
    assert receipt["manifest_delta"]["added_revision_identities"] == []
    assert not any("scripts/build_daily_volume_breakout_operation_section.py" in args or "scripts/update_daily_published_model_snapshots.py" in args for args in runner.commands)
    assert not list((root / correction.SNAPSHOT_ROOT).glob("*_r3_*.csv"))


@pytest.mark.parametrize("fault,match", [("score", "frozen field drift"), ("flag", "frozen field drift"), ("snapshot", "immutable snapshot changed"), ("outside", "write allowlist violation")])
def test_business_snapshot_and_other_model_drift_prevent_package(source_repo, fault: str, match: str) -> None:
    with pytest.raises(correction.CorrectionError, match=match):
        prepare(source_repo, PreparationRunner(fault))
    assert not source_repo[2].exists()


@pytest.mark.parametrize("fault,match", [
    ("manifest_drift", "original manifest row was changed or deleted"),
    ("manifest_delete", "original manifest row was changed or deleted"),
    ("manifest_extra", "unapproved new manifest row"),
])
def test_manifest_cannot_modify_delete_or_add_an_unrelated_family_row(source_repo, fault: str, match: str) -> None:
    with pytest.raises(correction.CorrectionError, match=match):
        prepare(source_repo, PreparationRunner(fault))
    assert not source_repo[2].exists()


def test_manifest_existing_rows_may_be_reordered_without_business_changes(source_repo) -> None:
    receipt = prepare(source_repo, PreparationRunner("manifest_reorder"))
    assert receipt["original_manifest_rows_preserved"] is True
    assert receipt["manifest_delta"]["final_row_count"] == receipt["manifest_delta"]["original_row_count"] + 2


def test_manifest_guard_also_runs_when_reusing_r2(source_repo) -> None:
    prepare(source_repo, PreparationRunner())
    root, _, output = source_repo
    source_sha = commit_fixture(root)
    with pytest.raises(correction.CorrectionError, match="original manifest row was changed or deleted"):
        prepare((root, source_sha, output.parent / "reuse-drift"), PreparationRunner("reuse_manifest_drift"))


@pytest.mark.parametrize("field", ["operation_score", "sample_size"])
def test_existing_r2_business_drift_is_checked_against_pinned_r1(source_repo, field: str) -> None:
    root, _, output = source_repo
    prepare(source_repo, PreparationRunner())
    source = root / "output/latest/daily_volume_breakout_operation_section_latest.csv"
    headers, rows = correction.read_rows(source)
    rows[0][field] = "999"
    write_rows(source, headers, rows)
    shutil.copyfile(source, root / "docs/latest" / source.name)
    manifest_headers, manifest_rows = correction.read_rows(root / correction.MANIFEST)
    artifact = "volume_breakout_operation_section"
    revision = next(row for row in manifest_rows if row["artifact_id"] == artifact and row["snapshot_revision"] == "r2")
    old_path = root / revision["snapshot_path"]
    digest = correction.sha256(source)
    relative = f"{correction.SNAPSHOT_ROOT}/{correction.ARTIFACTS[artifact]}_20261030_r2_{digest[:12]}.csv"
    shutil.copyfile(source, root / relative)
    old_path.unlink()
    revision.update({"snapshot_path": relative, "snapshot_sha256": digest, "source_sha256": digest})
    write_rows(root / correction.MANIFEST, manifest_headers, manifest_rows)
    source_sha = commit_fixture(root)
    runner = PreparationRunner()

    with pytest.raises(correction.CorrectionError, match="frozen field drift"):
        prepare((root, source_sha, output.parent / f"r2-business-drift-{field}"), runner)

    assert not runner.commands


def test_complete_latest_without_r2_cannot_change_r1_business_score(source_repo) -> None:
    root, _, output = source_repo
    PreparationRunner()(
        [sys.executable, "-B", "scripts/build_daily_volume_breakout_operation_section.py"],
        root, {"ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE": "1"},
    )
    source = root / "output/latest/daily_volume_breakout_operation_section_latest.csv"
    headers, rows = correction.read_rows(source)
    rows[0]["operation_score"] = "999"
    write_rows(source, headers, rows)
    source_sha = commit_fixture(root)
    runner = PreparationRunner()

    with pytest.raises(correction.CorrectionError, match="frozen field drift"):
        prepare((root, source_sha, output), runner)

    assert not runner.commands
    assert not output.exists()


def test_blank_management_cells_do_not_count_as_complete_schema(source_repo) -> None:
    root, _, output = source_repo
    for stem in correction.ARTIFACTS.values():
        path = root / "output/latest" / f"{stem}_latest.csv"
        headers, rows = correction.read_rows(path)
        headers += sorted(correction.MANAGEMENT_COLUMNS)
        for row in rows:
            row.update({field: "" for field in correction.MANAGEMENT_COLUMNS})
        write_rows(path, headers, rows)
    source_sha = commit_fixture(root)
    runner = PreparationRunner()

    prepare((root, source_sha, output), runner)

    assert runner.rebuild_environment == ["1"]


@pytest.mark.parametrize("sha,date,match", [("0" * 40, "20261030", "HEAD"), (None, "20261102", "restricted")])
def test_expected_source_and_report_date_are_required_bindings(source_repo, sha, date: str, match: str) -> None:
    root, actual_sha, output = source_repo
    runner = PreparationRunner()
    with pytest.raises(correction.CorrectionError, match=match):
        correction.prepare_correction(repo_root=root, expected_source_sha=sha or actual_sha, expected_report_date=date, output_dir=output, runner=runner)
    assert not runner.commands


def test_a_modified_original_r1_is_rejected_before_producer(source_repo) -> None:
    root, _, output = source_repo
    artifact = "volume_breakout_operation_section"
    path = root / correction.SNAPSHOT_ROOT / f"{correction.ARTIFACTS[artifact]}_20261030_r1_{correction.EXPECTED_R1_HASHES[artifact][:12]}.csv"
    path.write_bytes(path.read_bytes() + b"rewritten\n")
    source_sha = commit_fixture(root)
    runner = PreparationRunner()
    with pytest.raises(correction.CorrectionError, match="pinned r1 changed"):
        prepare((root, source_sha, output), runner)
    assert not runner.commands


def test_workflow_checks_out_immutable_source_and_only_uploads_readonly_package() -> None:
    path = Path(__file__).resolve().parents[1] / ".github/workflows/volume_v2_exit_management_correction.yml"
    text = path.read_text(encoding="utf-8")
    workflow = yaml.safe_load(text)
    events = workflow.get("on", workflow.get(True))
    assert set(events) == {"pull_request", "workflow_dispatch"}
    assert set(events["pull_request"]["paths"]) == {
        ".github/workflows/volume_v2_exit_management_correction.yml",
        "scripts/prepare_volume_v2_exit_management_correction.py",
        "tests/test_volume_exit_management_correction.py",
        "output/history/daily_model_snapshots/daily_volume_breakout_operation_section_20261030_r2_*.csv",
        "output/history/daily_model_snapshots/daily_volume_breakout_operation_evidence_audit_20261030_r2_*.csv",
    }
    assert workflow["permissions"] == {"contents": "read"}
    job = workflow["jobs"]["prepare-volume-v2-exit-management-correction"]
    checkout = next(step for step in job["steps"] if str(step.get("uses", "")).startswith("actions/checkout@"))
    assert checkout["uses"] == "actions/checkout@v6"
    assert next(step for step in job["steps"] if str(step.get("uses", "")).startswith("actions/setup-python@"))["uses"] == "actions/setup-python@v6"
    assert checkout["with"]["ref"] == "${{ github.event.pull_request.head.sha || github.sha }}"
    assert checkout["with"]["persist-credentials"] is False
    assert "--expected-source-sha" in text and "--expected-report-date" in text
    assert "--include-contract-audit" in text
    assert "model_data_independence_contract_audit_20261030.zip" in text
    assert "model_data_independence_contract_audit_receipt.json" in text
    assert "actions/upload-artifact@" in text
    for forbidden in ("git push", "git commit", "secrets.", "daily_full_pipeline.yml", "run_chatgpt_daily_report_entrypoint.py"):
        assert forbidden not in text


class ContractAuditRunner:
    def __init__(self, fault: str = ""):
        self.fault = fault
        self.commands = []

    def __call__(self, args: list[str], root: Path, env: dict[str, str]) -> None:
        self.commands.append(args)
        assert "ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE" not in env
        if args[0] == "git":
            correction.execute(args, root, env)
            return
        script = Path(args[2]).name
        if script == "build_model_data_independence_audit.py":
            for relative in correction.CONTRACT_AUDIT_PATHS:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("family,status\ncalendar,registered\n" if path.suffix == ".csv" else "# Registry and AST audit\n", encoding="utf-8")
            if self.fault == "outside":
                (root / "output/latest/other_model_statistics.csv").write_text("changed primary metric\n", encoding="utf-8")
            elif self.fault == "volume":
                (root / "output/latest/daily_volume_breakout_operation_section_latest.md").write_text("changed volume package\n", encoding="utf-8")
            elif self.fault == "snapshot":
                path = next((root / correction.SNAPSHOT_ROOT).glob("*_r1_*.csv"))
                path.write_bytes(path.read_bytes() + b"changed\n")
            elif self.fault == "manifest":
                headers, rows = correction.read_rows(root / correction.MANIFEST)
                next(row for row in rows if row["artifact_id"] not in correction.ARTIFACTS)["revision_reason"] = "changed_by_audit"
                write_rows(root / correction.MANIFEST, headers, rows)
        else:
            assert script == "validate_model_data_independence.py"
            assert args[-2:] == ["--base-ref", "origin/main"]


def test_contract_audit_is_a_separate_four_file_package_with_same_source(source_repo) -> None:
    root, source_sha, output = source_repo
    volume = prepare(source_repo, PreparationRunner())
    volume_archive_sha = correction.sha256(Path(volume["archive_path"]))
    runner = ContractAuditRunner()

    receipt = correction.prepare_contract_audit_package(
        repo_root=root, expected_source_sha=source_sha, output_dir=output,
        volume_receipt=volume, runner=runner,
    )

    assert receipt["source_sha"] == volume["source_sha"] == local_git(root, "rev-parse", "HEAD")
    assert set(receipt["allowed_paths"]) == set(correction.CONTRACT_AUDIT_PATHS)
    assert len(receipt["payload"]) == 4 and len(receipt["job_allowed_paths"]) == 15
    assert set(receipt["job_changed_paths"]).issubset(receipt["job_allowed_paths"])
    assert len(volume["allowed_paths"]) == 11
    assert receipt["volume_payload_unchanged"] is True
    assert correction.sha256(Path(volume["archive_path"])) == volume_archive_sha
    with zipfile.ZipFile(receipt["archive_path"]) as bundle:
        assert set(bundle.namelist()) == set(correction.CONTRACT_AUDIT_PATHS)
    stored = json.loads((output / "model_data_independence_contract_audit_receipt.json").read_text(encoding="utf-8"))
    assert stored["archive_sha256"] == correction.sha256(Path(receipt["archive_path"]))
    assert len(runner.commands) == 3


def test_contract_audit_cannot_modify_another_model_statistic(source_repo) -> None:
    root, source_sha, output = source_repo
    volume = prepare(source_repo, PreparationRunner())
    with pytest.raises(correction.CorrectionError, match="contract-audit write allowlist violation"):
        correction.prepare_contract_audit_package(
            repo_root=root, expected_source_sha=source_sha, output_dir=output,
            volume_receipt=volume, runner=ContractAuditRunner("outside"),
        )
    assert not (output / "model_data_independence_contract_audit_20261030.zip").exists()


@pytest.mark.parametrize("fault,match", [
    ("volume", "volume payload changed"),
    ("snapshot", "write allowlist violation"),
    ("manifest", "original manifest row was changed or deleted"),
])
def test_contract_audit_cannot_change_volume_payload_or_existing_snapshot(source_repo, fault: str, match: str) -> None:
    root, source_sha, output = source_repo
    volume = prepare(source_repo, PreparationRunner())
    with pytest.raises(correction.CorrectionError, match=match):
        correction.prepare_contract_audit_package(
            repo_root=root, expected_source_sha=source_sha, output_dir=output,
            volume_receipt=volume, runner=ContractAuditRunner(fault),
        )
    assert not (output / "model_data_independence_contract_audit_20261030.zip").exists()
