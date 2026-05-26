# INDIVIDUAL STOCK CHATGPT PACKET - 1413 宏洲

## Metadata
- generated_at: 2026-05-26 23:52:53 Asia/Taipei
- stock_id: 1413
- stock_name: 宏洲
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 132
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1413_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1413_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1413_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1413_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1413_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1413_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1413_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1413_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1413_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1413_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1413_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1413_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1413_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1413_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1413_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1413_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1413_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1413_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1413.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1413.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1413.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1413.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1413.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1413.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1413_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1413_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1413_latest.md?ref=main

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
- open: 9.36
- high: 9.44
- low: 9.31
- close: 9.42
- volume: 50431
- ma5: 9.44
- ema23_primary: 9.54
- distance_to_ema23_pct: -1.31
- ma20: 9.52
- ma60: 9.7
- ma120: 9.85
- return_5d: -0.84
- return_20d: -3.38
- volume_ratio: 1.89
- distance_to_ma20_pct_auxiliary: -1.08
- distance_to_high_60_pct: -8.99

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,9.75,9.75,9.61,9.69,14103,9.78,-0.93,9.81,9.83,0.66
20260429,9.74,9.74,9.4,9.5,22610,9.76,-2.64,9.79,9.82,1.06
20260430,9.57,9.57,9.52,9.53,15929,9.74,-2.14,9.78,9.82,0.75
20260504,9.57,9.6,9.53,9.55,45194,9.72,-1.78,9.77,9.81,1.99
20260505,9.53,9.6,9.53,9.55,23310,9.71,-1.63,9.76,9.81,1.05
20260506,9.61,9.66,9.5,9.65,54351,9.7,-0.55,9.75,9.8,2.25
20260507,9.65,9.65,9.64,9.64,5101,9.7,-0.6,9.73,9.8,0.21
20260508,9.68,9.68,9.44,9.65,12800,9.69,-0.46,9.72,9.79,0.53
20260511,9.5,9.64,9.5,9.63,17220,9.69,-0.61,9.71,9.79,0.74
20260512,9.63,9.63,9.31,9.45,65223,9.67,-2.27,9.69,9.78,2.51
20260513,9.37,9.47,9.37,9.46,16100,9.65,-1.99,9.67,9.77,0.62
20260514,9.33,9.55,9.33,9.47,21200,9.64,-1.73,9.65,9.77,0.84
20260515,9.5,9.5,9.42,9.45,20182,9.62,-1.78,9.63,9.76,0.79
20260518,9.52,9.53,9.36,9.52,70000,9.61,-0.96,9.62,9.75,2.57
20260519,9.5,9.5,9.5,9.5,2116,9.6,-1.07,9.6,9.74,0.08
20260520,9.45,9.5,9.45,9.5,4200,9.59,-0.99,9.58,9.74,0.17
20260521,9.33,9.53,9.33,9.53,20747,9.59,-0.62,9.57,9.73,0.85
20260522,9.52,9.55,9.42,9.42,4528,9.58,-1.62,9.55,9.72,0.19
20260525,9.42,9.42,9.35,9.35,47306,9.56,-2.16,9.54,9.71,1.88
20260526,9.36,9.44,9.31,9.42,50431,9.54,-1.31,9.52,9.7,1.89
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 75.65
- over_600_ratio: 73.49
- over_800_ratio: 72.08
- over_1000_ratio: 69.15
- over_400_change_1w: 0
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.56,,71.97,,69.04,,0,False,False
20260508,75.61,0.05,72.02,0.05,69.09,0.05,1,True,True
20260515,75.65,0.04,72.06,0.04,69.13,0.04,2,True,True
20260522,75.65,0,72.08,0.02,69.15,0.02,3,False,True
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
