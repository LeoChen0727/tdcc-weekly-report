"""Independent input-bound operation arithmetic; not selector/PIT proof.

This validator never imports or executes a producer or production business
function. Trace arithmetic is independent; legacy feature/selector completeness
is explicitly outside this claim and must remain unproven.
"""
from __future__ import annotations

import argparse
import ast
import csv
import gzip
import hashlib
import io
import json
import math
import subprocess
from pathlib import Path
from typing import Any

import pandas as pd

PREFIX = "price_pullback_23ema_replay_v1_"
SOURCE_REF = "eca870524360ede3ad3072e7c175b7353259ad86"
SEMANTIC_REF = "2f1374ff78376ced98e142a9632b227845507dd6"
VARIANTS = ("legacy_ge", "strict_gt_legacy_refs")
BASES = ("primary_retaining_unresolved_candidate", "candidate_exclusion_sensitivity_only")
FEATURES = ("feature_close_above_ema23", "feature_ma5_above_3_days_ago", "feature_volume_ratio_ge_1_5")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def truth(value: Any) -> bool:
    return value is True or str(value).strip().lower() in {"true", "1"}


def number(value: Any) -> float | None:
    try:
        result = float(value)
    except (ValueError, TypeError):
        return None
    return result if math.isfinite(result) else None


def same_number(left: Any, right: Any) -> bool:
    a, b = number(left), number(right)
    return a is None and b is None or a is not None and b is not None and math.isclose(a, b, rel_tol=1e-10, abs_tol=1e-8)


