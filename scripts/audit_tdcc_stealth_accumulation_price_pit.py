from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import io
import json
import subprocess
from collections import Counter
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from model_research_artifact_guard import load_ownership_rules, model_owned_artifact_guard, validate_changed_paths

ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
MODEL_NAME_ZH = "TDCC 潛伏吸籌"
OWNER_ID = "tdcc_stealth_accumulation_price_pit_audit"
PRODUCER = "scripts/audit_tdcc_stealth_accumulation_price_pit.py"
CONFIG = "config/tdcc_stealth_accumulation_price_pit_evidence_v1.json"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
STEM = "tdcc_stealth_accumulation_price_pit_audit_v1"
V2_STEM = "tdcc_stealth_accumulation_historical_selector_field_contract_replay"
ARTIFACT_COMMIT = "dde3ce9e39bc344297581223c6d2f10c802dc46c"
SOURCE_COMMIT = "7ef37a966280201a5ee236856306fdb513de7092"
TAIPEI = timezone(timedelta(hours=8))
CONTRACT = "config/daily_model_numerical_anomaly_disposition_contract.csv"
SOURCE_CANDIDATES = {
    "pattern": "output/latest/daily_pattern_watch_latest.csv",
    "revenue_pullback": "output/latest/revenue_pullback_latest.csv",
    "revenue_breakout_low_response": "output/latest/revenue_breakout_low_response_latest.csv",
}
FIELDS = [
    "observation_id", "model_id", "model_name_zh", "stock_id", "stock_name",
    "signal_date", "snapshot_date", "snapshot_row_number", "category", "horizon",
    "entry_date", "entry_open", "exit_date", "exit_close", "gross_return_pct",
    "same_stock_signal_rows", "same_stock_signal_categories", "snapshot_generated_at",
    "pipeline_commit_time", "generated_after_entry_open", "pipeline_after_entry_open",
    "enum_source_branch", "enum_window_dates", "selector_input_differences",
    "source_sequence_rows", "missing_stock_dates", "missing_weekdays",
    "disposition", "retained_in_primary", "formal_use", "trade_eligible",
    "promotion_evidence_allowed",
]


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def snapshot_digest_audit(payload: bytes, recorded: str) -> dict:
    lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    hashes = {"raw_git_bytes": sha(payload), "lf": sha(lf), "crlf": sha(lf.replace(b"\n", b"\r\n"))}
    matches = [basis for basis, value in hashes.items() if value == recorded]
    if not matches:
        raise RuntimeError("v2 snapshot digest does not match any declared line-ending basis")
    return {"recorded_v2_snapshot_sha256": recorded, "sha256_by_basis": hashes,
            "matching_bases": matches, "raw_bytes_match": recorded == hashes["raw_git_bytes"],
            "interpretation": "legacy_manifest_digest_accepts_raw_LF_CRLF_raw_Git_manifest_remains_exact"}


def clean(value: object) -> str:
    value = str(value or "").replace("\ufeff", "").strip()
    return "" if value.lower() in {"nan", "none", "nat", "<na>"} else value


def csv_rows(payload: bytes) -> list[dict[str, str]]:
    return [{str(k): clean(v) for k, v in row.items()} for row in csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))) ]


def timestamp(value: str) -> datetime:
    if value.endswith(" Asia/Taipei"):
        return datetime.strptime(value[:-12], "%Y-%m-%d %H:%M:%S").replace(tzinfo=TAIPEI)
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(TAIPEI)


def market_time(date: str, hour: int, minute: int = 0) -> datetime:
    return datetime.strptime(date, "%Y%m%d").replace(hour=hour, minute=minute, tzinfo=TAIPEI)


class Sources:
    """Read immutable Git objects; never materialize shared data roots."""

    def __init__(self, root: Path):
        self.root = root
        self.manifest: dict[str, dict] = {}
        self.cache: dict[str, bytes] = {}

    def git(self, *args: str) -> bytes:
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True).stdout

    def read(self, commit: str, path: str) -> bytes:
        key = f"{commit}:{path}"
        if key not in self.cache:
            value = self.git("show", key)
            self.cache[key] = value
            self.manifest[key] = {
                "commit": commit, "path": path, "sha256": sha(value), "bytes": len(value),
                "git_blob_oid": self.git("rev-parse", key).decode().strip(),
                "url": f"https://github.com/LeoChen0727/tdcc-weekly-report/blob/{commit}/{path}",
            }
        return self.cache[key]

    def rows(self, commit: str, path: str) -> list[dict[str, str]]:
        return csv_rows(self.read(commit, path))

    def row(self, commit: str, path: str, number: int) -> dict:
        rows = self.rows(commit, path)
        value = rows[number - 2]
        return {"source": f"{commit}:{path}", "row_number": number, "row": value, "row_sha256": sha(canonical_bytes(value))}

    def matching(self, commit: str, path: str, **identity: str) -> list[dict]:
        return [self.row(commit, path, i) for i, row in enumerate(self.rows(commit, path), 2)
                if all(row.get(k) == v for k, v in identity.items())]

    def commit_time(self, commit: str) -> str:
        return self.git("show", "-s", "--format=%cI", commit).decode().strip()

    def functions(self, commit: str, path: str, names: list[str]) -> list[dict]:
        text = self.read(commit, path).decode("utf-8-sig")
        tree = ast.parse(text)
        found = [{"source": f"{commit}:{path}", "name": node.name, "line": node.lineno,
                 "end_line": node.end_lineno, "function_sha256": sha(ast.get_source_segment(text, node).encode())}
                for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names]
        missing = set(names) - {item["name"] for item in found}
        if missing:
            raise RuntimeError(f"required producer functions missing: {path}: {sorted(missing)}")
        return found


