# INDIVIDUAL STOCK CHATGPT PACKET - 6186 新潤

## Metadata
- generated_at: 2026-05-26 23:54:32 Asia/Taipei
- stock_id: 6186
- stock_name: 新潤
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6186_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6186_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6186_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6186_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6186_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6186_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6186_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6186_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6186_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6186_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6186_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6186_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6186_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6186_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6186_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6186_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6186_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6186_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6186.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6186.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6186.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6186.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6186.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6186.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6186_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6186_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6186_latest.md?ref=main

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
- open: 39.35
- high: 40.1
- low: 39.3
- close: 40.05
- volume: 40000
- ma5: 39.89
- ema23_primary: 39.96
- distance_to_ema23_pct: 0.23
- ma20: 39.76
- ma60: 40.68
- ma120: 46.3
- return_5d: 0.63
- return_20d: -0.37
- volume_ratio: 0.05
- distance_to_ma20_pct_auxiliary: 0.74
- distance_to_high_60_pct: -11.78

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,40.05,40.2,39.5,40.05,725000,40.96,-2.23,40.34,42.94,1.01
20260429,40.1,40.35,39.95,40.15,553000,40.9,-1.82,40.38,42.81,0.77
20260430,40.15,40.2,39.8,40,624000,40.82,-2.01,40.47,42.66,0.9
20260504,40,40.2,39.9,39.95,690000,40.75,-1.96,40.53,42.51,0.97
20260505,40.05,40.3,39.95,40.15,583000,40.7,-1.35,40.6,42.38,0.81
20260506,40.15,40.15,39.9,39.95,713000,40.64,-1.69,40.61,42.25,0.96
20260507,39.95,40.5,39.5,40.5,1229000,40.62,-0.31,40.62,42.14,1.56
20260508,40.45,41.9,39.75,39.95,1292000,40.57,-1.52,40.6,42,1.57
20260511,40.25,40.35,39.55,39.65,1040000,40.49,-2.08,40.57,41.88,1.21
20260512,39.65,39.65,38,38.85,2334000,40.35,-3.73,40.51,41.74,2.42
20260513,38.85,38.85,38.1,38.25,1414000,40.18,-4.8,40.38,41.61,1.4
20260514,38.25,39.95,38.25,39.55,1207000,40.13,-1.44,40.33,41.48,1.14
20260515,39.55,40.5,38.75,39.05,1448000,40.04,-2.47,40.23,41.34,1.31
20260518,39.6,40.25,38.85,39.8,957000,40.02,-0.54,40.18,41.23,0.84
20260519,39.95,40.5,39.5,39.8,866000,40,-0.5,40.06,41.14,0.76
20260520,40.2,40.25,39.6,40,718000,40,0,39.98,41.06,0.62
20260521,40.2,40.3,39.9,40.1,915000,40.01,0.23,39.92,40.97,0.88
20260522,40.15,40.15,39.55,40,40000,40.01,-0.02,39.86,40.88,0.04
20260525,40,40,39,39.3,39000,39.95,-1.62,39.76,40.77,0.04
20260526,39.35,40.1,39.3,40.05,40000,39.96,0.23,39.76,40.68,0.05
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 52.32
- over_600_ratio: 50.08
- over_800_ratio: 47.95
- over_1000_ratio: 47.12
- over_400_change_1w: 0.46
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,52.66,,47.56,,47.14,,0,False,False
20260508,52.59,-0.07,47.55,-0.01,47.13,-0.01,1,False,False
20260515,51.86,-0.73,47.96,0.41,47.13,0,2,False,True
20260522,52.32,0.46,47.95,-0.01,47.12,-0.01,3,False,False
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
