"""TDCC 保守成交假設：只回放固定 ledger，保留原 primary 與未知曝險。"""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import contextmanager
import csv
from datetime import datetime, timezone
from decimal import Decimal, localcontext
import fnmatch
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import statistics
import subprocess

from model_research_artifact_guard import load_ownership_rules, load_protected_sentinels, validate_changed_paths

ROOT = Path(__file__).resolve().parents[1]
OWNER = "tdcc_stealth_accumulation_conservative_execution_research"
PRODUCER = f"scripts/build_{OWNER}.py"
CONTRACT = f"config/{OWNER}_v1.json"
CONTRACT_SHA256 = "3c3c0e12a575ae98a6db3eb0a9a9f71b65d7c7a6b17a5b94b690f1ddbdde2b7a"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
KINDS = ("positions_v1.csv.gz", "summary_v1.csv", "report_v1.md", "source_manifest_v1.json")
NAMES = {k: OWNER + "_" + k for k in KINDS}
GENERATED = frozenset(NAMES.values())
EXTRA = "source_trade_row_sha256 execution_model_id execution_cohort_id execution_entry_state execution_exit_state execution_entry_quantity execution_exit_quantity execution_entry_event_ids execution_exit_event_ids execution_entry_reason execution_exit_reason execution_position_state execution_blocking_trade_id execution_lock_retained original_primary_proxy_return_pct execution_proxy_return_pct execution_assumed_completed actual_fill_verified execution_evidence_state exception_coverage_verified".split()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha(value):
    return hashlib.sha256(value).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", "--no-replace-objects", "-C", str(root), *args])


def load_policy(root):
    policy = json.loads((Path(root) / CONTRACT).read_text(encoding="utf-8"))
    require(sha(canonical(policy)) == CONTRACT_SHA256, "封存政策 SHA 不符")
    return policy


