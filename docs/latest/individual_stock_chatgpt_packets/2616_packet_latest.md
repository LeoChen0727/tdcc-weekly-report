# INDIVIDUAL STOCK CHATGPT PACKET - 2616 山隆

## Metadata
- generated_at: 2026-05-30 23:41:36 Asia/Taipei
- stock_id: 2616
- stock_name: 山隆
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2616_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2616_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2616_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2616_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2616_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2616_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2616_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2616_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2616_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2616_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2616_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2616_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2616_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2616_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2616_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2616_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2616_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2616_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2616.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2616.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2616.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2616.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2616.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2616.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2616_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2616_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2616_latest.md?ref=main

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
- open: 13.6
- high: 13.65
- low: 13.35
- close: 13.65
- volume: 330550
- ma5: 13.45
- ema23_primary: 13.92
- distance_to_ema23_pct: -1.97
- ma20: 13.69
- ma60: 15.83
- ma120: 14.78
- return_5d: -0.73
- return_20d: -3.87
- volume_ratio: 0.86
- distance_to_ma20_pct_auxiliary: -0.29
- distance_to_high_60_pct: -42.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,14.2,14.2,13.85,13.95,575171,15.28,-8.7,15.19,15.9,0.85
20260505,14.2,14.35,13.95,14,428227,15.17,-7.73,15.07,15.9,0.68
20260506,14.15,14.15,13.9,14,249554,15.07,-7.13,14.97,15.91,0.42
20260507,14.15,14.15,13.8,14.05,390779,14.99,-6.27,14.91,15.91,0.7
20260508,14.05,14.05,13.85,14,329240,14.91,-6.08,14.83,15.91,0.61
20260511,14,14,13.85,13.9,432948,14.82,-6.23,14.75,15.91,0.82
20260512,13.85,13.85,13.5,13.7,433660,14.73,-6.99,14.62,15.92,0.87
20260513,13.7,13.85,13.7,13.75,318885,14.65,-6.13,14.5,15.92,0.66
20260514,13.75,13.85,13.65,13.65,318474,14.56,-6.28,14.39,15.92,0.69
20260515,13.8,13.8,13.45,13.45,428579,14.47,-7.06,14.29,15.92,0.95
20260518,13.45,13.45,13.25,13.4,224000,14.38,-6.83,14.19,15.91,0.52
20260519,13.45,13.65,13.45,13.55,207353,14.31,-5.33,14.11,15.91,0.5
20260520,13.7,13.7,13.55,13.65,304378,14.26,-4.26,14.04,15.91,0.77
20260521,13.7,13.8,13.6,13.75,304016,14.22,-3.27,13.97,15.91,0.77
20260522,13.95,13.95,13.7,13.75,302747,14.18,-3.01,13.91,15.91,0.82
20260525,13.75,13.75,13.3,13.4,584277,14.11,-5.04,13.85,15.91,1.53
20260526,13.4,13.45,13.3,13.35,447240,14.05,-4.97,13.79,15.91,1.21
20260527,13.35,13.35,13.2,13.3,443773,13.99,-4.91,13.75,15.9,1.2
20260528,13.15,13.65,13.15,13.55,665147,13.95,-2.87,13.72,15.88,1.71
20260529,13.6,13.65,13.35,13.65,330550,13.92,-1.97,13.69,15.83,0.86
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 44.82
- over_600_ratio: 43.54
- over_800_ratio: 43.54
- over_1000_ratio: 41
- over_400_change_1w: 0.36
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,45.12,,43.57,,41,,0,False,False
20260508,44.78,-0.34,43.57,0,41,0,0,False,False
20260515,44.49,-0.29,43.57,0,41,0,0,False,False
20260522,44.46,-0.03,43.54,-0.03,41,0,0,False,False
20260529,44.82,0.36,43.54,0,41,0,1,False,False
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
