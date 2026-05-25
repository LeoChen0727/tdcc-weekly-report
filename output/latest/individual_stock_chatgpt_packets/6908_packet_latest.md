# INDIVIDUAL STOCK CHATGPT PACKET - 6908 宏碁遊戲-創

## Metadata
- generated_at: 2026-05-26 02:30:42 Asia/Taipei
- stock_id: 6908
- stock_name: 宏碁遊戲-創
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6908_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6908_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6908_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6908.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6908.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6908.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6908.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6908.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6908.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6908_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6908_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6908_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 38.6
- high: 38.85
- low: 38.3
- close: 38.3
- volume: 12573
- ma5: 38.37
- ma20: 39.16
- ma60: 39.59
- ma120: 39.59
- ema23: 39.08
- return_5d: -0.52
- return_20d: -1.79
- volume_ratio: 0.74
- distance_to_ma20_pct: -2.19
- distance_to_high_60_pct: -29.07

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260325,50,54,45,48.1,451122,,,,,,,,,,,
20260326,47.35,47.4,45,45,281334,,,,,,-6.44,,,,,
20260327,44.5,44.5,41.5,42.1,152179,,,,,,-6.44,,,,,
20260330,41.5,41.5,39.25,40,105486,,,,,,-4.99,,,,,
20260331,39.8,39.95,39,39.85,53621,43.01,43.01,43.01,43.01,46.17,-0.38,,,0.26,-7.35,-26.2
20260401,40,41.6,40,41.05,86776,41.6,42.68,42.68,42.68,45.75,3.01,-14.66,,0.46,-3.83,-23.98
20260402,41.05,41.05,39.55,39.55,39200,40.51,42.24,42.24,42.24,45.23,-3.65,-12.11,,0.23,-6.36,-26.76
20260407,39.6,39.9,39.1,39.1,26369,39.91,41.84,41.84,41.84,44.72,-1.14,-7.13,,0.18,-6.56,-27.59
20260408,39.1,39.15,37.05,38.95,85460,39.7,41.52,41.52,41.52,44.24,-0.38,-2.62,,0.6,-6.19,-27.87
20260409,40.9,40.9,38,38.05,70390,39.34,41.17,41.17,41.17,43.72,-2.31,-4.52,,0.52,-7.59,-29.54
20260410,38.2,38.2,37.9,38.15,33789,38.76,40.9,40.9,40.9,43.26,0.26,-7.06,,0.27,-6.72,-29.35
20260413,38.15,38.15,37.5,37.65,30455,38.38,40.63,40.63,40.63,42.79,-1.31,-4.8,,0.26,-7.33,-30.28
20260414,38,38.5,37.9,37.9,28661,38.14,40.42,40.42,40.42,42.38,0.66,-3.07,,0.26,-6.23,-29.81
20260415,37.9,38.1,37.8,37.9,23768,37.93,40.24,40.24,40.24,42.01,0,-2.7,,0.23,-5.81,-29.81
20260416,37.9,39.4,37.9,38.9,49320,38.1,40.15,40.15,40.15,41.75,2.64,2.23,,0.49,-3.11,-27.96
20260417,42.7,42.7,40.1,41.55,83284,38.78,40.24,40.24,40.24,41.73,6.81,8.91,,0.83,3.26,-23.06
20260420,41.6,41.7,40.5,40.5,40082,39.35,40.25,40.25,40.25,41.63,-2.53,7.57,,0.42,0.61,-25
20260421,40.4,40.4,39.7,39.85,16371,39.74,40.23,40.23,40.23,41.48,-1.6,5.15,,0.18,-0.95,-26.2
20260422,39.9,40,39.85,39.85,11194,40.13,40.21,40.21,40.21,41.35,0,5.15,,0.13,-0.9,-26.2
20260423,40.5,40.5,39.35,39.35,35724,40.22,40.17,40.17,40.17,41.18,-1.25,1.16,,0.42,-2.04,-27.13
20260424,39.8,39.8,39,39,30301,39.71,39.71,40.11,40.11,41,-0.89,-6.14,-18.92,0.47,-1.79,-27.78
20260427,38.5,38.7,38.5,38.7,29647,39.35,39.4,40.05,40.05,40.81,-0.77,-4.44,-14,0.57,-1.77,-28.33
20260428,38.7,39,38.7,38.95,13020,39.17,39.24,40,40,40.65,0.65,-2.26,-7.48,0.29,-0.74,-27.87
20260429,38.95,40,38.95,39,12548,39,39.19,39.96,39.96,40.51,0.13,-2.13,-2.5,0.31,-0.48,-27.78
20260430,39.8,40.2,39.5,40.2,40524,39.17,39.21,39.97,39.97,40.49,3.08,2.16,0.88,1.03,2.53,-25.56
20260504,42,42,40.5,41.1,29683,39.59,39.21,40.01,40.01,40.54,2.24,5.38,0.12,0.81,4.82,-23.89
20260505,41.1,41.1,40.05,40.95,18373,40.04,39.28,40.05,40.05,40.57,-0.36,5.81,3.54,0.52,4.25,-24.17
20260506,41.5,41.5,40.5,40.55,19112,40.36,39.35,40.06,40.06,40.57,-0.98,4.11,3.71,0.54,3.04,-24.91
20260507,41,41,40.25,40.4,15018,40.64,39.42,40.08,40.08,40.56,-0.37,3.59,3.72,0.48,2.47,-25.19
20260508,40.1,40.1,39.55,40.1,10358,40.62,39.53,40.08,40.08,40.52,-0.74,-0.25,5.39,0.36,1.45,-25.74
20260511,39.15,40,39.15,39.45,22024,40.29,39.59,40.06,40.06,40.43,-1.62,-4.01,3.41,0.79,-0.36,-26.94
20260512,39.45,39.5,39.3,39.3,10130,39.96,39.67,40.03,40.03,40.34,-0.38,-4.03,4.38,0.38,-0.95,-27.22
20260513,39,39,38.7,38.7,20018,39.59,39.72,39.99,39.99,40.2,-1.53,-4.56,2.11,0.75,-2.56,-28.33
20260514,38.7,40.35,38.5,39,25012,39.31,39.77,39.96,39.96,40.1,0.78,-3.47,2.9,0.94,-1.94,-27.78
20260515,38.6,38.6,38.45,38.6,8200,39.01,39.76,39.92,39.92,39.97,-1.03,-3.74,-0.77,0.33,-2.91,-28.52
20260518,38,38.15,38,38.15,7000,38.75,39.59,39.88,39.88,39.82,-1.17,-3.3,-8.18,0.34,-3.63,-29.35
20260519,38.15,38.2,38.15,38.2,9000,38.53,39.47,39.83,39.83,39.69,0.13,-2.8,-5.68,0.47,-3.22,-29.26
20260520,39,39,38.1,38.1,5001,38.41,39.38,39.78,39.78,39.56,-0.26,-1.55,-4.39,0.27,-3.26,-29.44
20260521,38.6,38.6,38.3,38.5,3001,38.31,39.31,39.75,39.75,39.47,1.05,-1.28,-3.39,0.17,-2.07,-28.7
20260522,38.6,38.85,38.3,38.3,12573,38.25,39.26,39.72,39.72,39.37,-0.52,-0.78,-2.67,0.74,-2.45,-29.07
20260523,38.6,38.85,38.3,38.3,12573,38.28,39.23,39.68,39.68,39.28,0,0.39,-1.79,0.78,-2.36,-29.07
20260524,38.6,38.85,38.3,38.3,12573,38.3,39.21,39.65,39.65,39.2,0,0.26,-1.03,0.82,-2.31,-29.07
20260525,38.15,39.3,38.15,38.65,47511,38.41,39.19,39.62,39.62,39.15,0.91,1.44,-0.77,2.79,-1.38,-28.43
20260526,38.6,38.85,38.3,38.3,12573,38.37,39.16,39.59,39.59,39.08,-0.91,-0.52,-1.79,0.74,-2.19,-29.07
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 86.39
- over_600_ratio: 86.39
- over_800_ratio: 86.39
- over_1000_ratio: 86.39
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,86.39,,86.39,,86.39,,86.39,,0,False,False,False,,
20260508,86.39,0,86.39,0,86.39,0,86.39,0,0,False,False,False,,
20260515,86.39,0,86.39,0,86.39,0,86.39,0,0,False,False,False,,
20260522,86.39,0,86.39,0,86.39,0,86.39,0,0,False,False,False,,
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
