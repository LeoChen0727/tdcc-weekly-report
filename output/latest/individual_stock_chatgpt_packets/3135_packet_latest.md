# INDIVIDUAL STOCK CHATGPT PACKET - 3135 凌航

## Metadata
- generated_at: 2026-05-27 21:26:58 Asia/Taipei
- stock_id: 3135
- stock_name: 凌航
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3135_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3135_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3135_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3135_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3135_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3135_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3135_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3135_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3135_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3135_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3135_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3135_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3135_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3135_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3135_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3135_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3135_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3135_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3135.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3135.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3135.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3135.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3135.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3135.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3135_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3135_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3135_latest.md?ref=main

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
- open: 245
- high: 245
- low: 230
- close: 242
- volume: 3745800
- ma5: 217.5
- ema23_primary: 189.32
- distance_to_ema23_pct: 27.83
- ma20: 192.65
- ma60: 144.42
- ma120: 118.02
- return_5d: 27.03
- return_20d: 72.86
- volume_ratio: 0.52
- distance_to_ma20_pct_auxiliary: 25.62
- distance_to_high_60_pct: -1.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260429,138,154,137,144.5,16166985,125.59,15.06,121,119.72,3.5
20260430,145,146.5,137.5,141.5,7369306,126.92,11.49,122.97,119.98,1.55
20260504,154,155.5,145.5,155.5,12562088,129.3,20.26,125.42,120.55,2.35
20260505,158,170,157.5,163,14912139,132.11,23.39,128.35,121.18,2.47
20260506,173.5,176,163,172.5,11565930,135.47,27.33,131.78,122.04,1.76
20260507,173,174,165,169.5,7692167,138.31,22.55,134.55,122.82,1.12
20260508,164.5,185,156.5,177,11066363,141.53,25.06,137.75,123.78,1.5
20260511,194.5,194.5,194.5,194.5,2046323,145.95,33.27,141.7,125.04,0.28
20260512,209,213.5,208,213.5,6047746,151.58,40.85,146.57,126.71,0.79
20260513,213.5,218,204,211,17155118,156.53,34.8,150.95,128.43,2.03
20260514,220,227.5,206,220.5,10454721,161.86,36.23,155.72,130.29,1.18
20260515,240,240.5,214,216,9573342,166.37,29.83,160.43,132.12,1.03
20260518,206.5,210,199.5,208,2225043,169.84,22.47,164.88,133.86,0.24
20260519,203,206,187.5,188,2875439,171.35,9.71,168.62,135.09,0.31
20260520,191,194.5,181,190.5,1787495,172.95,10.15,171.95,136.38,0.2
20260521,199.5,200,195,195.5,1268106,174.83,11.82,175.07,137.73,0.15
20260522,199.5,214,199,211.5,1785665,177.88,18.9,179.18,139.37,0.22
20260525,210,214.5,203,213.5,1982348,180.85,18.05,183.22,140.85,0.25
20260526,219,225.5,219,225,2615871,184.53,21.93,187.55,142.47,0.35
20260527,245,245,230,242,3745800,189.32,27.83,192.65,144.42,0.52
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 55.94
- over_600_ratio: 53.36
- over_800_ratio: 50.64
- over_1000_ratio: 45.68
- over_400_change_1w: -1.05
- over_800_change_1w: -0.9
- over_1000_change_1w: 0.94
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.64,,51.92,,46.97,,0,False,False
20260508,52.82,-2.82,50.51,-1.41,46.46,-0.51,0,False,False
20260515,56.99,4.17,51.54,1.03,44.74,-1.72,1,False,True
20260522,55.94,-1.05,50.64,-0.9,45.68,0.94,2,False,True
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
