# INDIVIDUAL STOCK CHATGPT PACKET - 4958 臻鼎-KY

## Metadata
- generated_at: 2026-10-04 22:17:45 Asia/Taipei
- stock_id: 4958
- stock_name: 臻鼎-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 366
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4958_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4958_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4958_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4958_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4958_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4958_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4958_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4958.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4958.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4958.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4958.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4958_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4958_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4958_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: breakout_initial
- entry_style: breakout_follow
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20261002
- open: 515
- high: 561
- low: 514
- close: 561
- volume: 69348102
- ma5: 510.4
- ema23_primary: 493.68
- distance_to_ema23_pct: 13.64
- ma20: 490.9
- ma60: 491.12
- ma120: 481.57
- return_5d: 18.6
- return_20d: 10.65
- volume_ratio: 2.24
- distance_to_ma20_pct_auxiliary: 14.28
- distance_to_high_60_pct: -14.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,520,525,462,464,40982476,480.55,-3.44,475.3,521.88,1.14
20260904,476,477.5,446.5,463,33930146,479.09,-3.36,474.8,521.23,0.94
20260907,472.5,508,469,501,34247775,480.91,4.18,476.32,520.77,0.95
20260908,516,524,500,505,33442577,482.92,4.57,477.07,519.98,0.93
20260909,508,515,502,502,18639881,484.51,3.61,478.6,518.52,0.54
20260910,504,512,493.5,494.5,16351309,485.34,1.89,479.45,516.36,0.5
20260911,482,504,478,495,18746769,486.15,1.82,479.73,513.96,0.61
20260914,480,498,475.5,489.5,18946773,486.43,0.63,479.05,511.42,0.64
20260915,485.5,493.5,476,477.5,19168557,485.68,-1.68,479.23,509.01,0.67
20260916,482.5,498,471,493.5,21886748,486.33,1.47,481.05,507.45,0.78
20260917,496,504,475,476,26008525,485.47,-1.95,481.7,505.6,0.92
20260918,486,491,472,473,29899628,484.43,-2.36,483.3,503.45,1.06
20260921,476.5,482,463.5,470,26718285,483.23,-2.74,485.02,501.62,0.92
20260922,480,505,480,489,45198008,483.71,1.09,487.27,500.22,1.48
20260923,471.5,482.5,470,473,39517300,482.82,-2.03,488.27,497.6,1.24
20260924,473.5,480.5,472,475.5,20619766,482.21,-1.39,488.2,495.48,0.66
20260929,479,499.5,472.5,498.5,41991459,483.57,3.09,489.1,493.82,1.32
20260930,510,510,494,507,30846660,485.52,4.42,489.45,492.05,1
20261001,512,522,498.5,510,31694640,487.56,4.6,488.2,490.9,1.1
20261002,515,561,514,561,69348102,493.68,13.64,490.9,491.12,2.24
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 71.09
- over_600_ratio: 68.98
- over_800_ratio: 67.58
- over_1000_ratio: 65.78
- over_400_change_1w: 0.89
- over_800_change_1w: 0.75
- over_1000_change_1w: 0.84
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,74.2,1.5,69.61,1.32,67.29,0.93,2,True,True
20260724,72.76,-1.44,68.25,-1.36,65.94,-1.35,0,False,False
20260731,73.19,0.43,68.75,0.5,66.66,0.72,1,True,True
20260807,72.84,-0.35,68.57,-0.18,66.7,0.04,2,False,True
20260814,71.39,-1.45,67.36,-1.21,65.54,-1.16,0,False,False
20260821,70.74,-0.65,66.69,-0.67,64.98,-0.56,0,False,False
20260828,70.78,0.04,66.93,0.24,65.14,0.16,1,True,True
20260904,70.95,0.17,67,0.07,65.2,0.06,2,True,True
20260911,71.15,0.2,67.43,0.43,65.78,0.58,3,True,True
20260918,71.33,0.18,67.66,0.23,65.72,-0.06,4,False,True
20260924,70.2,-1.13,66.83,-0.83,64.94,-0.78,0,False,False
20261002,71.09,0.89,67.58,0.75,65.78,0.84,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 4958 | 臻鼎-KY | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  | mixed_flow | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 1.淮安經濟技術開發區富景路東側工業用地 2.淮安經濟技術開發區保五路東側工業用地 2.事實發生日:115/10/1~115/10/1 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年10月01日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 1.淮安經濟技術開發區富景路東側工業用地   土地面積：63,253.3平方公尺   交易總金額：人民幣2,417萬元   每單位價格：約人民幣382.11元/每平方公尺  2.淮安經濟技術開發區保五路東側工業用地   土地面積：147,106.8平方公尺   交易總金額：人民幣5,458萬元   每單位價格：約人民幣371.02元/每平方公尺 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人：淮安市自然資源和規劃局 與公司之關係：無 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依合約規定辦理(使用權50年) 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 決定方式：招標 決策單位：依核決權限 12.專業估價者事務所或公司名稱及其估價金額: 估價公司名稱：江蘇清華房地產資產評估造價咨詢有限公司 估價金額： 1.淮安經濟技術開發區富景路東側工業用地：人民幣2,436.01萬元 2.淮安經濟技術開發區保五路東側工業用地：人民幣5,495.47萬元 13.專業估價師姓名: 王大朋、陸茂榮 14.專業估價師開業證書字號: 王大朋：3220180265 陸茂榮：3220100030 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 無 23.取得或處分之具體目的或用途: 營運發展使用 24.本次交易表示異議之董事之意見: 不適用 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: CNYTWD折算匯率4.7359；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 4958 | 臻鼎-KY | 16 | 1 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 4958 | 臻鼎-KY | 384 | 21 | 95551730.0 | 1920380.0 | 49.76 | mixed_flow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
