from __future__ import annotations

import argparse
import csv
import io
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_model_operation_readiness as readiness_builder  # noqa: E402


MODEL_ID = "revenue_unreacted_range"

OUT_CSV_REL = "output/latest/model_operation_readiness_latest.csv"
OUT_MD_REL = "output/latest/model_operation_readiness_latest.md"
DOCS_CSV_REL = "docs/latest/model_operation_readiness_latest.csv"
DOCS_MD_REL = "docs/latest/model_operation_readiness_latest.md"
READINESS_MIRROR_RELS = (
    OUT_CSV_REL,
    OUT_MD_REL,
    DOCS_CSV_REL,
    DOCS_MD_REL,
)

PROMOTION_REGISTRY_REL = (
    "config/revenue_unreacted_range_promotion_preparation_registry.csv"
)
ANOMALY_REGISTRY_REL = (
    "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv"
)
FORWARD_HOLDOUT_V2_MANIFEST_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_manifest_latest.csv"
)
CANONICAL_SOURCE_RELS = (
    PROMOTION_REGISTRY_REL,
    ANOMALY_REGISTRY_REL,
    FORWARD_HOLDOUT_V2_MANIFEST_REL,
)

LEGACY_COLUMNS = (
    "generated_at",
    "model_id",
    "model_name_zh",
    "parity_status",
    "blocker",
    "operation_module_status",
    "daily_adapter_status",
    "approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "presentation_allowed",
    "operation_directive_level",
    "pdf_integration_status",
    "packet_integration_status",
    "registry_pattern_count",
    "registry_current_model_pattern_count",
    "registry_best_pattern_id",
    "registry_best_sample_size",
    "registry_best_win_rate",
    "registry_best_median_return",
    "daily_adapter_row_count",
    "daily_adapter_data_row_count",
    "daily_adapter_sections",
    "status_note_zh",
)
TARGET_COLUMNS = (
    *LEGACY_COLUMNS[:7],
    "formal_model_use_allowed",
    *LEGACY_COLUMNS[7:12],
    "production_allowed",
    *LEGACY_COLUMNS[12:],
)
REVENUE_PERMISSION_COLUMNS = {
    "formal_model_use_allowed",
    "production_allowed",
}
ROW_IDENTITY_COLUMNS = {"generated_at", "model_id", "model_name_zh"}
SUMMARY_COLUMNS = set(TARGET_COLUMNS) - ROW_IDENTITY_COLUMNS


def _git_blob(repo: Path, logical_path: str) -> bytes:
    result = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "show",
            f"HEAD:{logical_path}",
        ],
        cwd=repo,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise RuntimeError(
            f"cannot read committed source HEAD:{logical_path}: "
            + result.stderr.decode("utf-8", errors="replace").strip()
        )
    return result.stdout


def _parse_csv_bytes(data: bytes, source_name: str) -> tuple[list[str], list[dict[str, str]]]:
    try:
        text = data.decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(text))
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise ValueError("missing CSV header")
        if any(not field.strip() for field in fieldnames):
            raise ValueError("blank CSV header")
        if len(fieldnames) != len(set(fieldnames)):
            raise ValueError("duplicate CSV header")
        rows = list(reader)
        if any(None in row for row in rows):
            raise ValueError("CSV row has more values than the header")
    except (UnicodeDecodeError, csv.Error, ValueError) as exc:
        raise RuntimeError(f"malformed committed CSV source {source_name}: {exc}") from exc
    return fieldnames, rows


def _canonical_csv(data: bytes, source_name: str) -> bytes:
    fieldnames, rows = _parse_csv_bytes(data, source_name)
    return json.dumps(
        {"fieldnames": fieldnames, "rows": rows},
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")


def _canonical_markdown(data: bytes, source_name: str) -> bytes:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"malformed committed Markdown source {source_name}: {exc}") from exc
    normalized = text.replace("\r\n", "\n")
    if "\r" in normalized:
        raise RuntimeError(
            f"malformed committed Markdown source {source_name}: bare carriage return"
        )
    return normalized.encode("utf-8")


