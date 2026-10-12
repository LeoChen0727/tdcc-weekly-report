"""Model-owned, immutable confirmed-row lineage research; never production sync."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import subprocess
from collections import Counter
from contextlib import contextmanager
from datetime import datetime, time, timezone, timedelta
from pathlib import Path

import pandas as pd

MODEL_ID = "price_pullback_23ema"
OWNER_ID = "price_pullback_23ema_confirmation_lineage_research"
VERSION = "price_pullback_23ema_confirmation_lineage_research_v1"
PRODUCER = "scripts/build_price_pullback_23ema_confirmation_lineage_research.py"
SECTION_PATH = "output/latest/daily_price_pullback_23ema_operation_section_latest.csv"
RANK_PATH = "output/latest/daily_candidate_model_signals_for_report_latest.csv"
AUDIT_PATH = "output/latest/daily_price_pullback_23ema_operation_evidence_audit_latest.csv"
RULE_PATH = "scripts/build_daily_price_pullback_23ema_operation_section.py"
OUTPUT_NAMES = [VERSION + "_rows.csv", VERSION + "_summary.csv", VERSION + "_manifest.json"]
FIELDS = [
    "model_id", "artifact_version", "signal_date", "stock_id", "report_line",
    "model_rank", "display_rank", "model_rank_overall", "confirmed_buy_rank_eligible",
    "confirmation_ref", "confirmation_artifact_sha256", "confirmation_row_sha256",
    "rank_source_sha256", "rank_source_row_sha256", "decision_price_sha256", "decision_target_price", "active_ref", "active_artifact_sha256",
    "active_row_sha256", "active_price_sha256", "entry_date", "entry_price",
    "saved_active_state", "replayed_active_state", "target_price", "terminal_ref",
    "terminal_artifact_sha256", "terminal_row_sha256", "terminal_price_sha256",
    "saved_terminal_state", "replayed_terminal_state", "terminal_target_price", "exit_date", "exit_reason",
    "rule_lineage_status", "economic_unit_status", "return_evidence_allowed", "promotion_allowed",
]
ALLOW = {
    PRODUCER, "scripts/validate_price_pullback_23ema_confirmation_lineage_research.py",
    "tests/test_price_pullback_23ema_confirmation_lineage_research.py",
    "scripts/validate_model_research_workflow_isolation.py", "tests/test_model_research_workflow_isolation.py",
    "tests/test_model_data_independence.py",
    "config/daily_model_background_data_registry.csv", "config/daily_model_data_sharing_registry.csv",
    "config/daily_model_data_sharing_migrations.csv", "config/model_research_artifact_ownership.csv",
    "config/model_research_artifact_ownership_migrations.csv", "config/daily_model_validator_independence.csv",
    "config/repo_production_inventory.csv", "config/repo_file_lifecycle_inventory.csv", "config/report_artifact_lineage.csv",
    "output/latest/model_data_independence_audit_latest.csv", "output/latest/model_data_independence_audit_latest.md",
    "docs/latest/model_data_independence_audit_latest.csv", "docs/latest/model_data_independence_audit_latest.md",
    *("output/research/price_pullback_23ema/" + name for name in OUTPUT_NAMES),
}


def canonical(value) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def csv_rows(raw: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))


def stock(value: str) -> str:
    text = str(value).strip()
    return text[:-2] if text.endswith(".0") else text


def key(row: dict[str, str]) -> tuple[str, str, str]:
    return (str(row.get("signal_date", "")).replace("-", ""), stock(row.get("stock_id", "")),
            row.get("report_line") or row.get("report_bucket") or "")


class GitSources:
    def __init__(self, repo: Path):
        self.repo = repo
        self.cache: dict[tuple[str, str], tuple[bytes, dict]] = {}
        self.process = subprocess.Popen(
            ["git", "--no-replace-objects", "-C", str(repo), "cat-file", "--batch"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def get(self, ref: str, path: str) -> tuple[bytes, dict]:
        identity = (ref, path)
        if identity not in self.cache:
            self.process.stdin.write((ref + ":" + path + "\n").encode("utf-8"))
            self.process.stdin.flush()
            header = self.process.stdout.readline().decode("ascii").strip().split()
            if len(header) != 3 or header[1] != "blob":
                raise ValueError(f"missing canonical Git source {ref}:{path}")
            raw = self.process.stdout.read(int(header[2]))
            if len(raw) != int(header[2]) or self.process.stdout.read(1) != b"\n":
                raise ValueError("truncated Git blob")
            meta = dict(ref=ref, path=path, git_blob=header[0], bytes=len(raw), sha256=sha(raw))
            self.cache[identity] = (raw, meta)
        return self.cache[identity]

    def close(self):
        self.process.stdin.close()
        if self.process.wait(timeout=30):
            raise ValueError("Git source reader failed")


def protected_signature(repo: Path, *, include_allowed: bool = False) -> str:
    raw = subprocess.check_output(["git", "-C", str(repo), "ls-files", "--stage", "-z"])
    items = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, name = record.split(b"\t", 1)
        path = name.decode("utf-8")
        if path in ALLOW and not include_allowed:
            continue
        file = repo / path
        value = sha(file.read_bytes()) if file.is_file() else "__missing__"
        items[path] = [metadata.decode("ascii"), value] if include_allowed else value if file.is_file() else metadata.decode("ascii")
    for name in subprocess.check_output(["git", "-C", str(repo), "ls-files", "--others", "--exclude-standard", "-z"]).split(b"\0"):
        if name and (include_allowed or name.decode("utf-8") not in ALLOW):
            file = repo / name.decode("utf-8")
            items[name.decode("utf-8")] = sha(file.read_bytes())
    return sha(canonical(items))


def require_registration(repo: Path):
    owners = csv_rows((repo / "config/model_research_artifact_ownership.csv").read_bytes())
    shares = csv_rows((repo / "config/daily_model_data_sharing_registry.csv").read_bytes())
    for name in OUTPUT_NAMES:
        path = "output/research/price_pullback_23ema/" + name
        matches = [r for r in owners if r["artifact_glob"] == path]
        if len(matches) != 1 or matches[0]["producer"] != PRODUCER or matches[0]["owner_model_id"] != OWNER_ID or matches[0]["change_policy"] != "model_owned_write":
            raise ValueError(f"unregistered model-owned artifact {path}")
        if not any(r["registered_producers"] == PRODUCER and r["producer_write_scope"] == path
                   and MODEL_ID in r["approved_consumer_models"].split(";") for r in shares):
            raise ValueError(f"unregistered consumer/writer {path}")


@contextmanager
def model_owned_artifact_guard(repo: Path, output: Path):
    """Guard exact external artifacts and sparse Git state, including failures."""
    repo, output = repo.resolve(), output.resolve()
    if output == repo or repo in output.parents:
        raise ValueError("research evidence must use registered external artifact root")
    if output.exists() and any(output.iterdir()):
        raise ValueError("immutable research root is not empty")
    require_registration(repo)
    before = protected_signature(repo)
    repository_before = protected_signature(repo, include_allowed=True)
    receipt = dict(protected_sentinel_before_sha256=before, protected_sentinel_after_sha256=before)
    completed = False
    try:
        yield receipt
        completed = True
    finally:
        names = {path.name for path in output.iterdir()} if output.exists() else set()
        if names - set(OUTPUT_NAMES) or (output.exists() and any(not path.is_file() for path in output.iterdir())):
            raise ValueError("model-owned output scope changed outside three artifacts")
        after = protected_signature(repo)
        if before != after or repository_before != protected_signature(repo, include_allowed=True):
            raise ValueError("protected model/production artifacts or repository changed")
        receipt["protected_sentinel_after_sha256"] = after
        if completed and names != set(OUTPUT_NAMES):
            raise ValueError("model-owned producer did not create exactly three artifacts")


def model_rows(raw: bytes) -> list[dict[str, str]]:
    return [r for r in csv_rows(raw) if r.get("model_id") == MODEL_ID]


def operation_rows(raw: bytes, section: str) -> dict[tuple[str, str, str], dict[str, str]]:
    all_rows = [r for r in model_rows(raw) if r.get("row_type") == "data" and r.get("pdf_section") == section]
    grouped = {}
    for row in all_rows:
        grouped.setdefault(key(row), {})[row.get("pdf_view", "")] = row
    out = {}
    for identity, views in grouped.items():
        if set(views) != {"full", "highlight"}:
            raise ValueError("missing or conflicting operation PDF source views")
        columns = ("buy_rank_eligible", "entry_date", "entry_price", "model_score", "row_action_status")
        if any(views["full"].get(c) != views["highlight"].get(c) for c in columns):
            raise ValueError("operation source view conflict")
        out[identity] = views["full"]
    return out


def price_frame(raw: bytes) -> pd.DataFrame:
    frame = pd.DataFrame(csv_rows(raw))
    for col in ("open", "high", "low", "close", "volume"):
        frame[col] = pd.to_numeric(frame[col], errors="coerce")
    frame["date"] = frame["date"].astype(str).str.replace("-", "", regex=False)
    frame = frame.dropna(subset=["open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)
    if frame["date"].duplicated().any():
        raise ValueError("price dates are not unique")
    frame["ma20"] = frame["close"].rolling(20, min_periods=20).mean()
    frame["ema23"] = frame["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    return frame


def replay(frame: pd.DataFrame, signal_date: str, asof: str) -> dict:
    indices = frame.index[frame["date"].eq(signal_date)].tolist()
    visible = frame.index[frame["date"].le(asof)].tolist()
    if len(indices) != 1 or not visible:
        raise ValueError("missing signal/asof price")
    signal = indices[0]
    entry, last = signal + 1, visible[-1]
    if signal < 20 or entry > last:
        raise ValueError("insufficient warm-up or missing observed entry")
    target = float(frame.iloc[signal - 20:signal]["high"].max())
    result = dict(entry_date=str(frame.iloc[entry]["date"]), entry_price=float(frame.iloc[entry]["open"]),
                  target_price=target, exit_date="", exit_reason="")
    stop_days = 0
    for index in range(entry, min(last, entry + 19) + 1):
        row = frame.iloc[index]
        close = float(row["close"])
        stop = min(float(row["ma20"]), float(row["ema23"])) * .96
        target_hit = close > target
        stop_days = stop_days + 1 if math.isfinite(stop) and close <= stop else 0
        if target_hit or stop_days >= 4:
            reason = "close_prev20_high_break_next_open" if target_hit else "sustained_close_below_lower_ma20_ema23_4pct_4d"
            result.update(state=("target_exit_pending_next_open" if target_hit else "stop_exit_pending_next_open") if index == last else "exited",
                          exit_date=str(frame.iloc[index + 1]["date"]) if index + 1 < len(frame) else "", exit_reason=reason)
            return result
    result["state"] = "expired_d20_no_active_tracking" if last >= entry + 19 else "active_operation"
    return result


def capture_metadata(repo_slug: str, run_id: int) -> dict:
    raw = subprocess.check_output(["gh", "api", f"repos/{repo_slug}/actions/runs/{run_id}"], timeout=60)
    record = json.loads(raw)
    return dict(run_id=record["id"], head_sha=record["head_sha"], server_created_at=record["created_at"],
                event=record["event"], html_url=record["html_url"], conclusion=record["conclusion"], status=record["status"])


def number(value) -> str:
    return format(float(value), ".12g")


def build(repo: Path, decision_ref: str, active_ref: str, outcome_ref: str, capture: dict) -> tuple[list[dict], dict]:
    if capture["head_sha"] != decision_ref:
        raise ValueError("capture server head does not bind confirmed source")
    source = GitSources(repo)
    try:
        confirmed_raw, confirmed_meta = source.get(decision_ref, SECTION_PATH)
        rank_raw, rank_meta = source.get(decision_ref, RANK_PATH)
        active_raw, active_meta = source.get(active_ref, SECTION_PATH)
        audit_raw, audit_meta = source.get(outcome_ref, AUDIT_PATH)
        for ref in (decision_ref, active_ref, outcome_ref):
            source.get(ref, RULE_PATH)
        confirmed = operation_rows(confirmed_raw, "confirmed_operation")
        active = operation_rows(active_raw, "active_operation")
        ranks = {key(r): r for r in model_rows(rank_raw)}
        audits = {key(r): r for r in model_rows(audit_raw)}
        if not confirmed:
            raise ValueError("no source-confirmed cohort")
        rows = []
        captured = datetime.fromisoformat(capture["server_created_at"].replace("Z", "+00:00"))
        for identity, original in sorted(confirmed.items()):
            if original.get("buy_rank_eligible", "").lower() != "true" or original.get("approved_for_daily", "").lower() != "true":
                raise ValueError("source row was not approved buy-ranked confirmation")
            if identity not in active or identity not in ranks or identity not in audits:
                raise ValueError(f"incomplete frozen lineage {identity}")
            saved_active, rank, audit = active[identity], ranks[identity], audits[identity]
            if any(not rank.get(c) for c in ("model_rank", "display_rank", "model_rank_overall")):
                raise ValueError("missing original ranks")
            price_path = "data/stock_price_history/" + identity[1] + ".csv"
            decision_price, decision_price_meta = source.get(decision_ref, price_path)
            active_price, active_price_meta = source.get(active_ref, price_path)
            terminal_price, terminal_price_meta = source.get(outcome_ref, price_path)
            first = replay(price_frame(active_price), identity[0], saved_active["operation_asof_date"])
            terminal = replay(price_frame(terminal_price), identity[0], audit["operation_asof_date"])
            decision_frame = price_frame(decision_price)
            decision_indices = decision_frame.index[decision_frame["date"].eq(identity[0])].tolist()
            if len(decision_indices) != 1 or decision_indices[0] < 20:
                raise ValueError("missing decision-version target warm-up")
            decision_target = float(decision_frame.iloc[decision_indices[0] - 20:decision_indices[0]]["high"].max())
            if not math.isclose(decision_target, first["target_price"], abs_tol=.000001):
                raise ValueError("post-entry target differs from decision-version previous20 high")
            if not math.isclose(float(saved_active["target_price"]), first["target_price"], abs_tol=.000001):
                raise ValueError("saved active target differs from source replay")
            entry_time = datetime.combine(datetime.strptime(first["entry_date"], "%Y%m%d").date(), time(9), timezone(timedelta(hours=8)))
            if captured >= entry_time:
                raise ValueError("confirmed source was not captured before next-open entry")
            if saved_active.get("entry_date") != first["entry_date"] or not math.isclose(float(saved_active["entry_price"]), first["entry_price"], abs_tol=.000001):
                raise ValueError("saved entry differs from next-open replay")
            if saved_active.get("row_action_status") != first["state"] or audit.get("audit_status") != terminal["state"]:
                raise ValueError("saved lifecycle state differs from independent replay")
            if audit.get("exit_date", "") != terminal["exit_date"] or audit.get("exit_reason", "") != terminal["exit_reason"]:
                raise ValueError("terminal close-confirmed exit differs")
            rows.append(dict(model_id=MODEL_ID, artifact_version=VERSION, signal_date=identity[0], stock_id=identity[1], report_line=identity[2],
                model_rank=rank["model_rank"], display_rank=rank["display_rank"], model_rank_overall=rank["model_rank_overall"], confirmed_buy_rank_eligible="True",
                confirmation_ref=decision_ref, confirmation_artifact_sha256=confirmed_meta["sha256"], confirmation_row_sha256=sha(canonical(original)),
                rank_source_sha256=rank_meta["sha256"], rank_source_row_sha256=sha(canonical(rank)), decision_price_sha256=decision_price_meta["sha256"], decision_target_price=number(decision_target), active_ref=active_ref,
                active_artifact_sha256=active_meta["sha256"], active_row_sha256=sha(canonical(saved_active)), active_price_sha256=active_price_meta["sha256"],
                entry_date=first["entry_date"], entry_price=number(first["entry_price"]), saved_active_state=saved_active["row_action_status"], replayed_active_state=first["state"],
                target_price=number(first["target_price"]), terminal_ref=outcome_ref, terminal_artifact_sha256=audit_meta["sha256"], terminal_row_sha256=sha(canonical(audit)),
                terminal_price_sha256=terminal_price_meta["sha256"], saved_terminal_state=audit["audit_status"], replayed_terminal_state=terminal["state"],
                terminal_target_price=number(terminal["target_price"]), exit_date=terminal["exit_date"], exit_reason=terminal["exit_reason"], rule_lineage_status="frozen_confirmed_active_terminal_rule_consistent",
                economic_unit_status="unverified", return_evidence_allowed="False", promotion_allowed="False"))
        manifest = dict(schema_version=1, artifact_version=VERSION, model_id=MODEL_ID, owner_id=OWNER_ID, producer=PRODUCER,
            refs=dict(decision_ref=decision_ref, active_ref=active_ref, outcome_ref=outcome_ref), github_capture=capture,
            source_files=[meta for _, meta in sorted(source.cache.values(), key=lambda pair: (pair[1]["ref"], pair[1]["path"]))], columns=FIELDS,
            cohort_keys_sha256=sha(canonical([list(k) for k in sorted(confirmed)])), row_hash_definition="SHA256 of full source CSV row canonical JSON; UTF8, sorted keys, compact separators, no value normalization",
            evidence_type="frozen_source_confirmed_lifecycle_implementation_consistency", source_confirmed_mapping_proven=True,
            actual_broker_execution_proven=False, original_first_publication_proven=False, full_research_window_PIT_proven=False,
            production_adapter_consumed_prior_confirmation_proven=False, economic_unit_comparability_proven=False,
            return_evidence_allowed=False, promotion_allowed=False, original_primary_metrics_modified=False,
            legacy_producer_executed=False, production_or_latest_artifacts_written=False,
            limitations=["53-row bounded cohort is not the old1161 or complete model backtest", "GitHub server capture proves repository observed-by, not official first publication", "Original saved confirmed rows support this cohort; production adapter consumption is not proven", "D20 expiry has no realized D20 close price or return", "Corporate action economic units/calendar continuity and full-window PIT remain unverified"])
        return rows, manifest
    finally:
        source.close()


def summaries(rows: list[dict]) -> list[dict[str, str]]:
    values = dict(cohort_rows=len(rows), confirmed_buy_rank_eligible_rows=sum(r["confirmed_buy_rank_eligible"] == "True" for r in rows),
                  matched_next_open_entry_rows=len(rows), source_row_hash_bound_rows=len(rows))
    for field, prefix in (("saved_active_state", "first_active_"), ("saved_terminal_state", "terminal_"), ("report_line", "line_")):
        values.update({prefix + name: count for name, count in sorted(Counter(r[field] for r in rows).items())})
    values.update(return_evidence_allowed="False", promotion_allowed="False")
    return [dict(metric=name, value=str(value), basis="frozen_source_lineage_rule_consistency_not_model_performance") for name, value in values.items()]


def write_csv(path: Path, rows: list[dict], fields: list[str]):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--decision-ref", required=True)
    parser.add_argument("--active-ref", required=True)
    parser.add_argument("--outcome-ref", required=True)
    parser.add_argument("--capture-run-id", type=int, required=True)
    parser.add_argument("--repo-slug", default="LeoChen0727/tdcc-weekly-report")
    args = parser.parse_args()
    repo, output = args.repo_root.resolve(), args.output_root.resolve()
    with model_owned_artifact_guard(repo, output) as guard_receipt:
        rows, manifest = build(repo, args.decision_ref, args.active_ref, args.outcome_ref, capture_metadata(args.repo_slug, args.capture_run_id))
        output.mkdir(parents=True, exist_ok=True)
        write_csv(output / OUTPUT_NAMES[0], rows, FIELDS)
        write_csv(output / OUTPUT_NAMES[1], summaries(rows), ["metric", "value", "basis"])
        manifest.update(**guard_receipt,
                        output_files=[dict(path=name, bytes=(output / name).stat().st_size, sha256=sha((output / name).read_bytes())) for name in OUTPUT_NAMES[:2]])
        (output / OUTPUT_NAMES[2]).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"23EMA原confirmed來源映射 {len(rows)} 列；逐列entry/lifecycle一致；非績效或promotion證據。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
