"""獨立驗證 TDCC 潛伏吸籌固定交易對帳；不匯入 producer 或模型商業邏輯。"""
from __future__ import annotations

import argparse
import base64
from collections import defaultdict
import csv
from datetime import datetime
from decimal import Decimal, localcontext
import gzip
import hashlib
import io
import itertools
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OWNER = "tdcc_stealth_accumulation_medium_term_corporate_action_reconciliation"
CONTRACT_PATH = f"config/{OWNER}_v1.json"
CONTRACT_SHA256 = "44379fb80db5b6c1f2dd83bed610b31c56fba9d68ca4c9182adc66987ae16f57"
SOURCE_REF = "001b82f856c4ca1a863d64998890fb1fdfba8030"
SOURCE_PATH = "output/research/tdcc_stealth_accumulation/tdcc_stealth_accumulation_medium_term_trend_research_trades_v1.csv.gz"
SOURCE_SHA256 = "0636fc459583c5e8620fa0c42c948a3d4aaa215e15a6ae27019476d1b9875cc0"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
KINDS = ("source_manifest_v1.json", "events_v1.csv", "positions_v1.csv.gz", "blocked_v1.csv.gz", "summary_v1.csv", "report_v1.md")
APPENDED = "source_trade_row_sha256 matched_event_ids theoretical_exit_shares theoretical_whole_shares unresolved_fractional_shares pending_share_rights known_action_gross_price_proxy_pct known_action_costed_proxy_pct reconciliation_status reconciliation_block_reasons corporate_action_coverage_complete verified_total_return_pct reconciliation_total_return_verified reconciliation_formal_use reconciliation_promotion_evidence_allowed".split()
EVENT_FIELDS = "event_id stock_id kind holding_cutoff_date effective_date tradable_date record_date suspension_end share_factor cash_per_old_share documents source_sha256s".split()
BLOCK_FIELDS = "trade_id source_trade_row_sha256 matched_event_ids reconciliation_status reconciliation_block_reasons".split()
SUMMARY_FIELDS = "profile strategy horizon slippage_bps partition original_primary_samples original_primary_mean_net_return_pct matched_known_action_samples theoretical_gross_proxy_samples theoretical_gross_proxy_mean_pct conditional_costed_proxy_samples conditional_costed_proxy_mean_pct fractional_samples pending_rights_samples original_anomaly_candidate_samples corporate_action_coverage_complete total_return_verified formal_use promotion_evidence_allowed".split()
DOCUMENT_PINS = {
    "twse_8422_20251021": "f97a7cd9abd7d99751efe67ad49a96dcf6b0ee190fa10b1251b59d320b599cc0",
    "tpex_5904_20260714": "f0f91641e67cf1a6320eccd11414a6d364dd7dbeca60d1f6e3b3e54d4fa77196",
    "twse_2380_20260522": "2d970a454ac03c5ef94a0ca27882e9eef47715a4dd8b07a43c4ac362656bb807",
}
FACTS = (
    ("8422", "20251106", "20251114", "20251117", "10", "twse_8422_20251021"),
    ("5904", "20260730", "20260807", "20260810", "10", "tpex_5904_20260714"),
    ("2380", "20260617", "20260626", "20260629", "0.27658171", "twse_2380_20260522"),
)


def check(value, message):
    if not value: raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def sha(payload):
    return hashlib.sha256(payload).hexdigest()


def text(value):
    raw = format(value, "f")
    return raw.rstrip("0").rstrip(".") if "." in raw else raw


def unique(pairs):
    result = {}
    for key, value in pairs:
        check(key not in result, "JSON duplicate key")
        result[key] = value
    return result


def read_json(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=unique)


def csv_reader(raw, compressed=False):
    binary = gzip.GzipFile(fileobj=io.BytesIO(raw)) if compressed else io.BytesIO(raw)
    result = csv.DictReader(io.TextIOWrapper(binary, encoding="utf-8", newline=""))
    check(result.fieldnames and len(result.fieldnames) == len(set(result.fieldnames)), "CSV fields duplicate or absent")
    return result


