from __future__ import annotations

import argparse
import re
import subprocess
import sys
from io import BytesIO
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import normalize_date, now_text, read_csv, safe_str, write_csv  # noqa: E402
from update_daily_published_model_snapshots import (  # noqa: E402
    ARTIFACTS,
    MANIFEST_COLUMNS,
    MANIFEST_PATH,
    SNAPSHOT_DIR,
    SnapshotArtifact,
    csv_shape,
    sha256_file,
    validate_artifact_frame,
)


ROOT = Path(__file__).resolve().parents[1]
ALL_CANDIDATES_SOURCE = "output/latest/all_candidates_latest.csv"
PUBLISHED_MODEL_SIGNALS_RE = re.compile(r"daily_candidate_model_signals_for_report_(\d{8})\.csv$")


def all_candidates_artifact() -> SnapshotArtifact:
    for artifact in ARTIFACTS:
        if artifact.artifact_id == "all_candidates_source_rows":
            return artifact
    raise RuntimeError("all_candidates_source_rows artifact is not registered")


def git_output(repo_root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=repo_root, stderr=subprocess.DEVNULL)


def git_all_candidates_commits(repo_root: Path = ROOT) -> list[str]:
    output = git_output(repo_root, "log", "--format=%H", "--", ALL_CANDIDATES_SOURCE)
    return output.decode("ascii").splitlines()


def git_show_all_candidates(repo_root: Path, commit_sha: str) -> bytes:
    return git_output(repo_root, "show", f"{commit_sha}:{ALL_CANDIDATES_SOURCE}")


def published_model_signal_dates(snapshot_dir: Path = SNAPSHOT_DIR) -> list[str]:
    dates: set[str] = set()
    for path in snapshot_dir.glob("daily_candidate_model_signals_for_report_*.csv"):
        match = PUBLISHED_MODEL_SIGNALS_RE.match(path.name)
        if match:
            dates.add(match.group(1))
    return sorted(dates)


def candidate_blob_report_dates(blob: bytes, artifact: SnapshotArtifact) -> set[str]:
    df = pd.read_csv(BytesIO(blob), dtype=str, keep_default_na=False).fillna("")
    missing = [col for col in artifact.required_columns if col not in df.columns]
    if missing:
        raise RuntimeError(f"{ALL_CANDIDATES_SOURCE} missing required columns: {missing}")

    values: set[str] = set()
    for col in artifact.date_columns:
        if col not in df.columns:
            raise RuntimeError(f"{ALL_CANDIDATES_SOURCE} missing required date column: {col}")
        col_values = {normalize_date(value) for value in df[col].tolist()}
        col_values.discard("")
        if col_values:
            values.update(col_values)
    return values


def find_all_candidates_blob_for_date(
    report_date: str,
    *,
    repo_root: Path = ROOT,
    commits: list[str] | None = None,
    artifact: SnapshotArtifact | None = None,
) -> tuple[str, bytes]:
    report_date = normalize_date(report_date)
    if not report_date:
        raise RuntimeError("report_date is required")

    artifact = artifact or all_candidates_artifact()
    commits = commits if commits is not None else git_all_candidates_commits(repo_root)
    for commit_sha in commits:
        try:
            blob = git_show_all_candidates(repo_root, commit_sha)
        except subprocess.CalledProcessError:
            continue
        if candidate_blob_report_dates(blob, artifact) == {report_date}:
            return commit_sha, blob
    raise RuntimeError(f"no git-history {ALL_CANDIDATES_SOURCE} blob found for report_date={report_date}")


def manifest_template_for_date(manifest: pd.DataFrame, report_date: str) -> dict[str, str]:
    same_date = manifest[manifest["snapshot_report_date"].map(normalize_date).eq(report_date)]
    if same_date.empty:
        raise RuntimeError(f"manifest has no existing published snapshot rows for report_date={report_date}")
    row = same_date.iloc[0].to_dict()
    return {col: safe_str(row.get(col, "")) for col in MANIFEST_COLUMNS}


