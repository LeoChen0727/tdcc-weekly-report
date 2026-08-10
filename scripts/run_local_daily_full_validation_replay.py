#!/usr/bin/env python3
"""Create and run local Daily Full validation replay workspaces on F only."""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import scripts.git_worktree_safety as git_worktree_safety


REPLAY_DATE = "20260807"
CONSUMER_ID = "local_daily_full_validation_replay"
WORKSPACE_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]{0,79}$")
RUNNER_RELATIVE_PATH = Path("scripts/run_daily_full_validation_replay.py")
WORKSPACE_MANIFEST = "local_validation_replay_workspace_manifest.json"
WORKSPACE_MANIFEST_SHA = f"{WORKSPACE_MANIFEST}.sha256"
FORBIDDEN_SYSTEM_TEMP_PREFIXES = (
    "codex-daily-full-replay",
    "daily-full-replay",
    "daily_full_validation_replay",
    "local-validation-replay",
    "tdcc-daily-full-replay",
)
FORBIDDEN_SYSTEM_TEMP_EXACT_NAMES = ("r23",)


class LocalValidationReplayWorkspaceError(RuntimeError):
    pass


@dataclass(frozen=True)
class LocalReplayWorkspacePaths:
    workspace_root: Path
    source_root: Path
    runner_temp_root: Path
    synthetic_git_root: Path
    synthetic_index_path: Path
    synthetic_pathspec_path: Path
    render_root: Path
    extract_root: Path
    evidence_root: Path
    checkpoint_input_root: Path
    post_checkpoint_root: Path
    manifest_path: Path
    manifest_sha_path: Path

    def canonical_strings(self) -> dict[str, str]:
        return {
            key: str(value.resolve(strict=False))
            for key, value in asdict(self).items()
        }


def canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _run(
    command: Sequence[str],
    *,
    cwd: Path,
    env: dict[str, str] | None = None,
    label: str,
) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        list(command),
        cwd=str(cwd),
        env=env,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or label).strip()
        raise LocalValidationReplayWorkspaceError(
            f"{label} failed with exit={proc.returncode}: {detail}"
        )
    return proc


def _git(repo_root: Path, *args: str, env: dict[str, str] | None = None) -> str:
    return _run(
        ["git", "-C", str(repo_root), *args],
        cwd=repo_root,
        env=env,
        label=f"git {' '.join(args)}",
    ).stdout.strip()


def _path_is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _require_workspace_id(value: str) -> str:
    normalized = value.strip().lower()
    if (
        not WORKSPACE_ID_PATTERN.fullmatch(normalized)
        or ".." in normalized
        or normalized in {".", "..", ".git"}
    ):
        raise LocalValidationReplayWorkspaceError(
            "local validation replay workspace id must be a traceable lowercase "
            "task/run id without traversal"
        )
    return normalized


def _system_temp_root_for_audit() -> Path:
    if os.name != "nt":
        raise LocalValidationReplayWorkspaceError(
            "local validation replay F routing is supported only on Windows"
        )
    buffer = ctypes.create_unicode_buffer(32768)
    length = ctypes.windll.kernel32.GetTempPathW(len(buffer), buffer)
    if length == 0 or length >= len(buffer):
        raise LocalValidationReplayWorkspaceError(
            "cannot resolve Windows system Temp for no-fallback audit"
        )
    return Path(buffer.value).resolve()


def _forbidden_system_temp_entries(system_temp: Path) -> list[str]:
    if not system_temp.is_dir():
        raise LocalValidationReplayWorkspaceError(
            f"Windows system Temp is unavailable for no-fallback audit: {system_temp}"
        )
    return sorted(
        (
            str(child.resolve(strict=False))
            for child in system_temp.iterdir()
            if any(
                child.name.lower().startswith(prefix)
                for prefix in FORBIDDEN_SYSTEM_TEMP_PREFIXES
            )
            or child.name.lower() in FORBIDDEN_SYSTEM_TEMP_EXACT_NAMES
        ),
        key=str.casefold,
    )


