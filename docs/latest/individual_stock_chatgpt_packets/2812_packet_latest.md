# INDIVIDUAL STOCK CHATGPT PACKET - 2812 台中銀

## Metadata
- generated_at: 2026-05-26 23:00:56 Asia/Taipei
- stock_id: 2812
- stock_name: 台中銀
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2812_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2812_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2812_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2812_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2812_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2812_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2812_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2812_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2812_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2812_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2812_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2812_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2812_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2812_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2812_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2812_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2812_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2812_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2812.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2812.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2812.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2812.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2812.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2812.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2812_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2812_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2812_latest.md?ref=main

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
- open: 18.75
- high: 18.95
- low: 18.7
- close: 18.85
- volume: 10409943
- ma5: 18.89
- ema23_primary: 19.42
- distance_to_ema23_pct: -2.91
- ma20: 19.39
- ma60: 20.18
- ma120: 20.49
- return_5d: -1.57
- return_20d: -4.8
- volume_ratio: 0.58
- distance_to_ma20_pct_auxiliary: -2.77
- distance_to_high_60_pct: -11.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,19.8,20.1,19.6,20.1,12052520,20.45,-1.71,20.57,20.51,0.86
20260429,20.15,20.15,19.9,20,7860331,20.41,-2.02,20.55,20.5,0.56
20260430,20,20.05,19.75,19.85,12995569,20.36,-2.53,20.51,20.49,0.93
20260504,19.85,19.95,19.8,19.8,14606899,20.32,-2.55,20.46,20.48,1.03
20260505,19.8,19.8,19.7,19.8,13724186,20.27,-2.34,20.41,20.47,0.94
20260506,19.8,19.8,19.65,19.75,16516759,20.23,-2.38,20.35,20.46,1.13
20260507,19.8,19.8,19.6,19.7,19482807,20.19,-2.41,20.28,20.46,1.3
20260508,19.85,19.95,19.75,19.75,14905785,20.15,-1.99,20.22,20.45,0.96
20260511,19.8,19.8,19.65,19.75,13989928,20.12,-1.82,20.15,20.45,0.89
20260512,19.8,19.8,19.6,19.6,16289285,20.07,-2.36,20.09,20.44,1.03
20260513,19.45,19.45,19.3,19.45,28174558,20.02,-2.86,20.03,20.43,1.71
20260514,19.3,19.4,18.9,19,47828257,19.94,-4.7,19.95,20.41,2.59
20260515,18.95,18.95,18.55,18.75,47741218,19.84,-5.48,19.85,20.38,2.34
20260518,18.55,18.9,18.5,18.85,21964043,19.76,-4.58,19.77,20.36,1.06
20260519,18.85,19.3,18.7,19.15,16848788,19.7,-2.82,19.7,20.33,0.81
20260520,19.15,19.15,18.9,18.9,10579347,19.64,-3.76,19.62,20.31,0.51
20260521,18.95,19.05,18.9,19,7968092,19.58,-2.99,19.55,20.28,0.39
20260522,19,19.05,18.9,18.95,9345144,19.53,-2.98,19.5,20.25,0.48
20260525,19,19,18.75,18.75,13345189,19.47,-3.68,19.43,20.22,0.71
20260526,18.75,18.95,18.7,18.85,10409943,19.42,-2.91,19.39,20.18,0.58
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.79
- over_600_ratio: 56.22
- over_800_ratio: 54.66
- over_1000_ratio: 53.69
- over_400_change_1w: -0.22
- over_800_change_1w: -0.19
- over_1000_change_1w: -0.12
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.56,,55.62,,54.68,,0,False,False
20260508,59.24,-0.32,55.3,-0.32,54.31,-0.37,0,False,False
20260515,59.01,-0.23,54.85,-0.45,53.81,-0.5,0,False,False
20260522,58.79,-0.22,54.66,-0.19,53.69,-0.12,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2812 | 台中銀 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 2812 | 台中銀 | 4 | 4 | 4 | 4 | 4 | stale_signal | 反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。 |

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
