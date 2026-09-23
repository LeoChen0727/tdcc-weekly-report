"""TDCC 潛伏吸籌：固定中期交易的事後公司行動對帳，不重選股。"""
from __future__ import annotations

import argparse
import base64
from collections import defaultdict
from contextlib import contextmanager
import csv
from datetime import datetime
from decimal import Decimal, localcontext, ROUND_FLOOR
import fnmatch
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import urlparse

from model_research_artifact_guard import load_ownership_rules, load_protected_sentinels, validate_changed_paths

ROOT = Path(__file__).resolve().parents[1]
OWNER = "tdcc_stealth_accumulation_medium_term_corporate_action_reconciliation"
PRODUCER = f"scripts/build_{OWNER}.py"
CONTRACT = f"config/{OWNER}_v1.json"
CONTRACT_SHA256 = "44379fb80db5b6c1f2dd83bed610b31c56fba9d68ca4c9182adc66987ae16f57"
SOURCE_REF = "001b82f856c4ca1a863d64998890fb1fdfba8030"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
KINDS = ("source_manifest_v1.json", "events_v1.csv", "positions_v1.csv.gz", "blocked_v1.csv.gz", "summary_v1.csv", "report_v1.md")
NAMES = {kind: OWNER + "_" + kind for kind in KINDS}
GENERATED = frozenset(NAMES.values())
EXTRA = "source_trade_row_sha256 matched_event_ids theoretical_exit_shares theoretical_whole_shares unresolved_fractional_shares pending_share_rights known_action_gross_price_proxy_pct known_action_costed_proxy_pct reconciliation_status reconciliation_block_reasons corporate_action_coverage_complete verified_total_return_pct reconciliation_total_return_verified reconciliation_formal_use reconciliation_promotion_evidence_allowed".split()
EVENT_FIELDS = "event_id stock_id kind holding_cutoff_date effective_date tradable_date record_date suspension_end share_factor cash_per_old_share documents source_sha256s".split()
BLOCK_FIELDS = "trade_id source_trade_row_sha256 matched_event_ids reconciliation_status reconciliation_block_reasons".split()
SUMMARY_FIELDS = "profile strategy horizon slippage_bps partition original_primary_samples original_primary_mean_net_return_pct matched_known_action_samples theoretical_gross_proxy_samples theoretical_gross_proxy_mean_pct conditional_costed_proxy_samples conditional_costed_proxy_mean_pct fractional_samples pending_rights_samples original_anomaly_candidate_samples corporate_action_coverage_complete total_return_verified formal_use promotion_evidence_allowed".split()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def number(value):
    text = format(value, "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def decimal(value, positive=False):
    result = Decimal(str(value))
    require(result.is_finite() and (result > 0 if positive else result >= 0), "無效或負數公司行動數值")
    return result


def date(value, optional=False):
    if optional and value == "":
        return value
    require(isinstance(value, str) and re.fullmatch(r"\d{8}", value), "日期須為 YYYYMMDD")
    require(datetime.strptime(value, "%Y%m%d").strftime("%Y%m%d") == value, "日期無效")
    return value


def git(root, *arguments):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    return subprocess.check_output(["git", "--no-replace-objects", "-C", str(root), *arguments], env=env)


def validate_events(events):
    seen, economic = set(), set()
    for event in events:
        require(set(event) == set(EVENT_FIELDS) - {"source_sha256s"}, "事件欄位不符")
        require(event["event_id"] and event["event_id"] not in seen, "重複事件")
        key = (event["stock_id"], event["holding_cutoff_date"])
        require(key not in economic, "同股同日重複換股")
        seen.add(event["event_id"]); economic.add(key)
        require(re.fullmatch(r"[1-9]\d{3}", event["stock_id"]), "股票代號錯誤")
        require(event["kind"] == "share_exchange", "本版本僅核定換股事件")
        entitlement, effective = date(event["holding_cutoff_date"]), date(event["effective_date"])
        tradable = date(event["tradable_date"], optional=True)
        require(entitlement <= effective and (not tradable or effective <= tradable), "事件日期順序錯誤")
        require(entitlement <= date(event["record_date"]) <= effective and entitlement <= date(event["suspension_end"]) < effective, "換股基準日或停牌末日錯誤")
        decimal(event["share_factor"], positive=True)
        if event["cash_per_old_share"] != "":
            decimal(event["cash_per_old_share"])
        require(isinstance(event["documents"], list) and event["documents"] and len(set(event["documents"])) == len(event["documents"]), "事件原件引用不完整")


def load_contract(root):
    contract = json.loads((Path(root) / CONTRACT).read_text(encoding="utf-8"))
    require(digest(canonical(contract)) == CONTRACT_SHA256, "契約尚未封存或雜湊不符")
    require(contract["source_ref"] == SOURCE_REF and contract["source_trade_count"] == 305673, "固定來源不可改變")
    require(contract["owner_id"] == OWNER and contract["model_id"] == "tdcc_stealth_accumulation", "owner 不符")
    require(all(contract[k] is False for k in ("coverage_complete", "total_return_verified", "formal_use", "promotion_evidence_allowed", "first_publication_verified")), "研究界線不可解除")
    validate_events(contract["events"])
    require({e["stock_id"] for e in contract["events"]} == {"8422", "5904", "2380"}, "固定三股事件範圍不符")
    for key, doc in contract["documents"].items():
        raw = base64.b64decode(doc["payload_base64"], validate=True)
        require(digest(raw) == doc["sha256"] and len(raw) == doc["bytes"], f"官方原件完整性不符：{key}")
        parsed = urlparse(doc["url"])
        require(parsed.scheme == "https" and parsed.hostname in {"www.twse.com.tw", "www.tpex.org.tw", "mops.twse.com.tw", "mopsov.twse.com.tw"}, "非核定官方來源")
        require(datetime.fromisoformat(doc["retrieved_at"]).strftime("%Y%m%d") >= "20260923", "不可倒填收件時間")
        require(doc["first_publication_verified"] is False and doc["original_revision_chain_verified"] is False, "事後公告不可冒充首次發布")
        require(doc["required_tokens"] and all(t in raw.decode("utf-8-sig") for t in doc["required_tokens"]), "官方原件事件文字不符")
    require(all(set(e["documents"]) <= set(contract["documents"]) for e in contract["events"]), "事件引用未知原件")
    return contract


def reconcile(trade, events):
    """Append retrospective accounting only; never mutate frozen trade columns."""
    validate_events(events)
    entry, exit_ = date(trade["entry_date"]), date(trade["exit_date"])
    require(date(trade["signal_date"]) < entry <= exit_, "固定交易日期錯誤")
    require(trade["horizon"] in {"20", "60"} and trade["slippage_bps"] in {"0", "10", "20"}, "持有期／滑價不符")
    require(trade["primary_row_retained"] == "True" and trade["formal_use"] == "False" and trade["promotion_evidence_allowed"] == "False", "原列研究界線錯誤")
    require(not any(e["stock_id"] == trade["stock_id"] and e["holding_cutoff_date"] <= entry <= e["suspension_end"] for e in events), "原交易進場日落於已知停牌期間，須先查核")
    selected = sorted((e for e in events if e["stock_id"] == trade["stock_id"] and entry < e["holding_cutoff_date"] <= exit_), key=lambda e: (e["holding_cutoff_date"], e["event_id"]))
    reasons = {"corporate_action_coverage_incomplete", "retrospective_not_signal_pit", "dividend_coverage_unverified"}
    gross = costed = ""
    with localcontext() as context:
        context.prec = 50
        original = decimal(trade["shares"], positive=True)
        entry_price = decimal(trade["entry_open"], positive=True)
        exit_price = decimal(trade["exit_close"], positive=True)
        shares, pending = original, Decimal(0)
        last_delivery = ""
        unknown_cash = False
        for event in selected:
            require(not pending and (not last_delivery or last_delivery < event["holding_cutoff_date"]), "前次權利尚未可交易，不猜後續權利計算")
            converted = shares * decimal(event["share_factor"], positive=True)
            if event["tradable_date"] and event["tradable_date"] <= exit_:
                shares = converted
            else:
                pending, shares = converted, Decimal(0)
                reasons.add("share_rights_unsettled_at_original_exit")
            last_delivery = event["tradable_date"]
            if event["cash_per_old_share"] == "":
                unknown_cash = True
                reasons.add("action_cash_amount_unknown")
            elif Decimal(event["cash_per_old_share"]) != 0:
                unknown_cash = True
                reasons.add("action_cash_receipt_unverified")
        whole = shares.to_integral_value(rounding=ROUND_FLOOR)
        fraction = shares - whole
        if fraction:
            reasons.add("fractional_disposition_unverified")
        if not selected:
            reasons.add("no_event_is_not_absence_proof")
        elif not pending:
            gross = number((shares * exit_price / (original * entry_price) - 1) * 100)
            if not fraction and not unknown_cash:
                # Same frozen fee, tax and slippage contract; only theoretical shares differ.
                slip = Decimal(trade["slippage_bps"]) / 10000
                buy_value = original * entry_price * (1 + slip)
                entry_cash = buy_value + max(Decimal(20), buy_value * Decimal("0.001425"))
                require(entry_cash == Decimal(trade["entry_cash"]), "原始進場費稅基準不符")
                sale = shares * exit_price * (1 - slip)
                net = sale - max(Decimal(20), sale * Decimal("0.001425")) - sale * Decimal("0.003")
                costed = number((net / entry_cash - 1) * 100)
        status = "no_registered_action" if not selected else ("known_action_pending" if pending else "known_action_theoretical_only")
        return dict(source_trade_row_sha256=digest(canonical(trade)), matched_event_ids=";".join(e["event_id"] for e in selected), theoretical_exit_shares=number(shares), theoretical_whole_shares=number(whole), unresolved_fractional_shares=number(fraction), pending_share_rights=number(pending), known_action_gross_price_proxy_pct=gross, known_action_costed_proxy_pct=costed, reconciliation_status=status, reconciliation_block_reasons=";".join(sorted(reasons)), corporate_action_coverage_complete="False", verified_total_return_pct="", reconciliation_total_return_verified="False", reconciliation_formal_use="False", reconciliation_promotion_evidence_allowed="False")


def csv_payload(fields, rows):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fields, lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)
    return out.getvalue().encode("utf-8")


