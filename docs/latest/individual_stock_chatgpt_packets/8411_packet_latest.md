# INDIVIDUAL STOCK CHATGPT PACKET - 8411 福貞-KY

## Metadata
- generated_at: 2026-05-30 23:43:56 Asia/Taipei
- stock_id: 8411
- stock_name: 福貞-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8411_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8411_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8411_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8411_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8411_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8411_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8411_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8411_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8411_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8411_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8411_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8411_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8411_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8411_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8411_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8411_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8411_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8411_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8411.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8411.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8411.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8411.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8411.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8411.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8411_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8411_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8411_latest.md?ref=main

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
- open: 11.8
- high: 12.2
- low: 11.8
- close: 12.2
- volume: 216025
- ma5: 12.03
- ema23_primary: 12.11
- distance_to_ema23_pct: 0.75
- ma20: 12.12
- ma60: 12.21
- ma120: 12.21
- return_5d: 1.67
- return_20d: -0.41
- volume_ratio: 2.14
- distance_to_ma20_pct_auxiliary: 0.66
- distance_to_high_60_pct: -2.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,12.2,12.3,12.05,12.3,87074,12.26,0.31,12.28,12.24,1.08
20260505,12.25,12.25,12,12.05,191361,12.24,-1.58,12.27,12.24,2.16
20260506,12.2,12.2,12.05,12.15,85356,12.24,-0.7,12.27,12.24,0.99
20260507,12.15,12.35,12.05,12.35,91423,12.25,0.85,12.27,12.25,1.1
20260508,12.35,12.35,12.15,12.25,63145,12.25,0.03,12.26,12.26,0.76
20260511,12.2,12.25,12.1,12.25,91402,12.25,0.03,12.26,12.26,1.07
20260512,12.25,12.25,12.05,12.2,79001,12.24,-0.35,12.25,12.26,0.91
20260513,12.1,12.4,12.05,12.4,159211,12.26,1.18,12.25,12.27,1.78
20260514,12.3,12.4,12.2,12.25,89596,12.26,-0.04,12.24,12.27,1.04
20260515,12.15,12.2,12.15,12.2,27218,12.25,-0.41,12.23,12.27,0.32
20260518,12.1,12.1,11.95,12,156445,12.23,-1.88,12.22,12.27,1.79
20260519,12,12,11.9,12,55280,12.21,-1.72,12.2,12.27,0.63
20260520,12,12,11.85,11.85,72287,12.18,-2.71,12.18,12.26,0.82
20260521,11.9,12,11.9,12,42369,12.17,-1.36,12.17,12.26,0.48
20260522,12,12.1,11.9,12,27820,12.15,-1.25,12.17,12.24,0.33
20260525,11.9,12.1,11.85,12.1,52929,12.15,-0.39,12.16,12.24,0.65
20260526,12.1,12.1,11.95,12,50864,12.14,-1.11,12.15,12.23,0.64
20260527,12,12.05,11.85,12.05,179494,12.13,-0.64,12.14,12.23,2.13
20260528,12.05,12.05,11.8,11.8,198868,12.1,-2.48,12.12,12.21,2.14
20260529,11.8,12.2,11.8,12.2,216025,12.11,0.75,12.12,12.21,2.14
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 81.62
- over_600_ratio: 81.16
- over_800_ratio: 79.88
- over_1000_ratio: 78.66
- over_400_change_1w: 0.07
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,81.42,,79.76,,78.54,,0,False,False
20260508,81.47,0.05,79.81,0.05,78.59,0.05,1,True,True
20260515,81.54,0.07,79.88,0.07,78.66,0.07,2,True,True
20260522,81.55,0.01,79.89,0.01,78.67,0.01,3,True,True
20260529,81.62,0.07,79.88,-0.01,78.66,-0.01,4,False,False
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
