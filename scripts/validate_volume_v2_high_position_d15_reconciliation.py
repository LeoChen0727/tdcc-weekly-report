from __future__ import annotations

"""從凍結 bytes 獨立核對 volume_range_breakout_v2_high_position_volume_attack 日期 receipt；不匯入 producer。"""

import argparse
import csv
from datetime import datetime
import hashlib
import io
from itertools import combinations
import json
import os
from pathlib import Path
import subprocess
from typing import Any

MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"
AUDIT_ID = "volume_v2_high_position_d15_reconciliation_v1"
SOURCE_COMMIT = "e74d928fd34fc0f5e0c7c91ac1e5041f310851e5"
D15_PATH = "output/latest/research_backtest/volume_range_breakout_v2_high_position_improvement_audit_detail_latest.csv"
D15_SHA256 = "30e9be57e9f4d5456cb57255ff0d181c5a1da5b1246ff91a6c14e5aef9b0c941"
D15_VERSION = "volume_range_breakout_v2_high_position_improvement_audit_20260710"
D10_PATH = "output/latest/research_backtest/volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv"
D10_SHA256 = "46ec3908143b2e89720ca23b3c90a2cb253655b3f72084374c8f04032218294e"
D10_VERSION = "volume_range_breakout_v2_overlap_sensitivity_20260708"


def independently_parse(blob: bytes, expected_hash: str) -> list[dict[str, str]]:
    if hashlib.sha256(blob).hexdigest() != expected_hash:
        raise ValueError("來源 hash 漂移")
    reader = csv.DictReader(io.StringIO(blob.decode("utf-8-sig")))
    fields = reader.fieldnames or []
    required = {"source_event_key", "stock_id", "artifact_version", "signal_date", "confirmation_date", "entry_date", "exit_date"}
    if len(fields) != len(set(fields)) or required - set(fields):
        raise ValueError("來源欄位缺漏或重複")
    result = list(reader)
    keys = [row.get("source_event_key") for row in result]
    if not result or not all(keys) or len(set(keys)) != len(keys):
        raise ValueError("事件 key 空白或重複")
    if any(None in row or any(v is None for v in row.values()) for row in result):
        raise ValueError("CSV 欄列長度不符")
    return result


def independently_check_dates(row: dict[str, str]) -> None:
    parsed = []
    for name in ("signal_date", "confirmation_date", "entry_date", "exit_date"):
        raw = row[name]
        if len(raw) != 8 or not raw.isascii() or not raw.isdigit():
            raise ValueError("來源日期缺漏")
        parsed.append(datetime.strptime(raw, "%Y%m%d"))
    if not parsed[0] < parsed[1] < parsed[2] <= parsed[3] or not row["stock_id"]:
        raise ValueError("來源身份或時序錯誤")


