# INDIVIDUAL STOCK CHATGPT PACKET - 3287 廣寰科

## Metadata
- generated_at: 2026-05-30 23:41:58 Asia/Taipei
- stock_id: 3287
- stock_name: 廣寰科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3287_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3287_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3287_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3287_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3287_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3287_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3287_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3287_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3287_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3287_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3287_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3287_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3287_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3287_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3287_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3287_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3287_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3287_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3287.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3287.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3287.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3287.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3287.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3287.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3287_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3287_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3287_latest.md?ref=main

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
- open: 38.1
- high: 39.4
- low: 37.25
- close: 38
- volume: 38000
- ma5: 35.6
- ema23_primary: 32.18
- distance_to_ema23_pct: 18.08
- ma20: 31.58
- ma60: 29.73
- ma120: 29.71
- return_5d: 19.31
- return_20d: 35.47
- volume_ratio: 0.12
- distance_to_ma20_pct_auxiliary: 20.34
- distance_to_high_60_pct: -4.76

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,28.65,28.65,28.1,28.15,33000,28.64,-1.73,28.67,29.22,0.71
20260505,28.1,28.65,28.1,28.5,46000,28.63,-0.46,28.7,29.18,0.96
20260506,28.5,28.5,28.1,28.1,81000,28.59,-1.71,28.7,29.15,1.6
20260507,28.1,28.5,28.05,28.5,131000,28.58,-0.28,28.71,29.08,2.37
20260508,28.25,28.6,28.25,28.4,51000,28.57,-0.58,28.69,29.03,0.93
20260511,27.7,28.3,27.7,28.05,132000,28.52,-1.66,28.66,28.98,2.2
20260512,30.85,30.85,30.85,30.85,237000,28.72,7.43,28.77,29,3.38
20260513,31.85,33.9,31.85,32.1,3421000,29,10.69,28.93,29.03,14.3
20260514,32.1,32.45,31.35,31.35,687000,29.19,7.38,29.04,29.05,2.54
20260515,31.9,32.9,31.8,32,568000,29.43,8.74,29.17,29.08,1.92
20260518,32.2,32.2,30.8,31.2,305000,29.58,5.49,29.27,29.12,0.99
20260519,31.2,32.7,31,31.85,245000,29.77,7,29.38,29.16,0.78
20260520,32.05,32.3,31.2,31.2,143000,29.89,4.4,29.45,29.19,0.45
20260521,31.5,31.9,31.4,31.45,158000,30.02,4.78,29.57,29.22,0.49
20260522,31.6,32.6,31.6,31.85,32000,30.17,5.57,29.73,29.26,0.1
20260525,32.45,32.8,32.2,32.6,33000,30.37,7.34,29.94,29.31,0.1
20260526,32.6,33.15,32.25,33,33000,30.59,7.88,30.19,29.36,0.1
20260527,33.1,36.3,33.1,36.3,36000,31.07,16.85,30.58,29.46,0.11
20260528,37.5,39.9,37,38.1,39000,31.65,20.37,31.08,29.59,0.12
20260529,38.1,39.4,37.25,38,38000,32.18,18.08,31.58,29.73,0.12
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 59.26
- over_600_ratio: 52.39
- over_800_ratio: 50.95
- over_1000_ratio: 48.76
- over_400_change_1w: 1.09
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.17,,50.95,,48.76,,0,False,False
20260508,58.17,0,50.95,0,48.76,0,0,False,False
20260515,58.2,0.03,50.95,0,48.76,0,1,False,False
20260522,58.17,-0.03,50.95,0,48.76,0,0,False,False
20260529,59.26,1.09,50.95,0,48.76,0,1,False,False
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
