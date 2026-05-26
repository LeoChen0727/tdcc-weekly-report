# INDIVIDUAL STOCK CHATGPT PACKET - 2924 宏太-KY

## Metadata
- generated_at: 2026-05-26 23:53:33 Asia/Taipei
- stock_id: 2924
- stock_name: 宏太-KY
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 77
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2924_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2924_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2924_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2924_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2924_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2924_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2924_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2924_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2924_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2924_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2924_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2924_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2924_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2924_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2924_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2924_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2924_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2924_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2924.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2924.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2924.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2924.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2924.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2924.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2924_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2924_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2924_latest.md?ref=main

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
- open: 15.1
- high: 15.45
- low: 14.8
- close: 15.2
- volume: 15000
- ma5: 15.72
- ema23_primary: 17.62
- distance_to_ema23_pct: -13.72
- ma20: 18.15
- ma60: 18.88
- ma120: 19.8
- return_5d: -5
- return_20d: -10.59
- volume_ratio: 2.29
- distance_to_ma20_pct_auxiliary: -16.27
- distance_to_high_60_pct: -32.29

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260407,16,17.5,16,17.5,2000,18.83,-7.06,18.88,20.33,0.67
20260408,18,18.6,18,18.6,2000,18.81,-1.11,18.82,20.3,0.66
20260409,19.45,20.45,19.45,20.45,19000,18.95,7.94,18.85,20.31,4.81
20260410,20,20,20,20,3000,19.03,5.07,18.92,20.26,0.85
20260413,19.25,19.25,19.25,19.25,6000,19.05,1.04,18.93,20.1,1.58
20260414,18.75,20,18.7,20,4000,19.13,4.54,18.98,19.96,1.01
20260415,20.45,20.45,20.45,20.45,2000,19.24,6.28,19.06,19.87,0.5
20260417,20.75,20.75,20.75,20.75,3000,19.37,7.14,19.17,19.84,0.77
20260428,18.55,22.45,18.55,22.45,9000,19.62,14.4,19.34,19.82,2.14
20260429,21.55,21.55,21.55,21.55,1000,19.78,8.92,19.48,19.79,0.24
20260512,17.25,17.25,17.25,17.25,1000,19.57,-11.87,19.39,19.7,0.24
20260513,17,17,17,17,1000,19.36,-12.18,19.24,19.59,0.27
20260514,16.7,16.7,16.7,16.7,3000,19.14,-12.73,19.07,19.5,0.8
20260518,16.55,16.7,16.5,16.5,8000,18.92,-12.78,18.89,19.41,1.98
20260519,16,16,16,16,2000,18.67,-14.32,18.69,19.31,0.56
20260520,15.3,16,15.3,16,15000,18.45,-13.29,18.59,19.2,3.49
20260521,16,16.5,15.35,15.85,4000,18.23,-13.08,18.47,19.11,0.9
20260522,16.35,16.35,16.35,16.35,16000,18.08,-9.56,18.34,19.02,3.08
20260525,16.9,16.9,14.75,15.2,15000,17.84,-14.79,18.24,18.94,2.56
20260526,15.1,15.45,14.8,15.2,15000,17.62,-13.72,18.15,18.88,2.29
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 89.72
- over_600_ratio: 87.54
- over_800_ratio: 87.54
- over_1000_ratio: 84.08
- over_400_change_1w: 0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,89.7,,87.54,,84.08,,0,False,False
20260508,89.7,0,87.54,0,84.08,0,0,False,False
20260515,89.71,0.01,87.54,0,84.08,0,1,False,False
20260522,89.72,0.01,87.54,0,84.08,0,2,False,False
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
