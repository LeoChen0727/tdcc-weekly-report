from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_daily_operation_adapter_protected_fields as validator  # noqa: E402


def test_current_repo_protected_field_contract_passes() -> None:
    assert validator.validate() == []


def test_revenue_adapter_is_exactly_registered_as_a_mature_protected_model() -> None:
    _, rows = validator._read_contract()
    revenue_rows = [
        row for row in rows if row["model_id"] == "revenue_unreacted_range"
    ]
    assert {row["lifecycle_state"] for row in revenue_rows} == {
        "pending",
        "confirmed",
        "active",
        "empty",
    }
    assert {
        row["artifact_path"] for row in revenue_rows
    } == {
        "output/latest/daily_revenue_unreacted_range_operation_section_latest.csv"
    }


def test_ast_guard_rejects_duplicate_protected_global(tmp_path: Path) -> None:
    source = tmp_path / "producer.py"
    source.write_text("SECTION_ZH = {}\nSECTION_ZH = {}\n", encoding="utf-8")
    errors = validator._validate_producer_ast(source)
    assert any("protected global SECTION_ZH assigned more than once" in error for error in errors)


def test_ast_guard_rejects_duplicate_protected_dict_key(tmp_path: Path) -> None:
    source = tmp_path / "producer.py"
    source.write_text(
        "def build():\n    return {'quality_status_zh': 'a', 'quality_status_zh': 'b'}\n",
        encoding="utf-8",
    )
    errors = validator._validate_producer_ast(source)
    assert any("duplicate protected dict keys ['quality_status_zh']" in error for error in errors)


def test_ast_guard_rejects_repeated_protected_row_write(tmp_path: Path) -> None:
    source = tmp_path / "producer.py"
    source.write_text(
        "def build():\n"
        "    row = {'quality_status_zh': 'a'}\n"
        "    row['quality_status_zh'] = 'b'\n"
        "    return row\n",
        encoding="utf-8",
    )
    errors = validator._validate_producer_ast(source)
    assert any("writes protected field row['quality_status_zh'] more than once" in error for error in errors)


def test_runtime_guard_rejects_legacy_volume_confirmed_quality_text() -> None:
    model_id = "volume_range_breakout_v2_low_position_volume_attack"
    frame = pd.DataFrame(
        [
            {
                "model_id": model_id,
                "pdf_section": "confirmed_operation",
                "row_type": "data",
                "operation_status": "confirmed_operation",
                "operation_status_zh": "本日可買 / 已確認買入候選",
                "quality_status_zh": "已通過 v2 模型條件與 close-only 確認",
                "row_action_status": "confirmed_buy_candidate",
                "buy_rank_eligible": "True",
                "adapter_note_zh": "由 v2 正式模型條件與 close-only 確認產生；不使用舊 v1 hidden evidence gate。",
            }
        ]
    )
    errors = validator.validate_adapter_frame(frame, model_id)
    assert any("quality_status_zh" in error and "正向證據" in error for error in errors)
