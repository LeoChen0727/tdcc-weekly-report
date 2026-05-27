# INDIVIDUAL STOCK CHATGPT PACKET - 3164 景岳

## Metadata
- generated_at: 2026-05-27 21:26:59 Asia/Taipei
- stock_id: 3164
- stock_name: 景岳
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3164_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3164_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3164_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3164_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3164_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3164_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3164_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3164_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3164_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3164_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3164_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3164_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3164_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3164_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3164_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3164_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3164_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3164_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3164.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3164.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3164.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3164.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3164.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3164.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3164_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3164_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3164_latest.md?ref=main

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
- open: 16.4
- high: 16.5
- low: 16.2
- close: 16.25
- volume: 136464
- ma5: 16.52
- ema23_primary: 17.13
- distance_to_ema23_pct: -5.14
- ma20: 17.17
- ma60: 17.77
- ma120: 17.99
- return_5d: -4.41
- return_20d: -9.47
- volume_ratio: 1.52
- distance_to_ma20_pct_auxiliary: -5.36
- distance_to_high_60_pct: -13.1

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,17.95,17.95,17.7,17.75,41812,17.98,-1.29,18.01,18.06,0.83
20260430,17.8,17.9,17.7,17.7,91598,17.96,-1.44,17.99,18.05,1.72
20260504,17.75,17.8,17.7,17.7,51969,17.94,-1.32,17.95,18.04,0.98
20260505,17.7,17.8,17.7,17.7,32743,17.92,-1.21,17.91,18.03,0.61
20260506,17.9,17.9,17.5,17.6,94782,17.89,-1.63,17.86,18.02,1.83
20260507,17.6,17.6,17.45,17.5,57744,17.86,-2.01,17.84,18.01,1.15
20260508,17.75,17.75,17.4,17.4,54408,17.82,-2.36,17.81,17.99,1.07
20260511,17.5,17.8,17.3,17.6,157767,17.8,-1.13,17.8,17.98,2.78
20260512,17.5,17.7,17.3,17.6,66749,17.79,-1.04,17.79,17.98,1.15
20260513,17.35,17.4,17.3,17.3,33092,17.74,-2.51,17.75,17.96,0.57
20260514,17.25,17.3,17.05,17.2,164406,17.7,-2.82,17.71,17.95,2.64
20260515,17.25,17.25,17.05,17.05,58252,17.65,-3.37,17.67,17.94,0.91
20260518,17.05,17.1,16.9,16.9,57322,17.58,-3.88,17.62,17.92,0.88
20260519,16.9,17,16.75,16.8,84793,17.52,-4.1,17.55,17.9,1.25
20260520,16.75,17,16.45,17,177073,17.47,-2.72,17.5,17.89,2.39
20260521,16.8,16.8,16.65,16.65,131749,17.41,-4.34,17.44,17.87,1.7
20260522,16.85,16.85,16.45,16.8,164096,17.36,-3.2,17.4,17.85,1.99
20260525,16.6,16.6,16.45,16.45,73077,17.28,-4.8,17.33,17.82,0.88
20260526,16.45,16.55,16.3,16.45,63888,17.21,-4.42,17.25,17.8,0.75
20260527,16.4,16.5,16.2,16.25,136464,17.13,-5.14,17.17,17.77,1.52
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 55.14
- over_600_ratio: 50.66
- over_800_ratio: 46.61
- over_1000_ratio: 39.72
- over_400_change_1w: -0.73
- over_800_change_1w: -0.03
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.95,,46.72,,40.82,,0,False,False
20260508,55.88,-0.07,46.64,-0.08,39.65,-1.17,0,False,False
20260515,55.87,-0.01,46.64,0,39.71,0.06,1,False,True
20260522,55.14,-0.73,46.61,-0.03,39.72,0.01,2,False,True
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
