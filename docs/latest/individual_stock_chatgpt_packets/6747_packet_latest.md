# INDIVIDUAL STOCK CHATGPT PACKET - 6747 亨泰光

## Metadata
- generated_at: 2026-05-26 02:30:37 Asia/Taipei
- stock_id: 6747
- stock_name: 亨泰光
- packet_status: partial_rawdata_packet
- latest_price_date: 20251126
- price_rows: 17
- latest_tdcc_date: 
- tdcc_rows: 0
- tdcc_history_status: tdcc_missing
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history missing

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6747_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6747_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6747_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6747.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6747.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6747.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6747.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6747.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6747.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6747_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6747_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6747_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20251126
- open: 198.5
- high: 199
- low: 198.5
- close: 199
- volume: 29000
- ma5: 198.7
- ma20: 198.59
- ma60: 198.59
- ma120: 198.59
- ema23: 198.59
- return_5d: 0.25
- return_20d: 
- volume_ratio: 1.09
- distance_to_ma20_pct: 0.21
- distance_to_high_60_pct: 0

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20251103,198.5,198.5,198.5,198.5,46000,,,,,,,,,,,
20251105,198.5,198.5,198.5,198.5,39000,,,,,,0,,,,,
20251106,198.5,199,198.5,199,7000,,,,,,0.25,,,,,
20251107,198.5,199,198.5,198.5,5000,,,,,,-0.25,,,,,
20251110,198.5,198.5,198.5,198.5,89000,198.6,198.6,198.6,198.6,198.53,0,,,2.39,-0.05,-0.25
20251111,198.5,198.5,198.5,198.5,3000,198.6,198.58,198.58,198.58,198.53,0,0,,0.1,-0.04,-0.25
20251112,199,199,198.5,198.5,35000,198.6,198.57,198.57,198.57,198.53,0,0,,1.09,-0.04,-0.25
20251113,198.5,198.5,198.5,198.5,7000,198.5,198.56,198.56,198.56,198.53,0,-0.25,,0.24,-0.03,-0.25
20251114,198.5,198.5,198.5,198.5,20000,198.5,198.56,198.56,198.56,198.52,0,0,,0.72,-0.03,-0.25
20251117,198.5,198.5,198.5,198.5,11000,198.5,198.55,198.55,198.55,198.52,0,0,,0.42,-0.03,-0.25
20251118,198.5,198.5,198.5,198.5,58000,198.5,198.55,198.55,198.55,198.52,0,0,,1.99,-0.02,-0.25
20251119,198.5,198.5,198.5,198.5,37000,198.5,198.54,198.54,198.54,198.52,0,0,,1.24,-0.02,-0.25
20251120,198.5,198.5,198.5,198.5,4000,198.5,198.54,198.54,198.54,198.52,0,0,,0.14,-0.02,-0.25
20251121,198.5,198.5,198.5,198.5,19000,198.5,198.54,198.54,198.54,198.52,0,0,,0.7,-0.02,-0.25
20251124,199,199,198.5,198.5,16000,198.5,198.53,198.53,198.53,198.51,0,0,,0.61,-0.02,-0.25
20251125,198.5,199,198.5,199,29000,198.6,198.56,198.56,198.56,198.56,0.25,0.25,,1.09,0.22,0
20251126,198.5,199,198.5,199,29000,198.7,198.59,198.59,198.59,198.59,0,0.25,,1.09,0.21,0
```

## Latest TDCC Snapshot
- as_of_date: 
- over_400_ratio: 
- over_600_ratio: 
- over_800_ratio: 
- over_1000_ratio: 
- over_400_change_1w: 
- over_800_change_1w: 
- over_1000_change_1w: 
- tdcc_consecutive_up_weeks: 
- all_thresholds_up: 
- high_thresholds_up: 

## TDCC_WINDOW_12W_CSV
```csv
status,no_rows
no_rows,True
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
