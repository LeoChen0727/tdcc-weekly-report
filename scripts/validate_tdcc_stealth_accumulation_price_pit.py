from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import io
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
ARTIFACT_COMMIT = "dde3ce9e39bc344297581223c6d2f10c802dc46c"
SOURCE_COMMIT = "7ef37a966280201a5ee236856306fdb513de7092"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
STEM = "tdcc_stealth_accumulation_price_pit_audit_v1"
CONFIG = "config/tdcc_stealth_accumulation_price_pit_evidence_v1.json"
V2_STEM = "tdcc_stealth_accumulation_historical_selector_field_contract_replay"
SELECTOR_PATH = "scripts/build_tdcc_stealth_accumulation_historical_replay.py"
CONTRACT_PATH = "config/daily_model_numerical_anomaly_disposition_contract.csv"
TAIPEI = timezone(timedelta(hours=8))
EXPECTED_OBSERVATIONS = {
    "d10_max_observed_return": ("8261", 10), "d5_min_observed_return": ("2492", 5),
    "d5_max_observed_return": ("1447", 5), "d10_min_observed_return": ("3624", 10),
    "d20_min_observed_return": ("8358", 20), "d20_max_observed_return": ("3653", 20),
}
CANDIDATE_PATHS = {
    "pattern": "output/latest/daily_pattern_watch_latest.csv",
    "revenue_pullback": "output/latest/revenue_pullback_latest.csv",
    "revenue_breakout_low_response": "output/latest/revenue_breakout_low_response_latest.csv",
}
REQUIRED_CHECKS = [
    "identity_dedup_non_overlap", "formal_operation_replay", "point_in_time_and_trading_calendar",
    "raw_source_lineage_and_hash", "units_formula_and_adjustment_basis",
    "authoritative_business_event_history", "independent_source_corroboration",
    "reproducible_evidence_reference",
]
EXPECTED_CHECK_STATUSES = {name: "verified_commit_row_lineage" if name in {"raw_source_lineage_and_hash", "reproducible_evidence_reference"}
                           else "not_established_user_decision_pending" if name == "formal_operation_replay" else "partial"
                           for name in REQUIRED_CHECKS}
CSV_FIELDS = [
    "observation_id", "model_id", "model_name_zh", "stock_id", "stock_name",
    "signal_date", "snapshot_date", "snapshot_row_number", "category", "horizon",
    "entry_date", "entry_open", "exit_date", "exit_close", "gross_return_pct",
    "same_stock_signal_rows", "same_stock_signal_categories", "snapshot_generated_at",
    "pipeline_commit_time", "generated_after_entry_open", "pipeline_after_entry_open",
    "enum_source_branch", "enum_window_dates", "selector_input_differences",
    "source_sequence_rows", "missing_stock_dates", "missing_weekdays",
    "disposition", "retained_in_primary", "formal_use", "trade_eligible", "promotion_evidence_allowed",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def normalized(value: object) -> str:
    value = str(value or "").replace("\ufeff", "").strip()
    return "" if value.lower() in {"none", "nan", "nat", "<na>"} else value


def parse_rows(payload: bytes) -> list[dict[str, str]]:
    return [{str(k): normalized(v) for k, v in row.items()}
            for row in csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))) ]


def row_digest(row: dict) -> str:
    return digest(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())


def time_of(value: str) -> datetime:
    if value.endswith(" Asia/Taipei"):
        return datetime.strptime(value.removesuffix(" Asia/Taipei"), "%Y-%m-%d %H:%M:%S").replace(tzinfo=TAIPEI)
    value = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(value.tzinfo is not None, "timestamp must include timezone")
    return value.astimezone(TAIPEI)


def session_time(date: str, hour: int, minute: int = 0) -> datetime:
    return datetime.strptime(date, "%Y%m%d").replace(hour=hour, minute=minute, tzinfo=TAIPEI)


