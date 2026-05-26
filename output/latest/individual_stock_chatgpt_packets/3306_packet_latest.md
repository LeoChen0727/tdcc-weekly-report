# INDIVIDUAL STOCK CHATGPT PACKET - 3306 鼎天

## Metadata
- generated_at: 2026-05-26 21:25:28 Asia/Taipei
- stock_id: 3306
- stock_name: 鼎天
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3306_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3306_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3306_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3306_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3306_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3306_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3306_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3306_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3306_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3306_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3306_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3306_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3306_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3306_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3306_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3306_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3306_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3306_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3306.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3306.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3306.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3306.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3306.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3306.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3306_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3306_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3306_latest.md?ref=main

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
- open: 47.4
- high: 47.4
- low: 46.35
- close: 46.55
- volume: 47000
- ma5: 46.16
- ema23_primary: 46.38
- distance_to_ema23_pct: 0.36
- ma20: 46.27
- ma60: 46.96
- ma120: 48.2
- return_5d: 2.87
- return_20d: -0.96
- volume_ratio: 0.29
- distance_to_ma20_pct_auxiliary: 0.61
- distance_to_high_60_pct: -13.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,46.2,47.15,46.2,46.95,77000,47.55,-1.27,47.34,47.72,0.4
20260429,46.9,47.15,46.6,46.8,90000,47.49,-1.45,47.35,47.68,0.47
20260430,46.8,47.7,46.4,46.4,122000,47.4,-2.11,47.38,47.63,0.67
20260504,46.2,47.2,46.15,46.35,184000,47.31,-2.03,47.36,47.5,0.97
20260505,46.35,47.55,46.35,47.55,188000,47.33,0.46,47.43,47.43,0.99
20260506,47.6,47.85,47,47.6,222000,47.35,0.52,47.5,47.37,1.12
20260507,47.6,48.5,46.95,48.05,239000,47.41,1.35,47.52,47.33,1.17
20260508,48.3,48.3,47,47.5,189000,47.42,0.17,47.52,47.29,0.91
20260511,47.5,47.65,46.4,46.4,250000,47.33,-1.97,47.48,47.26,1.16
20260512,46.25,46.3,45,45.4,265000,47.17,-3.76,47.39,47.24,1.19
20260513,45.4,45.55,44.5,44.55,187000,46.95,-5.12,47.25,47.2,0.83
20260514,44.6,45.25,44.5,44.95,144000,46.79,-3.93,47.12,47.15,0.64
20260515,45,45.45,44.45,44.7,218000,46.61,-4.11,46.98,47.1,0.95
20260518,45.1,46.25,43.8,46.15,234000,46.57,-0.91,46.92,47.1,1
20260519,46.15,47.1,45,45.25,200000,46.46,-2.61,46.79,47.09,0.88
20260520,45.55,45.55,44.3,44.85,155000,46.33,-3.19,46.61,47.06,0.69
20260521,45.05,45.9,45.05,45.7,131000,46.28,-1.25,46.39,47.03,0.67
20260522,46,47.25,45.4,46.85,46000,46.33,1.13,46.32,47.01,0.26
20260525,46.85,47.5,46.2,46.85,47000,46.37,1.04,46.29,46.99,0.28
20260526,47.4,47.4,46.35,46.55,47000,46.38,0.36,46.27,46.96,0.29
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 47.55
- over_600_ratio: 45.94
- over_800_ratio: 43.14
- over_1000_ratio: 43.14
- over_400_change_1w: -0.13
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.84,,43.14,,43.14,,0,False,False
20260508,47.69,-0.15,43.14,0,43.14,0,0,False,False
20260515,47.68,-0.01,43.14,0,43.14,0,0,False,False
20260522,47.55,-0.13,43.14,0,43.14,0,0,False,False
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