def _committed_semantic_source(
    repo: Path,
    logical_path: str,
    *,
    csv_source: bool,
) -> tuple[bytes, str | None]:
    path = repo / logical_path
    try:
        worktree_data = path.read_bytes()
    except OSError as exc:
        raise RuntimeError(f"missing readiness sync source {logical_path}: {exc}") from exc
    committed_data = _git_blob(repo, logical_path)
    canonical = _canonical_csv if csv_source else _canonical_markdown
    if canonical(worktree_data, logical_path) != canonical(
        committed_data,
        f"HEAD:{logical_path}",
    ):
        raise RuntimeError(
            f"readiness sync source has semantic drift from HEAD: {logical_path}"
        )
    diagnostic = None
    if worktree_data != committed_data:
        diagnostic = (
            f"raw-byte diagnostic only (canonical semantics match HEAD): {logical_path}"
        )
    return committed_data, diagnostic


def _frame_from_csv_bytes(data: bytes, source_name: str) -> pd.DataFrame:
    fieldnames, rows = _parse_csv_bytes(data, source_name)
    return pd.DataFrame(rows, columns=fieldnames).fillna("")


def load_committed_inputs(
    repo: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, list[str]]:
    committed: dict[str, bytes] = {}
    diagnostics: list[str] = []
    for logical_path in READINESS_MIRROR_RELS:
        data, diagnostic = _committed_semantic_source(
            repo,
            logical_path,
            csv_source=logical_path.endswith(".csv"),
        )
        committed[logical_path] = data
        if diagnostic:
            diagnostics.append(diagnostic)
    for logical_path in CANONICAL_SOURCE_RELS:
        data, diagnostic = _committed_semantic_source(
            repo,
            logical_path,
            csv_source=True,
        )
        committed[logical_path] = data
        if diagnostic:
            diagnostics.append(diagnostic)

    if _canonical_csv(
        committed[OUT_CSV_REL], OUT_CSV_REL
    ) != _canonical_csv(committed[DOCS_CSV_REL], DOCS_CSV_REL):
        raise RuntimeError("committed output/docs readiness CSV mirrors differ")
    if _canonical_markdown(
        committed[OUT_MD_REL], OUT_MD_REL
    ) != _canonical_markdown(committed[DOCS_MD_REL], DOCS_MD_REL):
        raise RuntimeError("committed output/docs readiness Markdown mirrors differ")

    return (
        _frame_from_csv_bytes(committed[OUT_CSV_REL], OUT_CSV_REL),
        _frame_from_csv_bytes(committed[PROMOTION_REGISTRY_REL], PROMOTION_REGISTRY_REL),
        _frame_from_csv_bytes(committed[ANOMALY_REGISTRY_REL], ANOMALY_REGISTRY_REL),
        _frame_from_csv_bytes(
            committed[FORWARD_HOLDOUT_V2_MANIFEST_REL],
            FORWARD_HOLDOUT_V2_MANIFEST_REL,
        ),
        diagnostics,
    )


