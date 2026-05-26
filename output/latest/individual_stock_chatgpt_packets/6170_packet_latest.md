# INDIVIDUAL STOCK CHATGPT PACKET - 6170 統振

## Metadata
- generated_at: 2026-05-26 21:26:15 Asia/Taipei
- stock_id: 6170
- stock_name: 統振
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6170_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6170_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6170_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6170_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6170_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6170_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6170_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6170_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6170_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6170_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6170_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6170_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6170_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6170_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6170_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6170_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6170_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6170_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6170.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6170.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6170.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6170.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6170.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6170.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6170_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6170_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6170_latest.md?ref=main

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
- open: 50.2
- high: 50.7
- low: 50
- close: 50.2
- volume: 50000
- ma5: 50.32
- ema23_primary: 50.8
- distance_to_ema23_pct: -1.18
- ma20: 51.06
- ma60: 50.76
- ma120: 50.25
- return_5d: 0.4
- return_20d: -3.09
- volume_ratio: 0.2
- distance_to_ma20_pct_auxiliary: -1.68
- distance_to_high_60_pct: -6.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,51.8,52.1,51.3,51.7,266000,51.2,0.97,51.24,50.17,1.09
20260429,51.7,51.9,51.5,51.6,121000,51.23,0.71,51.26,50.21,0.51
20260430,51.7,53,51.7,52.1,464000,51.31,1.55,51.34,50.25,1.86
20260504,52.2,52.8,52.1,52.1,375000,51.37,1.42,51.38,50.29,1.43
20260505,52.1,52.7,52,52.6,253000,51.47,2.19,51.47,50.34,0.95
20260506,52.8,53,52.2,52.4,266000,51.55,1.65,51.52,50.4,0.97
20260507,52.7,52.7,51.4,52,456000,51.59,0.8,51.56,50.44,1.6
20260508,51.8,52,51.5,51.9,224000,51.62,0.55,51.59,50.49,0.8
20260511,51.7,51.8,50.6,51,851000,51.56,-1.09,51.58,50.53,2.7
20260512,50.9,51,50.6,50.6,424000,51.48,-1.72,51.57,50.57,1.31
20260513,50.9,51.2,50.7,50.7,200000,51.42,-1.4,51.54,50.6,0.61
20260514,50.8,51.1,50.2,50.3,357000,51.33,-2,51.49,50.62,1.08
20260515,50.4,50.7,50.1,50.3,183000,51.24,-1.83,51.44,50.63,0.55
20260518,50.3,50.4,49.95,50.3,128000,51.16,-1.68,51.4,50.64,0.39
20260519,50.4,50.6,50,50,128000,51.06,-2.08,51.35,50.64,0.39
20260520,50.2,50.6,50.1,50.2,124000,50.99,-1.55,51.31,50.66,0.39
20260521,50.5,50.8,50.5,50.6,135000,50.96,-0.71,51.25,50.69,0.45
20260522,50.5,50.5,50.2,50.4,50000,50.91,-1.01,51.2,50.71,0.18
20260525,50.4,50.4,50,50.2,50000,50.85,-1.29,51.14,50.73,0.18
20260526,50.2,50.7,50,50.2,50000,50.8,-1.18,51.06,50.76,0.2
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.23
- over_600_ratio: 51.21
- over_800_ratio: 50.53
- over_1000_ratio: 47.68
- over_400_change_1w: 0.05
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.44,,51.66,,48.77,,0,False,False
20260508,55.35,-0.09,51.6,-0.06,48.71,-0.06,0,False,False
20260515,54.18,-1.17,50.53,-1.07,47.68,-1.03,0,False,False
20260522,54.23,0.05,50.53,0,47.68,0,1,False,False
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
