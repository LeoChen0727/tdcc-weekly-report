# INDIVIDUAL STOCK CHATGPT PACKET - 8450 霹靂

## Metadata
- generated_at: 2026-05-28 19:33:52 Asia/Taipei
- stock_id: 8450
- stock_name: 霹靂
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8450_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8450_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8450_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8450_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8450_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8450_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8450_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8450_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8450_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8450_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8450_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8450_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8450_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8450_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8450_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8450_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8450_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8450_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8450.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8450.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8450.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8450.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8450.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8450.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8450_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8450_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8450_latest.md?ref=main

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
- open: 15.6
- high: 15.6
- low: 15.3
- close: 15.5
- volume: 73081
- ma5: 15.78
- ema23_primary: 16.1
- distance_to_ema23_pct: -3.73
- ma20: 15.98
- ma60: 16.81
- ma120: 16.97
- return_5d: -2.52
- return_20d: -7.46
- volume_ratio: 1.27
- distance_to_ma20_pct_auxiliary: -3.03
- distance_to_high_60_pct: -17.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,16.75,16.85,16,16.5,80000,17.06,-3.28,17.13,17.15,2.1
20260504,16.45,16.9,16.1,16.2,43000,16.99,-4.64,17.08,17.14,1.14
20260505,16.65,16.65,15.9,16.65,68000,16.96,-1.83,17.03,17.13,1.85
20260506,16.6,16.6,16.1,16.35,46000,16.91,-3.3,17,17.12,1.24
20260507,16.4,16.45,16,16.25,48000,16.85,-3.58,16.95,17.1,1.24
20260508,16.3,16.3,15.9,16,79000,16.78,-4.66,16.9,17.09,1.97
20260511,16.4,16.4,15.8,16,85000,16.72,-4.29,16.84,17.07,1.97
20260512,16,16.3,15.75,16.05,93000,16.66,-3.67,16.75,17.06,2.16
20260513,16.05,16.2,15.7,15.8,61000,16.59,-4.76,16.66,17.04,1.38
20260514,16.05,16.05,15.7,15.8,19000,16.52,-4.38,16.57,17.02,0.43
20260515,16.2,16.2,15.6,15.8,11000,16.46,-4.03,16.49,17,0.25
20260518,16.05,16.05,15.6,15.8,14000,16.41,-3.71,16.41,16.98,0.33
20260519,16,16,15.6,15.7,31000,16.35,-3.97,16.33,16.96,0.73
20260520,15.9,16.4,15.3,16,298000,16.32,-1.96,16.28,16.94,5.23
20260521,16.1,16.15,15.9,15.9,40000,16.29,-2.37,16.22,16.92,0.71
20260522,16.05,16.05,15.8,16,16000,16.26,-1.61,16.18,16.9,0.29
20260525,15.6,16.15,15.5,15.85,16000,16.23,-2.33,16.14,16.88,0.29
20260526,15.45,15.95,15.4,15.8,16000,16.19,-2.42,16.1,16.86,0.29
20260527,16,16.25,15.4,15.75,16000,16.15,-2.51,16.05,16.84,0.29
20260528,15.6,15.6,15.3,15.5,73081,16.1,-3.73,15.98,16.81,1.27
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 59.55
- over_600_ratio: 59.55
- over_800_ratio: 58.33
- over_1000_ratio: 56.66
- over_400_change_1w: -0.02
- over_800_change_1w: -1.24
- over_1000_change_1w: 0.39
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.68,,59.68,,56.27,,0,False,False
20260508,59.67,-0.01,59.67,-0.01,56.27,0,0,False,False
20260515,59.57,-0.1,59.57,-0.1,56.27,0,0,False,False
20260522,59.55,-0.02,58.33,-1.24,56.66,0.39,1,False,True
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
