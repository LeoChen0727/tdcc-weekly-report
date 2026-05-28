# INDIVIDUAL STOCK CHATGPT PACKET - 2230 泰茂

## Metadata
- generated_at: 2026-05-28 20:18:33 Asia/Taipei
- stock_id: 2230
- stock_name: 泰茂
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2230_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2230_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2230_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2230_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2230_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2230_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2230_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2230_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2230_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2230_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2230_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2230_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2230_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2230_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2230_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2230_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2230_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2230_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2230.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2230.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2230.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2230.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2230.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2230.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2230_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2230_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2230_latest.md?ref=main

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
- open: 28.25
- high: 28.95
- low: 28.2
- close: 28.25
- volume: 28000
- ma5: 28.86
- ema23_primary: 29.74
- distance_to_ema23_pct: -5
- ma20: 29.79
- ma60: 31.12
- ma120: 59.89
- return_5d: -2.42
- return_20d: 5.41
- volume_ratio: 0.06
- distance_to_ma20_pct_auxiliary: -5.15
- distance_to_high_60_pct: -25.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,27.55,27.55,26.75,27,331000,30.81,-12.38,29.78,44.33,0.98
20260504,26.9,28.05,26.9,28.05,365000,30.58,-8.28,29.59,43.29,1.05
20260505,27.85,29,27.85,29,405000,30.45,-4.77,29.48,42.27,1.13
20260506,29.25,31.9,29.25,31.9,734000,30.57,4.34,29.57,41.31,1.96
20260507,33.9,35.05,33.55,35.05,612000,30.95,13.26,29.75,40.42,1.55
20260508,35.75,37.95,33.15,33.85,3374000,31.19,8.54,29.91,39.5,6.1
20260511,32.7,33.15,31.3,31.35,1018000,31.2,0.48,29.97,38.57,1.73
20260512,31.4,32.95,30.65,30.7,591000,31.16,-1.47,29.98,37.59,0.97
20260513,31,31,29.7,29.75,365000,31.04,-4.16,29.94,36.63,0.59
20260514,30.4,30.75,29.8,30.15,287000,30.97,-2.64,29.93,35.69,0.46
20260515,29.85,30.2,29.05,29.05,300000,30.81,-5.71,29.85,34.76,0.48
20260518,28.05,29.35,27.8,28.9,264000,30.65,-5.71,29.79,33.96,0.43
20260519,29.25,29.3,28.75,29,167000,30.51,-4.95,29.71,33.3,0.27
20260520,29,29.15,28.55,28.7,146000,30.36,-5.47,29.62,32.75,0.24
20260521,28.7,29.4,28.7,28.95,234000,30.24,-4.28,29.57,32.3,0.38
20260522,29.65,29.65,28.8,29.5,29000,30.18,-2.26,29.57,31.95,0.05
20260525,29.5,29.8,28.65,28.65,29000,30.05,-4.67,29.55,31.67,0.05
20260526,28.5,30.1,28.1,29.45,29000,30,-1.84,29.64,31.45,0.06
20260527,29.95,29.95,28.45,28.45,29000,29.87,-4.77,29.71,31.28,0.06
20260528,28.25,28.95,28.2,28.25,28000,29.74,-5,29.79,31.12,0.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 46.05
- over_600_ratio: 41.72
- over_800_ratio: 36.65
- over_1000_ratio: 28.7
- over_400_change_1w: 0.37
- over_800_change_1w: 1.41
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.24,,35.15,,27.19,,0,False,False
20260508,45.59,-0.65,35.25,0.1,28.68,1.49,1,False,True
20260515,45.68,0.09,35.24,-0.01,28.67,-0.01,2,False,False
20260522,46.05,0.37,36.65,1.41,28.7,0.03,3,True,True
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
