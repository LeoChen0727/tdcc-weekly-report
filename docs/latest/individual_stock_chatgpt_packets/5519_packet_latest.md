# INDIVIDUAL STOCK CHATGPT PACKET - 5519 隆大

## Metadata
- generated_at: 2026-05-26 23:54:23 Asia/Taipei
- stock_id: 5519
- stock_name: 隆大
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5519_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5519_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5519_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5519_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5519_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5519_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5519_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5519_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5519_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5519_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5519_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5519_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5519_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5519_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5519_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5519_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5519_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5519_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5519.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5519.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5519.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5519.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5519.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5519.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5519_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5519_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5519_latest.md?ref=main

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
- open: 32.3
- high: 32.5
- low: 32.1
- close: 32.25
- volume: 317430
- ma5: 32.51
- ema23_primary: 32.58
- distance_to_ema23_pct: -1
- ma20: 32.52
- ma60: 32.99
- ma120: 32.53
- return_5d: -0.62
- return_20d: -0.15
- volume_ratio: 0.85
- distance_to_ma20_pct_auxiliary: -0.81
- distance_to_high_60_pct: -9.28

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,32.5,32.55,32.15,32.25,406382,32.98,-2.2,33.05,32.53,0.8
20260429,32.5,32.75,32.3,32.7,394775,32.95,-0.77,33.02,32.55,0.79
20260430,32.75,32.75,32.4,32.55,271023,32.92,-1.12,33.01,32.55,0.55
20260504,32.55,32.6,32.25,32.35,274157,32.87,-1.59,32.95,32.57,0.56
20260505,32.35,32.6,32.3,32.55,247121,32.85,-0.9,32.92,32.58,0.5
20260506,32.65,32.7,32.4,32.5,474381,32.82,-0.97,32.89,32.6,0.94
20260507,32.5,33.15,32.5,33.15,521123,32.84,0.93,32.88,32.63,1.02
20260508,33.2,33.25,32.8,33.1,346930,32.87,0.71,32.87,32.67,0.67
20260511,33.1,33.1,32.7,32.95,459053,32.87,0.23,32.85,32.7,0.88
20260512,33,33,32.6,32.7,397585,32.86,-0.48,32.82,32.74,0.78
20260513,32.6,32.6,32.3,32.35,520482,32.82,-1.42,32.77,32.77,1.01
20260514,32.35,32.4,32.1,32.1,465217,32.76,-2,32.71,32.8,0.9
20260515,32.15,32.15,31.9,31.95,463879,32.69,-2.26,32.63,32.82,0.91
20260518,31.95,32.25,31.75,32.1,253171,32.64,-1.65,32.59,32.85,0.55
20260519,32.35,32.7,32.3,32.45,357084,32.62,-0.53,32.58,32.88,0.82
20260520,32.45,32.7,32.3,32.6,203406,32.62,-0.07,32.58,32.92,0.48
20260521,32.65,32.85,32.65,32.75,230700,32.63,0.36,32.57,32.95,0.56
20260522,32.75,32.95,32.6,32.65,365403,32.63,0.05,32.55,32.97,0.92
20260525,32.65,32.65,32.1,32.3,529988,32.61,-0.94,32.52,32.98,1.31
20260526,32.3,32.5,32.1,32.25,317430,32.58,-1,32.52,32.99,0.85
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.37
- over_600_ratio: 54.74
- over_800_ratio: 51.85
- over_1000_ratio: 51.49
- over_400_change_1w: 0.35
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.23,,51.85,,51.49,,0,False,False
20260508,58.44,0.21,52.23,0.38,51.49,0,1,False,True
20260515,58.02,-0.42,51.85,-0.38,51.49,0,0,False,False
20260522,58.37,0.35,51.85,0,51.49,0,1,False,False
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
