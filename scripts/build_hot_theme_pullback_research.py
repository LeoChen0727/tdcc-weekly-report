from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

try:
    from scripts.model_research_artifact_guard import (
        load_ownership_rules,
        model_owned_artifact_guard,
    )
except ModuleNotFoundError:
    from model_research_artifact_guard import (
        load_ownership_rules,
        model_owned_artifact_guard,
    )


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "hot_theme_pullback"
PRODUCER = "scripts/build_hot_theme_pullback_research.py"
ARTIFACT_VERSION = "hot_theme_pullback_published_signal_replay_v1"
MANIFEST_PATH = (
    ROOT
    / "output"
    / "history"
    / "daily_model_snapshots"
    / "daily_published_model_snapshot_manifest.csv"
)
SNAPSHOT_ROOT = ROOT / "output" / "history" / "daily_model_snapshots"
PRICE_ROOT = ROOT / "data" / "stock_price_history"
LATEST_ROOT = ROOT / "output" / "latest" / "research_backtest"
HISTORY_ROOT = ROOT / "output" / "history" / "research"
DOCS_ROOT = ROOT / "docs" / "latest"
OWNERSHIP_REGISTRY_PATH = ROOT / "config" / "model_research_artifact_ownership.csv"
REQUIRED_OWNERSHIP_RULES = {
    (
        "output/latest/research_backtest/hot_theme_pullback_*",
        "model_research_output",
        "model_owned_write",
        "research_only",
    ),
    (
        "output/history/research/hot_theme_pullback_*",
        "model_research_history",
        "model_owned_write",
        "research_only",
    ),
    (
        "docs/latest/hot_theme_pullback_*",
        "model_research_docs",
        "model_owned_write",
        "research_only",
    ),
}
SCENARIOS = {
    "fixed_d5_close": 5,
    "fixed_d10_close": 10,
    "fixed_d20_close": 20,
}
SIGNAL_ARTIFACT_ID = "model_signals_for_report"
REQUIRED_SIGNAL_COLUMNS = {
    "signal_date",
    "stock_id",
    "stock_name",
    "model_id",
    "model_score",
}
REQUIRED_PRICE_COLUMNS = {"date", "open", "high", "low", "close"}


def _text(value: Any) -> str:
    if value is None:
        return ""
    result = str(value).strip()
    return "" if result.lower() == "nan" else result


def _date(value: Any) -> str:
    text = "" if value is None else str(value)
    if len(text) != 8 or not text.isdigit():
        return ""
    try:
        parsed = datetime.strptime(text, "%Y%m%d")
    except ValueError:
        return ""
    return text if parsed.strftime("%Y%m%d") == text else ""


def _code(value: Any) -> str:
    value_text = _text(value)
    if value_text.endswith(".0") and value_text[:-2].isdigit():
        value_text = value_text[:-2]
    return value_text.zfill(4) if value_text.isdigit() and len(value_text) < 4 else value_text


def _canonical_text_bytes(raw: bytes) -> bytes:
    decoded = raw.decode("utf-8-sig")
    return decoded.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def canonical_file_sha256(path: Path) -> str:
    return hashlib.sha256(_canonical_text_bytes(path.read_bytes())).hexdigest()


def _published_hash_candidates(path: Path) -> set[str]:
    raw = path.read_bytes()
    lf = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {hashlib.sha256(payload).hexdigest() for payload in (raw, lf, crlf)}


def canonical_row_sha256(row: pd.Series | dict[str, Any]) -> str:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    values.pop("event_row_canonical_sha256", None)
    normalized = {str(key): _text(value) for key, value in values.items()}
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def row_set_sha256(values: list[str]) -> str:
    payload = "\n".join(sorted(_text(value) for value in values if _text(value))) + "\n"
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing CSV: {path.as_posix()}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def _repo_path(value: Any) -> Path:
    path = Path(_text(value))
    return path if path.is_absolute() else ROOT / path


def _display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _revision_number(value: Any) -> int:
    revision = _text(value).lower()
    if revision.startswith("r") and revision[1:].isdigit():
        return int(revision[1:])
    raise RuntimeError(f"invalid snapshot revision: {value!r}")