def plan_workspace(
    repo_root: Path, workspace_id: str
) -> LocalReplayWorkspacePaths:
    repo_root = repo_root.resolve()
    approved_root = git_worktree_safety.approved_local_validation_replay_root(
        repo_root
    )
    workspace_id = _require_workspace_id(workspace_id)
    workspace_root = approved_root / workspace_id
    if not _path_is_within(workspace_root, approved_root):
        raise LocalValidationReplayWorkspaceError(
            "local validation replay workspace escaped the approved F root"
        )
    runner_temp_root = workspace_root / "runner-temp"
    render_root = workspace_root / "pdf-render"
    evidence_root = workspace_root / "evidence"
    return LocalReplayWorkspacePaths(
        workspace_root=workspace_root,
        source_root=workspace_root / "full-source",
        runner_temp_root=runner_temp_root,
        synthetic_git_root=(runner_temp_root / "price-history-extension.git-dir"),
        synthetic_index_path=(runner_temp_root / "price-history-extension.git-index"),
        synthetic_pathspec_path=(runner_temp_root / "price-history-extension-paths.bin"),
        render_root=render_root,
        extract_root=render_root / "visual_evidence",
        evidence_root=evidence_root,
        checkpoint_input_root=evidence_root / "checkpoint-input",
        post_checkpoint_root=evidence_root / "post-validation-checkpoint",
        manifest_path=evidence_root / WORKSPACE_MANIFEST,
        manifest_sha_path=evidence_root / WORKSPACE_MANIFEST_SHA,
    )


def _write_failure_evidence(
    paths: LocalReplayWorkspacePaths,
    *,
    source_ref: str,
    error: BaseException,
) -> None:
    try:
        paths.evidence_root.mkdir(parents=True, exist_ok=True)
        failure_path = paths.evidence_root / "workspace_failure.json"
        failure_path.write_bytes(
            canonical_json_bytes(
                {
                    "schema_version": 1,
                    "status": "failed_closed",
                    "source_ref": source_ref,
                    "error_type": type(error).__name__,
                    "error": str(error),
                    "production_not_run": True,
                    "official_pdf_published": False,
                    "c_temp_fallback_used": False,
                }
            )
        )
    except OSError:
        pass


def create_workspace(
    repo_root: Path,
    *,
    source_ref: str,
    workspace_id: str,
) -> tuple[LocalReplayWorkspacePaths, str]:
    repo_root = repo_root.resolve()
    paths = plan_workspace(repo_root, workspace_id)
    if paths.workspace_root.exists():
        raise LocalValidationReplayWorkspaceError(
            "local validation replay workspace collision; workspace ids are "
            f"single-use: {paths.workspace_root}"
        )
    paths.workspace_root.mkdir()
    paths.runner_temp_root.mkdir()
    paths.evidence_root.mkdir()
    try:
        source_sha = _git(repo_root, "rev-parse", "--verify", source_ref)
        git_worktree_safety.create_registered_full_local_validation_replay_worktree(
            repo_root,
            source_sha,
            paths.source_root,
            consumer_id=CONSUMER_ID,
        )
        observed_head = _git(paths.source_root, "rev-parse", "HEAD")
        status = _git(
            paths.source_root,
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
        )
        if observed_head != source_sha or status:
            raise LocalValidationReplayWorkspaceError(
                "full replay source materialization is not exact and clean"
            )
        prepared = {
            "schema_version": 1,
            "status": "prepared",
            "source_ref": source_ref,
            "source_sha": source_sha,
            "paths": paths.canonical_strings(),
            "production_not_run": True,
            "official_pdf_published": False,
            "c_temp_fallback_used": False,
        }
        _write_manifest(paths, prepared)
        return paths, source_sha
    except BaseException as error:
        _write_failure_evidence(paths, source_ref=source_ref, error=error)
        raise


