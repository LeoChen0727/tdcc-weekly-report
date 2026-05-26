# INDIVIDUAL STOCK CHATGPT PACKET - 1231 聯華食

## Metadata
- generated_at: 2026-05-26 23:00:08 Asia/Taipei
- stock_id: 1231
- stock_name: 聯華食
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1231_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1231_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1231_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1231_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1231_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1231_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1231_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1231_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1231_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1231_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1231_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1231_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1231_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1231_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1231_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1231_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1231_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1231_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1231.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1231.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1231.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1231.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1231.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1231.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1231_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1231_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1231_latest.md?ref=main

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
- open: 84.8
- high: 85.8
- low: 84.8
- close: 85.6
- volume: 317762
- ma5: 85.92
- ema23_primary: 86.83
- distance_to_ema23_pct: -1.41
- ma20: 86.47
- ma60: 88.19
- ma120: 92.12
- return_5d: -2.06
- return_20d: -0.35
- volume_ratio: 0.93
- distance_to_ma20_pct_auxiliary: -1.01
- distance_to_high_60_pct: -8.74

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,85.9,87.4,85.5,87,282180,89.35,-2.63,90.21,90.4,0.81
20260429,87.5,88,86.8,87.6,189723,89.2,-1.8,90,90.29,0.55
20260430,87.5,87.6,86.8,86.8,249240,89,-2.47,89.73,90.17,0.72
20260504,86.8,87.2,86.5,87,296874,88.84,-2.07,89.42,90.04,0.86
20260505,87.2,88.3,86.6,87.3,212339,88.71,-1.59,89.15,89.91,0.61
20260506,88,88,86.4,86.8,487004,88.55,-1.97,88.83,89.77,1.37
20260507,86.5,86.7,85.3,86.7,696874,88.39,-1.92,88.52,89.64,1.87
20260508,86.7,88,86.4,86.5,308676,88.24,-1.97,88.22,89.49,0.82
20260511,86.5,87.3,86.5,87,276520,88.13,-1.29,88.02,89.38,0.75
20260512,87,87,85.9,86.3,286616,87.98,-1.91,87.83,89.25,0.78
20260513,86.6,86.6,85.2,86.1,443430,87.82,-1.96,87.66,89.13,1.23
20260514,85.7,86.6,85.7,85.8,261328,87.66,-2.12,87.47,88.99,0.72
20260515,86.6,86.6,85.3,85.5,220191,87.48,-2.26,87.22,88.84,0.61
20260518,85.4,86.6,84.6,86,379159,87.35,-1.55,87.02,88.73,1.02
20260519,85.9,87.6,85.9,87.4,396249,87.36,0.05,86.93,88.64,1.09
20260520,87.4,87.8,86.2,86.6,289293,87.29,-0.79,86.83,88.54,0.81
20260521,86.2,86.8,86,86.8,245032,87.25,-0.52,86.72,88.43,0.69
20260522,86.6,86.6,85.8,85.8,302628,87.13,-1.53,86.59,88.33,0.88
20260525,85.5,85.5,84.1,84.8,673581,86.94,-2.46,86.48,88.23,1.9
20260526,84.8,85.8,84.8,85.6,317762,86.83,-1.41,86.47,88.19,0.93
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.67
- over_600_ratio: 63.6
- over_800_ratio: 63.6
- over_1000_ratio: 62.94
- over_400_change_1w: -0.19
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.05
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,64.89,,63.61,,62.95,,0,False,False
20260508,64.86,-0.03,63.59,-0.02,62.93,-0.02,0,False,False
20260515,64.86,0,63.65,0.06,62.99,0.06,1,False,True
20260522,64.67,-0.19,63.6,-0.05,62.94,-0.05,0,False,False
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
