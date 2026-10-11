"""Versioned 23EMA implementation-consistency diagnostic; never a production run.

Read pinned Git objects in memory and retain every eligible signal, including
suppressed and censored rows. Historical selected research AST is a reference
implementation, not independent promotion evidence or a restored 1,161 ledger.
"""
from __future__ import annotations

import argparse
import ast
import csv
from contextlib import contextmanager
import fnmatch
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import re
import subprocess
import time

import numpy as np
import pandas as pd

try:
    from .model_research_artifact_guard import load_ownership_rules, load_protected_sentinels, validate_changed_paths
except ImportError:
    from model_research_artifact_guard import load_ownership_rules, load_protected_sentinels, validate_changed_paths


MODEL_ID = "price_pullback_23ema"
OWNER_ID = "price_pullback_23ema_versioned_replay"
PRODUCER = "scripts/build_price_pullback_23ema_versioned_replay.py"
SOURCE_REF = "eca870524360ede3ad3072e7c175b7353259ad86"
SEMANTIC_REF = "2f1374ff78376ced98e142a9632b227845507dd6"
SIGNAL_START = "20251128"
SIGNAL_END = "20260602"
DATA_CEILING = "20260703"
PREFIX = "price_pullback_23ema_replay_v1_"
OUTPUT_NAMES = tuple(PREFIX + suffix for suffix in (
    "ledger.csv.gz", "pit_coverage.csv", "parity.csv", "summary.csv",
    "feature_comparison.csv", "manifest.json",
))
FEATURES = ("feature_close_above_ema23", "feature_ma5_above_3_days_ago", "feature_volume_ratio_ge_1_5")
KNOWN_CANDIDATES = {
    ("2380", "20260519"), ("7734", "20260526"), ("5498", "20260513"),
    ("6588", "20260508"), ("3189", "20260515"), ("3532", "20260515"),
}
PRIMARY_BASIS = "primary_retaining_unresolved_candidate"
SENSITIVITY_BASIS = "candidate_exclusion_sensitivity_only"


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def row_sha256(row: dict) -> str:
    return sha256(canonical_json(row).encode("utf-8"))


def git(repo_root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=repo_root)


def optional_number(value: object) -> float | None:
    try:
        number = float(value)
    except (ValueError, TypeError):
        return None
    return number if math.isfinite(number) else None


