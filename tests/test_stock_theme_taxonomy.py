from __future__ import annotations

import unittest

import pandas as pd

from scripts import build_stock_theme_taxonomy as taxonomy


class StockThemeTaxonomyTests(unittest.TestCase):
    def test_manual_mainstream_normalization(self) -> None:
        self.assertEqual(taxonomy.normalize_mainstream("主流"), "core_mainstream")
        self.assertEqual(taxonomy.normalize_mainstream("非主流"), "non_mainstream")

    def test_robotics_bucket_is_core_mainstream(self) -> None:
        bucket = taxonomy.infer_bucket("機器人", "自動化", "電機機械")
        self.assertEqual(bucket, "robotics_precision_motion_theme")
        self.assertEqual(taxonomy.infer_mainstream_label(bucket, "電機機械"), "core_mainstream")

    def test_non_mainstream_industry_fallback(self) -> None:
        bucket = taxonomy.infer_bucket("", "", "金融保險業")
        self.assertEqual(bucket, "non_mainstream_theme")
        self.assertEqual(taxonomy.infer_mainstream_label(bucket, "金融保險業"), "non_mainstream")

    def test_blank_theme_keeps_default_theme(self) -> None:
        row = pd.Series(
            {
                "stock_id": "2375",
                "stock_name": "凱美",
                "industry": "電子零組件業",
                "default_primary_theme": "passive components",
                "default_secondary_themes": "capacitors",
                "manual_primary_theme": "",
                "manual_theme_2": "",
                "manual_theme_3": "",
                "manual_theme_mainstream_label": "",
                "manual_structural_theme_bucket": "",
            }
        )
        primary = taxonomy.compact_text(row.get("manual_primary_theme", "")) or taxonomy.compact_text(row.get("default_primary_theme", ""))
        secondary = ";".join(taxonomy.split_themes(row.get("manual_theme_2", ""), row.get("manual_theme_3", ""), row.get("default_secondary_themes", "")))
        bucket = taxonomy.infer_bucket(primary, secondary, row.get("industry", ""), row.get("manual_structural_theme_bucket", ""))
        self.assertEqual(primary, "passive components")
        self.assertEqual(bucket, "passive_component_theme")

    def test_excel_template_has_simple_chinese_columns(self) -> None:
        source = pd.DataFrame(
            {
                "stock_id": ["2049"],
                "stock_name": ["上銀"],
                "industry": ["電機機械"],
                "primary_theme": ["機器人"],
                "secondary_themes": ["自動化"],
                "theme_mainstream_label": ["core_mainstream"],
                "notes": [""],
            }
        )
        template = pd.DataFrame(
            {
                "股票代號": source["stock_id"],
                "股票名稱": source["stock_name"],
                "目前產業": source["industry"],
                "主流/非主流": ["主流"],
                "主要族群1": source["primary_theme"],
                "族群2": ["自動化"],
                "族群3": [""],
                "備註": source["notes"],
            }
        )
        self.assertEqual(
            list(template.columns),
            ["股票代號", "股票名稱", "目前產業", "主流/非主流", "主要族群1", "族群2", "族群3", "備註"],
        )


if __name__ == "__main__":
    unittest.main()
