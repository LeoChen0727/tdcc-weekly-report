# INDIVIDUAL STOCK CHATGPT PACKET - 2905 三商

## Metadata
- generated_at: 2026-05-26 21:25:16 Asia/Taipei
- stock_id: 2905
- stock_name: 三商
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 133
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2905_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2905_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2905_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2905_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2905_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2905_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2905_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2905_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2905_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2905_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2905_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2905_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2905_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2905_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2905_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2905_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2905_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2905_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2905.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2905.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2905.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2905.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2905.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2905.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2905_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2905_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2905_latest.md?ref=main

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
- open: 13.5
- high: 13.75
- low: 13.5
- close: 13.65
- volume: 368343
- ma5: 13.5
- ema23_primary: 13.62
- distance_to_ema23_pct: 0.23
- ma20: 13.46
- ma60: 14.35
- ma120: 15.12
- return_5d: 2.63
- return_20d: -1.09
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: 1.37
- distance_to_high_60_pct: -17.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,13.85,13.9,13.7,13.9,459308,14.41,-3.52,14.4,15,0.63
20260429,14,14,13.7,13.85,611639,14.36,-3.55,14.37,14.98,0.84
20260430,13.85,13.85,13.55,13.7,501327,14.31,-4.23,14.34,14.95,0.68
20260504,13.6,13.75,13.35,13.35,1119596,14.23,-6.16,14.28,14.91,1.47
20260505,13.35,13.45,13.25,13.45,547955,14.16,-5.02,14.23,14.87,0.71
20260506,13.6,13.6,13.35,13.5,541464,14.11,-4.3,14.18,14.84,0.7
20260507,13.5,13.65,13.45,13.5,658562,14.06,-3.95,14.12,14.8,0.84
20260508,13.6,13.75,13.5,13.65,398294,14.02,-2.65,14.07,14.77,0.51
20260511,13.65,13.7,13.3,13.35,648692,13.97,-4.41,14,14.75,0.82
20260512,13.35,13.45,13.25,13.25,457518,13.91,-4.72,13.95,14.71,0.61
20260513,13.25,13.35,13.2,13.35,504063,13.86,-3.68,13.88,14.68,0.69
20260514,13.4,13.55,13.3,13.35,406534,13.82,-3.38,13.81,14.65,0.56
20260515,13.35,13.4,13.05,13.05,708775,13.75,-5.11,13.73,14.61,1.02
20260518,13.35,13.35,13.15,13.25,754265,13.71,-3.36,13.67,14.58,1.12
20260519,13.35,13.45,13.25,13.3,400521,13.68,-2.76,13.62,14.54,0.6
20260520,13.25,13.4,13.2,13.35,490341,13.65,-2.2,13.55,14.51,0.78
20260521,13.35,13.4,13.25,13.35,459699,13.62,-2.02,13.51,14.47,0.76
20260522,13.55,13.95,13.55,13.65,839769,13.63,0.17,13.49,14.43,1.4
20260525,13.7,13.7,13.4,13.5,700193,13.62,-0.85,13.47,14.39,1.17
20260526,13.5,13.75,13.5,13.65,368343,13.62,0.23,13.46,14.35,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 83.88
- over_600_ratio: 82.24
- over_800_ratio: 80.93
- over_1000_ratio: 80.16
- over_400_change_1w: 0
- over_800_change_1w: -0.23
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,83.82,,81.1,,80.14,,0,False,False
20260508,83.88,0.06,81.14,0.04,80.09,-0.05,1,False,True
20260515,83.88,0,81.16,0.02,80.13,0.04,2,False,True
20260522,83.88,0,80.93,-0.23,80.16,0.03,3,False,True
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
