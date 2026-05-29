# INDIVIDUAL STOCK CHATGPT PACKET - 8277 商丞

## Metadata
- generated_at: 2026-05-29 19:33:59 Asia/Taipei
- stock_id: 8277
- stock_name: 商丞
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8277_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8277_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8277_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8277_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8277_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8277_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8277_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8277_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8277_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8277_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8277_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8277_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8277_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8277_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8277_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8277_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8277_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8277_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8277.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8277.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8277.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8277.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8277.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8277.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8277_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8277_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8277_latest.md?ref=main

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
- date: 20260529
- open: 8.3
- high: 8.61
- low: 8.11
- close: 8.61
- volume: 9000
- ma5: 7.55
- ema23_primary: 7.3
- distance_to_ema23_pct: 17.99
- ma20: 7.15
- ma60: 7.68
- ma120: 8.48
- return_5d: 23
- return_20d: 7.89
- volume_ratio: 0.06
- distance_to_ma20_pct_auxiliary: 20.35
- distance_to_high_60_pct: -7.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,7.25,7.79,7.25,7.5,460000,7.55,-0.67,7.43,8.44,1.61
20260505,7.7,7.7,7.09,7.41,161000,7.54,-1.71,7.41,8.39,0.59
20260506,7.58,7.58,7.31,7.31,141000,7.52,-2.79,7.39,8.35,0.53
20260507,7.52,7.52,7.3,7.3,171000,7.5,-2.69,7.37,8.3,0.64
20260508,7.3,7.5,7,7.1,186000,7.47,-4.93,7.35,8.25,0.72
20260511,7.49,7.49,6.9,7.05,214000,7.43,-5.16,7.32,8.2,0.82
20260512,7.3,7.3,6.95,7.04,214000,7.4,-4.87,7.3,8.16,0.84
20260513,7.04,7.04,6.8,6.83,194000,7.35,-7.11,7.26,8.1,0.75
20260514,6.8,6.8,6.6,6.73,284000,7.3,-7.82,7.22,8.05,1.09
20260515,6.53,6.73,6.52,6.58,157000,7.24,-9.13,7.17,8,0.61
20260518,6.4,6.98,6.4,6.7,61000,7.2,-6.89,7.12,7.96,0.24
20260519,6.7,7,6.7,6.98,149000,7.18,-2.76,7.1,7.92,0.59
20260520,6.86,6.92,6.82,6.83,154000,7.15,-4.46,7.07,7.88,0.61
20260521,6.95,7.07,6.63,6.98,220000,7.13,-2.17,7.05,7.85,0.89
20260522,6.97,7.1,6.84,7,7000,7.12,-1.74,7.03,7.81,0.03
20260525,6.99,7.14,6.99,7.1,7000,7.12,-0.3,7.04,7.77,0.03
20260526,7.1,7.14,7,7.08,7000,7.12,-0.54,7.07,7.74,0.04
20260527,7.1,7.15,7.08,7.12,7000,7.12,0.02,7.09,7.7,0.04
20260528,7.2,7.83,7.2,7.83,8000,7.18,9.09,7.12,7.69,0.05
20260529,8.3,8.61,8.11,8.61,9000,7.3,17.99,7.15,7.68,0.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 19.5
- over_600_ratio: 16.4
- over_800_ratio: 13.48
- over_1000_ratio: 13.48
- over_400_change_1w: 0.46
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,18.94,,13.48,,13.48,,0,False,False
20260508,19.03,0.09,13.48,0,13.48,0,1,False,False
20260515,19.04,0.01,13.48,0,13.48,0,2,False,False
20260522,19.5,0.46,13.48,0,13.48,0,3,False,False
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
