# INDIVIDUAL STOCK CHATGPT PACKET - 1569 濱川

## Metadata
- generated_at: 2026-05-29 19:31:44 Asia/Taipei
- stock_id: 1569
- stock_name: 濱川
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1569_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1569_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1569_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1569_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1569_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1569_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1569_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1569_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1569_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1569_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1569_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1569_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1569_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1569_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1569_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1569_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1569_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1569_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1569.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1569.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1569.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1569.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1569.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1569.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1569_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1569_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1569_latest.md?ref=main

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
- open: 51
- high: 52
- low: 50.7
- close: 51.1
- volume: 51000
- ma5: 51.74
- ema23_primary: 53.31
- distance_to_ema23_pct: -4.15
- ma20: 54.19
- ma60: 53.38
- ma120: 53.71
- return_5d: -3.04
- return_20d: -11.59
- volume_ratio: 0.03
- distance_to_ma20_pct_auxiliary: -5.69
- distance_to_high_60_pct: -23.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,59.5,63.5,57.3,63.5,3905000,56.39,12.62,55.82,53.36,1.46
20260505,64.2,67.2,61.5,63.1,7243000,56.94,10.81,56.51,53.45,2.41
20260506,63.5,63.5,59.5,61.1,2650000,57.29,6.65,57.03,53.54,0.85
20260507,58.7,60.6,58.1,58.3,2696000,57.38,1.61,57.34,53.59,0.84
20260508,58.7,58.8,54.5,56.1,1931000,57.27,-2.04,57.59,53.62,0.59
20260511,56.2,57.8,55.4,55.8,1794000,57.15,-2.36,57.58,53.69,0.56
20260512,55.1,55.2,53.1,55,2250000,56.97,-3.45,57.55,53.74,0.72
20260513,54.4,54.4,51.9,52.4,1891000,56.59,-7.4,57.45,53.75,0.6
20260514,52.8,53,51.3,52,1247000,56.2,-7.48,57.37,53.75,0.39
20260515,52.1,53.7,51.1,52,1395000,55.85,-6.9,57.33,53.75,0.44
20260518,51.5,51.6,50.2,51,775000,55.45,-8.02,57.25,53.72,0.24
20260519,51.9,51.9,50.4,50.9,637000,55.07,-7.57,57.18,53.7,0.2
20260520,50.9,51.3,50.2,50.2,539000,54.66,-8.17,56.97,53.68,0.17
20260521,51,51.3,50.2,50.9,710000,54.35,-6.35,56.66,53.69,0.23
20260522,51.5,53.8,50.4,52.7,52000,54.21,-2.79,56.35,53.69,0.02
20260525,53.2,54.1,52.5,52.9,53000,54.1,-2.23,55.89,53.69,0.02
20260526,52.9,53.4,51.7,52,52000,53.93,-3.58,55.45,53.63,0.03
20260527,52.5,53.2,51.5,52.1,52000,53.78,-3.12,55,53.55,0.03
20260528,52.1,52.4,50.3,50.6,51000,53.51,-5.44,54.52,53.44,0.03
20260529,51,52,50.7,51.1,51000,53.31,-4.15,54.19,53.38,0.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 52.46
- over_600_ratio: 47.69
- over_800_ratio: 46.66
- over_1000_ratio: 46.02
- over_400_change_1w: 0.21
- over_800_change_1w: -0.47
- over_1000_change_1w: 0.12
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.9,,49.74,,48.43,,0,False,False
20260508,53.33,-2.57,47.61,-2.13,46.37,-2.06,0,False,False
20260515,52.25,-1.08,47.13,-0.48,45.9,-0.47,0,False,False
20260522,52.46,0.21,46.66,-0.47,46.02,0.12,1,False,True
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
