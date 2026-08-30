from __future__ import annotations

import csv
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_candidate_model_layer import build_parameter_table, build_specs  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]

OUT_CSV = ROOT / "output" / "latest" / "model_contract_parity_latest.csv"
OUT_MD = ROOT / "output" / "latest" / "model_contract_parity_latest.md"
RESEARCH_PARITY_CSV = ROOT / "output" / "latest" / "research_backtest" / "daily_model_research_parity_latest.csv"
RESEARCH_METRICS_CSV = ROOT / "output" / "latest" / "daily_model_parameter_research_latest.csv"

CONTRACT_REGISTRY_CSV = ROOT / "config" / "stock_model_contract_registry.csv"
CONDITION_SPEC_CSV = ROOT / "config" / "daily_model_condition_spec.csv"

# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
REVENUE_MODEL_ID = "revenue_unreacted_range"
REVENUE_EVIDENCE_VERSION = (
    "revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830"
)
REVENUE_EVIDENCE_PATH = (
    "config/approved_operation_evidence/"
    f"{REVENUE_EVIDENCE_VERSION}_manifest.csv"
)
REVENUE_EVIDENCE_STATUS = "provisional_backtest_supported_oos_unconfirmed"
REVENUE_EVIDENCE_PERMISSION_STATUS = "evidence_only_no_permission_grant"
REVENUE_RULE_SPEC_ID = "revenue_unreacted_range_source_mid_falling_d30_v1"
REVENUE_RULE_CANONICAL_SHA256 = (
    "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633"
)
REVENUE_OUTCOME_BASIS = "D2_open_after_close_confirmed_continuation_to_D30_close"
REVENUE_PRE_PROMOTION_BLOCKER = (
    "exact_frozen_evidence_ready_but_daily_model_condition_spec_and_"
    "production_permissions_not_promoted"
)
REVENUE_PRE_PROMOTION_COMPLETION_RULE = (
    "exact_frozen_rule_evidence_ready_contract_promotion_pending_no_permission_grant"
)
REVENUE_PRE_PROMOTION_ACTION = (
    "exact_frozen_evidence_ready_do_not_promote_until_model_contract_sync"
)
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

ALLOWED_PARITY_STATUSES = {
    "ok",
    "warning_research_variant_only",
    "missing_research_baseline",
    "hard_fail_contract_drift",
}

SUPPORTED_RESEARCH_BASELINE_STATUSES = {
    "production_parity",
    "production_proxy",
    "proxy_only",
}

CONTRACT_REQUIRED_COLUMNS = {
    "model_id",
    "contract_version",
    "owner_lane",
    "condition_function",
    "score_function",
    "score_profile_id",
    "pdf_visibility",
    "approved_for_daily_pdf",
    "research_baseline_required",
}

CONDITION_SPEC_REQUIRED_COLUMNS = {
    "model_id",
    "condition_function",
    "score_function",
    "score_profile_id",
}

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
    "research_evidence_path",
    "research_evidence_status",
    "research_permission_status",
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
        return str(path)


def load_csv_rows(path: Path) -> tuple[list[dict[str, str]], list[str], list[str]]:
    if not path.exists():
        return [], [], [f"missing CSV: {display_path(path)}"]
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = list(reader.fieldnames or [])
        rows = [{key: str(value or "").strip() for key, value in row.items()} for row in reader]
    if not fieldnames:
        return rows, fieldnames, [f"empty CSV header: {display_path(path)}"]
    return rows, fieldnames, []


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


def production_core_rows() -> tuple[dict[str, dict[str, str]], list[str]]:
    errors: list[str] = []
    try:
        table = build_parameter_table(build_specs()).copy()
    except Exception as exc:
        return {}, [f"cannot load production model layer: {exc}"]
    if "model_id" not in table.columns or "pdf_visibility" not in table.columns:
        return {}, ["production model layer missing model_id/pdf_visibility columns"]
    core = table[table["pdf_visibility"].astype(str).eq("pdf_core_model")].copy()
    rows: dict[str, dict[str, str]] = {}
    for _, raw_row in core.iterrows():
        row = {str(key): str(value or "").strip() for key, value in raw_row.to_dict().items()}
        model_id = row.get("model_id", "")
        if not model_id:
            errors.append("production model layer has pdf_core_model row with empty model_id")
            continue
        if model_id in rows:
            errors.append(f"production model layer has duplicate pdf_core_model model_id: {model_id}")
        rows[model_id] = row
    return rows, errors


