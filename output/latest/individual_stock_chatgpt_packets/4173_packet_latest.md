# INDIVIDUAL STOCK CHATGPT PACKET - 4173 久裕

## Metadata
- generated_at: 2026-05-28 19:32:39 Asia/Taipei
- stock_id: 4173
- stock_name: 久裕
- packet_status: standard_180d_window_packet
- latest_price_date: 20260528
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4173_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4173_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4173_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4173_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4173_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4173_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4173_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4173_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4173_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4173_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4173_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4173_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4173_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4173_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4173_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4173_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4173_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4173_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4173.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4173.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4173.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4173.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4173.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4173.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4173_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4173_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4173_latest.md?ref=main

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
- open: 18.05
- high: 18.05
- low: 17.9
- close: 18
- volume: 125749
- ma5: 18.16
- ema23_primary: 18.59
- distance_to_ema23_pct: -3.18
- ma20: 18.44
- ma60: 19.71
- ma120: 20.56
- return_5d: -1.64
- return_20d: -5.51
- volume_ratio: 1.23
- distance_to_ma20_pct_auxiliary: -2.39
- distance_to_high_60_pct: -18.74

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,19,19,18.9,18.95,84000,19.74,-3.98,19.83,20.7,0.54
20260504,19,19,18.7,18.75,192000,19.65,-4.6,19.73,20.65,1.17
20260505,18.75,18.9,18.5,18.7,92000,19.57,-4.47,19.64,20.6,0.55
20260506,18.8,18.8,18.5,18.5,153000,19.49,-5.06,19.53,20.55,0.89
20260507,18.5,18.7,18.4,18.55,251000,19.41,-4.42,19.43,20.5,1.41
20260508,18.6,18.8,18.6,18.75,49000,19.35,-3.11,19.34,20.45,0.28
20260511,18.75,18.8,18.65,18.65,76000,19.29,-3.34,19.25,20.4,0.43
20260512,18.65,18.65,18.45,18.45,150000,19.22,-4.02,19.14,20.36,0.91
20260513,18.45,18.5,18.25,18.5,186000,19.16,-3.46,19.05,20.31,1.16
20260514,18.5,18.65,18.5,18.5,99000,19.11,-3.18,18.95,20.26,0.63
20260515,18.8,18.8,18.3,18.4,109000,19.05,-3.41,18.88,20.21,0.74
20260518,18.35,18.4,18.25,18.35,76000,18.99,-3.37,18.82,20.16,0.56
20260519,18.25,18.5,18.2,18.35,117000,18.94,-3.1,18.75,20.11,0.86
20260520,18.25,18.3,18.15,18.3,113000,18.88,-3.09,18.7,20.06,0.84
20260521,18.25,18.3,18.2,18.3,101000,18.84,-2.84,18.65,20.01,0.78
20260522,18.35,18.35,18.25,18.35,18000,18.8,-2.37,18.62,19.96,0.15
20260525,18.35,18.35,18.1,18.2,18000,18.75,-2.91,18.58,19.9,0.17
20260526,18.15,18.3,18.15,18.25,18000,18.7,-2.43,18.54,19.84,0.18
20260527,18.2,18.2,18,18,18000,18.65,-3.46,18.49,19.77,0.18
20260528,18.05,18.05,17.9,18,125749,18.59,-3.18,18.44,19.71,1.23
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 43.95
- over_600_ratio: 42.04
- over_800_ratio: 41.24
- over_1000_ratio: 40
- over_400_change_1w: 0.02
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,43.33,,41.24,,40,,0,False,False
20260508,43.91,0.58,41.24,0,40,0,1,False,False
20260515,43.93,0.02,41.24,0,40,0,2,False,False
20260522,43.95,0.02,41.24,0,40,0,3,False,False
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
