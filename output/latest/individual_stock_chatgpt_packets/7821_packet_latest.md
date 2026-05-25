# INDIVIDUAL STOCK CHATGPT PACKET - 7821 神數

## Metadata
- generated_at: 2026-05-26 02:30:49 Asia/Taipei
- stock_id: 7821
- stock_name: 神數
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 28
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7821_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7821_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7821_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7821.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7821.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7821.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7821.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7821.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7821.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7821_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7821_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7821_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 44
- high: 44.6
- low: 43.9
- close: 44.4
- volume: 232610
- ma5: 44.44
- ma20: 44.86
- ma60: 45.57
- ma120: 45.57
- ema23: 45.34
- return_5d: 1.14
- return_20d: -7.5
- volume_ratio: 0.83
- distance_to_ma20_pct: -1.02
- distance_to_high_60_pct: -15.75

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260420,52.6,52.7,48,51.8,3781921,,,,,,,,,,,
20260421,51,51,48.5,49.25,2054591,,,,,,-4.92,,,,,
20260422,49.25,50.2,49,49.15,785792,,,,,,-0.2,,,,,
20260423,49.45,49.45,43,45.85,1186804,,,,,,-6.71,,,,,
20260424,45.85,46.1,43.75,43.9,746709,47.99,47.99,47.99,47.99,50.34,-4.25,,,0.44,-8.52,-16.7
20260427,44.1,44.6,42.9,43.25,497215,46.28,47.2,47.2,47.2,49.75,-1.48,-16.51,,0.33,-8.37,-17.93
20260428,43,47.55,43,47.55,666630,45.94,47.25,47.25,47.25,49.56,9.94,-3.45,,0.48,0.63,-9.77
20260429,47.8,49.25,47.6,48,885760,45.71,47.34,47.34,47.34,49.43,0.95,-2.34,,0.67,1.39,-8.92
20260430,48.1,48.75,46.5,47.7,572314,46.08,47.38,47.38,47.38,49.29,-0.62,4.03,,0.46,0.67,-9.49
20260504,48,48.3,47.05,47.3,442291,46.76,47.38,47.38,47.38,49.12,-0.84,7.74,,0.38,-0.16,-10.25
20260505,47.3,48,47,47.25,405103,47.56,47.36,47.36,47.36,48.97,-0.11,9.25,,0.37,-0.24,-10.34
20260506,47.6,47.6,46.45,46.65,481242,47.38,47.3,47.3,47.3,48.77,-1.27,-1.89,,0.46,-1.38,-11.48
20260507,46.15,46.4,46,46.05,351723,46.99,47.21,47.21,47.21,48.55,-1.29,-4.06,,0.36,-2.45,-12.62
20260508,46.4,46.55,45,45.45,221168,46.54,47.08,47.08,47.08,48.29,-1.3,-4.72,,0.24,-3.47,-13.76
20260511,45.4,45.4,44.5,44.85,226386,46.05,46.93,46.93,46.93,48,-1.32,-5.18,,0.26,-4.44,-14.9
20260512,44.85,45.65,44.2,44.5,275157,45.5,46.78,46.78,46.78,47.71,-0.78,-5.82,,0.32,-4.88,-15.56
20260513,44.5,45,43.9,44.15,227452,45,46.63,46.63,46.63,47.41,-0.79,-5.36,,0.28,-5.31,-16.22
20260514,44.35,44.4,43.35,43.6,299121,44.51,46.46,46.46,46.46,47.1,-1.25,-5.32,,0.38,-6.15,-17.27
20260515,43.65,44.25,43.5,43.5,273508,44.12,46.3,46.3,46.3,46.8,-0.23,-4.29,,0.36,-6.05,-17.46
20260518,43.5,43.5,42.7,43.1,206756,43.77,46.14,46.14,46.14,46.49,-0.92,-3.9,,0.28,-6.59,-18.22
20260519,43.1,44.4,43.1,43.4,154217,43.55,45.72,46.01,46.01,46.23,0.7,-2.47,-16.22,0.28,-5.08,-17.65
20260520,43.6,43.9,43.2,43.55,97944,43.43,45.44,45.9,45.9,46.01,0.35,-1.36,-11.57,0.22,-4.15,-17.36
20260521,43.6,44.2,43.45,43.9,191820,43.49,45.17,45.81,45.81,45.83,0.8,0.69,-10.68,0.46,-2.82,-16.7
20260522,44,44.6,43.9,44.4,232610,43.67,45.1,45.75,45.75,45.71,1.14,2.07,-3.16,0.62,-1.56,-15.75
20260523,44,44.6,43.9,44.4,232610,43.93,45.13,45.7,45.7,45.6,0,3.02,1.14,0.67,-1.61,-15.75
20260524,44,44.6,43.9,44.4,232610,44.13,45.19,45.65,45.65,45.5,0,2.3,2.66,0.7,-1.74,-15.75
20260525,44.4,44.6,43.8,44.6,252390,44.34,45.04,45.61,45.61,45.43,0.45,2.41,-6.2,0.81,-0.97,-15.37
20260526,44,44.6,43.9,44.4,232610,44.44,44.86,45.57,45.57,45.34,-0.45,1.14,-7.5,0.83,-1.02,-15.75
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 81.58
- over_600_ratio: 79.38
- over_800_ratio: 77.55
- over_1000_ratio: 75.97
- over_400_change_1w: -0.71
- over_800_change_1w: -1.2
- over_1000_change_1w: -0.44
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,83.03,,80.76,,78.86,,76.52,,0,False,False,False,,
20260508,82.82,-0.21,80.09,-0.67,78.82,-0.04,76.48,-0.04,0,False,False,False,,
20260515,82.29,-0.53,80.02,-0.07,78.75,-0.07,76.41,-0.07,0,False,False,False,,
20260522,81.58,-0.71,79.38,-0.64,77.55,-1.2,75.97,-0.44,0,False,False,False,,
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
