from __future__ import annotations

import csv
import hashlib
import io
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
MANIFEST_PATH = ROOT / "config/revenue_unreacted_range_legacy_runtime_evidence_manifest.csv"
REQUIRED_COLUMNS = (
    "archive_id",
    "model_id",
    "legacy_runtime_semantics",
    "source_artifact",
    "source_git_commit",
    "source_artifact_sha256",
    "source_total_rows",
    "archived_row_count",
    "first_signal_date",
    "last_signal_date",
    "archive_artifact",
    "archive_artifact_sha256",
    "row_encoding",
    "owner_lane",
    "allowed_use",
    "forbidden_use",
    "retirement_reason",
    "authorization_ref",
)


def _canonical_csv_bytes(csv_bytes: bytes) -> bytes:
    try:
        text = csv_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"CSV is not UTF-8: {exc}") from exc
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if not reader.fieldnames or any(field is None or not field for field in reader.fieldnames):
        raise RuntimeError("CSV header is missing or malformed")
    rows: list[dict[str, str]] = []
    for row in reader:
        if None in row or any(value is None for value in row.values()):
            raise RuntimeError("CSV row width does not match the canonical header")
        rows.append(dict(row))
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=reader.fieldnames,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(rows)
    return b"\xef\xbb\xbf" + output.getvalue().encode("utf-8")


def _git(repo: Path, *args: str) -> bytes:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.decode("utf-8", errors="replace").strip())
    return completed.stdout


def _canonical_filtered_source(source_bytes: bytes) -> tuple[bytes, int, int, str, str]:
    reader = csv.DictReader(io.StringIO(source_bytes.decode("utf-8-sig"), newline=""))
    if not reader.fieldnames or "model_id" not in reader.fieldnames:
        raise RuntimeError("source schema is missing model_id")
    source_rows = list(reader)
    rows = [row for row in source_rows if row.get("model_id", "") == MODEL_ID]
    if not rows:
        raise RuntimeError("source commit has no legacy revenue rows")
    dates = [row.get("signal_date", "").strip() for row in rows]
    if any(not date for date in dates):
        raise RuntimeError("legacy revenue evidence contains blank signal_date")
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=reader.fieldnames,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(rows)
    return (
        b"\xef\xbb\xbf" + output.getvalue().encode("utf-8"),
        len(source_rows),
        len(rows),
        min(dates),
        max(dates),
    )


def validate(repo: Path = ROOT, manifest_path: Path | None = None) -> list[str]:
    manifest = manifest_path or (repo / MANIFEST_PATH.relative_to(ROOT))
    errors: list[str] = []
    if not manifest.exists():
        return [f"missing legacy evidence manifest: {manifest}"]
    with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != REQUIRED_COLUMNS:
            return ["legacy evidence manifest schema drift"]
        rows = list(reader)
    if not rows:
        return ["legacy evidence manifest is empty"]
    archive_ids = [row.get("archive_id", "") for row in rows]
    if len(archive_ids) != len(set(archive_ids)):
        errors.append("legacy evidence manifest archive_id must be unique")

    for row in rows:
        archive_id = row.get("archive_id", "")
        if row.get("model_id") != MODEL_ID:
            errors.append(f"{archive_id}: model_id mismatch")
            continue
        if row.get("owner_lane") != "daily_model_maintenance":
            errors.append(f"{archive_id}: owner lane mismatch")
        if row.get("authorization_ref") != "user_authorized_4A_4C_20260830":
            errors.append(f"{archive_id}: authorization mismatch")
        forbidden_tokens = set((row.get("forbidden_use") or "").split(";"))
        if not {"daily_selection", "pdf", "promotion_evidence"} <= forbidden_tokens:
            errors.append(f"{archive_id}: forbidden-use retirement boundary incomplete")
        archive_rel = row.get("archive_artifact", "")
        if not archive_rel.startswith(
            "output/history/daily_candidate_models/legacy_revenue_v1_signals_"
        ):
            errors.append(f"{archive_id}: archive path is not model-owned")
            continue
        archive_path = repo / Path(archive_rel)
        if not archive_path.exists():
            errors.append(f"{archive_id}: archive artifact is missing")
            continue
        archive_bytes = archive_path.read_bytes()
        try:
            canonical_archive_bytes = _canonical_csv_bytes(archive_bytes)
        except RuntimeError as exc:
            errors.append(f"{archive_id}: archive artifact is invalid: {exc}")
            continue
        archive_sha = hashlib.sha256(canonical_archive_bytes).hexdigest()
        if archive_sha != row.get("archive_artifact_sha256"):
            errors.append(f"{archive_id}: archive canonical semantic SHA-256 mismatch")
        if not archive_path.name.endswith(f"_{archive_sha[:16]}.csv"):
            errors.append(f"{archive_id}: archive filename is not content-addressed")
        if row.get("row_encoding") != (
            "utf-8-sig_rfc4180_canonical_lf_source_column_order_"
            "raw_newline_diagnostic_only"
        ):
            errors.append(f"{archive_id}: row encoding/canonicalization contract mismatch")

        source_commit = row.get("source_git_commit", "")
        source_artifact = row.get("source_artifact", "")
        try:
            resolved = _git(repo, "rev-parse", f"{source_commit}^{{commit}}").decode(
                "ascii"
            ).strip()
            source_bytes = _git(repo, "show", f"{resolved}:{source_artifact}")
        except RuntimeError as exc:
            errors.append(f"{archive_id}: committed source unavailable: {exc}")
            continue
        if resolved != source_commit:
            errors.append(f"{archive_id}: source_git_commit is not canonical")
        if hashlib.sha256(source_bytes).hexdigest() != row.get(
            "source_artifact_sha256"
        ):
            errors.append(f"{archive_id}: committed source SHA-256 mismatch")
        try:
            expected_bytes, source_count, row_count, first_date, last_date = (
                _canonical_filtered_source(source_bytes)
            )
        except RuntimeError as exc:
            errors.append(f"{archive_id}: committed source invalid: {exc}")
            continue
        exact_values = {
            "source_total_rows": str(source_count),
            "archived_row_count": str(row_count),
            "first_signal_date": first_date,
            "last_signal_date": last_date,
        }
        for field_name, expected in exact_values.items():
            if row.get(field_name) != expected:
                errors.append(f"{archive_id}: {field_name} mismatch")
        if canonical_archive_bytes != expected_bytes:
            errors.append(f"{archive_id}: archive is not the exact canonical source slice")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: legacy revenue runtime evidence archive is immutable and reproducible")
    return 0


if __name__ == "__main__":
    sys.exit(main())
