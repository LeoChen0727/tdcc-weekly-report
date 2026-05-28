# INDIVIDUAL STOCK CHATGPT PACKET - 4127 天良

## Metadata
- generated_at: 2026-05-28 19:32:37 Asia/Taipei
- stock_id: 4127
- stock_name: 天良
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4127_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4127_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4127_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4127_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4127_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4127_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4127_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4127_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4127_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4127_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4127_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4127_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4127_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4127_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4127_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4127_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4127_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4127_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4127.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4127.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4127.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4127.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4127.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4127.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4127_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4127_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4127_latest.md?ref=main

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
- open: 65.3
- high: 69.2
- low: 65.3
- close: 65.8
- volume: 362581
- ma5: 66.52
- ema23_primary: 51.12
- distance_to_ema23_pct: 28.72
- ma20: 48.86
- ma60: 40.51
- ma120: 36.77
- return_5d: 15.04
- return_20d: 69.81
- volume_ratio: 0.65
- distance_to_ma20_pct_auxiliary: 34.67
- distance_to_high_60_pct: -12.03

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,38.6,38.65,37.4,37.65,53000,37.16,1.31,36.9,37.04,0.66
20260430,38.1,38.95,38,38.35,48000,37.26,2.92,37.02,37.09,0.58
20260504,38.4,38.95,38.05,38.55,85000,37.37,3.16,37.16,37.1,0.98
20260505,38.5,38.65,38.35,38.35,70000,37.45,2.4,37.32,37.07,0.79
20260506,39.9,39.9,38.5,38.75,195000,37.56,3.17,37.47,37.04,2
20260507,38.9,39.5,38.65,39.35,164000,37.71,4.35,37.67,37.03,1.57
20260508,40.5,40.5,39.3,39.8,302000,37.88,5.06,37.9,37.01,2.55
20260511,40.3,43.75,40.3,43.75,1039000,38.37,14.01,38.27,37.05,6.29
20260512,44.65,48.1,44.65,48.1,1366000,39.18,22.76,38.88,37.18,5.91
20260514,48,48,43.3,43.35,3276000,39.53,9.66,39.26,37.28,8.37
20260515,41.25,41.25,39.05,39.1,2595000,39.49,-1,39.43,37.32,5
20260518,40.15,43,40.15,43,358000,39.79,8.08,39.77,37.39,0.67
20260519,47.3,47.3,47.3,47.3,252000,40.41,17.04,40.26,37.52,0.47
20260520,52,52,52,52,474000,41.38,25.67,40.91,37.74,0.87
20260521,57.2,57.2,57.2,57.2,279000,42.7,33.97,41.79,38.06,0.51
20260522,62.9,62.9,54.6,62.9,60000,44.38,41.73,43.05,38.47,0.11
20260525,69.1,69.1,63,69.1,67000,46.44,48.79,44.62,38.99,0.12
20260526,69,74.8,65,68.1,69000,48.25,41.15,46.11,39.52,0.13
20260527,70.5,71.9,65.7,66.7,68000,49.78,33.98,47.51,40.03,0.12
20260528,65.3,69.2,65.3,65.8,362581,51.12,28.72,48.86,40.51,0.65
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.22
- over_600_ratio: 70.22
- over_800_ratio: 62.73
- over_1000_ratio: 59.17
- over_400_change_1w: -0.12
- over_800_change_1w: 2.16
- over_1000_change_1w: 2.16
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.63,,56.4,,54.65,,0,False,False
20260508,67.57,-0.06,56.39,-0.01,54.64,-0.01,0,False,False
20260515,70.34,2.77,60.57,4.18,57.01,2.37,1,True,True
20260522,70.22,-0.12,62.73,2.16,59.17,2.16,2,False,True
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
