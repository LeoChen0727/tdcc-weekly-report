from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = f"""# 台股每日監測報告

產生時間：{today}

## 1. 盤整帶量突破候選股

目前尚未啟用正式篩選。

## 2. 營收成長但股價回檔候選股

目前尚未啟用正式篩選。

## 3. 兩策略交集股

目前尚未啟用正式篩選。
"""

Path("output/stock_monitor_latest.md").write_text(report, encoding="utf-8")

print("Daily stock monitor report generated.")
