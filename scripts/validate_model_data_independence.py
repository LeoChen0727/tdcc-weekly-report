from __future__ import annotations

import argparse
import csv
import io
import subprocess
from pathlib import Path

try:
    from build_model_data_independence_audit import (
        DOCS_CSV,
        DOCS_MD,
        OUTPUT_COLUMNS,
        OUTPUT_CSV,
        OUTPUT_MD,
        build_rows,
    )
    from model_data_independence import (
        DATA_SHARING_MIGRATIONS,
        DATA_SHARING_MIGRATION_COLUMNS,
        ROOT,
        comprehensive_validation,
    )
except ModuleNotFoundError:  # Loaded as scripts.validate_model_data_independence.
    from scripts.build_model_data_independence_audit import (
        DOCS_CSV,
        DOCS_MD,
        OUTPUT_COLUMNS,
        OUTPUT_CSV,
        OUTPUT_MD,
        build_rows,
    )
    from scripts.model_data_independence import (
        DATA_SHARING_MIGRATIONS,
        DATA_SHARING_MIGRATION_COLUMNS,
        ROOT,
        comprehensive_validation,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default=None)
    return parser.parse_args()


def validate(*, base_ref: str | None = None) -> list[str]:
    errors, _ = comprehensive_validation(base_ref=base_ref)
    if base_ref:
        errors.extend(validate_data_sharing_migration_append_only(base_ref))
    if errors:
        return errors
    errors.extend(validate_audit_artifact())
    return errors


def _migration_records(raw: bytes, *, source: str) -> tuple[list[tuple[bytes, ...]], list[str]]:
    errors: list[str] = []
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        return [], [f"{source}: daily data-sharing migration CSV is not valid UTF-8: {exc}"]
    try:
        parsed = list(csv.reader(io.StringIO(text, newline="")))
    except csv.Error as exc:
        return [], [f"{source}: daily data-sharing migration CSV cannot be parsed: {exc}"]
    if not parsed:
        return [], [f"{source}: daily data-sharing migration CSV is empty"]
    header = tuple(parsed[0])
    if header != DATA_SHARING_MIGRATION_COLUMNS:
        errors.append(
            f"{source}: daily data-sharing migration CSV schema drift: "
            f"expected={DATA_SHARING_MIGRATION_COLUMNS!r} actual={header!r}"
        )
        return [], errors
    records: list[tuple[bytes, ...]] = []
    for line_number, values in enumerate(parsed[1:], start=2):
        if len(values) != len(header):
            errors.append(
                f"{source}: daily data-sharing migration row {line_number} field count "
                f"{len(values)} does not match header count {len(header)}"
            )
            continue
        records.append(tuple(value.encode("utf-8") for value in values))
    return records, errors


def validate_data_sharing_migration_append_only(
    base_ref: str,
    *,
    migration_path: Path | None = None,
    repository_root: Path | None = None,
) -> list[str]:
    """Require every base migration row to remain an exact current prefix."""

    errors: list[str] = []
    path = migration_path or DATA_SHARING_MIGRATIONS
    root = repository_root or ROOT
    try:
        relative_path = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return [f"daily data-sharing migration registry is outside repository root: {path}"]
    if not path.is_file():
        return [f"missing daily data-sharing migration registry: {relative_path}"]
    try:
        result = subprocess.run(
            ["git", "show", f"{base_ref}:{relative_path}"],
            cwd=root,
            capture_output=True,
            check=False,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [
            f"cannot read base daily data-sharing migrations from "
            f"{base_ref}:{relative_path}: {exc}"
        ]
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        return [
            f"cannot read base daily data-sharing migrations from {base_ref}:{relative_path}"
            + (f": {detail}" if detail else "")
        ]

    base_bytes = result.stdout
    current_bytes = path.read_bytes()
    base_records, base_errors = _migration_records(
        base_bytes,
        source=f"base_ref {base_ref}",
    )
    current_records, current_errors = _migration_records(
        current_bytes,
        source="current worktree",
    )
    errors.extend(base_errors)
    errors.extend(current_errors)
    if errors:
        return errors
    normalized_base = base_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    normalized_current = current_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if not normalized_current.startswith(normalized_base):
        errors.append(
            "daily_model_data_sharing_migrations.csv is append-only: "
            "base CSV bytes are not an exact current prefix after line-ending normalization"
        )
    if len(current_records) < len(base_records):
        errors.append(
            "daily_model_data_sharing_migrations.csv is append-only: "
            f"current row count {len(current_records)} deleted base rows from {len(base_records)}"
        )
        return errors
    for offset, base_record in enumerate(base_records):
        current_record = current_records[offset]
        if current_record == base_record:
            continue
        base_id = base_record[0].decode("utf-8", errors="replace") if base_record else ""
        current_id = (
            current_record[0].decode("utf-8", errors="replace")
            if current_record
            else ""
        )
        errors.append(
            "daily_model_data_sharing_migrations.csv is append-only: "
            f"base row {offset + 2} is not a byte/field-identical current prefix "
            f"(base migration_id={base_id!r}, current migration_id={current_id!r})"
        )
    return errors


def validate_audit_artifact() -> list[str]:
    errors: list[str] = []
    for path in (OUTPUT_CSV, OUTPUT_MD, DOCS_CSV, DOCS_MD):
        if not path.is_file():
            errors.append(f"missing model/data independence audit artifact: {path.as_posix()}")
    if errors:
        return errors
    if OUTPUT_CSV.read_bytes() != DOCS_CSV.read_bytes():
        errors.append("docs/latest model/data independence CSV must exactly mirror output/latest")
    if OUTPUT_MD.read_bytes() != DOCS_MD.read_bytes():
        errors.append("docs/latest model/data independence Markdown must exactly mirror output/latest")

    with OUTPUT_CSV.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if tuple(reader.fieldnames or ()) != OUTPUT_COLUMNS:
            errors.append("model/data independence audit CSV schema drift")
            return errors
        actual = [{key: str(value or "") for key, value in row.items()} for row in reader]
    if not actual:
        errors.append("model/data independence audit CSV is empty")
        return errors
    generated_values = {row["generated_at"] for row in actual}
    if len(generated_values) != 1 or not next(iter(generated_values)):
        errors.append("model/data independence audit must use one non-empty generated_at value")
    generated_at = next(iter(generated_values)) if generated_values else ""
    expected = build_rows(generated_at)
    if actual != expected:
        errors.append("model/data independence audit is stale relative to current contracts and AST ownership")
    if any(row["status"] == "FAIL" for row in actual):
        errors.append("model/data independence audit contains FAIL rows")
    return errors


def main() -> int:
    args = parse_args()
    errors = validate(base_ref=args.base_ref)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("model and data independence validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
