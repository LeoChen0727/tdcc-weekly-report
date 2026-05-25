# INDIVIDUAL STOCK CHATGPT PACKET - 6236 中湛

## Metadata
- generated_at: 2026-05-26 02:30:23 Asia/Taipei
- stock_id: 6236
- stock_name: 中湛
- packet_status: partial_rawdata_packet
- latest_price_date: 20260521
- price_rows: 33
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6236_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6236_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6236_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6236.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6236.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6236.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6236.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6236.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6236.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6236_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6236_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6236_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260521
- open: 20
- high: 20
- low: 20
- close: 20
- volume: 1000
- ma5: 19.53
- ma20: 25.08
- ma60: 24.46
- ma120: 24.46
- ema23: 23.93
- return_5d: -16.67
- return_20d: -21.88
- volume_ratio: 0.67
- distance_to_ma20_pct: -20.25
- distance_to_high_60_pct: -31.74

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20251103,29.3,29.3,29.3,29.3,1000,,,,,,,,,,,
20251226,21.75,21.75,21.75,21.75,1000,,,,,,-25.77,,,,,
20251229,19.6,19.6,19.6,19.6,5000,,,,,,-9.89,,,,,
20251230,21.55,21.55,21.55,21.55,1000,,,,,,9.95,,,,,
20260112,19.4,21.55,19.4,21.55,2000,22.75,22.75,22.75,22.75,26.9,0,,,1,-5.27,-26.45
20260113,22.2,22.2,22.2,22.2,1000,21.33,22.66,22.66,22.66,26.51,3.02,-24.23,,0.55,-2.02,-24.23
20260114,22.4,22.4,22.3,22.3,2000,21.44,22.61,22.61,22.61,26.16,0.45,2.53,,1.08,-1.36,-23.89
20260115,23,23,23,23,1000,22.12,22.66,22.66,22.66,25.89,3.14,17.35,,0.57,1.52,-21.5
20260116,23.7,23.7,23.7,23.7,1000,22.55,22.77,22.77,22.77,25.71,3.04,9.98,,0.6,4.07,-19.11
20260119,24.4,24.4,24.4,24.4,1000,23.12,22.93,22.93,22.93,25.6,2.95,13.23,,0.62,6.39,-16.72
20260120,25.15,25.15,25.15,25.15,1000,23.71,23.14,23.14,23.14,25.56,3.07,13.29,,0.65,8.7,-14.16
20260121,25.6,25.6,25.6,25.6,1000,24.37,23.34,23.34,23.34,25.57,1.79,14.8,,0.67,9.68,-12.63
20260122,25.6,25.6,25.6,25.6,1000,24.89,23.52,23.52,23.52,25.57,0,11.3,,0.68,8.86,-12.63
20260123,25.55,25.55,25.55,25.55,1000,25.26,23.66,23.66,23.66,25.57,-0.2,7.81,,0.7,7.98,-12.8
20260126,26.35,26.35,26.35,26.35,1000,25.65,23.84,23.84,23.84,25.63,3.13,7.99,,0.71,10.53,-10.07
20260127,26.95,26.95,26.95,26.95,1000,26.01,24.03,24.03,24.03,25.74,2.28,7.16,,0.73,12.13,-8.02
20260128,27.8,27.8,27.8,27.8,1000,26.45,24.26,24.26,24.26,25.91,3.15,8.59,,0.74,14.61,-5.12
20260129,27.9,27.9,27.9,27.9,1000,26.91,24.46,24.46,24.46,26.08,0.36,8.98,,0.75,14.07,-4.78
20260130,28.45,28.45,28.45,28.45,1000,27.49,24.67,24.67,24.67,26.28,1.97,11.35,,0.76,15.33,-2.9
20260202,28.4,28.4,28.4,28.4,1000,27.9,24.86,24.86,24.86,26.45,-0.18,7.78,,0.77,14.26,-3.07
20260203,28.35,28.35,28.35,28.35,1000,28.18,24.81,25.02,25.02,26.61,-0.18,5.19,-3.24,0.77,14.28,-3.24
20260204,28.25,28.25,28.25,28.25,1000,28.27,25.13,25.17,25.17,26.75,-0.35,1.62,29.89,0.77,12.4,-3.58
20260205,25.45,27.05,25.45,27.05,4000,28.1,25.5,25.25,25.25,26.77,-4.25,-3.05,38.01,3.2,6.06,-7.68
20260206,27.75,27.75,27.75,27.75,1000,27.96,25.82,25.35,25.35,26.86,2.59,-2.46,28.77,0.8,7.5,-5.29
20260209,27.7,27.7,27.7,27.7,1000,27.82,26.12,25.45,25.45,26.93,-0.18,-2.46,28.54,0.83,6.04,-5.46
20260210,28.55,28.55,24.95,26,3000,27.35,26.31,25.47,25.47,26.85,-6.14,-8.29,17.12,2.31,-1.19,-11.26
20260211,23.4,23.4,23.4,23.4,4000,26.38,26.37,25.39,25.39,26.56,-10,-17.17,4.93,2.86,-11.25,-20.14
20260224,24,24,24,24,1000,25.77,26.42,25.34,25.34,26.35,2.56,-11.28,4.35,0.71,-9.15,-18.09
20260226,22.7,22.7,21.6,21.6,3000,24.54,26.31,25.21,25.21,25.95,-10,-22.16,-8.86,2,-17.91,-26.28
20260414,18,18,18,18,1000,22.6,25.99,24.97,24.97,25.29,-16.67,-35.02,-26.23,0.67,-30.75,-38.57
20260421,19,19,19,19,1000,21.2,25.68,24.78,24.78,24.77,5.56,-26.92,-24.45,0.67,-26.03,-35.15
20260422,19.05,19.05,19.05,19.05,1000,20.33,25.36,24.6,24.6,24.29,0.26,-18.59,-25.59,0.67,-24.87,-34.98
20260521,20,20,20,20,1000,19.53,25.08,24.46,24.46,23.93,4.99,-16.67,-21.88,0.67,-20.25,-31.74
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 92.64
- over_600_ratio: 91.48
- over_800_ratio: 87.98
- over_1000_ratio: 87.98
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,92.64,,91.48,,87.98,,87.98,,0,False,False,False,,
20260508,92.64,0,91.48,0,87.98,0,87.98,0,0,False,False,False,,
20260515,92.64,0,91.48,0,87.98,0,87.98,0,0,False,False,False,,
20260522,92.64,0,91.48,0,87.98,0,87.98,0,0,False,False,False,,
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
