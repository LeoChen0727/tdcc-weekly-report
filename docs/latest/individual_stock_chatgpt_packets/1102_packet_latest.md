# INDIVIDUAL STOCK CHATGPT PACKET - 1102 亞泥

## Metadata
- generated_at: 2026-05-26 23:00:07 Asia/Taipei
- stock_id: 1102
- stock_name: 亞泥
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1102_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1102_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1102_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1102_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1102_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1102_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1102_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1102_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1102_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1102_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1102_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1102_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1102_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1102_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1102_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1102_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1102_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1102_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1102.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1102.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1102.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1102.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1102.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1102.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1102_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1102_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1102_latest.md?ref=main

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
- open: 33.55
- high: 33.65
- low: 33.25
- close: 33.25
- volume: 15247384
- ma5: 34.14
- ema23_primary: 34.67
- distance_to_ema23_pct: -4.1
- ma20: 34.73
- ma60: 34.92
- ma120: 35.87
- return_5d: -4.45
- return_20d: -5.67
- volume_ratio: 1.54
- distance_to_ma20_pct_auxiliary: -4.27
- distance_to_high_60_pct: -8.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,35.2,35.5,35.15,35.3,7654996,35.36,-0.17,35.45,35.14,0.72
20260429,35.5,35.65,35.25,35.4,7665391,35.36,0.1,35.47,35.14,0.74
20260430,35.2,35.5,35.05,35.05,11874662,35.34,-0.81,35.48,35.13,1.17
20260504,35.25,35.3,34.7,34.9,7454780,35.3,-1.13,35.47,35.12,0.74
20260505,34.85,35,34.6,34.95,5493007,35.27,-0.91,35.45,35.1,0.55
20260506,34.95,35.3,34.9,35.2,6226612,35.27,-0.19,35.44,35.1,0.63
20260507,35,35.3,34.95,34.95,7386318,35.24,-0.82,35.4,35.09,0.75
20260508,34.95,35.35,34.9,34.95,6615592,35.21,-0.75,35.35,35.08,0.69
20260511,35,35.05,34.6,34.65,8502942,35.17,-1.47,35.3,35.07,0.89
20260512,34.75,34.9,34.6,34.6,7762086,35.12,-1.48,35.26,35.07,0.82
20260513,34.45,35.5,34.45,35.3,9747610,35.14,0.47,35.24,35.09,1.03
20260514,35,35.45,35,35.2,13239584,35.14,0.17,35.24,35.09,1.37
20260515,35.2,35.2,34.35,34.35,11291933,35.08,-2.07,35.18,35.07,1.15
20260518,34.3,34.55,34.1,34.35,9040498,35.01,-1.9,35.11,35.05,0.94
20260519,34.7,35.2,34.45,34.8,9446874,35,-0.56,35.1,35.04,1.02
20260520,35,35,34.5,34.5,8318546,34.96,-1.3,35.06,35.03,0.92
20260521,34.75,34.95,34.5,34.95,6909878,34.95,-0.01,35.03,35.02,0.77
20260522,34.6,34.8,34.4,34.4,11752214,34.91,-1.46,34.95,35,1.35
20260525,34.45,34.5,33.6,33.6,26457340,34.8,-3.45,34.83,34.96,2.72
20260526,33.55,33.65,33.25,33.25,15247384,34.67,-4.1,34.73,34.92,1.54
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.19
- over_600_ratio: 81
- over_800_ratio: 80.12
- over_1000_ratio: 79.52
- over_400_change_1w: -0.19
- over_800_change_1w: -0.07
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.39,,80.3,,79.5,,0,False,False
20260508,82.3,-0.09,80.18,-0.12,79.45,-0.05,0,False,False
20260515,82.38,0.08,80.19,0.01,79.49,0.04,1,True,True
20260522,82.19,-0.19,80.12,-0.07,79.52,0.03,2,False,True
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
| 20260526 | 1102 | 亞泥 | 2 | 0 | 160.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
