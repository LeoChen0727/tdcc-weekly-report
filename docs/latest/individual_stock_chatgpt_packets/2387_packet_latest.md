# INDIVIDUAL STOCK CHATGPT PACKET - 2387 精元

## Metadata
- generated_at: 2026-05-30 23:41:24 Asia/Taipei
- stock_id: 2387
- stock_name: 精元
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2387_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2387_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2387_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2387_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2387_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2387_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2387_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2387_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2387_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2387_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2387_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2387_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2387_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2387_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2387_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2387_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2387_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2387_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2387.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2387.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2387.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2387.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2387.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2387.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2387_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2387_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2387_latest.md?ref=main

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
- open: 40.55
- high: 41.4
- low: 40.55
- close: 41.1
- volume: 850772
- ma5: 40.63
- ema23_primary: 40.05
- distance_to_ema23_pct: 2.62
- ma20: 39.81
- ma60: 41.21
- ma120: 40.32
- return_5d: 3.66
- return_20d: 1.48
- volume_ratio: 1.11
- distance_to_ma20_pct_auxiliary: 3.25
- distance_to_high_60_pct: -12.55

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,40.4,41.2,40.4,40.8,461170,40.99,-0.46,40.48,41.17,0.62
20260505,40.8,41.6,40.8,41.35,601301,41.02,0.81,40.57,41.2,0.82
20260506,41.8,41.8,40.7,41,594071,41.02,-0.04,40.66,41.24,0.81
20260507,41,41.7,41,41.65,852981,41.07,1.41,40.78,41.29,1.13
20260508,41.65,41.85,40.6,40.75,815719,41.04,-0.71,40.87,41.33,1.06
20260511,40.8,40.8,39.7,40,956562,40.96,-2.33,40.84,41.37,1.32
20260512,39.35,39.35,38.05,38.5,1484844,40.75,-5.52,40.72,41.39,1.97
20260513,38.4,38.4,37.85,38.15,1063033,40.53,-5.88,40.63,41.39,1.41
20260514,38,38.9,38,38.55,642732,40.37,-4.51,40.56,41.39,0.85
20260515,38.55,38.85,38,38.2,760499,40.19,-4.95,40.47,41.39,0.99
20260518,38.05,38.7,37.9,38.5,334466,40.05,-3.86,40.38,41.4,0.45
20260519,38.5,38.85,38.25,38.3,388065,39.9,-4.01,40.26,41.38,0.53
20260520,38.25,38.8,38.25,38.5,309107,39.79,-3.23,40.12,41.37,0.44
20260521,38.6,39.2,38.6,39.1,537022,39.73,-1.58,39.97,41.37,0.81
20260522,39.1,39.95,38.95,39.65,590091,39.72,-0.18,39.88,41.37,0.94
20260525,39.4,40,39.3,39.95,792161,39.74,0.53,39.79,41.38,1.23
20260526,40.05,41.55,40.05,41.4,1605583,39.88,3.81,39.8,41.35,2.31
20260527,41.5,41.5,40.25,40.35,1017313,39.92,1.08,39.79,41.3,1.4
20260528,40.2,41.1,40.05,40.35,707055,39.95,0.99,39.78,41.24,0.95
20260529,40.55,41.4,40.55,41.1,850772,40.05,2.62,39.81,41.21,1.11
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 57.65
- over_600_ratio: 55.94
- over_800_ratio: 54.49
- over_1000_ratio: 51.2
- over_400_change_1w: 0.56
- over_800_change_1w: 1
- over_1000_change_1w: 0.05
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.95,,54.03,,51.25,,0,False,False
20260508,57.53,0.58,54.09,0.06,51.25,0,1,False,True
20260515,56.97,-0.56,53.49,-0.6,51.15,-0.1,2,False,False
20260522,57.09,0.12,53.49,0,51.15,0,3,False,False
20260529,57.65,0.56,54.49,1,51.2,0.05,4,True,True
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
