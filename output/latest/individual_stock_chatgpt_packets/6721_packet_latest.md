# INDIVIDUAL STOCK CHATGPT PACKET - 6721 信實

## Metadata
- generated_at: 2026-05-26 21:26:34 Asia/Taipei
- stock_id: 6721
- stock_name: 信實
- packet_status: standard_180d_window_packet
- latest_price_date: 20260525
- price_rows: 122
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6721_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6721_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6721_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6721_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6721_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6721_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6721_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6721_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6721_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6721_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6721_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6721_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6721_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6721_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6721_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6721_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6721_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6721_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6721.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6721.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6721.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6721.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6721.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6721.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6721_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6721_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6721_latest.md?ref=main

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
- date: 20260525
- open: 58.7
- high: 59
- low: 58.5
- close: 59
- volume: 59000
- ma5: 59.1
- ema23_primary: 58.44
- distance_to_ema23_pct: 0.97
- ma20: 58.02
- ma60: 59.34
- ma120: 60.51
- return_5d: 1.9
- return_20d: 0.85
- volume_ratio: 4.61
- distance_to_ma20_pct_auxiliary: 1.68
- distance_to_high_60_pct: -4.99

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260427,58,58.1,57.1,57.1,13000,58.86,-2.99,58.68,60.63,0.8
20260428,57.8,57.8,57.8,57.8,1000,58.77,-1.66,58.59,60.58,0.06
20260429,57.6,58,57.6,57.9,5000,58.7,-1.36,58.53,60.51,0.31
20260430,57.9,57.9,57.7,57.7,4000,58.62,-1.56,58.45,60.44,0.25
20260504,57.7,57.7,57.1,57.1,3000,58.49,-2.38,58.35,60.35,0.19
20260505,57.8,57.8,57.8,57.8,1000,58.43,-1.08,58.27,60.28,0.06
20260506,58,58,58,58,6000,58.4,-0.68,58.22,60.22,0.38
20260507,57.1,57.8,57.1,57.8,10000,58.35,-0.94,58.16,60.15,0.69
20260508,57.8,57.8,57.5,57.6,4000,58.28,-1.18,58.12,60.07,0.31
20260511,57.6,57.6,57.1,57.5,23000,58.22,-1.24,58.02,59.99,1.9
20260512,57.2,57.5,57.1,57.5,6000,58.16,-1.13,57.97,59.9,0.6
20260513,57.5,57.6,57.1,57.6,8000,58.11,-0.88,57.92,59.82,1.06
20260514,58,58,57.5,57.9,8000,58.1,-0.34,57.87,59.74,1.02
20260515,57.9,57.9,57.7,57.8,4000,58.07,-0.47,57.83,59.66,0.52
20260518,57.9,57.9,57.5,57.9,14000,58.06,-0.27,57.8,59.59,1.7
20260519,58.1,58.5,58.1,58.5,2000,58.09,0.7,57.8,59.54,0.26
20260520,58,58.5,57.9,58.5,9000,58.13,0.64,57.81,59.47,1.15
20260521,58.3,61.4,58.3,60,16000,58.28,2.95,57.92,59.44,2.13
20260522,59.8,61.3,58.5,59.5,60000,58.38,1.91,58,59.39,5.88
20260525,58.7,59,58.5,59,59000,58.44,0.97,58.02,59.34,4.61
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 51.92
- over_600_ratio: 45.07
- over_800_ratio: 35.65
- over_1000_ratio: 35.65
- over_400_change_1w: 0.28
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,51.64,,35.65,,35.65,,0,False,False
20260508,51.64,0,35.65,0,35.65,0,0,False,False
20260515,51.64,0,35.65,0,35.65,0,0,False,False
20260522,51.92,0.28,35.65,0,35.65,0,1,False,False
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
