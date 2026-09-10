"""TDCC 潛伏吸籌公司行動帳本的唯讀、獨立驗證。

只讀固定 Git 原件、契約內官方原件及實際產物；不載入 producer 或模型
business code。通過只代表本次研究帳本契約成立，不認證總報酬或歷史 PIT。
"""
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import json
import os
import re
import subprocess
from collections import Counter
from datetime import datetime
from decimal import Decimal, ROUND_FLOOR, localcontext
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


MODEL_ID = "tdcc_stealth_accumulation"
OWNER_ID = "tdcc_stealth_accumulation_corporate_action_ledger"
PREFIX = OWNER_ID + "_"
ARTIFACT_VERSION = OWNER_ID + "_v1"
CONTRACT_FILE = "config/tdcc_stealth_accumulation_corporate_action_ledger_v1.json"
DEFAULT_DIRECTORY = "output/research/tdcc_stealth_accumulation"
SOURCE_REF = "3fe40157cf4b333ef03a1447e45c310d197cbc5b"
APPROVED_CONTRACT_SHA256 = "78bfd1c8fd6da0f95ae6659218144b79add312048da807d8dceeb75e02b2aa7f"
PRODUCER = "scripts/build_tdcc_stealth_accumulation_corporate_action_ledger.py"
VALIDATOR = "scripts/validate_tdcc_stealth_accumulation_corporate_action_ledger.py"
TEST_FILE = "tests/test_tdcc_stealth_accumulation_corporate_action_ledger.py"
FAMILY_ID = OWNER_ID + "_outputs"
REGISTRY_APPROVAL = "user_approval_20260910_tdcc_stealth_corporate_action_ledger"
APPROVAL = "user_approval_20260910_tdcc_corporate_action_ledger_scope"
STOCK_IDS = ("4747", "5386", "6461", "6669")
KINDS = {"source_manifest": "json", "events": "csv", "positions": "csv", "blocked": "csv", "report": "md"}
SOURCE_COUNTS = {"signals": 59, "trades": 90, "blocked": 381}
SOURCE_PINS = {
    "source_manifest": ("65ba9a496d2de3895280747ab8635d9d3a59ba87c1cc5a98d8e450cda0861fc0", 1659738),
    "signals": ("56154ab073a0d7b1717494a1562e6ca313b6c855dfc07a1ea8001ed43b896b22", 30673697),
    "trades": ("98849b77e38c40cc79fd138ffb499b9c0ed8138070923d57df4c91e03391fa2e", 30532546),
    "blocked": ("a47e9f5419ef2910b555cb84afd6b962451bc8d8d8c067f43b71d1c55f8ade0f", 25035468),
}
DOCUMENT_PINS = {
    "tpex_4747_suspension_notice.html": "5e707074b9fbd6823648dbffad8d399851d7ef6508667746881436d14ab08fc0",
    "tpex_4747_resumption_notice.html": "cda435fc7a711ef1978530491f6fcfb5a7ef41c31bf7c42f956e4fda84ed9575",
    "mops_5386_distribution.json": "efa0a4ac3e72f4e311f1501fbb074e2c60975434a8cc5cad3bae5ed6e15fffc2",
    "tpex_exdaily_20260720.json": "d6ef30477e5c23ecf1379ec67aebad92aee9ad37e059cd396a5d0665ffd0046f",
    "tpex_5386_capital_detail.json": "891b7a76e09de72859b3db93f06720b1b073e324c443cb77d9f47d9eb9cf98dd",
    "tpex_6461_suspension_notice.html": "0ade8ce633a477fe9a3f94e1a9f1d4402e66d3f61a1a2451922bdaa24e0e5b70",
    "tpex_revivt_20260909.json": "32952d53a54ffaf219f3b33780299ca15fd2a0d583d2055cf3402a28cc3fefaf",
    "mops_6669_fractional_current.json": "338083156d68b3642e94a31d49e58425848c715d812d67cd236aad9fdead7326",
    "mops_6669_exright_schedule.json": "312075a32a13d68e79d3c0ff21129c31cbe2c8e0edee45f1a0b8c429f7311440",
    "mops_6669_stock_dividend_adjustment.json": "c8ea5b46d7eecf048e03089f97a74385cbb88090a2153753f6fbaa969c19f711",
    "mops_6669_distribution_record_notice_20260819.html": "57068d16af54eccf4ce2b408d6c6935ead7fe66b581779f0876fffc328997bc7",
}
SCHEMAS = {
    "events": "event_id,stock_id,stock_name,kind,entitlement_date,effective_date,tradable_date,scheduled_payment_date,actual_payment_date,share_factor,new_shares_per_old_share,cash_per_old_share,record_date,suspension_start,suspension_end,payment_confirmed,payment_confirmation_ref,document_ids,document_sha256s,source_availability,coverage_complete,formal_use,promotion_evidence_allowed,total_return_verified".split(","),
    "positions": "trade_id,stock_id,stock_name,signal_date,horizon,slippage_bps,entry_date,exit_date,entry_open,exit_close,source_shares,source_signal_sha256,source_trade_sha256,source_row_json,matched_event_ids,known_event_share_balance,eligible_whole_share_component,unresolved_fractional_share_component,pending_share_rights,announced_gross_cash_entitlement,unsettled_gross_cash_entitlement,confirmed_cash_receipt,corporate_action_status,block_reasons,original_strict_v3_status,strict_lock_released,original_proxy_net_return_pct,verified_total_return_pct,coverage_complete,anomaly_disposition,primary_row_retained,formal_use,promotion_evidence_allowed,total_return_verified".split(","),
    "blocked": "record_type,stock_id,signal_date,horizon,trade_id,status,reasons,source_row_sha256,source_row_json,primary_row_retained,formal_use,promotion_evidence_allowed,total_return_verified".split(","),
}


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def artifact_name(kind):
    return f"{PREFIX}{kind}_v1.{KINDS[kind]}"


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        _require(key not in result, f"JSON 欄位重複：{key}")
        result[key] = value
    return result


