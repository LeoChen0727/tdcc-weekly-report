# INDIVIDUAL STOCK CHATGPT PACKET - 6188 廣明

## Metadata
- generated_at: 2026-05-26 23:54:32 Asia/Taipei
- stock_id: 6188
- stock_name: 廣明
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6188_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6188_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6188_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6188_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6188_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6188_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6188_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6188_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6188_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6188_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6188_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6188_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6188_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6188_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6188_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6188_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6188_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6188_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6188.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6188.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6188.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6188.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6188.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6188.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6188_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6188_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6188_latest.md?ref=main

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
- open: 87
- high: 88.5
- low: 84.6
- close: 85.5
- volume: 86000
- ma5: 84.48
- ema23_primary: 85.07
- distance_to_ema23_pct: 0.5
- ma20: 84.44
- ma60: 88.88
- ma120: 97.04
- return_5d: 4.4
- return_20d: 5.56
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: 1.26
- distance_to_high_60_pct: -16.99

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,81.5,82.7,80.5,81.3,2800000,87.31,-6.88,86.2,95.19,1.39
20260429,83.6,86.5,83.1,83.4,4712000,86.98,-4.12,86,94.81,2.17
20260430,82.7,86,82.1,83.4,2930000,86.68,-3.79,85.83,94.39,1.31
20260504,84,87.5,82.7,84.8,3213000,86.53,-1.99,85.66,93.99,1.35
20260505,85.9,89.3,85.8,88.5,4421000,86.69,2.09,85.81,93.61,1.77
20260506,88.1,88.2,85.6,86.8,4064000,86.7,0.12,85.8,93.24,1.53
20260507,86.9,87.3,85.6,86.4,2105000,86.67,-0.32,85.65,92.74,0.78
20260508,86.1,87.1,83.6,83.7,2852000,86.43,-3.15,85.45,92.31,1.02
20260511,84,85.3,83.4,84.8,1870000,86.29,-1.73,85.32,91.95,0.67
20260512,85.1,85.8,83.2,85.6,1621000,86.23,-0.73,85.27,91.69,0.58
20260513,85.1,85.3,82.8,83,1644000,85.96,-3.45,85.03,91.37,0.59
20260514,83,84.2,83,83.1,1004000,85.73,-3.06,84.86,91,0.37
20260515,83.5,87.8,83.5,84.3,5004000,85.61,-1.53,84.7,90.71,1.75
20260518,85.4,86.9,83.1,85.4,2667000,85.59,-0.22,84.66,90.5,0.92
20260519,85.5,86.6,81.8,81.9,3072000,85.28,-3.97,84.46,90.21,1.03
20260520,82.4,82.8,80.2,80.7,2584000,84.9,-4.95,84.22,89.88,0.88
20260521,81.5,84,81.5,83.5,2544000,84.78,-1.51,83.97,89.62,0.87
20260522,84.4,86.4,83.6,86.4,85000,84.92,1.75,84.04,89.37,0.03
20260525,87.5,87.5,85.8,86.3,86000,85.03,1.49,84.22,89.11,0.03
20260526,87,88.5,84.6,85.5,86000,85.07,0.5,84.44,88.88,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 44.99
- over_600_ratio: 42.76
- over_800_ratio: 40.55
- over_1000_ratio: 39.6
- over_400_change_1w: -0.31
- over_800_change_1w: -0.59
- over_1000_change_1w: -0.55
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,45.33,,41.37,,40.75,,0,False,False
20260508,45.11,-0.22,41.18,-0.19,40.55,-0.2,1,False,False
20260515,45.3,0.19,41.14,-0.04,40.15,-0.4,2,False,False
20260522,44.99,-0.31,40.55,-0.59,39.6,-0.55,0,False,False
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
