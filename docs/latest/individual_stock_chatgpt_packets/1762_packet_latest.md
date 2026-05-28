# INDIVIDUAL STOCK CHATGPT PACKET - 1762 中化生

## Metadata
- generated_at: 2026-05-28 19:31:41 Asia/Taipei
- stock_id: 1762
- stock_name: 中化生
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1762_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1762_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1762_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1762_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1762_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1762_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1762_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1762_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1762_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1762_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1762_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1762_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1762_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1762_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1762_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1762_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1762_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1762_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1762.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1762.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1762.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1762.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1762.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1762.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1762_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1762_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1762_latest.md?ref=main

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
- open: 39.75
- high: 40.6
- low: 39.7
- close: 39.95
- volume: 488010
- ma5: 39.48
- ema23_primary: 35.91
- distance_to_ema23_pct: 11.26
- ma20: 36.11
- ma60: 31.13
- ma120: 28.31
- return_5d: 5.83
- return_20d: 41.17
- volume_ratio: 0.61
- distance_to_ma20_pct_auxiliary: 10.64
- distance_to_high_60_pct: -2.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,28.3,28.45,28.15,28.25,94365,28.4,-0.54,28.39,27.99,0.85
20260504,28.6,28.6,27.7,27.7,117950,28.35,-2.28,28.34,28.02,1.05
20260505,27.6,29.25,27.6,29.15,183811,28.41,2.6,28.38,28.06,1.59
20260506,32.05,32.05,32.05,32.05,415960,28.72,11.61,28.6,28.13,3.23
20260507,35.25,35.25,35.25,35.25,269846,29.26,20.47,28.98,28.27,1.95
20260508,38.75,38.75,38.75,38.75,1200197,30.05,28.95,29.54,28.47,6.21
20260511,39.5,39.55,36.6,37.55,1725639,30.68,22.41,30.03,28.66,6.22
20260512,38.65,38.9,34.15,34.5,1487336,30.99,11.31,30.35,28.79,4.33
20260513,34.95,37.95,34.5,37.95,830433,31.57,20.19,30.77,28.99,2.2
20260514,39.4,40.85,36.25,37,2960555,32.03,15.53,31.13,29.16,5.75
20260515,37,37.75,35.5,35.85,763316,32.34,10.84,31.44,29.33,1.39
20260518,36,37.75,35.3,37.15,670238,32.75,13.45,31.83,29.52,1.16
20260519,36.75,38.7,36.65,37.1,546890,33.11,12.06,32.25,29.71,0.91
20260520,37.2,39.25,36.75,38.75,759124,33.58,15.4,32.76,29.93,1.2
20260521,38.9,39.4,37.65,37.75,875981,33.93,11.27,33.23,30.11,1.3
20260522,37.85,38.85,37.55,37.95,443017,34.26,10.77,33.74,30.28,0.65
20260525,38.25,40.5,37.95,40.2,1073209,34.76,15.66,34.35,30.5,1.46
20260526,39.8,40,39,39.6,455178,35.16,12.63,34.95,30.7,0.6
20260527,39.95,40.55,39.15,39.7,544340,35.54,11.71,35.52,30.91,0.7
20260528,39.75,40.6,39.7,39.95,488010,35.91,11.26,36.11,31.13,0.61
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 44.82
- over_600_ratio: 42.83
- over_800_ratio: 40.02
- over_1000_ratio: 37.68
- over_400_change_1w: -0.07
- over_800_change_1w: -0.07
- over_1000_change_1w: -0.07
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,44.53,,39.73,,37.4,,0,False,False
20260508,44.63,0.1,39.83,0.1,37.5,0.1,1,True,True
20260515,44.89,0.26,40.09,0.26,37.75,0.25,2,True,True
20260522,44.82,-0.07,40.02,-0.07,37.68,-0.07,0,False,False
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
