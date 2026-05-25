# INDIVIDUAL STOCK CHATGPT PACKET - 8923 時報

## Metadata
- generated_at: 2026-05-26 02:30:59 Asia/Taipei
- stock_id: 8923
- stock_name: 時報
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 71
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8923_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8923_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8923_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8923.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8923.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8923.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8923.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8923.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8923.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8923_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8923_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8923_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 20.1
- high: 20.1
- low: 20.1
- close: 20.1
- volume: 20
- ma5: 19.95
- ma20: 19.62
- ma60: 19.72
- ma120: 19.82
- ema23: 19.71
- return_5d: 2.55
- return_20d: 2.03
- volume_ratio: 0.01
- distance_to_ma20_pct: 2.42
- distance_to_high_60_pct: -1.95

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20251103,20.4,20.4,20.4,20.4,2000,,,,,,,,,,,
20251104,20.55,20.55,20.55,20.55,1000,,,,,,0.74,,,,,
20251106,20.2,21.5,20.2,20.5,71000,,,,,,-0.24,,,,,
20251107,20.2,20.45,20.2,20.45,3000,,,,,,-0.24,,,,,
20251111,20.15,21.5,20,21.05,30000,20.59,20.59,20.59,20.59,20.47,2.93,,,1.4,2.23,-2.09
20251112,20.15,20.55,20,20.2,59000,20.55,20.52,20.52,20.52,20.45,-4.04,-0.98,,2.13,-1.58,-6.05
20251113,20.05,20.15,20,20,8000,20.44,20.45,20.45,20.45,20.41,-0.99,-2.68,,0.32,-2.2,-6.98
20251114,20.35,20.4,20.15,20.4,5000,20.42,20.44,20.44,20.44,20.41,2,-0.49,,0.22,-0.21,-5.12
20251117,20.35,20.35,20.35,20.35,4000,20.4,20.43,20.43,20.43,20.41,-0.25,-0.49,,0.2,-0.41,-5.35
20251118,20.05,20.05,19.8,19.8,10000,20.15,20.37,20.37,20.37,20.36,-2.7,-5.94,,0.52,-2.8,-7.91
20251119,19.8,19.8,19.8,19.8,1000,20.07,20.32,20.32,20.32,20.31,0,-1.98,,0.06,-2.55,-7.91
20251121,19.7,20.25,19.7,20.25,5000,20.12,20.31,20.31,20.31,20.31,2.27,1.25,,0.3,-0.31,-5.81
20251124,19.9,19.9,19.4,19.4,16000,19.92,20.24,20.24,20.24,20.23,-4.2,-4.9,,0.97,-4.16,-9.77
20251125,19.55,19.55,19.4,19.5,5000,19.75,20.19,20.19,20.19,20.17,0.52,-4.18,,0.32,-3.41,-9.3
20251126,19.9,19.9,19.9,19.9,1000,19.77,20.17,20.17,20.17,20.15,2.05,0.51,,0.07,-1.34,-7.44
20251201,19.7,20.05,19.7,20.05,11000,19.82,20.16,20.16,20.16,20.14,0.75,1.26,,0.76,-0.56,-6.74
20251205,19.2,19.9,19.2,19.9,3000,19.75,20.15,20.15,20.15,20.12,-0.75,-1.73,,0.22,-1.23,-7.44
20251208,19.9,19.9,19.7,19.7,2000,19.81,20.12,20.12,20.12,20.08,-1,1.55,,0.15,-2.1,-8.37
20251209,19.8,19.8,19.8,19.8,3000,19.87,20.11,20.11,20.11,20.06,0.51,1.54,,0.24,-1.52,-7.91
20251210,19.8,20.1,19.8,20.1,2000,19.91,20.11,20.11,20.11,20.06,1.52,1,,0.17,-0.02,-6.51
20251212,19.6,19.6,19.6,19.6,1000,19.82,20.07,20.08,20.08,20.02,-2.49,-2.24,-3.92,0.08,-2.32,-8.84
20251217,20.2,20.5,20.2,20.5,6000,19.94,20.06,20.1,20.1,20.06,4.59,3.02,-0.24,0.49,2.18,-4.65
20251226,19.8,19.8,19.5,19.5,10000,19.9,20.01,20.07,20.07,20.02,-4.88,-1.02,-4.88,1.08,-2.56,-9.3
20251229,19.5,20,19.5,20,2000,19.94,19.99,20.07,20.07,20.02,2.56,1.01,-2.2,0.22,0.05,-6.98
20260107,19.2,19.3,19.2,19.3,5000,19.78,19.9,20.04,20.04,19.96,-3.5,-3.98,-8.31,0.63,-3.03,-10.23
20260115,19.45,19.45,19.4,19.4,2000,19.74,19.86,20.02,20.02,19.91,0.52,-1.02,-3.96,0.39,-2.33,-9.77
20260119,19.5,19.5,19.5,19.5,1000,19.54,19.84,20,20,19.88,0.52,-4.88,-2.5,0.21,-1.7,-9.3
20260120,20.1,20.1,20.1,20.1,2000,19.66,19.82,20,20,19.89,3.08,3.08,-1.47,0.43,1.4,-6.51
20260122,19.3,19.3,19.3,19.3,2000,19.52,19.77,19.98,19.98,19.84,-3.98,-3.5,-5.16,0.44,-2.38,-10.23
20260127,19.45,20.05,19.45,20.05,7000,19.67,19.78,19.98,19.98,19.86,3.89,3.89,1.26,1.61,1.35,-6.74
20260209,19.9,19.9,19.9,19.9,12000,19.77,19.79,19.98,19.98,19.87,-0.75,2.58,0.51,2.45,0.57,-7.44
20260225,19.3,19.3,19.1,19.1,7000,19.69,19.73,19.95,19.95,19.8,-4.02,-2.05,-5.68,1.4,-3.19,-11.16
20260302,19.75,19.95,19.75,19.95,5000,19.66,19.76,19.95,19.95,19.81,4.45,-0.75,2.84,1.12,0.97,-7.21
20260303,19.3,19.3,19.15,19.15,3000,19.63,19.74,19.93,19.93,19.76,-4.01,-0.78,-1.79,0.69,-2.99,-10.93
20260304,19.15,19.55,19.15,19.55,2000,19.53,19.72,19.91,19.91,19.74,2.09,-2.49,-1.76,0.45,-0.87,-9.07
20260309,18.1,19,18.1,18.7,14000,19.29,19.66,19.88,19.88,19.65,-4.35,-6.03,-6.73,3.08,-4.86,-13.02
20260310,19.25,19.65,19.15,19.3,14000,19.33,19.62,19.86,19.86,19.62,3.21,1.05,-3.02,2.75,-1.66,-10.23
20260311,19.9,19.9,19.9,19.9,2000,19.32,19.64,19.87,19.87,19.65,3.11,-0.25,1.02,0.39,1.35,-7.44
20260312,19.5,20.05,19.4,20.05,30000,19.5,19.65,19.87,19.87,19.68,0.75,4.7,1.26,4.65,2.05,-6.74
20260313,20.3,20.3,20.3,20.3,2000,19.65,19.66,19.88,19.88,19.73,1.25,3.84,0.99,0.31,3.27,-5.58
20260316,20,20,20,20,1000,19.91,19.68,19.88,19.88,19.76,-1.48,6.95,2.04,0.15,1.64,-6.98
20260323,19.35,19.8,19.25,19.25,6000,19.9,19.61,19.87,19.87,19.71,-3.75,-0.26,-6.1,0.93,-1.86,-10.47
20260324,18.65,20.2,18.65,20.2,5000,19.96,19.65,19.88,19.88,19.75,4.94,1.51,3.59,0.81,2.8,-6.05
20260325,20.25,20.25,19.75,20.25,20000,20,19.66,19.89,19.89,19.8,0.25,1,1.25,2.82,2.99,-5.81
20260326,19.8,19.8,19.8,19.8,2000,19.9,19.69,19.88,19.88,19.8,-2.22,-2.46,2.59,0.29,0.57,-7.91
20260327,20.05,20.05,20.05,20.05,2000,19.91,19.72,19.89,19.89,19.82,1.26,0.25,3.35,0.29,1.67,-6.74
20260330,19.55,19.55,19.55,19.55,2000,19.97,19.72,19.88,19.88,19.79,-2.49,1.56,0.26,0.29,-0.87,-9.07
20260401,19.95,19.95,19.95,19.95,3000,19.92,19.71,19.88,19.88,19.81,2.05,-1.24,-0.75,0.43,1.19,-7.21
20260402,20.15,20.15,20.15,20.15,1000,19.9,19.76,19.89,19.89,19.84,1,-0.49,4.4,0.14,1.99,-6.28
20260407,20.05,20.4,20.05,20.25,120000,19.99,19.77,19.89,19.89,19.87,0.5,2.27,1,9.49,2.44,-5.81
20260408,19.6,19.7,19.6,19.7,5000,19.92,19.76,19.89,19.89,19.86,-2.72,-1.75,-1,0.41,-0.29,-8.37
20260410,19.25,19.4,19.25,19.3,7000,19.87,19.77,19.88,19.88,19.81,-2.03,-1.28,1.05,0.57,-2.37,-10.23
20260413,19.45,19.65,19.45,19.65,2000,19.81,19.75,19.87,19.87,19.8,1.81,-1.5,-1.5,0.16,-0.52,-8.6
20260415,20.15,20.15,20.1,20.1,2000,19.8,19.8,19.88,19.88,19.82,2.29,-0.25,4.96,0.17,1.52,-6.51
20260417,19.85,19.85,19.85,19.85,1000,19.72,19.82,19.88,19.88,19.82,-1.24,-1.98,1.53,0.08,0.18,-7.67
20260420,19.85,19.85,19.85,19.85,1000,19.75,19.87,19.88,19.88,19.83,0,0.76,6.15,0.09,-0.11,-7.67
20260421,19.3,19.3,19.3,19.3,3000,19.75,19.87,19.87,19.87,19.78,-2.77,0,0,0.28,-2.88,-10.23
20260422,19.95,19.95,19.95,19.95,7000,19.81,19.88,19.87,19.87,19.8,3.37,1.53,0.25,0.63,0.38,-7.21
20260424,19.6,19.6,19.6,19.6,1000,19.71,19.85,19.86,19.86,19.78,-1.75,-2.49,-2.24,0.1,-1.27,-8.84
20260427,19.2,19.2,19.2,19.2,1000,19.58,19.8,19.85,19.85,19.73,-2.04,-3.27,-5.42,0.1,-3.02,-10.7
20260428,19.25,19.55,19.25,19.55,3000,19.52,19.77,19.84,19.85,19.72,1.82,-1.51,-2.25,0.31,-1.14,-9.07
20260508,19.1,19.1,19.1,19.1,4000,19.48,19.77,19.82,19.84,19.67,-2.3,-1.04,-0.78,0.42,-3.38,-11.16
20260512,19.2,19.4,19.2,19.4,4000,19.37,19.73,19.8,19.83,19.64,1.57,-2.76,-3.96,0.42,-1.66,-9.77
20260515,19.3,19.3,19.3,19.3,10000,19.31,19.68,19.78,19.82,19.61,-0.52,-1.53,-4.69,1.1,-1.93,-10.23
20260520,19,19,19,19,1000,19.27,19.64,19.74,19.81,19.56,-1.55,-1.04,-4.04,0.11,-3.26,-7.54
20260521,19.6,19.6,19.6,19.6,3000,19.28,19.62,19.73,19.81,19.57,3.16,0.26,-2.24,0.33,-0.09,-4.39
20260522,19.5,19.85,19.5,19.85,20,19.43,19.63,19.73,19.81,19.59,1.28,3.93,1.53,0,1.11,-3.17
20260523,19.5,19.85,19.5,19.85,20,19.52,19.63,19.72,19.81,19.61,0,2.32,-0.5,0,1.13,-3.17
20260524,19.5,19.85,19.5,19.85,20,19.63,19.61,19.71,19.81,19.63,0,2.85,-1.49,0,1.21,-3.17
20260525,20.1,20.1,20.1,20.1,20,19.85,19.61,19.72,19.81,19.67,1.26,5.79,-0.74,0.01,2.52,-1.95
20260526,20.1,20.1,20.1,20.1,20,19.95,19.62,19.72,19.82,19.71,0,2.55,2.03,0.01,2.42,-1.95
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 82.29
- over_600_ratio: 77.63
- over_800_ratio: 77.63
- over_1000_ratio: 74.55
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,82.29,,77.63,,77.63,,74.55,,0,False,False,False,,
20260508,82.29,0,77.63,0,77.63,0,74.55,0,0,False,False,False,,
20260515,82.29,0,77.63,0,77.63,0,74.55,0,0,False,False,False,,
20260522,82.29,0,77.63,0,77.63,0,74.55,0,0,False,False,False,,
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
