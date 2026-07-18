from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    HISTORY_DIR,
    LATEST_DIR,
    RESEARCH_LATEST_DIR,
    STOCK_PRICE_HISTORY_DIR,
    markdown_table,
    normalize_code,
    normalize_date,
    now_text,
    safe_str,
    to_number,
    write_csv,
)


SNAPSHOT_DIR = HISTORY_DIR / "daily_model_snapshots"
MANIFEST_CSV = SNAPSHOT_DIR / "daily_published_model_snapshot_manifest.csv"
RESEARCH_HISTORY_DIR = HISTORY_DIR / "research"

OUT_CSV = RESEARCH_LATEST_DIR / "daily_published_snapshot_ranking_backtest_latest.csv"
OUT_MD = RESEARCH_LATEST_DIR / "daily_published_snapshot_ranking_backtest_latest.md"
EVENTS_CSV = RESEARCH_HISTORY_DIR / "daily_published_snapshot_ranking_events.csv"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name
VOLUME_V2_LINEAGE_AUDIT_CSV = LATEST_DIR / "volume_v2_warrant_lineage_history_audit_latest.csv"

HORIZONS = [1, 3, 5, 10]
VOLUME_V2_MODEL_IDS = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
}
VOLUME_V2_LINEAGE_AUDIT_REQUIRED_COLUMNS = {
    "snapshot_report_date",
    "signal_date",
    "model_id",
    "stock_id",
    "formal_row_sha256",
    "formal_snapshot_sha256",
    "paired_source_resolution",
    "production_code_sha256",
    "watch_artifact_sha256",
    "candidate_artifact_sha256",
    "official_warrant_artifact_sha256",
    "formal_row_disposition",
    "evidence_status",
}
VOLUME_V2_LINEAGE_SOURCE_SHA_COLUMNS = (
    "production_code_sha256",
    "watch_artifact_sha256",
    "candidate_artifact_sha256",
    "official_warrant_artifact_sha256",
)
VOLUME_V2_EXACT_PAIRED_SOURCE_RESOLUTIONS = {
    "current_worktree_exact_source_files",
    "published_snapshot_exact_current_sources_pending_commit",
    "manifest_pipeline_commit_exact_source_blob",
    "snapshot_history_exact_blob_fallback",
}
REQUIRED_ARTIFACT_IDS = {
    "model_signals_for_report",
    "volume_breakout_operation_section",
}
MODEL_SIGNAL_COLUMNS = {
    "signal_date",
    "stock_id",
    "stock_name",
    "model_id",
    "model_name_zh",
    "model_score",
}
VOLUME_OPERATION_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "row_type",
    "stock_id",
    "signal_date",
    "buy_rank_eligible",
}
PRICE_COLUMNS = {"date", "open", "high", "low", "close"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_text_bytes(payload: bytes) -> bytes:
    text_payload = payload.decode("utf-8-sig")
    return text_payload.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def canonical_text_sha256(path: Path) -> str:
    return hashlib.sha256(canonical_text_bytes(path.read_bytes())).hexdigest()


def published_manifest_v1_sha256_candidates(path: Path) -> set[str]:
    """Read-only compatibility for immutable pre-canonical manifest-v1 rows.

    Older publishers pinned raw, LF, or CRLF bytes. These candidates are used
    only to validate that legacy container manifest; formal lineage eligibility
    always requires the single BOM-insensitive canonical hash above.
    """

    raw = path.read_bytes()
    lf = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {hashlib.sha256(payload).hexdigest() for payload in (raw, lf, crlf)}


def normalize_lineage_text(value: Any) -> str:
    if value is None:
        return ""
    text_value = str(value).strip()
    return "" if text_value.lower() == "nan" else text_value


def canonical_row_sha256(row: pd.Series | dict[str, Any]) -> str:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    normalized = {
        str(key): normalize_lineage_text(value) for key, value in values.items()
    }
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(canonical_text_bytes(payload)).hexdigest()


def is_sha256(value: Any) -> bool:
    text_value = safe_str(value).lower()
    return len(text_value) == 64 and all(char in "0123456789abcdef" for char in text_value)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def load_volume_v2_lineage_audit(
    path: Path = VOLUME_V2_LINEAGE_AUDIT_CSV,
) -> tuple[dict[tuple[str, str, str], list[dict[str, str]]], str]:
    audit = read_csv(path)
    if audit.empty:
        return {}, ""
    missing = sorted(VOLUME_V2_LINEAGE_AUDIT_REQUIRED_COLUMNS - set(audit.columns))
    if missing:
        raise RuntimeError(
            "volume v2 lineage audit missing columns: "
            f"audit={path.as_posix()} missing={missing}"
        )
    work = audit.copy()
    work["_signal_date"] = work["signal_date"].map(normalize_date)
    work["_model_id"] = work["model_id"].map(safe_str)
    work["_stock_id"] = work["stock_id"].map(normalize_code)
    index: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for _, row in work.iterrows():
        key = (row["_signal_date"], row["_model_id"], row["_stock_id"])
        evidence = {
            column: safe_str(row.get(column, "")) for column in audit.columns
        }
        index.setdefault(key, []).append(evidence)
    return index, sha256_file(path)


def load_formal_snapshot_lineage_index(
    manifest: pd.DataFrame,
) -> dict[tuple[str, str, str], list[dict[str, str]]]:
    index: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    formal_manifest = manifest[
        manifest["artifact_id"].astype(str).eq("model_signals_for_report")
    ]
    for _, manifest_row in formal_manifest.iterrows():
        report_date = normalize_date(manifest_row.get("snapshot_report_date", ""))
        path = Path(safe_str(manifest_row.get("snapshot_path", "")))
        formal = read_csv(path)
        if formal.empty:
            continue
        snapshot_sha256 = canonical_text_sha256(path)
        for _, row in formal.iterrows():
            model_id = safe_str(row.get("model_id", ""))
            if model_id not in VOLUME_V2_MODEL_IDS:
                continue
            stock_id = normalize_code(row.get("stock_id", ""))
            signal_date = normalize_date(row.get("signal_date", "")) or report_date
            if not stock_id or not signal_date:
                continue
            key = (signal_date, model_id, stock_id)
            index.setdefault(key, []).append(
                {
                    "formal_row_sha256": canonical_row_sha256(row),
                    "formal_snapshot_sha256": snapshot_sha256,
                    "formal_snapshot_path": path.as_posix(),
                }
            )
    return index


def volume_v2_lineage_payload(
    *,
    signal_date: str,
    model_id: str,
    stock_id: str,
    audit_index: dict[tuple[str, str, str], list[dict[str, str]]],
    formal_snapshot_index: dict[tuple[str, str, str], list[dict[str, str]]],
    audit_path: Path,
    audit_sha256: str,
) -> dict[str, str]:
    blank_hash_payload = {
        "lineage_formal_row_sha256": "",
        "lineage_observed_formal_row_sha256": "",
        "lineage_formal_snapshot_sha256": "",
        "lineage_observed_formal_snapshot_sha256": "",
        "lineage_paired_source_resolution": "",
        "lineage_production_code_sha256": "",
        "lineage_watch_artifact_sha256": "",
        "lineage_candidate_artifact_sha256": "",
        "lineage_official_warrant_artifact_sha256": "",
    }
    if model_id not in VOLUME_V2_MODEL_IDS:
        return {
            "lineage_gate_status": "not_applicable",
            "lineage_formal_row_disposition": "not_applicable",
            "lineage_evidence_status": "not_applicable",
            "lineage_audit_source": "",
            "lineage_audit_source_sha256": "",
            "summary_evidence_eligible": "True",
            "lineage_gate_pass_for_promotion_evidence": "not_applicable",
            **blank_hash_payload,
        }
    key = (normalize_date(signal_date), safe_str(model_id), normalize_code(stock_id))
    evidence_rows = audit_index.get(key, [])
    observed_rows = formal_snapshot_index.get(key, [])
    if not evidence_rows:
        return {
            "lineage_gate_status": "uncovered_fail_closed",
            "lineage_formal_row_disposition": "uncovered",
            "lineage_evidence_status": "missing",
            "lineage_audit_source": audit_path.as_posix(),
            "lineage_audit_source_sha256": audit_sha256,
            "summary_evidence_eligible": "False",
            "lineage_gate_pass_for_promotion_evidence": "False",
            **blank_hash_payload,
        }
    exact_matches = [
        (evidence, observed)
        for evidence in evidence_rows
        for observed in observed_rows
        if safe_str(evidence.get("formal_row_sha256", ""))
        == safe_str(observed.get("formal_row_sha256", ""))
        and safe_str(evidence.get("formal_snapshot_sha256", ""))
        == safe_str(observed.get("formal_snapshot_sha256", ""))
    ]
    if len(exact_matches) != 1:
        return {
            "lineage_gate_status": "non_clean_excluded",
            "lineage_formal_row_disposition": "hash_mismatch",
            "lineage_evidence_status": "incomplete",
            "lineage_audit_source": audit_path.as_posix(),
            "lineage_audit_source_sha256": audit_sha256,
            "summary_evidence_eligible": "False",
            "lineage_gate_pass_for_promotion_evidence": "False",
            **blank_hash_payload,
            "lineage_observed_formal_row_sha256": "|".join(
                sorted(
                    {
                        safe_str(row.get("formal_row_sha256", ""))
                        for row in observed_rows
                        if safe_str(row.get("formal_row_sha256", ""))
                    }
                )
            ),
            "lineage_observed_formal_snapshot_sha256": "|".join(
                sorted(
                    {
                        safe_str(row.get("formal_snapshot_sha256", ""))
                        for row in observed_rows
                        if safe_str(row.get("formal_snapshot_sha256", ""))
                    }
                )
            ),
        }
    evidence, observed = exact_matches[0]
    disposition = safe_str(evidence.get("formal_row_disposition", ""))
    evidence_status = safe_str(evidence.get("evidence_status", ""))
    paired_resolution = safe_str(evidence.get("paired_source_resolution", ""))
    source_hashes_complete = all(
        is_sha256(evidence.get(column, ""))
        for column in VOLUME_V2_LINEAGE_SOURCE_SHA_COLUMNS
    )
    exact_source_pair = paired_resolution in VOLUME_V2_EXACT_PAIRED_SOURCE_RESOLUTIONS
    clean = (
        disposition == "verified_clean"
        and evidence_status == "complete"
        and exact_source_pair
        and source_hashes_complete
    )
    return {
        "lineage_gate_status": "verified_clean" if clean else "non_clean_excluded",
        "lineage_formal_row_disposition": disposition or "missing",
        "lineage_evidence_status": evidence_status or "missing",
        "lineage_audit_source": audit_path.as_posix(),
        "lineage_audit_source_sha256": audit_sha256,
        "summary_evidence_eligible": "True" if clean else "False",
        "lineage_gate_pass_for_promotion_evidence": "True" if clean else "False",
        "lineage_formal_row_sha256": safe_str(evidence.get("formal_row_sha256", "")),
        "lineage_observed_formal_row_sha256": safe_str(
            observed.get("formal_row_sha256", "")
        ),
        "lineage_formal_snapshot_sha256": safe_str(
            evidence.get("formal_snapshot_sha256", "")
        ),
        "lineage_observed_formal_snapshot_sha256": safe_str(
            observed.get("formal_snapshot_sha256", "")
        ),
        "lineage_paired_source_resolution": paired_resolution,
        "lineage_production_code_sha256": safe_str(
            evidence.get("production_code_sha256", "")
        ),
        "lineage_watch_artifact_sha256": safe_str(
            evidence.get("watch_artifact_sha256", "")
        ),
        "lineage_candidate_artifact_sha256": safe_str(
            evidence.get("candidate_artifact_sha256", "")
        ),
        "lineage_official_warrant_artifact_sha256": safe_str(
            evidence.get("official_warrant_artifact_sha256", "")
        ),
    }


def pct_text(value: Any) -> str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return f"{num:.2f}%"


def normalize_bool_text(value: Any) -> str:
    return "True" if safe_str(value).lower() in {"true", "1", "1.0", "yes", "y"} else "False"


def score_decile(value: Any) -> str:
    score = to_number(value)
    if math.isnan(score):
        return "score_missing"
    lower = int(max(0, min(9, math.floor(score / 10)))) * 10
    upper = lower + 10
    if upper > 100:
        lower, upper = 90, 100
    upper_text = "100" if upper == 100 else f"{upper:02d}"
    return f"score_{lower:02d}_{upper_text}"


def rank_bucket(value: Any) -> str:
    rank = to_number(value)
    if math.isnan(rank) or rank <= 0:
        return "rank_missing"
    if rank <= 5:
        return "rank_001_005"
    if rank <= 10:
        return "rank_006_010"
    if rank <= 20:
        return "rank_011_020"
    return "rank_021_plus"


def mainstream_segment(row: pd.Series) -> str:
    for col in ["report_bucket", "report_line", "effective_mainstream_label"]:
        value = safe_str(row.get(col, ""))
        if value:
            return value
    return "segment_unknown"


def validate_snapshot_row(row: pd.Series, snapshot_root: Path = SNAPSHOT_DIR) -> list[str]:
    errors: list[str] = []
    snapshot_path = Path(safe_str(row.get("snapshot_path", "")))
    if not snapshot_path.exists():
        errors.append(f"missing snapshot file: {snapshot_path.as_posix()}")
        return errors

    root = snapshot_root.as_posix().rstrip("/") + "/"
    if not snapshot_path.as_posix().startswith(root):
        errors.append(f"{snapshot_path.as_posix()}: snapshot must stay under {root}")

    # snapshot_sha256 is the established manifest-v1 identity, which preserves
    # a UTF-8 BOM. Formal row lineage below uses canonical_text_sha256 instead.
    expected_hash = safe_str(row.get("snapshot_sha256", ""))
    if expected_hash and expected_hash not in published_manifest_v1_sha256_candidates(
        snapshot_path
    ):
        errors.append(f"{snapshot_path.as_posix()}: snapshot_sha256 mismatch")

    try:
        df = pd.read_csv(snapshot_path, dtype=str)
    except Exception as exc:
        errors.append(f"{snapshot_path.as_posix()}: failed to read CSV: {exc}")
        return errors

    if safe_str(row.get("row_count", "")) != str(len(df)):
        errors.append(f"{snapshot_path.as_posix()}: row_count mismatch")
    if safe_str(row.get("column_count", "")) != str(len(df.columns)):
        errors.append(f"{snapshot_path.as_posix()}: column_count mismatch")
    return errors


def load_manifest(manifest_path: Path = MANIFEST_CSV, snapshot_root: Path = SNAPSHOT_DIR) -> pd.DataFrame:
    manifest = read_csv(manifest_path)
    if manifest.empty:
        raise RuntimeError(f"missing or empty daily published snapshot manifest: {manifest_path.as_posix()}")

    required_cols = {
        "snapshot_report_date",
        "artifact_id",
        "snapshot_path",
        "snapshot_sha256",
        "row_count",
        "column_count",
        "purpose",
    }
    missing = required_cols - set(manifest.columns)
    if missing:
        raise RuntimeError(f"manifest missing columns: {sorted(missing)}")

    manifest = manifest.copy()
    manifest["snapshot_report_date"] = manifest["snapshot_report_date"].map(normalize_date)
    manifest = manifest[manifest["purpose"].astype(str).eq("as_published_daily_model_snapshot")]
    if manifest.empty:
        raise RuntimeError("manifest has no as_published_daily_model_snapshot rows")

    errors: list[str] = []
    duplicate_mask = manifest.duplicated(subset=["snapshot_report_date", "artifact_id"], keep=False)
    if duplicate_mask.any():
        dupes = manifest.loc[duplicate_mask, ["snapshot_report_date", "artifact_id"]].to_dict("records")
        errors.append(f"duplicate snapshot manifest keys: {dupes}")

    for _, row in manifest.iterrows():
        if safe_str(row.get("artifact_id", "")) in REQUIRED_ARTIFACT_IDS:
            errors.extend(validate_snapshot_row(row, snapshot_root=snapshot_root))

    by_date = manifest.groupby("snapshot_report_date")["artifact_id"].apply(set)
    for report_date, artifact_ids in by_date.items():
        missing_ids = sorted(REQUIRED_ARTIFACT_IDS - artifact_ids)
        if missing_ids:
            errors.append(f"report_date={report_date} missing required snapshot artifacts: {missing_ids}")

    if errors:
        raise RuntimeError("daily published snapshot manifest validation failed:\n" + "\n".join(errors))

    return manifest


def snapshot_path_for(manifest: pd.DataFrame, report_date: str, artifact_id: str) -> Path:
    part = manifest[
        manifest["snapshot_report_date"].astype(str).eq(report_date)
        & manifest["artifact_id"].astype(str).eq(artifact_id)
    ]
    if part.empty:
        return Path()
    return Path(safe_str(part.iloc[0].get("snapshot_path", "")))


def load_price_frame(stock_id: str, price_dir: Path = STOCK_PRICE_HISTORY_DIR) -> pd.DataFrame:
    path = price_dir / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    df = read_csv(path)
    if df.empty or not PRICE_COLUMNS.issubset(df.columns):
        return pd.DataFrame()
    out = df.copy()
    out["date"] = out["date"].map(normalize_date)
    for col in ["open", "high", "low", "close"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.dropna(subset=["date", "open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)
    return out


def forward_metrics(price: pd.DataFrame, anchor_date: str) -> dict[str, Any]:
    empty = {
        "entry_date": "",
        "entry_open_price": "",
        "forward_window_status": "missing_price_history",
    }
    for horizon in HORIZONS:
        empty[f"return_d{horizon}_close_pct"] = ""
        empty[f"mfe_d{horizon}_pct"] = ""
        empty[f"mae_d{horizon}_pct"] = ""
    if price.empty:
        return empty

    anchor = normalize_date(anchor_date)
    future = price[price["date"].astype(str).gt(anchor)].copy().sort_values("date").reset_index(drop=True)
    if future.empty:
        empty["forward_window_status"] = "no_forward_price"
        return empty

    entry = future.iloc[0]
    entry_price = float(entry["open"])
    out: dict[str, Any] = {
        "entry_date": safe_str(entry.get("date", "")),
        "entry_open_price": f"{entry_price:.4f}",
        "forward_window_status": "ready",
    }
    max_horizon = max(HORIZONS)
    if len(future) < max_horizon:
        out["forward_window_status"] = "partial_forward_price"

    for horizon in HORIZONS:
        if len(future) < horizon:
            out[f"return_d{horizon}_close_pct"] = ""
            out[f"mfe_d{horizon}_pct"] = ""
            out[f"mae_d{horizon}_pct"] = ""
            continue
        window = future.iloc[:horizon]
        close_price = float(window.iloc[-1]["close"])
        high_price = float(window["high"].max())
        low_price = float(window["low"].min())
        out[f"return_d{horizon}_close_pct"] = f"{(close_price / entry_price - 1.0) * 100.0:.4f}"
        out[f"mfe_d{horizon}_pct"] = f"{(high_price / entry_price - 1.0) * 100.0:.4f}"
        out[f"mae_d{horizon}_pct"] = f"{(low_price / entry_price - 1.0) * 100.0:.4f}"
    return out


def build_model_signal_events(
    manifest: pd.DataFrame,
    price_dir: Path = STOCK_PRICE_HISTORY_DIR,
    lineage_audit_path: Path = VOLUME_V2_LINEAGE_AUDIT_CSV,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    price_cache: dict[str, pd.DataFrame] = {}
    lineage_index, lineage_sha256 = load_volume_v2_lineage_audit(lineage_audit_path)
    formal_snapshot_index = load_formal_snapshot_lineage_index(manifest)
    for report_date in sorted(manifest["snapshot_report_date"].dropna().unique()):
        path = snapshot_path_for(manifest, report_date, "model_signals_for_report")
        signals = read_csv(path)
        if signals.empty:
            continue
        missing = MODEL_SIGNAL_COLUMNS - set(signals.columns)
        if missing:
            raise RuntimeError(f"{path.as_posix()} missing columns: {sorted(missing)}")

        for _, row in signals.iterrows():
            stock_id = normalize_code(row.get("stock_id", ""))
            if not stock_id:
                continue
            if stock_id not in price_cache:
                price_cache[stock_id] = load_price_frame(stock_id, price_dir=price_dir)
            display_rank = safe_str(row.get("display_rank", "")) or safe_str(row.get("model_rank", ""))
            anchor_date = normalize_date(row.get("signal_date", "")) or report_date
            model_id = safe_str(row.get("model_id", ""))
            lineage = volume_v2_lineage_payload(
                signal_date=anchor_date,
                model_id=model_id,
                stock_id=stock_id,
                audit_index=lineage_index,
                formal_snapshot_index=formal_snapshot_index,
                audit_path=lineage_audit_path,
                audit_sha256=lineage_sha256,
            )
            event = {
                "source_artifact": "model_signals_for_report",
                "snapshot_report_date": report_date,
                "stock_id": stock_id,
                "stock_name": safe_str(row.get("stock_name", "")),
                "model_id": model_id,
                "model_name_zh": safe_str(row.get("model_name_zh", "")),
                "report_line": safe_str(row.get("report_line", "")),
                "report_bucket": safe_str(row.get("report_bucket", "")),
                "mainstream_segment": mainstream_segment(row),
                "display_rank": display_rank,
                "rank_bucket": rank_bucket(display_rank),
                "model_score": safe_str(row.get("model_score", "")),
                "score_decile": score_decile(row.get("model_score", "")),
                "operation_section": "",
                "row_action_status": "",
                "buy_rank_eligible": "",
                "anchor_date": anchor_date,
                "ranking_evaluation_eligible": lineage["summary_evidence_eligible"],
                "trade_eligible": "False",
                "research_note": (
                    "as_published_model_ranking_truth;"
                    f"lineage_gate={lineage['lineage_gate_status']}"
                ),
            }
            event.update(lineage)
            event.update(forward_metrics(price_cache[stock_id], anchor_date))
            rows.append(event)
    return pd.DataFrame(rows)


def build_volume_operation_events(
    manifest: pd.DataFrame,
    price_dir: Path = STOCK_PRICE_HISTORY_DIR,
    lineage_audit_path: Path = VOLUME_V2_LINEAGE_AUDIT_CSV,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    price_cache: dict[str, pd.DataFrame] = {}
    lineage_index, lineage_sha256 = load_volume_v2_lineage_audit(lineage_audit_path)
    formal_snapshot_index = load_formal_snapshot_lineage_index(manifest)
    for report_date in sorted(manifest["snapshot_report_date"].dropna().unique()):
        path = snapshot_path_for(manifest, report_date, "volume_breakout_operation_section")
        ops = read_csv(path)
        if ops.empty:
            continue
        missing = VOLUME_OPERATION_COLUMNS - set(ops.columns)
        if missing:
            raise RuntimeError(f"{path.as_posix()} missing columns: {sorted(missing)}")

        work = ops[ops["row_type"].astype(str).eq("data")].copy()
        if "pdf_view" in work.columns and work["pdf_view"].astype(str).eq("full").any():
            work = work[work["pdf_view"].astype(str).eq("full")].copy()

        for _, row in work.iterrows():
            stock_id = normalize_code(row.get("stock_id", ""))
            if not stock_id:
                continue
            if stock_id not in price_cache:
                price_cache[stock_id] = load_price_frame(stock_id, price_dir=price_dir)
            section = safe_str(row.get("pdf_section", ""))
            confirmation_date = normalize_date(row.get("confirmation_date", ""))
            signal_date = normalize_date(row.get("signal_date", "")) or normalize_date(row.get("daily_signal_date", ""))
            anchor_date = confirmation_date if section in {"confirmed_operation", "active_operation"} else signal_date
            if not anchor_date:
                anchor_date = report_date
            model_id = safe_str(row.get("model_id", ""))
            lineage = volume_v2_lineage_payload(
                signal_date=signal_date,
                model_id=model_id,
                stock_id=stock_id,
                audit_index=lineage_index,
                formal_snapshot_index=formal_snapshot_index,
                audit_path=lineage_audit_path,
                audit_sha256=lineage_sha256,
            )
            trade_eligible = (
                section == "confirmed_operation"
                and safe_str(row.get("row_action_status", "")) == "confirmed_buy_candidate"
                and normalize_bool_text(row.get("buy_rank_eligible", "")) == "True"
                and lineage["summary_evidence_eligible"] == "True"
            )
            event = {
                "source_artifact": "volume_breakout_operation_section",
                "snapshot_report_date": report_date,
                "stock_id": stock_id,
                "stock_name": safe_str(row.get("stock_name", "")),
                "model_id": model_id,
                "model_name_zh": "放量攻擊模型",
                "report_line": "",
                "report_bucket": "",
                "mainstream_segment": "operation_section",
                "display_rank": safe_str(row.get("display_order", "")),
                "rank_bucket": rank_bucket(row.get("display_order", "")),
                "model_score": safe_str(row.get("research_score", "")),
                "score_decile": score_decile(row.get("research_score", "")),
                "operation_section": section,
                "row_action_status": safe_str(row.get("row_action_status", "")),
                "buy_rank_eligible": normalize_bool_text(row.get("buy_rank_eligible", "")),
                "anchor_date": anchor_date,
                "ranking_evaluation_eligible": "False",
                "trade_eligible": "True" if trade_eligible else "False",
                "research_note": (
                    "as_published_volume_operation_state;"
                    f"lineage_gate={lineage['lineage_gate_status']}"
                ),
            }
            event.update(lineage)
            event.update(forward_metrics(price_cache[stock_id], anchor_date))
            rows.append(event)
    return pd.DataFrame(rows)


def numeric_series(df: pd.DataFrame, col: str) -> pd.Series:
    if col not in df.columns:
        return pd.Series(dtype=float)
    return pd.to_numeric(df[col], errors="coerce")


def summarize_group(part: pd.DataFrame, segment_type: str, segment_value: str, generated_at: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "segment_type": segment_type,
        "segment_value": segment_value,
        "source_artifact": safe_str(part["source_artifact"].iloc[0]) if "source_artifact" in part.columns else "",
        "model_id": safe_str(part["model_id"].iloc[0]) if "model_id" in part.columns else "",
        "model_name_zh": safe_str(part["model_name_zh"].iloc[0]) if "model_name_zh" in part.columns else "",
        "sample_size": len(part),
        "report_date_min": safe_str(part["snapshot_report_date"].min()) if "snapshot_report_date" in part.columns else "",
        "report_date_max": safe_str(part["snapshot_report_date"].max()) if "snapshot_report_date" in part.columns else "",
        "snapshot_report_count": part["snapshot_report_date"].nunique() if "snapshot_report_date" in part.columns else 0,
        "generated_at": generated_at,
    }
    for horizon in HORIZONS:
        returns = numeric_series(part, f"return_d{horizon}_close_pct").dropna()
        row[f"evaluated_d{horizon}_count"] = len(returns)
        row[f"win_rate_d{horizon}"] = pct_text((returns.gt(0).mean() * 100.0) if len(returns) else math.nan)
        row[f"avg_return_d{horizon}"] = pct_text(returns.mean() if len(returns) else math.nan)
        row[f"median_return_d{horizon}"] = pct_text(returns.median() if len(returns) else math.nan)
        mfe = numeric_series(part, f"mfe_d{horizon}_pct").dropna()
        mae = numeric_series(part, f"mae_d{horizon}_pct").dropna()
        row[f"avg_mfe_d{horizon}"] = pct_text(mfe.mean() if len(mfe) else math.nan)
        row[f"avg_mae_d{horizon}"] = pct_text(mae.mean() if len(mae) else math.nan)
    min_eval = max(int(row.get("evaluated_d1_count", 0)), int(row.get("evaluated_d3_count", 0)))
    row["confidence_status"] = "ok_first_pass" if min_eval >= 100 else "small_or_early_snapshot_sample"
    row["advisory_only"] = "True"
    return row


def build_summary(events: pd.DataFrame, generated_at: str | None = None) -> pd.DataFrame:
    generated = generated_at or now_text()
    if events.empty:
        return pd.DataFrame()

    if "summary_evidence_eligible" in events.columns:
        eligible_events = events[
            events["summary_evidence_eligible"].astype(str).eq("True")
        ].copy()
        excluded_events = events[
            ~events["summary_evidence_eligible"].astype(str).eq("True")
        ].copy()
    else:
        eligible_events = events.copy()
        excluded_events = pd.DataFrame(columns=events.columns)

    rows: list[dict[str, Any]] = []
    group_specs = [
        ("model_overall", ["source_artifact", "model_id"]),
        ("model_report_bucket", ["source_artifact", "model_id", "report_bucket"]),
        ("model_mainstream_segment", ["source_artifact", "model_id", "mainstream_segment"]),
        ("model_rank_bucket", ["source_artifact", "model_id", "rank_bucket"]),
        ("model_score_decile", ["source_artifact", "model_id", "score_decile"]),
        ("volume_operation_section", ["source_artifact", "model_id", "operation_section"]),
    ]
    for segment_type, cols in group_specs:
        available = [col for col in cols if col in events.columns]
        if len(available) != len(cols):
            continue
        for key, part in eligible_events.groupby(available, dropna=False):
            values = key if isinstance(key, tuple) else (key,)
            if segment_type == "volume_operation_section" and values[0] != "volume_breakout_operation_section":
                continue
            if segment_type != "volume_operation_section" and values[0] == "volume_breakout_operation_section":
                continue
            segment_value = "|".join(safe_str(value) for value in values[1:] if safe_str(value))
            summary_row = summarize_group(part, segment_type, segment_value, generated)
            source_artifact = safe_str(summary_row.get("source_artifact"))
            model_id = safe_str(summary_row.get("model_id"))
            if excluded_events.empty:
                excluded_count = 0
            else:
                excluded_count = len(
                    excluded_events[
                        excluded_events["source_artifact"].astype(str).eq(source_artifact)
                        & excluded_events["model_id"].astype(str).eq(model_id)
                    ]
                )
            summary_row["lineage_excluded_count"] = excluded_count
            rows.append(summary_row)

    if not excluded_events.empty:
        exclusion_cols = [
            "source_artifact",
            "model_id",
            "lineage_gate_status",
            "lineage_formal_row_disposition",
        ]
        for key, part in excluded_events.groupby(exclusion_cols, dropna=False):
            source_artifact, model_id, gate_status, disposition = key
            row: dict[str, Any] = {
                "segment_type": "lineage_exclusion",
                "segment_value": "|".join(
                    [safe_str(model_id), safe_str(gate_status), safe_str(disposition)]
                ),
                "source_artifact": safe_str(source_artifact),
                "model_id": safe_str(model_id),
                "model_name_zh": safe_str(part["model_name_zh"].iloc[0]),
                "sample_size": len(part),
                "report_date_min": safe_str(part["snapshot_report_date"].min()),
                "report_date_max": safe_str(part["snapshot_report_date"].max()),
                "snapshot_report_count": part["snapshot_report_date"].nunique(),
                "generated_at": generated,
                "confidence_status": "excluded_from_summary_and_promotion_evidence",
                "advisory_only": "True",
                "lineage_excluded_count": len(part),
            }
            for horizon in HORIZONS:
                row[f"evaluated_d{horizon}_count"] = 0
                row[f"win_rate_d{horizon}"] = ""
                row[f"avg_return_d{horizon}"] = ""
                row[f"median_return_d{horizon}"] = ""
                row[f"avg_mfe_d{horizon}"] = ""
                row[f"avg_mae_d{horizon}"] = ""
            rows.append(row)

    out = pd.DataFrame(rows)
    existing_volume_sections: set[str] = set()
    if not out.empty:
        volume_rows = out[out["segment_type"].astype(str).eq("volume_operation_section")]
        existing_volume_sections = {
            safe_str(value).split("|")[-1]
            for value in volume_rows["segment_value"].astype(str).tolist()
            if safe_str(value)
        }
    for section in [
        "confirmed_operation",
        "confirmed_unranked_operation",
        "pending_confirmation",
        "active_operation",
    ]:
        if section in existing_volume_sections:
            continue
        row: dict[str, Any] = {
            "segment_type": "volume_operation_section",
            "segment_value": f"volume_range_breakout|{section}",
            "source_artifact": "volume_breakout_operation_section",
            "model_id": "volume_range_breakout",
            "model_name_zh": "放量攻擊模型",
            "sample_size": 0,
            "report_date_min": "",
            "report_date_max": "",
            "snapshot_report_count": 0,
            "generated_at": generated,
            "confidence_status": "empty_section_no_data_rows",
            "advisory_only": "True",
        }
        for horizon in HORIZONS:
            row[f"evaluated_d{horizon}_count"] = 0
            row[f"win_rate_d{horizon}"] = ""
            row[f"avg_return_d{horizon}"] = ""
            row[f"median_return_d{horizon}"] = ""
            row[f"avg_mfe_d{horizon}"] = ""
            row[f"avg_mae_d{horizon}"] = ""
        rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    sort_cols = [col for col in ["segment_type", "model_id", "segment_value"] if col in out.columns]
    return out.sort_values(sort_cols).reset_index(drop=True)


def write_markdown(summary: pd.DataFrame, events: pd.DataFrame, path: Path, generated_at: str) -> None:
    report_dates = sorted(events["snapshot_report_date"].dropna().astype(str).unique()) if not events.empty else []
    lineage_excluded_count = (
        int((~events["summary_evidence_eligible"].astype(str).eq("True")).sum())
        if not events.empty and "summary_evidence_eligible" in events.columns
        else 0
    )
    lines = [
        "# Daily Published Snapshot Ranking Backtest",
        "",
        f"generated_at: {generated_at}",
        f"snapshot_report_dates: {', '.join(report_dates) if report_dates else 'none'}",
        f"lineage_excluded_event_rows: {lineage_excluded_count}",
        "",
        "This research artifact uses date-stamped as-published snapshots only. It does not recalculate historical rankings with today's production model code and it does not mutate production parameters.",
        "",
        "## Summary",
        "",
        markdown_table(
            summary,
            [
                "segment_type",
                "segment_value",
                "model_id",
                "sample_size",
                "evaluated_d1_count",
                "win_rate_d1",
                "avg_return_d1",
                "median_return_d1",
                "evaluated_d5_count",
                "win_rate_d5",
                "avg_return_d5",
                "median_return_d5",
                "confidence_status",
            ],
            limit=80,
        ),
        "",
        "## Notes",
        "",
        "- Entry basis: next trading day open after the snapshot signal date or operation confirmation anchor.",
        "- D+1/D+3/D+5/D+10 returns use close prices; MFE/MAE use high/low versus entry open.",
        "- `model_signals_for_report` rows are ranking-evaluation samples, not trade-eligible operation rows.",
        "- `volume_breakout_operation_section` rows are evaluated separately by `confirmed_operation`, `confirmed_unranked_operation`, `pending_confirmation`, and `active_operation`.",
        "- Volume-v2 rows require exact historical lineage coverage with `formal_row_disposition=verified_clean` and `evidence_status=complete`; non-clean or uncovered rows remain in the event audit but are excluded from all performance summaries and promotion evidence.",
        "- The artifact is advisory-only and must not directly change daily production parameters.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_daily_published_snapshot_ranking_backtest(
    manifest_path: Path = MANIFEST_CSV,
    snapshot_root: Path = SNAPSHOT_DIR,
    price_dir: Path = STOCK_PRICE_HISTORY_DIR,
    lineage_audit_path: Path = VOLUME_V2_LINEAGE_AUDIT_CSV,
    generated_at: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    generated = generated_at or now_text()
    manifest = load_manifest(manifest_path=manifest_path, snapshot_root=snapshot_root)
    model_events = build_model_signal_events(
        manifest,
        price_dir=price_dir,
        lineage_audit_path=lineage_audit_path,
    )
    operation_events = build_volume_operation_events(
        manifest,
        price_dir=price_dir,
        lineage_audit_path=lineage_audit_path,
    )
    events = pd.concat([model_events, operation_events], ignore_index=True, sort=False)
    if events.empty:
        raise RuntimeError("no ranking or operation events were built from published snapshots")
    events["generated_at"] = generated
    summary = build_summary(events, generated_at=generated)
    if summary.empty:
        raise RuntimeError("no summary rows were built from published snapshot events")
    return summary, events


def main() -> int:
    try:
        generated = now_text()
        summary, events = build_daily_published_snapshot_ranking_backtest(generated_at=generated)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    write_csv(summary, OUT_CSV)
    write_csv(events, EVENTS_CSV)
    write_csv(summary, DOCS_CSV)
    write_markdown(summary, events, OUT_MD, generated)
    DOCS_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_MD.write_text(OUT_MD.read_text(encoding="utf-8"), encoding="utf-8")

    print("daily published snapshot ranking backtest built")
    print(f"summary={OUT_CSV.as_posix()} rows={len(summary)}")
    print(f"events={EVENTS_CSV.as_posix()} rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
