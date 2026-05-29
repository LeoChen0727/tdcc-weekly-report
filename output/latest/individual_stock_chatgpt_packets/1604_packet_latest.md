# INDIVIDUAL STOCK CHATGPT PACKET - 1604 聲寶

## Metadata
- generated_at: 2026-05-29 19:31:45 Asia/Taipei
- stock_id: 1604
- stock_name: 聲寶
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1604_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1604_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1604_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1604_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1604_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1604_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1604_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1604_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1604_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1604_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1604_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1604_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1604_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1604_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1604_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1604_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1604_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1604_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1604.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1604.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1604.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1604.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1604.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1604.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1604_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1604_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1604_latest.md?ref=main

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
- open: 23.4
- high: 23.4
- low: 23.05
- close: 23.4
- volume: 570211
- ma5: 23.32
- ema23_primary: 23.28
- distance_to_ema23_pct: 0.53
- ma20: 23.02
- ma60: 24.03
- ma120: 24.15
- return_5d: 0.86
- return_20d: 2.18
- volume_ratio: 1.53
- distance_to_ma20_pct_auxiliary: 1.63
- distance_to_high_60_pct: -9.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,22.9,22.9,22.75,22.8,389111,23.87,-4.48,24.11,24.36,0.62
20260505,22.8,22.85,22.75,22.8,290796,23.78,-4.13,23.98,24.34,0.46
20260506,22.85,22.85,22.7,22.8,362819,23.7,-3.79,23.84,24.32,0.58
20260507,22.75,22.85,22.7,22.85,337368,23.63,-3.29,23.71,24.3,0.56
20260508,22.9,22.9,22.7,22.75,306368,23.56,-3.42,23.58,24.27,0.51
20260511,22.75,22.8,22.7,22.8,400674,23.49,-2.95,23.46,24.25,0.69
20260512,22.9,23,22.7,22.8,458556,23.43,-2.71,23.35,24.23,0.83
20260513,22.8,22.95,22.7,22.9,442922,23.39,-2.1,23.23,24.21,0.83
20260514,22.9,23.15,22.8,22.85,317385,23.35,-2.12,23.1,24.2,0.71
20260515,23,23,22.75,22.8,325622,23.3,-2.14,23.05,24.18,0.79
20260518,22.8,23.1,22.7,23.1,288337,23.28,-0.79,23.02,24.17,0.77
20260519,23.1,23.15,22.95,23.15,244706,23.27,-0.52,23,24.16,0.7
20260520,23.15,23.15,22.95,23.1,252367,23.26,-0.68,22.97,24.15,0.72
20260521,23.05,23.2,23,23.2,384877,23.25,-0.23,22.95,24.13,1.09
20260522,23.1,23.3,22.9,23.2,361787,23.25,-0.21,22.95,24.11,1.06
20260525,23.2,23.2,22.9,23.2,554819,23.24,-0.19,22.95,24.09,1.66
20260526,23.2,23.35,23,23.35,371056,23.25,0.42,22.97,24.08,1.1
20260527,23.3,23.35,23.05,23.35,440966,23.26,0.38,22.99,24.06,1.28
20260528,23.4,23.5,23.1,23.3,366920,23.26,0.15,23,24.04,1.04
20260529,23.4,23.4,23.05,23.4,570211,23.28,0.53,23.02,24.03,1.53
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.99
- over_600_ratio: 55.53
- over_800_ratio: 53.9
- over_1000_ratio: 52.95
- over_400_change_1w: 0.09
- over_800_change_1w: 0.1
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.94,,54.13,,52.69,,0,False,False
20260508,57.85,-0.09,54.05,-0.08,52.63,-0.06,0,False,False
20260515,57.9,0.05,53.8,-0.25,52.85,0.22,1,False,True
20260522,57.99,0.09,53.9,0.1,52.95,0.1,2,True,True
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
