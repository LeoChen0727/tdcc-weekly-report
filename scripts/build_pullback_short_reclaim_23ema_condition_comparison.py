"""Frozen signal feature comparison; never a formal strategy or new price replay."""
from __future__ import annotations

import argparse
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
    _dirty_snapshot, changed_during_run, load_ownership_rules,
    load_protected_sentinels, validate_changed_paths,
)

ROOT = SCRIPT_DIR.parent
MODEL_ID = "pullback_short_reclaim"
OWNER_ID = "pullback_short_reclaim_23ema_condition_comparison"
VERSION = OWNER_ID + "_v1"
PRODUCER = "scripts/build_pullback_short_reclaim_23ema_condition_comparison.py"
SOURCE_COMMIT = "03387e6a610491078538c633d8ec5245c027db50"
SNAPSHOT_COMMIT = "50baf29c849e5ca54a54e0f59800cef3fbe410c0"
SOURCE_PREFIX = "output/research/pullback_short_reclaim/pullback_short_reclaim_share_unit_reconciliation_v1_"
SOURCE_ARTIFACTS = {
    "detail": {"path": SOURCE_PREFIX + "detail.csv", "raw_sha256": "5ac2768ef49a933e166ec1756d55a8b5ad6a468bbdf74a8fa570d1ed8e4f6dac"},
    "summary": {"path": SOURCE_PREFIX + "summary.csv", "raw_sha256": "436206ffa3c387904fc8c8d29d5bc0139238d1f6d6a5c874da07b7a2a4f1dd6f"},
}
OUTPUT_PREFIX = "output/research/pullback_short_reclaim/" + VERSION + "_"
OUTPUTS = {key: OUTPUT_PREFIX + key + extension for key, extension in (
    ("detail", ".csv"), ("summary", ".csv"), ("features", ".csv"), ("manifest", ".json"),
)}
FEATURE_FIELDS = (
    "return_20d", "price_pullback_signal_date", "price_pullback_tdcc_history_available",
    "price_pullback_high_thresholds_up", "price_pullback_obv_above_ma20",
    "price_pullback_rsi14", "price_pullback_macd_hist",
)
STATES = ("pass", "recorded_false", "unknown")
FEATURES = ("ret20_5_25", "tdcc_positive", "obv_positive", "technical_quality")
HORIZONS = (5, 10, 20)
METRIC_BASES = ("raw_primary", "raw_original_candidate_exclusion_sensitivity", "partial_share_unit_supplement")
GROUPS = (
    "baseline_all", "baseline_context_schema", "ret20_5_25_all", "ret20_5_25_context_schema",
    "baseline_tdcc_available", "tdcc_positive", "tdcc_recorded_false", "tdcc_unknown",
    "obv_positive", "obv_recorded_false", "obv_unknown", "technical_quality", "technical_recorded_false", "technical_unknown",
)
LIMITATIONS = {
    "formal_use_allowed": False, "trade_eligible": False, "promotion_evidence_allowed": False,
    "first_publication_pit_proven": False, "total_return_complete": False,
    "numerical_disposition_changed": False, "non_overlapping_trades_proven": False,
    "result_status": "frozen_published_signal_feature_comparison_research_only",
    "holding_basis": "original_individual_price_row_count_unchanged",
    "return_cost_basis": "original_before_costs_slippage_and_tax",
    "partial_share_unit_status": "partial_known_share_unit_price_proxy_not_corrected_primary",
    "false_flag_status": "recorded_false_does_not_prove_complete_feature_inputs",
    "cash_flow_status": "not_modelled_not_total_return",
}


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def _text(value: Any) -> str:
    value = str(value).replace("\ufeff", "").strip()
    return "" if value.lower() in {"nan", "none", "nat", "<na>"} else value


def _number(value: Any) -> float | None:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def _formatted(value: float | None) -> str:
    return "" if value is None else format(round(value, 6), ".6f")


def _git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "--no-replace-objects", "-C", str(root), *args],
                          check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60).stdout


