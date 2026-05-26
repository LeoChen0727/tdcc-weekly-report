# INDIVIDUAL STOCK CHATGPT PACKET - 8917 欣泰

## Metadata
- generated_at: 2026-05-26 23:55:14 Asia/Taipei
- stock_id: 8917
- stock_name: 欣泰
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 113
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8917_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8917_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8917_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8917_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8917_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8917_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8917_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8917_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8917_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8917_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8917_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8917_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8917_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8917_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8917_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8917_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8917_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8917_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8917.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8917.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8917.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8917.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8917.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8917.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8917_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8917_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8917_latest.md?ref=main

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
- open: 52.1
- high: 53
- low: 52.1
- close: 52.1
- volume: 53000
- ma5: 52.7
- ema23_primary: 52.87
- distance_to_ema23_pct: -1.45
- ma20: 52.76
- ma60: 54.54
- ma120: 56.05
- return_5d: 1.17
- return_20d: 0.97
- volume_ratio: 1.69
- distance_to_ma20_pct_auxiliary: -1.25
- distance_to_high_60_pct: -24.82

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260424,51.6,53,51.6,53,49000,53.59,-1.1,53.26,55.9,1.63
20260427,53.4,53.4,52,52,36000,53.46,-2.72,53.1,55.81,1.18
20260428,52.5,53.3,52.1,53.3,15000,53.44,-0.27,53.02,55.75,0.51
20260430,55,55,52.3,52.3,31000,53.35,-1.96,52.87,55.68,1.03
20260504,51.9,54,51.6,52.8,62000,53.3,-0.94,52.76,55.61,1.9
20260505,52.5,54,52.5,53.4,9000,53.31,0.17,52.69,55.55,0.28
20260506,52.5,53.5,52.5,53.3,18000,53.31,-0.02,52.72,55.48,0.76
20260507,53,54.1,52.3,52.3,21000,53.23,-1.74,52.7,55.4,0.87
20260508,53.3,54.3,53.3,53.6,18000,53.26,0.65,52.74,55.34,0.72
20260511,53.6,53.6,52.6,52.7,3000,53.21,-0.96,52.73,55.26,0.12
20260512,54.3,54.5,52.5,52.7,50000,53.17,-0.88,52.7,55.19,1.97
20260513,52.6,53.6,52.6,53,4000,53.15,-0.29,52.7,55.12,0.16
20260515,53.4,53.4,53.2,53.2,4000,53.16,0.08,52.72,55.07,0.16
20260518,53.2,53.4,51.6,52.6,33000,53.11,-0.96,52.66,55,1.42
20260519,52.5,52.5,51.5,51.5,51000,52.98,-2.79,52.61,54.91,2.04
20260520,52.6,52.9,51.6,52.8,42000,52.96,-0.31,52.61,54.85,1.59
20260521,52.9,53,52.9,53,23000,52.97,0.07,52.63,54.78,0.87
20260522,53.7,53.7,52.8,53.1,53000,52.98,0.23,52.7,54.7,1.89
20260525,52.3,53.3,52.3,52.5,53000,52.94,-0.82,52.73,54.62,1.77
20260526,52.1,53,52.1,52.1,53000,52.87,-1.45,52.76,54.54,1.69
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 83.02
- over_600_ratio: 75.99
- over_800_ratio: 70.22
- over_1000_ratio: 66.79
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
20260430,82.98,,70.18,,66.74,,0,False,False
20260508,83.01,0.03,70.21,0.03,66.77,0.03,1,True,True
20260515,83.02,0.01,70.22,0.01,66.78,0.01,2,True,True
20260522,83.02,0,70.22,0,66.79,0.01,3,False,True
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
