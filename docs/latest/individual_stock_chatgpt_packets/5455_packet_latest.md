# INDIVIDUAL STOCK CHATGPT PACKET - 5455 昇益

## Metadata
- generated_at: 2026-05-26 23:54:21 Asia/Taipei
- stock_id: 5455
- stock_name: 昇益
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 94
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5455_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5455_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5455_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5455_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5455_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5455_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5455_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5455_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5455_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5455_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5455_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5455_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5455_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5455_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5455_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5455_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5455_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5455_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5455.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5455.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5455.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5455.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5455.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5455.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5455_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5455_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5455_latest.md?ref=main

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
- open: 22
- high: 22.9
- low: 22
- close: 22.55
- volume: 22000
- ma5: 23.57
- ema23_primary: 24.51
- distance_to_ema23_pct: -7.98
- ma20: 24.74
- ma60: 25.52
- ma120: 26.66
- return_5d: -5.85
- return_20d: -10.52
- volume_ratio: 0.44
- distance_to_ma20_pct_auxiliary: -8.85
- distance_to_high_60_pct: -24.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,24.55,25.8,24.25,25.5,40000,25.19,1.22,24.45,26.8,1.88
20260429,24.8,25.9,24.7,25.25,27000,25.2,0.21,24.52,26.76,1.2
20260430,25.25,26.1,25,25.25,101000,25.2,0.19,24.6,26.73,3.68
20260504,24.65,24.9,24.5,24.9,4000,25.18,-1.1,24.66,26.68,0.15
20260505,24.8,26.1,24.25,24.9,90000,25.15,-1.01,24.7,26.62,2.83
20260506,25.5,25.6,24.25,25,115000,25.14,-0.56,24.77,26.57,3.07
20260507,25,26.45,24.45,26.45,74000,25.25,4.75,24.94,26.54,1.8
20260508,26.45,26.75,25.1,25.8,80000,25.3,1.99,25.04,26.48,1.78
20260511,25,26.4,24.7,24.7,24000,25.25,-2.16,25.09,26.4,0.52
20260512,24.7,25.7,24.7,25.55,50000,25.27,1.1,25.2,26.34,1.04
20260513,25,25.8,24.8,25.45,52000,25.29,0.65,25.28,26.28,1.03
20260514,25.45,26.15,24.3,24.8,27000,25.25,-1.77,25.31,26.21,0.58
20260515,24.35,25.85,24.3,24.95,127000,25.22,-1.08,25.36,26.15,2.41
20260518,24.15,24.5,23.75,24.5,16000,25.16,-2.63,25.37,26.06,0.3
20260519,24,24,23.95,23.95,2000,25.06,-4.43,25.3,25.97,0.04
20260520,23.7,25.95,23.7,24.2,42000,24.99,-3.16,25.24,25.88,0.79
20260521,24,24.95,23.7,24.2,59000,24.92,-2.9,25.16,25.79,1.06
20260522,23.95,24,23.75,24,24000,24.85,-3.4,25.04,25.71,0.48
20260525,23.2,23.8,22.4,22.9,23000,24.68,-7.23,24.87,25.62,0.46
20260526,22,22.9,22,22.55,22000,24.51,-7.98,24.74,25.52,0.44
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 93.98
- over_600_ratio: 93.98
- over_800_ratio: 89.92
- over_1000_ratio: 89.92
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
20260430,93.98,,89.92,,89.92,,0,False,False
20260508,93.98,0,89.92,0,89.92,0,0,False,False
20260515,93.98,0,89.92,0,89.92,0,0,False,False
20260522,93.98,0,89.92,0,89.92,0,0,False,False
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
