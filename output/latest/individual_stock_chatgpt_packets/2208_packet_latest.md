# INDIVIDUAL STOCK CHATGPT PACKET - 2208 台船

## Metadata
- generated_at: 2026-05-28 19:31:48 Asia/Taipei
- stock_id: 2208
- stock_name: 台船
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2208_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2208_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2208_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2208_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2208_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2208_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2208_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2208_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2208_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2208_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2208_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2208_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2208_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2208_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2208_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2208_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2208_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2208_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2208.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2208.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2208.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2208.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2208.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2208.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2208_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2208_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2208_latest.md?ref=main

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
- open: 18.1
- high: 18.3
- low: 17.85
- close: 18
- volume: 4882773
- ma5: 18.21
- ema23_primary: 19.22
- distance_to_ema23_pct: -6.35
- ma20: 19.34
- ma60: 20.45
- ma120: 20.92
- return_5d: -3.49
- return_20d: -10.45
- volume_ratio: 1.06
- distance_to_ma20_pct_auxiliary: -6.94
- distance_to_high_60_pct: -23.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,20.15,20.25,19.8,19.8,4440108,20.62,-3.96,20.45,21.52,1.3
20260504,20.1,20.4,20,20.15,3848501,20.58,-2.08,20.44,21.49,1.11
20260505,20.2,20.4,19.95,20.35,3136136,20.56,-1.02,20.45,21.45,0.9
20260506,20.4,20.5,20.15,20.15,3274135,20.52,-1.83,20.44,21.42,0.92
20260507,20.4,20.8,20.1,20.8,4392847,20.55,1.23,20.45,21.39,1.21
20260508,21.25,21.9,21.05,21.7,10171002,20.64,5.12,20.5,21.37,2.53
20260511,21.1,21.1,20,20.2,9882198,20.61,-1.97,20.49,21.34,2.25
20260512,20.25,20.3,20,20,5068206,20.56,-2.71,20.49,21.3,1.17
20260513,20.05,20.25,19.9,19.95,2963102,20.51,-2.71,20.47,21.28,0.68
20260514,20.2,20.2,19.75,19.75,3461234,20.44,-3.39,20.44,21.25,0.8
20260515,19.9,19.9,19.05,19.15,6029090,20.34,-5.83,20.36,21.22,1.36
20260518,19,19,18.7,18.7,4116617,20.2,-7.42,20.23,21.17,0.93
20260519,18.7,18.7,18.2,18.2,4223738,20.03,-9.15,20.1,21.09,0.95
20260520,18.35,18.7,18.2,18.25,2388246,19.88,-8.22,19.98,21.02,0.54
20260521,18.45,18.65,18.25,18.65,2526741,19.78,-5.72,19.88,20.94,0.57
20260522,18.8,18.9,18.35,18.55,3365368,19.68,-5.73,19.77,20.85,0.78
20260525,18.6,18.6,18.05,18.15,6580356,19.55,-7.17,19.67,20.75,1.46
20260526,18.4,18.4,18.15,18.25,3417302,19.44,-6.13,19.56,20.65,0.75
20260527,18.15,18.3,18.05,18.1,4181369,19.33,-6.37,19.45,20.54,0.91
20260528,18.1,18.3,17.85,18,4882773,19.22,-6.35,19.34,20.45,1.06
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.79
- over_600_ratio: 54.67
- over_800_ratio: 52.95
- over_1000_ratio: 52.12
- over_400_change_1w: -0.51
- over_800_change_1w: -0.5
- over_1000_change_1w: -0.58
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.65,,53.93,,53.25,,0,False,False
20260508,57.75,0.1,54.16,0.23,53.4,0.15,1,True,True
20260515,57.3,-0.45,53.45,-0.71,52.7,-0.7,0,False,False
20260522,56.79,-0.51,52.95,-0.5,52.12,-0.58,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2208 | 台船 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260528 | 2208 | 台船 | revenue_breakout_low_response | 營收爆發低反應股 | 12.0 | 29.0 | D_降級_TDCC轉弱 |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2208 | 台船 | 6 | 6 | 5 | 6 | 6 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

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