def load_contract_sources() -> tuple[
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
    list[str],
]:
    source_errors: list[str] = []
    registry_rows, registry_fields, registry_errors = load_csv_rows(CONTRACT_REGISTRY_CSV)
    source_errors.extend(registry_errors)
    missing_registry_cols = sorted(CONTRACT_REQUIRED_COLUMNS - set(registry_fields))
    if missing_registry_cols:
        source_errors.append(f"stock model contract registry missing columns: {missing_registry_cols}")

    condition_rows, condition_fields, condition_errors = load_csv_rows(CONDITION_SPEC_CSV)
    source_errors.extend(condition_errors)
    missing_condition_cols = sorted(CONDITION_SPEC_REQUIRED_COLUMNS - set(condition_fields))
    if missing_condition_cols:
        source_errors.append(f"daily model condition spec missing columns: {missing_condition_cols}")

    production_rows, production_errors = production_core_rows()
    source_errors.extend(production_errors)

    return (
        row_map(registry_rows, "model_id"),
        row_map(condition_rows, "model_id"),
        production_rows,
        source_errors,
    )


def load_research_parity() -> dict[str, dict[str, str]]:
    rows, _, _ = load_csv_rows(RESEARCH_PARITY_CSV)
    return row_map(rows, "model_id")


def load_research_metric_rows() -> dict[str, list[dict[str, str]]]:
    rows, _, _ = load_csv_rows(RESEARCH_METRICS_CSV)
    by_model: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        if row.get("parameter_role", "").strip() != "production_baseline":
            continue
        model_id = row.get("model_id", "").strip()
        if model_id:
            by_model.setdefault(model_id, []).append(row)
    return by_model


def is_active_contract_row(row: dict[str, str]) -> bool:
    visibility = row.get("pdf_visibility", "").strip()
    deprecated_after = row.get("deprecated_after", "").strip().lower()
    if visibility == "deprecated_not_pdf_core":
        return False
    if deprecated_after and deprecated_after != "none":
        return False
    return True


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


def contract_drift_blockers(
    model_id: str,
    registry_row: dict[str, str] | None,
    condition_row: dict[str, str] | None,
    production_row: dict[str, str] | None,
) -> list[str]:
    blockers: list[str] = []
    if registry_row is None:
        return ["production core model is not present in config/stock_model_contract_registry.csv"]
    if condition_row is None:
        blockers.append("contract model is missing from config/daily_model_condition_spec.csv")
    if production_row is None:
        blockers.append("contract model is missing from current production pdf_core_model table")

    if registry_row.get("owner_lane", "").strip() != "daily_model_maintenance":
        blockers.append("stock model contract owner_lane must be daily_model_maintenance")
    if registry_row.get("pdf_visibility", "").strip() != "pdf_core_model":
        blockers.append("stock model contract pdf_visibility must remain pdf_core_model for research parity")
    if registry_row.get("approved_for_daily_pdf", "").strip() != "true":
        blockers.append("production core model must keep approved_for_daily_pdf=true")
    if registry_row.get("research_baseline_required", "").strip() != "true":
        blockers.append("production core model must keep research_baseline_required=true")

    if condition_row is not None:
        for col in ["condition_function", "score_function", "score_profile_id"]:
            expected = condition_row.get(col, "").strip()
            observed = registry_row.get(col, "").strip()
            if observed != expected:
                blockers.append(f"{col} drift: registry={observed!r} condition_spec={expected!r}")

    if production_row is not None:
        observed_visibility = production_row.get("pdf_visibility", "").strip()
        if observed_visibility != registry_row.get("pdf_visibility", "").strip():
            blockers.append(
                "pdf_visibility drift: "
                f"registry={registry_row.get('pdf_visibility', '').strip()!r} "
                f"production={observed_visibility!r}"
            )
        production_score_profile = production_row.get("score_profile_id", "").strip()
        registry_score_profile = registry_row.get("score_profile_id", "").strip()
        if production_score_profile and production_score_profile.lower() != "nan":
            if production_score_profile != registry_score_profile:
                blockers.append(
                    "score_profile_id drift: "
                    f"registry={registry_score_profile!r} production={production_score_profile!r}"
                )

    return blockers


