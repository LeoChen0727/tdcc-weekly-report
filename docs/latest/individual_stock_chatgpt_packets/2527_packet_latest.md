# INDIVIDUAL STOCK CHATGPT PACKET - 2527 宏璟

## Metadata
- generated_at: 2026-05-26 22:18:40 Asia/Taipei
- stock_id: 2527
- stock_name: 宏璟
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2527_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2527_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2527_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2527_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2527_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2527_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2527_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2527_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2527_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2527_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2527_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2527_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2527_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2527_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2527_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2527_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2527_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2527_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2527.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2527.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2527.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2527.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2527.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2527.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2527_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2527_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2527_latest.md?ref=main

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
- open: 35.25
- high: 35.6
- low: 34.8
- close: 35.15
- volume: 436099
- ma5: 34
- ema23_primary: 33.95
- distance_to_ema23_pct: 3.55
- ma20: 34.03
- ma60: 32.57
- ma120: 30.83
- return_5d: 5.71
- return_20d: 0.57
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: 3.29
- distance_to_high_60_pct: -12.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,35,35,34.3,34.4,330184,33.8,1.76,33.89,31.11,0.35
20260429,34.4,34.85,34.4,34.55,263177,33.87,2.02,34.15,31.2,0.27
20260430,34.6,34.6,33.6,34.05,481402,33.88,0.5,34.41,31.27,0.5
20260504,34.2,35.55,34.2,34.85,591127,33.96,2.61,34.64,31.35,0.61
20260505,34.85,34.85,33.9,33.9,555457,33.96,-0.17,34.85,31.42,0.56
20260506,34.5,34.5,33.8,33.9,342629,33.95,-0.15,35.02,31.49,0.34
20260507,33.8,34.8,33.45,34.6,526189,34.01,1.75,35.21,31.57,0.52
20260508,34.9,35.2,33.85,34.65,304090,34.06,1.73,35.39,31.66,0.3
20260511,35.8,36.3,33.35,34.35,1141176,34.08,0.78,35.46,31.75,1.16
20260512,33.55,34.35,33.3,33.7,757097,34.05,-1.03,35.33,31.85,0.87
20260513,33.9,34.1,33.45,34.1,403776,34.06,0.13,35.15,31.94,0.53
20260514,34.1,34.35,33.35,33.35,455690,34,-1.9,34.85,32.02,0.66
20260515,33.55,34.05,33.3,33.3,406434,33.94,-1.88,34.53,32.1,0.62
20260518,33.3,33.7,32.7,33.65,324658,33.91,-0.78,34.38,32.19,0.58
20260519,33.3,33.7,33.1,33.25,119408,33.86,-1.8,34.23,32.26,0.22
20260520,33.05,33.2,32.7,33,231368,33.79,-2.33,34.07,32.31,0.45
20260521,33.15,33.7,33.1,33.35,241061,33.75,-1.19,34,32.37,0.49
20260522,33.35,33.55,33.05,33.55,339236,33.73,-0.55,33.97,32.43,0.73
20260525,33.7,35.1,33.7,34.95,621616,33.84,3.29,34.02,32.5,1.34
20260526,35.25,35.6,34.8,35.15,436099,33.95,3.55,34.03,32.57,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.69
- over_600_ratio: 77.38
- over_800_ratio: 75.12
- over_1000_ratio: 74.45
- over_400_change_1w: 0.17
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.96,,75.73,,74,,0,False,False
20260508,79.76,-0.2,75.68,-0.05,74.01,0.01,1,False,True
20260515,79.52,-0.24,75.11,-0.57,74.44,0.43,2,False,True
20260522,79.69,0.17,75.12,0.01,74.45,0.01,3,True,True
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
