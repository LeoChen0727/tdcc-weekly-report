from __future__ import annotations

import csv
import json
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent.parent
DAILY_PRODUCTION_ROOT = PROJECT_ROOT / "production" / "tdcc-daily-production"

OUT_CSV = ROOT / "output" / "latest" / "model_contract_parity_latest.csv"
OUT_MD = ROOT / "output" / "latest" / "model_contract_parity_latest.md"
RESEARCH_PARITY_CSV = ROOT / "output" / "latest" / "research_backtest" / "daily_model_research_parity_latest.csv"
RESEARCH_METRICS_CSV = ROOT / "output" / "latest" / "daily_model_parameter_research_latest.csv"

LOCAL_CONTRACT_REGISTRY = ROOT / "config" / "stock_model_contract_registry.csv"
LOCAL_CONTRACT_SNAPSHOT_JSON = ROOT / "output" / "latest" / "stock_model_contract_snapshot_latest.json"
DAILY_CONTRACT_REGISTRY = DAILY_PRODUCTION_ROOT / "config" / "stock_model_contract_registry.csv"
DAILY_CONTRACT_SNAPSHOT_JSON = DAILY_PRODUCTION_ROOT / "output" / "latest" / "stock_model_contract_snapshot_latest.json"

ALLOWED_PARITY_STATUSES = {
    "ok",
    "warning_research_variant_only",
    "missing_research_baseline",
    "hard_fail_contract_drift",
}
RESEARCH_PROXY_STATUSES = {"production_proxy", "proxy_only"}
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")

OUTPUT_COLUMNS = [
    "model_id",
    "production_contract_version",
    "research_contract_version",
    "parity_status",
    "fingerprint_match",
    "research_baseline_exists",
    "approved_research_variant",
    "promotion_required",
    "parity_blocker",
    "d5_metric_available",
    "d10_metric_available",
    "d20_metric_available",
    "recommended_action",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def bool_text(value: bool) -> str:
    return "True" if value else "False"


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        try:
            return path.relative_to(PROJECT_ROOT).as_posix()
        except ValueError:
            return str(path)


def resolve_required_path(env_name: str, local_path: Path, daily_path: Path) -> Path:
    candidates: list[Path] = []
    env_value = os.environ.get(env_name, "").strip()
    if env_value:
        candidates.append(Path(env_value))
    candidates.extend([local_path, daily_path])
    for candidate in candidates:
        if candidate.exists():
            return candidate
    searched = ", ".join(display_path(path) for path in candidates)
    raise FileNotFoundError(f"missing required contract source {env_name}; searched: {searched}")


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))


def row_map(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    mapped: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row.get(key, "").strip()
        if value:
            mapped[value] = row
    return mapped


def as_int(value: str) -> int:
    text = str(value or "").strip().replace(",", "")
    if not text:
        return 0
    try:
        return int(float(text))
    except ValueError:
        return 0


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(",") if part.strip()]


def load_contract_sources() -> tuple[Path, Path, list[dict[str, str]], dict[str, dict[str, str]], list[str]]:
    registry_path = resolve_required_path(
        "STOCK_MODEL_CONTRACT_REGISTRY",
        LOCAL_CONTRACT_REGISTRY,
        DAILY_CONTRACT_REGISTRY,
    )
    snapshot_path = resolve_required_path(
        "STOCK_MODEL_CONTRACT_SNAPSHOT_JSON",
        LOCAL_CONTRACT_SNAPSHOT_JSON,
        DAILY_CONTRACT_SNAPSHOT_JSON,
    )

    errors: list[str] = []
    registry_rows = load_csv_rows(registry_path)
    if not registry_rows:
        errors.append(f"empty production contract registry: {display_path(registry_path)}")

    snapshot_data = load_json(snapshot_path)
    snapshot_models_raw = snapshot_data.get("models", [])
    if not isinstance(snapshot_models_raw, list):
        errors.append(f"production contract snapshot JSON has no models list: {display_path(snapshot_path)}")
        snapshot_models_raw = []
    snapshot_models = [
        {key: str(value or "") for key, value in row.items()}
        for row in snapshot_models_raw
        if isinstance(row, dict)
    ]
    snapshot_by_model = row_map(snapshot_models, "model_id")

    return registry_path, snapshot_path, registry_rows, snapshot_by_model, errors


