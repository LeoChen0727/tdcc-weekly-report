"""Independent frozen-source verification of the reclaim feature comparison."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path
import re
import statistics
import subprocess
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "pullback_short_reclaim"
OWNER_ID = "pullback_short_reclaim_23ema_condition_comparison"
VERSION = OWNER_ID + "_v1"
SOURCE_COMMIT = "03387e6a610491078538c633d8ec5245c027db50"
SNAPSHOT_COMMIT = "50baf29c849e5ca54a54e0f59800cef3fbe410c0"
SOURCE_PREFIX = "output/research/pullback_short_reclaim/pullback_short_reclaim_share_unit_reconciliation_v1_"
SOURCE_ARTIFACTS = {
    "detail": {"path": SOURCE_PREFIX + "detail.csv", "raw_sha256": "5ac2768ef49a933e166ec1756d55a8b5ad6a468bbdf74a8fa570d1ed8e4f6dac"},
    "summary": {"path": SOURCE_PREFIX + "summary.csv", "raw_sha256": "436206ffa3c387904fc8c8d29d5bc0139238d1f6d6a5c874da07b7a2a4f1dd6f"},
}
PREFIX = "output/research/pullback_short_reclaim/" + VERSION + "_"
OUTPUTS = {key: PREFIX + key + suffix for key, suffix in (
    ("detail", ".csv"), ("summary", ".csv"), ("features", ".csv"), ("manifest", ".json"),
)}
FEATURE_FIELDS = (
    "return_20d", "price_pullback_signal_date", "price_pullback_tdcc_history_available",
    "price_pullback_high_thresholds_up", "price_pullback_obv_above_ma20",
    "price_pullback_rsi14", "price_pullback_macd_hist",
)
FEATURES = ("ret20_5_25", "tdcc_positive", "obv_positive", "technical_quality")
STATES = ("pass", "recorded_false", "unknown")
HORIZONS = (5, 10, 20)
BASES = ("raw_primary", "raw_original_candidate_exclusion_sensitivity", "partial_share_unit_supplement")
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
DETAIL_EXTRA = tuple("feature_" + f for f in FEATURE_FIELDS) + ("context_schema_available",) + tuple(
    f + "_state" for f in FEATURES
) + ("comparison_version",) + tuple(
    f"d{h}_comparison_anomaly_{suffix}" for h in HORIZONS for suffix in ("candidate", "disposition", "reason")
)


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _csv(payload: bytes) -> pd.DataFrame:
    reader = csv.reader(io.StringIO(payload.decode("utf-8-sig")))
    header = next(reader)
    if len(header) != len(set(header)) or any(not field for field in header):
        raise ValueError("invalid or duplicate CSV header")
    for row in reader:
        if len(row) != len(header):
            raise ValueError("malformed CSV row width")
    return pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False)


def _csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def _git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "--no-replace-objects", "-C", str(root), *args],
                          check=True, capture_output=True, timeout=60).stdout


def _read_blob(root: Path, commit: str, path: str, digest: str | None = None) -> bytes:
    if (not re.fullmatch(r"[0-9a-f]{40}", commit) or path.startswith(("/", "-")) or "\\" in path
            or any(part in {"", ".", ".."} for part in path.split("/"))):
        raise ValueError("immutable commit and exact safe path required")
    if _git(root, "rev-parse", "--verify", commit + "^{commit}").decode().strip() != commit:
        raise ValueError("source commit identity mismatch")
    entries = [x for x in _git(root, "ls-tree", "-z", commit, "--", path).split(b"\0") if x]
    if len(entries) != 1:
        raise ValueError("frozen source blob missing: " + path)
    metadata, actual_path = entries[0].split(b"\t", 1)
    mode, kind, oid = metadata.decode("ascii").split()
    if mode != "100644" or kind != "blob" or actual_path.decode("utf-8") != path:
        raise ValueError("source is not the exact regular Git blob")
    raw = _git(root, "cat-file", "blob", oid)
    if digest is not None and _sha(raw) != digest:
        raise ValueError("frozen source raw SHA mismatch: " + path)
    return raw


def load_sources(root: Path = ROOT) -> dict[str, Any]:
    sources: dict[str, Any] = {
        key: _read_blob(root, SOURCE_COMMIT, spec["path"], spec["raw_sha256"])
        for key, spec in SOURCE_ARTIFACTS.items()
    }
    sources["snapshots"] = {
        path: _read_blob(root, SNAPSHOT_COMMIT, path)
        for path in sorted(set(_csv(sources["detail"])["snapshot_path"]))
    }
    return sources


def _number(text: Any, *, optional: bool = False) -> Decimal | None:
    try:
        number = Decimal(str(text))
    except InvalidOperation as exc:
        if optional:
            return None
        raise ValueError("invalid finite number: " + str(text)) from exc
    if not number.is_finite():
        if optional:
            return None
        raise ValueError("non-finite number")
    return number


def _recorded_state(value: str) -> str:
    if value not in {"True", "False", ""}:
        raise ValueError("unrecognized published boolean")
    return {"True": "pass", "False": "recorded_false", "": "unknown"}[value]


def feature_values(event: dict[str, str], row: dict[str, str], schema: bool) -> dict[str, str]:
    """Interpret published fields only; no model feature reconstruction/import."""
    fields = {"feature_" + name: row.get(name, "").strip() for name in FEATURE_FIELDS}
    fields.update({name + "_state": "unknown" for name in FEATURES})
    fields["context_schema_available"] = str(schema)
    fields["comparison_version"] = VERSION
    ret20 = _number(row.get("return_20d", ""), optional=True)
    if ret20 is not None:
        fields["ret20_5_25_state"] = "pass" if Decimal(5) <= ret20 <= Decimal(25) else "recorded_false"
    if not schema:
        return fields
    if row["price_pullback_signal_date"] != event["signal_date"]:
        raise ValueError("feature date is not the frozen signal date")
    available = _recorded_state(row["price_pullback_tdcc_history_available"])
    high = _recorded_state(row["price_pullback_high_thresholds_up"])
    if available == "pass":
        fields["tdcc_positive_state"] = high
    fields["obv_positive_state"] = _recorded_state(row["price_pullback_obv_above_ma20"])
    rsi = _number(row["price_pullback_rsi14"], optional=True)
    macd = _number(row["price_pullback_macd_hist"], optional=True)
    if rsi is not None and macd is not None:
        fields["technical_quality_state"] = "pass" if rsi >= 60 and macd > 0 else "recorded_false"
    return fields


def review_values(event: dict[str, str]) -> dict[str, str]:
    result = {}
    for horizon in HORIZONS:
        prefix = f"d{horizon}"
        original = event[prefix + "_anomaly_candidate"] == "True"
        number = _number(event[prefix + "_return_pct"], optional=True)
        magnitude = number is not None and abs(number) >= 50
        candidate = original or magnitude
        result[prefix + "_comparison_anomaly_candidate"] = str(candidate)
        result[prefix + "_comparison_anomaly_disposition"] = "unresolved_anomaly_candidate" if candidate else "not_flagged_by_this_review"
        result[prefix + "_comparison_anomaly_reason"] = "source_candidate_retained" if original else "absolute_return_ge50_investigation_only" if magnitude else ""
    return result


def verify_detail(sources: dict[str, Any], actual: pd.DataFrame) -> tuple[list[dict[str, str]], list[dict[str, Any]], list[str]]:
    if set(sources) != {"detail", "summary", "snapshots"}:
        raise ValueError("unexpected source set")
    for key, spec in SOURCE_ARTIFACTS.items():
        if _sha(sources[key]) != spec["raw_sha256"]:
            raise ValueError("immutable source SHA mismatch: " + key)
    original = _csv(sources["detail"])
    if list(actual.columns) != [*original.columns, *DETAIL_EXTRA]:
        raise ValueError("detail schema mismatch")
    if not actual.loc[:, original.columns].equals(original):
        raise ValueError("original frozen cells or row order changed")
    rows = original.to_dict("records")
    primary = [r for r in rows if r["primary_metric_included"] == "True"]
    if len(rows) != 3020 or len(primary) != 2992 or len({r["signal_event_id"] for r in primary}) != 2992:
        raise ValueError("frozen population mismatch")
    if len({(r["snapshot_path"], r["snapshot_csv_row_number"]) for r in rows}) != 3020:
        raise ValueError("duplicate snapshot row identity")
    snapshots = sources["snapshots"]
    if set(snapshots) != {r["snapshot_path"] for r in rows} or len(snapshots) != 32:
        raise ValueError("snapshot population mismatch")
    parsed, receipts = {}, []
    for path in sorted(snapshots):
        payload = snapshots[path]
        lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        accepted_hashes = {_sha(p) for p in (payload, lf, lf.replace(b"\n", b"\r\n"))}
        frame = _csv(payload)
        schema = set(FEATURE_FIELDS).issubset(frame.columns)
        recorded = sorted({r["snapshot_sha256"] for r in rows if r["snapshot_path"] == path})
        if not set(recorded).issubset(accepted_hashes):
            raise ValueError("snapshot raw/LF/CRLF lineage SHA mismatch")
        parsed[path] = (frame, frame.to_dict("records"), schema)
        receipts.append({"path": path, "raw_sha256": _sha(payload), "recorded_transport_sha256": recorded,
                         "row_count": len(frame), "column_count": len(frame.columns), "context_schema_available": schema})
    reconstructed = []
    for event, output in zip(rows, actual.to_dict("records")):
        frame, snapshot_rows, schema = parsed[event["snapshot_path"]]
        if (len(frame) != int(event["snapshot_total_row_count"])
                or len(frame.columns) != int(event["snapshot_total_column_count"])):
            raise ValueError("snapshot dimension mismatch")
        position = int(event["snapshot_csv_row_number"]) - 2
        if position < 0 or position >= len(frame):
            raise ValueError("snapshot CSV row out of range")
        source_row = snapshot_rows[position]
        if _sha(_canonical({k: v.strip() for k, v in source_row.items()})) != event["source_row_sha256"]:
            raise ValueError("immutable source row SHA mismatch")
        for key in ("stock_id", "model_id", "signal_date", "report_line", "report_bucket"):
            if source_row[key].strip() != event[key] or event["model_id"] != MODEL_ID:
                raise ValueError("published row identity mismatch: " + key)
        if source_row["source_row_index"].strip() != event["published_source_row_index"]:
            raise ValueError("published source index mismatch")
        expected_id = _sha((MODEL_ID + "|" + event["signal_date"] + "|" + event["stock_id"]).encode("utf-8"))
        if event["signal_event_id"] != expected_id:
            raise ValueError("signal event identity mismatch")
        expected = {**feature_values(event, source_row, schema), **review_values(event)}
        if any(output[key] != value for key, value in expected.items()):
            raise ValueError("published feature/state/date mismatch")
        reconstructed.append({**event, **expected})
    if sum(r["context_schema_available"] == "True" for r in reconstructed if r["primary_metric_included"] == "True") != 1846:
        raise ValueError("frozen context cohort mismatch")
    return reconstructed, receipts, list(original.columns)


def _in_group(row: dict[str, str], group: str) -> bool:
    context = row["context_schema_available"] == "True"
    if group == "baseline_all":
        return True
    if group == "baseline_context_schema":
        return context
    if group == "ret20_5_25_all":
        return row["ret20_5_25_state"] == "pass"
    if group == "ret20_5_25_context_schema":
        return context and row["ret20_5_25_state"] == "pass"
    if group == "baseline_tdcc_available":
        return context and row["tdcc_positive_state"] != "unknown"
    requirements = {
        "tdcc_positive": ("tdcc_positive_state", "pass"),
        "tdcc_recorded_false": ("tdcc_positive_state", "recorded_false"),
        "tdcc_unknown": ("tdcc_positive_state", "unknown"),
        "obv_positive": ("obv_positive_state", "pass"),
        "obv_recorded_false": ("obv_positive_state", "recorded_false"),
        "obv_unknown": ("obv_positive_state", "unknown"),
        "technical_quality": ("technical_quality_state", "pass"),
        "technical_recorded_false": ("technical_quality_state", "recorded_false"),
        "technical_unknown": ("technical_quality_state", "unknown"),
    }
    key, value = requirements[group]
    return context and row[key] == value


def _mature(rows: list[dict[str, str]], horizon: int, basis: str) -> list[dict[str, str]]:
    return [r for r in rows if r[f"d{horizon}_maturity_status"] == "mature"
            and not (basis == "raw_original_candidate_exclusion_sensitivity" and r[f"d{horizon}_anomaly_candidate"] == "True")]


def _return(row: dict[str, str], horizon: int, basis: str) -> Decimal:
    suffix = "_share_unit_return_pct" if basis == "partial_share_unit_supplement" else "_return_pct"
    value = _number(row[f"d{horizon}" + suffix])
    assert value is not None
    return value


def return_metrics(rows: list[dict[str, str]], horizon: int, basis: str) -> dict[str, Any]:
    mature = _mature(rows, horizon, basis)
    values = [_return(r, horizon, basis) for r in mature]
    n = len(values)
    result: dict[str, Any] = {
        "signal_count": len(rows), "mature_count": n,
        "immature_count": sum(r[f"d{horizon}_maturity_status"] != "mature" for r in rows),
        "excluded_candidate_count": sum(r[f"d{horizon}_maturity_status"] == "mature" and r[f"d{horizon}_anomaly_candidate"] == "True" for r in rows) if basis == "raw_original_candidate_exclusion_sensitivity" else 0,
        "unresolved_retained_count": sum(r[f"d{horizon}_anomaly_candidate"] == "True" for r in mature),
        "retained_review_candidate_count": sum(r[f"d{horizon}_comparison_anomaly_candidate"] == "True" for r in mature),
        "unique_stock_count": len({r["stock_id"] for r in mature}),
        "signal_date_count": len({r["signal_date"] for r in mature}),
    }
    counts = {
        "win": sum(v > 0 for v in values), "neutral": sum(v == 0 for v in values),
        "failure": sum(v < 0 for v in values), "high_return_ge10": sum(v >= 10 for v in values),
        "loss": sum(v < 0 for v in values), "tail_loss_le_minus10": sum(v <= -10 for v in values),
    }
    for key, count in counts.items():
        result[key + "_count"] = count
        result[key + "_rate_pct"] = Decimal(count) * 100 / n if n else ""
    result["average_return_pct"] = sum(values) / n if n else ""
    result["median_return_pct"] = statistics.median(values) if n else ""
    result["minimum_return_pct"] = min(values) if n else ""
    result["maximum_return_pct"] = max(values) if n else ""
    return result


def expected_tables(rows: list[dict[str, str]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    primary = [r for r in rows if r["primary_metric_included"] == "True"]
    periods = ["all", *sorted({r["signal_date"][:6] for r in primary})]
    summary, features = [], []
    for period in periods:
        population = [r for r in primary if period == "all" or r["signal_date"].startswith(period)]
        for horizon in HORIZONS:
            for basis in BASES:
                identity = {"artifact_version": VERSION, "model_id": MODEL_ID, "period": period,
                            "horizon": horizon, "metric_basis": basis}
                for group in GROUPS:
                    selected = [r for r in population if _in_group(r, group)]
                    summary.append({**identity, "group_id": group, **return_metrics(selected, horizon, basis),
                                    "formal_use_allowed": "False", "promotion_evidence_allowed": "False"})
                for population_basis, baseline in (("all", "baseline_all"), ("context_schema", "baseline_context_schema"), ("tdcc_available", "baseline_tdcc_available")):
                    mature = _mature([r for r in population if _in_group(r, baseline)], horizon, basis)
                    bands: dict[str, list[dict[str, str]]] = {"high_ge10": [], "middle_0_to_lt10": [], "loss_lt0": []}
                    for row in mature:
                        value = _return(row, horizon, basis)
                        band = "loss_lt0" if value < 0 else "high_ge10" if value >= 10 else "middle_0_to_lt10"
                        bands[band].append(row)
                    feature_identity = {"artifact_version": VERSION, "model_id": MODEL_ID, "period": period,
                                        "horizon": horizon, "population_basis": population_basis, "metric_basis": basis}
                    for band, band_rows in bands.items():
                        for feature in FEATURES:
                            for state in STATES:
                                count = sum(r[feature + "_state"] == state for r in band_rows)
                                n = len(band_rows)
                                features.append({**feature_identity, "outcome_band": band, "feature": feature, "feature_state": state,
                                                 "band_count": n, "state_count": count,
                                                 "state_rate_pct": Decimal(count) * 100 / n if n else "",
                                                 "formal_use_allowed": "False", "promotion_evidence_allowed": "False"})
    return summary, features


def _verify_table(actual: pd.DataFrame, expected: list[dict[str, Any]], label: str) -> None:
    if list(actual.columns) != list(expected[0]) or len(actual) != len(expected):
        raise ValueError(label + " schema/exhaustive row population mismatch")
    for index, (row, reference) in enumerate(zip(actual.to_dict("records"), expected)):
        for key, expected_value in reference.items():
            actual_value = row[key]
            if isinstance(expected_value, Decimal):
                number = _number(actual_value)
                if number is None or abs(number - expected_value) > Decimal("0.00000051"):
                    raise ValueError(f"{label} calculation mismatch: row {index} {key}")
            elif str(actual_value) != str(expected_value):
                raise ValueError(f"{label} population/identity/boundary mismatch: row {index} {key}")


def validate_bundle(root: Path, detail: pd.DataFrame, summary: pd.DataFrame, features: pd.DataFrame,
                    manifest: dict[str, Any], *, sources: dict[str, Any] | None = None) -> dict[str, Any]:
    sources = load_sources(root) if sources is None else sources
    rows, receipts, original_columns = verify_detail(sources, detail)
    expected_summary, expected_features = expected_tables(rows)
    _verify_table(summary, expected_summary, "summary")
    _verify_table(features, expected_features, "features")
    original_summary = _csv(sources["summary"])
    for original in original_summary.to_dict("records"):
        horizon = int(original["horizon"].split("+")[1])
        observed = [r for r in expected_summary if r["period"] == "all" and r["horizon"] == horizon
                    and r["metric_basis"] == "raw_primary" and r["group_id"] == "baseline_all"]
        if len(observed) != 1:
            raise ValueError("original baseline row missing")
        for field in ("mature_count", "win_count", "neutral_count", "failure_count"):
            if str(observed[0][field]) != original[field]:
                raise ValueError("original baseline population changed")
        for field in ("average_return_pct", "median_return_pct", "win_rate_pct"):
            if abs(observed[0][field] - _number(original[field])) > Decimal("0.0000011"):
                raise ValueError("original baseline metric changed")
    primary = [r for r in rows if r["primary_metric_included"] == "True"]
    coverage = {feature: dict(sorted(Counter(r[feature + "_state"] for r in primary).items())) for feature in FEATURES}
    expected_manifest = {
        "artifact_version": VERSION, "model_id": MODEL_ID, "owner_id": OWNER_ID,
        "source_commit": SOURCE_COMMIT, "source_artifacts": SOURCE_ARTIFACTS, "snapshot_commit": SNAPSHOT_COMMIT,
        "snapshots": receipts, "source_row_count": 3020, "unique_signal_event_count": 2992,
        "context_schema_primary_count": 1846, "feature_state_coverage": coverage,
        "original_columns": original_columns, "old_cells_and_order_unchanged": True,
        "groups": list(GROUPS), "metric_bases": list(BASES),
        "descriptive_return_bands": {"high_ge10": ">=10%", "middle_0_to_lt10": "0%<=return<10%", "loss_lt0": "<0%", "tail_loss": "<=-10%"},
        "band_threshold_use": "descriptive_only_not_model_gate_or_anomaly_disposition",
        "period_analysis_status": "same_sample_month_diagnostics_not_independent_oos",
        "review_anomaly_trigger": "source_candidate_or_absolute_raw_return_ge50_investigation_only",
        "sensitivity_scope": "excludes_original_source_candidates_only_new_review_candidates_retained",
        "feature_population_bases": ["all", "context_schema", "tdcc_available"],
        "user_authorization_ref": "user_20261010_pullback_short_reclaim_23ema_condition_comparison",
        "output_sha256": {OUTPUTS[k]: _sha(_csv_bytes(v)) for k, v in (("detail", detail), ("summary", summary), ("features", features))},
        **LIMITATIONS,
    }
    if _canonical(manifest) != _canonical(expected_manifest):
        raise ValueError("manifest immutable sources/output hashes/method/boundaries mismatch")
    return {"source_rows": 3020, "unique_signal_events": 2992, "context_schema_primary_count": 1846,
            "snapshot_count": 32, "summary_rows": len(summary), "feature_rows": len(features),
            "original_cells_and_unresolved_anomalies_retained": True, "formal_use_allowed": False}


def validate(root: Path = ROOT) -> dict[str, Any]:
    raw = {key: (root / path).read_bytes() for key, path in OUTPUTS.items()}
    manifest = json.loads(raw["manifest"])
    if raw["manifest"] != _canonical(manifest) + b"\n":
        raise ValueError("manifest is not canonical JSON bytes")
    if manifest.get("output_sha256") != {OUTPUTS[key]: _sha(raw[key]) for key in ("detail", "summary", "features")}:
        raise ValueError("physical output byte SHA mismatch")
    return validate_bundle(root, _csv(raw["detail"]), _csv(raw["summary"]), _csv(raw["features"]), manifest)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    print(json.dumps(validate(args.repo_root), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
