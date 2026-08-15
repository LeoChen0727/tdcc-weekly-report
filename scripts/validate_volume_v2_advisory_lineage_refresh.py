from __future__ import annotations

import argparse
import csv
from datetime import datetime
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from typing import Any, Iterable


WATCH_CSV = "output/latest/volume_breakout_watch_latest.csv"
WATCH_MD = "output/latest/volume_breakout_watch_latest.md"
WATCH_PACKET_MD = "output/latest/volume_breakout_chatgpt_packet_latest.md"

THEME_LAYER_CSV = "output/latest/volume_attack_theme_layer_latest.csv"
THEME_LAYER_MD = "output/latest/volume_attack_theme_layer_latest.md"
THEME_STOCKS_CSV = "output/latest/volume_attack_theme_stocks_latest.csv"
THEME_STOCKS_MD = "output/latest/volume_attack_theme_stocks_latest.md"

DOCS_THEME_LAYER_CSV = "docs/latest/volume_attack_theme_layer_latest.csv"
DOCS_THEME_LAYER_MD = "docs/latest/volume_attack_theme_layer_latest.md"
DOCS_THEME_STOCKS_CSV = "docs/latest/volume_attack_theme_stocks_latest.csv"
DOCS_THEME_STOCKS_MD = "docs/latest/volume_attack_theme_stocks_latest.md"

VALIDATION_JSON = "output/latest/volume_attack_theme_layer_validation_latest.json"
VALIDATION_MD = "output/latest/volume_attack_theme_layer_validation_latest.md"

TEMPORARY_ALLOWLIST = frozenset(
    {
        WATCH_CSV,
        WATCH_MD,
        WATCH_PACKET_MD,
        THEME_LAYER_CSV,
        THEME_LAYER_MD,
        THEME_STOCKS_CSV,
        THEME_STOCKS_MD,
        DOCS_THEME_LAYER_CSV,
        DOCS_THEME_LAYER_MD,
        DOCS_THEME_STOCKS_CSV,
        DOCS_THEME_STOCKS_MD,
        VALIDATION_JSON,
        VALIDATION_MD,
    }
)

FINAL_EXPECTED_DIFF = frozenset(
    {
        WATCH_CSV,
        THEME_LAYER_MD,
        THEME_STOCKS_CSV,
        THEME_STOCKS_MD,
        DOCS_THEME_LAYER_MD,
        DOCS_THEME_STOCKS_CSV,
        DOCS_THEME_STOCKS_MD,
    }
)

POST_BUILD_METADATA_ONLY = frozenset(
    {
        WATCH_MD,
        WATCH_PACKET_MD,
        VALIDATION_JSON,
        VALIDATION_MD,
    }
)

THEME_LAYER_CSV_PATHS = (THEME_LAYER_CSV, DOCS_THEME_LAYER_CSV)
THEME_MARKDOWN_PATHS = (THEME_LAYER_MD, DOCS_THEME_LAYER_MD)
THEME_STOCK_MARKDOWN_PATHS = (THEME_STOCKS_MD, DOCS_THEME_STOCKS_MD)

WATCH_LINEAGE_COLUMN = "advisory_score_source_sha256"
EXPECTED_WATCH_ROWS = 13
THEME_STOCK_LINEAGE_COLUMNS = frozenset(
    {"advisory_score_source_sha256", "volume_watch_source_sha256"}
)
HEX_SHA256_RE = re.compile(r"[0-9a-f]{64}")
FULL_COMMIT_RE = re.compile(r"[0-9a-fA-F]{40}")
TEXT_METADATA_RE = re.compile(
    r"^(?P<prefix>\s*(?:[-*]\s*)?(?P<key>generated_at|validated_at)\s*:\s*)"
    r"(?P<value>.*?)(?P<ending>\r?\n)?$"
)


class GitError(RuntimeError):
    pass


def _git(
    repo_root: Path,
    *args: str,
    check: bool = True,
) -> subprocess.CompletedProcess[bytes]:
    proc = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).decode("utf-8", errors="replace").strip()
        raise GitError(f"git {' '.join(args)} failed: {detail or proc.returncode}")
    return proc


def _z_paths(payload: bytes) -> set[str]:
    return {
        item.decode("utf-8", errors="surrogateescape").replace("\\", "/")
        for item in payload.split(b"\0")
        if item
    }


def _working_changes(repo_root: Path, base_sha: str) -> set[str]:
    tracked = _z_paths(
        _git(
            repo_root,
            "diff",
            "--name-only",
            "-z",
            "--no-renames",
            base_sha,
            "--",
        ).stdout
    )
    untracked = _z_paths(
        _git(repo_root, "ls-files", "--others", "--exclude-standard", "-z").stdout
    )
    return tracked | untracked


def _staged_changes(repo_root: Path, base_sha: str) -> set[str]:
    return _z_paths(
        _git(
            repo_root,
            "diff",
            "--cached",
            "--name-only",
            "-z",
            "--no-renames",
            base_sha,
            "--",
        ).stdout
    )


