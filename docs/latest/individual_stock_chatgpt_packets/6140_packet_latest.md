# INDIVIDUAL STOCK CHATGPT PACKET - 6140 訊達

## Metadata
- generated_at: 2026-05-26 21:26:13 Asia/Taipei
- stock_id: 6140
- stock_name: 訊達
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6140_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6140_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6140_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6140_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6140_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6140_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6140_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6140_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6140_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6140_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6140_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6140_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6140_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6140_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6140_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6140_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6140_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6140_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6140.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6140.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6140.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6140.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6140.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6140.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6140_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6140_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6140_latest.md?ref=main

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
- open: 19.9
- high: 20
- low: 19.55
- close: 19.65
- volume: 20000
- ma5: 19.8
- ema23_primary: 19.92
- distance_to_ema23_pct: -1.35
- ma20: 20.08
- ma60: 20.06
- ma120: 23.18
- return_5d: 0.26
- return_20d: 3.69
- volume_ratio: 0.11
- distance_to_ma20_pct_auxiliary: -2.14
- distance_to_high_60_pct: -20.61

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,18.8,19.5,18.6,19,97000,19.27,-1.39,18.62,21.21,0.6
20260429,19,19.35,19,19.1,49000,19.25,-0.8,18.62,21.1,0.31
20260430,19.3,19.3,18.75,19.05,67000,19.24,-0.97,18.64,20.98,0.43
20260504,19.05,19.15,18.8,18.85,69000,19.21,-1.85,18.63,20.86,0.44
20260505,18.85,18.85,18.6,18.65,75000,19.16,-2.66,18.63,20.75,0.48
20260506,19,20.5,18.95,20.5,288000,19.27,6.38,18.76,20.66,1.87
20260507,22.55,22.55,22.55,22.55,290000,19.54,15.38,18.99,20.62,1.83
20260508,24.75,24.75,22.5,23.25,1192000,19.85,17.11,19.27,20.61,5.64
20260511,22.55,22.6,21.55,21.6,413000,20,8.01,19.5,20.59,1.85
20260512,22.1,22.1,20.5,21,244000,20.08,4.57,19.67,20.56,1.07
20260513,20.55,20.6,20.05,20.05,142000,20.08,-0.15,19.79,20.5,0.62
20260514,20.15,20.55,19.9,20.1,95000,20.08,0.1,19.89,20.44,0.41
20260515,20.4,20.4,19.6,19.85,155000,20.06,-1.06,19.93,20.39,0.69
20260518,19.3,20.8,19.3,19.45,134000,20.01,-2.8,19.96,20.35,0.6
20260519,19.55,20.1,19.45,19.6,69000,19.98,-1.88,20,20.31,0.31
20260520,19.45,19.55,19.35,19.35,64000,19.92,-2.88,20,20.27,0.29
20260521,19.35,19.95,19.35,19.75,72000,19.91,-0.8,19.97,20.22,0.35
20260522,19.7,20.4,19.4,20.35,20000,19.95,2.02,20.01,20.17,0.11
20260525,20.1,20.15,19.65,19.9,20000,19.94,-0.21,20.05,20.12,0.11
20260526,19.9,20,19.55,19.65,20000,19.92,-1.35,20.08,20.06,0.11
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.77
- over_600_ratio: 41.96
- over_800_ratio: 39.37
- over_1000_ratio: 34.47
- over_400_change_1w: 0.16
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,45.81,,39.37,,34.47,,0,False,False
20260508,45.75,-0.06,39.37,0,34.47,0,0,False,False
20260515,45.61,-0.14,39.37,0,34.47,0,0,False,False
20260522,45.77,0.16,39.37,0,34.47,0,1,False,False
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
