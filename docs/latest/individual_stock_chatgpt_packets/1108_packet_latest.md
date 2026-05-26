# INDIVIDUAL STOCK CHATGPT PACKET - 1108 幸福

## Metadata
- generated_at: 2026-05-26 23:52:48 Asia/Taipei
- stock_id: 1108
- stock_name: 幸福
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1108_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1108_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1108_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1108_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1108_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1108_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1108_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1108_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1108_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1108_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1108_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1108_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1108_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1108_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1108_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1108_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1108_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1108_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1108.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1108.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1108.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1108.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1108.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1108.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1108_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1108_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1108_latest.md?ref=main

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
- open: 13.5
- high: 13.55
- low: 13.45
- close: 13.5
- volume: 168883
- ma5: 13.62
- ema23_primary: 14.1
- distance_to_ema23_pct: -4.23
- ma20: 14.15
- ma60: 14.65
- ma120: 14.83
- return_5d: -2.17
- return_20d: -6.9
- volume_ratio: 0.52
- distance_to_ma20_pct_auxiliary: -4.58
- distance_to_high_60_pct: -12.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,14.55,14.6,14.45,14.55,113029,14.76,-1.43,14.76,14.96,0.39
20260429,14.65,14.65,14.5,14.65,89982,14.75,-0.69,14.74,14.96,0.31
20260430,14.65,14.65,14.5,14.55,86528,14.74,-1.26,14.74,14.95,0.32
20260504,14.6,14.6,14.45,14.55,168272,14.72,-1.15,14.72,14.94,0.62
20260505,14.55,14.6,14.45,14.6,198841,14.71,-0.75,14.71,14.93,0.74
20260506,14.65,14.65,14.55,14.6,188939,14.7,-0.69,14.71,14.92,0.7
20260507,14.6,14.6,14.5,14.6,249931,14.69,-0.63,14.69,14.91,0.92
20260508,14.65,14.65,14.55,14.55,141483,14.68,-0.89,14.68,14.9,0.55
20260511,14.6,14.65,14.55,14.6,241210,14.67,-0.5,14.67,14.9,1
20260512,14.55,14.55,14.15,14.2,1201937,14.63,-2.97,14.63,14.88,4.27
20260513,14.2,14.2,14.05,14.1,648954,14.59,-3.36,14.6,14.87,2.22
20260514,14.2,14.2,13.9,13.95,496257,14.54,-4.03,14.55,14.85,1.62
20260515,14,14,13.85,13.85,593916,14.48,-4.35,14.51,14.83,1.84
20260518,13.8,13.85,13.6,13.7,410659,14.41,-4.96,14.45,14.8,1.22
20260519,13.75,13.85,13.7,13.8,168863,14.36,-3.92,14.4,14.78,0.51
20260520,13.7,13.8,13.65,13.8,181269,14.32,-3.61,14.35,14.76,0.56
20260521,13.75,13.8,13.7,13.75,95924,14.27,-3.64,14.3,14.74,0.31
20260522,13.8,13.8,13.5,13.55,687476,14.21,-4.64,14.25,14.71,2.14
20260525,13.55,13.55,13.4,13.5,407880,14.15,-4.59,14.2,14.68,1.22
20260526,13.5,13.55,13.45,13.5,168883,14.1,-4.23,14.15,14.65,0.52
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 81.01
- over_600_ratio: 78.24
- over_800_ratio: 77.22
- over_1000_ratio: 76.27
- over_400_change_1w: 0.17
- over_800_change_1w: 0
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.86,,77.26,,76.33,,0,False,False
20260508,80.84,-0.02,77.26,0,76.33,0,0,False,False
20260515,80.84,0,77.22,-0.04,76.29,-0.04,0,False,False
20260522,81.01,0.17,77.22,0,76.27,-0.02,1,False,False
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
