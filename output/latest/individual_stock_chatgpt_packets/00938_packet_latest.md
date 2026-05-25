# INDIVIDUAL STOCK CHATGPT PACKET - 00938 凱基優選30

## Metadata
- generated_at: 2026-05-26 02:28:47 Asia/Taipei
- stock_id: 00938
- stock_name: 凱基優選30
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 5
- latest_tdcc_date: 
- tdcc_rows: 0
- tdcc_history_status: tdcc_missing
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history missing

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/00938_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/00938_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/00938_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/00938.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/00938.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/00938.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/00938.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/00938.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/00938.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/00938_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/00938_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/00938_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 20.87
- high: 20.99
- low: 20.87
- close: 20.99
- volume: 1757030
- ma5: 21.03
- ma20: 21.03
- ma60: 21.03
- ma120: 21.03
- ema23: 21.01
- return_5d: 
- return_20d: 
- volume_ratio: 1.09
- distance_to_ma20_pct: -0.21
- distance_to_high_60_pct: -1.46

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260522,20.87,20.99,20.87,20.99,1757030,,,,,,,,,,,
20260523,20.87,20.99,20.87,20.99,1757030,,,,,,0,,,,,
20260524,20.87,20.99,20.87,20.99,1757030,,,,,,0,,,,,
20260525,21.1,21.3,21.1,21.21,1066799,,,,,,1.05,,,,,
20260526,20.87,20.99,20.87,20.99,1757030,21.03,21.03,21.03,21.03,21.01,-1.04,,,1.09,-0.21,-1.46
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
