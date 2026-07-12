from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    from model_data_independence import (
        CONDITION_SPEC,
        DATA_SHARING_REGISTRY,
        FORMAL_EVIDENCE_PINS,
        MODEL_OWNERSHIP,
        RESEARCH_ARTIFACT_OWNERSHIP,
        ROOT,
        SHARED_SEMANTICS,
        VALIDATOR_INDEPENDENCE,
        comprehensive_validation,
        split_list,
    )
except ModuleNotFoundError:  # Loaded as scripts.build_model_data_independence_audit.
    from scripts.model_data_independence import (
        CONDITION_SPEC,
        DATA_SHARING_REGISTRY,
        FORMAL_EVIDENCE_PINS,
        MODEL_OWNERSHIP,
        RESEARCH_ARTIFACT_OWNERSHIP,
        ROOT,
        SHARED_SEMANTICS,
        VALIDATOR_INDEPENDENCE,
        comprehensive_validation,
        split_list,
    )


OUTPUT_CSV = ROOT / "output" / "latest" / "model_data_independence_audit_latest.csv"
OUTPUT_MD = ROOT / "output" / "latest" / "model_data_independence_audit_latest.md"
DOCS_CSV = ROOT / "docs" / "latest" / "model_data_independence_audit_latest.csv"
DOCS_MD = ROOT / "docs" / "latest" / "model_data_independence_audit_latest.md"

OUTPUT_COLUMNS = (
    "generated_at",
    "domain",
    "subject",
    "status",
    "ownership_mode",
    "consumer_count",
    "evidence",
    "remaining_gap",
)


def _read(path: Path) -> list[dict[str, str]]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = [{key: str(value or "").strip() for key, value in row.items()} for row in reader]
    if errors:
        raise RuntimeError("; ".join(errors))
    return rows


