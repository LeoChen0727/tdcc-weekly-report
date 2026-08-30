from __future__ import annotations

import argparse
import csv
import hashlib
import io
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
SOURCE_ARTIFACT = (
    "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv"
)
ARCHIVE_DIR = Path("output/history/daily_candidate_models")
MANIFEST_PATH = Path(
    "config/revenue_unreacted_range_legacy_runtime_evidence_manifest.csv"
)
ARCHIVE_ID = "legacy_revenue_unreacted_range_v1_signal_evidence_retirement_20260831"
AUTHORIZATION_REF = "user_authorized_4A_4C_20260830"

MANIFEST_COLUMNS = (
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


def canonical_csv_bytes(csv_bytes: bytes) -> bytes:
    """Return semantic CSV bytes independent of BOM and CRLF/LF checkout form."""

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
        raise RuntimeError(
            f"git {' '.join(args)} failed: "
            f"{completed.stderr.decode('utf-8', errors='replace').strip()}"
        )
    return completed.stdout


def canonical_legacy_rows(source_bytes: bytes) -> tuple[bytes, int, int, str, str]:
    text = source_bytes.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if not reader.fieldnames or "model_id" not in reader.fieldnames:
        raise RuntimeError("legacy signal source is missing model_id")
    rows = list(reader)
    legacy_rows = [row for row in rows if row.get("model_id", "") == MODEL_ID]
    if not legacy_rows:
        raise RuntimeError("legacy signal source has no revenue_unreacted_range rows")
    signal_dates = [row.get("signal_date", "").strip() for row in legacy_rows]
    if any(not value for value in signal_dates):
        raise RuntimeError("legacy revenue signal evidence has blank signal_date")

    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=reader.fieldnames,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(legacy_rows)
    archive_bytes = b"\xef\xbb\xbf" + output.getvalue().encode("utf-8")
    return (
        archive_bytes,
        len(rows),
        len(legacy_rows),
        min(signal_dates),
        max(signal_dates),
    )


def _read_manifest(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != MANIFEST_COLUMNS:
            raise RuntimeError("legacy evidence manifest schema drift")
        return list(reader)


def _manifest_bytes(rows: list[dict[str, str]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=MANIFEST_COLUMNS,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(rows)
    return b"\xef\xbb\xbf" + output.getvalue().encode("utf-8")


def archive(repo: Path, source_rev: str) -> tuple[Path, dict[str, str]]:
    source_commit = _git(repo, "rev-parse", f"{source_rev}^{{commit}}").decode(
        "ascii"
    ).strip()
    source_bytes = _git(repo, "show", f"{source_commit}:{SOURCE_ARTIFACT}")
    (
        archive_bytes,
        source_total_rows,
        archived_row_count,
        first_signal_date,
        last_signal_date,
    ) = canonical_legacy_rows(source_bytes)
    archive_sha256 = hashlib.sha256(canonical_csv_bytes(archive_bytes)).hexdigest()
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    archive_rel = ARCHIVE_DIR / (
        "legacy_revenue_v1_signals_"
        f"through_{last_signal_date}_{archive_sha256[:16]}.csv"
    )
    archive_path = repo / archive_rel
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    if archive_path.exists():
        try:
            existing_canonical = canonical_csv_bytes(archive_path.read_bytes())
        except RuntimeError as exc:
            raise RuntimeError(
                f"content-addressed archive is invalid: {archive_rel.as_posix()}: {exc}"
            ) from exc
        if existing_canonical != archive_bytes:
            raise RuntimeError(
                f"content-addressed archive collision: {archive_rel.as_posix()}"
            )
    else:
        archive_path.write_bytes(archive_bytes)

    manifest_row = {
        "archive_id": ARCHIVE_ID,
        "model_id": MODEL_ID,
        "legacy_runtime_semantics": "production_current_proxy_without_exact_production_backtest",
        "source_artifact": SOURCE_ARTIFACT,
        "source_git_commit": source_commit,
        "source_artifact_sha256": source_sha256,
        "source_total_rows": str(source_total_rows),
        "archived_row_count": str(archived_row_count),
        "first_signal_date": first_signal_date,
        "last_signal_date": last_signal_date,
        "archive_artifact": archive_rel.as_posix(),
        "archive_artifact_sha256": archive_sha256,
        "row_encoding": (
            "utf-8-sig_rfc4180_canonical_lf_source_column_order_"
            "raw_newline_diagnostic_only"
        ),
        "owner_lane": "daily_model_maintenance",
        "allowed_use": "immutable_audit_only;dependency_audit;historical_replay_reference",
        "forbidden_use": "daily_selection;pdf;ranking;promotion_evidence;formal_adapter;production_reactivation",
        "retirement_reason": "legacy_runtime_lacked_exact_production_backtest_and_was_replaced_by_source_mid_falling_v2",
        "authorization_ref": AUTHORIZATION_REF,
    }
    manifest_path = repo / MANIFEST_PATH
    rows = _read_manifest(manifest_path)
    matches = [row for row in rows if row.get("archive_id") == ARCHIVE_ID]
    if matches and matches != [manifest_row]:
        raise RuntimeError("append-only legacy evidence manifest row would change")
    if not matches:
        rows.append(manifest_row)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_bytes(_manifest_bytes(rows))
    return archive_path, manifest_row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--source-rev", default="HEAD")
    args = parser.parse_args()
    archive_path, row = archive(args.repo_root.resolve(), args.source_rev)
    print(
        "Archived legacy revenue runtime evidence: "
        f"path={archive_path}; rows={row['archived_row_count']}; "
        f"sha256={row['archive_artifact_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
