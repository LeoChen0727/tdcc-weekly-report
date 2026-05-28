# INDIVIDUAL STOCK CHATGPT PACKET - 6465 威潤

## Metadata
- generated_at: 2026-05-28 20:20:06 Asia/Taipei
- stock_id: 6465
- stock_name: 威潤
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 129
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6465_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6465_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6465_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6465_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6465_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6465_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6465_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6465_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6465_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6465_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6465_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6465_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6465_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6465_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6465_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6465_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6465_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6465_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6465.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6465.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6465.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6465.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6465.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6465.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6465_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6465_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6465_latest.md?ref=main

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
- open: 51.4
- high: 51.5
- low: 48.8
- close: 48.8
- volume: 50000
- ma5: 50.9
- ema23_primary: 48.37
- distance_to_ema23_pct: 0.89
- ma20: 47.95
- ma60: 44.62
- ma120: 39.18
- return_5d: -7.05
- return_20d: 5.97
- volume_ratio: 0.15
- distance_to_ma20_pct_auxiliary: 1.76
- distance_to_high_60_pct: -14.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,46.8,46.95,45.1,45.2,169000,46.23,-2.23,47.31,40.18,0.27
20260504,45.5,46.2,44.7,44.9,173000,46.12,-2.65,47.3,40.34,0.27
20260505,45.05,46.5,45.05,46,126000,46.11,-0.24,47.37,40.52,0.2
20260506,46,48.75,45.3,48.4,419000,46.3,4.53,47.55,40.75,0.64
20260507,48.45,51.8,48.45,49.9,519000,46.6,7.08,47.72,40.98,0.78
20260508,50,50,47.6,47.75,315000,46.7,2.25,47.78,41.2,0.48
20260511,48,48,45,45.6,383000,46.61,-2.16,47.84,41.37,0.6
20260512,45.7,45.7,44.05,44.2,175000,46.41,-4.75,47.66,41.53,0.29
20260513,44,45,43.5,44.2,220000,46.22,-4.37,47.52,41.69,0.38
20260514,47.95,48.6,47.1,48.6,765000,46.42,4.7,47.81,41.91,1.31
20260515,48.3,49.4,45.3,45.3,995000,46.33,-2.22,47.84,42.08,1.61
20260518,45.3,47.4,44,46.75,451000,46.36,0.84,47.73,42.3,0.77
20260519,47.45,49,46.35,46.7,474000,46.39,0.67,47.37,42.55,0.85
20260520,46.75,49.2,46.6,48.6,399000,46.57,4.35,46.97,42.83,0.86
20260521,49.2,53.3,49.2,52.5,712000,47.07,11.54,46.92,43.17,1.56
20260522,52.5,53.8,51.2,52.8,53000,47.55,11.05,47.01,43.5,0.13
20260525,53,53.7,50.8,51.3,52000,47.86,7.19,47.28,43.8,0.14
20260526,50.9,52.3,50,50.7,51000,48.1,5.42,47.55,44.08,0.15
20260527,51.4,51.5,48.8,50.9,50000,48.33,5.32,47.82,44.37,0.15
20260528,51.4,51.5,48.8,48.8,50000,48.37,0.89,47.95,44.62,0.15
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.17
- over_600_ratio: 66.39
- over_800_ratio: 65.09
- over_1000_ratio: 65.09
- over_400_change_1w: -0.18
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.89,,65.09,,65.09,,0,False,False
20260508,68.88,-0.01,65.09,0,65.09,0,0,False,False
20260515,68.35,-0.53,65.09,0,65.09,0,0,False,False
20260522,68.17,-0.18,65.09,0,65.09,0,0,False,False
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
