from __future__ import annotations

"""volume_range_breakout_v2_high_position_volume_attack 的凍結 D10/D15 日期對帳；不是策略或正式績效 producer。"""

import argparse
import csv
from datetime import datetime
import hashlib
import io
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
DATE_FIELDS = ("signal_date", "confirmation_date", "entry_date", "exit_date")


def row_digest(row: dict[str, str]) -> str:
    canonical = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def read_frozen_csv(blob: bytes, expected_sha256: str) -> list[dict[str, str]]:
    if hashlib.sha256(blob).hexdigest() != expected_sha256:
        raise ValueError("來源 SHA-256 與凍結版本不符")
    reader = csv.DictReader(io.StringIO(blob.decode("utf-8-sig")))
    header = reader.fieldnames or []
    required = {"source_event_key", "stock_id", "artifact_version", *DATE_FIELDS}
    if len(header) != len(set(header)) or not required.issubset(header):
        raise ValueError("來源欄位缺漏或重複")
    rows = list(reader)
    keys = [r.get("source_event_key", "") for r in rows]
    if not rows or not all(keys) or len(keys) != len(set(keys)):
        raise ValueError("來源事件 key 空白或重複")
    if any(None in r or any(v is None for v in r.values()) for r in rows):
        raise ValueError("CSV 列長度與欄位不符")
    return rows


def verify_dates(row: dict[str, str]) -> None:
    for field in DATE_FIELDS:
        value = row[field]
        if len(value) != 8 or not value.isascii() or not value.isdigit():
            raise ValueError(f"日期缺漏或格式錯誤: {field}")
        datetime.strptime(value, "%Y%m%d")
    if not row["signal_date"] < row["confirmation_date"] < row["entry_date"] <= row["exit_date"]:
        raise ValueError("收盤確認／進出場日期順序錯誤")
    if not row["stock_id"]:
        raise ValueError("股票身份缺漏")


