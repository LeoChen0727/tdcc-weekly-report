"""Frozen pullback replay supplement: one known share split, never formal returns."""
from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
import fnmatch
import hashlib
import io
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Iterator

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from model_research_artifact_guard import (  # noqa: E402
    _dirty_snapshot,
    changed_during_run,
    load_ownership_rules,
    load_protected_sentinels,
    validate_changed_paths,
)

ROOT = SCRIPT_DIR.parent
MODEL_ID = "pullback_short_reclaim"
OWNER_ID = "pullback_short_reclaim_share_unit_reconciliation"
VERSION = OWNER_ID + "_v1"
PRODUCER = "scripts/build_pullback_short_reclaim_share_unit_reconciliation.py"
CONFIG_REL = "config/pullback_short_reclaim_share_unit_reconciliation_v1.json"
SOURCE_COMMIT = "50baf29c849e5ca54a54e0f59800cef3fbe410c0"
PRICE_COMMIT = "12b817cbac0e198ac614a542e5cbf057959ed4a5"
PRICE_PATH = "data/stock_price_history/5904.csv"
PRICE_SHA256 = "0a2318bd5fc59c4f7fccebe36f54af1b9706977b022a42bc89a7856e67129b7f"
SOURCE_ARTIFACTS = {
    "events": {
        "path": "output/latest/research_backtest/pullback_short_reclaim_published_signal_replay_events_latest.csv",
        "raw_sha256": "f134c54fd2c854fe9397de525857ab58c5ca42867479f58acb5323e97838ed5b",
    },
    "summary": {
        "path": "output/latest/research_backtest/pullback_short_reclaim_published_signal_replay_summary_latest.csv",
        "raw_sha256": "d408734460e4760a024e165fd523cef6f770ef6ad9b56e5f43aa4db0cf82c742",
    },
    "anomalies": {
        "path": "output/latest/research_backtest/pullback_short_reclaim_published_signal_replay_anomaly_candidates_latest.csv",
        "raw_sha256": "7fd2e3e0ad6a00526f612a1df58de265834bf7c317fa2ba10af28f7a8c71a199",
    },
    "snapshot": {
        "path": "output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_20260713.csv",
        "raw_sha256": "bdc85cb76e4215785b3c7a72b7934b8655d5b824f1a8f2654f488891e851d564",
    },
}
ACTION_FACTS = {
    "stock_id": "5904", "effective_date": "20260810", "share_factor": 10,
    "suspension_start": "20260730", "suspension_end": "20260807",
    "official_url": "https://www.tpex.org.tw/storage/eb_data/11507/11500046541.html",
}
OFFICIAL_RECEIPT_SHA256 = "5a8f94d8d4707589b59920e3791bf303eab4a966f0bc47ae3f04a503097338ee"
CONFIG_LIMITATIONS = {
    "scope": "single_known_share_unit_price_supplement_not_corrected_primary",
    "first_publication_pit_verified": False, "full_corporate_action_coverage": False,
    "cash_flow_status": "not_modelled_not_total_return",
    "formal_model_use_allowed": False, "promotion_allowed": False,
    "old_research_preserved": True, "anomaly_disposition": "unresolved_anomaly_candidate",
    "horizon_basis": "original_available_stock_price_row_count_not_market_calendar",
}
OUTPUT_PREFIX = "output/research/pullback_short_reclaim/" + VERSION + "_"
OUTPUTS = {key: OUTPUT_PREFIX + filename for key, filename in (
    ("detail", "detail.csv"), ("summary", "summary.csv"), ("manifest", "manifest.json"),
)}
HORIZONS = (5, 10, 20)
SUPPLEMENT_STATUS = "partial_known_share_unit_price_proxy_not_corrected_primary"
UNCHANGED_STATUS = "no_known_split_applied_coverage_not_verified"
ADJUSTED_STATUS = "known_split_applied_partial_coverage"
LIMITATIONS = {
    "formal_use_allowed": False, "trade_eligible": False,
    "promotion_evidence_allowed": False, "first_publication_pit_proven": False,
    "total_return_complete": False, "numerical_disposition_changed": False,
    "cash_flow_status": "not_modelled_not_total_return",
    "result_status": SUPPLEMENT_STATUS,
    "holding_basis": "original_individual_price_row_count_unchanged",
    "other_corporate_action_coverage": "not_verified",
}


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(payload: Any) -> bytes:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _git(root: Path, *args: str) -> bytes:
    try:
        return subprocess.run(
            ["git", "--no-replace-objects", "-C", str(root), *args],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=60,
        ).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        raise RuntimeError(f"immutable pullback source unavailable: {args}") from exc


