from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_stock_theme_taxonomy import build_taxonomy  # noqa: E402


class StockThemeTaxonomyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = build_taxonomy()
        cls.by_id = {str(row["stock_id"]): row for _, row in cls.df.iterrows()}

    def assert_theme(self, stock_id: str, primary_theme: str, bucket: str | None = None) -> None:
        self.assertIn(stock_id, self.by_id)
        row = self.by_id[stock_id]
        self.assertEqual(row["primary_theme"], primary_theme)
        if bucket is not None:
            self.assertEqual(row["structural_theme_bucket"], bucket)

    def test_passive_component_examples(self) -> None:
        for stock_id in ["6862", "2327", "2375", "2492", "6173", "3357", "3624", "8043", "3026", "2472"]:
            self.assert_theme(stock_id, "被動元件", "passive_component_theme")

    def test_robotics_examples(self) -> None:
        for stock_id in ["2049", "4576", "3813"]:
            self.assert_theme(stock_id, "機器人/精密傳動", "robotics_precision_motion_theme")
        self.assert_theme("1590", "機器人/氣動自動化", "robotics_automation_theme")
        self.assert_theme("2374", "機器人/光學感測", "robotics_optics_sensor_theme")
        self.assert_theme("4585", "機器人/協作機器人", "robotics_collaborative_theme")
        self.assert_theme("2365", "機器人/周邊零組件", "robotics_component_theme")

    def test_low_earth_orbit_examples(self) -> None:
        for stock_id in ["2313", "6285", "4906", "3138", "6271", "3105", "5388", "3596"]:
            self.assert_theme(stock_id, "低軌衛星", "low_earth_orbit_satellite_theme")

    def test_glass_fiber_ccl_examples(self) -> None:
        for stock_id in ["1815", "5340", "1303", "1802", "5475"]:
            self.assert_theme(stock_id, "玻纖布/CCL", "glass_fiber_ccl_theme")

    def test_optical_communication_cpo_examples(self) -> None:
        for stock_id in ["3450", "3081", "3163", "3363", "4979", "6442", "4977", "4908", "3234", "6530"]:
            self.assert_theme(stock_id, "光通訊/CPO", "optical_communication_cpo_theme")
        self.assert_theme("2345", "網通/光通訊", "network_optical_datacenter_theme")

    def test_abf_and_pcb_examples(self) -> None:
        for stock_id in ["3037", "3189", "8046", "4958"]:
            self.assert_theme(stock_id, "ABF載板/IC載板", "abf_substrate_theme")
        for stock_id in ["2368", "6274", "6213", "5439", "2355", "3044"]:
            self.assert_theme(stock_id, "PCB/CCL", "pcb_ccl_theme")

    def test_ai_server_power_thermal_and_interconnect_examples(self) -> None:
        self.assert_theme("2382", "AI伺服器", "ai_server_ipc_theme")
        self.assert_theme("3013", "AI伺服器/機殼", "ai_server_mechanical_theme")
        self.assert_theme("3324", "散熱", "thermal_solution_theme")
        self.assert_theme("3665", "高速傳輸/連接器", "high_speed_interconnect_theme")

    def test_semiconductor_advanced_packaging_and_equipment_examples(self) -> None:
        self.assert_theme("2344", "記憶體/HBM", "memory_hbm_theme")
        self.assert_theme("3131", "半導體設備/材料", "semiconductor_equipment_material_theme")
        self.assert_theme("3711", "先進封裝/CoWoS", "advanced_packaging_cowos_theme")
        self.assert_theme("2449", "AI晶片測試", "ai_chip_testing_theme")
        self.assert_theme("6510", "半導體測試介面", "semiconductor_test_interface_theme")

    def test_non_mainstream_event_themes_are_not_core(self) -> None:
        for stock_id, primary_theme in [("2634", "防衛/航太"), ("8033", "防衛/無人機"), ("6279", "車用電子/EV")]:
            self.assert_theme(stock_id, primary_theme)
            self.assertEqual(self.by_id[stock_id]["theme_structural_status"], "non_mainstream_theme")

    def test_manual_taxonomy_expands_theme_coverage(self) -> None:
        self.assertGreaterEqual(len(self.df), 160)
        question_mark_rows = self.df[
            self.df[["stock_name", "official_industry", "primary_theme", "secondary_themes"]]
            .astype(str)
            .apply(lambda row: any("?" in value for value in row), axis=1)
        ]
        self.assertTrue(question_mark_rows.empty)


if __name__ == "__main__":
    unittest.main()