class GitSources:
    def __init__(self, root: Path):
        self.root = root
        self.cache: dict[str, bytes] = {}

    def git(self, *args: str) -> bytes:
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True).stdout

    def read(self, key: str) -> bytes:
        require(bool(re.fullmatch(r"[0-9a-f]{40}:[^\r\n]+", key)), "source must use full immutable commit")
        if key not in self.cache:
            self.cache[key] = self.git("show", key)
        return self.cache[key]

    def rows(self, key: str) -> list[dict]:
        return parse_rows(self.read(key))

    def commit_time(self, commit: str) -> str:
        return self.git("show", "-s", "--format=%cI", commit).decode().strip()

    def paths(self, commit: str, prefix: str) -> list[str]:
        return self.git("ls-tree", "-r", "--name-only", commit, prefix).decode().splitlines()


def verify_manifest(manifest: dict, sources: GitSources) -> None:
    require(bool(manifest), "empty source manifest")
    for key, entry in manifest.items():
        require(key == f"{entry['commit']}:{entry['path']}", f"manifest identity mismatch: {key}")
        payload = sources.read(key)
        oid = hashlib.sha1(b"blob " + str(len(payload)).encode() + b"\0" + payload).hexdigest()
        require(entry["sha256"] == digest(payload), f"source file hash mismatch: {key}")
        require(entry["bytes"] == len(payload), f"source byte count mismatch: {key}")
        require(entry["git_blob_oid"] == oid, f"source Git blob mismatch: {key}")
        require(entry["url"] == f"https://github.com/LeoChen0727/tdcc-weekly-report/blob/{entry['commit']}/{entry['path']}", "source URL mismatch")


def verify_references(value: object, manifest: dict, sources: GitSources) -> None:
    if isinstance(value, list):
        for item in value:
            verify_references(item, manifest, sources)
    elif isinstance(value, dict):
        if "row_sha256" in value:
            require(set(("source", "row_number", "row", "row_sha256")) <= value.keys(), "malformed row reference")
            key, number = value["source"], value["row_number"]
            require(key in manifest, f"row reference absent from manifest: {key}")
            rows = sources.rows(key)
            require(type(number) is int and 2 <= number <= len(rows) + 1, "raw row number outside source")
            require(value["row"] == rows[number - 2], f"raw row mismatch: {key}:{number}")
            require(value["row_sha256"] == row_digest(rows[number - 2]), f"canonical row hash mismatch: {key}:{number}")
        if "function_sha256" in value:
            key = value["source"]
            require(key in manifest, "producer function source absent from manifest")
            code = sources.read(key).decode("utf-8-sig")
            matches = [n for n in ast.walk(ast.parse(code)) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == value["name"] and n.lineno == value["line"]]
            require(len(matches) == 1, "producer function identity mismatch")
            node = matches[0]
            require(node.end_lineno == value["end_line"] and digest(ast.get_source_segment(code, node).encode()) == value["function_sha256"], "producer function hash mismatch")
        for child in value.values():
            verify_references(child, manifest, sources)


def input_names(sources: GitSources) -> set[str]:
    code = sources.read(f"{ARTIFACT_COMMIT}:{SELECTOR_PATH}").decode("utf-8-sig")
    nodes = [n for n in ast.parse(code).body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "SELECTOR_INPUT_NAMES" for t in n.targets)]
    require(len(nodes) == 1, "missing pinned selector input inventory")
    return {name + suffix for name in ast.literal_eval(nodes[0].value) for suffix in ("", "_x", "_y")}


def field_differences(left: dict, right: dict, fields: set[str]) -> dict:
    return {k: [left.get(k, ""), right.get(k, "")] for k in sorted(fields) if left.get(k, "") != right.get(k, "")}


def verify_selector_comparison(record: dict, fields: set[str]) -> None:
    left, right = record["pipeline_candidate_row"]["row"], record["snapshot_row"]["row"]
    expected = field_differences(left, right, fields)
    require(record["pipeline_selector_input_differences"] == expected, "selector input comparison mismatch")
    require(record["selector_input_differences"] == len(expected), "selector difference count mismatch")
    require(record["pipeline_common_field_differences"] == field_differences(left, right, set(left) & set(right)), "common field comparison mismatch")


