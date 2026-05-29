# INDIVIDUAL STOCK CHATGPT PACKET - 2852 第一保

## Metadata
- generated_at: 2026-05-29 19:32:16 Asia/Taipei
- stock_id: 2852
- stock_name: 第一保
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2852_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2852_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2852_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2852_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2852_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2852_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2852_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2852_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2852_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2852_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2852_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2852_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2852_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2852_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2852_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2852_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2852_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2852_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2852.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2852.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2852.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2852.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2852.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2852.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2852_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2852_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2852_latest.md?ref=main

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
- date: 20260529
- open: 26.9
- high: 27
- low: 26.8
- close: 26.95
- volume: 335290
- ma5: 26.87
- ema23_primary: 26.62
- distance_to_ema23_pct: 1.25
- ma20: 26.56
- ma60: 26.29
- ma120: 27.01
- return_5d: 0
- return_20d: 3.26
- volume_ratio: 0.73
- distance_to_ma20_pct_auxiliary: 1.48
- distance_to_high_60_pct: -3.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,26,26.3,26,26,342998,26.14,-0.52,26.1,26.51,1.23
20260505,26,26.1,25.95,26,217493,26.13,-0.48,26.11,26.48,0.77
20260506,26.1,26.2,25.95,26.05,288674,26.12,-0.26,26.12,26.46,0.99
20260507,26,26.2,26,26.1,235016,26.12,-0.07,26.13,26.44,0.82
20260508,26.2,26.25,26.1,26.15,187394,26.12,0.11,26.14,26.42,0.65
20260511,26.15,26.3,26.1,26.1,452498,26.12,-0.07,26.14,26.4,1.51
20260512,26.1,26.25,26.05,26.2,507747,26.13,0.29,26.14,26.39,1.6
20260513,26.3,26.35,26.1,26.3,294936,26.14,0.61,26.15,26.38,0.95
20260514,26.5,27.2,26.5,26.5,1096242,26.17,1.26,26.16,26.37,3.22
20260515,26.6,26.9,26.45,26.45,792447,26.19,0.98,26.16,26.35,2.16
20260518,26.45,27.1,26.3,26.85,827952,26.25,2.29,26.2,26.34,2.11
20260519,26.85,27.3,26.85,27,549657,26.31,2.62,26.24,26.34,1.36
20260520,26.8,27.25,26.8,27.1,518552,26.38,2.74,26.29,26.34,1.25
20260521,27.2,27.3,27,27.05,468929,26.43,2.34,26.32,26.34,1.09
20260522,27.1,27.1,26.9,26.95,409289,26.48,1.79,26.36,26.33,0.95
20260525,27.1,27.1,26.75,26.9,579647,26.51,1.47,26.41,26.32,1.3
20260526,26.8,26.9,26.7,26.75,231939,26.53,0.83,26.44,26.31,0.52
20260527,26.85,26.85,26.65,26.85,456309,26.56,1.1,26.48,26.3,1.04
20260528,26.95,26.95,26.7,26.9,363958,26.59,1.18,26.52,26.3,0.8
20260529,26.9,27,26.8,26.95,335290,26.62,1.25,26.56,26.29,0.73
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.54
- over_600_ratio: 61.15
- over_800_ratio: 57.55
- over_1000_ratio: 53.21
- over_400_change_1w: 0.44
- over_800_change_1w: 0.26
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.06,,57.5,,53.43,,0,False,False
20260508,65.07,0.01,57.5,0,53.43,0,1,False,False
20260515,65.1,0.03,57.29,-0.21,53.22,-0.21,2,False,False
20260522,65.54,0.44,57.55,0.26,53.21,-0.01,3,False,True
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
