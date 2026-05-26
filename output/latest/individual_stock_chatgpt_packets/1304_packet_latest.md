# INDIVIDUAL STOCK CHATGPT PACKET - 1304 台聚

## Metadata
- generated_at: 2026-05-26 23:52:50 Asia/Taipei
- stock_id: 1304
- stock_name: 台聚
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 26
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1304_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1304_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1304_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1304_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1304_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1304_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1304_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1304_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1304_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1304_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1304_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1304_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1304_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1304_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1304_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1304_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1304_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1304_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1304.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1304.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1304.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1304.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1304.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1304.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1304_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1304_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1304_latest.md?ref=main

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
- date: 20260526
- open: 12.25
- high: 12.35
- low: 11.95
- close: 12.1
- volume: 4668035
- ma5: 12.19
- ema23_primary: 13.02
- distance_to_ema23_pct: -7.08
- ma20: 12.89
- ma60: 14.09
- ma120: 12.75
- return_5d: -0.41
- return_20d: -12
- volume_ratio: 0.74
- distance_to_ma20_pct_auxiliary: -6.11
- distance_to_high_60_pct: -38.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,13.85,14.25,13.85,14.05,5781581,14.93,-5.87,15.77,13.76,0.19
20260429,14.15,14.5,13.75,13.75,6777063,14.83,-7.27,15.57,13.8,0.24
20260430,14.1,14.5,13.8,14.35,12389103,14.79,-2.97,15.37,13.85,0.53
20260504,13.85,13.95,13.35,13.55,9614007,14.69,-7.73,15.19,13.88,0.46
20260505,13.75,14,13.65,13.8,6822640,14.61,-5.56,14.98,13.9,0.39
20260506,13.65,13.65,13.15,13.2,7910042,14.49,-8.93,14.76,13.92,0.5
20260507,12.85,13.1,12.7,13,10936970,14.37,-9.53,14.61,13.93,0.72
20260508,13.15,13.25,12.7,12.7,5050191,14.23,-10.75,14.45,13.93,0.37
20260511,12.8,13.2,12.8,13.05,4518091,14.13,-7.66,14.3,13.95,0.36
20260512,13,13.1,12.75,12.75,3603088,14.02,-9.04,14.1,13.98,0.32
20260513,13.15,13.15,12.7,13,5639003,13.93,-6.69,13.94,14.01,0.52
20260514,12.85,12.85,12.55,12.75,4595745,13.83,-7.83,13.81,14.03,0.46
20260515,12.8,12.8,12.25,12.25,6115077,13.7,-10.59,13.66,14.04,0.62
20260518,12.65,12.85,12.4,12.45,7720480,13.6,-8.44,13.55,14.06,0.82
20260519,12.4,12.5,12.1,12.15,4163854,13.48,-9.84,13.43,14.07,0.46
20260520,12.15,12.3,11.95,12.15,4632300,13.37,-9.1,13.3,14.08,0.53
20260521,12.1,12.3,12.05,12.25,4599093,13.27,-7.71,13.2,14.09,0.53
20260522,12.25,12.35,12,12.3,5023347,13.19,-6.76,13.08,14.1,0.71
20260525,12.25,12.3,11.85,12.15,5604516,13.11,-7.29,12.97,14.1,0.85
20260526,12.25,12.35,11.95,12.1,4668035,13.02,-7.08,12.89,14.09,0.74
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 60.1
- over_600_ratio: 58.79
- over_800_ratio: 57.82
- over_1000_ratio: 57.23
- over_400_change_1w: 0.11
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.18
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260306,61.03,-0.29,58.7,-0.4,57.4,-0.5,0,False,False
20260313,60.61,-0.42,58.15,-0.55,57.26,-0.14,0,False,False
20260320,61.4,0.79,58.85,0.7,57.9,0.64,1,True,True
20260327,60.32,-1.08,57.97,-0.88,57.46,-0.44,0,False,False
20260402,59.58,-0.74,57.33,-0.64,56.71,-0.75,0,False,False
20260410,59.18,-0.4,56.77,-0.56,56.03,-0.68,0,False,False
20260417,59.48,0.3,57.03,0.26,56.34,0.31,1,True,True
20260424,59.18,-0.3,56.86,-0.17,56.16,-0.18,0,False,False
20260430,59.36,0.18,57.08,0.22,56.56,0.4,1,True,True
20260508,59.82,0.46,57.43,0.35,56.82,0.26,2,True,True
20260515,59.99,0.17,57.73,0.3,57.05,0.23,3,True,True
20260522,60.1,0.11,57.82,0.09,57.23,0.18,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260521 | 1304 | 台聚 | pattern | 型態觀察 |  |  |  | 預備發動型 |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 1304 | 台聚 | 4 | 4 | 4 | 4 | 4 | repeated_but_no_breakout | 近 10 日上榜 4 日、近 20 日上榜 4 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 1304 | 台聚 | 45 | 4 | 1182260.0 | 201040.0 | 5.88 | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
