# INDIVIDUAL STOCK CHATGPT PACKET - 6418 詠昇

## Metadata
- generated_at: 2026-05-29 19:33:26 Asia/Taipei
- stock_id: 6418
- stock_name: 詠昇
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6418_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6418_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6418_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6418_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6418_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6418_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6418_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6418_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6418_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6418_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6418_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6418_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6418_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6418_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6418_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6418_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6418_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6418_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6418.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6418.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6418.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6418.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6418.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6418.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6418_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6418_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6418_latest.md?ref=main

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
- open: 31.05
- high: 31.05
- low: 29.5
- close: 29.55
- volume: 30000
- ma5: 29.94
- ema23_primary: 30.89
- distance_to_ema23_pct: -4.33
- ma20: 31.11
- ma60: 30.98
- ma120: 36.15
- return_5d: -5.89
- return_20d: -13.6
- volume_ratio: 0.16
- distance_to_ma20_pct_auxiliary: -5
- distance_to_high_60_pct: -25.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,35,35,33,33,336000,32.11,2.78,31.07,32.09,0.89
20260505,33.2,35.2,33.2,33.7,283000,32.24,4.53,31.27,32.03,0.73
20260506,34.7,34.7,32.8,32.8,332000,32.29,1.59,31.45,31.96,0.82
20260507,32.85,33,32.05,32.15,230000,32.27,-0.39,31.59,31.88,0.56
20260508,32,33.55,31.6,31.8,301000,32.24,-1.35,31.75,31.8,0.72
20260511,30.9,31.5,30.9,31.3,104000,32.16,-2.67,31.89,31.75,0.25
20260512,30.95,31.9,30.55,31.9,216000,32.14,-0.73,32.08,31.72,0.5
20260513,31.85,34.5,31.65,32.6,483000,32.17,1.32,32.28,31.7,1.07
20260514,32.55,32.55,30.45,31,366000,32.08,-3.36,32.38,31.64,0.79
20260515,31,31,30,30,240000,31.9,-5.97,32.42,31.58,0.51
20260518,29.6,29.9,29.15,29.9,95000,31.74,-5.79,32.47,31.55,0.2
20260519,29.3,29.75,29.05,29.4,170000,31.54,-6.79,32.58,31.49,0.37
20260520,29.75,30.85,29.6,30.1,89000,31.42,-4.21,32.59,31.41,0.2
20260521,30.95,32.45,30.8,31.35,291000,31.42,-0.21,32.67,31.36,0.67
20260522,31.8,31.8,31,31.4,31000,31.41,-0.05,32.6,31.31,0.08
20260525,31,31.2,30.35,30.35,30000,31.33,-3.11,32.32,31.23,0.08
20260526,30.35,30.35,29.8,29.85,30000,31.2,-4.34,31.83,31.15,0.09
20260527,30.35,31,29.75,29.75,30000,31.08,-4.28,31.54,31.08,0.12
20260528,29.75,30.25,29.75,30.2,30000,31.01,-2.61,31.34,31.03,0.14
20260529,31.05,31.05,29.5,29.55,30000,30.89,-4.33,31.11,30.98,0.16
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.87
- over_600_ratio: 50.85
- over_800_ratio: 46.84
- over_1000_ratio: 46.84
- over_400_change_1w: -0.59
- over_800_change_1w: 0.06
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.11,,46.78,,46.78,,0,False,False
20260508,53.99,-0.12,46.78,0,46.78,0,0,False,False
20260515,55.46,1.47,46.78,0,46.78,0,1,False,False
20260522,54.87,-0.59,46.84,0.06,46.84,0.06,2,False,True
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
