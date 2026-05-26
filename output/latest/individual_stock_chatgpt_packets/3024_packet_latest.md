# INDIVIDUAL STOCK CHATGPT PACKET - 3024 憶聲

## Metadata
- generated_at: 2026-05-26 23:01:02 Asia/Taipei
- stock_id: 3024
- stock_name: 憶聲
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3024_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3024_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3024_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3024_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3024_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3024_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3024_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3024_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3024_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3024_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3024_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3024_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3024_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3024_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3024_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3024_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3024_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3024_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3024.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3024.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3024.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3024.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3024.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3024.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3024_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3024_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3024_latest.md?ref=main

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
- date: 20260526
- open: 16.05
- high: 16.25
- low: 15.5
- close: 16.1
- volume: 3156954
- ma5: 16.94
- ema23_primary: 15.25
- distance_to_ema23_pct: 5.59
- ma20: 15.36
- ma60: 12.29
- ma120: 11.58
- return_5d: -7.47
- return_20d: 17.52
- volume_ratio: 0.6
- distance_to_ma20_pct_auxiliary: 4.82
- distance_to_high_60_pct: -12.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,13.85,13.85,13.35,13.5,2829673,11.76,14.78,11.34,10.76,0.84
20260429,13.6,13.8,13,13.1,2602314,11.87,10.33,11.49,10.8,0.75
20260430,13.2,13.3,12.55,12.7,2469122,11.94,6.35,11.62,10.82,0.69
20260504,12.9,13.3,12.75,13.3,2386210,12.06,10.33,11.79,10.86,0.65
20260505,13.15,13.8,13.1,13.8,3183038,12.2,13.11,11.97,10.9,0.85
20260506,14,14.1,13.6,13.85,3917309,12.34,12.26,12.15,10.95,1
20260507,14.05,15.2,13.8,14.6,10343071,12.53,16.55,12.37,11.01,2.35
20260508,14.55,14.7,14,14.25,4213654,12.67,12.47,12.58,11.07,0.92
20260511,14.35,14.85,14.25,14.55,3765134,12.83,13.43,12.8,11.14,0.8
20260512,14.7,14.95,14.6,14.85,2834268,13,14.27,13.03,11.21,0.59
20260513,14.95,15.85,14.9,15.4,4880179,13.2,16.7,13.3,11.3,0.97
20260514,15.75,16.9,15.75,16.55,10894967,13.48,22.82,13.62,11.4,2
20260515,16.7,17.75,16.45,16.85,9045674,13.76,22.49,13.95,11.51,1.56
20260518,17,17.95,16.95,17.8,7458185,14.09,26.3,14.29,11.63,1.25
20260519,18.05,18.4,17.1,17.4,8784838,14.37,21.09,14.56,11.75,1.44
20260520,17.6,18.4,17.5,17.8,4598533,14.65,21.46,14.79,11.88,0.77
20260521,18.05,18.05,16.65,17.15,6003127,14.86,15.39,14.95,11.99,1.09
20260522,17.1,17.75,16.6,17.6,3534283,15.09,16.63,15.13,12.11,0.68
20260525,17.95,17.95,15.9,16.05,7539508,15.17,5.79,15.24,12.2,1.43
20260526,16.05,16.25,15.5,16.1,3156954,15.25,5.59,15.36,12.29,0.6
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 50.85
- over_600_ratio: 47.03
- over_800_ratio: 41.67
- over_1000_ratio: 38.09
- over_400_change_1w: 0.77
- over_800_change_1w: -0.82
- over_1000_change_1w: -0.64
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.76,,41.5,,38.52,,0,False,False
20260508,50.44,0.68,43.1,1.6,39.41,0.89,1,True,True
20260515,50.08,-0.36,42.49,-0.61,38.73,-0.68,0,False,False
20260522,50.85,0.77,41.67,-0.82,38.09,-0.64,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 3024 | 憶聲 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 3024 | 憶聲 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

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