def load_latest_signal_manifest(
    manifest_path: Path = MANIFEST_PATH,
    snapshot_root: Path = SNAPSHOT_ROOT,
) -> pd.DataFrame:
    manifest = _read_csv(manifest_path)
    required = {
        "snapshot_report_date",
        "snapshot_revision",
        "supersedes_snapshot_sha256",
        "pipeline_commit_sha",
        "artifact_id",
        "snapshot_path",
        "snapshot_sha256",
        "row_count",
        "column_count",
        "purpose",
    }
    missing = sorted(required - set(manifest.columns))
    if missing:
        raise RuntimeError(f"snapshot manifest missing columns: {missing}")
    work = manifest[
        manifest["artifact_id"].astype(str).eq(SIGNAL_ARTIFACT_ID)
        & manifest["purpose"].astype(str).eq("as_published_daily_model_snapshot")
    ].copy()
    if work.empty:
        raise RuntimeError("snapshot manifest contains no formal model signal rows")
    work["snapshot_report_date"] = work["snapshot_report_date"].map(_date)
    work["_revision_number"] = work["snapshot_revision"].map(_revision_number)
    if work["snapshot_report_date"].eq("").any():
        raise RuntimeError("snapshot manifest has invalid report dates")
    if work.duplicated(["snapshot_report_date", "_revision_number"]).any():
        raise RuntimeError("snapshot manifest has duplicate report-date revisions")

    root_resolved = snapshot_root.resolve()
    for report_date, revisions in work.groupby("snapshot_report_date", sort=True):
        ordered = revisions.sort_values("_revision_number")
        expected = list(range(1, len(ordered) + 1))
        actual = ordered["_revision_number"].astype(int).tolist()
        if actual != expected:
            raise RuntimeError(
                f"snapshot revision chain is not contiguous: date={report_date}; revisions={actual}"
            )
        prior_sha = ""
        for _, manifest_row in ordered.iterrows():
            if int(manifest_row["_revision_number"]) > 1:
                if _text(manifest_row["supersedes_snapshot_sha256"]) != prior_sha:
                    raise RuntimeError(
                        f"snapshot supersession mismatch: date={report_date}; "
                        f"revision={manifest_row['snapshot_revision']}"
                    )
            snapshot_path = _repo_path(manifest_row["snapshot_path"])
            try:
                snapshot_path.resolve().relative_to(root_resolved)
            except ValueError as exc:
                raise RuntimeError(
                    f"snapshot escaped registered root: {snapshot_path.as_posix()}"
                ) from exc
            snapshot = _read_csv(snapshot_path)
            if _text(manifest_row["snapshot_sha256"]) not in _published_hash_candidates(
                snapshot_path
            ):
                raise RuntimeError(f"snapshot SHA mismatch: {snapshot_path.as_posix()}")
            if int(_text(manifest_row["row_count"])) != len(snapshot):
                raise RuntimeError(f"snapshot row count mismatch: {snapshot_path.as_posix()}")
            if int(_text(manifest_row["column_count"])) != len(snapshot.columns):
                raise RuntimeError(f"snapshot column count mismatch: {snapshot_path.as_posix()}")
            prior_sha = _text(manifest_row["snapshot_sha256"])

    selected = (
        work.sort_values(["snapshot_report_date", "_revision_number"])
        .groupby("snapshot_report_date", as_index=False, sort=False)
        .tail(1)
        .copy()
    )
    selected["snapshot_revision_policy"] = "latest_revision_per_report_date_artifact"
    return selected.sort_values("snapshot_report_date").reset_index(drop=True)


