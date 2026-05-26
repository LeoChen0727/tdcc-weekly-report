# INDIVIDUAL STOCK CHATGPT PACKET - 1456 怡華

## Metadata
- generated_at: 2026-05-26 23:52:55 Asia/Taipei
- stock_id: 1456
- stock_name: 怡華
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1456_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1456_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1456_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1456_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1456_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1456_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1456_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1456_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1456_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1456_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1456_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1456_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1456_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1456_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1456_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1456_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1456_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1456_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1456.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1456.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1456.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1456.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1456.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1456.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1456_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1456_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1456_latest.md?ref=main

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
- open: 12.95
- high: 13.1
- low: 12.5
- close: 13
- volume: 172177
- ma5: 12.93
- ema23_primary: 13.44
- distance_to_ema23_pct: -3.25
- ma20: 13.44
- ma60: 13.77
- ma120: 13.42
- return_5d: -1.89
- return_20d: -2.62
- volume_ratio: 1.91
- distance_to_ma20_pct_auxiliary: -3.27
- distance_to_high_60_pct: -19.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,13.6,13.6,13.15,13.45,51101,14.01,-3.99,14.18,13.66,0.45
20260429,13.5,14,13.2,13.7,60100,13.98,-2.02,14.14,13.66,0.53
20260430,13.55,13.95,13.55,13.7,38759,13.96,-1.86,14.15,13.68,0.35
20260504,14.05,14.05,13.3,13.3,22240,13.9,-4.35,14.07,13.68,0.23
20260505,13.4,13.4,13.05,13.15,37352,13.84,-5,14.01,13.68,0.46
20260506,13.4,13.4,12.8,12.95,67030,13.77,-5.94,13.94,13.68,0.84
20260507,13.3,14.2,12.7,14.2,246686,13.8,2.87,13.95,13.7,2.9
20260508,14.45,14.45,13.5,14.2,186586,13.84,2.63,13.96,13.72,2.16
20260511,14.05,14.7,13.95,14.65,468699,13.9,5.36,13.96,13.75,4.55
20260512,14.85,15.1,14.1,14.1,114064,13.92,1.29,13.93,13.76,1.09
20260513,14.1,14.15,13.85,13.85,103468,13.91,-0.46,13.89,13.78,0.97
20260514,14.3,14.3,13.25,13.25,56159,13.86,-4.4,13.83,13.78,0.52
20260515,13,13.45,12.95,13.15,21935,13.8,-4.71,13.75,13.78,0.21
20260518,12.9,13.35,12.9,13.25,21069,13.75,-3.67,13.69,13.79,0.21
20260519,13.25,13.65,13.25,13.25,18451,13.71,-3.37,13.65,13.79,0.19
20260520,13.2,13.2,12.95,12.95,34304,13.65,-5.12,13.6,13.79,0.38
20260521,12.95,13.15,12.9,12.9,26383,13.59,-5.05,13.55,13.79,0.3
20260522,12.95,13.25,12.85,12.85,20124,13.53,-4.99,13.5,13.78,0.23
20260525,12.85,13,12.75,12.95,33992,13.48,-3.91,13.46,13.78,0.4
20260526,12.95,13.1,12.5,13,172177,13.44,-3.25,13.44,13.77,1.91
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.98
- over_600_ratio: 84.04
- over_800_ratio: 82.6
- over_1000_ratio: 80.64
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.41,,81.3,,79.34,,0,False,False
20260508,84.5,0.09,81.29,-0.01,79.33,-0.01,1,False,False
20260515,84.98,0.48,82.6,1.31,80.64,1.31,2,True,True
20260522,84.98,0,82.6,0,80.64,0,0,False,False
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
| status |
| --- |
| no rows |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