def selector_inputs(source: Sources) -> set[str]:
    text = source.read(ARTIFACT_COMMIT, "scripts/build_tdcc_stealth_accumulation_historical_replay.py").decode()
    for node in ast.parse(text).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "SELECTOR_INPUT_NAMES" for t in node.targets):
            return {name + suffix for name in ast.literal_eval(node.value) for suffix in ("", "_x", "_y")}
    raise RuntimeError("missing pinned selector input inventory")


def population_profile(rows: list[dict]) -> dict:
    count: Counter = Counter()
    dates = set()
    for row in rows:
        generated = timestamp(row["snapshot_generated_at"])
        signal = row["candidate_signal_date"]
        if generated.date() > market_time(signal, 13, 30).date():
            count["generated_calendar_date_after_signal_date"] += 1
            dates.add(row["snapshot_report_date"])
        count["generated_after_signal_close"] += generated > market_time(signal, 13, 30)
        entry = row["entry_date"]
        if not entry:
            count["no_entry_date"] += 1
            continue
        opening = market_time(entry, 9)
        count["with_entry_date"] += 1
        count["generated_after_entry_open"] += generated > opening
        relation = "before" if generated.date() < opening.date() else "after" if generated.date() > opening.date() else "on"
        count[f"generated_calendar_date_{relation}_entry_date"] += 1
    identities = Counter((r['snapshot_path'], r['snapshot_row_number']) for r in rows)
    stock_dates = Counter((r['stock_id'], r['candidate_signal_date']) for r in rows)
    return {"signal_rows": len(rows), "unique_stocks": len({r['stock_id'] for r in rows}),
            "unique_stock_signal_dates": len(stock_dates),
            "same_stock_signal_duplicate_groups": sum(n > 1 for n in stock_dates.values()),
            "duplicate_group_rows": sum(n for n in stock_dates.values() if n > 1),
            "excess_stock_signal_rows": len(rows) - len(stock_dates),
            "snapshot_identity_duplicate_groups": sum(n > 1 for n in identities.values()),
            "snapshot_dates_with_generated_calendar_date_after_signal": len(dates),
            **dict(count), "interpretation": "metadata_temporal_comparison_not_event_time_PIT_or_trade_eligibility_verdict"}