def json_value(payload):
    if isinstance(payload, bytes):
        _require(not payload.startswith(b"\xef\xbb\xbf"), "JSON 不允許 BOM")
        payload = payload.decode("utf-8")
    return json.loads(payload, object_pairs_hook=_unique_object,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"JSON 非有限數值：{value}")))


def csv_records(payload, fields=None, *, strict_transport=False):
    if strict_transport:
        _require(not payload.startswith(b"\xef\xbb\xbf") and b"\r" not in payload,
                 "研究 CSV 必須使用無 BOM 的 UTF-8/LF")
        _require(payload.endswith(b"\n"), "研究 CSV 缺少最終 LF")
    reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""), strict=True)
    headers = reader.fieldnames
    _require(headers is not None and len(headers) == len(set(headers)), "CSV 缺少欄名或欄名重複")
    if fields is not None:
        _require(headers == fields, "CSV 欄位或欄位順序不符")
    rows = list(reader)
    _require(all(None not in row and all(value is not None for value in row.values()) for row in rows),
             "CSV 行欄位數不符")
    return rows


class _TextOnlyHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def html_text(value):
    parser = _TextOnlyHTML()
    parser.feed(value)
    return re.sub(r"\s+", "", "".join(parser.parts))


def _tokens(value, tokens, label):
    normalized = re.sub(r"\s+", "", value)
    for token in tokens:
        _require(re.sub(r"\s+", "", token) in normalized, f"官方原件缺少契約證明 {label}：{token}")


def _mops_body(documents, name, company, declared_date):
    item = json_value(documents[name])
    _require(item.get("code") == 200, f"官方 MOPS 原件非成功回應：{name}")
    result = item["result"]
    _require(result["companyId"] == company, f"官方 MOPS 股票代號不符：{name}")
    _require(len(result["data"]) == 1, f"官方 MOPS 明細行數不符：{name}")
    row = result["data"][0]
    fields = [field["main"] for field in result["titles"]]
    _require(len(fields) == len(set(fields)) == len(row), f"官方 MOPS 欄位不符：{name}")
    mapped = dict(zip(fields, row))
    _require(mapped["發言日期"] == declared_date, f"官方 MOPS 公告日期不符：{name}")
    return mapped["說明"]


