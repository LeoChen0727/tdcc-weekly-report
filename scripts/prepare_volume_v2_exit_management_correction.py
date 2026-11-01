from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Callable
import zipfile


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_REPORT_DATE = "20261030"
SNAPSHOT_ROOT = "output/history/daily_model_snapshots"
MANIFEST = f"{SNAPSHOT_ROOT}/daily_published_model_snapshot_manifest.csv"
ARTIFACTS = {
    "volume_breakout_operation_section": "daily_volume_breakout_operation_section",
    "volume_breakout_operation_evidence_audit": "daily_volume_breakout_operation_evidence_audit",
}
EXPECTED_R1_HASHES = {
    "volume_breakout_operation_section": "3a7446e97fed8c953337ec1e4d644b51f893c60050fd4bd55b745faca4c20e10",
    "volume_breakout_operation_evidence_audit": "8ed5e0e7a5d35f8d74f8f4e217c0e065759f6df6559545bb0adb5a43c28be296",
}
MANAGEMENT_COLUMNS = {
    "stop_reference_price", "stop_reference_date", "stop_confirmed_days", "holding_days",
    "planned_entry_date", "planned_exit_date", "planned_exit_date_status", "next_action_date",
    "next_action_date_status", "stop_confirmation_date", "next_action_zh",
}
SECTION_METADATA_COLUMNS = MANAGEMENT_COLUMNS | {
    "operation_age_days", "stop_loss_price", "stop_loss_label_zh", "generated_at", "row_action_status",
}
AUDIT_METADATA_COLUMNS = MANAGEMENT_COLUMNS | {
    "operation_age_days", "stop_loss_price", "stop_loss_label_zh", "generated_at",
    "entry_date", "entry_price", "exit_date", "exit_price", "exit_reason", "exit_price_basis",
}
LATEST_PATHS = tuple(
    f"{directory}/{stem}_latest.{extension}"
    for directory in ("output/latest", "docs/latest")
    for stem in ARTIFACTS.values()
    for extension in ("csv", "md")
)
CONTRACT_AUDIT_PATHS = tuple(
    f"{directory}/model_data_independence_audit_latest.{extension}"
    for directory in ("output/latest", "docs/latest")
    for extension in ("csv", "md")
)
LOW = "volume_range_breakout_v2_low_position_volume_attack"
HIGH = "volume_range_breakout_v2_high_position_volume_attack"
EXPECTED_CONFIRMED = {(LOW, "8291"), (HIGH, "2321")}
EXPECTED_ACTIVE = {
    (LOW, "3321"), (LOW, "4960"), (LOW, "3379"),
    (HIGH, "2033"), (HIGH, "6221"), (HIGH, "8099"), (HIGH, "6141"),
}
REVISION_REASON = "volume_v2_exit_management_metadata_correction_20261101"


class CorrectionError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def execute(args: list[str], root: Path, env: dict[str, str]) -> None:
    result = subprocess.run(args, cwd=root, env=env, check=False)
    if result.returncode:
        raise CorrectionError(f"command failed ({result.returncode}): {' '.join(args)}")


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=False, capture_output=True,
        encoding="utf-8", errors="strict",
        env={**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_OPTIONAL_LOCKS": "0"},
    )
    if result.returncode:
        raise CorrectionError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def changed_paths(root: Path) -> set[str]:
    paths = set()
    for record in git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all").split("\0"):
        if not record:
            continue
        if "R" in record[:2] or "C" in record[:2]:
            raise CorrectionError("renames and copies are outside the metadata correction scope")
        paths.add(record[3:].replace("\\", "/"))
    return paths


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = list(reader.fieldnames or [])
        rows = list(reader)
    if not headers or not rows or any(None in row or any(value is None for value in row.values()) for row in rows):
        raise CorrectionError(f"missing or malformed CSV: {path}")
    return headers, rows


def assert_current_identities(rows: list[dict[str, str]]) -> None:
    full = [row for row in rows if row.get("pdf_view") == "full" and row.get("row_type") == "data"]
    for section, expected in (("confirmed_operation", EXPECTED_CONFIRMED), ("active_operation", EXPECTED_ACTIVE)):
        selected = [row for row in full if row.get("pdf_section") == section]
        identities = [(row.get("model_id"), row.get("stock_id")) for row in selected]
        if len(identities) != len(expected) or set(identities) != expected:
            raise CorrectionError(f"current {section} identities changed: {identities}")