def enum_lineage(source: Sources, pipeline: str, snapshot: dict) -> dict:
    row = snapshot["row"]
    stock = row["stock_id"]
    category = row["category"]
    candidate_path = SOURCE_CANDIDATES[category]
    candidates = source.matching(pipeline, candidate_path, stock_id=stock)
    exact_date = [r for r in candidates if r["row"].get("date") == row.get("date")]
    if exact_date:
        candidates = exact_date
    if len(candidates) != 1:
        raise RuntimeError(f"ambiguous upstream candidate {stock} {category}: {len(candidates)}")
    candidate = candidates[0]
    trend_rows = source.matching(pipeline, "output/latest/tdcc_trend_debug_latest.csv", stock_id=stock)
    if len(trend_rows) != 1:
        raise RuntimeError(f"ambiguous trend row {stock}")
    trend = trend_rows[0]
    inherited = bool(candidate["row"].get("tdcc_accumulation_signal"))
    chosen = candidate if inherited else trend
    if chosen["row"]["tdcc_accumulation_signal"] != row["tdcc_accumulation_signal"]:
        raise RuntimeError(f"enum lineage mismatch {stock}")
    funcs = source.functions(pipeline, "build_all_candidates_latest.py", ["merge_tdcc", "merge_without_duplicate_columns", "infer_tdcc_signal_from_numbers", "deduplicate_candidates"])
    result = {"branch": "existing_candidate_enum_preserved" if inherited else "blank_candidate_enum_filled_from_trend_debug",
              "candidate_source_row": candidate, "trend_debug_row": trend,
              "selected_source": chosen["source"], "selected_enum": chosen["row"]["tdcc_accumulation_signal"],
              "snapshot_tdcc_date": row.get("tdcc_date", ""),
              "enum_window_dates": trend["row"].get("tdcc_history_dates", "") if not inherited else "",
              "producer_functions": funcs,
              "event_time_availability": "unproven_original_input_filed_at_not_present",
              "runtime_invocation_evidence": "not_recorded",
              "interpretation": "reproducible_value_propagation_under_commit_code_not_runtime_attestation"}
    if inherited:
        result["producer_functions"] += source.functions(pipeline, "build_revenue_breakout_low_response.py", ["build_revenue_breakout_low_response_candidates"])
        result["producer_functions"] += source.functions(pipeline, "tdcc_trend_utils.py", ["load_tdcc_history_trend", "classify_accumulation"])
        paths = source.git("ls-tree", "-r", "--name-only", pipeline, "output/history/tdcc").decode().splitlines()
        history_paths = sorted(p for p in paths if Path(p).name.startswith("tdcc_holder_ratio_") and p.endswith(".csv"))[-4:]
        history = []
        missing_dates = []
        for path in history_paths:
            matches = source.matching(pipeline, path, code=stock)
            if len(matches) == 1:
                history.extend(matches)
            elif not matches:
                missing_dates.append(Path(path).stem[-8:])
            else:
                raise RuntimeError("ambiguous TDCC history identity")
        changes = {}
        for metric in ("400", "1000"):
            values = [Decimal(item["row"][f"over_{metric}_pct"]) for item in history]
            changes[f"tdcc_{metric}_change_sum"] = str(values[-1] - values[0])
            changes[f"tdcc_{metric}_up_weeks"] = sum(b > a for a, b in zip(values, values[1:]))
            if Decimal(candidate["row"][f"tdcc_{metric}_change_sum"]) != values[-1] - values[0]:
                raise RuntimeError("candidate TDCC history delta mismatch")
        result.update({"history_rows": history, "selected_history_paths": history_paths,
                       "missing_history_dates": missing_dates, "history_recomputed_metrics": changes,
                       "enum_window_dates": ",".join(item["row"]["date"] for item in history)})
    else:
        result["producer_functions"] += source.functions(pipeline, "tdcc_trend_utils.py", ["classify_accumulation"])
    return result


def price_sequence(source: Sources, stock: str, signal: str, entry: str, exit_date: str, horizon: int) -> dict:
    paths = source.git("ls-tree", "-r", "--name-only", SOURCE_COMMIT, "data/daily_price").decode().splitlines()
    dated = {Path(path).stem: path for path in paths if Path(path).stem.isdigit() and signal <= Path(path).stem <= exit_date}
    rows = []
    missing = []
    for date, path in sorted(dated.items()):
        matches = source.matching(SOURCE_COMMIT, path, stock_id=stock)
        if len(matches) > 1:
            raise RuntimeError(f"duplicate price identity {stock} {date}")
        if matches:
            rows.append(matches[0])
        else:
            missing.append(date)
    valid = [r for r in rows if r["row"].get("open") and r["row"].get("close")
             and Decimal(r["row"]["open"]) > 0 and Decimal(r["row"]["close"]) > 0]
    window = [r for r in valid if entry <= r["row"]["date"] <= exit_date]
    absent_weekdays = []
    day = market_time(signal, 0)
    while day <= market_time(exit_date, 0):
        date = day.strftime("%Y%m%d")
        if day.weekday() < 5 and date not in dated:
            absent_weekdays.append(date)
        day += timedelta(days=1)
    exceptions = source.rows(SOURCE_COMMIT, "data/market_calendar/exceptional_non_trading_days.csv")
    matched_exceptions = [r for r in exceptions if r["date"] in absent_weekdays]
    scheduled = source.rows(SOURCE_COMMIT, "config/twse_non_trading_days.csv")
    matched_scheduled = [r for r in scheduled if r["date"] in absent_weekdays]
    registered = {r["date"] for r in matched_exceptions + matched_scheduled}
    return {"raw_rows": rows, "source_dates": sorted(dated), "missing_stock_dates": missing,
            "missing_weekdays": absent_weekdays, "repo_exceptional_calendar_rows": matched_exceptions,
            "repo_scheduled_calendar_rows": matched_scheduled,
            "unexplained_missing_weekdays": [date for date in absent_weekdays if date not in registered],
            "source_window_rows": len(window), "source_window_matches_horizon": len(window) == horizon + 1,
            "source_date_presence_is_official_calendar_proof": False,
            "official_suspension_resumption_history_complete": False}


