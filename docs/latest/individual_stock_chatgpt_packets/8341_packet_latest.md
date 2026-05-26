# INDIVIDUAL STOCK CHATGPT PACKET - 8341 日友

## Metadata
- generated_at: 2026-05-26 23:55:10 Asia/Taipei
- stock_id: 8341
- stock_name: 日友
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8341_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8341_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8341_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8341_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8341_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8341_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8341_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8341_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8341_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8341_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8341_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8341_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8341_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8341_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8341_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8341_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8341_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8341_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8341.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8341.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8341.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8341.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8341.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8341.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8341_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8341_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8341_latest.md?ref=main

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
- open: 75.7
- high: 75.9
- low: 75.4
- close: 75.7
- volume: 164556
- ma5: 76.06
- ema23_primary: 75.86
- distance_to_ema23_pct: -0.21
- ma20: 75.64
- ma60: 76.27
- ma120: 77.67
- return_5d: -0.66
- return_20d: 2.02
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: 0.09
- distance_to_high_60_pct: -5.73

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,74,74.8,74,74.5,182079,75.75,-1.65,75.7,76.8,0.87
20260429,74.5,75.1,74.5,74.8,152968,75.67,-1.15,75.63,76.71,0.73
20260430,75.2,75.2,74.6,74.7,163846,75.59,-1.18,75.56,76.62,0.78
20260504,74.7,75,74.3,74.3,222177,75.48,-1.57,75.47,76.54,1.04
20260505,74.5,74.5,74,74.3,297801,75.39,-1.44,75.37,76.47,1.34
20260506,75.6,76.6,75,75.3,500798,75.38,-0.1,75.34,76.41,2.06
20260507,75.3,75.5,74.7,75.5,334218,75.39,0.15,75.31,76.36,1.32
20260508,75.5,76,74.9,75.8,301182,75.42,0.5,75.3,76.32,1.15
20260511,76.1,76.4,75.8,76.1,201442,75.48,0.82,75.3,76.31,0.76
20260512,76.4,76.8,76.2,76.2,219692,75.54,0.87,75.33,76.31,0.83
20260513,76,76.4,75.7,75.9,143358,75.57,0.44,75.34,76.31,0.54
20260514,76.3,77.6,76.1,76.2,368091,75.62,0.76,75.36,76.32,1.34
20260515,76.9,77.9,76.1,76.5,361429,75.69,1.06,75.36,76.32,1.28
20260518,76.1,76.1,75.5,76.1,188474,75.73,0.49,75.36,76.33,0.67
20260519,76.7,77,76.2,76.2,182067,75.77,0.57,75.42,76.34,0.7
20260520,76.3,76.3,75.6,76,165667,75.79,0.28,75.42,76.36,0.64
20260521,76.1,76.7,75.8,76.7,193062,75.86,1.1,75.47,76.36,0.75
20260522,76.5,76.5,76,76.2,142523,75.89,0.41,75.52,76.34,0.58
20260525,76.2,76.3,75.5,75.7,251067,75.88,-0.23,75.56,76.31,1.03
20260526,75.7,75.9,75.4,75.7,164556,75.86,-0.21,75.64,76.27,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 49.21
- over_600_ratio: 48.38
- over_800_ratio: 46.72
- over_1000_ratio: 46.72
- over_400_change_1w: 0.08
- over_800_change_1w: 0.08
- over_1000_change_1w: 0.08
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.05,,46.57,,45.86,,0,False,False
20260508,49.12,0.07,46.63,0.06,46.63,0.77,1,True,True
20260515,49.13,0.01,46.64,0.01,46.64,0.01,2,True,True
20260522,49.21,0.08,46.72,0.08,46.72,0.08,3,True,True
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
