# INDIVIDUAL STOCK CHATGPT PACKET - 6103 合邦

## Metadata
- generated_at: 2026-05-26 02:30:15 Asia/Taipei
- stock_id: 6103
- stock_name: 合邦
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 58
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6103_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6103_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6103_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6103.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6103.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6103.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6103.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6103.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6103.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6103_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6103_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6103_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 37.15
- high: 37.15
- low: 37.15
- close: 37.15
- volume: 37
- ma5: 36.58
- ma20: 38.59
- ma60: 40.46
- ma120: 40.46
- ema23: 38.8
- return_5d: -1.98
- return_20d: -4.74
- volume_ratio: 0.02
- distance_to_ma20_pct: -3.74
- distance_to_high_60_pct: -31.96

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20251126,32.65,35.85,32.65,35.85,2000,,,,,,,,,,,
20251202,31.85,34.75,31.85,34.75,2000,,,,,,-3.07,,,,,
20251211,34.4,34.4,34.4,34.4,1000,,,,,,-1.01,,,,,
20251212,34.95,35.45,34.95,35.45,2000,,,,,,3.05,,,,,
20251217,33.4,33.4,33.4,33.4,1000,34.77,34.77,34.77,34.77,35.44,-5.78,,,0.62,-3.94,-6.83
20251218,33.95,33.95,33.95,33.95,1000,34.39,34.63,34.63,34.63,35.32,1.65,-5.3,,0.67,-1.97,-5.3
20251219,34,35.95,34,35.95,3000,34.63,34.82,34.82,34.82,35.37,5.89,3.45,,1.75,3.24,0
20251222,36.4,36.4,36.4,36.4,1000,35.03,35.02,35.02,35.02,35.46,1.25,5.81,,0.62,3.94,0
20251223,36.45,36.45,36.45,36.45,1000,35.23,35.18,35.18,35.18,35.54,0.14,2.82,,0.64,3.62,0
20260107,35.65,35.65,35.65,35.65,1000,35.68,35.23,35.23,35.23,35.55,-2.19,6.74,,0.67,1.21,-2.19
20260114,35.5,35.5,35.5,35.5,1000,35.99,35.25,35.25,35.25,35.54,-0.42,4.57,,0.69,0.71,-2.61
20260127,34.95,34.95,34.95,34.95,1000,35.79,35.23,35.23,35.23,35.5,-1.55,-2.78,,0.71,-0.78,-4.12
20260311,36.6,37.4,36.6,37.4,9000,35.99,35.39,35.39,35.39,35.65,7.01,2.75,,4.5,5.67,0
20260312,39,41.1,39,41.1,13000,36.92,35.8,35.8,35.8,36.11,9.89,12.76,,4.67,14.8,0
20260313,44,45.2,44,45.2,17000,38.83,36.43,36.43,36.43,36.87,9.98,26.79,,4.55,24.08,0
20260316,49.7,49.7,49.7,49.7,7000,41.67,37.26,37.26,37.26,37.94,9.96,40,,1.78,33.4,0
20260317,54.6,54.6,52,52,104000,45.08,38.12,38.12,38.12,39.11,4.63,48.78,,10.59,36.4,-4.76
20260318,51.3,51.3,46.8,49.55,51000,47.51,38.76,38.76,38.76,39.98,-4.71,32.49,,4.21,27.84,-9.25
20260319,48,48.9,48,48,8000,48.89,39.24,39.24,39.24,40.65,-3.13,16.79,,0.67,22.31,-12.09
20260320,48.6,48.6,45.6,45.6,10000,48.97,39.56,39.56,39.56,41.06,-5,0.89,,0.85,15.26,-16.48
20260323,45.6,45.6,45.6,45.6,1000,48.15,40.05,39.85,39.85,41.44,0,-8.25,27.2,0.09,13.86,-16.48
20260324,48.75,50.1,46.9,46.9,21000,47.13,40.66,40.17,40.17,41.89,2.85,-9.81,34.96,1.65,15.35,-14.1
20260325,45.7,48.45,45.35,48.45,10000,46.91,41.36,40.53,40.53,42.44,3.3,-2.22,40.84,0.76,17.14,-11.26
20260326,48.5,48.6,48.45,48.45,5000,47,42.01,40.86,40.86,42.94,0,0.94,36.67,0.38,15.33,-11.26
20260327,48.7,48.8,48.7,48.8,3000,47.64,42.78,41.18,41.18,43.43,0.72,7.02,46.11,0.22,14.07,-10.62
20260330,48.8,48.8,46.35,46.4,5000,47.8,43.4,41.38,41.38,43.68,-4.92,1.75,36.67,0.37,6.91,-15.02
20260331,42.3,42.3,42.3,42.3,2000,46.88,43.72,41.41,41.41,43.56,-8.84,-9.81,17.66,0.15,-3.25,-22.53
20260401,43,44,39.5,39.5,8000,45.09,43.88,41.34,41.34,43.22,-6.62,-18.47,8.52,0.58,-9.97,-27.66
20260402,42.65,43.45,42.65,43.45,7000,44.09,44.23,41.42,41.42,43.24,10,-10.32,19.2,0.49,-1.75,-20.42
20260407,43.45,44.15,40.35,42.35,35000,42.8,44.56,41.45,41.45,43.17,-2.53,-13.22,18.79,2.2,-4.96,-22.44
20260408,42,42,41.2,41.5,7000,41.82,44.86,41.45,41.45,43.03,-2.01,-10.56,16.9,0.43,-7.49,-23.99
20260409,39.25,39.25,39.25,39.25,1000,41.21,45.08,41.38,41.38,42.71,-5.42,-7.21,12.3,0.06,-12.92,-28.11
20260410,42.65,43.15,40.05,43.15,18000,41.94,45.36,41.43,41.43,42.75,9.94,9.24,15.37,1.08,-4.88,-20.97
20260413,43.2,44.4,43,44,11000,42.05,45.51,41.51,41.51,42.85,1.97,1.27,7.06,0.66,-3.31,-19.41
20260414,41,42,40.6,41,18000,41.78,45.3,41.5,41.5,42.7,-6.82,-3.19,-9.29,1.08,-9.49,-24.91
20260415,41,41.8,41,41.8,4000,41.84,44.9,41.5,41.5,42.62,1.95,0.72,-15.9,0.24,-6.91,-23.44
20260416,41.8,41.9,41.7,41.9,3000,42.37,44.4,41.51,41.51,42.56,0.24,6.75,-19.42,0.26,-5.63,-23.26
20260420,38.55,39.3,38.55,39,9000,41.54,43.87,41.45,41.45,42.27,-6.92,-9.62,-21.29,0.97,-11.1,-28.57
20260421,39.1,39.1,39.1,39.1,1000,40.56,43.42,41.39,41.39,42,0.26,-11.14,-18.54,0.11,-9.96,-28.39
20260422,39.5,39.6,39.5,39.6,2000,40.28,43.12,41.34,41.34,41.8,1.28,-3.41,-13.16,0.23,-8.17,-27.47
20260423,39.7,39.7,39.6,39.6,3000,39.84,42.83,41.3,41.3,41.62,0,-5.26,-13.16,0.35,-7.53,-27.47
20260428,38.3,38.3,38.3,38.3,1000,39.12,42.4,41.23,41.23,41.34,-3.28,-8.59,-18.34,0.13,-9.66,-29.85
20260430,38.3,39.7,38.3,39.7,2000,39.26,41.96,41.19,41.19,41.21,3.66,1.79,-18.06,0.28,-5.38,-27.29
20260505,39.7,39.7,39.6,39.6,4000,39.36,41.52,41.16,41.16,41.07,-0.25,1.28,-18.27,0.56,-4.61,-27.47
20260506,39.6,39.6,39.6,39.6,1000,39.36,41.05,41.12,41.12,40.95,0,0,-18.85,0.14,-3.54,-27.47
20260507,40,40,39.7,39.7,4000,39.38,40.72,41.09,41.09,40.85,0.25,0.25,-14.44,0.57,-2.5,-27.29
20260508,39.7,40,39.7,40,2000,39.72,40.6,41.07,41.07,40.77,0.76,4.44,-5.44,0.28,-1.49,-26.74
20260511,40,40,40,40,2000,39.78,40.63,41.05,41.05,40.71,0,0.76,1.27,0.3,-1.55,-26.74
20260512,40,40,40,40,3000,39.86,40.46,41.03,41.03,40.65,0,1.01,-7.94,0.46,-1.13,-26.74
20260513,40,40,38,39.1,10000,39.76,40.3,40.99,40.99,40.52,-2.25,-1.26,-7.67,1.89,-2.97,-28.39
20260514,39.1,39.1,39.1,39.1,1000,39.64,40.17,40.95,40.95,40.4,0,-1.51,-5.78,0.2,-2.68,-28.39
20260515,37.65,37.65,37.65,37.65,1000,39.17,40.09,40.89,40.89,40.17,-3.71,-5.88,-4.08,0.2,-6.1,-31.04
20260518,37.9,37.9,37.9,37.9,1000,38.75,39.83,40.83,40.83,39.98,0.66,-5.25,-12.17,0.24,-4.85,-30.59
20260522,36.2,36.2,36.2,36.2,36,37.99,39.44,40.74,40.74,39.67,-4.49,-9.5,-17.73,0.01,-8.22,-33.7
20260523,36.2,36.2,36.2,36.2,36,37.41,39.2,40.66,40.66,39.38,0,-7.42,-11.71,0.01,-7.66,-33.7
20260524,36.2,36.2,36.2,36.2,36,36.83,38.92,40.58,40.58,39.12,0,-7.42,-13.4,0.01,-6.99,-33.7
20260525,37.15,37.15,37.15,37.15,37,36.73,38.69,40.52,40.52,38.95,2.62,-1.33,-11.34,0.02,-3.97,-31.96
20260526,37.15,37.15,37.15,37.15,37,36.58,38.59,40.46,40.46,38.8,0,-1.98,-4.74,0.02,-3.74,-31.96
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 91.11
- over_600_ratio: 83.84
- over_800_ratio: 83.84
- over_1000_ratio: 83.84
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,91.11,,83.84,,83.84,,83.84,,0,False,False,False,,
20260508,91.11,0,83.84,0,83.84,0,83.84,0,0,False,False,False,,
20260515,91.11,0,83.84,0,83.84,0,83.84,0,0,False,False,False,,
20260522,91.11,0,83.84,0,83.84,0,83.84,0,0,False,False,False,,
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