def verify_official_sources(contract):
    documents = contract["documents"]
    _require(set(documents) == set(DOCUMENT_PINS), "官方原件必須恰為已釘選的 11 份")
    raw = {}
    for name, expected_hash in DOCUMENT_PINS.items():
        doc = documents[name]
        payload = base64.b64decode(doc["payload_base64"], validate=True)
        _require(doc["sha256"] == expected_hash == digest(payload), f"官方原件 SHA-256 不符：{name}")
        _require(type(doc["bytes"]) is int and doc["bytes"] == len(payload), f"官方原件位元組數不符：{name}")
        _require(doc["first_publication_verified"] is False and doc["original_revision_chain_verified"] is False,
                 f"事後取件不可升格歷史 PIT：{name}")
        parsed = urlparse(doc["url"])
        _require(parsed.scheme == "https" and parsed.hostname in {"www.tpex.org.tw", "mops.twse.com.tw", "mopsov.twse.com.tw"},
                 f"官方原件來源網域不符：{name}")
        retrieved = datetime.fromisoformat(doc["retrieved_at"])
        _require(retrieved.strftime("%Y%m%d") >= "20260909", f"不可倒填原件實際取得日期：{name}")
        raw[name] = payload

    split = html_text(raw["tpex_4747_suspension_notice.html"].decode("utf-8"))
    _tokens(split, ["4747", "每1股換發新股票2股", "暫停股票櫃檯買賣日期：115年8月20日至115年8月28日",
                    "新股票換發基準日：115年8月28日", "公司新股票開始櫃檯買賣日期：115年8月31日"], "4747 分割")
    resume = html_text(raw["tpex_4747_resumption_notice.html"].decode("utf-8"))
    _tokens(resume, ["4747", "45,461,032股", "90,922,064股", "自115年8月31日起恢復"], "4747 恢復買賣")

    ex = json_value(raw["tpex_exdaily_20260720.json"])
    _require(ex["stat"] == "ok" and ex["date"] == "20260720~20260720", "青雲除權息查詢日期不符")
    table = ex["tables"][0]
    _require(len(table["fields"]) == len(set(table["fields"])), "除權息欄位重複")
    rows = [dict(zip(table["fields"], row)) for row in table["data"]]
    match = [row for row in rows if row["代號"] == "5386"]
    _require(len(match) == 1, "青雲除權息資料不是唯一列")
    _require(match[0]["除權息日期"] == "115/07/20" and match[0]["權/息"] == "除權息", "青雲除權息日期／類型不符")
    _require(Decimal(match[0]["每仟股無償配股"]) / 1000 == Decimal("0.50000001386") and
             Decimal(match[0]["現金股利"]) == Decimal("1.5"), "青雲配股率／現金股利不符")
    capital = json_value(raw["tpex_5386_capital_detail.json"])
    _require(capital["stat"] == "ok", "青雲權利證書公告非成功回應")
    _tokens(html_text(" ".join(capital["tables"][0]["data"][0])),
            ["5386", "新股權利證書17,755,993股", "上櫃股票開始買賣日期：115年8月14日"], "青雲新股權利證書")
    distribution = _mops_body(raw, "mops_5386_distribution.json", "5386", "115/07/03")
    _tokens(distribution, ["除權（息）交易日:115/07/20", "除權（息）基準日:115/07/26",
                           "普通股現金股利發放日期:115/08/14", "每股配發現金股利新台幣1.5元"], "青雲股利")

    reduction = html_text(raw["tpex_6461_suspension_notice.html"].decode("utf-8"))
    _tokens(reduction, ["6461", "減資彌補虧損", "每仟股換發新股票618.578股",
                        "暫停股票櫃檯買賣日期：115年9月2日至115年9月8日",
                        "新股票換發基準日：115年9月8日", "公司新股票開始櫃檯買賣日期：115年9月9日"], "益得減資")
    revival = json_value(raw["tpex_revivt_20260909.json"])
    _require(revival["stat"] == "ok" and revival["date"] == "20260909~20260909", "益得恢復交易查詢日期不符")
    table = revival["tables"][0]
    _require(len(table["fields"]) == len(set(table["fields"])), "恢復交易欄位重複")
    rows = [dict(zip(table["fields"], row)) for row in table["data"]]
    match = [row for row in rows if row["股票代號"] == "6461"]
    _require(len(match) == 1 and match[0]["恢復買賣日期"] == "1150909" and match[0]["減資原因"] == "彌補虧損",
             "益得恢復交易事件不符")
    _tokens(html_text(match[0]["詳細資料"]), ["每壹仟股換發新股票:618.57800000", "每股退還股款:0.00000000"], "益得非現金減資")

    schedule = _mops_body(raw, "mops_6669_exright_schedule.json", "6669", "115/08/07")
    _tokens(schedule, ["除權（息）交易日:115/09/02", "除權（息）基準日:115/09/08", "每仟股配發1,984.22578股"], "緯穎原公告")
    adjusted = _mops_body(raw, "mops_6669_stock_dividend_adjustment.json", "6669", "115/08/14")
    _tokens(adjusted, ["原發放股利", "1,984.22578股", "變更後發放股利", "每仟股配發1,982.79460股"], "緯穎配股率修訂")
    fractional = _mops_body(raw, "mops_6669_fractional_current.json", "6669", "115/09/08")
    _tokens(fractional, ["配發1,982.79460股", "9月16日-9月30日下午3:30止", "未滿一股之畸零股款", "必要之費用"], "緯穎畸零股")
    delivery = html_text(raw["mops_6669_distribution_record_notice_20260819.html"].decode("utf-8"))
    _tokens(delivery, ["6669", "1,982.79460", "主管機關核准變更登記後30日內", "屆時另行公告"], "緯穎交付日期未確定")
    return raw


def _event_facts():
    """獨立事件決策表；數值及時點由上列官方欄位／本文逐一證明。"""
    columns = "event_id stock_id stock_name kind entitlement_date effective_date tradable_date scheduled_payment_date share_factor new_shares_per_old_share cash_per_old_share record_date suspension_start suspension_end".split()
    values = [
        ("4747_share_exchange_20260831", "4747", "強生", "share_exchange", "20260820", "20260831", "20260831", "", "2", "0", "0", "20260828", "20260820", "20260828"),
        ("5386_stock_dividend_20260720", "5386", "青雲", "stock_dividend", "20260720", "20260720", "20260814", "", "1", "0.50000001386", "0", "20260726", "", ""),
        ("5386_cash_dividend_20260720", "5386", "青雲", "cash_dividend", "20260720", "20260720", "", "20260814", "1", "0", "1.5", "20260726", "", ""),
        ("6461_capital_reduction_20260909", "6461", "益得", "share_exchange", "20260902", "20260909", "20260909", "", "0.618578", "0", "0", "20260908", "20260902", "20260908"),
        ("6669_stock_dividend_20260902", "6669", "緯穎", "stock_dividend", "20260902", "20260902", "", "", "1", "1.98279460", "0", "20260908", "", ""),
    ]
    document_lists = [
        ["tpex_4747_suspension_notice.html", "tpex_4747_resumption_notice.html"],
        ["tpex_exdaily_20260720.json", "tpex_5386_capital_detail.json"],
        ["tpex_exdaily_20260720.json", "mops_5386_distribution.json"],
        ["tpex_6461_suspension_notice.html", "tpex_revivt_20260909.json"],
        ["mops_6669_exright_schedule.json", "mops_6669_stock_dividend_adjustment.json", "mops_6669_fractional_current.json", "mops_6669_distribution_record_notice_20260819.html"],
    ]
    events = []
    for values_row, documents in zip(values, document_lists):
        row = dict(zip(columns, values_row))
        row.update(payment_confirmed=False, payment_confirmation_ref="", actual_payment_date="", documents=documents)
        events.append(row)
    return events


