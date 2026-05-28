# INDIVIDUAL STOCK CHATGPT PACKET - 8383 千附

## Metadata
- generated_at: 2026-05-28 19:33:50 Asia/Taipei
- stock_id: 8383
- stock_name: 千附
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8383_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8383_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8383_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8383_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8383_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8383_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8383_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8383_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8383_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8383_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8383_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8383_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8383_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8383_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8383_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8383_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8383_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8383_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8383.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8383.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8383.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8383.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8383.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8383.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8383_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8383_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8383_latest.md?ref=main

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
- open: 60.9
- high: 62.6
- low: 59.9
- close: 60
- volume: 1493878
- ma5: 60.86
- ema23_primary: 58.67
- distance_to_ema23_pct: 2.27
- ma20: 59.33
- ma60: 52.94
- ma120: 47.02
- return_5d: 6.01
- return_20d: -3.23
- volume_ratio: 0.92
- distance_to_ma20_pct_auxiliary: 1.13
- distance_to_high_60_pct: -22.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,62.7,64.6,61.8,62.9,2426000,57.87,8.7,57.56,47.32,0.6
20260504,63.9,66.6,63.1,66.5,2353000,58.59,13.51,58.67,47.72,0.57
20260505,65.3,66.3,63.8,64.1,2239000,59.05,8.56,59.66,48.08,0.53
20260506,65,65.1,61.9,63.5,2155000,59.42,6.87,60.62,48.43,0.5
20260507,64.5,66.7,63.2,66.7,2408000,60.02,11.12,61.69,48.84,0.54
20260508,64,64.7,60.1,60.1,5203000,60.03,0.12,62.31,49.15,1.16
20260511,57.1,57.5,54.8,56,4114000,59.69,-6.19,62.67,49.4,0.91
20260512,56.1,57.2,55.1,56.7,1738000,59.45,-4.62,62.85,49.67,0.4
20260513,56,57.4,55.2,56,1343000,59.16,-5.34,62.98,49.93,0.32
20260514,57,57,54.1,54.6,1628000,58.78,-7.11,63.02,50.15,0.39
20260515,55,56,54.3,54.5,1009000,58.42,-6.71,62.91,50.37,0.25
20260518,54.4,54.5,53,54.2,874000,58.07,-6.66,62.5,50.6,0.24
20260519,54.2,55.8,54.2,55,1054000,57.81,-4.87,61.82,50.84,0.31
20260520,55,55.7,54.4,54.9,914000,57.57,-4.64,60.97,51.08,0.32
20260521,55.6,56.8,55.2,56.6,1210000,57.49,-1.55,60.17,51.34,0.46
20260522,58.9,60.9,58.1,59.3,60000,57.64,2.88,59.81,51.64,0.03
20260525,60.3,65,60.1,63.5,62000,58.13,9.24,59.77,52,0.03
20260526,64.1,64.1,61.1,61.3,62000,58.39,4.98,59.62,52.32,0.03
20260527,62.3,62.3,59.5,60.2,60000,58.54,2.83,59.43,52.63,0.04
20260528,60.9,62.6,59.9,60,1493878,58.67,2.27,59.33,52.94,0.92
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 51.81
- over_600_ratio: 48.36
- over_800_ratio: 45.83
- over_1000_ratio: 45.04
- over_400_change_1w: -0.16
- over_800_change_1w: -0.12
- over_1000_change_1w: -0.12
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.04,,47.1,,45.58,,0,False,False
20260508,53.68,-0.36,47.38,0.28,44.87,-0.71,1,False,True
20260515,51.97,-1.71,45.95,-1.43,45.16,0.29,2,False,True
20260522,51.81,-0.16,45.83,-0.12,45.04,-0.12,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8383 | 千附 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260528 | 8383 | 千附 | revenue_pullback | 營收成長股價回檔 | 67.0 |  |  |  |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8383 | 千附 | 1 | 1 | 2 | 2 | 2 | first_seen | 歷史上榜資料仍少，先當新訊號觀察。 |

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
