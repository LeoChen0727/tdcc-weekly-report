# INDIVIDUAL STOCK CHATGPT PACKET - 7769 鴻勁

## Metadata
- generated_at: 2026-05-26 22:20:38 Asia/Taipei
- stock_id: 7769
- stock_name: 鴻勁
- packet_status: standard_rawdata_packet
- latest_price_date: 20260526
- price_rows: 116
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: price history shorter than 120 rows; K-line context is partial; TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/7769_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7769_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7769_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7769_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7769_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7769_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7769_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7769_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7769_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/7769_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7769_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7769_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7769_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7769_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7769_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/7769_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7769_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7769_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7769.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/7769.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7769.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7769.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/7769.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7769.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7769_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7769_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7769_latest.md?ref=main

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
- open: 7560
- high: 8045
- low: 7560
- close: 7900
- volume: 296861
- ma5: 7586
- ema23_primary: 6461.89
- distance_to_ema23_pct: 22.26
- ma20: 6495.75
- ma60: 4960.42
- ma120: 4245.26
- return_5d: 19.7
- return_20d: 58.95
- volume_ratio: 0.28
- distance_to_ma20_pct_auxiliary: 21.62
- distance_to_high_60_pct: -1.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,5035,5140,4970,5100,1281018,4417.97,15.44,4311.25,4124.92,1.01
20260429,5105,5245,5060,5220,1310824,4484.81,16.39,4386.75,4152.33,1.02
20260430,5270,5285,4945,4945,1413854,4523.16,9.33,4458.75,4173.08,1.1
20260504,5140,5420,5030,5380,1639624,4594.56,17.09,4535,4200.58,1.25
20260505,5420,5635,5370,5600,1451459,4678.35,19.7,4623.25,4230.67,1.1
20260506,5690,5780,5435,5705,1442242,4763.9,19.75,4708,4262.83,1.07
20260507,5820,5900,5780,5835,758227,4853.16,20.23,4786.75,4296.92,0.57
20260508,5885,6040,5770,5800,1128305,4932.06,17.6,4864.5,4331.08,0.85
20260511,6000,6380,5805,6380,1484440,5052.73,26.27,4973.5,4374.92,1.08
20260512,6515,7000,6415,6870,2086975,5204.16,32.01,5112,4426.92,1.45
20260513,6840,7555,6840,7440,2412372,5390.48,38.02,5274.75,4486.67,1.62
20260514,7440,7995,7440,7560,675412,5571.28,35.7,5439.75,4549.25,0.46
20260515,7615,7615,6895,6895,881504,5681.59,21.36,5569.75,4602.42,0.6
20260518,6575,6975,6360,6655,768853,5762.71,15.48,5677.5,4651.83,0.55
20260519,6555,6780,6510,6600,420449,5832.48,13.16,5785.25,4697.67,0.31
20260520,6470,6995,6470,6980,453843,5928.11,17.74,5911,4747.33,0.34
20260521,7325,7675,7325,7675,339865,6073.68,26.36,6057.5,4802.83,0.27
20260522,7750,7785,7205,7730,567122,6211.71,24.44,6203.5,4858.33,0.48
20260525,7640,7785,7535,7645,374274,6331.15,20.75,6349.25,4909,0.33
20260526,7560,8045,7560,7900,296861,6461.89,22.26,6495.75,4960.42,0.28
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 68.01
- over_600_ratio: 63.49
- over_800_ratio: 60.35
- over_1000_ratio: 59.37
- over_400_change_1w: -0.23
- over_800_change_1w: -0.96
- over_1000_change_1w: -0.05
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.64,,61.33,,58.87,,0,False,False
20260508,68.29,-0.35,60.95,-0.38,58.56,-0.31,0,False,False
20260515,68.24,-0.05,61.31,0.36,59.42,0.86,1,False,True
20260522,68.01,-0.23,60.35,-0.96,59.37,-0.05,0,False,False
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
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 7769 | 鴻勁 | 24 | 0 | 6344330.0 | 0.0 |  | no_signal | 0 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
