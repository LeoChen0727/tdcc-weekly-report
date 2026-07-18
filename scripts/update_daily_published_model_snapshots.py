from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
from collections.abc import Collection
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
ALLOW_SNAPSHOT_REWRITE_ENV = "ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE"
REQUIRED_READY_COLUMNS = ["report_ready", "daily_pdf_ready"]
WARRANT_GRACE_COLUMNS = (
    "warrant_source_status",
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
    "warrant_model_effect_allowed",
    "warrant_pdf_effect_allowed",
)


@dataclass(frozen=True)
class SnapshotArtifact:
    artifact_id: str
    source_name: str
    snapshot_stem: str
    required_columns: tuple[str, ...] = ()
    date_columns: tuple[str, ...] = ()
    block_same_date_rewrite: bool = False


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
        required_columns=(
            "signal_date",
            "stock_id",
            "model_id",
            "model_name_zh",
            "model_score",
            "base_model_score",
            "operation_score",
            "tdcc_score",
            "pattern_score",
            "risk_penalty",
            "final_rank_score",
            "rank_reason_zh",
        ),
        date_columns=("signal_date",),
    ),
    SnapshotArtifact(
        artifact_id="all_candidates_source_rows",
        source_name="all_candidates_latest.csv",
        snapshot_stem="all_candidates",
        required_columns=(
            "date",
            "signal_date",
            "main_price_date",
            "stock_id",
            "stock_name",
            "category",
            "candidate_source_type",
            "candidate_line",
            "candidate_line_group",
            "source_row_index",
            "close",
            "ema23",
            "ma20",
            "distance_to_ema23_pct",
            "gap_ema23_pct",
            "platform_low",
            "short_platform_low",
            "previous_20d_low",
            "low_20",
            "ma5_turning_up_flag",
            "ma10_turning_up_flag",
            "volume_ratio",
            "return_20d",
            "latest_revenue_yoy",
            "cumulative_revenue_yoy",
            "off_60d_low_pct",
            "tdcc_judgement",
            "tdcc_accumulation_signal",
            "warrant_flow_signal",
            "false_breakout_risk",
        ),
        date_columns=("date", "signal_date", "main_price_date"),
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
        block_same_date_rewrite=True,
        required_columns=(
            "model_id",
            "pdf_view",
            "pdf_section",
            "row_type",
            "buy_rank_eligible",
            "selected_trigger_id",
            "operation_score",
            "tdcc_score",
            "pattern_score",
            "risk_penalty",
            "final_rank_score",
            "entry_rule_id",
            "stop_loss_rule_id",
            "stop_loss_price",
            "exit_rule_id",
            "planned_holding_days",
        ),
    ),
    SnapshotArtifact(
        artifact_id="volume_breakout_operation_evidence_audit",
        source_name="daily_volume_breakout_operation_evidence_audit_latest.csv",
        snapshot_stem="daily_volume_breakout_operation_evidence_audit",
        block_same_date_rewrite=True,
        required_columns=(
            "model_id",
            "operation_asof_date",
            "stock_id",
            "signal_date",
            "selected_trigger_id",
            "selected_confirmation_date",
            "operation_lifecycle_state",
            "audit_status",
            "included_in_daily_adapter",
            "reason",
        ),
    ),
    SnapshotArtifact(
        artifact_id="w_bottom_right_side_operation_section",
        source_name="daily_w_bottom_right_side_operation_section_latest.csv",
        snapshot_stem="daily_w_bottom_right_side_operation_section",
        required_columns=(
            "model_id",
            "pdf_view",
            "pdf_section",
            "row_type",
            "buy_rank_eligible",
            "row_action_status",
            "entry_rule_id",
            "stop_loss_rule_id",
            "stop_loss_price",
            "exit_rule_id",
            "planned_holding_days",
        ),
    ),
    SnapshotArtifact(
        artifact_id="neckline_volume_breakout_confirmation_operation_section",
        source_name="daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
        snapshot_stem="daily_neckline_volume_breakout_confirmation_operation_section",
        required_columns=(
            "model_id",
            "pdf_view",
            "pdf_section",
            "row_type",
            "buy_rank_eligible",
            "row_action_status",
            "entry_rule_id",
            "stop_loss_rule_id",
            "stop_loss_price",
            "exit_rule_id",
            "planned_holding_days",
        ),
    ),
)
ARTIFACTS_BY_ID = {artifact.artifact_id: artifact for artifact in ARTIFACTS}

