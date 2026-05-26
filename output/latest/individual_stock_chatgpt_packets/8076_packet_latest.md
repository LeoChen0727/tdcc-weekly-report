# INDIVIDUAL STOCK CHATGPT PACKET - 8076 伍豐

## Metadata
- generated_at: 2026-05-26 22:20:43 Asia/Taipei
- stock_id: 8076
- stock_name: 伍豐
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8076_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8076_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8076_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8076_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8076_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8076_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8076_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8076_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8076_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8076_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8076_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8076_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8076_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8076_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8076_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8076_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8076_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8076_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8076.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8076.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8076.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8076.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8076.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8076.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8076_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8076_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8076_latest.md?ref=main

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
- open: 24
- high: 24.2
- low: 23.6
- close: 23.85
- volume: 24000
- ma5: 23.89
- ema23_primary: 23.71
- distance_to_ema23_pct: 0.59
- ma20: 23.57
- ma60: 23.82
- ma120: 23.61
- return_5d: 1.71
- return_20d: 6.71
- volume_ratio: 0.02
- distance_to_ma20_pct_auxiliary: 1.19
- distance_to_high_60_pct: -13.59

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,22.35,22.6,22.3,22.6,370000,23.39,-3.4,23.27,23.76,0.45
20260429,22.6,22.65,22.3,22.6,1153000,23.33,-3.12,23.2,23.74,1.36
20260430,22.6,22.65,22.3,22.35,675000,23.25,-3.86,23.14,23.71,0.79
20260504,22.35,22.6,22.25,22.35,1448000,23.17,-3.55,23.06,23.68,1.59
20260505,22.35,22.75,22.3,22.75,763000,23.14,-1.67,23.02,23.66,0.82
20260506,22.75,22.85,22.35,22.45,1268000,23.08,-2.73,23,23.64,1.33
20260507,22.6,23.7,22.5,23.7,1858000,23.13,2.46,23.01,23.63,1.83
20260508,23.55,23.95,23.2,23.4,1121000,23.15,1.06,23.03,23.62,1.08
20260511,24.85,25,24,24.65,2901000,23.28,5.89,23.06,23.64,2.57
20260512,24.7,24.85,24.1,24.85,1498000,23.41,6.15,23.14,23.67,1.31
20260513,24.55,24.85,24.35,24.5,911000,23.5,4.25,23.21,23.7,0.8
20260514,24.5,25.3,23.9,25.05,3313000,23.63,6.01,23.3,23.73,2.63
20260515,25.05,25.2,23.9,23.9,2052000,23.65,1.05,23.32,23.73,1.55
20260518,23.8,23.9,23.3,23.35,1008000,23.63,-1.17,23.32,23.73,0.75
20260519,23.45,24.1,23.3,23.45,891000,23.61,-0.69,23.34,23.74,0.67
20260520,23.55,23.85,23.4,23.65,656000,23.62,0.15,23.34,23.75,0.5
20260521,23.9,24.2,23.8,24.05,929000,23.65,1.69,23.36,23.77,0.7
20260522,24.15,24.2,23.9,24.05,24000,23.68,1.54,23.43,23.79,0.02
20260525,24.3,24.5,23.85,23.85,24000,23.7,0.64,23.5,23.8,0.02
20260526,24,24.2,23.6,23.85,24000,23.71,0.59,23.57,23.82,0.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 34.24
- over_600_ratio: 31.01
- over_800_ratio: 28.94
- over_1000_ratio: 25.83
- over_400_change_1w: 0.13
- over_800_change_1w: -0.4
- over_1000_change_1w: -0.49
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,33.86,,29.22,,26.76,,0,False,False
20260508,34.4,0.54,29.51,0.29,26.77,0.01,1,True,True
20260515,34.11,-0.29,29.34,-0.17,26.32,-0.45,2,False,False
20260522,34.24,0.13,28.94,-0.4,25.83,-0.49,3,False,False
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
