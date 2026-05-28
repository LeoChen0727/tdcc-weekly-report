# INDIVIDUAL STOCK CHATGPT PACKET - 8182 加高

## Metadata
- generated_at: 2026-05-28 19:33:47 Asia/Taipei
- stock_id: 8182
- stock_name: 加高
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8182_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8182_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8182_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8182_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8182_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8182_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8182_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8182_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8182_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8182_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8182_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8182_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8182_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8182_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8182_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8182_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8182_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8182_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8182.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8182.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8182.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8182.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8182.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8182.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8182_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8182_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8182_latest.md?ref=main

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
- open: 44.65
- high: 48.5
- low: 44.35
- close: 47.5
- volume: 11345837
- ma5: 44.81
- ema23_primary: 39.42
- distance_to_ema23_pct: 20.5
- ma20: 39.35
- ma60: 33.53
- ma120: 30.17
- return_5d: 26.33
- return_20d: 27.18
- volume_ratio: 6.25
- distance_to_ma20_pct_auxiliary: 20.7
- distance_to_high_60_pct: -2.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,38.3,38.3,37,37,230000,34.6,6.93,34.55,29.86,0.12
20260504,37.5,38.45,36.35,38.15,247000,34.9,9.31,35,30.01,0.12
20260505,38.1,40.25,38.1,40.25,437000,35.35,13.88,35.62,30.19,0.22
20260506,41.8,41.8,38.8,39.2,546000,35.67,9.91,36.2,30.37,0.27
20260507,39.2,43.1,38.35,43.1,4011000,36.29,18.78,36.97,30.6,1.83
20260508,42.8,44.9,39,39.5,4403000,36.55,8.06,37.52,30.78,1.84
20260511,38.8,39,36.9,37.4,1627000,36.62,2.12,37.9,30.94,0.69
20260512,37.7,38.85,35.4,37.15,1590000,36.67,1.31,38.13,31.11,0.69
20260513,37.65,39,35.8,35.95,1660000,36.61,-1.8,38.34,31.25,0.72
20260514,36.9,37.9,34.6,34.7,1464000,36.45,-4.8,38.46,31.36,0.63
20260515,35.1,36.15,34,34.05,787000,36.25,-6.07,38.39,31.47,0.36
20260518,33.95,37.1,32.5,36.6,1579000,36.28,0.89,38.27,31.63,0.8
20260519,35.9,37.7,35.15,35.75,1328000,36.23,-1.34,37.91,31.77,0.8
20260520,36.05,38,35.9,36.65,2482000,36.27,1.05,37.53,31.94,1.77
20260521,37.4,38.8,37.35,37.6,2383000,36.38,3.35,37.34,32.12,1.68
20260522,38.5,41.35,38.35,41.35,41000,36.79,12.38,37.53,32.35,0.03
20260525,45.45,45.45,43.75,45.45,45000,37.52,21.15,37.95,32.65,0.03
20260526,45.45,45.9,42.2,45.65,44000,38.19,19.52,38.49,32.94,0.03
20260527,47.2,47.2,43.1,44.1,44000,38.69,14,38.85,33.21,0.03
20260528,44.65,48.5,44.35,47.5,11345837,39.42,20.5,39.35,33.53,6.25
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.01
- over_600_ratio: 67.01
- over_800_ratio: 65.04
- over_1000_ratio: 65.04
- over_400_change_1w: 0.16
- over_800_change_1w: 0.11
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.58,,65.12,,65.12,,0,False,False
20260508,68.55,-0.03,65.15,0.03,65.15,0.03,1,False,True
20260515,67.85,-0.7,64.93,-0.22,64.93,-0.22,0,False,False
20260522,68.01,0.16,65.04,0.11,65.04,0.11,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8182 | 加高 | true_breakout | 嚴格突破 | 102.0 |  |  | platform_breakout |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 8182 | 加高 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

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
