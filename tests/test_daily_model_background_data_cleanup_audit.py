from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_daily_model_background_data_cleanup_audit import build_audit_rows, deletion_decision  # noqa: E402
from validate_daily_model_background_data_cleanup_audit import validate_audit  # noqa: E402


@pytest.fixture(scope="module")
def audit_df() -> pd.DataFrame:
    return pd.DataFrame(build_audit_rows())


def test_cleanup_audit_current_artifacts_are_not_deletable(audit_df: pd.DataFrame) -> None:
    assert validate_audit(audit_df) == []
    assert set(audit_df["deletion_allowed"]) == {"False"}
    assert "eligible_for_cleanup_pr" not in set(audit_df["deletion_decision"])
    assert not audit_df["config_references"].str.contains("daily_model_background_data_registry.csv").any()


def test_active_family_cannot_be_marked_deletion_allowed(audit_df: pd.DataFrame) -> None:
    audit = audit_df.copy(deep=True)
    row_idx = audit.index[audit["data_family_id"].eq("stock_price_history")][0]
    audit.loc[row_idx, "deletion_allowed"] = "True"
    audit.loc[row_idx, "deletion_decision"] = "eligible_for_cleanup_pr"

    errors = validate_audit(audit)

    assert any("active or blocked data families must not have deletion_allowed=True" in error for error in errors)
    assert any("eligible_for_cleanup_pr requires cleanup_status=deprecated_candidate" in error for error in errors)


def test_deprecated_candidate_requires_no_dependencies_for_cleanup_pr() -> None:
    base = {
        "data_family_id": "old_unused_family",
        "scope": "model_research_output",
        "cleanup_status": "deprecated_candidate",
        "retention_policy": "delete_after_review",
    }

    blocked = deletion_decision(deepcopy(base), dependency_count=2)
    eligible = deletion_decision(deepcopy(base), dependency_count=0)

    assert blocked[0] == "blocked_deprecated_candidate_has_dependencies"
    assert blocked[3] is False
    assert eligible[0] == "eligible_for_cleanup_pr"
    assert eligible[3] is True


def test_revenue_panel_is_active_shared_source_not_deletion_target(audit_df: pd.DataFrame) -> None:
    revenue = audit_df[audit_df["data_family_id"].eq("monthly_revenue_point_in_time_panel")]

    assert len(revenue) == 1
    assert revenue.iloc[0]["deletion_decision"] == "retain_shared_objective_source"
    assert revenue.iloc[0]["deletion_allowed"] == "False"
