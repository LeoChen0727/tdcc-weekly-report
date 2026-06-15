from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_candidate_model_layer import build_parameter_table, build_specs  # noqa: E402
from build_daily_model_parameter_research import OUT_PARITY_CSV, rule_specs  # noqa: E402


ALLOWED_BASELINE_STATUSES = {
    "production_parity",
    "production_proxy",
    "proxy_only",
}


def production_core_model_ids() -> set[str]:
    table = build_parameter_table(build_specs())
    return set(table[table["pdf_visibility"].eq("pdf_core_model")]["model_id"].astype(str))


def validate_rule_specs() -> list[str]:
    errors: list[str] = []
    production_core = production_core_model_ids()
    specs = rule_specs()
    baseline_specs = [spec for spec in specs if spec.parameter_role == "production_baseline"]
    baseline_ids = {spec.model_id for spec in baseline_specs}

    missing = sorted(production_core - baseline_ids)
    if missing:
        errors.append(f"missing production_baseline RuleSpec rows for production core models: {missing}")

    extra = sorted(baseline_ids - production_core)
    if extra:
        errors.append(f"production_baseline RuleSpec rows are not production core models: {extra}")

    for spec in baseline_specs:
        if spec.production_parity_status not in ALLOWED_BASELINE_STATUSES:
            errors.append(
                f"{spec.model_id}/{spec.parameter_set_id} has invalid production_parity_status="
                f"{spec.production_parity_status!r}"
            )
        if spec.production_parity_status in {"production_proxy", "proxy_only"} and not spec.parity_blocker.strip():
            errors.append(f"{spec.model_id}/{spec.parameter_set_id} proxy baseline must state parity_blocker")
        if not spec.variant_of:
            errors.append(f"{spec.model_id}/{spec.parameter_set_id} production baseline must set variant_of")

    for spec in specs:
        if spec.pdf_visibility == "pdf_core_model" and spec.model_id not in production_core:
            errors.append(f"research pdf_core_model is not a production core model: {spec.model_id}")

    return errors


def validate_output_file() -> list[str]:
    errors: list[str] = []
    if not OUT_PARITY_CSV.exists():
        return [f"missing parity output: {OUT_PARITY_CSV}"]
    df = pd.read_csv(OUT_PARITY_CSV, dtype=str).fillna("")
    required_cols = {
        "model_id",
        "research_baseline_status",
        "research_baseline_parameter_set_id",
        "research_variant_count",
        "parity_blocker",
        "completion_rule",
    }
    missing_cols = sorted(required_cols - set(df.columns))
    if missing_cols:
        errors.append(f"parity output missing columns: {missing_cols}")
        return errors

    production_core = production_core_model_ids()
    output_ids = set(df["model_id"].astype(str))
    missing = sorted(production_core - output_ids)
    if missing:
        errors.append(f"parity output missing production core models: {missing}")

    missing_baseline = sorted(df.loc[df["research_baseline_parameter_set_id"].eq(""), "model_id"].astype(str))
    if missing_baseline:
        errors.append(f"parity output rows have empty baseline id: {missing_baseline}")

    bad_status = sorted(set(df["research_baseline_status"].astype(str)) - ALLOWED_BASELINE_STATUSES)
    if bad_status:
        errors.append(f"parity output has unsupported statuses: {bad_status}")

    unresolved_proxy = df[
        df["research_baseline_status"].isin(["production_proxy", "proxy_only"])
        & df["parity_blocker"].eq("")
    ]
    if not unresolved_proxy.empty:
        errors.append(
            "proxy parity rows must state blockers: "
            + ", ".join(unresolved_proxy["model_id"].astype(str).tolist())
        )

    return errors


def main() -> int:
    errors = validate_rule_specs() + validate_output_file()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("daily model research parity validation passed")
    print(f"validated_output={OUT_PARITY_CSV}")
    print(f"production_core_models={sorted(production_core_model_ids())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
