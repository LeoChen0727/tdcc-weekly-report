# INDIVIDUAL STOCK CHATGPT PACKET - 7822 倍利科

## Metadata
- generated_at: 2026-05-30 23:43:46 Asia/Taipei
- stock_id: 7822
- stock_name: 倍利科
- packet_status: partial_rawdata_packet
- latest_price_date: 20260529
- price_rows: 42
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7822_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7822_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7822_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7822_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7822_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7822_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7822_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7822_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7822_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7822_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7822_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7822_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7822_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7822_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7822_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7822_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7822_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7822_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7822.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7822.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7822.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7822.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7822.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7822.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7822_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7822_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7822_latest.md?ref=main

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
- date: 20260529
- open: 1120
- high: 1130
- low: 1055
- close: 1075
- volume: 410001
- ma5: 1138
- ema23_primary: 1214.2
- distance_to_ema23_pct: -11.46
- ma20: 1192.75
- ma60: 1372.02
- ma120: 1372.02
- return_5d: 0.47
- return_20d: -16.99
- volume_ratio: 1.18
- distance_to_ma20_pct_auxiliary: -9.87
- distance_to_high_60_pct: -42.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,1315,1420,1270,1390,538570,1487.6,-6.56,1520.5,1528.7,0.78
20260505,1410,1450,1355,1410,320005,1481.13,-4.8,1510.25,1523.75,0.49
20260506,1425,1425,1320,1330,327182,1468.54,-9.43,1489.75,1516,0.54
20260507,1320,1335,1275,1300,254555,1454.49,-10.62,1463.5,1507.69,0.45
20260508,1300,1300,1250,1260,242256,1438.28,-12.4,1441.5,1498.52,0.46
20260511,1280,1305,1275,1295,178924,1426.34,-9.21,1422,1491.25,0.35
20260512,1310,1330,1250,1270,269490,1413.32,-10.14,1407.75,1483.62,0.56
20260513,1275,1275,1180,1205,402088,1395.96,-13.68,1390.25,1474.33,0.85
20260514,1200,1210,1130,1140,618094,1374.63,-17.07,1361.75,1463.55,1.34
20260515,1145,1180,1125,1155,307915,1356.32,-14.84,1337.25,1453.91,0.7
20260518,1150,1185,1100,1170,249379,1340.8,-12.74,1317,1445.3,0.59
20260519,1130,1135,1055,1075,463604,1318.65,-18.48,1291.75,1434.41,1.1
20260520,1080,1080,1025,1040,219215,1295.43,-19.72,1266.25,1423.14,0.53
20260521,1065,1090,1050,1055,182677,1275.39,-17.28,1247,1412.92,0.5
20260522,1030,1100,1030,1070,250725,1258.28,-14.96,1233.5,1403.65,0.75
20260525,1100,1175,1100,1175,445123,1251.34,-6.1,1227,1397.63,1.34
20260526,1165,1200,1110,1180,463758,1245.39,-5.25,1224.25,1392.05,1.4
20260527,1180,1180,1125,1145,459778,1237.03,-7.44,1213.75,1385.88,1.35
20260528,1145,1245,1110,1115,342416,1226.86,-9.12,1203.75,1379.27,1
20260529,1120,1130,1055,1075,410001,1214.2,-11.46,1192.75,1372.02,1.18
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 68.25
- over_600_ratio: 68.25
- over_800_ratio: 65.6
- over_1000_ratio: 63.73
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.26,,65.6,,63.73,,0,False,False
20260508,68.26,0,65.6,0,63.73,0,0,False,False
20260515,68.25,-0.01,65.6,0,63.73,0,0,False,False
20260522,68.25,0,65.6,0,63.73,0,0,False,False
20260529,68.25,0,65.6,0,63.73,0,0,False,False
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
