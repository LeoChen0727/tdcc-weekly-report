# INDIVIDUAL STOCK CHATGPT PACKET - 3268 海德威

## Metadata
- generated_at: 2026-05-29 19:32:30 Asia/Taipei
- stock_id: 3268
- stock_name: 海德威
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3268_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3268_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3268_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3268_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3268_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3268_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3268_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3268_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3268_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3268_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3268_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3268_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3268_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3268_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3268_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3268_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3268_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3268_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3268.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3268.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3268.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3268.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3268.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3268.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3268_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3268_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3268_latest.md?ref=main

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
- open: 17.8
- high: 18.05
- low: 17.25
- close: 18
- volume: 18000
- ma5: 17.69
- ema23_primary: 17.47
- distance_to_ema23_pct: 3.06
- ma20: 17.66
- ma60: 16.53
- ma120: 16.89
- return_5d: 2.27
- return_20d: 4.65
- volume_ratio: 0.09
- distance_to_ma20_pct_auxiliary: 1.91
- distance_to_high_60_pct: -8.16

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,16.9,17.55,16.9,17.3,68000,16.79,3.02,16.66,16.12,0.35
20260505,17.5,17.6,17.15,17.35,81000,16.84,3.03,16.8,16.12,0.41
20260506,18.1,18.1,17.4,17.7,136000,16.91,4.66,16.95,16.14,0.67
20260507,18.5,19.45,18.3,19.45,1288000,17.12,13.59,17.19,16.18,4.9
20260508,19.45,19.6,18.35,18.35,721000,17.23,6.53,17.4,16.2,2.43
20260511,18.55,18.8,17.8,18.5,197000,17.33,6.74,17.55,16.22,0.66
20260512,18.9,18.9,17.75,17.75,243000,17.37,2.21,17.57,16.24,0.9
20260513,17.85,17.9,17.3,17.35,94000,17.36,-0.09,17.61,16.26,0.39
20260514,17.45,17.85,16.9,16.95,135000,17.33,-2.19,17.64,16.27,0.56
20260515,17.25,18.55,17.25,17.3,457000,17.33,-0.16,17.64,16.28,1.86
20260518,17.55,17.55,17.05,17.3,90000,17.33,-0.15,17.65,16.3,0.37
20260519,17.3,17.8,17.1,17.25,124000,17.32,-0.4,17.67,16.31,0.51
20260520,17.25,17.25,17.1,17.15,64000,17.3,-0.9,17.66,16.33,0.27
20260521,16.9,17.7,16.9,17.5,217000,17.32,1.03,17.63,16.36,0.93
20260522,17.5,17.85,17.5,17.6,18000,17.34,1.47,17.62,16.39,0.08
20260525,17.7,18.7,17.7,18,18000,17.4,3.45,17.62,16.43,0.09
20260526,18.05,18.1,17.3,17.7,18000,17.42,1.58,17.63,16.45,0.09
20260527,17.8,17.85,17.35,17.35,18000,17.42,-0.39,17.63,16.47,0.09
20260528,17.6,18.2,17.35,17.4,18000,17.42,-0.09,17.62,16.5,0.09
20260529,17.8,18.05,17.25,18,18000,17.47,3.06,17.66,16.53,0.09
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 34.75
- over_600_ratio: 29.1
- over_800_ratio: 29.1
- over_1000_ratio: 29.1
- over_400_change_1w: -0.08
- over_800_change_1w: -0.02
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,33.56,,29.12,,29.12,,0,False,False
20260508,34.53,0.97,28.94,-0.18,28.94,-0.18,1,False,False
20260515,34.83,0.3,29.12,0.18,29.12,0.18,2,True,True
20260522,34.75,-0.08,29.1,-0.02,29.1,-0.02,0,False,False
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
