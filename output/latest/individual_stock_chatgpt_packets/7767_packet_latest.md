# INDIVIDUAL STOCK CHATGPT PACKET - 7767 仁大資訊

## Metadata
- generated_at: 2026-05-28 20:20:28 Asia/Taipei
- stock_id: 7767
- stock_name: 仁大資訊
- packet_status: standard_rawdata_packet
- latest_price_date: 20260528
- price_rows: 108
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7767_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7767_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7767_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7767_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7767_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7767_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7767_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7767_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7767_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7767_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7767_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7767_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7767_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7767_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7767_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7767_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7767_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7767_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7767.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7767.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7767.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7767.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7767.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7767.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7767_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7767_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7767_latest.md?ref=main

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
- open: 43.4
- high: 43.4
- low: 42.9
- close: 42.9
- volume: 43000
- ma5: 43.31
- ema23_primary: 43.88
- distance_to_ema23_pct: -2.24
- ma20: 43.96
- ma60: 44.59
- ma120: 46.33
- return_5d: -1.61
- return_20d: -2.94
- volume_ratio: 1.62
- distance_to_ma20_pct_auxiliary: -2.41
- distance_to_high_60_pct: -11.73

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,45.3,45.3,44.45,44.75,18000,44.68,0.15,44.48,45.59,1.15
20260504,44.75,44.9,44.5,44.65,8000,44.68,-0.07,44.47,45.56,0.54
20260505,44.55,44.9,44.55,44.9,13000,44.7,0.45,44.51,45.51,0.86
20260506,44.9,44.9,44.5,44.55,25000,44.69,-0.3,44.52,45.46,1.55
20260507,44.2,44.25,44.2,44.2,20000,44.65,-1,44.52,45.41,1.2
20260508,44.35,44.35,44.15,44.2,24000,44.61,-0.91,44.52,45.35,1.36
20260511,44.9,44.9,44.2,44.2,46000,44.57,-0.84,44.51,45.3,2.45
20260512,44.2,44.25,44,44.25,22000,44.55,-0.67,44.52,45.25,1.16
20260513,43.35,44.55,43.35,44.3,34000,44.53,-0.51,44.54,45.21,1.79
20260514,44.3,44.3,43.9,43.9,38000,44.47,-1.29,44.51,45.14,1.94
20260515,44.45,44.45,43.7,43.7,16000,44.41,-1.6,44.45,45.08,0.79
20260518,43.7,44.15,43.5,44.15,22000,44.39,-0.54,44.43,45.03,1.06
20260519,43.65,43.9,43.65,43.85,3000,44.34,-1.11,44.41,44.98,0.15
20260520,43.3,43.45,43.3,43.45,11000,44.27,-1.85,44.35,44.94,0.57
20260521,43.5,43.9,43.5,43.6,14000,44.21,-1.39,44.28,44.89,0.74
20260522,43.65,43.65,43.55,43.65,44000,44.17,-1.17,44.22,44.85,2.16
20260525,43.65,43.65,43.35,43.35,44000,44.1,-1.7,44.16,44.79,1.99
20260526,43.4,43.4,43.25,43.4,43000,44.04,-1.45,44.1,44.72,1.83
20260527,43.4,43.4,43,43.25,43000,43.97,-1.65,44.02,44.66,1.69
20260528,43.4,43.4,42.9,42.9,43000,43.88,-2.24,43.96,44.59,1.62
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 72.47
- over_600_ratio: 65.54
- over_800_ratio: 61.22
- over_1000_ratio: 54.71
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.69,,61.22,,54.71,,0,False,False
20260508,72.64,-0.05,61.22,0,54.71,0,0,False,False
20260515,72.47,-0.17,61.22,0,54.71,0,0,False,False
20260522,72.47,0,61.22,0,54.71,0,0,False,False
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
