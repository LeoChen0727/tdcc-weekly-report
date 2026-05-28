# INDIVIDUAL STOCK CHATGPT PACKET - 4968 立積

## Metadata
- generated_at: 2026-05-28 19:32:51 Asia/Taipei
- stock_id: 4968
- stock_name: 立積
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4968_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4968_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4968_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4968_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4968_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4968_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4968_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4968_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4968_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4968_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4968_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4968_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4968_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4968_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4968_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4968_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4968_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4968_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4968.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4968.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4968.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4968.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4968.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4968.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4968_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4968_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4968_latest.md?ref=main

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
- open: 119
- high: 123
- low: 115
- close: 115.5
- volume: 1990469
- ma5: 118.3
- ema23_primary: 116.22
- distance_to_ema23_pct: -0.62
- ma20: 116.7
- ma60: 112.38
- ma120: 120
- return_5d: -0.43
- return_20d: -2.12
- volume_ratio: 1.43
- distance_to_ma20_pct_auxiliary: -1.03
- distance_to_high_60_pct: -13.81

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,118,120,115.5,116,1218746,114.83,1.02,113.03,113.99,0.58
20260504,114.5,115.5,113.5,115,1349189,114.84,0.14,113.53,113.84,0.63
20260505,117.5,124.5,117.5,121,2904508,115.35,4.9,114.47,113.72,1.29
20260506,122.5,123,117,117.5,2325369,115.53,1.7,115.08,113.58,1
20260507,118.5,121,116,119.5,1497247,115.86,3.14,115.65,113.49,0.64
20260508,120,125.5,117.5,119.5,2217431,116.17,2.87,116.35,113.44,0.92
20260511,121,123.5,119.5,121,1236844,116.57,3.8,117.17,113.47,0.51
20260512,121.5,123.5,118.5,120.5,1422030,116.9,3.08,117.95,113.58,0.58
20260513,119,119.5,115.5,115.5,1263815,116.78,-1.1,118.42,113.53,0.51
20260514,117,118.5,114.5,115.5,886310,116.67,-1.01,118.9,113.5,0.36
20260515,116.5,117.5,111,111.5,1195951,116.24,-4.08,118.95,113.21,0.48
20260518,110,111,107,111,666819,115.81,-4.15,118.9,113.05,0.28
20260519,110.5,115,109,110,954193,115.32,-4.61,118.55,112.92,0.44
20260520,110,114,109.5,113,688422,115.13,-1.85,118.1,112.79,0.33
20260521,115,116,114,116,821370,115.2,0.69,117.4,112.75,0.46
20260522,117,120,115.5,119.5,1392984,115.56,3.41,117.22,112.7,0.94
20260525,122,122.5,119,120.5,1396760,115.97,3.91,117.08,112.66,1
20260526,121.5,122.5,117,119,1228406,116.22,2.39,116.92,112.6,0.91
20260527,121,122.5,116,117,1216319,116.29,0.61,116.83,112.49,0.9
20260528,119,123,115,115.5,1990469,116.22,-0.62,116.7,112.38,1.43
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 15.67
- over_600_ratio: 13.44
- over_800_ratio: 9.86
- over_1000_ratio: 8.85
- over_400_change_1w: 0.66
- over_800_change_1w: -0.12
- over_1000_change_1w: -1.13
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,17.06,,10.02,,10.02,,0,False,False
20260508,15.78,-1.28,9.91,-0.11,9.91,-0.11,0,False,False
20260515,15.01,-0.77,9.98,0.07,9.98,0.07,1,False,True
20260522,15.67,0.66,9.86,-0.12,8.85,-1.13,2,False,False
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
| 20260528 | 4968 | 立積 | 38 | 3 | 2242650.0 | 156150.0 | 14.36 | call_inflow | 1 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
