# INDIVIDUAL STOCK CHATGPT PACKET - 3540 曜越

## Metadata
- generated_at: 2026-05-29 19:32:38 Asia/Taipei
- stock_id: 3540
- stock_name: 曜越
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3540_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3540_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3540_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3540_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3540_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3540_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3540_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3540_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3540_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3540_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3540_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3540_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3540_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3540_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3540_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3540_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3540_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3540_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3540.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3540.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3540.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3540.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3540.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3540.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3540_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3540_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3540_latest.md?ref=main

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
- open: 27.2
- high: 27.2
- low: 26.3
- close: 26.45
- volume: 27000
- ma5: 26.54
- ema23_primary: 26.76
- distance_to_ema23_pct: -1.16
- ma20: 26.78
- ma60: 27.54
- ma120: 29.29
- return_5d: 0.76
- return_20d: -5.03
- volume_ratio: 0.12
- distance_to_ma20_pct_auxiliary: -1.22
- distance_to_high_60_pct: -13.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,28.2,28.45,27.8,28,221000,27.81,0.67,27.36,28.83,0.51
20260505,28.05,28.55,28,28.1,188000,27.84,0.94,27.41,28.75,0.43
20260506,28.2,28.2,27.2,27.2,414000,27.79,-2.11,27.45,28.65,0.91
20260507,27.75,28.2,27.1,27.9,277000,27.79,0.38,27.5,28.58,0.61
20260508,28.4,28.4,27.3,27.35,209000,27.76,-1.47,27.56,28.5,0.46
20260511,27.4,27.8,27,27.7,324000,27.75,-0.19,27.63,28.44,0.69
20260512,27.6,28.25,26.55,27.95,705000,27.77,0.65,27.74,28.4,1.44
20260513,28.2,28.2,27.2,27.2,303000,27.72,-1.88,27.76,28.34,0.62
20260514,27.75,27.75,26.6,26.65,432000,27.63,-3.56,27.74,28.27,0.87
20260515,26.9,26.9,26,26.2,361000,27.51,-4.77,27.69,28.2,0.72
20260518,25.65,25.95,25.45,25.9,171000,27.38,-5.4,27.63,28.13,0.34
20260519,25.9,26.2,25.55,25.55,278000,27.23,-6.16,27.55,28.06,0.55
20260520,25.65,25.75,25.2,25.3,179000,27.07,-6.52,27.45,27.98,0.35
20260521,25.5,25.75,25.4,25.6,222000,26.94,-4.99,27.34,27.91,0.44
20260522,25.65,26.5,25.65,26.25,26000,26.89,-2.36,27.21,27.85,0.06
20260525,26.55,27.3,26.2,26.75,27000,26.87,-0.46,27.06,27.79,0.09
20260526,26.75,26.9,26.4,26.45,27000,26.84,-1.45,26.98,27.73,0.1
20260527,26.55,27.1,26.5,26.55,27000,26.82,-0.99,26.92,27.66,0.11
20260528,26.55,27.75,26.5,26.5,27000,26.79,-1.08,26.85,27.6,0.11
20260529,27.2,27.2,26.3,26.45,27000,26.76,-1.16,26.78,27.54,0.12
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 22.84
- over_600_ratio: 22.24
- over_800_ratio: 22.24
- over_1000_ratio: 22.24
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
20260430,23.58,,22.24,,22.24,,0,False,False
20260508,22.99,-0.59,22.24,0,22.24,0,0,False,False
20260515,22.84,-0.15,22.24,0,22.24,0,0,False,False
20260522,22.84,0,22.24,0,22.24,0,0,False,False
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
