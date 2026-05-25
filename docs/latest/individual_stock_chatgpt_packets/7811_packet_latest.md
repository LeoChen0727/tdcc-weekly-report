# INDIVIDUAL STOCK CHATGPT PACKET - 7811 民盛

## Metadata
- generated_at: 2026-05-26 02:30:49 Asia/Taipei
- stock_id: 7811
- stock_name: 民盛
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 44
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7811_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7811_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7811_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7811.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7811.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7811.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7811.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7811.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7811.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7811_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7811_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7811_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 77.3
- high: 77.5
- low: 77
- close: 77.5
- volume: 77
- ma5: 77.2
- ma20: 79.94
- ma60: 84.23
- ma120: 84.23
- ema23: 80.38
- return_5d: -0.26
- return_20d: -9.88
- volume_ratio: 0
- distance_to_ma20_pct: -3.06
- distance_to_high_60_pct: -17.02

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260325,93.1,93.4,89.1,92,533000,,,,,,,,,,,
20260326,92,92.7,90.4,92.5,202000,,,,,,0.54,,,,,
20260327,92.4,92.4,90.2,90.9,127000,,,,,,-1.73,,,,,
20260330,91.2,91.6,89,90.4,170000,,,,,,-0.55,,,,,
20260331,89.4,91.8,89.4,90,151000,91.16,91.16,91.16,91.16,91.67,-0.44,,,0.64,-1.27,-3.64
20260401,90.3,90.5,90,90,34000,90.76,90.97,90.97,90.97,91.53,0,-2.17,,0.17,-1.06,-3.64
20260402,89.9,89.9,88.6,88.9,60000,90.04,90.67,90.67,90.67,91.31,-1.22,-3.89,,0.33,-1.95,-4.82
20260407,89,89,86.9,87.2,34000,89.3,90.24,90.24,90.24,90.97,-1.91,-4.07,,0.21,-3.37,-6.64
20260408,87,87,85.8,86.8,53000,88.58,89.86,89.86,89.86,90.62,-0.46,-3.98,,0.35,-3.4,-7.07
20260409,86,86.6,85.1,86.1,52000,87.8,89.48,89.48,89.48,90.24,-0.81,-4.33,,0.37,-3.78,-7.82
20260410,86,86,85.4,85.5,73000,86.9,89.12,89.12,89.12,89.85,-0.7,-5,,0.54,-4.06,-8.46
20260413,85.5,88.6,84.6,87.8,182000,86.68,89.01,89.01,89.01,89.68,2.69,-1.24,,1.31,-1.36,-6
20260414,87.8,88,87.6,88,63000,86.84,88.93,88.93,88.93,89.54,0.23,0.92,,0.47,-1.05,-5.78
20260415,88,90.9,88,90.1,123000,87.5,89.01,89.01,89.01,89.58,2.39,3.8,,0.93,1.22,-3.53
20260416,90,90,88.1,88.8,40000,88.04,89,89,89,89.52,-1.44,3.14,,0.32,-0.22,-4.93
20260417,88.8,88.8,88,88.6,39000,88.66,88.97,88.97,88.97,89.44,-0.23,3.63,,0.32,-0.42,-5.14
20260420,88.6,88.6,86.8,86.8,55000,88.46,88.85,88.85,88.85,89.22,-2.03,-1.14,,0.47,-2.3,-7.07
20260421,86.8,86.8,86,86.3,39000,88.12,88.71,88.71,88.71,88.98,-0.58,-1.93,,0.35,-2.71,-7.6
20260422,86.3,86.3,85.8,85.8,35000,87.26,88.55,88.55,88.55,88.71,-0.58,-4.77,,0.32,-3.11,-8.14
20260423,85,85.8,84.9,85.2,57000,86.54,88.39,88.39,88.39,88.42,-0.7,-4.05,,0.54,-3.6,-8.78
20260424,85,85.2,84.8,85.2,57000,85.86,88.05,88.23,88.23,88.15,0,-3.84,-7.39,0.69,-3.23,-8.78
20260427,85.2,85.2,84.7,84.7,34000,85.44,87.66,88.07,88.07,87.86,-0.59,-2.42,-8.43,0.46,-3.37,-9.31
20260428,84.7,84.7,82.9,83.5,87000,84.88,87.28,87.87,87.87,87.5,-1.42,-3.24,-8.14,1.21,-4.34,-10.6
20260429,83.3,87,83,86,111000,84.92,87.06,87.8,87.8,87.38,2.99,0.23,-4.87,1.61,-1.22,-7.92
20260430,85,85.6,84.4,84.4,16000,84.76,86.78,87.66,87.66,87.13,-1.86,-0.94,-6.22,0.26,-2.75,-9.64
20260504,85,85,84.4,85,28000,84.72,86.53,87.56,87.56,86.95,0.71,-0.23,-5.56,0.45,-1.77,-8.99
20260505,85,85.3,83.6,83.6,27000,84.5,86.27,87.41,87.41,86.67,-1.65,-1.3,-5.96,0.45,-3.09,-10.49
20260506,83.6,83.6,79.8,81.5,147000,84.1,85.98,87.2,87.2,86.24,-2.51,-2.4,-6.54,2.23,-5.22,-12.74
20260507,81.4,81.5,80.1,80.2,70000,82.94,85.66,86.96,86.96,85.74,-1.6,-6.74,-7.6,1.05,-6.37,-14.13
20260508,80.5,81.5,80.5,81.2,41000,82.3,85.41,86.77,86.77,85.36,1.25,-3.79,-5.69,0.62,-4.93,-13.06
20260511,81.1,81.3,80,80.9,35000,81.48,85.18,86.58,86.58,84.99,-0.37,-4.82,-5.38,0.54,-5.02,-13.38
20260512,80.9,80.9,80.4,80.4,23000,80.84,84.81,86.38,86.38,84.61,-0.62,-3.83,-8.43,0.41,-5.2,-13.92
20260513,79.7,81.7,75,81.3,187000,80.8,84.47,86.23,86.23,84.33,1.12,-0.25,-7.61,2.99,-3.76,-12.96
20260514,79.3,83.4,78.5,81.4,65000,81.04,84.04,86.09,86.09,84.09,0.12,1.5,-9.66,1.09,-3.14,-12.85
20260515,78.9,82,78.6,80.9,76000,80.98,83.64,85.94,85.94,83.82,-0.61,-0.37,-8.9,1.24,-3.28,-13.38
20260518,79.1,79.1,78.9,78.9,16000,80.58,83.16,85.74,85.74,83.41,-2.47,-2.47,-10.95,0.27,-5.12,-15.52
20260519,78.9,79,78.2,78.4,25000,80.18,82.74,85.55,85.55,82.99,-0.63,-2.49,-9.68,0.43,-5.25,-16.06
20260520,78,78,77.1,77.1,20000,79.34,82.28,85.32,85.32,82.5,-1.66,-5.17,-10.66,0.35,-6.3,-17.45
20260521,77.5,78,77.5,77.7,9000,78.6,81.88,85.13,85.13,82.1,0.78,-4.55,-9.44,0.16,-5.1,-16.81
20260522,77.7,77.7,77,77,77,77.82,81.47,84.92,84.92,81.68,-0.9,-4.82,-9.62,0,-5.48,-17.56
20260523,77.7,77.7,77,77,77,77.44,81.06,84.73,84.73,81.29,0,-2.41,-9.62,0,-5,-17.56
20260524,77.7,77.7,77,77,77,77.16,80.67,84.55,84.55,80.93,0,-1.79,-9.09,0,-4.55,-17.56
20260525,77.3,77.5,77,77.5,77,77.24,80.37,84.38,84.38,80.64,0.65,0.52,-7.19,0,-3.57,-17.02
20260526,77.3,77.5,77,77.5,77,77.2,79.94,84.23,84.23,80.38,0,-0.26,-9.88,0,-3.06,-17.02
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 71.38
- over_600_ratio: 66.93
- over_800_ratio: 64.77
- over_1000_ratio: 64.77
- over_400_change_1w: 0.17
- over_800_change_1w: 0.17
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,70.84,,66.42,,64.26,,64.26,,0,False,False,False,,
20260508,70.85,0.01,66.42,0,64.26,0,64.26,0,1,False,False,False,,
20260515,71.21,0.36,66.76,0.34,64.6,0.34,64.6,0.34,2,True,True,True,,
20260522,71.38,0.17,66.93,0.17,64.77,0.17,64.77,0.17,3,True,True,True,,
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
