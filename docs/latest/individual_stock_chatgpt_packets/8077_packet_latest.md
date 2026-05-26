# INDIVIDUAL STOCK CHATGPT PACKET - 8077 洛碁

## Metadata
- generated_at: 2026-05-26 23:55:06 Asia/Taipei
- stock_id: 8077
- stock_name: 洛碁
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 65
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8077_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8077_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8077_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8077_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8077_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8077_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8077_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8077_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8077_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8077_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8077_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8077_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8077_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8077_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8077_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8077_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8077_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8077_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8077.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8077.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8077.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8077.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8077.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8077.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8077_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8077_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8077_latest.md?ref=main

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
- open: 45.3
- high: 45.3
- low: 45.3
- close: 45.3
- volume: 45000
- ma5: 44.46
- ema23_primary: 43.35
- distance_to_ema23_pct: 4.49
- ma20: 43.1
- ma60: 43.86
- ma120: 43.98
- return_5d: 4.38
- return_20d: 9.16
- volume_ratio: 4
- distance_to_ma20_pct_auxiliary: 5.09
- distance_to_high_60_pct: -3.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260401,42.75,44.2,42.75,44.2,4000,43.73,1.08,43.88,44.37,1.51
20260407,44.45,44.45,44.45,44.45,1000,43.79,1.51,43.88,44.37,0.38
20260409,42.5,44.1,42.5,44.1,7000,43.81,0.65,43.86,44.37,2.5
20260413,45.5,45.5,45,45.2,18000,43.93,2.89,43.95,44.38,4.93
20260414,44.1,44.1,44.1,44.1,1000,43.94,0.36,44.04,44.38,0.28
20260415,43.45,43.45,43.45,43.45,2000,43.9,-1.03,44.01,44.36,0.56
20260416,42.25,42.25,42.2,42.25,3000,43.76,-3.46,43.83,44.32,0.81
20260417,41.6,41.6,41.6,41.6,1000,43.58,-4.55,43.72,44.27,0.29
20260422,42.05,42.05,42.05,42.05,1000,43.46,-3.24,43.63,44.23,0.29
20260427,42.05,42.05,42,42,2000,43.33,-3.08,43.44,44.19,0.59
20260507,41,41,39.8,40.35,10000,43.09,-6.35,43.18,44.12,2.6
20260508,40.2,40.2,39.7,39.7,16000,42.8,-7.25,42.87,44.04,3.52
20260511,40,40,40,40,1000,42.57,-6.04,42.6,43.97,0.23
20260512,41,42.95,41,42.95,8000,42.6,0.82,42.56,43.95,1.84
20260518,43.4,43.4,43.4,43.4,1000,42.67,1.71,42.62,43.95,0.23
20260519,43.6,43.6,41.05,41.05,4000,42.53,-3.49,42.52,43.87,0.92
20260521,43.35,44.8,43.35,44.8,10000,42.72,4.86,42.61,43.86,2.08
20260522,44.95,45.55,44.95,45.55,45000,42.96,6.03,42.73,43.85,6.52
20260525,45.6,45.6,45.6,45.6,45000,43.18,5.61,42.91,43.85,4.97
20260526,45.3,45.3,45.3,45.3,45000,43.35,4.49,43.1,43.86,4
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.25
- over_600_ratio: 79.84
- over_800_ratio: 76.98
- over_1000_ratio: 76.98
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
20260430,82.25,,76.98,,76.98,,0,False,False
20260508,82.25,0,76.98,0,76.98,0,0,False,False
20260515,82.25,0,76.98,0,76.98,0,0,False,False
20260522,82.25,0,76.98,0,76.98,0,0,False,False
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
