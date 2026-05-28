# INDIVIDUAL STOCK CHATGPT PACKET - 3311 閎暉

## Metadata
- generated_at: 2026-05-28 19:32:23 Asia/Taipei
- stock_id: 3311
- stock_name: 閎暉
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3311_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3311_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3311_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3311_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3311_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3311_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3311_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3311_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3311_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3311_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3311_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3311_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3311_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3311_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3311_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3311_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3311_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3311_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3311.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3311.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3311.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3311.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3311.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3311.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3311_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3311_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3311_latest.md?ref=main

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
- open: 35
- high: 38.35
- low: 34.7
- close: 36.45
- volume: 4396543
- ma5: 34.91
- ema23_primary: 32.92
- distance_to_ema23_pct: 10.71
- ma20: 32.4
- ma60: 32.31
- ma120: 32.16
- return_5d: 11.47
- return_20d: 17.39
- volume_ratio: 7.26
- distance_to_ma20_pct_auxiliary: 12.52
- distance_to_high_60_pct: -4.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,31.05,31.05,30.55,30.65,265551,31.99,-4.2,32.15,32.31,1.05
20260504,30.6,31,30.5,30.5,150051,31.87,-4.3,32.06,32.25,0.59
20260505,30.5,30.9,30.5,30.75,99370,31.78,-3.23,32.03,32.2,0.39
20260506,31,31.1,30.35,30.55,235861,31.67,-3.55,31.97,32.15,0.91
20260507,30.65,32.1,30.65,31.55,338608,31.66,-0.36,31.91,32.12,1.31
20260508,32.6,32.85,31.8,32.4,372960,31.73,2.13,31.91,32.11,1.36
20260511,32.6,33.2,32.55,32.8,389701,31.82,3.1,31.96,32.11,1.37
20260512,33.15,34,33,33.1,305449,31.92,3.69,31.95,32.12,1.17
20260513,33.2,33.2,31.85,31.95,207526,31.92,0.08,31.91,32.12,0.82
20260514,32,32,31,31.45,165470,31.88,-1.36,31.83,32.1,0.65
20260515,31.8,32.25,30.8,31,263292,31.81,-2.55,31.73,32.09,1.04
20260518,31.1,31.45,30.6,31.45,111721,31.78,-1.04,31.65,32.1,0.45
20260519,31.6,31.9,30.95,31,119106,31.72,-2.26,31.57,32.09,0.51
20260520,31.7,32.2,31.2,31.5,201759,31.7,-0.62,31.52,32.1,0.9
20260521,31.7,32.8,31.65,32.7,285464,31.78,2.89,31.52,32.14,1.24
20260522,32.7,34.45,32.55,33.85,627003,31.95,5.93,31.6,32.18,2.61
20260525,34.05,34.65,33.6,33.85,472417,32.11,5.41,31.71,32.2,1.86
20260526,34,35.65,33.85,35.5,1812556,32.39,9.59,31.93,32.26,5.48
20260527,36.9,37.25,34.05,34.9,1289529,32.6,7.05,32.12,32.27,3.3
20260528,35,38.35,34.7,36.45,4396543,32.92,10.71,32.4,32.31,7.26
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 55.56
- over_600_ratio: 53.12
- over_800_ratio: 50.89
- over_1000_ratio: 50.04
- over_400_change_1w: -0.06
- over_800_change_1w: -0.09
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.67,,50.89,,49.98,,0,False,False
20260508,55.52,0.85,50.9,0.01,50.03,0.05,1,True,True
20260515,55.62,0.1,50.98,0.08,50.04,0.01,2,True,True
20260522,55.56,-0.06,50.89,-0.09,50.04,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3311 | 閎暉 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3311 | 閎暉 | 3 | 2 | 3 | 3 | 3 | continued_2_3d | 連續 3 個交易日上榜，訊號延續但仍需確認。 |

## Warrant Context
| status |
| --- |
| no rows |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