def population_expected(rows: list[dict]) -> dict:
    count = Counter()
    late_dates = set()
    for row in rows:
        generated = time_of(row["snapshot_generated_at"])
        signal = session_time(row["candidate_signal_date"], 13, 30)
        if generated.date() > signal.date():
            count["generated_calendar_date_after_signal_date"] += 1
            late_dates.add(row["snapshot_report_date"])
        count["generated_after_signal_close"] += generated > signal
        if not row["entry_date"]:
            count["no_entry_date"] += 1
            continue
        opening = session_time(row["entry_date"], 9)
        count["with_entry_date"] += 1
        count["generated_after_entry_open"] += generated > opening
        relation = "before" if generated.date() < opening.date() else "after" if generated.date() > opening.date() else "on"
        count[f"generated_calendar_date_{relation}_entry_date"] += 1
    groups = Counter((r["stock_id"], r["candidate_signal_date"]) for r in rows)
    identities = Counter((r["snapshot_path"], r["snapshot_row_number"]) for r in rows)
    return {"signal_rows": len(rows), "unique_stocks": len({r["stock_id"] for r in rows}),
            "snapshot_dates_with_generated_calendar_date_after_signal": len(late_dates), **dict(count),
            "unique_stock_signal_dates": len(groups), "same_stock_signal_duplicate_groups": sum(n > 1 for n in groups.values()),
            "duplicate_group_rows": sum(n for n in groups.values() if n > 1), "excess_stock_signal_rows": sum(n - 1 for n in groups.values()),
            "snapshot_identity_duplicate_groups": sum(n > 1 for n in identities.values())}


def verify_population(population: dict, rows: list[dict]) -> None:
    for key, value in population_expected(rows).items():
        require(population.get(key, 0) == value, f"population mismatch: {key}")
    require(population["interpretation"] == "metadata_temporal_comparison_not_event_time_PIT_or_trade_eligibility_verdict", "metadata lateness must not be a look-ahead verdict")


def verify_disposition(record: dict) -> None:
    require(record["disposition"] == "unresolved_anomaly_candidate" and record["retained_in_primary"] is True, "unresolved observation must remain in primary")
    require(all(record[k] is False for k in ("formal_use", "trade_eligible", "promotion_evidence_allowed")), "observation research boundary violated")
    require(record["checks"] == [{"check": name, "status": EXPECTED_CHECK_STATUSES[name]} for name in REQUIRED_CHECKS], "observation eight-check status/order mismatch")


def embedded_digest_expected(detail_payload: bytes, summary_rows: list[dict]) -> dict:
    reader = csv.DictReader(io.StringIO(detail_payload.decode("utf-8-sig")))
    fields, rows = reader.fieldnames, list(reader)
    require(bool(rows) and {"large_return_observation_codes", "large_return_spotcheck_status"} <= set(fields or []), "v2 annotation columns missing")
    before = [{**r, "large_return_observation_codes": "", "large_return_spotcheck_status": ""} for r in rows]
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(before)
    embedded = sorted({r["detail_artifact_sha256"] for r in summary_rows})
    reconstructed = digest(buffer.getvalue().encode("utf-8"))
    return {"actual_detail_sha256": digest(detail_payload), "summary_embedded_detail_sha256": embedded,
            "embedded_hash_mismatch": embedded != [digest(detail_payload)],
            "pre_observation_annotation_reconstruction_sha256": reconstructed,
            "pre_observation_reconstruction_matches_embedded": embedded == [reconstructed],
            "annotation_rows": sum(bool(r["large_return_observation_codes"] or r["large_return_spotcheck_status"]) for r in rows),
            "interpretation": "v2_wrapper_annotations_added_after_base_detail_digest_not_price_or_return_error", "old_artifact_modified": False}


def verify_companions(audit: dict, csv_payload: bytes, report_payload: bytes) -> None:
    require(audit["companion_sha256"] == {"csv": digest(csv_payload), "md": digest(report_payload)}, "companion artifact hash mismatch")


