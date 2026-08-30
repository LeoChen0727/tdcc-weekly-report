from __future__ import annotations

from formal_model_evidence import PIN_REGISTRY, ROOT, load_evidence_pins, validate_evidence_pin


REQUIRED_MODELS = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
    "w_bottom_right_side",
    "neckline_volume_breakout_confirmation",
    "price_pullback_23ema",
}


def validate() -> list[str]:
    errors: list[str] = []
    try:
        pins = load_evidence_pins()
    except RuntimeError as exc:
        return [str(exc)]
    model_ids = [pin.model_id for pin in pins]
    duplicates = sorted({model_id for model_id in model_ids if model_ids.count(model_id) > 1})
    if duplicates:
        errors.append(f"duplicate formal model evidence pins: {duplicates}")
    missing = sorted(REQUIRED_MODELS - set(model_ids))
    extra = sorted(set(model_ids) - REQUIRED_MODELS)
    if missing:
        errors.append(f"missing formal model evidence pins: {missing}")
    if extra:
        errors.append(f"unexpected formal model evidence pins: {extra}")
    for pin in pins:
        errors.extend(validate_evidence_pin(pin))
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"formal model evidence pin validation passed: {PIN_REGISTRY.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
