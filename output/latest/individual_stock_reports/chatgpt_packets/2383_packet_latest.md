# INDIVIDUAL STOCK CHATGPT PACKET - 2383 台光電

## Metadata
- generated_at: 2026-08-22 22:26:53 Asia/Taipei
- stock_id: 2383
- stock_name: 台光電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2383_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2383_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2383_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2383_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2383_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2383_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2383_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2383_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2383_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2383_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2383_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2383_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2383.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2383.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2383.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2383.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2383_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2383_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2383_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: unclear
- entry_style: no_entry_now
- position_sizing: observe_only

### management_plan
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_tdcc_warning
- no_major_volume_price_failure
- acceptable_risk_reward

### post_entry_watch_items
- next_monthly_revenue
- next_tdcc_update
- 23ema_hold_or_reclaim
- volume_price_confirmation
- prior_high_breakout_quality
- sector_benchmark_strength
- event_follow_through
- warrant_overheat_check

### downgrade_reason
- none

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260821
- open: 6005
- high: 6015
- low: 5650
- close: 5680
- volume: 2568603
- ma5: 6020
- ema23_primary: 5504.38
- distance_to_ema23_pct: 3.19
- ma20: 5340.25
- ma60: 5222.67
- ma120: 4445.04
- return_5d: -7.87
- return_20d: 19.45
- volume_ratio: 1.03
- distance_to_ma20_pct_auxiliary: 6.36
- distance_to_high_60_pct: -12.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,4825,4890,4640,4815,1443744,5049.49,-4.64,5154.5,5059.08,0.67
20260728,4420,4690,4400,4410,2370592,4996.2,-11.73,5102.5,5056.83,1.07
20260729,4380,4475,3985,4100,3501983,4921.52,-16.69,5038,5045.92,1.5
20260730,4005,4510,3930,4315,5227758,4870.98,-11.41,4977,5039,2.05
20260731,4745,4745,4745,4745,1418920,4860.48,-2.38,4931.5,5035.58,0.55
20260803,5135,5195,4930,4980,4183768,4870.44,2.25,4876.5,5035.92,1.59
20260804,4995,5210,4875,5140,2925218,4892.9,5.05,4859.75,5042.42,1.13
20260805,5425,5425,5165,5245,2477774,4922.24,6.56,4861,5049,0.98
20260806,5200,5380,5105,5305,1863164,4954.14,7.08,4860.5,5055.75,0.75
20260807,5400,5400,5180,5240,1362847,4977.96,5.26,4857.75,5060.92,0.56
20260810,5330,5510,5230,5290,1972845,5003.96,5.72,4866,5067.08,0.8
20260811,5300,5535,5240,5535,2826640,5048.22,9.64,4894.25,5082.42,1.15
20260812,5500,5730,5480,5730,1635510,5105.03,12.24,4926.75,5102.17,0.66
20260813,5875,5875,5655,5690,1568694,5153.78,10.4,4961.75,5121.42,0.63
20260814,5790,6200,5770,6165,2986895,5238.05,17.7,5045.25,5150.92,1.2
20260817,6165,6445,6110,6350,1910755,5330.71,19.12,5143,5178.58,0.79
20260818,6350,6470,6170,6205,2005998,5403.57,14.83,5211.75,5198.58,0.85
20260819,5855,6130,5810,5880,3119237,5443.27,8.02,5249.5,5204.83,1.29
20260820,6100,6200,5780,5985,2514908,5488.42,9.05,5294,5216.42,1.02
20260821,6005,6015,5650,5680,2568603,5504.38,3.19,5340.25,5222.67,1.03
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 68.98
- over_600_ratio: 63.11
- over_800_ratio: 59.22
- over_1000_ratio: 56.33
- over_400_change_1w: -0.4
- over_800_change_1w: -0.89
- over_1000_change_1w: -0.82
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,68.82,-0.78,59.53,-0.15,56.23,-0.44,1,False,False
20260612,68.99,0.17,59.75,0.22,56.48,0.25,2,False,True
20260618,69.2,0.21,60.53,0.78,56.52,0.04,3,True,True
20260626,69.34,0.14,60.56,0.03,57.91,1.39,4,True,True
20260703,69.09,-0.25,60.84,0.28,57.96,0.05,5,False,True
20260709,69.13,0.04,60.29,-0.55,57.16,-0.8,6,False,False
20260717,69.24,0.11,61.03,0.74,57.95,0.79,7,True,True
20260724,69.43,0.19,61.02,-0.01,58.1,0.15,8,False,True
20260731,69.7,0.27,61.19,0.17,58.22,0.12,9,True,True
20260807,69.26,-0.44,60.36,-0.83,57.45,-0.77,0,False,False
20260814,69.38,0.12,60.11,-0.25,57.15,-0.3,1,False,False
20260821,68.98,-0.4,59.22,-0.89,56.33,-0.82,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2383 | 台光電 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | repeated_but_no_breakout | 1.契約種類:工程契約 2.事實發生日:115/8/20~115/8/20 3.董事會通過日期: 民國114年7月30日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 昆山博明工程有限公司 與公司關係：無 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 辦公樓裝修及機電工程案， 過去一年內累計向同一相對人發包工程價款累計金額折合新台幣約509,187仟元。 工程係依公司建造時程規劃發包。 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 營運所需 11.本次交易表示異議之董事意見: 不適用 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期: 1.民國 年 月 日 2.不適用，請寫原因 (以上文字請自行增刪) 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: ex_dividend on 20260828; status=confirmed; proximity=within_7d |
| 20260821 | 2383 | 台光電 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.契約種類:工程契約 2.事實發生日:115/8/20~115/8/20 3.董事會通過日期: 民國114年7月30日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 昆山博明工程有限公司 與公司關係：無 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 辦公樓裝修及機電工程案， 過去一年內累計向同一相對人發包工程價款累計金額折合新台幣約509,187仟元。 工程係依公司建造時程規劃發包。 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 營運所需 11.本次交易表示異議之董事意見: 不適用 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期: 1.民國 年 月 日 2.不適用，請寫原因 (以上文字請自行增刪) 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: ex_dividend on 20260828; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2383 | 台光電 | 1 | 1 | 4 | 9 | 16 | repeated_but_no_breakout | 近 10 日上榜 9 次、近 20 日上榜 16 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2383 | 台光電 | 65 | 8 | 5902190.0 | 3980.0 | 1482.96 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
