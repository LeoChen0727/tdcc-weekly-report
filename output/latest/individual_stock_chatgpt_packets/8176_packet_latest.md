# INDIVIDUAL STOCK CHATGPT PACKET - 8176 智捷

## Metadata
- generated_at: 2026-05-26 23:02:52 Asia/Taipei
- stock_id: 8176
- stock_name: 智捷
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8176_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8176_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8176_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8176_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8176_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8176_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8176_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8176_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8176_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8176_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8176_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8176_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8176_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8176_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8176_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8176_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8176_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8176_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8176.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8176.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8176.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8176.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8176.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8176.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8176_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8176_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8176_latest.md?ref=main

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
- open: 10.15
- high: 10.2
- low: 10.05
- close: 10.15
- volume: 10000
- ma5: 10.01
- ema23_primary: 10.29
- distance_to_ema23_pct: -1.39
- ma20: 10.21
- ma60: 10.89
- ma120: 10.86
- return_5d: 0.99
- return_20d: -2.87
- volume_ratio: 0.07
- distance_to_ma20_pct_auxiliary: -0.6
- distance_to_high_60_pct: -29.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,10.4,10.5,10.4,10.45,61000,10.91,-4.24,10.85,11.15,0.26
20260429,10.45,10.5,10.4,10.45,27000,10.87,-3.9,10.8,11.14,0.12
20260430,10.45,10.45,10.25,10.3,161000,10.83,-4.86,10.77,11.12,0.73
20260504,10.3,10.35,10.15,10.25,141000,10.78,-4.9,10.71,11.1,0.64
20260505,10.2,10.4,10.15,10.35,71000,10.74,-3.66,10.66,11.09,0.34
20260506,10.25,10.3,10.1,10.3,248000,10.71,-3.79,10.63,11.07,1.24
20260507,10.3,10.3,10.05,10.2,258000,10.66,-4.35,10.58,11.06,1.3
20260508,10.1,10.2,10.05,10.15,196000,10.62,-4.43,10.54,11.04,0.98
20260511,10.45,10.45,10.1,10.25,145000,10.59,-3.21,10.5,11.03,0.72
20260512,10.5,10.75,10.45,10.5,269000,10.58,-0.78,10.49,11.03,1.41
20260513,10.6,10.6,10.2,10.3,207000,10.56,-2.45,10.48,11.02,1.13
20260514,10.5,10.5,10.15,10.3,367000,10.54,-2.25,10.47,11,1.93
20260515,10.5,10.65,10.1,10.15,268000,10.51,-3.38,10.45,10.99,1.37
20260518,10.15,10.15,10,10.15,49000,10.48,-3.11,10.42,10.97,0.26
20260519,10.1,10.1,9.98,10.05,239000,10.44,-3.74,10.39,10.96,1.29
20260520,10.05,10.05,9.85,9.89,198000,10.39,-4.85,10.33,10.94,1.1
20260521,10.1,10.1,9.94,9.98,125000,10.36,-3.67,10.29,10.93,0.7
20260522,10,10.05,9.95,10.05,10000,10.33,-2.75,10.25,10.91,0.06
20260525,10.05,10.15,9.98,10,10000,10.31,-2.97,10.23,10.9,0.06
20260526,10.15,10.2,10.05,10.15,10000,10.29,-1.39,10.21,10.89,0.07
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 34.42
- over_600_ratio: 28.23
- over_800_ratio: 26.32
- over_1000_ratio: 20.1
- over_400_change_1w: -0.08
- over_800_change_1w: 1.23
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,34.98,,26.6,,20.05,,0,False,False
20260508,34.91,-0.07,26.48,-0.12,20.09,0.04,1,False,True
20260515,34.5,-0.41,25.09,-1.39,20.09,0,0,False,False
20260522,34.42,-0.08,26.32,1.23,20.1,0.01,1,False,True
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
