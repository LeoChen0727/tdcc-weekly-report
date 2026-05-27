# INDIVIDUAL STOCK CHATGPT PACKET - 6512 啟發電

## Metadata
- generated_at: 2026-05-27 21:28:02 Asia/Taipei
- stock_id: 6512
- stock_name: 啟發電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 124
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6512_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6512_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6512_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6512_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6512_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6512_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6512_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6512_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6512_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6512_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6512_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6512_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6512_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6512_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6512_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6512_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6512_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6512_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6512.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6512.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6512.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6512.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6512.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6512.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6512_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6512_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6512_latest.md?ref=main

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
- date: 20260527
- open: 19.55
- high: 19.7
- low: 19.3
- close: 19.3
- volume: 20000
- ma5: 19.33
- ema23_primary: 19.3
- distance_to_ema23_pct: -0
- ma20: 19.18
- ma60: 19.59
- ma120: 20.13
- return_5d: 1.31
- return_20d: 0.78
- volume_ratio: 1.97
- distance_to_ma20_pct_auxiliary: 0.63
- distance_to_high_60_pct: -7.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,19.15,19.15,19.15,19.15,3000,19.57,-2.17,19.6,19.98,0.34
20260429,19.15,19.2,19.05,19.05,4000,19.53,-2.46,19.54,19.95,0.45
20260430,19.15,19.15,19.05,19.05,4000,19.49,-2.26,19.51,19.92,0.45
20260504,18.95,19.1,18.6,18.75,18000,19.43,-3.49,19.45,19.88,1.88
20260505,18.75,19.1,18.75,19,11000,19.39,-2.03,19.41,19.85,1.11
20260506,19,19.1,19,19.1,12000,19.37,-1.39,19.39,19.83,1.17
20260507,19.45,19.45,19.35,19.35,4000,19.37,-0.09,19.38,19.81,0.43
20260508,19.3,19.3,19.3,19.3,2000,19.36,-0.32,19.33,19.78,0.21
20260511,19.3,19.3,19.2,19.2,22000,19.35,-0.77,19.3,19.76,2.13
20260512,19.2,19.2,19.2,19.2,9000,19.34,-0.7,19.29,19.74,0.89
20260513,19.2,19.2,19.2,19.2,1000,19.32,-0.64,19.27,19.72,0.11
20260514,19.2,19.2,19.2,19.2,2000,19.31,-0.59,19.26,19.71,0.23
20260518,19.15,19.15,19.15,19.15,2000,19.3,-0.78,19.24,19.69,0.25
20260519,18.85,19.2,18.85,19.2,10000,19.29,-0.48,19.21,19.68,1.23
20260520,19.2,19.2,19.05,19.05,6000,19.27,-1.15,19.18,19.66,0.74
20260521,19.45,19.45,18.95,18.95,14000,19.25,-1.53,19.14,19.64,1.63
20260522,18.95,19,18.95,19,19000,19.22,-1.17,19.12,19.63,2.09
20260525,18.95,19.85,18.95,19.75,20000,19.27,2.5,19.14,19.62,2.11
20260526,19.75,19.75,19.65,19.65,20000,19.3,1.81,19.17,19.61,2.05
20260527,19.55,19.7,19.3,19.3,20000,19.3,-0,19.18,19.59,1.97
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 35.97
- over_600_ratio: 27.63
- over_800_ratio: 25.21
- over_1000_ratio: 17.58
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,35.99,,25.23,,17.58,,0,False,False
20260508,35.98,-0.01,25.22,-0.01,17.58,0,0,False,False
20260515,35.98,0,25.22,0,17.58,0,0,False,False
20260522,35.97,-0.01,25.21,-0.01,17.58,0,0,False,False
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
