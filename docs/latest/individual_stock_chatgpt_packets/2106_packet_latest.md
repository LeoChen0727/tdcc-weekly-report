# INDIVIDUAL STOCK CHATGPT PACKET - 2106 建大

## Metadata
- generated_at: 2026-05-28 20:18:32 Asia/Taipei
- stock_id: 2106
- stock_name: 建大
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2106_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2106_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2106_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2106_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2106_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2106_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2106_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2106_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2106_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2106_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2106_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2106_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2106_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2106_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2106_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2106_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2106_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2106_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2106.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2106.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2106.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2106.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2106.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2106.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2106_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2106_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2106_latest.md?ref=main

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
- open: 16.65
- high: 16.8
- low: 16.6
- close: 16.65
- volume: 917141
- ma5: 16.67
- ema23_primary: 17.08
- distance_to_ema23_pct: -2.51
- ma20: 16.96
- ma60: 17.87
- ma120: 18.97
- return_5d: -1.19
- return_20d: -4.86
- volume_ratio: 1.12
- distance_to_ma20_pct_auxiliary: -1.84
- distance_to_high_60_pct: -16.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,17.55,17.6,17.25,17.25,602508,18.09,-4.62,18.19,18.82,0.85
20260504,17.3,17.35,17.05,17.1,934157,18,-5.02,18.11,18.77,1.35
20260505,17.1,17.35,17.05,17.35,378769,17.95,-3.34,18.05,18.71,0.57
20260506,17.4,17.45,17.3,17.35,604721,17.9,-3.07,17.99,18.66,0.92
20260507,17.2,17.5,17.15,17.5,816093,17.87,-2.05,17.95,18.61,1.23
20260508,17.55,17.6,17.2,17.2,602485,17.81,-3.43,17.89,18.56,0.9
20260511,17.2,17.4,17.2,17.35,443409,17.77,-2.37,17.85,18.52,0.66
20260512,17.35,17.35,17.05,17.05,777630,17.71,-3.74,17.79,18.48,1.17
20260513,17.15,17.15,16.95,17.05,711833,17.66,-3.44,17.71,18.45,1.09
20260514,17.05,17.15,16.75,16.85,1169230,17.59,-4.2,17.63,18.4,1.73
20260515,16.85,17,16.6,16.65,915814,17.51,-4.92,17.53,18.36,1.31
20260518,16.65,16.8,16.5,16.8,637183,17.45,-3.73,17.44,18.31,0.9
20260519,16.75,17.05,16.75,16.85,535735,17.4,-3.17,17.36,18.27,0.76
20260520,16.8,16.85,16.6,16.7,579498,17.34,-3.71,17.27,18.22,0.81
20260521,16.8,16.9,16.75,16.85,772786,17.3,-2.61,17.2,18.17,1.08
20260522,16.85,16.9,16.6,16.7,1245216,17.25,-3.2,17.14,18.11,1.72
20260525,16.7,16.7,16.4,16.65,1903748,17.2,-3.21,17.09,18.05,2.41
20260526,16.65,16.85,16.65,16.7,795443,17.16,-2.68,17.05,17.99,1.02
20260527,16.75,16.8,16.55,16.65,980002,17.12,-2.73,17,17.93,1.21
20260528,16.65,16.8,16.6,16.65,917141,17.08,-2.51,16.96,17.87,1.12
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.6
- over_600_ratio: 77.18
- over_800_ratio: 75.94
- over_1000_ratio: 74.8
- over_400_change_1w: -0.2
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.95,,76.16,,74.94,,0,False,False
20260508,79.96,0.01,76.26,0.1,75.03,0.09,1,True,True
20260515,79.8,-0.16,76.09,-0.17,74.88,-0.15,0,False,False
20260522,79.6,-0.2,75.94,-0.15,74.8,-0.08,0,False,False
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
