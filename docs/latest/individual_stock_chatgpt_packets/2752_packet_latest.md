# INDIVIDUAL STOCK CHATGPT PACKET - 2752 豆府

## Metadata
- generated_at: 2026-05-28 19:32:07 Asia/Taipei
- stock_id: 2752
- stock_name: 豆府
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2752_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2752_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2752_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2752_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2752_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2752_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2752_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2752_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2752_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2752_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2752_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2752_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2752_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2752_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2752_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2752_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2752_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2752_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2752.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2752.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2752.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2752.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2752.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2752.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2752_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2752_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2752_latest.md?ref=main

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
- open: 173
- high: 173
- low: 172
- close: 172.5
- volume: 13413
- ma5: 173.6
- ema23_primary: 180.5
- distance_to_ema23_pct: -4.43
- ma20: 179.35
- ma60: 195.31
- ma120: 202.15
- return_5d: -2.54
- return_20d: -7.01
- volume_ratio: 0.21
- distance_to_ma20_pct_auxiliary: -3.82
- distance_to_high_60_pct: -22.65

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,186.5,186.5,185.5,185.5,11000,194.54,-4.64,194.65,204.28,0.36
20260504,185.5,185.5,185,185.5,22000,193.78,-4.27,193.57,203.89,0.72
20260505,185.5,185.5,183,184.5,39000,193.01,-4.41,192.43,203.5,1.25
20260506,184.5,184.5,180,181,61000,192.01,-5.73,190.93,203.05,1.89
20260507,181,181,180.5,181,30000,191.09,-5.28,189.38,202.61,1.03
20260508,180.5,185,180,184,42000,190.5,-3.41,188.72,202.24,1.47
20260511,183,183,181.5,182,26000,189.79,-4.11,187.93,201.84,0.92
20260512,182.5,182.5,181.5,181.5,13000,189.1,-4.02,187.22,201.45,0.46
20260513,181,182.5,181,182.5,15000,188.55,-3.21,186.57,201.07,0.53
20260514,183,183,182,182,15000,188,-3.19,185.95,200.66,0.54
20260515,183,183,180,182,27000,187.5,-2.94,185.45,200.25,0.97
20260518,182,182,179.5,180,30000,186.88,-3.68,184.88,199.82,1.07
20260519,180,180,176,176.5,66000,186.01,-5.11,184.2,199.34,2.2
20260520,177,177,174,174,113000,185.01,-5.95,183.43,198.75,3.4
20260521,174.5,177,174,177,33000,184.35,-3.98,182.82,198.22,0.98
20260522,177,177,175.5,177,176000,183.73,-3.66,182.22,197.7,4.28
20260525,175,175,171.5,172.5,173000,182.8,-5.63,181.38,197.12,3.55
20260526,172,173,172,173,173000,181.98,-4.93,180.65,196.53,3.07
20260527,172.5,173,172,173,172000,181.23,-4.54,180,195.92,2.73
20260528,173,173,172,172.5,13413,180.5,-4.43,179.35,195.31,0.21
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 64.44
- over_600_ratio: 54.48
- over_800_ratio: 41.45
- over_1000_ratio: 41.45
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,64.62,,41.45,,41.45,,0,False,False
20260508,64.51,-0.11,41.45,0,41.45,0,0,False,False
20260515,64.44,-0.07,41.45,0,41.45,0,0,False,False
20260522,64.44,0,41.45,0,41.45,0,0,False,False
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