def _index_changes_from_head(repo_root: Path) -> set[str]:
    return _z_paths(
        _git(
            repo_root,
            "diff",
            "--cached",
            "--name-only",
            "-z",
            "--no-renames",
            "--",
        ).stdout
    )


def _revision_changes(repo_root: Path, base_sha: str, head_sha: str) -> set[str]:
    return _z_paths(
        _git(
            repo_root,
            "diff",
            "--name-only",
            "-z",
            "--no-renames",
            base_sha,
            head_sha,
            "--",
        ).stdout
    )


def _unstaged_changes(repo_root: Path) -> set[str]:
    return _z_paths(
        _git(
            repo_root,
            "diff",
            "--name-only",
            "-z",
            "--no-renames",
            "--",
        ).stdout
    )


def _name_status(
    repo_root: Path,
    base_sha: str,
    *,
    staged: bool,
) -> list[tuple[str, tuple[str, ...]]]:
    args = ["diff"]
    if staged:
        args.append("--cached")
    args.extend(("--name-status", "--find-renames", base_sha, "--"))
    payload = _git(repo_root, *args).stdout.decode("utf-8", errors="surrogateescape")
    result: list[tuple[str, tuple[str, ...]]] = []
    for line in payload.splitlines():
        fields = line.split("\t")
        if len(fields) < 2 or not fields[0]:
            raise GitError(f"malformed git name-status output: {line!r}")
        result.append((fields[0], tuple(field.replace("\\", "/") for field in fields[1:])))
    return result


def _revision_name_status(
    repo_root: Path,
    base_sha: str,
    head_sha: str,
) -> list[tuple[str, tuple[str, ...]]]:
    payload = _git(
        repo_root,
        "diff",
        "--name-status",
        "--find-renames",
        base_sha,
        head_sha,
        "--",
    ).stdout.decode("utf-8", errors="surrogateescape")
    result: list[tuple[str, tuple[str, ...]]] = []
    for line in payload.splitlines():
        fields = line.split("\t")
        if len(fields) < 2 or not fields[0]:
            raise GitError(f"malformed git revision name-status output: {line!r}")
        result.append((fields[0], tuple(field.replace("\\", "/") for field in fields[1:])))
    return result


def _staged_mode_type_errors(repo_root: Path, paths: Iterable[str]) -> list[str]:
    errors: list[str] = []
    for relative_path in sorted(paths):
        payload = _git(repo_root, "ls-files", "--stage", "-z", "--", relative_path).stdout
        records = [record for record in payload.split(b"\0") if record]
        if len(records) != 1:
            errors.append(
                f"staged path must have exactly one index entry: path={relative_path} "
                f"entries={len(records)}"
            )
            continue
        try:
            metadata, encoded_path = records[0].split(b"\t", 1)
            mode, object_id, stage = metadata.decode("ascii").split()
            indexed_path = encoded_path.decode("utf-8", errors="surrogateescape").replace(
                "\\", "/"
            )
        except (ValueError, UnicodeDecodeError) as exc:
            errors.append(f"malformed staged index entry for {relative_path}: {exc}")
            continue
        if indexed_path != relative_path:
            errors.append(
                f"staged index path mismatch: expected={relative_path} actual={indexed_path}"
            )
        if mode != "100644" or stage != "0":
            errors.append(
                f"staged path must be stage-0 mode 100644 regular file: path={relative_path} "
                f"mode={mode} stage={stage}"
            )
        object_type = _git(repo_root, "cat-file", "-t", object_id, check=False)
        observed_type = object_type.stdout.decode("ascii", errors="replace").strip()
        if object_type.returncode != 0 or observed_type != "blob":
            errors.append(
                f"staged path must reference a blob: path={relative_path} "
                f"object={object_id} type={observed_type or 'unavailable'}"
            )
    return errors


def _committed_mode_type_errors(
    repo_root: Path,
    head_sha: str,
    paths: Iterable[str],
) -> list[str]:
    errors: list[str] = []
    for relative_path in sorted(paths):
        payload = _git(repo_root, "ls-tree", "-z", head_sha, "--", relative_path).stdout
        records = [record for record in payload.split(b"\0") if record]
        if len(records) != 1:
            errors.append(
                f"committed path must have exactly one tree entry: path={relative_path} "
                f"entries={len(records)}"
            )
            continue
        try:
            metadata, encoded_path = records[0].split(b"\t", 1)
            mode, tree_type, object_id = metadata.decode("ascii").split()
            tree_path = encoded_path.decode("utf-8", errors="surrogateescape").replace(
                "\\", "/"
            )
        except (ValueError, UnicodeDecodeError) as exc:
            errors.append(f"malformed committed tree entry for {relative_path}: {exc}")
            continue
        if tree_path != relative_path:
            errors.append(
                f"committed tree path mismatch: expected={relative_path} actual={tree_path}"
            )
        if mode != "100644" or tree_type != "blob":
            errors.append(
                f"committed path must be mode 100644 blob: path={relative_path} "
                f"mode={mode} type={tree_type}"
            )
        object_type = _git(repo_root, "cat-file", "-t", object_id, check=False)
        observed_type = object_type.stdout.decode("ascii", errors="replace").strip()
        if object_type.returncode != 0 or observed_type != "blob":
            errors.append(
                f"committed path must reference a blob object: path={relative_path} "
                f"object={object_id} type={observed_type or 'unavailable'}"
            )
    return errors


