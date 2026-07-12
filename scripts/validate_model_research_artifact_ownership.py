from __future__ import annotations

from pathlib import Path

from model_research_artifact_guard import (
    DEFAULT_REGISTRY,
    DEFAULT_SENTINEL_REGISTRY,
    ROOT,
    load_ownership_rules,
    load_protected_sentinels,
    protected_sentinel_snapshot,
)


REQUIRED_MODEL_PRODUCERS = {
    "revenue_unreacted_range": "scripts/build_revenue_unreacted_range_research.py",
    "price_pullback_23ema": "scripts/build_price_pullback_23ema_research.py",
    "volume_range_breakout_v2": "scripts/build_volume_range_breakout_v2_research.py",
}
REQUIRED_PROTECTED_CLASSES = {
    "formal_operation_adapter",
    "production_snapshot",
    "formal_readiness",
    "formal_approval",
    "cross_model_aggregate",
}


def validate() -> list[str]:
    errors: list[str] = []
    try:
        rules = load_ownership_rules(DEFAULT_REGISTRY)
    except RuntimeError as exc:
        return [str(exc)]

    patterns = [rule.artifact_glob for rule in rules]
    duplicates = sorted({pattern for pattern in patterns if patterns.count(pattern) > 1})
    if duplicates:
        errors.append(f"duplicate artifact ownership globs: {duplicates}")

    model_owned_model_ids = sorted(
        {rule.owner_model_id for rule in rules if rule.change_policy == "model_owned_write"}
    )
    missing_required_models = sorted(set(REQUIRED_MODEL_PRODUCERS) - set(model_owned_model_ids))
    if missing_required_models:
        errors.append(f"missing required model-owned producers: {missing_required_models}")

    for model_id in model_owned_model_ids:
        rows = [rule for rule in rules if rule.owner_model_id == model_id and rule.change_policy == "model_owned_write"]
        if not rows:
            errors.append(f"{model_id} missing model_owned_write rows")
            continue
        producers = {row.producer for row in rows}
        if len(producers) != 1:
            errors.append(f"{model_id} must have exactly one model-owned producer: {sorted(producers)}")
            continue
        producer = next(iter(producers))
        expected_producer = REQUIRED_MODEL_PRODUCERS.get(model_id)
        if expected_producer and producer != expected_producer:
            errors.append(f"{model_id} producer must be {expected_producer}")
        path = ROOT / producer
        if not path.exists():
            errors.append(f"missing model-owned producer: {producer}")
            continue
        text = path.read_text(encoding="utf-8")
        if "model_owned_artifact_guard" not in text:
            errors.append(f"{producer} must invoke model_owned_artifact_guard")

    protected = {rule.artifact_class for rule in rules if rule.change_policy != "model_owned_write"}
    missing_protected = sorted(REQUIRED_PROTECTED_CLASSES - protected)
    if missing_protected:
        errors.append(f"missing protected artifact classes: {missing_protected}")

    legacy_rows = [rule for rule in rules if rule.producer == "scripts/build_daily_model_parameter_research.py"]
    if not legacy_rows or {row.change_policy for row in legacy_rows} != {"cross_model_migration_only"}:
        errors.append("legacy cross-model parameter research outputs must be cross_model_migration_only")

    try:
        sentinels = load_protected_sentinels()
        _snapshot, sentinel_errors = protected_sentinel_snapshot(ROOT, sentinels)
        errors.extend(sentinel_errors)
    except RuntimeError as exc:
        errors.append(str(exc))
        sentinels = []
    required_sentinel_classes = {
        "formal_contract",
        "formal_evidence",
        "formal_operation_adapter",
        "formal_readiness",
        "production_snapshot",
    }
    actual_sentinel_classes = {sentinel.sentinel_class for sentinel in sentinels}
    missing_sentinel_classes = sorted(required_sentinel_classes - actual_sentinel_classes)
    if missing_sentinel_classes:
        errors.append(f"missing protected sentinel classes: {missing_sentinel_classes}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"model research artifact ownership validation passed: {DEFAULT_REGISTRY.relative_to(ROOT)}")
    print(f"protected sentinel registry passed: {DEFAULT_SENTINEL_REGISTRY.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
