# INDIVIDUAL STOCK CHATGPT PACKET - 6222 立軒

## Metadata
- generated_at: 2026-05-30 23:42:57 Asia/Taipei
- stock_id: 6222
- stock_name: 立軒
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 272
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6222_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6222_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6222_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6222_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6222_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6222_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6222_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6222_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6222_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6222_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6222_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6222_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6222_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6222_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6222_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6222_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6222_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6222_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6222.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6222.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6222.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6222.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6222.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6222.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6222_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6222_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6222_latest.md?ref=main

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
- open: 20.6
- high: 21
- low: 20.2
- close: 21
- volume: 20000
- ma5: 20.93
- ema23_primary: 21.2
- distance_to_ema23_pct: -0.95
- ma20: 21.62
- ma60: 20.85
- ma120: 19.98
- return_5d: 1.94
- return_20d: -3.45
- volume_ratio: 1.05
- distance_to_ma20_pct_auxiliary: -2.88
- distance_to_high_60_pct: -11.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,21.75,23.1,21.75,23.1,43000,21.05,9.72,21.04,20,1.11
20260505,23.1,23.6,22.45,22.65,53000,21.19,6.91,21.14,20.07,1.3
20260506,22.65,22.75,22.55,22.55,15000,21.3,5.87,21.22,20.13,0.37
20260507,23,23,22.45,22.95,24000,21.44,7.06,21.33,20.21,0.65
20260508,23,23,22.35,22.35,12000,21.51,3.89,21.41,20.26,0.33
20260511,22.95,23,22.25,22.9,39000,21.63,5.88,21.52,20.33,1.02
20260512,23.05,23.4,22.3,22.45,21000,21.7,3.47,21.6,20.39,0.54
20260513,22.4,22.5,22,22,12000,21.72,1.28,21.67,20.45,0.33
20260514,22,22,21.75,21.75,4000,21.72,0.12,21.71,20.5,0.12
20260515,21.05,21.05,21.05,21.05,2000,21.67,-2.85,21.72,20.54,0.06
20260518,21.05,21.8,21,21,9000,21.61,-2.84,21.73,20.58,0.27
20260519,21.6,21.6,21,21,16000,21.56,-2.61,21.74,20.61,0.52
20260520,20.55,20.7,20.55,20.7,5000,21.49,-3.68,21.73,20.64,0.18
20260521,20.75,20.75,20.75,20.75,2000,21.43,-3.17,21.73,20.67,0.07
20260522,20.6,20.6,20.2,20.6,20000,21.36,-3.55,21.71,20.69,0.8
20260525,20.9,22.65,19.8,21.5,21000,21.37,0.6,21.76,20.74,0.83
20260526,21.5,21.5,20.45,20.75,21000,21.32,-2.67,21.75,20.78,0.86
20260527,20.9,21,20.7,20.7,21000,21.27,-2.67,21.71,20.8,0.87
20260528,20.7,20.7,20.6,20.7,21000,21.22,-2.45,21.66,20.82,0.95
20260529,20.6,21,20.2,21,20000,21.2,-0.95,21.62,20.85,1.05
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 90.1
- over_600_ratio: 88.49
- over_800_ratio: 86.44
- over_1000_ratio: 84.52
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
20260430,90.1,,86.44,,84.52,,0,False,False
20260508,90.1,0,86.44,0,84.52,0,0,False,False
20260515,90.1,0,86.44,0,84.52,0,0,False,False
20260522,90.1,0,86.44,0,84.52,0,0,False,False
20260529,90.1,0,86.44,0,84.52,0,0,False,False
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
