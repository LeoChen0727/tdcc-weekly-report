# INDIVIDUAL STOCK CHATGPT PACKET - 6233 旺玖

## Metadata
- generated_at: 2026-05-26 23:54:35 Asia/Taipei
- stock_id: 6233
- stock_name: 旺玖
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6233_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6233_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6233_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6233_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6233_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6233_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6233_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6233_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6233_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6233_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6233_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6233_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6233_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6233_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6233_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6233_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6233_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6233_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6233.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6233.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6233.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6233.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6233.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6233.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6233_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6233_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6233_latest.md?ref=main

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
- open: 26.95
- high: 27.15
- low: 25.9
- close: 26.1
- volume: 26000
- ma5: 26.11
- ema23_primary: 26.39
- distance_to_ema23_pct: -1.1
- ma20: 26.62
- ma60: 26.73
- ma120: 24.75
- return_5d: 4.82
- return_20d: -6.62
- volume_ratio: 0.04
- distance_to_ma20_pct_auxiliary: -1.94
- distance_to_high_60_pct: -15.81

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,27.95,28.65,27.5,27.55,421000,26.93,2.31,26.42,26.1,0.51
20260429,27.25,28.35,27.1,27.85,330000,27.01,3.13,26.53,26.16,0.4
20260430,28,29.5,28,28.25,1052000,27.11,4.21,26.7,26.21,1.23
20260504,28.5,29.45,28.5,28.8,920000,27.25,5.69,26.87,26.27,1.05
20260505,28.8,29.5,28.6,29.35,730000,27.43,7.02,27.09,26.34,0.81
20260506,29.4,29.4,26.6,26.6,2157000,27.36,-2.77,27.18,26.37,2.16
20260507,26.8,26.8,26.2,26.4,738000,27.28,-3.21,27.23,26.39,0.72
20260508,26.25,27.95,26.25,26.8,1104000,27.24,-1.61,27.28,26.43,1.04
20260511,27.2,27.5,26.45,26.5,579000,27.18,-2.49,27.32,26.48,0.54
20260512,26.85,26.85,26.2,26.5,373000,27.12,-2.28,27.36,26.53,0.34
20260513,26.3,26.3,25,25.3,931000,26.97,-6.18,27.31,26.56,0.84
20260514,25.7,25.95,25.15,25.85,374000,26.87,-3.81,27.27,26.56,0.35
20260515,26.05,26.25,25.2,25.3,443000,26.74,-5.4,27.21,26.57,0.41
20260518,25.3,26.1,24.4,25.85,318000,26.67,-3.07,27.2,26.6,0.3
20260519,25.9,26.3,24.9,24.9,467000,26.52,-6.11,27.09,26.63,0.44
20260520,24.95,25.75,24.85,25.25,266000,26.42,-4.41,27.01,26.66,0.27
20260521,25.8,26.35,25.75,26.05,329000,26.39,-1.27,26.86,26.69,0.37
20260522,26.05,26.65,25.8,26.55,26000,26.4,0.57,26.82,26.72,0.03
20260525,26.8,27,26.35,26.6,27000,26.42,0.7,26.71,26.75,0.04
20260526,26.95,27.15,25.9,26.1,26000,26.39,-1.1,26.62,26.73,0.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 28.96
- over_600_ratio: 25.72
- over_800_ratio: 23.83
- over_1000_ratio: 19.43
- over_400_change_1w: -0.01
- over_800_change_1w: -0.1
- over_1000_change_1w: -0.07
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,28.6,,25.33,,20.87,,0,False,False
20260508,28.77,0.17,23.95,-1.38,19.5,-1.37,1,False,False
20260515,28.97,0.2,23.93,-0.02,19.5,0,2,False,False
20260522,28.96,-0.01,23.83,-0.1,19.43,-0.07,0,False,False
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
