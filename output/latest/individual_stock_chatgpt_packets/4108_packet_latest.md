# INDIVIDUAL STOCK CHATGPT PACKET - 4108 懷特

## Metadata
- generated_at: 2026-05-29 19:32:45 Asia/Taipei
- stock_id: 4108
- stock_name: 懷特
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4108_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4108_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4108_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4108_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4108_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4108_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4108_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4108_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4108_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4108_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4108_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4108_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4108_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4108_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4108_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4108_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4108_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4108_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4108.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4108.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4108.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4108.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4108.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4108.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4108_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4108_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4108_latest.md?ref=main

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
- open: 12.55
- high: 12.6
- low: 12.3
- close: 12.4
- volume: 192577
- ma5: 12.4
- ema23_primary: 12.25
- distance_to_ema23_pct: 1.23
- ma20: 12.1
- ma60: 12.62
- ma120: 13.28
- return_5d: -3.88
- return_20d: 1.22
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: 2.52
- distance_to_high_60_pct: -11.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,12.25,12.35,12.2,12.2,206588,12.58,-3,12.48,13.28,0.9
20260505,12.2,12.2,12,12.15,289590,12.54,-3.13,12.46,13.25,1.2
20260506,12.15,12.2,12,12.15,187707,12.51,-2.87,12.44,13.2,0.77
20260507,12.1,12.2,12,12,118626,12.47,-3.75,12.4,13.16,0.51
20260508,12,12.25,12,12.1,213286,12.44,-2.71,12.38,13.12,0.89
20260511,12.1,12.1,12,12.1,220047,12.41,-2.49,12.36,13.09,0.91
20260512,12,12,11.8,11.8,309629,12.36,-4.51,12.33,13.05,1.25
20260513,11.8,12,11.8,11.95,187974,12.32,-3.03,12.32,13.02,0.77
20260514,11.95,11.95,11.7,11.75,356903,12.28,-4.28,12.29,12.98,1.43
20260515,11.8,11.8,11.7,11.7,183647,12.23,-4.32,12.22,12.95,0.82
20260518,11.65,11.65,11.4,11.55,226928,12.17,-5.11,12.16,12.91,1.03
20260519,11.55,11.6,11.5,11.55,183031,12.12,-4.7,12.12,12.87,0.83
20260520,11.6,12.65,11.6,12,518269,12.11,-0.91,12.09,12.83,2.21
20260521,12.1,12.25,11.95,12,267695,12.1,-0.83,12.05,12.79,1.15
20260522,12.45,13.15,12.4,12.9,949991,12.17,6.02,12.08,12.76,3.58
20260525,13.15,13.15,12.35,12.55,584761,12.2,2.88,12.08,12.73,2.04
20260526,12.4,12.4,12.15,12.25,241363,12.2,0.38,12.08,12.7,0.85
20260527,12.45,12.45,12.2,12.25,287143,12.21,0.35,12.08,12.67,0.99
20260528,12.5,12.7,12.5,12.55,295489,12.24,2.57,12.09,12.64,0.99
20260529,12.55,12.6,12.3,12.4,192577,12.25,1.23,12.1,12.62,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 29.87
- over_600_ratio: 27.04
- over_800_ratio: 25.61
- over_1000_ratio: 23.76
- over_400_change_1w: 0.09
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.09
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,29.72,,25.46,,23.61,,0,False,False
20260508,29.72,0,25.46,0,23.61,0,0,False,False
20260515,29.78,0.06,25.52,0.06,23.67,0.06,1,True,True
20260522,29.87,0.09,25.61,0.09,23.76,0.09,2,True,True
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
