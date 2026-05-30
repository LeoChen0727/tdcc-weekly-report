# INDIVIDUAL STOCK CHATGPT PACKET - 3205 佰研

## Metadata
- generated_at: 2026-05-30 23:41:55 Asia/Taipei
- stock_id: 3205
- stock_name: 佰研
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3205_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3205_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3205_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3205_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3205_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3205_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3205_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3205_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3205_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3205_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3205_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3205_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3205_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3205_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3205_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3205_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3205_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3205_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3205.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3205.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3205.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3205.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3205.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3205.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3205_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3205_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3205_latest.md?ref=main

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
- open: 54.2
- high: 54.5
- low: 53.7
- close: 54
- volume: 54000
- ma5: 53.54
- ema23_primary: 54.79
- distance_to_ema23_pct: -1.44
- ma20: 54.51
- ma60: 55.48
- ma120: 52.52
- return_5d: -0.92
- return_20d: -3.91
- volume_ratio: 0.36
- distance_to_ma20_pct_auxiliary: -0.93
- distance_to_high_60_pct: -19.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,55.9,56.6,55,56.5,392000,57.78,-2.22,59.41,54.01,0.71
20260505,55.7,56.7,55.6,55.7,155000,57.61,-3.31,59.15,54.13,0.34
20260506,56.1,56.3,55.1,56.3,138000,57.5,-2.09,58.99,54.25,0.32
20260507,56,56.3,55.5,56,112000,57.38,-2.4,58.74,54.32,0.29
20260508,55.8,59.1,55.6,56.4,482000,57.29,-1.56,58.56,54.39,1.28
20260511,57.6,57.6,56,56.4,152000,57.22,-1.43,58.38,54.5,0.42
20260512,56.9,56.9,54.7,54.8,316000,57.02,-3.89,58.1,54.62,0.89
20260513,54.6,54.8,53.5,53.5,238000,56.72,-5.68,57.7,54.72,0.7
20260514,53.1,54,53.1,53.1,164000,56.42,-5.89,57.36,54.81,0.5
20260515,53,54.6,52.8,53.1,154000,56.15,-5.42,56.92,54.89,0.49
20260518,53.5,54,52.8,53.6,126000,55.93,-4.17,56.49,55,0.41
20260519,53.7,55,53.4,53.6,80000,55.74,-3.84,56.22,55.09,0.28
20260520,53.2,54,53.2,53.9,61000,55.59,-3.03,55.95,55.19,0.22
20260521,54.5,55.2,54.3,55,140000,55.54,-0.97,55.8,55.27,0.52
20260522,55.6,55.6,54.3,54.5,55000,55.45,-1.71,55.51,55.31,0.24
20260525,54.2,54.8,53.2,53.3,54000,55.27,-3.57,55.2,55.35,0.29
20260526,53.3,54.2,53.2,53.3,54000,55.11,-3.28,54.98,55.37,0.32
20260527,53.4,53.4,52.7,52.9,53000,54.92,-3.68,54.72,55.39,0.32
20260528,52.7,54.6,52.7,54.2,54000,54.86,-1.21,54.62,55.44,0.35
20260529,54.2,54.5,53.7,54,54000,54.79,-1.44,54.51,55.48,0.36
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 66.3
- over_600_ratio: 64.95
- over_800_ratio: 63.05
- over_1000_ratio: 61.71
- over_400_change_1w: 0.04
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,66.7,,62.46,,59.7,,0,False,False
20260508,66.7,0,62.46,0,59.7,0,0,False,False
20260515,66.27,-0.43,63.06,0.6,61.72,2.02,1,False,True
20260522,66.26,-0.01,63.05,-0.01,61.71,-0.01,0,False,False
20260529,66.3,0.04,63.05,0,61.71,0,1,False,False
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
