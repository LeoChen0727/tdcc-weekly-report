# INDIVIDUAL STOCK CHATGPT PACKET - 2718 全心投控

## Metadata
- generated_at: 2026-05-26 22:18:45 Asia/Taipei
- stock_id: 2718
- stock_name: 全心投控
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2718_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2718_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2718_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2718_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2718_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2718_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2718_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2718_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2718_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2718_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2718_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2718_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2718_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2718_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2718_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2718_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2718_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2718_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2718.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2718.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2718.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2718.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2718.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2718.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2718_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2718_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2718_latest.md?ref=main

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
- open: 45.1
- high: 45.25
- low: 44.8
- close: 45.1
- volume: 45000
- ma5: 45.75
- ema23_primary: 45.27
- distance_to_ema23_pct: -0.38
- ma20: 44.36
- ma60: 46.59
- ma120: 49.35
- return_5d: -2.38
- return_20d: 3.2
- volume_ratio: 0.58
- distance_to_ma20_pct_auxiliary: 1.66
- distance_to_high_60_pct: -11.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,43.25,43.65,43.05,43.35,74000,46.6,-6.98,46.58,48.16,1.77
20260429,43.65,44.45,43.6,43.6,21000,46.35,-5.94,46.37,48.03,0.58
20260430,44.2,44.55,43.7,43.7,28000,46.13,-5.27,46.22,47.92,0.78
20260504,43.95,43.95,43.1,43.25,74000,45.89,-5.76,46.03,47.79,1.93
20260505,43.1,43.1,42.65,42.75,84000,45.63,-6.31,45.84,47.65,2.02
20260506,43,43.1,42.7,43,45000,45.41,-5.31,45.67,47.52,1.04
20260507,43.1,43.1,42.2,42.4,121000,45.16,-6.11,45.46,47.38,2.49
20260508,42.5,42.5,41.4,41.7,89000,44.87,-7.07,45.23,47.25,1.7
20260511,41.7,41.75,41.15,41.2,97000,44.57,-7.55,44.99,47.12,1.75
20260512,41.6,43.3,41.5,42.7,71000,44.41,-3.85,44.73,47.02,1.3
20260513,46.85,46.85,43.55,45.5,215000,44.5,2.25,44.61,46.98,3.4
20260514,45.9,46.5,45.55,46.35,120000,44.65,3.8,44.55,46.94,1.78
20260515,47.05,47.05,46.3,46.4,116000,44.8,3.57,44.48,46.9,1.61
20260518,45.15,46.5,45.15,46.4,54000,44.93,3.26,44.41,46.87,0.73
20260519,46.5,46.6,46.2,46.2,69000,45.04,2.58,44.36,46.84,0.9
20260520,46.35,46.4,45.4,46.2,71000,45.14,2.36,44.33,46.81,0.91
20260521,46.1,46.35,46.1,46.2,59000,45.22,2.16,44.3,46.77,0.73
20260522,46.2,46.2,45.2,46.1,46000,45.3,1.77,44.3,46.72,0.56
20260525,46.1,46.1,44.6,45.15,45000,45.29,-0.3,44.29,46.66,0.56
20260526,45.1,45.25,44.8,45.1,45000,45.27,-0.38,44.36,46.59,0.58
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 86.92
- over_600_ratio: 86.92
- over_800_ratio: 86.92
- over_1000_ratio: 86.92
- over_400_change_1w: 0.27
- over_800_change_1w: 0.27
- over_1000_change_1w: 0.27
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,86.53,,86.53,,86.53,,0,False,False
20260508,86.53,0,86.53,0,86.53,0,0,False,False
20260515,86.65,0.12,86.65,0.12,86.65,0.12,1,True,True
20260522,86.92,0.27,86.92,0.27,86.92,0.27,2,True,True
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