def reconcile(
    d15_blob: bytes,
    d10_blob: bytes,
    *,
    expected_d15_sha256: str = D15_SHA256,
    expected_d10_sha256: str = D10_SHA256,
) -> dict[str, Any]:
    d15 = read_frozen_csv(d15_blob, expected_d15_sha256)
    d10 = read_frozen_csv(d10_blob, expected_d10_sha256)
    if {r["artifact_version"] for r in d15} != {D15_VERSION}:
        raise ValueError("D15 artifact version 錯誤")
    if {r["artifact_version"] for r in d10} != {D10_VERSION}:
        raise ValueError("D10 artifact version 錯誤")
    if any(r.get("candidate_model_id") != MODEL_ID or r.get("base_model_member") not in {"True", "False"} for r in d15):
        raise ValueError("D15 模型或 base membership 錯誤")
    target = [(i + 2, r) for i, r in enumerate(d15) if r.get("base_model_member") == "True"]
    if not target:
        raise ValueError("來源沒有目標模型列")
    if {r.get("model_id", "") for r in d10} != {"volume_range_breakout"}:
        raise ValueError("D10 原研究模型錯誤")
    d10_by_key = {r["source_event_key"]: (i + 2, r) for i, r in enumerate(d10)}
    rows: list[dict[str, Any]] = []
    for line_number, current in target:
        verify_dates(current)
        found = d10_by_key.get(current["source_event_key"])
        if found is None:
            raise ValueError("D15 事件缺原 D10 admission 證據")
        d10_line, original = found
        verify_dates(original)
        if original.get("same_stock_non_overlap_included") != "True":
            raise ValueError("原 D10 admission 並非已納入")
        identity = ("stock_id", "signal_date", "confirmation_date", "entry_date")
        if any(current[k] != original[k] for k in identity):
            raise ValueError("D10 與 D15 身份或進場日期不同")
        rows.append({
            "source_event_key": current["source_event_key"],
            "stock_id": current["stock_id"],
            "d15_csv_record_number": line_number,
            "d15_source_row_sha256": row_digest(current),
            "d15_source_row": dict(current),
            "original_d10_csv_record_number": d10_line,
            "original_d10_source_row_sha256": row_digest(original),
            "original_d10_source_row": dict(original),
            "original_d10_admitted": True,
        })
    ordered = sorted(rows, key=lambda r: (
        r["stock_id"], r["d15_source_row"]["entry_date"],
        r["d15_source_row"]["exit_date"], r["source_event_key"],
    ))
    pairs: list[dict[str, Any]] = []
    for index, first in enumerate(ordered):
        for second in ordered[index + 1:]:
            if first["stock_id"] != second["stock_id"]:
                continue
            a, b = first["d15_source_row"], second["d15_source_row"]
            old_exit = first["original_d10_source_row"]["exit_date"]
            if b["entry_date"] <= old_exit:
                raise ValueError("目標樣本的原 D10 admission 已有持倉交疊")
            if b["entry_date"] <= a["exit_date"]:
                pairs.append({
                    "stock_id": first["stock_id"],
                    "first_source_event_key": first["source_event_key"],
                    "second_source_event_key": second["source_event_key"],
                    "first_d10_exit_date": old_exit,
                    "first_d15_exit_date": a["exit_date"],
                    "second_confirmation_date": b["confirmation_date"],
                    "second_entry_date": b["entry_date"],
                    "original_d10_windows_overlap": False,
                    "d15_windows_overlap": True,
                    "same_day_entry_and_prior_exit": b["entry_date"] == a["exit_date"],
                })
    return {
        "schema_version": 1,
        "audit_id": AUDIT_ID,
        "model_id": MODEL_ID,
        "source_commit": SOURCE_COMMIT,
        "scope": "frozen_research_d15_dates_only_not_formal_positions",
        "audit_record_complete": True,
        "formal_publication_parity_verified": False,
        "formal_position_parity_verified": False,
        "promotion_allowed": False,
        "return_evidence_allowed": False,
        "all_target_rows_preserved": True,
        "original_unresolved_flags_preserved": True,
        "primary_statistics_modified": False,
        "new_returns_calculated": False,
        "network_used": False,
        "sources": {
            "d15": {"path": D15_PATH, "sha256": expected_d15_sha256, "artifact_version": D15_VERSION},
            "d10_admission": {"path": D10_PATH, "sha256": expected_d10_sha256, "artifact_version": D10_VERSION},
        },
        "source_d15_record_count": len(d15),
        "research_row_count": len(rows),
        "retained_row_count": len(rows),
        "overlap_pair_count": len(pairs),
        "rows": rows,
        "overlap_pairs": pairs,
        "limitations": [
            "原 D10 admission 不等於 D15 持倉不重疊。所有原研究列及欄位保留，不產刪列子集績效。",
            "未讀正式發布排名與持倉，未核三個 volume 模型間的競合；不能宣稱正式發布或持倉 parity。",
            "正式 adapter 在確認日即由 active 壓制新 confirmed，出場當日仍 active；此對帳不模擬該流程。",
            "來源列 hash 是 UTF-8 canonical JSON（欄名排序、無額外空白）的 SHA-256，非原始 CSV 行 bytes。",
        ],
    }


def read_git_blob(repo_root: Path, path: str) -> bytes:
    env = dict(os.environ, GIT_NO_LAZY_FETCH="1")
    return subprocess.check_output(
        ["git", "-C", str(repo_root), "show", f"{SOURCE_COMMIT}:{path}"], env=env,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="凍結研究 D10/D15 日期對帳；不計算新報酬。")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--require-formal-position-parity", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.output.resolve().is_relative_to(args.repo_root.resolve()):
            raise ValueError("audit receipt 必須保存在 repo 以外的證據目錄")
        receipt = reconcile(read_git_blob(args.repo_root, D15_PATH), read_git_blob(args.repo_root, D10_PATH))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(receipt, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print(json.dumps({"audit_record_complete": True, "research_row_count": receipt["research_row_count"],
                          "overlap_pair_count": receipt["overlap_pair_count"],
                          "formal_position_parity_verified": False}, ensure_ascii=False))
        if args.require_formal_position_parity:
            print("阻擋：沒有正式發布與持倉 parity 證據。")
            return 2
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"對帳失敗：{error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