def read_git_blob(root: Path, commit: str, path: str, expected_sha256: str) -> bytes:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise RuntimeError("an exact full source commit is required")
    if (not path or path.startswith(("/", "-")) or "\\" in path
            or any(part in {"", ".", ".."} for part in path.split("/"))):
        raise RuntimeError("source path must be an exact repository-relative file")
    observed = _git(root, "rev-parse", "--verify", commit + "^{commit}").decode("ascii").strip()
    if observed != commit:
        raise RuntimeError("immutable source commit identity mismatch")
    tree = _git(root, "ls-tree", "-z", commit, "--", path).split(b"\0")
    entries = [entry for entry in tree if entry]
    if len(entries) != 1:
        raise RuntimeError(f"exact source blob missing: {path}")
    metadata, observed_path = entries[0].split(b"\t", 1)
    mode, kind, oid = metadata.decode("ascii").split()
    if mode != "100644" or kind != "blob" or observed_path.decode("utf-8") != path:
        raise RuntimeError(f"source must be an exact regular Git blob: {path}")
    payload = _git(root, "cat-file", "blob", oid)
    if sha256(payload) != expected_sha256:
        raise RuntimeError(f"immutable source raw SHA-256 mismatch: {path}")
    return payload


def validate_config(config: dict[str, Any]) -> None:
    if config.get("artifact_version") != VERSION or config.get("model_id") != MODEL_ID:
        raise RuntimeError("share-unit model/version contract mismatch")
    if config.get("source_commit") != SOURCE_COMMIT or config.get("source_artifacts") != SOURCE_ARTIFACTS:
        raise RuntimeError("frozen replay source pins must not change")
    if config.get("price_source") != {"commit": PRICE_COMMIT, "path": PRICE_PATH, "raw_sha256": PRICE_SHA256}:
        raise RuntimeError("original 5904 price source pin must not change")
    action = config.get("action", {})
    if any(action.get(key) != value for key, value in ACTION_FACTS.items()):
        raise RuntimeError("only the exact 5904 share-unit action is allowed")
    if action.get("receipt_sha256") != OFFICIAL_RECEIPT_SHA256:
        raise RuntimeError("official action receipt SHA-256 must match the pinned receipt")
    try:
        receipt = base64.b64decode(action.get("receipt_body_base64", ""), validate=True)
    except (ValueError, TypeError) as exc:
        raise RuntimeError("official action receipt must contain valid base64 bytes") from exc
    if not receipt or sha256(receipt) != action["receipt_sha256"]:
        raise RuntimeError("official action receipt bytes/SHA-256 mismatch")
    if not isinstance(action.get("retrieved_at"), str) or not action["retrieved_at"].strip():
        raise RuntimeError("official action receipt retrieval time is required")
    limitations = config.get("limitations", {})
    if not isinstance(limitations, dict) or set(limitations) != set(CONFIG_LIMITATIONS) | {"user_authorization_ref"}:
        raise RuntimeError("exact research-only limitations are required")
    for key, expected in CONFIG_LIMITATIONS.items():
        value = limitations.get(key)
        if type(value) is not type(expected) or value != expected:
            raise RuntimeError(f"research-only limitation must not change: {key}")
    if not isinstance(limitations["user_authorization_ref"], str) or not limitations["user_authorization_ref"].strip():
        raise RuntimeError("research supplement user authorization reference is required")


