# INDIVIDUAL STOCK CHATGPT PACKET - 8091 翔名

## Metadata
- generated_at: 2026-05-30 23:43:51 Asia/Taipei
- stock_id: 8091
- stock_name: 翔名
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 273
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8091_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8091_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8091_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8091_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8091_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8091_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8091_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8091_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8091_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8091_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8091_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8091_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8091_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8091_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8091_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8091_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8091_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8091_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8091.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8091.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8091.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8091.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8091.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8091.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8091_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8091_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8091_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260529
- open: 259.5
- high: 262
- low: 257.5
- close: 260.5
- volume: 260000
- ma5: 266.1
- ema23_primary: 232.42
- distance_to_ema23_pct: 12.08
- ma20: 230.9
- ma60: 183.12
- ma120: 154.03
- return_5d: -2.43
- return_20d: 35.68
- volume_ratio: 0.18
- distance_to_ma20_pct_auxiliary: 12.82
- distance_to_high_60_pct: -6.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,198.5,204.5,194,197,1671000,176.18,11.82,180.93,153.01,1.1
20260505,195,197.5,189,191,707000,177.42,7.66,182.45,153.91,0.51
20260506,194,194,185.5,190,706000,178.47,6.46,183.62,154.78,0.54
20260507,192,194,188,189.5,678000,179.38,5.64,184.7,155.62,0.54
20260508,188.5,195.5,187.5,191,721000,180.35,5.9,185.03,156.43,0.65
20260511,196,209,195,200,1908000,181.99,9.9,185.88,157.48,1.75
20260512,197,197,188,190,1214000,182.66,4.02,186.32,158.38,1.11
20260513,195.5,205,195,196,1522000,183.77,6.66,187.15,159.35,1.35
20260514,200,215.5,191,215.5,1737000,186.41,15.6,188.68,160.68,1.5
20260515,215.5,237,212.5,237,2859000,190.63,24.33,191.6,162.46,2.3
20260518,248,260.5,241,260.5,6267000,196.45,32.6,195.55,164.61,4.15
20260519,262,271,251,263.5,5040000,202.04,30.42,199.15,166.74,3.13
20260520,260.5,261,252,253.5,728000,206.33,22.86,202.4,168.73,0.46
20260521,254,257,240.5,246,904000,209.63,17.35,205.47,170.62,0.57
20260522,248.5,267,244,267,257000,214.41,24.53,210,172.76,0.17
20260525,275,278,267,273.5,273000,219.34,24.69,214.57,174.88,0.18
20260526,273.5,273.5,266,269.5,269000,223.52,20.57,219.1,177,0.18
20260527,280,280,264,269,272000,227.31,18.34,223.6,179.07,0.18
20260528,266,269,255,258,262000,229.87,12.24,227.47,181.05,0.18
20260529,259.5,262,257.5,260.5,260000,232.42,12.08,230.9,183.12,0.18
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 52.66
- over_600_ratio: 45.3
- over_800_ratio: 37.74
- over_1000_ratio: 34.32
- over_400_change_1w: 0.51
- over_800_change_1w: -0.34
- over_1000_change_1w: -0.28
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,50.6,,38.16,,32.76,,0,False,False
20260508,49.41,-1.19,36.35,-1.81,32.71,-0.05,0,False,False
20260515,50.88,1.47,36.26,-0.09,32.64,-0.07,1,False,False
20260522,52.15,1.27,38.08,1.82,34.6,1.96,2,True,True
20260529,52.66,0.51,37.74,-0.34,34.32,-0.28,3,False,False
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