def build_replay_command(
    paths: LocalReplayWorkspacePaths,
    *,
    source_sha: str,
    run_id: str,
    checkpoint_run_id: str,
    checkpoint_source_sha: str,
    checkpoint_artifact_id: str,
    checkpoint_artifact_digest: str,
) -> list[str]:
    return [
        sys.executable,
        "-B",
        str(paths.source_root / RUNNER_RELATIVE_PATH),
        "replay",
        "--repo-root",
        str(paths.source_root),
        "--runner-temp",
        str(paths.runner_temp_root),
        "--replay-date",
        REPLAY_DATE,
        "--source-sha",
        source_sha,
        "--run-id",
        run_id,
        "--bundle-dir",
        str(paths.checkpoint_input_root),
        "--checkpoint-run-id",
        checkpoint_run_id,
        "--checkpoint-source-sha",
        checkpoint_source_sha,
        "--checkpoint-artifact-id",
        checkpoint_artifact_id,
        "--checkpoint-artifact-digest",
        checkpoint_artifact_digest,
        "--post-bundle-dir",
        str(paths.post_checkpoint_root),
    ]


def build_render_command(
    paths: LocalReplayWorkspacePaths,
    *,
    source_sha: str,
    run_id: str,
) -> list[str]:
    return [
        sys.executable,
        "-B",
        str(paths.source_root / RUNNER_RELATIVE_PATH),
        "render-pdfs",
        "--repo-root",
        str(paths.source_root),
        "--runner-temp",
        str(paths.runner_temp_root),
        "--replay-date",
        REPLAY_DATE,
        "--source-sha",
        source_sha,
        "--run-id",
        run_id,
        "--bundle-dir",
        str(paths.post_checkpoint_root),
        "--output-dir",
        str(paths.render_root),
    ]


def _is_reparse_path(path: Path) -> bool:
    attributes = getattr(path.lstat(), "st_file_attributes", 0)
    reparse_attribute = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    return path.is_symlink() or bool(attributes & reparse_attribute)


def _require_no_reparse_tree(root: Path) -> None:
    if not root.is_dir() or _is_reparse_path(root):
        raise LocalValidationReplayWorkspaceError(
            f"checkpoint source must be a real directory: {root}"
        )
    for path in root.rglob("*"):
        if _is_reparse_path(path):
            raise LocalValidationReplayWorkspaceError(
                f"checkpoint source contains a reparse path: {path}"
            )


def _require_checkpoint_bundle_outside_system_temp(
    checkpoint_bundle: Path,
) -> None:
    system_temp = _system_temp_root_for_audit()
    if _path_is_within(checkpoint_bundle.resolve(), system_temp):
        raise LocalValidationReplayWorkspaceError(
            "checkpoint bundle must not be materialized in Windows system Temp"
        )


def run_local_replay(args: argparse.Namespace) -> int:
    paths, source_sha = create_workspace(
        args.repo_root,
        source_ref=args.source_ref,
        workspace_id=args.workspace_id,
    )
    checkpoint_bundle = args.checkpoint_bundle.resolve()
    _require_checkpoint_bundle_outside_system_temp(checkpoint_bundle)
    _require_no_reparse_tree(checkpoint_bundle)
    shutil.copytree(checkpoint_bundle, paths.checkpoint_input_root)
    _run(
        build_replay_command(
            paths,
            source_sha=source_sha,
            run_id=args.run_id,
            checkpoint_run_id=args.checkpoint_run_id,
            checkpoint_source_sha=args.checkpoint_source_sha,
            checkpoint_artifact_id=args.checkpoint_artifact_id,
            checkpoint_artifact_digest=args.checkpoint_artifact_digest,
        ),
        cwd=paths.source_root,
        label="local validation replay",
    )
    _run(
        build_render_command(paths, source_sha=source_sha, run_id=args.run_id),
        cwd=paths.source_root,
        label="local isolated PDF validation",
    )
    if not paths.extract_root.is_dir():
        raise LocalValidationReplayWorkspaceError(
            "local replay PDF extraction root was not materialized at the contracted F path"
        )
    print(json.dumps(paths.canonical_strings(), ensure_ascii=False, sort_keys=True))
    return 0