def contract_fingerprint_blockers(
    model_id: str,
    registry_row: dict[str, str] | None,
    snapshot_row: dict[str, str] | None,
) -> list[str]:
    blockers: list[str] = []
    if registry_row is None:
        return ["snapshot model is not present in production contract registry"]
    if snapshot_row is None:
        return ["production contract snapshot is missing this model"]

    comparisons = [
        ("contract_version", "contract_version"),
        ("input_columns", "required_input_columns"),
        ("output_columns", "output_columns"),
    ]
    for registry_col, snapshot_col in comparisons:
        expected = registry_row.get(registry_col, "").strip()
        observed = snapshot_row.get(snapshot_col, "").strip()
        if expected != observed:
            blockers.append(f"{registry_col} snapshot drift: registry={expected!r} snapshot={observed!r}")

    for col in ["condition_function_hash", "score_function_hash", "score_profile_hash"]:
        if not snapshot_row.get(col, "").strip():
            blockers.append(f"snapshot missing {col}")

    source_commit = snapshot_row.get("source_commit_sha", "").strip()
    if source_commit and not COMMIT_RE.match(source_commit):
        blockers.append("snapshot source_commit_sha is not a 40-character git SHA")
    if not snapshot_row.get("generated_at_utc", "").strip().endswith("Z"):
        blockers.append("snapshot generated_at_utc must be UTC Z format")
    if registry_row.get("owner_lane", "").strip() != "daily_production":
        blockers.append("production contract owner_lane must be daily_production")
    return blockers


def load_research_parity() -> dict[str, dict[str, str]]:
    if not RESEARCH_PARITY_CSV.exists():
        return {}
    return row_map(load_csv_rows(RESEARCH_PARITY_CSV), "model_id")


def load_research_metric_rows() -> dict[str, list[dict[str, str]]]:
    if not RESEARCH_METRICS_CSV.exists():
        return {}
    rows = load_csv_rows(RESEARCH_METRICS_CSV)
    by_model: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        if row.get("parameter_role", "").strip() != "production_baseline":
            continue
        model_id = row.get("model_id", "").strip()
        if model_id:
            by_model.setdefault(model_id, []).append(row)
    return by_model


def metric_available(metric_rows: list[dict[str, str]], horizon: int, baseline_ids: list[str]) -> bool:
    if not metric_rows:
        return False
    selected = [
        row for row in metric_rows
        if not baseline_ids or row.get("parameter_set_id", "").strip() in baseline_ids
    ]
    if not selected:
        selected = metric_rows
    mature_col = f"d{horizon}_mature_count"
    win_col = f"d{horizon}_close_win_rate_pct"
    avg_col = f"d{horizon}_avg_close_return_pct"
    for row in selected:
        has_sample = as_int(row.get(mature_col, "")) > 0
        has_metric = bool(row.get(win_col, "").strip() or row.get(avg_col, "").strip())
        if has_sample and has_metric:
            return True
    return False