def schema_complete(headers: list[str], rows: list[dict[str, str]], audit_headers: list[str]) -> bool:
    if not MANAGEMENT_COLUMNS.issubset(headers) or not MANAGEMENT_COLUMNS.issubset(audit_headers):
        return False
    for row in rows:
        section = row.get("pdf_section")
        if row.get("row_type") != "data" or section not in {"confirmed_operation", "active_operation"}:
            continue
        required = {"stop_reference_price", "stop_reference_date", "planned_exit_date_status", "next_action_zh"}
        if section == "active_operation":
            required |= {"holding_days", "stop_confirmed_days"}
        if row.get("row_action_status") == "stop_exit_pending_next_open":
            required |= {"stop_confirmation_date", "next_action_date_status"}
        if any(not row.get(field, "").strip() for field in required):
            return False
    return True


def assert_frozen_fields(
    before: tuple[list[str], list[dict[str, str]]],
    after: tuple[list[str], list[dict[str, str]]],
    metadata: set[str],
    *, section: bool,
) -> None:
    old_headers, old_rows = before
    headers, rows = after
    if not set(old_headers).issubset(headers) or set(headers) - set(old_headers) - metadata:
        raise CorrectionError("unapproved column addition or removal")
    frozen = sorted(set(old_headers) - metadata)

    def signature(row: dict[str, str]) -> str:
        return json.dumps({key: row.get(key, "") for key in frozen}, sort_keys=True, ensure_ascii=False)

    if Counter(map(signature, old_rows)) != Counter(map(signature, rows)):
        raise CorrectionError("identity, rank, score, metric, flag or other frozen field drift")
    if section:
        original_actions: dict[str, Counter] = {}
        for row in old_rows:
            original_actions.setdefault(signature(row), Counter())[row.get("row_action_status", "")] += 1
        for row in rows:
            actions = original_actions[signature(row)]
            action = row.get("row_action_status", "")
            prior = action
            if not actions[prior] and action == "stop_exit_pending_next_open" and row.get("pdf_section") == "active_operation":
                prior = "active_operation"
            if not actions[prior]:
                raise CorrectionError("unapproved row_action_status transition")
            actions[prior] -= 1


def immutable_snapshot_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256(path)
        for path in sorted((root / SNAPSHOT_ROOT).rglob("*.csv"))
        if path.relative_to(root).as_posix() != MANIFEST
    }


def assert_immutable_snapshots(root: Path, before: dict[str, str]) -> None:
    for relative, expected in before.items():
        path = root / relative
        if not path.is_file() or sha256(path) != expected:
            raise CorrectionError(f"existing immutable snapshot changed: {relative}")


def assert_manifest_correction_delta(
    before: tuple[list[str], list[dict[str, str]]],
    after: tuple[list[str], list[dict[str, str]]],
) -> dict:
    headers, original_rows = before
    final_headers, final_rows = after
    if final_headers != headers:
        raise CorrectionError("manifest schema changed during correction")

    def signature(row: dict[str, str]) -> tuple[str, ...]:
        return tuple(row[field] for field in headers)

    original = Counter(map(signature, original_rows))
    final = Counter(map(signature, final_rows))
    if original - final:
        raise CorrectionError("original manifest row was changed or deleted")
    added = final - original
    allowed = {(EXPECTED_REPORT_DATE, artifact, "r2") for artifact in ARTIFACTS}
    original_identities = {
        (row.get("snapshot_report_date"), row.get("artifact_id"), row.get("snapshot_revision"))
        for row in original_rows
    }
    new_identities = []
    for values, count in added.items():
        row = dict(zip(headers, values))
        identity = (row.get("snapshot_report_date"), row.get("artifact_id"), row.get("snapshot_revision"))
        if identity not in allowed or identity in original_identities or count != 1 or identity in new_identities:
            raise CorrectionError(f"unapproved new manifest row: {identity}")
        new_identities.append(identity)
    return {
        "original_row_count": len(original_rows), "final_row_count": len(final_rows),
        "added_revision_identities": [list(identity) for identity in sorted(new_identities)],
    }