def validate_base_readiness(frame: pd.DataFrame) -> None:
    columns = tuple(frame.columns)
    if columns not in {LEGACY_COLUMNS, TARGET_COLUMNS}:
        raise RuntimeError(
            "committed readiness schema drift: expected exact legacy or revenue-extended "
            f"schema, got {list(columns)}"
        )
    if frame.empty:
        raise RuntimeError("committed readiness CSV is empty")
    model_ids = frame["model_id"].astype(str)
    if model_ids.str.strip().eq("").any():
        raise RuntimeError("committed readiness contains a blank model_id")
    duplicate_ids = sorted(model_ids[model_ids.duplicated(keep=False)].unique().tolist())
    if duplicate_ids:
        raise RuntimeError(
            f"committed readiness contains duplicate model_id values: {duplicate_ids}"
        )
    if int(model_ids.eq(MODEL_ID).sum()) != 1:
        raise RuntimeError(f"committed readiness must contain exactly one {MODEL_ID} row")
    for field_name in ("approved_for_daily", "presentation_allowed"):
        invalid = sorted(set(frame[field_name].astype(str)) - {"True", "False"})
        if invalid:
            raise RuntimeError(
                f"committed readiness {field_name} has non-canonical values: {invalid}"
            )

    if columns == TARGET_COLUMNS:
        revenue_mask = model_ids.eq(MODEL_ID)
        for field_name in sorted(REVENUE_PERMISSION_COLUMNS):
            values = frame[field_name].astype(str)
            if not values[revenue_mask].eq("False").all():
                raise RuntimeError(
                    f"committed {MODEL_ID} readiness {field_name} must be explicit False"
                )
            conflicting = frame.loc[~revenue_mask & values.ne(""), "model_id"]
            if not conflicting.empty:
                raise RuntimeError(
                    f"committed readiness {field_name} is revenue-only; non-revenue "
                    f"rows must remain neutral blank: {sorted(conflicting.tolist())}"
                )


def build_revenue_only_readiness(
    base: pd.DataFrame,
    revenue_summary: dict[str, Any],
    *,
    generated_at: str,
) -> pd.DataFrame:
    validate_base_readiness(base)
    if set(revenue_summary) != SUMMARY_COLUMNS:
        missing = sorted(SUMMARY_COLUMNS - set(revenue_summary))
        extra = sorted(set(revenue_summary) - SUMMARY_COLUMNS)
        raise RuntimeError(
            f"revenue readiness summary schema drift: missing={missing}; extra={extra}"
        )

    out = base.copy()
    if tuple(out.columns) == LEGACY_COLUMNS:
        out.insert(
            out.columns.get_loc("approved_for_daily"),
            "formal_model_use_allowed",
            "",
        )
        out.insert(
            out.columns.get_loc("presentation_allowed") + 1,
            "production_allowed",
            "",
        )
    if tuple(out.columns) != TARGET_COLUMNS:
        raise RuntimeError("revenue readiness target column order is not canonical")

    revenue_mask = out["model_id"].astype(str).eq(MODEL_ID)
    revenue_index = out.index[revenue_mask][0]
    preserved_model_name = str(out.at[revenue_index, "model_name_zh"])
    replacement = {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "model_name_zh": preserved_model_name,
        **{
            field_name: "" if value is None else str(value)
            for field_name, value in revenue_summary.items()
        },
    }
    out.loc[revenue_index, list(TARGET_COLUMNS)] = [
        replacement[field_name] for field_name in TARGET_COLUMNS
    ]

    base_non_revenue = base.loc[~revenue_mask].reset_index(drop=True)
    out_non_revenue = out.loc[~revenue_mask].reset_index(drop=True)
    for field_name in LEGACY_COLUMNS:
        if not out_non_revenue[field_name].equals(base_non_revenue[field_name]):
            raise RuntimeError(
                f"revenue-only readiness sync changed non-revenue field {field_name}"
            )
    for field_name in sorted(REVENUE_PERMISSION_COLUMNS):
        if not out_non_revenue[field_name].astype(str).eq("").all():
            raise RuntimeError(
                f"revenue-only readiness sync populated non-revenue field {field_name}"
            )
    validate_base_readiness(out)
    return out


