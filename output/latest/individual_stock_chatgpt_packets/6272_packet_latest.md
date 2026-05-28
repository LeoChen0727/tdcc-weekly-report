# INDIVIDUAL STOCK CHATGPT PACKET - 6272 驊陞

## Metadata
- generated_at: 2026-05-28 20:20:02 Asia/Taipei
- stock_id: 6272
- stock_name: 驊陞
- packet_status: standard_rawdata_packet
- latest_price_date: 20260528
- price_rows: 101
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6272_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6272_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6272_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6272_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6272_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6272_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6272_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6272_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6272_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6272_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6272_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6272_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6272_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6272_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6272_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6272_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6272_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6272_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6272.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6272.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6272.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6272.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6272.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6272.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6272_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6272_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6272_latest.md?ref=main

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
- date: 20260528
- open: 34.2
- high: 35
- low: 34.05
- close: 34.2
- volume: 488756
- ma5: 33.67
- ema23_primary: 32.51
- distance_to_ema23_pct: 5.19
- ma20: 32.1
- ma60: 33.03
- ma120: 37.09
- return_5d: 6.71
- return_20d: 7.38
- volume_ratio: 1.18
- distance_to_ma20_pct_auxiliary: 6.55
- distance_to_high_60_pct: -13.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,32.5,32.95,32.05,32.05,228686,32.64,-1.79,32.08,35.8,0.71
20260504,32.15,33,32.05,32.1,250102,32.59,-1.5,32.08,35.64,0.77
20260505,32.1,32.55,31.8,32.4,294591,32.57,-0.54,32.13,35.49,0.89
20260506,32.4,32.4,31.2,31.9,510445,32.52,-1.9,32.12,35.33,1.48
20260507,31.9,32.35,31.7,31.95,299067,32.47,-1.6,32.1,35.16,0.86
20260508,32,32.75,31.55,31.55,358874,32.39,-2.61,32.05,34.97,1.02
20260511,31.6,31.6,30.8,30.8,626262,32.26,-4.53,32.09,34.78,1.83
20260512,30.6,30.8,30.1,30.3,447542,32.1,-5.6,32.02,34.6,1.3
20260513,31.15,31.45,31,31.2,551216,32.02,-2.57,32.03,34.44,1.55
20260514,31.5,32,30.6,30.8,527168,31.92,-3.51,31.98,34.26,1.45
20260515,30.85,31.5,30.8,30.85,568326,31.83,-3.08,31.91,34.08,1.5
20260518,30.8,33.5,30.5,32.25,638538,31.87,1.2,31.89,33.93,1.62
20260519,31.95,32.2,31.7,31.8,316118,31.86,-0.19,31.83,33.78,0.81
20260520,31.85,32.8,31.45,31.6,277938,31.84,-0.75,31.72,33.65,0.73
20260521,31.65,32.4,31.65,32.05,255282,31.86,0.61,31.66,33.54,0.67
20260522,32.2,33.8,32.2,33.65,519209,32.01,5.14,31.73,33.43,1.36
20260525,34.3,34.3,32.7,33,496052,32.09,2.84,31.78,33.3,1.26
20260526,33.1,33.45,32.85,33.3,259032,32.19,3.45,31.86,33.19,0.66
20260527,33.5,34.2,33.3,34.2,342409,32.36,5.69,31.98,33.1,0.86
20260528,34.2,35,34.05,34.2,488756,32.51,5.19,32.1,33.03,1.18
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 51.12
- over_600_ratio: 46.77
- over_800_ratio: 41.39
- over_1000_ratio: 35.18
- over_400_change_1w: 0.2
- over_800_change_1w: -0.72
- over_1000_change_1w: 1.36
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,50.82,,41.05,,33.8,,0,False,False
20260508,50.86,0.04,41.09,0.04,33.8,0,1,False,True
20260515,50.92,0.06,42.11,1.02,33.82,0.02,2,True,True
20260522,51.12,0.2,41.39,-0.72,35.18,1.36,3,False,True
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
