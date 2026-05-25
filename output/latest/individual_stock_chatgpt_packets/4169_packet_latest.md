# INDIVIDUAL STOCK CHATGPT PACKET - 4169 泰宗

## Metadata
- generated_at: 2026-05-26 02:29:53 Asia/Taipei
- stock_id: 4169
- stock_name: 泰宗
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 36
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4169_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4169_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4169_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4169.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4169.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4169.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4169.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4169.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4169.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4169_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4169_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4169_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 158
- high: 161
- low: 157
- close: 159
- volume: 134518
- ma5: 158.9
- ma20: 155.47
- ma60: 158.51
- ma120: 158.51
- ema23: 156.34
- return_5d: 0.95
- return_20d: 0.63
- volume_ratio: 0.85
- distance_to_ma20_pct: 2.27
- distance_to_high_60_pct: -12.15

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260408,147,150,135,145,1878735,,,,,,,,,,,
20260409,149.5,170,148,168.5,1198318,,,,,,16.21,,,,,
20260410,168.5,175.5,153.5,157.5,1036110,,,,,,-6.53,,,,,
20260413,151.5,156,148.5,150,600863,,,,,,-4.76,,,,,
20260414,150,154,148.5,150,360523,154.2,154.2,154.2,154.2,148.18,0,,,0.36,-2.72,-14.53
20260415,154.5,156,152,155.5,419389,156.3,154.42,154.42,154.42,148.79,3.67,7.24,,0.46,0.7,-11.4
20260416,157,171,152,167.5,554127,156.1,156.29,156.29,156.29,150.35,7.72,-0.59,,0.64,7.18,-4.56
20260417,169,176,165,166.5,630667,157.9,157.56,157.56,157.56,151.7,-0.6,5.71,,0.76,5.67,-5.4
20260420,170,174,166,169.5,537968,161.8,158.89,158.89,158.89,153.18,1.8,13,,0.67,6.68,-3.69
20260421,170,178,167,176.5,507151,167.1,160.65,160.65,160.65,155.12,4.13,17.67,,0.66,9.87,-0.84
20260422,180.5,181,171.5,172,400831,170.4,161.68,161.68,161.68,156.53,-2.55,10.61,,0.54,6.38,-4.97
20260423,172.5,177.5,169.5,176,438847,172.1,162.88,162.88,162.88,158.15,2.33,5.07,,0.61,8.06,-2.76
20260424,175.5,175.5,166.5,167,358102,172.2,163.19,163.19,163.19,158.89,-5.11,0.3,,0.52,2.33,-7.73
20260427,164,164,157,160,393381,170.3,162.96,162.96,162.96,158.98,-4.19,-5.6,,0.59,-1.82,-11.6
20260428,160,162,157.5,157.5,160782,166.5,162.6,162.6,162.6,158.86,-1.56,-10.76,,0.25,-3.14,-12.98
20260429,157.5,163.5,156.5,158,176959,163.7,162.31,162.31,162.31,158.79,0.32,-8.14,,0.29,-2.66,-12.71
20260430,158,162.5,156,161.5,148288,160.8,162.26,162.26,162.26,159.01,2.22,-8.24,,0.26,-0.47,-10.77
20260504,162,164,158.5,159.5,170233,159.3,162.11,162.11,162.11,159.05,-1.24,-4.49,,0.31,-1.61,-11.88
20260505,159,163,156.5,160,127252,159.3,162,162,162,159.13,0.31,0,,0.24,-1.23,-11.6
20260506,158.5,159.5,155,155,285504,158.8,161.65,161.65,161.65,158.79,-3.12,-1.59,,0.55,-4.11,-14.36
20260507,156.5,156.5,152.5,153,248635,157.8,162.05,161.24,161.24,158.31,-1.29,-3.16,5.52,0.57,-5.58,-15.47
20260508,154,160,153.5,156,172403,156.7,161.43,161,161,158.11,1.96,-3.41,-7.42,0.45,-3.36,-13.81
20260511,156,156.5,153,154,97623,155.6,161.25,160.7,160.7,157.77,-1.28,-3.45,-2.22,0.29,-4.5,-14.92
20260512,154,159,152,155.5,114977,154.7,161.53,160.48,160.48,157.58,0.97,-2.81,3.67,0.36,-3.73,-14.09
20260513,159,159,152,152,126202,154.1,161.62,160.14,160.14,157.12,-2.25,-1.94,1.33,0.42,-5.96,-16.02
20260514,152,153,149.5,150,194113,153.5,161.35,159.75,159.75,156.52,-1.32,-1.96,-3.54,0.66,-7.03,-17.13
20260515,155,155,148,148.5,139789,152,160.4,159.33,159.33,155.85,-1,-4.81,-11.34,0.51,-7.42,-17.96
20260518,148.5,153.5,148,150.5,154308,151.3,159.6,159.02,159.02,155.41,1.35,-2.27,-9.61,0.62,-5.7,-16.85
20260519,153.5,154.5,150,150,123199,150.2,158.62,158.71,158.71,154.96,-0.33,-3.54,-11.5,0.54,-5.44,-17.13
20260520,150,152,148.5,152,91421,150.2,157.4,158.48,158.48,154.71,1.33,0,-13.88,0.44,-3.43,-16.02
20260521,152,162,152,157.5,216382,151.7,156.68,158.45,158.45,154.94,3.62,5,-8.43,1.1,0.53,-12.98
20260522,158,161,157,159,134518,153.8,155.82,158.47,158.47,155.28,0.95,7.07,-9.66,0.74,2.04,-12.15
20260523,158,161,157,159,134518,155.5,155.43,158.48,158.48,155.59,0,5.65,-4.79,0.79,2.3,-12.15
20260524,158,161,157,159,134518,157.3,155.38,158.5,158.5,155.88,0,6,-0.62,0.85,2.33,-12.15
20260525,156,159,152,158.5,217243,158.6,155.43,158.5,158.5,156.09,-0.31,4.28,0.63,1.35,1.98,-12.43
20260526,158,161,157,159,134518,158.9,155.47,158.51,158.51,156.34,0.32,0.95,0.63,0.85,2.27,-12.15
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.72
- over_600_ratio: 49.58
- over_800_ratio: 46.18
- over_1000_ratio: 46.18
- over_400_change_1w: 0.38
- over_800_change_1w: -1.42
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,54.72,,50.19,,47.98,,47.98,,0,False,False,False,,
20260508,54.49,-0.23,49.96,-0.23,47.75,-0.23,46.29,-1.69,0,False,False,False,,
20260515,54.34,-0.15,49.81,-0.15,47.6,-0.15,46.27,-0.02,0,False,False,False,,
20260522,54.72,0.38,49.58,-0.23,46.18,-1.42,46.18,-0.09,1,False,False,False,,
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