def backfill_historical_all_candidates_snapshots(
    *,
    repo_root: Path = ROOT,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
    dates: list[str] | None = None,
    overwrite: bool = False,
    dry_run: bool = False,
    generated_at: str | None = None,
) -> pd.DataFrame:
    artifact = all_candidates_artifact()
    dates = dates if dates is not None else published_model_signal_dates(snapshot_dir)
    dates = sorted({normalize_date(date) for date in dates if normalize_date(date)})
    if not dates:
        raise RuntimeError("no report dates were selected for all_candidates backfill")

    manifest = read_csv(manifest_path, dtype=str)
    if manifest.empty:
        raise RuntimeError(f"{manifest_path.as_posix()} is missing or empty")
    for col in MANIFEST_COLUMNS:
        if col not in manifest.columns:
            manifest[col] = ""
    manifest = manifest[MANIFEST_COLUMNS].fillna("")

    generated_at = generated_at or now_text()
    commits = git_all_candidates_commits(repo_root)
    rows: list[dict[str, str]] = []
    for report_date in dates:
        target = snapshot_dir / f"all_candidates_{report_date}.csv"
        existing = target.exists()
        if existing and not overwrite:
            continue

        commit_sha, blob = find_all_candidates_blob_for_date(
            report_date,
            repo_root=repo_root,
            commits=commits,
            artifact=artifact,
        )
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(blob)
            validate_artifact_frame(target, artifact, report_date)
            row_count, column_count = csv_shape(target)
            digest = sha256_file(target)
        else:
            df = pd.read_csv(BytesIO(blob), dtype=str, keep_default_na=False)
            row_count, column_count = len(df), len(df.columns)
            digest = ""

        template = manifest_template_for_date(manifest, report_date)
        rows.append(
            {
                **template,
                "snapshot_report_date": report_date,
                "generated_at": generated_at,
                "pipeline_commit_sha": commit_sha,
                "main_price_date": report_date,
                "artifact_id": artifact.artifact_id,
                "source_path": ALL_CANDIDATES_SOURCE,
                "snapshot_path": target.as_posix(),
                "source_sha256": digest,
                "snapshot_sha256": digest,
                "row_count": str(row_count),
                "column_count": str(column_count),
                "purpose": "as_published_daily_model_snapshot",
            }
        )

    new_rows = pd.DataFrame(rows, columns=MANIFEST_COLUMNS)
    if not dry_run and not new_rows.empty:
        keys = set(zip(new_rows["snapshot_report_date"], new_rows["artifact_id"]))
        keep_mask = [
            (safe_str(row.get("snapshot_report_date", "")), safe_str(row.get("artifact_id", ""))) not in keys
            for _, row in manifest.iterrows()
        ]
        combined = pd.concat([manifest.loc[keep_mask], new_rows], ignore_index=True)
        combined = combined[MANIFEST_COLUMNS]
        combined = combined.sort_values(["snapshot_report_date", "artifact_id"]).reset_index(drop=True)
        write_csv(combined, manifest_path)

    return new_rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Backfill historical all_candidates source-row snapshots from git history."
    )
    parser.add_argument(
        "--dates",
        help="Comma-separated YYYYMMDD report dates. Defaults to all published model signal snapshot dates.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing all_candidates_YYYYMMDD.csv files.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned rows without writing files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected_dates = None
    if args.dates:
        selected_dates = [part.strip() for part in args.dates.split(",") if part.strip()]

    try:
        rows = backfill_historical_all_candidates_snapshots(
            dates=selected_dates,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    action = "planned" if args.dry_run else "backfilled"
    print(f"{action} historical all_candidates snapshots: {len(rows)}")
    for _, row in rows.iterrows():
        print(
            f"{row['snapshot_report_date']} {row['snapshot_path']} "
            f"rows={row['row_count']} commit={str(row['pipeline_commit_sha'])[:10]}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
