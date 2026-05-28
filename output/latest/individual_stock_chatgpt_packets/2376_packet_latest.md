# INDIVIDUAL STOCK CHATGPT PACKET - 2376 技嘉

## Metadata
- generated_at: 2026-05-28 19:31:53 Asia/Taipei
- stock_id: 2376
- stock_name: 技嘉
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
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/2376_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2376_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2376_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2376_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2376_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2376_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2376_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2376_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2376_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/2376_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2376_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2376_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2376_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2376_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2376_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/2376_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2376_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2376_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2376.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/2376.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2376.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2376.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/2376.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2376.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2376_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2376_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2376_latest.md?ref=main

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
- open: 336
- high: 350
- low: 331
- close: 337.5
- volume: 17174957
- ma5: 333
- ema23_primary: 311.28
- distance_to_ema23_pct: 8.42
- ma20: 314.5
- ma60: 270.06
- ma120: 254.43
- return_5d: 6.64
- return_20d: 23.85
- volume_ratio: 1.01
- distance_to_ma20_pct_auxiliary: 7.31
- distance_to_high_60_pct: -3.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260430,273,280,271,273,5636066,265.8,2.71,266.35,243.38,0.58
20260504,278,282,270.5,279,6508646,266.9,4.53,268.7,244.06,0.66
20260505,279,281,275.5,279.5,4539828,267.95,4.31,271.27,244.68,0.46
20260506,283,304.5,283,301,24158935,270.7,11.19,275.2,245.68,2.2
20260507,311,316.5,300.5,309,24537224,273.89,12.82,278.43,246.82,2.1
20260508,316,323.5,304.5,317,21918327,277.49,14.24,281.73,248.15,1.8
20260511,329,333,317,324.5,20716173,281.4,15.31,284.82,249.68,1.67
20260512,327.5,329,315,321,12394600,284.7,12.75,287.68,251.23,0.99
20260513,317.5,318,310.5,313.5,12824543,287.1,9.19,290.18,252.66,1.01
20260514,322.5,332,320,327,16985216,290.43,12.59,292.57,254.29,1.39
20260515,330,332,315,326.5,20435886,293.43,11.27,294.85,255.97,1.64
20260518,336,351,328,330.5,39137868,296.52,11.46,297.3,257.68,2.82
20260519,320,324,304.5,305,33752266,297.23,2.61,298.6,259.03,2.23
20260520,309,313.5,300,302,13967293,297.63,1.47,299.27,260.29,0.93
20260521,308,319.5,305,316.5,15510557,299.2,5.78,300.85,261.74,1.01
20260522,318.5,325,311.5,322.5,13226599,301.14,7.09,303.23,263.33,0.85
20260525,331.5,343,331,336.5,17128036,304.09,10.66,306.15,265.14,1.06
20260526,340,340.5,330,336,11025246,306.75,9.54,308.7,266.82,0.67
20260527,341,341,331,332.5,9035273,308.89,7.64,311.25,268.38,0.55
20260528,336,350,331,337.5,17174957,311.28,8.42,314.5,270.06,1.01
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 69.87
- over_600_ratio: 67.4
- over_800_ratio: 65.42
- over_1000_ratio: 63.5
- over_400_change_1w: -0.19
- over_800_change_1w: -0.37
- over_1000_change_1w: -0.66
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.49,,63.37,,61.37,,0,False,False
20260508,69.35,1.86,65.49,2.12,63.36,1.99,1,True,True
20260515,70.06,0.71,65.79,0.3,64.16,0.8,2,True,True
20260522,69.87,-0.19,65.42,-0.37,63.5,-0.66,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2376 | 技嘉 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260528 | 2376 | 技嘉 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | no_signal | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2376 | 技嘉 | 6 | 6 | 5 | 6 | 6 | repeated_but_no_breakout | 近 10 日上榜 6 日、近 20 日上榜 6 日，尚未突破，需分辨醞釀或鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 2376 | 技嘉 | 102 | 2 | 22826610.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