def _days(trace: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    rows = {}
    for row in trace:
        day = int(row["day"])
        if day in rows:
            raise ValueError(f"duplicate forward day: {day}")
        rows[day] = row
    return rows


def replay_legacy(trace: list[dict[str, Any]], entry_price: Any, target_price: Any,
                  variant: str = "legacy_ge") -> dict[str, Any]:
    """Independently reproduce the legacy-reference event and D20 semantics."""
    if variant not in VARIANTS:
        raise ValueError(f"unknown rule variant: {variant}")
    rows = _days(trace)
    entry, target = number(entry_price), number(target_price)
    # Legacy valid/dropna requires every forward20 reference and D21 open,
    # even when a possible earlier target has a known next open.
    mature = entry is not None and entry > 0 and target is not None
    mature = mature and all(day in rows and all(number(rows[day].get(k)) is not None
                                               for k in ("close", "ma20", "ema23")) for day in range(1, 21))
    mature = mature and all(day in rows and number(rows[day].get("open")) is not None
                           for day in range(2, 22))
    if not mature:
        return {"mature": False, "exit_reason": "right_censored", "realized_return_pct": None,
                "outcome_bucket": "not_mature"}
    target_pct = (target / entry - 1) * 100
    target_day = stop_day = None
    streak = 0
    for day in range(1, 21):
        row = rows[day]
        close_pct = (float(row["close"]) / entry - 1) * 100
        stop_price = min(float(row["ma20"]), float(row["ema23"])) * .96
        stop_pct = (stop_price / entry - 1) * 100
        target_hit = close_pct >= target_pct if variant == "legacy_ge" else close_pct > target_pct
        streak = streak + 1 if close_pct <= stop_pct else 0
        if target_day is None and target_hit:
            target_day = day
        if stop_day is None and streak >= 4:
            stop_day = day
    if target_day is not None and target_day == stop_day:
        reason, chosen_day, price, bucket = "same_day_unresolved", target_day, None, "same_day_unresolved"
    elif target_day is not None and (stop_day is None or target_day < stop_day):
        reason, chosen_day, bucket = "target_breakout_next_open", target_day, "win"
        price = float(rows[chosen_day + 1]["open"])
    elif stop_day is not None:
        reason, chosen_day, bucket = "sustained_stop_next_open", stop_day, "failure"
        price = float(rows[chosen_day + 1]["open"])
    else:
        reason, chosen_day = "d20_close", 20
        price = float(rows[20]["close"])
        bucket = "neutral" if price >= entry else "failure"
    offset = chosen_day + (reason != "d20_close")
    return {"mature": True, "target_day": target_day, "stop_day": stop_day, "realized_days": chosen_day,
            "exit_reason": reason, "confirmation_date": rows[chosen_day]["date"],
            "exit_date": rows[int(offset)]["date"], "exit_price": price,
            "exit_stock_day_offset": int(offset),
            "realized_return_pct": (price / entry - 1) * 100 if price is not None else None,
            "outcome_bucket": bucket, "d20_date": rows[20]["date"], "d20_close": float(rows[20]["close"])}


def replay_formal(trace: list[dict[str, Any]], entry_price: Any, target_price: Any) -> dict[str, Any]:
    """Formal full-history references, target first, no realized D20 expiry."""
    rows = _days(trace)
    entry, target = number(entry_price), number(target_price)
    if entry is None or entry <= 0 or 1 not in rows:
        return {"state": "pending_next_open_entry", "realized_return_pct": None}
    streak = 0
    for day in range(1, 21):
        if day not in rows:
            return {"state": "active_operation", "stop_confirmed_days": streak, "realized_return_pct": None}
        row = rows[day]
        close = number(row.get("close"))
        refs = [v for k in ("ma20", "ema23") if (v := number(row.get(k))) is not None and v > 0]
        stop = min(refs) * .96 if refs else None
        reason = None
        # Ordering is deliberate: the formal adapter does not increment the
        # stop counter on a target-confirmation day.
        if target is not None and close is not None and close > target:
            reason = "close_prev20_high_break_next_open"
        else:
            streak = streak + 1 if close is not None and stop is not None and close <= stop else 0
            if streak >= 4:
                reason = "sustained_close_below_lower_ma20_ema23_4pct_4d"
        if reason is not None:
            next_row = rows.get(day + 1, {})
            price = number(next_row.get("open"))
            pending = price is None
            state = ("target_exit_pending_next_open" if reason == "close_prev20_high_break_next_open" else "stop_exit_pending_next_open") if pending else "exited"
            return {"state": state, "exit_reason": reason, "confirmation_date": row["date"],
                    "realized_days": day, "exit_date": next_row.get("date", ""), "exit_price": price,
                    "stop_confirmed_days": streak,
                    "realized_return_pct": (price / entry - 1) * 100 if price is not None else None}
    return {"state": "expired_d20_no_active_tracking", "exit_price": None, "exit_date": "",
            "realized_return_pct": None, "stop_confirmed_days": streak}


def expected_lifecycle(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Stock-only legacy locks; equality at prior exit position is eligible."""
    active = {}
    result = {}
    ordered = sorted(rows, key=lambda r: (r["rule_variant"], r["stock_id"], int(r["stock_day_position"]), int(r["new_global_index"])))
    for row in ordered:
        key = row["rule_variant"], row["stock_id"]
        prior = active.get(key)
        position = int(row["stock_day_position"])
        eligible = truth(row.get("gate_eligible", True))
        suppressed = eligible and prior is not None and position < prior["exit_position"]
        replay = replay_legacy(json.loads(row["trace_json"]), row["entry_price"], row["target_price"], row["rule_variant"])
        exit_position = position + replay["exit_stock_day_offset"] if eligible and replay["mature"] else int(row.get("stock_work_rows", position + len(json.loads(row["trace_json"])) + 1))
        result[row["trade_id"]] = {"accepted_trade": eligible and not suppressed,
                                    "suppressed_by_trade_id": prior["trade_id"] if suppressed else "",
                                    "exit_stock_day_position": exit_position, "mature": replay["mature"] and eligible}
        if eligible and not suppressed:
            active[key] = {"trade_id": row["trade_id"], "exit_position": exit_position}
    return result


def metrics(rows: list[dict[str, Any]], *, high_cut: float | None = None) -> dict[str, Any]:
    n = len(rows)
    returns = [v for row in rows if (v := number(row.get("realized_return_pct"))) is not None]
    ordered = sorted(returns)
    cut = float(pd.Series(ordered, dtype=float).quantile(.75)) if high_cut is None and ordered else high_cut
    rate = lambda count: 100 * count / n if n else None
    return {"n": n, "mature_count": n, "finite_return_count": len(returns), "missing_return_count": n - len(returns),
            "win_pct": rate(sum(r["outcome_bucket"] == "win" for r in rows)),
            "neutral_pct": rate(sum(r["outcome_bucket"] == "neutral" for r in rows)),
            "failure_pct": rate(sum(r["outcome_bucket"] == "failure" for r in rows)),
            "mean_return_pct": sum(returns) / len(returns) if returns else None,
            "median_return_pct": float(pd.Series(ordered, dtype=float).median()) if ordered else None,
            "high_return_threshold_pct": cut,
            "high_return_hit_rate_pct": rate(sum(v >= cut for v in returns)) if cut is not None else None,
            "loss_pct": rate(sum(v < 0 for v in returns)),
            "unresolved_candidate_count": sum(r.get("anomaly_status") == "unresolved_anomaly_candidate" for r in rows)}


def canonical_row_sha256(row: dict[str, Any]) -> str:
    return digest(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def source_ast_sha256(raw: bytes, selected_symbols: list[str]) -> str:
    tree = ast.parse(raw.decode("utf-8-sig"))
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
    if set(selected_symbols) - set(nodes):
        raise ValueError("selected AST symbols absent from pinned source")
    selected = sorted({id(nodes[name]): nodes[name] for name in selected_symbols}.values(), key=lambda n: n.lineno)
    module = ast.Module(body=[ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0), *selected], type_ignores=[])
    return digest(ast.dump(module, include_attributes=False).encode("utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, mode="rt", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def git_blob(repo_root: Path, ref: str, path: str) -> bytes:
    return subprocess.run(["git", "--no-replace-objects", "show", f"{ref}:{path}"], cwd=repo_root,
                          check=True, capture_output=True).stdout


def _check_metrics(expected: dict[str, Any], observed: dict[str, Any], label: str, errors: list[str]) -> None:
    for key, value in expected.items():
        if key not in observed or not same_number(observed[key], value):
            errors.append(f"{label}: metric {key} mismatch: expected={value} observed={observed.get(key)}")


def _git_sources(repo: Path, manifest: dict[str, Any], ledger: list[dict[str, str]], errors: list[str]) -> dict[str, bytes]:
    """Batch object verification; never materialize data or invoke business code."""
    listing = subprocess.run(["git", "--no-replace-objects", "ls-tree", "-r", "-z", SOURCE_REF, "--",
                              "data/stock_price_history", "data/tdcc_stock_history"], cwd=repo, check=True, capture_output=True).stdout
    tree = {}
    for raw in listing.split(b"\0"):
        if not raw:
            continue
        meta, path = raw.split(b"\t", 1)
        if path.endswith(b".csv"):
            tree[path.decode()] = meta.split()[2].decode()
    files = manifest["source_files"]
    if {r["path"] for r in files} != set(tree):
        errors.append("source inventory differs from exact pinned Git source families")
        return {}
    if any(tree[r["path"]] != r["git_blob"] for r in files):
        errors.append("source Git blob identity mismatch")
        return {}
    payload = subprocess.run(["git", "--no-replace-objects", "cat-file", "--batch"], cwd=repo, check=True,
                             input=("\n".join(r["git_blob"] for r in files) + "\n").encode(), capture_output=True).stdout
    wanted = {f"data/{family}/{row['stock_id']}.csv" for row in ledger for family in ("stock_price_history", "tdcc_stock_history")}
    retained = {}
    offset = 0
    view = memoryview(payload)
    for record in files:
        header_end = payload.index(b"\n", offset)
        oid, kind, size_text = payload[offset:header_end].split()
        size = int(size_text)
        raw = view[header_end + 1:header_end + 1 + size]
        if oid.decode() != record["git_blob"] or kind != b"blob" or size != int(record["bytes"]) or digest(raw) != record["sha256"]:
            errors.append(f"source bytes/hash binding mismatch: {record['path']}")
        if record["path"] in wanted:
            retained[record["path"]] = bytes(raw)
        offset = header_end + size + 2
    for record in manifest["code_sources"]:
        raw = git_blob(repo, record["ref"], record["path"])
        if digest(raw) != record["sha256"]:
            errors.append(f"pinned code SHA mismatch: {record['path']}")
        if record["selected_symbols"] and source_ast_sha256(raw, record["selected_symbols"]) != record["ast_sha256"]:
            errors.append(f"pinned code AST SHA mismatch: {record['path']}")
    return retained


def _source_frames(raw: bytes) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, dict[str, str]]]:
    originals = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
    originals = [r for r in originals if r["date"] <= "20260703"]
    by_date = {r["date"]: r for r in originals}
    if len(by_date) != len(originals):
        raise ValueError("duplicate source stock/date")
    full = pd.DataFrame(originals)
    for key in ("open", "high", "low", "close", "volume"):
        full[key] = pd.to_numeric(full[key], errors="coerce")
    formal = full.dropna(subset=["open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)
    formal["ma20"] = formal["close"].rolling(20, min_periods=20).mean()
    formal["ema23"] = formal["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    clean = full.dropna(subset=["high", "low", "close", "volume"])
    clean = clean[(clean["high"] > 0) & (clean["low"] > 0) & (clean["volume"] > 0)].sort_values("date").reset_index(drop=True)
    previous_mean = clean["volume"].shift(1).rolling(20, min_periods=20).mean()
    warmup = pd.DataFrame({"a": clean["volume"] / previous_mean,
                           "b": clean["volume"].shift(1) / clean["volume"].shift(2).rolling(20, min_periods=20).mean(),
                           "c": clean["volume"].rolling(5, min_periods=5).mean() / previous_mean,
                           "d": clean["volume"].shift(1).rolling(5, min_periods=5).mean() / previous_mean}).notna().all(axis=1)
    next_open = clean["open"].shift(-1)
    warmup &= (next_open.notna() & (next_open / clean["close"] - 1).notna()) | (clean.index == len(clean) - 1)
    work = clean.loc[warmup].reset_index(drop=True)
    work["ma20"] = work["close"].rolling(20, min_periods=20).mean()
    work["ema23"] = work["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    return clean, work, formal, by_date


def _check_source_rows(ledger: list[dict[str, str]], retained: dict[str, bytes], errors: list[str]) -> None:
    cache = {}
    for row in ledger:
        stock, date = row["stock_id"], row["signal_date"]
        if stock not in cache:
            path = f"data/stock_price_history/{stock}.csv"
            raw = retained[path]
            clean, work, formal, by_date = _source_frames(raw)
            clean[FEATURES[0]] = (clean["close"] > clean["close"].ewm(span=23, adjust=False, min_periods=23).mean()).where(clean["close"].ewm(span=23, adjust=False, min_periods=23).mean().notna())
            ma5 = clean["close"].rolling(5, min_periods=5).mean()
            clean[FEATURES[1]] = (ma5 > ma5.shift(3)).where(ma5.notna() & ma5.shift(3).notna())
            vol_mean = clean["volume"].rolling(20, min_periods=20).mean()
            clean[FEATURES[2]] = (clean["volume"] / vol_mean >= 1.5).where(vol_mean.notna() & vol_mean.gt(0))
            tdcc_raw = retained.get(f"data/tdcc_stock_history/{stock}.csv", b"")
            tdcc = list(csv.DictReader(io.StringIO(tdcc_raw.decode("utf-8-sig")))) if tdcc_raw else []
            tdcc = sorted((r for r in tdcc if r.get("as_of_date", "") <= "20260703"), key=lambda r: r.get("as_of_date", ""))
            cache[stock] = clean.set_index("date"), work, formal, by_date, digest(raw), tdcc, digest(tdcc_raw) if tdcc_raw else ""
        clean, work, formal, by_date, price_sha, tdcc, tdcc_sha = cache[stock]
        label = row["trade_id"]
        if row["price_blob_sha256"] != price_sha or row["signal_row_sha256"] != canonical_row_sha256(by_date[date]):
            errors.append(f"{label}: signal price row/blob binding mismatch")
        if int(row["stock_work_rows"]) != len(work):
            errors.append(f"{label}: stock work-row count mismatch")
        position = int(row["stock_day_position"])
        if position >= len(work) or str(work.iloc[position]["date"]) != date:
            errors.append(f"{label}: stock-day position mismatch")
            continue
        expected_target = work.iloc[max(0, position - 20):position]["high"].max() if position >= 20 else None
        if not same_number(row["target_price"], expected_target):
            errors.append(f"{label}: legacy target prefix mismatch")
        formal_position = formal.index[formal["date"].eq(date)].tolist()[0]
        formal_target = formal.iloc[max(0, formal_position - 20):formal_position]["high"].max() if formal_position else None
        if not same_number(row["formal_target_price"], formal_target):
            errors.append(f"{label}: formal full-history target mismatch")
        for column, frame, start in (("trace_json", work, position), ("formal_adapter_trace_json", formal, formal_position)):
            trace = json.loads(row[column])
            expected = frame.iloc[start + 1:start + 22]
            if len(trace) != len(expected):
                errors.append(f"{label}: {column} forward coverage mismatch")
                continue
            for trace_row, (_, original) in zip(trace, expected.iterrows()):
                trace_date = str(original["date"])
                if trace_row["date"] != trace_date or trace_row["source_row_sha256"] != canonical_row_sha256(by_date[trace_date]):
                    errors.append(f"{label}: {column} date/row-hash mismatch")
                if any(not same_number(trace_row.get(k), original[k]) for k in ("open", "close", "ma20", "ema23")):
                    errors.append(f"{label}: {column} raw prices or independently recomputed MA/EMA mismatch")
        feature_row = clean.loc[date]
        for feature in FEATURES:
            expected_feature = None if pd.isna(feature_row[feature]) else bool(feature_row[feature])
            observed_feature = None if row[feature] == "" else truth(row[feature])
            if observed_feature != expected_feature:
                errors.append(f"{label}: objective feature {feature} mismatch")
        eligible_tdcc = [r for r in tdcc if r.get("as_of_date", "") <= date]
        chosen = eligible_tdcc[-1] if eligible_tdcc else None
        if row["tdcc_blob_sha256"] != tdcc_sha or row["tdcc_as_of_date"] != (chosen.get("as_of_date", "") if chosen else "") or row["tdcc_row_sha256"] != (canonical_row_sha256(chosen) if chosen else ""):
            errors.append(f"{label}: TDCC backward-join row/blob binding mismatch")


def validate(artifact_root: Path, *, repo_root: Path | None = None) -> list[str]:
    errors: list[str] = []
    try:
        manifest = json.loads((artifact_root / (PREFIX + "manifest.json")).read_text(encoding="utf-8-sig"))
        expected_names = {PREFIX + "ledger.csv.gz"} | {PREFIX + name + ".csv" for name in ("pit_coverage", "parity", "summary", "feature_comparison")}
        if set(manifest["output_hashes"]) != expected_names:
            errors.append("manifest must bind exactly the five versioned CSV artifacts")
        for name in expected_names:
            if digest((artifact_root / name).read_bytes()) != manifest["output_hashes"].get(name):
                errors.append(f"artifact SHA mismatch: {name}")
        for key in ("promotion_allowed", "original_1161_ledger_restored", "original_primary_metrics_modified",
                    "original_publication_version_verified", "formal_signal_selector_parity_proven",
                    "formal_model_backtest_parity_or_anomaly_disposition_proven"):
            if manifest.get(key) is not False:
                errors.append(f"unproven manifest claim must remain false: {key}")
        if (manifest.get("source_ref"), manifest.get("semantic_ref"), manifest.get("formal_ref")) != (SOURCE_REF, SEMANTIC_REF, SOURCE_REF):
            errors.append("immutable source/semantic/formal reference mismatch")
        if (manifest.get("signal_start"), manifest.get("signal_end"), manifest.get("data_ceiling")) != ("20251128", "20260602", "20260703"):
            errors.append("fixed signal window/data ceiling mismatch")
        ledger = read_csv(artifact_root / (PREFIX + "ledger.csv.gz"))
        summaries = read_csv(artifact_root / (PREFIX + "summary.csv"))
        comparisons = read_csv(artifact_root / (PREFIX + "feature_comparison.csv"))
        pit = read_csv(artifact_root / (PREFIX + "pit_coverage.csv"))
        parity = read_csv(artifact_root / (PREFIX + "parity.csv"))
        required = {"rule_variant", "trade_id", "signal_id", "stock_id", "signal_date", "stock_day_position", "stock_work_rows",
                    "new_global_index", "gate_eligible", "accepted_trade", "mature", "primary_included", "trace_json",
                    "formal_adapter_trace_json", "formal_adapter_result_json", "formal_target_price", "fullselectorparity_not_proven", *FEATURES}
        if not ledger or not required.issubset(ledger[0]):
            return errors + ["ledger empty or required independent replay inputs missing"]
        ids = set(); pairs = {}
        for row in ledger:
            label = row["trade_id"]
            if label in ids:
                errors.append(f"duplicate trade identity: {label}")
            ids.add(label)
            key = row["stock_id"], row["signal_date"]
            pairs.setdefault(key, set()).add(row["rule_variant"])
            if row["rule_variant"] not in VARIANTS:
                errors.append(f"{label}: unknown rule variant")
                continue
            if not "20251128" <= row["signal_date"] <= "20260602":
                errors.append(f"{label}: signal outside fixed window")
            if not truth(row["fullselectorparity_not_proven"]) or row["formal_position_status"] != "not_formal_position" or not truth(row["pre_effective_from"]):
                errors.append(f"{label}: counterfactual formal/selector claim inflated")
            if row["pit_status"] != "unknown_original_publication" or row["publication_available_at"]:
                errors.append(f"{label}: unverified first-publication PIT claim")
            trace = json.loads(row["trace_json"])
            if any(t["date"] > "20260703" for t in trace):
                errors.append(f"{label}: trace exceeds data ceiling")
            replay = replay_legacy(trace, row["entry_price"], row["target_price"], row["rule_variant"])
            left = not truth(row["gate_eligible"]) and row["selector_status"] == "unknown_left_censored"
            if left:
                if truth(row["accepted_trade"]) or truth(row["mature"]) or number(row["realized_return_pct"]) is not None or row["exit_reason"] != "left_censored":
                    errors.append(f"{label}: left-censored row acquires a position or realized return")
            elif truth(row["mature"]) != replay["mature"]:
                errors.append(f"{label}: maturity mismatch")
            if replay["mature"] and not left:
                for field in ("target_day", "stop_day", "realized_days", "exit_price", "realized_return_pct", "d20_close"):
                    if not same_number(row.get(field), replay[field]):
                        errors.append(f"{label}: independent numeric {field} mismatch")
                for field in ("exit_reason", "exit_date", "outcome_bucket", "d20_date"):
                    if row.get(field) != replay[field]:
                        errors.append(f"{label}: independent lifecycle {field} mismatch")
            elif number(row["realized_return_pct"]) is not None:
                errors.append(f"{label}: censored row has realized return")
            expected_primary = truth(row["accepted_trade"]) and truth(row["mature"])
            if truth(row["primary_included"]) != expected_primary:
                errors.append(f"{label}: primary excludes/admits row outside accepted mature basis")
            formal_trace = json.loads(row["formal_adapter_trace_json"])
            formal_entry = formal_trace[0]["open"] if formal_trace else None
            formal_expected = replay_formal(formal_trace, formal_entry, row["formal_target_price"])
            formal_actual = json.loads(row["formal_adapter_result_json"])
            # The diagnostic labels an incomplete no-event tape right-censored;
            # it does not claim a buy-ranked formal active position.
            actual_state = formal_actual.get("state")
            if actual_state == "right_censored":
                actual_state = "active_operation"
            if actual_state != formal_expected["state"] or formal_actual.get("exit_date", "") != formal_expected.get("exit_date", ""):
                errors.append(f"{label}: formal hypothetical numeric lifecycle mismatch")
            expected_reason = formal_expected.get("exit_reason", "")
            if formal_actual.get("exit_reason", "") != expected_reason:
                errors.append(f"{label}: formal hypothetical event priority mismatch")
        if any(variants != set(VARIANTS) for variants in pairs.values()) or len(ledger) != 2 * len(pairs):
            errors.append("paired rule variants do not share exact stock/signal cohort")
        lifecycle = expected_lifecycle(ledger)
        for row in ledger:
            expected = lifecycle[row["trade_id"]]
            if truth(row["accepted_trade"]) != expected["accepted_trade"] or row["suppressed_by_trade_id"] != expected["suppressed_by_trade_id"]:
                errors.append(f"{row['trade_id']}: same-stock accepted/suppression lineage mismatch")
            if int(row["exit_stock_day_position"]) != expected["exit_stock_day_position"]:
                errors.append(f"{row['trade_id']}: lifecycle exit position mismatch")
        summary_keys = {(r["rule_variant"], r["basis"]) for r in summaries}
        if len(summaries) != 4 or summary_keys != {(v, b) for v in VARIANTS for b in BASES}:
            errors.append("summary primary/sensitivity groups incomplete or duplicated")
        comparison_keys = set()
        for variant in VARIANTS:
            variant_rows = [r for r in ledger if r["rule_variant"] == variant]
            primary = [r for r in variant_rows if truth(r["accepted_trade"]) and truth(r["mature"])]
            for basis in BASES:
                rows = primary if basis == BASES[0] else [r for r in primary if r["anomaly_status"] != "unresolved_anomaly_candidate"]
                stat = metrics(rows)
                observed = next((r for r in summaries if (r["rule_variant"], r["basis"]) == (variant, basis)), {})
                _check_metrics(stat, observed, f"summary/{variant}/{basis}", errors)
                status_counts = {"eligible_signal_count": sum(truth(r["gate_eligible"]) for r in variant_rows),
                                 "suppressed_signal_count": sum(r["lifecycle_status"] == "suppressed_active_position" for r in variant_rows),
                                 "immature_signal_count": sum(truth(r["gate_eligible"]) and not truth(r["mature"]) for r in variant_rows),
                                 "left_censored_count": sum(r["lifecycle_status"] == "left_censored" for r in variant_rows)}
                _check_metrics(status_counts, observed, f"summary_status/{variant}/{basis}", errors)
                for flag in ("promotion_allowed", "original_1161_ledger_restored"):
                    if truth(observed.get(flag)):
                        errors.append(f"summary/{variant}/{basis}: inflated {flag}")
                cut = stat["high_return_threshold_pct"]
                groups = {"high_return_upper_quartile": [r for r in rows if number(r["realized_return_pct"]) is not None and cut is not None and float(r["realized_return_pct"]) >= cut],
                          "negative_return": [r for r in rows if number(r["realized_return_pct"]) is not None and float(r["realized_return_pct"]) < 0],
                          "matched_single_feature": rows}
                for group, cohort in groups.items():
                    for feature in FEATURES:
                        key = variant, basis, group, feature
                        comparison_keys.add(key)
                        observed = next((r for r in comparisons if (r["rule_variant"], r["basis"], r["group"], r["feature"]) == key), {})
                        selected = [r for r in cohort if truth(r[feature])]
                        known = sum(r[feature] != "" for r in cohort)
                        expected_metrics = metrics(selected if group == "matched_single_feature" else cohort, high_cut=cut)
                        expected_metrics.update(cohort_n=len(cohort), known_n=known, unknown_n=len(cohort) - known,
                                                feature_true_pct_of_known=100 * len(selected) / known if known else None)
                        _check_metrics(expected_metrics, observed, f"features/{key}", errors)
                        if observed.get("buy_sell_holding_basis") != "same_accepted_trade_cohort_no_signal_reselection":
                            errors.append(f"features/{key}: comparison changes buy/sell/holding cohort")
        if len(comparisons) != 36 or {(r["rule_variant"], r["basis"], r["group"], r["feature"]) for r in comparisons} != comparison_keys:
            errors.append("paired three-feature comparison groups incomplete or duplicated")
        if any(r.get("pit_status") != "unknown_original_publication" or truth(r.get("promotion_allowed")) for r in pit):
            errors.append("PIT coverage inflates unknown-publication source into promotion evidence")
        if any(r.get("status") not in {"different", "not_proven"} for r in parity):
            errors.append("formal parity claims exceed independently checked numeric lifecycle scope")
        if repo_root is not None:
            retained = _git_sources(repo_root, manifest, ledger, errors)
            if retained:
                _check_source_rows(ledger, retained, errors)
    except (OSError, ValueError, KeyError, TypeError, IndexError, subprocess.CalledProcessError) as exc:
        errors.append(f"cannot validate versioned replay inputs: {type(exc).__name__}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="獨立檢查23EMA版本化研究的數值與lifecycle；不證明selector或PIT。")
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path)
    args = parser.parse_args()
    errors = validate(args.artifact_root, repo_root=args.repo_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    git_status = "Git source blobs已核對" if args.repo_root else "Git source blobs未執行核對"
    print(f"23EMA版本化研究數值/lifecycle檢查通過；{git_status}；selector/PIT/promotion仍未證明。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
