# INDIVIDUAL STOCK CHATGPT PACKET - 6028 公勝保經

## Metadata
- generated_at: 2026-05-26 02:30:15 Asia/Taipei
- stock_id: 6028
- stock_name: 公勝保經
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6028_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6028_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6028_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6028.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6028.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6028.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6028.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6028.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6028.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6028_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6028_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6028_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 79.6
- high: 80
- low: 79
- close: 80
- volume: 79
- ma5: 79.76
- ma20: 80.08
- ma60: 81.65
- ma120: 81.65
- ema23: 80.54
- return_5d: -0.12
- return_20d: 0.76
- volume_ratio: 0
- distance_to_ma20_pct: -0.1
- distance_to_high_60_pct: -13.04

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260330,86.5,89.6,81.6,89,675000,,,,,,,,,,,
20260331,89,92,89,89.5,353000,,,,,,0.56,,,,,
20260401,90.7,91,89.1,89.7,219000,,,,,,0.22,,,,,
20260402,89.7,90,88,88.1,81000,,,,,,-1.78,,,,,
20260407,88.1,88.1,86.6,87,104000,88.66,88.66,88.66,88.66,88.85,-1.25,,,0.36,-1.87,-5.43
20260408,88.8,90.2,87.2,90.2,246000,88.9,88.92,88.92,88.92,88.96,3.68,1.35,,0.88,1.44,-1.96
20260409,84.5,84.5,82,84,134000,87.8,88.21,88.21,88.21,88.55,-6.87,-6.15,,0.52,-4.78,-8.7
20260410,84.6,84.7,83.8,84.5,70000,86.76,87.75,87.75,87.75,88.21,0.6,-5.8,,0.3,-3.7,-8.15
20260413,84.8,84.8,82.5,82.5,71000,85.64,87.17,87.17,87.17,87.73,-2.37,-6.36,,0.33,-5.35,-10.33
20260414,82.5,83.4,82.1,82.1,33000,84.66,86.66,86.66,86.66,87.26,-0.48,-5.63,,0.17,-5.26,-10.76
20260415,82.1,82.1,81.6,81.7,32000,82.96,86.21,86.21,86.21,86.8,-0.49,-9.42,,0.17,-5.23,-11.2
20260416,81.7,82,81.1,81.4,36000,82.44,85.81,85.81,85.81,86.35,-0.37,-3.1,,0.21,-5.14,-11.52
20260417,81.1,81.1,80.3,80.4,58000,81.62,85.39,85.39,85.39,85.85,-1.23,-4.85,,0.36,-5.85,-12.61
20260420,80.4,80.4,78.9,79.1,81000,80.94,84.94,84.94,84.94,85.29,-1.62,-4.12,,0.52,-6.88,-14.02
20260421,79.1,79.6,78.8,79.6,22000,80.44,84.59,84.59,84.59,84.82,0.63,-3.05,,0.15,-5.9,-13.48
20260422,79.7,81.3,79.7,80.2,48000,80.14,84.31,84.31,84.31,84.43,0.75,-1.84,,0.34,-4.88,-12.83
20260423,81.2,81.5,79.9,80,34000,79.86,84.06,84.06,84.06,84.06,-0.25,-1.72,,0.25,-4.83,-13.04
20260424,80,80,79,79,24000,79.58,83.78,83.78,83.78,83.64,-1.25,-1.74,,0.19,-5.7,-14.13
20260427,80,80,78.2,78.4,27000,79.44,83.49,83.49,83.49,83.2,-0.76,-0.89,,0.22,-6.1,-14.78
20260428,78.2,80.1,78.2,80.1,26000,79.54,83.33,83.33,83.33,82.95,2.17,0.63,,0.22,-3.87,-12.93
20260429,79.4,79.4,79.4,79.4,3000,79.38,82.84,83.14,83.14,82.65,-0.87,-1,-10.79,0.04,-4.16,-13.7
20260430,79.4,80,78.8,79.9,19000,79.36,82.36,82.99,82.99,82.42,0.63,-0.12,-10.73,0.28,-2.99,-13.15
20260504,80,80,79.5,79.5,13000,79.46,81.86,82.84,82.84,82.18,-0.5,0.63,-11.37,0.22,-2.88,-13.59
20260505,79.2,79.5,78.5,79.1,20000,79.6,81.41,82.68,82.68,81.92,-0.5,0.89,-10.22,0.36,-2.83,-14.02
20260506,79.1,79.3,78.8,78.8,9000,79.34,81,82.53,82.53,81.66,-0.38,-1.62,-9.43,0.18,-2.71,-14.35
20260507,78.8,78.8,78.4,78.5,26000,79.16,80.41,82.37,82.37,81.4,-0.38,-1.13,-12.97,0.66,-2.38,-14.67
20260508,78.5,79.1,78.5,78.7,13000,78.92,80.14,82.24,82.24,81.17,0.25,-1.5,-6.31,0.39,-1.8,-14.46
20260511,80.6,82.5,80,81.9,96000,79.4,80.02,82.22,82.22,81.23,4.07,3.02,-3.08,2.78,2.36,-10.98
20260512,82.3,82.3,80.6,81.4,28000,79.86,79.96,82.2,82.2,81.25,-0.61,2.91,-1.33,0.86,1.8,-11.52
20260513,81.9,81.9,81,81,46000,80.3,79.91,82.16,82.16,81.23,-0.49,2.79,-1.34,1.39,1.37,-11.96
20260514,81.3,82.7,81.3,82.2,55000,81.04,79.93,82.16,82.16,81.31,1.48,4.71,0.61,1.61,2.84,-10.65
20260515,82.2,82.2,80.7,80.8,21000,81.46,79.9,82.12,82.12,81.27,-1.7,2.67,-0.74,0.63,1.13,-12.17
20260518,80,81,80,80.8,11000,81.24,79.92,82.08,82.08,81.23,0,-1.34,0.5,0.35,1.1,-12.17
20260519,80.1,80.6,80,80,17000,80.96,79.97,82.01,82.01,81.12,-0.99,-1.72,1.14,0.61,0.04,-13.04
20260520,80.1,80.1,80,80.1,5000,80.78,79.99,81.96,81.96,81.04,0.12,-1.11,0.63,0.18,0.14,-12.93
20260521,80.1,81,80,80.1,24000,80.36,79.98,81.91,81.91,80.96,0,-2.55,-0.12,0.93,0.14,-12.93
20260522,80.7,80.7,79.1,79.6,80,80.12,79.97,81.85,81.85,80.85,-0.62,-1.49,-0.5,0,-0.46,-13.48
20260523,80.7,80.7,79.1,79.6,80,79.88,80,81.79,81.79,80.74,0,-1.49,0.76,0,-0.49,-13.48
20260524,80.7,80.7,79.1,79.6,80,79.8,80.06,81.73,81.73,80.65,0,-0.5,1.53,0,-0.57,-13.48
20260525,79.6,80,79,80,79,79.78,80.05,81.69,81.69,80.59,0.5,-0.12,-0.12,0,-0.06,-13.04
20260526,79.6,80,79,80,79,79.76,80.08,81.65,81.65,80.54,0,-0.12,0.76,0,-0.1,-13.04
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.25
- over_600_ratio: 50.64
- over_800_ratio: 50.64
- over_1000_ratio: 50.64
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,64.25,,50.64,,50.64,,50.64,,0,False,False,False,,
20260508,64.25,0,50.64,0,50.64,0,50.64,0,0,False,False,False,,
20260515,64.25,0,50.64,0,50.64,0,50.64,0,0,False,False,False,,
20260522,64.25,0,50.64,0,50.64,0,50.64,0,0,False,False,False,,
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
