# INDIVIDUAL STOCK CHATGPT PACKET - 3036 文曄

## Metadata
- generated_at: 2026-05-28 19:32:14 Asia/Taipei
- stock_id: 3036
- stock_name: 文曄
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3036_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3036_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3036_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3036_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3036_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3036_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3036_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3036_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3036_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3036_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3036_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3036_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3036_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3036_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3036_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3036_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3036_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3036_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3036.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3036.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3036.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3036.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3036.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3036.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3036_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3036_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3036_latest.md?ref=main

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
- open: 299.5
- high: 299.5
- low: 289
- close: 289.5
- volume: 6314889
- ma5: 293.9
- ema23_primary: 264.3
- distance_to_ema23_pct: 9.54
- ma20: 261.55
- ma60: 236.56
- ma120: 194.14
- return_5d: -0.69
- return_20d: 42.61
- volume_ratio: 0.43
- distance_to_ma20_pct_auxiliary: 10.69
- distance_to_high_60_pct: -6.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,203,207.5,202.5,204,4991122,215.22,-5.21,218.88,204.77,0.67
20260504,206,213.5,206,210.5,10172435,214.83,-2.01,218.15,205.83,1.37
20260505,209.5,212,208,209,6083395,214.34,-2.49,217.4,206.86,0.83
20260506,214.5,219,211.5,214,13521901,214.31,-0.15,216.72,207.8,1.75
20260507,219,226,214,219,19016615,214.7,2,216,208.7,2.24
20260508,240.5,240.5,240.5,240.5,6029324,216.85,10.9,216.82,210.06,0.71
20260511,264.5,264.5,248,264.5,22384053,220.82,19.78,218.78,211.87,2.4
20260512,270,283,260,275.5,43177088,225.38,22.24,221.15,213.92,3.84
20260513,272.5,291.5,260,284,27419536,230.27,23.34,223.97,216.04,2.25
20260514,288,288,270,271.5,16745879,233.7,16.17,226.07,217.91,1.32
20260515,273,278,267,270,15102527,236.73,14.06,227.82,219.82,1.15
20260518,271,271,258.5,263.5,8558521,238.96,10.27,229.5,221.63,0.65
20260519,265,274.5,262,265,9225075,241.13,9.9,231.9,223.45,0.71
20260520,270.5,291.5,267.5,279,23525822,244.28,14.21,234.97,225.29,1.71
20260521,281,293,278.5,291.5,16763571,248.22,17.44,238.88,227.23,1.19
20260522,291,301.5,288.5,289,12509307,251.62,14.86,243.03,229.09,0.88
20260525,292,308,289,301.5,13776354,255.77,17.88,248.15,231.11,0.96
20260526,299,303.5,291.5,293.5,8573585,258.92,13.36,252.78,232.95,0.59
20260527,300,304.5,292.5,296,9274773,262.01,12.97,257.23,234.82,0.63
20260528,299.5,299.5,289,289.5,6314889,264.3,9.54,261.55,236.56,0.43
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 89.07
- over_600_ratio: 87.53
- over_800_ratio: 85.99
- over_1000_ratio: 84.51
- over_400_change_1w: -0.23
- over_800_change_1w: -0.21
- over_1000_change_1w: -0.35
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,89.37,,86.27,,84.28,,0,False,False
20260508,89.12,-0.25,86.14,-0.13,84.29,0.01,1,False,True
20260515,89.3,0.18,86.2,0.06,84.86,0.57,2,False,True
20260522,89.07,-0.23,85.99,-0.21,84.51,-0.35,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3036 | 文曄 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | no_signal | continued_overheated | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3036 | 文曄 | 3 | 3 | 3 | 3 | 3 | continued_overheated | 連續上榜但短期漲幅或乖離過熱，精華追蹤應降級。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3036 | 文曄 | 76 | 1 | 9466170.0 | 394400.0 | 24.0 | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
