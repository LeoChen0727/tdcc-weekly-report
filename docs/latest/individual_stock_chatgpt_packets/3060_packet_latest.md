# INDIVIDUAL STOCK CHATGPT PACKET - 3060 銘異

## Metadata
- generated_at: 2026-05-28 20:19:02 Asia/Taipei
- stock_id: 3060
- stock_name: 銘異
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/3060_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3060_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3060_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3060_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3060_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3060_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3060_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3060_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3060_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/3060_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3060_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3060_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3060_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3060_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3060_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/3060_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3060_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3060_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3060.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/3060.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3060.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3060.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/3060.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3060.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3060_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3060_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3060_latest.md?ref=main

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
- open: 29.8
- high: 30.1
- low: 28.45
- close: 28.7
- volume: 3731614
- ma5: 28.94
- ema23_primary: 28.4
- distance_to_ema23_pct: 1.04
- ma20: 28.09
- ma60: 29.34
- ma120: 30.71
- return_5d: 4.17
- return_20d: 1.41
- volume_ratio: 1.62
- distance_to_ma20_pct_auxiliary: 2.16
- distance_to_high_60_pct: -21.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,28,29.2,27.7,28.05,3036479,29.31,-4.29,29.27,30.66,1.02
20260504,28.25,28.45,27.6,27.85,1515443,29.19,-4.58,29.21,30.59,0.51
20260505,28.15,28.7,28.1,28.55,1542576,29.13,-2,29.21,30.52,0.54
20260506,29.25,29.4,28.05,28.15,1953854,29.05,-3.1,29.17,30.46,0.68
20260507,28.4,29.5,28.05,28.9,2487147,29.04,-0.48,29.1,30.37,0.87
20260508,29.3,29.7,27.8,28,2684914,28.95,-3.29,29.03,30.25,0.94
20260511,28.6,29.15,28.4,28.55,2387673,28.92,-1.27,28.98,30.13,0.83
20260512,28.95,29,28.05,28.55,1648102,28.89,-1.17,28.94,30.08,0.57
20260513,28.6,28.65,27.85,28.05,1357353,28.82,-2.66,28.78,30.03,0.48
20260514,28.3,29,27.65,27.8,2183668,28.73,-3.25,28.6,29.96,0.83
20260515,28.2,28.5,26.65,26.85,2450296,28.58,-6.04,28.41,29.91,0.92
20260518,26.5,27.1,26.15,26.95,1281123,28.44,-5.24,28.24,29.87,0.49
20260519,27.3,27.5,26.7,26.75,1166124,28.3,-5.48,28.06,29.8,0.45
20260520,27.05,27.3,26.5,26.6,858509,28.16,-5.53,27.87,29.75,0.34
20260521,27.2,27.6,26.95,27.55,1277801,28.11,-1.98,27.75,29.7,0.52
20260522,27.75,28.85,27.75,28.85,2515376,28.17,2.42,27.81,29.65,1.08
20260525,29.25,29.4,28.4,29,3144615,28.24,2.7,27.91,29.57,1.33
20260526,29.05,29.3,28.1,28.35,1791412,28.25,0.36,27.96,29.49,0.75
20260527,28.7,30.5,28.65,29.8,7140557,28.38,5.01,28.07,29.42,2.64
20260528,29.8,30.1,28.45,28.7,3731614,28.4,1.04,28.09,29.34,1.62
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 17.28
- over_600_ratio: 13.16
- over_800_ratio: 12.2
- over_1000_ratio: 11.49
- over_400_change_1w: 0.47
- over_800_change_1w: 0.05
- over_1000_change_1w: -0.66
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,17.11,,10.94,,10.25,,0,False,False
20260508,17.99,0.88,11.76,0.82,11.16,0.91,1,True,True
20260515,16.81,-1.18,12.15,0.39,12.15,0.99,2,False,True
20260522,17.28,0.47,12.2,0.05,11.49,-0.66,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3060 | 銘異 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 3060 | 銘異 | 3 | 1 | 3 | 3 | 3 | continued_2_3d | 連續 3 個交易日上榜，訊號延續但仍需確認。 |

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
