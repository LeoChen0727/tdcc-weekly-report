# INDIVIDUAL STOCK CHATGPT PACKET - 3031 佰鴻

## Metadata
- generated_at: 2026-05-28 20:18:59 Asia/Taipei
- stock_id: 3031
- stock_name: 佰鴻
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3031_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3031_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3031_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3031_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3031_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3031_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3031_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3031_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3031_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3031_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3031_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3031_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3031_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3031_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3031_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3031_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3031_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3031_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3031.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3031.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3031.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3031.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3031.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3031.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3031_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3031_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3031_latest.md?ref=main

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
- open: 31.65
- high: 33.15
- low: 31
- close: 31.3
- volume: 4864784
- ma5: 32.14
- ema23_primary: 30.69
- distance_to_ema23_pct: 1.98
- ma20: 30.76
- ma60: 27.16
- ma120: 23.52
- return_5d: -6.85
- return_20d: -4.57
- volume_ratio: 1.23
- distance_to_ma20_pct_auxiliary: 1.76
- distance_to_high_60_pct: -11.33

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,32.5,33.25,31.1,31.55,5958933,29.38,7.39,29.73,23.82,0.57
20260504,32,32,30.75,31.55,3005546,29.56,6.74,30.16,24.01,0.29
20260505,31.45,32.4,31.35,31.4,2810346,29.71,5.68,30.56,24.19,0.27
20260506,31.75,32.3,30.4,30.5,3954215,29.78,2.42,30.94,24.35,0.37
20260507,30.9,31.15,30.4,30.55,1782289,29.84,2.37,31.28,24.51,0.17
20260508,30.4,31,29.15,29.55,2199161,29.82,-0.9,31.47,24.66,0.21
20260511,30,31.15,29.55,30,2498345,29.83,0.56,31.55,24.83,0.26
20260512,30.2,30.3,29.2,29.85,1849391,29.83,0.05,31.49,25,0.22
20260513,29.45,29.95,28.7,29.3,2255617,29.79,-1.64,31.4,25.16,0.32
20260514,29.65,30.3,29.6,30,1597357,29.81,0.65,31.28,25.32,0.26
20260515,30.25,30.55,28.85,28.95,2128860,29.74,-2.64,31.08,25.47,0.37
20260518,28.3,28.6,27.25,28.55,1557925,29.64,-3.67,30.84,25.61,0.29
20260519,28.7,29.3,28.4,28.6,918497,29.55,-3.22,30.74,25.76,0.18
20260520,29.2,30.9,28.5,30.55,3517200,29.63,3.09,30.68,25.94,0.75
20260521,31.25,33.6,30.55,33.6,15829043,29.96,12.13,30.76,26.17,3.06
20260522,34.75,34.8,33.2,33.75,10695490,30.28,11.46,30.96,26.39,1.96
20260525,34,34.4,32.85,32.85,6364027,30.49,7.73,31.04,26.6,1.17
20260526,32.95,33,31.4,31.85,3058086,30.61,4.06,30.98,26.8,0.61
20260527,32,32.35,30.7,30.95,2554703,30.64,1.03,30.84,26.98,0.58
20260528,31.65,33.15,31,31.3,4864784,30.69,1.98,30.76,27.16,1.23
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 60.01
- over_600_ratio: 59.18
- over_800_ratio: 59.18
- over_1000_ratio: 58.15
- over_400_change_1w: 0.67
- over_800_change_1w: 0.51
- over_1000_change_1w: 0.49
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.83,,58.31,,56.19,,0,False,False
20260508,58.87,0.04,58.29,-0.02,56.18,-0.01,1,False,False
20260515,59.34,0.47,58.67,0.38,57.66,1.48,2,True,True
20260522,60.01,0.67,59.18,0.51,58.15,0.49,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3031 | 佰鴻 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3031 | 佰鴻 | 3 | 3 | 4 | 5 | 5 | continued_2_3d | 連續 3 個交易日上榜，訊號延續但仍需確認。 |

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
