# INDIVIDUAL STOCK CHATGPT PACKET - 1210 大成

## Metadata
- generated_at: 2026-05-28 19:31:26 Asia/Taipei
- stock_id: 1210
- stock_name: 大成
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1210_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1210_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1210_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1210_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1210_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1210_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1210_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1210_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1210_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1210_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1210_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1210_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1210_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1210_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1210_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1210_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1210_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1210_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1210.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1210.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1210.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1210.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1210.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1210.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1210_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1210_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1210_latest.md?ref=main

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
- date: 20260528
- open: 51.7
- high: 52
- low: 51.6
- close: 51.8
- volume: 2413257
- ma5: 52.02
- ema23_primary: 52.68
- distance_to_ema23_pct: -1.68
- ma20: 52.51
- ma60: 53.21
- ma120: 52.37
- return_5d: -2.08
- return_20d: -3.54
- volume_ratio: 1.13
- distance_to_ma20_pct_auxiliary: -1.34
- distance_to_high_60_pct: -7.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,53.8,53.8,53.2,53.4,1675829,53.9,-0.93,54.27,52.84,0.72
20260504,53.4,53.4,52.4,52.6,3276791,53.79,-2.21,54.16,52.84,1.37
20260505,52.6,52.6,52.1,52.4,1881368,53.67,-2.37,54.05,52.84,0.8
20260506,52.4,52.4,51.8,52,2593678,53.54,-2.87,53.91,52.85,1.11
20260507,52,52.5,51.9,52.3,1287351,53.43,-2.12,53.8,52.86,0.57
20260508,52.2,52.9,52.2,52.9,1921851,53.39,-0.91,53.72,52.88,0.84
20260511,52.8,53,52.1,52.3,2608180,53.3,-1.87,53.62,52.9,1.1
20260512,52.3,52.6,52,52.1,2474523,53.2,-2.06,53.47,52.93,1.06
20260513,52.1,52.5,52,52.3,1705869,53.12,-1.55,53.38,52.95,0.74
20260514,52.3,52.9,52.3,52.6,1734524,53.08,-0.9,53.27,52.98,0.77
20260515,52.6,53.2,52.6,52.9,2142428,53.06,-0.31,53.17,53.01,0.94
20260518,52.9,53.4,52.5,52.8,1932609,53.04,-0.46,53.1,53.04,0.85
20260519,53,54.1,53,53.5,2553880,53.08,0.79,53.02,53.09,1.15
20260520,53.5,53.6,52.8,53,1669943,53.07,-0.14,52.97,53.12,0.79
20260521,53.1,53.5,52.9,52.9,1506691,53.06,-0.3,52.91,53.15,0.73
20260522,53,53,52.3,52.4,2137410,53,-1.14,52.85,53.16,1.08
20260525,52.4,52.4,52,52.1,2601117,52.93,-1.57,52.8,53.17,1.29
20260526,52.3,52.6,52,52.1,1760583,52.86,-1.44,52.72,53.19,0.88
20260527,52.3,52.4,51.6,51.7,2773905,52.76,-2.01,52.6,53.2,1.34
20260528,51.7,52,51.6,51.8,2413257,52.68,-1.68,52.51,53.21,1.13
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 63.02
- over_600_ratio: 61.03
- over_800_ratio: 59.88
- over_1000_ratio: 58.9
- over_400_change_1w: 0.13
- over_800_change_1w: 0.25
- over_1000_change_1w: 0.26
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.5,,60.28,,59.32,,0,False,False
20260508,63,-0.5,59.8,-0.48,58.73,-0.59,0,False,False
20260515,62.89,-0.11,59.63,-0.17,58.64,-0.09,0,False,False
20260522,63.02,0.13,59.88,0.25,58.9,0.26,1,True,True
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
| 20260528 | 1210 | 大成 | 1 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
