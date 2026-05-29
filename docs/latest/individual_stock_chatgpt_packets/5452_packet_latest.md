# INDIVIDUAL STOCK CHATGPT PACKET - 5452 佶優

## Metadata
- generated_at: 2026-05-29 19:33:08 Asia/Taipei
- stock_id: 5452
- stock_name: 佶優
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5452_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5452_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5452_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5452_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5452_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5452_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5452_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5452_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5452_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5452_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5452_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5452_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5452_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5452_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5452_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5452_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5452_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5452_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5452.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5452.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5452.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5452.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5452.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5452.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5452_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5452_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5452_latest.md?ref=main

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
- open: 32.5
- high: 35.5
- low: 32.05
- close: 34.95
- volume: 34000
- ma5: 33.7
- ema23_primary: 33.18
- distance_to_ema23_pct: 5.34
- ma20: 33.05
- ma60: 33.4
- ma120: 30.66
- return_5d: 1.01
- return_20d: 11.13
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: 5.76
- distance_to_high_60_pct: -14.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,32,33.3,31.55,32.15,1837000,33.03,-2.65,33.08,32.76,0.67
20260505,32.75,33.5,32.3,33.5,1971000,33.06,1.32,33.18,32.73,0.73
20260506,33.85,34.5,32.45,33.6,3143000,33.11,1.48,33.25,32.75,1.14
20260507,34.1,34.1,32.9,32.95,1958000,33.1,-0.44,33.25,32.77,0.7
20260508,32.95,34.65,31.8,32.15,2946000,33.02,-2.63,33.23,32.79,1.04
20260511,32.4,34,32.3,33.6,2878000,33.07,1.62,33.28,32.86,0.99
20260512,33.75,34,32.7,33.5,1973000,33.1,1.2,33.21,32.93,0.7
20260513,33.5,33.6,32.6,32.9,1344000,33.09,-0.56,33.16,32.95,0.49
20260514,33.2,33.7,32.05,32.85,1544000,33.07,-0.65,33.16,32.98,0.56
20260515,33.4,33.6,31.55,31.7,2082000,32.95,-3.8,33.02,33.01,0.76
20260518,31.7,32.75,31.2,32.35,1222000,32.9,-1.68,32.93,33.06,0.46
20260519,32.8,33.15,31.95,32.05,1224000,32.83,-2.38,32.73,33.11,0.54
20260520,32.05,32.1,31.25,31.75,1007000,32.74,-3.03,32.56,33.16,0.47
20260521,31.9,33.3,31.9,32.8,1802000,32.75,0.17,32.46,33.23,0.86
20260522,33.4,34.95,33.05,34.6,34000,32.9,5.17,32.59,33.28,0.02
20260525,35.45,35.5,34.65,34.85,35000,33.06,5.41,32.76,33.35,0.02
20260526,35,35.55,33.2,33.5,34000,33.1,1.21,32.82,33.4,0.02
20260527,33.8,33.85,32.7,32.85,33000,33.08,-0.69,32.88,33.42,0.02
20260528,32.85,34,32,32.35,33000,33.02,-2.02,32.87,33.38,0.02
20260529,32.5,35.5,32.05,34.95,34000,33.18,5.34,33.05,33.4,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 43.39
- over_600_ratio: 39.22
- over_800_ratio: 38.82
- over_1000_ratio: 38.82
- over_400_change_1w: 0.49
- over_800_change_1w: 0.21
- over_1000_change_1w: 0.21
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.39,,39.24,,38.61,,0,False,False
20260508,43.09,0.7,38.74,-0.5,38.74,0.13,1,False,True
20260515,42.9,-0.19,38.61,-0.13,38.61,-0.13,2,False,False
20260522,43.39,0.49,38.82,0.21,38.82,0.21,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260521 | 5452 | 佶優 | pattern | 型態觀察 |  |  |  | 預備發動型 |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 5452 | 佶優 | 7 | 7 | 5 | 7 | 7 | repeated_but_no_breakout | 近 10 日上榜 7 日、近 20 日上榜 7 日，尚未突破，需分辨醞釀或鈍化。 |

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
