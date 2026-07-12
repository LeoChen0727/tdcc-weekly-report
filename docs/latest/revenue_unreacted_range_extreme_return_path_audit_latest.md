# 營收低反應模型極端報酬價格路徑稽核

- artifact_version: `extreme_return_path_raw_price_v1_20260712`
- extreme threshold: `abs(realized_return_pct) >= 80%`
- operation basis: 確認後下一交易日開盤進場，確認日後第 20 個交易日收盤出場。
- raw verification: 每個持有交易日的 OHLC 均逐列對照 `data/daily_price/YYYYMMDD.csv`。
- interpretation: `plausible_extreme_continuous_gain` 表示價格路徑可實現且 raw 資料一致，不表示適合直接用於 promotion。
- calendar limitation: 現有 company calendar 不是完整歷史公司行動 PIT 層，因此公司行動欄只作輔助揭露。
- decision: 可實現極端值保留於主樣本，同時另列排除 `abs >= 80%` 的敏感度結果。
- financial statement scope: EPS、毛利率、營益率、營業利益、業外與淨利均未納入。

|   stock_id | stock_name   |   entry_date |   entry_open |   exit_date |   exit_close |   realized_return_pct |   price_path_trading_rows |   max_abs_daily_price_move_pct |   limit_up_like_day_count |   market_limit_violation_count | price_path_classification         |
|-----------:|:-------------|-------------:|-------------:|------------:|-------------:|----------------------:|--------------------------:|-------------------------------:|--------------------------:|-------------------------------:|:----------------------------------|
|       2327 | 國巨*        |     20260429 |       325    |    20260527 |        701   |              115.692  |                        20 |                        10      |                         6 |                              0 | plausible_extreme_continuous_gain |
|       3229 | 晟鈦         |     20260414 |        24.25 |    20260512 |         49   |              102.062  |                        20 |                         9.9875 |                         6 |                              0 | plausible_extreme_continuous_gain |
|       6658 | 聯策         |     20260422 |        84.9  |    20260520 |        170   |              100.236  |                        20 |                         9.988  |                        10 |                              0 | plausible_extreme_continuous_gain |
|       3090 | 日電貿       |     20260506 |       110    |    20260602 |        220   |              100      |                        20 |                        10      |                         8 |                              0 | plausible_extreme_continuous_gain |
|       3093 | 港建*        |     20260210 |        27    |    20260319 |         53.9 |               99.6296 |                        20 |                        10      |                         5 |                              0 | plausible_extreme_continuous_gain |
|       5475 | 德宏         |     20260120 |       109.5  |    20260225 |        216   |               97.2603 |                        20 |                         9.9237 |                         6 |                              0 | plausible_extreme_continuous_gain |
|       5464 | 霖宏         |     20260421 |        32    |    20260519 |         62.5 |               95.3125 |                        20 |                        10      |                         7 |                              0 | plausible_extreme_continuous_gain |
|       3443 | 創意         |     20260410 |      2695    |    20260508 |       5210   |               93.321  |                        20 |                         9.9899 |                         4 |                              0 | plausible_extreme_continuous_gain |
|       6949 | 沛爾生醫-創  |     20250711 |       160.5  |    20250807 |        309.5 |               92.8349 |                        20 |                         9.9609 |                         6 |                              0 | plausible_extreme_continuous_gain |
|       4908 | 前鼎         |     20260410 |       120    |    20260508 |        229.5 |               91.25   |                        20 |                        10      |                         9 |                              0 | plausible_extreme_continuous_gain |
|       6683 | 雍智科技     |     20260120 |       439.5  |    20260225 |        835   |               89.9886 |                        20 |                        10      |                         5 |                              0 | plausible_extreme_continuous_gain |
|       3339 | 泰谷         |     20260324 |        37.25 |    20260422 |         69.1 |               85.5034 |                        20 |                        10      |                         7 |                              0 | plausible_extreme_continuous_gain |
|       6588 | 東典光電     |     20260116 |        56    |    20260223 |        101.5 |               81.25   |                        20 |                        10      |                         8 |                              0 | plausible_extreme_continuous_gain |
|       7750 | 新代         |     20260409 |      1445    |    20260507 |       2605   |               80.2768 |                        20 |                         9.8398 |                         2 |                              0 | plausible_extreme_continuous_gain |