def read_git_blob(root: Path, commit: str, path: str, expected_sha256: str | None = None) -> bytes:
    if (not re.fullmatch(r"[0-9a-f]{40}", commit) or not path or path.startswith(("/", "-"))
            or "\\" in path or any(x in {"", ".", ".."} for x in path.split("/"))):
        raise RuntimeError("exact source commit and safe regular-blob path required")
    if _git(root, "rev-parse", "--verify", commit + "^{commit}").decode().strip() != commit:
        raise RuntimeError("source commit identity mismatch")
    entries = [x for x in _git(root, "ls-tree", "-z", commit, "--", path).split(b"\0") if x]
    if len(entries) != 1:
        raise RuntimeError("exact source blob missing: " + path)
    metadata, actual_path = entries[0].split(b"\t", 1)
    mode, kind, oid = metadata.decode().split()
    if mode != "100644" or kind != "blob" or actual_path.decode() != path:
        raise RuntimeError("source must be exact regular Git blob")
    payload = _git(root, "cat-file", "blob", oid)
    if expected_sha256 is not None and sha256(payload) != expected_sha256:
        raise RuntimeError("immutable source SHA mismatch: " + path)
    return payload


def enrich_events(events: pd.DataFrame, snapshots: dict[str, bytes]) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    """Join exact published rows, preserving every original cell and row order."""
    detail = events.copy(deep=True)
    if events.duplicated(["snapshot_path", "snapshot_csv_row_number"]).any():
        raise RuntimeError("duplicate snapshot-row identity")
    receipts = []
    for field in FEATURE_FIELDS:
        detail["feature_" + field] = ""
    detail["context_schema_available"] = "False"
    for name in FEATURES:
        detail[name + "_state"] = "unknown"
    for path, indices in events.groupby("snapshot_path", sort=True).groups.items():
        payload = snapshots[path]
        lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        hashes = {sha256(x) for x in (payload, lf, lf.replace(b"\n", b"\r\n"))}
        snapshot = pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False)
        context_schema = all(f in snapshot.columns for f in FEATURE_FIELDS)
        expected_hashes = set()
        for index in indices:
            event = events.loc[index]
            expected_hashes.add(event["snapshot_sha256"])
            if event["snapshot_sha256"] not in hashes:
                raise RuntimeError("snapshot transport SHA mismatch")
            if len(snapshot) != int(event["snapshot_total_row_count"]) or len(snapshot.columns) != int(event["snapshot_total_column_count"]):
                raise RuntimeError("snapshot dimensions mismatch")
            position = int(event["snapshot_csv_row_number"]) - 2
            if position < 0 or position >= len(snapshot):
                raise RuntimeError("snapshot row out of range")
            row = snapshot.iloc[position]
            normalized = {str(k): _text(v) for k, v in row.items()}
            if sha256(canonical_json(normalized)) != event["source_row_sha256"]:
                raise RuntimeError("source row SHA mismatch")
            for field in ("model_id", "stock_id", "signal_date", "report_line", "report_bucket"):
                if _text(row[field]) != _text(event[field]):
                    raise RuntimeError("source identity mismatch: " + field)
            if _text(row.get("source_row_index", "")) != event["published_source_row_index"]:
                raise RuntimeError("source row index mismatch")
            if row["model_id"] != MODEL_ID:
                raise RuntimeError("another model cannot enter this comparison")
            for field in FEATURE_FIELDS:
                detail.at[index, "feature_" + field] = _text(row.get(field, ""))
            ret20 = _number(row.get("return_20d"))
            if ret20 is not None:
                detail.at[index, "ret20_5_25_state"] = "pass" if 5 <= ret20 <= 25 else "recorded_false"
            if not context_schema:
                continue
            if row["price_pullback_signal_date"] != event["signal_date"]:
                raise RuntimeError("feature signal date mismatch")
            detail.at[index, "context_schema_available"] = "True"
            for field in ("price_pullback_tdcc_history_available", "price_pullback_high_thresholds_up", "price_pullback_obv_above_ma20"):
                if row[field] not in {"True", "False", ""}:
                    raise RuntimeError("unknown feature boolean encoding")
            if row["price_pullback_tdcc_history_available"] == "True" and row["price_pullback_high_thresholds_up"]:
                detail.at[index, "tdcc_positive_state"] = "pass" if row["price_pullback_high_thresholds_up"] == "True" else "recorded_false"
            if row["price_pullback_obv_above_ma20"]:
                detail.at[index, "obv_positive_state"] = "pass" if row["price_pullback_obv_above_ma20"] == "True" else "recorded_false"
            rsi, macd = _number(row["price_pullback_rsi14"]), _number(row["price_pullback_macd_hist"])
            if rsi is not None and macd is not None:
                detail.at[index, "technical_quality_state"] = "pass" if rsi >= 60 and macd > 0 else "recorded_false"
        receipts.append({"path": path, "raw_sha256": sha256(payload), "recorded_transport_sha256": sorted(expected_hashes),
                         "row_count": len(snapshot), "column_count": len(snapshot.columns), "context_schema_available": context_schema})
    detail["comparison_version"] = VERSION
    for horizon in HORIZONS:
        prefix = f"d{horizon}"
        for index, row in detail.iterrows():
            value = _number(row[prefix + "_return_pct"])
            original = row[prefix + "_anomaly_candidate"] == "True"
            magnitude = value is not None and abs(value) >= 50
            candidate = original or magnitude
            detail.at[index, prefix + "_comparison_anomaly_candidate"] = str(candidate)
            detail.at[index, prefix + "_comparison_anomaly_disposition"] = "unresolved_anomaly_candidate" if candidate else "not_flagged_by_this_review"
            detail.at[index, prefix + "_comparison_anomaly_reason"] = "source_candidate_retained" if original else "absolute_return_ge50_investigation_only" if magnitude else ""
    return detail, receipts


