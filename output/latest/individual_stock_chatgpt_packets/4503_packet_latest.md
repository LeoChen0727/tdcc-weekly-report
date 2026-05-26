# INDIVIDUAL STOCK CHATGPT PACKET - 4503 金雨

## Metadata
- generated_at: 2026-05-26 21:25:48 Asia/Taipei
- stock_id: 4503
- stock_name: 金雨
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4503_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4503_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4503_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4503_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4503_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4503_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4503_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4503_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4503_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4503_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4503_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4503_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4503_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4503_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4503_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4503_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4503_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4503_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4503.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4503.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4503.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4503.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4503.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4503.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4503_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4503_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4503_latest.md?ref=main

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
- open: 44
- high: 44.2
- low: 41.65
- close: 41.75
- volume: 42000
- ma5: 42.6
- ema23_primary: 43.13
- distance_to_ema23_pct: -3.2
- ma20: 43.88
- ma60: 40.79
- ma120: 41.19
- return_5d: -2
- return_20d: -4.13
- volume_ratio: 0.15
- distance_to_ma20_pct_auxiliary: -4.84
- distance_to_high_60_pct: -14.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,43.6,46.45,43,45.2,420000,41.68,8.46,41.52,39.43,1.81
20260429,45.2,45.8,44.45,44.6,207000,41.92,6.4,41.84,39.5,0.88
20260430,44.6,45.75,44.4,44.4,153000,42.13,5.4,42.16,39.55,0.66
20260504,44.65,44.65,42.6,42.95,258000,42.19,1.79,42.34,39.57,1.1
20260505,42.7,43.95,42.55,43.7,179000,42.32,3.26,42.58,39.61,0.77
20260506,43.7,44.95,43.6,44.2,220000,42.48,4.06,42.8,39.66,0.93
20260507,44.25,44.25,42.8,42.95,160000,42.52,1.02,42.94,39.7,0.67
20260508,42.5,45.45,42.25,45.15,539000,42.74,5.65,43.19,39.78,2.1
20260511,46.5,48.55,44.85,47,793000,43.09,9.07,43.52,39.91,2.77
20260512,47.6,48.35,46.5,46.5,781000,43.37,7.2,43.77,40.04,2.5
20260513,46.5,46.85,45,45.05,366000,43.51,3.53,43.93,40.15,1.13
20260514,45.4,45.6,43.85,44.1,326000,43.56,1.23,44.09,40.24,0.98
20260515,44.45,44.8,43.4,43.4,270000,43.55,-0.34,44.23,40.32,0.8
20260518,42.75,44.8,42.4,42.7,252000,43.48,-1.79,44.28,40.4,0.74
20260519,43,43,42.25,42.6,113000,43.41,-1.86,44.22,40.47,0.35
20260520,42.55,42.85,41.65,41.9,137000,43.28,-3.19,44.1,40.53,0.44
20260521,42.55,43.5,41.8,42.15,252000,43.19,-2.4,44.01,40.59,0.81
20260522,42.8,43.3,42.5,43.2,43000,43.19,0.03,43.99,40.65,0.14
20260525,43.6,44.4,42.7,44,43000,43.25,1.72,43.97,40.74,0.15
20260526,44,44.2,41.65,41.75,42000,43.13,-3.2,43.88,40.79,0.15
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.86
- over_600_ratio: 62.47
- over_800_ratio: 59.79
- over_1000_ratio: 59.79
- over_400_change_1w: -0.51
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,66.31,,59.76,,59.76,,0,False,False
20260508,66.23,-0.08,59.77,0.01,59.77,0.01,1,False,True
20260515,66.37,0.14,59.77,0,59.77,0,2,False,False
20260522,65.86,-0.51,59.79,0.02,59.79,0.02,3,False,True
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