def _base_blob(repo_root: Path, base_sha: str, relative_path: str) -> bytes:
    proc = _git(repo_root, "show", f"{base_sha}:{relative_path}", check=False)
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).decode("utf-8", errors="replace").strip()
        raise GitError(f"base blob unavailable: path={relative_path} detail={detail}")
    return proc.stdout


def _current_blob(repo_root: Path, relative_path: str) -> bytes:
    path = repo_root / Path(*PurePosixPath(relative_path).parts)
    if not path.is_file():
        raise OSError(f"current artifact is missing or not a file: {relative_path}")
    return path.read_bytes()


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _read_csv_bytes(payload: bytes, label: str) -> tuple[list[str], list[dict[str, str]]]:
    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{label} is not valid UTF-8: {exc}") from exc
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if reader.fieldnames is None:
        raise ValueError(f"{label} has no CSV header")
    if len(reader.fieldnames) != len(set(reader.fieldnames)):
        raise ValueError(f"{label} has duplicate CSV columns")
    try:
        rows = list(reader)
    except csv.Error as exc:
        raise ValueError(f"{label} is malformed CSV: {exc}") from exc
    if any(None in row for row in rows):
        raise ValueError(f"{label} contains a row wider than its header")
    return list(reader.fieldnames), rows


def _compare_csv_except(
    base_payload: bytes,
    current_payload: bytes,
    *,
    label: str,
    allowed_columns: frozenset[str],
) -> tuple[list[str], list[dict[str, str]], list[dict[str, str]]]:
    errors: list[str] = []
    try:
        base_columns, base_rows = _read_csv_bytes(base_payload, f"base {label}")
        current_columns, current_rows = _read_csv_bytes(current_payload, f"current {label}")
    except ValueError as exc:
        return [str(exc)], [], []

    if base_columns != current_columns:
        errors.append(
            f"{label} column/order drift: expected={base_columns!r} actual={current_columns!r}"
        )
        return errors, base_rows, current_rows
    missing_allowed = sorted(allowed_columns - set(current_columns))
    if missing_allowed:
        errors.append(f"{label} missing lineage columns: {missing_allowed}")
    if len(base_rows) != len(current_rows):
        errors.append(
            f"{label} row-count drift: expected={len(base_rows)} actual={len(current_rows)}"
        )
        return errors, base_rows, current_rows

    compared_columns = [column for column in current_columns if column not in allowed_columns]
    for row_number, (base_row, current_row) in enumerate(
        zip(base_rows, current_rows, strict=True), start=2
    ):
        for column in compared_columns:
            if base_row.get(column, "") != current_row.get(column, ""):
                errors.append(
                    f"{label} business/order drift: row={row_number} column={column} "
                    f"expected={base_row.get(column, '')!r} actual={current_row.get(column, '')!r}"
                )
    return errors, base_rows, current_rows


def _strict_calendar_date(value: object) -> str:
    raw = str(value).strip()
    for date_format in ("%Y%m%d", "%Y-%m-%d"):
        try:
            parsed = datetime.strptime(raw, date_format)
        except ValueError:
            continue
        if parsed.strftime(date_format) == raw and parsed.strftime("%Y").startswith("20"):
            return parsed.strftime("%Y%m%d")
    return ""


def _canonical_csv_slice_sha256(path: Path, as_of_date: str) -> str:
    normalized_as_of = _strict_calendar_date(as_of_date)
    if not normalized_as_of:
        raise ValueError(f"advisory score source as-of date is invalid: {as_of_date!r}")
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"advisory score source cannot be read: {path.as_posix()}: {exc}") from exc
    canonical_text = text.replace("\r\n", "\n").replace("\r", "\n")
    try:
        rows = list(csv.reader(io.StringIO(canonical_text, newline=""), strict=True))
    except csv.Error as exc:
        raise ValueError(
            f"advisory score source CSV is invalid: {path.as_posix()}: {exc}"
        ) from exc
    if not rows:
        raise ValueError(f"advisory score source CSV is empty: {path.as_posix()}")
    header = rows[0]
    if header.count("date") != 1:
        raise ValueError(
            "advisory score source CSV must contain exactly one date column: "
            f"{path.as_posix()} count={header.count('date')}"
        )
    date_index = header.index("date")
    selected_rows = [header]
    exact_as_of_count = 0
    previous_date = ""
    for line_number, values in enumerate(rows[1:], start=2):
        if len(values) != len(header):
            raise ValueError(
                "advisory score source CSV field count mismatch: "
                f"{path.as_posix()} line={line_number} "
                f"expected={len(header)} actual={len(values)}"
            )
        row_date = _strict_calendar_date(values[date_index])
        if not row_date:
            raise ValueError(
                "advisory score source CSV row date is invalid: "
                f"{path.as_posix()} line={line_number} value={values[date_index]!r}"
            )
        if row_date <= normalized_as_of:
            if previous_date and row_date <= previous_date:
                raise ValueError(
                    "advisory score source CSV dates through as-of must be strictly "
                    "increasing and unique: "
                    f"{path.as_posix()} line={line_number} "
                    f"previous={previous_date} actual={row_date}"
                )
            canonical_values = list(values)
            canonical_values[date_index] = row_date
            selected_rows.append(canonical_values)
            previous_date = row_date
            exact_as_of_count += int(row_date == normalized_as_of)
    if exact_as_of_count != 1:
        raise ValueError(
            "advisory score source CSV must contain exactly one as-of row: "
            f"{path.as_posix()} as_of={normalized_as_of} count={exact_as_of_count}"
        )
    buffer = io.StringIO(newline="")
    csv.writer(buffer, lineterminator="\n").writerows(selected_rows)
    return _sha256(buffer.getvalue().encode("utf-8"))


