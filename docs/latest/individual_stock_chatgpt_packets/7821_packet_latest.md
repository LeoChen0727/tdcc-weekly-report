# INDIVIDUAL STOCK CHATGPT PACKET - 7821 神數

## Metadata
- generated_at: 2026-05-27 21:28:24 Asia/Taipei
- stock_id: 7821
- stock_name: 神數
- packet_status: partial_rawdata_packet
- latest_price_date: 20260527
- price_rows: 27
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7821_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7821_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7821_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7821_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7821_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7821_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7821_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7821_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7821_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7821_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7821_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7821_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7821_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7821_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7821_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7821_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7821_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7821_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7821.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7821.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7821.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7821.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7821.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7821.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7821_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7821_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7821_latest.md?ref=main

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
- open: 44.5
- high: 44.5
- low: 43.35
- close: 43.35
- volume: 320496
- ma5: 44.14
- ema23_primary: 45.34
- distance_to_ema23_pct: -4.39
- ma20: 44.99
- ma60: 45.57
- ma120: 45.57
- return_5d: -0.46
- return_20d: -8.83
- volume_ratio: 1.02
- distance_to_ma20_pct_auxiliary: -3.64
- distance_to_high_60_pct: -17.74

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,47.8,49.25,47.6,48,885760,49.43,-2.9,47.34,47.34,0.67
20260430,48.1,48.75,46.5,47.7,572314,49.29,-3.22,47.38,47.38,0.46
20260504,48,48.3,47.05,47.3,442291,49.12,-3.71,47.38,47.38,0.38
20260505,47.3,48,47,47.25,405103,48.97,-3.51,47.36,47.36,0.37
20260506,47.6,47.6,46.45,46.65,481242,48.77,-4.36,47.3,47.3,0.46
20260507,46.15,46.4,46,46.05,351723,48.55,-5.14,47.21,47.21,0.36
20260508,46.4,46.55,45,45.45,221168,48.29,-5.88,47.08,47.08,0.24
20260511,45.4,45.4,44.5,44.85,226386,48,-6.57,46.93,46.93,0.26
20260512,44.85,45.65,44.2,44.5,275157,47.71,-6.73,46.78,46.78,0.32
20260513,44.5,45,43.9,44.15,227452,47.41,-6.88,46.63,46.63,0.28
20260514,44.35,44.4,43.35,43.6,299121,47.1,-7.42,46.46,46.46,0.38
20260515,43.65,44.25,43.5,43.5,273508,46.8,-7.04,46.3,46.3,0.36
20260518,43.5,43.5,42.7,43.1,206756,46.49,-7.29,46.14,46.14,0.28
20260519,43.1,44.4,43.1,43.4,154217,46.23,-6.12,45.72,46.01,0.28
20260520,43.6,43.9,43.2,43.55,97944,46.01,-5.34,45.44,45.9,0.22
20260521,43.6,44.2,43.45,43.9,191820,45.83,-4.22,45.17,45.81,0.46
20260522,44,44.6,43.9,44.4,232610,45.71,-2.87,45.1,45.75,0.62
20260525,44.4,44.6,43.8,44.6,252390,45.62,-2.24,45.14,45.71,0.73
20260526,45.25,45.3,44,44.45,150410,45.52,-2.36,45.2,45.66,0.45
20260527,44.5,44.5,43.35,43.35,320496,45.34,-4.39,44.99,45.57,1.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 81.58
- over_600_ratio: 79.38
- over_800_ratio: 77.55
- over_1000_ratio: 75.97
- over_400_change_1w: -0.71
- over_800_change_1w: -1.2
- over_1000_change_1w: -0.44
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,83.03,,78.86,,76.52,,0,False,False
20260508,82.82,-0.21,78.82,-0.04,76.48,-0.04,0,False,False
20260515,82.29,-0.53,78.75,-0.07,76.41,-0.07,0,False,False
20260522,81.58,-0.71,77.55,-1.2,75.97,-0.44,0,False,False
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
