# INDIVIDUAL STOCK CHATGPT PACKET - 1316 上曜

## Metadata
- generated_at: 2026-05-28 19:31:28 Asia/Taipei
- stock_id: 1316
- stock_name: 上曜
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1316_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1316_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1316_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1316_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1316_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1316_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1316_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1316_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1316_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1316_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1316_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1316_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1316_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1316_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1316_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1316_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1316_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1316_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1316.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1316.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1316.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1316.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1316.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1316.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1316_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1316_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1316_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260528
- open: 10.15
- high: 10.3
- low: 10.1
- close: 10.2
- volume: 2386967
- ma5: 10.24
- ema23_primary: 10.86
- distance_to_ema23_pct: -6.06
- ma20: 10.84
- ma60: 11.8
- ma120: 13.24
- return_5d: -5.12
- return_20d: -9.33
- volume_ratio: 0.91
- distance_to_ma20_pct_auxiliary: -5.9
- distance_to_high_60_pct: -24.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,11.3,11.3,10.95,11,1376821,11.79,-6.71,11.78,12.76,0.68
20260504,11.15,11.15,10.95,11,1567491,11.73,-6.19,11.72,12.71,0.77
20260505,11.1,11.3,11.1,11.25,6835182,11.69,-3.73,11.68,12.66,2.93
20260506,11.25,11.85,11.2,11.5,4857269,11.67,-1.46,11.65,12.62,1.92
20260507,11.55,11.55,11.25,11.35,2466302,11.64,-2.52,11.61,12.57,0.95
20260508,11.35,11.45,11.15,11.2,1780506,11.61,-3.51,11.57,12.52,0.68
20260511,11.3,11.65,11.25,11.45,2066476,11.59,-1.24,11.53,12.48,0.78
20260512,11.65,11.8,11.25,11.45,2250319,11.58,-1.14,11.5,12.44,0.83
20260513,11.45,11.45,11.1,11.15,1316023,11.55,-3.43,11.46,12.4,0.51
20260514,11.2,11.25,10.95,11.15,1682769,11.51,-3.15,11.4,12.35,0.64
20260515,11,11.05,10.5,10.6,4400670,11.44,-7.32,11.32,12.29,1.61
20260518,10.6,10.9,10.5,10.75,1389564,11.38,-5.53,11.26,12.25,0.52
20260519,10.8,10.85,10.4,10.4,2380410,11.3,-7.95,11.19,12.2,0.89
20260520,10.45,10.75,10.25,10.6,2759166,11.24,-5.69,11.12,12.15,1.02
20260521,10.7,11.1,10.7,10.75,2280279,11.2,-4.01,11.07,12.09,0.86
20260522,10.75,10.75,10.35,10.4,2522591,11.13,-6.58,11.02,12.03,0.96
20260525,10.4,10.4,10,10.25,3960158,11.06,-7.31,10.98,11.97,1.48
20260526,10.2,10.4,10.1,10.2,1657656,10.99,-7.17,10.95,11.91,0.63
20260527,10.2,10.2,10,10.15,2616714,10.92,-7.03,10.89,11.85,1.01
20260528,10.15,10.3,10.1,10.2,2386967,10.86,-6.06,10.84,11.8,0.91
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 39.08
- over_600_ratio: 34.55
- over_800_ratio: 30.55
- over_1000_ratio: 28.02
- over_400_change_1w: -0.36
- over_800_change_1w: 0.33
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,39.16,,31.44,,28.56,,0,False,False
20260508,39.19,0.03,30.67,-0.77,28.32,-0.24,1,False,False
20260515,39.44,0.25,30.22,-0.45,28.11,-0.21,2,False,False
20260522,39.08,-0.36,30.55,0.33,28.02,-0.09,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1316 | 上曜 | revenue_pullback | 營收成長股價回檔 | 57.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1316 | 上曜 | 1 | 1 | 4 | 5 | 5 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

## Warrant Context
| status |
| --- |
| no rows |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
