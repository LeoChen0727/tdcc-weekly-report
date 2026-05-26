# INDIVIDUAL STOCK CHATGPT PACKET - 2102 泰豐

## Metadata
- generated_at: 2026-05-26 21:24:52 Asia/Taipei
- stock_id: 2102
- stock_name: 泰豐
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2102_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2102_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2102_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2102_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2102_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2102_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2102_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2102_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2102_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2102_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2102_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2102_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2102_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2102_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2102_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2102_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2102_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2102_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2102.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2102.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2102.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2102.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2102.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2102.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2102_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2102_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2102_latest.md?ref=main

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
- open: 18.05
- high: 18.2
- low: 17.95
- close: 18.1
- volume: 251315
- ma5: 18.1
- ema23_primary: 18.49
- distance_to_ema23_pct: -2.1
- ma20: 18.43
- ma60: 19.11
- ma120: 19.52
- return_5d: 1.12
- return_20d: -5.24
- volume_ratio: 0.55
- distance_to_ma20_pct_auxiliary: -1.76
- distance_to_high_60_pct: -15.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,19.15,19.2,19,19.15,278616,19.42,-1.4,19.57,19.6,0.56
20260429,19.2,19.35,19,19.15,535763,19.4,-1.28,19.56,19.59,1.06
20260430,19.05,19.1,18.8,18.8,447443,19.35,-2.84,19.52,19.58,0.89
20260504,18.8,18.8,18.55,18.6,479753,19.29,-3.56,19.45,19.56,0.99
20260505,18.6,18.8,18.3,18.5,588516,19.22,-3.75,19.37,19.53,1.22
20260506,18.5,18.6,18.4,18.45,342872,19.16,-3.69,19.29,19.51,0.72
20260507,18.5,18.75,18.25,18.7,482966,19.12,-2.19,19.22,19.48,1.05
20260508,18.8,18.9,18.7,18.8,251028,19.09,-1.53,19.16,19.46,0.55
20260511,18.9,18.9,18.5,18.6,604465,19.05,-2.37,19.09,19.43,1.32
20260512,18.55,18.7,18.45,18.55,649585,19.01,-2.42,19.02,19.41,1.36
20260513,18.45,18.55,18.3,18.35,338439,18.95,-3.19,18.94,19.38,0.73
20260514,18.3,18.5,18.05,18.15,600479,18.89,-3.9,18.89,19.35,1.28
20260515,18.1,18.45,18.05,18.15,459710,18.83,-3.59,18.84,19.32,0.95
20260518,18.05,18.2,17.95,18.15,582664,18.77,-3.3,18.8,19.29,1.18
20260519,18.05,18.15,17.9,17.9,358863,18.7,-4.26,18.73,19.27,0.74
20260520,17.9,17.9,17.7,17.75,505345,18.62,-4.66,18.64,19.24,1.03
20260521,17.75,18.3,17.75,18.3,557696,18.59,-1.57,18.59,19.22,1.11
20260522,18.3,18.5,18.15,18.3,412138,18.57,-1.44,18.53,19.19,0.85
20260525,18.3,18.3,18,18.05,424661,18.52,-2.56,18.48,19.15,0.9
20260526,18.05,18.2,17.95,18.1,251315,18.49,-2.1,18.43,19.11,0.55
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 80.09
- over_600_ratio: 78.36
- over_800_ratio: 77.19
- over_1000_ratio: 75.82
- over_400_change_1w: 0.17
- over_800_change_1w: 0.32
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.75,,76.84,,75.33,,0,False,False
20260508,79.65,-0.1,77.05,0.21,75.56,0.23,1,False,True
20260515,79.92,0.27,76.87,-0.18,75.72,0.16,2,False,True
20260522,80.09,0.17,77.19,0.32,75.82,0.1,3,True,True
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
