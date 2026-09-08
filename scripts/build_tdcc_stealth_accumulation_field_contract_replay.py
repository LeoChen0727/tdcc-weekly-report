from __future__ import annotations

import argparse
import csv
import hashlib
import json
from contextlib import contextmanager
from decimal import Decimal
from pathlib import Path
from typing import Any, Iterator

import build_tdcc_stealth_accumulation_historical_replay as base
from model_research_artifact_guard import model_owned_artifact_guard


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = base.MODEL_ID
OWNER_ID = "tdcc_stealth_accumulation_field_contract_replay"
PRODUCER = "scripts/build_tdcc_stealth_accumulation_field_contract_replay.py"
ARTIFACT_VERSION = "tdcc_stealth_accumulation_historical_selector_field_contract_replay_v2"
REPLAY_KIND = "research_only_enum_field_contract_repair_same_historical_population"
SELECTOR_CONTRACT_VERSION = "current_selector_with_model_owned_enum_fallback_v2"
FIELD_CONTRACT_PATH = Path("config/tdcc_stealth_accumulation_research_field_contract_v2.csv")
DETAIL_NAME = "tdcc_stealth_accumulation_historical_selector_field_contract_replay_detail_v2.csv"
SUMMARY_NAME = "tdcc_stealth_accumulation_historical_selector_field_contract_replay_summary_v2.csv"
REPORT_NAME = "tdcc_stealth_accumulation_historical_selector_field_contract_replay_report_v2.md"
POSITIVE = {"strong_accumulation", "mild_accumulation"}
NONPOSITIVE = {"distribution_warning", "neutral"}
BASE_EVALUATE_SELECTOR = base.evaluate_selector
DETAIL_EXTRA_FIELDS = [
    "tdcc_accumulation_signal_raw",
    "tdcc_positive_resolution",
    "tdcc_positive_source",
    "tdcc_field_conflict",
    "tdcc_field_contract_status",
    "large_return_observation_codes",
    "large_return_spotcheck_status",
]
SUMMARY_EXTRA_FIELDS = [
    "observed_min_return_pct",
    "observed_max_return_pct",
    "automatic_anomaly_candidate_count",
    "bounded_large_return_spotcheck_count",
    "large_return_review_status",
]


def _text(value: Any) -> str:
    return base._text(value).lower()


def _recognized_polarity(value: str) -> str:
    if value in POSITIVE:
        return "positive"
    if value in NONPOSITIVE:
        return "nonpositive"
    return "unknown" if value else "blank"


def _resolve_tdcc_positive(row: dict[str, str], phase: str, status: str) -> dict[str, Any]:
    enum_raw, enum_source = base._row_text(row, "tdcc_accumulation_signal")
    enum_value = enum_raw.lower()
    status_polarity = _recognized_polarity(status)
    enum_polarity = _recognized_polarity(enum_value)
    conflict = bool(status and enum_value and status_polarity != enum_polarity)

    if phase:
        return {
            "positive": phase == "tdcc_leading_price",
            "resolution": (
                "explicit_phase_tdcc_leading_price"
                if phase == "tdcc_leading_price"
                else "explicit_phase_not_positive_or_forbidden"
            ),
            "source": "tdcc_price_phase",
            "conflict": conflict,
            "enum_raw": enum_value,
        }
    if status:
        current_boolean = base._flag(row, "tdcc_accumulation_signal")
        return {
            "positive": status in POSITIVE or current_boolean,
            "resolution": (
                "recognized_status_positive"
                if status in POSITIVE
                else "current_boolean_positive_preserved"
                if current_boolean
                else "recognized_status_nonpositive_fail_closed"
                if status in NONPOSITIVE
                else "unknown_status_fail_closed"
            ),
            "source": "status_alias",
            "conflict": conflict,
            "enum_raw": enum_value,
        }
    if base._flag(row, "tdcc_accumulation_signal"):
        return {
            "positive": True,
            "resolution": "current_boolean_positive_preserved",
            "source": enum_source or "tdcc_accumulation_signal",
            "conflict": False,
            "enum_raw": enum_value,
        }
    if enum_value in POSITIVE:
        return {
            "positive": True,
            "resolution": "recognized_enum_positive_fallback",
            "source": enum_source or "tdcc_accumulation_signal",
            "conflict": False,
            "enum_raw": enum_value,
        }
    if enum_value in NONPOSITIVE:
        return {
            "positive": False,
            "resolution": "recognized_enum_nonpositive_fail_closed",
            "source": enum_source or "tdcc_accumulation_signal",
            "conflict": False,
            "enum_raw": enum_value,
        }
    return {
        "positive": False,
        "resolution": "unknown_enum_fail_closed" if enum_value else "missing_positive_evidence_fail_closed",
        "source": enum_source or "",
        "conflict": False,
        "enum_raw": enum_value,
    }


