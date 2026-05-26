# INDIVIDUAL STOCK CHATGPT PACKET - 6821 聯寶

## Metadata
- generated_at: 2026-05-26 23:54:53 Asia/Taipei
- stock_id: 6821
- stock_name: 聯寶
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6821_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6821_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6821_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6821_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6821_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6821_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6821_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6821_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6821_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6821_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6821_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6821_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6821_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6821_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6821_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6821_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6821_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6821_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6821.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6821.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6821.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6821.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6821.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6821.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6821_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6821_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6821_latest.md?ref=main

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
- open: 62.9
- high: 69.4
- low: 58.9
- close: 69.4
- volume: 66000
- ma5: 59.82
- ema23_primary: 55.58
- distance_to_ema23_pct: 24.86
- ma20: 53.53
- ma60: 50.92
- ma120: 44.12
- return_5d: 36.35
- return_20d: 30.45
- volume_ratio: 0.11
- distance_to_ma20_pct_auxiliary: 29.63
- distance_to_high_60_pct: -6.47

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,53.2,54.1,52.2,54,858000,57.6,-6.25,60.82,45.94,0.45
20260429,54,54,52.5,53.1,339000,57.23,-7.21,60.42,46.23,0.21
20260430,54,57.2,52.5,52.8,874000,56.86,-7.14,60.32,46.5,0.56
20260504,54.2,54.5,51,52,550000,56.45,-7.89,59.97,46.71,0.36
20260505,52,52.8,51.1,52,419000,56.08,-7.28,59.74,46.9,0.28
20260506,54,57,53,54,1490000,55.91,-3.41,59.84,47.15,0.99
20260507,54.2,57,52.6,52.8,1201000,55.65,-5.12,59.81,47.38,0.79
20260508,52.8,53.3,50.7,51,657000,55.26,-7.71,59.66,47.59,0.43
20260511,51.8,51.8,49.1,50,610000,54.82,-8.8,59.2,47.79,0.41
20260512,51,51.5,49.15,50,331000,54.42,-8.12,58.46,47.99,0.24
20260513,49.8,50.5,48.95,49.2,354000,53.99,-8.87,57.37,48.19,0.26
20260514,50.4,50.7,49,49.95,496000,53.65,-6.9,56.55,48.38,0.39
20260515,50,50.4,48.75,48.95,289000,53.26,-8.09,55.93,48.59,0.25
20260518,48.9,51.6,47.3,50.9,545000,53.06,-4.07,55.1,48.82,0.51
20260519,51,52.4,49.95,50.9,738000,52.88,-3.75,54.2,49.04,0.84
20260520,51.5,53.5,50.9,52,917000,52.81,-1.53,53.47,49.28,1.11
20260521,53.7,57.2,53,57.2,1270000,53.17,7.57,52.79,49.6,1.6
20260522,59.7,60.8,56.9,57.4,58000,53.53,7.24,52.44,49.94,0.08
20260525,57.2,63.1,55.1,63.1,60000,54.32,16.16,52.73,50.38,0.09
20260526,62.9,69.4,58.9,69.4,66000,55.58,24.86,53.53,50.92,0.11
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 52.08
- over_600_ratio: 48.86
- over_800_ratio: 47.03
- over_1000_ratio: 41.68
- over_400_change_1w: -0.52
- over_800_change_1w: -0.4
- over_1000_change_1w: -0.37
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.66,,48.38,,42.83,,0,False,False
20260508,52.78,-0.88,47.6,-0.78,42.14,-0.69,0,False,False
20260515,52.6,-0.18,47.43,-0.17,42.05,-0.09,0,False,False
20260522,52.08,-0.52,47.03,-0.4,41.68,-0.37,0,False,False
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