def verify_timing(record: dict, sources: GitSources, fields: set[str]) -> None:
    replay, pit = record["v2_detail"]["row"], record["pit"]
    generated = time_of(replay["snapshot_generated_at"])
    opening = session_time(replay["entry_date"], 9)
    closing = session_time(replay["candidate_signal_date"], 13, 30)
    commit_time = sources.commit_time(replay["snapshot_pipeline_commit_sha"])
    require(record["pipeline_commit_time"] == commit_time, "pipeline commit time mismatch")
    require(record["generated_after_entry_open"] is (generated > opening), "generated/entry comparison mismatch")
    require(record["pipeline_after_entry_open"] is (time_of(commit_time) > opening), "pipeline/entry comparison mismatch")
    require(pit["signal_close"] == closing.isoformat() and pit["research_entry_open"] == opening.isoformat(), "session time mismatch")
    require(pit["generated_after_signal_close"] is (generated > closing), "generated/close comparison mismatch")
    require(pit["original_publication_time_proven"] is False and pit["metadata_is_first_publication_or_input_filed_at"] is False, "metadata cannot prove original availability")
    earlier = pit["earlier_selector_evidence"]
    early_commit, path = earlier["source"].split(":", 1)
    require(path == "output/latest/all_candidates_latest.csv", "earlier evidence must be candidate source")
    snapshot = record["snapshot_row"]["row"]
    require(all(earlier["row"].get(k) == snapshot.get(k) for k in ("stock_id", "date", "category")), "earlier candidate composite identity mismatch")
    require(not field_differences(earlier["row"], snapshot, fields), "earlier selector inputs differ")
    early_time = sources.commit_time(early_commit)
    require(pit["matching_commit_time"] == early_time and pit["matching_before_entry_open"] is (time_of(early_time) < opening), "earlier candidate availability comparison mismatch")


