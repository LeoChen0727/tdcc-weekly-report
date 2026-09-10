"""TDCC 潛伏吸籌：固定四股研究的公司行動帳務，不重跑模型或認證總報酬。"""
from __future__ import annotations

import argparse
import base64
from collections import Counter, defaultdict
from contextlib import contextmanager
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_FLOOR, localcontext
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess

from model_research_artifact_guard import load_ownership_rules, validate_changed_paths

ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
OWNER_ID = "tdcc_stealth_accumulation_corporate_action_ledger"
PRODUCER = "scripts/build_tdcc_stealth_accumulation_corporate_action_ledger.py"
CONTRACT_FILE = "config/tdcc_stealth_accumulation_corporate_action_ledger_v1.json"
CONTRACT_SHA256 = "78bfd1c8fd6da0f95ae6659218144b79add312048da807d8dceeb75e02b2aa7f"
SOURCE_REF = "3fe40157cf4b333ef03a1447e45c310d197cbc5b"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
KINDS = ("source_manifest_v1.json", "events_v1.csv", "positions_v1.csv", "blocked_v1.csv", "report_v1.md")
GENERATED = {OWNER_ID + "_" + kind for kind in KINDS}
FLAGS = {"formal_use": "False", "promotion_evidence_allowed": "False", "total_return_verified": "False"}
EVENT_FIELDS = "event_id stock_id stock_name kind entitlement_date effective_date tradable_date scheduled_payment_date actual_payment_date share_factor new_shares_per_old_share cash_per_old_share record_date suspension_start suspension_end payment_confirmed payment_confirmation_ref document_ids document_sha256s source_availability coverage_complete formal_use promotion_evidence_allowed total_return_verified".split()
POSITION_FIELDS = "trade_id stock_id stock_name signal_date horizon slippage_bps entry_date exit_date entry_open exit_close source_shares source_signal_sha256 source_trade_sha256 source_row_json matched_event_ids known_event_share_balance eligible_whole_share_component unresolved_fractional_share_component pending_share_rights announced_gross_cash_entitlement unsettled_gross_cash_entitlement confirmed_cash_receipt corporate_action_status block_reasons original_strict_v3_status strict_lock_released original_proxy_net_return_pct verified_total_return_pct coverage_complete anomaly_disposition primary_row_retained formal_use promotion_evidence_allowed total_return_verified".split()
BLOCKED_FIELDS = "record_type stock_id signal_date horizon trade_id status reasons source_row_sha256 source_row_json primary_row_retained formal_use promotion_evidence_allowed total_return_verified".split()


def require(value, message):
    if not value:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha(payload):
    return hashlib.sha256(payload).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"JSON 重複鍵：{key}")
        result[key] = value
    return result


def parse_json(payload):
    return json.loads(payload.decode("utf-8-sig"), object_pairs_hook=unique_object)


def git(root, *args):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    return subprocess.check_output(["git", "--no-replace-objects", "-C", str(root), *args], env=env)


def rows(payload):
    reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig")))
    require(reader.fieldnames and len(reader.fieldnames) == len(set(reader.fieldnames)), "CSV 缺表頭或重複欄位")
    result = list(reader)
    require(all(None not in r and None not in r.values() for r in result), "CSV 列寬不符")
    return result


def valid_date(value, optional=False):
    if value == "" and optional:
        return value
    require(isinstance(value, str) and re.fullmatch(r"\d{8}", value), "日期必須為 YYYYMMDD；未知日期保留空白")
    require(datetime.strptime(value, "%Y%m%d").strftime("%Y%m%d") == value, "不合法日期")
    return value


def decimal(value, positive=False):
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError("數值不可解析") from exc
    require(result.is_finite() and (result > 0 if positive else result >= 0), "數值不得負值或非有限值")
    return result


