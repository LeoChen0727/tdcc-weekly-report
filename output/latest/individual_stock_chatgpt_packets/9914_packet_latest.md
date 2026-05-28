# INDIVIDUAL STOCK CHATGPT PACKET - 9914 美利達

## Metadata
- generated_at: 2026-05-28 19:33:56 Asia/Taipei
- stock_id: 9914
- stock_name: 美利達
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9914_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9914_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9914_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9914_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9914_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9914_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9914_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9914_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9914_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9914_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9914_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9914_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9914_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9914_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9914_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9914_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9914_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9914_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9914.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9914.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9914.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9914.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9914.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9914.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9914_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9914_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9914_latest.md?ref=main

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
- open: 65.2
- high: 66
- low: 63.8
- close: 66
- volume: 1319080
- ma5: 66.84
- ema23_primary: 64.53
- distance_to_ema23_pct: 2.28
- ma20: 63.28
- ma60: 64.29
- ma120: 75.09
- return_5d: -5.71
- return_20d: 13.99
- volume_ratio: 0.53
- distance_to_ma20_pct_auxiliary: 4.3
- distance_to_high_60_pct: -10.57

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,57.7,59,57.5,57.9,1026952,61.43,-5.75,60.45,70.52,0.5
20260504,58,59.3,57.6,57.9,901335,61.14,-5.29,60.06,70.01,0.44
20260505,57.9,58.7,57.6,58.2,619505,60.89,-4.42,59.74,69.52,0.32
20260506,58.1,58.1,56,56.4,1736951,60.52,-6.8,59.38,68.98,0.93
20260507,56.2,56.8,55.9,56.1,1679026,60.15,-6.73,59.09,68.48,0.98
20260508,56.2,57.7,55.6,55.7,1574072,59.78,-6.82,58.98,67.97,1.09
20260511,56,58.5,55.5,57.5,1655212,59.59,-3.5,58.88,67.52,1.18
20260512,57.3,59.7,56.7,59.5,2803103,59.58,-0.14,58.81,67.08,2
20260513,59.6,63.4,59,62.9,4887176,59.86,5.08,58.94,66.64,3.12
20260514,63.5,65.6,63,63.8,4035922,60.19,6,59.1,66.28,2.36
20260515,65,70.1,64.6,70.1,7273623,61.01,14.89,59.49,66,3.64
20260518,70,71,67.3,68.4,4717338,61.63,10.99,59.87,65.75,2.18
20260519,68.1,70.6,67.3,68.5,2449898,62.2,10.13,60.26,65.51,1.09
20260520,68.5,69.6,67.5,68.5,1683649,62.73,9.21,60.6,65.28,0.73
20260521,68.6,70.7,68.5,70,2660265,63.33,10.53,61.02,65.08,1.11
20260522,69.6,69.6,67.5,67.8,3290541,63.7,6.43,61.42,64.91,1.34
20260525,68.5,68.9,67.3,68.2,1424014,64.08,6.43,61.95,64.74,0.59
20260526,68.2,68.2,66.1,67.3,1786005,64.35,4.59,62.46,64.59,0.74
20260527,67.4,67.4,64.7,64.9,2068266,64.39,0.79,62.88,64.42,0.84
20260528,65.2,66,63.8,66,1319080,64.53,2.28,63.28,64.29,0.53
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 66.06
- over_600_ratio: 63.38
- over_800_ratio: 62.2
- over_1000_ratio: 56.52
- over_400_change_1w: 1.32
- over_800_change_1w: 1.79
- over_1000_change_1w: 1.82
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,64.32,,60.19,,55.71,,0,False,False
20260508,64.42,0.1,60.34,0.15,54.36,-1.35,1,False,True
20260515,64.74,0.32,60.41,0.07,54.7,0.34,2,True,True
20260522,66.06,1.32,62.2,1.79,56.52,1.82,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 9914 | 美利達 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260521 | 9914 | 美利達 | pattern | 型態觀察 |  |  |  | 接近突破型 |  | no_signal | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 9914 | 美利達 | 6 | 6 | 5 | 6 | 6 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 9914 | 美利達 | 9 | 0 | 160280.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