@contextmanager
def compressed_writer(fields):
    out = io.BytesIO()
    with gzip.GzipFile(fileobj=out, mode="wb", filename="", mtime=0) as compressed:
        with io.TextIOWrapper(compressed, encoding="utf-8", newline="", write_through=True) as text:
            writer = csv.DictWriter(text, fields, lineterminator="\n")
            writer.writeheader()
            yield writer, out


def source_trades(root, contract):
    info = contract["source_trades"]
    raw = git(root, "show", SOURCE_REF + ":" + info["path"])
    require(digest(raw) == info["sha256"] and len(raw) == info["bytes"], "原始交易 bytes 不符")
    return raw


def build(root=ROOT):
    root = Path(root)
    contract = load_contract(root)
    raw = source_trades(root, contract)
    reader = csv.DictReader(io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(raw)), encoding="utf-8", newline=""))
    fields = reader.fieldnames
    require(fields and len(set(fields)) == len(fields) and not set(fields) & set(EXTRA), "原欄位重複或覆寫")
    seen, stats = set(), defaultdict(lambda: dict(n=0, raw=Decimal(0), matches=0, gross=[], costed=[], fractional=0, pending=0, anomaly=0))
    with compressed_writer(fields + EXTRA) as (positions, pbuf), compressed_writer(BLOCK_FIELDS) as (blocked, bbuf):
        for trade in reader:
            require(None not in trade and None not in trade.values() and trade["trade_id"] not in seen, "交易重複或 CSV 列寬不符")
            seen.add(trade["trade_id"])
            extra = reconcile(trade, contract["events"])
            positions.writerow({**trade, **extra})
            blocked.writerow({field: trade[field] if field in trade else extra[field] for field in BLOCK_FIELDS})
            for partition in (trade["partition"], "all"):
                key = tuple(trade[f] for f in ("profile", "strategy", "horizon", "slippage_bps")) + (partition,)
                group = stats[key]
                group["n"] += 1; group["raw"] += Decimal(trade["net_return_pct"])
                group["matches"] += bool(extra["matched_event_ids"])
                group["fractional"] += Decimal(extra["unresolved_fractional_shares"]) != 0
                group["pending"] += Decimal(extra["pending_share_rights"]) != 0
                group["anomaly"] += trade["anomaly_candidate"] == "True"
                for name, field in (("gross", "known_action_gross_price_proxy_pct"), ("costed", "known_action_costed_proxy_pct")):
                    if extra[field] != "": group[name].append(Decimal(extra[field]))
    require(len(seen) == contract["source_trade_count"], "完整原交易列數不符")
    summaries = []
    for key, group in sorted(stats.items()):
        row = dict(zip(SUMMARY_FIELDS[:5], key))
        row.update(original_primary_samples=group["n"], original_primary_mean_net_return_pct=number(group["raw"] / group["n"]), matched_known_action_samples=group["matches"], theoretical_gross_proxy_samples=len(group["gross"]), theoretical_gross_proxy_mean_pct=number(sum(group["gross"]) / len(group["gross"])) if group["gross"] else "", conditional_costed_proxy_samples=len(group["costed"]), conditional_costed_proxy_mean_pct=number(sum(group["costed"]) / len(group["costed"])) if group["costed"] else "", fractional_samples=group["fractional"], pending_rights_samples=group["pending"], original_anomaly_candidate_samples=group["anomaly"], corporate_action_coverage_complete="False", total_return_verified="False", formal_use="False", promotion_evidence_allowed="False")
        summaries.append(row)
    event_rows = [{**e, "documents": ";".join(e["documents"]), "source_sha256s": ";".join(contract["documents"][d]["sha256"] for d in e["documents"])} for e in contract["events"]]
    report = ("# TDCC 潛伏吸籌：中期公司行動對帳 v1\n\n"
        f"完整保留 {len(seen)} 列固定原交易；不重選股、不改日期、持有期、費稅、滑價與舊候選旗標。\n\n"
        "原始 primary 報酬只是舊 raw-price proxy，未覆寫。新欄位僅套用三個已封存換股事件，並非全市場修正績效。\n\n"
        "theoretical gross proxy 是理論股數乘原退出收盤價的股價可比觀察，包含算術分數股，不代表分數股可出售。conditional costed proxy 僅在整股、已知可交易日、換股現金已明示為零時列出，保留原費稅滑價；仍不含未證實股利、帳戶交付或其他公司行動。\n\n"
        "沒有匹配事件不是無事件證明；未知現金不當零；未交付權利不出售、不延長退出；異常候選保留。summary 兩種新 proxy 各有條件分母，不得與全樣本 primary 混稱修正勝率。\n\n"
        "coverage_complete=False；total_return_verified=False；verified_total_return_pct 全空；formal_use=False；promotion_evidence_allowed=False。官方事後收件不證明首次發布 PIT；沒有真正未見樣本外證據。\n\n"
        "月營收及 EPS、毛利率、營益率、營業利益、業外損益、淨利、季／年財報均未納入。正式模型、adapter、六份 PDF、其他模型及舊研究產物不變。\n")
    payloads = {NAMES["events_v1.csv"]: csv_payload(EVENT_FIELDS, event_rows), NAMES["positions_v1.csv.gz"]: pbuf.getvalue(), NAMES["blocked_v1.csv.gz"]: bbuf.getvalue(), NAMES["summary_v1.csv"]: csv_payload(SUMMARY_FIELDS, summaries), NAMES["report_v1.md"]: report.encode("utf-8")}
    manifest = dict(artifact_version=OWNER + "_v1", owner_id=OWNER, model_id="tdcc_stealth_accumulation", source_ref=SOURCE_REF, source_trades=contract["source_trades"], source_trade_count=len(seen), original_fields=fields, appended_fields=EXTRA, contract_sha256=CONTRACT_SHA256, artifacts={n: {"sha256": digest(b), "bytes": len(b)} for n, b in sorted(payloads.items())}, coverage_complete=False, total_return_verified=False, formal_use=False, promotion_evidence_allowed=False)
    payloads[NAMES["source_manifest_v1.json"]] = json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n"
    return payloads


