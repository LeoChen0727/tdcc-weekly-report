# INDIVIDUAL STOCK CHATGPT PACKET - 8291 尚茂

## Metadata
- generated_at: 2026-05-26 02:30:55 Asia/Taipei
- stock_id: 8291
- stock_name: 尚茂
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 50
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8291_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8291_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8291_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8291.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8291.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8291.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8291.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8291.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8291.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8291_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8291_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8291_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 100
- high: 100
- low: 100
- close: 100
- volume: 100
- ma5: 94.66
- ma20: 58.48
- ma60: 32.12
- ma120: 32.12
- ema23: 61.35
- return_5d: 20.63
- return_20d: 398.75
- volume_ratio: 0
- distance_to_ma20_pct: 71
- distance_to_high_60_pct: 0

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260225,18.8,18.8,15.5,15.6,11000,,,,,,,,,,,
20260226,15.15,15.15,14.15,14.6,20000,,,,,,-6.41,,,,,
20260302,15.45,15.45,15,15,7000,,,,,,2.74,,,,,
20260303,15,15,15,15,16000,,,,,,0,,,,,
20260304,15,15,15,15,1000,15.04,15.04,15.04,15.04,15.4,0,,,0.09,-0.27,-20.21
20260305,15,15,15,15,6000,14.92,15.03,15.03,15.03,15.36,0,-3.85,,0.59,-0.22,-20.21
20260306,14.5,14.5,14.5,14.5,1000,14.9,14.96,14.96,14.96,15.29,-3.33,-0.68,,0.11,-3.06,-22.87
20260309,14.5,14.5,14.5,14.5,1000,14.8,14.9,14.9,14.9,15.23,0,-3.33,,0.13,-2.68,-22.87
20260310,14.5,14.5,14.5,14.5,2000,14.7,14.86,14.86,14.86,15.17,0,-3.33,,0.28,-2.39,-22.87
20260311,14.5,14.5,13.35,13.35,6000,14.37,14.71,14.71,14.71,15.01,-7.93,-11,,0.85,-9.21,-28.99
20260312,14.15,14.65,14.15,14.65,22000,14.3,14.7,14.7,14.7,14.98,9.74,-2.33,,2.6,-0.34,-22.07
20260313,14.65,15,13.6,13.7,15000,14.14,14.62,14.62,14.62,14.88,-6.48,-5.52,,1.67,-6.27,-27.13
20260316,13.7,13.9,13.25,13.9,8000,14.02,14.56,14.56,14.56,14.8,1.46,-4.14,,0.9,-4.54,-26.06
20260317,13.35,14.15,13.35,13.95,11000,13.91,14.52,14.52,14.52,14.73,0.36,-3.79,,1.21,-3.91,-25.8
20260319,13.95,14,13.85,14,4000,14.04,14.48,14.48,14.48,14.66,0.36,4.87,,0.46,-3.34,-25.53
20260320,14,14,14,14,2000,13.91,14.45,14.45,14.45,14.61,0,-4.44,,0.24,-3.14,-25.53
20260325,14.4,15.15,14.4,15.15,7000,14.2,14.49,14.49,14.49,14.65,8.21,10.58,,0.85,4.53,-19.41
20260331,14.4,14.4,14.3,14.4,6000,14.3,14.49,14.49,14.49,14.63,-4.95,3.6,,0.74,-0.61,-23.4
20260402,14,14,13.25,13.25,4000,14.16,14.42,14.42,14.42,14.52,-7.99,-5.02,,0.51,-8.14,-29.52
20260408,13.2,13.25,13.2,13.25,2000,14.01,14.37,14.37,14.37,14.41,0,-5.36,,0.26,-7.76,-29.52
20260414,13.25,14.55,13.25,13.4,20000,13.89,14.26,14.32,14.32,14.33,1.13,-4.29,-14.1,2.48,-6,-28.72
20260416,13.6,13.6,13.5,13.5,19000,13.56,14.2,14.28,14.28,14.26,0.75,-10.89,-7.53,2.38,-4.93,-28.19
20260420,12.2,12.25,12.15,12.15,3000,13.11,14.06,14.19,14.19,14.08,-10,-15.62,-19,0.38,-13.57,-35.37
20260421,12.75,12.8,12.5,12.5,6000,12.96,13.93,14.12,14.12,13.95,2.88,-5.66,-16.67,0.82,-10.28,-33.51
20260422,13,13.75,13,13.75,33000,13.06,13.87,14.1,14.1,13.93,10,3.77,-8.33,3.71,-0.87,-26.86
20260423,13.75,13.75,13.75,13.75,3000,13.13,13.81,14.09,14.09,13.92,0,2.61,-8.33,0.34,-0.42,-26.86
20260424,13.75,15.1,13.75,15.1,18000,13.45,13.84,14.13,14.13,14.02,9.82,11.85,4.14,1.88,9.12,-19.68
20260427,16.6,16.6,16.6,16.6,32000,14.34,13.94,14.22,14.22,14.23,9.93,36.63,14.48,2.87,19.06,-11.7
20260428,18.25,18.25,18.25,18.25,26000,15.49,14.13,14.36,14.36,14.57,9.94,46,25.86,2.11,29.16,-2.93
20260429,20.05,20.05,20.05,20.05,3000,16.75,14.46,14.54,14.54,15.02,9.86,45.82,50.19,0.25,38.61,0
20260430,22.05,22.05,20.1,22.05,110000,18.41,14.84,14.79,14.79,15.61,9.98,60.36,50.51,6.63,48.63,0
20260504,24.25,24.25,24.25,24.25,118000,20.24,15.36,15.08,15.08,16.33,9.98,60.6,77.01,5.43,57.85,0
20260505,26.65,26.65,26.65,26.65,163000,22.25,16,15.43,15.43,17.19,9.9,60.54,91.73,5.53,66.56,0
20260506,29.3,29.3,27,29.3,154000,24.46,16.77,15.84,15.84,18.2,9.94,60.55,110.04,4.2,74.74,0
20260507,32.2,32.2,32.2,32.2,158000,26.89,17.68,16.31,16.31,19.37,9.9,60.6,130,3.56,82.15,0
20260508,35.4,35.4,35.4,35.4,145000,29.56,18.75,16.84,16.84,20.7,9.94,60.54,152.86,2.82,88.83,0
20260511,38.9,38.9,38.9,38.9,109000,32.49,19.93,17.44,17.44,22.22,9.89,60.41,156.77,1.93,95.13,0
20260512,42.75,42.75,42.75,42.75,61000,35.71,21.35,18.1,18.1,23.93,9.9,60.41,196.88,1.03,100.21,0
20260513,47,47,47,47,178000,39.25,23.04,18.84,18.84,25.85,9.94,60.41,254.72,2.62,103.99,0
20260514,51.7,51.7,51.7,51.7,112000,43.15,24.96,19.66,19.66,28.01,10,60.56,290.19,1.52,107.11,0
20260515,56.8,56.8,56.8,56.8,153000,47.43,27.13,20.57,20.57,30.41,9.86,60.45,323.88,1.91,109.34,0
20260518,62.4,62.4,62.4,62.4,148000,52.13,29.58,21.57,21.57,33.07,9.86,60.41,362.22,1.71,110.97,0
20260519,68.6,68.6,68.6,68.6,162000,57.3,32.4,22.66,22.66,36.03,9.94,60.47,464.61,1.71,111.73,0
20260520,75.4,75.4,75.4,75.4,180000,62.98,35.55,23.86,23.86,39.31,9.91,60.43,503.2,1.74,112.13,0
20260521,82.9,82.9,82.9,82.9,179000,69.22,39,25.17,25.17,42.95,9.95,60.35,502.91,1.62,112.55,0
20260522,91.1,91.1,91.1,91.1,91,76.08,42.87,26.6,26.6,46.96,9.89,60.39,562.55,0,112.5,0
20260523,91.1,91.1,91.1,91.1,91,81.82,46.67,27.98,27.98,50.64,0,45.99,503.31,0,95.2,0
20260524,91.1,91.1,91.1,91.1,91,86.32,50.4,29.29,29.29,54.01,0,32.8,448.8,0,80.77,0
20260525,100,100,100,100,100,91.24,54.48,30.73,30.73,57.84,9.77,32.63,447.95,0,83.55,0
20260526,100,100,100,100,100,94.66,58.48,32.12,32.12,61.35,0,20.63,398.75,0,71,0
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 75.44
- over_600_ratio: 75.44
- over_800_ratio: 71.9
- over_1000_ratio: 71.9
- over_400_change_1w: -2.87
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,79.4,,79.4,,71.94,,71.94,,0,False,False,False,,
20260508,79.4,0,79.4,0,71.94,0,71.94,0,0,False,False,False,,
20260515,78.31,-1.09,75.76,-3.64,71.94,0,71.94,0,0,False,False,False,,
20260522,75.44,-2.87,75.44,-0.32,71.9,-0.04,71.9,-0.04,0,False,False,False,,
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
