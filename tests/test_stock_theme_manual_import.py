from __future__ import annotations

import pandas as pd

from scripts.import_stock_theme_manual_overrides import normalize_input


def test_import_chinese_template_with_both_and_multiple_themes() -> None:
    df = pd.DataFrame(
        {
            "股票代號": ["1234"],
            "股票名稱": ["測試股"],
            "上市櫃產業": ["電子通路業"],
            "基本族群": ["電子通路"],
            "主流/非主流": ["都有"],
            "熱門族群1": ["機器人自動化"],
            "熱門族群2": ["低軌衛星"],
            "熱門族群3": ["玻纖布"],
            "熱門族群4": ["AI伺服器"],
            "熱門族群5": ["矽智財/ASIC"],
            "備註": ["manual check"],
        }
    )

    out = normalize_input(df)

    assert len(out) == 1
    row = out.iloc[0]
    assert row["stock_id"] == "1234"
    assert row["stock_name"] == "測試股"
    assert row["basic_theme"] == "電子通路"
    assert row["theme_mainstream_label"] == "both"
    assert row["primary_theme"] == "機器人自動化"
    assert row["theme_2"] == "低軌衛星"
    assert row["theme_3"] == "玻纖布"
    assert row["theme_4"] == "AI伺服器"
    assert row["theme_5"] == "矽智財/ASIC"