def _canonical_price_path(row: dict[str, str], row_number: int) -> tuple[str | None, str | None]:
    stock_id = str(row.get("stock_id", "")).strip()
    source = str(row.get("advisory_score_source_artifact", "")).strip().replace("\\", "/")
    if not stock_id:
        return None, f"watch row={row_number} has blank stock_id"
    expected = f"data/stock_price_history/{stock_id}.csv"
    if source != expected:
        return None, (
            f"watch row={row_number} stock_id={stock_id} has non-canonical source artifact: "
            f"expected={expected!r} actual={source!r}"
        )
    parts = PurePosixPath(source).parts
    if len(parts) != 3 or parts[:2] != ("data", "stock_price_history"):
        return None, f"watch row={row_number} has unsafe canonical source path: {source!r}"
    return source, None


def _validate_watch_lineage(
    repo_root: Path,
    rows: list[dict[str, str]],
) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    by_stock: dict[str, str] = {}
    for row_number, row in enumerate(rows, start=2):
        stock_id = str(row.get("stock_id", "")).strip()
        source, source_error = _canonical_price_path(row, row_number)
        if source_error:
            errors.append(source_error)
            continue
        assert source is not None
        if stock_id in by_stock:
            errors.append(f"watch contains duplicate stock_id: {stock_id}")
            continue
        signal_date = _strict_calendar_date(row.get("signal_date", ""))
        advisory_as_of = _strict_calendar_date(row.get("advisory_score_as_of", ""))
        if not signal_date:
            errors.append(
                f"watch row={row_number} stock_id={stock_id} has missing/invalid signal_date: "
                f"{row.get('signal_date', '')!r}"
            )
            continue
        if not advisory_as_of:
            errors.append(
                f"watch row={row_number} stock_id={stock_id} has missing/invalid "
                f"advisory_score_as_of: {row.get('advisory_score_as_of', '')!r}"
            )
            continue
        if advisory_as_of != signal_date:
            errors.append(
                f"watch row={row_number} stock_id={stock_id} advisory_score_as_of must "
                f"equal signal_date after normalization: advisory_score_as_of={advisory_as_of} "
                f"signal_date={signal_date}"
            )
            continue
        try:
            source_path = repo_root / Path(*PurePosixPath(source).parts)
            canonical_sha = _canonical_csv_slice_sha256(
                source_path, str(row.get("advisory_score_as_of", ""))
            )
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(
                f"watch canonical slice invalid: row={row_number} stock_id={stock_id} "
                f"error={exc}"
            )
            continue
        actual_sha = str(row.get(WATCH_LINEAGE_COLUMN, "")).strip().lower()
        if not HEX_SHA256_RE.fullmatch(actual_sha):
            errors.append(
                f"watch row={row_number} stock_id={stock_id} has invalid {WATCH_LINEAGE_COLUMN}: "
                f"{actual_sha!r}"
            )
            continue
        if actual_sha != canonical_sha:
            errors.append(
                f"watch canonical SHA mismatch: row={row_number} stock_id={stock_id} "
                f"expected={canonical_sha} actual={actual_sha}"
            )
        by_stock[stock_id] = actual_sha
    return errors, by_stock


