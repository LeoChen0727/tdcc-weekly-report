# INDIVIDUAL STOCK CHATGPT PACKET - 2704 國賓

## Metadata
- generated_at: 2026-05-26 23:00:53 Asia/Taipei
- stock_id: 2704
- stock_name: 國賓
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2704_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2704_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2704_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2704_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2704_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2704_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2704_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2704_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2704_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2704_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2704_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2704_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2704_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2704_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2704_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2704_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2704_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2704_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2704.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2704.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2704.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2704.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2704.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2704.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2704_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2704_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2704_latest.md?ref=main

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
- open: 42
- high: 42.2
- low: 42
- close: 42.05
- volume: 70468
- ma5: 41.95
- ema23_primary: 42.17
- distance_to_ema23_pct: -0.29
- ma20: 42.13
- ma60: 42.47
- ma120: 42.88
- return_5d: 0.36
- return_20d: 0.12
- volume_ratio: 0.6
- distance_to_ma20_pct_auxiliary: -0.2
- distance_to_high_60_pct: -4.86

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,42.1,42.6,41.75,42.1,92838,42.55,-1.05,42.55,42.87,0.65
20260429,43.1,43.1,42.1,42.7,118942,42.56,0.33,42.58,42.87,0.83
20260430,42.9,42.9,41.65,41.7,259967,42.49,-1.85,42.56,42.81,1.71
20260504,42,42.3,41.8,41.85,184919,42.43,-1.38,42.53,42.78,1.18
20260505,41.85,42,41.75,41.75,37362,42.38,-1.48,42.5,42.74,0.24
20260506,42.8,42.8,41.8,42.05,111494,42.35,-0.71,42.49,42.7,0.72
20260507,41.9,42.2,41.8,42,153923,42.32,-0.76,42.47,42.67,0.99
20260508,42.7,42.7,42,42.5,109151,42.34,0.39,42.49,42.64,0.69
20260511,42.5,43.4,42.5,42.8,153740,42.37,1,42.52,42.63,0.98
20260512,43.05,43.8,42.8,42.8,171076,42.41,0.92,42.5,42.63,1.18
20260513,43.25,43.4,42.8,43.35,94286,42.49,2.03,42.52,42.64,0.68
20260514,43.25,43.3,42.15,42.2,102018,42.46,-0.62,42.49,42.62,0.74
20260515,42.35,42.35,41.55,41.6,169621,42.39,-1.87,42.4,42.59,1.21
20260518,41.95,41.95,41.6,41.6,107683,42.33,-1.72,42.31,42.57,0.76
20260519,41.65,42.2,41.65,41.9,68514,42.29,-0.92,42.24,42.56,0.49
20260520,42.05,42.05,41.75,41.75,59243,42.25,-1.17,42.16,42.55,0.44
20260521,41.85,42.2,41.75,42.05,66191,42.23,-0.42,42.12,42.54,0.51
20260522,41.75,42.05,41.75,41.85,85852,42.2,-0.82,42.12,42.52,0.74
20260525,41.95,42.05,41.75,42.05,142043,42.19,-0.32,42.13,42.5,1.18
20260526,42,42.2,42,42.05,70468,42.17,-0.29,42.13,42.47,0.6
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 87.91
- over_600_ratio: 86.23
- over_800_ratio: 84.79
- over_1000_ratio: 82.49
- over_400_change_1w: -0.02
- over_800_change_1w: 0.17
- over_1000_change_1w: -0.32
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,87.78,,84.81,,82.5,,0,False,False
20260508,87.74,-0.04,84.58,-0.23,82.77,0.27,1,False,True
20260515,87.93,0.19,84.62,0.04,82.81,0.04,2,True,True
20260522,87.91,-0.02,84.79,0.17,82.49,-0.32,3,False,True
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
