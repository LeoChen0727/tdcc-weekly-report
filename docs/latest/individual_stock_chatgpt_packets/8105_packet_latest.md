# INDIVIDUAL STOCK CHATGPT PACKET - 8105 凌巨

## Metadata
- generated_at: 2026-05-26 23:02:50 Asia/Taipei
- stock_id: 8105
- stock_name: 凌巨
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8105_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8105_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8105_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8105_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8105_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8105_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8105_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8105_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8105_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8105_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8105_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8105_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8105_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8105_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8105_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8105_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8105_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8105_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8105.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8105.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8105.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8105.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8105.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8105.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8105_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8105_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8105_latest.md?ref=main

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
- open: 17.5
- high: 17.7
- low: 16.4
- close: 16.6
- volume: 7976565
- ma5: 16.65
- ema23_primary: 15.22
- distance_to_ema23_pct: 9.05
- ma20: 14.93
- ma60: 13.83
- ma120: 12.98
- return_5d: 5.73
- return_20d: 26.24
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: 11.22
- distance_to_high_60_pct: -10.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,13.25,13.45,13,13.45,1232213,13.59,-1.01,13.65,13.06,0.49
20260429,13.5,13.55,13.35,13.5,813893,13.58,-0.58,13.69,13.05,0.33
20260430,13.5,13.6,13.2,13.3,919832,13.56,-1.89,13.73,13.04,0.37
20260504,13.3,13.45,13.1,13.15,1479035,13.52,-2.75,13.75,13.04,0.6
20260505,13.15,13.6,13.15,13.5,1246357,13.52,-0.15,13.77,13.03,0.52
20260506,13.6,13.7,13.25,13.4,1259996,13.51,-0.82,13.78,13.03,0.52
20260507,13.5,14,13.4,13.85,2016731,13.54,2.3,13.79,13.05,0.86
20260508,13.85,14.3,13.45,13.55,2228695,13.54,0.08,13.78,13.07,0.99
20260511,13.55,13.75,13.3,13.45,1849601,13.53,-0.61,13.76,13.1,0.85
20260512,14.15,14.75,14.15,14.75,11599617,13.63,8.19,13.79,13.15,4.56
20260513,14.9,16.2,14.7,16.2,34255421,13.85,16.99,13.87,13.22,8.63
20260514,16.3,16.6,15.6,16,25024914,14.03,14.07,13.95,13.28,4.97
20260515,16.2,17.05,15.55,15.7,13266503,14.17,10.83,14.02,13.34,2.38
20260518,15.7,15.8,15,15.75,5277160,14.3,10.15,14.11,13.41,0.92
20260519,15.75,16.45,15.5,15.7,6530107,14.42,8.91,14.19,13.47,1.1
20260520,15.7,15.75,15.15,15.45,2928632,14.5,6.54,14.26,13.53,0.49
20260521,15.75,16.65,15.75,16.45,7709033,14.66,12.18,14.37,13.61,1.22
20260522,16.5,17.45,16.45,17.4,16041135,14.89,16.84,14.54,13.69,2.3
20260525,17.85,18.6,17.25,17.35,18363632,15.1,14.93,14.75,13.77,2.36
20260526,17.5,17.7,16.4,16.6,7976565,15.22,9.05,14.93,13.83,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 63.52
- over_600_ratio: 61.86
- over_800_ratio: 61.08
- over_1000_ratio: 60.66
- over_400_change_1w: 0.51
- over_800_change_1w: 0.26
- over_1000_change_1w: 0.46
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,62.12,,59.57,,58.35,,0,False,False
20260508,62.4,0.28,60.25,0.68,59.2,0.85,1,True,True
20260515,63.01,0.61,60.82,0.57,60.2,1,2,True,True
20260522,63.52,0.51,61.08,0.26,60.66,0.46,3,True,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 8105 | 凌巨 | 4 | 4 | 4 | 4 | 4 | repeated_but_no_breakout | 近 10 日上榜 4 日、近 20 日上榜 4 日，尚未突破，需分辨醞釀或鈍化。 |

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