def classify_row(
    model_id: str,
    registry_row: dict[str, str] | None,
    snapshot_row: dict[str, str] | None,
    research_row: dict[str, str] | None,
    metric_rows: list[dict[str, str]],
) -> dict[str, str]:
    contract_blockers = contract_fingerprint_blockers(model_id, registry_row, snapshot_row)
    fingerprint_match = not contract_blockers
    production_version = (registry_row or snapshot_row or {}).get("contract_version", "").strip()

    baseline_ids = split_ids((research_row or {}).get("research_baseline_parameter_set_id", ""))
    research_status = (research_row or {}).get("research_baseline_status", "").strip()
    baseline_exists = bool(baseline_ids)
    baseline_blocker = (research_row or {}).get("parity_blocker", "").strip()

    if not fingerprint_match:
        parity_status = "hard_fail_contract_drift"
        recommended_action = "fix_production_contract_snapshot_before_using_research_results"
        approved_research_variant = False
        promotion_required = False
        blockers = contract_blockers
        research_version = ",".join(baseline_ids)
    elif not baseline_exists or research_status not in {"production_parity", "production_proxy", "proxy_only"}:
        parity_status = "missing_research_baseline"
        recommended_action = "add_research_production_baseline_before_parameter_experiments"
        approved_research_variant = False
        promotion_required = False
        blockers = ["research production_baseline row is missing or unsupported"]
        if baseline_blocker:
            blockers.append(baseline_blocker)
        research_version = ""
    elif research_status == "production_parity":
        parity_status = "ok"
        recommended_action = "keep_research_advisory_monitoring"
        approved_research_variant = False
        promotion_required = False
        blockers = []
        research_version = production_version
    else:
        parity_status = "warning_research_variant_only"
        recommended_action = "research_variant_only_do_not_promote_without_explicit_promotion_pr"
        approved_research_variant = True
        promotion_required = True
        blockers = [baseline_blocker or f"research baseline status is {research_status}, not production_parity"]
        research_version = ",".join(f"research:{baseline_id}" for baseline_id in baseline_ids)

    row = {
        "model_id": model_id,
        "production_contract_version": production_version,
        "research_contract_version": research_version,
        "parity_status": parity_status,
        "fingerprint_match": bool_text(fingerprint_match),
        "research_baseline_exists": bool_text(baseline_exists),
        "approved_research_variant": bool_text(approved_research_variant),
        "promotion_required": bool_text(promotion_required),
        "parity_blocker": "; ".join(part for part in blockers if part),
        "d5_metric_available": bool_text(metric_available(metric_rows, 5, baseline_ids)),
        "d10_metric_available": bool_text(metric_available(metric_rows, 10, baseline_ids)),
        "d20_metric_available": bool_text(metric_available(metric_rows, 20, baseline_ids)),
        "recommended_action": recommended_action,
    }
    return row


def build_parity_rows() -> tuple[list[dict[str, str]], dict[str, str], list[str]]:
    registry_path, snapshot_path, registry_rows, snapshot_by_model, source_errors = load_contract_sources()
    research_by_model = load_research_parity()
    metric_by_model = load_research_metric_rows()

    registry_by_model = row_map(registry_rows, "model_id")
    model_ids = sorted(set(registry_by_model) | set(snapshot_by_model))
    rows = [
        classify_row(
            model_id=model_id,
            registry_row=registry_by_model.get(model_id),
            snapshot_row=snapshot_by_model.get(model_id),
            research_row=research_by_model.get(model_id),
            metric_rows=metric_by_model.get(model_id, []),
        )
        for model_id in model_ids
    ]
    metadata = {
        "generated_at": now_text(),
        "production_registry": display_path(registry_path),
        "production_snapshot_json": display_path(snapshot_path),
        "research_parity": display_path(RESEARCH_PARITY_CSV),
        "research_metrics": display_path(RESEARCH_METRICS_CSV),
    }
    return rows, metadata, source_errors


