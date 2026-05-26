# INDIVIDUAL STOCK CHATGPT PACKET - 2482 連宇

## Metadata
- generated_at: 2026-05-26 21:25:05 Asia/Taipei
- stock_id: 2482
- stock_name: 連宇
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2482_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2482_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2482_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2482_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2482_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2482_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2482_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2482_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2482_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2482_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2482_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2482_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2482_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2482_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2482_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2482_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2482_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2482_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2482.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2482.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2482.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2482.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2482.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2482.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2482_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2482_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2482_latest.md?ref=main

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
- open: 16.85
- high: 16.95
- low: 16.6
- close: 16.7
- volume: 95371
- ma5: 16.58
- ema23_primary: 16.68
- distance_to_ema23_pct: 0.13
- ma20: 16.6
- ma60: 16.83
- ma120: 17.21
- return_5d: 1.83
- return_20d: -2.05
- volume_ratio: 0.56
- distance_to_ma20_pct_auxiliary: 0.62
- distance_to_high_60_pct: -9.73

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,16.8,17,16.8,16.95,146267,17.21,-1.53,17.2,17.3,0.7
20260429,17.1,17.1,16.85,16.95,90986,17.19,-1.4,17.19,17.28,0.44
20260430,16.8,17,16.8,16.85,125404,17.16,-1.82,17.19,17.25,0.63
20260504,16.9,16.95,16.65,16.65,209619,17.12,-2.74,17.18,17.22,1.07
20260505,16.7,16.75,16.6,16.75,173970,17.09,-1.98,17.18,17.19,0.88
20260506,16.75,16.75,16.5,16.75,181005,17.06,-1.82,17.18,17.16,0.9
20260507,16.6,16.7,16.55,16.65,175747,17.03,-2.21,17.16,17.13,0.86
20260508,16.55,16.85,16.55,16.7,165268,17,-1.76,17.15,17.1,0.8
20260511,16.6,16.8,16.6,16.75,132444,16.98,-1.35,17.14,17.08,0.64
20260512,16.75,16.75,16.45,16.55,293286,16.94,-2.32,17.12,17.06,1.38
20260513,16.45,16.45,16.25,16.25,178484,16.89,-3.76,17.07,17.04,0.86
20260514,16.25,17.15,16.25,16.35,289580,16.84,-2.91,17.03,17.01,1.36
20260515,16.3,16.5,16.05,16.2,236065,16.79,-3.5,16.98,16.98,1.09
20260518,16.15,16.4,15.95,16.3,135890,16.75,-2.67,16.91,16.96,0.7
20260519,16.3,16.4,16.2,16.4,66911,16.72,-1.9,16.83,16.94,0.35
20260520,16.4,16.4,16.15,16.15,57507,16.67,-3.12,16.74,16.92,0.31
20260521,16.25,16.4,16.2,16.3,94130,16.64,-2.04,16.66,16.89,0.55
20260522,16.15,17,16.15,16.9,281322,16.66,1.43,16.64,16.87,1.65
20260525,17,17.1,16.6,16.85,298883,16.68,1.04,16.61,16.85,1.67
20260526,16.85,16.95,16.6,16.7,95371,16.68,0.13,16.6,16.83,0.56
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 41.36
- over_600_ratio: 38.78
- over_800_ratio: 36.2
- over_1000_ratio: 35.02
- over_400_change_1w: 0.1
- over_800_change_1w: 0.11
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,40.87,,36.21,,35.02,,0,False,False
20260508,40.87,0,36.22,0.01,35.02,0,1,False,True
20260515,41.26,0.39,36.09,-0.13,35.02,0,2,False,False
20260522,41.36,0.1,36.2,0.11,35.02,0,3,False,True
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
