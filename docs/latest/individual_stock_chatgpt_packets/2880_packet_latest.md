# INDIVIDUAL STOCK CHATGPT PACKET - 2880 華南金

## Metadata
- generated_at: 2026-05-28 19:32:08 Asia/Taipei
- stock_id: 2880
- stock_name: 華南金
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2880_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2880_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2880_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2880_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2880_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2880_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2880_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2880_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2880_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2880_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2880_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2880_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2880_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2880_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2880_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2880_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2880_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2880_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2880.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2880.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2880.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2880.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2880.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2880.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2880_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2880_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2880_latest.md?ref=main

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
- open: 30.1
- high: 30.3
- low: 29.6
- close: 29.6
- volume: 96181130
- ma5: 30.44
- ema23_primary: 32.07
- distance_to_ema23_pct: -7.69
- ma20: 32
- ma60: 33.55
- ma120: 32.96
- return_5d: -7.64
- return_20d: -10.03
- volume_ratio: 2.87
- distance_to_ma20_pct_auxiliary: -7.49
- distance_to_high_60_pct: -19.57

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,32.7,32.9,32.05,32.05,29661385,34.31,-6.59,34.56,34.33,1.52
20260504,31.8,32.3,31.8,32.05,28476672,34.12,-6.08,34.48,34.31,1.41
20260505,32.3,32.85,32.2,32.65,10848723,34,-3.97,34.42,34.3,0.54
20260506,32.95,33,32.65,32.7,17806705,33.89,-3.52,34.35,34.3,0.88
20260507,32.9,33.7,32.9,33.3,25270265,33.84,-1.6,34.32,34.29,1.21
20260508,33.8,33.8,32.95,33.3,19776951,33.8,-1.47,34.26,34.29,0.94
20260511,33.4,33.45,33.15,33.25,13827593,33.75,-1.49,34.22,34.29,0.65
20260512,33.5,33.5,32.55,32.55,22674751,33.65,-3.27,34.14,34.28,1.04
20260513,32.55,32.95,32.5,32.75,11743640,33.58,-2.46,34.03,34.28,0.55
20260514,32.45,33.25,32.45,32.6,13664690,33.5,-2.67,33.86,34.27,0.65
20260515,32.9,33.15,32.4,32.4,13394492,33.4,-3.01,33.68,34.25,0.65
20260518,32.65,32.65,31.85,31.85,21630660,33.27,-4.28,33.47,34.22,1.03
20260519,32.1,33.15,32,32.2,26823110,33.18,-2.97,33.28,34.19,1.27
20260520,32.2,32.6,31.95,32.05,31589810,33.09,-3.14,33.12,34.15,1.45
20260521,32.5,32.5,31.95,32.05,30912031,33,-2.89,32.96,34.11,1.39
20260522,32,32.4,31.6,31.95,32193459,32.92,-2.93,32.8,34.03,1.42
20260525,32,32,30.55,30.55,66355162,32.72,-6.63,32.57,33.92,2.63
20260526,30.85,31.45,30.15,30.15,79395720,32.5,-7.24,32.32,33.8,2.81
20260527,30.35,30.55,29.95,29.95,78460919,32.29,-7.25,32.16,33.66,2.6
20260528,30.1,30.3,29.6,29.6,96181130,32.07,-7.69,32,33.55,2.87
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 80.81
- over_600_ratio: 79.67
- over_800_ratio: 79.03
- over_1000_ratio: 78.37
- over_400_change_1w: -0.03
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.95,,79.12,,78.44,,0,False,False
20260508,80.86,-0.09,79.03,-0.09,78.36,-0.08,0,False,False
20260515,80.84,-0.02,79.02,-0.01,78.36,0,0,False,False
20260522,80.81,-0.03,79.03,0.01,78.37,0.01,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2880 | 華南金 | revenue_pullback | 營收成長股價回檔 | 57.0 |  |  |  |  | no_signal | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2880 | 華南金 | 6 | 6 | 5 | 6 | 6 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2880 | 華南金 | 3 | 0 | 206370.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
