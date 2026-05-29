# INDIVIDUAL STOCK CHATGPT PACKET - 6240 松崗

## Metadata
- generated_at: 2026-05-29 19:33:23 Asia/Taipei
- stock_id: 6240
- stock_name: 松崗
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 127
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6240_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6240_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6240_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6240_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6240_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6240_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6240_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6240_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6240_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6240_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6240_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6240_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6240_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6240_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6240_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6240_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6240_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6240_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6240.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6240.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6240.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6240.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6240.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6240.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6240_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6240_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6240_latest.md?ref=main

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
- open: 17.85
- high: 18.1
- low: 17.65
- close: 17.9
- volume: 18000
- ma5: 17.84
- ema23_primary: 18.1
- distance_to_ema23_pct: -1.09
- ma20: 18.08
- ma60: 18.41
- ma120: 18.66
- return_5d: 1.42
- return_20d: -6.28
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: -1.01
- distance_to_high_60_pct: -13.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,18.85,18.85,18.4,18.8,10000,18.73,0.35,18.68,18.64,0.65
20260505,18.8,18.8,18.8,18.8,1000,18.74,0.32,18.72,18.63,0.07
20260506,18.8,18.8,18,18.6,89000,18.73,-0.68,18.74,18.62,4.65
20260507,18.25,18.55,18.2,18.25,15000,18.69,-2.35,18.72,18.61,0.79
20260508,18.25,18.5,18.25,18.5,8000,18.67,-0.92,18.71,18.6,0.43
20260511,18.1,18.5,18.1,18.5,18000,18.66,-0.85,18.7,18.59,0.95
20260512,18.5,18.5,18.1,18.1,9000,18.61,-2.75,18.69,18.58,0.49
20260513,18.15,18.35,17.9,17.9,48000,18.55,-3.52,18.66,18.57,2.39
20260514,17.9,18.25,17.55,17.85,13000,18.49,-3.48,18.61,18.56,0.64
20260515,17.3,17.9,17.05,17.8,24000,18.44,-3.45,18.58,18.54,1.13
20260518,17.8,18.15,17.8,17.95,8000,18.4,-2.42,18.54,18.52,0.38
20260519,17.95,18.1,17.95,18.1,3000,18.37,-1.47,18.5,18.51,0.14
20260520,18,18,17.85,17.85,2000,18.33,-2.61,18.45,18.49,0.1
20260521,17.9,17.9,17.7,17.8,12000,18.28,-2.64,18.41,18.48,0.7
20260522,17.4,17.8,17.4,17.65,18000,18.23,-3.19,18.36,18.47,1.03
20260525,17.6,18,16.9,17.55,18000,18.17,-3.43,18.3,18.45,1.08
20260526,17.45,18,17.4,17.75,18000,18.14,-2.14,18.24,18.44,1.08
20260527,18.2,18.95,17.9,18.15,18000,18.14,0.06,18.2,18.43,1.04
20260528,18.15,18.35,17.75,17.85,18000,18.12,-1.47,18.14,18.42,1
20260529,17.85,18.1,17.65,17.9,18000,18.1,-1.09,18.08,18.41,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.12
- over_600_ratio: 77.77
- over_800_ratio: 75.04
- over_1000_ratio: 70.93
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.12,,75.04,,70.93,,0,False,False
20260508,82.12,0,75.04,0,70.93,0,0,False,False
20260515,82.12,0,75.04,0,70.93,0,0,False,False
20260522,82.12,0,75.04,0,70.93,0,0,False,False
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
