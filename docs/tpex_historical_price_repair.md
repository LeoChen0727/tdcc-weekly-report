# 2025 年 9 月上櫃歷史行情修訂

本次修訂僅包含 `config/tpex_historical_price_repair_202509.csv` 登記的 17 日
`data/daily_price/YYYYMMDD.csv`。原檔每一筆 `listed` 實體 CSV 行原樣保留；
只依官方原文更正 `otc`，不重建 per-stock history、模型、回測或 PDF。

最新 main 查核時，17 個原檔均與既有調查的 SHA-256 一致；每日 1,121 個上櫃列
除日期外整批重複。1,121 不是正確列數的契約，也不能當成認證普通股數量。
原匯入提交 `8ede6166fa59aa5c91d78e5c17a15c889a6bebab` 的 HTTP 原文未保存，
因此不推論當年伺服器、快取或 redirect 的具體行為。

## 來源與收件

`backfill_official_daily_price.py` 仍由 `official_price_backfill.yml` 使用。
修正其 TPEx 收件，核對官方回應日期、完整證券代號與重複批次。
一般行情及區間補檔另使用 `fetch_official_daily_price.py`，本次不改該路徑。

官方來源為 TPEx `afterTrading/otc?date=YYYY/MM/DD&type=EW&response=json`，
表名「上櫃股票每日收盤行情(不含定價)」。成交股數單位為股、成交金額為元；
最後買賣量的張數不作成交量。完整代號先判斷既有四位非 `00` 篩選條件，
長代號不截短。無成交價格不補昨收或 0；未通過既有 close/volume 非空條件
的列不寫進本次 legacy daily CSV，所有原列均保存在官方 raw。

這是現在回查的歷史版本，`original_publication_version_verified=false`。
修正價格不等於首次發布 PIT 認證，也不改寫舊研究結論或產物。

## 重現與驗收

原文及查詢收據保存於 `retained-evidence/tpex-history-repair-202509/raw/`。
20250919、20250926 重用既有核實原件；其他 15 日僅各抓取目標日。
manifest 逐日記錄原 Git SHA、原檔 SHA、修訂 SHA、上市實體行 SHA、
官方 raw SHA、URL、查詢時間及列數。原始完整檔案由登記的 Git 提交保留。

```text
python scripts/repair_historical_tpex_prices.py
python -m pytest tests/test_backfill_official_daily_price.py tests/test_historical_tpex_price_repair.py -q
```

預設命令僅離線驗證，不下載、不重寫檔案。`--verify-ref origin/main` 可直接讀 Git
objects 驗收，不需完整 checkout 資料樹。驗證逐日從官方原文重建上櫃列並比對
實際資料，同時核對上市實體行、修訂來源、17 日邊界及跨日整批重複。
`--collect` 只收指定 17 日原文；`--apply --source-ref <ref>` 才寫修訂檔，
已有本機目標若與 source ref 不同會拒絕覆寫。每次整批重建與重複檢查通過後才寫入。

PR 與合併後的 `Daily Model Maintenance PR Validation` 在
`repo-current-contracts` 執行 focused pytest。當中的
`test_registered_repair_replays_official_raw` 直接呼叫 `repair.validate(root)`，
實際核對 repo 的 17 日原文、雜湊、修訂資料及上市列；CI 不執行修復 CLI，
也不執行 `--collect` 或 `--apply`。

手動 CLI 登錄於 [production inventory 操作說明](repo_production_inventory.md)。
合併後採 main `workflow_dispatch`、`validation_profile=all`，再以手動
`python scripts/repair_historical_tpex_prices.py --verify-ref origin/main` 驗收
main 的實際資料；不派送正式產報 workflow。
