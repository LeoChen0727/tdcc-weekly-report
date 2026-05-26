# INDIVIDUAL STOCK CHATGPT PACKET - 2015 豐興

## Metadata
- generated_at: 2026-05-26 23:53:07 Asia/Taipei
- stock_id: 2015
- stock_name: 豐興
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2015_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2015_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2015_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2015_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2015_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2015_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2015_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2015_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2015_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2015_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2015_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2015_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2015_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2015_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2015_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2015_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2015_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2015_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2015.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2015.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2015.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2015.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2015.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2015.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2015_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2015_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2015_latest.md?ref=main

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
- open: 62.7
- high: 62.9
- low: 61.5
- close: 61.6
- volume: 349276
- ma5: 62.04
- ema23_primary: 62.44
- distance_to_ema23_pct: -1.34
- ma20: 62.22
- ma60: 64.14
- ma120: 63.95
- return_5d: -1.91
- return_20d: 1.15
- volume_ratio: 1.02
- distance_to_ma20_pct_auxiliary: -0.99
- distance_to_high_60_pct: -12.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,61.2,61.5,60.5,61.5,357645,63.03,-2.42,62.38,65.14,0.83
20260429,61.7,62,61.2,61.8,474464,62.92,-1.79,62.39,65.12,1.11
20260430,61.5,61.7,60.9,60.9,568175,62.76,-2.96,62.37,65.07,1.34
20260504,61,61.2,60.5,60.6,268168,62.58,-3.16,62.29,65.02,0.66
20260505,60.6,61.3,60.5,60.7,290998,62.42,-2.76,62.24,64.96,0.73
20260506,61.4,62.5,61.1,62.5,416842,62.43,0.12,62.27,64.94,1.03
20260507,61.6,62.6,61.6,62.5,284282,62.43,0.11,62.23,64.89,0.7
20260508,62.5,62.8,61.8,62.5,474805,62.44,0.1,62.16,64.84,1.13
20260511,62.5,64.3,62.5,64.3,606366,62.59,2.73,62.22,64.84,1.37
20260512,64.2,64.2,63.3,63.9,280307,62.7,1.91,62.27,64.83,0.63
20260513,63.9,63.9,62.5,62.6,181887,62.69,-0.15,62.22,64.79,0.41
20260514,62.1,63.3,62.1,63.1,239573,62.73,0.59,62.2,64.74,0.55
20260515,63.1,63.2,62.4,62.6,212172,62.72,-0.19,62.15,64.69,0.49
20260518,62.1,62.2,61.4,61.8,405290,62.64,-1.34,62.09,64.63,0.93
20260519,61.8,62.8,61.8,62.8,255772,62.65,0.23,62.11,64.59,0.6
20260520,62.2,62.4,61.5,61.8,214558,62.58,-1.25,62.06,64.53,0.52
20260521,61.9,62.4,61.8,62.4,155253,62.57,-0.27,62.08,64.44,0.39
20260522,62.5,62.5,61.5,61.6,225466,62.49,-1.42,62.09,64.33,0.6
20260525,62,62.9,62,62.8,556841,62.51,0.46,62.18,64.25,1.46
20260526,62.7,62.9,61.5,61.6,349276,62.44,-1.34,62.22,64.14,1.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 88.19
- over_600_ratio: 84.81
- over_800_ratio: 83.6
- over_1000_ratio: 82.35
- over_400_change_1w: 0.09
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,88.01,,83.76,,82.35,,0,False,False
20260508,88.01,0,83.66,-0.1,82.41,0.06,1,False,True
20260515,88.1,0.09,83.65,-0.01,82.39,-0.02,2,False,False
20260522,88.19,0.09,83.6,-0.05,82.35,-0.04,3,False,False
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
