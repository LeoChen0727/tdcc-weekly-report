# INDIVIDUAL STOCK CHATGPT PACKET - 1708 東鹼

## Metadata
- generated_at: 2026-05-30 23:41:06 Asia/Taipei
- stock_id: 1708
- stock_name: 東鹼
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1708_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1708_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1708_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1708_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1708_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1708_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1708_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1708_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1708_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1708_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1708_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1708_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1708_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1708_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1708_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1708_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1708_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1708_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1708.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1708.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1708.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1708.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1708.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1708.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1708_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1708_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1708_latest.md?ref=main

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
- open: 37
- high: 38.3
- low: 36.9
- close: 38.2
- volume: 2553741
- ma5: 38.3
- ema23_primary: 39.39
- distance_to_ema23_pct: -3.03
- ma20: 39.36
- ma60: 40.27
- ma120: 36.87
- return_5d: -2.43
- return_20d: -8.61
- volume_ratio: 0.75
- distance_to_ma20_pct_auxiliary: -2.95
- distance_to_high_60_pct: -19.49

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,41.8,41.8,39.3,39.45,6270914,40.72,-3.12,40.63,38.88,1.06
20260505,39.8,40.25,39.55,40.2,3275644,40.68,-1.18,40.55,38.99,0.56
20260506,40.45,40.45,39.2,39.2,2786604,40.56,-3.34,40.34,39.08,0.49
20260507,39.2,39.2,37.7,38.1,4980963,40.35,-5.58,40.3,39.15,0.95
20260508,38.1,38.7,37.15,37.2,3689998,40.09,-7.21,40.19,39.2,0.73
20260511,38.65,40.4,38.55,40.15,6248057,40.09,0.14,40.22,39.31,1.2
20260512,39.95,41.8,39.25,41.75,4377500,40.23,3.77,40.22,39.45,0.87
20260513,41.35,42.35,41.1,41.6,3175429,40.35,3.11,40.23,39.58,0.64
20260514,41.6,41.6,40.45,40.5,2487053,40.36,0.35,40.23,39.67,0.52
20260515,40.45,40.45,39.4,39.65,2218495,40.3,-1.61,40.21,39.76,0.46
20260518,40.2,40.5,39.35,39.65,1866456,40.25,-1.48,40.23,39.85,0.4
20260519,39.65,40.95,39.5,39.85,2597635,40.21,-0.9,40.25,39.93,0.55
20260520,40.05,40.3,39.1,39.55,1830618,40.16,-1.51,40.27,40,0.39
20260521,39.5,39.9,39.45,39.7,1518169,40.12,-1.04,40.3,40.08,0.33
20260522,39.65,39.7,39.05,39.15,2613423,40.04,-2.22,40.28,40.14,0.58
20260525,39.15,40.4,38.8,40.05,3465125,40.04,0.03,40.23,40.21,0.81
20260526,40.15,40.2,38.3,38.3,6095701,39.89,-4,40.02,40.25,1.58
20260527,38.5,38.75,38.2,38.45,2433743,39.77,-3.33,39.83,40.29,0.65
20260528,37.1,37.7,36.5,36.5,3428516,39.5,-7.6,39.54,40.27,0.96
20260529,37,38.3,36.9,38.2,2553741,39.39,-3.03,39.36,40.27,0.75
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 46.58
- over_600_ratio: 45.44
- over_800_ratio: 42.63
- over_1000_ratio: 40.43
- over_400_change_1w: -2.33
- over_800_change_1w: -2.91
- over_1000_change_1w: -2.62
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,48.13,,44.87,,41.69,,0,False,False
20260508,47.11,-1.02,42.65,-2.22,39.82,-1.87,0,False,False
20260515,49.62,2.51,46.37,3.72,43.13,3.31,1,True,True
20260522,48.91,-0.71,45.54,-0.83,43.05,-0.08,0,False,False
20260529,46.58,-2.33,42.63,-2.91,40.43,-2.62,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260530 | 1708 | 東鹼 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260521 | 1708 | 東鹼 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  | call_inflow | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260530 | 1708 | 東鹼 | 8 | 8 | 5 | 8 | 8 | repeated_but_no_breakout | 近 10 日上榜 8 日、近 20 日上榜 8 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260529 | 1708 | 東鹼 | 23 | 0 | 1263710.0 | 0.0 |  | call_inflow | 1 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
