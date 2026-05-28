# INDIVIDUAL STOCK CHATGPT PACKET - 2211 長榮鋼

## Metadata
- generated_at: 2026-05-28 20:18:33 Asia/Taipei
- stock_id: 2211
- stock_name: 長榮鋼
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2211_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2211_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2211_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2211_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2211_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2211_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2211_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2211_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2211_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2211_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2211_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2211_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2211_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2211_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2211_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2211_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2211_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2211_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2211.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2211.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2211.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2211.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2211.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2211.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2211_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2211_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2211_latest.md?ref=main

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
- open: 92.4
- high: 92.9
- low: 91.4
- close: 91.4
- volume: 601077
- ma5: 92.04
- ema23_primary: 94.88
- distance_to_ema23_pct: -3.67
- ma20: 95.08
- ma60: 98.59
- ma120: 102.2
- return_5d: -0.65
- return_20d: -7.68
- volume_ratio: 0.79
- distance_to_ma20_pct_auxiliary: -3.87
- distance_to_high_60_pct: -12.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,98.5,99,97.5,97.5,921013,99.63,-2.14,99.63,100.96,1.39
20260504,97.4,98.5,97.4,98.1,589502,99.5,-1.41,99.53,100.92,0.93
20260505,98.2,98.8,98.1,98.7,459269,99.44,-0.74,99.52,100.88,0.73
20260506,99.4,99.4,98.4,98.7,513067,99.37,-0.68,99.48,100.84,0.83
20260507,98.5,99.3,98.5,99.1,569278,99.35,-0.25,99.42,100.81,0.92
20260508,99.6,99.6,98,98.5,613286,99.28,-0.79,99.34,100.73,0.97
20260511,98.6,98.6,97.7,97.7,800693,99.15,-1.46,99.22,100.64,1.24
20260512,97.7,97.7,96.5,96.6,1228730,98.94,-2.36,99.07,100.57,1.81
20260513,96.6,96.7,96.1,96.4,709690,98.72,-2.35,98.89,100.47,1.02
20260514,96.1,96.8,96.1,96.8,507039,98.56,-1.79,98.73,100.38,0.73
20260515,96.1,96.1,92.8,93.9,1705941,98.18,-4.36,98.4,100.22,2.27
20260518,92.7,93.4,92.2,93.2,674101,97.76,-4.67,98.06,100.04,0.88
20260519,93.2,93.6,92.2,92.8,717813,97.35,-4.67,97.67,99.85,0.93
20260520,92.8,93.4,91,91.4,1001357,96.85,-5.63,97.19,99.64,1.24
20260521,91.5,92.1,91,92,530749,96.45,-4.61,96.75,99.5,0.65
20260522,91.8,92.2,91.5,92,797049,96.08,-4.24,96.34,99.33,0.98
20260525,91.7,93.5,91.3,92.9,916635,95.81,-3.04,96.04,99.15,1.11
20260526,93,93.1,92,92.2,617798,95.51,-3.47,95.78,98.98,0.82
20260527,92.7,92.7,91.5,91.7,827571,95.19,-3.67,95.46,98.79,1.08
20260528,92.4,92.9,91.4,91.4,601077,94.88,-3.67,95.08,98.59,0.79
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.91
- over_600_ratio: 81.45
- over_800_ratio: 80.19
- over_1000_ratio: 78.74
- over_400_change_1w: 0.04
- over_800_change_1w: 0.02
- over_1000_change_1w: -0.18
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.66,,80.29,,78.81,,0,False,False
20260508,83.24,0.58,80.02,-0.27,78.54,-0.27,1,False,False
20260515,82.87,-0.37,80.17,0.15,78.92,0.38,2,False,True
20260522,82.91,0.04,80.19,0.02,78.74,-0.18,3,False,True
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
| 20260528 | 2211 | 長榮鋼 | 5 | 0 | 15030.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
