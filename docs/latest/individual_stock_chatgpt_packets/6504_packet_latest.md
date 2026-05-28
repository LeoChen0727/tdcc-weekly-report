# INDIVIDUAL STOCK CHATGPT PACKET - 6504 南六

## Metadata
- generated_at: 2026-05-28 19:33:20 Asia/Taipei
- stock_id: 6504
- stock_name: 南六
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6504_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6504_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6504_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6504_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6504_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6504_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6504_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6504_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6504_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6504_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6504_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6504_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6504_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6504_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6504_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6504_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6504_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6504_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6504.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6504.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6504.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6504.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6504.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6504.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6504_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6504_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6504_latest.md?ref=main

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
- open: 37.4
- high: 38.7
- low: 36.85
- close: 36.9
- volume: 113463
- ma5: 37.81
- ema23_primary: 38.86
- distance_to_ema23_pct: -5.05
- ma20: 38.86
- ma60: 39.8
- ma120: 41.03
- return_5d: -4.77
- return_20d: -6.58
- volume_ratio: 1.68
- distance_to_ma20_pct_auxiliary: -5.05
- distance_to_high_60_pct: -15.37

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,39.4,39.5,39,39.45,32534,40.43,-2.43,40.93,40.93,0.66
20260504,39.5,39.5,38.8,38.9,75390,40.3,-3.48,40.78,40.91,1.6
20260505,39.5,39.5,38.9,39.3,31449,40.22,-2.29,40.71,40.88,0.67
20260506,40.4,40.4,39.3,39.9,41586,40.19,-0.73,40.66,40.81,0.87
20260507,40.2,40.2,39.35,39.65,54270,40.15,-1.24,40.52,40.65,1.15
20260508,39.65,40.35,39.55,39.8,56320,40.12,-0.79,40.37,40.58,1.24
20260511,39.9,41.2,39.9,40.75,93557,40.17,1.44,40.33,40.55,2.05
20260512,40.7,40.7,39.35,39.4,39943,40.11,-1.76,40.22,40.5,0.86
20260513,39.6,39.6,38.95,39.05,39607,40.02,-2.42,40.08,40.45,0.86
20260514,39.4,39.4,38.75,38.75,29690,39.91,-2.91,39.93,40.39,0.64
20260515,38.75,39,38.5,38.5,39545,39.8,-3.26,39.79,40.34,0.86
20260518,38.8,39.65,38.45,38.5,73953,39.69,-2.99,39.64,40.3,1.53
20260519,39.1,39.1,38.6,38.75,16512,39.61,-2.17,39.52,40.24,0.37
20260520,38.95,38.95,38.4,38.75,28567,39.54,-1.99,39.39,40.17,0.65
20260521,38.8,39.25,38.7,38.75,65200,39.47,-1.83,39.31,40.12,1.43
20260522,38.45,38.95,38.45,38.55,70508,39.4,-2.15,39.24,40.07,1.51
20260525,38.5,38.95,38,38.1,171381,39.29,-3.02,39.15,40.01,3.16
20260526,38.3,38.8,38,38,102369,39.18,-3.01,39.08,39.95,1.82
20260527,37.9,38.15,37.5,37.5,174757,39.04,-3.94,38.99,39.88,2.75
20260528,37.4,38.7,36.85,36.9,113463,38.86,-5.05,38.86,39.8,1.68
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 69.79
- over_600_ratio: 67.1
- over_800_ratio: 65.4
- over_1000_ratio: 64.3
- over_400_change_1w: 0.02
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,69.72,,65.33,,64.23,,0,False,False
20260508,69.74,0.02,65.35,0.02,64.25,0.02,1,True,True
20260515,69.77,0.03,65.38,0.03,64.28,0.03,2,True,True
20260522,69.79,0.02,65.4,0.02,64.3,0.02,3,True,True
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