def independent_row_hash(row: dict[str, str]) -> str:
    encoded = json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_receipt(
    receipt: dict[str, Any],
    d15_blob: bytes,
    d10_blob: bytes,
    *,
    expected_d15_sha256: str = D15_SHA256,
    expected_d10_sha256: str = D10_SHA256,
) -> None:
    if not isinstance(receipt, dict):
        raise ValueError("receipt 必須是 JSON object")
    current = independently_parse(d15_blob, expected_d15_sha256)
    original = independently_parse(d10_blob, expected_d10_sha256)
    if {r["artifact_version"] for r in current} != {D15_VERSION}:
        raise ValueError("D15 version 錯誤")
    if {r["artifact_version"] for r in original} != {D10_VERSION}:
        raise ValueError("D10 version 錯誤")
    if {r.get("candidate_model_id") for r in current} != {MODEL_ID} or any(r.get("base_model_member") not in {"True", "False"} for r in current):
        raise ValueError("D15 模型或 base membership 錯誤")
    selected = [(i + 2, r) for i, r in enumerate(current) if r.get("base_model_member") == "True"]
    if not selected:
        raise ValueError("缺目標模型列")
    if any(row.get("model_id") != "volume_range_breakout" for row in original):
        raise ValueError("原 D10 模型錯誤")
    originals = {r["source_event_key"]: (index + 2, r) for index, r in enumerate(original)}
    expected_top = {
        "schema_version": 1, "audit_id": AUDIT_ID, "model_id": MODEL_ID,
        "source_commit": SOURCE_COMMIT, "scope": "frozen_research_d15_dates_only_not_formal_positions",
        "audit_record_complete": True, "formal_publication_parity_verified": False,
        "formal_position_parity_verified": False, "promotion_allowed": False,
        "return_evidence_allowed": False, "all_target_rows_preserved": True,
        "original_unresolved_flags_preserved": True, "primary_statistics_modified": False,
        "new_returns_calculated": False, "network_used": False,
        "source_d15_record_count": len(current), "research_row_count": len(selected),
        "retained_row_count": len(selected),
        "sources": {
            "d15": {"path": D15_PATH, "sha256": expected_d15_sha256, "artifact_version": D15_VERSION},
            "d10_admission": {"path": D10_PATH, "sha256": expected_d10_sha256, "artifact_version": D10_VERSION},
        },
    }
    for name, value in expected_top.items():
        actual = receipt.get(name)
        if type(actual) is not type(value) or actual != value:
            raise ValueError(f"receipt 欄位錯誤: {name}")
    received_rows = receipt.get("rows")
    if not isinstance(received_rows, list) or len(received_rows) != len(selected):
        raise ValueError("原研究列沒有全數保留")
    for (line, row), observed in zip(selected, received_rows):
        independently_check_dates(row)
        before = originals.get(row["source_event_key"])
        if before is None:
            raise ValueError("缺原 D10 admission")
        old_line, old = before
        independently_check_dates(old)
        if old.get("same_stock_non_overlap_included") != "True":
            raise ValueError("原 D10 不在 admission")
        if any(row[k] != old[k] for k in ("stock_id", "signal_date", "confirmation_date", "entry_date")):
            raise ValueError("D10/D15 身份不符")
        expected = {
            "source_event_key": row["source_event_key"], "stock_id": row["stock_id"],
            "d15_csv_record_number": line, "d15_source_row_sha256": independent_row_hash(row),
            "d15_source_row": row, "original_d10_csv_record_number": old_line,
            "original_d10_source_row_sha256": independent_row_hash(old),
            "original_d10_source_row": old, "original_d10_admitted": True,
        }
        if json.dumps(observed, sort_keys=True, ensure_ascii=False) != json.dumps(expected, sort_keys=True, ensure_ascii=False):
            raise ValueError("原列身份、日期、原始標記或 row hash 被改動")
    pairs = []
    by_key = {r["source_event_key"]: r for _, r in selected}
    order = lambda r: (r["stock_id"], r["entry_date"], r["exit_date"], r["source_event_key"])
    for left, right in combinations(by_key.values(), 2):
        if left["stock_id"] != right["stock_id"]:
            continue
        a, b = sorted((left, right), key=order)
        old_exit = originals[a["source_event_key"]][1]["exit_date"]
        if b["entry_date"] <= old_exit:
            raise ValueError("原 D10 admission 交疊")
        if a["entry_date"] <= b["exit_date"] and b["entry_date"] <= a["exit_date"]:
            pairs.append({
                "stock_id": a["stock_id"], "first_source_event_key": a["source_event_key"],
                "second_source_event_key": b["source_event_key"], "first_d10_exit_date": old_exit,
                "first_d15_exit_date": a["exit_date"], "second_confirmation_date": b["confirmation_date"],
                "second_entry_date": b["entry_date"], "original_d10_windows_overlap": False,
                "d15_windows_overlap": True,
                "same_day_entry_and_prior_exit": b["entry_date"] == a["exit_date"],
            })
    pair_order = lambda pair: (order(by_key[pair["first_source_event_key"]]), order(by_key[pair["second_source_event_key"]]))
    pairs.sort(key=pair_order)
    if type(receipt.get("overlap_pair_count")) is not int or receipt["overlap_pair_count"] != len(pairs):
        raise ValueError("重疊 pair 數量錯誤")
    if json.dumps(receipt.get("overlap_pairs"), sort_keys=True, ensure_ascii=False) != json.dumps(pairs, sort_keys=True, ensure_ascii=False):
        raise ValueError("重疊 pair 或日期邊界錯誤")
    if not isinstance(receipt.get("limitations"), list) or len(receipt["limitations"]) < 4:
        raise ValueError("缺研究與正式持倉的限制說明")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="獨立核對凍結研究日期 receipt；不是正式持倉驗收。")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--require-formal-position-parity", action="store_true")
    args = parser.parse_args(argv)
    try:
        env = dict(os.environ, GIT_NO_LAZY_FETCH="1")
        def frozen(path: str) -> bytes:
            return subprocess.check_output(["git", "-C", str(args.repo_root), "show", f"{SOURCE_COMMIT}:{path}"], env=env)
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
        validate_receipt(receipt, frozen(D15_PATH), frozen(D10_PATH))
        print("凍結研究日期 receipt 核對通過；正式發布及持倉 parity 仍未通過。")
        if args.require_formal_position_parity:
            return 2
        return 0
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print(f"獨立核對失敗：{error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