def _validate_theme_stock_lineage(
    rows: list[dict[str, str]],
    *,
    watch_by_stock: dict[str, str],
    watch_sha256: str,
) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        stock_id = str(row.get("stock_id", "")).strip()
        if not stock_id:
            errors.append(f"theme stocks row={row_number} has blank stock_id")
            continue
        if stock_id in seen:
            errors.append(f"theme stocks contains duplicate stock_id: {stock_id}")
        seen.add(stock_id)

        expected_price_sha = watch_by_stock.get(stock_id)
        actual_price_sha = str(row.get("advisory_score_source_sha256", "")).strip().lower()
        if expected_price_sha is None:
            errors.append(
                f"theme stocks row={row_number} stock_id={stock_id} is absent from current watch"
            )
        elif actual_price_sha != expected_price_sha:
            errors.append(
                f"theme stocks price-lineage mismatch: row={row_number} stock_id={stock_id} "
                f"expected={expected_price_sha} actual={actual_price_sha}"
            )

        watch_artifact = str(row.get("volume_watch_source_artifact", "")).strip().replace(
            "\\", "/"
        )
        if watch_artifact != WATCH_CSV:
            errors.append(
                f"theme stocks watch artifact mismatch: row={row_number} stock_id={stock_id} "
                f"expected={WATCH_CSV!r} actual={watch_artifact!r}"
            )
        actual_watch_sha = str(row.get("volume_watch_source_sha256", "")).strip().lower()
        if actual_watch_sha != watch_sha256:
            errors.append(
                f"theme stocks watch SHA mismatch: row={row_number} stock_id={stock_id} "
                f"expected={watch_sha256} actual={actual_watch_sha}"
            )
    return errors


def _json_without_metadata(value: Any, *, changed_values: list[Any]) -> Any:
    if isinstance(value, dict):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if key in {"generated_at", "validated_at"}:
                changed_values.append(child)
                result[key] = "<metadata-timestamp>"
            else:
                result[key] = _json_without_metadata(child, changed_values=changed_values)
        return result
    if isinstance(value, list):
        return [_json_without_metadata(child, changed_values=changed_values) for child in value]
    return value


def _metadata_only_json_errors(base_payload: bytes, current_payload: bytes, label: str) -> list[str]:
    try:
        base_value = json.loads(base_payload.decode("utf-8-sig"))
        current_value = json.loads(current_payload.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"{label} metadata-only JSON parse failed: {exc}"]
    base_metadata: list[Any] = []
    current_metadata: list[Any] = []
    normalized_base = _json_without_metadata(base_value, changed_values=base_metadata)
    normalized_current = _json_without_metadata(current_value, changed_values=current_metadata)
    errors: list[str] = []
    if normalized_base != normalized_current:
        errors.append(f"{label} changed outside generated_at/validated_at")
    if base_payload != current_payload:
        if len(base_metadata) != len(current_metadata) or not current_metadata:
            errors.append(f"{label} metadata change is not a matched timestamp-field update")
        elif any(not isinstance(value, str) or not value.strip() for value in current_metadata):
            errors.append(f"{label} has blank or non-string generated_at/validated_at")
    return errors


def _metadata_only_text_errors(base_payload: bytes, current_payload: bytes, label: str) -> list[str]:
    try:
        base_lines = base_payload.decode("utf-8-sig").splitlines(keepends=True)
        current_lines = current_payload.decode("utf-8-sig").splitlines(keepends=True)
    except UnicodeDecodeError as exc:
        return [f"{label} metadata-only text parse failed: {exc}"]
    if len(base_lines) != len(current_lines):
        return [f"{label} changed line count outside generated_at/validated_at"]
    errors: list[str] = []
    changed_metadata = 0
    for line_number, (base_line, current_line) in enumerate(
        zip(base_lines, current_lines, strict=True), start=1
    ):
        if base_line == current_line:
            continue
        base_match = TEXT_METADATA_RE.fullmatch(base_line)
        current_match = TEXT_METADATA_RE.fullmatch(current_line)
        if not base_match or not current_match:
            errors.append(
                f"{label} changed outside generated_at/validated_at at line={line_number}"
            )
            continue
        if (
            base_match.group("key") != current_match.group("key")
            or base_match.group("prefix") != current_match.group("prefix")
            or base_match.group("ending") != current_match.group("ending")
        ):
            errors.append(f"{label} metadata field structure drift at line={line_number}")
            continue
        value = current_match.group("value").strip().strip("`").strip()
        if not value:
            errors.append(f"{label} blank metadata timestamp at line={line_number}")
        changed_metadata += 1
    if base_payload != current_payload and changed_metadata == 0:
        errors.append(f"{label} differs without a generated_at/validated_at update")
    return errors


def _metadata_only_errors(base_payload: bytes, current_payload: bytes, label: str) -> list[str]:
    if label.endswith(".json"):
        return _metadata_only_json_errors(base_payload, current_payload, label)
    return _metadata_only_text_errors(base_payload, current_payload, label)


def _normalized_markdown(
    payload: bytes,
    *,
    label: str,
    allowed_keys: frozenset[str],
) -> tuple[list[str], list[str]]:
    try:
        lines = payload.decode("utf-8-sig").splitlines(keepends=True)
    except UnicodeDecodeError as exc:
        return [], [f"{label} is not valid UTF-8: {exc}"]
    normalized: list[str] = []
    found: set[str] = set()
    pattern = re.compile(
        r"^(?P<prefix>\s*[-*]\s*(?P<key>generated_at|source_watch_sha256)\s*:\s*)"
        r"(?P<value>.*?)(?P<ending>\r?\n)?$"
    )
    for line in lines:
        match = pattern.fullmatch(line)
        if match and match.group("key") in allowed_keys:
            key = match.group("key")
            found.add(key)
            normalized.append(
                f"{match.group('prefix')}<allowed-{key}>{match.group('ending') or ''}"
            )
        else:
            normalized.append(line)
    missing = sorted(allowed_keys - found)
    errors = [f"{label} missing required metadata field: {key}" for key in missing]
    return normalized, errors