def load_ledger(root, policy, source_ledger=None):
    raw = Path(source_ledger).read_bytes() if source_ledger else git(root, "show", policy["source_ref"] + ":" + policy["source_ledger"])
    require(sha(raw) == policy["source_ledger_sha256"], "固定 ledger SHA 不符")
    selected, total = [], 0
    with gzip.open(io.BytesIO(raw), "rt", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        require(fields and not set(fields) & set(EXTRA), "來源欄位與新增欄位衝突")
        for row in reader:
            total += 1
            if all(row[k] == policy[k] for k in ("profile", "partition", "horizon", "slippage_bps")) and row["strategy"] in policy["strategies"]:
                require(row["shares"] == "1000" and int(row["exit_target_index"]) - int(row["entry_index"]) == 20, "原 shares/D20 不符")
                require(row["signal_date"] < row["entry_date"] <= row["exit_date"], "原日期順序不符")
                require(row["primary_row_retained"] == "True" and row["formal_use"] == row["promotion_evidence_allowed"] == "False", "來源研究邊界不符")
                require(Decimal(row["net_return_pct"]) == costed_return(row, policy), "原 primary 費稅算式不符")
                selected.append(row)
    require(total == policy["source_rows"], "來源總列數不符")
    require(Counter(r["strategy"] for r in selected) == policy["strategies"], "固定兩策略樣本數不符")
    require(Counter(r["strategy"] for r in selected if r["anomaly_candidate"] == "True") == policy["original_candidate_counts"], "舊候選數不符")
    require(len({r["trade_id"] for r in selected}) == len(selected), "重複 trade_id")
    return fields, selected, total


def costed_return(row, policy):
    with localcontext() as ctx:
        ctx.prec = 50
        costs = policy["costs"]
        quantity = Decimal(costs["shares"])
        slip = Decimal(policy["slippage_bps"]) / 10000
        buy = quantity * Decimal(row["entry_open"]) * (1 + slip)
        sell = quantity * Decimal(row["exit_close"]) * (1 - slip)
        fee, floor = Decimal(costs["fee_each_side"]), Decimal(costs["minimum_fee_each_side"])
        entry_cash = buy + max(floor, buy * fee)
        net_pnl = sell - max(floor, sell * fee) - sell * Decimal(costs["sell_tax"]) - entry_cash
        return net_pnl / entry_cash * 100


def evaluate_leg(day, stock, policy):
    matched = [e for e in policy["exceptions"] if e["stock_id"] == stock and e["start_date"] <= day and (e["end_date"] is None or day <= e["end_date"])]
    if not matched:
        return "assumed_regular_price_proxy", 1000, "", "bounded_normal_regime_assumption_not_verified"
    ids = ";".join(sorted(e["event_id"] for e in matched))
    reasons = ";".join(sorted({e["reason"] for e in matched}))
    if any(e["state"] == "evidenced_no_fill" and e.get("full_validity_covered") is True for e in matched):
        return "evidenced_no_fill", 0, ids, reasons
    partial = [e for e in matched if e["state"] == "partial_fill_out_of_scope"]
    if partial:
        quantities = {e.get("supported_quantity") for e in partial}
        require(len(quantities) == 1, "部分成交證據量衝突")
        qty = next(iter(quantities))
        require(type(qty) is int and 0 < qty < 1000, "部分成交須為整數0<qty<1000")
        return "partial_fill_out_of_scope", qty, ids, reasons
    return "unknown", "", ids, reasons


def replay(rows, policy):
    result, locks, events = {}, {}, []
    for original in rows:
        trade_id = original["trade_id"]
        require(trade_id not in result, "重複 replay trade_id")
        result[trade_id] = dict(original, **dict.fromkeys(EXTRA, ""))
        result[trade_id].update(source_trade_row_sha256=sha(canonical(original)), execution_model_id=policy["model_id"], execution_cohort_id=policy["cohort_id"], original_primary_proxy_return_pct=original["net_return_pct"], execution_assumed_completed=False, actual_fill_verified=False, execution_evidence_state="unknown", exception_coverage_verified=False, execution_lock_retained=False)
        events.extend([(original["entry_date"], 0, trade_id), (original["exit_date"], 1, trade_id)])
    for day, phase, trade_id in sorted(events):
        row = result[trade_id]
        key = (policy["model_id"], row["strategy"], policy["cohort_id"], row["stock_id"])
        if phase == 0:
            if key in locks:
                row.update(execution_entry_state="blocked_existing_lock", execution_exit_state="not_evaluated_entry_unresolved", execution_position_state="lock_blocked", execution_blocking_trade_id=locks[key], execution_entry_reason="prior_position_lock_not_released", execution_lock_retained=True)
                continue
            state, qty, ids, reason = evaluate_leg(day, row["stock_id"], policy)
            row.update(execution_entry_state=state, execution_entry_quantity=qty, execution_entry_event_ids=ids, execution_entry_reason=reason)
            if state == "evidenced_no_fill":
                row.update(execution_position_state="no_entry", execution_exit_state="not_applicable_no_entry")
                continue
            locks[key] = trade_id
            row["execution_lock_retained"] = True
            row["execution_position_state"] = {"unknown": "entry_unknown", "partial_fill_out_of_scope": "entry_partial", "assumed_regular_price_proxy": "assumed_active"}[state]
        elif row["execution_position_state"] not in {"no_entry", "lock_blocked"}:
            if row["execution_entry_state"] != "assumed_regular_price_proxy":
                row["execution_exit_state"] = "not_evaluated_entry_unresolved"
                continue
            state, qty, ids, reason = evaluate_leg(day, row["stock_id"], policy)
            row.update(execution_exit_state=state, execution_exit_quantity=qty, execution_exit_event_ids=ids, execution_exit_reason=reason)
            if state == "assumed_regular_price_proxy":
                row.update(execution_position_state="assumed_closed", execution_assumed_completed=True, execution_proxy_return_pct=str(costed_return(row, policy)), execution_lock_retained=False)
                require(locks.pop(key) == trade_id, "鎖的持有人不符")
            else:
                row["execution_position_state"] = {"unknown": "exit_unknown", "partial_fill_out_of_scope": "exit_partial", "evidenced_no_fill": "exit_no_fill"}[state]
    return sorted(result.values(), key=lambda r: (r["strategy"], r["entry_date"], r["trade_id"]))


def statistics_row(values):
    n = len(values)
    counts = dict(win_count=sum(x > 0 for x in values), neutral_count=sum(x == 0 for x in values), failure_count=sum(x < 0 for x in values))
    with localcontext() as ctx:
        ctx.prec = 50
        rates = {k.replace("count", "rate_pct"): str(Decimal(v) / n * 100) if n else "" for k, v in counts.items()}
        return dict(samples=n, **counts, **rates, mean_net_return_pct=str(sum(values) / n) if n else "", median_net_return_pct=str(statistics.median(values)) if n else "", high_return_ge10_rate_pct=str(Decimal(sum(x >= 10 for x in values)) / n * 100) if n else "", loss_le_minus10_rate_pct=str(Decimal(sum(x <= -10 for x in values)) / n * 100) if n else "", min_net_return_pct=str(min(values)) if n else "", max_net_return_pct=str(max(values)) if n else "")


def summarize(rows):
    summaries = []
    for strategy in ("baseline_4", "trend_8"):
        base = [r for r in rows if r["strategy"] == strategy]
        assumed = [r for r in base if r["execution_assumed_completed"]]
        for population, selected, field in (("original_primary_proxy", base, "net_return_pct"), ("assumed_completed_subset", assumed, "execution_proxy_return_pct"), ("original_candidate_exclusion_sensitivity", [r for r in base if r["anomaly_candidate"] != "True"], "net_return_pct"), ("assumed_completed_candidate_exclusion_sensitivity", [r for r in assumed if r["anomaly_candidate"] != "True"], "execution_proxy_return_pct")):
            summaries.append(dict(strategy=strategy, population=population, primary_samples=len(base), assumed_completed_samples=len(assumed), execution_not_computable_samples=len(base)-len(assumed), execution_not_computable_pct=str(Decimal(len(base)-len(assumed))/len(base)*100) if base else "", execution_evidence_unknown_samples=len(base), original_candidate_samples=sum(r["anomaly_candidate"] == "True" for r in base), population_candidate_samples=sum(r["anomaly_candidate"] == "True" for r in selected), stocks=len({r["stock_id"] for r in selected}), signal_dates=len({r["signal_date"] for r in selected}), **statistics_row([Decimal(r[field]) for r in selected]), actual_fill_verified=False, execution_evidence_state="unknown", formal_use=False, promotion_evidence_allowed=False))
    return summaries


def csv_bytes(rows, fields=None):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields or list(rows[0]), lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def report(rows, summary, started):
    lines = ["# TDCC 潛伏吸籌：保守成交假設研究 v1", "", "本次為 frozen-ledger replay；原 primary 全保留，不是實際成交、正式勝率或正式升級。", "已看過 validation 非未見 OOS；current-version 非首次發布 PIT。", "", f"政策固定：2026-09-30T15:29:39+00:00；replay_started_at={started}。", "", "## 固定比較與分母", "", "common_12 / validation / D20 / 1,000股 / 10bps；雙邊費率0.001425最低20，賣出稅0.003。", "所有列的 execution_evidence_state=unknown、actual_fill_verified=False；下表可計算只代表已假設完成。", "全市場例外清單未核實，不把一般假設稱 verified_normal。", "", "| 策略 | 統計母體 | N | 候選數 | 勝/中立/失敗 | 平均% | 中位數% | >=10%比例 | <=-10%比例 |", "|---|---|---:|---:|---|---:|---:|---:|---:|"]
    for s in summary:
        fmt = lambda key: f"{Decimal(s[key]):.6f}" if s[key] != "" else "未知"
        lines.append(f"| {s['strategy']} | {s['population']} | {s['samples']} | {s['population_candidate_samples']} | {s['win_count']}/{s['neutral_count']}/{s['failure_count']} | {fmt('mean_net_return_pct')} | {fmt('median_net_return_pct')} | {fmt('high_return_ge10_rate_pct')} | {fmt('loss_le_minus10_rate_pct')} |")
    lines.extend(["", "原候選排除僅為既有敏感度，不是修正主績效；假設完成子集的平均／勝率不能代表全母體。", "", "## 全母體狀態", ""])
    for strategy in ("baseline_4", "trend_8"):
        group = [r for r in rows if r["strategy"] == strategy]
        s = next(s for s in summary if s['strategy'] == strategy)
        lines.append(f"- {strategy}：原primary {len(group)}；不可計算 {s['execution_not_computable_samples']}（{Decimal(s['execution_not_computable_pct']):.6f}%）；狀態 {dict(sorted(Counter(r['execution_position_state'] for r in group).items()))}。")
    lines.extend(["", "## 已證例外與傳遞鎖", "", "例外按股票及官方日期套用全部 ledger 列，不使用報酬挑選或用TickType/成交量推論成交。", "同模型/strategy/固定common12-validation/stock按日期處理；unknown/partial及未完成exit保留鎖；後續受阻列不刪除。", "", "| 策略 | 股票 | signal | entry | exit | entry狀態 | exit狀態 | 最終狀態 | 原primary% | 新proxy% | 阻擋trade_id |", "|---|---|---|---|---|---|---|---|---:|---:|---|"])
    for r in rows:
        if r['stock_id'] in {'2492', '6806'}:
            lines.append("| " + " | ".join(str(r[k]) for k in ("strategy", "stock_id", "signal_date", "entry_date", "exit_date", "execution_entry_state", "execution_exit_state", "execution_position_state", "original_primary_proxy_return_pct", "execution_proxy_return_pct", "execution_blocking_trade_id")) + " |")
    lines.extend(["", "## 數值警訊及結論界線", "", "沿用已完成的候選／價位／費稅查核，所有235/144舊候選留在primary，不新增cutoff，不把大幅報酬判錯。", "不能將排除未知交易後的子集變化解讀成策略變好或變差；特殊制度與正負交易都可能使樣本無法計算。", "四日OHLC既有官方對帳相符；Tick與日量盤別範圍不同，總量差不等於漏檔，也不是1,000股分配證明。", "6806公告6/23下市不是本輪已核實執行；已知制度未核實結束日只維持研究unknown。", "不補舊nonoverlap略過訊號，無法推論完整訊號序列重播結果；不新增試單/延後買賣/改D20。", "月營收及季年財報不納入；formal_use=False、promotion_evidence_allowed=False。", "", "## 重現", "", f"`python -B {PRODUCER} --source-ledger <唯讀既有F來源>`", f"`python -B scripts/validate_{OWNER}.py --source-ledger <同一來源>`", "新主表保留每個原欄位與source_trade_row_sha256；source_manifest列來源、政策hash、精確產物hash。付費raw CSV不納repo。", ""])
    return "\n".join(lines).encode("utf-8")


def snapshot(root):
    """Existing technical guard pattern: compare Git mappings and physical non-owned bytes."""
    allowed = {DIRECTORY + "/" + n for n in GENERATED}
    mappings, paths = [], set()
    for command in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z")):
        kept = []
        for entry in git(root, *command).split(b"\0"):
            if not entry: continue
            path = entry.split(b"\t", 1)[1].decode("utf-8")
            paths.add(path)
            if path not in allowed: kept.append(entry)
        mappings.append(sha(b"\0".join(kept)))
    for item in load_protected_sentinels(root / "config/model_research_protected_sentinels.csv"):
        require(not item.required or any(fnmatch.fnmatchcase(p, item.artifact_glob) for p in paths), "必要保護來源在Git缺失")
    physical = {}
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            path = Path(current) / name
            rel = path.relative_to(root).as_posix()
            if rel != ".git" and rel not in allowed:
                physical[rel] = sha(path.read_bytes())
    return mappings, physical


@contextmanager
def model_owned_artifact_guard(root):
    before = snapshot(root)
    try:
        yield before
    finally:
        require(snapshot(root) == before, "非本次產物 bytes 或 Git mapping 改變")


def build(root, source_ledger=None):
    policy = load_policy(root)
    started = datetime.now(timezone.utc).isoformat()
    require(datetime.fromisoformat(policy["policy_fixed_at"]) < datetime.fromisoformat(started), "政策須先於replay固定")
    fields, source, total = load_ledger(root, policy, source_ledger)
    rows = replay(source, policy)
    summary = summarize(rows)
    payloads = {NAMES['positions_v1.csv.gz']: gzip.compress(csv_bytes(rows, fields + EXTRA), mtime=0), NAMES['summary_v1.csv']: csv_bytes(summary), NAMES['report_v1.md']: report(rows, summary, started)}
    manifest = dict(artifact_version=policy['artifact_version'], owner_id=OWNER, model_id=policy['model_id'], replay_kind=policy['replay_kind'], policy_fixed_at=policy['policy_fixed_at'], replay_started_at=started, policy_canonical_sha256=CONTRACT_SHA256, source_ref=policy['source_ref'], source_ledger=policy['source_ledger'], source_ledger_sha256=policy['source_ledger_sha256'], source_rows=total, selected_rows=len(rows), source_fields=fields, appended_fields=EXTRA, cohort_id=policy['cohort_id'], source_row_preservation='all original fields unchanged', state_counts=dict(Counter(r['execution_position_state'] for r in rows)), artifacts={name: dict(sha256=sha(raw), bytes=len(raw)) for name, raw in sorted(payloads.items())}, actual_fill_verified=False, execution_evidence_state='unknown', exception_coverage_verified=False, formal_use=False, promotion_evidence_allowed=False)
    payloads[NAMES['source_manifest_v1.json']] = json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2).encode('utf-8') + b'\n'
    return payloads


def write_outputs(root, payloads):
    require(set(payloads) == GENERATED, "只准寫四個精確新產物")
    paths = [DIRECTORY + "/" + n for n in sorted(GENERATED)]
    require(not validate_changed_paths(OWNER, PRODUCER, paths, load_ownership_rules(root / 'config/model_research_artifact_ownership.csv')), "writer/allowlist尚未登錄")
    for name, raw in payloads.items():
        destination = root / DIRECTORY / name
        require(not destination.is_symlink(), "產物不可為symlink")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository-root', type=Path, default=ROOT)
    parser.add_argument('--source-ledger', type=Path)
    args = parser.parse_args(argv)
    root = args.repository_root.resolve()
    with model_owned_artifact_guard(root) as protected:
        payloads = build(root, args.source_ledger)
        write_outputs(root, payloads)
        if args.source_ledger:
            require(sha(args.source_ledger.read_bytes()) == load_policy(root)['source_ledger_sha256'], '舊ledger bytes改變')
    print(json.dumps(dict(owner=OWNER, artifacts=4, selected_rows=7967, source_bytes_unchanged=True, protected_non_owned_bytes_unchanged=True, protected_physical_files=len(protected[1]), protected_git_mapping_sha256=protected[0]), ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
