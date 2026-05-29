# INDIVIDUAL STOCK CHATGPT PACKET - 4169 泰宗

## Metadata
- generated_at: 2026-05-29 19:32:48 Asia/Taipei
- stock_id: 4169
- stock_name: 泰宗
- packet_status: partial_rawdata_packet
- latest_price_date: 20260529
- price_rows: 37
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/4169_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/4169_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/4169_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4169_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4169_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4169_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4169_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4169_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4169_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/4169_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/4169_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/4169_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4169_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4169_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4169_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/4169_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/4169_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/4169_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4169.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/4169.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4169.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4169.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/4169.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4169.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4169_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4169_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4169_latest.md?ref=main

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
- open: 154.5
- high: 157.5
- low: 154
- close: 157
- volume: 130894
- ma5: 155.5
- ema23_primary: 155.34
- distance_to_ema23_pct: 1.07
- ma20: 154.5
- ma60: 158.07
- ma120: 158.07
- return_5d: -1.26
- return_20d: -2.79
- volume_ratio: 0.85
- distance_to_ma20_pct_auxiliary: 1.62
- distance_to_high_60_pct: -13.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,162,164,158.5,159.5,170233,159.05,0.28,162.11,162.11,0.31
20260505,159,163,156.5,160,127252,159.13,0.55,162,162,0.24
20260506,158.5,159.5,155,155,285504,158.79,-2.39,161.65,161.65,0.55
20260507,156.5,156.5,152.5,153,248635,158.31,-3.35,162.05,161.24,0.57
20260508,154,160,153.5,156,172403,158.11,-1.34,161.43,161,0.45
20260511,156,156.5,153,154,97623,157.77,-2.39,161.25,160.7,0.29
20260512,154,159,152,155.5,114977,157.58,-1.32,161.53,160.48,0.36
20260513,159,159,152,152,126202,157.12,-3.26,161.62,160.14,0.42
20260514,152,153,149.5,150,194113,156.52,-4.17,161.35,159.75,0.66
20260515,155,155,148,148.5,139789,155.85,-4.72,160.4,159.33,0.51
20260518,148.5,153.5,148,150.5,154308,155.41,-3.16,159.6,159.02,0.62
20260519,153.5,154.5,150,150,123199,154.96,-3.2,158.62,158.71,0.54
20260520,150,152,148.5,152,91421,154.71,-1.75,157.4,158.48,0.44
20260521,152,162,152,157.5,216382,154.94,1.65,156.68,158.45,1.1
20260522,158,161,157,159,134518,155.28,2.39,155.82,158.47,0.74
20260525,156,159,152,158.5,217243,155.55,1.9,155.4,158.47,1.24
20260526,158.5,158.5,155,155,93166,155.5,-0.32,155.15,158.37,0.58
20260527,155,155,152,152.5,124556,155.25,-1.77,154.9,158.2,0.79
20260528,157.5,157.5,152,154.5,131773,155.19,-0.45,154.72,158.1,0.85
20260529,154.5,157.5,154,157,130894,155.34,1.07,154.5,158.07,0.85
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 54.72
- over_600_ratio: 49.58
- over_800_ratio: 46.18
- over_1000_ratio: 46.18
- over_400_change_1w: 0.38
- over_800_change_1w: -1.42
- over_1000_change_1w: -0.09
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.72,,47.98,,47.98,,0,False,False
20260508,54.49,-0.23,47.75,-0.23,46.29,-1.69,0,False,False
20260515,54.34,-0.15,47.6,-0.15,46.27,-0.02,0,False,False
20260522,54.72,0.38,46.18,-1.42,46.18,-0.09,1,False,False
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
