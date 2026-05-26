# INDIVIDUAL STOCK CHATGPT PACKET - 5457 宣德

## Metadata
- generated_at: 2026-05-26 23:01:56 Asia/Taipei
- stock_id: 5457
- stock_name: 宣德
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5457_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5457_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5457_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5457_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5457_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5457_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5457_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5457_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5457_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5457_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5457_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5457_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5457_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5457_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5457_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5457_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5457_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5457_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5457.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5457.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5457.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5457.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5457.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5457.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5457_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5457_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5457_latest.md?ref=main

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
- open: 32.25
- high: 33.2
- low: 31.1
- close: 31.25
- volume: 32000
- ma5: 29.35
- ema23_primary: 33.1
- distance_to_ema23_pct: -5.59
- ma20: 33.66
- ma60: 35.07
- ma120: 37.4
- return_5d: 11.21
- return_20d: -17.11
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: -7.15
- distance_to_high_60_pct: -25.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,37.9,38.55,37.3,37.4,718000,37.32,0.22,37.38,36.27,0.55
20260429,37.35,37.35,36.3,36.7,516000,37.27,-1.52,37.48,36.24,0.39
20260430,36.75,36.9,36.35,36.35,415000,37.19,-2.26,37.59,36.19,0.31
20260504,36.5,37.5,36.2,36.8,498000,37.16,-0.96,37.67,36.15,0.37
20260505,36.8,37.25,36.5,36.95,362000,37.14,-0.51,37.78,36.11,0.27
20260506,37.7,37.7,36.05,36.5,634000,37.09,-1.58,37.87,36.08,0.47
20260507,36.65,37.15,36.25,36.8,469000,37.06,-0.71,37.92,36.06,0.35
20260508,36.8,37.15,36.2,36.25,553000,36.99,-2.01,37.77,36.04,0.5
20260511,36.7,37,35.75,36.4,467000,36.95,-1.48,37.66,36.04,0.47
20260512,37,37,35.55,35.7,711000,36.84,-3.1,37.49,36.04,0.73
20260513,35.7,35.7,34.65,34.7,653000,36.66,-5.35,37.29,36.03,0.68
20260514,34.7,35.1,34.3,34.4,638000,36.47,-5.69,37.1,35.99,0.73
20260515,34.45,34.85,33.3,33.3,785000,36.21,-8.04,36.87,35.92,0.89
20260518,30.1,30.6,30,30,2014000,35.69,-15.95,36.46,35.81,2.17
20260519,29.85,29.85,27.75,28.1,2747000,35.06,-19.85,35.89,35.67,2.77
20260520,28.3,28.95,27.65,27.75,1766000,34.45,-19.45,35.34,35.51,1.72
20260521,28.1,28.8,28.1,28.5,906000,33.95,-16.06,34.77,35.39,0.92
20260522,28.65,29.45,28.5,29.05,29000,33.55,-13.4,34.32,35.27,0.03
20260525,30,30.25,29.2,30.2,30000,33.27,-9.22,33.98,35.16,0.04
20260526,32.25,33.2,31.1,31.25,32000,33.1,-5.59,33.66,35.07,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 55.65
- over_600_ratio: 54.05
- over_800_ratio: 50.94
- over_1000_ratio: 48.73
- over_400_change_1w: -0.74
- over_800_change_1w: -0.42
- over_1000_change_1w: -0.94
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.71,,50.52,,49.69,,0,False,False
20260508,56.85,0.14,50.54,0.02,49.71,0.02,1,True,True
20260515,56.39,-0.46,51.36,0.82,49.67,-0.04,2,False,True
20260522,55.65,-0.74,50.94,-0.42,48.73,-0.94,0,False,False
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
