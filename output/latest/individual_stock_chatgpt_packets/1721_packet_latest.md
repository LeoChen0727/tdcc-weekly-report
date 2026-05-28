# INDIVIDUAL STOCK CHATGPT PACKET - 1721 三晃

## Metadata
- generated_at: 2026-05-28 19:31:40 Asia/Taipei
- stock_id: 1721
- stock_name: 三晃
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1721_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1721_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1721_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1721_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1721_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1721_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1721_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1721_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1721_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1721_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1721_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1721_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1721_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1721_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1721_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1721_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1721_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1721_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1721.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1721.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1721.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1721.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1721.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1721.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1721_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1721_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1721_latest.md?ref=main

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
- open: 30.5
- high: 30.6
- low: 28.3
- close: 28.5
- volume: 5581311
- ma5: 29.05
- ema23_primary: 28.25
- distance_to_ema23_pct: 0.89
- ma20: 29.39
- ma60: 22.96
- ma120: 19.2
- return_5d: -4.68
- return_20d: 13.55
- volume_ratio: 0.74
- distance_to_ma20_pct_auxiliary: -3.01
- distance_to_high_60_pct: -20.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,25.1,25.1,24,24.2,3069232,22.39,8.07,21.63,19.33,0.53
20260504,24.55,25.05,24.15,24.3,2114095,22.55,7.75,21.98,19.42,0.36
20260505,24.5,26.7,24.3,26.7,3607637,22.9,16.61,22.45,19.54,0.6
20260506,29.35,29.35,26.7,28.4,7475302,23.36,21.6,23.04,19.69,1.18
20260507,28.45,30,27.45,30,4310558,23.91,25.47,23.69,19.87,0.66
20260508,29.95,29.95,27.85,28.5,3096013,24.29,17.32,24.21,20.04,0.47
20260511,28.9,31.35,27.1,31.35,12326720,24.88,26,24.89,20.27,1.74
20260512,32,34.45,29.3,34.45,20915270,25.68,34.16,25.7,20.57,2.61
20260513,33.7,36,32.85,34.75,17015859,26.43,31.46,26.44,20.87,2
20260514,34.7,34.75,32.5,32.5,9805262,26.94,20.64,27.1,21.1,1.13
20260515,33,33.4,29.8,31.4,9987691,27.31,14.97,27.74,21.3,1.11
20260518,30.6,30.65,28.9,29.3,5574659,27.48,6.64,28.18,21.49,0.63
20260519,29.3,29.9,27,28.7,5416906,27.58,4.07,28.48,21.68,0.62
20260520,28.85,29.8,27.6,28,4106826,27.61,1.4,28.64,21.86,0.48
20260521,28,30.8,28,29.9,9103471,27.8,7.54,28.78,22.07,1.09
20260522,28.7,29.65,28.3,29,8117373,27.9,3.93,28.73,22.26,1.14
20260525,29.15,29.15,27.6,28.15,6290308,27.92,0.81,28.77,22.41,0.89
20260526,28.5,30.1,27.6,29.45,5562530,28.05,4.99,29.01,22.59,0.78
20260527,29.9,31,29.1,30.15,7613323,28.23,6.82,29.21,22.78,1.03
20260528,30.5,30.6,28.3,28.5,5581311,28.25,0.89,29.39,22.96,0.74
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 42.15
- over_600_ratio: 39.99
- over_800_ratio: 36.58
- over_1000_ratio: 34.1
- over_400_change_1w: -1.31
- over_800_change_1w: -0.68
- over_1000_change_1w: -1.14
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,44.33,,38.89,,36.52,,0,False,False
20260508,45.65,1.32,39.29,0.4,36.81,0.29,1,True,True
20260515,43.46,-2.19,37.26,-2.03,35.24,-1.57,0,False,False
20260522,42.15,-1.31,36.58,-0.68,34.1,-1.14,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1721 | 三晃 | pattern | 型態觀察 | 43.0 |  |  | pullback_entry_zone |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1721 | 三晃 | 3 | 3 | 3 | 3 | 3 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

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
