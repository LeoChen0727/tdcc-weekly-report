# INDIVIDUAL STOCK CHATGPT PACKET - 1752 南光

## Metadata
- generated_at: 2026-05-29 19:31:49 Asia/Taipei
- stock_id: 1752
- stock_name: 南光
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 137
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1752_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1752_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1752_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1752_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1752_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1752_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1752_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1752_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1752_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1752_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1752_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1752_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1752_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1752_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1752_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1752_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1752_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1752_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1752.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1752.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1752.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1752.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1752.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1752.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1752_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1752_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1752_latest.md?ref=main

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
- open: 32.4
- high: 32.85
- low: 32.3
- close: 32.85
- volume: 134686
- ma5: 32.55
- ema23_primary: 33.23
- distance_to_ema23_pct: -1.15
- ma20: 33.01
- ma60: 34.88
- ma120: 36.05
- return_5d: 0.31
- return_20d: -1.94
- volume_ratio: 1.35
- distance_to_ma20_pct_auxiliary: -0.48
- distance_to_high_60_pct: -11.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,33.65,33.65,33.35,33.5,93500,35,-4.29,35.1,36.08,1.2
20260505,33.45,33.6,33.2,33.6,148993,34.89,-3.68,35,36.03,1.8
20260506,33.6,33.6,33.3,33.55,79188,34.77,-3.52,34.88,35.98,0.93
20260507,34,34,33.45,33.5,126752,34.67,-3.37,34.77,35.93,1.44
20260508,34.45,34.45,33.45,33.9,54904,34.6,-2.03,34.68,35.88,0.62
20260511,33.9,33.9,33.4,33.55,100040,34.52,-2.8,34.57,35.83,1.1
20260512,33.55,33.55,33.35,33.4,71115,34.42,-2.97,34.46,35.78,0.76
20260513,33.35,33.45,33.05,33.45,132530,34.34,-2.6,34.34,35.73,1.36
20260514,33.25,33.3,33,33,143727,34.23,-3.59,34.2,35.67,1.4
20260515,33.2,33.2,32.7,32.8,178688,34.11,-3.84,34.06,35.61,1.66
20260518,32.55,32.6,32.35,32.45,74012,33.97,-4.48,33.91,35.54,0.69
20260519,32.45,32.5,32.35,32.5,34230,33.85,-3.99,33.76,35.48,0.32
20260520,33.4,33.4,32.4,32.7,36180,33.75,-3.12,33.62,35.41,0.35
20260521,32.95,33,32.7,32.75,126379,33.67,-2.73,33.49,35.33,1.19
20260522,32.85,32.85,32.65,32.75,60177,33.59,-2.51,33.38,35.26,0.57
20260525,32.75,32.75,32.35,32.4,143797,33.49,-3.27,33.25,35.18,1.3
20260526,32.4,32.5,32.3,32.5,105645,33.41,-2.73,33.16,35.11,1
20260527,32.5,32.5,32.2,32.5,74627,33.34,-2.51,33.09,35.03,0.74
20260528,32.5,32.65,32.35,32.5,79660,33.27,-2.3,33.04,34.95,0.81
20260529,32.4,32.85,32.3,32.85,134686,33.23,-1.15,33.01,34.88,1.35
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 63.94
- over_600_ratio: 63.03
- over_800_ratio: 61.06
- over_1000_ratio: 57.58
- over_400_change_1w: 0.04
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.88,,61.02,,57.56,,0,False,False
20260508,63.88,0,61.02,0,57.56,0,0,False,False
20260515,63.9,0.02,61.04,0.02,57.56,0,1,False,True
20260522,63.94,0.04,61.06,0.02,57.58,0.02,2,True,True
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