def selected_snapshot_paths(root: Path, *, require_r2: bool) -> dict[str, str]:
    _, rows = read_rows(root / MANIFEST)
    paths = {}
    for artifact, stem in ARTIFACTS.items():
        selected = [row for row in rows if row.get("snapshot_report_date") == EXPECTED_REPORT_DATE and row.get("artifact_id") == artifact]
        revisions = {row.get("snapshot_revision"): row for row in selected}
        if len(revisions) != len(selected) or set(revisions) not in ({"r1"}, {"r1", "r2"}):
            raise CorrectionError(f"unexpected same-day revision chain for {artifact}; r3 is forbidden")
        r1 = revisions["r1"]
        r1_sha = EXPECTED_R1_HASHES[artifact]
        r1_path = f"{SNAPSHOT_ROOT}/{stem}_{EXPECTED_REPORT_DATE}_r1_{r1_sha[:12]}.csv"
        if r1.get("snapshot_path") != r1_path or r1.get("snapshot_sha256") != r1_sha or sha256(root / r1_path) != r1_sha:
            raise CorrectionError(f"original pinned r1 changed: {artifact}")
        if "r2" not in revisions:
            if require_r2:
                raise CorrectionError(f"missing corrected r2: {artifact}")
            continue
        row = revisions["r2"]
        digest = row.get("snapshot_sha256", "")
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise CorrectionError(f"invalid r2 SHA: {artifact}")
        path = f"{SNAPSHOT_ROOT}/{stem}_{EXPECTED_REPORT_DATE}_r2_{digest[:12]}.csv"
        if (
            row.get("snapshot_path") != path
            or row.get("supersedes_snapshot_sha256") != r1_sha
            or row.get("source_sha256") != digest
            or sha256(root / path) != digest
            or sha256(root / "output/latest" / f"{stem}_latest.csv") != digest
        ):
            raise CorrectionError(f"r2/current source binding mismatch: {artifact}")
        paths[artifact] = path
    return paths


