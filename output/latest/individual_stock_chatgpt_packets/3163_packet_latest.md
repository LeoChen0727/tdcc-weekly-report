# INDIVIDUAL STOCK CHATGPT PACKET - 3163 波若威

## Metadata
- generated_at: 2026-05-27 21:26:59 Asia/Taipei
- stock_id: 3163
- stock_name: 波若威
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3163_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3163_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3163_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3163_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3163_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3163_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3163_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3163_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3163_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3163_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3163_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3163_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3163_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3163_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3163_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3163_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3163_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3163_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3163.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3163.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3163.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3163.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3163.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3163.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3163_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3163_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3163_latest.md?ref=main

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
- date: 20260527
- open: 1225
- high: 1230
- low: 1100
- close: 1100
- volume: 1151000
- ma5: 1144
- ema23_primary: 1074.63
- distance_to_ema23_pct: 2.36
- ma20: 1073.85
- ma60: 1002.62
- ma120: 704.83
- return_5d: 15.55
- return_20d: 2.8
- volume_ratio: 0.59
- distance_to_ma20_pct_auxiliary: 2.44
- distance_to_high_60_pct: -16.35

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,1015,1070,1010,1045,3192000,1075.2,-2.81,1122.55,827.2,0.95
20260430,1145,1145,1125,1145,3316000,1081.02,5.92,1140.4,840.08,0.95
20260504,1255,1255,1190,1255,4996000,1095.52,14.56,1159.85,854.63,1.39
20260505,1260,1300,1205,1220,7597000,1105.89,10.32,1173.25,868.53,2.06
20260506,1220,1225,1100,1135,5976000,1108.32,2.41,1177.75,880.38,1.74
20260507,1075,1100,1070,1085,1185000,1106.38,-1.93,1174.75,890.68,0.35
20260508,1035,1050,1000,1010,1248000,1098.34,-8.04,1164.25,899.64,0.42
20260511,1030,1050,1000,1040,697000,1093.48,-4.89,1153.25,909.38,0.24
20260512,1100,1130,1065,1065,482000,1091.11,-2.39,1146.5,919.96,0.16
20260513,1020,1055,1010,1035,418000,1086.43,-4.73,1138.25,929.58,0.14
20260514,1075,1075,1020,1020,368000,1080.9,-5.63,1128.75,938.42,0.13
20260515,1020,1020,950,950,716000,1069.99,-11.21,1119.5,946.38,0.25
20260518,902,931,865,900,957000,1055.82,-14.76,1103.25,953.23,0.33
20260519,897,930,897,900,378000,1042.84,-13.7,1083.5,959.28,0.13
20260520,904,990,904,952,587000,1035.27,-8.04,1068.1,965.7,0.2
20260521,995,1045,974,1045,2511000,1036.08,0.86,1061.35,973.3,0.85
20260522,1135,1145,1080,1145,1123000,1045.16,9.55,1060.6,981.6,0.38
20260525,1245,1255,1145,1210,1206000,1058.89,14.27,1063.35,989.92,0.49
20260526,1215,1250,1150,1220,1206000,1072.32,13.77,1072.35,997.22,0.52
20260527,1225,1230,1100,1100,1151000,1074.63,2.36,1073.85,1002.62,0.59
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 40.97
- over_600_ratio: 32.55
- over_800_ratio: 29.26
- over_1000_ratio: 23.46
- over_400_change_1w: 0.86
- over_800_change_1w: 0.04
- over_1000_change_1w: 1.4
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.11,,26.75,,23.29,,0,False,False
20260508,40.49,-1.62,27.33,0.58,22.57,-0.72,1,False,True
20260515,40.11,-0.38,29.22,1.89,22.06,-0.51,2,False,True
20260522,40.97,0.86,29.26,0.04,23.46,1.4,3,True,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| status |
| --- |
| no rows |

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