def classify_row(
    model_id: str,
    registry_row: dict[str, str] | None,
    condition_row: dict[str, str] | None,
    production_row: dict[str, str] | None,
    research_row: dict[str, str] | None,
    metric_rows: list[dict[str, str]],
) -> dict[str, str]:
    contract_blockers = contract_drift_blockers(model_id, registry_row, condition_row, production_row)
    fingerprint_match = not contract_blockers
    production_version = (registry_row or {}).get("contract_version", "").strip()

    baseline_ids = split_ids((research_row or {}).get("research_baseline_parameter_set_id", ""))
    research_status = (research_row or {}).get("research_baseline_status", "").strip()
    baseline_exists = bool(baseline_ids)
    baseline_blocker = (research_row or {}).get("parity_blocker", "").strip()
    evidence_path = (research_row or {}).get(
        "research_baseline_evidence_path", ""
    ).strip()
    evidence_status = (research_row or {}).get(
        "research_baseline_evidence_status", ""
    ).strip()
    permission_status = (research_row or {}).get(
        "research_baseline_permission_status", ""
    ).strip()

    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    revenue_binding_blockers: list[str] = []
    if model_id == REVENUE_MODEL_ID:
        expected_binding = {
            "research_baseline_status": "proxy_only",
            "research_baseline_parameter_set_id": REVENUE_EVIDENCE_VERSION,
            "parity_blocker": REVENUE_PRE_PROMOTION_BLOCKER,
            "completion_rule": REVENUE_PRE_PROMOTION_COMPLETION_RULE,
            "research_baseline_evidence_path": REVENUE_EVIDENCE_PATH,
            "research_baseline_evidence_status": REVENUE_EVIDENCE_STATUS,
            "research_baseline_rule_spec_id": REVENUE_RULE_SPEC_ID,
            "research_baseline_rule_canonical_sha256": (
                REVENUE_RULE_CANONICAL_SHA256
            ),
            "research_baseline_outcome_basis": REVENUE_OUTCOME_BASIS,
            "research_baseline_permission_status": (
                REVENUE_EVIDENCE_PERMISSION_STATUS
            ),
            "research_baseline_forward_holdout_policy": (
                "post_launch_monitoring_non_hard_no_tuning"
            ),
            "research_baseline_financial_statement_scope": (
                "monthly_revenue_only;EPS_gross_margin_operating_margin_"
                "operating_income_non_operating_income_net_income_excluded"
            ),
        }
        for field, expected in expected_binding.items():
            observed = (research_row or {}).get(field, "").strip()
            if observed != expected:
                revenue_binding_blockers.append(
                    f"{field}={observed!r} expected={expected!r}"
                )
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

    if not fingerprint_match:
        parity_status = "hard_fail_contract_drift"
        recommended_action = "fix_production_stock_model_contract_registry_before_using_research_results"
        approved_research_variant = False
        promotion_required = False
        blockers = contract_blockers
        research_version = ",".join(baseline_ids)
    elif not baseline_exists or research_status not in SUPPORTED_RESEARCH_BASELINE_STATUSES:
        parity_status = "missing_research_baseline"
        recommended_action = "add_research_production_baseline_before_parameter_experiments"
        approved_research_variant = False
        promotion_required = False
        blockers = ["research production_baseline row is missing or unsupported"]
        if baseline_blocker:
            blockers.append(baseline_blocker)
        research_version = ""
    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    elif revenue_binding_blockers:
        parity_status = "missing_research_baseline"
        recommended_action = "repair_frozen_revenue_exact_evidence_binding"
        approved_research_variant = False
        promotion_required = False
        blockers = [
            "revenue frozen exact-evidence binding mismatch: "
            + "; ".join(revenue_binding_blockers)
        ]
        research_version = ""
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    elif research_status == "production_parity":
        parity_status = "ok"
        # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
        if model_id == REVENUE_MODEL_ID:
            recommended_action = (
                "monitor_frozen_rule_post_launch_without_tuning_or_reselection"
            )
        else:
            recommended_action = "keep_research_advisory_monitoring"
        # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
        approved_research_variant = False
        promotion_required = False
        blockers = []
        # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
        research_version = (
            REVENUE_EVIDENCE_VERSION
            if model_id == REVENUE_MODEL_ID
            else production_version
        )
        # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    else:
        parity_status = "warning_research_variant_only"
        # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
        recommended_action = (
            REVENUE_PRE_PROMOTION_ACTION
            if model_id == REVENUE_MODEL_ID
            else "research_variant_only_do_not_promote_without_explicit_promotion_pr"
        )
        # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
        approved_research_variant = True
        promotion_required = True
        blockers = [baseline_blocker or f"research baseline status is {research_status}, not production_parity"]
        research_version = ",".join(f"research:{baseline_id}" for baseline_id in baseline_ids)

    return {
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
        "research_evidence_path": evidence_path,
        "research_evidence_status": evidence_status,
        "research_permission_status": permission_status,
        "recommended_action": recommended_action,
    }


