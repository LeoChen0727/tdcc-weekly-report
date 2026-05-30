# INDIVIDUAL STOCK CHATGPT PACKET - 6804 明係

## Metadata
- generated_at: 2026-05-30 23:43:19 Asia/Taipei
- stock_id: 6804
- stock_name: 明係
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 272
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6804_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6804_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6804_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6804_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6804_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6804_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6804_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6804_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6804_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6804_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6804_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6804_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6804_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6804_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6804_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6804_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6804_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6804_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6804.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6804.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6804.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6804.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6804.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6804.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6804_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6804_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6804_latest.md?ref=main

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
- open: 16.2
- high: 16.4
- low: 16.1
- close: 16.1
- volume: 16000
- ma5: 16.23
- ema23_primary: 15.79
- distance_to_ema23_pct: 1.96
- ma20: 15.51
- ma60: 16.21
- ma120: 17
- return_5d: 2.55
- return_20d: 4.55
- volume_ratio: 0.3
- distance_to_ma20_pct_auxiliary: 3.84
- distance_to_high_60_pct: -6.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,15.4,15.75,15.1,15.15,47000,16.15,-6.21,16.23,16.69,1.43
20260505,15.35,16,14.95,15.55,99000,16.1,-3.43,16.17,16.65,2.69
20260506,15.55,15.55,14.95,15,130000,16.01,-6.31,16.09,16.6,3.06
20260507,15,15.1,14.95,15.1,45000,15.93,-5.24,16.01,16.56,1.03
20260508,15.1,15.55,15.1,15.55,85000,15.9,-2.22,15.96,16.53,1.8
20260511,15.5,15.5,14.95,15.05,132000,15.83,-4.94,15.88,16.5,2.51
20260512,15.15,15.2,14.9,15.1,106000,15.77,-4.25,15.8,16.46,1.86
20260513,14.95,15,14.9,15,37000,15.71,-4.5,15.72,16.43,0.65
20260514,15.15,15.25,14.95,15,36000,15.65,-4.14,15.64,16.4,0.62
20260515,15.15,15.45,15,15.05,82000,15.6,-3.51,15.56,16.37,1.33
20260518,15.15,15.75,15.15,15.4,83000,15.58,-1.16,15.5,16.34,1.29
20260519,15.3,15.65,15.25,15.55,40000,15.58,-0.18,15.46,16.32,0.62
20260520,15.4,15.55,15.35,15.35,15000,15.56,-1.35,15.42,16.3,0.24
20260521,15.4,15.85,15.4,15.4,49000,15.55,-0.94,15.37,16.27,0.77
20260522,15.75,15.8,15.4,15.7,16000,15.56,0.91,15.35,16.26,0.26
20260525,15.85,16.35,15.85,16.3,16000,15.62,4.35,15.36,16.25,0.26
20260526,16.65,16.65,16.45,16.5,16000,15.69,5.14,15.42,16.24,0.29
20260527,16.85,16.85,16.2,16.2,16000,15.74,2.95,15.45,16.23,0.29
20260528,16.2,16.4,15.9,16.05,16000,15.76,1.82,15.47,16.22,0.29
20260529,16.2,16.4,16.1,16.1,16000,15.79,1.96,15.51,16.21,0.3
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 62.36
- over_600_ratio: 57.34
- over_800_ratio: 52.89
- over_1000_ratio: 47.15
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
20260430,61.47,,52.89,,47.15,,0,False,False
20260508,61.47,0,52.89,0,47.15,0,0,False,False
20260515,62.35,0.88,52.89,0,47.15,0,1,False,False
20260522,62.36,0.01,52.89,0,47.15,0,2,False,False
20260529,62.36,0,52.89,0,47.15,0,0,False,False
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