def _price_frame(stock_id: str, price_root: Path) -> tuple[pd.DataFrame, Path, str]:
    path = price_root / f"{_code(stock_id)}.csv"
    if not path.is_file():
        raise RuntimeError(f"missing price history: {path.as_posix()}")
    frame = _read_csv(path)
    missing = sorted(REQUIRED_PRICE_COLUMNS - set(frame.columns))
    if missing:
        raise RuntimeError(
            f"price history missing required columns: {path.as_posix()}; {missing}"
        )
    if frame.empty:
        raise RuntimeError(f"empty price history: {path.as_posix()}")
    frame = frame.copy()
    frame["date"] = frame["date"].map(_date)
    parsed_dates = pd.to_datetime(frame["date"], format="%Y%m%d", errors="coerce")
    if frame["date"].eq("").any() or parsed_dates.isna().any():
        raise RuntimeError(f"price history contains invalid date: {path.as_posix()}")
    if frame["date"].duplicated(keep=False).any():
        duplicates = sorted(
            set(frame.loc[frame["date"].duplicated(keep=False), "date"].astype(str))
        )
        raise RuntimeError(
            f"price history contains duplicate date: {path.as_posix()}; {duplicates}"
        )
    for column in ["open", "high", "low", "close"]:
        numeric = pd.to_numeric(frame[column], errors="coerce")
        if (
            numeric.isna().any()
            or not numeric.map(math.isfinite).all()
            or (numeric <= 0).any()
        ):
            raise RuntimeError(
                f"price history contains invalid required price: "
                f"{path.as_posix()}; column={column}"
            )
        frame[column] = numeric
    frame = frame.sort_values("date").reset_index(drop=True)
    return frame, path, canonical_file_sha256(path)


def _signal_bases(manifest: pd.DataFrame) -> list[dict[str, Any]]:
    bases: list[dict[str, Any]] = []
    for _, manifest_row in manifest.iterrows():
        snapshot_path = _repo_path(manifest_row["snapshot_path"])
        snapshot = _read_csv(snapshot_path)
        missing = sorted(REQUIRED_SIGNAL_COLUMNS - set(snapshot.columns))
        if missing:
            raise RuntimeError(f"signal snapshot missing columns: {snapshot_path}; {missing}")
        selected = snapshot[snapshot["model_id"].astype(str).eq(MODEL_ID)].copy()
        if selected.empty:
            continue
        selected["_signal_date"] = selected["signal_date"].map(_date)
        selected["_stock_id"] = selected["stock_id"].map(_code)
        if selected["_signal_date"].eq("").any() or selected["_stock_id"].eq("").any():
            raise RuntimeError(f"invalid model signal identity: {snapshot_path.as_posix()}")
        if not selected["_signal_date"].eq(manifest_row["snapshot_report_date"]).all():
            raise RuntimeError(
                f"signal date differs from snapshot report date: {snapshot_path.as_posix()}"
            )
        for (signal_date, stock_id), rows in selected.groupby(
            ["_signal_date", "_stock_id"], sort=True
        ):
            sort_columns = [
                column for column in ["report_bucket", "model_rank"] if column in rows.columns
            ]
            ordered = rows.sort_values(sort_columns) if sort_columns else rows
            representative = ordered.iloc[0]
            source_hashes = sorted(canonical_row_sha256(row) for _, row in rows.iterrows())
            report_buckets = (
                rows["report_bucket"].tolist()
                if "report_bucket" in rows.columns
                else []
            )
            bases.append(
                {
                    "artifact_version": ARTIFACT_VERSION,
                    "model_id": MODEL_ID,
                    "signal_event_key": f"{MODEL_ID}|{signal_date}|{stock_id}",
                    "signal_date": signal_date,
                    "stock_id": stock_id,
                    "stock_name": _text(representative.get("stock_name", "")),
                    "model_score": _text(representative.get("model_score", "")),
                    "model_rank": _text(representative.get("model_rank", "")),
                    "report_bucket_memberships": "|".join(
                        sorted({_text(value) for value in report_buckets if _text(value)})
                    ),
                    "source_signal_row_count": len(rows),
                    "source_signal_row_sha256s": "|".join(source_hashes),
                    "source_signal_row_set_sha256": row_set_sha256(source_hashes),
                    "snapshot_report_date": _text(
                        manifest_row["snapshot_report_date"]
                    ),
                    "snapshot_revision": _text(manifest_row["snapshot_revision"]),
                    "snapshot_revision_policy": _text(
                        manifest_row["snapshot_revision_policy"]
                    ),
                    "snapshot_path": _display_path(snapshot_path),
                    "snapshot_sha256": canonical_file_sha256(snapshot_path),
                    "snapshot_manifest_row_sha256": canonical_row_sha256(
                        {
                            key: manifest_row[key]
                            for key in manifest.columns
                            if not key.startswith("_")
                        }
                    ),
                    "snapshot_pipeline_commit_sha": _text(
                        manifest_row["pipeline_commit_sha"]
                    ),
                }
            )
    identities = [base["signal_event_key"] for base in bases]
    if len(identities) != len(set(identities)):
        raise RuntimeError("published signal replay produced duplicate signal event keys")
    return bases


