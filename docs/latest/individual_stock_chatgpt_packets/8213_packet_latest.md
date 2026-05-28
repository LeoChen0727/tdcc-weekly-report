# INDIVIDUAL STOCK CHATGPT PACKET - 8213 志超

## Metadata
- generated_at: 2026-05-28 19:33:48 Asia/Taipei
- stock_id: 8213
- stock_name: 志超
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8213_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8213_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8213_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8213_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8213_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8213_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8213_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8213_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8213_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8213_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8213_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8213_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8213_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8213_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8213_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8213_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8213_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8213_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8213.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8213.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8213.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8213.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8213.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8213.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8213_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8213_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8213_latest.md?ref=main

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
- open: 40.6
- high: 41.2
- low: 38.7
- close: 38.9
- volume: 1626156
- ma5: 39.38
- ema23_primary: 38.11
- distance_to_ema23_pct: 2.07
- ma20: 38.28
- ma60: 36.15
- ma120: 35.24
- return_5d: 3.18
- return_20d: 5.99
- volume_ratio: 0.9
- distance_to_ma20_pct_auxiliary: 1.62
- distance_to_high_60_pct: -11.19

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,37,37,36.1,36.25,536355,36.11,0.4,35.89,35.5,0.49
20260504,36.45,37.25,36.4,36.55,433128,36.14,1.13,36.04,35.51,0.41
20260505,36.5,37.2,36.5,37.1,442150,36.22,2.42,36.23,35.53,0.42
20260506,37.4,37.4,36.65,37,657058,36.29,1.96,36.45,35.54,0.62
20260507,37.1,38.25,37.1,37.9,906349,36.42,4.06,36.66,35.57,0.84
20260508,38,38.5,37.45,38,1122368,36.55,3.96,36.88,35.6,0.99
20260511,39,41.8,39,41.8,6809218,36.99,13,37.23,35.71,4.86
20260512,43.8,43.8,40.9,41.2,6136318,37.34,10.33,37.59,35.81,3.68
20260513,39.5,39.5,37.2,38.7,4588231,37.45,3.33,37.78,35.87,2.48
20260514,39.05,39.6,38.4,38.55,2124804,37.55,2.67,37.94,35.88,1.12
20260515,38.95,39.25,37.35,37.35,1479948,37.53,-0.48,38.01,35.9,0.77
20260518,37,37.35,35.75,37.15,1094473,37.5,-0.93,38.03,35.93,0.58
20260519,37.15,37.85,36.7,36.75,672000,37.44,-1.83,37.94,35.97,0.39
20260520,36.75,37.2,36.6,36.7,498431,37.37,-1.8,37.83,36,0.3
20260521,37.4,37.85,37.2,37.7,716820,37.4,0.8,37.76,36.02,0.45
20260522,38.3,38.95,37.9,38.55,947138,37.5,2.81,37.81,36.05,0.6
20260525,39,39.9,38.5,39.55,1638323,37.67,5,37.89,36.09,1.01
20260526,39.55,39.65,38.8,39.25,838540,37.8,3.84,37.99,36.11,0.51
20260527,39.4,41.85,39.4,40.65,3044794,38.04,6.87,38.17,36.14,1.74
20260528,40.6,41.2,38.7,38.9,1626156,38.11,2.07,38.28,36.15,0.9
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 51.12
- over_600_ratio: 46.66
- over_800_ratio: 43.2
- over_1000_ratio: 40.54
- over_400_change_1w: -0.29
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.68
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,50.16,,43.12,,40.43,,0,False,False
20260508,50.3,0.14,42.84,-0.28,40.48,0.05,1,False,True
20260515,51.41,1.11,43.23,0.39,41.22,0.74,2,True,True
20260522,51.12,-0.29,43.2,-0.03,40.54,-0.68,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8213 | 志超 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8213 | 志超 | 3 | 1 | 3 | 3 | 3 | continued_2_3d | 連續 3 個交易日上榜，訊號延續但仍需確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8213 | 志超 | 2 | 0 | 116800.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
