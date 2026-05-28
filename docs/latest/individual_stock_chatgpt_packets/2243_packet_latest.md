# INDIVIDUAL STOCK CHATGPT PACKET - 2243 宏旭-KY

## Metadata
- generated_at: 2026-05-28 19:31:48 Asia/Taipei
- stock_id: 2243
- stock_name: 宏旭-KY
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2243_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2243_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2243_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2243_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2243_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2243_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2243_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2243_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2243_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2243_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2243_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2243_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2243_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2243_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2243_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2243_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2243_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2243_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2243.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2243.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2243.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2243.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2243.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2243.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2243_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2243_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2243_latest.md?ref=main

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
- open: 24.05
- high: 25.95
- low: 24.05
- close: 24.85
- volume: 1550575
- ma5: 23.68
- ema23_primary: 23.05
- distance_to_ema23_pct: 7.81
- ma20: 23.35
- ma60: 21.11
- ma120: 16.3
- return_5d: 12.95
- return_20d: -11.88
- volume_ratio: 1.21
- distance_to_ma20_pct_auxiliary: 6.44
- distance_to_high_60_pct: -13.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,28.5,28.8,27.05,27.25,2172650,23.23,17.29,23.47,17.48,1.24
20260504,28.5,28.55,24.55,24.75,4059440,23.36,5.96,23.61,17.71,2.13
20260505,24.75,26.4,24.7,26,1686101,23.58,10.27,23.91,17.95,0.89
20260506,26.1,26.55,25.3,26.4,930278,23.81,10.86,24.18,18.2,0.5
20260507,26.5,26.95,25.7,26.4,1167660,24.03,9.86,24.48,18.45,0.62
20260508,23.8,23.8,23.8,23.8,2037725,24.01,-0.88,24.53,18.65,1.08
20260511,23.2,23.2,21.45,21.65,3155492,23.81,-9.09,24.49,18.82,1.75
20260512,21.65,22.8,21.05,22.2,1438943,23.68,-6.25,24.45,19,0.79
20260513,22.7,22.7,21.7,21.7,615974,23.51,-7.72,24.39,19.18,0.35
20260514,21.95,21.95,21,21,728154,23.3,-9.89,24.29,19.33,0.41
20260515,21.4,21.75,20.9,21.2,526636,23.13,-8.34,24.19,19.49,0.3
20260518,21.3,22.65,20.95,21.7,876240,23.01,-5.69,24.09,19.66,0.51
20260519,21.85,22.35,21.5,21.6,532571,22.89,-5.65,24.07,19.83,0.31
20260520,21.55,21.95,20.9,20.9,600912,22.73,-8.04,23.95,19.98,0.36
20260521,21.65,22,20.95,22,900681,22.67,-2.94,23.87,20.15,0.54
20260522,22.45,22.95,22.2,22.8,627322,22.68,0.54,23.81,20.33,0.38
20260525,22.8,23.5,22.15,23.5,954090,22.75,3.32,23.77,20.52,0.6
20260526,23.55,24,23,23.5,610555,22.81,3.03,23.7,20.71,0.4
20260527,23.9,24.2,23.5,23.75,493649,22.89,3.77,23.52,20.9,0.35
20260528,24.05,25.95,24.05,24.85,1550575,23.05,7.81,23.35,21.11,1.21
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.04
- over_600_ratio: 47.24
- over_800_ratio: 41.42
- over_1000_ratio: 38.81
- over_400_change_1w: -0.63
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.98,,41.7,,38.88,,0,False,False
20260508,54.76,-0.22,40.12,-1.58,38.69,-0.19,0,False,False
20260515,54.67,-0.09,41.39,1.27,38.78,0.09,1,False,True
20260522,54.04,-0.63,41.42,0.03,38.81,0.03,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2243 | 宏旭-KY | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2243 | 宏旭-KY | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。 |

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
