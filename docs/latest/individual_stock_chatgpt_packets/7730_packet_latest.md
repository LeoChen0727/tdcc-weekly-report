# INDIVIDUAL STOCK CHATGPT PACKET - 7730 暉盛-創

## Metadata
- generated_at: 2026-05-29 19:33:49 Asia/Taipei
- stock_id: 7730
- stock_name: 暉盛-創
- packet_status: standard_180d_window_packet
- latest_price_date: 20260529
- price_rows: 136
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7730_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7730_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7730_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7730_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7730_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7730_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7730_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7730_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7730_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7730_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7730_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7730_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7730_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7730_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7730_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7730_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7730_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7730_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7730.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7730.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7730.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7730.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7730.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7730.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7730_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7730_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7730_latest.md?ref=main

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
- open: 215.5
- high: 216.5
- low: 210
- close: 213.5
- volume: 79623
- ma5: 214.9
- ema23_primary: 197.61
- distance_to_ema23_pct: 8.04
- ma20: 194.15
- ma60: 171.88
- ma120: 133.43
- return_5d: -7.17
- return_20d: 31.79
- volume_ratio: 0.45
- distance_to_ma20_pct_auxiliary: 9.97
- distance_to_high_60_pct: -12.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260504,166.5,166.5,161,162.5,51431,168.35,-3.48,177.07,141.89,0.52
20260505,168,168,164,167,34023,168.24,-0.74,177.05,142.98,0.35
20260506,172,172.5,166.5,166.5,23614,168.09,-0.95,176.78,144.09,0.26
20260507,167,172.5,166.5,169.5,61601,168.21,0.77,175.9,145.26,0.74
20260508,178.5,178.5,168,168,119223,168.19,-0.12,174.45,146.4,1.53
20260511,168,182,168,181,121329,169.26,6.94,174.15,147.83,1.54
20260512,184,185,175,175,82200,169.74,3.1,173.43,149.12,1.04
20260513,175,175,170,171,49053,169.84,0.68,172.47,150.29,0.64
20260514,171,173,169,171,27322,169.94,0.62,171.47,151.47,0.37
20260515,173,188,173,181,248303,170.86,5.93,170.97,152.82,2.98
20260518,177,199,176,199,368718,173.21,14.89,172.3,154.49,4.01
20260519,218.5,218.5,218.5,218.5,172736,176.98,23.46,174.28,156.44,1.87
20260520,239,239.5,222.5,226,479936,181.07,24.82,176.68,158.5,4.26
20260521,231.5,231.5,211.5,222.5,266492,184.52,20.58,178.8,160.5,2.18
20260522,227,244.5,227,230,634782,188.31,22.14,181.62,162.65,4.18
20260525,225,229,207.5,219,271730,190.87,14.74,184.07,164.65,1.7
20260526,220.5,225.5,215.5,216,130787,192.96,11.94,186.7,166.58,0.81
20260527,212,214.5,209,212,155242,194.55,8.97,189.12,168.45,0.93
20260528,213,224,210.5,214,134789,196.17,9.09,191.57,170.18,0.78
20260529,215.5,216.5,210,213.5,79623,197.61,8.04,194.15,171.88,0.45
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 70.66
- over_600_ratio: 65.27
- over_800_ratio: 63.62
- over_1000_ratio: 61.18
- over_400_change_1w: -1.37
- over_800_change_1w: -2.93
- over_1000_change_1w: -0.39
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.29,,66.74,,61.57,,0,False,False
20260508,72.09,-0.2,66.54,-0.2,61.56,-0.01,0,False,False
20260515,72.03,-0.06,66.55,0.01,61.57,0.01,1,False,True
20260522,70.66,-1.37,63.62,-2.93,61.18,-0.39,0,False,False
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
