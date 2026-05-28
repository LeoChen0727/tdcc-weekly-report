# INDIVIDUAL STOCK CHATGPT PACKET - 2832 台產

## Metadata
- generated_at: 2026-05-28 20:18:53 Asia/Taipei
- stock_id: 2832
- stock_name: 台產
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2832_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2832_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2832_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2832_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2832_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2832_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2832_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2832_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2832_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2832_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2832_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2832_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2832_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2832_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2832_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2832_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2832_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2832_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2832.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2832.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2832.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2832.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2832.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2832.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2832_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2832_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2832_latest.md?ref=main

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
- open: 53.2
- high: 53.5
- low: 52.8
- close: 53
- volume: 215239
- ma5: 53
- ema23_primary: 52.53
- distance_to_ema23_pct: 0.89
- ma20: 53.08
- ma60: 50.1
- ma120: 50.26
- return_5d: -0.93
- return_20d: 2.32
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: -0.15
- distance_to_high_60_pct: -3.81

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,52,52.3,51.7,52.3,158267,49.9,4.81,49.48,48.81,0.7
20260504,52.9,52.9,52,52.1,215892,50.08,4.02,49.72,48.86,0.92
20260505,51.9,52.3,51.9,52,99953,50.24,3.49,49.98,48.9,0.42
20260506,52,52.6,52,52.5,148204,50.43,4.1,50.26,48.94,0.62
20260507,52.2,52.8,52.2,52.7,164244,50.62,4.11,50.51,49,0.68
20260508,52.8,53.8,52.7,53.6,319750,50.87,5.37,50.83,49.07,1.25
20260511,54.1,54.5,53.2,53.6,338858,51.1,4.9,51.1,49.15,1.27
20260512,53.9,53.9,53.1,53.6,209354,51.31,4.47,51.4,49.24,0.76
20260513,54.2,54.7,53.7,54,313372,51.53,4.79,51.7,49.33,1.11
20260514,54,55.1,53.8,53.9,495280,51.73,4.2,51.97,49.42,1.72
20260515,54.7,54.7,52.6,52.8,353770,51.82,1.9,52.16,49.49,1.22
20260518,52.9,53.7,52.7,53.5,192856,51.96,2.97,52.38,49.58,0.66
20260519,53.5,53.8,52.9,52.9,207093,52.04,1.66,52.45,49.66,0.82
20260520,53.4,53.6,52.6,53.6,209091,52.17,2.75,52.58,49.74,0.89
20260521,54,54,53.2,53.5,110481,52.28,2.34,52.68,49.82,0.49
20260522,53.3,53.5,53.1,53.2,122179,52.35,1.62,52.78,49.88,0.56
20260525,53,53,52.7,52.9,242039,52.4,0.95,52.88,49.94,1.09
20260526,52.8,53.2,52.8,53,99346,52.45,1.05,52.98,49.99,0.45
20260527,53,53.2,52.9,52.9,197868,52.49,0.79,53.02,50.05,0.92
20260528,53.2,53.5,52.8,53,215239,52.53,0.89,53.08,50.1,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.81
- over_600_ratio: 66.2
- over_800_ratio: 64.06
- over_1000_ratio: 62.63
- over_400_change_1w: -0.11
- over_800_change_1w: 0
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.78,,64.29,,63.19,,0,False,False
20260508,68.95,0.17,64.11,-0.18,63.02,-0.17,1,False,False
20260515,68.92,-0.03,64.06,-0.05,62.62,-0.4,0,False,False
20260522,68.81,-0.11,64.06,0,62.63,0.01,1,False,True
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
