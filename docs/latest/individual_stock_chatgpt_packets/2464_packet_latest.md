# INDIVIDUAL STOCK CHATGPT PACKET - 2464 盟立

## Metadata
- generated_at: 2026-05-28 19:31:58 Asia/Taipei
- stock_id: 2464
- stock_name: 盟立
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2464_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2464_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2464_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2464_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2464_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2464_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2464_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2464_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2464_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2464_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2464_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2464_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2464_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2464_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2464_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2464_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2464_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2464_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2464.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2464.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2464.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2464.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2464.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2464.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2464_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2464_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2464_latest.md?ref=main

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
- open: 177
- high: 177
- low: 163.5
- close: 168
- volume: 17695107
- ma5: 164.1
- ema23_primary: 131.38
- distance_to_ema23_pct: 27.88
- ma20: 131.68
- ma60: 94.59
- ma120: 79.92
- return_5d: 23.53
- return_20d: 46.72
- volume_ratio: 0.67
- distance_to_ma20_pct_auxiliary: 27.59
- distance_to_high_60_pct: -8.7

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,112,118,111.5,113.5,30874543,86.77,30.8,82.58,75.03,1.91
20260504,116,120,113,116,25160104,89.21,30.03,84.98,75.81,1.45
20260505,118,121.5,111.5,113,18018922,91.19,23.92,87.31,76.52,0.99
20260506,113,115,105,111,18892967,92.84,19.56,89.56,77.22,1
20260507,112,113.5,107,111,13371619,94.35,17.64,91.72,77.91,0.68
20260508,112,122,109,122,55247054,96.66,26.22,94.43,78.77,2.49
20260511,120.5,123,114,120,30281910,98.6,21.7,96.98,79.63,1.28
20260512,120.5,123,116,118,14892576,100.22,17.74,99.38,80.53,0.62
20260513,117,117.5,110,112.5,13200083,101.24,11.12,101.25,81.25,0.54
20260514,114,118.5,112.5,115,12945170,102.39,12.32,103.28,81.97,0.52
20260515,117,126.5,116.5,126.5,21760158,104.4,21.17,105.94,82.93,0.85
20260518,126.5,139,119,139,57632475,107.28,29.56,108.94,84.05,2.07
20260519,138,140.5,129.5,135,45558018,109.59,23.18,111.34,85.06,1.56
20260520,136.5,136.5,123.5,124.5,26449390,110.83,12.33,113.27,85.93,0.91
20260521,126,136.5,124.5,136,28460951,112.93,20.43,115.36,87.02,0.98
20260522,134.5,149,134,144,37571437,115.52,24.65,118.33,88.2,1.26
20260525,156,158,155,158,8728463,119.06,32.71,121.65,89.62,0.3
20260526,163.5,173.5,163.5,173.5,17717493,123.6,40.38,125.47,91.32,0.63
20260527,177,184,173,177,32535439,128.05,38.23,129,93.03,1.16
20260528,177,177,163.5,168,17695107,131.38,27.88,131.68,94.59,0.67
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 47.32
- over_600_ratio: 45.23
- over_800_ratio: 42.94
- over_1000_ratio: 41.61
- over_400_change_1w: 1.75
- over_800_change_1w: 1.47
- over_1000_change_1w: 3.21
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,48.16,,44.05,,40.96,,0,False,False
20260508,46.44,-1.72,42.27,-1.78,40.93,-0.03,0,False,False
20260515,45.57,-0.87,41.47,-0.8,38.4,-2.53,1,False,False
20260522,47.32,1.75,42.94,1.47,41.61,3.21,2,True,True
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
| 20260528 | 2464 | 盟立 | 110 | 3 | 16721800.0 | 841590.0 | 19.87 | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
