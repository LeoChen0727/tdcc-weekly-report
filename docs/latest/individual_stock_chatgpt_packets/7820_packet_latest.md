# INDIVIDUAL STOCK CHATGPT PACKET - 7820 立盈

## Metadata
- generated_at: 2026-05-26 02:30:49 Asia/Taipei
- stock_id: 7820
- stock_name: 立盈
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 23
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7820_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7820_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7820_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7820.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7820.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7820.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7820.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7820.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7820.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7820_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7820_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7820_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 134
- high: 139.5
- low: 134
- close: 136
- volume: 137
- ma5: 134.8
- ma20: 139.53
- ma60: 139.98
- ma120: 139.98
- ema23: 138.62
- return_5d: 0.74
- return_20d: -2.86
- volume_ratio: 0
- distance_to_ma20_pct: -2.53
- distance_to_high_60_pct: -15

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260427,150,160,130,144,1103000,,,,,,,,,,,
20260428,133,154.5,130,145,519000,,,,,,0.69,,,,,
20260429,145,145,139,140,170000,,,,,,-3.45,,,,,
20260430,140,145,139,139.5,114000,,,,,,-0.36,,,,,
20260504,144,154.5,144,152,528000,144.1,144.1,144.1,144.1,144.11,8.96,,,1.08,5.48,-5
20260505,150,151,145.5,148.5,219000,145,144.83,144.83,144.83,144.47,-2.3,3.12,,0.5,2.53,-7.19
20260506,150,150,140.5,143,209000,144.6,144.57,144.57,144.57,144.35,-3.7,-1.38,,0.51,-1.09,-10.62
20260507,143,143.5,138.5,142,170000,145,144.25,144.25,144.25,144.15,-0.7,1.43,,0.45,-1.56,-11.25
20260508,142,142.5,139,141,114000,145.3,143.89,143.89,143.89,143.89,-0.7,1.08,,0.33,-2.01,-11.88
20260511,155,155,147.5,150,307000,144.9,144.5,144.5,144.5,144.4,6.38,-1.32,,0.89,3.81,-6.25
20260512,150,150.5,146,146,109000,144.4,144.64,144.64,144.64,144.53,-2.67,-1.68,,0.34,0.94,-8.75
20260513,146,146,140,141,113000,144,144.33,144.33,144.33,144.24,-3.42,-1.4,,0.37,-2.31,-11.88
20260514,142,143,138,139.5,145000,143.5,143.96,143.96,143.96,143.84,-1.06,-1.76,,0.49,-3.1,-12.81
20260515,138,143.5,133.5,134,116000,142.1,143.25,143.25,143.25,143.02,-3.94,-4.96,,0.41,-6.46,-16.25
20260518,134,138.5,134,137.5,49000,139.6,142.87,142.87,142.87,142.56,2.61,-8.33,,0.18,-3.76,-14.06
20260519,137.5,137.5,132.5,133.5,39000,137.1,142.28,142.28,142.28,141.81,-2.91,-8.56,,0.16,-6.17,-16.56
20260520,133,134,132,134,42000,135.7,141.79,141.79,141.79,141.16,0.37,-4.96,,0.18,-5.5,-16.25
20260521,134.5,135,134,135,29000,134.8,141.42,141.42,141.42,140.64,0.75,-3.23,,0.13,-4.54,-15.62
20260522,135.5,135.5,132.5,134,134,134.8,141.03,141.03,141.03,140.09,-0.74,0,,0,-4.98,-16.25
20260523,135.5,135.5,132.5,134,134,134.1,140.68,140.68,140.68,139.58,0,-2.55,,0,-4.75,-16.25
20260524,135.5,135.5,132.5,134,134,134.2,140.18,140.36,140.36,139.12,0,0.37,-6.94,0,-4.41,-16.25
20260525,134,139.5,134,136,137,134.6,139.72,140.16,140.16,138.86,1.49,1.49,-6.21,0,-2.67,-15
20260526,134,139.5,134,136,137,134.8,139.53,139.98,139.98,138.62,0,0.74,-2.86,0,-2.53,-15
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 75.09
- over_600_ratio: 75.09
- over_800_ratio: 67.51
- over_1000_ratio: 65.32
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,75.09,,75.09,,67.51,,65.32,,0,False,False,False,,
20260508,75.09,0,75.09,0,67.51,0,65.32,0,0,False,False,False,,
20260515,75.09,0,75.09,0,67.51,0,65.32,0,0,False,False,False,,
20260522,75.09,0,75.09,0,67.51,0,65.32,0,0,False,False,False,,
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