def select_group(frame: pd.DataFrame, group: str) -> pd.DataFrame:
    schema = frame["context_schema_available"].eq("True")
    if group == "baseline_all":
        return frame
    if group == "baseline_context_schema":
        return frame[schema]
    if group.startswith("ret20_5_25_"):
        selected = frame["ret20_5_25_state"].eq("pass")
        return frame[selected & (schema if group.endswith("context_schema") else True)]
    if group == "baseline_tdcc_available":
        return frame[schema & frame["tdcc_positive_state"].ne("unknown")]
    states = {
        "tdcc_positive": ("tdcc_positive", "pass"), "tdcc_recorded_false": ("tdcc_positive", "recorded_false"),
        "tdcc_unknown": ("tdcc_positive", "unknown"), "obv_positive": ("obv_positive", "pass"),
        "obv_recorded_false": ("obv_positive", "recorded_false"), "obv_unknown": ("obv_positive", "unknown"),
        "technical_quality": ("technical_quality", "pass"), "technical_recorded_false": ("technical_quality", "recorded_false"),
        "technical_unknown": ("technical_quality", "unknown"),
    }
    feature, state = states[group]
    return frame[schema & frame[feature + "_state"].eq(state)]


def describe_returns(frame: pd.DataFrame, horizon: int, basis: str) -> dict[str, Any]:
    prefix = f"d{horizon}"
    mature = frame[frame[prefix + "_maturity_status"].eq("mature")]
    if basis == "raw_original_candidate_exclusion_sensitivity":
        mature = mature[~mature[prefix + "_anomaly_candidate"].eq("True")]
    field = prefix + ("_share_unit_return_pct" if basis == "partial_share_unit_supplement" else "_return_pct")
    values = pd.to_numeric(mature[field], errors="raise").astype(float)
    if not all(math.isfinite(x) for x in values):
        raise RuntimeError("nonfinite mature return")
    count = len(values)
    counts = {"win": int((values > 0).sum()), "neutral": int((values == 0).sum()), "failure": int((values < 0).sum()),
              "high_return_ge10": int((values >= 10).sum()), "loss": int((values < 0).sum()), "tail_loss_le_minus10": int((values <= -10).sum())}
    result = {"signal_count": len(frame), "mature_count": count,
              "immature_count": int(frame[prefix + "_maturity_status"].ne("mature").sum()),
              "excluded_candidate_count": int((frame[prefix + "_maturity_status"].eq("mature") & frame[prefix + "_anomaly_candidate"].eq("True")).sum()) if basis == "raw_original_candidate_exclusion_sensitivity" else 0,
              "unresolved_retained_count": int(mature[prefix + "_anomaly_candidate"].eq("True").sum()),
              "retained_review_candidate_count": int(mature[prefix + "_comparison_anomaly_candidate"].eq("True").sum()),
              "unique_stock_count": mature["stock_id"].nunique(), "signal_date_count": mature["signal_date"].nunique()}
    for key, value in counts.items():
        result[key + "_count"] = value
        result[key + "_rate_pct"] = _formatted(value / count * 100) if count else ""
    for key, value in (("average", values.mean()), ("median", values.median()), ("minimum", values.min()), ("maximum", values.max())):
        result[key + "_return_pct"] = _formatted(float(value)) if count else ""
    return result