def contract(root):
    obj = read_json((root / CONTRACT_PATH).read_bytes())
    check(sha(canonical(obj)) == CONTRACT_SHA256, "contract pin mismatch")
    check(obj["source_ref"] == SOURCE_REF and obj["source_trades"] == {"path": SOURCE_PATH, "bytes": 30352445, "sha256": SOURCE_SHA256}, "frozen input changed")
    check(obj["source_trade_count"] == 305673 and obj["owner_id"] == OWNER and obj["model_id"] == "tdcc_stealth_accumulation", "source count or owner mismatch")
    for flag in ("coverage_complete", "total_return_verified", "formal_use", "promotion_evidence_allowed", "first_publication_verified"):
        check(obj[flag] is False, "research-only flag changed")
    check(set(obj["documents"]) == set(DOCUMENT_PINS), "official receipt set mismatch")
    raw_docs = {}
    for name, expected in DOCUMENT_PINS.items():
        doc = obj["documents"][name]
        raw = base64.b64decode(doc["payload_base64"], validate=True)
        check(sha(raw) == expected == doc["sha256"] and len(raw) == doc["bytes"], "official bytes mismatch")
        check(doc["first_publication_verified"] is False and doc["original_revision_chain_verified"] is False, "retrospective receipt falsely upgraded")
        check(datetime.fromisoformat(doc["retrieved_at"]).strftime("%Y%m%d") >= "20260923", "retrieval timestamp backdated")
        raw_docs[name] = raw.decode("utf-8")
    # Independent factual tokens, not the producer's configurable token list.
    tokens = {
        "twse_8422_20251021": ("8422", "每1股換發新股票10股", "114年11月6日起至114年11月14日止", "民國114年11月17日"),
        "tpex_5904_20260714": ("寶雅國際股份有限公司", "每1股換發新股票10股", "115年7月30日至115年8月7日", "115年8月10日"),
        "twse_2380_20260522": ("2380", "每壹仟股換發新股票276.58171股", "115年6月17日起至115年6月26日止", "115年6月29日"),
    }
    for name, expected in tokens.items(): check(all(token in raw_docs[name] for token in expected), "official fact token mismatch")
    expected_events = []
    for sid, cutoff, record, tradable, factor, doc in FACTS:
        expected_events.append(dict(event_id=f"{sid}_share_exchange_{tradable}", stock_id=sid, kind="share_exchange", holding_cutoff_date=cutoff, effective_date=tradable, tradable_date=tradable, record_date=record, suspension_end=record, share_factor=factor, cash_per_old_share="", documents=[doc]))
    check(obj["events"] == expected_events, "event facts differ from independently fixed official receipts")
    return obj


def accounting(trade, events):
    """Independent share-unit computation; output remains conditional, not realized."""
    source_dates = [trade[key] for key in ("signal_date", "entry_date", "exit_date")]
    for value in source_dates:
        check(re.fullmatch(r"\d{8}", value) and datetime.strptime(value, "%Y%m%d").strftime("%Y%m%d") == value, "invalid source date")
    signal, entry, exit_ = source_dates
    check(signal < entry <= exit_, "source date order")
    check(trade["horizon"] in {"20", "60"} and trade["slippage_bps"] in {"0", "10", "20"}, "operation rule changed")
    check(trade["primary_row_retained"] == "True" and trade["formal_use"] == "False" and trade["promotion_evidence_allowed"] == "False", "source restrictions changed")
    check(not any(e["stock_id"] == trade["stock_id"] and e["holding_cutoff_date"] <= entry <= e["suspension_end"] for e in events), "entry during suspension")
    actions = sorted([e for e in events if e["stock_id"] == trade["stock_id"] and entry < e["holding_cutoff_date"] <= exit_], key=lambda e: (e["holding_cutoff_date"], e["event_id"]))
    reasons = {"corporate_action_coverage_incomplete", "retrospective_not_signal_pit", "dividend_coverage_unverified"}
    with localcontext() as context:
        context.prec = 50
        initial, buy, sell = (Decimal(trade[key]) for key in ("shares", "entry_open", "exit_close"))
        check(all(value.is_finite() and value > 0 for value in (initial, buy, sell)), "nonpositive source price or shares")
        deliverable, pending, last_delivery, action_cash_unknown = initial, Decimal(0), "", False
        for action in actions:
            check(not pending and (not last_delivery or last_delivery < action["holding_cutoff_date"]), "overlapping unsettled rights")
            theoretical = deliverable * Decimal(action["share_factor"])
            if action["tradable_date"] and action["tradable_date"] <= exit_:
                deliverable = theoretical
            else:
                deliverable, pending = Decimal(0), theoretical
                reasons.add("share_rights_unsettled_at_original_exit")
            last_delivery = action["tradable_date"]
            if action["cash_per_old_share"] == "":
                action_cash_unknown = True; reasons.add("action_cash_amount_unknown")
            elif Decimal(action["cash_per_old_share"]) != 0:
                action_cash_unknown = True; reasons.add("action_cash_receipt_unverified")
        integer_shares = Decimal(int(deliverable))
        fraction = deliverable % 1
        if fraction: reasons.add("fractional_disposition_unverified")
        gross, net_proxy = "", ""
        if not actions: reasons.add("no_event_is_not_absence_proof")
        elif pending == 0:
            gross = text(100 * (sell * deliverable - buy * initial) / (buy * initial))
            if fraction == 0 and not action_cash_unknown:
                rate = Decimal(trade["slippage_bps"]) / Decimal(10000)
                outlay = initial * buy * (1 + rate)
                outlay += max(outlay * Decimal("0.001425"), Decimal(20))
                check(outlay == Decimal(trade["entry_cash"]), "frozen entry fee mismatch")
                proceeds = deliverable * sell * (1 - rate)
                deduction = max(Decimal(20), proceeds * Decimal("0.001425")) + proceeds * Decimal("0.003")
                net_proxy = text(100 * (proceeds - deduction - outlay) / outlay)
        state = "no_registered_action" if not actions else ("known_action_pending" if pending else "known_action_theoretical_only")
        return dict(source_trade_row_sha256=sha(canonical(trade)), matched_event_ids=";".join(e["event_id"] for e in actions), theoretical_exit_shares=text(deliverable), theoretical_whole_shares=text(integer_shares), unresolved_fractional_shares=text(fraction), pending_share_rights=text(pending), known_action_gross_price_proxy_pct=gross, known_action_costed_proxy_pct=net_proxy, reconciliation_status=state, reconciliation_block_reasons=";".join(sorted(reasons)), corporate_action_coverage_complete="False", verified_total_return_pct="", reconciliation_total_return_verified="False", reconciliation_formal_use="False", reconciliation_promotion_evidence_allowed="False")


