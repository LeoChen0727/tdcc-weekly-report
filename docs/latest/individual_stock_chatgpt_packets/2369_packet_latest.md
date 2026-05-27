# INDIVIDUAL STOCK CHATGPT PACKET - 2369 菱生

## Metadata
- generated_at: 2026-05-27 21:26:32 Asia/Taipei
- stock_id: 2369
- stock_name: 菱生
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2369_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2369_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2369_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2369_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2369_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2369_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2369_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2369_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2369_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2369_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2369_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2369_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2369_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2369_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2369_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2369_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2369_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2369_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2369.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2369.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2369.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2369.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2369.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2369.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2369_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2369_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2369_latest.md?ref=main

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
- date: 20260527
- open: 38.85
- high: 41
- low: 36.95
- close: 40.15
- volume: 90986427
- ma5: 34.84
- ema23_primary: 32.09
- distance_to_ema23_pct: 25.12
- ma20: 31.66
- ma60: 30.51
- ma120: 27.6
- return_5d: 39.17
- return_20d: 29.94
- volume_ratio: 4.46
- distance_to_ma20_pct_auxiliary: 26.8
- distance_to_high_60_pct: -2.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,30.6,31,30.2,30.2,6701317,30.45,-0.83,30.48,29,0.42
20260430,30.4,30.8,29.55,29.55,6553599,30.38,-2.72,30.55,28.99,0.42
20260504,29.7,31.8,29.6,31.15,14772236,30.44,2.33,30.6,29.05,0.98
20260505,31.9,33.45,31.7,33.2,33947083,30.67,8.24,30.81,29.12,2.14
20260506,34.25,34.25,31.6,31.9,29516138,30.77,3.66,31,29.18,1.75
20260507,31.9,33.25,31.1,33,20027439,30.96,6.59,31.09,29.25,1.17
20260508,32.8,33.75,30.25,30.7,20342123,30.94,-0.77,31.11,29.3,1.18
20260511,30.9,31.95,30.7,31,11030333,30.94,0.18,31.11,29.36,0.66
20260512,31.05,31.45,30,31.2,10320942,30.96,0.76,31.08,29.45,0.63
20260513,30.55,30.75,30,30.45,6876758,30.92,-1.52,31,29.54,0.43
20260514,30.95,31.4,29.85,30.25,9942030,30.87,-1.99,30.94,29.61,0.63
20260515,30.5,30.55,29.35,29.7,7720999,30.77,-3.47,30.87,29.68,0.5
20260518,29.4,29.6,28.25,29.45,5621016,30.66,-3.94,30.82,29.76,0.36
20260519,29.45,29.55,28.3,28.5,7241474,30.48,-6.49,30.73,29.81,0.47
20260520,28.75,29.15,27.8,28.85,6078386,30.34,-4.92,30.54,29.88,0.43
20260521,29.3,30.3,29.3,30,7045079,30.31,-1.04,30.45,29.96,0.52
20260522,30.5,32.7,30.3,32.05,20618549,30.46,5.22,30.59,30.04,1.54
20260525,33,34.7,31.7,34.3,34218864,30.78,11.44,30.86,30.15,2.35
20260526,37.1,37.7,36.65,37.7,58300950,31.36,20.23,31.2,30.32,3.5
20260527,38.85,41,36.95,40.15,90986427,32.09,25.12,31.66,30.51,4.46
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 31.62
- over_600_ratio: 29.85
- over_800_ratio: 28.66
- over_1000_ratio: 27.54
- over_400_change_1w: -0.12
- over_800_change_1w: -0.41
- over_1000_change_1w: -0.35
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,30.59,,26.75,,25.56,,0,False,False
20260508,33.96,3.37,30.74,3.99,29.61,4.05,1,True,True
20260515,31.74,-2.22,29.07,-1.67,27.89,-1.72,0,False,False
20260522,31.62,-0.12,28.66,-0.41,27.54,-0.35,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260527 | 2369 | 菱生 | true_breakout | 嚴格突破 | 86.0 |  |  | platform_breakout |  | call_strong_inflow | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260521 | 2369 | 菱生 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  | call_strong_inflow | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260527 | 2369 | 菱生 | 5 | 5 | 5 | 5 | 5 | continued_overheated | 連續上榜但短期漲幅或乖離過熱，精華追蹤應降級。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260527 | 2369 | 菱生 | 36 | 0 | 18922650.0 | 0.0 |  | call_strong_inflow | 2 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
