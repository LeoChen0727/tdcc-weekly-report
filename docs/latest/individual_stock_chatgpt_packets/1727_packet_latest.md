# INDIVIDUAL STOCK CHATGPT PACKET - 1727 中華化

## Metadata
- generated_at: 2026-05-28 19:31:40 Asia/Taipei
- stock_id: 1727
- stock_name: 中華化
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1727_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1727_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1727_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1727_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1727_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1727_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1727_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1727_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1727_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1727_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1727_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1727_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1727_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1727_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1727_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1727_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1727_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1727_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1727.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1727.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1727.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1727.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1727.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1727.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1727_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1727_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1727_latest.md?ref=main

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
- open: 96.8
- high: 98
- low: 92.3
- close: 94.2
- volume: 8406055
- ma5: 98.84
- ema23_primary: 84.74
- distance_to_ema23_pct: 11.17
- ma20: 86.02
- ma60: 65.51
- ma120: 54.49
- return_5d: 1.29
- return_20d: 13.22
- volume_ratio: 0.53
- distance_to_ma20_pct_auxiliary: 9.51
- distance_to_high_60_pct: -15.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,81.8,84.6,80.2,81.5,28077140,63.12,29.12,60.8,52.27,2.03
20260504,81,85,80.5,81.5,11580079,64.65,26.06,62.41,52.87,0.81
20260505,82,84.5,78.6,80,11850054,65.93,21.34,64,53.43,0.8
20260506,79.6,80.8,74.8,78.1,9548641,66.95,16.66,65.56,53.96,0.63
20260507,78.2,83,76.6,78.2,9981149,67.88,15.2,66.94,54.49,0.65
20260508,77.4,78.5,71.1,72.3,8658563,68.25,5.93,68.03,54.96,0.55
20260511,72.8,77.6,72.8,76.3,8600152,68.92,10.7,69.06,55.51,0.55
20260512,76.3,80.3,75.3,78.6,9270424,69.73,12.72,70.06,56.13,0.62
20260513,79.6,85,78.6,80,22144848,70.58,13.34,71.16,56.75,1.41
20260514,80,80.6,77.5,79.5,8180752,71.33,11.46,72.28,57.35,0.51
20260515,80.2,87.4,77.1,87.4,21498216,72.67,20.27,73.94,58.1,1.29
20260518,88,90,84,87.7,39662634,73.92,18.64,75.51,58.88,2.16
20260519,88,92.7,85.6,87.5,22201371,75.05,16.59,77.01,59.66,1.16
20260520,87.4,87.8,82.6,84.6,9804791,75.85,11.54,78.29,60.4,0.51
20260521,85.2,93,85.1,93,23469350,77.28,20.35,79.69,61.24,1.2
20260522,94,102,94,102,15109095,79.34,28.57,81.58,62.17,0.83
20260525,109,112,101,104.5,24179813,81.43,28.32,83.27,63.12,1.33
20260526,103,104.5,95.5,97,13293351,82.73,17.25,84.43,63.94,0.79
20260527,97.3,103,95.2,96.5,11971351,83.88,15.05,85.47,64.75,0.73
20260528,96.8,98,92.3,94.2,8406055,84.74,11.17,86.02,65.51,0.53
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.73
- over_600_ratio: 55.29
- over_800_ratio: 54.25
- over_1000_ratio: 52.73
- over_400_change_1w: 3.85
- over_800_change_1w: 4.18
- over_1000_change_1w: 3.39
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.63,,59.91,,57.09,,0,False,False
20260508,59.31,-4.32,54.75,-5.16,53.36,-3.73,0,False,False
20260515,54.88,-4.43,50.07,-4.68,49.34,-4.02,0,False,False
20260522,58.73,3.85,54.25,4.18,52.73,3.39,1,True,True
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
