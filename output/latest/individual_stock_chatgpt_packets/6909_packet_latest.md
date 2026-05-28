# INDIVIDUAL STOCK CHATGPT PACKET - 6909 創控

## Metadata
- generated_at: 2026-05-28 19:33:35 Asia/Taipei
- stock_id: 6909
- stock_name: 創控
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6909_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6909_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6909_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6909_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6909_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6909_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6909_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6909_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6909_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6909_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6909_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6909_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6909_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6909_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6909_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6909_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6909_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6909_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6909.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6909.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6909.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6909.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6909.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6909.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6909_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6909_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6909_latest.md?ref=main

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
- open: 53
- high: 54.3
- low: 51
- close: 51.3
- volume: 678797
- ma5: 53.52
- ema23_primary: 54.21
- distance_to_ema23_pct: -5.37
- ma20: 54.99
- ma60: 51.47
- ma120: 46.37
- return_5d: -3.57
- return_20d: -12.31
- volume_ratio: 0.59
- distance_to_ma20_pct_auxiliary: -6.72
- distance_to_high_60_pct: -28.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,59.4,63.5,58.3,61.6,2629454,55.95,10.09,56.29,47.57,0.61
20260504,62.7,62.9,58.7,58.7,2527027,56.18,4.48,57.02,47.76,0.58
20260505,58.2,60.3,57.5,58.8,1241088,56.4,4.26,57.54,47.98,0.29
20260506,59,60.5,57.6,57.7,1394486,56.51,2.11,57.98,48.2,0.34
20260507,58,60.4,57.6,59.5,1187178,56.76,4.83,58.52,48.44,0.3
20260508,59.5,61.6,55.7,56.9,1979970,56.77,0.23,58.87,48.66,0.51
20260511,56.3,56.8,55.1,56.3,878688,56.73,-0.76,59.23,48.88,0.23
20260512,57,59.6,56.1,57.2,1307441,56.77,0.76,59.63,49.15,0.33
20260513,56.8,56.9,54.4,54.7,1110097,56.6,-3.35,59.73,49.37,0.3
20260514,51,55.5,51,52.4,1280906,56.25,-6.84,59.45,49.54,0.38
20260515,53.2,53.8,51,52,672671,55.89,-6.97,59.1,49.7,0.23
20260518,51.2,52.8,50.6,52.1,422617,55.58,-6.26,58.46,49.88,0.16
20260519,52.3,52.5,50,50.5,824649,55.15,-8.44,57.65,50.04,0.38
20260520,50.6,51.8,49.6,50.7,602870,54.78,-7.45,56.9,50.2,0.31
20260521,52.5,54.3,51.4,53.2,798377,54.65,-2.65,56.24,50.42,0.49
20260522,53.2,54.4,53.1,53.7,867335,54.57,-1.6,55.95,50.63,0.62
20260525,55,55.3,54.2,54.4,685223,54.56,-0.29,55.73,50.86,0.54
20260526,54.9,56.4,53.2,55.2,953843,54.61,1.08,55.65,51.09,0.79
20260527,55.8,56.5,53,53,949319,54.48,-2.71,55.35,51.29,0.8
20260528,53,54.3,51,51.3,678797,54.21,-5.37,54.99,51.47,0.59
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 39.4
- over_600_ratio: 33.53
- over_800_ratio: 26.81
- over_1000_ratio: 22.65
- over_400_change_1w: 0.42
- over_800_change_1w: -0.27
- over_1000_change_1w: -0.27
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,39.83,,26.57,,23.79,,0,False,False
20260508,38.47,-1.36,26.57,0,23.79,0,0,False,False
20260515,38.98,0.51,27.08,0.51,22.92,-0.87,1,False,True
20260522,39.4,0.42,26.81,-0.27,22.65,-0.27,2,False,False
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