def _scenario_row(
    base: dict[str, Any],
    scenario_id: str,
    horizon: int,
    price: pd.DataFrame,
    price_path: Path,
    price_sha256: str,
) -> dict[str, Any]:
    row = {
        **base,
        "scenario_id": scenario_id,
        "horizon_sessions": horizon,
        "entry_price_basis": "next_trading_day_open",
        "exit_price_basis": f"d{horizon}_close",
        "price_source_path": (
            price_path.relative_to(ROOT).as_posix()
            if price_path.is_absolute() and ROOT in price_path.parents
            else price_path.as_posix()
        ),
        "price_source_sha256": price_sha256,
        "entry_date": "",
        "entry_open_price": "",
        "exit_date": "",
        "exit_close_price": "",
        "entry_price_row_sha256": "",
        "exit_price_row_sha256": "",
        "return_valid": False,
        "right_censored": False,
        "invalid_reason": "",
        "gross_return_pct": "",
        "return_outcome": "not_mature",
        "primary_metric_included": False,
        "anomaly_candidate_flag": False,
        "anomaly_candidate_kinds": "",
        "anomaly_disposition": "not_triggered",
        "formal_use_allowed": False,
        "approved_for_daily": False,
        "presentation_allowed": False,
        "operation_contract_status": "decision_required",
        "full_historical_condition_replay_status": (
            "blocked_missing_point_in_time_hot_theme_labels"
        ),
        "research_only": True,
    }
    if price.empty:
        row["invalid_reason"] = "missing_or_invalid_price_history"
        return row
    future = price[price["date"].astype(str) > base["signal_date"]].reset_index(drop=True)
    if future.empty:
        row["right_censored"] = True
        row["invalid_reason"] = "missing_next_trading_day"
        return row
    entry = future.iloc[0]
    row["entry_date"] = _text(entry["date"])
    row["entry_open_price"] = float(entry["open"])
    row["entry_price_row_sha256"] = canonical_row_sha256(entry)
    exit_index = horizon - 1
    if exit_index >= len(future):
        row["right_censored"] = True
        row["invalid_reason"] = f"right_censored_before_d{horizon}"
        return row
    exit_row = future.iloc[exit_index]
    entry_price = float(entry["open"])
    exit_price = float(exit_row["close"])
    row["exit_date"] = _text(exit_row["date"])
    row["exit_close_price"] = exit_price
    row["exit_price_row_sha256"] = canonical_row_sha256(exit_row)
    if not math.isfinite(entry_price) or entry_price <= 0 or not math.isfinite(exit_price):
        row["invalid_reason"] = "nonpositive_or_nonfinite_operation_price"
        return row
    realized = (exit_price / entry_price - 1.0) * 100.0
    row["gross_return_pct"] = round(realized, 8)
    row["return_valid"] = True
    row["primary_metric_included"] = True
    row["return_outcome"] = "win" if realized > 0 else "failure" if realized < 0 else "neutral"
    return row