def load_sources(repository_root: Path, config: dict[str, Any]) -> dict[str, bytes]:
    validate_config(config)
    payloads = {
        key: read_git_blob(repository_root, SOURCE_COMMIT, spec["path"], spec["raw_sha256"])
        for key, spec in SOURCE_ARTIFACTS.items()
    }
    payloads["price"] = read_git_blob(repository_root, PRICE_COMMIT, PRICE_PATH, PRICE_SHA256)
    return payloads


def _csv(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False)


def csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def _number(value: Any) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"invalid numeric research value: {value!r}") from exc
    if not math.isfinite(result):
        raise RuntimeError("non-finite research value")
    return result


def _formatted(value: float) -> str:
    return f"{value:.6f}".rstrip("0").rstrip(".") or "0"


def _row_sha(row: pd.Series) -> str:
    return sha256(canonical_json({str(key): str(value).strip() for key, value in row.items()}))


def _check_price_lineage(events: pd.DataFrame, price: pd.DataFrame) -> None:
    if not {"date", "open", "close"}.issubset(price.columns) or price["date"].duplicated().any():
        raise RuntimeError("original 5904 price schema/date identity mismatch")
    if price["date"].between("20260730", "20260807").any():
        raise RuntimeError("original 5904 prices unexpectedly contain official suspension dates")
    if "20260810" not in set(price["date"]):
        raise RuntimeError("original 5904 price source is missing resumption date")
    ordered = price.sort_values("date")
    for _, event in events[events["stock_id"].eq("5904")].iterrows():
        future = ordered[ordered["date"].gt(event["signal_date"])].reset_index(drop=True)
        if not event["entry_date"]:
            if not future.empty:
                raise RuntimeError("original 5904 entry date omitted existing forward price")
            continue
        if future.empty or future.iloc[0]["date"] != event["entry_date"]:
            raise RuntimeError("original 5904 entry row sequence mismatch")
        entry = future.iloc[0]
        if (abs(_number(entry["open"]) - _number(event["entry_open_price"])) > 1e-6
                or _row_sha(entry) != event["entry_price_row_sha256"]):
            raise RuntimeError("original 5904 entry price/row hash mismatch")
        for horizon in HORIZONS:
            prefix = f"d{horizon}"
            if event[prefix + "_maturity_status"] != "mature":
                continue
            if len(future) < horizon:
                raise RuntimeError("original 5904 mature horizon exceeds source rows")
            exit_row = future.iloc[horizon - 1]
            if (exit_row["date"] != event[prefix + "_exit_date"]
                    or _row_sha(exit_row) != event[prefix + "_exit_price_row_sha256"]
                    or abs(_number(exit_row["close"]) - _number(event[prefix + "_exit_close_price"])) > 1e-6):
                raise RuntimeError("original 5904 exit date/price/row hash mismatch")


