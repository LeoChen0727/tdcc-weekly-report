# INDIVIDUAL STOCK CHATGPT PACKET - 3577 泓格

## Metadata
- generated_at: 2026-05-28 19:32:31 Asia/Taipei
- stock_id: 3577
- stock_name: 泓格
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3577_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3577_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3577_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3577_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3577_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3577_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3577_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3577_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3577_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3577_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3577_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3577_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3577_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3577_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3577_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3577_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3577_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3577_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3577.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3577.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3577.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3577.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3577.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3577.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3577_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3577_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3577_latest.md?ref=main

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
- open: 146.5
- high: 161
- low: 145
- close: 161
- volume: 2526105
- ma5: 153.3
- ema23_primary: 119.11
- distance_to_ema23_pct: 35.17
- ma20: 115.46
- ma60: 85.73
- ma120: 74.3
- return_5d: 21.51
- return_20d: 95.63
- volume_ratio: 2.18
- distance_to_ma20_pct_auxiliary: 39.44
- distance_to_high_60_pct: -3.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,84,89.5,83.5,87.3,535000,78.19,11.65,79.22,68.55,2.15
20260504,90.9,91.5,87.8,88.9,421000,79.08,12.42,80.08,68.97,1.6
20260505,89.3,90.1,86,88.4,202000,79.86,10.7,80.89,69.38,0.75
20260506,89.8,90.5,86.5,89.7,171000,80.68,11.18,81.57,69.83,0.65
20260507,89.7,90.1,87.6,87.6,172000,81.25,7.81,82.14,70.24,0.66
20260508,87.7,89.9,87,89.5,158000,81.94,9.22,82.75,70.7,0.61
20260511,98,98.2,91.3,92.1,671000,82.79,11.25,83.51,71.23,2.52
20260512,89.8,92.3,88.4,90.6,326000,83.44,8.58,84.17,71.72,1.22
20260513,94.5,99.6,93.2,99.6,1661000,84.79,17.47,85.36,72.36,4.82
20260514,109.5,109.5,109.5,109.5,1591000,86.85,26.09,86.97,73.14,3.88
20260515,113,119.5,105.5,108,3289000,88.61,21.89,88.5,73.92,5.81
20260518,106,118.5,106,118.5,1721000,91.1,30.08,90.42,74.86,2.69
20260519,119.5,130,117,126.5,4183000,94.05,34.5,92.71,75.91,4.98
20260520,126.5,136,122.5,134,2587000,97.38,37.61,95.33,77.05,2.69
20260521,134.5,140.5,129.5,132.5,2373000,100.31,32.1,97.81,78.18,2.22
20260522,143,145.5,135.5,145.5,143000,104.07,39.81,100.92,79.54,0.14
20260525,155,160,151.5,160,158000,108.73,47.15,104.76,81.14,0.15
20260526,160,166,153.5,153.5,159000,112.46,36.49,108.28,82.67,0.15
20260527,158.5,159,141.5,146.5,150000,115.3,27.06,111.53,84.08,0.14
20260528,146.5,161,145,161,2526105,119.11,35.17,115.46,85.73,2.18
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.07
- over_600_ratio: 62.83
- over_800_ratio: 58.58
- over_1000_ratio: 50.15
- over_400_change_1w: -0.92
- over_800_change_1w: -1.5
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,69,,61.26,,50.1,,0,False,False
20260508,69.11,0.11,60.12,-1.14,50.13,0.03,1,False,True
20260515,68.99,-0.12,60.08,-0.04,50.15,0.02,2,False,True
20260522,68.07,-0.92,58.58,-1.5,50.15,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3577 | 泓格 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3577 | 泓格 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

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
