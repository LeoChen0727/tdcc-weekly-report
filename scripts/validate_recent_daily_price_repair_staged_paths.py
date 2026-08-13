from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_SCHEMA = "daily_source_recovery_bundle_v1"
STATE_SCHEMA = "daily_source_recovery_state_v1"
DATE_RE = re.compile(r"20\d{6}")
SHA1_RE = re.compile(r"[0-9a-f]{40}")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
RELEASE_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{7,127}")
OFFICIAL_TRIPLET = {
    "output/latest/official_daily_price_latest.csv",
    "output/latest/official_price_fetch_latest.json",
    "output/latest/official_price_fetch_latest.md",
}

ALLOWED_EXACT = {
    "data/market_calendar/exceptional_non_trading_days.csv",
    "output/latest/recent_daily_price_gap_repair_latest.json",
    "output/latest/recent_daily_price_gap_repair_latest.md",
    "output/latest/repair_daily_price_range_check_code_latest.csv",
    "output/latest/stock_price_history_manifest.csv",
    "output/latest/stock_price_history_manifest.json",
    "output/latest/stock_price_history_manifest.md",
    "output/latest/daily_price_history_continuity_latest.json",
    "output/latest/daily_price_history_continuity_latest.md",
    "docs/latest/stock_price_history_manifest.csv",
    "docs/latest/stock_price_history_manifest.json",
    "docs/latest/stock_price_history_manifest.md",
}
ALLOWED_PATTERNS = (
    re.compile(r"^data/daily_price/(?:daily_price_)?20\d{6}\.csv$"),
    re.compile(r"^data/stock_price_history/[0-9A-Za-z_-]+\.csv$"),
    re.compile(r"^output/latest/repair_daily_price_range_latest\.(?:csv|json|md)$"),
    re.compile(r"^output/latest/official_daily_price_latest\.csv$"),
    re.compile(r"^output/latest/official_price_fetch_latest\.(?:json|md)$"),
    re.compile(
        r"^output/history/daily_source_bundles/(20\d{6})/"
        r"[A-Za-z0-9][A-Za-z0-9._:-]{7,127}/(?:"
        r"manifest\.json|state\.json|market_session_status\.json|"
        r"files/01-20\d{6}\.csv|files/02-daily_price_20\d{6}\.csv|"
        r"files/03-official_daily_price_latest\.csv|"
        r"files/04-official_price_fetch_latest\.json|"
        r"files/05-official_price_fetch_latest\.md|"
        r"files/06-exceptional_non_trading_days\.csv)$"
    ),
)


def _is_allowed(path: str) -> bool:
    return path in ALLOWED_EXACT or any(pattern.fullmatch(path) for pattern in ALLOWED_PATTERNS)


def validate_entries(entries: list[tuple[str, tuple[str, ...]]]) -> list[str]:
    errors: list[str] = []
    if not entries:
        return ["recent daily-price repair has no staged paths to validate"]
    for status, paths in entries:
        if status not in {"A", "M"}:
            errors.append(
                "recent daily-price repair staged change must be add/modify only: "
                f"status={status} paths={list(paths)}"
            )
            continue
        if len(paths) != 1:
            errors.append(
                "recent daily-price repair staged change has unexpected path arity: "
                f"status={status} paths={list(paths)}"
            )
            continue
        path = paths[0].replace("\\", "/")
        if not _is_allowed(path):
            errors.append(f"recent daily-price repair staged path is not allowed: {path}")
    return errors


def validate_staged_object_identities(
    entries: list[tuple[str, tuple[str, ...]]],
    *,
    read_index_mode: Callable[[str], str],
    read_index_type: Callable[[str], str],
) -> list[str]:
    errors: list[str] = []
    for status, paths in entries:
        if status not in {"A", "M"} or len(paths) != 1:
            continue
        path = paths[0].replace("\\", "/")
        try:
            mode = read_index_mode(path)
            object_type = read_index_type(path)
        except Exception as exc:
            errors.append(
                "recent daily-price repair staged object identity is unreadable: "
                f"{path}: {exc}"
            )
            continue
        if mode != "100644":
            errors.append(
                "recent daily-price repair staged path mode must be 100644: "
                f"path={path} observed={mode}"
            )
        if object_type != "blob":
            errors.append(
                "recent daily-price repair staged path object type must be blob: "
                f"path={path} observed={object_type}"
            )
    return errors


