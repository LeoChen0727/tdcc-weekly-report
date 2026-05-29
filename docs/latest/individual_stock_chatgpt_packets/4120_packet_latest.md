# INDIVIDUAL STOCK CHATGPT PACKET - 4120 友華

## Metadata
- generated_at: 2026-05-29 19:32:45 Asia/Taipei
- stock_id: 4120
- stock_name: 友華
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4120_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4120_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4120_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4120_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4120_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4120_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4120_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4120_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4120_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4120_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4120_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4120_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4120_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4120_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4120_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4120_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4120_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4120_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4120.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4120.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4120.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4120.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4120.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4120.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4120_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4120_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4120_latest.md?ref=main

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
- open: 44.4
- high: 44.6
- low: 44.4
- close: 44.6
- volume: 44000
- ma5: 44.74
- ema23_primary: 45.85
- distance_to_ema23_pct: -2.73
- ma20: 46.02
- ma60: 46.31
- ma120: 45.39
- return_5d: -3.04
- return_20d: -7.08
- volume_ratio: 0.89
- distance_to_ma20_pct_auxiliary: -3.08
- distance_to_high_60_pct: -8.98

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,47.95,48,47.3,47.4,76000,46.88,1.11,47.16,45.81,2.63
20260505,46.9,46.95,46.6,46.65,28000,46.86,-0.45,47.14,45.85,0.94
20260506,46.65,46.9,46.6,46.6,68000,46.84,-0.51,47.1,45.89,2.26
20260507,46.6,47,46.55,46.6,83000,46.82,-0.47,47.02,45.93,2.63
20260508,46.6,46.6,46.15,46.55,84000,46.8,-0.53,46.98,45.95,2.39
20260511,46.55,46.7,46.5,46.5,53000,46.77,-0.58,46.95,45.98,1.42
20260512,46.55,46.55,46.35,46.5,18000,46.75,-0.54,46.93,46.01,0.48
20260513,46.5,46.9,46.5,46.5,56000,46.73,-0.49,46.91,46.04,1.4
20260514,46.5,46.5,46.25,46.25,35000,46.69,-0.94,46.87,46.06,0.85
20260515,46.25,46.75,46.2,46.2,126000,46.65,-0.96,46.8,46.08,2.88
20260518,46.3,46.3,46.15,46.15,51000,46.61,-0.98,46.74,46.1,1.11
20260519,46.15,46.4,46.15,46.2,18000,46.57,-0.8,46.67,46.14,0.39
20260520,46.25,46.3,45.9,46.3,8000,46.55,-0.54,46.62,46.18,0.18
20260521,46.3,46.3,46.2,46.2,19000,46.52,-0.69,46.56,46.22,0.42
20260522,46.2,46.2,46,46,46000,46.48,-1.03,46.52,46.25,0.99
20260525,45.9,45.9,45.55,45.55,46000,46.4,-1.83,46.45,46.27,0.97
20260526,45.3,45.3,44.75,44.8,45000,46.27,-3.17,46.37,46.29,0.93
20260527,45,45,44.35,44.4,44000,46.11,-3.71,46.28,46.3,0.88
20260528,44.2,44.5,44.15,44.35,44000,45.96,-3.51,46.19,46.3,0.85
20260529,44.4,44.6,44.4,44.6,44000,45.85,-2.73,46.02,46.31,0.89
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.41
- over_600_ratio: 69.29
- over_800_ratio: 67.69
- over_1000_ratio: 63.62
- over_400_change_1w: 0.02
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.3,,67.67,,63.58,,0,False,False
20260508,70.38,0.08,67.66,-0.01,63.6,0.02,1,False,True
20260515,70.39,0.01,67.67,0.01,63.61,0.01,2,True,True
20260522,70.41,0.02,67.69,0.02,63.62,0.01,3,True,True
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