def same(actual, expected, key):
    if key in {"known_action_gross_price_proxy_pct", "known_action_costed_proxy_pct"} and actual != "" and expected != "":
        check(abs(Decimal(actual) - Decimal(expected)) < Decimal("1e-40"), f"independent arithmetic mismatch: {key}")
    else: check(actual == expected, f"independent field mismatch: {key}")


def approved_report(row_count):
    """Exact v1 narrative contract; keeping keywords cannot conceal contradictory prose."""
    return ("# TDCC 潛伏吸籌：中期公司行動對帳 v1\n\n"
        f"完整保留 {row_count} 列固定原交易；不重選股、不改日期、持有期、費稅、滑價與舊候選旗標。\n\n"
        "原始 primary 報酬只是舊 raw-price proxy，未覆寫。新欄位僅套用三個已封存換股事件，並非全市場修正績效。\n\n"
        "theoretical gross proxy 是理論股數乘原退出收盤價的股價可比觀察，包含算術分數股，不代表分數股可出售。conditional costed proxy 僅在整股、已知可交易日、換股現金已明示為零時列出，保留原費稅滑價；仍不含未證實股利、帳戶交付或其他公司行動。\n\n"
        "沒有匹配事件不是無事件證明；未知現金不當零；未交付權利不出售、不延長退出；異常候選保留。summary 兩種新 proxy 各有條件分母，不得與全樣本 primary 混稱修正勝率。\n\n"
        "coverage_complete=False；total_return_verified=False；verified_total_return_pct 全空；formal_use=False；promotion_evidence_allowed=False。官方事後收件不證明首次發布 PIT；沒有真正未見樣本外證據。\n\n"
        "月營收及 EPS、毛利率、營益率、營業利益、業外損益、淨利、季／年財報均未納入。正式模型、adapter、六份 PDF、其他模型及舊研究產物不變。\n").encode("utf-8")