MANIFEST_COLUMNS = [
    "snapshot_report_date",
    "generated_at",
    "pipeline_commit_sha",
    "main_price_date",
    "report_ready",
    "warrant_ready",
    "warrant_source_status",
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
    "warrant_model_effect_allowed",
    "warrant_pdf_effect_allowed",
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
    # Published model snapshots are CSV/text artifacts committed from Linux
    # Actions and also validated from Windows worktrees. Normalize line endings
    # so Git checkout CRLF conversion cannot create false hash mismatches.
    # Do not strip a UTF-8 BOM here: snapshot_sha256 is an established immutable
    # manifest-v1 identity. The formal-lineage audit records its separate
    # BOM-insensitive canonical hash without rewriting historical manifests.
    digest = hashlib.sha256()
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    digest.update(data)
    return digest.hexdigest()


def csv_shape(path: Path) -> tuple[int, int]:
    df = pd.read_csv(path, dtype=str)
    return len(df), len(df.columns)


def true_text(value: object) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def warrant_grace_allows_publish(row: pd.Series) -> bool:
    return bool(
        safe_str(row.get("warrant_source_status", "")) == "warning_grace"
        and true_text(row.get("warrant_daily_publish_allowed", ""))
        and safe_str(row.get("warrant_pdf_visibility", "")) == "hidden_unavailable"
        and not true_text(row.get("warrant_model_effect_allowed", ""))
        and not true_text(row.get("warrant_pdf_effect_allowed", ""))
    )


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
    warrant_ready = safe_str(row.get("warrant_ready", ""))
    if warrant_ready != "True" and not warrant_grace_allows_publish(row):
        raise RuntimeError(
            "warrant_ready must be True before publishing model snapshots unless bounded "
            f"warrant_unavailable grace hides warrant effects; observed={warrant_ready}"
        )
    state["warrant_ready"] = warrant_ready
    if warrant_ready == "True":
        defaults = {
            "warrant_source_status": "ok",
            "warrant_daily_publish_allowed": "True",
            "warrant_pdf_visibility": "visible",
            "warrant_model_effect_allowed": "True",
            "warrant_pdf_effect_allowed": "True",
        }
    else:
        defaults = {col: "" for col in WARRANT_GRACE_COLUMNS}
    for col in WARRANT_GRACE_COLUMNS:
        state[col] = safe_str(row.get(col, "")) or defaults[col]
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


def snapshot_rewrite_allowed() -> bool:
    return safe_str(os.environ.get(ALLOW_SNAPSHOT_REWRITE_ENV, "")).lower() in {"1", "true", "yes", "y"}


def guard_existing_snapshot(source: Path, target: Path, artifact: SnapshotArtifact, report_date: str) -> None:
    if not artifact.block_same_date_rewrite:
        return
    if not target.exists():
        return
    source_hash = sha256_file(source)
    target_hash = sha256_file(target)
    if source_hash == target_hash:
        return
    if snapshot_rewrite_allowed():
        return
    raise RuntimeError(
        "published daily model snapshot rewrite blocked: "
        f"report_date={report_date} artifact_id={artifact.artifact_id} "
        f"source={source.as_posix()} target={target.as_posix()} "
        f"source_sha256={source_hash} existing_snapshot_sha256={target_hash}; "
        f"set {ALLOW_SNAPSHOT_REWRITE_ENV}=1 only for an explicit correction run"
    )


def selected_artifacts(artifact_ids: Collection[str] | None) -> tuple[SnapshotArtifact, ...]:
    if artifact_ids is None:
        return ARTIFACTS
    requested = {safe_str(artifact_id) for artifact_id in artifact_ids if safe_str(artifact_id)}
    if not requested:
        raise RuntimeError("explicit daily snapshot artifact selection must not be empty")
    unknown = sorted(requested - set(ARTIFACTS_BY_ID))
    if unknown:
        raise RuntimeError(f"unknown daily snapshot artifact ids: {unknown}")
    return tuple(artifact for artifact in ARTIFACTS if artifact.artifact_id in requested)


def build_daily_published_model_snapshots(
    latest_dir: Path = LATEST_DIR,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
    generated_at: str | None = None,
    commit_sha: str | None = None,
    artifact_ids: Collection[str] | None = None,
) -> pd.DataFrame:
    state = freshness_state(latest_dir)
    report_date = state["main_price_date"]
    generated_at = generated_at or now_text()
    commit_sha = commit_sha if commit_sha is not None else git_sha()
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    old_manifest = read_csv(manifest_path, dtype=str)
    if not old_manifest.empty:
        for col in MANIFEST_COLUMNS:
            if col not in old_manifest.columns:
                old_manifest[col] = ""
        old_manifest = old_manifest[MANIFEST_COLUMNS]

    rows: list[dict[str, str]] = []
    for artifact in selected_artifacts(artifact_ids):
        source = latest_dir / artifact.source_name
        if not source.exists():
            raise RuntimeError(f"required daily published artifact is missing: {source.as_posix()}")

        validate_artifact_frame(source, artifact, report_date)
        target = snapshot_dir / snapshot_name(artifact, report_date)
        existing_rows = (
            old_manifest[
                old_manifest["snapshot_report_date"].map(normalize_date).eq(report_date)
                & old_manifest["artifact_id"].astype(str).eq(artifact.artifact_id)
            ]
            if not old_manifest.empty
            else pd.DataFrame(columns=MANIFEST_COLUMNS)
        )
        if len(existing_rows) > 1:
            raise RuntimeError(
                "duplicate current daily snapshot manifest rows: "
                f"report_date={report_date} artifact_id={artifact.artifact_id}"
            )
        if target.exists() and sha256_file(source) == sha256_file(target) and len(existing_rows) == 1:
            rows.append(
                {column: safe_str(existing_rows.iloc[0].get(column, "")) for column in MANIFEST_COLUMNS}
            )
            continue
        guard_existing_snapshot(source, target, artifact, report_date)
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
                "warrant_source_status": state["warrant_source_status"],
                "warrant_daily_publish_allowed": state["warrant_daily_publish_allowed"],
                "warrant_pdf_visibility": state["warrant_pdf_visibility"],
                "warrant_model_effect_allowed": state["warrant_model_effect_allowed"],
                "warrant_pdf_effect_allowed": state["warrant_pdf_effect_allowed"],
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
    if old_manifest.empty:
        combined = new_manifest
    else:
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


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish immutable daily model snapshots")
    parser.add_argument(
        "--artifact-id",
        action="append",
        choices=sorted(ARTIFACTS_BY_ID),
        help="Publish only the named artifact family; repeat for multiple families",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        manifest_rows = build_daily_published_model_snapshots(artifact_ids=args.artifact_id)
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
