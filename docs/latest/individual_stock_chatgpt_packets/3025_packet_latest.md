# INDIVIDUAL STOCK CHATGPT PACKET - 3025 星通

## Metadata
- generated_at: 2026-05-28 20:18:59 Asia/Taipei
- stock_id: 3025
- stock_name: 星通
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3025_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3025_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3025_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3025_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3025_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3025_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3025_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3025_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3025_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3025_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3025_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3025_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3025_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3025_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3025_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3025_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3025_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3025_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3025.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3025.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3025.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3025.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3025.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3025.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3025_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3025_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3025_latest.md?ref=main

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
- open: 77.2
- high: 79.3
- low: 74.6
- close: 75.5
- volume: 2256619
- ma5: 76.12
- ema23_primary: 66.79
- distance_to_ema23_pct: 13.04
- ma20: 65.36
- ma60: 62.4
- ma120: 62.79
- return_5d: 16.87
- return_20d: 23.37
- volume_ratio: 1.65
- distance_to_ma20_pct_auxiliary: 15.51
- distance_to_high_60_pct: -11.18

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,61.4,61.8,60,60.1,387168,61.7,-2.59,62.26,61.94,0.52
20260504,61,61.4,60,61,425388,61.64,-1.04,62.4,61.77,0.56
20260505,61,62.9,60.6,62.9,565287,61.74,1.87,62.67,61.61,0.73
20260506,64,64.9,62.9,64.9,1125793,62.01,4.67,62.8,61.45,1.47
20260507,65.6,65.6,62.8,63.5,1232532,62.13,2.2,62.76,61.24,1.64
20260508,63.7,66.2,62.8,63.3,1119876,62.23,1.72,62.7,61.02,1.48
20260511,63.6,63.6,62.5,62.8,590233,62.28,0.84,62.59,60.91,0.8
20260512,64.5,64.5,62.7,62.9,492785,62.33,0.92,62.59,60.86,0.68
20260513,63.9,63.9,61.1,61.8,683524,62.28,-0.78,62.53,60.76,0.94
20260514,63.2,63.2,60.8,60.8,545627,62.16,-2.19,62.38,60.65,0.76
20260515,61.9,61.9,60.3,60.3,499515,62.01,-2.75,62.23,60.53,0.7
20260518,58.7,60.2,58.5,60,341758,61.84,-2.97,62.01,60.51,0.5
20260519,60,60.6,58,58.5,519452,61.56,-4.97,61.71,60.54,0.78
20260520,58.8,60.3,58.4,59.2,409424,61.36,-3.53,61.45,60.59,0.63
20260521,60.6,64.6,59.6,64.6,1337422,61.63,4.81,61.47,60.77,1.93
20260522,71,71,70.8,71,2775275,62.41,13.76,61.98,61.03,3.68
20260525,78.1,78.1,77.7,78.1,2240145,63.72,22.57,62.92,61.4,2.68
20260526,85,85,74.2,78.8,7419415,64.98,21.27,63.84,61.8,6.31
20260527,79.9,79.9,76.3,77.2,2305912,66,16.98,64.64,62.11,1.82
20260528,77.2,79.3,74.6,75.5,2256619,66.79,13.04,65.36,62.4,1.65
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 27.07
- over_600_ratio: 24.52
- over_800_ratio: 17.2
- over_1000_ratio: 12.38
- over_400_change_1w: -0.74
- over_800_change_1w: -0.13
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,29.86,,17.7,,14.31,,0,False,False
20260508,29.15,-0.71,17.25,-0.45,12.38,-1.93,0,False,False
20260515,27.81,-1.34,17.33,0.08,12.38,0,1,False,True
20260522,27.07,-0.74,17.2,-0.13,12.38,0,2,False,False
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