def build(root: Path = ROOT) -> dict:
    settings = json.loads((root / CONFIG).read_text(encoding="utf-8"))
    if settings["artifact_commit"] != ARTIFACT_COMMIT or settings["replay_source_commit"] != SOURCE_COMMIT:
        raise RuntimeError("audit must use explicitly pinned v2 and replay sources")
    source = Sources(root)
    artifact_manifest = []
    for suffix, extension in (("detail", "csv"), ("summary", "csv"), ("report", "md")):
        path = f"{DIRECTORY}/{V2_STEM}_{suffix}_v2.{extension}"
        payload = source.read(ARTIFACT_COMMIT, path)
        if sha(payload) != settings["v2_sha256"][suffix]:
            raise RuntimeError(f"pinned v2 {suffix} artifact SHA-256 mismatch")
        artifact_manifest.append(source.manifest[f"{ARTIFACT_COMMIT}:{path}"])
    detail_path = artifact_manifest[0]["path"]
    detail = source.rows(ARTIFACT_COMMIT, detail_path)
    summary = source.rows(ARTIFACT_COMMIT, artifact_manifest[1]["path"])
    original_rows = list(csv.DictReader(io.StringIO(source.read(ARTIFACT_COMMIT, detail_path).decode("utf-8-sig"))))
    before_observations = [{**r, "large_return_observation_codes": "", "large_return_spotcheck_status": ""} for r in original_rows]
    reconstruction = io.StringIO(newline="")
    reconstruction_writer = csv.DictWriter(reconstruction, fieldnames=list(original_rows[0]), lineterminator="\n")
    reconstruction_writer.writeheader()
    reconstruction_writer.writerows(before_observations)
    embedded = sorted({r["detail_artifact_sha256"] for r in summary})
    reconstructed_sha = sha(reconstruction.getvalue().encode("utf-8"))
    digest_audit = {"actual_detail_sha256": artifact_manifest[0]["sha256"],
                    "summary_embedded_detail_sha256": embedded,
                    "embedded_hash_mismatch": embedded != [artifact_manifest[0]["sha256"]],
                    "pre_observation_annotation_reconstruction_sha256": reconstructed_sha,
                    "pre_observation_reconstruction_matches_embedded": embedded == [reconstructed_sha],
                    "annotation_rows": sum(bool(r["large_return_observation_codes"] or r["large_return_spotcheck_status"]) for r in original_rows),
                    "interpretation": "v2_wrapper_annotations_added_after_base_detail_digest_not_price_or_return_error",
                    "old_artifact_modified": False}
    source.functions(ARTIFACT_COMMIT, "scripts/build_tdcc_stealth_accumulation_field_contract_replay.py", ["build"])
    source.functions(ARTIFACT_COMMIT, "scripts/build_tdcc_stealth_accumulation_historical_replay.py", ["build"])
    digest_contract = source.functions(ARTIFACT_COMMIT, "scripts/build_tdcc_stealth_accumulation_historical_replay.py", ["_hash_candidates"])
    historical_backfill = source.functions("e44cd24a89b25121bf0cedb23137f0716f36d411", "scripts/backfill_historical_all_candidates_snapshots_from_git_history.py", ["find_all_candidates_blob_for_date"])
    debug_origin = "13848a4a401246a57618e29c458e8034c0a5534a"
    source.read(debug_origin, "output/latest/tdcc_trend_debug_latest.csv")
    source.read(SOURCE_COMMIT, "fetch_official_daily_price.py")
    inputs = selector_inputs(source)
    contract = source.rows(settings["code_baseline_commit"], CONTRACT)
    checks = next(r for r in contract if r["disposition_id"] == "unresolved_anomaly_candidate")["required_root_checks"].split(";")
    observations = []
    for target in settings["observations"]:
        candidates = [(i, r) for i, r in enumerate(detail, 2) if r["stock_id"] == target["stock_id"] and target["code"] in r["large_return_observation_codes"].split(";")]
        if len(candidates) != 1:
            raise RuntimeError(f"observation identity not unique: {target}")
        number, replay = candidates[0]
        snapshot = source.row(SOURCE_COMMIT, replay["snapshot_path"], int(replay["snapshot_row_number"]))
        snapshot_digest = snapshot_digest_audit(source.read(SOURCE_COMMIT, replay["snapshot_path"]), replay["snapshot_sha256"])
        if snapshot["row_sha256"] != replay["snapshot_row_sha256"]:
            raise RuntimeError("pinned snapshot row hash mismatch")
        pipeline = replay["snapshot_pipeline_commit_sha"]
        snapshot_value = snapshot["row"]
        matches = source.matching(pipeline, "output/latest/all_candidates_latest.csv", **{k: snapshot_value[k] for k in ("stock_id", "date", "category")})
        if len(matches) != 1:
            raise RuntimeError("pipeline candidate composite identity is ambiguous")
        pipeline_row = matches[0]
        common = set(snapshot_value) & set(pipeline_row["row"])
        differences = {k: [pipeline_row["row"][k], snapshot_value[k]] for k in sorted(common) if pipeline_row["row"][k] != snapshot_value[k]}
        input_differences = {k: [pipeline_row["row"].get(k, ""), snapshot_value.get(k, "")] for k in sorted(inputs) if pipeline_row["row"].get(k, "") != snapshot_value.get(k, "")}
        h = target["horizon"]
        endpoints = []
        for prefix in ("entry", f"exit_d{h}"):
            path = replay[f"{prefix}_price_source_path"]
            match = source.matching(SOURCE_COMMIT, path, stock_id=replay["stock_id"])
            if len(match) != 1 or match[0]["row_sha256"] != replay[f"{prefix}_price_row_sha256"]:
                raise RuntimeError("price endpoint row/hash mismatch")
            if source.manifest[match[0]["source"]]["sha256"] != replay[f"{prefix}_price_source_sha256"]:
                raise RuntimeError("price endpoint file hash mismatch")
            endpoints.append(match[0])
        computed = ((Decimal(endpoints[1]["row"]["close"]) / Decimal(endpoints[0]["row"]["open"]) - 1) * 100).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
        if computed != Decimal(replay[f"return_d{h}_pct"]):
            raise RuntimeError("gross return formula mismatch")
        same_signal = [r for r in detail if r["stock_id"] == replay["stock_id"] and r["candidate_signal_date"] == replay["candidate_signal_date"]]
        signal_identities = [{k: r[k] for k in ("snapshot_path", "snapshot_row_number", "snapshot_row_sha256")} for r in same_signal]
        same_categories = [source.row(SOURCE_COMMIT, r["snapshot_path"], int(r["snapshot_row_number"]))["row"]["category"] for r in same_signal]
        generated = timestamp(replay["snapshot_generated_at"])
        commit_time = source.commit_time(pipeline)
        opening = market_time(replay["entry_date"], 9)
        sequence = price_sequence(source, replay["stock_id"], replay["candidate_signal_date"], replay["entry_date"], replay[f"exit_d{h}_date"], h)
        lineage = enum_lineage(source, pipeline, snapshot)
        matching_commit = settings["matching_candidate_commits"][replay["stock_id"]]
        earlier = source.matching(matching_commit, "output/latest/all_candidates_latest.csv", **{k: snapshot_value[k] for k in ("stock_id", "date", "category")})
        if len(earlier) != 1 or any(earlier[0]["row"].get(k, "") != snapshot_value.get(k, "") for k in inputs):
            raise RuntimeError("historical candidate does not match pinned selector inputs")
        matching_time = source.commit_time(matching_commit)
        record = {
            "observation_id": target["code"], "model_id": MODEL_ID, "model_name_zh": MODEL_NAME_ZH,
            "stock_id": replay["stock_id"], "stock_name": replay["stock_name"],
            "signal_date": replay["candidate_signal_date"], "snapshot_date": replay["snapshot_report_date"],
            "snapshot_row_number": replay["snapshot_row_number"], "category": snapshot_value["category"], "horizon": h,
            "entry_date": replay["entry_date"], "entry_open": endpoints[0]["row"]["open"],
            "exit_date": replay[f"exit_d{h}_date"], "exit_close": endpoints[1]["row"]["close"],
            "gross_return_pct": str(computed), "same_stock_signal_rows": len(same_signal),
            "same_stock_signal_categories": ";".join(same_categories),
            "snapshot_generated_at": replay["snapshot_generated_at"], "pipeline_commit_time": commit_time,
            "generated_after_entry_open": generated > opening, "pipeline_after_entry_open": timestamp(commit_time) > opening,
            "enum_source_branch": lineage["branch"], "enum_window_dates": lineage["enum_window_dates"],
            "selector_input_differences": len(input_differences),
            "source_sequence_rows": sequence["source_window_rows"],
            "missing_stock_dates": ";".join(sequence["missing_stock_dates"]),
            "missing_weekdays": ";".join(sequence["missing_weekdays"]),
            "disposition": "unresolved_anomaly_candidate", "retained_in_primary": True,
            "formal_use": False, "trade_eligible": False, "promotion_evidence_allowed": False,
            "v2_detail": source.row(ARTIFACT_COMMIT, detail_path, number), "snapshot_row": snapshot,
            "snapshot_digest_audit": snapshot_digest,
            "pipeline_candidate_row": pipeline_row, "pipeline_common_field_differences": differences,
            "pipeline_selector_input_differences": input_differences,
            "same_stock_signal_identities": signal_identities, "price_endpoints": endpoints,
            "price_sequence": sequence, "enum_lineage": lineage,
            "pit": {"signal_close": market_time(replay["candidate_signal_date"], 13, 30).isoformat(),
                    "research_entry_open": opening.isoformat(), "generated_after_signal_close": generated > market_time(replay["candidate_signal_date"], 13, 30),
                    "original_publication_time_proven": False,
                    "metadata_is_first_publication_or_input_filed_at": False,
                    "earlier_selector_evidence": earlier[0], "matching_commit_time": matching_time,
                    "matching_before_entry_open": timestamp(matching_time) < opening,
                    "matching_search_scope": settings["matching_candidate_search_limit_zh"]},
            "checks": [{"check": name, "status": "verified_commit_row_lineage" if name in {"raw_source_lineage_and_hash", "reproducible_evidence_reference"} else "partial" if name != "formal_operation_replay" else "not_established_user_decision_pending"} for name in checks],
        }
        observations.append(record)
    return {
        "schema_version": "tdcc_stealth_accumulation_price_pit_audit_v1",
        "model_id": MODEL_ID, "model_name_zh": MODEL_NAME_ZH,
        "code_baseline_commit": settings["code_baseline_commit"], "artifact_commit": ARTIFACT_COMMIT,
        "replay_source_commit": SOURCE_COMMIT, "evidence_as_of_date": settings["evidence_as_of_date"],
        "configuration_sha256": sha((root / CONFIG).read_bytes()),
        "snapshot_digest_contract_functions": digest_contract,
        "primary_metric_basis": "signal_row_weighted_not_independent_positions_or_tradable_strategy",
        "v2_artifact_manifest": artifact_manifest, "v2_embedded_digest_audit": digest_audit,
        "snapshot_backfill_function_evidence": historical_backfill,
        "debug_existing_commit": debug_origin, "debug_existing_commit_time": source.commit_time(debug_origin),
        "population": population_profile(detail),
        "observations": observations, "external_evidence": settings["external_evidence"],
        "source_manifest": source.manifest,
        "formal_operation_replay": "not_established_entry_exit_cost_same_stock_overlap_rules_require_user_decision",
        "formal_use": False, "trade_eligible": False, "promotion_evidence_allowed": False,
        "primary_replay_modified": False, "corrected_performance_published": False,
    }