def _markdown_refresh_errors(
    base_payload: bytes,
    current_payload: bytes,
    *,
    label: str,
    watch_sha256: str,
) -> list[str]:
    allowed = frozenset({"generated_at", "source_watch_sha256"})
    base_normalized, errors = _normalized_markdown(
        base_payload, label=f"base {label}", allowed_keys=allowed
    )
    current_normalized, current_errors = _normalized_markdown(
        current_payload, label=f"current {label}", allowed_keys=allowed
    )
    errors.extend(current_errors)
    if base_normalized != current_normalized:
        errors.append(f"{label} changed outside generated_at/source_watch_sha256")
    try:
        current_text = current_payload.decode("utf-8-sig")
    except UnicodeDecodeError:
        return errors
    matches = re.findall(r"(?m)^\s*[-*]\s*source_watch_sha256\s*:\s*`?([0-9a-fA-F]{64})`?\s*$", current_text)
    if matches != [watch_sha256]:
        errors.append(
            f"{label} source_watch_sha256 mismatch: expected={[watch_sha256]!r} "
            f"actual={[value.lower() for value in matches]!r}"
        )
    return errors


def _format_paths(paths: Iterable[str]) -> str:
    return ";".join(sorted(paths)) or "none"


def _validate_git_state(
    repo_root: Path,
    base_sha: str,
    phase: str,
) -> tuple[list[str], str | None, set[str]]:
    errors: list[str] = []
    if not FULL_COMMIT_RE.fullmatch(base_sha):
        return ["--base-sha must be an exact 40-hex commit SHA"], None, set()
    try:
        resolved_base = (
            _git(repo_root, "rev-parse", "--verify", f"{base_sha}^{{commit}}")
            .stdout.decode("ascii")
            .strip()
            .lower()
        )
        head_sha = _git(repo_root, "rev-parse", "--verify", "HEAD^{commit}").stdout.decode(
            "ascii"
        ).strip().lower()
    except (GitError, UnicodeDecodeError) as exc:
        return [str(exc)], None, set()
    if resolved_base != base_sha.lower():
        errors.append(
            f"base SHA did not resolve exactly: supplied={base_sha.lower()} resolved={resolved_base}"
        )
    ancestry = _git(
        repo_root,
        "merge-base",
        "--is-ancestor",
        resolved_base,
        head_sha,
        check=False,
    )
    if ancestry.returncode != 0:
        errors.append(f"base SHA is not an ancestor of HEAD: base={resolved_base} head={head_sha}")
    if phase != "committed" and head_sha != resolved_base:
        errors.append(
            f"HEAD must remain the exact refresh base during validation: base={resolved_base} head={head_sha}"
        )
    if phase == "committed":
        try:
            parent_tokens = (
                _git(repo_root, "rev-list", "--parents", "-n", "1", head_sha)
                .stdout.decode("ascii")
                .strip()
                .lower()
                .split()
            )
            revision_count_text = (
                _git(repo_root, "rev-list", "--count", f"{resolved_base}..{head_sha}")
                .stdout.decode("ascii")
                .strip()
            )
        except (GitError, UnicodeDecodeError) as exc:
            errors.append(str(exc))
            parent_tokens = []
            revision_count_text = ""
        parents = parent_tokens[1:] if parent_tokens and parent_tokens[0] == head_sha else []
        if parents != [resolved_base]:
            errors.append(
                f"committed phase requires HEAD direct single parent=base: "
                f"base={resolved_base} head={head_sha} parents={parents!r}"
            )
        try:
            revision_count = int(revision_count_text)
        except ValueError:
            revision_count = -1
        if revision_count != 1:
            errors.append(
                f"committed phase requires exactly one revision in base..HEAD: "
                f"count={revision_count_text or 'unavailable'}"
            )

    try:
        changed = _working_changes(repo_root, resolved_base)
        staged = _staged_changes(repo_root, resolved_base)
        unstaged = _unstaged_changes(repo_root)
        index_changes_from_head = _index_changes_from_head(repo_root)
        untracked = _z_paths(
            _git(repo_root, "ls-files", "--others", "--exclude-standard", "-z").stdout
        )
    except GitError as exc:
        return errors + [str(exc)], resolved_base, set()

    extra = changed - TEMPORARY_ALLOWLIST
    if extra:
        errors.append(f"changes outside temporary 13-path allowlist: {_format_paths(extra)}")
    if phase == "post-build":
        if staged:
            errors.append(f"post-build phase forbids staged residue: {_format_paths(staged)}")
        if not FINAL_EXPECTED_DIFF <= changed:
            errors.append(
                "post-build phase is missing required refresh paths: "
                f"{_format_paths(FINAL_EXPECTED_DIFF - changed)}"
            )
        unexpected = changed - FINAL_EXPECTED_DIFF - POST_BUILD_METADATA_ONLY
        if unexpected:
            errors.append(
                f"post-build changed non-final non-metadata paths: {_format_paths(unexpected)}"
            )
    elif phase == "final":
        try:
            statuses = _name_status(repo_root, resolved_base, staged=False)
        except GitError as exc:
            errors.append(str(exc))
            statuses = []
        for status, status_paths in statuses:
            if status != "M":
                errors.append(
                    f"final phase forbids delete/rename/add/type change: status={status} "
                    f"paths={_format_paths(status_paths)}"
                )
        if staged:
            errors.append(f"final phase forbids staged residue: {_format_paths(staged)}")
        if changed != FINAL_EXPECTED_DIFF:
            errors.append(
                f"final phase requires exact 7-path diff: expected={_format_paths(FINAL_EXPECTED_DIFF)} "
                f"actual={_format_paths(changed)}"
            )
    elif phase == "staged":
        try:
            statuses = _name_status(repo_root, resolved_base, staged=True)
        except GitError as exc:
            errors.append(str(exc))
            statuses = []
        for status, status_paths in statuses:
            if status != "M":
                errors.append(
                    f"staged phase forbids delete/rename/add/type change: status={status} "
                    f"paths={_format_paths(status_paths)}"
                )
        if changed != FINAL_EXPECTED_DIFF:
            errors.append(
                f"staged phase requires exact 7-path working diff: "
                f"expected={_format_paths(FINAL_EXPECTED_DIFF)} actual={_format_paths(changed)}"
            )
        if staged != FINAL_EXPECTED_DIFF:
            errors.append(
                f"staged phase requires exact 7 staged paths: "
                f"expected={_format_paths(FINAL_EXPECTED_DIFF)} actual={_format_paths(staged)}"
            )
        if unstaged:
            errors.append(f"staged phase forbids unstaged residue: {_format_paths(unstaged)}")
        if untracked:
            errors.append(f"staged phase forbids untracked residue: {_format_paths(untracked)}")
        if staged == FINAL_EXPECTED_DIFF:
            try:
                errors.extend(_staged_mode_type_errors(repo_root, FINAL_EXPECTED_DIFF))
            except GitError as exc:
                errors.append(str(exc))
    elif phase == "committed":
        try:
            committed_paths = _revision_changes(repo_root, resolved_base, head_sha)
            statuses = _revision_name_status(repo_root, resolved_base, head_sha)
        except GitError as exc:
            errors.append(str(exc))
            committed_paths = set()
            statuses = []
        if committed_paths != FINAL_EXPECTED_DIFF:
            errors.append(
                f"committed phase requires exact 7-path base..HEAD diff: "
                f"expected={_format_paths(FINAL_EXPECTED_DIFF)} "
                f"actual={_format_paths(committed_paths)}"
            )
        for status, status_paths in statuses:
            if status != "M":
                errors.append(
                    f"committed phase permits only modified paths: status={status} "
                    f"paths={_format_paths(status_paths)}"
                )
        if changed != FINAL_EXPECTED_DIFF:
            errors.append(
                f"committed phase working tree must resolve to exact 7-path base diff: "
                f"expected={_format_paths(FINAL_EXPECTED_DIFF)} "
                f"actual={_format_paths(changed)}"
            )
        if index_changes_from_head:
            errors.append(
                f"committed phase forbids index residue against HEAD: "
                f"{_format_paths(index_changes_from_head)}"
            )
        if unstaged:
            errors.append(
                f"committed phase forbids unstaged residue: {_format_paths(unstaged)}"
            )
        if untracked:
            errors.append(
                f"committed phase forbids untracked residue: {_format_paths(untracked)}"
            )
        try:
            errors.extend(
                _committed_mode_type_errors(repo_root, head_sha, FINAL_EXPECTED_DIFF)
            )
        except GitError as exc:
            errors.append(str(exc))
    return errors, resolved_base, changed


