# INDIVIDUAL STOCK CHATGPT PACKET - 1419 新紡

## Metadata
- generated_at: 2026-05-28 20:18:16 Asia/Taipei
- stock_id: 1419
- stock_name: 新紡
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1419_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1419_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1419_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1419_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1419_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1419_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1419_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1419_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1419_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1419_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1419_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1419_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1419_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1419_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1419_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1419_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1419_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1419_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1419.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1419.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1419.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1419.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1419.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1419.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1419_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1419_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1419_latest.md?ref=main

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
- open: 64
- high: 64.3
- low: 62.6
- close: 63.8
- volume: 95061
- ma5: 64.58
- ema23_primary: 63.85
- distance_to_ema23_pct: -0.07
- ma20: 63.95
- ma60: 63.14
- ma120: 67.19
- return_5d: 2.08
- return_20d: 0.31
- volume_ratio: 0.47
- distance_to_ma20_pct_auxiliary: -0.23
- distance_to_high_60_pct: -10.14

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,63.2,64.5,62.8,64.4,131676,63.26,1.8,63.06,65.53,1.3
20260504,64.4,65.4,63.3,64.8,154221,63.39,2.22,63.19,65.33,1.49
20260505,64.3,65.2,62.7,63.1,95948,63.37,-0.42,63.31,65.06,0.91
20260506,64.4,65,62.9,64.3,133902,63.45,1.35,63.47,64.81,1.22
20260507,63.8,64.3,63.5,64.3,77575,63.52,1.23,63.55,64.58,0.74
20260508,64.8,64.8,63.8,64.3,64742,63.58,1.13,63.63,64.37,0.61
20260511,64.1,64.2,63.8,64.1,45169,63.63,0.75,63.71,64.21,0.44
20260512,64.2,64.2,62,62.5,107050,63.53,-1.62,63.7,64.13,1.07
20260513,62.3,64.1,61.6,63.8,101289,63.55,0.39,63.73,64.02,1.04
20260514,63.1,65.3,62.7,62.7,177677,63.48,-1.23,63.67,63.89,1.76
20260515,67.2,68.9,65.5,66.9,834067,63.77,4.91,63.83,63.86,6.03
20260518,65.1,65.5,63.4,63.4,374846,63.74,-0.53,63.8,63.79,2.47
20260519,63.4,64.6,63,63,116464,63.68,-1.06,63.73,63.7,0.78
20260520,62.6,62.6,61.6,62,170989,63.54,-2.42,63.58,63.57,1.12
20260521,62,63.4,62,62.5,90420,63.45,-1.5,63.47,63.42,0.58
20260522,62.5,63,62.1,62.6,133934,63.38,-1.23,63.44,63.31,0.86
20260525,64.7,66.6,64.5,65.9,380392,63.59,3.63,63.62,63.27,2.22
20260526,67.9,71,66.3,66.8,456299,63.86,4.61,63.9,63.27,2.41
20260527,66.9,66.9,63.5,63.8,334670,63.85,-0.08,63.94,63.2,1.65
20260528,64,64.3,62.6,63.8,95061,63.85,-0.07,63.95,63.14,0.47
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 90.54
- over_600_ratio: 89.1
- over_800_ratio: 87.28
- over_1000_ratio: 85.56
- over_400_change_1w: -0.02
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,90.59,,87.57,,85.57,,0,False,False
20260508,90.58,-0.01,87.31,-0.26,85.59,0.02,1,False,True
20260515,90.56,-0.02,87.31,0,85.59,0,0,False,False
20260522,90.54,-0.02,87.28,-0.03,85.56,-0.03,0,False,False
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
