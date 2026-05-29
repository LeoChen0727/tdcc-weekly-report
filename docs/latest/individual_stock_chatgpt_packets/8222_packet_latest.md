# INDIVIDUAL STOCK CHATGPT PACKET - 8222 寶一

## Metadata
- generated_at: 2026-05-29 19:33:58 Asia/Taipei
- stock_id: 8222
- stock_name: 寶一
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/8222_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8222_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8222_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8222_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8222_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8222_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8222_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8222_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8222_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/8222_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8222_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8222_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8222_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8222_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8222_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/8222_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8222_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8222_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8222.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/8222.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8222.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8222.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/8222.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8222.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8222_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8222_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8222_latest.md?ref=main

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
- open: 36.35
- high: 37.85
- low: 36.3
- close: 36.35
- volume: 957494
- ma5: 35.47
- ema23_primary: 35.91
- distance_to_ema23_pct: 1.23
- ma20: 36.03
- ma60: 36.42
- ma120: 38.91
- return_5d: 0
- return_20d: 3.56
- volume_ratio: 1.94
- distance_to_ma20_pct_auxiliary: 0.89
- distance_to_high_60_pct: -10.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,35.5,37.75,35.5,36.3,519958,36.31,-0.04,35.89,37.85,1.26
20260505,36.9,38,36.2,37.85,372718,36.44,3.86,36.07,37.76,0.89
20260506,38.2,38.3,36.5,37.1,375345,36.5,1.65,36.22,37.68,0.88
20260507,37.2,37.5,36.7,37.25,257545,36.56,1.89,36.35,37.6,0.6
20260508,37.7,39,37.2,37.95,736620,36.68,3.47,36.53,37.53,1.63
20260511,37.65,37.65,34.85,35.5,833790,36.58,-2.95,36.6,37.45,1.73
20260512,35.6,36.25,35.45,35.8,339318,36.51,-1.95,36.67,37.38,0.7
20260513,35.8,36.7,35.1,35.2,307140,36.4,-3.31,36.7,37.3,0.63
20260514,35.35,35.95,35.05,35.15,288079,36.3,-3.17,36.63,37.2,0.62
20260515,35.9,37.85,35.9,36.25,1127785,36.29,-0.12,36.56,37.14,2.51
20260518,36.25,36.25,35.35,35.7,319941,36.25,-1.5,36.45,37.09,0.73
20260519,35.9,36,35.15,35.2,250853,36.16,-2.65,36.32,37.02,0.59
20260520,35.55,36.05,35.3,35.3,219150,36.09,-2.18,36.21,36.95,0.52
20260521,35.7,36.6,35.7,36.35,435256,36.11,0.67,36.11,36.89,1.04
20260522,36.8,36.8,36,36.35,277952,36.13,0.61,36.06,36.82,0.68
20260525,36.8,37.1,35.3,35.75,613544,36.1,-0.96,36.02,36.74,1.44
20260526,35.6,36,35.1,35.1,435031,36.01,-2.54,35.97,36.66,1
20260527,35.35,35.35,34.35,34.4,518544,35.88,-4.12,35.94,36.56,1.19
20260528,35.25,36.3,35.05,35.75,692892,35.87,-0.33,35.97,36.48,1.5
20260529,36.35,37.85,36.3,36.35,957494,35.91,1.23,36.03,36.42,1.94
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 38.2
- over_600_ratio: 35.42
- over_800_ratio: 33.41
- over_1000_ratio: 33.41
- over_400_change_1w: 0.2
- over_800_change_1w: 0.07
- over_1000_change_1w: 0.07
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,36.99,,33.19,,33.19,,0,False,False
20260508,37.98,0.99,33.2,0.01,33.2,0.01,1,True,True
20260515,38,0.02,33.34,0.14,33.34,0.14,2,True,True
20260522,38.2,0.2,33.41,0.07,33.41,0.07,3,True,True
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
