# INDIVIDUAL STOCK CHATGPT PACKET - 3049 精金

## Metadata
- generated_at: 2026-05-30 23:41:49 Asia/Taipei
- stock_id: 3049
- stock_name: 精金
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3049_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3049_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3049_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3049_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3049_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3049_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3049_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3049_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3049_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3049_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3049_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3049_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3049_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3049_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3049_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3049_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3049_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3049_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3049.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3049.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3049.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3049.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3049.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3049.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3049_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3049_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3049_latest.md?ref=main

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
- open: 12.5
- high: 12.6
- low: 12.15
- close: 12.5
- volume: 6122628
- ma5: 12.4
- ema23_primary: 12.48
- distance_to_ema23_pct: 0.18
- ma20: 12.59
- ma60: 12.9
- ma120: 10.49
- return_5d: 0.4
- return_20d: 2.46
- volume_ratio: 0.77
- distance_to_ma20_pct_auxiliary: -0.7
- distance_to_high_60_pct: -30.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,13.2,13.4,13.2,13.4,8081115,12.67,5.77,12.44,11.99,0.7
20260505,13.95,13.95,13.05,13.15,19229495,12.71,3.47,12.54,12.05,1.6
20260506,13.15,13.55,12.8,12.85,8504885,12.72,1.02,12.64,12.12,0.7
20260507,12.55,13.35,12.55,13.1,8482171,12.75,2.73,12.72,12.19,0.69
20260508,13.1,13.35,12.55,12.75,6791201,12.75,-0.02,12.73,12.26,0.57
20260511,12.85,13.7,12.6,13.6,10301675,12.82,6.06,12.82,12.33,0.9
20260512,13.5,13.55,12.95,12.95,9134343,12.83,0.91,12.87,12.38,0.79
20260513,12.85,13.2,12.65,12.8,5338736,12.83,-0.24,12.93,12.43,0.47
20260514,13.05,13.05,12.65,12.65,4568469,12.82,-1.29,12.97,12.48,0.4
20260515,12.8,12.9,12.1,12.2,6605740,12.76,-4.42,12.94,12.53,0.6
20260518,12.2,12.3,11.8,12.05,6383656,12.7,-5.15,12.85,12.57,0.66
20260519,12.15,12.35,11.85,11.9,4731071,12.64,-5.84,12.72,12.62,0.56
20260520,12,12.2,11.8,11.9,3672594,12.58,-5.38,12.64,12.66,0.48
20260521,11.95,12.3,11.9,12,5233233,12.53,-4.22,12.59,12.71,0.71
20260522,12.05,12.75,12.05,12.45,6060149,12.52,-0.57,12.59,12.76,0.85
20260525,12.7,12.8,12.4,12.75,8925372,12.54,1.67,12.62,12.81,1.23
20260526,13,13,12.1,12.15,8396092,12.51,-2.86,12.63,12.86,1.14
20260527,12.25,12.3,11.9,12.2,7476197,12.48,-2.26,12.58,12.88,1.01
20260528,12.3,13.2,12.3,12.4,14374387,12.48,-0.61,12.57,12.9,1.83
20260529,12.5,12.6,12.15,12.5,6122628,12.48,0.18,12.59,12.9,0.77
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 47.83
- over_600_ratio: 45.89
- over_800_ratio: 44.71
- over_1000_ratio: 43.77
- over_400_change_1w: 0.51
- over_800_change_1w: 0.4
- over_1000_change_1w: 0.72
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.47,,44.27,,43.48,,0,False,False
20260508,47.72,0.25,44.54,0.27,43.74,0.26,1,True,True
20260515,47.65,-0.07,44.45,-0.09,43.42,-0.32,0,False,False
20260522,47.32,-0.33,44.31,-0.14,43.05,-0.37,0,False,False
20260529,47.83,0.51,44.71,0.4,43.77,0.72,1,True,True
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
| 20260529 | 3049 | 精金 | 1 | 0 | 88570.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
