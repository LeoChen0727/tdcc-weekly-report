# INDIVIDUAL STOCK CHATGPT PACKET - 3221 台嘉碩

## Metadata
- generated_at: 2026-05-28 19:32:20 Asia/Taipei
- stock_id: 3221
- stock_name: 台嘉碩
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3221_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3221_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3221_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3221_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3221_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3221_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3221_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3221_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3221_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3221_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3221_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3221_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3221_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3221_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3221_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3221_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3221_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3221_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3221.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3221.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3221.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3221.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3221.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3221.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3221_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3221_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3221_latest.md?ref=main

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
- open: 56.9
- high: 62
- low: 56.9
- close: 60.2
- volume: 21252232
- ma5: 58.5
- ema23_primary: 49.14
- distance_to_ema23_pct: 22.52
- ma20: 48.09
- ma60: 40.45
- ma120: 32.37
- return_5d: 17.35
- return_20d: 37.44
- volume_ratio: 2.93
- distance_to_ma20_pct_auxiliary: 25.18
- distance_to_high_60_pct: -2.9

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,44.5,44.5,42.75,42.85,1056000,41.31,3.74,41.88,34.25,0.1
20260504,43.6,44,42.1,43.5,1519000,41.49,4.85,42.12,34.51,0.15
20260505,43.7,44.4,42.7,44.4,1270000,41.73,6.39,42.56,34.79,0.13
20260506,45.8,45.8,43.5,43.9,1579000,41.91,4.74,43.01,35.07,0.17
20260507,44.2,48.2,43.9,48.2,3804000,42.44,13.58,43.61,35.43,0.41
20260508,49.9,53,45,45.2,19072000,42.67,5.94,44.13,35.72,1.91
20260511,45.25,45.4,42,43.8,6538000,42.76,2.43,44.52,35.95,0.65
20260512,43.9,44.95,41.5,43.8,5661000,42.85,2.22,44.72,36.22,0.59
20260513,43.3,45.4,42.25,42.25,5348000,42.8,-1.28,44.95,36.45,0.6
20260514,42.35,44.3,40.85,41.85,4897000,42.72,-2.03,44.96,36.62,0.58
20260515,42.2,43.75,40,40.55,4501000,42.54,-4.67,44.7,36.78,0.59
20260518,40,44.6,39,44.6,7385000,42.71,4.43,44.71,37.06,1.09
20260519,44.75,49,44.2,45.2,23336000,42.92,5.32,44.53,37.34,3.26
20260520,45.05,49.4,45.05,47.9,17978000,43.33,10.54,44.25,37.7,2.54
20260521,50.9,52.1,50,51.3,19727000,44,16.6,44.29,38.11,2.86
20260522,53,56.4,53,56.4,56000,45.03,25.25,44.84,38.6,0.01
20260525,61.8,62,59.2,60.2,61000,46.29,30.04,45.68,39.11,0.01
20260526,59.1,59.4,55.1,59.3,57000,47.38,25.16,46.62,39.6,0.01
20260527,61.7,61.8,56,56.4,57000,48.13,17.18,47.27,40.01,0.01
20260528,56.9,62,56.9,60.2,21252232,49.14,22.52,48.09,40.45,2.93
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 28.55
- over_600_ratio: 21.51
- over_800_ratio: 14.05
- over_1000_ratio: 10.76
- over_400_change_1w: -1.11
- over_800_change_1w: -1.05
- over_1000_change_1w: -0.11
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,31.79,,16.67,,12.61,,0,False,False
20260508,31.44,-0.35,15.61,-1.06,11.44,-1.17,0,False,False
20260515,29.66,-1.78,15.1,-0.51,10.87,-0.57,0,False,False
20260522,28.55,-1.11,14.05,-1.05,10.76,-0.11,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3221 | 台嘉碩 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3221 | 台嘉碩 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

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