def verify_enum(record: dict, sources: GitSources) -> None:
    lineage, snapshot = record["enum_lineage"], record["snapshot_row"]["row"]
    pipeline = record["v2_detail"]["row"]["snapshot_pipeline_commit_sha"]
    candidate, trend = lineage["candidate_source_row"], lineage["trend_debug_row"]
    require(candidate["source"] == f"{pipeline}:{CANDIDATE_PATHS[snapshot['category']]}", "candidate enum source path mismatch")
    require(trend["source"] == f"{pipeline}:output/latest/tdcc_trend_debug_latest.csv", "debug enum source path mismatch")
    for ref in (candidate, trend):
        require(ref["row"].get("stock_id") == snapshot["stock_id"], "enum stock identity mismatch")
    require(candidate["row"].get("date") == snapshot["date"], "enum candidate date mismatch")
    explicit = bool(candidate["row"].get("tdcc_accumulation_signal"))
    selected = candidate if explicit else trend
    expected_branch = "existing_candidate_enum_preserved" if explicit else "blank_candidate_enum_filled_from_trend_debug"
    require(lineage["branch"] == record["enum_source_branch"] == expected_branch, "enum branch mismatch")
    require(lineage["selected_source"] == selected["source"], "enum selected source mismatch")
    require(lineage["selected_enum"] == selected["row"]["tdcc_accumulation_signal"] == snapshot["tdcc_accumulation_signal"], "enum inheritance mismatch")
    require(lineage["snapshot_tdcc_date"] == snapshot.get("tdcc_date", ""), "holder date must remain separate from enum window")
    require(lineage["runtime_invocation_evidence"] == "not_recorded" and lineage["event_time_availability"] == "unproven_original_input_filed_at_not_present", "enum values cannot prove runtime invocation or original availability")
    required = {(f"{pipeline}:build_all_candidates_latest.py", name) for name in ("merge_tdcc", "merge_without_duplicate_columns", "infer_tdcc_signal_from_numbers", "deduplicate_candidates")}
    required.add((f"{pipeline}:tdcc_trend_utils.py", "classify_accumulation"))
    if explicit:
        required |= {(f"{pipeline}:tdcc_trend_utils.py", "load_tdcc_history_trend"), (f"{pipeline}:build_revenue_breakout_low_response.py", "build_revenue_breakout_low_response_candidates")}
    actual = {(r["source"], r["name"]) for r in lineage["producer_functions"]}
    require(required <= actual, f"missing required producer function: {sorted(required - actual)}")
    if not explicit:
        require(lineage["enum_window_dates"] == trend["row"].get("tdcc_history_dates", ""), "debug enum history window mismatch")
    else:
        selected_paths = sorted(p for p in sources.paths(pipeline, "output/history/tdcc") if re.fullmatch(r"output/history/tdcc/tdcc_holder_ratio_\d{8}\.csv", p))[-4:]
        require(lineage["selected_history_paths"] == selected_paths, "explicit enum history path selection mismatch")
        observed = []
        missing = []
        for path in selected_paths:
            matches = [r for r in sources.rows(f"{pipeline}:{path}") if (r.get("stock_id") or r.get("ticker") or r.get("code")) == snapshot["stock_id"]]
            require(len(matches) <= 1, "ambiguous TDCC history identity")
            if matches:
                observed.append((path, matches[0]))
            else:
                missing.append(Path(path).stem[-8:])
        require([(r["source"].split(":", 1)[1], r["row"]) for r in lineage["history_rows"]] == observed, "explicit enum history rows mismatch")
        require(lineage["missing_history_dates"] == missing, "missing TDCC history dates mismatch")
        require(len(observed) >= 2, "insufficient explicit enum history evidence")
        window = ",".join(Path(p).stem[-8:] for p, _ in observed)
        require(lineage["enum_window_dates"] == window, "explicit enum window mismatch")
        sequences = [[Decimal(r[f"over_{size}_pct"]) for _, r in observed] for size in (400, 1000)]
        changes = [x[-1] - x[0] for x in sequences]
        ups = [sum(b > a for a, b in zip(x, x[1:])) for x in sequences]
        expected_metrics = {f"tdcc_{size}_change_sum": str(change) for size, change in zip((400, 1000), changes)}
        expected_metrics.update({f"tdcc_{size}_up_weeks": up for size, up in zip((400, 1000), ups)})
        require(lineage["history_recomputed_metrics"] == expected_metrics, "reported enum history metrics mismatch")
        expected = "strong_accumulation" if all(v > 0 for v in changes) and min(ups) >= 2 else "mild_accumulation" if any(v > 0 for v in changes) else "distribution_warning" if any(v < 0 for v in changes) else "neutral"
        require(candidate["row"]["tdcc_accumulation_signal"] == expected, "explicit enum history classification mismatch")
        for size, change, up in zip((400, 1000), changes, ups):
            require(Decimal(candidate["row"][f"tdcc_{size}_change_sum"]) == change and Decimal(candidate["row"][f"tdcc_{size}_up_weeks"]) == up, "explicit enum history metrics mismatch")
        require(Decimal(candidate["row"]["tdcc_weeks_used"]) == len(observed), "explicit enum history weeks mismatch")
    require(record["enum_window_dates"] == lineage["enum_window_dates"], "enum window CSV projection mismatch")


def expected_snapshot_digest(payload: bytes, recorded: str) -> dict:
    normalized_bytes = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    hashes = {"raw_git_bytes": digest(payload), "lf": digest(normalized_bytes),
              "crlf": digest(normalized_bytes.replace(b"\n", b"\r\n"))}
    matches = [basis for basis, value in hashes.items() if value == recorded]
    require(bool(matches), "v2 snapshot file hash mismatch on all declared line-ending bases")
    return {"recorded_v2_snapshot_sha256": recorded, "sha256_by_basis": hashes,
            "matching_bases": matches, "raw_bytes_match": recorded == hashes["raw_git_bytes"],
            "interpretation": "legacy_manifest_digest_accepts_raw_LF_CRLF_raw_Git_manifest_remains_exact"}