def _mark_anomaly_candidates(events: pd.DataFrame) -> pd.DataFrame:
    out = events.copy()
    for _, indexes in out.groupby("scenario_id").groups.items():
        mature_indexes = [
            index for index in indexes if bool(out.at[index, "return_valid"])
        ]
        if not mature_indexes:
            continue
        values = pd.to_numeric(
            out.loc[mature_indexes, "gross_return_pct"], errors="coerce"
        )
        q1 = float(values.quantile(0.25))
        q3 = float(values.quantile(0.75))
        iqr = q3 - q1
        absolute_total = float(values.abs().sum())
        for index, value in values.items():
            triggers: list[str] = []
            if abs(float(value)) >= 30.0:
                triggers.append("absolute_return_30pct")
            if iqr > 0 and (float(value) < q1 - 6 * iqr or float(value) > q3 + 6 * iqr):
                triggers.append("six_iqr_distance")
            if (
                len(values) >= 10
                and absolute_total > 0
                and abs(float(value)) / absolute_total >= 0.10
            ):
                triggers.append("absolute_contribution_10pct")
            if triggers:
                out.at[index, "anomaly_candidate_flag"] = True
                out.at[index, "anomaly_candidate_kinds"] = "|".join(triggers)
                out.at[index, "anomaly_disposition"] = "unresolved_anomaly_candidate"
    out["event_row_canonical_sha256"] = [
        canonical_row_sha256(row) for _, row in out.iterrows()
    ]
    return out


