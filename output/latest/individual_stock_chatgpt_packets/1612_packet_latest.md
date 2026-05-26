# INDIVIDUAL STOCK CHATGPT PACKET - 1612 宏泰

## Metadata
- generated_at: 2026-05-26 21:24:44 Asia/Taipei
- stock_id: 1612
- stock_name: 宏泰
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1612_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1612_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1612_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1612_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1612_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1612_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1612_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1612_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1612_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1612_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1612_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1612_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1612_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1612_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1612_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1612_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1612_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1612_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1612.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1612.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1612.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1612.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1612.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1612.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1612_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1612_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1612_latest.md?ref=main

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
- open: 36.8
- high: 37.25
- low: 36.7
- close: 36.95
- volume: 908224
- ma5: 36.51
- ema23_primary: 36.19
- distance_to_ema23_pct: 2.1
- ma20: 36.35
- ma60: 35.5
- ma120: 35.43
- return_5d: 3.79
- return_20d: 6.18
- volume_ratio: 0.96
- distance_to_ma20_pct_auxiliary: 1.64
- distance_to_high_60_pct: -1.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,35,35.5,34.7,35.45,795798,35.23,0.62,35.11,35.54,1.39
20260429,35.5,35.6,35.25,35.55,633371,35.26,0.83,35.14,35.51,1.07
20260430,35.55,35.75,35.4,35.65,787418,35.29,1.02,35.22,35.47,1.33
20260504,35.7,36.6,35.65,36.45,1864508,35.39,3,35.3,35.44,2.79
20260505,36.9,36.9,36.25,36.6,1348483,35.49,3.13,35.41,35.43,1.87
20260506,36.8,36.9,36.35,36.75,1238369,35.59,3.25,35.52,35.41,1.63
20260507,36.95,37.5,36.8,37.2,1950220,35.73,4.12,35.63,35.4,2.34
20260508,37.05,37.2,36.35,36.7,1257492,35.81,2.49,35.73,35.38,1.44
20260511,37,37.45,36.7,37.25,1196642,35.93,3.68,35.84,35.4,1.32
20260512,37.55,37.55,36.75,36.8,724207,36,2.22,35.91,35.42,0.78
20260513,36.95,37,36.55,36.85,557304,36.07,2.16,35.98,35.45,0.6
20260514,36.85,37.05,36.15,36.15,826641,36.08,0.2,36.02,35.45,0.89
20260515,36.15,36.4,35.7,35.8,840316,36.06,-0.71,36.03,35.44,0.89
20260518,35.55,35.85,35.25,35.7,473669,36.03,-0.9,36.03,35.44,0.51
20260519,35.7,36.2,35.55,35.6,632821,35.99,-1.08,36.04,35.44,0.68
20260520,35.85,36,35.5,35.75,372564,35.97,-0.61,36.05,35.44,0.4
20260521,36.15,37.05,36,36.6,922455,36.02,1.6,36.09,35.46,0.98
20260522,36.6,36.75,36.3,36.6,773135,36.07,1.47,36.16,35.47,0.83
20260525,36.8,37.2,36.55,36.65,838679,36.12,1.47,36.24,35.47,0.89
20260526,36.8,37.25,36.7,36.95,908224,36.19,2.1,36.35,35.5,0.96
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 62.47
- over_600_ratio: 59.79
- over_800_ratio: 58.28
- over_1000_ratio: 56.84
- over_400_change_1w: 0.04
- over_800_change_1w: 0.27
- over_1000_change_1w: -0.3
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.44,,57.2,,56.6,,0,False,False
20260508,62.41,0.97,57.98,0.78,57.09,0.49,1,True,True
20260515,62.43,0.02,58.01,0.03,57.14,0.05,2,False,True
20260522,62.47,0.04,58.28,0.27,56.84,-0.3,3,False,True
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
| 20260526 | 1612 | 宏泰 | 6 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
