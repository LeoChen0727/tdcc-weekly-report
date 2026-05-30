# INDIVIDUAL STOCK CHATGPT PACKET - 2348 海悅

## Metadata
- generated_at: 2026-05-30 23:41:21 Asia/Taipei
- stock_id: 2348
- stock_name: 海悅
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2348_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2348_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2348_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2348_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2348_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2348_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2348_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2348_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2348_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2348_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2348_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2348_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2348_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2348_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2348_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2348_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2348_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2348_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2348.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2348.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2348.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2348.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2348.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2348.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2348_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2348_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2348_latest.md?ref=main

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
- open: 67.9
- high: 68.3
- low: 67.6
- close: 68.1
- volume: 188375
- ma5: 67.94
- ema23_primary: 70.24
- distance_to_ema23_pct: -3.05
- ma20: 69.73
- ma60: 74.08
- ma120: 76.79
- return_5d: -1.3
- return_20d: -4.22
- volume_ratio: 0.66
- distance_to_ma20_pct_auxiliary: -2.34
- distance_to_high_60_pct: -23.91

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,70.9,72.9,70.9,72,304523,75.27,-4.35,76.17,75.94,0.9
20260505,72.2,72.4,71.2,72,228768,75,-4,75.78,75.84,0.7
20260506,71.5,71.8,70.6,71.1,330010,74.68,-4.79,75.31,75.73,1.04
20260507,71.2,71.5,70.7,71.3,254195,74.39,-4.16,74.89,75.64,0.83
20260508,71.7,71.7,70.4,70.9,311024,74.1,-4.32,74.59,75.5,1.06
20260511,70.9,71.6,70.7,71,251697,73.84,-3.85,74.3,75.41,0.87
20260512,70.8,70.9,70,70.9,231706,73.6,-3.67,73.94,75.33,0.79
20260513,70.2,70.9,70.1,70.3,134689,73.32,-4.12,73.56,75.23,0.47
20260514,70.1,70.6,69.1,69.7,518389,73.02,-4.55,73.1,75.09,1.72
20260515,70,71.7,69.2,69.5,410267,72.73,-4.44,72.65,74.96,1.34
20260518,69.3,69.7,68.8,69.3,231263,72.44,-4.34,72.24,74.86,0.75
20260519,69.3,70.1,69.3,69.5,207965,72.2,-3.74,71.88,74.78,0.68
20260520,69.5,69.5,68.9,69.1,197378,71.94,-3.95,71.47,74.68,0.65
20260521,69.7,70,69.3,69.4,159505,71.73,-3.25,71.09,74.6,0.53
20260522,69.3,69.5,69,69,198293,71.5,-3.5,70.81,74.51,0.72
20260525,69,69.3,67.7,68.3,608426,71.23,-4.12,70.57,74.42,2.1
20260526,68.3,68.6,67.4,67.8,286170,70.95,-4.44,70.36,74.32,1.02
20260527,68,68.4,67.8,67.9,432858,70.69,-3.95,70.14,74.23,1.48
20260528,68.2,68.4,67.4,67.6,226248,70.44,-4.03,69.89,74.14,0.77
20260529,67.9,68.3,67.6,68.1,188375,70.24,-3.05,69.73,74.08,0.66
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 70.49
- over_600_ratio: 68.18
- over_800_ratio: 67.72
- over_1000_ratio: 67.12
- over_400_change_1w: -0.03
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.7,,68.39,,67.14,,0,False,False
20260508,70.62,-0.08,68.31,-0.08,67.13,-0.01,0,False,False
20260515,70.54,-0.08,68.23,-0.08,67.11,-0.02,0,False,False
20260522,70.52,-0.02,67.71,-0.52,67.11,0,0,False,False
20260529,70.49,-0.03,67.72,0.01,67.12,0.01,1,False,True
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
| 20260529 | 2348 | 海悅 | 9 | 0 | 10000.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
