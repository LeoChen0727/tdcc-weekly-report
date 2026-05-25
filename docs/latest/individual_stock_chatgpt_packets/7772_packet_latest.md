# INDIVIDUAL STOCK CHATGPT PACKET - 7772 耀穎

## Metadata
- generated_at: 2026-05-26 02:30:48 Asia/Taipei
- stock_id: 7772
- stock_name: 耀穎
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 15
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7772_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7772_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7772_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7772.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7772.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7772.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7772.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7772.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7772.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7772_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7772_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7772_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 175
- high: 178.5
- low: 168
- close: 170.5
- volume: 173
- ma5: 167.5
- ma20: 165.83
- ma60: 165.83
- ma120: 165.83
- ema23: 173.23
- return_5d: 13.29
- return_20d: 
- volume_ratio: 0
- distance_to_ma20_pct: 2.81
- distance_to_high_60_pct: -18.42

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260508,196,196.5,179,196.5,1271000,,,,,,,,,,,
20260511,198.5,209,186,186.5,894000,,,,,,-5.09,,,,,
20260512,190,192,173,175,688000,,,,,,-6.17,,,,,
20260513,168,169.5,161.5,164.5,427000,,,,,,-6,,,,,
20260514,166.5,181,166.5,170,434000,178.5,178.5,178.5,178.5,189.7,3.34,,,0.58,-4.76,-18.66
20260515,167,172.5,153,155,637000,170.2,174.58,174.58,174.58,186.81,-8.82,-21.12,,0.88,-11.22,-25.84
20260518,153,153,139.5,144,505000,161.7,170.21,170.21,170.21,183.24,-7.1,-22.79,,0.73,-15.4,-31.1
20260519,145.5,158,142,158,501000,158.3,168.69,168.69,168.69,181.14,9.72,-9.71,,0.75,-6.34,-24.4
20260520,163,165,148,150,437000,155.4,166.61,166.61,166.61,178.54,-5.06,-8.81,,0.68,-9.97,-28.23
20260521,151,156.5,150,150.5,205000,151.5,165,165,165,176.21,0.33,-11.47,,0.34,-8.79,-27.99
20260522,155,165.5,151.5,165.5,159,153.6,165.05,165.05,165.05,175.31,9.97,6.77,,0,0.28,-20.81
20260523,155,165.5,151.5,165.5,159,157.9,165.08,165.08,165.08,174.5,0,14.93,,0,0.25,-20.81
20260524,155,165.5,151.5,165.5,159,159.4,165.12,165.12,165.12,173.75,0,4.75,,0,0.23,-20.81
20260525,175,178.5,168,170.5,173,163.5,165.5,165.5,165.5,173.48,3.02,13.67,,0,3.02,-18.42
20260526,175,178.5,168,170.5,173,167.5,165.83,165.83,165.83,173.23,0,13.29,,0,2.81,-18.42
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 56.09
- over_600_ratio: 52.82
- over_800_ratio: 52.82
- over_1000_ratio: 52.82
- over_400_change_1w: -1.52
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,63.8,,58.13,,58.13,,58.13,,0,False,False,False,,
20260508,57.78,-6.02,52.82,-5.31,52.82,-5.31,52.82,-5.31,0,False,False,False,,
20260515,57.61,-0.17,52.82,0,52.82,0,52.82,0,0,False,False,False,,
20260522,56.09,-1.52,52.82,0,52.82,0,52.82,0,0,False,False,False,,
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
