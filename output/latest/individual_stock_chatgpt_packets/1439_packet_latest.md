# INDIVIDUAL STOCK CHATGPT PACKET - 1439 雋揚

## Metadata
- generated_at: 2026-05-26 22:18:04 Asia/Taipei
- stock_id: 1439
- stock_name: 雋揚
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 132
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1439_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1439_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1439_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1439_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1439_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1439_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1439_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1439_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1439_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1439_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1439_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1439_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1439_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1439_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1439_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1439_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1439_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1439_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1439.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1439.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1439.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1439.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1439.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1439.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1439_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1439_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1439_latest.md?ref=main

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
- open: 25.35
- high: 26.3
- low: 25.1
- close: 26
- volume: 147078
- ma5: 25.85
- ema23_primary: 26.23
- distance_to_ema23_pct: -0.88
- ma20: 26.12
- ma60: 27.21
- ma120: 28.09
- return_5d: 2.16
- return_20d: -1.89
- volume_ratio: 2.56
- distance_to_ma20_pct_auxiliary: -0.45
- distance_to_high_60_pct: -13.62

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,26.35,26.65,26.25,26.4,26143,27.36,-3.51,27.32,28.42,0.42
20260428,27,27,26.15,26.35,39000,27.28,-3.4,27.23,28.35,0.6
20260429,26.9,26.9,26,26.65,87034,27.22,-2.11,27.21,28.3,1.32
20260430,27,27,26.4,26.55,40051,27.17,-2.28,27.2,28.24,0.6
20260504,26.2,26.55,26.2,26.55,33725,27.12,-2.09,27.16,28.19,0.5
20260506,26.9,26.9,26.2,26.6,28001,27.07,-1.75,27.12,28.13,0.41
20260507,26.3,26.6,25.85,26.4,21158,27.02,-2.29,27.06,28.08,0.31
20260508,27.3,27.3,26.1,26.85,16658,27,-0.57,27.02,28.03,0.25
20260511,27,27,26.35,26.65,32003,26.97,-1.2,26.96,27.98,0.47
20260512,26.75,26.75,26.3,26.5,13000,26.93,-1.61,26.89,27.92,0.19
20260513,26.35,26.35,26.25,26.25,6170,26.88,-2.34,26.84,27.86,0.09
20260514,26,26.3,25.6,25.6,19293,26.77,-4.37,26.75,27.79,0.52
20260515,25.55,25.7,24.95,24.95,38489,26.62,-6.27,26.59,27.7,1.05
20260518,25,25.75,24.6,25.35,49037,26.51,-4.39,26.49,27.63,1.28
20260519,24.8,25.45,24.8,25.45,242201,26.43,-3.69,26.38,27.56,4.85
20260520,25.6,25.6,25.15,25.5,54134,26.35,-3.22,26.28,27.49,1.07
20260521,25.5,26.2,25.4,25.65,44550,26.29,-2.43,26.21,27.42,1.04
20260522,24.95,26.2,24.95,25.9,169052,26.26,-1.36,26.15,27.35,3.34
20260525,25.55,26.5,25.55,26.2,43234,26.25,-0.2,26.14,27.29,0.85
20260526,25.35,26.3,25.1,26,147078,26.23,-0.88,26.12,27.21,2.56
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.51
- over_600_ratio: 80
- over_800_ratio: 78.56
- over_1000_ratio: 74.64
- over_400_change_1w: -0.4
- over_800_change_1w: -0.99
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.87,,79.51,,74.62,,0,False,False
20260508,84.89,0.02,79.53,0.02,74.62,0,1,False,True
20260515,84.91,0.02,79.55,0.02,74.63,0.01,2,True,True
20260522,84.51,-0.4,78.56,-0.99,74.64,0.01,3,False,True
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
