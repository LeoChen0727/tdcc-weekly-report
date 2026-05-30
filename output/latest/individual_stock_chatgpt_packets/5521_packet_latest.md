# INDIVIDUAL STOCK CHATGPT PACKET - 5521 工信

## Metadata
- generated_at: 2026-05-30 23:42:44 Asia/Taipei
- stock_id: 5521
- stock_name: 工信
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/5521_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5521_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5521_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5521_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5521_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5521_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5521_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5521_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5521_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/5521_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5521_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5521_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5521_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5521_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5521_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/5521_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5521_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5521_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5521.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/5521.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5521.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5521.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/5521.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5521.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5521_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5521_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5521_latest.md?ref=main

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
- open: 10.25
- high: 10.35
- low: 10.1
- close: 10.35
- volume: 3640749
- ma5: 10.28
- ema23_primary: 11
- distance_to_ema23_pct: -5.91
- ma20: 10.92
- ma60: 12.81
- ma120: 17.14
- return_5d: -3.27
- return_20d: -8.81
- volume_ratio: 0.62
- distance_to_ma20_pct_auxiliary: -5.22
- distance_to_high_60_pct: -58.93

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,11.35,11.5,11.1,11.3,3251481,12.47,-9.35,12.01,16.43,0.64
20260505,11.3,11.75,11.25,11.7,4137668,12.4,-5.66,11.96,16.26,0.81
20260506,11.85,12.55,11.65,12.15,9545162,12.38,-1.86,11.94,16.09,1.75
20260507,12.25,12.25,11.85,12,5367187,12.35,-2.82,11.92,15.93,1.06
20260508,12.1,12.25,11.2,11.55,12172904,12.28,-5.96,11.88,15.76,2.26
20260511,11.65,12.15,11.65,12.1,5264685,12.27,-1.36,11.87,15.61,0.95
20260512,12.05,12.05,11.4,11.5,6398045,12.2,-5.76,11.84,15.45,1.16
20260513,11.5,11.5,11.05,11.15,7415274,12.12,-7.97,11.78,15.27,1.32
20260514,11.25,11.25,10.6,10.6,9682936,11.99,-11.59,11.7,15.09,1.69
20260515,10.6,10.6,10.1,10.25,9342331,11.84,-13.46,11.59,14.91,1.58
20260518,10.3,10.45,10.1,10.25,4748191,11.71,-12.48,11.49,14.74,0.79
20260519,10.35,10.45,10.15,10.25,2927189,11.59,-11.56,11.41,14.57,0.5
20260520,10.3,10.65,10.2,10.55,5103165,11.5,-8.28,11.34,14.41,0.87
20260521,10.8,11,10.55,10.95,5286727,11.46,-4.42,11.28,14.25,0.88
20260522,11.05,11.1,10.5,10.7,5641295,11.39,-6.09,11.23,14.06,0.96
20260525,10.8,10.9,10.25,10.35,7019858,11.31,-8.46,11.16,13.83,1.19
20260526,10.3,10.4,10.2,10.25,2778885,11.22,-8.63,11.1,13.61,0.48
20260527,10.3,10.45,10.2,10.3,3331925,11.14,-7.56,11.03,13.34,0.57
20260528,10.35,10.4,10.15,10.15,4119533,11.06,-8.22,10.97,13.06,0.7
20260529,10.25,10.35,10.1,10.35,3640749,11,-5.91,10.92,12.81,0.62
```

## Latest TDCC Snapshot
- as_of_date: 20260529
- over_400_ratio: 58.5
- over_600_ratio: 56.4
- over_800_ratio: 54.42
- over_1000_ratio: 52.81
- over_400_change_1w: -0.24
- over_800_change_1w: -0.43
- over_1000_change_1w: -0.77
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.14,,56.79,,55.69,,0,False,False
20260508,60.55,-0.59,56.22,-0.57,54.79,-0.9,0,False,False
20260515,58.61,-1.94,54.7,-1.52,53.82,-0.97,0,False,False
20260522,58.74,0.13,54.85,0.15,53.58,-0.24,1,False,True
20260529,58.5,-0.24,54.42,-0.43,52.81,-0.77,0,False,False
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