def build_tables(detail: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    canonical = detail[detail["primary_metric_included"].eq("True")]
    rows, feature_rows = [], []
    periods = ["all", *sorted(canonical["signal_date"].str[:6].unique())]
    for period in periods:
        population = canonical if period == "all" else canonical[canonical["signal_date"].str.startswith(period)]
        for horizon in HORIZONS:
            for basis in METRIC_BASES:
                for group in GROUPS:
                    selected = select_group(population, group)
                    rows.append({"artifact_version": VERSION, "model_id": MODEL_ID, "period": period, "horizon": horizon,
                                 "metric_basis": basis, "group_id": group, **describe_returns(selected, horizon, basis),
                                 "formal_use_allowed": "False", "promotion_evidence_allowed": "False"})
                field = f"d{horizon}" + ("_share_unit_return_pct" if basis == "partial_share_unit_supplement" else "_return_pct")
                for population_basis, baseline_group in (("all", "baseline_all"), ("context_schema", "baseline_context_schema"), ("tdcc_available", "baseline_tdcc_available")):
                    feature_population = select_group(population, baseline_group)
                    mature = feature_population[feature_population[f"d{horizon}_maturity_status"].eq("mature")]
                    if basis == "raw_original_candidate_exclusion_sensitivity":
                        mature = mature[~mature[f"d{horizon}_anomaly_candidate"].eq("True")]
                    values = pd.to_numeric(mature[field], errors="raise").astype(float)
                    for band, mask in (("high_ge10", values >= 10), ("middle_0_to_lt10", (values >= 0) & (values < 10)), ("loss_lt0", values < 0)):
                        band_rows = mature[mask]
                        for feature in FEATURES:
                            for state in STATES:
                                count = int(band_rows[feature + "_state"].eq(state).sum())
                                feature_rows.append({"artifact_version": VERSION, "model_id": MODEL_ID, "period": period, "horizon": horizon,
                                                     "population_basis": population_basis, "metric_basis": basis, "outcome_band": band, "feature": feature, "feature_state": state,
                                                     "band_count": len(band_rows), "state_count": count,
                                                     "state_rate_pct": _formatted(count / len(band_rows) * 100) if len(band_rows) else "",
                                                     "formal_use_allowed": "False", "promotion_evidence_allowed": "False"})
    return pd.DataFrame(rows), pd.DataFrame(feature_rows)


def build_bundle(repository_root: Path = ROOT) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    root = Path(repository_root)
    inputs = {key: read_git_blob(root, SOURCE_COMMIT, spec["path"], spec["raw_sha256"]) for key, spec in SOURCE_ARTIFACTS.items()}
    events = pd.read_csv(io.BytesIO(inputs["detail"]), dtype=str, keep_default_na=False)
    canonical = events[events["primary_metric_included"].eq("True")]
    if len(events) != 3020 or len(canonical) != 2992 or canonical["signal_event_id"].nunique() != 2992:
        raise RuntimeError("frozen event population mismatch")
    snapshots = {path: read_git_blob(root, SNAPSHOT_COMMIT, path) for path in sorted(events["snapshot_path"].unique())}
    detail, receipts = enrich_events(events, snapshots)
    summary, features = build_tables(detail)
    original_summary = pd.read_csv(io.BytesIO(inputs["summary"]), dtype=str, keep_default_na=False)
    for _, original in original_summary.iterrows():
        horizon = int(original["horizon"].split("+")[1])
        observed = summary[(summary["period"] == "all") & (summary["horizon"] == horizon)
                           & (summary["metric_basis"] == "raw_primary") & (summary["group_id"] == "baseline_all")]
        if len(observed) != 1:
            raise RuntimeError("exact baseline summary row missing")
        result = observed.iloc[0]
        for field in ("mature_count", "win_count", "neutral_count", "failure_count"):
            if int(original[field]) != int(result[field]):
                raise RuntimeError("original baseline count drift: " + field)
        for field in ("average_return_pct", "median_return_pct", "win_rate_pct"):
            if abs(float(original[field]) - float(result[field])) > 0.0000011:
                raise RuntimeError("original baseline metric drift: " + field)
    coverage = {f: detail.loc[detail["primary_metric_included"].eq("True"), f + "_state"].value_counts().sort_index().to_dict() for f in FEATURES}
    manifest = {"artifact_version": VERSION, "model_id": MODEL_ID, "owner_id": OWNER_ID,
                "source_commit": SOURCE_COMMIT, "source_artifacts": SOURCE_ARTIFACTS, "snapshot_commit": SNAPSHOT_COMMIT,
                "snapshots": receipts, "source_row_count": len(detail), "unique_signal_event_count": len(canonical),
                "context_schema_primary_count": int((detail["primary_metric_included"].eq("True") & detail["context_schema_available"].eq("True")).sum()),
                "feature_state_coverage": coverage, "original_columns": list(events.columns),
                "old_cells_and_order_unchanged": True, "groups": list(GROUPS), "metric_bases": list(METRIC_BASES),
                "descriptive_return_bands": {"high_ge10": ">=10%", "middle_0_to_lt10": "0%<=return<10%", "loss_lt0": "<0%", "tail_loss": "<=-10%"},
                "band_threshold_use": "descriptive_only_not_model_gate_or_anomaly_disposition",
                "period_analysis_status": "same_sample_month_diagnostics_not_independent_oos",
                "review_anomaly_trigger": "source_candidate_or_absolute_raw_return_ge50_investigation_only",
                "sensitivity_scope": "excludes_original_source_candidates_only_new_review_candidates_retained",
                "feature_population_bases": ["all", "context_schema", "tdcc_available"],
                "user_authorization_ref": "user_20261010_pullback_short_reclaim_23ema_condition_comparison",
                "output_sha256": {OUTPUTS[k]: sha256(csv_bytes(v)) for k, v in (("detail", detail), ("summary", summary), ("features", features))},
                **LIMITATIONS}
    return detail, summary, features, manifest


def protected_snapshot(root: Path) -> dict[str, Any]:
    sentinels = load_protected_sentinels(root / "config/model_research_protected_sentinels.csv")
    patterns = [s.artifact_glob for s in sentinels] + [v["path"] for v in SOURCE_ARTIFACTS.values()] + ["output/history/daily_model_snapshots/*"]
    def matches(path: str) -> bool:
        return any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)
    maps = []
    for command in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z")):
        mapping = {}
        for entry in _git(root, *command).decode().split("\0"):
            if entry:
                metadata, path = entry.split("\t", 1)
                if matches(path):
                    mapping[path] = metadata
        maps.append(mapping)
    paths = set(maps[0]) | set(maps[1])
    for pattern in patterns:
        paths.update(p.relative_to(root).as_posix() for p in root.glob(pattern) if p.is_file())
    for sentinel in sentinels:
        if sentinel.required and not any(fnmatch.fnmatchcase(path, sentinel.artifact_glob) for path in paths):
            raise RuntimeError("missing protected sentinel: " + sentinel.sentinel_id)
    return {"tree": maps[0], "index": maps[1], "physical": {p: sha256((root / p).read_bytes()) for p in paths if (root / p).is_file()}}


