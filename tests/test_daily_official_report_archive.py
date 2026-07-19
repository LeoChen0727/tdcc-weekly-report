from __future__ import annotations

import json
from pathlib import Path

from scripts import archive_daily_official_report_bundles as archive
from scripts import validate_daily_official_report_archive_contract as contract_validator


CURRENT = "20240104"
BASELINE = "20240103"
OLDER_A = "20240101"
OLDER_B = "20240102"


def authority() -> archive.AuthorityState:
    return archive.AuthorityState(
        current_date=CURRENT,
        authority_ref="origin/main",
        authority_sha="a" * 40,
        report_manifest_path="output/latest/report_manifest_latest.json",
        freshness_csv_path="output/latest/data_freshness_latest.csv",
    )


def test_authority_files_are_read_from_the_resolved_immutable_sha(
    tmp_path: Path, monkeypatch
) -> None:
    resolved_sha = "b" * 40
    calls: list[list[str]] = []

    def fake_run_git(_repo_root: Path, args: list[str]) -> str:
        calls.append(args)
        if args == ["rev-parse", "origin/main"]:
            return resolved_sha + "\n"
        if args == ["show", f"{resolved_sha}:output/latest/report_manifest_latest.json"]:
            return json.dumps(
                {
                    "main_price_date": CURRENT,
                    "report_ready": True,
                    "history_path_contract": "canonical_daily_market_history_only",
                }
            )
        if args == ["show", f"{resolved_sha}:output/latest/data_freshness_latest.csv"]:
            return (
                "main_price_date,report_ready,warrant_ready,daily_pdf_ready\n"
                f"{CURRENT},True,True,True\n"
            )
        raise AssertionError(args)

    monkeypatch.setattr(archive, "run_git", fake_run_git)

    state = archive.load_authority_state(
        tmp_path.resolve(), "origin/main", archive.load_contract()
    )

    assert state.authority_sha == resolved_sha
    assert calls[0] == ["rev-parse", "origin/main"]
    assert all(
        call == ["rev-parse", "origin/main"] or call[1].startswith(f"{resolved_sha}:")
        for call in calls
    )


def write_bundle(root: Path, report_date: str, *, retained: bool) -> None:
    bundle = root / report_date
    bundle.mkdir(parents=True)
    if retained:
        for index in range(6):
            (bundle / f"report-{index + 1}.pdf").write_bytes(
                f"{report_date}-pdf-{index + 1}".encode()
            )
        runtime = {
            "manifest_type": "chatgpt_daily_report_runtime_manifest",
            "main_price_date": report_date,
            "expected_main_price_date": report_date,
            "source_ref": "origin/main",
            "official_entrypoint": "scripts/run_chatgpt_daily_report_entrypoint.py",
            "report_ready": True,
            "warrant_ready": True,
            "daily_pdf_ready": True,
            "pdf_count": 6,
        }
        (bundle / "chatgpt_daily_report_runtime_manifest.json").write_text(
            json.dumps(runtime), encoding="utf-8"
        )
    else:
        (bundle / "report.pdf").write_bytes(f"{report_date}-pdf".encode())
        (bundle / "chart.png").write_bytes(f"{report_date}-png".encode())
        (bundle / "validation.csv").write_text("status\npass\n", encoding="utf-8")
        (bundle / "evidence.json").write_text('{"status":"pass"}', encoding="utf-8")


def make_environment(tmp_path: Path) -> tuple[Path, Path, Path, archive.ArchiveContract]:
    source = tmp_path / "source" / "chatgpt_side_outputs_official"
    destination = tmp_path / "archive"
    reports = tmp_path / "reports"
    source.mkdir(parents=True)
    destination.mkdir()
    reports.mkdir()
    write_bundle(source, OLDER_A, retained=False)
    write_bundle(source, OLDER_B, retained=False)
    write_bundle(source, BASELINE, retained=True)
    write_bundle(source, CURRENT, retained=True)
    return source, destination, reports, archive.load_contract()


def storage(*, filesystem: str = "NTFS", free_bytes: int = 10**9) -> archive.StorageProbe:
    return lambda _path: archive.StorageInfo(
        volume="F:", filesystem=filesystem, free_bytes=free_bytes
    )


