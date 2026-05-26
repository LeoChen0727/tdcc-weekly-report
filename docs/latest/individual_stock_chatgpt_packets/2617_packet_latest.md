# INDIVIDUAL STOCK CHATGPT PACKET - 2617 台航

## Metadata
- generated_at: 2026-05-26 21:25:10 Asia/Taipei
- stock_id: 2617
- stock_name: 台航
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2617_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2617_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2617_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2617_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2617_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2617_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2617_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2617_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2617_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2617_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2617_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2617_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2617_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2617_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2617_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2617_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2617_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2617_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2617.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2617.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2617.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2617.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2617.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2617.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2617_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2617_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2617_latest.md?ref=main

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
- open: 29
- high: 29.3
- low: 28.9
- close: 29
- volume: 674718
- ma5: 28.99
- ema23_primary: 29.31
- distance_to_ema23_pct: -1.07
- ma20: 29.19
- ma60: 30.37
- ma120: 30.59
- return_5d: 0.52
- return_20d: -1.53
- volume_ratio: 0.96
- distance_to_ma20_pct_auxiliary: -0.66
- distance_to_high_60_pct: -13.04

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,29.5,29.65,29.3,29.65,507504,30.3,-2.16,30.23,30.88,0.75
20260429,29.9,30.05,29.7,29.8,576638,30.26,-1.53,30.21,30.85,0.84
20260430,29.75,29.75,29.35,29.35,642601,30.19,-2.77,30.19,30.82,0.94
20260504,29.35,29.6,29.15,29.2,850802,30.1,-3,30.12,30.79,1.22
20260505,29.15,29.5,29,29.3,470980,30.04,-2.45,30.08,30.75,0.67
20260506,29.7,29.7,29.25,29.5,610139,29.99,-1.64,30.03,30.73,0.84
20260507,29.6,29.95,29.55,29.8,950641,29.98,-0.59,29.99,30.7,1.28
20260508,29.75,29.75,29.3,29.4,1156747,29.93,-1.77,29.94,30.66,1.47
20260511,29.3,29.4,29.2,29.25,968419,29.87,-2.08,29.88,30.63,1.18
20260512,29.25,29.45,29.1,29.1,640272,29.81,-2.37,29.82,30.61,0.78
20260513,29.2,29.35,29.05,29.15,494129,29.75,-2.03,29.77,30.58,0.62
20260514,29.2,29.45,29.1,29.15,493895,29.7,-1.86,29.68,30.55,0.65
20260515,29.15,29.4,28.65,28.65,1414122,29.61,-3.26,29.55,30.52,1.78
20260518,28.6,28.75,28.3,28.75,638129,29.54,-2.68,29.44,30.5,0.8
20260519,28.75,29.05,28.7,28.85,363834,29.49,-2.15,29.38,30.48,0.48
20260520,28.65,29,28.65,28.8,296321,29.43,-2.13,29.31,30.46,0.4
20260521,28.8,29.05,28.6,29.05,777934,29.4,-1.18,29.26,30.44,1.03
20260522,29.05,29.3,28.85,29,624051,29.36,-1.24,29.23,30.42,0.88
20260525,29,29.1,28.6,29.1,879161,29.34,-0.82,29.21,30.4,1.22
20260526,29,29.3,28.9,29,674718,29.31,-1.07,29.19,30.37,0.96
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.97
- over_600_ratio: 59.73
- over_800_ratio: 58.47
- over_1000_ratio: 56.73
- over_400_change_1w: 0.1
- over_800_change_1w: 0.4
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.97,,58.42,,57.09,,0,False,False
20260508,61.97,0,58.6,0.18,57.09,0,1,False,True
20260515,61.87,-0.1,58.07,-0.53,56.76,-0.33,2,False,False
20260522,61.97,0.1,58.47,0.4,56.73,-0.03,3,False,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| status |
| --- |
| no rows |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2617 | 台航 | 4 | 0 | 4900.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
