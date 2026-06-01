from __future__ import annotations

import unittest

import pandas as pd

from scripts import build_stock_theme_taxonomy as taxonomy


class StockThemeTaxonomyTests(unittest.TestCase):
    def test_manual_mainstream_normalization(self) -> None:
        self.assertEqual(taxonomy.normalize_mainstream("主流"), "core_mainstream")
        self.assertEqual(taxonomy.normalize_mainstream("非主流"), "non_mainstream")
        self.assertEqual(taxonomy.normalize_mainstream("未分類"), "theme_unknown")

    def test_official_industry_fallbacks(self) -> None:
        self.assertEqual(taxonomy.infer_industry_mainstream_label("半導體業"), "core_mainstream")
        self.assertEqual(taxonomy.infer_industry_mainstream_label("電機機械"), "core_mainstream")
        self.assertEqual(taxonomy.infer_industry_mainstream_label("電器電纜"), "core_mainstream")
        self.assertEqual(taxonomy.infer_industry_mainstream_label("金融保險業"), "non_mainstream")
        self.assertEqual(taxonomy.infer_industry_mainstream_label("塑膠工業"), "non_mainstream")

    def test_theme_keywords_are_core_mainstream(self) -> None:
        cases = [
            ("機器人自動化", "", "robotics_precision_motion_theme"),
            ("玻纖布", "PCB_CCL_ABF材料", "glass_fiber_ccl_theme"),
            ("被動元件", "", "passive_component_theme"),
            ("低軌衛星", "", "low_earth_orbit_satellite_theme"),
            ("CPO光通訊", "網通交換器", "network_optical_datacenter_theme"),
            ("AI伺服器", "", "ai_server_ipc_theme"),
        ]
        for primary, secondary, expected in cases:
            with self.subTest(primary=primary):
                bucket = taxonomy.infer_bucket(primary, secondary, "")
                self.assertEqual(bucket, expected)
                self.assertEqual(taxonomy.infer_mainstream_label(bucket, ""), "core_mainstream")

    def test_authorized_seed_contains_user_theme_stocks(self) -> None:
        seed = taxonomy.load_authorized_seed()
        huatung = seed[seed["stock_id"].eq("2313")].iloc[0]
        qiqi = seed[seed["stock_id"].eq("6285")].iloc[0]
        hiwin = seed[seed["stock_id"].eq("2049")].iloc[0]
        self.assertEqual(huatung["primary_theme"], "PCB_CCL_ABF材料")
        self.assertIn("低軌衛星", huatung["secondary_themes"])
        self.assertEqual(qiqi["primary_theme"], "低軌衛星")
        self.assertIn("網通交換器", qiqi["secondary_themes"])
        self.assertEqual(hiwin["primary_theme"], "機器人自動化")

    def test_dual_industry_and_theme_identity(self) -> None:
        industry_label = taxonomy.infer_industry_mainstream_label("塑膠工業")
        theme_label = taxonomy.infer_mainstream_label("glass_fiber_ccl_theme", "塑膠工業")
        effective = taxonomy.effective_mainstream_label(theme_label, industry_label)
        flag, note = taxonomy.mainstream_conflict_note(industry_label, theme_label, effective)
        membership = taxonomy.report_membership_fields(industry_label, theme_label, effective)

        self.assertEqual(industry_label, "non_mainstream")
        self.assertEqual(theme_label, "core_mainstream")
        self.assertEqual(effective, "core_mainstream")
        self.assertEqual(flag, "True")
        self.assertIn("report_routing=core_mainstream", note)
        self.assertEqual(membership["report_line_memberships"], "mainstream|non_mainstream")
        self.assertEqual(membership["dual_report_membership_flag"], "True")

    def test_blank_manual_theme_keeps_default_theme(self) -> None:
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
                "primary_theme": ["機器人自動化"],
                "secondary_themes": [""],
                "industry_mainstream_label": ["core_mainstream"],
                "theme_mainstream_label": ["core_mainstream"],
                "effective_mainstream_label": ["core_mainstream"],
                "mainstream_conflict_flag": ["False"],
                "report_line_memberships": ["mainstream"],
                "mainstream_report_eligible": ["True"],
                "non_mainstream_report_eligible": ["False"],
                "notes": [""],
            }
        )
        template = taxonomy.build_template(source, rows_per_sheet=500, write_files=False)
        self.assertEqual(
            list(template.columns),
            [
                "股票代號",
                "股票名稱",
                "上市櫃產業",
                "基本族群",
                "主流/非主流",
                "熱門族群1",
                "熱門族群2",
                "熱門族群3",
                "熱門族群4",
                "熱門族群5",
                "備註",
            ],
        )

    def test_manual_both_routes_to_both_reports(self) -> None:
        industry_label = taxonomy.infer_industry_mainstream_label("金融保險業")
        theme_label = taxonomy.normalize_mainstream("都有")
        effective = taxonomy.effective_mainstream_label(theme_label, industry_label)
        flag, note = taxonomy.mainstream_conflict_note(industry_label, theme_label, effective)
        membership = taxonomy.report_membership_fields(industry_label, theme_label, effective)

        self.assertEqual(industry_label, "non_mainstream")
        self.assertEqual(theme_label, "both")
        self.assertEqual(effective, "both")
        self.assertEqual(flag, "True")
        self.assertIn("report_routing=both", note)
        self.assertEqual(membership["report_line_memberships"], "mainstream|non_mainstream")
        self.assertEqual(membership["mainstream_report_eligible"], "True")
        self.assertEqual(membership["non_mainstream_report_eligible"], "True")
        self.assertEqual(membership["dual_report_membership_flag"], "True")


if __name__ == "__main__":
    unittest.main()