def verify_identity(record: dict, detail: list[dict], sources: GitSources) -> None:
    replay, snapshot = record["v2_detail"]["row"], record["snapshot_row"]
    require(snapshot["source"] == f"{SOURCE_COMMIT}:{replay['snapshot_path']}" and snapshot["row_number"] == int(replay["snapshot_row_number"]) and snapshot["row_sha256"] == replay["snapshot_row_sha256"], "snapshot composite identity mismatch")
    require(record["snapshot_digest_audit"] == expected_snapshot_digest(sources.read(snapshot["source"]), replay["snapshot_sha256"]), "snapshot digest basis audit mismatch")
    require(record["pipeline_candidate_row"]["source"] == f"{replay['snapshot_pipeline_commit_sha']}:output/latest/all_candidates_latest.csv", "pipeline candidate source mismatch")
    left, right = snapshot["row"], record["pipeline_candidate_row"]["row"]
    require(all(left.get(k) == right.get(k) for k in ("stock_id", "date", "category")), "pipeline candidate composite identity mismatch")
    same = [r for r in detail if r["stock_id"] == replay["stock_id"] and r["candidate_signal_date"] == replay["candidate_signal_date"]]
    identities = [{k: r[k] for k in ("snapshot_path", "snapshot_row_number", "snapshot_row_sha256")} for r in same]
    categories = [sources.rows(f"{SOURCE_COMMIT}:{r['snapshot_path']}")[int(r["snapshot_row_number"]) - 2]["category"] for r in same]
    require(record["same_stock_signal_rows"] == len(same) and record["same_stock_signal_identities"] == identities, "same-stock signal identity count mismatch")
    require(record["same_stock_signal_categories"] == ";".join(categories), "same-stock category provenance mismatch")


def verify_prices(record: dict, sources: GitSources) -> None:
    replay, horizon = record["v2_detail"]["row"], record["horizon"]
    endpoints = record["price_endpoints"]
    require(len(endpoints) == 2, "price endpoints must contain entry and exit")
    for endpoint, prefix in zip(endpoints, ("entry", f"exit_d{horizon}")):
        require(endpoint["source"] == f"{SOURCE_COMMIT}:{replay[prefix + '_price_source_path']}" and endpoint["row_sha256"] == replay[prefix + "_price_row_sha256"], "v2 endpoint lineage mismatch")
        require(digest(sources.read(endpoint["source"])) == replay[prefix + "_price_source_sha256"], "v2 endpoint file hash mismatch")
        require(endpoint["row"]["stock_id"] == record["stock_id"], "price endpoint stock mismatch")
        require(endpoint["row"]["date"] == (record["entry_date"] if prefix == "entry" else record["exit_date"]), "price endpoint date mismatch")
    opening, close = Decimal(endpoints[0]["row"]["open"]), Decimal(endpoints[1]["row"]["close"])
    require(opening > 0 and close > 0, "invalid price endpoint")
    value = ((close / opening - 1) * 100).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    require(Decimal(record["gross_return_pct"]) == value == Decimal(replay[f"return_d{horizon}_pct"]), "gross return formula mismatch")
    require(Decimal(record["entry_open"]) == opening == Decimal(replay["entry_open_price"]), "entry open mismatch")
    require(Decimal(record["exit_close"]) == close == Decimal(replay[f"exit_d{horizon}_close_price"]), "exit close mismatch")
    sequence = record["price_sequence"]
    paths = sorted(p for p in sources.paths(SOURCE_COMMIT, "data/daily_price") if re.fullmatch(r"data/daily_price/\d{8}\.csv", p) and record["signal_date"] <= Path(p).stem <= record["exit_date"])
    expected_rows, missing = [], []
    for path in paths:
        matches = [(i, r) for i, r in enumerate(sources.rows(f"{SOURCE_COMMIT}:{path}"), 2) if r.get("stock_id") == record["stock_id"]]
        require(len(matches) <= 1, "duplicate raw price stock/date")
        if matches:
            expected_rows.append((f"{SOURCE_COMMIT}:{path}", matches[0][0]))
        else:
            missing.append(Path(path).stem)
    require([(r["source"], r["row_number"]) for r in sequence["raw_rows"]] == expected_rows, "price sequence row omission or addition")
    require(sequence["source_dates"] == [Path(p).stem for p in paths] and sequence["missing_stock_dates"] == missing, "price sequence dates mismatch")
    valid = [r for r in sequence["raw_rows"] if r["row"].get("open") and r["row"].get("close") and Decimal(r["row"]["open"]) > 0 and Decimal(r["row"]["close"]) > 0]
    after = [r for r in valid if r["row"]["date"] > record["signal_date"]]
    require(after and after[0]["row"]["date"] == record["entry_date"] and len(after) > horizon and after[horizon]["row"]["date"] == record["exit_date"], "next available open/future close sequence mismatch")
    count = sum(record["entry_date"] <= r["row"]["date"] <= record["exit_date"] for r in valid)
    require(record["source_sequence_rows"] == sequence["source_window_rows"] == count and sequence["source_window_matches_horizon"] is (count == horizon + 1), "source horizon count mismatch")
    weekdays = []
    date = session_time(record["signal_date"], 0)
    while date <= session_time(record["exit_date"], 0):
        if date.weekday() < 5 and date.strftime("%Y%m%d") not in sequence["source_dates"]:
            weekdays.append(date.strftime("%Y%m%d"))
        date += timedelta(days=1)
    require(sequence["missing_weekdays"] == weekdays and record["missing_weekdays"] == ";".join(weekdays) and record["missing_stock_dates"] == ";".join(missing), "missing-date projection mismatch")
    require(sequence["source_date_presence_is_official_calendar_proof"] is False and sequence["official_suspension_resumption_history_complete"] is False, "source sequence cannot prove official calendar")


