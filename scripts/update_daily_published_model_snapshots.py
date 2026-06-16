from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    HISTORY_DIR,
    LATEST_DIR,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    write_csv,
)


SNAPSHOT_DIR = HISTORY_DIR / "daily_model_snapshots"
MANIFEST_PATH = SNAPSHOT_DIR / "daily_published_model_snapshot_manifest.csv"
REQUIRED_READY_COLUMNS = ["report_ready", "warrant_ready", "daily_pdf_ready"]


@dataclass(frozen=True)
class SnapshotArtifact:
    artifact_id: str
    source_name: str
    snapshot_stem: str
    required_columns: tuple[str, ...] = ()
    date_columns: tuple[str, ...] = ()


ARTIFACTS: tuple[SnapshotArtifact, ...] = (
    SnapshotArtifact(
        artifact_id="data_freshness",
        source_name="data_freshness_latest.csv",
        snapshot_stem="data_freshness",
        required_columns=("main_price_date", "report_ready", "warrant_ready", "daily_pdf_ready"),
        date_columns=("main_price_date",),
    ),
    SnapshotArtifact(
        artifact_id="model_signals_for_report",
        source_name="daily_candidate_model_signals_for_report_latest.csv",
        snapshot_stem="daily_candidate_model_signals_for_report",
        required_columns=("signal_date", "stock_id", "model_id", "model_name_zh", "model_score"),
        date_columns=("signal_date",),
    ),
    SnapshotArtifact(
        artifact_id="model_summary_for_report",
        source_name="daily_candidate_model_summary_for_report_latest.csv",
        snapshot_stem="daily_candidate_model_summary_for_report",
        required_columns=("signal_date", "report_line", "model_id", "model_name_zh"),
        date_columns=("signal_date",),
    ),
    SnapshotArtifact(
        artifact_id="model_registry",
        source_name="daily_report_model_registry_latest.csv",
        snapshot_stem="daily_report_model_registry",
        required_columns=("model_id", "model_name_zh", "model_registry_order"),
    ),
    SnapshotArtifact(
        artifact_id="model_parameters",
        source_name="daily_candidate_model_parameters_latest.csv",
        snapshot_stem="daily_candidate_model_parameters",
        required_columns=("model_id", "model_name_zh"),
    ),
    SnapshotArtifact(
        artifact_id="volume_breakout_operation_section",
        source_name="daily_volume_breakout_operation_section_latest.csv",
        snapshot_stem="daily_volume_breakout_operation_section",
        required_columns=("model_id", "pdf_view", "pdf_section", "row_type", "buy_rank_eligible"),
    ),
)

MANIFEST_COLUMNS = [
    "snapshot_report_date",
    "generated_at",
    "pipeline_commit_sha",
    "main_price_date",
    "report_ready",
    "warrant_ready",
    "daily_pdf_ready",
    "artifact_id",
    "source_path",
    "snapshot_path",
    "source_sha256",
    "snapshot_sha256",
    "row_count",
    "column_count",
    "purpose",
]


def git_sha() -> str:
    env = os.environ.get("GITHUB_SHA", "").strip()
    if env:
        return env
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return ""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def csv_shape(path: Path) -> tuple[int, int]:
    df = pd.read_csv(path, dtype=str)
    return len(df), len(df.columns)


def freshness_state(latest_dir: Path = LATEST_DIR) -> dict[str, str]:
    path = latest_dir / "data_freshness_latest.csv"
    freshness = read_csv(path, dtype=str)
    if freshness.empty:
        raise RuntimeError(f"{path.as_posix()} is missing or empty")

    row = freshness.iloc[0]
    main_price_date = normalize_date(row.get("main_price_date", ""))
    if not main_price_date:
        raise RuntimeError("data_freshness_latest.csv does not contain main_price_date")

    state = {"main_price_date": main_price_date}
    for col in REQUIRED_READY_COLUMNS:
        value = safe_str(row.get(col, ""))
        if value != "True":
            raise RuntimeError(f"{col} must be True before publishing model snapshots; observed={value}")
        state[col] = value
    return state


