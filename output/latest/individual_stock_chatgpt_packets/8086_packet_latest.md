# INDIVIDUAL STOCK CHATGPT PACKET - 8086 宏捷科

## Metadata
- generated_at: 2026-05-28 19:33:45 Asia/Taipei
- stock_id: 8086
- stock_name: 宏捷科
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8086_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8086_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8086_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8086_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8086_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8086_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8086_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8086_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8086_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8086_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8086_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8086_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8086_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8086_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8086_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8086_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8086_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8086_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8086.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8086.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8086.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8086.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8086.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8086.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8086_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8086_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8086_latest.md?ref=main

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
- open: 174.5
- high: 175.5
- low: 161
- close: 165.5
- volume: 9736370
- ma5: 168.1
- ema23_primary: 154.95
- distance_to_ema23_pct: 6.81
- ma20: 156.15
- ma60: 141.46
- ma120: 126.35
- return_5d: 11.07
- return_20d: 16.55
- volume_ratio: 1.35
- distance_to_ma20_pct_auxiliary: 5.99
- distance_to_high_60_pct: -9.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,142.5,150,142.5,144,7988000,138.4,4.04,139.97,128.98,0.79
20260504,148.5,151,144,150.5,8543000,139.41,7.95,141.35,129.4,0.83
20260505,150,156,149,154,8655000,140.63,9.51,142.78,129.92,0.82
20260506,159.5,163,151.5,156,14249000,141.91,9.93,143.68,130.44,1.34
20260507,159,159.5,151,155,7504000,143,8.39,144.15,130.97,0.74
20260508,158,170.5,155,159.5,29253000,144.37,10.48,145,131.68,2.62
20260511,163.5,165,153.5,162,14740000,145.84,11.08,145.88,132.51,1.29
20260512,164.5,167.5,157,158,8776000,146.86,7.59,146.85,133.42,0.76
20260513,156,161,153,157,6471000,147.7,6.3,147.9,134.23,0.56
20260514,159.5,160.5,152.5,154,4808000,148.23,3.9,148.9,134.88,0.42
20260515,155.5,160,148.5,150,7638000,148.37,1.1,149.35,135.43,0.67
20260518,147,148,140.5,147.5,3877000,148.3,-0.54,149.3,136.03,0.38
20260519,145.5,148.5,140.5,141.5,4264000,147.73,-4.22,148.88,136.47,0.45
20260520,141.5,146,140.5,144.5,3355000,147.46,-2.01,148.8,136.94,0.37
20260521,146,151,145,149,3651000,147.59,0.95,148.78,137.57,0.42
20260522,151,162,150,159.5,158000,148.58,7.35,149.97,138.32,0.02
20260525,166,171.5,161,163,166000,149.79,8.82,151.22,138.98,0.02
20260526,166,179,158.5,179,170000,152.22,17.59,153.47,139.96,0.02
20260527,182.5,183,170.5,173.5,175000,153.99,12.67,154.97,140.8,0.03
20260528,174.5,175.5,161,165.5,9736370,154.95,6.81,156.15,141.46,1.35
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.21
- over_600_ratio: 53.49
- over_800_ratio: 53.16
- over_1000_ratio: 50.72
- over_400_change_1w: -0.95
- over_800_change_1w: -0.51
- over_1000_change_1w: -1.12
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.95,,50.81,,48.55,,0,False,False
20260508,58.07,3.12,53.37,2.56,51.99,3.44,1,True,True
20260515,58.16,0.09,53.67,0.3,51.84,-0.15,2,False,True
20260522,57.21,-0.95,53.16,-0.51,50.72,-1.12,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8086 | 宏捷科 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260528 | 8086 | 宏捷科 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260521 | 8086 | 宏捷科 | pattern | 型態觀察 |  |  |  | 已突破但未過熱 |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8086 | 宏捷科 | 6 | 6 | 5 | 6 | 6 | repeated_but_no_breakout | 近 10 日上榜 6 日、近 20 日上榜 6 日，尚未突破，需分辨醞釀或鈍化。 |

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