def verify_document(audit: dict, settings: dict, sources: GitSources) -> None:
    require(audit["schema_version"] == STEM and audit["model_id"] == MODEL_ID, "audit model/schema mismatch")
    require(audit["artifact_commit"] == settings["artifact_commit"] == ARTIFACT_COMMIT and audit["replay_source_commit"] == settings["replay_source_commit"] == SOURCE_COMMIT, "immutable audit source pin mismatch")
    require(audit["code_baseline_commit"] == settings["code_baseline_commit"], "code baseline mismatch")
    require(audit["primary_metric_basis"] == "signal_row_weighted_not_independent_positions_or_tradable_strategy", "signal-row weighting boundary missing")
    for key in ("formal_use", "trade_eligible", "promotion_evidence_allowed", "primary_replay_modified", "corrected_performance_published"):
        require(audit[key] is False, f"research boundary violated: {key}")
    require(audit["formal_operation_replay"] == "not_established_entry_exit_cost_same_stock_overlap_rules_require_user_decision", "formal operation replay cannot be established")
    manifest = audit["source_manifest"]
    verify_manifest(manifest, sources)
    verify_references(audit, manifest, sources)
    require([(r["source"], r["name"]) for r in audit["snapshot_digest_contract_functions"]] == [(f"{ARTIFACT_COMMIT}:{SELECTOR_PATH}", "_hash_candidates")], "legacy snapshot digest contract source mismatch")
    v2keys = [f"{ARTIFACT_COMMIT}:{DIRECTORY}/{V2_STEM}_{suffix}_v2.{ext}" for suffix, ext in (("detail", "csv"), ("summary", "csv"), ("report", "md"))]
    require(audit["v2_artifact_manifest"] == [manifest[k] for k in v2keys], "v2 artifact triplet mismatch")
    expected_digest = embedded_digest_expected(sources.read(v2keys[0]), sources.rows(v2keys[1]))
    require(audit["v2_embedded_digest_audit"] == expected_digest, "v2 embedded digest audit mismatch")
    require(expected_digest["embedded_hash_mismatch"] is True and expected_digest["pre_observation_reconstruction_matches_embedded"] is True, "pinned v2 annotation/digest discrepancy not reproduced")
    detail = sources.rows(v2keys[0])
    verify_population(audit["population"], detail)
    checks = next(r for r in sources.rows(f"{audit['code_baseline_commit']}:{CONTRACT_PATH}") if r["disposition_id"] == "unresolved_anomaly_candidate")["required_root_checks"].split(";")
    require(checks == REQUIRED_CHECKS, "eight-check contract order mismatch")
    fields = input_names(sources)
    records = audit["observations"]
    require(len(records) == 6 and {r["observation_id"] for r in records} == set(EXPECTED_OBSERVATIONS), "six observation identities required")
    for record in records:
        require((record["stock_id"], record["horizon"]) == EXPECTED_OBSERVATIONS[record["observation_id"]], "observation stock/horizon mismatch")
        replay = record["v2_detail"]["row"]
        require(record["v2_detail"]["source"] == v2keys[0] and record["observation_id"] in replay["large_return_observation_codes"].split(";"), "observation is not the pinned v2 extreme row")
        for key, field in (("stock_id", "stock_id"), ("stock_name", "stock_name"), ("signal_date", "candidate_signal_date"), ("snapshot_date", "snapshot_report_date"), ("snapshot_row_number", "snapshot_row_number"), ("entry_date", "entry_date"), ("snapshot_generated_at", "snapshot_generated_at")):
            require(record[key] == replay[field], f"observation field mismatch: {key}")
        require(record["exit_date"] == replay[f"exit_d{record['horizon']}_date"] and record["category"] == record["snapshot_row"]["row"]["category"], "observation exit/category mismatch")
        verify_disposition(record)
        verify_identity(record, detail, sources)
        verify_selector_comparison(record, fields)
        verify_timing(record, sources, fields)
        verify_prices(record, sources)
        verify_enum(record, sources)
    require(audit["external_evidence"] == settings["external_evidence"], "external evidence differs from reviewed configuration")
    for evidence in audit["external_evidence"]:
        if "ohlc" in str(evidence).lower() or "OHLC" in evidence.get("title", ""):
            require(evidence.get("status") not in {"accepted", "verified", "confirmed", "pass"}, "independent OHLC not accepted in this audit")


