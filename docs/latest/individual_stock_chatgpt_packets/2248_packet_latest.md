# INDIVIDUAL STOCK CHATGPT PACKET - 2248 華勝-KY

## Metadata
- generated_at: 2026-05-28 19:31:49 Asia/Taipei
- stock_id: 2248
- stock_name: 華勝-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2248_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2248_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2248_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2248_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2248_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2248_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2248_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2248_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2248_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2248_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2248_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2248_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2248_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2248_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2248_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2248_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2248_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2248_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2248.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2248.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2248.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2248.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2248.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2248.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2248_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2248_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2248_latest.md?ref=main

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
- open: 53.8
- high: 56.3
- low: 53.6
- close: 54.7
- volume: 160927
- ma5: 54.46
- ema23_primary: 54.68
- distance_to_ema23_pct: 0.03
- ma20: 54.97
- ma60: 52.57
- ma120: 50.79
- return_5d: -0.55
- return_20d: -4.7
- volume_ratio: 2.31
- distance_to_ma20_pct_auxiliary: -0.48
- distance_to_high_60_pct: -11.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,56.8,57.1,55.6,56.5,59587,54.38,3.89,53.88,50.44,0.53
20260504,57,57,55,56,75048,54.52,2.72,54.25,50.55,0.65
20260505,55.7,56.3,55.1,55.1,68201,54.57,0.98,54.6,50.65,0.59
20260506,56.4,56.5,53.9,54.5,66592,54.56,-0.11,54.88,50.74,0.56
20260507,54.7,54.7,54.1,54.4,31006,54.55,-0.27,55.13,50.84,0.27
20260508,55.4,56,53.5,55.6,46407,54.63,1.77,55.46,50.97,0.39
20260511,58.7,58.8,57.2,57.8,122767,54.9,5.29,55.92,51.13,0.99
20260512,58,58,54.1,54.1,243381,54.83,-1.33,55.97,51.24,2.14
20260513,53.8,55.3,53.8,54.3,40142,54.79,-0.89,56.02,51.35,0.36
20260514,54.2,54.9,53.2,54.7,47158,54.78,-0.15,56.09,51.47,0.43
20260515,54.4,55.4,53.6,54.1,46249,54.72,-1.14,56.16,51.58,0.42
20260518,54,55,54,54.8,13500,54.73,0.13,56.19,51.72,0.13
20260519,54.9,55,54.4,54.9,138375,54.74,0.28,56.11,51.86,1.33
20260520,55,55.3,54.7,55.2,22150,54.78,0.76,56.09,52,0.22
20260521,54.8,55.3,54.7,55,32102,54.8,0.36,55.97,52.12,0.33
20260522,55.4,55.4,54.4,54.6,48111,54.78,-0.34,55.73,52.22,0.62
20260525,54.6,54.6,53.3,54.2,68927,54.73,-0.98,55.44,52.3,0.94
20260526,54.5,54.8,53.8,54.5,25819,54.72,-0.39,55.23,52.39,0.38
20260527,54.1,54.5,53,54.3,37339,54.68,-0.7,55.1,52.49,0.58
20260528,53.8,56.3,53.6,54.7,160927,54.68,0.03,54.97,52.57,2.31
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.52
- over_600_ratio: 78.42
- over_800_ratio: 77.03
- over_1000_ratio: 71.79
- over_400_change_1w: -0.8
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.32,,77.03,,71.79,,0,False,False
20260508,80.32,0,77.03,0,71.79,0,0,False,False
20260515,80.32,0,77.03,0,71.79,0,0,False,False
20260522,79.52,-0.8,77.03,0,71.79,0,1,False,False
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