def verify_contract(contract):
    _require(digest(canonical_json(contract)) == APPROVED_CONTRACT_SHA256, "契約 canonical SHA-256 與核准版本不符")
    required = {"model_id": MODEL_ID, "model_name_zh": "TDCC 潛伏吸籌", "ownership_id": OWNER_ID,
                "source_ref": SOURCE_REF, "as_of": "20260909", "stock_ids": list(STOCK_IDS),
                "authorization_reference": APPROVAL, "expected_source_counts": SOURCE_COUNTS,
                "output_kinds": [artifact_name(kind)[len(PREFIX):] for kind in KINDS]}
    for key, expected in required.items():
        _require(contract[key] == expected, f"契約欄位不符：{key}")
    _require(type(contract["version"]) is int and contract["version"] == 1, "契約版本必須為整數 1")
    for key in ("coverage_complete", "individual_cash_receipts_verified", "formal_use", "promotion_evidence_allowed", "total_return_verified"):
        _require(contract[key] is False, f"契約 {key} 必須為 JSON false")
    expected_events = _event_facts()
    _require(len(contract["events"]) == 5, "契約事件數不符")
    for row, expected in zip(contract["events"], expected_events):
        for key, value in expected.items():
            _require(row[key] == value and (not isinstance(value, bool) or row[key] is value),
                     f"事件契約不符：{expected['event_id']} / {key}")
    verify_official_sources(contract)
    return expected_events


def _git_blob(root, path):
    environment = {key: value for key, value in os.environ.items() if not key.upper().startswith("GIT_")}
    return subprocess.check_output(["git", "--no-replace-objects", "-C", str(root), "show", f"{SOURCE_REF}:{path}"], env=environment)


def fixed_sources(root, contract):
    _require(set(contract["source_files"]) == set(SOURCE_PINS), "固定來源必須恰為四份原研究產物")
    results = {}
    for kind, (expected_hash, expected_bytes) in SOURCE_PINS.items():
        path = f"{DEFAULT_DIRECTORY}/tdcc_stealth_accumulation_receipted_marketwide_replay_{kind}_v1.{ 'json' if kind == 'source_manifest' else 'csv'}"
        _require(contract["source_files"][kind] == {"path": path, "sha256": expected_hash, "bytes": expected_bytes},
                 f"固定原研究來源釘選不符：{kind}")
        payload = _git_blob(root, path)
        _require(digest(payload) == expected_hash and len(payload) == expected_bytes, f"Git 原件 SHA-256 或長度不符：{kind}")
        if kind == "source_manifest":
            original = json_value(payload)
            _require(original["formal_use"] is False and original["promotion_evidence_allowed"] is False,
                     "原始研究不可升格正式證據")
            results[kind] = original
        else:
            rows = [row for row in csv_records(payload) if row["stock_id"] in STOCK_IDS]
            _require(len(rows) == SOURCE_COUNTS[kind], f"原研究四股 {kind} 列數不符")
            results[kind] = rows
    signal_keys = [(row["stock_id"], row["signal_date"]) for row in results["signals"]]
    _require(len(signal_keys) == len(set(signal_keys)), "原研究 signal 鍵重複")
    trade_ids = [row["trade_id"] for row in results["trades"]]
    _require(len(trade_ids) == len(set(trade_ids)), "原研究 trade_id 重複")
    _require(all((row["stock_id"], row["signal_date"]) in set(signal_keys) for row in results["trades"]), "原研究交易缺少原始 signal")
    return results


def _registration_rows(root, name):
    return csv_records((root / "config" / name).read_bytes())


def _unique_row(rows, key, value, label):
    matches = [row for row in rows if row[key] == value]
    _require(len(matches) == 1, f"登錄缺少唯一列：{label}")
    return matches[0]


