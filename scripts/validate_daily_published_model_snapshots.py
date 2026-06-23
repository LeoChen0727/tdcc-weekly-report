from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, normalize_date, read_csv, safe_str  # noqa: E402
from update_daily_published_model_snapshots import (  # noqa: E402
    ARTIFACTS,
    MANIFEST_PATH,
    MANIFEST_COLUMNS,
    SNAPSHOT_DIR,
    freshness_state,
    sha256_file,
    snapshot_name,
    validate_artifact_frame,
)


FORBIDDEN_SNAPSHOT_PATH_FRAGMENTS = (
    "volume_breakout_operation_pdf_preview",
    "volume_breakout_confirmed_operation_rank",
    "volume_breakout_pending_operation_queue",
    "historical_pattern_operation_registry",
    "approved_operation_patterns",
    "daily_model_parameter_research",
    "daily_model_parameter_recommendations",
    "research/",
    "research\\",
    "tdcc_signals/",
    "tdcc_signals\\",
)


def true_text(value: object) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def warrant_grace_allows_publish(row: dict[str, str]) -> bool:
    return bool(
        safe_str(row.get("warrant_source_status", "")) == "warning_grace"
        and true_text(row.get("warrant_daily_publish_allowed", ""))
        and safe_str(row.get("warrant_pdf_visibility", "")) == "hidden_unavailable"
        and not true_text(row.get("warrant_model_effect_allowed", ""))
        and not true_text(row.get("warrant_pdf_effect_allowed", ""))
    )


def load_manifest(manifest_path: Path = MANIFEST_PATH) -> pd.DataFrame:
    manifest = read_csv(manifest_path, dtype=str)
    if manifest.empty:
        raise RuntimeError(f"{manifest_path.as_posix()} is missing or empty")
    migration_defaults = {
        "warrant_source_status": "ok",
        "warrant_daily_publish_allowed": "True",
        "warrant_pdf_visibility": "visible",
        "warrant_model_effect_allowed": "True",
        "warrant_pdf_effect_allowed": "True",
    }
    warrant_ready_values = (
        manifest["warrant_ready"]
        if "warrant_ready" in manifest.columns
        else pd.Series([""] * len(manifest), index=manifest.index)
    )
    for col, default in migration_defaults.items():
        if col not in manifest.columns:
            manifest[col] = warrant_ready_values.map(lambda value: default if safe_str(value) == "True" else "")
    missing = [col for col in MANIFEST_COLUMNS if col not in manifest.columns]
    if missing:
        raise RuntimeError(f"{manifest_path.as_posix()} missing columns: {missing}")
    return manifest[MANIFEST_COLUMNS].fillna("")


def validate_manifest_paths(manifest: pd.DataFrame, snapshot_dir: Path = SNAPSHOT_DIR) -> list[str]:
    errors: list[str] = []
    snapshot_root = snapshot_dir.as_posix().rstrip("/") + "/"
    for _, row in manifest.iterrows():
        source_path = safe_str(row.get("source_path", ""))
        snapshot_path = safe_str(row.get("snapshot_path", ""))
        combined = f"{source_path}\n{snapshot_path}"
        for fragment in FORBIDDEN_SNAPSHOT_PATH_FRAGMENTS:
            if fragment in combined:
                errors.append(f"{snapshot_path}: forbidden research/backtest artifact fragment {fragment}")
        if snapshot_path and not snapshot_path.startswith(snapshot_root):
            errors.append(f"{snapshot_path}: snapshot must stay under {snapshot_root}")
    return errors


