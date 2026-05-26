# INDIVIDUAL STOCK CHATGPT PACKET - 1442 名軒

## Metadata
- generated_at: 2026-05-26 22:18:04 Asia/Taipei
- stock_id: 1442
- stock_name: 名軒
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1442_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1442_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1442_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1442_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1442_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1442_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1442_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1442_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1442_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1442_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1442_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1442_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1442_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1442_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1442_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1442_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1442_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1442_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1442.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1442.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1442.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1442.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1442.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1442.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1442_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1442_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1442_latest.md?ref=main

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
- open: 25.8
- high: 25.8
- low: 25.55
- close: 25.7
- volume: 222552
- ma5: 25.98
- ema23_primary: 26.61
- distance_to_ema23_pct: -3.42
- ma20: 26.5
- ma60: 27.05
- ma120: 28.74
- return_5d: -1.91
- return_20d: -7.22
- volume_ratio: 0.46
- distance_to_ma20_pct_auxiliary: -3.02
- distance_to_high_60_pct: -16.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,28.05,28.05,27,27,719010,27.78,-2.81,27.46,28.02,0.78
20260429,27.65,27.65,26.9,27.4,773388,27.75,-1.26,27.53,27.98,0.83
20260430,27.55,27.55,26.2,26.2,925843,27.62,-5.14,27.54,27.92,0.96
20260504,26.8,26.9,26.25,26.45,398081,27.52,-3.9,27.54,27.87,0.41
20260505,26.25,26.75,26.2,26.45,281949,27.43,-3.58,27.56,27.82,0.29
20260506,26.85,26.85,26.2,26.3,449945,27.34,-3.8,27.5,27.78,0.47
20260507,26.6,26.9,26.2,26.75,420244,27.29,-1.98,27.45,27.74,0.44
20260508,26.75,27.6,26.3,27.1,663209,27.27,-0.64,27.49,27.7,0.7
20260511,26.9,27.05,26.6,26.9,344708,27.24,-1.26,27.52,27.65,0.37
20260512,26.95,27.1,26.4,26.95,455993,27.22,-0.99,27.57,27.61,0.49
20260513,26.95,26.95,26.55,26.8,188603,27.18,-1.41,27.61,27.56,0.2
20260514,26.6,26.95,26.35,26.35,593247,27.11,-2.82,27.57,27.5,0.64
20260515,26.35,26.75,26.3,26.75,409503,27.08,-1.23,27.54,27.45,0.45
20260518,26.75,26.9,26.35,26.5,259830,27.04,-1.98,27.41,27.4,0.31
20260519,26.5,26.95,26.2,26.2,307901,26.97,-2.84,27.24,27.34,0.42
20260520,26.1,26.25,25.8,26.25,481058,26.91,-2.44,27.05,27.28,0.78
20260521,26.2,26.45,26.15,26.15,410371,26.84,-2.58,26.88,27.21,0.72
20260522,26.05,26.1,25.7,26,707761,26.77,-2.89,26.75,27.15,1.29
20260525,26.1,26.1,25.65,25.8,768359,26.69,-3.34,26.6,27.1,1.5
20260526,25.8,25.8,25.55,25.7,222552,26.61,-3.42,26.5,27.05,0.46
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 86.33
- over_600_ratio: 83.54
- over_800_ratio: 80.5
- over_1000_ratio: 77.62
- over_400_change_1w: 0.02
- over_800_change_1w: 0
- over_1000_change_1w: 0.27
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,86.88,,81.07,,78.18,,0,False,False
20260508,86.49,-0.39,81.05,-0.02,78.13,-0.05,0,False,False
20260515,86.31,-0.18,80.5,-0.55,77.35,-0.78,0,False,False
20260522,86.33,0.02,80.5,0,77.62,0.27,1,False,True
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
| 20260526 | 1442 | 名軒 | 3 | 0 | 300.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