def evaluate_selector(row: dict[str, str]) -> dict[str, Any]:
    phase, phase_source = base._row_text(row, "tdcc_price_phase")
    phase = phase.lower()
    status, status_source = base._row_text(row, "tdcc_status", "tdcc_judgement", "tdcc_judge")
    status = status.lower()
    resolution = _resolve_tdcc_positive(row, phase, status)
    result = BASE_EVALUATE_SELECTOR(row)
    phase_forbidden = phase in {"price_leading_tdcc", "overheated_after_tdcc"}
    phase_ok = bool(resolution["positive"]) and not phase_forbidden
    selected = (
        not phase_forbidden
        and not result["attack_already_started"]
        and result["volume_below_2_5"]
        and phase_ok
        and result["short_not_attacked"]
        and result["not_rallied"]
        and result["in_recent_range_10pct"]
    )
    result.update(
        {
            "tdcc_price_phase": phase,
            "tdcc_price_phase_source": phase_source,
            "tdcc_status": status,
            "tdcc_status_source": status_source,
            "tdcc_accumulation_signal": resolution["enum_raw"],
            "tdcc_accumulation_signal_raw": resolution["enum_raw"],
            "tdcc_positive_resolution": resolution["resolution"],
            "tdcc_positive_source": resolution["source"],
            "tdcc_field_conflict": resolution["conflict"],
            "tdcc_field_contract_status": "research_only_v2_enum_contract",
            "phase_ok": phase_ok,
            "selector_selected": selected,
        }
    )
    return result


def _field_contract_sha256(root: Path) -> str:
    payload = (root / FIELD_CONTRACT_PATH).read_bytes()
    rows = list(csv.DictReader(payload.decode("utf-8-sig").splitlines()))
    if {row["field_role"] for row in rows} != {"phase", "status", "enum_fallback"}:
        raise RuntimeError("field contract must define phase, status, and enum_fallback")
    enum_row = next(row for row in rows if row["field_role"] == "enum_fallback")
    if enum_row["unknown_behavior"] != "fail_closed":
        raise RuntimeError("adopted enum fallback must fail closed for unknown values")
    return hashlib.sha256(payload).hexdigest()


