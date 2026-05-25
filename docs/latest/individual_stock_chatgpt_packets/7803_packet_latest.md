# INDIVIDUAL STOCK CHATGPT PACKET - 7803 雲象科技-創

## Metadata
- generated_at: 2026-05-26 02:30:48 Asia/Taipei
- stock_id: 7803
- stock_name: 雲象科技-創
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 7
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7803_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7803_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7803_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7803.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7803.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7803.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7803.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7803.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7803.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7803_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7803_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7803_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 23
- high: 23.95
- low: 22.95
- close: 23.9
- volume: 518300
- ma5: 24.17
- ma20: 23.8
- ma60: 23.8
- ma120: 23.8
- ema23: 23.38
- return_5d: 4.82
- return_20d: 
- volume_ratio: 0.8
- distance_to_ma20_pct: 0.42
- distance_to_high_60_pct: -12.45

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260520,22.25,24.3,20,22.95,920496,,,,,,,,,,,
20260521,22.2,23.45,22.05,22.8,448396,,,,,,-0.65,,,,,
20260522,23,23.95,22.95,23.9,518300,,,,,,4.82,,,,,
20260523,23,23.95,22.95,23.9,518300,,,,,,0,,,,,
20260524,23,23.95,22.95,23.9,518300,23.49,23.49,23.49,23.49,23.16,0,,,0.89,1.75,-1.65
20260525,25,27.3,25,25.25,1106004,23.95,23.78,23.78,23.78,23.33,5.65,10.02,,1.65,6.17,-7.51
20260526,23,23.95,22.95,23.9,518300,24.17,23.8,23.8,23.8,23.38,-5.35,4.82,,0.8,0.42,-12.45
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 80.47
- over_600_ratio: 75.5
- over_800_ratio: 73.97
- over_1000_ratio: 71.96
- over_400_change_1w: -4.66
- over_800_change_1w: -4.7
- over_1000_change_1w: -4.58
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,85.48,,80.57,,78.92,,76.79,,0,False,False,False,,
20260508,85.31,-0.17,80.44,-0.13,78.8,-0.12,76.67,-0.12,0,False,False,False,,
20260515,85.13,-0.18,80.3,-0.14,78.67,-0.13,76.54,-0.13,0,False,False,False,,
20260522,80.47,-4.66,75.5,-4.8,73.97,-4.7,71.96,-4.58,0,False,False,False,,
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