def number(value):
    text = format(value, "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def validate_events(events):
    require(isinstance(events, list), "events 必須為陣列")
    ids, economic_keys = set(), set()
    for event in events:
        eid = event.get("event_id")
        key = (event.get("stock_id"), event.get("kind"), event.get("entitlement_date"))
        require(eid and eid not in ids and key not in economic_keys, "重複公司行動會重複計算股數或現金")
        ids.add(eid); economic_keys.add(key)
        require(event.get("kind") in {"share_exchange", "stock_dividend", "cash_dividend"}, "未授權的公司行動種類")
        require(re.fullmatch(r"[1-9]\d{3}", str(event.get("stock_id", ""))), "公司行動證券代號不合法")
        require(isinstance(event.get("documents"), list) and event["documents"] and all(isinstance(x, str) and x for x in event["documents"]), "公司行動缺少原件引用")
        entitlement = valid_date(event["entitlement_date"])
        effective = valid_date(event["effective_date"])
        require(entitlement <= effective, "生效日期不得早於權利辨識日期")
        for field in ("tradable_date", "scheduled_payment_date", "actual_payment_date", "record_date", "suspension_start", "suspension_end"):
            value = valid_date(event.get(field, ""), optional=True)
            if field in {"tradable_date", "scheduled_payment_date", "actual_payment_date", "record_date"} and value:
                require(value >= entitlement, "公司行動時點先後矛盾")
        if event.get("tradable_date"):
            require(event["tradable_date"] >= effective, "可交易日不得早於生效日")
        if event.get("suspension_start") or event.get("suspension_end"):
            require(event.get("suspension_start") and event.get("suspension_end") and event["suspension_start"] <= event["suspension_end"], "停牌起訖缺失或矛盾")
        decimal(event["share_factor"], positive=True)
        decimal(event["new_shares_per_old_share"])
        if event.get("cash_per_old_share") != "":
            decimal(event["cash_per_old_share"])
        require(type(event.get("payment_confirmed")) is bool, "付款確認必須是布林值")
        if event["payment_confirmed"]:
            require(event.get("actual_payment_date") and event.get("payment_confirmation_ref"), "已收現金缺少實際付款日或確認證據")


def load_contract(root):
    contract = parse_json((Path(root) / CONTRACT_FILE).read_bytes())
    require(sha(canonical(contract).encode("utf-8")) == CONTRACT_SHA256, "契約雜湊不符：不得改寫既有條件或來源")
    require(contract["source_ref"] == SOURCE_REF, "必須讀固定 v1 來源")
    require(all(contract[key] is False for key in ("formal_use", "promotion_evidence_allowed", "total_return_verified", "coverage_complete")), "研究禁用旗標不符")
    for identifier, document in contract["documents"].items():
        payload = base64.b64decode(document["payload_base64"], validate=True)
        require(sha(payload) == document["sha256"] and len(payload) == document["bytes"], f"官方原件雜湊不符：{identifier}")
        require(document["first_publication_verified"] is False and document["original_revision_chain_verified"] is False, "事後原件不得充作歷史首次發布證明")
    validate_events(contract["events"])
    require(all(set(e["documents"]) <= contract["documents"].keys() for e in contract["events"]), "公司行動有孤立來源引用")
    return contract


def reconcile_position(trade, events, signal):
    """Pure retrospective quantity reconciliation; never emits a certified return."""
    validate_events(events)
    require(signal.get("stock_id") == trade.get("stock_id") and signal.get("signal_date") == trade.get("signal_date"), "交易與訊號身分不符")
    entry, exit_ = valid_date(trade["entry_date"]), valid_date(trade["exit_date"])
    decimal(trade["entry_open"], positive=True)
    decimal(trade["exit_close"], positive=True)
    require(valid_date(trade["signal_date"]) < entry <= exit_, "固定交易日期順序不符")
    require(str(trade["horizon"]) in {"5", "10", "20"} and str(trade["slippage_bps"]) in {"0", "10", "20"}, "持有期或滑價不可改寫")
    selected = sorted([e for e in events if e["stock_id"] == trade["stock_id"] and entry < e["entitlement_date"] <= exit_], key=lambda e: (e["entitlement_date"], e["event_id"]))
    grouped = defaultdict(list)
    for event in selected:
        grouped[event["entitlement_date"]].append(event)
    reasons = {"corporate_action_coverage_incomplete", "retrospective_documents_not_signal_pit"}
    with localcontext() as ctx:
        ctx.prec = 50
        balance = decimal(trade["shares"], positive=True)
        pending = Decimal(0); announced = Decimal(0); unsettled = Decimal(0); received = Decimal(0)
        unknown_cash = False; receipt_seen = False
        cash_event_seen = any(e["kind"] == "cash_dividend" for e in selected)
        prior_delivery_dates = []
        for entitlement_date, group in sorted(grouped.items()):
            require(all(delivery and delivery < entitlement_date for delivery in prior_delivery_dates), "未結清權利再遇新權利事件，缺乏經批准的後續解讀契約")
            require(pending == 0, "未結清權利再遇新權利事件，缺乏經批准的後續解讀契約")
            basis = balance
            require(sum(e["kind"] != "cash_dividend" for e in group) <= 1, "同日多個股份變更缺少經證實的順序")
            for event in group:
                if event["kind"] == "share_exchange":
                    replacement = basis * decimal(event["share_factor"], positive=True)
                    if event["tradable_date"] and event["tradable_date"] <= exit_:
                        balance = replacement
                    else:
                        balance = Decimal(0)
                        pending += replacement
                elif event["kind"] == "stock_dividend":
                    new_rights = basis * decimal(event["new_shares_per_old_share"])
                    if event["tradable_date"] and event["tradable_date"] <= exit_:
                        balance += new_rights
                    else:
                        pending += new_rights
                else:
                    if event["cash_per_old_share"] == "":
                        unknown_cash = True
                        reasons.add("cash_entitlement_amount_unknown")
                        continue
                    entitlement = basis * decimal(event["cash_per_old_share"])
                    announced += entitlement
                    if event["payment_confirmed"] and event["actual_payment_date"] <= exit_:
                        received += entitlement
                        receipt_seen = True
                    else:
                        unsettled += entitlement
                        if entitlement:
                            reasons.add("cash_receipt_unverified")
                            if event["scheduled_payment_date"] and event["scheduled_payment_date"] > exit_:
                                reasons.add("payment_scheduled_after_exit")
                if event["kind"] != "cash_dividend" and not event["tradable_date"]:
                    reasons.add("share_tradability_date_unknown")
                if event["kind"] != "cash_dividend" and (not event["tradable_date"] or event["tradable_date"] > entitlement_date):
                    prior_delivery_dates.append(event["tradable_date"])
        whole = balance.to_integral_value(rounding=ROUND_FLOOR)
        fraction = balance - whole
        if pending:
            reasons.add("share_rights_unsettled_at_scheduled_exit")
        if fraction:
            reasons.add("fractional_disposition_unverified")
        if not selected:
            reasons.add("no_event_is_not_absence_proof")
        status = "known_events_unsettled" if pending or unsettled or fraction or unknown_cash else ("known_events_reconciled_unverified_coverage" if selected else "no_registered_action_in_window")
        result = {key: trade[key] for key in ("trade_id", "stock_id", "stock_name", "signal_date", "horizon", "slippage_bps", "entry_date", "exit_date", "entry_open", "exit_close")}
        result.update(source_shares=trade["shares"], source_signal_sha256=sha(canonical(signal).encode()), source_trade_sha256=sha(canonical(trade).encode()), source_row_json=canonical(trade), matched_event_ids=";".join(e["event_id"] for e in selected), known_event_share_balance=number(balance), eligible_whole_share_component=number(whole), unresolved_fractional_share_component=number(fraction), pending_share_rights=number(pending), announced_gross_cash_entitlement="" if unknown_cash or not cash_event_seen else number(announced), unsettled_gross_cash_entitlement="" if unknown_cash or not cash_event_seen else number(unsettled), confirmed_cash_receipt=number(received) if receipt_seen and not unsettled and not unknown_cash else "", corporate_action_status=status, block_reasons=";".join(sorted(reasons)), original_strict_v3_status=trade.get("strict_v3_status", ""), strict_lock_released="False", original_proxy_net_return_pct=trade.get("net_return_pct", ""), verified_total_return_pct="", coverage_complete="False", anomaly_disposition="unresolved_anomaly_candidate" if trade.get("anomaly_candidate") == "True" else "not_finally_classified", primary_row_retained="True", **FLAGS)
        return result


def csv_bytes(fields, data):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(data)
    return stream.getvalue().encode("utf-8")


def render_report(counts, positions):
    matches = sum(bool(p["matched_event_ids"]) for p in positions)
    return ("# TDCC 潛伏吸籌：公司行動研究帳本 v1\n\n"
        "這是固定四股的事後帳務補證，不是選股重算、修正勝率或正式模型升級。\n\n"
        f"來源：{SOURCE_REF}；截止日 20260909。保留 {counts['signals']} 個來源訊號、{counts['trades']} 列原研究交易情境與 {counts['source_blocked']} 列原阻擋紀錄。\n\n"
        f"交易情境含 0／10／20 bps 三種滑價，共 {counts['positions']} 列；10 bps 為 {sum(p['slippage_bps']=='10' for p in positions)} 個各持有期部位，不同持有期不能當成互相獨立實驗。已知事件涉及 {matches} 列情境；未匹配事件不等於證明沒有其他事件。\n\n"
        "| 股票 | 已知事件與帳務界線 |\n|---|---|\n"
        "| 強生 4747 | 1 股換 2 股；8/20～8/28 停牌，8/31 新股恢復交易。只核對理論股數，不推定其他公司行動已完整查核。 |\n"
        "| 青雲 5386 | 7/20 取得配股／股息權利；每仟股 500.00001386 股、每股現金 1.5 元。8/14 新股權利證書才可交易；原 7/22／8/5 出場不能賣出未到手權利。 |\n"
        "| 益得 6461 | 減資後每仟股換 618.578 股，9/9 復牌；每股退還股款 0。整股／小數只是數學組成，不假設畸零股合併、出售或現金入帳。 |\n"
        "| 緯穎 6669 | 每仟股配發 1982.79460 股，9/2 除權；交付／可交易日未取得，保留待交付權利。9/16～9/30 認購繳款期不是交付日期。 |\n\n"
        "`known_event_share_balance` 是僅套用已列事件的理論股數；`eligible_whole_share_component`／`unresolved_fractional_share_component` 是算術拆分，不是已成交或已入帳證明。`pending_share_rights` 與 `unsettled_gross_cash_entitlement` 分開；公告付款日不是實收證據。沒有現金確認證據時 `confirmed_cash_receipt` 空白，不填零冒充已核實。\n\n"
        "原定 D+5／D+10／D+20 出場日、原訊號及持倉鎖不變。未到帳權利不假造價格、不延長賣出日、不計已實現收益。舊 proxy 報酬僅保留於 `original_proxy_net_return_pct`，不得稱為修正績效。所有 `verified_total_return_pct` 空白，`total_return_verified=False`；沒有正式勝率分母。\n\n"
        "官方原件取回在事件之後，只供 retrospective reconciliation，不作 signal PIT 證據。未建立完整公司行動覆蓋、個別實收／畸零股證明，也沒有補回 21 個既有版本收據缺口。異常候選保留原列、不作最終 disposition 或剔除。\n\n"
        "五個模型專屬產物以 source_manifest 綁定最終 bytes SHA-256；契約內封存官方原件及固定 Git 來源。獨立 validator 不匯入 producer 商業邏輯。研究仍 `formal_use=False`、`promotion_evidence_allowed=False`；其他模型、舊產物、六份 PDF、Apps Script、月營收及 EPS 等季度／年度財報均不變。\n").encode("utf-8")


def build(root=ROOT):
    root = Path(root).resolve()
    contract = load_contract(root)
    source = {}
    for kind, info in contract["source_files"].items():
        data = git(root, "show", SOURCE_REF + ":" + info["path"])
        require(sha(data) == info["sha256"] and len(data) == info["bytes"], "固定 v1 來源 bytes 不符")
        source[kind] = parse_json(data) if kind == "source_manifest" else rows(data)
    selected = {kind: [r for r in source[kind] if r["stock_id"] in contract["stock_ids"]] for kind in ("signals", "trades", "blocked")}
    require({kind: len(data) for kind, data in selected.items()} == contract["expected_source_counts"], "四股來源列數不符")
    signals = {(r["stock_id"], r["signal_date"]): r for r in selected["signals"]}
    require(len(signals) == len(selected["signals"]), "來源訊號身分重複")
    require(len({r["trade_id"] for r in selected["trades"]}) == len(selected["trades"]), "來源交易身分重複")
    positions = [reconcile_position(t, contract["events"], signals[(t["stock_id"], t["signal_date"])]) for t in selected["trades"]]
    event_rows = []
    for event in contract["events"]:
        row = {field: event.get(field, "") for field in EVENT_FIELDS if field in event}
        row.update(document_ids=";".join(event["documents"]), document_sha256s=";".join(contract["documents"][name]["sha256"] for name in event["documents"]), source_availability="retrospective_only", coverage_complete="False", **FLAGS)
        event_rows.append(row)
    blocked = []
    for row in selected["blocked"]:
        blocked.append(dict(record_type="source_" + row["record_type"], stock_id=row["stock_id"], signal_date=row["signal_date"], horizon=row.get("horizon", ""), trade_id="", status=row.get("strict_v3_status", ""), reasons=row.get("reasons", ""), source_row_sha256=sha(canonical(row).encode()), source_row_json=canonical(row), primary_row_retained="True", **FLAGS))
    for row in positions:
        blocked.append(dict(record_type="ledger_evidence_gap", stock_id=row["stock_id"], signal_date=row["signal_date"], horizon=row["horizon"], trade_id=row["trade_id"], status=row["corporate_action_status"], reasons=row["block_reasons"], source_row_sha256=row["source_trade_sha256"], source_row_json=row["source_row_json"], primary_row_retained="True", **FLAGS))
    counts = {"signals": len(signals), "trades": len(selected["trades"]), "source_blocked": len(selected["blocked"]), "events": len(event_rows), "positions": len(positions), "blocked": len(blocked), "verified_total_return_positions": 0}
    payloads = {OWNER_ID + "_events_v1.csv": csv_bytes(EVENT_FIELDS, event_rows), OWNER_ID + "_positions_v1.csv": csv_bytes(POSITION_FIELDS, positions), OWNER_ID + "_blocked_v1.csv": csv_bytes(BLOCKED_FIELDS, blocked), OWNER_ID + "_report_v1.md": render_report(counts, positions)}
    manifest = dict(schema_version=1, artifact_version=OWNER_ID + "_v1", model_id=MODEL_ID, ownership_id=OWNER_ID, contract_sha256=CONTRACT_SHA256, source_ref=SOURCE_REF, source_files=contract["source_files"], document_sha256s={k: v["sha256"] for k, v in contract["documents"].items()}, artifacts={name: {"sha256": sha(data), "bytes": len(data)} for name, data in sorted(payloads.items())}, counts=counts, formal_use=False, promotion_evidence_allowed=False, total_return_verified=False)
    payloads[OWNER_ID + "_source_manifest_v1.json"] = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    return payloads


def no_reparse(path, root):
    current = path
    while current != root:
        require(root in current.parents, "產物路徑逸出 repository")
        if current.exists() or current.is_symlink():
            require(not current.is_symlink() and not (getattr(current.lstat(), "st_file_attributes", 0) & 0x400), "產物或父目錄不可為 symlink/reparse point")
        current = current.parent


def write_outputs(root, payloads):
    root = Path(root).resolve()
    require(set(payloads) == GENERATED and all(isinstance(v, bytes) for v in payloads.values()), "產物必須為 exact five byte payloads")
    destination = root / DIRECTORY
    for name in payloads:
        no_reparse(destination / name, root)
    paths = [DIRECTORY + "/" + name for name in sorted(GENERATED)]
    errors = validate_changed_paths(OWNER_ID, PRODUCER, paths, load_ownership_rules(root / "config/model_research_artifact_ownership.csv"))
    require(not errors, "產物 ownership 登錄不符：" + "; ".join(errors))
    destination.mkdir(parents=True, exist_ok=True)
    for name, value in payloads.items():
        (destination / name).write_bytes(value)


def snapshot(root):
    """Bind all Git mappings and physical files outside the exact five outputs."""
    allowed = {DIRECTORY + "/" + name for name in GENERATED}
    mappings = {}
    for command in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z")):
        records_ = [r for r in git(root, *command).split(b"\0") if r and r.split(b"\t", 1)[1].decode() not in allowed]
        mappings[command[0]] = sha(b"\0".join(records_))
    physical = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative == ".git" or relative.startswith(".git/") or relative in allowed:
            continue
        require(not path.is_symlink(), "工作樹含未納入契約的符號連結")
        if path.is_file():
            physical[relative] = sha(path.read_bytes())
    return mappings, physical


@contextmanager
def artifact_guard(root):
    before = snapshot(root)
    try:
        yield
    finally:
        require(snapshot(root) == before, "producer 改動了五個產物以外的 Git mapping 或實體檔案")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.repository_root.resolve()
    with artifact_guard(root):
        payloads = build(root)
        write_outputs(root, payloads)
    print(f"{OWNER_ID}: artifacts=5 research_only=True verified_total_returns=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
