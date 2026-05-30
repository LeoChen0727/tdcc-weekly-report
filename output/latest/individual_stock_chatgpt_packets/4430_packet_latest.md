# INDIVIDUAL STOCK CHATGPT PACKET - 4430 耀億

## Metadata
- generated_at: 2026-05-30 23:42:20 Asia/Taipei
- stock_id: 4430
- stock_name: 耀億
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4430_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4430_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4430_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4430_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4430_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4430_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4430_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4430_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4430_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4430_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4430_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4430_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4430_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4430_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4430_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4430_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4430_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4430_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4430.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4430.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4430.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4430.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4430.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4430.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4430_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4430_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4430_latest.md?ref=main

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
- open: 17.2
- high: 17.2
- low: 16.85
- close: 17.15
- volume: 17000
- ma5: 17.02
- ema23_primary: 17.12
- distance_to_ema23_pct: 0.2
- ma20: 16.98
- ma60: 17.67
- ma120: 17.81
- return_5d: 1.48
- return_20d: -6.28
- volume_ratio: 0.7
- distance_to_ma20_pct_auxiliary: 0.99
- distance_to_high_60_pct: -11.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,18,18,17.5,17.5,18000,17.74,-1.36,17.67,18.15,0.75
20260505,17.25,17.45,17,17.05,49000,17.68,-3.58,17.63,18.12,1.87
20260506,17.1,17.4,17,17.05,16000,17.63,-3.3,17.58,18.1,0.67
20260507,17.1,17.3,17.05,17.05,9000,17.58,-3.03,17.54,18.08,0.38
20260508,17.05,17.3,16.95,17.05,9000,17.54,-2.78,17.5,18.06,0.39
20260511,17.05,17.05,16.5,16.85,60000,17.48,-3.61,17.45,18.04,2.39
20260512,17,17.35,16.9,17,17000,17.44,-2.53,17.41,18.02,0.67
20260513,17.25,17.25,16.5,17.05,92000,17.41,-2.06,17.37,18,3.15
20260514,17.1,17.1,16.75,16.75,25000,17.35,-3.48,17.34,17.97,0.87
20260515,16.55,17.15,16.55,17,22000,17.32,-1.87,17.32,17.95,0.76
20260518,16.6,17.1,16.55,16.65,19000,17.27,-3.58,17.28,17.92,0.72
20260519,16.9,17.05,16.65,16.9,7000,17.24,-1.96,17.25,17.9,0.28
20260520,16.9,16.95,16.6,16.85,17000,17.2,-2.06,17.21,17.88,0.69
20260521,16.8,16.9,16.65,16.9,23000,17.18,-1.63,17.18,17.84,0.91
20260522,16.65,16.95,16.65,16.9,17000,17.16,-1.49,17.14,17.81,0.7
20260525,16.9,17.1,16.7,16.8,17000,17.13,-1.91,17.09,17.78,0.7
20260526,16.6,16.8,16.55,16.8,17000,17.1,-1.75,17.06,17.75,0.69
20260527,16.8,17.2,16.55,17.1,17000,17.1,0,17.04,17.72,0.7
20260528,17.05,17.35,16.8,17.25,17000,17.11,0.81,17.04,17.7,0.69
20260529,17.2,17.2,16.85,17.15,17000,17.12,0.2,16.98,17.67,0.7
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 63.3
- over_600_ratio: 60.1
- over_800_ratio: 57.6
- over_1000_ratio: 53.29
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.3,,57.6,,53.29,,0,False,False
20260508,63.3,0,57.6,0,53.29,0,0,False,False
20260515,63.3,0,57.6,0,53.29,0,0,False,False
20260522,63.3,0,57.6,0,53.29,0,0,False,False
20260529,63.3,0,57.6,0,53.29,0,0,False,False
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
