# INDIVIDUAL STOCK CHATGPT PACKET - 8489 三貝德

## Metadata
- generated_at: 2026-05-28 20:20:40 Asia/Taipei
- stock_id: 8489
- stock_name: 三貝德
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8489_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8489_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8489_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8489_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8489_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8489_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8489_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8489_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8489_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8489_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8489_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8489_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8489_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8489_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8489_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8489_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8489_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8489_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8489.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8489.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8489.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8489.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8489.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8489.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8489_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8489_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8489_latest.md?ref=main

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
- date: 20260528
- open: 22.75
- high: 23.05
- low: 22.45
- close: 22.7
- volume: 23000
- ma5: 23.31
- ema23_primary: 24.83
- distance_to_ema23_pct: -8.59
- ma20: 24.76
- ma60: 25.54
- ma120: 32.51
- return_5d: -6.97
- return_20d: -16.54
- volume_ratio: 0.23
- distance_to_ma20_pct_auxiliary: -8.31
- distance_to_high_60_pct: -27.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,28,28.05,26.2,26.35,55000,27.08,-2.68,26.85,29.31,0.2
20260504,26,26,25.7,25.85,93000,26.97,-4.17,26.83,29.1,0.38
20260505,25.55,26,25.55,25.85,37000,26.88,-3.83,26.79,28.91,0.16
20260506,25.45,25.6,24.9,25.15,131000,26.74,-5.93,26.71,28.7,0.58
20260507,25.15,25.2,24.75,25.2,59000,26.61,-5.29,26.62,28.49,0.27
20260508,25,25,24.6,24.8,54000,26.46,-6.27,26.58,28.29,0.25
20260511,24.5,25.1,24.5,25,70000,26.34,-5.07,26.56,28.09,0.33
20260512,24.95,25.3,24.75,25,104000,26.22,-4.67,26.55,27.89,0.51
20260513,25,25,24.6,24.8,50000,26.11,-5,26.53,27.67,0.25
20260514,24.8,24.85,24.4,24.55,58000,25.98,-5.49,26.45,27.46,0.3
20260515,24.15,24.65,24.15,24.4,17000,25.85,-5.59,26.34,27.24,0.11
20260518,26.8,26.8,26.8,26.8,231000,25.92,3.38,26.34,27.07,1.37
20260519,26.7,27.15,25.1,25.45,336000,25.89,-1.68,26.23,26.87,2.15
20260520,25.7,25.7,23.05,25,368000,25.81,-3.14,26.05,26.67,2.61
20260521,24.9,25.2,24.15,24.4,178000,25.69,-5.04,25.82,26.46,1.33
20260522,24.35,24.35,23,23.9,24000,25.54,-6.44,25.59,26.25,0.21
20260525,23.9,23.9,23.45,23.55,24000,25.38,-7.2,25.39,26.04,0.23
20260526,23.5,23.75,23.25,23.45,24000,25.22,-7.01,25.2,25.86,0.23
20260527,23.8,23.8,22.95,22.95,23000,25.03,-8.3,24.98,25.69,0.23
20260528,22.75,23.05,22.45,22.7,23000,24.83,-8.59,24.76,25.54,0.23
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.96
- over_600_ratio: 56.07
- over_800_ratio: 51.62
- over_1000_ratio: 45.96
- over_400_change_1w: 0.02
- over_800_change_1w: 0.04
- over_1000_change_1w: 1.64
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.2,,51.49,,44.24,,0,False,False
20260508,58.2,0,51.5,0.01,44.24,0,1,False,True
20260515,56.94,-1.26,51.58,0.08,44.32,0.08,2,False,True
20260522,56.96,0.02,51.62,0.04,45.96,1.64,3,True,True
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
