from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import market_session_calendar  # noqa: E402


MARKET_SESSION_PATH = Path("output/latest/market_session_status_latest.json")
FRESHNESS_CSV_PATH = Path("output/latest/data_freshness_latest.csv")
FRESHNESS_MD_PATH = Path("output/latest/data_freshness_latest.md")
RELEASE_MANIFEST_PATH = Path("output/latest/daily_authority_release_latest.json")
TRANSACTION_DIR_PATH = Path("output/latest/.daily_authority_release_transaction")
AUTHORITY_PATHS = (
    MARKET_SESSION_PATH,
    FRESHNESS_CSV_PATH,
    FRESHNESS_MD_PATH,
    RELEASE_MANIFEST_PATH,
)
RELEASE_ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{7,127}")
SHA_PATTERN = re.compile(r"[0-9a-f]{40}")
RELEASE_MARKDOWN_HEADING = "## Daily Authority Release"


class DailyAuthorityReleaseError(RuntimeError):
    pass


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def json_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def read_json(path: Path) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        raise DailyAuthorityReleaseError(f"cannot read JSON authority surface {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise DailyAuthorityReleaseError(f"JSON authority surface must be an object: {path}")
    return payload


def read_single_csv(path: Path) -> tuple[list[str], dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fieldnames = list(reader.fieldnames or [])
            rows = list(reader)
    except Exception as exc:
        raise DailyAuthorityReleaseError(f"cannot read CSV authority surface {path}: {exc}") from exc
    if not fieldnames or len(rows) != 1:
        raise DailyAuthorityReleaseError(
            f"CSV authority surface must contain one row and a header: {path}; rows={len(rows)}"
        )
    return fieldnames, {str(key): str(value or "") for key, value in rows[0].items()}


def csv_bytes(fieldnames: list[str], row: dict[str, str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerow({field: row.get(field, "") for field in fieldnames})
    return b"\xef\xbb\xbf" + buffer.getvalue().encode("utf-8")


def validate_cross_surface_values(
    market: dict[str, object],
    freshness: dict[str, str],
) -> None:
    pairs = {
        "market_session_status": "market_status",
        "market_session_date": "market_session_date",
        "expected_main_price_date": "expected_main_price_date",
        "market_session_reason_code": "reason_code",
        "market_session_generated_at": "generated_at",
    }
    errors = []
    for csv_field, json_field in pairs.items():
        csv_value = str(freshness.get(csv_field) or "").strip()
        json_value = str(market.get(json_field) or "").strip()
        if csv_value != json_value:
            errors.append(f"{csv_field}={csv_value!r} != {json_field}={json_value!r}")
    if errors:
        raise DailyAuthorityReleaseError("daily authority surface mismatch: " + "; ".join(errors))


def render_release_markdown(existing: str, manifest: dict[str, object]) -> bytes:
    marker = "\n" + RELEASE_MARKDOWN_HEADING + "\n"
    base = existing.split(marker, 1)[0].rstrip()
    lines = [
        base,
        "",
        RELEASE_MARKDOWN_HEADING,
        "",
        f"- release_id: `{manifest['release_id']}`",
        f"- generation_id: `{manifest['generation_id']}`",
        f"- producer: `{manifest['producer']}`",
        f"- base_commit_sha: `{manifest['base_commit_sha']}`",
        f"- market_session_date: `{manifest['market_session_date']}`",
        f"- expected_main_price_date: `{manifest['expected_main_price_date']}`",
        f"- market_status: `{manifest['market_status']}`",
        "",
    ]
    return "\n".join(lines).encode("utf-8")


def _write_fsynced(path: Path, payload: bytes) -> None:
    with path.open("wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())


def _fsync_directory(path: Path) -> None:
    if os.name == "nt":
        return
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _fsync_file(path: Path) -> None:
    if os.name == "nt":
        return
    with path.open("rb") as handle:
        os.fsync(handle.fileno())


def _discard_inactive_preparations(root: Path) -> None:
    transaction = root / TRANSACTION_DIR_PATH
    for preparing in transaction.parent.glob(f"{transaction.name}.preparing.*"):
        if preparing.is_symlink() or not preparing.is_dir():
            raise DailyAuthorityReleaseError(f"invalid authority preparation path: {preparing}")
        for child in preparing.iterdir():
            if child.is_symlink() or child.is_dir() or not re.fullmatch(
                r"(?:backup|candidate)-[0-9]+\.bin|journal\.json",
                child.name,
            ):
                raise DailyAuthorityReleaseError(f"unexpected authority preparation content: {child}")
        shutil.rmtree(preparing)
        _fsync_directory(transaction.parent)


def recover_interrupted_authority_release(root: Path) -> bool:
    root = root.resolve()
    transaction = root / TRANSACTION_DIR_PATH
    transaction.parent.mkdir(parents=True, exist_ok=True)
    _discard_inactive_preparations(root)
    if not transaction.exists():
        return False
    if transaction.is_symlink() or not transaction.is_dir():
        raise DailyAuthorityReleaseError(f"invalid authority transaction path: {transaction}")
    journal = read_json(transaction / "journal.json")
    entries = journal.get("entries")
    if journal.get("schema_version") != "daily_authority_transaction_v1" or not isinstance(entries, list):
        raise DailyAuthorityReleaseError("invalid interrupted authority transaction journal")
    expected_paths = {path.as_posix() for path in AUTHORITY_PATHS}
    observed_paths = {str(entry.get("path") or "") for entry in entries if isinstance(entry, dict)}
    if observed_paths != expected_paths or len(entries) != len(expected_paths):
        raise DailyAuthorityReleaseError(
            "interrupted authority transaction path set mismatch: "
            f"expected={sorted(expected_paths)} observed={sorted(observed_paths)}"
        )
    validated: list[tuple[Path, bool, Path | None, int | None]] = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise DailyAuthorityReleaseError("invalid interrupted authority transaction entry")
        relative_path = Path(str(entry["path"]))
        existed = entry.get("existed") is True
        mode_value = entry.get("mode")
        mode = int(mode_value) if mode_value is not None else None
        backup: Path | None = None
        if existed:
            backup = transaction / str(entry.get("backup") or "")
            if not backup.is_file():
                raise DailyAuthorityReleaseError(f"missing authority rollback backup: {relative_path}")
            expected_sha = str(entry.get("backup_sha256") or "")
            observed_sha = sha256_bytes(backup.read_bytes())
            if observed_sha != expected_sha:
                raise DailyAuthorityReleaseError(
                    f"authority rollback backup SHA mismatch: {relative_path}; "
                    f"expected={expected_sha} observed={observed_sha}"
                )
        validated.append((relative_path, existed, backup, mode))
    for relative_path, existed, backup, mode in validated:
        target = root / relative_path
        if existed:
            assert backup is not None
            rollback = target.with_name(f".{target.name}.{uuid.uuid4().hex}.rollback")
            _write_fsynced(rollback, backup.read_bytes())
            if mode is not None:
                os.chmod(rollback, mode)
            os.replace(rollback, target)
            _fsync_directory(target.parent)
        else:
            target.unlink(missing_ok=True)
    shutil.rmtree(transaction)
    _fsync_directory(transaction.parent)
    return True


def atomic_replace_many(
    root: Path,
    payloads: dict[Path, bytes],
    *,
    fail_after_replace: int = 0,
    replace: Callable[[Path, Path], None] | None = None,
    post_replace_validate: Callable[[], None] | None = None,
) -> None:
    if set(payloads) != set(AUTHORITY_PATHS):
        raise DailyAuthorityReleaseError("authority transaction payload set must be exact")
    replace = replace or (lambda source, target: os.replace(source, target))
    recover_interrupted_authority_release(root)
    transaction = root / TRANSACTION_DIR_PATH
    preparing = transaction.with_name(f"{transaction.name}.preparing.{uuid.uuid4().hex}")
    if transaction.exists() or any(transaction.parent.glob(f"{transaction.name}.preparing.*")):
        raise DailyAuthorityReleaseError("authority transaction workspace collision")
    try:
        preparing.mkdir(parents=True, exist_ok=False)
        entries: list[dict[str, object]] = []
        for index, (relative_path, content) in enumerate(payloads.items()):
            target = root / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            existed = target.exists()
            mode = (target.stat().st_mode & 0o777) if existed else None
            backup_name = f"backup-{index}.bin"
            if existed:
                original = target.read_bytes()
                _write_fsynced(preparing / backup_name, original)
                backup_sha = sha256_bytes(original)
            else:
                backup_sha = ""
            candidate_name = f"candidate-{index}.bin"
            _write_fsynced(preparing / candidate_name, content)
            if mode is not None:
                os.chmod(preparing / candidate_name, mode)
                _fsync_file(preparing / candidate_name)
            entries.append(
                {
                    "path": relative_path.as_posix(),
                    "existed": existed,
                    "mode": mode,
                    "backup": backup_name if existed else "",
                    "backup_sha256": backup_sha,
                    "candidate": candidate_name,
                }
            )
        _write_fsynced(
            preparing / "journal.json",
            json_bytes({"schema_version": "daily_authority_transaction_v1", "entries": entries}),
        )
        _fsync_directory(preparing)
        os.replace(preparing, transaction)
        _fsync_directory(transaction.parent)
        for index, relative_path in enumerate(payloads, start=1):
            entry = entries[index - 1]
            replace(transaction / str(entry["candidate"]), root / relative_path)
            _fsync_directory((root / relative_path).parent)
            if fail_after_replace and index == fail_after_replace:
                raise DailyAuthorityReleaseError("injected partial authority release failure")
        if post_replace_validate is not None:
            post_replace_validate()
    except Exception as exc:
        if transaction.exists():
            recover_interrupted_authority_release(root)
        raise
    else:
        shutil.rmtree(transaction)
        _fsync_directory(transaction.parent)
    finally:
        if preparing.exists():
            shutil.rmtree(preparing)


def publish_authority_release(
    root: Path,
    *,
    release_id: str,
    producer: str,
    base_commit_sha: str,
    previous_market: dict[str, object],
    fail_after_replace: int = 0,
    replace: Callable[[Path, Path], None] | None = None,
) -> dict[str, object]:
    root = root.resolve()
    recover_interrupted_authority_release(root)
    if not RELEASE_ID_PATTERN.fullmatch(release_id):
        raise DailyAuthorityReleaseError(f"invalid authority release id: {release_id!r}")
    if not SHA_PATTERN.fullmatch(base_commit_sha):
        raise DailyAuthorityReleaseError(f"invalid authority base commit SHA: {base_commit_sha!r}")
    market = read_json(root / MARKET_SESSION_PATH)
    transition_errors = market_session_calendar.market_session_transition_errors(
        previous_market,
        market,
    )
    if transition_errors:
        raise DailyAuthorityReleaseError("forbidden market-session transition: " + "; ".join(transition_errors))
    fieldnames, freshness = read_single_csv(root / FRESHNESS_CSV_PATH)
    validate_cross_surface_values(market, freshness)

    market["authority_release_id"] = release_id
    market["authority_generation_id"] = release_id
    market["authority_base_commit_sha"] = base_commit_sha
    market["authority_producer"] = producer
    for name in (
        "authority_release_id",
        "authority_generation_id",
        "authority_base_commit_sha",
        "authority_producer",
    ):
        if name not in fieldnames:
            fieldnames.append(name)
        freshness[name] = str(market[name])

    market_payload = json_bytes(market)
    freshness_payload = csv_bytes(fieldnames, freshness)
    manifest: dict[str, object] = {
        "schema_version": "daily_authority_release_v1",
        "release_id": release_id,
        "generation_id": release_id,
        "producer": producer,
        "base_commit_sha": base_commit_sha,
        "transition_baseline": {
            "kind": "git_object",
            "commit_sha": base_commit_sha,
            "path": MARKET_SESSION_PATH.as_posix(),
        },
        "market_session_date": str(market.get("market_session_date") or ""),
        "expected_main_price_date": str(market.get("expected_main_price_date") or ""),
        "market_status": str(market.get("market_status") or ""),
        "reason_code": str(market.get("reason_code") or ""),
        "generated_at": str(market.get("generated_at") or ""),
        "surfaces": {
            MARKET_SESSION_PATH.as_posix(): sha256_bytes(market_payload),
            FRESHNESS_CSV_PATH.as_posix(): sha256_bytes(freshness_payload),
        },
    }
    markdown_existing = (root / FRESHNESS_MD_PATH).read_text(encoding="utf-8-sig")
    markdown_payload = render_release_markdown(markdown_existing, manifest)
    manifest["surfaces"][FRESHNESS_MD_PATH.as_posix()] = sha256_bytes(markdown_payload)  # type: ignore[index]
    payloads = {
        MARKET_SESSION_PATH: market_payload,
        FRESHNESS_CSV_PATH: freshness_payload,
        FRESHNESS_MD_PATH: markdown_payload,
        RELEASE_MANIFEST_PATH: json_bytes(manifest),
    }
    atomic_replace_many(
        root,
        payloads,
        fail_after_replace=fail_after_replace,
        replace=replace,
        post_replace_validate=lambda: validate_authority_release(
            root,
            expected_release_id=release_id,
            allow_active_transaction=True,
        ),
    )
    validate_authority_release(root, expected_release_id=release_id)
    return manifest


def validate_authority_release(
    root: Path,
    *,
    expected_release_id: str = "",
    allow_active_transaction: bool = False,
) -> dict[str, object]:
    root = root.resolve()
    if not allow_active_transaction and (root / TRANSACTION_DIR_PATH).exists():
        raise DailyAuthorityReleaseError("interrupted authority transaction requires recovery")
    market = read_json(root / MARKET_SESSION_PATH)
    _, freshness = read_single_csv(root / FRESHNESS_CSV_PATH)
    manifest = read_json(root / RELEASE_MANIFEST_PATH)
    validate_cross_surface_values(market, freshness)
    if manifest.get("schema_version") != "daily_authority_release_v1":
        raise DailyAuthorityReleaseError("invalid daily authority release schema version")
    if str(manifest.get("producer") or "") != "daily_full_pipeline":
        raise DailyAuthorityReleaseError("daily authority release producer must be daily_full_pipeline")
    release_id = str(manifest.get("release_id") or "")
    if expected_release_id and release_id != expected_release_id:
        raise DailyAuthorityReleaseError(
            f"authority release id mismatch: expected={expected_release_id!r} observed={release_id!r}"
        )
    identities = {
        release_id,
        str(manifest.get("generation_id") or ""),
        str(market.get("authority_release_id") or ""),
        str(market.get("authority_generation_id") or ""),
        freshness.get("authority_release_id", ""),
        freshness.get("authority_generation_id", ""),
    }
    if len(identities) != 1 or not release_id:
        raise DailyAuthorityReleaseError(f"authority release identity mismatch: {sorted(identities)}")
    if str(manifest.get("base_commit_sha") or "") != str(market.get("authority_base_commit_sha") or ""):
        raise DailyAuthorityReleaseError("authority base commit SHA differs between manifest and market surface")
    if freshness.get("authority_base_commit_sha", "") != str(manifest.get("base_commit_sha") or ""):
        raise DailyAuthorityReleaseError("authority base commit SHA differs between manifest and freshness surface")
    expected_baseline = {
        "kind": "git_object",
        "commit_sha": str(manifest.get("base_commit_sha") or ""),
        "path": MARKET_SESSION_PATH.as_posix(),
    }
    if manifest.get("transition_baseline") != expected_baseline:
        raise DailyAuthorityReleaseError(
            "authority transition baseline identity mismatch: "
            f"expected={expected_baseline!r} observed={manifest.get('transition_baseline')!r}"
        )
    semantic_values = {
        "producer": str(market.get("authority_producer") or ""),
        "market_session_date": str(market.get("market_session_date") or ""),
        "expected_main_price_date": str(market.get("expected_main_price_date") or ""),
        "market_status": str(market.get("market_status") or ""),
        "reason_code": str(market.get("reason_code") or ""),
        "generated_at": str(market.get("generated_at") or ""),
    }
    for key, expected in semantic_values.items():
        observed = str(manifest.get(key) or "")
        if observed != expected:
            raise DailyAuthorityReleaseError(
                f"authority manifest semantic mismatch: {key} expected={expected!r} observed={observed!r}"
            )
    if freshness.get("authority_producer", "") != semantic_values["producer"]:
        raise DailyAuthorityReleaseError("authority producer differs between manifest and freshness surface")
    expected_surfaces = manifest.get("surfaces")
    if not isinstance(expected_surfaces, dict):
        raise DailyAuthorityReleaseError("authority release manifest surfaces must be an object")
    expected_surface_paths = {
        MARKET_SESSION_PATH.as_posix(),
        FRESHNESS_CSV_PATH.as_posix(),
        FRESHNESS_MD_PATH.as_posix(),
    }
    if set(expected_surfaces) != expected_surface_paths:
        raise DailyAuthorityReleaseError(
            "authority release manifest surface set mismatch: "
            f"expected={sorted(expected_surface_paths)} observed={sorted(expected_surfaces)}"
        )
    for relative_path in (MARKET_SESSION_PATH, FRESHNESS_CSV_PATH, FRESHNESS_MD_PATH):
        observed = sha256_bytes((root / relative_path).read_bytes())
        expected = str(expected_surfaces.get(relative_path.as_posix()) or "")
        if observed != expected:
            raise DailyAuthorityReleaseError(
                f"authority surface SHA mismatch: {relative_path.as_posix()} expected={expected} observed={observed}"
            )
    return manifest


def git_show_json(root: Path, revision: str, path: Path) -> dict[str, object]:
    if not SHA_PATTERN.fullmatch(revision):
        raise DailyAuthorityReleaseError(f"invalid Git revision for authority baseline: {revision!r}")
    result = subprocess.run(
        ["git", "show", f"{revision}:{path.as_posix()}"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        raise DailyAuthorityReleaseError(
            f"cannot read authority baseline {revision}:{path.as_posix()}: "
            + result.stderr.decode("utf-8", errors="replace")
        )
    payload = json.loads(result.stdout.decode("utf-8-sig"))
    if not isinstance(payload, dict):
        raise DailyAuthorityReleaseError("authority baseline JSON must be an object")
    return payload


def git_head_sha(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    head = result.stdout.strip()
    if not SHA_PATTERN.fullmatch(head):
        raise DailyAuthorityReleaseError(f"invalid repository HEAD SHA: {head!r}")
    return head


def validate_staged_authority_release(root: Path, *, expected_release_id: str) -> None:
    root = root.resolve()
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    staged = {item for item in result.stdout.decode("utf-8").split("\0") if item}
    required = {path.as_posix() for path in AUTHORITY_PATHS}
    touched = staged & required
    if touched != required:
        raise DailyAuthorityReleaseError(
            "daily authority release must stage all authority surfaces in one commit: "
            f"required={sorted(required)} observed={sorted(touched)}"
        )
    manifest = validate_authority_release(root, expected_release_id=expected_release_id)
    head = git_head_sha(root)
    if str(manifest.get("base_commit_sha") or "") != head:
        raise DailyAuthorityReleaseError(
            "staged authority release base SHA must equal current HEAD: "
            f"manifest={manifest.get('base_commit_sha')!r} head={head!r}"
        )
    previous_market = git_show_json(root, head, MARKET_SESSION_PATH)
    current_market = read_json(root / MARKET_SESSION_PATH)
    transition_errors = market_session_calendar.market_session_transition_errors(
        previous_market,
        current_market,
    )
    if transition_errors:
        raise DailyAuthorityReleaseError(
            "staged authority release has forbidden market-session transition: "
            + "; ".join(transition_errors)
        )
    for relative_path in AUTHORITY_PATHS:
        staged_blob = subprocess.run(
            ["git", "show", f":{relative_path.as_posix()}"],
            cwd=root,
            check=True,
            capture_output=True,
        ).stdout
        working = (root / relative_path).read_bytes()
        if staged_blob != working:
            raise DailyAuthorityReleaseError(
                f"staged authority surface differs from working release: {relative_path.as_posix()}"
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish or validate the atomic daily authority release.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    subparsers = parser.add_subparsers(dest="command", required=True)
    publish = subparsers.add_parser("publish")
    publish.add_argument("--release-id", required=True)
    publish.add_argument("--producer", choices=("daily_full_pipeline",), required=True)
    publish.add_argument("--base-sha", required=True)
    validate = subparsers.add_parser("validate")
    validate.add_argument("--expected-release-id", default="")
    staged = subparsers.add_parser("validate-staged")
    staged.add_argument("--expected-release-id", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.repo_root.resolve()
    try:
        if args.command == "publish":
            head = git_head_sha(root)
            if args.base_sha != head:
                raise DailyAuthorityReleaseError(
                    f"authority publish base SHA must equal current HEAD: supplied={args.base_sha} head={head}"
                )
            previous = git_show_json(root, args.base_sha, MARKET_SESSION_PATH)
            publish_authority_release(
                root,
                release_id=args.release_id,
                producer=args.producer,
                base_commit_sha=args.base_sha,
                previous_market=previous,
            )
        elif args.command == "validate":
            validate_authority_release(root, expected_release_id=args.expected_release_id)
        else:
            validate_staged_authority_release(root, expected_release_id=args.expected_release_id)
    except Exception as exc:
        print(f"ERROR: daily authority release failed: {exc}", file=sys.stderr)
        return 1
    print(f"daily authority release {args.command} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
