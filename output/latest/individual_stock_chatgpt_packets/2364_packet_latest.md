# INDIVIDUAL STOCK CHATGPT PACKET - 2364 倫飛

## Metadata
- generated_at: 2026-05-26 23:53:15 Asia/Taipei
- stock_id: 2364
- stock_name: 倫飛
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2364_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2364_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2364_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2364_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2364_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2364_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2364_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2364_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2364_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2364_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2364_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2364_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2364_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2364_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2364_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2364_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2364_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2364_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2364.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2364.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2364.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2364.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2364.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2364.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2364_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2364_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2364_latest.md?ref=main

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
- open: 69.9
- high: 70.5
- low: 68
- close: 68.6
- volume: 239473
- ma5: 68.16
- ema23_primary: 66.7
- distance_to_ema23_pct: 2.85
- ma20: 66.68
- ma60: 64.17
- ma120: 65.13
- return_5d: 4.57
- return_20d: 7.02
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: 2.88
- distance_to_high_60_pct: -5.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,64.7,64.7,63.5,63.9,71440,63.55,0.56,63.38,63.03,0.33
20260429,63.9,64.6,63.6,64.1,68963,63.59,0.8,63.58,63.02,0.32
20260430,65.1,65.1,63,63,76164,63.54,-0.85,63.75,62.97,0.36
20260504,63.3,64.2,63.1,63.7,60829,63.56,0.23,63.92,62.94,0.28
20260505,63.5,64.2,63.5,63.8,140552,63.58,0.35,63.8,62.91,0.79
20260506,64.3,65.4,64.1,65.1,231183,63.7,2.19,63.91,62.91,1.6
20260507,65.6,65.9,64.5,65.3,170694,63.84,2.29,63.99,62.94,1.15
20260508,65,65.2,63.7,63.9,116438,63.84,0.09,63.98,62.94,0.77
20260511,66.6,70.2,66.6,70.2,1052931,64.37,9.05,64.31,63.07,5.31
20260512,70.9,72,68.3,70.9,1832357,64.92,9.22,64.71,63.22,6.49
20260513,70.2,72,69.2,71.1,609355,65.43,8.66,65.11,63.38,1.98
20260514,72.1,72.6,69,69,516557,65.73,4.98,65.39,63.49,1.59
20260515,69.4,71,66.8,66.9,342663,65.83,1.63,65.55,63.55,1.02
20260518,66.9,67.3,65.5,66.3,173225,65.87,0.66,65.61,63.61,0.52
20260519,66.6,67.3,65.1,65.6,193407,65.84,-0.37,65.71,63.68,0.58
20260520,65.8,66.2,65.6,66,103921,65.86,0.22,65.84,63.75,0.31
20260521,67,68,66.7,67.4,229181,65.98,2.14,65.95,63.85,0.69
20260522,68.4,70,67.8,69.7,342965,66.29,5.14,66.19,63.97,1.02
20260525,70.5,70.8,68.6,69.1,375061,66.53,3.87,66.45,64.08,1.1
20260526,69.9,70.5,68,68.6,239473,66.7,2.85,66.68,64.17,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 55.02
- over_600_ratio: 55.02
- over_800_ratio: 51.35
- over_1000_ratio: 51.35
- over_400_change_1w: -0.77
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.8,,51.35,,51.35,,0,False,False
20260508,55.86,0.06,51.35,0,51.35,0,1,False,False
20260515,55.79,-0.07,51.35,0,51.35,0,0,False,False
20260522,55.02,-0.77,51.35,0,51.35,0,0,False,False
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
