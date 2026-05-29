# INDIVIDUAL STOCK CHATGPT PACKET - 3684 榮昌

## Metadata
- generated_at: 2026-05-29 19:32:42 Asia/Taipei
- stock_id: 3684
- stock_name: 榮昌
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3684_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3684_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3684_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3684_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3684_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3684_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3684_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3684_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3684_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3684_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3684_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3684_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3684_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3684_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3684_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3684_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3684_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3684_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3684.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3684.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3684.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3684.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3684.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3684.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3684_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3684_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3684_latest.md?ref=main

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
- open: 59
- high: 60.3
- low: 59
- close: 59.3
- volume: 60000
- ma5: 59.82
- ema23_primary: 59.56
- distance_to_ema23_pct: -0.44
- ma20: 59.63
- ma60: 59.65
- ma120: 58.29
- return_5d: -3.58
- return_20d: 2.07
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: -0.56
- distance_to_high_60_pct: -14.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,57.4,61.6,57.4,60.1,152000,58.74,2.31,58.26,59.24,1.59
20260505,60.6,60.6,59.3,59.7,62000,58.82,1.49,58.34,59.3,0.65
20260506,59.4,59.9,58.8,59,74000,58.84,0.28,58.34,59.34,0.77
20260507,58.8,59.4,58.3,58.6,80000,58.82,-0.37,58.26,59.38,0.83
20260508,58.9,60.4,58.5,59.5,151000,58.88,1.06,58.2,59.45,1.49
20260511,60,60.8,59,59,173000,58.89,0.19,58.34,59.53,1.95
20260512,58.7,58.7,57.6,58.4,120000,58.84,-0.76,58.41,59.63,1.35
20260513,58,58.1,57.5,57.5,42000,58.73,-2.1,58.39,59.7,0.5
20260514,57.5,59.3,56.2,58.3,128000,58.7,-0.68,58.41,59.76,1.47
20260515,58.3,60.1,58.3,59.3,180000,58.75,0.94,58.48,59.85,1.91
20260518,58.2,63,58,61.1,147000,58.94,3.66,58.59,59.96,1.52
20260519,61.1,61.2,59.5,60.5,57000,59.07,2.42,58.72,60.04,0.6
20260520,61.3,61.8,60.3,60.6,88000,59.2,2.36,58.84,60.11,0.9
20260521,61.5,61.9,60.5,60.5,67000,59.31,2.01,58.92,60.22,0.68
20260522,61.3,62.6,60.8,61.5,62000,59.49,3.38,59.15,60.25,0.65
20260525,62.8,63.1,61.5,62.4,62000,59.73,4.46,59.36,60.2,0.65
20260526,63,63,59,60.1,60000,59.76,0.56,59.49,60.1,0.63
20260527,60.2,60.2,58.4,59,59000,59.7,-1.17,59.59,59.96,0.61
20260528,59.3,60,57.5,58.3,59000,59.58,-2.15,59.58,59.77,0.63
20260529,59,60.3,59,59.3,60000,59.56,-0.44,59.63,59.65,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.44
- over_600_ratio: 57.9
- over_800_ratio: 53.11
- over_1000_ratio: 53.11
- over_400_change_1w: 0.29
- over_800_change_1w: 0.29
- over_1000_change_1w: 0.29
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.16,,52.83,,52.83,,0,False,False
20260508,61.15,-0.01,52.82,-0.01,52.82,-0.01,0,False,False
20260515,61.15,0,52.82,0,52.82,0,0,False,False
20260522,61.44,0.29,53.11,0.29,53.11,0.29,1,True,True
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
