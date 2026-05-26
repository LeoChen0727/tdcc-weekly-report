# INDIVIDUAL STOCK CHATGPT PACKET - 5355 佳總

## Metadata
- generated_at: 2026-05-26 22:19:47 Asia/Taipei
- stock_id: 5355
- stock_name: 佳總
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 132
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5355_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5355_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5355_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5355_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5355_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5355_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5355_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5355_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5355_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5355_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5355_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5355_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5355_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5355_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5355_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5355_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5355_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5355_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5355.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5355.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5355.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5355.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5355.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5355.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5355_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5355_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5355_latest.md?ref=main

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
- open: 6.32
- high: 6.66
- low: 6.31
- close: 6.55
- volume: 6000
- ma5: 6.43
- ema23_primary: 6.61
- distance_to_ema23_pct: -0.96
- ma20: 6.68
- ma60: 6.86
- ma120: 6.81
- return_5d: 2.34
- return_20d: 0.46
- volume_ratio: 0.09
- distance_to_ma20_pct_auxiliary: -1.98
- distance_to_high_60_pct: -19.53

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,6.15,6.97,6.15,6.96,98000,6.72,3.55,6.57,7.04,1.26
20260429,6.98,6.98,6.36,6.79,11000,6.73,0.93,6.57,7.03,0.15
20260430,6.77,6.77,6.4,6.72,57000,6.73,-0.1,6.58,7.03,0.82
20260504,6.72,6.74,6.51,6.74,125000,6.73,0.18,6.59,7.02,1.84
20260505,6.59,6.89,6.59,6.83,56000,6.74,1.39,6.61,7.01,0.9
20260506,6.72,6.83,6.66,6.83,118000,6.74,1.27,6.64,7.01,1.79
20260507,6.82,6.84,6.72,6.84,104000,6.75,1.3,6.66,7,1.51
20260508,6.71,7.19,6.71,7.08,73000,6.78,4.43,6.68,6.99,1.02
20260511,6.84,7,6.83,7,105000,6.8,2.97,6.71,6.99,1.41
20260512,6.99,7,6.71,6.99,94000,6.81,2.59,6.73,6.99,1.2
20260513,6.73,6.95,6.5,6.9,198000,6.82,1.16,6.75,6.98,2.36
20260514,6.88,6.88,6.5,6.51,46000,6.8,-4.2,6.76,6.97,0.56
20260515,6.23,6.57,6.21,6.56,62000,6.78,-3.18,6.76,6.96,0.73
20260518,6.4,6.4,6.21,6.34,11000,6.74,-5.92,6.76,6.95,0.13
20260519,6.42,6.45,6.03,6.4,38000,6.71,-4.63,6.75,6.94,0.48
20260520,6.08,6.4,6.08,6.4,45000,6.68,-4.26,6.73,6.92,0.6
20260521,6.39,6.45,6.2,6.45,34000,6.67,-3.23,6.71,6.91,0.46
20260522,6.38,6.45,6.3,6.3,6000,6.63,-5.05,6.68,6.89,0.09
20260525,6.45,6.45,6.26,6.45,6000,6.62,-2.56,6.68,6.88,0.09
20260526,6.32,6.66,6.31,6.55,6000,6.61,-0.96,6.68,6.86,0.09
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 69.66
- over_600_ratio: 67.57
- over_800_ratio: 65.04
- over_1000_ratio: 62.26
- over_400_change_1w: 0.03
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,69.2,,64.87,,62.09,,0,False,False
20260508,69.55,0.35,64.87,0,62.09,0,1,False,False
20260515,69.63,0.08,65.01,0.14,62.23,0.14,2,True,True
20260522,69.66,0.03,65.04,0.03,62.26,0.03,3,True,True
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