def build_reconciliation(
    events: pd.DataFrame, summary: pd.DataFrame, anomalies: pd.DataFrame,
    price: pd.DataFrame, config: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    validate_config(config)
    for label, frame in (("events", events), ("summary", summary), ("anomalies", anomalies)):
        if not frame.columns.is_unique:
            raise RuntimeError(f"duplicate source columns: {label}")
        if not frame.empty and set(frame["model_id"]) != {MODEL_ID}:
            raise RuntimeError(f"another model in frozen {label}")
        for field in ("formal_use_allowed", "promotion_evidence_allowed"):
            if field not in frame or (not frame.empty and set(frame[field]) != {"False"}):
                raise RuntimeError(f"{label}: {field} must remain False")
        if "operation_contract_status" not in frame or (not frame.empty and set(frame["operation_contract_status"]) != {"decision_required"}):
            raise RuntimeError(f"{label}: operation contract must remain decision_required")
        if label != "anomalies" and ("trade_eligible" not in frame or set(frame["trade_eligible"]) != {"False"}):
            raise RuntimeError(f"{label}: trade_eligible must remain False")
    if events.empty or set(events["primary_metric_included"]) - {"True", "False"}:
        raise RuntimeError("invalid frozen primary population")
    if set(summary["horizon"]) != {"D+5", "D+10", "D+20"} or len(summary) != 3:
        raise RuntimeError("frozen summary must have exactly three horizons")
    if "share_unit_reconciliation_version" in events or "partial_known_share_unit_result_status" in summary:
        raise RuntimeError("already reconciled input cannot be adjusted twice")
    _check_price_lineage(events, price)
    detail = events.copy(deep=True)
    adjusted = pd.Series(False, index=detail.index)
    for horizon in HORIZONS:
        prefix = f"d{horizon}"
        factors: list[str] = []
        returns: list[str] = []
        for index, event in events.iterrows():
            mature = event[prefix + "_maturity_status"] == "mature"
            crossing = (mature and event["stock_id"] == "5904"
                        and event["entry_date"] < "20260810" <= event[prefix + "_exit_date"])
            factors.append("10" if crossing else "1")
            original = event[prefix + "_return_pct"]
            if crossing:
                opening = _number(event["entry_open_price"])
                closing = _number(event[prefix + "_exit_close_price"])
                if opening <= 0 or closing <= 0:
                    raise RuntimeError("known-action price endpoints must be positive")
                returns.append(_formatted((closing * 10 / opening - 1) * 100))
                adjusted.at[index] = True
            else:
                returns.append(original)
        detail[prefix + "_share_factor"] = factors
        detail[prefix + "_share_unit_return_pct"] = returns
    detail["share_unit_reconciliation_version"] = VERSION
    detail["unit_adjustment_status"] = [ADJUSTED_STATUS if value else UNCHANGED_STATUS for value in adjusted]
    detail["cash_flow_status"] = LIMITATIONS["cash_flow_status"]
    detail["share_unit_result_status"] = SUPPLEMENT_STATUS
    detail["first_publication_pit_proven"] = "False"
    detail["total_return_complete"] = "False"
    detail["numerical_disposition_changed"] = "False"
    detail["known_share_action_evidence_url"] = [ACTION_FACTS["official_url"] if value else "" for value in adjusted]
    result = summary.copy(deep=True)
    for index, source_row in summary.iterrows():
        horizon = int(source_row["horizon"].split("+")[1])
        prefix = f"d{horizon}"
        mature = detail[detail["primary_metric_included"].eq("True") & detail[prefix + "_maturity_status"].eq("mature")]
        values = [_number(value) for value in mature[prefix + "_share_unit_return_pct"]]
        series = pd.Series(values, dtype=float)
        count = len(values)
        wins = sum(value > 0 for value in values)
        metrics = {
            "mature_count": str(count), "affected_count": str(int(mature[prefix + "_share_factor"].eq("10").sum())),
            "win_count": str(wins), "neutral_count": str(sum(value == 0 for value in values)),
            "failure_count": str(sum(value < 0 for value in values)),
            "win_rate_pct": _formatted(wins / count * 100) if count else "",
            "average_return_pct": _formatted(float(series.mean())) if count else "",
            "median_return_pct": _formatted(float(series.median())) if count else "",
            "result_status": SUPPLEMENT_STATUS,
        }
        for field, value in metrics.items():
            result.at[index, "partial_known_share_unit_" + field] = value
    result["cash_flow_status"] = LIMITATIONS["cash_flow_status"]
    result["first_publication_pit_proven"] = "False"
    result["total_return_complete"] = "False"
    result["numerical_disposition_changed"] = "False"
    return detail, result


def build_bundle(repository_root: Path, config_path: Path | None = None) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    root = Path(repository_root)
    config = json.loads((config_path or root / CONFIG_REL).read_text(encoding="utf-8-sig"))
    sources = load_sources(root, config)
    frames = {key: _csv(payload) for key, payload in sources.items()}
    events = frames["events"]
    canonical = events[events["primary_metric_included"].eq("True")]
    if len(events) != 3020 or len(canonical) != 2992 or canonical["signal_event_id"].nunique() != 2992:
        raise RuntimeError("frozen 3020-row/2992-event population mismatch")
    detail, summary = build_reconciliation(events, frames["summary"], frames["anomalies"], frames["price"], config)
    manifest = {
        "artifact_version": VERSION, "model_id": MODEL_ID, "owner_id": OWNER_ID,
        "source_commit": SOURCE_COMMIT, "source_artifacts": SOURCE_ARTIFACTS,
        "price_source": config["price_source"], "action": config["action"],
        "config_canonical_sha256": sha256(canonical_json(config)),
        "source_row_count": len(events), "unique_signal_event_count": len(canonical),
        "source_anomaly_count": len(frames["anomalies"]),
        "old_columns_and_row_order_unchanged": True,
        "original_primary_metrics_and_unresolved_dispositions_retained": True,
        "output_sha256": {OUTPUTS["detail"]: sha256(csv_bytes(detail)), OUTPUTS["summary"]: sha256(csv_bytes(summary))},
        **LIMITATIONS,
    }
    return detail, summary, manifest


def protected_snapshot(root: Path) -> dict[str, Any]:
    sentinels = load_protected_sentinels(root / "config/model_research_protected_sentinels.csv")
    patterns = [item.artifact_glob for item in sentinels] + [spec["path"] for spec in SOURCE_ARTIFACTS.values()]
    matches = lambda path: any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)
    maps = []
    for command in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z")):
        mapping = {}
        for entry in _git(root, *command).decode("utf-8").split("\0"):
            if entry:
                metadata, path = entry.split("\t", 1)
                if matches(path):
                    mapping[path] = metadata
        maps.append(mapping)
    paths = set(maps[0]) | set(maps[1])
    for pattern in patterns:
        paths.update(path.relative_to(root).as_posix() for path in root.glob(pattern) if path.is_file())
    for sentinel in sentinels:
        if sentinel.required and not any(fnmatch.fnmatchcase(path, sentinel.artifact_glob) for path in paths):
            raise RuntimeError("missing protected sentinel: " + sentinel.sentinel_id)
    return {"tree": maps[0], "index": maps[1], "physical": {path: sha256((root / path).read_bytes()) for path in paths if (root / path).is_file()}}


