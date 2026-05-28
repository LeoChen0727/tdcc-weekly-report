# INDIVIDUAL STOCK CHATGPT PACKET - 2420 新巨

## Metadata
- generated_at: 2026-05-28 19:31:56 Asia/Taipei
- stock_id: 2420
- stock_name: 新巨
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2420_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2420_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2420_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2420_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2420_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2420_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2420_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2420_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2420_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2420_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2420_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2420_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2420_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2420_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2420_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2420_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2420_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2420_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2420.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2420.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2420.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2420.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2420.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2420.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2420_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2420_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2420_latest.md?ref=main

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
- open: 63
- high: 65.6
- low: 62.9
- close: 64.5
- volume: 1508337
- ma5: 63.42
- ema23_primary: 59.1
- distance_to_ema23_pct: 9.13
- ma20: 58.66
- ma60: 54.67
- ma120: 52.84
- return_5d: 3.2
- return_20d: 18.78
- volume_ratio: 1.76
- distance_to_ma20_pct_auxiliary: 9.96
- distance_to_high_60_pct: -1.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,54.3,55.3,54.3,54.7,181803,53.99,1.32,53.95,52.33,0.58
20260504,55.2,56,55.1,55.4,325268,54.1,2.39,54.16,52.35,0.99
20260505,55.6,55.6,55.1,55.4,175322,54.21,2.19,54.39,52.38,0.53
20260506,55.7,56,54.8,55,260758,54.28,1.33,54.6,52.42,0.76
20260507,55.5,56.7,55,55.5,557128,54.38,2.06,54.78,52.48,1.54
20260508,55,56,55,55.5,695633,54.47,1.88,54.94,52.55,1.82
20260511,55.5,56.8,55.3,56.5,836257,54.64,3.4,55.13,52.66,2.07
20260512,57,58,56.1,58,802900,54.92,5.6,55.35,52.79,1.93
20260513,57,57,55.5,56.3,833424,55.04,2.29,55.48,52.89,1.9
20260514,56.3,57.9,56.3,56.9,616267,55.19,3.09,55.56,52.99,1.5
20260515,57,57.5,55.9,56.7,563444,55.32,2.5,55.63,53.09,1.35
20260518,56.7,59.7,56.4,59.5,1123579,55.67,6.89,55.85,53.24,2.43
20260519,59.5,59.9,58.4,59.3,835693,55.97,5.95,56.03,53.39,1.71
20260520,59.1,59.3,58.7,58.9,1053397,56.21,4.78,56.19,53.53,2
20260521,59.9,63.4,58.9,62.5,2686317,56.74,10.16,56.52,53.72,4.15
20260522,62.6,63.2,62.1,62.7,1115539,57.23,9.55,56.91,53.9,1.66
20260525,62.7,64.8,62.7,64.7,1060173,57.86,11.83,57.38,54.11,1.48
20260526,64.9,64.9,62.3,62.7,992129,58.26,7.62,57.77,54.3,1.31
20260527,63,64.2,62.3,62.5,927025,58.61,6.63,58.15,54.47,1.17
20260528,63,65.6,62.9,64.5,1508337,59.1,9.13,58.66,54.67,1.76
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 50.87
- over_600_ratio: 46.21
- over_800_ratio: 42.65
- over_1000_ratio: 39.81
- over_400_change_1w: 0.09
- over_800_change_1w: -0.26
- over_1000_change_1w: -0.21
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,50.42,,43.59,,40.7,,0,False,False
20260508,50.71,0.29,43.47,-0.12,40.02,-0.68,1,False,False
20260515,50.78,0.07,42.91,-0.56,40.02,0,2,False,False
20260522,50.87,0.09,42.65,-0.26,39.81,-0.21,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2420 | 新巨 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2420 | 新巨 | 1 | 1 | 2 | 3 | 3 | repeated_but_no_breakout | 近 10 日上榜 3 日、近 20 日上榜 3 日，尚未突破，需分辨醞釀或鈍化。 |

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
