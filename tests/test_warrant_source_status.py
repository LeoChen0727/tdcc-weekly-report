from __future__ import annotations

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