def trueish(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def read_git_inputs(repo_root: Path) -> tuple[dict[str, bytes], list[dict]]:
    """Read canonical Git bytes without archive checkout/EOL conversion."""
    tree = git(repo_root, "ls-tree", "-r", SOURCE_REF, "data/stock_price_history", "data/tdcc_stock_history")
    objects = {}
    for line in tree.decode("utf-8").splitlines():
        meta, path = line.split("\t", 1)
        if path.endswith(".csv"):
            objects[path] = meta.split()[2]
    paths = sorted(objects)
    payload = subprocess.check_output(
        ["git", "--no-replace-objects", "cat-file", "--batch"], cwd=repo_root,
        input=("\n".join(objects[path] for path in paths) + "\n").encode("utf-8"),
    )
    blobs, offset = {}, 0
    for path in paths:
        end = payload.index(b"\n", offset)
        oid, kind, size = payload[offset:end].split()
        if oid.decode() != objects[path] or kind != b"blob":
            raise ValueError(f"canonical Git blob mismatch: {path}")
        size = int(size)
        blobs[path] = payload[end + 1:end + 1 + size]
        offset = end + size + 2
    sources = [{"path": path, "git_blob": objects[path], "sha256": sha256(payload), "bytes": len(payload)}
               for path, payload in sorted(blobs.items())]
    return blobs, sources


def protected_snapshot(repo_root: Path) -> dict:
    """Use existing sentinel ownership without expanding protected sparse roots."""
    sentinels = load_protected_sentinels(repo_root / "config/model_research_protected_sentinels.csv")
    snapshot = {}
    for line in git(repo_root, "ls-tree", "-r", SOURCE_REF).decode("utf-8").splitlines():
        meta, path = line.split("\t", 1)
        if not any(fnmatch.fnmatchcase(path, sentinel.artifact_glob) for sentinel in sentinels):
            continue
        present = repo_root / path
        snapshot[path] = {"git_blob": meta.split()[2],
                          "present_sparse_sha256": sha256(present.read_bytes()) if present.is_file() else None}
    return snapshot


def output_snapshot(output_root: Path) -> dict[str, str]:
    if not output_root.exists():
        return {}
    return {path.name: sha256(path.read_bytes()) if path.is_file() else "directory"
            for path in output_root.iterdir()}


@contextmanager
def model_owned_artifact_guard(repo_root: Path, output_root: Path):
    """Guard this model's actual six external outputs and sparse source state."""
    repo_root, output_root = repo_root.resolve(), output_root.resolve()
    if output_root == repo_root or repo_root in output_root.parents:
        raise ValueError("diagnostic output-root must be outside the sparse repository")
    if any((output_root / name).exists() for name in OUTPUT_NAMES):
        raise ValueError("versioned replay refuses to overwrite an existing artifact")
    rules = load_ownership_rules(repo_root / "config/model_research_artifact_ownership.csv")
    logical_outputs = [f"output/research/price_pullback_23ema/{name}" for name in OUTPUT_NAMES]
    errors = validate_changed_paths(OWNER_ID, PRODUCER, logical_outputs, rules)
    if errors:
        raise RuntimeError("\n".join(errors))
    repository_before = git(repo_root, "status", "--porcelain=v1", "--untracked-files=all")
    protected_before = protected_snapshot(repo_root)
    external_before = output_snapshot(output_root)
    protected_hash = row_sha256(protected_before)
    receipt = {
        "protected_sentinel_before_sha256": protected_hash,
        "protected_sentinel_after_sha256": protected_hash,
        "protected_sentinel_method": "immutable_Git_blob_hashes_and_present_sparse_file_SHA256",
    }
    completed = False
    try:
        yield receipt
        completed = True
    finally:
        external_after = output_snapshot(output_root)
        changed = {name for name in set(external_before) | set(external_after)
                   if external_before.get(name) != external_after.get(name)}
        if changed - set(OUTPUT_NAMES):
            raise RuntimeError("model-owned output scope changed outside six artifacts")
        if git(repo_root, "status", "--porcelain=v1", "--untracked-files=all") != repository_before:
            raise RuntimeError("repository changed during diagnostic producer")
        if protected_snapshot(repo_root) != protected_before:
            raise RuntimeError("protected mature-model artifacts changed during replay")
        if completed and changed != set(OUTPUT_NAMES):
            raise RuntimeError("model-owned producer did not create exactly six artifacts")


def extract_research_functions(repo_root: Path, path: str, roots: tuple[str, ...]) -> tuple[dict, dict]:
    """Compile only pinned research functions and module-local dependencies.

    No import statements from the referenced modules are executed. In particular,
    the legacy aggregate and its production imports never run.
    """
    payload = git(repo_root, "show", f"{SEMANTIC_REF}:{path}")
    tree = ast.parse(payload.decode("utf-8-sig"))
    nodes = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            nodes[node.name] = node
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    nodes[target.id] = node
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            nodes[node.target.id] = node
    namespace = {"pd": pd, "np": np, "math": math, "re": re, "Path": Path}
    selected = {}
    def visit(name):
        if name in namespace or name in selected or name not in nodes:
            return
        node = nodes[name]
        selected[name] = node
        for child in ast.walk(node):
            if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
                visit(child.id)
    for root in roots:
        visit(root)
    unique = {id(node): node for node in selected.values()}
    body = [ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)]
    body.extend(sorted(unique.values(), key=lambda node: node.lineno))
    module = ast.fix_missing_locations(ast.Module(body=body, type_ignores=[]))
    exec(compile(module, f"{SEMANTIC_REF}:{path}", "exec"), namespace)
    receipt = {
        "path": path, "ref": SEMANTIC_REF, "sha256": sha256(payload),
        "selected_symbols": sorted(selected),
        "ast_sha256": sha256(ast.dump(module, include_attributes=False).encode("utf-8")),
    }
    return namespace, receipt


