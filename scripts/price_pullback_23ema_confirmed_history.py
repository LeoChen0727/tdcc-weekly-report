"""23EMA's original buy-ranked confirmations, never reconstructed from signals."""
from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path
import re
from typing import Mapping

import pandas as pd

from daily_snapshot_revision_utils import (
    MANIFEST_NAME,
    REQUIRED_MANIFEST_COLUMNS,
    SNAPSHOT_REPOSITORY_PATH,
    _require_path_under_snapshot_dir,
    _resolve_snapshot_path,
    normalize_report_date,
    normalize_revision_manifest_schema,
    normalize_snapshot_revision,
    snapshot_payload_sha256,
    snapshot_payload_sha256_candidates,
)


MODEL_ID = "price_pullback_23ema"
ARTIFACT_ID = "price_pullback_23ema_operation_section"
SNAPSHOT_STEM = "daily_price_pullback_23ema_operation_section"
# Earliest permitted forward capture, subject to the official source/runtime gates.
# History consumption is authorized by the model-owned 20261023 activation
# migration and pinned to the first real r1. It is not return or promotion proof.
CAPTURE_NOT_BEFORE_REPORT_DATE = "20261019"
CONFIRMATION_CONSUMER_ENABLED = True
FIRST_REAL_R1_REPORT_DATE = "20261019"
FIRST_REAL_R1_PATH = (
    "output/history/daily_model_snapshots/"
    "daily_price_pullback_23ema_operation_section_20261019_r1_d41214b72349.csv"
)
FIRST_REAL_R1_SHA256 = "d41214b72349a9683cd686636a5c750b03752caebfd2c85bbb5dcee718b9008f"
RANK_COLUMNS = ("model_rank", "display_rank", "model_rank_overall")
PROOF_COLUMNS = (
    "confirmation_source_artifact",
    "confirmation_source_sha256",
    "confirmation_row_sha256",
    "confirmation_snapshot_revision",
    "confirmation_snapshot_report_date",
)
IDENTITY_COLUMNS = ("stock_id", "signal_date", "report_line")
REQUIRED_ROW_COLUMNS = {
    "model_id", "row_type", "pdf_view", "pdf_section", "stock_id",
    "signal_date", "report_line", "operation_asof_date", "buy_rank_eligible",
}


