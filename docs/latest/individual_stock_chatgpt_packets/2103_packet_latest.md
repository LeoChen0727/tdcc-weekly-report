# INDIVIDUAL STOCK CHATGPT PACKET - 2103 台橡

## Metadata
- generated_at: 2026-05-28 19:31:46 Asia/Taipei
- stock_id: 2103
- stock_name: 台橡
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2103_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2103_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2103_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2103_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2103_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2103_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2103_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2103_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2103_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2103_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2103_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2103_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2103_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2103_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2103_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2103_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2103_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2103_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2103.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2103.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2103.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2103.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2103.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2103.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2103_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2103_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2103_latest.md?ref=main

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
- open: 18.8
- high: 19.1
- low: 18.65
- close: 18.95
- volume: 3295837
- ma5: 19.26
- ema23_primary: 19.86
- distance_to_ema23_pct: -4.59
- ma20: 20.12
- ma60: 19.91
- ma120: 17.86
- return_5d: -7.33
- return_20d: -3.32
- volume_ratio: 0.54
- distance_to_ma20_pct_auxiliary: -5.83
- distance_to_high_60_pct: -16.52

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,19.6,19.95,19.4,19.65,3362384,19.39,1.34,19.32,18.76,0.68
20260504,19.7,19.8,19,19.15,3406465,19.37,-1.13,19.3,18.83,0.68
20260505,19.25,19.9,19.15,19.65,3060226,19.39,1.32,19.34,18.89,0.63
20260506,19.85,20.65,19.75,19.95,6143797,19.44,2.63,19.35,18.97,1.23
20260507,19.95,19.95,19,19.25,5911029,19.42,-0.89,19.36,19.03,1.17
20260508,19.95,21.15,19.8,20.3,23456135,19.5,4.12,19.4,19.11,3.89
20260511,20.1,21.5,20.1,21.1,12265925,19.63,7.49,19.48,19.2,1.89
20260512,21.1,21.6,20.75,21.3,6247887,19.77,7.74,19.57,19.31,0.94
20260513,21.4,21.9,20.9,21.6,5137610,19.92,8.42,19.65,19.43,0.77
20260514,21.7,22.45,21.5,22,6625740,20.1,9.48,19.78,19.55,0.99
20260515,22.2,22.2,20.75,20.75,7747420,20.15,2.98,19.85,19.64,1.11
20260518,20.7,20.8,20.1,20.4,4472465,20.17,1.14,19.92,19.73,0.63
20260519,20.6,20.8,20.1,20.25,2728500,20.18,0.36,20.01,19.79,0.4
20260520,20.25,20.4,19.65,20.35,4846150,20.19,0.78,20.09,19.86,0.69
20260521,20.45,20.65,20.2,20.45,2830863,20.21,1.17,20.18,19.93,0.4
20260522,20.5,20.5,19.75,19.8,5476070,20.18,-1.88,20.21,19.97,0.77
20260525,19.8,19.8,19.2,19.5,5589920,20.12,-3.09,20.26,19.96,0.78
20260526,19.7,19.75,19.2,19.25,3510625,20.05,-3.99,20.2,19.94,0.54
20260527,19.4,19.4,18.7,18.8,7012270,19.95,-5.74,20.16,19.91,1.13
20260528,18.8,19.1,18.65,18.95,3295837,19.86,-4.59,20.12,19.91,0.54
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 53.16
- over_600_ratio: 50.69
- over_800_ratio: 49.72
- over_1000_ratio: 48.3
- over_400_change_1w: -0.56
- over_800_change_1w: -0.73
- over_1000_change_1w: -0.31
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,52.56,,48.97,,47.79,,0,False,False
20260508,52.6,0.04,48.99,0.02,47.89,0.1,1,False,True
20260515,53.72,1.12,50.45,1.46,48.61,0.72,2,True,True
20260522,53.16,-0.56,49.72,-0.73,48.3,-0.31,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260521 | 2103 | 台橡 | pattern | 型態觀察 |  |  |  | 接近突破型 |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2103 | 台橡 | 6 | 6 | 5 | 6 | 6 | repeated_but_no_breakout | 近 10 日上榜 6 日、近 20 日上榜 6 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2103 | 台橡 | 5 | 0 | 216510.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
