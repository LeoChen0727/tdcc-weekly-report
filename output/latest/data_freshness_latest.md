# 每日資料新鮮度狀態

- 產生時間：`2026-05-23 15:41:11 Asia/Taipei`
- 主資料日期：`20260523`
- 是否可產出正式每日報告：`True`
- 判斷說明：完整候選清單與官方價格資料日期一致，可以產出正式每日報告

## 各檔案日期

| 檔案 | 日期 | 說明 |
|---|---:|---|
| all_candidates_latest.csv | 20260523 | 完整候選股清單日期，正式報告主資料來源 |
| official_price_fetch_latest.md/json | 20260523 | 官方價格抓取狀態檔日期 |
| stock_monitor_latest.md | 20260523 | 舊版主監測報告日期，若落後只列警告 |
| warrant_flow_latest.csv | 20260523 | 權證輔助資料日期 |

## 判斷規則

1. 每日全市場候選股報告以 `all_candidates_latest.csv` 作為主要資料來源。
2. `official_price_fetch_latest.json/md` 用來確認官方價格資料是否已更新。
3. `stock_monitor_latest.md` 若落後主資料日期，只列為警告，不阻止正式每日報告產出。
4. `warrant_flow_latest.csv` 是權證輔助資料，日期可作為輔助檢查，不應單獨阻止主報告產出。

## 補充說明

- all candidates：主資料來源日期為 `20260523`
- official price fetch：official_price_fetch_latest.md 與主資料日期一致
- stock monitor：stock_monitor_latest.md 與主資料日期一致
- warrant flow：權證資料與主價格資料日期一致
