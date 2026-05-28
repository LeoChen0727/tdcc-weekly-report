# INDIVIDUAL STOCK CHATGPT PACKET - 3324 雙鴻

## Metadata
- generated_at: 2026-05-28 19:32:23 Asia/Taipei
- stock_id: 3324
- stock_name: 雙鴻
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3324_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3324_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3324_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3324_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3324_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3324_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3324_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3324_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3324_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3324_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3324_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3324_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3324_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3324_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3324_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3324_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3324_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3324_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3324.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3324.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3324.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3324.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3324.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3324.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3324_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3324_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3324_latest.md?ref=main

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
- open: 1050
- high: 1070
- low: 1000
- close: 1005
- volume: 3211817
- ma5: 1020
- ema23_primary: 1033.28
- distance_to_ema23_pct: -2.74
- ma20: 1046.6
- ma60: 1029.42
- ma120: 997.36
- return_5d: 0.5
- return_20d: -13.36
- volume_ratio: 1.14
- distance_to_ma20_pct_auxiliary: -3.97
- distance_to_high_60_pct: -22.99

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,1160,1175,1130,1140,2903000,1070.59,6.48,1043.95,1021.38,0.54
20260504,1160,1200,1125,1190,4138000,1080.54,10.13,1057.45,1025.72,0.76
20260505,1200,1210,1145,1170,3161000,1087.99,7.54,1070.45,1029.68,0.58
20260506,1190,1190,1055,1105,5880000,1089.41,1.43,1079.8,1032.67,1.05
20260507,1140,1140,1050,1070,4430000,1087.79,-1.64,1083.05,1035.02,0.8
20260508,1070,1105,1035,1065,3939000,1085.89,-1.92,1086.85,1037.1,0.71
20260511,1070,1090,1055,1070,3199000,1084.57,-1.34,1090.85,1039.77,0.58
20260512,1080,1085,1055,1060,2651000,1082.52,-2.08,1096.85,1041.8,0.5
20260513,1055,1065,1040,1065,1805000,1081.06,-1.49,1101.85,1042.8,0.35
20260514,1085,1095,1015,1015,3906000,1075.56,-5.63,1104,1042.8,0.75
20260515,1040,1050,990,995,2499000,1068.84,-6.91,1101.5,1042.72,0.51
20260518,980,994,941,982,2634000,1061.61,-7.5,1098.85,1041.92,0.55
20260519,986,986,964,966,2412000,1053.64,-8.32,1095.15,1039.6,0.51
20260520,970,972,936,939,2741000,1044.09,-10.06,1089.6,1037.25,0.59
20260521,964,1015,957,1000,2494000,1040.41,-3.88,1081.85,1036.17,0.58
20260522,1035,1040,1005,1010,1023000,1037.88,-2.69,1077.1,1036.08,0.27
20260525,1035,1040,1010,1010,1022000,1035.56,-2.47,1066.85,1035.42,0.3
20260526,1030,1045,1010,1040,1032000,1035.93,0.39,1059.85,1033.5,0.35
20260527,1070,1080,1025,1035,1050000,1035.85,-0.08,1054.35,1031.5,0.38
20260528,1050,1070,1000,1005,3211817,1033.28,-2.74,1046.6,1029.42,1.14
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 46.7
- over_600_ratio: 42.31
- over_800_ratio: 36.36
- over_1000_ratio: 29.4
- over_400_change_1w: -2.15
- over_800_change_1w: -0.99
- over_1000_change_1w: -1.87
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,51.66,,39.53,,35.53,,0,False,False
20260508,49.63,-2.03,39.21,-0.32,33.17,-2.36,0,False,False
20260515,48.85,-0.78,37.35,-1.86,31.27,-1.9,1,False,False
20260522,46.7,-2.15,36.36,-0.99,29.4,-1.87,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3324 | 雙鴻 | revenue_pullback | 營收成長股價回檔 | 74.0 |  |  |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260521 | 3324 | 雙鴻 | pattern | 型態觀察 |  |  |  | 預備發動型 |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3324 | 雙鴻 | 6 | 6 | 5 | 6 | 6 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

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
