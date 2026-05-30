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

    def test_authorized_theme_buckets_are_core_mainstream(self) -> None:
        cases = [
            ("重電電網", "", "power_grid_theme"),
            ("軍工無人機", "", "defense_drone_theme"),
            ("網通交換器", "", "network_switch_theme"),
            ("車用電子", "", "automotive_electronics_theme"),
        ]
        for primary, secondary, expected in cases:
            with self.subTest(primary=primary):
                bucket = taxonomy.infer_bucket(primary, secondary, "")
                self.assertEqual(bucket, expected)
                self.assertEqual(taxonomy.infer_mainstream_label(bucket, ""), "core_mainstream")

    def test_authorized_seed_contains_multi_theme_stocks(self) -> None:
        seed = taxonomy.load_authorized_seed()
        huatung = seed[seed["stock_id"].eq("2313")].iloc[0]
        qiqi = seed[seed["stock_id"].eq("6285")].iloc[0]
        self.assertEqual(huatung["primary_theme"], "PCB_CCL_ABF材料")
        self.assertIn("低軌衛星", huatung["secondary_themes"])
        self.assertEqual(qiqi["primary_theme"], "低軌衛星")
        self.assertIn("網通交換器", qiqi["secondary_themes"])

    def test_non_mainstream_industry_fallback(self) -> None:
        bucket = taxonomy.infer_bucket("", "", "金融保險業")
        self.assertEqual(bucket, "non_mainstream_theme")
        self.assertEqual(taxonomy.infer_mainstream_label(bucket, "金融保險業"), "non_mainstream")

    def test_dual_industry_and_theme_identity(self) -> None:
        industry_label = taxonomy.infer_industry_mainstream_label("塑膠工業")
        theme_label = taxonomy.infer_mainstream_label("glass_fiber_ccl_theme", "塑膠工業")
        effective = taxonomy.effective_mainstream_label(theme_label, industry_label)
        flag, note = taxonomy.mainstream_conflict_note(industry_label, theme_label, effective)
        self.assertEqual(industry_label, "non_mainstream")
        self.assertEqual(theme_label, "core_mainstream")
        self.assertEqual(effective, "core_mainstream")
        self.assertEqual(flag, "True")
        self.assertIn("report_routing=core_mainstream", note)

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