def write_csv(rows: list[dict[str, str]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, str]], columns: list[str]) -> str:
    if not rows:
        return "No rows."
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        values = [str(row.get(col, "")).replace("|", "/").replace("\n", " ") for col in columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def write_markdown(rows: list[dict[str, str]], metadata: dict[str, str], source_errors: list[str]) -> None:
    counts = Counter(row["parity_status"] for row in rows)
    summary_rows = [
        {"parity_status": status, "count": str(counts.get(status, 0))}
        for status in sorted(ALLOWED_PARITY_STATUSES)
    ]
    ok_rows = [row for row in rows if row["parity_status"] == "ok"]
    warning_rows = [row for row in rows if row["parity_status"] == "warning_research_variant_only"]
    missing_rows = [row for row in rows if row["parity_status"] == "missing_research_baseline"]
    hard_fail_rows = [row for row in rows if row["parity_status"] == "hard_fail_contract_drift"]

    lines = [
        "# Research Against Stock Model Contract Parity",
        "",
        f"- generated_at: `{metadata.get('generated_at', '')}`",
        f"- production_registry: `{metadata.get('production_registry', '')}`",
        f"- production_snapshot_json: `{metadata.get('production_snapshot_json', '')}`",
        f"- research_parity: `{metadata.get('research_parity', '')}`",
        f"- research_metrics: `{metadata.get('research_metrics', '')}`",
        "- scope: research/backtest advisory-only; this artifact is not a daily production baseline.",
        "- rule: production contract drift and missing research baselines fail validation.",
        "- rule: research proxy rows are marked as research variants and require explicit promotion PR before daily production use.",
        "",
        "## Status Summary",
        "",
        markdown_table(summary_rows, ["parity_status", "count"]),
        "",
        "## OK Models",
        "",
        markdown_table(
            ok_rows,
            ["model_id", "production_contract_version", "research_contract_version", "d5_metric_available", "d10_metric_available", "d20_metric_available"],
        ),
        "",
        "## Research Variant / Proxy Only",
        "",
        markdown_table(
            warning_rows,
            ["model_id", "research_contract_version", "promotion_required", "parity_blocker", "recommended_action"],
        ),
        "",
        "## Missing Research Baseline",
        "",
        markdown_table(missing_rows, ["model_id", "parity_blocker", "recommended_action"]),
        "",
        "## Hard Fail Contract Drift",
        "",
        markdown_table(hard_fail_rows, ["model_id", "fingerprint_match", "parity_blocker", "recommended_action"]),
    ]
    if source_errors:
        lines.extend(["", "## Source Errors", "", *[f"- {error}" for error in source_errors]])
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def validate_rows(rows: list[dict[str, str]], source_errors: list[str]) -> list[str]:
    errors = list(source_errors)
    if not rows:
        errors.append("model contract parity output has no rows")
        return errors
    for row in rows:
        missing_cols = [column for column in OUTPUT_COLUMNS if column not in row]
        if missing_cols:
            errors.append(f"{row.get('model_id', '<unknown>')} missing output columns: {missing_cols}")
            continue
        if row["parity_status"] not in ALLOWED_PARITY_STATUSES:
            errors.append(f"{row['model_id']} has invalid parity_status={row['parity_status']!r}")
        for col in [
            "fingerprint_match",
            "research_baseline_exists",
            "approved_research_variant",
            "promotion_required",
            "d5_metric_available",
            "d10_metric_available",
            "d20_metric_available",
        ]:
            if row[col] not in {"True", "False"}:
                errors.append(f"{row['model_id']} has non-boolean {col}: {row[col]!r}")
        if row["parity_status"] == "warning_research_variant_only":
            if row["approved_research_variant"] != "True":
                errors.append(f"{row['model_id']} research variant row must set approved_research_variant=True")
            if row["promotion_required"] != "True":
                errors.append(f"{row['model_id']} research variant row must set promotion_required=True")
            if not row["parity_blocker"].strip():
                errors.append(f"{row['model_id']} research variant row must state parity_blocker")
        if row["parity_status"] == "ok" and row["promotion_required"] != "False":
            errors.append(f"{row['model_id']} exact parity row must not require promotion")

    failing_models = [
        row["model_id"]
        for row in rows
        if row["parity_status"] in {"hard_fail_contract_drift", "missing_research_baseline"}
    ]
    if failing_models:
        errors.append(f"blocking stock model contract parity statuses: {failing_models}")
    return errors


def main() -> int:
    try:
        rows, metadata, source_errors = build_parity_rows()
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    write_csv(rows)
    write_markdown(rows, metadata, source_errors)
    errors = validate_rows(rows, source_errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"wrote_output={display_path(OUT_CSV)}")
        return 1

    counts = Counter(row["parity_status"] for row in rows)
    print("research stock model contract parity validation passed")
    print(f"validated_output={display_path(OUT_CSV)}")
    for status in sorted(ALLOWED_PARITY_STATUSES):
        print(f"{status}={counts.get(status, 0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
