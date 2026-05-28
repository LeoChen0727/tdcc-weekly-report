# INDIVIDUAL STOCK CHATGPT PACKET - 5488 松普

## Metadata
- generated_at: 2026-05-28 19:33:00 Asia/Taipei
- stock_id: 5488
- stock_name: 松普
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5488_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5488_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5488_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5488_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5488_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5488_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5488_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5488_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5488_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5488_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5488_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5488_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5488_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5488_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5488_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5488_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5488_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5488_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5488.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5488.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5488.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5488.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5488.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5488.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5488_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5488_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5488_latest.md?ref=main

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
- open: 12
- high: 12
- low: 11.5
- close: 11.5
- volume: 465027
- ma5: 11.73
- ema23_primary: 10.9
- distance_to_ema23_pct: 5.53
- ma20: 10.74
- ma60: 10.26
- ma120: 10.02
- return_5d: -2.54
- return_20d: 16.87
- volume_ratio: 0.72
- distance_to_ma20_pct_auxiliary: 7.06
- distance_to_high_60_pct: -7.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,9.84,9.94,9.84,9.89,125000,10.04,-1.45,10.12,10.01,0.4
20260504,9.94,9.97,9.82,9.9,200000,10.02,-1.24,10.11,10,0.64
20260505,9.9,10.1,9.85,10.1,307000,10.03,0.69,10.12,10,0.95
20260506,10.15,10.15,9.96,10.1,211000,10.04,0.63,10.12,10,0.64
20260507,10.1,10.1,9.96,10,198000,10.03,-0.34,10.12,9.99,0.61
20260508,10,10.15,9.95,10.1,277000,10.04,0.61,10.11,9.99,0.86
20260511,10.3,10.6,10.3,10.4,982000,10.07,3.28,10.1,10,3.07
20260512,10.4,10.45,10.05,10.1,590000,10.07,0.28,10.08,10.01,1.8
20260513,10.2,10.55,10.1,10.4,654000,10.1,2.98,10.07,10.02,1.9
20260514,10.4,10.55,10.1,10.5,496000,10.13,3.63,10.09,10.03,1.42
20260515,10.6,10.6,10.15,10.2,779000,10.14,0.61,10.09,10.04,2.05
20260518,10.1,10.35,10.05,10.3,207000,10.15,1.46,10.1,10.05,0.54
20260519,10.3,11,10.2,10.7,1067000,10.2,4.93,10.11,10.06,2.54
20260520,10.95,11.75,10.85,11.7,3783000,10.32,13.34,10.18,10.09,6.39
20260521,11.7,12.1,11.35,11.8,2527000,10.45,12.97,10.26,10.12,3.59
20260522,11.85,12.4,11.55,11.55,12000,10.54,9.61,10.34,10.15,0.02
20260525,11.8,12.3,11.75,11.9,12000,10.65,11.72,10.45,10.18,0.02
20260526,12.1,12.25,11.75,11.85,12000,10.75,10.22,10.56,10.21,0.02
20260527,12.2,12.25,11.5,11.85,12000,10.84,9.29,10.66,10.24,0.02
20260528,12,12,11.5,11.5,465027,10.9,5.53,10.74,10.26,0.72
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 44.06
- over_600_ratio: 38.06
- over_800_ratio: 35.77
- over_1000_ratio: 34.88
- over_400_change_1w: 0.84
- over_800_change_1w: 0.05
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.53,,35.7,,34.82,,0,False,False
20260508,43.04,0.51,35.72,0.02,34.84,0.02,1,True,True
20260515,43.22,0.18,35.72,0,34.84,0,2,False,False
20260522,44.06,0.84,35.77,0.05,34.88,0.04,3,True,True
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