def prepare_stock_frame(raw: pd.DataFrame, technical: dict, research: dict) -> pd.DataFrame:
    """Keep the old volume warm-up, and retain the right-edge pending signal.

    The original weekly helper drops rows without next-open/future outcomes.
    Here only that right-edge maturity drop is removed, so it is visible in the
    ledger rather than silently disappearing from the diagnostic cohort.
    """
    if len(raw) < 26:
        return pd.DataFrame()
    work = raw.copy()
    previous_volume_mean = work["volume"].shift(1).rolling(20, min_periods=20).mean()
    work["start_day_volume_ratio_vs_prev20"] = work["volume"] / previous_volume_mean
    warmup = pd.DataFrame({
        "current_ratio": work["start_day_volume_ratio_vs_prev20"],
        "previous_ratio": work["volume"].shift(1) / work["volume"].shift(2).rolling(20, min_periods=20).mean(),
        "current_five_ratio": work["volume"].rolling(5, min_periods=5).mean() / previous_volume_mean,
        "previous_five_ratio": work["volume"].shift(1).rolling(5, min_periods=5).mean() / previous_volume_mean,
    }).notna().all(axis=1)
    work["next_open"] = work["open"].shift(-1)
    work["next_open_to_d20_close_return_pct"] = (work["close"].shift(-20) / work["next_open"] - 1) * 100
    next_open_gap = (work["next_open"] / work["close"] - 1) * 100
    old_entry_fields_valid = work["next_open"].notna() & next_open_gap.notna()
    right_edge = work.index == len(work) - 1
    work = work.loc[warmup & (old_entry_fields_valid | right_edge)].reset_index(drop=True)
    if work.empty:
        return work
    work = technical["add_technical_features"](work)
    return research["add_price_structure_features"](work)


def replay_trace(trace: list[dict], entry_price: float | None, target_price: float | None, variant: str) -> dict:
    """Scalar replay of the old research's close-confirmed operation basis."""
    target_day = stop_day = None
    streak = 0
    for row in trace[:20]:
        day, close = row["day"], optional_number(row.get("close"))
        ma20, ema23 = optional_number(row.get("ma20")), optional_number(row.get("ema23"))
        if close is not None and target_price is not None and target_day is None:
            hit = close >= target_price if variant == "legacy_ge" else close > target_price
            if hit:
                target_day = day
        below = close is not None and ma20 is not None and ema23 is not None and close <= min(ma20, ema23) * 0.96
        streak = streak + 1 if below else 0
        if streak >= 4 and stop_day is None:
            stop_day = day
    result = {"target_day": target_day, "stop_day": stop_day, "exit_date": "", "exit_price": None,
              "exit_reason": "right_censored", "realized_return_pct": None, "outcome_bucket": "immature",
              "realized_days": None, "exit_offset": None, "mature": False}
    if not trace or entry_price is None or entry_price <= 0:
        result["exit_reason"] = "pending_next_open_entry"
        return result
    # Preserve the historical ALL-D1..D20-reference + D2..D21-open maturity rule.
    complete = target_price is not None and len(trace) >= 21 and all(
        optional_number(row.get(column)) is not None
        for row in trace[:20] for column in ("close", "ma20", "ema23")
    ) and all(optional_number(row.get("open")) is not None and float(row["open"]) > 0 for row in trace[:21])
    if not complete:
        return result
    result["mature"] = True
    if target_day is not None and target_day == stop_day:
        result.update(exit_reason="same_day_unresolved", outcome_bucket="same_day_unresolved",
                      realized_days=target_day, exit_offset=target_day + 1,
                      exit_date=trace[target_day]["date"])
        return result
    if target_day is not None and (stop_day is None or target_day < stop_day):
        day, bucket, reason = target_day, "win", "target_breakout_next_open"
    elif stop_day is not None:
        day, bucket, reason = stop_day, "failure", "sustained_stop_next_open"
    else:
        day, bucket, reason = 20, None, "d20_close"
    exit_row = trace[day] if reason != "d20_close" else trace[19]
    exit_price = float(exit_row["open"] if reason != "d20_close" else exit_row["close"])
    realized_return = (exit_price / entry_price - 1) * 100
    result.update(exit_date=exit_row["date"], exit_price=exit_price, exit_reason=reason,
                  realized_return_pct=realized_return,
                  outcome_bucket=bucket or ("neutral" if realized_return >= 0 else "failure"),
                  realized_days=day, exit_offset=day + (reason != "d20_close"))
    return result


