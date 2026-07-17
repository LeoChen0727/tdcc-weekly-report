from __future__ import annotations

import pytest

from scripts import validate_warrant_source_status as validator


def test_warning_grace_requires_explicit_noncritical_allowance() -> None:
    status = {
        "status": "warning_grace",
        "daily_publish_allowed": True,
        "warrant_pdf_visibility": "hidden_unavailable",
        "model_effect_allowed": False,
        "pdf_effect_allowed": False,
    }

    assert validator.validate_status(status, allow_noncritical_grace=True) == []
    assert validator.validate_status(status, allow_noncritical_grace=False) == [
        "warrant source is unavailable and grace was not enabled"
    ]


def test_warning_grace_rejects_visible_or_effect_enabled_status() -> None:
    status = {
        "status": "warning_grace",
        "daily_publish_allowed": True,
        "warrant_pdf_visibility": "visible",
        "model_effect_allowed": True,
        "pdf_effect_allowed": True,
    }

    errors = validator.validate_status(status, allow_noncritical_grace=True)

    assert "warning_grace status must set warrant_pdf_visibility=hidden_unavailable" in errors
    assert "warning_grace status must not allow warrant model effect" in errors
    assert "warning_grace status must not allow formal warrant PDF effect" in errors


def test_failed_status_blocks_after_bounded_grace() -> None:
    errors = validator.validate_status(
        {
            "status": "failed",
            "consecutive_unavailable_trading_days": 3,
            "hard_fail_after_days": 3,
        },
        allow_noncritical_grace=True,
    )

    assert any("warrant source unavailable grace expired" in error for error in errors)


def formal_current_status(**overrides: object) -> dict[str, object]:
    status: dict[str, object] = {
        "status": "ok",
        "requested_date": "20260716",
        "target_date": "20260716",
        "data_date": "20260716",
        "daily_publish_allowed": True,
        "warrant_pdf_visibility": "visible",
        "model_effect_allowed": True,
        "pdf_effect_allowed": True,
    }
    status.update(overrides)
    return status


def test_formal_current_status_requires_exact_date_and_effect_contract() -> None:
    assert validator.validate_status(
        formal_current_status(),
        allow_noncritical_grace=False,
        require_formal_current=True,
        expected_date="2026-07-16",
    ) == []


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        (
            "daily_publish_allowed",
            False,
            "formal current warrant status must set daily_publish_allowed=true",
        ),
        (
            "model_effect_allowed",
            False,
            "formal current warrant status must set model_effect_allowed=true",
        ),
        (
            "pdf_effect_allowed",
            False,
            "formal current warrant status must set pdf_effect_allowed=true",
        ),
        (
            "warrant_pdf_visibility",
            "hidden_unavailable",
            "formal current warrant status must set warrant_pdf_visibility=visible",
        ),
    ],
)
def test_formal_current_status_rejects_disabled_effects(
    field: str,
    value: object,
    message: str,
) -> None:
    errors = validator.validate_status(
        formal_current_status(**{field: value}),
        allow_noncritical_grace=False,
        require_formal_current=True,
        expected_date="20260716",
    )

    assert message in errors


def test_formal_current_status_rejects_missing_or_divergent_dates() -> None:
    missing_errors = validator.validate_status(
        formal_current_status(data_date=""),
        allow_noncritical_grace=False,
        require_formal_current=True,
        expected_date="20260716",
    )
    divergent_errors = validator.validate_status(
        formal_current_status(data_date="20260715"),
        allow_noncritical_grace=False,
        require_formal_current=True,
        expected_date="20260716",
    )

    assert "formal current warrant status has invalid or missing data_date" in missing_errors
    assert any("dates must match" in error for error in divergent_errors)
    assert any("data_date must equal main_price_date 20260716" in error for error in divergent_errors)


def test_formal_current_status_rejects_expected_main_date_mismatch() -> None:
    errors = validator.validate_status(
        formal_current_status(),
        allow_noncritical_grace=False,
        require_formal_current=True,
        expected_date="20260717",
    )

    assert len([error for error in errors if "must equal main_price_date 20260717" in error]) == 3