@contextmanager
def model_owned_artifact_guard(root: Path) -> Iterator[None]:
    rules = load_ownership_rules(root / "config/model_research_artifact_ownership.csv")
    errors = validate_changed_paths(OWNER_ID, PRODUCER, list(OUTPUTS.values()), rules)
    if errors:
        raise RuntimeError("unregistered condition comparison outputs: " + "; ".join(errors))
    before, protected = _dirty_snapshot(root), protected_snapshot(root)
    index_before, head_before = _git(root, "ls-files", "--stage", "-z"), _git(root, "rev-parse", "HEAD")
    try:
        yield
    finally:
        if (set(changed_during_run(root, before)) - set(OUTPUTS.values()) or protected_snapshot(root) != protected
                or _git(root, "ls-files", "--stage", "-z") != index_before or _git(root, "rev-parse", "HEAD") != head_before):
            raise RuntimeError("condition comparison changed protected/out-of-scope paths")


def write_bundle(bundle: tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, Any]], repository_root: Path = ROOT) -> None:
    root = Path(repository_root).resolve()
    detail, summary, features, manifest = bundle
    payloads = {OUTPUTS[k]: csv_bytes(v) for k, v in (("detail", detail), ("summary", summary), ("features", features))}
    if manifest.get("output_sha256") != {p: sha256(v) for p, v in payloads.items()}:
        raise RuntimeError("output hash mismatch")
    payloads[OUTPUTS["manifest"]] = canonical_json(manifest) + b"\n"
    with model_owned_artifact_guard(root):
        for relative, payload in payloads.items():
            target = root / relative
            if not target.resolve().is_relative_to(root) or any(p.is_symlink() for p in (target, *target.parents) if p != root):
                raise RuntimeError("unsafe output path")
            if target.exists() and target.read_bytes() != payload:
                raise RuntimeError("immutable comparison output already differs")
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
    print("回檔後短線轉強：固定訊號條件比較已產出；不是正式勝率或模型升級。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
