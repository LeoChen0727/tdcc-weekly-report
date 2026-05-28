# INDIVIDUAL STOCK CHATGPT PACKET - 2481 強茂

## Metadata
- generated_at: 2026-05-28 19:31:59 Asia/Taipei
- stock_id: 2481
- stock_name: 強茂
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2481_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2481_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2481_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2481_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2481_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2481_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2481_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2481_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2481_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2481_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2481_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2481_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2481_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2481_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2481_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2481_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2481_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2481_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2481.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2481.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2481.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2481.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2481.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2481.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2481_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2481_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2481_latest.md?ref=main

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
- open: 146.5
- high: 160.5
- low: 143
- close: 148
- volume: 86464838
- ma5: 142
- ema23_primary: 124.16
- distance_to_ema23_pct: 19.2
- ma20: 121.26
- ma60: 105.74
- ma120: 96.02
- return_5d: 11.7
- return_20d: 46.53
- volume_ratio: 1.8
- distance_to_ma20_pct_auxiliary: 22.05
- distance_to_high_60_pct: -8.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,102,105.5,100,101,17478248,101.09,-0.09,102.27,95.33,0.57
20260504,102.5,103,99.6,99.7,10493178,100.98,-1.27,102.83,95.5,0.34
20260505,100,102.5,99.3,102,12111510,101.06,0.93,103.17,95.72,0.41
20260506,103.5,107,101,101.5,23109803,101.1,0.4,103.02,95.92,0.82
20260507,102.5,105.5,101.5,103.5,18298452,101.3,2.17,103.09,96.1,0.71
20260508,103,104.5,98.5,99.5,15039951,101.15,-1.63,103.05,96.12,0.6
20260511,101.5,109,101.5,109,32693462,101.8,7.07,103.44,96.43,1.27
20260512,113,118.5,112,115.5,61667155,102.95,12.2,104.17,96.89,2.19
20260513,115,122,113,121,67427334,104.45,15.85,105.27,97.42,2.2
20260514,130.5,133,114.5,115.5,73640871,105.37,9.61,106.05,97.88,2.19
20260515,118,124.5,114,117.5,46935445,106.38,10.45,106.55,98.29,1.4
20260518,115.5,129,111.5,129,42888825,108.27,19.15,107.09,98.99,1.29
20260519,130,140.5,126.5,135,98492171,110.49,22.18,108.34,99.81,2.82
20260520,137,138,128.5,133,59601681,112.37,18.36,109.47,100.56,1.63
20260521,136.5,140.5,129.5,132.5,66182056,114.05,16.18,110.92,101.36,1.73
20260522,134,141,130.5,133.5,50103219,115.67,15.42,112.59,102.14,1.27
20260525,135.5,142.5,133,134,51247093,117.2,14.34,114.3,102.91,1.25
20260526,137,147,135.5,147,52336498,119.68,22.83,116.5,103.9,1.25
20260527,157.5,161.5,143,147.5,72240943,122,20.9,118.91,104.85,1.62
20260528,146.5,160.5,143,148,86464838,124.16,19.2,121.26,105.74,1.8
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 66.05
- over_600_ratio: 63.18
- over_800_ratio: 61.06
- over_1000_ratio: 58.92
- over_400_change_1w: 0.42
- over_800_change_1w: -0.64
- over_1000_change_1w: -0.18
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.76,,53.18,,51.27,,0,False,False
20260508,57.62,0.86,53.61,0.43,51.43,0.16,1,True,True
20260515,65.63,8.01,61.7,8.09,59.1,7.67,2,True,True
20260522,66.05,0.42,61.06,-0.64,58.92,-0.18,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2481 | 強茂 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_right_side |  | call_inflow | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2481 | 強茂 | 3 | 1 | 3 | 3 | 3 | continued_overheated | 連續上榜但短期漲幅或乖離過熱，精華追蹤應降級。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2481 | 強茂 | 148 | 3 | 51421830.0 | 560.0 | 91824.7 | call_inflow | 1 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