def snapshot(root):
    """Bind complete Git mappings and existing physical files without materializing sparse paths."""
    allowed = {DIRECTORY + "/" + name for name in GENERATED}
    mappings = []
    paths = set()
    for command in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z")):
        records = []
        for entry in git(root, *command).split(b"\0"):
            if not entry: continue
            path = entry.split(b"\t", 1)[1].decode("utf-8")
            paths.add(path)
            if path not in allowed: records.append(entry)
        mappings.append(digest(b"\0".join(records)))
    for sentinel in load_protected_sentinels(root / "config/model_research_protected_sentinels.csv"):
        require(not sentinel.required or any(fnmatch.fnmatchcase(p, sentinel.artifact_glob) for p in paths), "必要保護來源在 Git 缺失")
    physical = {}
    walk_root = Path("\\\\?\\" + str(root)) if os.name == "nt" and not str(root).startswith("\\\\?\\") else root
    for current, dirs, files in os.walk(walk_root, followlinks=False):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in dirs + files:
            path = Path(current) / name
            relative = path.relative_to(walk_root).as_posix()
            require(not path.is_symlink() and not getattr(path.lstat(), "st_file_attributes", 0) & 0x400, "不可追蹤 reparse/symlink")
            if path.is_file() and relative != ".git" and relative not in allowed:
                physical[relative] = digest(path.read_bytes())
    return mappings, physical


