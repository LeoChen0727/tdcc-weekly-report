from __future__ import annotations

import argparse
import csv

try:
    from build_model_data_independence_audit import (
        DOCS_CSV,
        DOCS_MD,
        OUTPUT_COLUMNS,
        OUTPUT_CSV,
        OUTPUT_MD,
        build_rows,
    )
    from model_data_independence import comprehensive_validation
except ModuleNotFoundError:  # Loaded as scripts.validate_model_data_independence.
    from scripts.build_model_data_independence_audit import (
        DOCS_CSV,
        DOCS_MD,
        OUTPUT_COLUMNS,
        OUTPUT_CSV,
        OUTPUT_MD,
        build_rows,
    )
    from scripts.model_data_independence import comprehensive_validation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default=None)
    return parser.parse_args()


def validate(*, base_ref: str | None = None) -> list[str]:
    errors, _ = comprehensive_validation(base_ref=base_ref)
    if errors:
        return errors
    errors.extend(validate_audit_artifact())
    return errors


def validate_audit_artifact() -> list[str]:
    errors: list[str] = []
    for path in (OUTPUT_CSV, OUTPUT_MD, DOCS_CSV, DOCS_MD):
        if not path.is_file():
            errors.append(f"missing model/data independence audit artifact: {path.as_posix()}")
    if errors:
        return errors
    if OUTPUT_CSV.read_bytes() != DOCS_CSV.read_bytes():
        errors.append("docs/latest model/data independence CSV must exactly mirror output/latest")
    if OUTPUT_MD.read_bytes() != DOCS_MD.read_bytes():
        errors.append("docs/latest model/data independence Markdown must exactly mirror output/latest")

    with OUTPUT_CSV.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if tuple(reader.fieldnames or ()) != OUTPUT_COLUMNS:
            errors.append("model/data independence audit CSV schema drift")
            return errors
        actual = [{key: str(value or "") for key, value in row.items()} for row in reader]
    if not actual:
        errors.append("model/data independence audit CSV is empty")
        return errors
    generated_values = {row["generated_at"] for row in actual}
    if len(generated_values) != 1 or not next(iter(generated_values)):
        errors.append("model/data independence audit must use one non-empty generated_at value")
    generated_at = next(iter(generated_values)) if generated_values else ""
    expected = build_rows(generated_at)
    if actual != expected:
        errors.append("model/data independence audit is stale relative to current contracts and AST ownership")
    if any(row["status"] == "FAIL" for row in actual):
        errors.append("model/data independence audit contains FAIL rows")
    return errors


def main() -> int:
    args = parse_args()
    errors = validate(base_ref=args.base_ref)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("model and data independence validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