def render_report(audit: dict) -> str:
    p = audit["population"]
    lines = [f"# {MODEL_NAME_ZH}（`{MODEL_ID}`）價格異常與 PIT 查證", "",
             "六筆 observation 的 repo 原始價格、列雜湊與 gross return 算式可核對；PIT、調整基礎與正式操作回放尚未成立，因此六筆仍為 `unresolved_anomaly_candidate`，全部留在既有主結果。這份稽核不發布修正績效。", "",
             f"code baseline：`{audit['code_baseline_commit']}`；v2 artifact：`{ARTIFACT_COMMIT}`；replay source：`{SOURCE_COMMIT}`。", "",
             "## 資料與時間口徑", "",
             f"v2 母體為 {p['signal_rows']} signal rows、{p['unique_stocks']} 股票；按訊號列加權，不代表獨立交易、可執行部位或投組策略。", "",
             f"唯一 stock+signal_date 為 {p['unique_stock_signal_dates']}；同股同日多來源 groups={p['same_stock_signal_duplicate_groups']}，涵蓋 {p['duplicate_group_rows']} 列，多於一列部分共 {p['excess_stock_signal_rows']} 列。snapshot path+row number 重複 groups={p['snapshot_identity_duplicate_groups']}。多 category 訊號與持倉窗重疊是不同問題，本次不去重或重算主績效。", "",
             f"snapshot generated_at 的日曆日期晚於 signal date：{p.get('generated_calendar_date_after_signal_date', 0)} 列／{p['snapshot_dates_with_generated_calendar_date_after_signal']} snapshot 日期；晚於 signal close：{p.get('generated_after_signal_close', 0)} 列。", "",
             f"有 entry date 的 {p['with_entry_date']} 列中，generated_at 晚於 entry open：{p.get('generated_after_entry_open', 0)} 列；日曆日 before/on/after entry date 分別 {p.get('generated_calendar_date_before_entry_date', 0)}/{p.get('generated_calendar_date_on_entry_date', 0)}/{p.get('generated_calendar_date_after_entry_date', 0)} 列；無 entry date：{p['no_entry_date']} 列。以上僅為 metadata 時間比較，不能直接認定前視偏誤或資料錯誤。", "",
             "## 六筆價格與根因狀態", "",
             "|股票|signal|entry open|exit close|窗|gross return|enum 來源資料窗|disposition|",
             "|---|---|---|---|---|---:|---|---|"]
    for r in audit["observations"]:
        lines.append(f"|{r['stock_id']} {r['stock_name']}|{r['signal_date']}|{r['entry_date']} / {r['entry_open']}|{r['exit_date']} / {r['exit_close']}|D{r['horizon']}|{r['gross_return_pct']}%|{r['enum_window_dates'] or 'candidate producer 原始窗待核對'}|{r['disposition']}|")
    lines += ["", "gross return = (exit close / entry open − 1) × 100；不含手續費、交易稅、滑價或現金股利。價格來源欄位是 repo 的來源標籤，並不等於本次取得獨立官方回應。數字大小只能觸發調查。", ""]
    for r in audit["observations"]:
        lines += [f"## {r['stock_id']} {r['stock_name']}：`{r['observation_id']}`", "",
                  f"identity：snapshot `{r['snapshot_date']}` row `{r['snapshot_row_number']}`、category=`{r['category']}`；同股同 signal date 有 {r['same_stock_signal_rows']} 列，categories=`{r['same_stock_signal_categories']}`。重複訊號不等於 byte duplicate，也未依持倉窗去重。", "",
                  f"generated_at=`{r['snapshot_generated_at']}`；pipeline commit time=`{r['pipeline_commit_time']}`；相對 entry open，generated_after={r['generated_after_entry_open']}、pipeline_after={r['pipeline_after_entry_open']}。commit time 證明該 commit 的時間，不能代替第一次發布或原始輸入 filed-at。", "",
                  f"有界查得相同 selector inputs 的歷史 candidate commit：`{r['pit']['earlier_selector_evidence']['source'].split(':')[0]}`，time=`{r['pit']['matching_commit_time']}`，早於 entry open=`{r['pit']['matching_before_entry_open']}`。這能核對 repository 中該版輸入的存在時間，但不是完整官方 filed-at 證明。", "",
                  f"snapshot 與 pipeline candidate 的 selector input 差異 {r['selector_input_differences']}；其他共同欄位差異：`{','.join(r['pipeline_common_field_differences']) or 'none'}`。enum 分支=`{r['enum_source_branch']}`；candidate 顯示的 tdcc_date=`{r['enum_lineage']['snapshot_tdcc_date']}`，不可直接當作 enum 的來源窗。", "",
                  f"entry 至 exit 的 source sequence {r['source_sequence_rows']} 列（含 entry）；個股缺列日期=`{r['missing_stock_dates'] or 'none'}`；repo 無日期檔的平日=`{r['missing_weekdays'] or 'none'}`，其中 repo 已登錄休市=`{','.join(x['date'] for x in r['price_sequence']['repo_scheduled_calendar_rows'] + r['price_sequence']['repo_exceptional_calendar_rows']) or 'none'}`；未有休市登錄的缺檔平日=`{','.join(r['price_sequence']['unexplained_missing_weekdays']) or 'none'}`。已登錄休市不當作 missing-price 錯誤；回溯登錄亦不是當時官方原公告的完整證明。", "",
                  "enum 來源指指定 Git bytes 按指定程式可重現的傳遞路徑；沒有逐次 invocation attestation，不宣稱已證明當日實際執行該函式。", "",
                  "|八項根因檢查|本次狀態|", "|---|---|"]
        lines += [f"|`{c['check']}`|`{c['status']}`|" for c in r["checks"]]
        lines += ["", "可重現來源：", ""]
        for e in [r["snapshot_row"], r["pipeline_candidate_row"], r["pit"]["earlier_selector_evidence"], *r["price_endpoints"], r["enum_lineage"]["candidate_source_row"], r["enum_lineage"]["trend_debug_row"], *r["enum_lineage"].get("history_rows", [])]:
            m = audit["source_manifest"][e["source"]]
            lines.append(f"- [{m['path']} row {e['row_number']}]({m['url']})；file SHA-256=`{m['sha256']}`；canonical row SHA-256=`{e['row_sha256']}`。")
        lines.append("")
    lines += ["## 外部事件證據與取得限制", ""]
    for e in audit["external_evidence"]:
        lines.append(f"- {e['stock_id']}：[{e['title']}]({e['url']})；status=`{e['status']}`。{e['finding_zh']} {e['limitation_zh']}")
    digest = audit["v2_embedded_digest_audit"]
    lines += ["", "## Snapshot 換行與雜湊基礎", "",
              "舊 replay 的 snapshot_sha256 沿用 snapshot manifest；既有 producer 接受 raw、LF、CRLF 三種換行表示。本 audit 另以 source_manifest 鎖定 raw Git bytes，逐筆列出舊摘要匹配基礎；換行差異不等於價格、欄位內容或歷史版本變更。", ""]
    for record in audit["observations"]:
        evidence = record["snapshot_digest_audit"]
        lines.append(f"- {record['stock_id']}：v2 snapshot_sha256=`{evidence['recorded_v2_snapshot_sha256']}`；raw Git SHA-256=`{evidence['sha256_by_basis']['raw_git_bytes']}`；matching_bases=`{';'.join(evidence['matching_bases'])}`。")
    lines += ["", "## v2 原有 artifact digest 差異", "",
              f"detail 實際 SHA-256=`{digest['actual_detail_sha256']}`；summary 內嵌值=`{';'.join(digest['summary_embedded_detail_sha256'])}`。embedded_hash_mismatch={digest['embedded_hash_mismatch']}。", "",
              f"僅在記憶體清空 {digest['annotation_rows']} 列的 observation code/status 兩欄、其餘內容與欄序不變，重新序列化得到 `{digest['pre_observation_annotation_reconstruction_sha256']}`，與內嵌值相符={digest['pre_observation_reconstruction_matches_embedded']}。v2 wrapper 在 base.build 計算 digest 後才加標籤；這是摘要綁定缺陷，不是價格或報酬算術錯誤。本次沿用實際 Git bytes 雜湊，未修寫舊 artifacts。", "",
              "## 判讀與後續界線", "",
              "八項檢查中的 formal_operation_replay 尚未成立：正式 entry/exit、成本與同股重疊處理仍待使用者決定。價格調整基礎、官方停復牌／事件覆蓋、獨立 OHLC 佐證與原始輸入可用時間亦有缺口。因此本稽核可供研究查證，不構成模型 promotion 證據。", "",
              "EPS、毛利率、營業利益率、營業利益、業外損益、稅後淨利與季度／年度財報不在本次範圍；月營收僅在既有 candidate producer lineage 需要時作來源追溯。", "",
              "若要修復共享 source 或制定正式 operation 規則，須由使用者另定範圍；本次只保存查證結果。舊 v1 零訊號與 v2 原始績效未覆寫，formal_use=False、trade_eligible=False、promotion_evidence_allowed=False。", "",
              f"機器可核對證據：`{STEM}.json`；六筆表格：`{STEM}.csv`。JSON 包含原始列、Git blob、file/row SHA-256、各段價格序列與 producer function 位置。", ""]
    return "\n".join(lines)


