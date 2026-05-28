# INDIVIDUAL STOCK CHATGPT PACKET - 2061 風青

## Metadata
- generated_at: 2026-05-28 19:31:45 Asia/Taipei
- stock_id: 2061
- stock_name: 風青
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2061_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2061_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2061_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2061_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2061_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2061_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2061_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2061_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2061_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2061_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2061_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2061_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2061_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2061_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2061_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2061_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2061_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2061_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2061.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2061.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2061.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2061.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2061.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2061.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2061_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2061_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2061_latest.md?ref=main

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
- open: 32.9
- high: 33.9
- low: 32.7
- close: 33
- volume: 1240720
- ma5: 30.95
- ema23_primary: 24.26
- distance_to_ema23_pct: 36.05
- ma20: 23.72
- ma60: 19.24
- ma120: 18.79
- return_5d: 34.69
- return_20d: 71.88
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: 39.11
- distance_to_high_60_pct: -4.62

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,19.15,20.2,19.05,19.35,1075000,17.28,11.96,16.95,17.43,2.16
20260504,19.65,19.9,19.25,19.6,888000,17.48,12.15,17.08,17.47,1.66
20260505,19.75,20,19.6,19.9,672000,17.68,12.57,17.23,17.5,1.19
20260506,20,21.65,19.9,20.65,2377000,17.93,15.2,17.42,17.56,3.5
20260507,21.2,21.9,20.7,21.15,1370000,18.19,16.24,17.63,17.62,1.85
20260508,21.2,21.3,20.35,20.6,956000,18.4,11.99,17.84,17.66,1.22
20260511,20.7,22.65,20.7,22,3037000,18.7,17.68,18.11,17.69,3.27
20260512,22.75,23.25,21.15,21.5,1558000,18.93,13.58,18.37,17.73,1.56
20260513,21.75,22.1,21.05,21.75,1131000,19.16,13.49,18.62,17.77,1.08
20260514,21.8,21.95,20.5,21.8,1258000,19.38,12.46,18.9,17.82,1.15
20260515,21.6,22,21.15,21.15,705000,19.53,8.29,19.14,17.86,0.62
20260518,20.8,22,20.8,21.75,353000,19.72,10.32,19.43,17.92,0.31
20260519,21.75,21.9,21.15,21.7,357000,19.88,9.15,19.71,17.97,0.31
20260520,21.7,22.5,21.4,22.3,959000,20.08,11.04,20.04,18.05,0.8
20260521,24.5,24.5,23.65,24.5,7518000,20.45,19.8,20.47,18.15,4.81
20260522,24.7,26.95,24.1,26.65,26000,20.97,27.1,21.03,18.3,0.02
20260525,27.4,29.3,27.4,29.3,29000,21.66,35.26,21.64,18.49,0.02
20260526,30.95,32.2,30,32.2,32000,22.54,42.86,22.32,18.73,0.02
20260527,31.55,34.6,31.55,33.6,33000,23.46,43.21,23.03,18.99,0.03
20260528,32.9,33.9,32.7,33,1240720,24.26,36.05,23.72,19.24,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.08
- over_600_ratio: 47.44
- over_800_ratio: 37.02
- over_1000_ratio: 35.55
- over_400_change_1w: -3.06
- over_800_change_1w: -2.33
- over_1000_change_1w: -2.33
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.81,,40.06,,38.59,,0,False,False
20260508,58.14,0.33,39.67,-0.39,36.65,-1.94,1,False,False
20260515,59.14,1,39.35,-0.32,37.88,1.23,2,False,True
20260522,56.08,-3.06,37.02,-2.33,35.55,-2.33,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2061 | 風青 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 55.0 |  |  | neckline_challenge |  |  | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260521 | 2061 | 風青 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  |  | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2061 | 風青 | 6 | 6 | 5 | 6 | 6 | continued_overheated | 連續上榜但短期漲幅或乖離過熱，精華追蹤應降級。 |

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
