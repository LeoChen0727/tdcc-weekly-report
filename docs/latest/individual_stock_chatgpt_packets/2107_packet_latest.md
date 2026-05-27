# INDIVIDUAL STOCK CHATGPT PACKET - 2107 厚生

## Metadata
- generated_at: 2026-05-27 21:26:26 Asia/Taipei
- stock_id: 2107
- stock_name: 厚生
- packet_status: standard_180d_window_packet
- latest_price_date: 20260527
- price_rows: 135
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2107_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2107_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2107_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2107_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2107_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2107_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2107_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2107_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2107_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2107_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2107_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2107_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2107_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2107_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2107_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2107_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2107_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2107_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2107.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2107.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2107.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2107.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2107.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2107.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2107_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2107_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2107_latest.md?ref=main

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
- date: 20260527
- open: 24.8
- high: 24.8
- low: 24.6
- close: 24.75
- volume: 360266
- ma5: 24.99
- ema23_primary: 25.41
- distance_to_ema23_pct: -2.59
- ma20: 25.58
- ma60: 25.49
- ma120: 25.07
- return_5d: -1.79
- return_20d: -5.35
- volume_ratio: 1.03
- distance_to_ma20_pct_auxiliary: -3.24
- distance_to_high_60_pct: -6.78

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,26.15,26.4,26.05,26.15,307067,25.79,1.41,25.79,25.37,0.99
20260430,26.15,26.3,26.05,26.25,248067,25.83,1.64,25.84,25.39,0.79
20260504,26.35,26.5,26.15,26.2,401700,25.86,1.33,25.89,25.41,1.23
20260505,26.15,26.2,26,26.1,159404,25.88,0.86,25.92,25.42,0.49
20260506,26.2,26.3,26,26.1,261697,25.9,0.79,25.96,25.43,0.78
20260507,26.05,26.5,26.05,26.5,541723,25.95,2.14,26.01,25.45,1.54
20260508,26.5,26.55,26.1,26.1,304467,25.96,0.54,26.04,25.47,0.85
20260511,26.1,26.2,26.05,26.05,177572,25.97,0.32,26.06,25.49,0.5
20260512,26.05,26.15,25.95,25.95,273621,25.96,-0.06,26.07,25.5,0.79
20260513,25.95,25.95,25.25,25.25,950034,25.91,-2.53,26.05,25.51,2.5
20260514,25.35,25.6,25.35,25.45,367215,25.87,-1.61,26.03,25.52,0.96
20260515,25.55,25.55,25.1,25.2,507728,25.81,-2.37,25.98,25.53,1.32
20260518,25.1,25.2,24.8,24.85,422377,25.73,-3.43,25.93,25.53,1.09
20260519,24.85,25.3,24.85,25.25,187493,25.69,-1.72,25.89,25.54,0.49
20260520,25.15,25.3,25.1,25.2,215419,25.65,-1.76,25.86,25.54,0.57
20260521,25.1,25.35,25.1,25.25,248828,25.62,-1.43,25.81,25.54,0.69
20260522,25.25,25.4,25.2,25.25,288058,25.59,-1.32,25.76,25.53,0.82
20260525,25.25,25.25,24.85,24.9,504764,25.53,-2.47,25.7,25.52,1.46
20260526,24.9,24.9,24.7,24.8,290192,25.47,-2.63,25.65,25.51,0.84
20260527,24.8,24.8,24.6,24.75,360266,25.41,-2.59,25.58,25.49,1.03
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.14
- over_600_ratio: 58.21
- over_800_ratio: 56.68
- over_1000_ratio: 56.08
- over_400_change_1w: 0.04
- over_800_change_1w: 0.2
- over_1000_change_1w: 0.47
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.25,,55.75,,55.15,,0,False,False
20260508,60.66,0.41,56.19,0.44,55.32,0.17,1,True,True
20260515,61.1,0.44,56.48,0.29,55.61,0.29,2,True,True
20260522,61.14,0.04,56.68,0.2,56.08,0.47,3,True,True
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
