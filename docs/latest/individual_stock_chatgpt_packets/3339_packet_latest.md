# INDIVIDUAL STOCK CHATGPT PACKET - 3339 泰谷

## Metadata
- generated_at: 2026-05-27 21:27:04 Asia/Taipei
- stock_id: 3339
- stock_name: 泰谷
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3339_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3339_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3339_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3339_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3339_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3339_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3339_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3339_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3339_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3339_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3339_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3339_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3339_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3339_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3339_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3339_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3339_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3339_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3339.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3339.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3339.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3339.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3339.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3339.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3339_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3339_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3339_latest.md?ref=main

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
- open: 51.8
- high: 52.5
- low: 48.15
- close: 48.4
- volume: 50000
- ma5: 49.06
- ema23_primary: 50.88
- distance_to_ema23_pct: -4.87
- ma20: 52.4
- ma60: 45.63
- ma120: 36.14
- return_5d: 1.89
- return_20d: -7.81
- volume_ratio: 0.02
- distance_to_ma20_pct_auxiliary: -7.63
- distance_to_high_60_pct: -33.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,50.6,55.8,50.6,54.9,983000,52.21,5.16,53.53,38.07,0.14
20260430,56,57.8,54.8,54.8,1042000,52.42,4.54,54.44,38.48,0.16
20260504,58.4,60,55.5,60,876000,53.05,13.09,55.49,38.98,0.14
20260505,59.9,60.5,57.8,59.8,629000,53.62,11.53,56.52,39.48,0.1
20260506,60,60.2,58.1,59.5,857000,54.11,9.97,57.43,39.96,0.15
20260507,60.5,64,59.2,63.1,677000,54.86,15.03,58.31,40.51,0.13
20260508,64.6,68.8,58.2,58.8,9076000,55.18,6.55,58.91,41.02,1.88
20260511,56.8,57,53,54,4848000,55.09,-1.97,59.28,41.45,1.03
20260512,52.5,54.9,51,52.3,5003000,54.85,-4.66,59.34,41.88,1.11
20260513,51.2,54.5,49,49.35,3962000,54.4,-9.28,59.2,42.23,0.99
20260514,50.2,50.7,48.35,48.75,2691000,53.92,-9.6,58.77,42.58,0.72
20260515,49.15,53,47.6,48.05,3069000,53.44,-10.08,58.03,42.91,0.95
20260518,47.65,47.65,43.6,46.35,2643000,52.84,-12.29,56.88,43.22,1
20260519,46.2,47,43.35,45.45,2745000,52.23,-12.98,55.84,43.51,1.06
20260520,45.5,49,45.5,47.5,2790000,51.83,-8.36,54.64,43.84,1.1
20260521,48.25,49.4,46.6,46.6,2602000,51.4,-9.34,53.52,44.17,1.03
20260522,47.7,51.2,47.7,50.2,50000,51.3,-2.14,52.92,44.55,0.02
20260525,51.5,52,49.15,49.3,50000,51.13,-3.58,52.58,44.91,0.02
20260526,49.65,53.4,49.1,50.8,51000,51.1,-0.6,52.6,45.29,0.02
20260527,51.8,52.5,48.15,48.4,50000,50.88,-4.87,52.4,45.63,0.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 27.76
- over_600_ratio: 24.23
- over_800_ratio: 18.9
- over_1000_ratio: 18.9
- over_400_change_1w: 1.06
- over_800_change_1w: -0.08
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,27.13,,19.4,,19.4,,0,False,False
20260508,27.74,0.61,19.21,-0.19,19.21,-0.19,1,False,False
20260515,26.7,-1.04,18.98,-0.23,18.98,-0.23,0,False,False
20260522,27.76,1.06,18.9,-0.08,18.9,-0.08,1,False,False
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