def build_rows(generated_at: str) -> list[dict[str, str]]:
    errors, semantics = comprehensive_validation(base_ref="")
    if errors:
        raise RuntimeError("independence contracts are invalid: " + "; ".join(errors))
    ownership = {row["model_id"]: row for row in _read(MODEL_OWNERSHIP)}
    shared = _read(SHARED_SEMANTICS)
    data = _read(DATA_SHARING_REGISTRY)
    validator_rows = _read(VALIDATOR_INDEPENDENCE)
    research_rows = _read(RESEARCH_ARTIFACT_OWNERSHIP)
    condition = {row["model_id"]: row for row in _read(CONDITION_SPEC)}
    pinned = {row["model_id"] for row in _read(FORMAL_EVIDENCE_PINS)}

    shared_counts: dict[str, int] = {model_id: 0 for model_id in semantics}
    legacy_counts: dict[str, int] = {model_id: 0 for model_id in semantics}
    for row in shared:
        for model_id in split_list(row["consumer_models"]):
            shared_counts[model_id] = shared_counts.get(model_id, 0) + 1
            if row["semantic_class"] == "contained_legacy_cross_model_semantic":
                legacy_counts[model_id] = legacy_counts.get(model_id, 0) + 1

    rows: list[dict[str, str]] = []
    for model_id in sorted(semantics):
        owner = ownership[model_id]
        status = "PASS" if owner["ownership_status"] == "model_owned_module" else "CONTAINED"
        remaining = "none"
        if status == "CONTAINED":
            remaining = (
                "existing shared producer/semantic remains frozen; future model must use a model-owned module"
            )
        rows.append(
            {
                "generated_at": generated_at,
                "domain": "production_model_semantics",
                "subject": model_id,
                "status": status,
                "ownership_mode": owner["ownership_status"],
                "consumer_count": "1",
                "evidence": (
                    f"source={owner['production_source_file']}; entries={owner['execution_entry_functions']}; "
                    f"semantic_items={owner['semantic_item_count']}; sha256={owner['semantic_sha256']}; "
                    f"shared_items={shared_counts.get(model_id, 0)}; legacy_shared_items={legacy_counts.get(model_id, 0)}"
                ),
                "remaining_gap": remaining,
            }
        )

    for semantic_class in sorted({row["semantic_class"] for row in shared}):
        class_rows = [row for row in shared if row["semantic_class"] == semantic_class]
        status = "PASS" if semantic_class == "shared_technical" else "CONTAINED"
        rows.append(
            {
                "generated_at": generated_at,
                "domain": "shared_production_semantics",
                "subject": semantic_class,
                "status": status,
                "ownership_mode": semantic_class,
                "consumer_count": str(len({m for row in class_rows for m in split_list(row['consumer_models'])})),
                "evidence": f"registered_semantic_items={len(class_rows)}; exact consumers and AST SHA are pinned",
                "remaining_gap": (
                    "none" if status == "PASS" else "legacy sharing is contained but not physically separated"
                ),
            }
        )

    for row in data:
        contained_modes = {
            "latest_context_not_historical",
            "cross_model_audit_not_model_evidence",
            "legacy_frozen_no_new_consumers",
        }
        rows.append(
            {
                "generated_at": generated_at,
                "domain": "data_family_ownership",
                "subject": row["data_family_id"],
                "status": "CONTAINED" if row["ownership_mode"] in contained_modes else "PASS",
                "ownership_mode": row["ownership_mode"],
                "consumer_count": str(len(split_list(row["approved_consumer_models"]))),
                "evidence": (
                    f"writer={row['registered_producers']}; write_scope={row['producer_write_scope']}; "
                    f"access={row['consumer_access_mode']}; contract_sha256={row['data_contract_sha256']}; "
                    f"migration={row['last_migration_id']}; decision={row['sharing_decision_reference']}"
                ),
                "remaining_gap": (
                    "legacy/latest/audit data is barred from formal model evidence"
                    if row["ownership_mode"] in contained_modes
                    else "none"
                ),
            }
        )

    model_owned_research = {
        row["owner_model_id"]: row["producer"]
        for row in research_rows
        if row["change_policy"] == "model_owned_write"
    }
    for model_id, model_contract in sorted(condition.items()):
        research_owner = (
            "volume_range_breakout_v2"
            if model_id.startswith("volume_range_breakout_v2_")
            else model_id
        )
        producer = model_owned_research.get(research_owner, "")
        isolated = bool(producer)
        rows.append(
            {
                "generated_at": generated_at,
                "domain": "research_producer_ownership",
                "subject": model_id,
                "status": "PASS" if isolated else "CONTAINED",
                "ownership_mode": (
                    "model_owned_write"
                    if isolated
                    else "no_enabled_model_owned_research_entrypoint"
                ),
                "consumer_count": "1",
                "evidence": (
                    f"research_baseline_status={model_contract['research_baseline_status']}; "
                    f"producer={producer or 'none'}; research workflow cannot fall back to the legacy aggregate"
                ),
                "remaining_gap": (
                    "none"
                    if isolated
                    else "before reopening research this model needs its own producer artifact allowlist and sentinel test"
                ),
            }
        )

    for model_id, row in sorted(condition.items()):
        if row["operation_contract"].lower() in {"", "none"}:
            continue
        rows.append(
            {
                "generated_at": generated_at,
                "domain": "formal_evidence_binding",
                "subject": model_id,
                "status": "PASS" if model_id in pinned else "FAIL",
                "ownership_mode": "pinned_formal_evidence",
                "consumer_count": "1",
                "evidence": f"operation_contract={row['operation_contract']}; evidence_pin={model_id in pinned}",
                "remaining_gap": "none" if model_id in pinned else "formal evidence pin missing",
            }
        )

    for row in validator_rows:
        independent = row["independence_claim"].lower() == "true"
        rows.append(
            {
                "generated_at": generated_at,
                "domain": "validator_independence",
                "subject": row["validator_path"],
                "status": "PASS" if independent else "DISCLOSED_NOT_INDEPENDENT",
                "ownership_mode": row["validator_role"],
                "consumer_count": "1",
                "evidence": (
                    f"imports_production_symbols={row['imported_production_symbols'] or 'none'}; "
                    f"allowed_use={row['allowed_evidence_use']}"
                ),
                "remaining_gap": (
                    "none" if independent else "may verify implementation consistency only; cannot prove model correctness independently"
                ),
            }
        )
    return rows


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, str]], generated_at: str) -> None:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    lines = [
        "# 每日股票模型與資料獨立性稽核",
        "",
        f"- 產生時間：`{generated_at}`",
        f"- 結果：`{', '.join(f'{key}={value}' for key, value in sorted(counts.items()))}`",
        "- 原則：新模型與新資料 family 預設獨立；跨模型共用商業語意必須先有使用者核准與 migration evidence。",
        "- `CONTAINED` 代表既有共用已被凍結與精確盤點，不代表已物理拆分。",
        "- `DISCLOSED_NOT_INDEPENDENT` 代表該 validator 只能做 implementation consistency，不得當成獨立模型正確性證據。",
        "",
        "| 領域 | 對象 | 狀態 | ownership | 剩餘缺口 |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['domain']} | {row['subject']} | {row['status']} | "
            f"{row['ownership_mode']} | {row['remaining_gap']} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")
    try:
        rows = build_rows(generated_at)
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1
    for path in (OUTPUT_CSV, DOCS_CSV):
        _write_csv(path, rows)
    for path in (OUTPUT_MD, DOCS_MD):
        _write_md(path, rows, generated_at)
    print(f"model_data_independence_audit_rows={len(rows)}")
    print(f"model_data_independence_audit_csv={OUTPUT_CSV.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
