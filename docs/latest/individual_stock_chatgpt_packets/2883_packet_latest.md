# INDIVIDUAL STOCK CHATGPT PACKET - 2883 凱基金

## Metadata
- generated_at: 2026-05-26 23:00:57 Asia/Taipei
- stock_id: 2883
- stock_name: 凱基金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2883_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2883_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2883_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2883_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2883_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2883_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2883_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2883_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2883_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2883_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2883_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2883_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2883_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2883_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2883_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2883_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2883_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2883_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2883.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2883.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2883.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2883.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2883.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2883.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2883_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2883_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2883_latest.md?ref=main

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
- open: 21.6
- high: 21.9
- low: 21.5
- close: 21.55
- volume: 69290986
- ma5: 21.58
- ema23_primary: 21.55
- distance_to_ema23_pct: 0.02
- ma20: 21.82
- ma60: 20.89
- ma120: 19.19
- return_5d: -0.46
- return_20d: 5.12
- volume_ratio: 1.12
- distance_to_ma20_pct_auxiliary: -1.25
- distance_to_high_60_pct: -6.71

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,20.65,21.4,20.55,21.3,77572767,20.56,3.59,20.6,19.88,1.8
20260429,21.4,21.7,21.3,21.7,62206130,20.66,5.05,20.72,19.95,1.42
20260430,21.5,21.6,21.3,21.5,56240224,20.73,3.73,20.83,20.01,1.27
20260504,21.4,21.75,21.3,21.4,81104455,20.78,2.97,20.91,20.07,1.75
20260505,21.5,21.8,21.35,21.8,58189842,20.87,4.47,21,20.13,1.21
20260506,21.95,22.3,21.95,22.2,68298084,20.98,5.82,21.09,20.2,1.39
20260507,22.25,22.8,22,22.45,74881281,21.1,6.39,21.14,20.27,1.55
20260508,22.6,22.95,22.3,22.9,60958656,21.25,7.76,21.22,20.35,1.23
20260511,22.9,23.1,22.8,22.8,41098922,21.38,6.64,21.3,20.43,0.83
20260512,22.8,22.8,21.6,21.6,75956504,21.4,0.94,21.33,20.49,1.46
20260513,21.5,22,21.5,21.95,42152868,21.44,2.36,21.39,20.55,0.83
20260514,22.25,22.9,22.1,22.1,58899047,21.5,2.8,21.45,20.61,1.14
20260515,22.25,22.65,21.75,21.85,56055465,21.53,1.49,21.49,20.67,1.06
20260518,21.7,21.75,21.3,21.35,65259089,21.51,-0.76,21.51,20.72,1.2
20260519,21.4,22.1,21.3,21.65,76513659,21.52,0.58,21.55,20.77,1.34
20260520,21.75,21.85,21.5,21.6,52721982,21.53,0.32,21.6,20.81,0.9
20260521,21.85,21.95,21.4,21.4,61915375,21.52,-0.56,21.63,20.85,1.02
20260522,21.45,21.75,21.25,21.7,43900065,21.54,0.77,21.7,20.87,0.73
20260525,21.8,21.8,21.4,21.65,53325245,21.54,0.49,21.77,20.88,0.88
20260526,21.6,21.9,21.5,21.55,69290986,21.55,0.02,21.82,20.89,1.12
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 66.49
- over_600_ratio: 64.64
- over_800_ratio: 63.42
- over_1000_ratio: 62.55
- over_400_change_1w: -0.13
- over_800_change_1w: -0.14
- over_1000_change_1w: -0.14
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,66.21,,63.03,,62.13,,0,False,False
20260508,66.58,0.37,63.48,0.45,62.61,0.48,1,True,True
20260515,66.62,0.04,63.56,0.08,62.69,0.08,2,True,True
20260522,66.49,-0.13,63.42,-0.14,62.55,-0.14,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2883 | 凱基金 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260521 | 2883 | 凱基金 | pattern | 型態觀察 |  |  |  | 接近突破型 |  | call_inflow | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2883 | 凱基金 | 4 | 4 | 4 | 4 | 4 | repeated_but_no_breakout | 近 10 日上榜 4 日、近 20 日上榜 4 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2883 | 凱基金 | 13 | 0 | 2900460.0 | 0.0 |  | call_inflow | 1 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
