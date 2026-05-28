# INDIVIDUAL STOCK CHATGPT PACKET - 2409 友達

## Metadata
- generated_at: 2026-05-28 19:31:55 Asia/Taipei
- stock_id: 2409
- stock_name: 友達
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2409_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2409_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2409_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2409_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2409_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2409_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2409_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2409_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2409_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2409_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2409_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2409_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2409_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2409_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2409_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2409_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2409_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2409_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2409.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2409.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2409.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2409.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2409.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2409.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2409_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2409_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2409_latest.md?ref=main

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
- open: 21.9
- high: 23.4
- low: 21.2
- close: 21.2
- volume: 538705306
- ma5: 22.32
- ema23_primary: 19.92
- distance_to_ema23_pct: 6.42
- ma20: 19.68
- ma60: 17.73
- ma120: 15.66
- return_5d: 4.95
- return_20d: 22.54
- volume_ratio: 1.59
- distance_to_ma20_pct_auxiliary: 7.74
- distance_to_high_60_pct: -17.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,17.5,17.6,16.95,17.2,107364483,17.55,-2.02,18.11,16.24,0.29
20260504,16.9,17.25,16.6,16.95,185186551,17.5,-3.17,18.16,16.27,0.5
20260505,17.25,18,17.2,17.85,283447210,17.53,1.81,18.2,16.32,0.81
20260506,18.15,18.4,17.5,18.05,247854591,17.58,2.7,18.3,16.38,0.72
20260507,18.3,18.8,18.05,18.35,263748821,17.64,4.02,18.36,16.45,0.77
20260508,18.45,18.9,17.75,17.85,206094211,17.66,1.09,18.32,16.52,0.65
20260511,18.5,19.1,18.25,18.85,317856734,17.76,6.15,18.35,16.6,1.09
20260512,19.2,20.7,18.85,20.7,730161791,18,14.98,18.48,16.72,2.32
20260513,20.2,20.5,19.25,20.2,518461486,18.19,11.08,18.5,16.83,1.66
20260514,20.7,20.7,19.3,19.55,323755549,18.3,6.83,18.48,16.9,1.1
20260515,19.6,20.3,18.9,19.05,317634644,18.36,3.75,18.4,16.96,1.14
20260518,18.8,19.5,18.2,19.25,207880657,18.44,4.42,18.37,17.03,0.77
20260519,19.25,20.15,19,19.15,189970827,18.5,3.54,18.36,17.1,0.72
20260520,19.25,19.3,18.6,18.75,118262550,18.52,1.26,18.36,17.16,0.46
20260521,19.1,20.45,19.05,20.2,367725205,18.66,8.27,18.44,17.23,1.38
20260522,20.85,22.2,20.55,22.2,394425774,18.95,17.14,18.66,17.34,1.46
20260525,24.35,24.4,24.15,24.4,82302936,19.41,25.73,19.02,17.47,0.31
20260526,25.5,25.8,22,22,818361725,19.62,12.12,19.25,17.57,2.77
20260527,22.15,22.2,20.5,21.8,566175271,19.8,10.08,19.48,17.66,1.78
20260528,21.9,23.4,21.2,21.2,538705306,19.92,6.42,19.68,17.73,1.59
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 53.08
- over_600_ratio: 50.86
- over_800_ratio: 49.43
- over_1000_ratio: 48.24
- over_400_change_1w: 1.64
- over_800_change_1w: 1.82
- over_1000_change_1w: 1.77
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.96,,46.02,,44.82,,0,False,False
20260508,49.63,-0.33,45.72,-0.3,44.54,-0.28,0,False,False
20260515,51.44,1.81,47.61,1.89,46.47,1.93,1,True,True
20260522,53.08,1.64,49.43,1.82,48.24,1.77,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2409 | 友達 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_put_bullish | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2409 | 友達 | 1 | 1 | 3 | 3 | 3 | repeated_but_no_breakout | 近 10 日上榜 3 日、近 20 日上榜 3 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2409 | 友達 | 190 | 11 | 53495110.0 | 188680.0 | 283.52 | call_put_bullish | 3 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
