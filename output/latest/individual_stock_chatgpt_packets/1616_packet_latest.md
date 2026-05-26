# INDIVIDUAL STOCK CHATGPT PACKET - 1616 億泰

## Metadata
- generated_at: 2026-05-26 21:24:44 Asia/Taipei
- stock_id: 1616
- stock_name: 億泰
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1616_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1616_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1616_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1616_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1616_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1616_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1616_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1616_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1616_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1616_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1616_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1616_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1616_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1616_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1616_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1616_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1616_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1616_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1616.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1616.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1616.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1616.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1616.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1616.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1616_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1616_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1616_latest.md?ref=main

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
- open: 22.1
- high: 22.4
- low: 21.7
- close: 21.7
- volume: 519659
- ma5: 21.78
- ema23_primary: 22.06
- distance_to_ema23_pct: -1.64
- ma20: 21.84
- ma60: 23.72
- ma120: 26.22
- return_5d: 5.34
- return_20d: -2.03
- volume_ratio: 0.86
- distance_to_ma20_pct_auxiliary: -0.63
- distance_to_high_60_pct: -26.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,22.4,22.45,22,22.3,245059,23.59,-5.46,23.25,25.95,0.54
20260429,22.65,22.65,22.15,22.3,267885,23.48,-5.03,23.2,25.83,0.59
20260430,22.2,22.5,22.1,22.15,357052,23.37,-5.22,23.16,25.7,0.8
20260504,22.25,22.7,22.05,22.35,491595,23.29,-4.02,23.11,25.58,1.07
20260505,22.2,22.45,22.15,22.3,445016,23.2,-3.89,23.07,25.46,0.95
20260506,22.45,22.45,21.75,21.75,1000211,23.08,-5.77,23.01,25.33,2.04
20260507,21.8,22.45,21.7,22.35,914342,23.02,-2.92,22.95,25.2,1.78
20260508,22.6,22.85,22.15,22.15,929892,22.95,-3.48,22.88,25.08,1.7
20260511,22.55,22.65,22.05,22.35,463857,22.9,-2.4,22.83,24.97,0.84
20260512,22.5,22.6,22.25,22.55,437827,22.87,-1.4,22.79,24.89,0.78
20260513,22.55,22.6,22.1,22.1,513685,22.81,-3.09,22.72,24.8,0.91
20260514,22.1,22.4,21.55,21.55,1162382,22.7,-5.07,22.62,24.69,1.93
20260515,21.6,21.75,20.7,20.7,1106201,22.53,-8.14,22.47,24.57,1.74
20260518,20.5,20.6,20.2,20.35,483544,22.35,-8.96,22.3,24.44,0.76
20260519,20.35,21,20.3,20.6,355552,22.21,-7.23,22.15,24.31,0.56
20260520,20.65,21.25,20.65,21.25,450259,22.13,-3.96,22.03,24.19,0.71
20260521,21.75,21.9,21.5,21.85,674716,22.1,-1.15,21.94,24.09,1.05
20260522,22,22.1,21.5,22.05,585382,22.1,-0.22,21.89,23.96,0.97
20260525,22.25,22.5,22,22.05,740073,22.09,-0.2,21.86,23.85,1.2
20260526,22.1,22.4,21.7,21.7,519659,22.06,-1.64,21.84,23.72,0.86
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 60.94
- over_600_ratio: 59.42
- over_800_ratio: 58.79
- over_1000_ratio: 57.02
- over_400_change_1w: -0.12
- over_800_change_1w: -0.08
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.16,,58.97,,57.2,,0,False,False
20260508,61.59,0.43,59.18,0.21,57.41,0.21,1,True,True
20260515,61.06,-0.53,58.87,-0.31,57.1,-0.31,0,False,False
20260522,60.94,-0.12,58.79,-0.08,57.02,-0.08,0,False,False
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
| 20260526 | 1616 | 億泰 | 3 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
