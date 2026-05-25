# INDIVIDUAL STOCK CHATGPT PACKET - 7823 奧義賽博-KY創

## Metadata
- generated_at: 2026-05-26 02:30:49 Asia/Taipei
- stock_id: 7823
- stock_name: 奧義賽博-KY創
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 70
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7823_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7823_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7823_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7823.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7823.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7823.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7823.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7823.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7823.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7823_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7823_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7823_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 109
- high: 109
- low: 100
- close: 107
- volume: 107216
- ma5: 106
- ma20: 97.32
- ma60: 86.88
- ma120: 89.69
- ema23: 97.36
- return_5d: -1.83
- return_20d: 32.26
- volume_ratio: 1.18
- distance_to_ma20_pct: 9.95
- distance_to_high_60_pct: -3.6

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260205,165,165,146,148,823224,,,,,,,,,,,
20260206,150,150,110,131,619706,,,,,,-11.49,,,,,
20260209,128.5,128.5,110,113.5,362621,,,,,,-13.36,,,,,
20260210,113.5,113.5,106.5,109.5,264079,,,,,,-3.52,,,,,
20260211,109,110,101,104.5,248480,121.3,121.3,121.3,121.3,137.93,-4.57,,,0.54,-13.85,-36.67
20260223,102,107,95,97,271867,111.1,117.25,117.25,117.25,134.52,-7.18,-34.46,,0.63,-17.27,-41.21
20260224,95.2,95.2,90.1,90.2,234744,102.94,113.39,113.39,113.39,130.82,-7.01,-31.14,,0.58,-20.45,-45.33
20260225,93.4,93.4,88,89.5,145002,98.14,110.4,110.4,110.4,127.38,-0.78,-21.15,,0.39,-18.93,-45.76
20260226,89.5,91.6,88.9,90.9,121088,94.42,108.23,108.23,108.23,124.34,1.56,-16.99,,0.35,-16.01,-44.91
20260302,89.4,92.1,88.9,91.8,79884,91.88,106.59,106.59,106.59,121.63,0.99,-12.15,,0.25,-13.88,-44.36
20260303,92.6,92.6,89.5,90.3,51856,90.54,105.11,105.11,105.11,119.02,-1.63,-6.91,,0.18,-14.09,-45.27
20260304,89,89,88.2,88.8,50560,90.26,103.75,103.75,103.75,116.5,-1.66,-1.55,,0.19,-14.41,-46.18
20260305,88.8,90,88.8,89.8,29042,90.32,102.68,102.68,102.68,114.27,1.13,0.34,,0.11,-12.54,-45.58
20260306,88.8,89,81.2,86,72310,89.34,101.49,101.49,101.49,111.92,-4.23,-5.39,,0.3,-15.26,-47.88
20260309,80.3,84.4,77.7,82.5,73104,87.48,100.22,100.22,100.22,109.47,-4.07,-10.13,,0.32,-17.68,-50
20260310,84.9,86.7,82.2,84.4,31712,86.3,99.23,99.23,99.23,107.38,2.3,-6.53,,0.15,-14.95,-48.85
20260311,84,84,82.5,82.8,21874,85.1,98.26,98.26,98.26,105.33,-1.9,-6.76,,0.11,-15.74,-49.82
20260312,80.5,82.6,80.5,82.6,17779,83.66,97.39,97.39,97.39,103.44,-0.24,-8.02,,0.09,-15.19,-49.94
20260313,82.6,82.6,80.8,82,17844,82.86,96.58,96.58,96.58,101.65,-0.73,-4.65,,0.1,-15.1,-50.3
20260316,82,82,76,78.5,96197,82.06,95.68,95.68,95.68,99.72,-4.27,-4.85,,0.53,-17.96,-52.42
20260317,78.9,85.5,78.9,83,92442,81.78,92.43,95.08,95.08,98.33,5.73,-1.66,-43.92,0.64,-10.2,-49.7
20260318,83,83.5,81.9,82.6,31190,81.74,90.01,94.51,94.51,97.02,-0.48,-0.24,-36.95,0.27,-8.23,-49.94
20260319,80.2,81.1,79.5,81,25573,81.42,88.39,93.92,93.92,95.68,-1.94,-1.94,-28.63,0.26,-8.36,-50.91
20260320,80.2,81,80,81,16689,81.22,86.96,93.38,93.38,94.46,0,-1.22,-26.03,0.19,-6.85,-50.91
20260323,81,82,80.5,80.7,20182,81.66,85.77,92.88,92.88,93.31,-0.37,2.8,-22.78,0.27,-5.91,-51.09
20260324,80.5,81.3,80.5,81.3,3140,81.32,84.98,92.43,92.43,92.31,0.74,-2.05,-16.19,0.05,-4.34,-50.73
20260325,81.2,86.5,81.2,85.8,23131,81.96,84.77,92.19,92.19,91.77,5.54,3.87,-4.88,0.45,1.22,-48
20260326,85.5,85.5,82,82.5,28060,82.26,84.42,91.84,91.84,91,-3.85,1.85,-7.82,0.62,-2.27,-50
20260327,82.2,83,82.2,83,5522,82.66,84.02,91.53,91.53,90.33,0.61,2.47,-8.69,0.14,-1.21,-49.7
20260330,82.8,82.8,80.6,81.5,6370,82.82,83.5,91.2,91.2,89.59,-1.81,0.99,-11.22,0.18,-2.4,-50.61
20260331,80.3,81,80,81,13614,82.76,83.04,90.87,90.87,88.88,-0.61,-0.37,-10.3,0.4,-2.46,-50.91
20260401,81,82.7,81,82.2,27218,82.04,82.71,90.6,90.6,88.32,1.48,-4.2,-7.43,0.83,-0.62,-50.18
20260402,82.4,82.5,82.4,82.5,2054,82.04,82.34,90.35,90.35,87.84,0.36,0,-8.13,0.07,0.19,-50
20260407,80.5,81,75.2,79.9,26369,81.42,82.04,90.05,90.05,87.17,-3.15,-3.73,-7.09,0.91,-2.61,-51.58
20260408,78.9,80.5,78,80.5,20211,81.22,81.94,89.77,89.77,86.62,0.75,-1.23,-2.42,0.77,-1.76,-51.21
20260409,82,82,79.8,80.5,16142,81.12,81.75,89.52,89.52,86.11,0,-0.62,-4.62,0.63,-1.52,-51.21
20260410,80.6,81.5,80.6,81,19146,80.88,81.66,89.29,89.29,85.68,0.62,-1.46,-2.17,0.75,-0.8,-50.91
20260413,79,80,78.1,79,35200,80.18,81.47,89.02,89.02,85.13,-2.47,-4.24,-4.36,1.34,-3.04,-52.12
20260414,79.5,80,79,79,29141,80,81.33,88.76,88.76,84.62,0,-1.13,-3.66,1.08,-2.86,-52.12
20260415,79.5,79.9,79.4,79.8,8145,79.86,81.39,88.53,88.53,84.21,1.01,-0.87,1.66,0.36,-1.95,-51.64
20260416,79.9,80,78.7,80,20149,79.76,81.24,88.33,88.33,83.86,0.25,-0.62,-3.61,1.07,-1.53,-51.52
20260417,79.5,79.9,79.5,79.6,12459,79.48,81.09,88.12,88.12,83.51,-0.5,-1.73,-3.63,0.69,-1.84,-51.76
20260420,79,80,78,78,58078,79.28,80.94,87.88,87.88,83.05,-2.01,-1.27,-3.7,2.97,-3.63,-52.73
20260421,78.5,79.5,78.3,78.8,19802,79.24,80.83,87.68,87.68,82.69,1.03,-0.25,-2.72,1,-2.51,-52.24
20260422,78.6,78.8,78.2,78.8,19209,79.04,80.73,87.48,87.48,82.37,0,-1.25,-2.35,0.98,-2.4,-52.24
20260423,78.6,78.6,77.4,77.6,28168,78.56,80.55,87.27,87.27,81.97,-1.52,-3,-4.55,1.35,-3.66,-52.97
20260424,76.5,76.8,76.2,76.8,16697,78,80.1,87.04,87.04,81.54,-1.03,-3.52,-10.49,0.81,-4.12,-53.45
20260427,77,80,77,80,36811,78.4,79.97,86.9,86.9,81.41,4.17,2.56,-3.03,1.75,0.03,-51.52
20260428,79.5,80.1,79.1,80.1,24158,78.66,79.83,86.76,86.76,81.3,0.12,1.65,-3.49,1.1,0.34,-51.45
20260429,80.1,80.9,79.7,80.9,30220,79.08,79.8,86.64,86.64,81.27,1,2.67,-0.74,1.31,1.38,-50.97
20260430,81.5,83.2,81.5,82.6,38833,80.08,79.88,86.56,86.56,81.38,2.1,6.44,1.98,1.59,3.41,-49.94
20260504,83,90,83,90,100650,82.72,80.27,86.63,86.63,82.1,8.96,17.19,9.49,3.58,12.12,-45.45
20260505,90,90,85.8,86.1,75908,83.94,80.45,86.62,86.62,82.43,-4.33,7.62,4.36,2.39,7.02,-47.82
20260506,86.1,93.8,85.8,93.6,71412,86.64,81.14,86.75,86.75,83.36,8.71,16.85,17.15,2.1,15.36,-43.27
20260507,93.6,93.6,88.5,90.6,56495,88.58,81.64,86.82,86.82,83.97,-3.21,11.99,12.55,1.58,10.97,-45.09
20260508,90.6,90.6,88,89.9,32803,90.04,82.11,86.87,86.87,84.46,-0.77,8.84,11.68,0.89,9.49,-45.52
20260511,89.9,90.7,88.9,89,46147,89.84,82.51,86.91,86.91,84.84,-1,-1.11,9.88,1.21,7.87,-46.06
20260512,88.4,90,87.3,90,38704,90.62,83.06,86.96,86.96,85.27,1.12,4.53,13.92,1.01,8.36,-45.45
20260513,89.8,90.5,87,90.2,32149,89.94,83.62,87.02,87.02,85.68,0.22,-3.63,14.18,0.84,7.87,-45.33
20260514,90.2,99.1,90,98.5,219792,91.52,84.56,87.21,87.21,86.75,9.2,8.72,23.43,4.49,16.49,-40.3
20260515,97.1,102.5,96.1,100,191738,93.54,85.56,86.41,87.42,87.85,1.52,11.23,25,3.33,16.88,-33.33
20260518,99.9,100,97.2,99.9,99166,95.72,86.57,85.89,87.62,88.86,-0.1,12.25,25.5,1.6,15.4,-22.26
20260519,99.9,100,99,100,46860,97.72,87.67,85.67,87.82,89.79,0.1,11.11,28.21,0.76,14.06,-11.89
20260520,100,108.5,97.1,107,227915,101.08,89.08,85.62,88.12,91.22,7,18.63,35.79,3.18,20.12,-2.73
20260521,107.5,111,106.5,109,84962,103.18,90.59,85.7,88.44,92.7,1.87,10.66,38.32,1.13,20.32,-1.8
20260522,109,109,100,107,107216,104.58,92.06,85.86,88.72,93.89,-1.83,7,37.89,1.36,16.23,-3.6
20260523,109,109,100,107,107216,106,93.57,86.14,88.99,94.99,0,7.11,39.32,1.28,14.35,-3.6
20260524,109,109,100,107,107216,107.4,94.92,86.44,89.26,95.99,0,7,33.75,1.23,12.73,-3.6
20260525,107,107,102,102,28523,106.4,96.02,86.62,89.44,96.49,-4.67,-4.67,27.34,0.33,6.23,-8.11
20260526,109,109,100,107,107216,106,97.32,86.88,89.69,97.36,4.9,-1.83,32.26,1.18,9.95,-3.6
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 73.34
- over_600_ratio: 70.03
- over_800_ratio: 64.14
- over_1000_ratio: 58.59
- over_400_change_1w: 1.6
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,72.06,,68.75,,64.14,,58.59,,0,False,False,False,,
20260508,71.83,-0.23,68.52,-0.23,64.14,0,58.59,0,0,False,False,False,,
20260515,71.74,-0.09,68.43,-0.09,64.17,0.03,58.62,0.03,1,False,True,False,,
20260522,73.34,1.6,70.03,1.6,64.14,-0.03,58.59,-0.03,2,False,False,False,,
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