def render_markdown(readiness: pd.DataFrame, *, generated_at: str) -> bytes:
    lines: list[str] = [
        "# Model Operation Readiness",
        "",
        f"- generated_at: `{generated_at}`",
        "- purpose: track model parity, operation-module readiness, daily adapter status, and promotion boundaries",
        "- rule: `approved_for_daily=True` requires an explicit approved operation artifact",
        "- rule: raw research evidence rows can remain research-only even after an operation module is approved",
        "- rule: PDF/packet integration 必須 render adapter artifact，不得重新計算操作規則",
        "",
    ]
    summary_cols = [
        "operation_module_status",
        "daily_adapter_status",
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ]
    for field_name in summary_cols:
        counts = readiness[field_name].value_counts().reset_index()
        counts.columns = [field_name, "count"]
        lines.extend(
            [
                f"## {field_name}",
                "",
                readiness_builder.markdown_table(counts, [field_name, "count"]),
                "",
            ]
        )

    show_cols = [
        "model_id",
        "parity_status",
        "operation_module_status",
        "daily_adapter_status",
        "formal_model_use_allowed",
        "approved_for_daily",
        "approval_status",
        "operation_module_id",
        "approval_version",
        "presentation_allowed",
        "production_allowed",
        "operation_directive_level",
        "pdf_integration_status",
        "packet_integration_status",
        "blocker",
        "status_note_zh",
    ]
    lines.extend(
        [
            "## Status Table",
            "",
            readiness_builder.markdown_table(readiness, show_cols, limit=200),
            "",
        ]
    )
    return ("\n".join(lines).rstrip() + "\n").encode("utf-8")


def write_readiness_mirrors(
    repo: Path,
    readiness: pd.DataFrame,
    *,
    generated_at: str,
) -> None:
    csv_data = readiness.to_csv(index=False, lineterminator="\n").encode("utf-8")
    markdown_data = render_markdown(readiness, generated_at=generated_at)
    payloads = {
        OUT_CSV_REL: csv_data,
        DOCS_CSV_REL: csv_data,
        OUT_MD_REL: markdown_data,
        DOCS_MD_REL: markdown_data,
    }
    if set(payloads) != set(READINESS_MIRROR_RELS):
        raise RuntimeError("readiness sync output scope drifted from the exact four mirrors")
    for logical_path, data in payloads.items():
        path = repo / logical_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    if (repo / OUT_CSV_REL).read_bytes() != (repo / DOCS_CSV_REL).read_bytes():
        raise RuntimeError("written output/docs readiness CSV mirrors differ")
    if (repo / OUT_MD_REL).read_bytes() != (repo / DOCS_MD_REL).read_bytes():
        raise RuntimeError("written output/docs readiness Markdown mirrors differ")


def sync(repo: Path, *, generated_at: str | None = None) -> tuple[pd.DataFrame, list[str]]:
    repo = repo.resolve()
    (
        base,
        promotion_registry,
        anomaly_registry,
        forward_holdout_v2_manifest,
        diagnostics,
    ) = load_committed_inputs(repo)

    _, promotion_errors = readiness_builder.validate_revenue_promotion_registry(
        repo / PROMOTION_REGISTRY_REL
    )
    _, anomaly_errors = readiness_builder.validate_revenue_anomaly_registry(
        repo / ANOMALY_REGISTRY_REL,
        expected_anomalies=readiness_builder.REVENUE_EXPECTED_ANOMALIES,
        version_label="v2",
    )
    source_errors = [
        *(f"promotion source: {error}" for error in promotion_errors),
        *(f"anomaly source: {error}" for error in anomaly_errors),
    ]
    if source_errors:
        raise RuntimeError("; ".join(source_errors))

    revenue_summary = readiness_builder.summarize_revenue_promotion_readiness(
        promotion_registry,
        anomaly_registry,
        forward_holdout_v2_manifest,
    )
    generated = generated_at or readiness_builder.now_text()
    readiness = build_revenue_only_readiness(
        base,
        revenue_summary,
        generated_at=generated,
    )
    write_readiness_mirrors(repo, readiness, generated_at=generated)
    return readiness, diagnostics


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        readiness, diagnostics = sync(args.repo_root)
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1
    for diagnostic in diagnostics:
        print(f"DIAGNOSTIC: {diagnostic}")
    print(
        "Saved exact four revenue-only readiness mirrors; "
        f"rows={len(readiness)}; model_id={MODEL_ID}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
