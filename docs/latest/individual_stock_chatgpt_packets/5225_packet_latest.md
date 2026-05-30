# INDIVIDUAL STOCK CHATGPT PACKET - 5225 東科-KY

## Metadata
- generated_at: 2026-05-30 23:42:36 Asia/Taipei
- stock_id: 5225
- stock_name: 東科-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5225_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5225_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5225_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5225_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5225_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5225_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5225_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5225_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5225_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5225_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5225_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5225_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5225_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5225_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5225_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5225_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5225_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5225_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5225.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5225.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5225.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5225.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5225.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5225.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5225_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5225_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5225_latest.md?ref=main

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
- open: 70.2
- high: 71.1
- low: 70
- close: 70.9
- volume: 312023
- ma5: 70.7
- ema23_primary: 72.95
- distance_to_ema23_pct: -2.81
- ma20: 72.44
- ma60: 80.27
- ma120: 90.95
- return_5d: -0.42
- return_20d: -7.44
- volume_ratio: 0.94
- distance_to_ma20_pct_auxiliary: -2.13
- distance_to_high_60_pct: -26.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,76.8,78.5,76.4,78,353307,79.45,-1.83,77.67,88.83,1.12
20260505,78,78,76.8,77.7,250652,79.31,-2.03,77.67,88.32,0.79
20260506,77.9,78,76.9,76.9,248859,79.11,-2.79,77.55,87.87,0.79
20260507,76.5,76.9,76.4,76.9,238166,78.92,-2.56,77.39,87.45,0.76
20260508,76.3,76.4,74.1,74.4,634930,78.55,-5.28,77.13,87.02,1.89
20260511,74.3,74.6,73.2,73.4,566668,78.12,-6.04,76.85,86.61,1.62
20260512,73.7,73.9,71.4,71.6,658169,77.57,-7.7,76.53,86.19,1.78
20260513,71.5,72,70.5,71.5,309557,77.07,-7.23,76.22,85.78,0.84
20260514,71.8,71.8,70.8,70.8,223860,76.55,-7.51,75.89,85.33,0.61
20260515,70.8,71.6,69.8,70.3,357403,76.03,-7.53,75.48,84.89,0.97
20260518,70,71.3,69.4,70.8,279571,75.59,-6.34,75.11,84.49,0.76
20260519,70.8,71.2,69.8,70.5,213437,75.17,-6.21,74.78,84.05,0.6
20260520,70,70.8,69.9,70.3,118920,74.76,-5.97,74.41,83.6,0.35
20260521,70.6,71.4,70.6,71.1,191510,74.46,-4.51,74.06,83.15,0.56
20260522,71.1,71.5,70.5,71.2,234790,74.18,-4.02,73.75,82.61,0.72
20260525,71.5,71.5,70.3,70.5,352033,73.88,-4.57,73.48,82.11,1.09
20260526,70.9,71.4,70.2,71.3,214490,73.66,-3.21,73.28,81.64,0.68
20260527,71.5,72.3,69.8,70.6,525158,73.41,-3.82,73.06,81.16,1.57
20260528,70.6,71.1,69.7,70.2,369262,73.14,-4.02,72.73,80.7,1.1
20260529,70.2,71.1,70,70.9,312023,72.95,-2.81,72.44,80.27,0.94
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 46.8
- over_600_ratio: 43.96
- over_800_ratio: 43.96
- over_1000_ratio: 40.57
- over_400_change_1w: 0.64
- over_800_change_1w: 1.05
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,45.76,,44.09,,40.63,,0,False,False
20260508,45.58,-0.18,42.97,-1.12,40.6,-0.03,0,False,False
20260515,46.6,1.02,42.93,-0.04,40.55,-0.05,1,False,False
20260522,46.16,-0.44,42.91,-0.02,40.58,0.03,2,False,True
20260529,46.8,0.64,43.96,1.05,40.57,-0.01,3,False,True
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
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 5225 | 東科-KY | 2 | 0 | 1410.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