def validate_current_report_snapshots(
    latest_dir: Path = LATEST_DIR,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
) -> list[str]:
    errors: list[str] = []
    try:
        state = freshness_state(latest_dir)
    except Exception as exc:
        return [str(exc)]

    report_date = state["main_price_date"]
    try:
        manifest = load_manifest(manifest_path)
    except Exception as exc:
        return [str(exc)]

    errors.extend(validate_manifest_paths(manifest, snapshot_dir))
    current = manifest[manifest["snapshot_report_date"].map(normalize_date).eq(report_date)]
    required_artifact_ids = {artifact.artifact_id for artifact in ARTIFACTS}
    observed_artifact_ids = {safe_str(value) for value in current["artifact_id"].tolist()}
    missing = sorted(required_artifact_ids - observed_artifact_ids)
    if missing:
        errors.append(f"manifest missing current report_date={report_date} artifact rows: {missing}")

    duplicate_keys = current.duplicated(subset=["snapshot_report_date", "artifact_id"], keep=False)
    if duplicate_keys.any():
        duplicates = current.loc[duplicate_keys, ["snapshot_report_date", "artifact_id"]].to_dict("records")
        errors.append(f"manifest has duplicate current snapshot rows: {duplicates}")

    artifacts_by_id = {artifact.artifact_id: artifact for artifact in ARTIFACTS}
    for _, row in current.iterrows():
        artifact_id = safe_str(row.get("artifact_id", ""))
        artifact = artifacts_by_id.get(artifact_id)
        if artifact is None:
            errors.append(f"unknown artifact_id in manifest: {artifact_id}")
            continue

        source = latest_dir / artifact.source_name
        expected_snapshot = snapshot_dir / snapshot_name(artifact, report_date)
        snapshot = Path(safe_str(row.get("snapshot_path", "")))
        if snapshot != expected_snapshot:
            errors.append(
                f"{artifact_id}: snapshot_path must be {expected_snapshot.as_posix()}, observed={snapshot.as_posix()}"
            )

        if not source.exists():
            errors.append(f"{artifact_id}: source missing: {source.as_posix()}")
            continue
        if not snapshot.exists():
            errors.append(f"{artifact_id}: snapshot missing: {snapshot.as_posix()}")
            continue

        try:
            validate_artifact_frame(snapshot, artifact, report_date)
        except Exception as exc:
            errors.append(f"{artifact_id}: {exc}")

        source_hash = sha256_file(source)
        snapshot_hash = sha256_file(snapshot)
        if safe_str(row.get("source_sha256", "")) != source_hash:
            errors.append(f"{artifact_id}: source_sha256 does not match current source")
        if safe_str(row.get("snapshot_sha256", "")) != snapshot_hash:
            errors.append(f"{artifact_id}: snapshot_sha256 does not match snapshot file")
        if source_hash != snapshot_hash:
            errors.append(f"{artifact_id}: source and snapshot hashes differ")

        try:
            df = pd.read_csv(snapshot, dtype=str)
        except Exception as exc:
            errors.append(f"{artifact_id}: failed to read snapshot CSV: {exc}")
            continue
        if safe_str(row.get("row_count", "")) != str(len(df)):
            errors.append(f"{artifact_id}: row_count mismatch")
        if safe_str(row.get("column_count", "")) != str(len(df.columns)):
            errors.append(f"{artifact_id}: column_count mismatch")
        if safe_str(row.get("main_price_date", "")) != report_date:
            errors.append(f"{artifact_id}: main_price_date mismatch")
        for col in ("report_ready", "daily_pdf_ready"):
            if safe_str(row.get(col, "")) != "True":
                errors.append(f"{artifact_id}: {col} must be True")
        if safe_str(row.get("warrant_ready", "")) != "True" and not warrant_grace_allows_publish(row):
            errors.append(f"{artifact_id}: warrant_ready must be True unless bounded warrant grace hides effects")
        if safe_str(row.get("purpose", "")) != "as_published_daily_model_snapshot":
            errors.append(f"{artifact_id}: unexpected purpose")

    return errors


def main() -> int:
    errors = validate_current_report_snapshots()
    if errors:
        print("ERROR: daily published model snapshot validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    state = freshness_state()
    print(f"daily published model snapshot validation passed for report_date={state['main_price_date']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
