# INDIVIDUAL STOCK CHATGPT PACKET - 6708 天擎

## Metadata
- generated_at: 2026-05-26 21:26:34 Asia/Taipei
- stock_id: 6708
- stock_name: 天擎
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 131
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6708_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6708_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6708_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6708_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6708_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6708_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6708_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6708_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6708_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6708_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6708_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6708_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6708_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6708_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6708_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6708_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6708_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6708_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6708.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6708.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6708.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6708.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6708.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6708.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6708_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6708_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6708_latest.md?ref=main

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
- open: 40.95
- high: 40.95
- low: 40.5
- close: 40.5
- volume: 41000
- ma5: 40.4
- ema23_primary: 40.98
- distance_to_ema23_pct: -1.16
- ma20: 41.36
- ma60: 40.48
- ma120: 40.46
- return_5d: 1.25
- return_20d: -1.22
- volume_ratio: 0.95
- distance_to_ma20_pct_auxiliary: -2.08
- distance_to_high_60_pct: -11.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,41.3,42.3,41,41,38000,40.47,1.3,40.15,41.02,0.85
20260429,41,41.5,40.25,41.5,43000,40.56,2.32,40.26,40.99,0.92
20260430,40.7,41,40,40.2,29000,40.53,-0.81,40.31,40.95,0.61
20260504,40.2,44,40.2,42.4,69000,40.69,4.21,40.41,40.92,1.37
20260505,43,44.5,42.4,42.95,54000,40.87,5.08,40.54,40.83,1.03
20260506,42.9,43.6,42.3,42.5,42000,41.01,3.63,40.62,40.77,0.78
20260507,42.45,42.8,41.1,42.5,61000,41.13,3.32,40.74,40.73,1.09
20260508,42.4,42.5,41.4,41.4,32000,41.16,0.59,40.87,40.7,0.56
20260511,41.95,43.3,41.95,42.8,54000,41.29,3.65,41.05,40.71,0.92
20260512,41.5,42.9,41.1,41.7,47000,41.33,0.9,41.18,40.73,0.77
20260513,42.35,42.35,40.3,40.35,36000,41.25,-2.17,41.25,40.69,0.6
20260514,42.8,42.8,41.45,42.45,22000,41.35,2.67,41.44,40.69,0.37
20260515,43.05,43.05,41,42.35,55000,41.43,2.22,41.63,40.7,0.89
20260518,42.95,42.95,41,41.1,33000,41.4,-0.73,41.72,40.68,0.53
20260519,40.75,40.75,39.85,40,47000,41.29,-3.11,41.8,40.65,0.79
20260520,40,41,39.6,40.5,28000,41.22,-1.75,41.86,40.62,0.48
20260521,40.5,40.5,39.5,40.3,52000,41.14,-2.05,41.71,40.6,0.94
20260522,39.05,40,39.05,40,40000,41.05,-2.55,41.54,40.57,0.8
20260525,40.6,41.8,40.4,40.7,41000,41.02,-0.78,41.38,40.53,0.92
20260526,40.95,40.95,40.5,40.5,41000,40.98,-1.16,41.36,40.48,0.95
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 50.72
- over_600_ratio: 47.66
- over_800_ratio: 42.99
- over_1000_ratio: 42.99
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
20260430,50.72,,42.99,,42.99,,0,False,False
20260508,50.72,0,42.99,0,42.99,0,0,False,False
20260515,50.72,0,42.99,0,42.99,0,0,False,False
20260522,50.72,0,42.99,0,42.99,0,0,False,False
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
