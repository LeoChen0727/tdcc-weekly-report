# INDIVIDUAL STOCK CHATGPT PACKET - 2912 統一超

## Metadata
- generated_at: 2026-05-26 21:25:16 Asia/Taipei
- stock_id: 2912
- stock_name: 統一超
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2912_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2912_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2912_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2912_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2912_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2912_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2912_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2912_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2912_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2912_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2912_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2912_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2912_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2912_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2912_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2912_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2912_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2912_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2912.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2912.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2912.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2912.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2912.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2912.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2912_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2912_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2912_latest.md?ref=main

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
- date: 20260526
- open: 215.5
- high: 219
- low: 209.5
- close: 209.5
- volume: 11659854
- ma5: 217
- ema23_primary: 223.41
- distance_to_ema23_pct: -6.23
- ma20: 224.03
- ma60: 224.09
- ma120: 223.82
- return_5d: -7.91
- return_20d: -7.3
- volume_ratio: 3.28
- distance_to_ma20_pct_auxiliary: -6.48
- distance_to_high_60_pct: -12.53

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,226,226.5,223.5,224,2052777,228.46,-1.95,230,221.82,0.78
20260429,224,225,223.5,224.5,2239213,228.13,-1.59,230.05,221.94,0.87
20260430,224,226.5,224,224,2596640,227.78,-1.66,230.03,222.12,1.03
20260504,225,227.5,224,225.5,2012658,227.59,-0.92,230.03,222.35,0.79
20260505,225,226.5,224,224,1774033,227.29,-1.45,229.88,222.52,0.71
20260506,225.5,228,225,227,2170810,227.27,-0.12,229.68,222.78,0.87
20260507,226,230,226,228.5,2968761,227.37,0.5,229.65,223.12,1.17
20260508,229.5,233.5,229,232,3176895,227.76,1.86,229.7,223.42,1.22
20260511,231.5,231.5,226,227.5,2356962,227.74,-0.1,229.7,223.65,0.89
20260512,227.5,230,226,226,1493470,227.59,-0.7,229.75,223.88,0.57
20260513,225,227,224.5,225.5,1968228,227.42,-0.84,229.65,224.07,0.75
20260514,225.5,229.5,225.5,226.5,1388979,227.34,-0.37,229.4,224.28,0.54
20260515,227,229,227,227.5,1764455,227.35,0.06,229.07,224.42,0.71
20260518,228,228,225,225.5,1780910,227.2,-0.75,228.47,224.44,0.74
20260519,225.5,229.5,225,227.5,2897346,227.22,0.12,227.95,224.56,1.22
20260520,228.5,229.5,221.5,222,5331799,226.79,-2.11,227.22,224.55,2.15
20260521,223,224,218.5,221,6362466,226.31,-2.34,226.35,224.52,2.43
20260522,221,222,219.5,220,6284429,225.78,-2.56,225.62,224.47,2.24
20260525,221,221,212.5,212.5,8794576,224.67,-5.42,224.85,224.31,2.87
20260526,215.5,219,209.5,209.5,11659854,223.41,-6.23,224.03,224.09,3.28
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 84.24
- over_600_ratio: 82.37
- over_800_ratio: 80.17
- over_1000_ratio: 79.3
- over_400_change_1w: -0.2
- over_800_change_1w: -0.19
- over_1000_change_1w: -0.29
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.6,,80.3,,79.53,,0,False,False
20260508,84.6,0,80.32,0.02,79.54,0.01,1,False,True
20260515,84.44,-0.16,80.36,0.04,79.59,0.05,2,False,True
20260522,84.24,-0.2,80.17,-0.19,79.3,-0.29,0,False,False
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