def confirmation_row_sha256(row: Mapping[str, str]) -> str:
    """Hash all full-view string fields parsed from the canonical LF payload."""
    payload = json.dumps(dict(row), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def has_original_ranks(row: Mapping[str, str]) -> bool:
    return all(re.fullmatch(r"[1-9][0-9]*", str(row.get(field, ""))) for field in RANK_COLUMNS)


def load_prior_confirmed_operations(
    report_date: str,
    *,
    repository_root: Path,
    snapshot_dir: Path | None = None,
    manifest_path: Path | None = None,
) -> pd.DataFrame:
    """Read only r1 confirmations before report_date from the publisher manifest.

    Later revisions cannot introduce a position or upgrade an original unranked
    confirmation. Capture-only deployment cannot create positions, even when
    old files exist. An activated consumer must fail closed on missing history.
    """
    asof = normalize_report_date(report_date)
    if not asof:
        raise RuntimeError(f"invalid 23EMA confirmation report_date: {report_date!r}")
    if not CONFIRMATION_CONSUMER_ENABLED:
        result = pd.DataFrame()
        result.attrs.update(
            history_status=("capture_not_started" if asof < CAPTURE_NOT_BEFORE_REPORT_DATE
                            else "capture_only_consumer_disabled"),
            rejected_confirmations=[],
        )
        return result
    root = Path(repository_root).resolve()
    directory = Path(snapshot_dir or root / SNAPSHOT_REPOSITORY_PATH).resolve()
    manifest_file = Path(manifest_path or directory / MANIFEST_NAME)
    accepted: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []
    status = "missing_confirmation_manifest"
    if not manifest_file.is_file():
        raise RuntimeError("activated 23EMA confirmation consumer is missing its manifest")
    manifest = pd.read_csv(manifest_file, dtype=str, keep_default_na=False)
    missing = REQUIRED_MANIFEST_COLUMNS - set(manifest.columns)
    if missing:
        raise RuntimeError(f"23EMA confirmation manifest missing columns: {sorted(missing)}")
    manifest = normalize_revision_manifest_schema(manifest, source=manifest_file.as_posix())
    work = manifest[manifest["artifact_id"].eq(ARTIFACT_ID)].copy()
    if work.empty:
        raise RuntimeError("activated 23EMA confirmation consumer is missing its history family")
    work["_date"] = work["snapshot_report_date"].map(normalize_report_date)
    if work["_date"].eq("").any():
        raise RuntimeError("23EMA confirmation manifest has an invalid snapshot date")
    if work["_date"].lt(CAPTURE_NOT_BEFORE_REPORT_DATE).any():
        raise RuntimeError("23EMA confirmation snapshot predates forward capture start")
    work["_revision"] = work["snapshot_revision"].map(normalize_snapshot_revision)
    first_real = work[
        work["_date"].eq(FIRST_REAL_R1_REPORT_DATE) & work["_revision"].eq("r1")
    ]
    if len(first_real) != 1:
        raise RuntimeError("23EMA confirmation history requires exactly one pinned first real r1")
    first_source = first_real.iloc[0]
    if (str(first_source["snapshot_sha256"]) != FIRST_REAL_R1_SHA256
            or str(first_source["snapshot_path"]).replace("\\", "/") != FIRST_REAL_R1_PATH
            or str(first_source["supersedes_snapshot_sha256"])):
        raise RuntimeError("23EMA pinned first real r1 manifest identity mismatch")
    first_path = _resolve_snapshot_path(
        str(first_source["snapshot_path"]), repository_root=root,
        approved_relative_path=Path(FIRST_REAL_R1_PATH), snapshot_dir=directory,
    )
    _require_path_under_snapshot_dir(first_path, directory)
    if snapshot_payload_sha256(first_path.read_bytes()) != FIRST_REAL_R1_SHA256:
        raise RuntimeError("23EMA pinned first real r1 source SHA-256 mismatch")
    work = work[work["_date"].lt(asof)]
    status = "no_prior_confirmation_snapshot"
    for date, group in work.groupby("_date", sort=True):
        first = group[group["_revision"].eq("r1")]
        if len(first) != 1:
            raise RuntimeError(f"23EMA confirmation snapshot requires exactly one r1: {date}")
        source = first.iloc[0]
        expected_sha = str(source["snapshot_sha256"])
        if re.fullmatch(r"[0-9a-f]{64}", expected_sha) is None:
            raise RuntimeError(f"23EMA confirmation snapshot has invalid SHA-256: {date}")
        if str(source["supersedes_snapshot_sha256"]):
            raise RuntimeError(f"23EMA r1 confirmation snapshot cannot supersede another: {date}")
        filename = f"{SNAPSHOT_STEM}_{date}_r1_{expected_sha[:12]}.csv"
        legacy_name = f"{SNAPSHOT_STEM}_{date}.csv"
        name = Path(str(source["snapshot_path"]).replace("\\", "/")).name
        legacy = source["revision_reason"] == "legacy_v1_manifest"
        if name != filename and not (legacy and name == legacy_name):
            raise RuntimeError(f"23EMA confirmation snapshot path identity mismatch: {date}")
        relative = SNAPSHOT_REPOSITORY_PATH / name
        path = _resolve_snapshot_path(
            str(source["snapshot_path"]), repository_root=root,
            approved_relative_path=relative, snapshot_dir=directory,
        )
        _require_path_under_snapshot_dir(path, directory)
        payload = path.read_bytes()
        if expected_sha not in snapshot_payload_sha256_candidates(payload):
            raise RuntimeError(f"23EMA confirmation snapshot SHA-256 mismatch: {date}")
        canonical_payload = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        reader = csv.DictReader(io.StringIO(canonical_payload.decode("utf-8-sig"), newline=""))
        if not REQUIRED_ROW_COLUMNS.issubset(reader.fieldnames or []):
            raise RuntimeError(f"23EMA confirmation snapshot missing operation columns: {date}")
        pairs: dict[tuple[str, str, str], dict[str, dict[str, str]]] = {}
        for row in reader:
            if row["model_id"] != MODEL_ID or row["row_type"] != "data":
                continue
            if row["pdf_section"] not in {"confirmed_operation", "confirmed_unranked_operation"}:
                continue
            key = tuple(row[field] for field in IDENTITY_COLUMNS)
            if row["signal_date"] != date or row["operation_asof_date"] != date:
                raise RuntimeError(f"23EMA original confirmation date differs from snapshot: {key}")
            views = pairs.setdefault(key, {})
            if row["pdf_view"] not in {"full", "highlight"} or row["pdf_view"] in views:
                raise RuntimeError(f"23EMA original confirmation has duplicate/invalid view: {key}")
            views[row["pdf_view"]] = row
        status = "no_eligible_prior_confirmation"
        for key, views in pairs.items():
            if set(views) != {"full", "highlight"}:
                raise RuntimeError(f"23EMA original confirmation requires both views: {key}")
            full = views["full"]
            if {k: v for k, v in full.items() if k != "pdf_view"} != {
                k: v for k, v in views["highlight"].items() if k != "pdf_view"
            }:
                raise RuntimeError(f"23EMA original confirmation views conflict: {key}")
            proof = {
                "confirmation_source_artifact": relative.as_posix(),
                "confirmation_source_sha256": snapshot_payload_sha256(payload),
                "confirmation_row_sha256": confirmation_row_sha256(full),
                "confirmation_snapshot_revision": "r1",
                "confirmation_snapshot_report_date": date,
            }
            frozen = {**full, **proof}
            if full["pdf_section"] != "confirmed_operation" or full["buy_rank_eligible"] != "True":
                rejected.append({**frozen, "confirmation_rejection_reason": "original_confirmation_not_buy_ranked"})
            elif not has_original_ranks(full):
                rejected.append({**frozen, "confirmation_rejection_reason": "original_confirmation_missing_rank"})
            else:
                accepted.append(frozen)
    result = pd.DataFrame(accepted)
    result.attrs.update(
        history_status="original_confirmations_loaded" if accepted else status,
        rejected_confirmations=rejected,
    )
    return result
