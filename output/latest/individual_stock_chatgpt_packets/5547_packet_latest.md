# INDIVIDUAL STOCK CHATGPT PACKET - 5547 久舜

## Metadata
- generated_at: 2026-05-26 22:19:53 Asia/Taipei
- stock_id: 5547
- stock_name: 久舜
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 70
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5547_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5547_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5547_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5547_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5547_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5547_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5547_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5547_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5547_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5547_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5547_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5547_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5547_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5547_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5547_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5547_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5547_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5547_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5547.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5547.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5547.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5547.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5547.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5547.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5547_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5547_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5547_latest.md?ref=main

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
- open: 21.6
- high: 21.8
- low: 21.6
- close: 21.6
- volume: 22000
- ma5: 21.54
- ema23_primary: 21.6
- distance_to_ema23_pct: -0.02
- ma20: 21.52
- ma60: 22.05
- ma120: 22.16
- return_5d: 0.7
- return_20d: 3.35
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: 0.38
- distance_to_high_60_pct: -7.1

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,21,21,20.85,20.9,43000,21.87,-4.43,21.92,22.38,0.72
20260429,20.9,21.05,20.9,21.05,16000,21.8,-3.44,21.85,22.36,0.28
20260430,21.05,22,20.95,21.9,39000,21.81,0.42,21.83,22.35,0.72
20260504,21.9,21.9,21.1,21.2,35000,21.76,-2.56,21.77,22.33,0.66
20260505,21.8,21.9,21.6,21.6,30000,21.74,-0.67,21.74,22.31,0.56
20260506,21.6,21.9,21.5,21.7,45000,21.74,-0.19,21.7,22.3,0.84
20260507,21.6,21.85,21.55,21.85,12000,21.75,0.46,21.67,22.29,0.24
20260508,21.8,21.85,21.75,21.75,10000,21.75,-0,21.64,22.28,0.2
20260511,22,22.05,21.85,21.85,85000,21.76,0.42,21.63,22.28,1.61
20260512,21.95,22.05,21.6,22,35000,21.78,1.02,21.62,22.27,0.66
20260513,21.7,21.7,21.3,21.35,69000,21.74,-1.81,21.58,22.23,1.3
20260514,21.4,21.4,21.35,21.35,16000,21.71,-1.66,21.54,22.2,0.32
20260515,21.35,21.6,21.3,21.35,41000,21.68,-1.52,21.5,22.17,0.81
20260518,21.35,21.4,21.3,21.35,15000,21.65,-1.4,21.47,22.14,0.34
20260519,21.4,21.45,21.35,21.45,34000,21.64,-0.86,21.45,22.12,0.76
20260520,21.6,21.7,21.45,21.5,25000,21.62,-0.58,21.45,22.11,0.61
20260521,21.5,21.5,21.4,21.4,26000,21.61,-0.95,21.45,22.09,0.66
20260522,21.4,21.6,21.35,21.6,21000,21.61,-0.02,21.47,22.08,0.58
20260525,21.6,21.65,21.5,21.6,22000,21.6,-0.02,21.48,22.06,0.63
20260526,21.6,21.8,21.6,21.6,22000,21.6,-0.02,21.52,22.05,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 65.82
- over_600_ratio: 63.95
- over_800_ratio: 62.55
- over_1000_ratio: 54.69
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
20260430,66.8,,62.55,,54.69,,0,False,False
20260508,66.74,-0.06,62.55,0,54.69,0,0,False,False
20260515,65.82,-0.92,62.55,0,54.69,0,0,False,False
20260522,65.82,0,62.55,0,54.69,0,0,False,False
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