def write_outputs(root, payloads):
    require(set(payloads) == GENERATED and all(isinstance(v, bytes) for v in payloads.values()), "只准寫精確六個新產物")
    paths = [DIRECTORY + "/" + name for name in sorted(GENERATED)]
    require(not validate_changed_paths(OWNER, PRODUCER, paths, load_ownership_rules(root / "config/model_research_artifact_ownership.csv")), "writer 未正確登錄")
    for relative in paths:
        path = root / relative
        for part in [path, *path.parents]:
            if part == root: break
            require(not part.is_symlink() and (not part.exists() or not getattr(part.lstat(), "st_file_attributes", 0) & 0x400), "產物路徑不可 reparse/symlink")
    destination = root / DIRECTORY
    destination.mkdir(parents=True, exist_ok=True)
    for name, payload in payloads.items(): (destination / name).write_bytes(payload)


@contextmanager
def model_owned_artifact_guard(root):
    """Protect all non-owned bytes and Git mappings throughout the producer."""
    before = snapshot(root)
    try:
        yield
    finally:
        require(snapshot(root) == before, "寫入範圍以外檔案或 Git mapping 漂移")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.repository_root.resolve()
    with model_owned_artifact_guard(root):
        write_outputs(root, build(root))
    print(f"{OWNER}: original_rows=305673 artifacts=6 verified_total_returns=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
