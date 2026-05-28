# INDIVIDUAL STOCK CHATGPT PACKET - 5245 智晶

## Metadata
- generated_at: 2026-05-28 20:19:42 Asia/Taipei
- stock_id: 5245
- stock_name: 智晶
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5245_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5245_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5245_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5245_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5245_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5245_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5245_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5245_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5245_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5245_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5245_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5245_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5245_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5245_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5245_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5245_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5245_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5245_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5245.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5245.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5245.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5245.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5245.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5245.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5245_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5245_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5245_latest.md?ref=main

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
- open: 26.15
- high: 28.35
- low: 26.15
- close: 26.8
- volume: 28000
- ma5: 26.45
- ema23_primary: 25.71
- distance_to_ema23_pct: 4.24
- ma20: 25.55
- ma60: 25.26
- ma120: 25.2
- return_5d: 1.9
- return_20d: 9.16
- volume_ratio: 0.2
- distance_to_ma20_pct_auxiliary: 4.88
- distance_to_high_60_pct: -10.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,24.55,25.2,24.2,24.3,48000,24.8,-2.03,24.4,26.24,0.49
20260504,24.55,25.5,24,24,102000,24.74,-2.98,24.35,26.21,1.01
20260505,24.3,24.3,24.05,24.2,67000,24.69,-1.99,24.35,26.18,0.65
20260506,24.35,24.35,23.9,24,52000,24.63,-2.57,24.4,26.16,0.52
20260507,24.5,26.4,24.5,26.4,282000,24.78,6.53,24.55,26.18,2.56
20260508,27.3,27.9,25.7,25.7,644000,24.86,3.39,24.68,26.14,4.59
20260511,26.15,26.15,25.25,25.5,117000,24.91,2.36,24.81,26.05,0.82
20260512,25.9,25.9,25,25.15,85000,24.93,0.88,24.91,25.9,0.6
20260513,25.1,25.25,24.45,24.85,87000,24.92,-0.3,24.99,25.76,0.61
20260514,25.3,25.3,24.65,24.7,76000,24.91,-0.82,24.95,25.64,0.55
20260515,25.1,27.15,25.1,25.15,590000,24.93,0.9,24.97,25.56,3.86
20260518,25.1,26.1,24.5,25.75,163000,24.99,3.02,24.98,25.52,1.07
20260519,25.75,26.45,25.45,26.45,128000,25.12,5.31,25.06,25.5,0.83
20260520,26.85,26.85,26.3,26.35,86000,25.22,4.49,25.11,25.49,0.55
20260521,26.85,26.85,26,26.3,160000,25.31,3.92,25.12,25.48,1.03
20260522,26.65,26.65,26,26.25,26000,25.39,3.4,25.16,25.45,0.18
20260525,26.4,28.6,26.25,27.1,27000,25.53,6.15,25.29,25.45,0.19
20260526,27.1,27.1,26.2,26.3,26000,25.59,2.76,25.39,25.38,0.18
20260527,26.85,26.85,25.8,25.8,26000,25.61,0.74,25.44,25.3,0.19
20260528,26.15,28.35,26.15,26.8,28000,25.71,4.24,25.55,25.26,0.2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.85
- over_600_ratio: 53.86
- over_800_ratio: 50.79
- over_1000_ratio: 40.76
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.87,,50.82,,40.79,,0,False,False
20260508,57.85,-0.02,50.8,-0.02,40.77,-0.02,0,False,False
20260515,57.86,0.01,50.8,0,40.77,0,1,False,False
20260522,57.85,-0.01,50.79,-0.01,40.76,-0.01,0,False,False
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
