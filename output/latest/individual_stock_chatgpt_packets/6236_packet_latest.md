# INDIVIDUAL STOCK CHATGPT PACKET - 6236 中湛

## Metadata
- generated_at: 2026-05-28 19:33:13 Asia/Taipei
- stock_id: 6236
- stock_name: 中湛
- packet_status: partial_rawdata_packet
- latest_price_date: 20260521
- price_rows: 33
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6236_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6236_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6236_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6236_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6236_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6236_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6236_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6236_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6236_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6236_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6236_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6236_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6236_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6236_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6236_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6236_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6236_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6236_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6236.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6236.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6236.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6236.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6236.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6236.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6236_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6236_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6236_latest.md?ref=main

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
- date: 20260521
- open: 20
- high: 20
- low: 20
- close: 20
- volume: 1000
- ma5: 19.53
- ema23_primary: 23.93
- distance_to_ema23_pct: -16.43
- ma20: 25.08
- ma60: 24.46
- ma120: 24.46
- return_5d: -16.67
- return_20d: -21.88
- volume_ratio: 0.67
- distance_to_ma20_pct_auxiliary: -20.25
- distance_to_high_60_pct: -31.74

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260123,25.55,25.55,25.55,25.55,1000,25.57,-0.07,23.66,23.66,0.7
20260126,26.35,26.35,26.35,26.35,1000,25.63,2.8,23.84,23.84,0.71
20260127,26.95,26.95,26.95,26.95,1000,25.74,4.69,24.03,24.03,0.73
20260128,27.8,27.8,27.8,27.8,1000,25.91,7.28,24.26,24.26,0.74
20260129,27.9,27.9,27.9,27.9,1000,26.08,6.98,24.46,24.46,0.75
20260130,28.45,28.45,28.45,28.45,1000,26.28,8.27,24.67,24.67,0.76
20260202,28.4,28.4,28.4,28.4,1000,26.45,7.36,24.86,24.86,0.77
20260203,28.35,28.35,28.35,28.35,1000,26.61,6.53,24.81,25.02,0.77
20260204,28.25,28.25,28.25,28.25,1000,26.75,5.61,25.13,25.17,0.77
20260205,25.45,27.05,25.45,27.05,4000,26.77,1.03,25.5,25.25,3.2
20260206,27.75,27.75,27.75,27.75,1000,26.86,3.33,25.82,25.35,0.8
20260209,27.7,27.7,27.7,27.7,1000,26.93,2.88,26.12,25.45,0.83
20260210,28.55,28.55,24.95,26,3000,26.85,-3.16,26.31,25.47,2.31
20260211,23.4,23.4,23.4,23.4,4000,26.56,-11.9,26.37,25.39,2.86
20260224,24,24,24,24,1000,26.35,-8.91,26.42,25.34,0.71
20260226,22.7,22.7,21.6,21.6,3000,25.95,-16.77,26.31,25.21,2
20260414,18,18,18,18,1000,25.29,-28.82,25.99,24.97,0.67
20260421,19,19,19,19,1000,24.77,-23.28,25.68,24.78,0.67
20260422,19.05,19.05,19.05,19.05,1000,24.29,-21.57,25.36,24.6,0.67
20260521,20,20,20,20,1000,23.93,-16.43,25.08,24.46,0.67
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 92.64
- over_600_ratio: 91.48
- over_800_ratio: 87.98
- over_1000_ratio: 87.98
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,92.64,,87.98,,87.98,,0,False,False
20260508,92.64,0,87.98,0,87.98,0,0,False,False
20260515,92.64,0,87.98,0,87.98,0,0,False,False
20260522,92.64,0,87.98,0,87.98,0,0,False,False
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
