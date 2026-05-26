# INDIVIDUAL STOCK CHATGPT PACKET - 1806 冠軍

## Metadata
- generated_at: 2026-05-26 21:24:48 Asia/Taipei
- stock_id: 1806
- stock_name: 冠軍
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1806_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1806_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1806_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1806_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1806_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1806_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1806_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1806_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1806_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1806_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1806_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1806_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1806_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1806_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1806_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1806_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1806_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1806_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1806.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1806.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1806.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1806.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1806.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1806.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1806_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1806_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1806_latest.md?ref=main

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
- open: 8.02
- high: 8.09
- low: 7.99
- close: 8.02
- volume: 379222
- ma5: 8.05
- ema23_primary: 8.18
- distance_to_ema23_pct: -1.96
- ma20: 8.23
- ma60: 8.43
- ma120: 8.73
- return_5d: -0.74
- return_20d: -0.74
- volume_ratio: 0.6
- distance_to_ma20_pct_auxiliary: -2.55
- distance_to_high_60_pct: -11.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,8.48,8.88,8.48,8.88,1576753,8.41,5.62,8.35,8.67,1.77
20260429,9.08,9.08,8.51,8.84,2923488,8.44,4.69,8.37,8.66,2.87
20260430,8.83,8.83,8.6,8.6,861297,8.46,1.69,8.38,8.65,0.83
20260504,8.63,8.66,8.34,8.35,775134,8.45,-1.16,8.37,8.64,0.73
20260505,8.35,8.35,8.15,8.25,716347,8.43,-2.15,8.36,8.63,0.66
20260506,8.45,8.46,8.22,8.22,512391,8.41,-2.3,8.36,8.62,0.47
20260507,8.2,8.25,8.15,8.22,539121,8.4,-2.12,8.35,8.6,0.49
20260508,8.29,8.29,8.2,8.25,248201,8.39,-1.61,8.35,8.59,0.23
20260511,8.25,8.31,8.19,8.23,458448,8.37,-1.7,8.35,8.58,0.42
20260512,8.18,8.22,8.16,8.17,338580,8.36,-2.22,8.34,8.57,0.31
20260513,8.16,8.16,8.08,8.12,352006,8.34,-2.59,8.33,8.55,0.32
20260514,8.08,8.27,8.08,8.09,468336,8.32,-2.71,8.31,8.54,0.42
20260515,8.05,8.17,8.04,8.05,376779,8.29,-2.93,8.29,8.53,0.34
20260518,8.03,8.05,8.01,8.01,276263,8.27,-3.14,8.28,8.51,0.25
20260519,8.04,8.1,8.01,8.08,349124,8.25,-2.11,8.27,8.5,0.31
20260520,8.09,8.12,8.04,8.04,133284,8.24,-2.38,8.25,8.49,0.12
20260521,8.04,8.19,8.04,8.07,316744,8.22,-1.85,8.24,8.47,0.28
20260522,8.14,8.14,8.05,8.06,209099,8.21,-1.81,8.24,8.46,0.19
20260525,8.08,8.08,8,8.04,835862,8.19,-1.89,8.23,8.44,0.74
20260526,8.02,8.09,7.99,8.02,379222,8.18,-1.96,8.23,8.43,0.6
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 74.34
- over_600_ratio: 72.41
- over_800_ratio: 71.14
- over_1000_ratio: 70.3
- over_400_change_1w: -0.01
- over_800_change_1w: -0.27
- over_1000_change_1w: -0.27
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,74.3,,71.39,,70.76,,0,False,False
20260508,74.29,-0.01,71.21,-0.18,70.58,-0.18,1,False,False
20260515,74.35,0.06,71.41,0.2,70.57,-0.01,2,False,True
20260522,74.34,-0.01,71.14,-0.27,70.3,-0.27,0,False,False
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