def replay_formal_adapter(trace: list[dict], target_price: float | None) -> dict:
    """Independent literal reading of adapter ordering; no formal signal claim."""
    if not trace:
        return {"state": "pending_next_open_entry", "confirmation_date": "", "confirmation_day": None,
                "exit_date": "", "exit_reason": ""}
    streak = 0
    for row in trace[:20]:
        close = optional_number(row.get("close"))
        ma20, ema23 = optional_number(row.get("ma20")), optional_number(row.get("ema23"))
        valid_refs = [ref for ref in (ma20, ema23) if ref is not None and ref > 0]
        stop_price = min(valid_refs) * 0.96 if valid_refs else None
        reason = None
        if close is not None and target_price is not None and close > target_price:
            reason = "close_prev20_high_break_next_open"
        else:
            streak = streak + 1 if close is not None and stop_price is not None and close <= stop_price else 0
            if streak >= 4:
                reason = "sustained_close_below_lower_ma20_ema23_4pct_4d"
        if reason:
            next_row = trace[row["day"]] if row["day"] < len(trace) else None
            pending_state = "target_exit_pending_next_open" if reason == "close_prev20_high_break_next_open" else "stop_exit_pending_next_open"
            return {"state": "exited" if next_row is not None else pending_state,
                    "confirmation_date": row["date"], "confirmation_day": row["day"],
                    "exit_date": next_row["date"] if next_row else "", "exit_reason": reason}
    return {"state": "expired_d20_no_active_tracking" if len(trace) >= 20 else "right_censored",
            "confirmation_date": "", "confirmation_day": None, "exit_date": "", "exit_reason": ""}


def metrics(rows: list[dict], high_return_threshold: float | None = None) -> dict:
    n = len(rows)
    values = [float(row["realized_return_pct"]) for row in rows if optional_number(row.get("realized_return_pct")) is not None]
    if high_return_threshold is None and values:
        high_return_threshold = float(np.quantile(values, 0.75))
    rate = lambda count: 100 * count / n if n else None
    return {
        "n": n, "mature_count": n, "finite_return_count": len(values), "missing_return_count": n - len(values),
        "win_pct": rate(sum(row["outcome_bucket"] == "win" for row in rows)),
        "neutral_pct": rate(sum(row["outcome_bucket"] == "neutral" for row in rows)),
        "failure_pct": rate(sum(row["outcome_bucket"] == "failure" for row in rows)),
        "mean_return_pct": float(np.mean(values)) if values else None,
        "median_return_pct": float(np.median(values)) if values else None,
        "high_return_threshold_pct": high_return_threshold,
        "high_return_hit_rate_pct": rate(sum(value >= high_return_threshold for value in values)) if high_return_threshold is not None else None,
        "loss_pct": rate(sum(value < 0 for value in values)),
        "unresolved_candidate_count": sum(row["anomaly_status"] == "unresolved_anomaly_candidate" for row in rows),
    }


def build_metrics(ledger: list[dict]) -> tuple[list[dict], list[dict]]:
    summaries, comparisons = [], []
    for variant in ("legacy_ge", "strict_gt_legacy_refs"):
        variant_rows = [row for row in ledger if row["rule_variant"] == variant]
        primary = [row for row in variant_rows if row["accepted_trade"] and row["mature"]]
        for basis in (PRIMARY_BASIS, SENSITIVITY_BASIS):
            rows = primary if basis == PRIMARY_BASIS else [row for row in primary if row["anomaly_status"] != "unresolved_anomaly_candidate"]
            stat = metrics(rows)
            summaries.append({"rule_variant": variant, "basis": basis,
                              "eligible_signal_count": sum(row["gate_eligible"] for row in variant_rows),
                              "suppressed_signal_count": sum(row["lifecycle_status"] == "suppressed_active_position" for row in variant_rows),
                              "immature_signal_count": sum(row["gate_eligible"] and not row["mature"] for row in variant_rows),
                              "left_censored_count": sum(row["lifecycle_status"] == "left_censored" for row in variant_rows),
                              "promotion_allowed": False, "original_1161_ledger_restored": False, **stat})
            high = stat["high_return_threshold_pct"]
            for group_name, group in (
                ("high_return_upper_quartile", [row for row in rows if optional_number(row["realized_return_pct"]) is not None and row["realized_return_pct"] >= high] if high is not None else []),
                ("negative_return", [row for row in rows if optional_number(row["realized_return_pct"]) is not None and row["realized_return_pct"] < 0]),
                ("matched_single_feature", rows),
            ):
                for feature in FEATURES:
                    selected = [row for row in group if row[feature] is True]
                    known = sum(row[feature] is not None for row in group)
                    comparisons.append({"rule_variant": variant, "basis": basis, "group": group_name, "feature": feature,
                                        "cohort_n": len(group), "known_n": known, "unknown_n": len(group) - known,
                                        "feature_true_pct_of_known": 100 * len(selected) / known if known else None,
                                        "buy_sell_holding_basis": "same_accepted_trade_cohort_no_signal_reselection",
                                        **metrics(selected if group_name == "matched_single_feature" else group, high)})
    return summaries, comparisons


