# INDIVIDUAL STOCK CHATGPT PACKET - 1903 士紙

## Metadata
- generated_at: 2026-05-30 23:41:11 Asia/Taipei
- stock_id: 1903
- stock_name: 士紙
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1903_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1903_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1903_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1903_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1903_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1903_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1903_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1903_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1903_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1903_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1903_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1903_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1903_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1903_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1903_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1903_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1903_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1903_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1903.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1903.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1903.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1903.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1903.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1903.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1903_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1903_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1903_latest.md?ref=main

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
- open: 49.05
- high: 49.4
- low: 48.85
- close: 49.2
- volume: 197745
- ma5: 49.51
- ema23_primary: 48.97
- distance_to_ema23_pct: 0.48
- ma20: 48.77
- ma60: 49.53
- ma120: 52.55
- return_5d: 2.61
- return_20d: -0.51
- volume_ratio: 0.76
- distance_to_ma20_pct_auxiliary: 0.88
- distance_to_high_60_pct: -7.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,49.45,49.6,49.3,49.45,125008,49.74,-0.58,49.49,51.63,0.58
20260505,49.45,50.2,49.1,49.45,204490,49.71,-0.53,49.55,51.46,1.05
20260506,49.75,49.75,47.8,49.15,306760,49.67,-1.04,49.55,51.3,1.52
20260507,49.3,49.65,49.25,49.5,116162,49.65,-0.31,49.53,51.14,0.58
20260508,49.55,49.85,49.25,49.3,147554,49.62,-0.65,49.5,50.99,0.74
20260511,49.3,49.5,49.25,49.3,115729,49.6,-0.6,49.45,50.87,0.57
20260512,49.3,49.3,48.3,48.5,312151,49.5,-2.03,49.38,50.77,1.58
20260513,48.5,48.5,48.2,48.3,141219,49.4,-2.24,49.32,50.67,0.73
20260514,48.05,48.3,47.55,47.55,319984,49.25,-3.45,49.25,50.54,1.61
20260515,47.6,49.6,47.6,48.1,538898,49.15,-2.14,49.18,50.43,2.48
20260518,48.1,48.15,47.6,47.7,178999,49.03,-2.72,49.1,50.33,0.82
20260519,48.2,48.7,47.8,47.9,207773,48.94,-2.12,49.05,50.23,0.95
20260520,48.1,48.3,47.55,47.65,170928,48.83,-2.42,48.95,50.1,0.78
20260521,47.85,48.1,47.7,48.05,118566,48.77,-1.47,48.83,49.98,0.58
20260522,48,48.5,47.9,47.95,182981,48.7,-1.54,48.76,49.88,0.94
20260525,48.95,50.5,48.55,50.2,606373,48.82,2.82,48.8,49.82,2.76
20260526,50.6,52.6,49.75,49.9,441103,48.91,2.02,48.83,49.76,1.88
20260527,50,50.5,48.8,49.25,424995,48.94,0.63,48.83,49.68,1.7
20260528,49.25,50,49,49,324125,48.95,0.11,48.78,49.6,1.26
20260529,49.05,49.4,48.85,49.2,197745,48.97,0.48,48.77,49.53,0.76
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 80.61
- over_600_ratio: 78.57
- over_800_ratio: 77.74
- over_1000_ratio: 74.58
- over_400_change_1w: -0.14
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.84,,77.37,,74.53,,0,False,False
20260508,80.87,0.03,77.66,0.29,74.52,-0.01,1,False,True
20260515,80.74,-0.13,77.71,0.05,74.56,0.04,2,False,True
20260522,80.75,0.01,77.72,0.01,74.56,0,3,False,True
20260529,80.61,-0.14,77.74,0.02,74.58,0.02,4,False,True
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
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 1903 | 士紙 | 3 | 0 | 22500.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
