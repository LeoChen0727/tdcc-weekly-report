# 每日資料新鮮度狀態

- 產生時間：`2026-05-22 21:39:53 Asia/Taipei`
- 主資料日期：`20260522`
- 是否可產出正式每日報告：`False`
- 判斷說明：主監測報告與完整候選清單日期不一致，暫不建議產出正式每日報告

## 各檔案日期

| 檔案 | 日期 | 說明 |
|---|---:|---|
| stock_monitor_latest.md | 20260521 | 主監測報告日期 |
| all_candidates_latest.csv | 20260522 | 完整候選股清單日期 |
| official_price_fetch_latest.md | 20260522 | 價格抓取狀態檔日期 |
| warrant_flow_latest.csv | 20260522 | 權證輔助資料日期 |

## 判斷規則

1. 每日全市場候選股報告應以 `main_price_date` 判斷主資料日期。
2. `main_price_date` 優先取 `stock_monitor_latest.md` 與 `all_candidates_latest.csv` 的最新日期。
3. `official_price_fetch_latest.md` 只作為價格抓取狀態參考，不可作為唯一判斷。
4. `warrant_flow_latest.csv` 是權證輔助資料，日期可落後主資料，不應阻止主報告產出。

## 補充說明

- official price fetch：official_price_fetch_latest.md 與主資料日期一致
- warrant flow：權證資料與主價格資料日期一致