def validate_refresh(repo_root: Path, base_sha: str, phase: str) -> list[str]:
    repo_root = repo_root.resolve()
    errors, resolved_base, changed = _validate_git_state(repo_root, base_sha, phase)
    if resolved_base is None:
        return errors

    base_blobs: dict[str, bytes] = {}
    current_blobs: dict[str, bytes] = {}
    for relative_path in sorted(TEMPORARY_ALLOWLIST):
        try:
            base_blobs[relative_path] = _base_blob(repo_root, resolved_base, relative_path)
            current_blobs[relative_path] = _current_blob(repo_root, relative_path)
        except (GitError, OSError) as exc:
            errors.append(str(exc))
    if len(base_blobs) != len(TEMPORARY_ALLOWLIST) or len(current_blobs) != len(
        TEMPORARY_ALLOWLIST
    ):
        return errors

    watch_errors, base_watch_rows, watch_rows = _compare_csv_except(
        base_blobs[WATCH_CSV],
        current_blobs[WATCH_CSV],
        label=WATCH_CSV,
        allowed_columns=frozenset({WATCH_LINEAGE_COLUMN}),
    )
    errors.extend(watch_errors)
    if len(base_watch_rows) != EXPECTED_WATCH_ROWS or len(watch_rows) != EXPECTED_WATCH_ROWS:
        errors.append(
            f"watch refresh requires exact {EXPECTED_WATCH_ROWS} base/current rows: "
            f"base={len(base_watch_rows)} current={len(watch_rows)}"
        )
    changed_lineage_count = 0
    if len(base_watch_rows) == len(watch_rows):
        for row_number, (base_row, current_row) in enumerate(
            zip(base_watch_rows, watch_rows, strict=True), start=2
        ):
            old_sha = str(base_row.get(WATCH_LINEAGE_COLUMN, "")).strip().lower()
            new_sha = str(current_row.get(WATCH_LINEAGE_COLUMN, "")).strip().lower()
            if old_sha == new_sha:
                errors.append(
                    f"watch stale lineage was not refreshed: row={row_number} "
                    f"stock_id={current_row.get('stock_id', '')} sha={new_sha!r}"
                )
            else:
                changed_lineage_count += 1
    if changed_lineage_count != EXPECTED_WATCH_ROWS:
        errors.append(
            f"watch refresh requires stale-to-new lineage on 13/13 rows: "
            f"changed={changed_lineage_count} expected={EXPECTED_WATCH_ROWS}"
        )
    lineage_errors, watch_by_stock = _validate_watch_lineage(repo_root, watch_rows)
    errors.extend(lineage_errors)
    watch_sha256 = _sha256(current_blobs[WATCH_CSV])

    theme_errors, _base_theme_rows, theme_rows = _compare_csv_except(
        base_blobs[THEME_STOCKS_CSV],
        current_blobs[THEME_STOCKS_CSV],
        label=THEME_STOCKS_CSV,
        allowed_columns=THEME_STOCK_LINEAGE_COLUMNS,
    )
    errors.extend(theme_errors)
    errors.extend(
        _validate_theme_stock_lineage(
            theme_rows,
            watch_by_stock=watch_by_stock,
            watch_sha256=watch_sha256,
        )
    )

    for relative_path in THEME_LAYER_CSV_PATHS:
        if current_blobs[relative_path] != base_blobs[relative_path]:
            errors.append(f"theme layer CSV must remain byte-identical to base: {relative_path}")

    mirror_pairs = (
        (THEME_LAYER_CSV, DOCS_THEME_LAYER_CSV),
        (THEME_LAYER_MD, DOCS_THEME_LAYER_MD),
        (THEME_STOCKS_CSV, DOCS_THEME_STOCKS_CSV),
        (THEME_STOCKS_MD, DOCS_THEME_STOCKS_MD),
    )
    for output_path, docs_path in mirror_pairs:
        if current_blobs[output_path] != current_blobs[docs_path]:
            errors.append(
                f"output/docs mirror byte mismatch: output={output_path} docs={docs_path}"
            )

    if current_blobs[DOCS_THEME_STOCKS_CSV] != current_blobs[THEME_STOCKS_CSV]:
        errors.append("docs theme stocks CSV does not mirror the validated output CSV")

    for relative_path in THEME_MARKDOWN_PATHS + THEME_STOCK_MARKDOWN_PATHS:
        errors.extend(
            _markdown_refresh_errors(
                base_blobs[relative_path],
                current_blobs[relative_path],
                label=relative_path,
                watch_sha256=watch_sha256,
            )
        )

    for relative_path in POST_BUILD_METADATA_ONLY:
        if phase == "post-build":
            errors.extend(
                _metadata_only_errors(
                    base_blobs[relative_path], current_blobs[relative_path], relative_path
                )
            )
        elif current_blobs[relative_path] != base_blobs[relative_path]:
            errors.append(
                f"{phase} phase requires metadata-only artifact restored to base: {relative_path}"
            )

    if phase != "post-build":
        unexpected_metadata_diff = changed & POST_BUILD_METADATA_ONLY
        if unexpected_metadata_diff:
            errors.append(
                f"{phase} phase retains metadata-only changes: "
                f"{_format_paths(unexpected_metadata_diff)}"
            )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the bounded Volume V2 advisory lineage-only refresh."
    )
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--base-sha", required=True)
    parser.add_argument(
        "--phase",
        choices=("post-build", "final", "staged", "committed"),
        required=True,
    )
    args = parser.parse_args(argv)

    try:
        errors = validate_refresh(args.repo_root, args.base_sha, args.phase)
    except (GitError, OSError, ValueError) as exc:
        errors = [f"validator failed closed: {exc}"]
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "volume-v2 advisory lineage refresh validation pass: "
        f"phase={args.phase} final_paths={len(FINAL_EXPECTED_DIFF)} "
        f"temporary_allowlist={len(TEMPORARY_ALLOWLIST)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
