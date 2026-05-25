# INDIVIDUAL STOCK CHATGPT PACKET - 7828 創新服務

## Metadata
- generated_at: 2026-05-26 02:30:49 Asia/Taipei
- stock_id: 7828
- stock_name: 創新服務
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 26
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7828_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7828_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7828_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7828.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7828.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7828.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7828.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7828.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7828.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7828_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7828_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7828_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 1225
- high: 1280
- low: 1195
- close: 1280
- volume: 1251
- ma5: 1211
- ma20: 1208.25
- ma60: 1232.31
- ma120: 1232.31
- ema23: 1243.93
- return_5d: 20.75
- return_20d: 0.39
- volume_ratio: 0.01
- distance_to_ma20_pct: 5.94
- distance_to_high_60_pct: -22.89

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260422,1535,1660,1520,1560,1188000,,,,,,,,,,,
20260423,1560,1590,1310,1380,1052000,,,,,,-11.54,,,,,
20260424,1385,1385,1240,1260,825000,,,,,,-8.7,,,,,
20260427,1260,1305,1155,1200,627000,,,,,,-4.76,,,,,
20260428,1210,1280,1180,1200,439000,1320,1320,1320,1320,1469.94,0,,,0.53,-9.09,-27.71
20260429,1175,1290,1090,1275,713000,1263,1312.5,1312.5,1312.5,1453.69,6.25,-18.27,,0.88,-2.86,-23.19
20260430,1245,1275,1180,1230,422000,1233,1300.71,1300.71,1300.71,1435.05,-3.53,-10.87,,0.56,-5.44,-25.9
20260504,1245,1340,1205,1325,363000,1246,1303.75,1303.75,1303.75,1425.88,7.72,5.16,,0.52,1.63,-20.18
20260505,1295,1320,1260,1275,284000,1261,1300.56,1300.56,1300.56,1413.31,-3.77,6.25,,0.43,-1.97,-23.19
20260506,1275,1280,1200,1230,335000,1267,1293.5,1293.5,1293.5,1398.03,-3.53,2.5,,0.54,-4.91,-25.9
20260507,1245,1275,1185,1190,225000,1250,1284.09,1284.09,1284.09,1380.7,-3.25,-6.67,,0.38,-7.33,-28.31
20260508,1170,1205,1075,1115,479000,1227,1270,1270,1270,1358.56,-6.3,-9.35,,0.83,-12.2,-32.83
20260511,1205,1225,1205,1225,115000,1207,1266.54,1266.54,1266.54,1347.43,9.87,-7.55,,0.21,-3.28,-26.2
20260512,1315,1345,1295,1345,697000,1221,1272.14,1272.14,1272.14,1347.22,9.8,5.49,,1.26,5.73,-18.98
20260513,1230,1315,1230,1295,330000,1234,1273.67,1273.67,1273.67,1342.87,-3.72,5.28,,0.61,1.68,-21.99
20260514,1310,1320,1255,1275,289000,1251,1273.75,1273.75,1273.75,1337.22,-1.54,7.14,,0.55,0.1,-23.19
20260515,1300,1305,1180,1195,228000,1267,1269.12,1269.12,1269.12,1325.36,-6.27,7.17,,0.45,-5.84,-28.01
20260518,1130,1200,1120,1185,150000,1259,1264.44,1264.44,1264.44,1313.67,-0.84,-3.27,,0.31,-6.28,-28.61
20260519,1185,1185,1100,1100,222000,1210,1255.79,1255.79,1255.79,1295.86,-7.17,-18.22,,0.47,-12.41,-33.73
20260520,1070,1095,990,1065,461000,1164,1246.25,1246.25,1246.25,1276.62,-3.18,-17.76,,0.98,-14.54,-35.84
20260521,1075,1095,1050,1060,213000,1121,1221.25,1237.38,1237.38,1258.57,-0.47,-16.86,-32.05,0.5,-13.2,-36.14
20260522,1105,1165,1105,1165,1159,1115,1210.5,1234.09,1234.09,1250.77,9.91,-2.51,-15.58,0,-3.76,-29.82
20260523,1105,1165,1105,1165,1159,1111,1205.75,1231.09,1231.09,1243.63,0,-1.69,-7.54,0,-3.38,-29.82
20260524,1105,1165,1105,1165,1159,1124,1204,1228.33,1228.33,1237.07,0,5.91,-2.92,0,-3.24,-29.82
20260525,1225,1280,1195,1280,1251,1167,1208,1230.4,1230.4,1240.65,9.87,20.19,6.67,0,5.96,-22.89
20260526,1225,1280,1195,1280,1251,1211,1208.25,1232.31,1232.31,1243.93,0,20.75,0.39,0.01,5.94,-22.89
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 62.48
- over_600_ratio: 59.04
- over_800_ratio: 55.95
- over_1000_ratio: 53.85
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,62.54,,59.1,,56.01,,53.85,,0,False,False,False,,
20260508,62.52,-0.02,59.08,-0.02,55.99,-0.02,53.85,0,0,False,False,False,,
20260515,62.48,-0.04,59.04,-0.04,55.95,-0.04,53.85,0,0,False,False,False,,
20260522,62.48,0,59.04,0,55.95,0,53.85,0,0,False,False,False,,
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
