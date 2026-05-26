# INDIVIDUAL STOCK CHATGPT PACKET - 1440 南紡

## Metadata
- generated_at: 2026-05-26 21:24:37 Asia/Taipei
- stock_id: 1440
- stock_name: 南紡
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1440_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1440_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1440_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1440_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1440_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1440_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1440_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1440_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1440_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1440_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1440_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1440_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1440_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1440_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1440_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1440_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1440_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1440_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1440.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1440.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1440.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1440.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1440.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1440.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1440_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1440_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1440_latest.md?ref=main

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
- open: 11.95
- high: 12
- low: 11.7
- close: 11.7
- volume: 2186995
- ma5: 11.55
- ema23_primary: 12.03
- distance_to_ema23_pct: -2.73
- ma20: 12.02
- ma60: 12.66
- ma120: 13.13
- return_5d: 3.08
- return_20d: -7.87
- volume_ratio: 1.08
- distance_to_ma20_pct_auxiliary: -2.64
- distance_to_high_60_pct: -16.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,12.85,13.1,12.75,12.85,1929792,13.03,-1.36,13.01,13.16,1.04
20260429,12.95,12.95,12.75,12.8,733191,13.01,-1.6,13,13.15,0.4
20260430,12.8,12.85,12.65,12.65,1083859,12.98,-2.53,13,13.13,0.6
20260504,12.7,12.7,12.5,12.6,1691339,12.95,-2.68,12.99,13.12,0.91
20260505,12.6,12.65,12.5,12.55,1536904,12.91,-2.81,12.98,13.09,0.82
20260506,12.6,12.65,12.5,12.55,1488947,12.88,-2.59,12.98,13.07,0.78
20260507,12.55,12.55,12.25,12.4,3386115,12.84,-3.45,12.97,13.05,1.68
20260508,12.4,12.45,12.15,12.25,2036232,12.79,-4.25,12.95,13.02,0.99
20260511,12.2,12.25,12.1,12.15,1805387,12.74,-4.63,12.92,12.99,0.86
20260512,12.2,12.2,11.9,12.05,2707050,12.68,-4.99,12.85,12.97,1.37
20260513,12.05,12.05,11.75,11.85,1958338,12.61,-6.05,12.76,12.95,1.07
20260514,11.75,11.8,11.6,11.65,2601272,12.53,-7.04,12.66,12.92,1.4
20260515,11.65,11.8,11.45,11.5,2751897,12.45,-7.61,12.55,12.88,1.43
20260518,11.5,11.5,11.3,11.4,2022869,12.36,-7.76,12.46,12.85,1.09
20260519,11.45,11.5,11.3,11.35,1543173,12.28,-7.54,12.37,12.81,0.82
20260520,11.4,11.45,11.25,11.3,1616262,12.19,-7.33,12.27,12.78,0.86
20260521,11.4,11.45,11.35,11.4,765357,12.13,-6,12.18,12.75,0.41
20260522,11.35,11.4,11.25,11.35,1668542,12.06,-5.91,12.11,12.71,0.92
20260525,11.4,12.2,11.4,12,4948174,12.06,-0.48,12.07,12.69,2.49
20260526,11.95,12,11.7,11.7,2186995,12.03,-2.73,12.02,12.66,1.08
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.21
- over_600_ratio: 76.07
- over_800_ratio: 74.64
- over_1000_ratio: 73.02
- over_400_change_1w: -0.01
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.46,,74.6,,73.16,,0,False,False
20260508,78.39,-0.07,74.45,-0.15,73.12,-0.04,0,False,False
20260515,78.22,-0.17,74.61,0.16,72.96,-0.16,1,False,True
20260522,78.21,-0.01,74.64,0.03,73.02,0.06,2,False,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 1440 | 南紡 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

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