def validate_artifact_frame(path: Path, artifact: SnapshotArtifact, report_date: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str)
    missing = [col for col in artifact.required_columns if col not in df.columns]
    if missing:
        raise RuntimeError(f"{path.as_posix()} missing required columns: {missing}")

    for col in artifact.date_columns:
        if col not in df.columns:
            raise RuntimeError(f"{path.as_posix()} missing required date column: {col}")
        values = {normalize_date(value) for value in df[col].tolist()}
        values.discard("")
        if values and values != {report_date}:
            raise RuntimeError(
                f"{path.as_posix()} column {col} must match report date {report_date}; observed={sorted(values)}"
            )
    return df


def snapshot_name(artifact: SnapshotArtifact, report_date: str) -> str:
    return f"{artifact.snapshot_stem}_{report_date}.csv"


def build_daily_published_model_snapshots(
    latest_dir: Path = LATEST_DIR,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
    generated_at: str | None = None,
    commit_sha: str | None = None,
) -> pd.DataFrame:
    state = freshness_state(latest_dir)
    report_date = state["main_price_date"]
    generated_at = generated_at or now_text()
    commit_sha = commit_sha if commit_sha is not None else git_sha()
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    for artifact in ARTIFACTS:
        source = latest_dir / artifact.source_name
        if not source.exists():
            raise RuntimeError(f"required daily published artifact is missing: {source.as_posix()}")

        validate_artifact_frame(source, artifact, report_date)
        target = snapshot_dir / snapshot_name(artifact, report_date)
        shutil.copyfile(source, target)
        row_count, column_count = csv_shape(target)
        rows.append(
            {
                "snapshot_report_date": report_date,
                "generated_at": generated_at,
                "pipeline_commit_sha": commit_sha,
                "main_price_date": state["main_price_date"],
                "report_ready": state["report_ready"],
                "warrant_ready": state["warrant_ready"],
                "daily_pdf_ready": state["daily_pdf_ready"],
                "artifact_id": artifact.artifact_id,
                "source_path": source.as_posix(),
                "snapshot_path": target.as_posix(),
                "source_sha256": sha256_file(source),
                "snapshot_sha256": sha256_file(target),
                "row_count": str(row_count),
                "column_count": str(column_count),
                "purpose": "as_published_daily_model_snapshot",
            }
        )

    new_manifest = pd.DataFrame(rows, columns=MANIFEST_COLUMNS)
    old_manifest = read_csv(manifest_path, dtype=str)
    if old_manifest.empty:
        combined = new_manifest
    else:
        for col in MANIFEST_COLUMNS:
            if col not in old_manifest.columns:
                old_manifest[col] = ""
        old_manifest = old_manifest[MANIFEST_COLUMNS]
        keys = set(zip(new_manifest["snapshot_report_date"], new_manifest["artifact_id"]))
        keep_mask = [
            (safe_str(row.get("snapshot_report_date", "")), safe_str(row.get("artifact_id", ""))) not in keys
            for _, row in old_manifest.iterrows()
        ]
        combined = pd.concat([old_manifest.loc[keep_mask], new_manifest], ignore_index=True)

    combined = combined[MANIFEST_COLUMNS]
    combined = combined.sort_values(["snapshot_report_date", "artifact_id"]).reset_index(drop=True)
    write_csv(combined, manifest_path)
    return new_manifest


def main() -> int:
    try:
        manifest_rows = build_daily_published_model_snapshots()
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    report_date = safe_str(manifest_rows["snapshot_report_date"].iloc[0]) if not manifest_rows.empty else ""
    print(f"saved daily published model snapshots for report_date={report_date}")
    for _, row in manifest_rows.iterrows():
        print(
            "saved "
            f"{row['artifact_id']}: {row['snapshot_path']} "
            f"rows={row['row_count']} sha256={str(row['snapshot_sha256'])[:12]}"
        )
    print(f"saved manifest: {MANIFEST_PATH.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