def verify_registration(root):
    pattern = f"{DEFAULT_DIRECTORY}/{PREFIX}*_v1.*"
    ownership = _unique_row(_registration_rows(root, "model_research_artifact_ownership.csv"), "owner_model_id", OWNER_ID, "artifact ownership")
    for key, expected in {"producer": PRODUCER, "artifact_glob": pattern, "artifact_class": "model_research_output",
                          "change_policy": "model_owned_write", "formal_evidence_status": "research_only"}.items():
        _require(ownership[key] == expected, f"artifact ownership 欄位不符：{key}")
    registry = _unique_row(_registration_rows(root, "daily_model_data_sharing_registry.csv"), "data_family_id", FAMILY_ID, "data sharing")
    for key, expected in {"ownership_mode": "model_owned_not_shared", "owner_model_or_family": OWNER_ID,
                          "registered_producers": PRODUCER, "producer_write_scope": pattern,
                          "consumer_access_mode": "owner_model_research_only", "approved_consumer_models": MODEL_ID,
                          "sharing_decision_reference": REGISTRY_APPROVAL,
                          "formal_evidence_policy": "research_only_corporate_action_accounting_not_formal_operation_total_return_or_promotion_evidence",
                          "new_consumer_policy": "user_approval_and_append_only_registry_migration_required"}.items():
        _require(registry[key] == expected, f"data sharing 欄位不符：{key}")
    _require(re.fullmatch(r"[0-9a-f]{64}", registry["data_contract_sha256"]), "登錄 data contract SHA 不合法")
    migration = _unique_row(_registration_rows(root, "daily_model_data_sharing_migrations.csv"), "migration_id", registry["last_migration_id"], "data migration")
    for key, expected in {"changed_data_families": FAMILY_ID, "previous_contract_sha256s": "NEW",
                          "new_contract_sha256s": registry["data_contract_sha256"], "affected_models": MODEL_ID,
                          "user_approval_reference": REGISTRY_APPROVAL,
                          "migration_status": "validated_user_approved_migration"}.items():
        _require(migration[key] == expected, f"data migration 欄位不符：{key}")
    _require(f"python {VALIDATOR}" in migration["validation_commands"].split(";"), "migration 缺少獨立帳本驗證")
    independence = _unique_row(_registration_rows(root, "daily_model_validator_independence.csv"), "validator_path", VALIDATOR, "validator independence")
    for key, expected in {"validator_role": "independent_research_replay_validator", "production_source_file": PRODUCER,
                          "imported_production_symbols": "", "independence_claim": "True",
                          "allowed_evidence_use": "independent_corporate_action_research_accounting_validation_only_not_formal_or_promotion_proof"}.items():
        _require(independence[key] == expected, f"獨立驗證登錄欄位不符：{key}")
    inventory = _registration_rows(root, "repo_file_lifecycle_inventory.csv")
    producer = _unique_row(inventory, "path", PRODUCER, "producer inventory")
    expected_paths = {f"{DEFAULT_DIRECTORY}/{artifact_name(kind)}" for kind in KINDS}
    _require(set(producer["writes_artifact"].split(";")) == expected_paths, "producer inventory 寫入範圍不是恰好五份產物")
    _require(producer["owner"] == "research_backtest" and producer["status"] == "active", "producer inventory owner/status 不符")
    for path in (PRODUCER, VALIDATOR):
        row = _unique_row(inventory, "path", path, "lifecycle inventory")
        _require(TEST_FILE in row["tested_by"].split(";"), f"inventory 缺少專屬測試：{path}")


def _false_fields(row, fields=("formal_use", "promotion_evidence_allowed", "total_return_verified")):
    for key in fields:
        _require(row[key] == "False", f"產物 {key} 必須為 False")


def _decimal(value):
    number = Decimal(value)
    _require(number.is_finite(), "帳本禁止非有限數值")
    return number


