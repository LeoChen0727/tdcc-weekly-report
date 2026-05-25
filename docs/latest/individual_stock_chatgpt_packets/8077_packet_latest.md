# INDIVIDUAL STOCK CHATGPT PACKET - 8077 洛碁

## Metadata
- generated_at: 2026-05-26 02:30:51 Asia/Taipei
- stock_id: 8077
- stock_name: 洛碁
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 67
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8077_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8077_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8077_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8077.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8077.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8077.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8077.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8077.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8077.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8077_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8077_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8077_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 45.6
- high: 45.6
- low: 45.6
- close: 45.6
- volume: 45
- ma5: 45.57
- ma20: 43.24
- ma60: 43.87
- ma120: 44.04
- ema23: 43.73
- return_5d: 1.79
- return_20d: 2.59
- volume_ratio: 0.01
- distance_to_ma20_pct: 5.45
- distance_to_high_60_pct: -2.88

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20251104,43.85,45.3,43.8,45.3,12000,,,,,,,,,,,
20251105,45.4,45.4,45,45.4,18000,,,,,,0.22,,,,,
20251106,46.45,46.45,46.45,46.45,1000,,,,,,2.31,,,,,
20251113,42.9,45.5,42.9,45.5,9000,,,,,,-2.05,,,,,
20251117,43.1,44.55,43.1,44.55,10000,45.44,45.44,45.44,45.44,45.34,-2.09,,,1,-1.96,-4.09
20251118,45.85,45.85,45.85,45.85,1000,45.55,45.51,45.51,45.51,45.38,2.92,1.21,,0.12,0.75,-1.29
20251119,45.9,45.9,45.4,45.4,6000,45.55,45.49,45.49,45.49,45.38,-0.98,0,,0.74,-0.2,-2.26
20251120,46.3,46.3,46.3,46.3,1000,45.52,45.59,45.59,45.59,45.46,1.98,-0.32,,0.14,1.55,-0.32
20251121,46.1,46.1,46.1,46.1,1000,45.64,45.65,45.65,45.65,45.51,-0.43,1.32,,0.15,0.99,-0.75
20251124,45.8,46.1,45.8,46.1,2000,45.95,45.7,45.7,45.7,45.56,0,3.48,,0.33,0.89,-0.75
20251126,46,46,46,46,1000,45.98,45.72,45.72,45.72,45.6,-0.22,0.33,,0.18,0.61,-0.97
20251204,46.45,46.45,46.45,46.45,1000,46.19,45.78,45.78,45.78,45.67,0.98,2.31,,0.19,1.46,0
20251208,46.95,46.95,46.45,46.45,2000,46.22,45.83,45.83,45.83,45.73,0,0.32,,0.4,1.34,-1.06
20251209,46.45,46.45,44.5,44.6,4000,45.92,45.75,45.75,45.75,45.64,-3.98,-3.25,,0.81,-2.51,-5.01
20251211,44.35,44.35,43.8,43.8,4000,45.46,45.62,45.62,45.62,45.49,-1.79,-4.99,,0.82,-3.98,-6.71
20251215,43.85,43.9,43.85,43.9,2000,45.04,45.51,45.51,45.51,45.35,0.23,-4.57,,0.43,-3.54,-6.5
20251216,42.8,42.8,42.8,42.8,1000,44.31,45.35,45.35,45.35,45.14,-2.51,-7.86,,0.22,-5.62,-8.84
20251218,42.8,42.8,42.8,42.8,1000,43.58,45.21,45.21,45.21,44.95,0,-7.86,,0.23,-5.33,-8.84
20251223,42.9,42.9,42.9,42.9,5000,43.24,45.09,45.09,45.09,44.78,0.23,-3.81,,1.16,-4.85,-8.63
20251229,43.6,43.6,43.6,43.6,1000,43.2,45.01,45.01,45.01,44.68,1.63,-0.46,,0.24,-3.14,-7.14
20251230,43.5,43.5,43.45,43.45,2000,43.11,44.92,44.94,44.94,44.58,-0.34,-1.03,-4.08,0.55,-3.27,-7.45
20251231,43.45,43.95,43.45,43.95,2000,43.34,44.85,44.89,44.89,44.52,1.15,2.69,-3.19,0.7,-2,-6.39
20260106,43.5,43.5,43.5,43.5,5000,43.48,44.7,44.83,44.83,44.44,-1.02,1.64,-6.35,1.64,-2.68,-7.35
20260107,42.1,43.4,42,43.4,12000,43.58,44.59,44.77,44.77,44.35,-0.23,1.17,-4.62,3.75,-2.68,-7.56
20260108,43.2,45.95,43.2,45.95,6000,44.05,44.66,44.82,44.82,44.48,5.88,5.39,3.14,2,2.88,-2.13
20260109,46.95,46.95,43,43,11000,43.96,44.52,44.75,44.75,44.36,-6.42,-1.04,-6.22,3.14,-3.42,-8.41
20260112,43.95,44.4,43.95,44.4,2000,44.05,44.47,44.74,44.74,44.36,3.26,1.02,-2.2,0.61,-0.16,-5.43
20260114,44.35,44.5,44.35,44.5,3000,44.25,44.38,44.73,44.73,44.38,0.23,2.3,-3.89,0.88,0.26,-5.22
20260116,43.5,43.5,43.5,43.5,1000,44.27,44.25,44.69,44.69,44.3,-2.25,0.23,-5.64,0.29,-1.7,-7.35
20260121,42.2,42.2,42.2,42.2,3000,43.52,44.06,44.6,44.6,44.13,-2.99,-8.16,-8.46,0.87,-4.22,-10.12
20260126,44.2,44.2,44.2,44.2,1000,43.76,43.97,44.59,44.59,44.13,4.74,2.79,-3.91,0.29,0.53,-5.86
20260129,45.7,45.7,45.7,45.7,1000,44.02,43.93,44.62,44.62,44.26,3.39,2.93,-1.61,0.29,4.03,-2.66
20260204,42.45,43.9,42.45,43.9,5000,43.9,43.8,44.6,44.6,44.23,-3.94,-1.35,-5.49,1.39,0.22,-6.5
20260205,43.9,43.9,43.8,43.85,3000,43.97,43.77,44.58,44.58,44.2,-0.11,0.8,-1.68,0.85,0.19,-6.6
20260206,44,45.7,44,45.7,2000,44.67,43.86,44.61,44.61,44.33,4.22,8.29,4.34,0.58,4.2,-2.66
20260209,45.65,45.65,45.65,45.65,1000,44.96,43.95,44.64,44.64,44.44,-0.11,3.28,3.99,0.29,3.87,-2.77
20260210,45.75,45.8,45.75,45.8,2000,44.98,44.1,44.67,44.67,44.55,0.33,0.22,7.01,0.58,3.86,-2.45
20260211,44.9,45.5,44.9,45.5,6000,45.3,44.23,44.69,44.69,44.63,-0.66,3.64,6.31,1.62,2.87,-3.09
20260224,44,44,43.2,43.6,7000,45.25,44.27,44.67,44.67,44.54,-4.18,-0.57,1.63,1.84,-1.51,-7.14
20260226,42.25,42.25,42.25,42.25,1000,44.56,44.2,44.61,44.61,44.35,-3.1,-7.55,-3.1,0.26,-4.41,-10.01
20260313,44.2,44.35,43.05,43.05,4000,44.04,44.18,44.57,44.57,44.24,1.89,-5.7,-0.92,1.03,-2.56,-8.31
20260316,43.05,43.05,43.05,43.05,1000,43.49,44.13,44.53,44.53,44.14,0,-6,-2.05,0.26,-2.46,-8.31
20260318,43.05,44,43.05,43.05,3000,43,44.11,44.5,44.5,44.05,0,-5.38,-1.03,0.8,-2.41,-8.31
20260319,43.1,43.1,42,42,2000,42.68,44.04,44.44,44.44,43.88,-2.44,-3.67,-3.23,0.62,-4.64,-10.54
20260324,41.5,41.5,41.5,41.5,1000,42.53,43.82,44.38,44.38,43.68,-1.19,-1.78,-9.68,0.33,-5.29,-11.61
20260401,42.75,44.2,42.75,44.2,4000,42.76,43.88,44.37,44.37,43.73,6.51,2.67,2.79,1.51,0.73,-5.86
20260407,44.45,44.45,44.45,44.45,1000,43.04,43.88,44.37,44.37,43.79,0.57,3.25,0.11,0.38,1.29,-5.32
20260409,42.5,44.1,42.5,44.1,7000,43.25,43.86,44.37,44.37,43.81,-0.79,2.44,-0.9,2.5,0.54,-6.07
20260413,45.5,45.5,45,45.2,18000,43.89,43.95,44.38,44.38,43.93,2.49,7.62,3.91,4.93,2.85,-3.73
20260414,44.1,44.1,44.1,44.1,1000,44.41,44.04,44.38,44.38,43.94,-2.43,6.27,4.5,0.28,0.13,-6.07
20260415,43.45,43.45,43.45,43.45,2000,44.26,44.01,44.36,44.36,43.9,-1.47,-1.7,-1.7,0.56,-1.26,-7.45
20260416,42.25,42.25,42.2,42.25,3000,43.82,43.83,44.32,44.32,43.76,-2.76,-4.95,-7.55,0.81,-3.61,-10.01
20260417,41.6,41.6,41.6,41.6,1000,43.32,43.72,44.27,44.27,43.58,-1.54,-5.67,-5.24,0.29,-4.84,-11.4
20260422,42.05,42.05,42.05,42.05,1000,42.69,43.63,44.23,44.23,43.46,1.08,-6.97,-4.1,0.29,-3.62,-10.44
20260427,42.05,42.05,42,42,2000,42.27,43.44,44.19,44.19,43.33,-0.12,-4.76,-8.1,0.59,-3.32,-10.54
20260507,41,41,39.8,40.35,10000,41.65,43.18,44.12,44.12,43.09,-3.93,-7.13,-11.61,2.6,-6.55,-14.06
20260508,40.2,40.2,39.7,39.7,16000,41.14,42.87,44.04,44.04,42.8,-1.61,-6.04,-13.32,3.52,-7.4,-15.44
20260511,40,40,40,40,1000,40.82,42.6,43.97,43.97,42.57,0.76,-3.85,-12.09,0.23,-6.1,-14.8
20260512,41,42.95,41,42.95,8000,41,42.56,43.95,43.95,42.6,7.38,2.14,-1.49,1.84,0.9,-8.52
20260518,43.4,43.4,43.4,43.4,1000,41.28,42.62,43.95,43.95,42.67,1.05,3.33,2.72,0.23,1.82,-7.56
20260519,43.6,43.6,41.05,41.05,4000,41.42,42.52,43.87,43.9,42.53,-5.41,1.73,-4.65,0.92,-3.46,-12.57
20260521,43.35,44.8,43.35,44.8,10000,42.44,42.61,43.86,43.91,42.72,9.14,12.85,4.07,2.08,5.14,-4.58
20260522,44.95,45.55,44.95,45.55,45,43.55,42.73,43.85,43.94,42.96,1.67,13.88,5.81,0.01,6.59,-2.98
20260523,44.95,45.55,44.95,45.55,45,44.07,42.91,43.85,43.96,43.17,0,6.05,8.45,0.01,6.15,-2.98
20260524,44.95,45.55,44.95,45.55,45,44.5,43.12,43.87,43.99,43.37,0,4.95,9.76,0.01,5.65,-2.98
20260525,45.6,45.6,45.6,45.6,45,45.41,43.19,43.86,44.01,43.56,0.11,11.08,3.17,0.01,5.59,-2.88
20260526,45.6,45.6,45.6,45.6,45,45.57,43.24,43.87,44.04,43.73,0,1.79,2.59,0.01,5.45,-2.88
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.25
- over_600_ratio: 79.84
- over_800_ratio: 76.98
- over_1000_ratio: 76.98
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,82.25,,79.84,,76.98,,76.98,,0,False,False,False,,
20260508,82.25,0,79.84,0,76.98,0,76.98,0,0,False,False,False,,
20260515,82.25,0,79.84,0,76.98,0,76.98,0,0,False,False,False,,
20260522,82.25,0,79.84,0,76.98,0,76.98,0,0,False,False,False,,
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