def build_parity_rows() -> tuple[list[dict[str, str]], dict[str, str], list[str]]:
    registry_by_model, condition_by_model, production_by_model, source_errors = load_contract_sources()
    research_by_model = load_research_parity()
    metric_by_model = load_research_metric_rows()

    active_registry_models = {
        model_id
        for model_id, row in registry_by_model.items()
        if is_active_contract_row(row)
    }
    model_ids = sorted(active_registry_models | set(condition_by_model) | set(production_by_model))
    rows = [
        classify_row(
            model_id=model_id,
            registry_row=registry_by_model.get(model_id),
            condition_row=condition_by_model.get(model_id),
            production_row=production_by_model.get(model_id),
            research_row=research_by_model.get(model_id),
            metric_rows=metric_by_model.get(model_id, []),
        )
        for model_id in model_ids
    ]
    metadata = {
        "generated_at": now_text(),
        "production_contract_source": display_path(CONTRACT_REGISTRY_CSV),
        "production_condition_spec": display_path(CONDITION_SPEC_CSV),
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
        f"- production_contract_source: `{metadata.get('production_contract_source', '')}`",
        f"- production_condition_spec: `{metadata.get('production_condition_spec', '')}`",
        f"- research_parity: `{metadata.get('research_parity', '')}`",
        f"- research_metrics: `{metadata.get('research_metrics', '')}`",
        "- scope: research/backtest advisory-only; this artifact is not a daily production baseline.",
        "- rule: config/stock_model_contract_registry.csv is the production stock-model source of truth for this validator.",
        "- rule: production contract drift and missing research baselines fail validation.",
        "- rule: research proxy rows are marked as research variants and require explicit promotion PR before daily production use.",
        "- revenue pre-promotion rule: exact frozen evidence may be bound while parity remains proxy_only/warning and all production permissions remain false.",
        "- rule: this validator does not read or create stock_model_contract_snapshot_latest.json.",
        "",
        "## Status Summary",
        "",
        markdown_table(summary_rows, ["parity_status", "count"]),
        "",
        "## OK Models",
        "",
        markdown_table(
            ok_rows,
            [
                "model_id",
                "production_contract_version",
                "research_contract_version",
                "d5_metric_available",
                "d10_metric_available",
                "d20_metric_available",
                "research_evidence_path",
                "research_evidence_status",
                "research_permission_status",
            ],
        ),
        "",
        "## Research Variant / Proxy Only",
        "",
        markdown_table(
            warning_rows,
            [
                "model_id",
                "research_contract_version",
                "promotion_required",
                "parity_blocker",
                "research_evidence_path",
                "research_evidence_status",
                "research_permission_status",
                "recommended_action",
            ],
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
        # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
        if row["model_id"] == REVENUE_MODEL_ID:
            expected = {
                "parity_status": "warning_research_variant_only",
                "research_contract_version": f"research:{REVENUE_EVIDENCE_VERSION}",
                "research_evidence_path": REVENUE_EVIDENCE_PATH,
                "research_evidence_status": REVENUE_EVIDENCE_STATUS,
                "research_permission_status": REVENUE_EVIDENCE_PERMISSION_STATUS,
                "approved_research_variant": "True",
                "promotion_required": "True",
                "parity_blocker": REVENUE_PRE_PROMOTION_BLOCKER,
                "recommended_action": REVENUE_PRE_PROMOTION_ACTION,
            }
            for field, expected_value in expected.items():
                if row[field] != expected_value:
                    errors.append(
                        "revenue contract parity drift: "
                        f"{field}={row[field]!r} expected={expected_value!r}"
                    )
        # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

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
    print(f"contract_source={display_path(CONTRACT_REGISTRY_CSV)}")
    print(f"validated_output={display_path(OUT_CSV)}")
    for status in sorted(ALLOWED_PARITY_STATUSES):
        print(f"{status}={counts.get(status, 0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
