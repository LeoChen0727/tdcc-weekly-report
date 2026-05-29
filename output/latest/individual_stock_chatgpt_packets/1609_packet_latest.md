# INDIVIDUAL STOCK CHATGPT PACKET - 1609 大亞

## Metadata
- generated_at: 2026-05-29 19:31:46 Asia/Taipei
- stock_id: 1609
- stock_name: 大亞
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1609_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1609_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1609_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1609_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1609_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1609_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1609_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1609_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1609_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1609_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1609_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1609_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1609_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1609_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1609_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1609_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1609_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1609_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1609.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1609.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1609.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1609.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1609.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1609.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1609_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1609_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1609_latest.md?ref=main

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
- open: 38
- high: 39.45
- low: 38
- close: 39.25
- volume: 40746891
- ma5: 36.79
- ema23_primary: 35.12
- distance_to_ema23_pct: 11.75
- ma20: 34.95
- ma60: 34.33
- ma120: 36.99
- return_5d: 10.56
- return_20d: 21.89
- volume_ratio: 4.66
- distance_to_ma20_pct_auxiliary: 12.29
- distance_to_high_60_pct: -0.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,32.45,34.15,32.45,33.2,5162433,33.37,-0.5,33.2,36.03,1.81
20260505,33.4,33.4,32.85,33,2398254,33.34,-1.01,33.23,35.87,0.85
20260506,33.35,33.45,32.75,32.9,3014664,33.3,-1.2,33.27,35.7,1.04
20260507,33,34.4,32.9,34.05,6676214,33.36,2.06,33.3,35.53,2.18
20260508,35.2,37.15,35.15,36.05,27013965,33.59,7.33,33.47,35.41,6.29
20260511,36.5,36.5,35.3,36.35,9597557,33.82,7.49,33.62,35.32,2.06
20260512,36.2,36.25,35.2,35.3,7042653,33.94,4,33.7,35.25,1.44
20260513,35.3,35.45,34.3,34.55,4874133,33.99,1.64,33.73,35.17,0.98
20260514,34.55,35.2,34.05,34.1,4011744,34,0.29,33.73,35.08,0.8
20260515,34.45,34.8,33.3,33.5,4736048,33.96,-1.35,33.69,35,0.92
20260518,33.45,34.15,32.8,34.05,3388035,33.97,0.25,33.66,34.94,0.65
20260519,34.45,34.65,33.75,33.75,3214370,33.95,-0.59,33.63,34.87,0.62
20260520,34,34.1,33.45,33.8,3104558,33.94,-0.4,33.62,34.8,0.6
20260521,34.25,35.3,34.25,35.05,5644560,34.03,3,33.69,34.74,1.06
20260522,35.3,35.6,34.8,35.5,5018270,34.15,3.95,33.82,34.65,0.93
20260525,35.95,36.25,35.65,36,7956444,34.31,4.94,33.99,34.58,1.41
20260526,36.65,37,36,36.05,7401608,34.45,4.64,34.19,34.49,1.27
20260527,36.4,37.35,36.3,36.75,10689675,34.64,6.08,34.42,34.43,1.7
20260528,37,38.1,35.7,35.9,13182790,34.75,3.32,34.6,34.34,1.93
20260529,38,39.45,38,39.25,40746891,35.12,11.75,34.95,34.33,4.66
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 31.61
- over_600_ratio: 29.9
- over_800_ratio: 28.79
- over_1000_ratio: 28.02
- over_400_change_1w: 0.21
- over_800_change_1w: 0.64
- over_1000_change_1w: 0.56
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,31.8,,29.11,,28.44,,0,False,False
20260508,31.99,0.19,29.15,0.04,28.71,0.27,1,True,True
20260515,31.4,-0.59,28.15,-1,27.46,-1.25,0,False,False
20260522,31.61,0.21,28.79,0.64,28.02,0.56,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 1609 | 大亞 | true_breakout | 嚴格突破 | 131.0 |  |  | breakout_confirmed |  | call_strong_inflow | continued_many_days | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d |
| 20260521 | 1609 | 大亞 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  | call_strong_inflow | continued_many_days | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 1609 | 大亞 | 7 | 7 | 5 | 7 | 7 | continued_many_days | 連續 7 個交易日上榜，需判斷是持續醞釀或訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 1609 | 大亞 | 25 | 1 | 3371960.0 | 0.0 |  | call_strong_inflow | 2 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