def validate_payloads(root, cfg, payloads, source_raw):
    names = {OWNER + "_" + suffix for suffix in KINDS}
    check(set(payloads) == names and all(isinstance(v, bytes) for v in payloads.values()), "exact six artifacts required")
    manifest = read_json(payloads[OWNER + "_source_manifest_v1.json"])
    for key, expected in {"artifact_version": OWNER + "_v1", "owner_id": OWNER, "model_id": "tdcc_stealth_accumulation", "source_ref": SOURCE_REF, "source_trades": cfg["source_trades"], "source_trade_count": cfg["source_trade_count"], "contract_sha256": CONTRACT_SHA256, "appended_fields": APPENDED, "coverage_complete": False, "total_return_verified": False, "formal_use": False, "promotion_evidence_allowed": False}.items(): check(manifest[key] == expected, f"manifest {key} mismatch")
    bound = {n: {"sha256": sha(raw), "bytes": len(raw)} for n, raw in payloads.items() if not n.endswith("source_manifest_v1.json")}
    check(manifest["artifacts"] == bound, "artifact bytes binding mismatch")
    check(sha(source_raw) == cfg["source_trades"]["sha256"] and len(source_raw) == cfg["source_trades"]["bytes"], "frozen source bytes changed")
    original = csv_reader(source_raw, True)
    positions = csv_reader(payloads[OWNER + "_positions_v1.csv.gz"], True)
    blocked = csv_reader(payloads[OWNER + "_blocked_v1.csv.gz"], True)
    check(manifest["original_fields"] == original.fieldnames and positions.fieldnames == original.fieldnames + APPENDED and blocked.fieldnames == BLOCK_FIELDS, "source/appended schema mismatch")
    seen, groups = set(), defaultdict(list)
    for old, new, block in itertools.zip_longest(original, positions, blocked):
        check(old is not None and new is not None and block is not None, "lost or extra frozen rows")
        check(None not in old and None not in new and None not in block and None not in old.values() and None not in new.values() and None not in block.values(), "malformed CSV row")
        check(old["trade_id"] not in seen, "duplicate source trade")
        seen.add(old["trade_id"])
        check(all(new[k] == old[k] for k in original.fieldnames), "frozen original field changed")
        expected = accounting(old, cfg["events"])
        for key in APPENDED: same(new[key], expected[key], key)
        check(block == {key: old[key] if key in old else new[key] for key in BLOCK_FIELDS}, "blocked row mismatch")
        data = (Decimal(old["net_return_pct"]), bool(new["matched_event_ids"]), Decimal(new["known_action_gross_price_proxy_pct"]) if new["known_action_gross_price_proxy_pct"] else None, Decimal(new["known_action_costed_proxy_pct"]) if new["known_action_costed_proxy_pct"] else None, Decimal(new["unresolved_fractional_shares"]) != 0, Decimal(new["pending_share_rights"]) != 0, old["anomaly_candidate"] == "True")
        for part in (old["partition"], "all"):
            groups[tuple(old[k] for k in SUMMARY_FIELDS[:4]) + (part,)].append(data)
    check(len(seen) == cfg["source_trade_count"], "source row count mismatch")
    summaries = csv_reader(payloads[OWNER + "_summary_v1.csv"])
    check(summaries.fieldnames == SUMMARY_FIELDS, "summary schema mismatch")
    actual = list(summaries)
    check(len(actual) == len(groups), "summary population coverage mismatch")
    for row, (key, observations) in zip(actual, sorted(groups.items())):
        check(tuple(row[k] for k in SUMMARY_FIELDS[:5]) == key, "summary group mismatch")
        gross = [r[2] for r in observations if r[2] is not None]
        net = [r[3] for r in observations if r[3] is not None]
        values = [len(observations), sum(r[0] for r in observations) / len(observations), sum(r[1] for r in observations), len(gross), sum(gross) / len(gross) if gross else "", len(net), sum(net) / len(net) if net else "", sum(r[4] for r in observations), sum(r[5] for r in observations), sum(r[6] for r in observations)]
        for name, value in zip(SUMMARY_FIELDS[5:15], values): check(row[name] == (text(value) if isinstance(value, Decimal) else str(value)), f"summary metric mismatch: {name}")
        check(all(row[k] == "False" for k in SUMMARY_FIELDS[15:]), "summary claimed formal result")
    events = csv_reader(payloads[OWNER + "_events_v1.csv"])
    check(events.fieldnames == EVENT_FIELDS, "event schema mismatch")
    expected_events = [{**e, "documents": ";".join(e["documents"]), "source_sha256s": ";".join(cfg["documents"][d]["sha256"] for d in e["documents"])} for e in cfg["events"]]
    check(list(events) == expected_events, "published events mismatch")
    check(payloads[OWNER + "_report_v1.md"] == approved_report(len(seen)), "report caveats or exact approved narrative changed")
    return len(seen)


def validate(root=ROOT):
    root = Path(root).resolve()
    cfg = contract(root)
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    source = subprocess.check_output(["git", "--no-replace-objects", "-C", str(root), "show", SOURCE_REF + ":" + SOURCE_PATH], env=env)
    output = root / DIRECTORY
    expected = {OWNER + "_" + kind for kind in KINDS}
    check({p.name for p in output.glob(OWNER + "_*")} == expected, "unexpected or missing artifact file")
    for name in expected:
        path = output / name
        check(not any(p.is_symlink() or (p.exists() and getattr(p.lstat(), "st_file_attributes", 0) & 0x400) for p in [path, *path.parents]), "artifact symlink/reparse forbidden")
    return validate_payloads(root, cfg, {n: (output / n).read_bytes() for n in expected}, source)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    count = validate(args.repository_root)
    print(f"validated_original_rows={count} known_actions=3 total_return_verified=False")
    return 0


if __name__ == "__main__": raise SystemExit(main())
