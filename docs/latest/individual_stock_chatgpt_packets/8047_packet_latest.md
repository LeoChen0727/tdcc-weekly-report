# INDIVIDUAL STOCK CHATGPT PACKET - 8047 星雲

## Metadata
- generated_at: 2026-05-27 21:28:26 Asia/Taipei
- stock_id: 8047
- stock_name: 星雲
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8047_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8047_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8047_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8047_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8047_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8047_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8047_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8047_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8047_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8047_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8047_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8047_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8047_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8047_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8047_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8047_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8047_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8047_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8047.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8047.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8047.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8047.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8047.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8047.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8047_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8047_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8047_latest.md?ref=main

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
- date: 20260527
- open: 42
- high: 44
- low: 42
- close: 43.3
- volume: 43000
- ma5: 44.29
- ema23_primary: 49.37
- distance_to_ema23_pct: -12.3
- ma20: 50.66
- ma60: 52.5
- ma120: 51.14
- return_5d: 3.84
- return_20d: -17.52
- volume_ratio: 0.41
- distance_to_ma20_pct_auxiliary: -14.54
- distance_to_high_60_pct: -27.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,52.6,56.8,52.6,56.1,143000,54.38,3.16,54.55,51.68,0.94
20260429,56.5,56.8,53.8,56,118000,54.52,2.72,54.65,51.83,0.83
20260430,56,56,52.7,55.9,184000,54.63,2.32,54.67,51.98,1.28
20260504,56.5,56.5,53.5,53.5,163000,54.54,-1.9,54.66,52.06,1.11
20260505,53,56.4,52.6,56.4,75000,54.69,3.12,54.92,52.18,0.52
20260506,56.4,56.4,54,56.1,116000,54.81,2.35,55.16,52.3,0.78
20260507,55.7,55.7,54,54,91000,54.74,-1.36,55.24,52.38,0.61
20260508,54.7,54.9,53.9,54,84000,54.68,-1.25,55.27,52.48,0.57
20260511,54,54,52.5,53.6,57000,54.59,-1.82,55.08,52.58,0.5
20260512,55,55,50.4,53.3,41000,54.48,-2.17,54.87,52.68,0.37
20260514,58.6,58.6,52.5,54.4,211000,54.48,-0.14,54.71,52.78,1.85
20260515,53.9,53.9,51.2,51.2,128000,54.2,-5.54,54.4,52.83,1.08
20260518,51.1,51.1,50.1,50.3,48000,53.88,-6.64,54.11,52.86,0.43
20260519,50,50.1,45.35,45.35,107000,53.17,-14.7,53.61,52.82,0.94
20260520,44.5,44.5,41.3,41.7,164000,52.21,-20.13,53.06,52.71,1.39
20260521,42.3,45.85,42.3,45.85,188000,51.68,-11.28,52.74,52.69,1.53
20260522,45.85,47.95,45,45,46000,51.12,-11.98,52.28,52.65,0.38
20260525,45,45,42,44.6,43000,50.58,-11.82,51.84,52.62,0.36
20260526,44.45,44.45,42.7,42.7,43000,49.92,-14.47,51.12,52.55,0.39
20260527,42,44,42,43.3,43000,49.37,-12.3,50.66,52.5,0.41
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 79.51
- over_600_ratio: 78.22
- over_800_ratio: 74.79
- over_1000_ratio: 70.41
- over_400_change_1w: 0.18
- over_800_change_1w: 0.17
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.44,,72.89,,70.73,,0,False,False
20260508,79.26,-0.18,74.54,1.65,70.32,-0.41,1,False,True
20260515,79.33,0.07,74.62,0.08,70.24,-0.08,2,False,True
20260522,79.51,0.18,74.79,0.17,70.41,0.17,3,True,True
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
