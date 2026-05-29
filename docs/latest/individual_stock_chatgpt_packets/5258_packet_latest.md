# INDIVIDUAL STOCK CHATGPT PACKET - 5258 虹堡

## Metadata
- generated_at: 2026-05-29 19:33:04 Asia/Taipei
- stock_id: 5258
- stock_name: 虹堡
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5258_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5258_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5258_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5258_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5258_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5258_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5258_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5258_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5258_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5258_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5258_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5258_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5258_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5258_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5258_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5258_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5258_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5258_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5258.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5258.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5258.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5258.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5258.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5258.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5258_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5258_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5258_latest.md?ref=main

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
- open: 51.7
- high: 51.8
- low: 49.95
- close: 50
- volume: 1960853
- ma5: 53.66
- ema23_primary: 53.42
- distance_to_ema23_pct: -6.41
- ma20: 53.98
- ma60: 49.72
- ma120: 56.88
- return_5d: -13.19
- return_20d: 4.93
- volume_ratio: 0.85
- distance_to_ma20_pct_auxiliary: -7.38
- distance_to_high_60_pct: -20.63

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,47.65,48.05,46.9,47.5,611889,48.47,-2,48.39,50.02,1.18
20260505,47.8,48.75,47.35,48.75,500108,48.49,0.53,48.48,49.81,0.94
20260506,49.9,49.9,48.05,48.45,565150,48.49,-0.08,48.65,49.61,1.07
20260507,48.9,48.9,47.95,48.5,428177,48.49,0.02,48.74,49.41,0.8
20260508,48.95,53.3,48.9,53.3,2531194,48.89,9.02,49.1,49.31,3.89
20260511,55.8,57,53.1,54.3,5599519,49.34,10.05,49.48,49.27,6.1
20260512,54.5,54.9,51.6,53.2,1921065,49.66,7.12,49.75,49.23,1.96
20260513,50.1,56.6,49.9,56.6,2786827,50.24,12.65,50.2,49.24,2.53
20260514,57.1,61,54.5,55.7,4603021,50.7,9.87,50.57,49.22,3.55
20260515,54,58.4,53.3,53.5,2849217,50.93,5.05,50.72,49.17,2.05
20260518,57.2,58.8,55.4,58.8,1742017,51.59,13.98,51.06,49.24,1.22
20260519,57.7,63,56.1,60,4429958,52.29,14.75,51.52,49.33,2.75
20260520,58,59.4,57,58,2884898,52.76,9.92,51.85,49.38,1.67
20260521,58.3,60,57,57.2,2773983,53.13,7.65,52.14,49.48,1.52
20260522,57.3,59.2,56.1,57.6,1997455,53.51,7.65,52.53,49.57,1.05
20260525,57.9,58.8,56.7,58.3,1359018,53.91,8.15,53.02,49.66,0.7
20260526,59,59,56.2,57,1423020,54.16,5.24,53.48,49.74,0.72
20260527,57.3,57.8,51.6,52,3663026,53.98,-3.67,53.7,49.73,1.7
20260528,52.3,53.4,50.3,51,1357276,53.73,-5.09,53.87,49.72,0.61
20260529,51.7,51.8,49.95,50,1960853,53.42,-6.41,53.98,49.72,0.85
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 50.8
- over_600_ratio: 44.98
- over_800_ratio: 41.26
- over_1000_ratio: 37.99
- over_400_change_1w: -0.26
- over_800_change_1w: 0.25
- over_1000_change_1w: 1.03
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.67,,41.46,,38.16,,0,False,False
20260508,52.95,-0.72,41.33,-0.13,38.03,-0.13,0,False,False
20260515,51.06,-1.89,41.01,-0.32,36.96,-1.07,0,False,False
20260522,50.8,-0.26,41.26,0.25,37.99,1.03,1,False,True
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
| 20260529 | 5258 | 虹堡 | 1 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
