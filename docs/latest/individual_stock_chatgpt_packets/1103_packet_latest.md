# INDIVIDUAL STOCK CHATGPT PACKET - 1103 嘉泥

## Metadata
- generated_at: 2026-05-28 20:18:10 Asia/Taipei
- stock_id: 1103
- stock_name: 嘉泥
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/1103_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1103_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1103_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1103_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1103_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1103_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1103_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1103_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1103_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/1103_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1103_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1103_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1103_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1103_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1103_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/1103_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1103_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1103_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1103.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/1103.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1103.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1103.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/1103.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1103.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1103_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1103_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1103_latest.md?ref=main

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
- open: 13.2
- high: 13.25
- low: 13.1
- close: 13.2
- volume: 296973
- ma5: 13.19
- ema23_primary: 13.26
- distance_to_ema23_pct: -0.49
- ma20: 13.21
- ma60: 13.52
- ma120: 13.76
- return_5d: 1.15
- return_20d: -2.22
- volume_ratio: 0.93
- distance_to_ma20_pct_auxiliary: -0.09
- distance_to_high_60_pct: -6.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,13.5,13.55,13.4,13.45,195326,13.67,-1.62,13.73,13.79,0.63
20260504,13.45,13.45,13.25,13.3,554406,13.64,-2.49,13.71,13.78,1.78
20260505,13.3,13.35,13.25,13.3,217684,13.61,-2.29,13.69,13.77,0.69
20260506,13.4,13.45,13.25,13.45,335248,13.6,-1.09,13.67,13.75,1.03
20260507,13.35,13.55,13.35,13.45,383890,13.59,-1,13.65,13.74,1.23
20260508,13.4,13.6,13.4,13.4,202306,13.57,-1.26,13.63,13.72,0.65
20260511,13.4,13.55,13.35,13.45,241941,13.56,-0.81,13.62,13.71,0.79
20260512,13.45,13.45,13.25,13.3,341516,13.54,-1.76,13.59,13.7,1.08
20260513,13.3,13.3,13.15,13.2,405949,13.51,-2.3,13.55,13.69,1.26
20260514,13.1,13.25,13,13.05,445299,13.47,-3.13,13.52,13.67,1.34
20260515,13.1,13.15,12.95,12.95,421373,13.43,-3.56,13.47,13.66,1.23
20260518,12.95,13,12.85,12.9,392527,13.38,-3.62,13.41,13.64,1.13
20260519,12.9,13.05,12.9,13.05,153129,13.36,-2.3,13.37,13.63,0.45
20260520,12.95,13.1,12.9,13,300923,13.33,-2.45,13.33,13.61,0.89
20260521,13.1,13.1,13,13.05,206857,13.3,-1.91,13.29,13.59,0.62
20260522,13,13.15,12.95,13.1,183262,13.29,-1.41,13.27,13.58,0.58
20260525,13.1,13.25,13.05,13.2,413873,13.28,-0.6,13.25,13.56,1.24
20260526,13.2,13.25,13.1,13.25,291791,13.28,-0.2,13.24,13.55,0.94
20260527,13.25,13.25,13.1,13.2,412829,13.27,-0.53,13.23,13.53,1.31
20260528,13.2,13.25,13.1,13.2,296973,13.26,-0.49,13.21,13.52,0.93
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 78.91
- over_600_ratio: 77.47
- over_800_ratio: 76.13
- over_1000_ratio: 75.46
- over_400_change_1w: -0.1
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.01,,76.13,,75.47,,0,False,False
20260508,79.06,0.05,76.16,0.03,75.49,0.02,1,False,True
20260515,79.01,-0.05,76.16,0,75.49,0,2,False,False
20260522,78.91,-0.1,76.13,-0.03,75.46,-0.03,0,False,False
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
