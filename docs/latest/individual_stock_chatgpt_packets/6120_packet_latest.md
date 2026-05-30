# INDIVIDUAL STOCK CHATGPT PACKET - 6120 達運

## Metadata
- generated_at: 2026-05-30 23:42:49 Asia/Taipei
- stock_id: 6120
- stock_name: 達運
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 266
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6120_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6120_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6120_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6120_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6120_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6120_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6120_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6120_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6120_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6120_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6120_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6120_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6120_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6120_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6120_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6120_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6120_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6120_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6120.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6120.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6120.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6120.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6120.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6120.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6120_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6120_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6120_latest.md?ref=main

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
- open: 14.05
- high: 14.45
- low: 13.85
- close: 14.35
- volume: 4929934
- ma5: 14.23
- ema23_primary: 13.6
- distance_to_ema23_pct: 5.53
- ma20: 13.34
- ma60: 13.42
- ma120: 13.09
- return_5d: -2.38
- return_20d: 12.11
- volume_ratio: 1.05
- distance_to_ma20_pct_auxiliary: 7.59
- distance_to_high_60_pct: -8.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,12.85,13,12.65,12.65,2622334,13.57,-6.79,13.88,13.35,0.41
20260505,12.75,13.2,12.75,13,3423101,13.52,-3.87,13.89,13.33,0.54
20260506,13.2,13.3,12.85,13.05,2710860,13.48,-3.22,13.91,13.33,0.42
20260507,13.15,13.45,13.05,13.3,3077645,13.47,-1.25,13.9,13.33,0.49
20260508,13.45,13.75,12.85,12.9,4290593,13.42,-3.89,13.82,13.32,0.83
20260511,12.95,13.1,12.7,12.8,2855177,13.37,-4.26,13.76,13.32,0.62
20260512,12.95,13.3,12.8,13.05,4237194,13.34,-2.2,13.69,13.33,0.93
20260513,13.05,13.15,12.75,12.95,2607759,13.31,-2.71,13.58,13.33,0.64
20260514,13.15,13.25,12.7,12.95,3537449,13.28,-2.49,13.46,13.32,0.92
20260515,13.05,13.4,12.5,12.6,4071072,13.22,-4.72,13.34,13.31,1.12
20260518,12.55,12.75,12.25,12.75,1959042,13.18,-3.29,13.24,13.3,0.56
20260519,12.8,13.1,12.6,12.65,1982818,13.14,-3.73,13.14,13.3,0.57
20260520,12.8,12.85,12.5,12.85,1807342,13.12,-2.02,13.05,13.31,0.54
20260521,12.9,13.5,12.9,13.4,5778820,13.14,1.99,13,13.32,1.68
20260522,13.4,14.7,13.4,14.7,13984511,13.27,10.78,13.06,13.35,3.65
20260525,15,15.55,14.85,15.15,11824535,13.43,12.84,13.18,13.38,2.79
20260526,15.3,15.35,13.85,14,8405416,13.47,3.91,13.22,13.39,1.9
20260527,14.1,14.3,13.55,13.9,4557108,13.51,2.89,13.24,13.39,1.01
20260528,13.95,14.6,13.65,13.75,5365705,13.53,1.63,13.26,13.39,1.15
20260529,14.05,14.45,13.85,14.35,4929934,13.6,5.53,13.34,13.42,1.05
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 60.64
- over_600_ratio: 58.64
- over_800_ratio: 57.35
- over_1000_ratio: 56.18
- over_400_change_1w: 0.89
- over_800_change_1w: 0.86
- over_1000_change_1w: 0.85
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.01,,56.29,,54.62,,0,False,False
20260508,59.78,-0.23,56.31,0.02,54.34,-0.28,1,False,True
20260515,59.57,-0.21,55.73,-0.58,54.53,0.19,2,False,True
20260522,59.75,0.18,56.49,0.76,55.33,0.8,3,True,True
20260529,60.64,0.89,57.35,0.86,56.18,0.85,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260530 | 6120 | 達運 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_inflow | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d |
| 20260521 | 6120 | 達運 | pattern | 型態觀察 |  |  |  | 接近突破型 |  | call_inflow | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260530 | 6120 | 達運 | 8 | 8 | 5 | 8 | 8 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 6120 | 達運 | 8 | 0 | 1201270.0 | 0.0 |  | call_inflow | 1 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
