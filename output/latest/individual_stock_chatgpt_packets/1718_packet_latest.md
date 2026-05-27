# INDIVIDUAL STOCK CHATGPT PACKET - 1718 中纖

## Metadata
- generated_at: 2026-05-27 21:26:18 Asia/Taipei
- stock_id: 1718
- stock_name: 中纖
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1718_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1718_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1718_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1718_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1718_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1718_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1718_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1718_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1718_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1718_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1718_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1718_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1718_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1718_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1718_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1718_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1718_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1718_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1718.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1718.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1718.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1718.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1718.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1718.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1718_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1718_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1718_latest.md?ref=main

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
- date: 20260527
- open: 6.42
- high: 6.46
- low: 6.29
- close: 6.31
- volume: 5049612
- ma5: 6.41
- ema23_primary: 6.56
- distance_to_ema23_pct: -3.77
- ma20: 6.48
- ma60: 7
- ma120: 7
- return_5d: -1.87
- return_20d: -5.96
- volume_ratio: 1.22
- distance_to_ma20_pct_auxiliary: -2.63
- distance_to_high_60_pct: -23.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,6.74,6.74,6.64,6.65,2865949,6.99,-4.83,7.03,7.2,0.53
20260430,6.7,6.7,6.53,6.55,4072047,6.95,-5.77,6.99,7.19,0.81
20260504,6.57,6.57,6.46,6.5,5848102,6.91,-5.98,6.94,7.18,1.17
20260505,6.52,6.56,6.5,6.51,2060575,6.88,-5.38,6.89,7.17,0.42
20260506,6.56,6.56,6.42,6.42,4191899,6.84,-6.16,6.84,7.15,0.86
20260507,6.37,6.41,6.25,6.35,6233106,6.8,-6.63,6.79,7.13,1.27
20260508,6.35,6.42,6.28,6.34,4962962,6.76,-6.24,6.75,7.12,1.01
20260511,6.38,6.52,6.37,6.48,3648024,6.74,-3.84,6.71,7.11,0.76
20260512,6.59,6.77,6.51,6.71,6025698,6.74,-0.39,6.68,7.11,1.24
20260513,6.71,6.71,6.47,6.51,5416415,6.72,-3.09,6.65,7.1,1.11
20260514,6.57,6.73,6.52,6.68,5573917,6.71,-0.51,6.63,7.09,1.17
20260515,6.7,6.72,6.35,6.36,5715247,6.68,-4.86,6.6,7.08,1.17
20260518,6.48,6.58,6.36,6.58,3298141,6.68,-1.44,6.58,7.08,0.71
20260519,6.58,6.61,6.48,6.51,3057086,6.66,-2.29,6.57,7.07,0.68
20260520,6.57,6.57,6.41,6.43,2230114,6.64,-3.2,6.55,7.06,0.51
20260521,6.43,6.52,6.43,6.47,2518892,6.63,-2.39,6.53,7.05,0.59
20260522,6.47,6.5,6.4,6.46,2980947,6.61,-2.33,6.52,7.04,0.72
20260525,6.5,6.5,6.35,6.4,4201915,6.6,-2.98,6.51,7.03,1.02
20260526,6.41,6.45,6.35,6.39,2845982,6.58,-2.88,6.5,7.01,0.69
20260527,6.42,6.46,6.29,6.31,5049612,6.56,-3.77,6.48,7,1.22
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 55.83
- over_600_ratio: 52.83
- over_800_ratio: 51.33
- over_1000_ratio: 49.88
- over_400_change_1w: -0.05
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.15
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.68,,51.2,,49.68,,0,False,False
20260508,55.7,0.02,51.18,-0.02,49.67,-0.01,1,False,False
20260515,55.88,0.18,51.38,0.2,50.03,0.36,2,True,True
20260522,55.83,-0.05,51.33,-0.05,49.88,-0.15,0,False,False
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
| 20260527 | 1718 | 中纖 | 3 | 0 | 13760.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
