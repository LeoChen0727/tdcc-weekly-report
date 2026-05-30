# INDIVIDUAL STOCK CHATGPT PACKET - 1786 科妍

## Metadata
- generated_at: 2026-05-30 23:41:10 Asia/Taipei
- stock_id: 1786
- stock_name: 科妍
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1786_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1786_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1786_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1786_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1786_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1786_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1786_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1786_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1786_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1786_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1786_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1786_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1786_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1786_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1786_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1786_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1786_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1786_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1786.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1786.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1786.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1786.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1786.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1786.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1786_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1786_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1786_latest.md?ref=main

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
- open: 52.8
- high: 53.1
- low: 52.2
- close: 52.6
- volume: 252191
- ma5: 53.36
- ema23_primary: 56.77
- distance_to_ema23_pct: -7.34
- ma20: 56.02
- ma60: 61.18
- ma120: 68.87
- return_5d: -9.62
- return_20d: -8.52
- volume_ratio: 0.46
- distance_to_ma20_pct_auxiliary: -6.11
- distance_to_high_60_pct: -26.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,57.5,58,55.4,55.9,414831,61.85,-9.62,61.41,67.4,1.36
20260505,55.9,57.5,55.5,56.2,399693,61.38,-8.44,61.19,67,1.34
20260506,56.9,58.5,56.2,58.1,448980,61.11,-4.92,61.09,66.64,1.45
20260507,57.5,57.6,56.6,57.6,277267,60.81,-5.29,60.92,66.23,0.88
20260508,57.2,58.2,56.8,56.8,264535,60.48,-6.08,60.8,65.82,0.85
20260511,56.7,56.7,55.6,56,311826,60.11,-6.83,60.59,65.45,0.98
20260512,56,56,52.8,54.2,709161,59.61,-9.08,60.27,65.08,2.07
20260513,53.6,54.5,53.3,54.4,178573,59.18,-8.08,59.8,64.71,0.54
20260514,53.6,54,51.3,51.5,745079,58.54,-12.03,59.2,64.32,2.15
20260515,54.8,56.6,53.5,56,2137006,58.33,-3.99,58.76,64,4.78
20260518,54.8,60.1,53.6,60,1418316,58.47,2.62,58.59,63.77,2.83
20260519,58.5,60,56.5,60,758831,58.6,2.4,58.38,63.56,1.44
20260520,58.3,62,57.9,59.3,555899,58.65,1.1,58.12,63.35,1.02
20260521,58.6,59.7,58.2,59.5,320323,58.72,1.32,57.89,63.15,0.58
20260522,58.7,59,58.2,58.2,293862,58.68,-0.82,57.62,62.86,0.53
20260525,58.7,58.7,55.1,55.1,489809,58.38,-5.62,57.33,62.54,0.87
20260526,55.1,55.2,53.6,53.6,309901,57.98,-7.56,56.94,62.2,0.55
20260527,53.8,54.2,53,53.3,283503,57.59,-7.45,56.58,61.84,0.51
20260528,53.4,53.5,52.1,52.2,371753,57.14,-8.65,56.27,61.51,0.68
20260529,52.8,53.1,52.2,52.6,252191,56.77,-7.34,56.02,61.18,0.46
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 50.97
- over_600_ratio: 46.82
- over_800_ratio: 45.11
- over_1000_ratio: 43.79
- over_400_change_1w: 0.19
- over_800_change_1w: 0.15
- over_1000_change_1w: 0.13
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,51.61,,44.45,,43.19,,0,False,False
20260508,50.92,-0.69,44.33,-0.12,43.05,-0.14,0,False,False
20260515,49.58,-1.34,44.36,0.03,43.08,0.03,1,False,True
20260522,50.78,1.2,44.96,0.6,43.66,0.58,2,True,True
20260529,50.97,0.19,45.11,0.15,43.79,0.13,3,True,True
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
| 20260529 | 1786 | 科妍 | 4 | 0 | 24590.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
