# INDIVIDUAL STOCK CHATGPT PACKET - 3632 研勤

## Metadata
- generated_at: 2026-05-28 19:32:33 Asia/Taipei
- stock_id: 3632
- stock_name: 研勤
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 130
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3632_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3632_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3632_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3632_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3632_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3632_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3632_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3632_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3632_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3632_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3632_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3632_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3632_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3632_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3632_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3632_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3632_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3632_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3632.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3632.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3632.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3632.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3632.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3632.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3632_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3632_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3632_latest.md?ref=main

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
- date: 20260528
- open: 9.3
- high: 9.6
- low: 9.3
- close: 9.3
- volume: 248925
- ma5: 8.12
- ema23_primary: 8.33
- distance_to_ema23_pct: 11.58
- ma20: 8.24
- ma60: 9.03
- ma120: 9.23
- return_5d: 26.36
- return_20d: 5.56
- volume_ratio: 5.7
- distance_to_ma20_pct_auxiliary: 12.88
- distance_to_high_60_pct: -12.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,8.77,8.78,8.77,8.78,21000,9.11,-3.58,9.11,9.4,1.04
20260504,8.78,8.8,8.77,8.77,103000,9.08,-3.39,9.06,9.39,4.08
20260505,8.8,8.8,8.7,8.7,44000,9.05,-3.83,9.01,9.38,1.63
20260506,8.72,8.73,8.7,8.7,29000,9.02,-3.52,8.99,9.36,1.03
20260507,8.67,8.67,8.5,8.5,153000,8.97,-5.29,8.94,9.35,4.5
20260508,8.5,8.5,8.5,8.5,22000,8.93,-4.87,8.9,9.33,0.64
20260511,8.5,8.5,8.33,8.35,49000,8.89,-6.03,8.85,9.31,1.42
20260512,8.35,8.35,8.31,8.32,20000,8.84,-5.87,8.81,9.3,0.57
20260513,8.32,8.33,8.31,8.31,7000,8.79,-5.51,8.78,9.28,0.2
20260514,8.3,8.47,8.3,8.32,6000,8.76,-4.97,8.74,9.26,0.17
20260515,8.23,8.23,8.22,8.22,21000,8.71,-5.63,8.7,9.24,0.61
20260518,8.1,8.34,8.1,8.13,16000,8.66,-6.15,8.65,9.22,0.47
20260519,8.13,8.13,7.54,7.62,55000,8.58,-11.14,8.59,9.2,1.68
20260520,7.58,7.58,7.57,7.58,19000,8.49,-10.74,8.51,9.17,0.58
20260521,7.51,7.51,7.32,7.36,28000,8.4,-12.36,8.43,9.14,0.85
20260522,7.32,7.35,7.32,7.35,7000,8.31,-11.56,8.35,9.11,0.22
20260525,7.22,7.3,7.22,7.28,7000,8.22,-11.49,8.27,9.07,0.22
20260526,7.29,7.95,7.29,7.95,8000,8.2,-3.07,8.22,9.05,0.25
20260527,8.58,8.74,8.58,8.74,9000,8.25,5.98,8.21,9.05,0.29
20260528,9.3,9.6,9.3,9.3,248925,8.33,11.58,8.24,9.03,5.7
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 17.49
- over_600_ratio: 17.49
- over_800_ratio: 15.87
- over_1000_ratio: 15.87
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
20260430,18.11,,16.49,,16.49,,0,False,False
20260508,17.56,-0.55,15.94,-0.55,15.94,-0.55,0,False,False
20260515,17.49,-0.07,15.87,-0.07,15.87,-0.07,0,False,False
20260522,17.49,0,15.87,0,15.87,0,0,False,False
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