def prepare_correction(
    *, repo_root: Path, expected_source_sha: str, expected_report_date: str,
    output_dir: Path, runner: Callable | None = None,
) -> dict:
    root = repo_root.resolve()
    output = output_dir.resolve()
    if output == root or root in output.parents:
        raise CorrectionError("output-dir must be outside the source checkout")
    if expected_report_date != EXPECTED_REPORT_DATE:
        raise CorrectionError(f"this one-time correction is restricted to {EXPECTED_REPORT_DATE}")
    if not re.fullmatch(r"[0-9a-f]{40}", expected_source_sha) or git(root, "rev-parse", "HEAD").strip() != expected_source_sha:
        raise CorrectionError("expected-source-sha must equal immutable checkout HEAD")
    if changed_paths(root):
        raise CorrectionError("correction source checkout must start clean")
    _, freshness = read_rows(root / "output/latest/data_freshness_latest.csv")
    if len(freshness) != 1 or freshness[0].get("main_price_date") != expected_report_date:
        raise CorrectionError("committed source report date differs from expected-report-date")
    if any(freshness[0].get(field) != "True" for field in ("report_ready", "daily_pdf_ready")):
        raise CorrectionError("committed report source is not ready")
    section_path = root / "output/latest/daily_volume_breakout_operation_section_latest.csv"
    audit_path = root / "output/latest/daily_volume_breakout_operation_evidence_audit_latest.csv"
    original_section, original_audit = read_rows(section_path), read_rows(audit_path)
    original_manifest = read_rows(root / MANIFEST)
    original_manifest_sha256 = sha256(root / MANIFEST)
    original_artifact_hashes = {artifact: sha256(root / "output/latest" / f"{stem}_latest.csv") for artifact, stem in ARTIFACTS.items()}
    assert_current_identities(original_section[1])
    immutable = immutable_snapshot_hashes(root)
    existing_r2 = selected_snapshot_paths(root, require_r2=False)
    pinned_baselines = {
        artifact: read_rows(root / SNAPSHOT_ROOT / f"{stem}_{EXPECTED_REPORT_DATE}_r1_{EXPECTED_R1_HASHES[artifact][:12]}.csv")
        for artifact, stem in ARTIFACTS.items()
    }
    section_baseline = pinned_baselines["volume_breakout_operation_section"]
    audit_baseline = pinned_baselines["volume_breakout_operation_evidence_audit"]
    assert_current_identities(section_baseline[1])
    assert_frozen_fields(section_baseline, original_section, SECTION_METADATA_COLUMNS, section=True)
    assert_frozen_fields(audit_baseline, original_audit, AUDIT_METADATA_COLUMNS, section=False)
    complete = schema_complete(*original_section, original_audit[0])
    if existing_r2 and (len(existing_r2) != len(ARTIFACTS) or not complete):
        raise CorrectionError("existing corrected r2 is incomplete; refusing to create r3")
    commands: list[list[str]] = []
    environment = {**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_OPTIONAL_LOCKS": "0"}
    run = runner or execute

    def step(args: list[str], *, rebuild: bool = False) -> None:
        commands.append(args)
        env = dict(environment)
        if rebuild:
            env["ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE"] = "1"
        else:
            env.pop("ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE", None)
        run(args, root, env)

    mode = "reused_corrected_r2" if existing_r2 else "prepared_corrected_r2"
    if not complete:
        step([sys.executable, "-B", "scripts/build_daily_volume_breakout_operation_section.py"], rebuild=True)
    current_section, current_audit = read_rows(section_path), read_rows(audit_path)
    if not schema_complete(*current_section, current_audit[0]):
        raise CorrectionError("regenerated management schema is missing or incomplete")
    assert_current_identities(current_section[1])
    assert_frozen_fields(section_baseline, current_section, SECTION_METADATA_COLUMNS, section=True)
    assert_frozen_fields(audit_baseline, current_audit, AUDIT_METADATA_COLUMNS, section=False)
    assert_immutable_snapshots(root, immutable)
    step([sys.executable, "-B", "scripts/validate_daily_volume_breakout_operation_section.py", "--output-only"])
    artifact_args = [part for artifact in ARTIFACTS for part in ("--artifact-id", artifact)]
    if not existing_r2:
        step([sys.executable, "-B", "scripts/update_daily_published_model_snapshots.py", *artifact_args, "--revision-reason", REVISION_REASON])
    assert_manifest_correction_delta(original_manifest, read_rows(root / MANIFEST))
    r2_paths = selected_snapshot_paths(root, require_r2=True)
    for relative in LATEST_PATHS:
        if relative.startswith("docs/latest/"):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / "output/latest" / target.name, target)
    step([sys.executable, "-B", "scripts/validate_daily_published_model_snapshots.py", *artifact_args, "--phase", "runtime"])
    step([sys.executable, "-B", "scripts/stage_daily_published_snapshot_revisions.py", "--report-date", expected_report_date, *artifact_args])
    step(["git", "add", "--", *LATEST_PATHS])
    step([sys.executable, "-B", "scripts/validate_daily_volume_breakout_operation_section.py"])
    allowed = set(LATEST_PATHS) | {MANIFEST, *r2_paths.values()}
    if len(allowed) != 11:
        raise CorrectionError("correction payload must contain exactly eleven registered paths")
    changed = changed_paths(root)
    if changed - allowed:
        raise CorrectionError(f"write allowlist violation: {sorted(changed - allowed)}")
    assert_immutable_snapshots(root, immutable)
    final_section, final_audit = read_rows(section_path), read_rows(audit_path)
    assert_current_identities(final_section[1])
    assert_frozen_fields(section_baseline, final_section, SECTION_METADATA_COLUMNS, section=True)
    assert_frozen_fields(audit_baseline, final_audit, AUDIT_METADATA_COLUMNS, section=False)
    manifest_delta = assert_manifest_correction_delta(original_manifest, read_rows(root / MANIFEST))
    if not schema_complete(*final_section, final_audit[0]) or selected_snapshot_paths(root, require_r2=True) != r2_paths:
        raise CorrectionError("final corrected schema or snapshot binding changed during validation")
    if git(root, "rev-parse", "HEAD").strip() != expected_source_sha:
        raise CorrectionError("source HEAD changed during preparation")
    payload = [{"path": path, "sha256": sha256(root / path), "bytes": (root / path).stat().st_size} for path in sorted(allowed)]
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"volume_v2_exit_management_correction_{expected_report_date}.zip"
    receipt_path = output / "volume_v2_exit_management_correction_receipt.json"
    if archive.exists() or receipt_path.exists():
        raise CorrectionError("output artifacts already exist; refusing overwrite")
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as bundle:
        for item in payload:
            bundle.write(root / item["path"], item["path"])
    with zipfile.ZipFile(archive) as bundle:
        if set(bundle.namelist()) != allowed:
            raise CorrectionError("archive paths differ from the exact allowlist")
        for item in payload:
            if hashlib.sha256(bundle.read(item["path"])).hexdigest() != item["sha256"]:
                raise CorrectionError("archive payload hash mismatch")
    receipt = {
        "receipt_type": "volume_v2_exit_management_correction_v1", "status": "reviewable_metadata_package",
        "source_sha": expected_source_sha, "report_date": expected_report_date, "mode": mode,
        "confirmed_count": 2, "active_count": 7, "frozen_business_fields_unchanged": True,
        "frozen_business_baseline": "pinned_immutable_r1_raw_sha256_verified",
        "existing_snapshots_unchanged": True, "existing_snapshot_count": len(immutable),
        "existing_snapshot_hashes_sha256": hashlib.sha256(json.dumps(immutable, sort_keys=True).encode()).hexdigest(),
        "pinned_r1_hashes": EXPECTED_R1_HASHES, "r2_paths": r2_paths,
        "original_artifact_hashes": original_artifact_hashes,
        "original_manifest_sha256": original_manifest_sha256, "manifest_delta": manifest_delta,
        "original_manifest_rows_preserved": True,
        "allowed_section_metadata_columns": sorted(SECTION_METADATA_COLUMNS),
        "allowed_audit_metadata_columns": sorted(AUDIT_METADATA_COLUMNS),
        "allowed_paths": sorted(allowed), "changed_paths": sorted(changed), "payload": payload,
        "commands": commands, "archive_path": str(archive), "archive_sha256": sha256(archive),
        "boundary_zh": "僅準備可審查當期metadata包；未fetch行情、未修改選股或績效、未commit/push、未產製packet或PDF，CI成功不代表合併或正式報告驗收。",
    }
    with receipt_path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(receipt, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return receipt


def prepare_contract_audit_package(
    *, repo_root: Path, expected_source_sha: str, output_dir: Path,
    volume_receipt: dict, runner: Callable | None = None,
) -> dict:
    root, output = repo_root.resolve(), output_dir.resolve()
    if output == root or root in output.parents:
        raise CorrectionError("output-dir must be outside the source checkout")
    if (
        volume_receipt.get("source_sha") != expected_source_sha
        or volume_receipt.get("report_date") != EXPECTED_REPORT_DATE
        or git(root, "rev-parse", "HEAD").strip() != expected_source_sha
    ):
        raise CorrectionError("contract audit source must match the volume package HEAD and report date")
    volume_paths = set(LATEST_PATHS) | {MANIFEST, *volume_receipt["r2_paths"].values()}
    if len(volume_paths) != 11 or volume_paths != set(volume_receipt["allowed_paths"]):
        raise CorrectionError("volume package does not declare its exact eleven-path contract")
    if changed_paths(root) - volume_paths:
        raise CorrectionError("unexpected changes before the separate contract-audit refresh")

    def assert_volume_payload_unchanged() -> None:
        for item in volume_receipt["payload"]:
            if sha256(root / item["path"]) != item["sha256"]:
                raise CorrectionError(f"volume payload changed during contract-audit refresh: {item['path']}")

    assert_volume_payload_unchanged()
    immutable = immutable_snapshot_hashes(root)
    original_manifest = read_rows(root / MANIFEST)
    before = {path: sha256(root / path) if (root / path).is_file() else "" for path in CONTRACT_AUDIT_PATHS}
    env = {**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_OPTIONAL_LOCKS": "0"}
    env.pop("ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE", None)
    commands = [
        [sys.executable, "-B", "scripts/build_model_data_independence_audit.py"],
        [sys.executable, "-B", "scripts/validate_model_data_independence.py", "--base-ref", "origin/main"],
        ["git", "add", "--", *CONTRACT_AUDIT_PATHS],
    ]
    run = runner or execute
    for args in commands:
        run(args, root, env)
    allowed = set(CONTRACT_AUDIT_PATHS)
    job_allowed = volume_paths | allowed
    changes = changed_paths(root)
    if len(job_allowed) != 15 or changes - job_allowed:
        raise CorrectionError(f"contract-audit write allowlist violation: {sorted(changes - job_allowed)}")
    assert_immutable_snapshots(root, immutable)
    manifest_delta = assert_manifest_correction_delta(original_manifest, read_rows(root / MANIFEST))
    assert_volume_payload_unchanged()
    if git(root, "rev-parse", "HEAD").strip() != expected_source_sha:
        raise CorrectionError("source HEAD changed during contract-audit refresh")
    payload = [{"path": path, "sha256": sha256(root / path), "bytes": (root / path).stat().st_size} for path in sorted(allowed)]
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"model_data_independence_contract_audit_{EXPECTED_REPORT_DATE}.zip"
    receipt_path = output / "model_data_independence_contract_audit_receipt.json"
    if archive.exists() or receipt_path.exists():
        raise CorrectionError("contract-audit artifacts already exist; refusing overwrite")
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as bundle:
        for item in payload:
            bundle.write(root / item["path"], item["path"])
    with zipfile.ZipFile(archive) as bundle:
        if set(bundle.namelist()) != allowed:
            raise CorrectionError("contract-audit archive paths differ from its four-path contract")
        for item in payload:
            if hashlib.sha256(bundle.read(item["path"])).hexdigest() != item["sha256"]:
                raise CorrectionError("contract-audit archive payload hash mismatch")
    receipt = {
        "receipt_type": "model_data_independence_contract_audit_package_v1",
        "status": "reviewable_contract_audit_package", "source_sha": expected_source_sha,
        "report_date": EXPECTED_REPORT_DATE, "allowed_paths": sorted(allowed),
        "job_allowed_paths": sorted(job_allowed), "job_changed_paths": sorted(changes),
        "original_audit_hashes": before, "payload": payload, "commands": commands,
        "volume_archive_sha256": volume_receipt["archive_sha256"],
        "volume_payload_unchanged": True, "existing_snapshots_unchanged": True,
        "manifest_delta": manifest_delta, "original_manifest_rows_preserved": True,
        "archive_path": str(archive), "archive_sha256": sha256(archive),
        "boundary_zh": "獨立四檔registry/AST治理稽核刷新包；原放量11檔包不變，整個job僅允許15檔。未補行情、研究、績效或未決資料，未commit/push。",
    }
    with receipt_path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(receipt, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return receipt


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare the one-time Volume V2 exit-management correction package without publication.")
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--expected-source-sha", required=True)
    parser.add_argument("--expected-report-date", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--include-contract-audit", action="store_true", help="Also prepare the separate four-file registry/AST governance audit package.")
    args = parser.parse_args(argv)
    try:
        receipt = prepare_correction(
            repo_root=args.repo_root, expected_source_sha=args.expected_source_sha,
            expected_report_date=args.expected_report_date, output_dir=args.output_dir,
        )
        audit_receipt = prepare_contract_audit_package(
            repo_root=args.repo_root, expected_source_sha=args.expected_source_sha,
            output_dir=args.output_dir, volume_receipt=receipt,
        ) if args.include_contract_audit else None
    except (CorrectionError, OSError, ValueError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    summary = {key: receipt[key] for key in ("status", "mode", "source_sha", "report_date", "archive_path", "archive_sha256")}
    if audit_receipt:
        summary["contract_audit_archive_path"] = audit_receipt["archive_path"]
        summary["contract_audit_archive_sha256"] = audit_receipt["archive_sha256"]
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
