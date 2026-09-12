# INDIVIDUAL STOCK CHATGPT PACKET - 8070 長華*

## Metadata
- generated_at: 2026-09-12 22:17:58 Asia/Taipei
- stock_id: 8070
- stock_name: 長華*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8070_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8070_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8070_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8070_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8070_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8070_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8070_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8070_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8070_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8070_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8070_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8070_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8070.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8070.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8070.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8070.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8070_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8070_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8070_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260911
- open: 48.9
- high: 49.25
- low: 48.6
- close: 49
- volume: 1242250
- ma5: 49.64
- ema23_primary: 49.76
- distance_to_ema23_pct: -1.53
- ma20: 50.23
- ma60: 50.47
- ma120: 49.81
- return_5d: -2.97
- return_20d: -1.31
- volume_ratio: 0.29
- distance_to_ma20_pct_auxiliary: -2.45
- distance_to_high_60_pct: -19.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,50,51.6,49.1,49.5,2732076,48.59,1.88,47.15,52.11,1.01
20260818,49.3,54.4,49.15,54.4,13023416,49.07,10.86,47.5,52.27,4.08
20260819,53.8,54.5,50.9,51,22770769,49.23,3.59,47.6,52.34,5.46
20260820,52.3,52.7,48.85,50.2,10682175,49.31,1.8,47.7,52.35,2.33
20260821,50,50,48.7,48.8,3019561,49.27,-0.95,47.75,52.33,0.65
20260824,48.55,50.1,48.55,49,2059235,49.25,-0.5,47.84,52.3,0.45
20260825,49,49.4,47.8,49.3,1968286,49.25,0.1,48.09,52.24,0.43
20260826,49.8,52.2,49.65,51.3,4085266,49.42,3.8,48.55,52.22,0.91
20260827,51.6,51.8,50.7,50.7,2041840,49.53,2.36,49.01,52.1,0.46
20260828,51.1,53.9,50.8,51.4,5604465,49.68,3.45,49.3,51.95,1.24
20260831,50.9,51,49.5,50.2,3101741,49.73,0.95,49.46,51.7,0.68
20260901,50.2,50.8,50.1,50.3,1384859,49.78,1.05,49.63,51.5,0.31
20260902,50,51.2,49.8,50.6,1705588,49.84,1.52,49.8,51.35,0.38
20260903,50.8,51.1,49.2,49.2,1829131,49.79,-1.19,49.9,51.18,0.41
20260904,49.7,50.7,49.3,50.5,1640539,49.85,1.3,50.05,51.06,0.37
20260907,51.1,51.2,49.9,49.9,1655755,49.85,0.09,50.11,50.91,0.37
20260908,50.4,50.6,49.2,50,2123393,49.87,0.27,50.18,50.79,0.48
20260909,50.1,50.8,49.85,49.85,1221478,49.86,-0.03,50.24,50.67,0.28
20260910,49.85,50.1,49.45,49.45,1251187,49.83,-0.76,50.26,50.57,0.28
20260911,48.9,49.25,48.6,49,1242250,49.76,-1.53,50.23,50.47,0.29
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 73.51
- over_600_ratio: 72.29
- over_800_ratio: 70.82
- over_1000_ratio: 69.36
- over_400_change_1w: -0.09
- over_800_change_1w: 0.15
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,74.12,-1.12,71.38,-1.32,70.13,-1.32,0,False,False
20260703,74.13,0.01,71.43,0.05,70.19,0.06,1,True,True
20260709,74.03,-0.1,71.52,0.09,70.27,0.08,2,False,True
20260717,73.78,-0.25,71.14,-0.38,70.15,-0.12,0,False,False
20260724,73.11,-0.67,70.54,-0.6,69.69,-0.46,0,False,False
20260731,73.05,-0.06,69.81,-0.73,68.8,-0.89,0,False,False
20260807,73.28,0.23,70.05,0.24,69.18,0.38,1,True,True
20260814,73.2,-0.08,70.21,0.16,69.49,0.31,2,False,True
20260821,73.42,0.22,70.44,0.23,69.58,0.09,3,True,True
20260828,73.62,0.2,70.58,0.14,69.49,-0.09,4,False,True
20260904,73.6,-0.02,70.67,0.09,69.19,-0.3,5,False,True
20260911,73.51,-0.09,70.82,0.15,69.36,0.17,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8070 | 長華* | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.證券名稱: 頎邦科技股份有限公司普通股 2.交易日期:115/6/4~115/9/9 3.董事會通過日期: 民國115年6月12日 4.其他核決日期: 核決層級:董事長核決 民國115年6月1日 5.交易數量、每單位價格及交易總金額: (1)交易數量：1,475,000股 (2)每單位價格：平均每股206.02元 (3)交易總金額：303,875千元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益204,485千元 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: (1)累積持有股數：30,655千股 (2)累積持有金額：2,043,997千元 (3)持股比例：4.12% (4)權利受限情形：無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: (1)占公司最近期財務報表總資產比例：116.06 % (2)於母公司業主之權益比例：113.53% (3)財務報表營運資金：5,976,847千元 10.取得或處分之具體目的: 實現資本利得，有助整體股東權益 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 無 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 1.115/6/4至115/6/11之處分，係依115/6/1董事長不超過新台幣3億元額度授權辦理；   115/6/12至115/9/9之處分，係依115/6/12董事會決議辦理，並已於115/6/12公告。 2.115/6/12董事會決議授權處分頎邦（6147）普通股股票不超過10,000,000股，   得分次處分，預計交易期間為115年6月12日起一年內： (1) 截至115/9/9止執行率：10.75% (2) 預估本次授權處分完畢後累積持有股數：21,730千股 (3) 預估本次授權處分完畢後累積持有金額：新台幣1,448,956千元 (4) 預估本次授權處分完畢後持股比例：2.92%；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8070 | 長華* | 29 | 7 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8070 | 長華* | 20 | 0 | 97120.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