def _manifest_entries(
    root: Path,
    *,
    excludes: Iterable[Path] = (),
) -> list[dict[str, Any]]:
    excluded = tuple(path.resolve(strict=False) for path in excludes)
    rows: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*"), key=lambda value: str(value).casefold()):
        absolute = path.resolve(strict=False)
        if any(
            absolute == excluded_path or _path_is_within(absolute, excluded_path)
            for excluded_path in excluded
        ):
            continue
        if _is_reparse_path(path):
            raise LocalValidationReplayWorkspaceError(
                f"pilot manifest encountered a reparse path: {path}"
            )
        if not path.is_file() or path.name == ".git":
            continue
        rows.append(
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return rows


def _prepare_synthetic_git_probe(
    paths: LocalReplayWorkspacePaths, source_sha: str
) -> str:
    _run(
        ["git", "init", "--bare", str(paths.synthetic_git_root)],
        cwd=paths.runner_temp_root,
        label="initialize F-routed synthetic Git repository",
    )
    common_dir = Path(_git(paths.source_root, "rev-parse", "--git-common-dir"))
    if not common_dir.is_absolute():
        common_dir = paths.source_root / common_dir
    alternates = paths.synthetic_git_root / "objects/info/alternates"
    alternates.parent.mkdir(parents=True, exist_ok=True)
    alternates.write_bytes(
        ((common_dir.resolve() / "objects").as_posix() + "\n").encode(
            "utf-8"
        )
    )
    env = os.environ.copy()
    env.update(
        {
            "GIT_DIR": str(paths.synthetic_git_root),
            "GIT_INDEX_FILE": str(paths.synthetic_index_path),
            "GIT_WORK_TREE": str(paths.source_root),
            "GIT_NO_REPLACE_OBJECTS": "1",
        }
    )
    for command, label in (
        (["git", "read-tree", source_sha], "populate F-routed synthetic Git index"),
        (["git", "update-ref", "refs/heads/main", source_sha], "set F-routed synthetic Git main ref"),
        (["git", "symbolic-ref", "HEAD", "refs/heads/main"], "set F-routed synthetic Git HEAD"),
    ):
        _run(command, cwd=paths.source_root, env=env, label=label)
    synthetic_tree = _run(
        ["git", "write-tree"],
        cwd=paths.source_root,
        env=env,
        label="verify F-routed synthetic Git index",
    ).stdout.strip()
    source_tree = _git(paths.source_root, "rev-parse", f"{source_sha}^{{tree}}")
    if synthetic_tree != source_tree:
        raise LocalValidationReplayWorkspaceError(
            "F-routed synthetic Git index tree does not match source tree"
        )
    paths.synthetic_pathspec_path.write_bytes(b"scripts\0tests\0")
    return synthetic_tree


def _write_manifest(
    paths: LocalReplayWorkspacePaths, payload: dict[str, Any]
) -> str:
    paths.manifest_path.write_bytes(canonical_json_bytes(payload))
    digest = sha256_file(paths.manifest_path)
    paths.manifest_sha_path.write_text(digest + "\n", encoding="ascii")
    return digest


def _pilot_categories(
    paths: LocalReplayWorkspacePaths,
) -> dict[str, dict[str, Any]]:
    runner_probe = paths.runner_temp_root / "routing-pilot-runner-temp.txt"
    return {
        "full_source": {
            "root": str(paths.source_root.resolve()),
            "files": _manifest_entries(paths.source_root),
        },
        "synthetic_git_index_objects_metadata": {
            "root": str(paths.runner_temp_root.resolve()),
            "files": _manifest_entries(
                paths.runner_temp_root, excludes=(runner_probe,)
            ),
        },
        "runner_local_temp": {
            "root": str(paths.runner_temp_root.resolve()),
            "files": [
                {
                    "path": runner_probe.name,
                    "bytes": runner_probe.stat().st_size,
                    "sha256": sha256_file(runner_probe),
                }
            ],
        },
        "pdf_test_render": {
            "root": str(paths.render_root.resolve()),
            "files": _manifest_entries(
                paths.render_root, excludes=(paths.extract_root,)
            ),
        },
        "pdf_text_extract": {
            "root": str(paths.extract_root.resolve()),
            "files": _manifest_entries(paths.extract_root),
        },
        "manifest_evidence": {
            "root": str(paths.evidence_root.resolve()),
            "files": _manifest_entries(
                paths.evidence_root,
                excludes=(paths.manifest_path, paths.manifest_sha_path),
            ),
        },
    }


def verify_pilot_manifest(paths: LocalReplayWorkspacePaths) -> dict[str, Any]:
    observed_digest = sha256_file(paths.manifest_path)
    expected_digest = paths.manifest_sha_path.read_text(encoding="ascii").strip()
    if observed_digest != expected_digest:
        raise LocalValidationReplayWorkspaceError(
            "local replay pilot manifest/sidecar SHA mismatch"
        )
    payload = json.loads(paths.manifest_path.read_text(encoding="utf-8"))
    if payload.get("status") != "pilot_verified":
        raise LocalValidationReplayWorkspaceError(
            "local replay pilot manifest status mismatch"
        )
    if payload.get("forbidden_system_temp_replay_paths_after") != []:
        raise LocalValidationReplayWorkspaceError(
            "local replay pilot detected forbidden C Temp materialization"
        )
    if Path(str(payload.get("workspace_root", ""))).resolve(strict=False) != (
        paths.workspace_root.resolve(strict=False)
    ):
        raise LocalValidationReplayWorkspaceError(
            "local replay pilot workspace root drifted"
        )
    if (
        payload.get("source_tree_sha") != payload.get("synthetic_tree_sha")
        or payload.get("production_not_run") is not True
        or payload.get("official_pdf_published") is not False
        or payload.get("repo_artifacts_pushed_by_replay") is not False
        or payload.get("c_temp_fallback_used") is not False
    ):
        raise LocalValidationReplayWorkspaceError(
            "local replay pilot safety identity drifted"
        )
    expected_roots = {
        "full_source": paths.source_root,
        "synthetic_git_index_objects_metadata": paths.runner_temp_root,
        "runner_local_temp": paths.runner_temp_root,
        "pdf_test_render": paths.render_root,
        "pdf_text_extract": paths.extract_root,
        "manifest_evidence": paths.evidence_root,
    }
    if set(payload.get("categories", {})) != set(expected_roots):
        raise LocalValidationReplayWorkspaceError(
            "local replay pilot category set drifted"
        )
    actual_categories = _pilot_categories(paths)
    for category, block in payload.get("categories", {}).items():
        root = Path(str(block.get("root", ""))).resolve(strict=False)
        if root != expected_roots[category].resolve(strict=False):
            raise LocalValidationReplayWorkspaceError(
                f"local replay pilot category root drifted: {category}"
            )
        if block.get("files") != actual_categories[category]["files"]:
            raise LocalValidationReplayWorkspaceError(
                f"pilot manifest path/bytes/SHA set drift: {category}"
            )
        for row in block.get("files", []):
            path = root / Path(str(row["path"]))
            if not _path_is_within(path.resolve(strict=False), root):
                raise LocalValidationReplayWorkspaceError(
                    f"pilot manifest path escaped category {category}: {path}"
                )
            if (
                not path.is_file()
                or path.stat().st_size != int(row["bytes"])
                or sha256_file(path) != row["sha256"]
            ):
                raise LocalValidationReplayWorkspaceError(
                    f"pilot manifest bytes/SHA drift: {category}/{row['path']}"
                )
    return payload


def run_pilot(args: argparse.Namespace) -> int:
    system_temp = _system_temp_root_for_audit()
    before = _forbidden_system_temp_entries(system_temp)
    if before:
        raise LocalValidationReplayWorkspaceError(
            f"pre-existing replay materialization remains in C Temp: {before}"
        )
    paths, source_sha = create_workspace(
        args.repo_root,
        source_ref=args.source_ref,
        workspace_id=args.workspace_id,
    )
    synthetic_tree = _prepare_synthetic_git_probe(paths, source_sha)
    runner_probe = paths.runner_temp_root / "routing-pilot-runner-temp.txt"
    runner_probe.write_text("runner_temp=F_only\n", encoding="utf-8")
    paths.render_root.mkdir()
    render_probe = paths.render_root / "routing-pilot-render.txt"
    render_probe.write_text("pdf_render=isolated_validation_only\n", encoding="utf-8")
    paths.extract_root.mkdir()
    extract_probe = paths.extract_root / "routing-pilot-extract.txt"
    extract_probe.write_text(
        "pdf_text_and_page_extract=isolated_validation_only\n", encoding="utf-8"
    )
    evidence_probe = paths.evidence_root / "routing-pilot-evidence.txt"
    evidence_probe.write_text("manifest_evidence=F_only\n", encoding="utf-8")
    after = _forbidden_system_temp_entries(system_temp)
    categories = _pilot_categories(paths)
    payload = {
        "schema_version": 1,
        "status": "pilot_verified",
        "workspace_id": args.workspace_id,
        "workspace_root": str(paths.workspace_root.resolve()),
        "source_ref": args.source_ref,
        "source_sha": source_sha,
        "source_tree_sha": _git(paths.source_root, "rev-parse", f"{source_sha}^{{tree}}"),
        "synthetic_tree_sha": synthetic_tree,
        "categories": categories,
        "system_temp_root": str(system_temp),
        "forbidden_system_temp_replay_paths_before": before,
        "forbidden_system_temp_replay_paths_after": after,
        "production_not_run": True,
        "official_pdf_published": False,
        "repo_artifacts_pushed_by_replay": False,
        "c_temp_fallback_used": False,
    }
    manifest_sha = _write_manifest(paths, payload)
    verify_pilot_manifest(paths)
    print(json.dumps({"status": "pilot_verified", "workspace_root": str(paths.workspace_root.resolve()), "manifest": str(paths.manifest_path.resolve()), "manifest_sha256": manifest_sha}, ensure_ascii=False, sort_keys=True))
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    subparsers = result.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--repo-root", type=Path, required=True)
    common.add_argument("--source-ref", required=True)
    common.add_argument("--workspace-id", required=True)
    subparsers.add_parser("prepare", parents=[common])
    subparsers.add_parser("pilot", parents=[common])
    replay = subparsers.add_parser("run-replay", parents=[common])
    replay.add_argument("--checkpoint-bundle", type=Path, required=True)
    replay.add_argument("--checkpoint-run-id", required=True)
    replay.add_argument("--checkpoint-source-sha", required=True)
    replay.add_argument("--checkpoint-artifact-id", required=True)
    replay.add_argument("--checkpoint-artifact-digest", required=True)
    replay.add_argument("--run-id", required=True)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.command == "prepare":
        paths, source_sha = create_workspace(
            args.repo_root, source_ref=args.source_ref, workspace_id=args.workspace_id
        )
        print(json.dumps({"source_sha": source_sha, "paths": paths.canonical_strings()}, ensure_ascii=False, sort_keys=True))
        return 0
    if args.command == "pilot":
        return run_pilot(args)
    return run_local_replay(args)


if __name__ == "__main__":
    raise SystemExit(main())
