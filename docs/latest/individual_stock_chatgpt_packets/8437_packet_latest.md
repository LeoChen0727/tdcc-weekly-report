# INDIVIDUAL STOCK CHATGPT PACKET - 8437 大地-KY

## Metadata
- generated_at: 2026-05-26 21:26:57 Asia/Taipei
- stock_id: 8437
- stock_name: 大地-KY
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8437_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8437_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8437_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8437_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8437_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8437_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8437_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8437_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8437_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8437_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8437_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8437_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8437_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8437_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8437_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8437_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8437_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8437_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8437.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8437.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8437.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8437.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8437.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8437.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8437_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8437_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8437_latest.md?ref=main

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
- open: 11.4
- high: 11.9
- low: 11.4
- close: 11.75
- volume: 12000
- ma5: 11.83
- ema23_primary: 11.93
- distance_to_ema23_pct: -1.47
- ma20: 11.79
- ma60: 12.72
- ma120: 14.67
- return_5d: 2.17
- return_20d: -8.91
- volume_ratio: 0.2
- distance_to_ma20_pct_auxiliary: -0.38
- distance_to_high_60_pct: -24.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,12.9,12.9,12.5,12.9,49000,12.89,0.05,12.62,14.07,0.49
20260429,12.9,12.95,12.5,12.55,81000,12.87,-2.45,12.62,14,0.78
20260430,12.6,12.6,12.5,12.5,26000,12.83,-2.61,12.61,13.93,0.25
20260504,12.45,12.55,11.8,12,181000,12.77,-5.99,12.58,13.85,1.65
20260505,12,12,11.8,11.8,108000,12.68,-6.97,12.54,13.78,0.95
20260506,11.8,12,11.7,11.7,39000,12.6,-7.16,12.5,13.7,0.34
20260507,11.7,12.1,11.7,11.8,29000,12.54,-5.87,12.46,13.62,0.26
20260508,11.7,12,11.65,11.9,48000,12.48,-4.67,12.43,13.55,0.43
20260511,11.7,11.7,11.55,11.55,50000,12.41,-6.89,12.39,13.48,0.45
20260512,11.55,11.6,11.35,11.4,67000,12.32,-7.48,12.36,13.41,0.62
20260513,11.35,11.8,11.25,11.3,58000,12.24,-7.65,12.31,13.34,0.55
20260514,11.35,11.35,11.15,11.25,73000,12.15,-7.44,12.26,13.26,0.72
20260515,11.25,11.25,11,11.2,69000,12.07,-7.24,12.2,13.17,0.68
20260518,11.55,11.55,11.2,11.4,28000,12.02,-5.14,12.14,13.1,0.28
20260519,11.3,11.6,11.3,11.5,34000,11.98,-3.97,12.1,13.03,0.34
20260520,11.4,11.5,11.35,11.35,38000,11.92,-4.81,11.99,12.96,0.47
20260521,11.35,12.35,11.35,12.05,157000,11.93,0.98,11.94,12.9,2.02
20260522,11.95,12.9,11.85,12.35,12000,11.97,3.19,11.92,12.85,0.17
20260525,12.15,12.5,11.65,11.65,12000,11.94,-2.44,11.85,12.78,0.19
20260526,11.4,11.9,11.4,11.75,12000,11.93,-1.47,11.79,12.72,0.2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 39.3
- over_600_ratio: 32.47
- over_800_ratio: 29.44
- over_1000_ratio: 25.37
- over_400_change_1w: 0.06
- over_800_change_1w: 0.05
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,38.9,,29.16,,25.2,,0,False,False
20260508,39.17,0.27,29.36,0.2,25.36,0.16,1,True,True
20260515,39.24,0.07,29.39,0.03,25.36,0,2,False,True
20260522,39.3,0.06,29.44,0.05,25.37,0.01,3,True,True
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