@contextmanager
def model_owned_artifact_guard(root: Path) -> Iterator[None]:
    rules = load_ownership_rules(root / "config/model_research_artifact_ownership.csv")
    errors = validate_changed_paths(OWNER_ID, PRODUCER, list(OUTPUTS.values()), rules)
    if errors:
        raise RuntimeError("unregistered share-unit output: " + "; ".join(errors))
    before, protected = _dirty_snapshot(root), protected_snapshot(root)
    index_before = _git(root, "ls-files", "--stage", "-z")
    head_before = _git(root, "rev-parse", "HEAD")
    try:
        yield
    finally:
        if (set(changed_during_run(root, before)) - set(OUTPUTS.values())
                or protected_snapshot(root) != protected
                or _git(root, "ls-files", "--stage", "-z") != index_before
                or _git(root, "rev-parse", "HEAD") != head_before):
            raise RuntimeError("share-unit producer changed protected/out-of-scope files")


def write_bundle(bundle: tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]], repository_root: Path = ROOT) -> None:
    root = Path(repository_root).resolve()
    detail, summary, manifest = bundle
    payloads = {OUTPUTS["detail"]: csv_bytes(detail), OUTPUTS["summary"]: csv_bytes(summary)}
    if manifest.get("output_sha256") != {path: sha256(payload) for path, payload in payloads.items()}:
        raise RuntimeError("bundle output hash mismatch")
    payloads[OUTPUTS["manifest"]] = canonical_json(manifest) + b"\n"
    with model_owned_artifact_guard(root):
        for relative, payload in payloads.items():
            target = root / relative
            if not target.resolve().is_relative_to(root) or any(parent.is_symlink() for parent in (target, *target.parents) if parent != root):
                raise RuntimeError("share-unit output path must stay inside repository without symlinks")
            if target.exists() and target.read_bytes() != payload:
                raise RuntimeError("immutable share-unit output already differs: " + relative)
        for relative, payload in payloads.items():
            target = root / relative
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open("xb") as handle:
                    handle.write(payload)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    write_bundle(build_bundle(args.repo_root), args.repo_root)
    print("回檔後短線轉強模型：已產生凍結來源股份單位補充；不是正式勝率或完整總報酬。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