def execute(
    tmp_path: Path,
    *,
    apply_copy: bool,
    include_dates: tuple[str, ...] = (),
    storage_probe: archive.StorageProbe | None = None,
    copy_function: archive.CopyFunction | None = None,
) -> tuple[archive.ArchiveResult, Path, Path, Path]:
    source, destination, reports, contract = make_environment(tmp_path)
    result = archive.execute_archive(
        repo_root=tmp_path,
        source_root=source,
        destination_root=destination,
        report_dir=reports,
        expected_destination_volume="F:",
        authority_ref="origin/main",
        contract=contract,
        apply_copy=apply_copy,
        include_dates=include_dates,
        storage_probe=storage_probe or storage(),
        authority_state=authority(),
        copy_function=copy_function,
    )
    return result, source, destination, reports


def test_current_and_baseline_stay_on_source_and_only_older_bundles_are_selected(tmp_path: Path) -> None:
    result, source, destination, _reports = execute(tmp_path, apply_copy=True)

    assert result.success
    assert result.current_date == CURRENT
    assert result.baseline_date == BASELINE
    assert {item.report_date for item in result.selected_files} == {OLDER_A, OLDER_B}
    assert (source / CURRENT).exists()
    assert (source / BASELINE).exists()
    assert not (destination / "daily" / CURRENT).exists()
    assert not (destination / "daily" / BASELINE).exists()


def test_copy_verifies_sha_parity_and_preserves_complete_source_fingerprint(tmp_path: Path) -> None:
    result, _source, _destination, _reports = execute(tmp_path, apply_copy=True)

    assert result.success
    assert result.source_fingerprint_before == result.source_fingerprint_after
    assert result.source_file_count_before == result.source_file_count_after
    assert all(item.destination_sha256 == item.sha256 for item in result.selected_files)
    assert all(item.source_sha256_after == item.sha256 for item in result.selected_files)


def test_same_sha_rerun_is_idempotent_and_does_not_duplicate_files(tmp_path: Path) -> None:
    first, source, destination, reports = execute(tmp_path, apply_copy=True)
    first_count = len(list(destination.rglob("*.*")))
    second = archive.execute_archive(
        repo_root=tmp_path,
        source_root=source,
        destination_root=destination,
        report_dir=reports,
        expected_destination_volume="F:",
        authority_ref="origin/main",
        contract=archive.load_contract(),
        apply_copy=True,
        storage_probe=storage(),
        authority_state=authority(),
    )

    assert first.success and second.success
    assert len(list(destination.rglob("*.*"))) == first_count
    assert {item.copy_action for item in second.selected_files} == {
        "already_present_same_sha"
    }


def test_idempotent_rerun_requires_only_margin_space(tmp_path: Path) -> None:
    first, source, destination, reports = execute(tmp_path, apply_copy=True)
    contract = archive.load_contract()
    second = archive.execute_archive(
        repo_root=tmp_path,
        source_root=source,
        destination_root=destination,
        report_dir=reports,
        expected_destination_volume="F:",
        authority_ref="origin/main",
        contract=contract,
        apply_copy=True,
        storage_probe=storage(free_bytes=contract.free_space_margin_bytes),
        authority_state=authority(),
    )

    assert first.success and second.success
    report = json.loads(second.report_path.read_text(encoding="utf-8"))
    assert report["copy_required_bytes"] == 0


def test_different_sha_destination_collision_fails_before_any_copy(tmp_path: Path) -> None:
    source, destination, reports, contract = make_environment(tmp_path)
    collision = destination / "daily" / OLDER_A / "report.pdf"
    collision.parent.mkdir(parents=True)
    collision.write_bytes(b"different")

    result = archive.execute_archive(
        repo_root=tmp_path,
        source_root=source,
        destination_root=destination,
        report_dir=reports,
        expected_destination_volume="F:",
        authority_ref="origin/main",
        contract=contract,
        apply_copy=True,
        storage_probe=storage(),
        authority_state=authority(),
    )

    assert not result.success
    assert result.completion_state == "copy_failed"
    assert "collision" in result.error
    assert {item.report_date for item in result.selected_files} == {OLDER_A, OLDER_B}
    assert not (destination / "daily" / OLDER_B).exists()
    assert json.loads(result.report_path.read_text(encoding="utf-8"))["completion_state"] == "copy_failed"


def test_non_ntfs_destination_fails_closed_and_writes_report(tmp_path: Path) -> None:
    result, _source, _destination, _reports = execute(
        tmp_path, apply_copy=True, storage_probe=storage(filesystem="exFAT")
    )

    assert not result.success
    assert "filesystem must be NTFS" in result.error
    assert result.manifest_path.exists()
    assert result.report_path.exists()