def _json_bytes(payload: dict[str, object]) -> bytes:
    return (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _required_source_paths(target_date: str) -> tuple[str, ...]:
    return (
        f"data/daily_price/{target_date}.csv",
        f"data/daily_price/daily_price_{target_date}.csv",
        "output/latest/official_daily_price_latest.csv",
        "output/latest/official_price_fetch_latest.json",
        "output/latest/official_price_fetch_latest.md",
        "data/market_calendar/exceptional_non_trading_days.csv",
    )


def validate_bundle_identity(
    entries: list[tuple[str, tuple[str, ...]]],
    *,
    target_date: str,
    source_base_sha: str,
    observed_head_sha: str,
    manifest_path: str,
    manifest_sha256: str,
    source_bundle_sha: str,
    read_index_bytes: Callable[[str], bytes],
    read_index_mode: Callable[[str], str],
    read_index_type: Callable[[str], str],
) -> list[str]:
    errors = validate_entries(entries)
    if errors:
        return errors
    errors = validate_staged_object_identities(
        entries,
        read_index_mode=read_index_mode,
        read_index_type=read_index_type,
    )
    if errors:
        return errors
    if not DATE_RE.fullmatch(target_date):
        return ["recent daily-price repair target date is invalid"]
    if not SHA1_RE.fullmatch(source_base_sha):
        return ["recent daily-price repair source base SHA is invalid"]
    if observed_head_sha != source_base_sha:
        return ["recent daily-price repair source base SHA does not equal repository HEAD"]
    if not SHA256_RE.fullmatch(manifest_sha256):
        return ["recent daily-price repair manifest SHA-256 is invalid"]
    if not SHA256_RE.fullmatch(source_bundle_sha):
        return ["recent daily-price repair source bundle SHA-256 is invalid"]

    changed_paths = {
        paths[0].replace("\\", "/") for _status, paths in entries if len(paths) == 1
    }
    try:
        manifest_payload = read_index_bytes(manifest_path)
    except Exception as exc:
        errors.append(f"recent daily-price repair staged manifest is unreadable: {exc}")
        return errors
    if read_index_mode(manifest_path) != "100644":
        errors.append("recent daily-price repair staged manifest mode must be 100644")
    if manifest_path not in changed_paths:
        errors.append("recent daily-price repair manifest is not staged")
    if _sha256(manifest_payload) != manifest_sha256:
        errors.append("recent daily-price repair staged manifest SHA-256 mismatch")
    try:
        manifest = json.loads(manifest_payload.decode("utf-8"))
    except Exception as exc:
        errors.append(f"recent daily-price repair staged manifest JSON is invalid: {exc}")
        return errors
    if not isinstance(manifest, dict):
        return errors + ["recent daily-price repair staged manifest must be an object"]
    if manifest.get("schema_version") != BUNDLE_SCHEMA:
        errors.append("recent daily-price repair staged manifest schema mismatch")
    if manifest.get("trading_date") != target_date:
        errors.append("recent daily-price repair staged manifest target date mismatch")
    if manifest.get("source_base_sha") != source_base_sha:
        errors.append("recent daily-price repair staged manifest source base SHA mismatch")
    release_id = str(manifest.get("release_id") or "")
    if not RELEASE_RE.fullmatch(release_id):
        errors.append("recent daily-price repair staged manifest release id is invalid")
        return errors
    bundle_root = f"output/history/daily_source_bundles/{target_date}/{release_id}"
    expected_manifest_path = f"{bundle_root}/manifest.json"
    if manifest_path != expected_manifest_path:
        errors.append(
            "recent daily-price repair staged manifest path mismatch: "
            f"expected={expected_manifest_path} observed={manifest_path}"
        )
    identity = dict(manifest)
    observed_bundle_sha = str(identity.pop("source_bundle_sha", ""))
    if observed_bundle_sha != source_bundle_sha:
        errors.append("recent daily-price repair staged source bundle SHA mismatch")
    if _sha256(_json_bytes(identity)) != source_bundle_sha:
        errors.append("recent daily-price repair staged source bundle identity mismatch")

    required_paths = _required_source_paths(target_date)
    files = manifest.get("files")
    if (
        not isinstance(files, list)
        or len(files) != len(required_paths)
        or not all(isinstance(item, dict) for item in files)
        or [item.get("path") for item in files] != list(required_paths)
    ):
        errors.append("recent daily-price repair staged bundle file set mismatch")
        return errors
    entries_by_path = {str(item["path"]): item for item in files}
    for index, source_path in enumerate(required_paths, start=1):
        item = entries_by_path[source_path]
        bundle_path = f"{bundle_root}/files/{index:02d}-{Path(source_path).name}"
        if item.get("bundle_path") != bundle_path:
            errors.append(
                f"recent daily-price repair staged bundle path mismatch: {source_path}"
            )
            continue
        if item.get("mode") != "100644":
            errors.append(
                f"recent daily-price repair manifest mode mismatch: {source_path}"
            )
        try:
            source_payload = read_index_bytes(source_path)
            bundle_payload = read_index_bytes(bundle_path)
            source_mode = read_index_mode(source_path)
            bundle_mode = read_index_mode(bundle_path)
        except Exception as exc:
            errors.append(
                f"recent daily-price repair staged bundle payload is unreadable: "
                f"{source_path}: {exc}"
            )
            continue
        if bundle_path not in changed_paths:
            errors.append(
                f"recent daily-price repair bundle payload is not staged: {bundle_path}"
            )
        if source_mode != "100644" or bundle_mode != "100644":
            errors.append(
                f"recent daily-price repair source/bundle mode mismatch: {source_path}"
            )
        if source_payload != bundle_payload:
            errors.append(
                f"recent daily-price repair source/bundle bytes mismatch: {source_path}"
            )
        if (
            int(item.get("bytes") or -1) != len(bundle_payload)
            or item.get("sha256") != _sha256(bundle_payload)
        ):
            errors.append(
                f"recent daily-price repair source/bundle identity mismatch: {source_path}"
            )

    canonical_price_path = f"data/daily_price/daily_price_{target_date}.csv"
    try:
        canonical_price = read_index_bytes(canonical_price_path)
        latest_price = read_index_bytes(
            "output/latest/official_daily_price_latest.csv"
        )
        fetch_payload = read_index_bytes(
            "output/latest/official_price_fetch_latest.json"
        )
        markdown_payload = read_index_bytes(
            "output/latest/official_price_fetch_latest.md"
        )
        fetch_status = json.loads(fetch_payload.decode("utf-8"))
    except Exception as exc:
        errors.append(f"recent daily-price repair official triplet is invalid: {exc}")
        return errors
    if canonical_price != latest_price:
        errors.append("recent daily-price repair official latest price bytes mismatch")
    try:
        rows = list(
            csv.DictReader(io.StringIO(canonical_price.decode("utf-8-sig")))
        )
    except Exception as exc:
        errors.append(f"recent daily-price repair official price CSV is invalid: {exc}")
        rows = []
    market_counts = {"TWSE": 0, "TPEx": 0}
    wrong_date_rows = 0
    invalid_rows = 0
    for row in rows:
        if str(row.get("date") or "").replace("-", "") != target_date:
            wrong_date_rows += 1
            continue
        if not str(row.get("stock_id") or "").strip():
            invalid_rows += 1
            continue
        market_name = str(row.get("market") or "").strip().lower()
        if market_name in {"twse", "listed"}:
            market_counts["TWSE"] += 1
        elif market_name in {"tpex", "otc", "emerging"}:
            market_counts["TPEx"] += 1
        else:
            invalid_rows += 1
    observed_counts = {
        "twse_rows": market_counts["TWSE"],
        "tpex_rows": market_counts["TPEx"],
        "total_rows": market_counts["TWSE"] + market_counts["TPEx"],
        "wrong_date_rows": wrong_date_rows,
    }
    if (
        market_counts["TWSE"] <= 0
        or market_counts["TPEx"] <= 0
        or wrong_date_rows
        or invalid_rows
    ):
        errors.append(
            "recent daily-price repair official price CSV is not exact full-market data: "
            f"TWSE={market_counts['TWSE']} TPEx={market_counts['TPEx']} "
            f"wrong_date_rows={wrong_date_rows} invalid_rows={invalid_rows}"
        )
    expected_status = {
        "target_date": target_date,
        "saved_price_date": target_date,
        "is_target_date": True,
        "full_market_ok": True,
    }
    for field, expected in expected_status.items():
        if fetch_status.get(field) != expected:
            errors.append(
                f"recent daily-price repair official fetch {field} mismatch"
            )
    for field, observed in observed_counts.items():
        if int(fetch_status.get(field) or 0) != observed:
            errors.append(
                f"recent daily-price repair official fetch {field} row count mismatch"
            )
    if (
        int(fetch_status.get("latest_price_bytes") or -1) != len(latest_price)
        or fetch_status.get("latest_price_sha256") != _sha256(latest_price)
        or int(fetch_status.get("fetch_markdown_bytes") or -1)
        != len(markdown_payload)
        or fetch_status.get("fetch_markdown_sha256") != _sha256(markdown_payload)
    ):
        errors.append("recent daily-price repair official triplet identity mismatch")

    confirmation = manifest.get("official_price_confirmation")
    expected_confirmation = {
        "path": canonical_price_path,
        "fetch_status_path": "output/latest/official_price_fetch_latest.json",
        "fetch_markdown_path": "output/latest/official_price_fetch_latest.md",
    }
    if not isinstance(confirmation, dict):
        errors.append("recent daily-price repair staged confirmation is missing")
    else:
        for field, expected in expected_confirmation.items():
            if confirmation.get(field) != expected:
                errors.append(
                    f"recent daily-price repair staged confirmation {field} mismatch"
                )
        confirmation_identities = {
            "price": (canonical_price, "price_bytes", "price_sha256"),
            "fetch status": (
                fetch_payload,
                "fetch_status_bytes",
                "fetch_status_sha256",
            ),
            "fetch markdown": (
                markdown_payload,
                "fetch_markdown_bytes",
                "fetch_markdown_sha256",
            ),
        }
        for label, (payload, bytes_field, sha_field) in confirmation_identities.items():
            if (
                int(confirmation.get(bytes_field) or -1) != len(payload)
                or confirmation.get(sha_field) != _sha256(payload)
            ):
                errors.append(
                    f"recent daily-price repair staged confirmation {label} identity mismatch"
                )
        for field, observed in observed_counts.items():
            if int(confirmation.get(field) or 0) != observed:
                errors.append(
                    f"recent daily-price repair staged confirmation {field} row count mismatch"
                )

    market = manifest.get("market_session")
    market_path = f"{bundle_root}/market_session_status.json"
    try:
        market_payload = read_index_bytes(market_path)
        market_status = json.loads(market_payload.decode("utf-8"))
    except Exception as exc:
        errors.append(f"recent daily-price repair staged market evidence is invalid: {exc}")
        return errors
    if market_path not in changed_paths or read_index_mode(market_path) != "100644":
        errors.append("recent daily-price repair staged market evidence is missing or unsafe")
    required_market = {
        "market_status": "open_confirmed",
        "phase": "confirm",
        "market_session_date": target_date,
        "expected_main_price_date": target_date,
    }
    if (
        not isinstance(market, dict)
        or market.get("bundle_path") != market_path
        or market.get("payload") != market_status
    ):
        errors.append("recent daily-price repair staged market payload mismatch")
    else:
        if (
            market.get("mode") != "100644"
            or int(market.get("bytes") or -1) != len(market_payload)
            or market.get("sha256") != _sha256(market_payload)
        ):
            errors.append("recent daily-price repair staged market identity mismatch")
    for field, expected in required_market.items():
        if market_status.get(field) != expected:
            errors.append(
                f"recent daily-price repair staged market {field} mismatch"
            )

    state_path = f"{bundle_root}/state.json"
    try:
        state = json.loads(read_index_bytes(state_path).decode("utf-8"))
    except Exception as exc:
        errors.append(f"recent daily-price repair staged state is invalid: {exc}")
        return errors
    if state_path not in changed_paths or read_index_mode(state_path) != "100644":
        errors.append("recent daily-price repair staged state is missing or unsafe")
    required_state = {
        "schema_version": STATE_SCHEMA,
        "phase": "bundle_ready",
        "trading_date": target_date,
        "release_id": release_id,
        "source_bundle_sha": source_bundle_sha,
        "source_base_sha": source_base_sha,
    }
    for field, expected in required_state.items():
        if state.get(field) != expected:
            errors.append(f"recent daily-price repair staged state {field} mismatch")
    return errors


def staged_entries() -> list[tuple[str, tuple[str, ...]]]:
    raw = subprocess.check_output(
        ["git", "diff", "--cached", "--name-status", "-z"],
        cwd=ROOT,
    )
    tokens = raw.decode("utf-8", errors="strict").split("\0")
    if tokens and tokens[-1] == "":
        tokens.pop()
    entries: list[tuple[str, tuple[str, ...]]] = []
    index = 0
    while index < len(tokens):
        status_token = tokens[index]
        index += 1
        status = status_token[:1]
        path_count = 2 if status in {"R", "C"} else 1
        if index + path_count > len(tokens):
            raise RuntimeError("malformed staged name-status output")
        paths = tuple(tokens[index : index + path_count])
        index += path_count
        entries.append((status, paths))
    return entries


def unstaged_or_untracked_paths() -> list[str]:
    unstaged = subprocess.check_output(
        ["git", "diff", "--name-only", "-z"],
        cwd=ROOT,
    )
    untracked = subprocess.check_output(
        ["git", "ls-files", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
    )
    paths: set[str] = set()
    for payload in (unstaged, untracked):
        for path in payload.decode("utf-8", errors="strict").split("\0"):
            normalized = path.replace("\\", "/")
            if normalized:
                paths.add(normalized)
    return sorted(paths)


def validate_no_unstaged_or_untracked_paths(paths: list[str]) -> list[str]:
    return [
        "recent daily-price repair has unstaged or untracked output before "
        f"commit: {path}"
        for path in sorted(set(paths))
    ]


def read_staged_bytes(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f":{path}"], cwd=ROOT)


def _read_staged_index_record(path: str) -> tuple[str, str]:
    raw = subprocess.check_output(
        ["git", "ls-files", "--stage", "-z", "--", path], cwd=ROOT
    )
    records = [item for item in raw.decode("utf-8").split("\0") if item]
    if len(records) != 1:
        raise RuntimeError(f"staged path has ambiguous index identity: {path}")
    match = re.fullmatch(r"([0-9]{6}) ([0-9a-f]{40,64}) 0\t(.+)", records[0])
    if not match or match.group(3).replace("\\", "/") != path:
        raise RuntimeError(f"staged path identity is malformed: {path}")
    return match.group(1), match.group(2)


def read_staged_mode(path: str) -> str:
    return _read_staged_index_record(path)[0]


def read_staged_object_type(path: str) -> str:
    object_id = _read_staged_index_record(path)[1]
    return subprocess.check_output(
        ["git", "cat-file", "-t", object_id], cwd=ROOT, text=True
    ).strip()


def repository_head_sha() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate recent repair staged paths and immutable bundle identity."
    )
    parser.add_argument("--target-date", required=True)
    parser.add_argument("--source-base-sha", required=True)
    parser.add_argument("--manifest-path", required=True)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--source-bundle-sha", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_bundle_identity(
        staged_entries(),
        target_date=args.target_date,
        source_base_sha=args.source_base_sha,
        observed_head_sha=repository_head_sha(),
        manifest_path=args.manifest_path,
        manifest_sha256=args.manifest_sha256,
        source_bundle_sha=args.source_bundle_sha,
        read_index_bytes=read_staged_bytes,
        read_index_mode=read_staged_mode,
        read_index_type=read_staged_object_type,
    )
    errors.extend(
        validate_no_unstaged_or_untracked_paths(unstaged_or_untracked_paths())
    )
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print(
        "[PASS] recent daily-price repair staged paths and immutable bundle "
        "identity are exact"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
