# INDIVIDUAL STOCK CHATGPT PACKET - 3290 東浦

## Metadata
- generated_at: 2026-05-26 23:01:13 Asia/Taipei
- stock_id: 3290
- stock_name: 東浦
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3290_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3290_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3290_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3290_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3290_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3290_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3290_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3290_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3290_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3290_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3290_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3290_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3290_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3290_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3290_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3290_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3290_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3290_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3290.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3290.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3290.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3290.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3290.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3290.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3290_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3290_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3290_latest.md?ref=main

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
- open: 47.45
- high: 48.9
- low: 46.95
- close: 48.45
- volume: 48000
- ma5: 47.53
- ema23_primary: 47.31
- distance_to_ema23_pct: 2.41
- ma20: 47.28
- ma60: 46.39
- ma120: 45.6
- return_5d: 4.53
- return_20d: -0.92
- volume_ratio: 0.06
- distance_to_ma20_pct_auxiliary: 2.47
- distance_to_high_60_pct: -12.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,48.9,49.6,47.25,47.5,1233000,47.33,0.35,46.91,46.45,1.03
20260429,47.9,49.25,47.2,47.4,892000,47.34,0.13,47.16,46.52,0.73
20260430,47.4,47.7,46.3,46.65,652000,47.28,-1.34,47.45,46.58,0.54
20260504,46.8,48.1,46.6,47.15,772000,47.27,-0.26,47.63,46.65,0.63
20260505,47.25,47.6,47.05,47.4,264000,47.28,0.25,47.88,46.72,0.21
20260506,47.35,48.65,45.75,48.05,1027000,47.35,1.49,48.04,46.73,0.83
20260507,48.5,48.7,46.85,47.05,812000,47.32,-0.57,48.09,46.71,0.66
20260508,46.9,47.3,46.35,46.6,431000,47.26,-1.4,48.16,46.67,0.39
20260511,46.8,48.75,46.8,48.6,848000,47.37,2.59,48.27,46.66,0.76
20260512,49.05,49.05,47.35,47.75,649000,47.4,0.73,48.32,46.67,0.59
20260513,47.9,47.9,46.9,47.5,432000,47.41,0.19,48.19,46.63,0.46
20260514,48.4,49.9,47.7,48.4,2098000,47.49,1.91,48.1,46.61,2.24
20260515,48.45,48.8,44.15,45.05,2949000,47.29,-4.74,47.89,46.54,2.91
20260518,45.1,46.85,44.1,46.5,719000,47.22,-1.53,47.78,46.51,0.7
20260519,46.85,47.3,45.5,46.35,498000,47.15,-1.7,47.72,46.46,0.5
20260520,46.95,46.95,46.15,46.55,288000,47.1,-1.17,47.55,46.42,0.3
20260521,47.1,47.35,46.8,47.25,353000,47.11,0.29,47.39,46.42,0.4
20260522,47.3,48.75,47.15,48.25,48000,47.21,2.21,47.38,46.43,0.06
20260525,48.55,48.85,47.1,47.15,48000,47.2,-0.11,47.3,46.4,0.06
20260526,47.45,48.9,46.95,48.45,48000,47.31,2.41,47.28,46.39,0.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.83
- over_600_ratio: 52.29
- over_800_ratio: 47.03
- over_1000_ratio: 44.99
- over_400_change_1w: -1.31
- over_800_change_1w: -0.12
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.97,,47.23,,45.15,,0,False,False
20260508,55.75,-0.22,47.55,0.32,45.47,0.32,1,False,True
20260515,56.14,0.39,47.15,-0.4,45.07,-0.4,2,False,False
20260522,54.83,-1.31,47.03,-0.12,44.99,-0.08,0,False,False
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
