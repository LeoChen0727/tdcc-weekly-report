# INDIVIDUAL STOCK CHATGPT PACKET - 6679 鈺太

## Metadata
- generated_at: 2026-05-28 19:33:27 Asia/Taipei
- stock_id: 6679
- stock_name: 鈺太
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6679_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6679_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6679_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6679_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6679_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6679_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6679_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6679_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6679_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6679_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6679_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6679_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6679_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6679_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6679_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6679_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6679_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6679_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6679.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6679.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6679.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6679.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6679.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6679.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6679_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6679_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6679_latest.md?ref=main

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
- open: 331
- high: 338
- low: 310
- close: 316.5
- volume: 648848
- ma5: 334.1
- ema23_primary: 312.29
- distance_to_ema23_pct: 1.35
- ma20: 316.9
- ma60: 274.65
- ma120: 229.79
- return_5d: -5.52
- return_20d: 11.64
- volume_ratio: 0.94
- distance_to_ma20_pct_auxiliary: -0.13
- distance_to_high_60_pct: -10.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,288,298,284,286,474000,267.36,6.97,267.7,235.51,0.86
20260504,295,295.5,285.5,290,615000,269.25,7.71,269.75,237.29,1.09
20260505,308,308,286,287,928000,270.73,6.01,271.88,238.93,1.55
20260506,294.5,309,292,302,1878000,273.33,10.49,274.68,240.82,2.78
20260507,305,316,297,312,1099000,276.56,12.82,277.57,242.88,1.56
20260508,314,343,312,331,1728000,281.09,17.75,281.57,245.32,2.26
20260511,325,332,315,327,797000,284.92,14.77,285.48,247.7,1.05
20260512,329,334.5,320.5,324.5,461000,288.22,12.59,288.85,250.17,0.61
20260513,321.5,327,315,320,374000,290.87,10.02,291.77,252.38,0.5
20260514,324,324,311,315,375000,292.88,7.55,294.18,254.39,0.51
20260515,315.5,322.5,305,305,475000,293.89,3.78,296.12,256.31,0.64
20260518,303,317.5,291.5,312.5,604000,295.44,5.78,297.95,258.39,0.82
20260519,306.5,314.5,305,306.5,350000,296.36,3.42,299.73,260.37,0.48
20260520,308,323.5,306,314,643000,297.83,5.43,301.02,262.42,0.9
20260521,324,337,321.5,335,988000,300.93,11.32,303.52,264.82,1.35
20260522,341,343.5,333.5,335.5,337000,303.81,10.43,306.3,267.02,0.49
20260525,338.5,350,337,345.5,344000,307.28,12.44,309.8,269.27,0.5
20260526,348,352.5,334.5,343,342000,310.26,10.55,313.2,271.47,0.5
20260527,342,345,327,330,336000,311.9,5.8,315.25,273.18,0.5
20260528,331,338,310,316.5,648848,312.29,1.35,316.9,274.65,0.94
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 61.64
- over_600_ratio: 54.86
- over_800_ratio: 53.42
- over_1000_ratio: 50.4
- over_400_change_1w: 0.56
- over_800_change_1w: -1.03
- over_1000_change_1w: 0.5
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.67,,53.85,,50.61,,0,False,False
20260508,61.09,1.42,53.2,-0.65,50.21,-0.4,1,False,False
20260515,61.08,-0.01,54.45,1.25,49.9,-0.31,2,False,True
20260522,61.64,0.56,53.42,-1.03,50.4,0.5,3,False,True
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