def build_events(
    manifest_path: Path = MANIFEST_PATH,
    snapshot_root: Path = SNAPSHOT_ROOT,
    price_root: Path = PRICE_ROOT,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    manifest = load_latest_signal_manifest(manifest_path, snapshot_root)
    rows: list[dict[str, Any]] = []
    price_cache: dict[str, tuple[pd.DataFrame, Path, str]] = {}
    for base in _signal_bases(manifest):
        stock_id = base["stock_id"]
        if stock_id not in price_cache:
            price_cache[stock_id] = _price_frame(stock_id, price_root)
        price, price_path, price_sha256 = price_cache[stock_id]
        for scenario_id, horizon in SCENARIOS.items():
            rows.append(
                _scenario_row(
                    base,
                    scenario_id,
                    horizon,
                    price,
                    price_path,
                    price_sha256,
                )
            )
    if not rows:
        raise RuntimeError(f"no {MODEL_ID} rows found in published signal snapshots")
    events = _mark_anomaly_candidates(pd.DataFrame(rows))
    return events.sort_values(
        ["signal_date", "stock_id", "horizon_sessions"]
    ).reset_index(drop=True), manifest


def _rate(count: int, total: int) -> float | str:
    return round(count / total * 100.0, 8) if total else ""


def build_summary(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    unique_signal_count = events["signal_event_key"].nunique()
    for scenario_id, horizon in SCENARIOS.items():
        part = events[events["scenario_id"].astype(str).eq(scenario_id)]
        mature = part[part["return_valid"].astype(bool)].copy()
        returns = pd.to_numeric(mature["gross_return_pct"], errors="coerce").dropna()
        wins = int((returns > 0).sum())
        neutral = int((returns == 0).sum())
        failures = int((returns < 0).sum())
        candidates = mature[mature["anomaly_candidate_flag"].astype(bool)]
        sensitivity = mature[~mature["anomaly_candidate_flag"].astype(bool)]
        sensitivity_returns = pd.to_numeric(
            sensitivity["gross_return_pct"], errors="coerce"
        ).dropna()
        rows.append(
            {
                "artifact_version": ARTIFACT_VERSION,
                "model_id": MODEL_ID,
                "analysis_scope": "published_signal_exact_membership",
                "scenario_id": scenario_id,
                "horizon_sessions": horizon,
                "entry_basis": "next_trading_day_open",
                "exit_basis": f"d{horizon}_close",
                "signal_event_count": unique_signal_count,
                "mature_count": len(returns),
                "right_censored_count": int(part["right_censored"].astype(bool).sum()),
                "invalid_count": int(
                    (
                        ~part["return_valid"].astype(bool)
                        & ~part["right_censored"].astype(bool)
                    ).sum()
                ),
                "unique_stock_count": mature["stock_id"].nunique(),
                "win_count": wins,
                "neutral_count": neutral,
                "failure_count": failures,
                "win_rate_pct": _rate(wins, len(returns)),
                "neutral_rate_pct": _rate(neutral, len(returns)),
                "failure_rate_pct": _rate(failures, len(returns)),
                "avg_return_pct": (
                    round(float(returns.mean()), 8) if len(returns) else ""
                ),
                "median_return_pct": (
                    round(float(returns.median()), 8) if len(returns) else ""
                ),
                "high_return_threshold_pct": 10.0,
                "high_return_hit_rate_pct": _rate(
                    int((returns >= 10.0).sum()), len(returns)
                ),
                "loss_rate_pct": _rate(failures, len(returns)),
                "anomaly_candidate_count": len(candidates),
                "unresolved_anomaly_count": len(candidates),
                "primary_metrics_retain_unresolved_candidates": True,
                "candidate_exclusion_sensitivity_count": len(sensitivity_returns),
                "candidate_exclusion_sensitivity_win_rate_pct": _rate(
                    int((sensitivity_returns > 0).sum()), len(sensitivity_returns)
                ),
                "candidate_exclusion_sensitivity_avg_return_pct": (
                    round(float(sensitivity_returns.mean()), 8)
                    if len(sensitivity_returns)
                    else ""
                ),
                "sensitivity_is_corrected_primary": False,
                "formal_use_allowed": False,
                "operation_contract_status": "decision_required",
                "full_historical_condition_replay_status": (
                    "blocked_missing_point_in_time_hot_theme_labels"
                ),
                "research_status": "published_signal_exact_replay_research_only",
            }
        )
    return pd.DataFrame(rows)


def build_manifest(
    events: pd.DataFrame,
    summary: pd.DataFrame,
    selected_manifest: pd.DataFrame,
    manifest_path: Path = MANIFEST_PATH,
) -> pd.DataFrame:
    event_hashes = events["event_row_canonical_sha256"].astype(str).tolist()
    snapshot_hashes = sorted(set(events["snapshot_sha256"].astype(str)))
    price_hashes = sorted(
        {value for value in events["price_source_sha256"].astype(str) if value}
    )
    return pd.DataFrame(
        [
            {
                "artifact_version": ARTIFACT_VERSION,
                "model_id": MODEL_ID,
                "producer_path": PRODUCER,
                "producer_canonical_sha256": canonical_file_sha256(ROOT / PRODUCER),
                "evidence_basis": "as_published_formal_signal_membership",
                "production_condition_recalculated": False,
                "snapshot_revision_policy": "latest_revision_per_report_date_artifact",
                "source_manifest_path": _display_path(manifest_path),
                "source_manifest_sha256": canonical_file_sha256(manifest_path),
                "selected_snapshot_count": len(selected_manifest),
                "selected_snapshot_date_min": selected_manifest[
                    "snapshot_report_date"
                ].min(),
                "selected_snapshot_date_max": selected_manifest[
                    "snapshot_report_date"
                ].max(),
                "selected_snapshot_bundle_sha256": row_set_sha256(snapshot_hashes),
                "price_input_file_count": len(price_hashes),
                "price_input_bundle_sha256": row_set_sha256(price_hashes),
                "signal_event_count": events["signal_event_key"].nunique(),
                "scenario_event_count": len(events),
                "events_row_set_sha256": row_set_sha256(event_hashes),
                "summary_row_set_sha256": row_set_sha256(
                    [canonical_row_sha256(row) for _, row in summary.iterrows()]
                ),
                "anomaly_candidate_count": int(
                    events["anomaly_candidate_flag"].astype(bool).sum()
                ),
                "effective_anomaly_blocker_count": int(
                    events["anomaly_candidate_flag"].astype(bool).sum()
                ),
                "semantic_version_binding_status": (
                    "published_pipeline_commit_only_no_current_ast_binding"
                ),
                "full_historical_condition_replay_status": (
                    "blocked_missing_point_in_time_hot_theme_labels"
                ),
                "operation_contract_status": "decision_required",
                "formal_use_allowed": False,
                "approved_for_daily": False,
                "presentation_allowed": False,
                "promotion_evidence_allowed": False,
                "production_change": False,
            }
        ]
    )


def build_research(
    manifest_path: Path = MANIFEST_PATH,
    snapshot_root: Path = SNAPSHOT_ROOT,
    price_root: Path = PRICE_ROOT,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    events, selected_manifest = build_events(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    summary = build_summary(events)
    anomalies = events[events["anomaly_candidate_flag"].astype(bool)].copy()
    manifest = build_manifest(events, summary, selected_manifest, manifest_path)
    return events, summary, anomalies, manifest


def _write_csv(frame: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, encoding="utf-8-sig")


def preflight_model_owned_output_registration(
    registry_path: Path | None = None,
) -> None:
    path = registry_path or OWNERSHIP_REGISTRY_PATH
    rules = load_ownership_rules(path)
    model_rules = [rule for rule in rules if rule.owner_model_id == MODEL_ID]
    observed = {
        (
            rule.artifact_glob,
            rule.artifact_class,
            rule.change_policy,
            rule.formal_evidence_status,
        )
        for rule in model_rules
        if rule.producer == PRODUCER
    }
    wrong_producers = sorted(
        {rule.producer for rule in model_rules if rule.producer != PRODUCER}
    )
    errors: list[str] = []
    if observed != REQUIRED_OWNERSHIP_RULES:
        errors.append(
            "exact model-owned artifact rules mismatch: "
            f"missing={sorted(REQUIRED_OWNERSHIP_RULES - observed)}; "
            f"extra={sorted(observed - REQUIRED_OWNERSHIP_RULES)}"
        )
    if wrong_producers:
        errors.append(
            f"model ownership contains wrong producers: {wrong_producers}"
        )
    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise RuntimeError(
            f"{MODEL_ID} ownership preflight failed before artifact writes:\n"
            f"{details}"
        )


def write_outputs(
    events: pd.DataFrame,
    summary: pd.DataFrame,
    anomalies: pd.DataFrame,
    manifest: pd.DataFrame,
) -> list[Path]:
    stems = {
        "events": "hot_theme_pullback_published_signal_events_latest.csv",
        "summary": "hot_theme_pullback_published_signal_summary_latest.csv",
        "anomalies": "hot_theme_pullback_published_signal_anomaly_candidates_latest.csv",
        "manifest": "hot_theme_pullback_published_signal_manifest_latest.csv",
    }
    frames = {"events": events, "summary": summary, "anomalies": anomalies}
    paths: list[Path] = []
    for key, frame in frames.items():
        latest = LATEST_ROOT / stems[key]
        docs = DOCS_ROOT / stems[key]
        _write_csv(frame, latest)
        _write_csv(frame, docs)
        paths.extend([latest, docs])
    manifest = manifest.copy()
    for key in ["events", "summary", "anomalies"]:
        latest = LATEST_ROOT / stems[key]
        manifest[f"{key}_path"] = latest.relative_to(ROOT).as_posix()
        manifest[f"{key}_file_sha256"] = canonical_file_sha256(latest)
        manifest[f"{key}_row_count"] = len(frames[key])
    manifest["evidence_payload_bundle_sha256"] = row_set_sha256(
        [
            _text(manifest.at[0, "events_file_sha256"]),
            _text(manifest.at[0, "summary_file_sha256"]),
            _text(manifest.at[0, "anomalies_file_sha256"]),
        ]
    )
    latest_manifest = LATEST_ROOT / stems["manifest"]
    docs_manifest = DOCS_ROOT / stems["manifest"]
    _write_csv(manifest, latest_manifest)
    _write_csv(manifest, docs_manifest)
    paths.extend([latest_manifest, docs_manifest])
    bundle = _text(manifest.at[0, "evidence_payload_bundle_sha256"])[:12]
    for key, frame in {**frames, "manifest": manifest}.items():
        history_name = stems[key].replace("_latest.csv", f"_{bundle}.csv")
        history = HISTORY_ROOT / history_name
        _write_csv(frame, history)
        paths.append(history)
    return paths


def main() -> int:
    preflight_model_owned_output_registration()
    with model_owned_artifact_guard(MODEL_ID, PRODUCER):
        outputs = write_outputs(*build_research())
    print(f"{MODEL_ID} published-signal research built")
    for path in outputs:
        print(path.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
