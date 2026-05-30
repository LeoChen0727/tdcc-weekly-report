# INDIVIDUAL STOCK CHATGPT PACKET - 3708 上緯投控

## Metadata
- generated_at: 2026-05-30 23:42:13 Asia/Taipei
- stock_id: 3708
- stock_name: 上緯投控
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3708_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3708_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3708_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3708_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3708_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3708_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3708_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3708_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3708_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3708_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3708_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3708_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3708_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3708_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3708_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3708_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3708_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3708_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3708.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3708.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3708.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3708.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3708.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3708.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3708_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3708_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3708_latest.md?ref=main

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
- open: 126
- high: 126.5
- low: 123.5
- close: 124.5
- volume: 873664
- ma5: 127.2
- ema23_primary: 122.51
- distance_to_ema23_pct: 1.62
- ma20: 121.85
- ma60: 120.95
- ma120: 116.92
- return_5d: -1.19
- return_20d: 6.87
- volume_ratio: 0.55
- distance_to_ma20_pct_auxiliary: 2.17
- distance_to_high_60_pct: -11.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,116.5,122.5,116.5,120.5,947068,119.84,0.55,118.92,118.81,0.76
20260505,120,127.5,119.5,126,1547894,120.36,4.69,119.42,118.86,1.25
20260506,126,127.5,119.5,121,1442118,120.41,0.49,119.83,118.85,1.15
20260507,122,123,119.5,120.5,863738,120.42,0.07,120.17,118.86,0.68
20260508,121.5,121.5,117,118.5,730189,120.26,-1.46,120.4,118.85,0.57
20260511,119,124.5,118,121.5,1704405,120.36,0.95,120.67,118.93,1.29
20260512,122.5,124.5,120.5,121.5,1045779,120.46,0.87,120.92,119.09,0.79
20260513,119.5,119.5,115.5,118,1480802,120.25,-1.87,121,119.18,1.07
20260514,118.5,120.5,116,116.5,797924,119.94,-2.87,121.15,119.17,0.58
20260515,116.5,117.5,113,113.5,937925,119.4,-4.94,120.9,119.18,0.68
20260518,112,116.5,111.5,116.5,546872,119.16,-2.23,120.55,119.33,0.42
20260519,115,118,114,115.5,398360,118.86,-2.82,119.92,119.52,0.33
20260520,116,119.5,114.5,119,963824,118.87,0.11,119.47,119.75,0.83
20260521,120.5,130.5,119.5,126.5,3945233,119.5,5.85,119.5,120.14,3.07
20260522,126,128,125,126,1321676,120.04,4.96,119.55,120.36,1.12
20260525,128,128.5,123,125,1009619,120.46,3.77,119.67,120.46,0.86
20260526,125.5,135.5,124,131.5,4629976,121.38,8.34,120.42,120.68,3.57
20260527,133,140.5,128.5,131,4430689,122.18,7.22,121.08,120.84,2.97
20260528,132,133.5,123,124,2389494,122.33,1.36,121.45,120.87,1.52
20260529,126,126.5,123.5,124.5,873664,122.51,1.62,121.85,120.95,0.55
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 54.42
- over_600_ratio: 49.33
- over_800_ratio: 46.15
- over_1000_ratio: 44.36
- over_400_change_1w: -0.74
- over_800_change_1w: -1.01
- over_1000_change_1w: 0.6
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.12,,43.26,,42.24,,0,False,False
20260508,53.63,0.51,44.26,1,43.37,1.13,1,False,True
20260515,54,0.37,45.55,1.29,43.65,0.28,2,True,True
20260522,55.16,1.16,47.16,1.61,43.76,0.11,3,True,True
20260529,54.42,-0.74,46.15,-1.01,44.36,0.6,4,False,True
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
| 20260529 | 3708 | 上緯投控 | 27 | 2 | 1229160.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
