# INDIVIDUAL STOCK CHATGPT PACKET - 9912 偉聯

## Metadata
- generated_at: 2026-05-28 19:33:56 Asia/Taipei
- stock_id: 9912
- stock_name: 偉聯
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/9912_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/9912_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/9912_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9912_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9912_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9912_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9912_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9912_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9912_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/9912_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/9912_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/9912_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9912_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9912_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9912_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/9912_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/9912_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/9912_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9912.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/9912.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9912.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9912.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/9912.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9912.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9912_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9912_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9912_latest.md?ref=main

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
- open: 12.4
- high: 12.6
- low: 12.4
- close: 12.5
- volume: 23680
- ma5: 12.53
- ema23_primary: 12.49
- distance_to_ema23_pct: 0.05
- ma20: 12.52
- ma60: 12.48
- ma120: 12.3
- return_5d: 0.81
- return_20d: -0.79
- volume_ratio: 0.16
- distance_to_ma20_pct_auxiliary: -0.18
- distance_to_high_60_pct: -3.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,12.4,12.75,12.4,12.75,228281,12.5,1.97,12.56,12.33,2.64
20260504,12.75,12.9,12.6,12.8,168086,12.53,2.17,12.57,12.35,1.88
20260505,12.75,13,12.6,12.9,245998,12.56,2.71,12.57,12.36,2.7
20260506,12.85,13,12.6,12.65,264013,12.57,0.66,12.57,12.37,2.68
20260507,12.65,12.7,12.45,12.65,174716,12.57,0.6,12.56,12.38,1.72
20260508,12.45,12.7,12.45,12.65,34830,12.58,0.55,12.57,12.39,0.34
20260511,12.65,12.65,12.25,12.35,168331,12.56,-1.68,12.55,12.39,1.6
20260512,12.25,12.5,12.15,12.2,171237,12.53,-2.64,12.53,12.4,1.56
20260513,12,12.4,11.85,12.35,82810,12.52,-1.33,12.52,12.41,0.75
20260514,12.45,12.55,12.3,12.4,55536,12.51,-0.85,12.51,12.41,0.5
20260515,12.6,12.65,12.4,12.4,57847,12.5,-0.78,12.49,12.42,0.51
20260518,12.4,12.5,12.35,12.35,751057,12.49,-1.08,12.48,12.43,5.12
20260519,12.25,12.5,12.25,12.45,30767,12.48,-0.26,12.48,12.43,0.22
20260520,12.5,12.6,12.4,12.5,48849,12.48,0.13,12.49,12.44,0.34
20260521,12.6,12.6,12.4,12.4,49931,12.48,-0.61,12.49,12.45,0.36
20260522,12.35,12.6,12.35,12.5,87874,12.48,0.17,12.5,12.46,0.62
20260525,12.5,12.85,12.4,12.75,213498,12.5,1.99,12.52,12.47,1.42
20260526,12.75,12.75,12.45,12.45,62960,12.5,-0.38,12.53,12.47,0.42
20260527,12.45,12.55,12.4,12.45,43840,12.49,-0.34,12.53,12.48,0.29
20260528,12.4,12.6,12.4,12.5,23680,12.49,0.05,12.52,12.48,0.16
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.05
- over_600_ratio: 59.12
- over_800_ratio: 56.68
- over_1000_ratio: 56.68
- over_400_change_1w: 0.26
- over_800_change_1w: 0.26
- over_1000_change_1w: 0.26
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.07,,55.7,,55.7,,0,False,False
20260508,60.26,0.19,55.89,0.19,55.89,0.19,1,True,True
20260515,60.79,0.53,56.42,0.53,56.42,0.53,2,True,True
20260522,61.05,0.26,56.68,0.26,56.68,0.26,3,True,True
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