def build_replay(repo_root: Path) -> dict:
    blobs, source_files = read_git_inputs(repo_root)
    weekly, weekly_receipt = extract_research_functions(repo_root, "scripts/research_weekly_20pct_surge_volume.py", ("read_price",))
    technical, technical_receipt = extract_research_functions(repo_root, "scripts/research_weekly_surge_technical_grid.py", ("add_technical_features",))
    research, research_receipt = extract_research_functions(repo_root, "scripts/build_daily_model_parameter_research.py",
                                                         ("add_price_structure_features", "current_price_pullback_approved_operation_baseline"))
    code_sources = [weekly_receipt, technical_receipt, research_receipt]
    for path in ("scripts/build_daily_candidate_model_layer.py", "scripts/build_daily_price_pullback_23ema_operation_section.py"):
        payload = git(repo_root, "show", f"{SOURCE_REF}:{path}")
        code_sources.append({"path": path, "ref": SOURCE_REF, "sha256": sha256(payload), "selected_symbols": [], "ast_sha256": "", "use": "read_only_formal_semantic_reference_not_executed"})
    ledger, pit_coverage = [], []
    global_offset = 0
    for path in sorted(path for path in blobs if path.startswith("data/stock_price_history/")):
        stock = Path(path).stem
        payload = blobs[path]
        raw_rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))))
        source_by_date = {str(row["date"]): row for row in raw_rows if str(row["date"]) <= DATA_CEILING}
        if len(source_by_date) != sum(str(row["date"]) <= DATA_CEILING for row in raw_rows):
            raise ValueError(f"duplicate source stock/date: {path}")
        raw = weekly["read_price"](io.BytesIO(payload))
        raw = raw[raw["date"].astype(str).le(DATA_CEILING)].reset_index(drop=True)
        raw["_clean_position"] = range(len(raw))
        full = pd.read_csv(io.BytesIO(payload), dtype={"stock_id": str}, keep_default_na=False)
        full = full[full["date"].astype(str).le(DATA_CEILING)].copy()
        for column in ("open", "high", "low", "close", "volume"):
            full[column] = pd.to_numeric(full[column], errors="coerce")
        full = full.dropna(subset=["open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)
        full["ma20"] = full["close"].rolling(20, min_periods=20).mean()
        full["ema23"] = full["close"].ewm(span=23, adjust=False, min_periods=23).mean()
        full_positions = {str(row["date"]): index for index, row in full.iterrows()}
        raw_features = pd.DataFrame(index=raw.index)
        raw_ema = raw["close"].ewm(span=23, adjust=False, min_periods=23).mean()
        raw_ma5 = raw["close"].rolling(5, min_periods=5).mean()
        raw_volume_mean = raw["volume"].rolling(20, min_periods=20).mean()
        raw_features[FEATURES[0]] = (raw["close"] > raw_ema).where(raw_ema.notna())
        raw_features[FEATURES[1]] = (raw_ma5 > raw_ma5.shift(3)).where(raw_ma5.notna() & raw_ma5.shift(3).notna())
        raw_features[FEATURES[2]] = (raw["volume"] / raw_volume_mean >= 1.5).where(raw_volume_mean.notna() & raw_volume_mean.gt(0))
        tdcc_path = f"data/tdcc_stock_history/{stock}.csv"
        tdcc_payload = blobs.get(tdcc_path, b"")
        tdcc_rows = list(csv.DictReader(io.StringIO(tdcc_payload.decode("utf-8-sig")))) if tdcc_payload else []
        tdcc_rows = sorted((row for row in tdcc_rows if str(row.get("as_of_date", "")) <= DATA_CEILING), key=lambda row: str(row.get("as_of_date", "")))
        for family, family_path, records in (("price", path, list(source_by_date.values())), ("tdcc", tdcc_path, tdcc_rows)):
            dates = [str(row.get("date" if family == "price" else "as_of_date", "")) for row in records]
            publication_known = sum(bool(row.get("available_at")) for row in records)
            pit_coverage.append({"stock_id": stock, "source_family": family, "path": family_path,
                                 "source_rows": len(records), "first_date": min(dates) if dates else "", "last_date": max(dates) if dates else "",
                                 "publication_available_at_known_rows": publication_known,
                                 "pit_status": "unknown_original_publication", "promotion_allowed": False})
        work = prepare_stock_frame(raw, technical, research)
        if work.empty:
            global_offset += len(raw)
            continue
        last_tdcc = None
        tdcc_index = 0
        availability, high_up, joined_tdcc = [], [], []
        for date in work["date"].astype(str):
            while tdcc_index < len(tdcc_rows) and str(tdcc_rows[tdcc_index].get("as_of_date", "")) <= date:
                last_tdcc = tdcc_rows[tdcc_index]
                tdcc_index += 1
            availability.append(last_tdcc is not None)
            high_up.append(trueish(last_tdcc.get("high_thresholds_up", "")) if last_tdcc else False)
            joined_tdcc.append(last_tdcc)
        work["tdcc_history_available"] = availability
        work["high_thresholds_up"] = high_up
        gates = research["current_price_pullback_approved_operation_baseline"](work).fillna(False)
        active = {variant: None for variant in ("legacy_ge", "strict_gt_legacy_refs")}
        for position, signal in work.iterrows():
            date = str(signal["date"])
            if not SIGNAL_START <= date <= SIGNAL_END:
                continue
            left_censored = any(optional_number(signal.get(column)) is None for column in ("ema23", "ma20", "return_20d_pct", "range_high_20d_prev"))
            gate = bool(gates.iloc[position])
            if not gate and not left_censored:
                continue
            signal_id = sha256(f"{SOURCE_REF}|{stock}|{date}|legacy_five_gate_v1".encode())
            target = optional_number(signal.get("range_high_20d_prev"))
            forward = work.iloc[position + 1:position + 22]
            trace = [{"day": day, "date": str(row["date"]),
                      **{column: optional_number(row.get(column)) for column in ("open", "high", "low", "close", "ma20", "ema23")},
                      "source_row_sha256": row_sha256(source_by_date[str(row["date"])])}
                     for day, (_, row) in enumerate(forward.iterrows(), start=1)]
            full_pos = full_positions.get(date)
            formal_target = optional_number(full.iloc[max(0, full_pos - 20):full_pos]["high"].max()) if full_pos is not None and full_pos else None
            formal_forward = full.iloc[full_pos + 1:full_pos + 22] if full_pos is not None else full.iloc[0:0]
            formal_trace = [{"day": day, "date": str(row["date"]),
                             **{column: optional_number(row.get(column)) for column in ("open", "high", "low", "close", "ma20", "ema23")},
                             "source_row_sha256": row_sha256(source_by_date[str(row["date"])])}
                            for day, (_, row) in enumerate(formal_forward.iterrows(), start=1)]
            tdcc = joined_tdcc[position]
            clean_position = int(signal["_clean_position"])
            feature_values = {feature: None if pd.isna(raw_features.iloc[clean_position][feature]) else bool(raw_features.iloc[clean_position][feature]) for feature in FEATURES}
            entry_price = optional_number(trace[0]["open"]) if trace else None
            for variant in ("legacy_ge", "strict_gt_legacy_refs"):
                trade_id = sha256(f"{signal_id}|{variant}".encode())
                outcome = replay_trace(trace, entry_price, target, variant)
                if left_censored and not gate:
                    outcome.update(mature=False, realized_return_pct=None, outcome_bucket="immature",
                                   exit_reason="left_censored", exit_price=None, exit_date="",
                                   realized_days=None, exit_offset=None)
                status = "exited" if outcome["mature"] else outcome["exit_reason"]
                if outcome["exit_reason"] == "same_day_unresolved":
                    status = "same_day_unresolved"
                accepted, suppressed_by = gate, ""
                previous = active[variant]
                if gate and previous is not None and position < previous["exit_position"]:
                    accepted, suppressed_by, status = False, previous["trade_id"], "suppressed_active_position"
                exit_position = position + outcome["exit_offset"] if outcome["exit_offset"] is not None else len(work)
                if accepted:
                    active[variant] = {"trade_id": trade_id, "exit_position": exit_position}
                if left_censored and not gate:
                    status = "left_censored"
                reasons = []
                if (stock, date) in KNOWN_CANDIDATES:
                    reasons.append("retained_six_case_unresolved_candidate")
                if outcome["realized_return_pct"] is not None and abs(outcome["realized_return_pct"]) >= 20:
                    reasons.append("absolute_return_ge20_investigation_trigger_only")
                if any(row["open"] is not None and row["close"] is not None and row["open"] > 0 and abs(row["close"] / row["open"] - 1) >= 0.5 for row in trace[:20]):
                    reasons.append("large_same_day_price_move_investigation_trigger_only")
                ledger.append({
                    "source_ref": SOURCE_REF, "semantic_ref": SEMANTIC_REF, "formal_ref": SOURCE_REF,
                    "model_id": MODEL_ID, "signal_id": signal_id, "trade_id": trade_id,
                    "stock_id": stock, "signal_date": date, "rule_variant": variant,
                    "new_global_index": global_offset + clean_position, "stock_day_position": position,
                    "stock_work_rows": len(work),
                    "selector_status": "legacy_gate_eligible" if gate else "unknown_left_censored",
                    "gate_eligible": gate, "lifecycle_status": status, "accepted_trade": accepted,
                    "suppressed_by_trade_id": suppressed_by, "entry_date": trace[0]["date"] if trace else "",
                    "entry_price": entry_price, "target_price": target, **outcome,
                    "d20_date": trace[19]["date"] if len(trace) >= 20 else "",
                    "d20_close": trace[19]["close"] if len(trace) >= 20 else None,
                    "exit_stock_day_position": exit_position,
                    "anomaly_status": "unresolved_anomaly_candidate" if reasons else "no_candidate_trigger",
                    "anomaly_reasons": ";".join(reasons), "primary_included": accepted and outcome["mature"],
                    "pit_status": "unknown_original_publication", "tdcc_as_of_date": str(tdcc.get("as_of_date", "")) if tdcc else "",
                    "publication_available_at": "", "price_blob_sha256": sha256(payload),
                    "signal_row_sha256": row_sha256(source_by_date[date]),
                    "tdcc_blob_sha256": sha256(tdcc_payload) if tdcc_payload else "",
                    "tdcc_row_sha256": row_sha256(tdcc) if tdcc else "",
                    "trace_json": canonical_json(trace), "formal_adapter_trace_json": canonical_json(formal_trace),
                    "formal_target_price": formal_target, "formal_adapter_result_json": canonical_json(replay_formal_adapter(formal_trace, formal_target)),
                    "formal_position_status": "not_formal_position", "pre_effective_from": date < "20260703",
                    "fullselectorparity_not_proven": True, **feature_values,
                })
        global_offset += len(raw)
    summary, feature_comparison = build_metrics(ledger)
    parity = [
        {"check_id": "target_operator", "research_rule": ">=", "formal_rule": ">", "status": "different", "detail": "strict_gt_legacy_refs changes only the operator on identical legacy gate/features"},
        {"check_id": "same_day_priority", "research_rule": "same_day_unresolved", "formal_rule": "target_first", "status": "different", "detail": "formal independent trace checks target before updating the four-day stop"},
        {"check_id": "d20_terminal", "research_rule": "realized_D20_close", "formal_rule": "expired_d20_no_active_tracking", "status": "not_proven", "detail": "adapter emits no realized D20 price; do not infer full formal return parity"},
        {"check_id": "support_fields", "research_rule": "OR across all support fields", "formal_rule": "first_numeric_alias", "status": "not_proven", "detail": "production candidate rows and alias precedence are not reconstructed"},
        {"check_id": "return20", "research_rule": "recomputed trimmed close history", "formal_rule": "saved return_20d first", "status": "not_proven", "detail": "rounding and candidate field lineage can change edge gates"},
        {"check_id": "obv", "research_rule": "trimmed research prefix", "formal_rule": "full price prefix", "status": "not_proven", "detail": "no production selector import or matched historical input snapshot"},
        {"check_id": "tdcc", "research_rule": "as_of backward join", "formal_rule": "production as_of/latest row", "status": "not_proven", "detail": "no original available_at or complete revision history"},
        {"check_id": "warmup", "research_rule": "weekly positive-volume warm-up then technical", "formal_rule": "full cleaned OHLC", "status": "different", "detail": "formal target/MA/EMA trace is separately recomputed; pending right edge retained"},
        {"check_id": "nonoverlap", "research_rule": "stock/signal position before previous exit suppressed", "formal_rule": "formal buy-ranked position lineage", "status": "not_proven", "detail": "counterfactual diagnostic positions are not formal positions"},
        {"check_id": "effective_date", "research_rule": "20251128..20260602", "formal_rule": "from 20260703", "status": "different", "detail": "all research window rows predate formal signal effective_from"},
        {"check_id": "full_production_selector_and_ranking", "research_rule": "legacy five-gate cohort", "formal_rule": "candidate source/context/ranking/report line", "status": "not_proven", "detail": "same-gate exit comparison is not full production parity"},
    ]
    manifest = {
        "schema_version": 1, "artifact_version": "price_pullback_23ema_replay_v1", "model_id": MODEL_ID,
        "owner_id": OWNER_ID, "producer": PRODUCER, "source_ref": SOURCE_REF, "semantic_ref": SEMANTIC_REF,
        "formal_ref": SOURCE_REF, "signal_start": SIGNAL_START, "signal_end": SIGNAL_END, "data_ceiling": DATA_CEILING,
        "source_files": source_files, "code_sources": code_sources, "formal_rule_differences": parity,
        "primary_basis": PRIMARY_BASIS, "sensitivity_basis": SENSITIVITY_BASIS,
        "numerical_trigger_interpretation": "investigation_candidates_only_no_final_disposition_or_primary_exclusion",
        "row_hash_definition": "sha256 compact sorted UTF8 JSON of original all-string CSV row",
        "pending_policy": "new diagnostic pending locks until source right edge; not original accepted-ledger restoration",
        "diagnostic_type": "new_model_owned_implementation_consistency_replay",
        "original_1161_ledger_restored": False, "original_primary_metrics_modified": False,
        "original_publication_version_verified": False, "formal_signal_selector_parity_proven": False,
        "trading_calendar_continuity_proven": False,
        "formal_model_backtest_parity_or_anomaly_disposition_proven": False,
        "promotion_allowed": False, "production_business_functions_imported": False,
        "legacy_aggregate_producer_executed": False, "production_or_latest_artifacts_written": False,
        "pit_blocker": "price/TDCC original publication available_at and revision lineage not verified",
    }
    return {"ledger": ledger, "pit_coverage": pit_coverage, "parity": parity, "summary": summary,
            "feature_comparison": feature_comparison, "manifest": manifest}


def deterministic_gzip(payload: bytes) -> bytes:
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb", filename="", mtime=0) as stream:
        stream.write(payload)
    return buffer.getvalue()


def write_outputs(output_root: Path, result: dict) -> dict[str, str]:
    targets = [output_root / name for name in OUTPUT_NAMES]
    if any(path.exists() for path in targets):
        raise ValueError("versioned replay refuses to overwrite an existing artifact")
    output_root.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for key in ("ledger", "pit_coverage", "parity", "summary", "feature_comparison"):
        frame = pd.DataFrame(result[key])
        payload = frame.to_csv(index=False, lineterminator="\n").encode("utf-8")
        name = PREFIX + key + ".csv"
        if key == "ledger":
            name += ".gz"
            payload = deterministic_gzip(payload)
        with (output_root / name).open("xb") as stream:
            stream.write(payload)
        hashes[name] = sha256(payload)
    manifest = dict(result["manifest"], output_hashes=hashes)
    with (output_root / (PREFIX + "manifest.json")).open("xb") as stream:
        stream.write((json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8"))
    return hashes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="產生新的23EMA完整診斷ledger；不覆寫latest或宣稱原1161還原。")
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args(argv)
    repo_root, output_root = args.repo_root.resolve(), args.output_root.resolve()
    started = time.monotonic()
    with model_owned_artifact_guard(repo_root, output_root) as guard_receipt:
        result = build_replay(repo_root)
        result["manifest"].update(guard_receipt)
        hashes = write_outputs(output_root, result)
    print(json.dumps({"state": "diagnostic_outputs_created_pending_independent_validation", "ledger_rows": len(result["ledger"]),
                      "output_root": str(output_root), "output_hashes": hashes,
                      "elapsed_seconds": round(time.monotonic() - started, 3), "promotion_allowed": False}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