@contextmanager
def output_guard(root: Path):
    sparse = subprocess.run(["git", "-C", str(root), "config", "--bool", "core.sparseCheckout"],
                            check=False, capture_output=True, text=True).stdout.strip().lower() == "true"
    if not sparse:
        with model_owned_artifact_guard(
            OWNER_ID, PRODUCER, root=root,
            registry_path=root / "config/model_research_artifact_ownership.csv",
            sentinel_registry_path=root / "config/model_research_protected_sentinels.csv",
        ):
            yield
        return
    def state() -> dict[str, str]:
        paths = subprocess.run(["git", "-C", str(root), "status", "--porcelain=v1", "--untracked-files=all"], check=True, capture_output=True, text=True).stdout
        return {line[3:]: sha((root / line[3:]).read_bytes()) if (root / line[3:]).is_file() else "missing" for line in paths.splitlines() if len(line) > 3}
    before = state()
    try:
        yield
    finally:
        after = state()
        changed = [p for p in before.keys() | after.keys() if before.get(p) != after.get(p)]
        errors = validate_changed_paths(OWNER_ID, PRODUCER, changed, load_ownership_rules(root / "config/model_research_artifact_ownership.csv"))
        if errors:
            raise RuntimeError("\n".join(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit six pinned TDCC price/PIT observations without changing replay performance.")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.repository_root.resolve()
    output_paths = [f"{DIRECTORY}/{STEM}.{extension}" for extension in ("json", "csv", "md")]
    errors = validate_changed_paths(OWNER_ID, PRODUCER, output_paths, load_ownership_rules(root / "config/model_research_artifact_ownership.csv"))
    if errors:
        raise RuntimeError("\n".join(errors))
    audit = build(root)
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows({k: r[k] for k in FIELDS} for r in audit["observations"])
    report = render_report(audit)
    audit["companion_sha256"] = {"csv": sha(buffer.getvalue().encode("utf-8")), "md": sha(report.encode("utf-8"))}
    with output_guard(root):
        (root / DIRECTORY).mkdir(parents=True, exist_ok=True)
        (root / output_paths[0]).write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        (root / output_paths[1]).write_text(buffer.getvalue(), encoding="utf-8", newline="\n")
        (root / output_paths[2]).write_text(report, encoding="utf-8", newline="\n")
    print(f"price_pit_audit observations={len(audit['observations'])} sources={len(audit['source_manifest'])} all_dispositions=unresolved_anomaly_candidate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
