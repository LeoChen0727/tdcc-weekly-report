from __future__ import annotations

import pandas as pd

from scripts import build_daily_report_model_summary as summary


def test_price_pullback_registry_description_uses_formal_operation_rules() -> None:
    params = pd.DataFrame(
        [
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "23EMA回檔模型",
                "pdf_visibility": "pdf_core_model",
                "main_conditions": "股價回到23EMA或支撐附近，且23EMA/均線結構未破。",
                "operation_guidance": "舊操作說明不應直接出現在PDF標題下方。",
            }
        ]
    )

    registry = summary.build_registry(params)
    description = registry.loc[0, "model_description_zh"]

    assert description == summary.PRICE_PULLBACK_PDF_OPERATION_DESCRIPTION_ZH
    assert "買入：本表股票為23EMA回檔模型通過候選" in description
    assert "賣出：收盤突破訊號日前20日高點後" in description
    assert "停損：收盤連續4天低於MA20/EMA23較低者4%" in description
    assert "股價回到23EMA或支撐附近" not in description


def test_non_price_pullback_registry_still_uses_main_conditions() -> None:
    params = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
                "pdf_visibility": "pdf_core_model",
                "main_conditions": "放量突破條件。",
                "operation_guidance": "操作說明。",
            }
        ]
    )

    registry = summary.build_registry(params)

    assert registry.loc[0, "model_description_zh"] == "放量突破條件。"