def _decimal_text(value):
    text = format(value, "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def independent_accounting(trade, events):
    """由原交易與獨立事件表驗證股數／未結清權利；不算經濟總報酬。"""
    entry, exit_date = trade["entry_date"], trade["exit_date"]
    _require(re.fullmatch(r"[0-9]{8}", entry) and re.fullmatch(r"[0-9]{8}", exit_date) and entry <= exit_date,
             "原始交易入出場日期不合法")
    datetime.strptime(entry, "%Y%m%d")
    datetime.strptime(exit_date, "%Y%m%d")
    for field in ("entry_open", "exit_close"):
        _require(_decimal(trade[field]) > 0, f"原交易 {field} 必須為有限正值")
    applicable = [event for event in events if event["stock_id"] == trade["stock_id"]
                  and entry < event["entitlement_date"] <= exit_date]
    applicable.sort(key=lambda event: (event["entitlement_date"], event["event_id"]))
    reasons = {"corporate_action_coverage_incomplete", "retrospective_documents_not_signal_pit"}
    with localcontext() as context:
        context.prec = 50
        balance = _decimal(trade["shares"])
        _require(balance >= 0, "原始持股數不得為負")
        pending = Decimal(0)
        cash = Decimal(0)
        # 每一事件日只讀一次當日開始的舊股數，股利不得套用當日新增股。
        for day in sorted({event["entitlement_date"] for event in applicable}):
            base = balance
            day_events = [event for event in applicable if event["entitlement_date"] == day]
            _require(sum(event["kind"] == "share_exchange" for event in day_events) <= 1,
                     "同一股票同一事件日不得有多個換股事件")
            for event in day_events:
                if event["kind"] == "cash_dividend":
                    entitled = base * _decimal(event["cash_per_old_share"])
                    _require(entitled >= 0, "公告現金股利不得為負")
                    cash += entitled
                    if entitled:
                        reasons.add("cash_receipt_unverified")
                        if event["scheduled_payment_date"] and event["scheduled_payment_date"] > exit_date:
                            reasons.add("payment_scheduled_after_exit")
                elif event["kind"] == "stock_dividend":
                    entitled = base * _decimal(event["new_shares_per_old_share"])
                    if event["tradable_date"] and event["tradable_date"] <= exit_date:
                        balance += entitled
                    else:
                        pending += entitled
                        if not event["tradable_date"]:
                            reasons.add("share_tradability_date_unknown")
                elif event["kind"] == "share_exchange":
                    replacement = base * _decimal(event["share_factor"])
                    if event["tradable_date"] and event["tradable_date"] <= exit_date:
                        balance = replacement
                    else:
                        balance = Decimal(0)
                        pending += replacement
                else:
                    raise ValueError(f"不允許的公司行動類型：{event['kind']}")
        _require(balance >= 0 and pending >= 0, "股數／未結清權利不得為負")
        whole = balance.to_integral_value(rounding=ROUND_FLOOR)
        fractional = balance - whole
        if pending:
            reasons.add("share_rights_unsettled_at_scheduled_exit")
        if fractional:
            reasons.add("fractional_disposition_unverified")
        if not applicable:
            reasons.add("no_event_is_not_absence_proof")
        status = ("known_events_unsettled" if pending or cash or fractional else
                  "known_events_reconciled_unverified_coverage" if applicable else "no_registered_action_in_window")
        return {
            "matched_event_ids": ";".join(event["event_id"] for event in applicable),
            "known_event_share_balance": _decimal_text(balance),
            "eligible_whole_share_component": _decimal_text(whole),
            "unresolved_fractional_share_component": _decimal_text(fractional),
            "pending_share_rights": _decimal_text(pending),
            "announced_gross_cash_entitlement": _decimal_text(cash) if any(event["kind"] == "cash_dividend" for event in applicable) else "",
            "unsettled_gross_cash_entitlement": _decimal_text(cash) if any(event["kind"] == "cash_dividend" for event in applicable) else "",
            "confirmed_cash_receipt": "",
            "corporate_action_status": status,
            "block_reasons": ";".join(sorted(reasons)),
        }


def _validate_events(rows, facts):
    _require(len(rows) == 5 and len({row["event_id"] for row in rows}) == 5, "事件產物必須有五個唯一事件")
    by_id = {row["event_id"]: row for row in rows}
    _require(set(by_id) == {event["event_id"] for event in facts}, "事件產物 ID 集合不符")
    for event in facts:
        row = by_id[event["event_id"]]
        for key, value in event.items():
            if key != "documents":
                expected = "False" if value is False else str(value)
                _require(row[key] == expected, f"事件產物欄位不符：{event['event_id']} / {key}")
        _require(row["document_ids"] == ";".join(event["documents"]), "事件官方原件清單不符")
        _require(row["document_sha256s"] == ";".join(DOCUMENT_PINS[name] for name in event["documents"]), "事件官方原件雜湊不符")
        _require(row["source_availability"] == "retrospective_only", "事件不得冒充歷史 PIT")
        _false_fields(row, ("coverage_complete", "formal_use", "promotion_evidence_allowed", "total_return_verified"))


def _validate_positions(rows, sources, events):
    _require(len(rows) == 90 and len({row["trade_id"] for row in rows}) == 90, "positions 必須完整保留 90 個唯一原交易")
    originals = {row["trade_id"]: row for row in sources["trades"]}
    signals = {(row["stock_id"], row["signal_date"]): row for row in sources["signals"]}
    _require({row["trade_id"] for row in rows} == set(originals), "positions 交易母體與原研究不同")
    for row in rows:
        original = originals[row["trade_id"]]
        signal = signals[(original["stock_id"], original["signal_date"])]
        for key in ("stock_id", "stock_name", "signal_date", "horizon", "slippage_bps", "entry_date", "exit_date", "entry_open", "exit_close"):
            _require(row[key] == original[key], f"原交易欄位被變更：{row['trade_id']} / {key}")
        _require(row["source_row_json"] == canonical_json(original).decode("utf-8"), f"原交易完整列未保留：{row['trade_id']}")
        _require(row["source_trade_sha256"] == digest(canonical_json(original)), "原交易 row hash 不符")
        _require(row["source_signal_sha256"] == digest(canonical_json(signal)), "原 signal row hash 不符")
        _require(row["source_shares"] == original["shares"], "原始股數被變更")
        _require(row["original_strict_v3_status"] == original["strict_v3_status"], "原始 strict status 被變更")
        _require(row["original_proxy_net_return_pct"] == original["net_return_pct"], "原始 proxy 報酬被變更")
        _require(row["strict_lock_released"] == "False", "研究帳本不得解除原始 strict lock")
        _require(row["verified_total_return_pct"] == "", "未驗證總報酬必須留白")
        _require(row["primary_row_retained"] == "True", "不得刪除原始主要研究樣本")
        expected_disposition = "unresolved_anomaly_candidate" if original["anomaly_candidate"] == "True" else "not_finally_classified"
        _require(row["anomaly_disposition"] == expected_disposition, "不得擅自判定異常最終處置")
        _false_fields(row, ("coverage_complete", "formal_use", "promotion_evidence_allowed", "total_return_verified"))
        calculated = independent_accounting(original, events)
        for key, value in calculated.items():
            _require(row[key] == value, f"獨立公司行動帳本計算不符：{row['trade_id']} / {key}，expected={value!r} actual={row[key]!r}")


def _validate_blocked(rows, sources, positions):
    _require(len(rows) == 471, "blocked 必須完整保留 381 原列並加入 90 帳本缺口")
    original_counts = Counter(digest(canonical_json(row)) for row in sources["blocked"])
    originals = {digest(canonical_json(row)): row for row in sources["blocked"]}
    seen_originals = Counter()
    ledger_ids = []
    trades = {row["trade_id"]: row for row in sources["trades"]}
    by_id = {row["trade_id"]: row for row in positions}
    for row in rows:
        _false_fields(row)
        _require(row["primary_row_retained"] == "True", "blocked 不得剔除主要樣本")
        if row["record_type"] == "ledger_evidence_gap":
            _require(row["trade_id"] in trades, "帳本 blocked 連到未知交易")
            original = trades[row["trade_id"]]
            position = by_id[row["trade_id"]]
            ledger_ids.append(row["trade_id"])
            _require(row["status"] == position["corporate_action_status"] and row["reasons"] == position["block_reasons"],
                     "帳本 blocked 缺口與 position 不一致")
        else:
            source_hash = row["source_row_sha256"]
            _require(source_hash in originals, "blocked 原始 row hash 不在固定來源")
            original = originals[source_hash]
            seen_originals[source_hash] += 1
            _require(row["record_type"] == "source_" + original["record_type"] and row["trade_id"] == "",
                     "原始 blocked 類型或 trade_id 被變更")
            _require(row["status"] == original.get("strict_v3_status", "") and row["reasons"] == original["reasons"],
                     "原始 blocked 狀態／原因被變更")
        _require(row["source_row_sha256"] == digest(canonical_json(original)), "blocked 原始 row hash 不符")
        _require(row["source_row_json"] == canonical_json(original).decode("utf-8"), "blocked 未完整保留原列")
        for field in ("stock_id", "signal_date", "horizon"):
            _require(row[field] == original.get(field, ""), f"blocked 原列欄位不符：{field}")
    _require(seen_originals == original_counts, "原始 blocked 母體有遺漏／重複")
    _require(len(ledger_ids) == 90 and set(ledger_ids) == set(trades), "帳本缺口必須與 90 原交易一對一")


def _validate_report(payload, positions):
    _require(not payload.startswith(b"\xef\xbb\xbf") and b"\r" not in payload and payload.endswith(b"\n"),
             "報告必須使用 UTF-8/LF 且不得帶 BOM")
    report = payload.decode("utf-8")
    for text in (
        "# TDCC 潛伏吸籌：公司行動研究帳本 v1", SOURCE_REF, "截止日 20260909",
        "59 個來源訊號", "90 列原研究交易情境", "381 列原阻擋紀錄", "共 90 列", "10 bps 為 30 個",
        "不是選股重算、修正勝率或正式模型升級", "不同持有期不能當成互相獨立實驗",
        "未匹配事件不等於證明沒有其他事件", "原定 D+5／D+10／D+20 出場日、原訊號及持倉鎖不變",
        "不延長賣出日", "不得稱為修正績效", "所有 `verified_total_return_pct` 空白",
        "`total_return_verified=False`", "沒有正式勝率分母", "不作 signal PIT 證據",
        "沒有補回 21 個既有版本收據缺口", "異常候選保留原列", "`formal_use=False`", "`promotion_evidence_allowed=False`",
        "公告付款日不是實收證據", "`confirmed_cash_receipt` 空白", "六份 PDF",
    ):
        _require(text in report, f"報告缺少數量或研究限制說明：{text}")
    matches = sum(bool(row["matched_event_ids"]) for row in positions)
    _require(f"已知事件涉及 {matches} 列情境" in report, "報告已知事件情境數與實際 position 不符")
    facts = {
        "強生 4747": ["1 股換 2 股", "8/20～8/28", "8/31"],
        "青雲 5386": ["7/20", "500.00001386", "1.5 元", "8/14", "7/22／8/5", "不能賣出未到手權利"],
        "益得 6461": ["618.578", "9/9", "每股退還股款 0", "不假設畸零股"],
        "緯穎 6669": ["1982.79460", "9/2", "可交易日未取得", "9/16～9/30", "不是交付日期"],
    }
    for stock, tokens in facts.items():
        lines = [line for line in report.splitlines() if line.startswith(f"| {stock} |")]
        _require(len(lines) == 1, f"報告股票事件表缺少唯一列：{stock}")
        _tokens(lines[0], tokens, stock)


def validate_artifacts(repository_root, contract, artifacts):
    """測試入口；產物 bytes 由呼叫端提供，固定原件仍從指定 repo 讀取。"""
    errors = []
    try:
        root = Path(repository_root).resolve()
        expected = {artifact_name(kind) for kind in KINDS}
        _require(set(artifacts) == expected, "公司行動研究產物必須恰為五份，禁止缺檔／額外檔案")
        events = verify_contract(contract)
        verify_registration(root)
        sources = fixed_sources(root, contract)
        _validate_outputs(contract, artifacts, sources, events)
    except (ValueError, KeyError, TypeError, AttributeError, IndexError, ArithmeticError, UnicodeError,
            csv.Error, subprocess.CalledProcessError, OSError) as exc:
        errors.append(f"獨立帳本驗證 fail-closed：{type(exc).__name__}：{exc}")
    return errors


def _validate_outputs(contract, artifacts, sources, events):
    manifest = json_value(artifacts[artifact_name("source_manifest")])
    keys = {"schema_version", "artifact_version", "model_id", "ownership_id", "contract_sha256", "source_ref",
            "source_files", "document_sha256s", "artifacts", "counts", "formal_use", "promotion_evidence_allowed", "total_return_verified"}
    _require(set(manifest) == keys, "source_manifest 欄位集合不符")
    _require(type(manifest["schema_version"]) is int and manifest["schema_version"] == 1, "manifest schema_version 必須為整數 1")
    for key, value in {"artifact_version": ARTIFACT_VERSION, "model_id": MODEL_ID, "ownership_id": OWNER_ID,
                       "contract_sha256": APPROVED_CONTRACT_SHA256, "source_ref": SOURCE_REF,
                       "source_files": contract["source_files"], "document_sha256s": DOCUMENT_PINS}.items():
        _require(manifest[key] == value, f"source_manifest 來源欄位不符：{key}")
    for field in ("formal_use", "promotion_evidence_allowed", "total_return_verified"):
        _require(manifest[field] is False, f"source_manifest {field} 必須為 JSON false")
    counts = {"signals": 59, "trades": 90, "source_blocked": 381, "events": 5,
              "positions": 90, "blocked": 471, "verified_total_return_positions": 0}
    _require(manifest["counts"] == counts and all(type(value) is int for value in manifest["counts"].values()),
             "source_manifest 列數／已驗證總報酬數不符")
    expected_hashes = {name: {"sha256": digest(payload), "bytes": len(payload)}
                       for name, payload in artifacts.items() if name != artifact_name("source_manifest")}
    _require(manifest["artifacts"] == expected_hashes, "source_manifest 最終產物 bytes/hash 綁定不符")
    rows = {kind: csv_records(artifacts[artifact_name(kind)], fields, strict_transport=True)
            for kind, fields in SCHEMAS.items()}
    _validate_events(rows["events"], events)
    _validate_positions(rows["positions"], sources, events)
    _validate_blocked(rows["blocked"], sources, rows["positions"])
    _validate_report(artifacts[artifact_name("report")], rows["positions"])


def validate(repository_root, output_root=None):
    try:
        raw_root = Path(repository_root).absolute()
        raw_output = Path(output_root).absolute() if output_root is not None else raw_root / DEFAULT_DIRECTORY
        for target in (raw_root, raw_output):
            for path in (target, *target.parents):
                if path.exists() or path.is_symlink():
                    attributes = getattr(path.lstat(), "st_file_attributes", 0)
                    _require(not path.is_symlink() and not attributes & 0x400,
                             f"驗證路徑不得透過 symlink／reparse point：{path}")
        root, output = raw_root.resolve(), raw_output.resolve()
        contract = json_value((root / CONTRACT_FILE).read_bytes())
        paths = list(output.glob(PREFIX + "*"))
        _require(all(path.is_file() and not path.is_symlink() and not getattr(path.lstat(), "st_file_attributes", 0) & 0x400
                     for path in paths), "研究產物必須為實際一般檔案")
        # 缺檔必須失敗；絕不以 git HEAD 的舊產物冒充實際輸出。
        artifacts = {path.name: path.read_bytes() for path in paths}
    except (ValueError, OSError, UnicodeError) as exc:
        return [f"無法讀取實際契約／產物：{exc}"]
    return validate_artifacts(root, contract, artifacts)


def main(argv=None):
    parser = argparse.ArgumentParser(description="唯讀獨立驗證 TDCC 潛伏吸籌公司行動研究帳本")
    parser.add_argument("--repository-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-root", type=Path)
    args = parser.parse_args(argv)
    errors = validate(args.repository_root, args.output_root)
    print(json.dumps({"status": "fail" if errors else "pass", "errors": errors,
                      "formal_use": False, "promotion_evidence_allowed": False,
                      "total_return_verified": False}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
