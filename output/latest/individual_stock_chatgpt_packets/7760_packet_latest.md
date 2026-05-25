# INDIVIDUAL STOCK CHATGPT PACKET - 7760 享溫馨

## Metadata
- generated_at: 2026-05-26 02:30:47 Asia/Taipei
- stock_id: 7760
- stock_name: 享溫馨
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 22
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7760_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7760_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7760_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7760.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7760.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7760.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7760.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7760.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7760.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7760_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7760_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7760_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 33.55
- high: 33.55
- low: 33.4
- close: 33.4
- volume: 81002
- ma5: 33.38
- ma20: 34.06
- ma60: 34.18
- ma120: 34.18
- ema23: 34.16
- return_5d: -0.15
- return_20d: -4.57
- volume_ratio: 0.52
- distance_to_ma20_pct: -1.95
- distance_to_high_60_pct: -6.7

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260428,35.6,35.8,34.5,35.8,925663,,,,,,,,,,,
20260429,35,35.6,34.85,35,466437,,,,,,-2.23,,,,,
20260430,35,35.05,33.1,35.05,365191,,,,,,0.14,,,,,
20260504,35.05,35.1,34.5,35.05,153706,,,,,,0,,,,,
20260505,34.25,35,34.25,35,117692,35.18,35.18,35.18,35.18,35.57,-0.14,,,0.29,-0.51,-2.23
20260506,34.75,34.75,33.8,33.8,288898,34.78,34.95,34.95,34.95,35.42,-3.43,-5.59,,0.75,-3.29,-5.59
20260507,33.5,34.4,33.5,34.4,208737,34.66,34.87,34.87,34.87,35.34,1.78,-1.71,,0.58,-1.35,-3.91
20260508,34,35.1,34,34.5,240533,34.55,34.83,34.83,34.83,35.27,0.29,-1.57,,0.7,-0.93,-3.63
20260511,34.5,34.5,34.2,34.3,125737,34.4,34.77,34.77,34.77,35.19,-0.58,-2.14,,0.39,-1.34,-4.19
20260512,34.3,34.6,34.2,34.3,162067,34.26,34.72,34.72,34.72,35.11,0,-2,,0.53,-1.21,-4.19
20260513,34.2,34.2,33.55,34.1,89417,34.32,34.66,34.66,34.66,35.03,-0.58,0.89,,0.31,-1.63,-4.75
20260514,34,34.2,33.85,34.2,56794,34.28,34.62,34.62,34.62,34.96,0.29,-0.58,,0.21,-1.23,-4.47
20260515,34.15,34.25,33.75,34.25,107080,34.23,34.6,34.6,34.6,34.9,0.15,-0.72,,0.42,-1,-4.33
20260518,34.2,34.25,34.1,34.25,63098,34.22,34.57,34.57,34.57,34.85,0,-0.15,,0.26,-0.93,-4.33
20260519,33.95,34.1,33.95,34.05,34776,34.17,34.54,34.54,34.54,34.78,-0.58,-0.73,,0.15,-1.41,-4.89
20260520,34.05,34.05,33.5,33.65,180724,34.08,34.48,34.48,34.48,34.69,-1.17,-1.32,,0.81,-2.41,-6.01
20260521,33.15,33.85,33.15,33.45,132586,33.93,34.42,34.42,34.42,34.58,-0.59,-2.19,,0.61,-2.82,-6.56
20260522,33.55,33.55,33.4,33.4,81002,33.76,34.36,34.36,34.36,34.48,-0.15,-2.48,,0.38,-2.8,-6.7
20260523,33.55,33.55,33.4,33.4,81002,33.59,34.31,34.31,34.31,34.39,0,-2.48,,0.4,-2.66,-6.7
20260524,33.55,33.55,33.4,33.4,81002,33.46,34.27,34.27,34.27,34.31,0,-1.91,,0.41,-2.53,-6.7
20260525,33.3,33.5,32.75,33.3,486321,33.39,34.14,34.22,34.22,34.23,-0.3,-1.04,-6.98,2.76,-2.47,-6.98
20260526,33.55,33.55,33.4,33.4,81002,33.38,34.06,34.18,34.18,34.16,0.3,-0.15,-4.57,0.52,-1.95,-6.7
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 59.56
- over_600_ratio: 48.88
- over_800_ratio: 44.84
- over_1000_ratio: 42.31
- over_400_change_1w: -0.41
- over_800_change_1w: 0.4
- over_1000_change_1w: 0.41
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,58.89,,48.22,,44.1,,41.41,,0,False,False,False,,
20260508,59.2,0.31,48.48,0.26,44.43,0.33,41.74,0.33,1,True,True,True,,
20260515,59.97,0.77,49.4,0.92,44.44,0.01,41.9,0.16,2,True,True,True,,
20260522,59.56,-0.41,48.88,-0.52,44.84,0.4,42.31,0.41,3,False,True,False,,
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