def test_wrong_destination_volume_fails_closed_and_keeps_selected_evidence(tmp_path: Path) -> None:
    result, _source, _destination, _reports = execute(
        tmp_path,
        apply_copy=True,
        storage_probe=lambda _path: archive.StorageInfo(
            volume="G:", filesystem="NTFS", free_bytes=10**9
        ),
    )

    assert not result.success
    assert result.completion_state == "copy_failed"
    assert "destination volume mismatch" in result.error
    assert {item.report_date for item in result.selected_files} == {OLDER_A, OLDER_B}


def test_insufficient_space_fails_closed(tmp_path: Path) -> None:
    result, _source, _destination, _reports = execute(
        tmp_path, apply_copy=True, storage_probe=storage(free_bytes=1)
    )

    assert not result.success
    assert "free space is insufficient" in result.error


def test_illegal_destination_inside_source_fails_closed(tmp_path: Path) -> None:
    source, _destination, reports, contract = make_environment(tmp_path)
    illegal_destination = source / "archive"
    illegal_destination.mkdir()
    result = archive.execute_archive(
        repo_root=tmp_path,
        source_root=source,
        destination_root=illegal_destination,
        report_dir=reports,
        expected_destination_volume="F:",
        authority_ref="origin/main",
        contract=contract,
        apply_copy=True,
        storage_probe=storage(),
        authority_state=authority(),
    )

    assert not result.success
    assert "unexpected entries" in result.error or "disjoint" in result.error


def test_partial_copy_failure_is_not_success_and_sources_remain_unchanged(tmp_path: Path) -> None:
    source, destination, reports, contract = make_environment(tmp_path)
    before = {
        path.relative_to(source): archive.hash_file_stable(path)[1]
        for path in source.rglob("*")
        if path.is_file()
    }
    calls = 0

    def fail_second(item: archive.FileEvidence) -> tuple[str, str]:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise archive.ArchiveError("injected partial copy failure")
        return archive.copy_candidate_atomic(item, destination)

    result = archive.execute_archive(
        repo_root=tmp_path,
        source_root=source,
        destination_root=destination,
        report_dir=reports,
        expected_destination_volume="F:",
        authority_ref="origin/main",
        contract=contract,
        apply_copy=True,
        storage_probe=storage(),
        authority_state=authority(),
        copy_function=fail_second,
    )
    after = {
        path.relative_to(source): archive.hash_file_stable(path)[1]
        for path in source.rglob("*")
        if path.is_file()
    }

    assert not result.success
    assert "injected partial copy failure" in result.error
    assert before == after
    assert any(item.copy_action == "copied_new" for item in result.selected_files)
    assert any(item.copy_action == "copy_failed" for item in result.selected_files)


def test_include_date_cannot_select_current_or_baseline(tmp_path: Path) -> None:
    result, _source, _destination, _reports = execute(
        tmp_path, apply_copy=True, include_dates=(CURRENT,)
    )

    assert not result.success
    assert "not older than the retained baseline" in result.error


def test_bounded_pilot_selects_one_eligible_bundle(tmp_path: Path) -> None:
    result, _source, destination, _reports = execute(
        tmp_path, apply_copy=True, include_dates=(OLDER_A,)
    )

    assert result.success
    assert {item.report_date for item in result.selected_files} == {OLDER_A}
    assert (destination / "daily" / OLDER_A).is_dir()
    assert not (destination / "daily" / OLDER_B).exists()


def test_validate_only_never_copies(tmp_path: Path) -> None:
    result, _source, destination, _reports = execute(tmp_path, apply_copy=False)

    assert result.success
    assert result.completion_state == "validation_passed"
    assert {item.copy_action for item in result.selected_files} == {"validated_not_copied"}
    assert list(destination.rglob("*.*")) == []


def test_relative_repo_root_is_resolved_for_cli_compatible_execution(
    tmp_path: Path, monkeypatch
) -> None:
    source, destination, reports, contract = make_environment(tmp_path)
    monkeypatch.chdir(tmp_path)

    result = archive.execute_archive(
        repo_root=Path("."),
        source_root=source,
        destination_root=destination,
        report_dir=reports,
        expected_destination_volume="F:",
        authority_ref="origin/main",
        contract=contract,
        apply_copy=False,
        storage_probe=storage(),
        authority_state=authority(),
    )
    report = json.loads(result.report_path.read_text(encoding="utf-8"))

    assert result.success
    assert report["repo_root"] == str(tmp_path.resolve())


def test_archive_contract_validator_passes() -> None:
    assert contract_validator.validate() == []
