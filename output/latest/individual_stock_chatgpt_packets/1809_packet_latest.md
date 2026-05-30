# INDIVIDUAL STOCK CHATGPT PACKET - 1809 中釉

## Metadata
- generated_at: 2026-05-30 23:41:11 Asia/Taipei
- stock_id: 1809
- stock_name: 中釉
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1809_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1809_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1809_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1809_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1809_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1809_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1809_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1809_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1809_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1809_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1809_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1809_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1809_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1809_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1809_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1809_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1809_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1809_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1809.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1809.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1809.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1809.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1809.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1809.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1809_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1809_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1809_latest.md?ref=main

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
- date: 20260529
- open: 43.3
- high: 44.2
- low: 41.2
- close: 43.55
- volume: 8472822
- ma5: 44.93
- ema23_primary: 38.36
- distance_to_ema23_pct: 13.53
- ma20: 39.02
- ma60: 30.81
- ma120: 25.95
- return_5d: 4.94
- return_20d: 69.46
- volume_ratio: 0.77
- distance_to_ma20_pct_auxiliary: 11.6
- distance_to_high_60_pct: -12.9

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,26.2,28.25,25.7,28.25,4405037,26.71,5.77,26.56,26.23,1.23
20260505,29.95,31.05,28.7,31.05,16142640,27.07,14.7,26.86,26.29,3.78
20260506,34.15,34.15,32.9,34.15,19148538,27.66,23.46,27.33,26.41,3.73
20260507,37.3,37.4,33.25,34.5,39198080,28.23,22.2,27.74,26.56,5.64
20260508,34.75,37.25,33.65,36,23648739,28.88,24.66,28.24,26.75,2.96
20260511,36.25,39.6,35.2,39.6,12762844,29.77,33.01,28.94,27,1.5
20260512,43.45,43.55,40,40.4,34259462,30.66,31.78,29.63,27.27,3.41
20260513,38.8,39.9,37.9,39,4833251,31.35,24.39,30.25,27.48,0.48
20260514,40.2,41.45,39,39.25,3396542,32.01,22.61,30.85,27.7,0.34
20260515,40,40.2,38.45,38.6,2679589,32.56,18.55,31.43,27.93,0.27
20260518,38.6,38.6,36.55,37.6,3027153,32.98,14.01,31.95,28.17,0.31
20260519,38.45,40,38.3,38.3,1920649,33.42,14.59,32.46,28.42,0.2
20260520,39.7,39.7,38.45,38.45,1836059,33.84,13.62,33.01,28.68,0.19
20260521,39.05,39.95,39.05,39.2,1993002,34.29,14.32,33.52,28.94,0.22
20260522,38.95,41.55,38.85,41.5,4046781,34.89,18.95,34.26,29.22,0.44
20260525,42.5,45.65,42.5,45.65,5416039,35.79,27.56,35.26,29.57,0.58
20260526,46.9,50,44.6,49.3,6371593,36.91,33.56,36.47,29.99,0.67
20260527,47.05,48.5,44.4,44.4,13175875,37.54,18.28,37.37,30.3,1.31
20260528,44.45,44.9,40.55,41.75,12395902,37.89,10.19,38.13,30.54,1.17
20260529,43.3,44.2,41.2,43.55,8472822,38.36,13.53,39.02,30.81,0.77
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 50.99
- over_600_ratio: 49.03
- over_800_ratio: 46.47
- over_1000_ratio: 45.92
- over_400_change_1w: -2.59
- over_800_change_1w: -3.81
- over_1000_change_1w: -2.21
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,51.88,,47.25,,46.7,,0,False,False
20260508,53.69,1.81,48.16,0.91,47.61,0.91,1,True,True
20260515,54.72,1.03,49.67,1.51,48.07,0.46,2,True,True
20260522,53.58,-1.14,50.28,0.61,48.13,0.06,3,False,True
20260529,50.99,-2.59,46.47,-3.81,45.92,-2.21,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260530 | 1809 | 中釉 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260530 | 1809 | 中釉 | 1 | 1 | 1 | 2 | 2 | first_seen | 歷史上榜資料仍少，先當新訊號觀察。 |

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