def verify_presentations(audit: dict, csv_payload: bytes, report: str) -> None:
    reader = csv.DictReader(io.StringIO(csv_payload.decode("utf-8-sig")))
    fields, rows = reader.fieldnames or [], list(reader)
    require(fields == CSV_FIELDS and len(rows) == 6, "audit CSV exact column contract mismatch")
    require(rows == [{k: str(r[k]) for k in fields} for r in audit["observations"]], "CSV/JSON six-row parity mismatch")
    required = [MODEL_ID, audit["code_baseline_commit"], ARTIFACT_COMMIT, SOURCE_COMMIT,
                "unresolved_anomaly_candidate", "全部留在既有主結果", "不發布修正績效", "按訊號列加權",
                "不能直接認定前視偏誤", "formal_operation_replay", "formal_use=False", "promotion_evidence_allowed=False"]
    for token in required:
        require(token in report, f"report research conclusion missing: {token}")
    for record in audit["observations"]:
        require(record["stock_id"] in report and record["observation_id"] in report and record["gross_return_pct"] in report, "report observation omission")


def validate(root: Path) -> dict:
    settings_bytes = (root / CONFIG).read_bytes()
    settings = json.loads(settings_bytes)
    audit = json.loads((root / DIRECTORY / f"{STEM}.json").read_text(encoding="utf-8"))
    require(audit["configuration_sha256"] == digest(settings_bytes), "configuration hash mismatch")
    verify_document(audit, settings, GitSources(root))
    csv_payload = (root / DIRECTORY / f"{STEM}.csv").read_bytes()
    report_payload = (root / DIRECTORY / f"{STEM}.md").read_bytes()
    verify_companions(audit, csv_payload, report_payload)
    verify_presentations(audit, csv_payload, report_payload.decode("utf-8"))
    return {"observations": len(audit["observations"]), "sources": len(audit["source_manifest"]), "status": "pass"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Independently validate the pinned TDCC price/PIT audit.")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    print(json.dumps(validate(args.repository_root.resolve()), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
