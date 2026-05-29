# INDIVIDUAL STOCK CHATGPT PACKET - 3522 御嵿

## Metadata
- generated_at: 2026-05-29 19:32:37 Asia/Taipei
- stock_id: 3522
- stock_name: 御嵿
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3522_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3522_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3522_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3522_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3522_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3522_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3522_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3522_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3522_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3522_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3522_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3522_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3522_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3522_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3522_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3522_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3522_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3522_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3522.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3522.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3522.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3522.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3522.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3522.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3522_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3522_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3522_latest.md?ref=main

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
- open: 11.75
- high: 12
- low: 11.6
- close: 11.75
- volume: 12000
- ma5: 11.97
- ema23_primary: 12.4
- distance_to_ema23_pct: -5.25
- ma20: 12.4
- ma60: 12.93
- ma120: 14.75
- return_5d: -5.24
- return_20d: -6.75
- volume_ratio: 0.13
- distance_to_ma20_pct_auxiliary: -5.28
- distance_to_high_60_pct: -20.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,12.6,12.8,12.1,12.5,143000,12.9,-3.13,12.82,13.91,1.28
20260505,12.7,12.8,12.45,12.5,71000,12.87,-2.87,12.82,13.85,0.64
20260506,12.95,12.95,12.35,12.45,69000,12.83,-3,12.79,13.78,0.62
20260507,12.4,12.5,12.3,12.4,121000,12.8,-3.11,12.77,13.72,1.07
20260508,12.6,12.6,12.3,12.5,73000,12.77,-2.14,12.77,13.66,0.65
20260511,12.2,12.6,12,12.55,398000,12.76,-1.61,12.74,13.61,3.13
20260512,12.2,12.6,12.15,12.55,137000,12.74,-1.48,12.71,13.55,1.08
20260513,12.6,13,12.2,13,247000,12.76,1.88,12.7,13.5,1.83
20260514,13,13,12.45,13,111000,12.78,1.72,12.7,13.46,0.81
20260515,12.9,13.2,12.6,12.65,162000,12.77,-0.93,12.68,13.41,1.19
20260518,12.55,12.55,12.5,12.55,34000,12.75,-1.57,12.65,13.37,0.26
20260519,13,13,12.4,12.4,64000,12.72,-2.53,12.62,13.32,0.52
20260520,12.35,12.75,12.25,12.4,31000,12.69,-2.32,12.59,13.27,0.27
20260521,12.4,12.45,12.4,12.4,47000,12.67,-2.13,12.57,13.23,0.42
20260522,12.25,12.4,12.25,12.4,12000,12.65,-1.96,12.56,13.18,0.11
20260525,12.5,12.5,12.15,12.2,12000,12.61,-3.25,12.53,13.13,0.12
20260526,12.1,12.2,12.05,12.15,12000,12.57,-3.36,12.52,13.09,0.12
20260527,12.4,12.5,11.9,12,12000,12.52,-4.19,12.49,13.03,0.13
20260528,11.8,11.95,11.65,11.75,12000,12.46,-5.7,12.45,12.98,0.13
20260529,11.75,12,11.6,11.75,12000,12.4,-5.25,12.4,12.93,0.13
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.82
- over_600_ratio: 55.86
- over_800_ratio: 53.19
- over_1000_ratio: 52.39
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.28,,53.17,,52.31,,0,False,False
20260508,57.84,-0.44,53.21,0.04,52.35,0.04,1,False,True
20260515,57.82,-0.02,53.19,-0.02,52.38,0.03,2,False,True
20260522,57.82,0,53.19,0,52.39,0.01,3,False,True
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
