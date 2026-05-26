# INDIVIDUAL STOCK CHATGPT PACKET - 3494 誠研

## Metadata
- generated_at: 2026-05-26 23:53:50 Asia/Taipei
- stock_id: 3494
- stock_name: 誠研
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3494_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3494_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3494_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3494_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3494_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3494_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3494_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3494_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3494_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3494_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3494_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3494_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3494_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3494_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3494_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3494_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3494_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3494_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3494.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3494.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3494.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3494.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3494.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3494.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3494_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3494_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3494_latest.md?ref=main

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
- open: 8.15
- high: 8.18
- low: 8.09
- close: 8.12
- volume: 293407
- ma5: 7.89
- ema23_primary: 7.87
- distance_to_ema23_pct: 3.18
- ma20: 7.82
- ma60: 8.08
- ma120: 8.38
- return_5d: 6.98
- return_20d: 2.01
- volume_ratio: 1.97
- distance_to_ma20_pct_auxiliary: 3.81
- distance_to_high_60_pct: -9.78

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,8.01,8.01,7.8,7.98,67504,8.12,-1.7,8.04,8.54,0.66
20260429,8.09,8.09,7.82,7.98,95522,8.11,-1.56,8.04,8.49,0.95
20260430,7.98,7.98,7.75,7.75,77923,8.08,-4.05,8.03,8.45,0.77
20260504,7.75,7.85,7.52,7.63,82728,8.04,-5.1,8.02,8.41,0.81
20260505,7.8,8.39,7.62,8.23,331008,8.06,2.17,8.03,8.38,2.92
20260506,8.23,8.39,8.05,8.05,132691,8.06,-0.06,8.04,8.35,1.13
20260507,7.94,8.04,7.89,8.03,98125,8.05,-0.29,8.05,8.33,0.82
20260508,8.03,8.09,7.93,8.02,79480,8.05,-0.38,8.06,8.31,0.66
20260511,8.02,8.02,7.78,7.8,122879,8.03,-2.86,8.06,8.28,1
20260512,7.96,7.98,7.71,7.78,108811,8.01,-2.85,8.04,8.26,0.87
20260513,7.78,7.78,7.53,7.59,159674,7.97,-4.81,8.01,8.24,1.25
20260514,7.76,7.98,7.17,7.55,147644,7.94,-4.89,7.97,8.22,1.13
20260515,7.69,7.69,7.48,7.56,93939,7.91,-4.39,7.94,8.19,0.72
20260518,7.61,7.61,7.45,7.45,115420,7.87,-5.32,7.89,8.16,0.9
20260519,7.45,7.69,7.45,7.59,75960,7.85,-3.26,7.86,8.14,0.62
20260520,7.35,7.57,7.35,7.56,46182,7.82,-3.35,7.83,8.12,0.39
20260521,7.69,7.9,7.58,7.74,174325,7.82,-0.96,7.81,8.1,1.48
20260522,7.98,7.99,7.75,7.95,353043,7.83,1.58,7.81,8.09,2.71
20260525,7.95,8.16,7.95,8.08,328560,7.85,2.96,7.81,8.09,2.32
20260526,8.15,8.18,8.09,8.12,293407,7.87,3.18,7.82,8.08,1.97
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.17
- over_600_ratio: 58.49
- over_800_ratio: 57.05
- over_1000_ratio: 56.2
- over_400_change_1w: -0.01
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.2,,57.04,,56.19,,0,False,False
20260508,61.17,-0.03,57.02,-0.02,56.17,-0.02,0,False,False
20260515,61.18,0.01,57.01,-0.01,56.16,-0.01,1,False,False
20260522,61.17,-0.01,57.05,0.04,56.2,0.04,2,False,True
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
