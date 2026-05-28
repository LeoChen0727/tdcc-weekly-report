# INDIVIDUAL STOCK CHATGPT PACKET - 1532 勤美

## Metadata
- generated_at: 2026-05-28 19:31:35 Asia/Taipei
- stock_id: 1532
- stock_name: 勤美
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1532_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1532_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1532_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1532_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1532_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1532_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1532_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1532_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1532_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1532_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1532_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1532_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1532_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1532_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1532_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1532_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1532_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1532_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1532.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1532.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1532.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1532.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1532.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1532.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1532_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1532_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1532_latest.md?ref=main

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
- open: 20.85
- high: 21
- low: 20.7
- close: 20.8
- volume: 822161
- ma5: 20.69
- ema23_primary: 20.83
- distance_to_ema23_pct: -0.12
- ma20: 20.61
- ma60: 21.72
- ma120: 23.82
- return_5d: 0.48
- return_20d: -0.48
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: 0.91
- distance_to_high_60_pct: -14.58

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,20.9,21,20.7,20.85,934378,21.66,-3.73,21.6,22.93,1.4
20260504,20.85,20.9,20.5,20.5,858593,21.56,-4.92,21.54,22.85,1.24
20260505,20.5,20.75,20.35,20.6,1196734,21.48,-4.1,21.48,22.78,1.62
20260506,20.9,20.9,20.5,20.6,1011419,21.41,-3.77,21.41,22.7,1.32
20260507,20.7,20.9,20.5,20.8,915114,21.36,-2.61,21.34,22.64,1.17
20260508,20.95,21.05,20.65,20.65,977300,21.3,-3.04,21.27,22.57,1.2
20260511,20.65,20.7,20.45,20.6,585302,21.24,-3.01,21.21,22.5,0.72
20260512,20.6,20.6,20.4,20.4,878193,21.17,-3.64,21.14,22.45,1.06
20260513,20.4,20.5,20.2,20.45,1013320,21.11,-3.13,21.06,22.38,1.19
20260514,20.25,20.5,20.05,20.2,1515750,21.03,-3.96,20.98,22.31,1.72
20260515,20.4,21.2,20.35,20.4,1389761,20.98,-2.77,20.89,22.25,1.51
20260518,20.4,21,20.2,20.9,794770,20.97,-0.35,20.85,22.2,0.86
20260519,20.65,21.3,20.6,20.6,813648,20.94,-1.64,20.8,22.14,0.88
20260520,20.75,20.8,20.45,20.55,498241,20.91,-1.72,20.74,22.07,0.54
20260521,20.55,20.85,20.55,20.7,266832,20.89,-0.92,20.69,22.01,0.29
20260522,21,21,20.5,20.55,703021,20.86,-1.51,20.65,21.95,0.81
20260525,20.6,20.75,20.5,20.65,500648,20.85,-0.94,20.63,21.89,0.58
20260526,20.65,20.95,20.65,20.65,558870,20.83,-0.86,20.62,21.83,0.66
20260527,20.65,20.85,20.6,20.8,801405,20.83,-0.13,20.62,21.77,0.94
20260528,20.85,21,20.7,20.8,822161,20.83,-0.12,20.61,21.72,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.63
- over_600_ratio: 60.76
- over_800_ratio: 58.23
- over_1000_ratio: 56.49
- over_400_change_1w: -0.08
- over_800_change_1w: 0.32
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,64.71,,58.11,,56.79,,0,False,False
20260508,64.59,-0.12,57.65,-0.46,56.13,-0.66,0,False,False
20260515,64.71,0.12,57.91,0.26,56.57,0.44,1,True,True
20260522,64.63,-0.08,58.23,0.32,56.49,-0.08,2,False,True
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
| 20260528 | 1532 | 勤美 | 2 | 0 | 0.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
