# INDIVIDUAL STOCK CHATGPT PACKET - 7822 倍利科

## Metadata
- generated_at: 2026-05-26 02:30:49 Asia/Taipei
- stock_id: 7822
- stock_name: 倍利科
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 41
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7822_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7822_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7822_packet_latest.md?ref=main
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
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 1030
- high: 1100
- low: 1030
- close: 1070
- volume: 250725
- ma5: 1091
- ma20: 1192.25
- ma60: 1373.66
- ma120: 1373.66
- ema23: 1210.96
- return_5d: 1.42
- return_20d: -18.63
- volume_ratio: 0.79
- distance_to_ma20_pct: -10.25
- distance_to_high_60_pct: -42.93

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260330,1480,1755,1475,1695,1447908,,,,,,,,,,,
20260331,1675,1675,1470,1510,881544,,,,,,-10.91,,,,,
20260401,1590,1620,1470,1545,696319,,,,,,2.32,,,,,
20260402,1555,1700,1520,1615,1071121,,,,,,4.53,,,,,
20260407,1665,1790,1560,1740,1169881,1621,1621,1621,1621,1670.26,7.74,,,1.11,7.34,-2.79
20260408,1745,1875,1700,1825,1091208,1647,1655,1655,1655,1683.16,4.89,7.67,,1.03,10.27,-2.67
20260409,1750,1780,1685,1700,932072,1685,1661.43,1661.43,1661.43,1684.56,-6.85,12.58,,0.9,2.32,-9.33
20260410,1700,1730,1660,1685,515194,1713,1664.38,1664.38,1664.38,1684.6,-0.88,9.06,,0.53,1.24,-10.13
20260413,1615,1655,1540,1555,837554,1701,1652.22,1652.22,1652.22,1673.8,-7.72,-3.72,,0.87,-5.88,-17.07
20260414,1555,1600,1500,1555,614861,1664,1642.5,1642.5,1642.5,1663.9,0,-10.63,,0.66,-5.33,-17.07
20260415,1590,1710,1555,1710,861492,1641,1648.64,1648.64,1648.64,1667.74,9.97,-6.3,,0.94,3.72,-8.8
20260416,1745,1780,1625,1645,778141,1630,1648.33,1648.33,1648.33,1665.84,-3.8,-3.24,,0.86,-0.2,-12.27
20260417,1605,1635,1565,1575,560294,1608,1642.69,1642.69,1642.69,1658.27,-4.26,-6.53,,0.64,-4.12,-16
20260420,1580,1630,1535,1580,543845,1613,1638.21,1638.21,1638.21,1651.75,0.32,1.61,,0.63,-3.55,-15.73
20260421,1615,1615,1550,1550,379974,1612,1632.33,1632.33,1632.33,1643.27,-1.9,-0.32,,0.46,-5.04,-17.33
20260422,1555,1555,1440,1440,1056890,1558,1620.31,1620.31,1620.31,1626.33,-7.1,-15.79,,1.26,-11.13,-23.2
20260423,1470,1470,1300,1340,914691,1497,1603.82,1603.82,1603.82,1602.47,-6.94,-18.54,,1.08,-16.45,-28.53
20260424,1375,1395,1250,1305,480211,1443,1587.22,1587.22,1587.22,1577.68,-2.61,-17.14,,0.58,-17.78,-30.4
20260427,1305,1305,1185,1235,479270,1374,1568.68,1568.68,1568.68,1549.12,-5.36,-21.84,,0.59,-21.27,-34.13
20260428,1260,1355,1240,1355,297164,1335,1558,1558,1558,1532.95,9.72,-12.58,,0.38,-13.03,-27.73
20260429,1355,1365,1300,1315,304065,1310,1539,1546.43,1546.43,1514.79,-2.95,-8.68,-22.42,0.42,-14.55,-29.87
20260430,1315,1340,1270,1295,306322,1301,1528.25,1535,1535,1496.47,-1.52,-3.36,-14.24,0.44,-15.26,-30.93
20260504,1315,1420,1270,1390,538570,1318,1520.5,1528.7,1528.7,1487.6,7.34,6.51,-10.03,0.78,-8.58,-25.87
20260505,1410,1450,1355,1410,320005,1353,1510.25,1523.75,1523.75,1481.13,1.44,14.17,-12.69,0.49,-6.64,-24.8
20260506,1425,1425,1320,1330,327182,1348,1489.75,1516,1516,1468.54,-5.67,-1.84,-23.56,0.54,-10.72,-29.07
20260507,1320,1335,1275,1300,254555,1345,1463.5,1507.69,1507.69,1454.49,-2.26,-1.14,-28.77,0.45,-11.17,-30.67
20260508,1300,1300,1250,1260,242256,1338,1441.5,1498.52,1498.52,1438.28,-3.08,-2.7,-25.88,0.46,-12.59,-32.8
20260511,1280,1305,1275,1295,178924,1319,1422,1491.25,1491.25,1426.34,2.78,-6.83,-23.15,0.35,-8.93,-30.93
20260512,1310,1330,1250,1270,269490,1291,1407.75,1483.62,1483.62,1413.32,-1.93,-9.93,-18.33,0.56,-9.79,-32.27
20260513,1275,1275,1180,1205,402088,1266,1390.25,1474.33,1474.33,1395.96,-5.12,-9.4,-22.51,0.85,-13.32,-35.73
20260514,1200,1210,1130,1140,618094,1234,1361.75,1463.55,1463.55,1374.63,-5.39,-12.31,-33.33,1.34,-16.28,-39.2
20260515,1145,1180,1125,1155,307915,1213,1337.25,1453.91,1453.91,1356.32,1.32,-8.33,-29.79,0.7,-13.63,-38.4
20260518,1150,1185,1100,1170,249379,1188,1317,1445.3,1445.3,1340.8,1.3,-9.65,-25.71,0.59,-11.16,-37.6
20260519,1130,1135,1055,1075,463604,1149,1291.75,1434.41,1434.41,1318.65,-8.12,-15.35,-31.96,1.1,-16.78,-42.67
20260520,1080,1080,1025,1040,219215,1116,1266.25,1423.14,1423.14,1295.43,-3.26,-13.69,-32.9,0.53,-17.87,-44.53
20260521,1065,1090,1050,1055,182677,1099,1247,1412.92,1412.92,1275.39,1.44,-7.46,-26.74,0.5,-15.4,-43.73
20260522,1030,1100,1030,1070,250725,1082,1233.5,1403.65,1403.65,1258.28,1.42,-7.36,-20.15,0.75,-13.26,-42.93
20260523,1030,1100,1030,1070,250725,1062,1221.75,1394.87,1394.87,1242.59,0,-8.55,-18.01,0.78,-12.42,-42.93
20260524,1030,1100,1030,1070,250725,1061,1213.5,1386.54,1386.54,1228.2,0,-0.47,-13.36,0.8,-11.83,-42.93
20260525,1100,1175,1100,1175,445123,1088,1204.5,1381.25,1381.25,1223.77,9.81,12.98,-13.28,1.4,-2.45,-37.33
20260526,1030,1100,1030,1070,250725,1091,1192.25,1373.66,1373.66,1210.96,-8.94,1.42,-18.63,0.79,-10.25,-42.93
```

## Latest TDCC Snapshot
- as_of_date: 20260522
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

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,68.26,,68.26,,65.6,,63.73,,0,False,False,False,,
20260508,68.26,0,68.26,0,65.6,0,63.73,0,0,False,False,False,,
20260515,68.25,-0.01,68.25,-0.01,65.6,0,63.73,0,0,False,False,False,,
20260522,68.25,0,68.25,0,65.6,0,63.73,0,0,False,False,False,,
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
