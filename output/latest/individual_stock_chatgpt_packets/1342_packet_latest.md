# INDIVIDUAL STOCK CHATGPT PACKET - 1342 八貫

## Metadata
- generated_at: 2026-05-30 23:40:56 Asia/Taipei
- stock_id: 1342
- stock_name: 八貫
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1342_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1342_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1342_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1342_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1342_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1342_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1342_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1342_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1342_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1342_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1342_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1342_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1342_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1342_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1342_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1342_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1342_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1342_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1342.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1342.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1342.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1342.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1342.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1342.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1342_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1342_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1342_latest.md?ref=main

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
- open: 91.7
- high: 92.4
- low: 91
- close: 91.6
- volume: 215666
- ma5: 92.16
- ema23_primary: 92.8
- distance_to_ema23_pct: -1.29
- ma20: 93.39
- ma60: 91.28
- ma120: 92
- return_5d: -2.76
- return_20d: -0.43
- volume_ratio: 0.74
- distance_to_ma20_pct_auxiliary: -1.91
- distance_to_high_60_pct: -11.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,93.1,94.4,92.2,93.9,237010,92.19,1.86,91.75,92.86,0.43
20260505,92.7,94.1,92.4,93.1,237029,92.27,0.9,92.22,92.83,0.43
20260506,94.2,94.7,92.5,93.8,529774,92.39,1.52,92.56,92.8,0.97
20260507,94.8,96,94.1,95.6,525680,92.66,3.17,92.9,92.82,0.96
20260508,96.1,96.5,93.3,94.2,415981,92.79,1.52,93.22,92.82,0.74
20260511,94.4,95.6,94.1,95.5,298776,93.01,2.67,93.59,92.86,0.53
20260512,95.6,95.6,94.4,95,215867,93.18,1.95,93.9,92.87,0.39
20260513,94.3,94.9,93.8,94.3,286343,93.27,1.1,94.16,92.88,0.51
20260514,94.6,95.2,93.1,93.5,310006,93.29,0.22,94.42,92.84,0.55
20260515,93.6,95.1,93,93.2,261308,93.28,-0.09,94.48,92.78,0.47
20260518,92.7,93.5,91,93.5,166127,93.3,0.21,94.6,92.67,0.3
20260519,93.1,94.1,91.9,91.9,230523,93.19,-1.38,94.56,92.5,0.42
20260520,91.9,92.3,91,92,179427,93.09,-1.17,94.22,92.33,0.38
20260521,92.3,94.6,92.3,93.2,211385,93.1,0.11,93.92,92.21,0.47
20260522,93.2,95.3,93,94.2,354050,93.19,1.09,93.63,92.08,0.9
20260525,94.3,94.5,92.5,93.3,287556,93.2,0.11,93.48,91.92,0.91
20260526,93.3,93.3,92.2,92.7,158651,93.16,-0.49,93.51,91.75,0.55
20260527,92.9,94,91.5,91.8,398250,93.04,-1.34,93.51,91.58,1.38
20260528,91.4,92.3,90.3,91.4,273258,92.91,-1.62,93.41,91.42,0.95
20260529,91.7,92.4,91,91.6,215666,92.8,-1.29,93.39,91.28,0.74
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 56.2
- over_600_ratio: 53.19
- over_800_ratio: 51.58
- over_1000_ratio: 51.58
- over_400_change_1w: 0.46
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.57,,51.58,,51.58,,0,False,False
20260508,55.67,0.1,51.58,0,51.58,0,1,False,False
20260515,55.75,0.08,51.58,0,51.58,0,2,False,False
20260522,55.74,-0.01,51.58,0,51.58,0,0,False,False
20260529,56.2,0.46,51.58,0,51.58,0,1,False,False
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
