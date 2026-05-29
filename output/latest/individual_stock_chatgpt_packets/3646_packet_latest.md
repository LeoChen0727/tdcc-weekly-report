# INDIVIDUAL STOCK CHATGPT PACKET - 3646 艾恩特

## Metadata
- generated_at: 2026-05-29 19:32:41 Asia/Taipei
- stock_id: 3646
- stock_name: 艾恩特
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3646_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3646_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3646_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3646_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3646_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3646_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3646_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3646_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3646_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3646_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3646_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3646_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3646_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3646_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3646_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3646_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3646_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3646_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3646.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3646.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3646.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3646.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3646.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3646.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3646_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3646_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3646_latest.md?ref=main

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
- open: 23.8
- high: 23.95
- low: 23.5
- close: 23.8
- volume: 24000
- ma5: 23.64
- ema23_primary: 23.54
- distance_to_ema23_pct: 1.09
- ma20: 23.45
- ma60: 23.84
- ma120: 24.6
- return_5d: 1.71
- return_20d: 1.93
- volume_ratio: 0.7
- distance_to_ma20_pct_auxiliary: 1.48
- distance_to_high_60_pct: -8.46

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,23.35,23.35,23.05,23.3,18000,23.6,-1.26,23.51,24.4,0.76
20260504,23.7,24.4,23.1,23.3,25000,23.57,-1.16,23.46,24.36,1.02
20260506,23.3,23.3,23.1,23.3,23000,23.55,-1.06,23.42,24.33,0.92
20260507,23.15,23.6,23,23.15,51000,23.52,-1.56,23.37,24.3,1.96
20260508,23.05,23.2,23,23.2,28000,23.49,-1.24,23.33,24.25,1.07
20260511,23.15,23.2,23,23.2,24000,23.47,-1.14,23.3,24.21,0.95
20260512,23,23.2,23,23.2,9000,23.44,-1.04,23.29,24.17,0.37
20260513,23.2,23.2,23.05,23.15,13000,23.42,-1.15,23.28,24.13,0.54
20260514,23.8,25.45,23.65,24.2,181000,23.48,3.05,23.34,24.1,6.1
20260515,24.45,24.6,23.3,23.8,95000,23.51,1.23,23.36,24.08,2.85
20260518,23.5,23.8,23.35,23.5,4000,23.51,-0.04,23.37,24.06,0.13
20260519,23.5,23.55,23.3,23.5,28000,23.51,-0.04,23.37,24.04,0.88
20260520,23.3,23.4,23.15,23.15,23000,23.48,-1.4,23.36,24.01,0.7
20260521,23.8,23.8,23.15,23.5,21000,23.48,0.08,23.36,23.99,0.62
20260522,23.4,23.4,23.2,23.4,23000,23.47,-0.32,23.36,23.96,0.7
20260525,23.25,23.35,23.2,23.2,23000,23.45,-1.07,23.36,23.93,0.71
20260526,23.2,23.85,23.2,23.4,23000,23.45,-0.2,23.37,23.91,0.72
20260527,23.4,23.85,23.25,23.85,24000,23.48,1.57,23.4,23.89,0.74
20260528,23.45,25,23.45,23.95,24000,23.52,1.83,23.43,23.87,0.71
20260529,23.8,23.95,23.5,23.8,24000,23.54,1.09,23.45,23.84,0.7
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 48.93
- over_600_ratio: 41.06
- over_800_ratio: 37.58
- over_1000_ratio: 19.84
- over_400_change_1w: -0.06
- over_800_change_1w: -0.08
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.9,,37.59,,19.75,,0,False,False
20260508,49.01,1.11,37.67,0.08,19.79,0.04,1,True,True
20260515,48.99,-0.02,37.66,-0.01,19.84,0.05,2,False,True
20260522,48.93,-0.06,37.58,-0.08,19.84,0,0,False,False
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
