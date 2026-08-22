from __future__ import annotations

import argparse
import csv
from datetime import datetime
import hashlib
import os
from pathlib import Path
import tempfile
from typing import Sequence
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
NORMALIZE_PREIMAGE_BYTES = 41_920
NORMALIZE_PREIMAGE_SHA256 = (
    "ffa88dfff82d1c20dc6fc8c51a5c330054957d8f8c4a40368b928dbf367c383a"
)
NORMALIZE_PREIMAGE_GIT_BLOB_SHA1 = "434870523b8d093d4fde319f9f040f867c5d78c6"
NORMALIZE_PREIMAGE_CRLF_COUNT = 96
NORMALIZE_POSTIMAGE_BYTES = 41_824
NORMALIZE_POSTIMAGE_SHA256 = (
    "2ff7e9c3140f0540ffb0238ba0937893b03de39bd2bcd5d84559b53a649685be"
)
NORMALIZE_POSTIMAGE_LF_COUNT = 96
UTF8_BOM = b"\xef\xbb\xbf"
NUMERICAL_ANOMALY_CONTRACT = (
    ROOT / "config" / "daily_model_numerical_anomaly_disposition_contract.csv"
)

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

    anomaly_contract_rows = _read(NUMERICAL_ANOMALY_CONTRACT)
    rows.append(
        {
            "generated_at": generated_at,
            "domain": "numerical_anomaly_governance",
            "subject": "repo_wide_root_cause_disposition_contract",
            "status": "PASS",
            "ownership_mode": "repo_wide_governance_contract",
            "consumer_count": "all_models",
            "evidence": (
                f"contract={NUMERICAL_ANOMALY_CONTRACT.relative_to(ROOT).as_posix()}; "
                f"dispositions={len(anomaly_contract_rows)}; threshold_only_final_disposition_forbidden"
            ),
            "remaining_gap": "none",
        }
    )
    for subject, ownership_mode, evidence, gap in (
        (
            "monthly_revenue_history_legacy_threshold_flag",
            "legacy_threshold_flag_candidate_only",
            "full_monthly_revenue_numerical_anomaly_flag must not auto-exclude primary model metrics",
            "source schema still uses a legacy anomaly field name and must be treated as candidate-only",
        ),
        (
            "revenue_unreacted_range",
            "model_owned_root_cause_pending",
            "primary metrics retain unresolved source/path/return candidates; exclusion views are sensitivity-only",
            "corporate-action PIT, independent-source corroboration, and adjustment-basis checks remain incomplete",
        ),
        (
            "price_pullback_23ema",
            "model_owned_root_cause_pending",
            "legacy 2380 data-quality row is downgraded to an unresolved candidate and retained in primary metrics",
            "all root-cause checks must complete before any candidate may be excluded",
        ),
        (
            "volume_range_breakout_v2_legacy_quantile_artifacts",
            "legacy_threshold_artifacts_contained",
            "quantile-labelled anomaly artifacts are barred from formal evidence pins",
            "republish under the root-cause disposition contract before reopening or promotion",
        ),
    ):
        rows.append(
            {
                "generated_at": generated_at,
                "domain": "numerical_anomaly_governance",
                "subject": subject,
                "status": "CONTAINED",
                "ownership_mode": ownership_mode,
                "consumer_count": "1",
                "evidence": evidence,
                "remaining_gap": gap,
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
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
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


def _git_blob_sha1(raw: bytes) -> str:
    header = f"blob {len(raw)}\0".encode("ascii")
    return hashlib.sha1(header + raw).hexdigest()


def _validate_normalization_preimage(raw: bytes, *, label: str) -> None:
    errors: list[str] = []
    if len(raw) != NORMALIZE_PREIMAGE_BYTES:
        errors.append(
            f"bytes={len(raw)} expected={NORMALIZE_PREIMAGE_BYTES}"
        )
    sha256 = hashlib.sha256(raw).hexdigest()
    if sha256 != NORMALIZE_PREIMAGE_SHA256:
        errors.append(
            f"sha256={sha256} expected={NORMALIZE_PREIMAGE_SHA256}"
        )
    git_blob_sha1 = _git_blob_sha1(raw)
    if git_blob_sha1 != NORMALIZE_PREIMAGE_GIT_BLOB_SHA1:
        errors.append(
            "git_blob_sha1="
            f"{git_blob_sha1} expected={NORMALIZE_PREIMAGE_GIT_BLOB_SHA1}"
        )
    if not raw.startswith(UTF8_BOM):
        errors.append("utf8_bom=missing")
    crlf_count = raw.count(b"\r\n")
    if crlf_count != NORMALIZE_PREIMAGE_CRLF_COUNT:
        errors.append(
            f"crlf_count={crlf_count} expected={NORMALIZE_PREIMAGE_CRLF_COUNT}"
        )
    without_crlf = raw.replace(b"\r\n", b"")
    if b"\n" in without_crlf:
        errors.append("bare_lf=present")
    if b"\r" in without_crlf:
        errors.append("other_cr=present")
    if errors:
        raise RuntimeError(
            f"{label}: normalization preimage contract failed: " + "; ".join(errors)
        )


def _validate_normalization_postimage(raw: bytes) -> None:
    errors: list[str] = []
    if len(raw) != NORMALIZE_POSTIMAGE_BYTES:
        errors.append(
            f"bytes={len(raw)} expected={NORMALIZE_POSTIMAGE_BYTES}"
        )
    sha256 = hashlib.sha256(raw).hexdigest()
    if sha256 != NORMALIZE_POSTIMAGE_SHA256:
        errors.append(
            f"sha256={sha256} expected={NORMALIZE_POSTIMAGE_SHA256}"
        )
    if not raw.startswith(UTF8_BOM):
        errors.append("utf8_bom=missing")
    lf_count = raw.count(b"\n")
    if lf_count != NORMALIZE_POSTIMAGE_LF_COUNT:
        errors.append(
            f"lf_count={lf_count} expected={NORMALIZE_POSTIMAGE_LF_COUNT}"
        )
    if b"\r" in raw:
        errors.append("cr=present")
    if errors:
        raise RuntimeError(
            "normalization postimage contract failed: " + "; ".join(errors)
        )


def _prepare_atomic_replacement(path: Path, raw: bytes) -> Path:
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=path.parent,
            prefix=f".{path.name}.normalize-",
            suffix=".tmp",
            delete=False,
        ) as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
            temporary_path = Path(handle.name)
    except OSError as exc:
        raise RuntimeError(f"{path}: unable to prepare atomic replacement: {exc}") from exc
    if temporary_path.read_bytes() != raw:
        temporary_path.unlink(missing_ok=True)
        raise RuntimeError(f"{path}: prepared atomic replacement bytes drifted")
    return temporary_path


def _normalize_existing_csv_line_endings_only() -> None:
    paths = (OUTPUT_CSV, DOCS_CSV)
    raw_by_path: dict[Path, bytes] = {}
    for path in paths:
        try:
            raw_by_path[path] = path.read_bytes()
        except OSError as exc:
            raise RuntimeError(f"{path}: unable to read normalization preimage: {exc}") from exc

    output_raw = raw_by_path[OUTPUT_CSV]
    docs_raw = raw_by_path[DOCS_CSV]
    if output_raw != docs_raw:
        raise RuntimeError(
            "model data independence CSV normalization preimages are not byte-identical"
        )
    for path in paths:
        _validate_normalization_preimage(
            raw_by_path[path], label=path.relative_to(ROOT).as_posix()
        )

    normalized = output_raw.replace(b"\r\n", b"\n")
    _validate_normalization_postimage(normalized)

    replacements: dict[Path, Path] = {}
    rollbacks: dict[Path, Path] = {}
    installed: list[Path] = []
    try:
        for path in paths:
            replacements[path] = _prepare_atomic_replacement(path, normalized)
            rollbacks[path] = _prepare_atomic_replacement(path, raw_by_path[path])
        for path in paths:
            if path.read_bytes() != raw_by_path[path]:
                raise RuntimeError(
                    f"{path}: normalization preimage changed before atomic replacement"
                )
        for path in paths:
            try:
                os.replace(replacements[path], path)
            except OSError as exc:
                raise RuntimeError(
                    f"{path}: unable to install atomic replacement: {exc}"
                ) from exc
            installed.append(path)

        for path in paths:
            written = path.read_bytes()
            if written != normalized:
                raise RuntimeError(
                    f"{path}: normalized bytes do not match the approved postimage"
                )
            _validate_normalization_postimage(written)
    except Exception as exc:
        rollback_errors: list[str] = []
        for path in reversed(installed):
            try:
                os.replace(rollbacks[path], path)
            except OSError as rollback_exc:
                rollback_errors.append(f"{path}: {rollback_exc}")
        if rollback_errors:
            raise RuntimeError(
                "normalization failed and rollback could not restore the approved "
                f"preimage: {'; '.join(rollback_errors)}"
            ) from exc
        raise
    finally:
        for temporary_path in (*replacements.values(), *rollbacks.values()):
            temporary_path.unlink(missing_ok=True)


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--normalize-existing-csv-line-endings-only",
        action="store_true",
        help=(
            "Normalize the two fixed model-data-independence CSV mirrors from the "
            "approved CRLF preimage to the approved LF postimage without rebuilding."
        ),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    if args.normalize_existing_csv_line_endings_only:
        try:
            _normalize_existing_csv_line_endings_only()
        except RuntimeError as exc:
            print(f"ERROR: {exc}")
            return 1
        print("model_data_independence_audit_csv_line_endings_normalized=true")
        print(f"model_data_independence_audit_csv_bytes={NORMALIZE_POSTIMAGE_BYTES}")
        print(
            "model_data_independence_audit_csv_sha256="
            f"{NORMALIZE_POSTIMAGE_SHA256}"
        )
        return 0

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