@contextmanager
def _patched_base(root: Path) -> Iterator[None]:
    contract_sha = _field_contract_sha256(root)
    patch = {
        "OWNER_ID": OWNER_ID,
        "PRODUCER": PRODUCER,
        "ARTIFACT_VERSION": ARTIFACT_VERSION,
        "REPLAY_KIND": REPLAY_KIND,
        "SELECTOR_CONTRACT_VERSION": SELECTOR_CONTRACT_VERSION,
        "DETAIL_NAME": DETAIL_NAME,
        "SUMMARY_NAME": SUMMARY_NAME,
        "REPORT_NAME": REPORT_NAME,
        "DETAIL_FIELDS": list(base.DETAIL_FIELDS) + DETAIL_EXTRA_FIELDS,
        "SUMMARY_FIELDS": list(base.SUMMARY_FIELDS) + SUMMARY_EXTRA_FIELDS,
        "evaluate_selector": evaluate_selector,
        "_selector_contract_sha256": lambda: hashlib.sha256(
            json.dumps(
                {
                    "version": SELECTOR_CONTRACT_VERSION,
                    "field_contract_sha256": contract_sha,
                    "positive_enum": sorted(POSITIVE),
                    "nonpositive_enum": sorted(NONPOSITIVE),
                    "unknown": "fail_closed",
                    "conflict": "record_preserve_existing_priority",
                    "unchanged_gates": "attack;volume;return_5d;return_20d;recent_range",
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest(),
    }
    original = {name: getattr(base, name) for name in patch}
    try:
        for name, value in patch.items():
            setattr(base, name, value)
        yield
    finally:
        for name, value in original.items():
            setattr(base, name, value)


def build(*, root: Path, source_ref: str):
    with _patched_base(root):
        detail, summary, report = base.build(root=root, source_ref=source_ref)
    observations: list[tuple[int, str, dict[str, str], Decimal]] = []
    for horizon in (5, 10, 20):
        key = f"return_d{horizon}_pct"
        rows = [(row, Decimal(row[key])) for row in detail if row[key]]
        for label, selected in (("min", min(rows, key=lambda item: item[1])), ("max", max(rows, key=lambda item: item[1]))):
            selected_row, value = selected
            code = f"d{horizon}_{label}_observed_return"
            existing = selected_row.get("large_return_observation_codes", "")
            selected_row["large_return_observation_codes"] = ";".join(filter(None, (existing, code)))
            selected_row["large_return_spotcheck_status"] = "unresolved_bounded_source_continuity_check_only"
            observations.append((horizon, label, selected_row, value))
    summary_by_horizon = {int(row["horizon"][1:]): row for row in summary}
    for horizon in (5, 10, 20):
        values = [Decimal(row[f"return_d{horizon}_pct"]) for row in detail if row[f"return_d{horizon}_pct"]]
        row = summary_by_horizon[horizon]
        row["phase_classifier_status"] = "not_invoked_model_owned_enum_field_contract_repair_v2"
        row["promotion_blockers"] += ";field_contract_repair_is_research_only_not_production_semantics"
        row["observed_min_return_pct"] = base._fmt_number(min(values))
        row["observed_max_return_pct"] = base._fmt_number(max(values))
        row["automatic_anomaly_candidate_count"] = row["unresolved_anomaly_candidate_count"]
        row["bounded_large_return_spotcheck_count"] = "2"
        row["large_return_review_status"] = "unresolved_not_an_exclusion_or_correction"
    report = report.replace(
        "historical selector research replay v1",
        "historical selector field-contract repair replay v2",
        1,
    )
    source_sha = summary[0]["source_commit_sha"]
    date_min = summary[0]["snapshot_report_date_min"]
    date_max = summary[0]["snapshot_report_date_max"]
    published_match_count = summary[0]["published_membership_match_count"]
    conclusion_start = report.index("本報告是固定 ")
    conclusion_end = report.index("\n\n## 研究績效", conclusion_start)
    report = (
        report[:conclusion_start]
        + f"本報告以固定 `{source_sha}` 的選股條件為基礎，套用本次 research-only 欄位修復版本；不是 production selector，也不是當時實際發布推薦。資料日期為 {date_min}–{date_max}，共讀取 36 個 immutable commit-bound 候選快照、19361 列候選，v2 選出 {len(detail)} signal rows、{len({row['stock_id'] for row in detail})} stocks；其中與實際發布的 `{MODEL_ID}` 推薦相符 {published_match_count} 列。同母體 v1 current-rule replay 仍為 0 列。"
        + report[conclusion_end:]
    )
    report = report.replace(
        "未解異常候選 |",
        "列級自動候選數（任一窗觸發） |",
    )
    report = report.replace("## 零樣本資料契約診斷", "## 欄位契約診斷")
    report = report.replace(
        "這是歷史 snapshot 與 current selector 的欄位語意不相容，不能解讀為真實沒有正向 TDCC 狀態，也不能在本研究中擅自 reinterpret enum。",
        "v2 只在 phase 與 status 皆空白、且既有 boolean 路徑未放行時，依獨立研究欄位契約將 `mild_accumulation` / `strong_accumulation` 解讀為正向 fallback；`distribution_warning` / `neutral` 與 unknown 不放行。其他衝突只揭露並保留既有優先序。此修復不改 production selector。",
    )
    report = report.replace(
        "- phase：不呼叫任何共用 `classify_tdcc_price_phase()`；完整保留現行空白 `tdcc_price_phase` 加 `tdcc_positive` fallback。",
        "- phase / status / enum：不呼叫共用 phase classifier；保留 current selector 的 phase、status alias 與 boolean 行為，只對兩者空白時的已知正向 enum增加研究 fallback。",
    )
    report = report.replace(
        "- 同股重疊：全部保留於 primary metrics，並在 detail 標記。",
        "- 同股後續/重複訊號：`overlap_with_prior_signal=True` 只表示同股票已有更早 signal；不是依 D5/D10/D20 持倉窗驗證的真正重疊部位。全部 signal rows 保留於 primary metrics，因此結果是訊號列加權，不是獨立部位或投組績效。",
    )
    automatic_candidates = [row for row in detail if row["anomaly_candidate"] == "True"]
    automatic_candidate_text = "；".join(
        f"`{row['stock_id']}` {row['candidate_signal_date']}（{row['anomaly_trigger_codes']}）"
        for row in automatic_candidates
    ) or "無"
    report = report.replace(
        "- 異常：數值觸發只標記 `unresolved_anomaly_candidate`，仍保留於 primary；排除後僅為 sensitivity，不能稱為修正績效。",
        f"- 異常：表中各 horizon 顯示的是同一組列級自動候選（任一窗觸發），不是各窗各自新增；本次為 {automatic_candidate_text}。候選仍保留於 primary；排除後僅為 sensitivity，不能稱為修正績效。",
    )
    report = report.replace(
        "- PIT：候選與價格檔均綁定 source commit 與 SHA-256，但 snapshot `generated_at` 不是完整 event-time filed-at 證明；價格調整／公司行動基礎尚未權威核實。",
        "- PIT：候選與價格檔均綁定 source commit 與 SHA-256，但 snapshot `generated_at` 不是完整 event-time filed-at 證明；價格調整／公司行動基礎尚未權威核實。`invalid_price_count=0` 只表示既有價格有效性檢查通過，不證明交易日完整性或調整基礎。",
    )
    report += (
        "\n## v1 / v2 比較界線\n\n"
        "- v1 current-rule replay：同一歷史母體選出 0 列，原因是 enum 被 boolean `flag()` 讀取。\n"
        f"- v2 field-contract replay：同一歷史母體選出 {len(detail)} 列；這不是 `8434`，後者只是通過前三關且 enum 為正向的診斷列數。\n"
        "- 三個上游 enum producer 的 strong/mild 細節不同，snapshot 無法證明逐列 producer branch；只採共同允許值語意。\n"
        "- 結論仍為 advisory-only；不得作 promotion、正式 ranking/scoring、PDF 或 operation evidence。\n"
    )
    tree = base.GitTree(root, source_ref)
    prices = base._load_prices(tree, min(row["candidate_signal_date"] for row in detail))
    report += (
        "\n## 大幅報酬有界 spot-check 待解清單\n\n"
        "下列僅列各 horizon 的 observed min/max，最多六組。`automatic anomaly candidate` 仍只有既有 `abs(return)>=80%` 規則標記的列；本表其他數字是人工查核待解觀察，不是新增排除規則。來源價格序列連續只代表 immutable source 中從 entry 到 exit 可取得預期列數，不能替代公司行動、除權息或調整基礎的權威證據。\n\n"
        "| horizon | observation | stock | signal | entry | exit | return | source sequence | entry SHA-256 | exit SHA-256 | status |\n"
        "|---|---|---|---|---|---|---:|---|---|---|---|\n"
    )
    for horizon, label, row, value in observations:
        stock_prices = prices[row["stock_id"]]
        entry_index = next(index for index, price in enumerate(stock_prices) if price.date == row["entry_date"])
        exit_index = next(index for index, price in enumerate(stock_prices) if price.date == row[f"exit_d{horizon}_date"])
        sequence = "available_source_sequence_matches_D_horizon" if exit_index - entry_index == horizon else "unresolved_source_sequence_gap"
        report += (
            f"| D{horizon} | observed {label} | {row['stock_id']} {row['stock_name']} | {row['candidate_signal_date']} | "
            f"{row['entry_date']} @ {row['entry_open_price']} | {row[f'exit_d{horizon}_date']} @ {row[f'exit_d{horizon}_close_price']} | "
            f"{base._fmt_number(value)}% | {sequence} | `{row['entry_price_source_sha256']}` | "
            f"`{row[f'exit_d{horizon}_price_source_sha256']}` | unresolved; retained in primary |\n"
        )
    return detail, summary, report


def _artifact_guard(root: Path):
    sparse = base.subprocess.run(
        ["git", "config", "--bool", "core.sparseCheckout"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout.strip().lower() == "true"
    if sparse:
        return base._sparse_model_owned_artifact_guard(root)
    return model_owned_artifact_guard(
        OWNER_ID,
        PRODUCER,
        root=root,
        registry_path=root / "config/model_research_artifact_ownership.csv",
        sentinel_registry_path=root / "config/model_research_protected_sentinels.csv",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build research-only TDCC enum field-contract replay v2.")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--source-ref", default="HEAD")
    args = parser.parse_args(argv)
    root = args.repository_root.resolve()
    detail, summary, report = build(root=root, source_ref=args.source_ref)
    with _patched_base(root):
        with _artifact_guard(root):
            base._write_outputs(root, detail, summary, report)
    print(f"tdcc_stealth_field_contract_replay_detail_rows={len(detail)}")
    print(f"tdcc_stealth_field_contract_replay_summary_rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
