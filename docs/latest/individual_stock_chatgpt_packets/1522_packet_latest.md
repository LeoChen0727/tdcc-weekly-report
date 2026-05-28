# INDIVIDUAL STOCK CHATGPT PACKET - 1522 堤維西

## Metadata
- generated_at: 2026-05-28 19:31:34 Asia/Taipei
- stock_id: 1522
- stock_name: 堤維西
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1522_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1522_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1522_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1522_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1522_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1522_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1522_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1522_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1522_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1522_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1522_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1522_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1522_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1522_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1522_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1522_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1522_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1522_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1522.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1522.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1522.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1522.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1522.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1522.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1522_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1522_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1522_latest.md?ref=main

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
- open: 31.35
- high: 31.45
- low: 31.35
- close: 31.45
- volume: 3536658
- ma5: 29.56
- ema23_primary: 30.56
- distance_to_ema23_pct: 2.9
- ma20: 30.48
- ma60: 33.04
- ma120: 40.34
- return_5d: 6.07
- return_20d: 0.64
- volume_ratio: 2.28
- distance_to_ma20_pct_auxiliary: 3.17
- distance_to_high_60_pct: -28.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,31.55,31.6,30.8,30.95,1013932,32.64,-5.18,31.94,38.44,1.29
20260504,30.95,31.4,30.8,31,815461,32.5,-4.63,31.88,38.11,1.03
20260505,31.15,31.85,31,31.7,1063622,32.44,-2.27,31.89,37.79,1.3
20260506,31.7,31.9,31.05,31.05,1080544,32.32,-3.93,31.88,37.45,1.29
20260507,31.1,34.15,31.05,34.15,3033993,32.47,5.16,31.97,37.18,3.16
20260508,32.8,33.3,32,32.1,5454156,32.44,-1.05,32,36.89,4.53
20260511,32,32,31.2,31.6,1798417,32.37,-2.38,32.01,36.6,1.42
20260512,32,32,31.05,31.4,1252650,32.29,-2.76,31.97,36.32,0.99
20260513,31.4,31.4,30.85,31.1,949110,32.19,-3.39,31.89,36.02,0.74
20260514,31.1,31.1,30.1,30.15,1976686,32.02,-5.84,31.76,35.7,1.47
20260515,30.15,30.4,29.5,29.5,1748604,31.81,-7.27,31.57,35.38,1.26
20260518,29.45,29.45,28.9,29.25,1081556,31.6,-7.43,31.39,35.09,0.78
20260519,29.25,29.7,29,29.2,689029,31.4,-7,31.24,34.79,0.5
20260520,29.45,29.45,28.85,29.1,691073,31.21,-6.75,31.07,34.48,0.5
20260521,29.2,29.65,29.2,29.65,621407,31.08,-4.59,30.95,34.23,0.45
20260522,29.65,29.7,29.25,29.45,729760,30.94,-4.82,30.84,33.99,0.54
20260525,29.55,29.9,29.05,29.2,1045104,30.8,-5.18,30.73,33.74,0.77
20260526,29.2,29.5,29,29.1,775512,30.65,-5.07,30.62,33.5,0.57
20260527,29.1,29.1,28.55,28.6,1649272,30.48,-6.18,30.48,33.24,1.17
20260528,31.35,31.45,31.35,31.45,3536658,30.56,2.9,30.48,33.04,2.28
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 57.86
- over_600_ratio: 55.32
- over_800_ratio: 54.51
- over_1000_ratio: 53.15
- over_400_change_1w: -0.11
- over_800_change_1w: 0.07
- over_1000_change_1w: 0.07
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.4,,54.81,,52.86,,0,False,False
20260508,59.14,-0.26,54.84,0.03,52.89,0.03,1,False,True
20260515,57.97,-1.17,54.44,-0.4,53.08,0.19,2,False,True
20260522,57.86,-0.11,54.51,0.07,53.15,0.07,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1522 | 堤維西 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260528 | 1522 | 堤維西 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260528 | 1522 | 堤維西 | revenue_breakout_low_response | 營收爆發低反應股 | 13.0 | 19.0 | B_可觀察 |  |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260528 | 1522 | 堤維西 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1522 | 堤維西 | 4 | 4 | 4 | 4 | 4 | repeated_but_no_breakout | 近 10 日上榜 4 日、近 20 日上榜 4 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1522 | 堤維西 | 3 | 0 | 37830.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
