# INDIVIDUAL STOCK CHATGPT PACKET - 5222 全訊

## Metadata
- generated_at: 2026-05-28 19:32:54 Asia/Taipei
- stock_id: 5222
- stock_name: 全訊
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5222_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5222_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5222_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5222_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5222_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5222_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5222_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5222_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5222_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5222_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5222_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5222_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5222_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5222_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5222_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5222_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5222_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5222_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5222.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5222.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5222.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5222.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5222.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5222.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5222_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5222_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5222_latest.md?ref=main

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
- open: 125.5
- high: 126.5
- low: 121
- close: 122.5
- volume: 561201
- ma5: 125.7
- ema23_primary: 128.1
- distance_to_ema23_pct: -4.37
- ma20: 128.7
- ma60: 131.49
- ma120: 133.35
- return_5d: -1.61
- return_20d: -7.55
- volume_ratio: 0.9
- distance_to_ma20_pct_auxiliary: -4.82
- distance_to_high_60_pct: -19.93

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,133.5,133.5,131,131.5,368987,133.69,-1.64,130.93,134.93,0.26
20260504,133,139,133,135.5,773411,133.85,1.24,131.35,134.72,0.53
20260505,134.5,137.5,134.5,137.5,360603,134.15,2.5,132.1,134.54,0.25
20260506,139.5,139.5,133,134,509616,134.14,-0.1,133.2,134.39,0.37
20260507,136,137,133,136.5,741314,134.33,1.61,134.2,134.32,0.54
20260508,137,142,136.5,139,1191807,134.72,3.17,135.32,134.26,0.85
20260511,136.5,136.5,130,131.5,1552619,134.45,-2.2,136.03,134.17,1.06
20260512,131.5,131.5,128,129,873079,134,-3.73,136.07,134.07,0.61
20260513,127,130,126,127,602208,133.42,-4.81,135.88,133.9,0.43
20260514,127,128,125,126,459301,132.8,-5.12,135.68,133.62,0.33
20260515,126,129,125.5,125.5,528663,132.19,-5.06,135.38,133.44,0.39
20260518,124,125,123,123.5,440963,131.47,-6.06,134.32,133.32,0.38
20260519,124,126,122,122,517155,130.68,-6.64,133.25,133.17,0.59
20260520,121.5,125,121.5,122.5,311940,130,-5.77,132.25,133.04,0.39
20260521,124,126.5,123.5,124.5,430575,129.54,-3.89,131.32,132.89,0.56
20260522,125.5,128,125.5,128,618434,129.41,-1.09,130.62,132.7,0.94
20260525,130,130.5,127.5,128,687694,129.29,-1,130.12,132.45,1.06
20260526,128,128.5,125,125,440890,128.93,-3.05,129.55,132.11,0.71
20260527,125,127,124.5,125,541836,128.61,-2.8,129.2,131.79,0.88
20260528,125.5,126.5,121,122.5,561201,128.1,-4.37,128.7,131.49,0.9
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 32.56
- over_600_ratio: 27.6
- over_800_ratio: 26.93
- over_1000_ratio: 22.88
- over_400_change_1w: -0.08
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,32.72,,26.67,,22.62,,0,False,False
20260508,32.72,0,26.78,0.11,22.73,0.11,1,False,True
20260515,32.64,-0.08,26.96,0.18,22.91,0.18,2,False,True
20260522,32.56,-0.08,26.93,-0.03,22.88,-0.03,0,False,False
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
| 20260528 | 5222 | 全訊 | 15 | 0 | 442150.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
