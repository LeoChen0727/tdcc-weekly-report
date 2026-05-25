# INDIVIDUAL STOCK CHATGPT PACKET - 2072 世紀風電

## Metadata
- generated_at: 2026-05-26 02:29:06 Asia/Taipei
- stock_id: 2072
- stock_name: 世紀風電
- packet_status: partial_rawdata_packet
- latest_price_date: 20260526
- price_rows: 43
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2072_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2072_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2072_packet_latest.md?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2072.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2072.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2072.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2072.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2072.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2072.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2072_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2072_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2072_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 172.5
- high: 172.5
- low: 168.5
- close: 169
- volume: 443434
- ma5: 168.7
- ma20: 174.93
- ma60: 178.02
- ma120: 178.02
- ema23: 174.17
- return_5d: -2.03
- return_20d: -6.63
- volume_ratio: 0.75
- distance_to_ma20_pct: -3.39
- distance_to_high_60_pct: -15.5

## PRICE_WINDOW_180D_CSV
This compact OHLCV window is for K-line, MA20/MA60/EMA23, volume, support/resistance, and recent pattern checks.
```csv
date,open,high,low,close,volume,ma5,ma20,ma60,ma120,ema23,return_1d,return_5d,return_20d,volume_ratio,distance_to_ma20_pct,distance_to_high_60_pct
20260326,200,200,185,187.5,4659483,,,,,,,,,,,
20260327,185,188,180.5,184,988127,,,,,,-1.87,,,,,
20260330,180.5,185,177.5,184.5,693109,,,,,,0.27,,,,,
20260331,184,190,183.5,185,805303,,,,,,0.27,,,,,
20260401,186,189,182.5,183,591772,184.8,184.8,184.8,184.8,186.5,-1.08,,,0.38,-0.97,-8.5
20260402,183,184,170,170.5,1143983,181.4,182.42,182.42,182.42,185.17,-6.83,-9.07,,0.77,-6.53,-14.75
20260407,174.5,178.5,173,177,647231,180,181.64,181.64,181.64,184.49,3.81,-3.8,,0.48,-2.56,-11.5
20260408,179,186,176,185,742807,180.1,182.06,182.06,182.06,184.53,4.52,0.27,,0.58,1.61,-7.5
20260409,185,190.5,183.5,190,1113015,181.1,182.94,182.94,182.94,184.98,2.7,2.7,,0.88,3.86,-5
20260410,185,186.5,181,182.5,710856,181,182.9,182.9,182.9,184.78,-3.95,-0.27,,0.59,-0.22,-8.75
20260413,182.5,183,172,179.5,893345,182.8,182.59,182.59,182.59,184.34,-1.64,5.28,,0.76,-1.69,-10.25
20260414,178,178,173,173.5,571567,182.1,181.83,181.83,181.83,183.43,-3.34,-1.98,,0.51,-4.58,-13.25
20260415,174.5,176.5,171.5,175,457885,180.1,181.31,181.31,181.31,182.73,0.86,-5.41,,0.42,-3.48,-12.5
20260416,177.5,189,176.5,185,866290,179.1,181.57,181.57,181.57,182.92,5.71,-2.63,,0.81,1.89,-7.5
20260417,183,185,179,181,522526,178.8,181.53,181.53,181.53,182.76,-2.16,-0.82,,0.51,-0.29,-9.5
20260420,182,191,182,184.5,1024355,179.8,181.72,181.72,181.72,182.91,1.93,2.79,,1,1.53,-7.75
20260421,187.5,188,180.5,182,730410,181.5,181.74,181.74,181.74,182.83,-1.35,4.9,,0.72,0.15,-9
20260422,181.5,185,180,185,466824,183.5,181.92,181.92,181.92,183.01,1.65,5.71,,0.48,1.69,-7.5
20260423,186,186,176,178,698373,182.1,181.71,181.71,181.71,182.59,-3.78,-3.78,,0.72,-2.04,-11
20260424,179.5,179.5,175,175,436124,180.9,181.38,181.38,181.38,181.96,-1.69,-3.31,,0.46,-3.51,-12.5
20260427,175,175,171.5,173.5,443902,178.7,180.68,181,181,181.26,-0.86,-5.96,-7.47,0.61,-3.97,-13.25
20260428,173.5,174.5,172,174.5,251268,177.2,180.2,180.7,180.7,180.69,0.58,-4.12,-5.16,0.36,-3.16,-12.75
20260429,175.5,181,175,181,552348,176.4,180.03,180.72,180.72,180.72,3.72,-2.16,-1.9,0.81,0.54,-9.5
20260430,182.5,186.5,180,185,844488,177.8,180.03,180.9,180.9,181.07,2.21,3.93,0,1.23,2.76,-7.5
20260504,187,188,179.5,181,684357,179,179.93,180.9,180.9,181.07,-2.16,3.43,-1.09,0.99,0.6,-9.5
20260505,181,181.5,178.5,178.5,382172,180,180.32,180.81,180.81,180.85,-1.38,2.88,4.69,0.59,-1.01,-10.75
20260506,181.5,181.5,175,176,396294,180.3,180.28,180.63,180.63,180.45,-1.4,0.86,-0.56,0.62,-2.37,-12
20260507,180,181.5,176.5,179,527916,179.9,179.97,180.57,180.57,180.33,1.7,-1.1,-3.24,0.84,-0.54,-10.5
20260508,180,183.5,177.5,180.5,478389,179,179.5,180.57,180.57,180.34,0.84,-2.43,-5,0.8,0.56,-9.75
20260511,182,185,179,179.5,601845,178.7,179.35,180.53,180.53,180.27,-0.55,-0.83,-1.64,1.02,0.08,-10.25
20260512,180,181,178.5,178.5,357990,178.7,179.3,180.47,180.47,180.13,-0.56,0,-0.56,0.63,-0.45,-10.75
20260513,178.5,178.5,173.5,175,523656,178.5,179.38,180.3,180.3,179.7,-1.96,-0.57,0.86,0.93,-2.44,-12.5
20260514,173,173.5,162.5,171.5,1178767,177,179.2,180.03,180.03,179.02,-2,-4.19,-2,1.97,-4.3,-14.25
20260515,172,186,170,180,1623924,176.9,178.95,180.03,180.03,179.1,4.96,-0.28,-2.7,2.55,0.59,-10
20260518,180,180,173.5,174.5,590882,175.9,178.62,179.87,179.87,178.71,-3.06,-2.79,-3.59,0.92,-2.31,-12.75
20260519,177.5,179.5,174.5,174.5,333041,175.1,178.12,179.72,179.72,178.36,0,-2.24,-5.42,0.55,-2.04,-12.75
20260520,174.5,174.5,168.5,169,509179,173.9,177.47,179.43,179.43,177.58,-3.15,-3.43,-7.14,0.86,-4.78,-15.5
20260521,171,174.5,169.5,172.5,358246,174.1,176.85,179.25,179.25,177.16,2.07,0.58,-6.76,0.61,-2.46,-13.75
20260522,172.5,172.5,168.5,169,443434,171.9,176.4,178.99,178.99,176.48,-2.03,-6.11,-5.06,0.77,-4.2,-15.5
20260523,172.5,172.5,168.5,169,443434,170.8,176.1,178.74,178.74,175.86,0,-3.15,-3.43,0.77,-4.03,-15.5
20260524,172.5,172.5,168.5,169,443434,169.7,175.88,178.5,178.5,175.28,0,-3.15,-2.59,0.77,-3.91,-15.5
20260525,171,171,165,167.5,595215,169.4,175.53,178.24,178.24,174.64,-0.89,-0.89,-4.01,1,-4.57,-16.25
20260526,172.5,172.5,168.5,169,443434,168.7,174.93,178.02,178.02,174.17,0.9,-2.03,-6.63,0.75,-3.39,-15.5
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 75.28
- over_600_ratio: 73.06
- over_800_ratio: 72.31
- over_1000_ratio: 71.38
- over_400_change_1w: -0.14
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.15
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC_WINDOW_12W_CSV
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_600_ratio,over_600_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up,four_thresholds_sync_up,retail_ratio,total_shareholders
20260430,75.56,,73.14,,72.39,,71.46,,0,False,False,False,,
20260508,75.58,0.02,73.21,0.07,72.46,0.07,71.53,0.07,1,True,True,True,,
20260515,75.42,-0.16,73.21,0,72.46,0,71.53,0,0,False,False,False,,
20260522,75.28,-0.14,73.06,-0.15,72.31,-0.15,71.38,-0.15,0,False,False,False,,
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
