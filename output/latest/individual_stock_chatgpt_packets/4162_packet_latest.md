# INDIVIDUAL STOCK CHATGPT PACKET - 4162 智擎

## Metadata
- generated_at: 2026-05-29 19:32:47 Asia/Taipei
- stock_id: 4162
- stock_name: 智擎
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4162_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4162_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4162_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4162_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4162_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4162_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4162_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4162_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4162_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4162_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4162_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4162_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4162_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4162_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4162_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4162_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4162_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4162_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4162.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4162.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4162.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4162.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4162.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4162.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4162_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4162_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4162_latest.md?ref=main

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
- open: 53.5
- high: 53.8
- low: 53.1
- close: 53.6
- volume: 53000
- ma5: 54.3
- ema23_primary: 55.59
- distance_to_ema23_pct: -3.58
- ma20: 55.73
- ma60: 57.1
- ma120: 63.44
- return_5d: -4.96
- return_20d: -2.37
- volume_ratio: 0.18
- distance_to_ma20_pct_auxiliary: -3.82
- distance_to_high_60_pct: -15.59

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,55,55.8,54.7,55.3,348000,56.85,-2.73,56.99,60.25,0.94
20260505,55.7,57,55.4,56.8,469000,56.85,-0.08,56.88,60.03,1.25
20260506,56.8,57.3,56.3,56.9,406000,56.85,0.08,56.8,59.81,1.05
20260507,56.9,58.1,56.9,57.8,437000,56.93,1.53,56.77,59.64,1.1
20260508,58.2,59.2,57.7,57.8,479000,57,1.4,56.8,59.47,1.2
20260511,57.6,57.6,55.8,56.1,520000,56.93,-1.45,56.74,59.29,1.26
20260512,56.4,57.2,56.1,56.3,304000,56.88,-1.01,56.63,59.14,0.73
20260513,56.3,56.8,55.5,56.2,403000,56.82,-1.09,56.55,59,0.95
20260514,56,56.3,55.5,55.8,519000,56.73,-1.65,56.42,58.85,1.2
20260515,56.2,56.3,55,55,408000,56.59,-2.81,56.23,58.69,0.94
20260518,55,55,53.9,54.4,344000,56.41,-3.56,56.01,58.56,0.78
20260519,54.9,55.9,54.9,55.2,394000,56.31,-1.97,55.84,58.42,0.88
20260520,55.8,56,55,56,274000,56.28,-0.5,55.77,58.28,0.62
20260521,56,57.1,55.9,57.1,422000,56.35,1.33,55.77,58.15,0.94
20260522,57.1,57.3,56.3,56.4,57000,56.35,0.08,55.8,57.98,0.14
20260525,57.3,57.3,55.2,56,56000,56.32,-0.58,55.88,57.81,0.15
20260526,56.2,56.3,54.5,54.8,55000,56.2,-2.49,55.93,57.62,0.16
20260527,55,55.3,54,54.1,54000,56.02,-3.43,55.88,57.44,0.17
20260528,53.9,54.1,53,53,53000,55.77,-4.97,55.8,57.26,0.17
20260529,53.5,53.8,53.1,53.6,53000,55.59,-3.58,55.73,57.1,0.18
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 45.03
- over_600_ratio: 42.34
- over_800_ratio: 40.96
- over_1000_ratio: 38.96
- over_400_change_1w: 0.28
- over_800_change_1w: -0.51
- over_1000_change_1w: 0.69
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,44.7,,41.11,,39.12,,0,False,False
20260508,45.08,0.38,41.6,0.49,39.04,-0.08,1,False,True
20260515,44.75,-0.33,41.47,-0.13,38.27,-0.77,2,False,False
20260522,45.03,0.28,40.96,-0.51,38.96,0.69,3,False,True
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
