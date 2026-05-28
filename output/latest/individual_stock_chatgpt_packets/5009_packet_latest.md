# INDIVIDUAL STOCK CHATGPT PACKET - 5009 榮剛

## Metadata
- generated_at: 2026-05-28 19:32:53 Asia/Taipei
- stock_id: 5009
- stock_name: 榮剛
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5009_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5009_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5009_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5009_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5009_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5009_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5009_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5009_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5009_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5009_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5009_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5009_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5009_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5009_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5009_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5009_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5009_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5009_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5009.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5009.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5009.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5009.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5009.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5009.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5009_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5009_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5009_latest.md?ref=main

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
- open: 35.75
- high: 36.45
- low: 35.25
- close: 35.5
- volume: 3794465
- ma5: 35.76
- ema23_primary: 35.35
- distance_to_ema23_pct: 0.42
- ma20: 35.97
- ma60: 33.94
- ma120: 33.36
- return_5d: -0.14
- return_20d: 6.45
- volume_ratio: 0.67
- distance_to_ma20_pct_auxiliary: -1.31
- distance_to_high_60_pct: -13.31

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,33.8,33.8,32.2,32.2,4071000,32.32,-0.36,32.02,33.31,1.7
20260504,32.8,33.8,32.6,33.4,4752000,32.41,3.06,32.06,33.31,1.84
20260505,33.55,35,33.4,34.8,6677000,32.61,6.73,32.2,33.32,2.34
20260506,35,35.3,34.2,35.1,5737000,32.81,6.96,32.36,33.35,1.86
20260507,35.35,36.9,34.95,36.1,10550000,33.09,9.1,32.54,33.39,2.96
20260508,36.4,37.15,35.25,36.5,11111000,33.37,9.37,32.77,33.42,2.74
20260511,38.55,40.15,38.5,40.15,18481000,33.94,18.31,33.18,33.52,3.76
20260512,40.95,40.95,37.3,38.05,17691000,34.28,11,33.52,33.59,3.13
20260513,38.05,38.55,37.5,37.85,6469000,34.58,9.46,33.86,33.67,1.1
20260514,38,39.2,37.2,37.5,5568000,34.82,7.69,34.17,33.73,0.91
20260515,37.5,38.95,37.15,37.3,5324000,35.03,6.49,34.48,33.78,0.85
20260518,37.3,37.3,35.3,35.45,4962000,35.06,1.1,34.69,33.82,0.77
20260519,35.5,36.1,34.85,35.3,3087000,35.08,0.62,34.77,33.83,0.49
20260520,35.25,35.45,34.95,35.4,1931000,35.11,0.83,34.85,33.86,0.31
20260521,35.8,35.8,35.15,35.55,2669000,35.15,1.15,34.98,33.88,0.42
20260522,35.45,36.65,35.25,35.6,36000,35.18,1.18,35.16,33.88,0.01
20260525,35.8,37.2,35.8,36.75,37000,35.31,4.07,35.43,33.91,0.01
20260526,37.2,37.2,35.35,35.8,36000,35.35,1.26,35.68,33.92,0.01
20260527,36.1,36.1,35,35.15,35000,35.34,-0.53,35.87,33.93,0.01
20260528,35.75,36.45,35.25,35.5,3794465,35.35,0.42,35.97,33.94,0.67
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 48.95
- over_600_ratio: 45.88
- over_800_ratio: 44.94
- over_1000_ratio: 43.99
- over_400_change_1w: -0.55
- over_800_change_1w: -0.31
- over_1000_change_1w: 0.13
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,48.56,,44.84,,43.77,,0,False,False
20260508,49.84,1.28,45.82,0.98,44.74,0.97,1,True,True
20260515,49.5,-0.34,45.25,-0.57,43.86,-0.88,0,False,False
20260522,48.95,-0.55,44.94,-0.31,43.99,0.13,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260521 | 5009 | 榮剛 | pattern | 型態觀察 |  |  |  | 接近突破型 |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 5009 | 榮剛 | 6 | 6 | 5 | 6 | 6 | repeated_but_no_breakout | 近 10 日上榜 6 日、近 20 日上榜 6 日，尚未突破，需分辨醞釀或鈍化。 |

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
