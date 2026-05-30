# INDIVIDUAL STOCK CHATGPT PACKET - 7744 崴寶

## Metadata
- generated_at: 2026-05-30 23:43:44 Asia/Taipei
- stock_id: 7744
- stock_name: 崴寶
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 255
- latest_tdcc_date: 20260529
- tdcc_rows: 5
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7744_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7744_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7744_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7744_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7744_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7744_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7744_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7744_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7744_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7744_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7744_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7744_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7744_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7744_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7744_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7744_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7744_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7744_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7744.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7744.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7744.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7744.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7744.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7744.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7744_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7744_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7744_latest.md?ref=main

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
- open: 489
- high: 498
- low: 486.5
- close: 492
- volume: 492000
- ma5: 498.4
- ema23_primary: 516.32
- distance_to_ema23_pct: -4.71
- ma20: 534.1
- ma60: 496.02
- ma120: 413.25
- return_5d: -1.8
- return_20d: -3.91
- volume_ratio: 1.69
- distance_to_ma20_pct_auxiliary: -7.88
- distance_to_high_60_pct: -20.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,514,521,509,520,100000,497.12,4.6,499.5,445.45,0.55
20260505,538,572,522,572,251000,503.36,13.64,506.18,449.65,1.29
20260506,575,581,540,562,391000,508.24,10.58,511.82,453.76,1.86
20260507,573,573,545,556,133000,512.22,8.55,514.95,457.74,0.64
20260508,536,573,534,564,127000,516.54,9.19,519.27,462.05,0.64
20260511,585,585,548,553,207000,519.58,6.43,522.12,466.22,1.04
20260512,550,563,540,555,112000,522.53,6.21,525.8,470.58,0.57
20260513,549,609,548,598,250000,528.82,13.08,531.85,475.52,1.23
20260514,591,618,582,608,218000,535.42,13.56,537.8,480.3,1.07
20260515,592,592,548,548,435000,536.47,2.15,540.9,483.93,1.97
20260518,521,542,521,542,69000,536.93,0.94,543.25,486.92,0.32
20260519,543,545,512,517,123000,535.27,-3.41,543.85,489.05,0.58
20260520,520,520,490,490,273000,531.49,-7.81,541.85,490.89,1.29
20260521,507,516,496.5,504,126000,529.2,-4.76,541.2,493.16,0.62
20260522,513,525,491,501,504000,526.85,-4.91,538.85,494.77,2.42
20260525,516,527,513,520,521000,526.28,-1.19,537.75,496.28,2.42
20260526,520,521,499,505,506000,524.51,-3.72,537.3,496.84,2.22
20260527,508,508,495,497,502000,522.22,-4.83,536.4,496.61,2.01
20260528,498.5,505,478,478,493000,518.53,-7.82,535.1,495.76,1.82
20260529,489,498,486.5,492,492000,516.32,-4.71,534.1,496.02,1.69
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 81.07
- over_600_ratio: 77.95
- over_800_ratio: 66.95
- over_1000_ratio: 58.25
- over_400_change_1w: -0.75
- over_800_change_1w: -3.39
- over_1000_change_1w: -3.39
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.92,,70.07,,58.28,,0,False,False
20260508,80.13,0.21,70.28,0.21,61.62,3.34,1,True,True
20260515,80.38,0.25,70.53,0.25,61.83,0.21,2,True,True
20260522,81.82,1.44,70.34,-0.19,61.64,-0.19,3,False,False
20260529,81.07,-0.75,66.95,-3.39,58.25,-3.39,4,False,False
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
