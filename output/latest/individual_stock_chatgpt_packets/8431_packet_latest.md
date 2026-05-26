# INDIVIDUAL STOCK CHATGPT PACKET - 8431 匯鑽科

## Metadata
- generated_at: 2026-05-26 21:26:57 Asia/Taipei
- stock_id: 8431
- stock_name: 匯鑽科
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8431_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8431_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8431_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8431_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8431_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8431_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8431_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8431_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8431_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8431_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8431_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8431_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8431_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8431_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8431_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8431_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8431_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8431_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8431.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8431.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8431.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8431.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8431.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8431.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8431_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8431_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8431_latest.md?ref=main

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
- open: 60
- high: 60.5
- low: 58.5
- close: 59.2
- volume: 59000
- ma5: 58.9
- ema23_primary: 60.8
- distance_to_ema23_pct: -2.63
- ma20: 60.45
- ma60: 64.15
- ma120: 62.81
- return_5d: 1.02
- return_20d: -6.03
- volume_ratio: 0.07
- distance_to_ma20_pct_auxiliary: -2.06
- distance_to_high_60_pct: -23.71

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,63.1,63.4,62,62.8,925000,65.65,-4.34,64.36,64.79,0.36
20260429,64.5,67.9,64.5,64.5,2538000,65.55,-1.6,64.44,64.83,0.96
20260430,66,66,62.9,63,1160000,65.34,-3.58,64.69,64.84,0.44
20260504,63,64.5,62.1,62.9,1410000,65.14,-3.43,64.89,64.83,0.53
20260505,63,63.4,62.1,62.8,978000,64.94,-3.3,65.23,64.83,0.37
20260506,63.5,63.5,61.3,62,1113000,64.7,-4.17,65.57,64.88,0.42
20260507,63.1,63.8,61.9,62,988000,64.47,-3.83,65.63,64.9,0.37
20260508,63,63,60.3,60.7,808000,64.16,-5.39,65.33,64.85,0.31
20260511,60.6,61.8,60.1,60.9,742000,63.89,-4.67,65.02,64.84,0.31
20260512,60.9,61.3,60.4,61.1,540000,63.65,-4.01,64.83,64.86,0.23
20260513,60.5,60.8,58.5,59.1,884000,63.27,-6.6,64.42,64.81,0.38
20260514,59.2,60,56.7,57.5,1105000,62.79,-8.43,63.94,64.72,0.49
20260515,58.2,61.5,58,58.5,916000,62.44,-6.3,63.59,64.69,0.4
20260518,58.1,58.4,57,58,321000,62.07,-6.55,63.19,64.6,0.14
20260519,58.6,61.6,58.2,58.6,820000,61.78,-5.14,62.78,64.58,0.39
20260520,58.9,59.1,57,57.1,470000,61.39,-6.98,62.12,64.53,0.25
20260521,58.3,58.7,57.5,57.6,684000,61.07,-5.68,61.32,64.5,0.47
20260522,57.8,62,57.8,60.8,61000,61.05,-0.41,60.95,64.43,0.06
20260525,61.2,61.9,59.1,59.8,60000,60.94,-1.88,60.63,64.34,0.07
20260526,60,60.5,58.5,59.2,59000,60.8,-2.63,60.45,64.15,0.07
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 24.34
- over_600_ratio: 20.86
- over_800_ratio: 17.63
- over_1000_ratio: 15.79
- over_400_change_1w: -0.08
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,24.43,,17.61,,15.77,,0,False,False
20260508,24.33,-0.1,17.61,0,15.77,0,0,False,False
20260515,24.42,0.09,17.63,0.02,15.79,0.02,1,True,True
20260522,24.34,-0.08,17.63,0,15.79,0,0,False,False
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
