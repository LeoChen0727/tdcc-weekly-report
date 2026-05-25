# INDIVIDUAL STOCK CHATGPT PACKET - 4178 永笙-KY

## Metadata
- generated_at: 2026-05-26 02:29:53 Asia/Taipei
- stock_id: 4178
- stock_name: 永笙-KY
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 20
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4178_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4178_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4178_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4178.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4178.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4178.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4178.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4178.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4178.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4178_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4178_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4178_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 19
- high: 19
- low: 18.8
- close: 18.95
- volume: 354843
- ma5: 18.94
- ma20: 19
- ma60: 19
- ma120: 19
- ema23: 19
- return_5d: -0.26
- return_20d: 
- volume_ratio: 0.32
- distance_to_ma20_pct: -0.26
- distance_to_high_60_pct: -1.81

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260430,18.9,19.3,18,19.1,8215510,,,,,,,,,,,
20260504,18.95,19.2,18.65,19.1,2152179,,,,,,0,,,,,
20260505,19.1,19.1,18.8,19.05,1030659,,,,,,-0.26,,,,,
20260506,19.15,19.15,18.75,19,1167523,,,,,,-0.26,,,,,
20260507,19.1,19.1,18.8,19,867525,19.05,19.05,19.05,19.05,19.08,0,,,0.32,-0.26,-1.55
20260508,19,19.1,18.7,19,1492221,19.03,19.04,19.04,19.04,19.07,0,-0.52,,0.6,-0.22,-1.55
20260511,19,19.05,18.9,19,695168,19.01,19.04,19.04,19.04,19.07,0,-0.52,,0.31,-0.19,-1.55
20260512,19,19.1,18.95,19.05,565464,19.01,19.04,19.04,19.04,19.07,0.26,0,,0.28,0.07,-1.3
20260513,19,19.1,18.95,19.05,553368,19.02,19.04,19.04,19.04,19.06,0,0.26,,0.3,0.06,-1.3
20260514,19,19.1,18.8,19,593525,19.02,19.04,19.04,19.04,19.06,-0.26,0,,0.34,-0.18,-1.55
20260515,19,19,18.8,19,429546,19.02,19.03,19.03,19.03,19.05,0,0,,0.27,-0.17,-1.55
20260518,18.8,19,18.8,18.95,383470,19.01,19.02,19.02,19.02,19.05,-0.26,-0.26,,0.25,-0.39,-1.81
20260519,19,19,18.85,19,490811,19,19.02,19.02,19.02,19.04,0.26,-0.26,,0.34,-0.12,-1.55
20260520,18.95,19.05,18.9,19,387286,18.99,19.02,19.02,19.02,19.04,0,-0.26,,0.28,-0.11,-1.55
20260521,19,19.15,18.95,19,432922,18.99,19.02,19.02,19.02,19.04,0,0,,0.33,-0.11,-1.55
20260522,19,19,18.8,18.95,354843,18.98,19.02,19.02,19.02,19.03,-0.26,-0.26,,0.29,-0.35,-1.81
20260523,19,19,18.8,18.95,354843,18.98,19.01,19.01,19.01,19.02,0,0,,0.3,-0.32,-1.81
20260524,19,19,18.8,18.95,354843,18.97,19.01,19.01,19.01,19.02,0,-0.26,,0.31,-0.31,-1.81
20260525,18.95,18.95,18.6,18.9,1348005,18.95,19,19,19,19.01,-0.26,-0.53,,1.17,-0.54,-2.07
20260526,19,19,18.8,18.95,354843,18.94,19,19,19,19,0.26,-0.26,,0.32,-0.26,-1.81
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 77.03
- over_600_ratio: 74.72
- over_800_ratio: 71.77
- over_1000_ratio: 71.37
- over_400_change_1w: 0.15
- over_800_change_1w: 0.36
- over_1000_change_1w: 0.36
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,75.62,,72.61,,69.29,,68.89,,0,False,False,False,,
20260508,76.38,0.76,73.8,1.19,70.85,1.56,70.45,1.56,1,True,True,True,,
20260515,76.88,0.5,74.36,0.56,71.41,0.56,71.01,0.56,2,True,True,True,,
20260522,77.03,0.15,74.72,0.36,71.77,0.36,71.37,0.36,3,True,True,True,,
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
