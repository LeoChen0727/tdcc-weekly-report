# INDIVIDUAL STOCK CHATGPT PACKET - 6910 德鴻

## Metadata
- generated_at: 2026-05-26 21:26:41 Asia/Taipei
- stock_id: 6910
- stock_name: 德鴻
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 106
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6910_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6910_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6910_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6910_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6910_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6910_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6910_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6910_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6910_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6910_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6910_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6910_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6910_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6910_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6910_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6910_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6910_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6910_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6910.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6910.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6910.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6910.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6910.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6910.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6910_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6910_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6910_latest.md?ref=main

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
- open: 28.05
- high: 28.05
- low: 27.55
- close: 27.55
- volume: 28000
- ma5: 27.91
- ema23_primary: 28.28
- distance_to_ema23_pct: -2.58
- ma20: 28.23
- ma60: 29.72
- ma120: 32.38
- return_5d: 4.36
- return_20d: -6.13
- volume_ratio: 0.5
- distance_to_ma20_pct_auxiliary: -2.41
- distance_to_high_60_pct: -20.49

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,29.2,30,29.2,29.3,51000,29.88,-1.93,29.48,32.01,0.59
20260429,29.3,29.7,29.25,29.45,71000,29.84,-1.31,29.49,31.89,0.8
20260430,29.45,29.9,29.45,29.9,47000,29.85,0.18,29.57,31.77,0.55
20260504,29.3,29.4,29.1,29.35,54000,29.81,-1.53,29.6,31.64,0.63
20260505,29.3,29.45,29.25,29.45,53000,29.78,-1.09,29.57,31.51,0.67
20260506,29.6,29.65,29.05,29.1,100000,29.72,-2.08,29.56,31.37,1.26
20260507,29.1,29.2,28.65,28.9,146000,29.65,-2.53,29.5,31.23,1.81
20260508,28.9,28.9,28.6,28.75,85000,29.58,-2.79,29.46,31.12,1.02
20260511,28.75,28.75,28.3,28.4,81000,29.48,-3.66,29.39,31.01,0.95
20260512,28.25,28.25,27.6,28,85000,29.35,-4.62,29.3,30.89,0.99
20260513,27.65,27.65,27.55,27.65,26000,29.21,-5.35,29.2,30.78,0.31
20260514,27.35,27.35,27.05,27.15,88000,29.04,-6.51,29.1,30.64,1.16
20260515,27.15,27.15,26.75,26.75,33000,28.85,-7.28,28.98,30.5,0.46
20260518,26.5,26.55,26.3,26.5,33000,28.65,-7.52,28.83,30.35,0.47
20260519,26.5,26.5,26.4,26.4,22000,28.47,-7.26,28.68,30.22,0.32
20260520,27.5,27.5,26.45,26.9,25000,28.34,-5.07,28.52,30.1,0.38
20260521,28.6,28.6,27.45,28,45000,28.31,-1.09,28.42,30,0.71
20260522,28.2,28.8,28,28.8,28000,28.35,1.59,28.38,29.91,0.47
20260525,29,29,28.2,28.3,28000,28.34,-0.16,28.32,29.82,0.47
20260526,28.05,28.05,27.55,27.55,28000,28.28,-2.58,28.23,29.72,0.5
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.79
- over_600_ratio: 52.47
- over_800_ratio: 52.47
- over_1000_ratio: 49.29
- over_400_change_1w: 0.02
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.77,,52.45,,49.27,,0,False,False
20260508,56.77,0,52.45,0,49.27,0,0,False,False
20260515,56.77,0,52.45,0,49.27,0,0,False,False
20260522,56.79,0.02,52.47,0.02,49.29,0.02,1,True,True
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
