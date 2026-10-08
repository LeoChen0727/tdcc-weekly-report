# INDIVIDUAL STOCK CHATGPT PACKET - 8027 鈦昇

## Metadata
- generated_at: 2026-10-08 22:19:52 Asia/Taipei
- stock_id: 8027
- stock_name: 鈦昇
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 266
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8027_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8027_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8027_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8027_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8027_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8027_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8027_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8027_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8027_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8027_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8027_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8027_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8027.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8027.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8027.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8027.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8027_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8027_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8027_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- open: 210
- high: 217
- low: 207
- close: 213.5
- volume: 5264000
- ma5: 206.2
- ema23_primary: 187.84
- distance_to_ema23_pct: 13.66
- ma20: 183.28
- ma60: 187.26
- ma120: 204.45
- return_5d: 20.96
- return_20d: 17.31
- volume_ratio: 1.62
- distance_to_ma20_pct_auxiliary: 16.49
- distance_to_high_60_pct: -18.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,184,192.5,176.5,177,5860000,181.17,-2.3,178.3,202.74,2.53
20260904,178,186.5,173,181.5,3883000,181.2,0.17,178.78,201.96,1.61
20260907,185,186,180,185.5,2261000,181.55,2.17,178.95,201.19,0.93
20260908,181.5,187,175.5,177,3972000,181.18,-2.3,178.72,200.27,1.56
20260909,180,184.5,177,178,2525000,180.91,-1.61,178.03,199.25,1.01
20260910,178,178,169,174,2039000,180.33,-3.51,177.22,198.03,0.82
20260911,170.5,173.5,167.5,167.5,1500000,179.27,-6.56,176.28,196.71,0.6
20260914,165.5,169.5,161,166,1374000,178.16,-6.83,175.47,195.46,0.55
20260915,165,170.5,164,164,1073000,176.98,-7.33,175.2,194.11,0.44
20260916,165,174,165,174,1962000,176.73,-1.55,175.45,193.06,0.8
20260917,174.5,183.5,172,173,2630000,176.42,-1.94,175.57,192.08,1.05
20260918,177,180,173.5,180,4010000,176.72,1.86,176.15,191.2,1.51
20260921,180,182,176.5,179.5,1843000,176.95,1.44,176.75,190.69,0.68
20260922,183,189,180,181,3220000,177.29,2.09,177.32,190.43,1.14
20260923,183,185,176,176.5,1426000,177.22,-0.41,177.25,189.76,0.52
20260924,175.5,188,175.5,184,3342000,177.79,3.49,177.5,188.88,1.22
20260929,187,202,185.5,202,6192000,179.8,12.34,178.35,188.24,2.19
20260930,222,222,219,222,1773000,183.32,21.1,180.47,187.79,0.63
20261001,225,225,207,209.5,8948000,185.5,12.94,181.7,187.3,2.88
20261002,210,217,207,213.5,5264000,187.84,13.66,183.28,187.26,1.62
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 28.03
- over_600_ratio: 23.1
- over_800_ratio: 19.53
- over_1000_ratio: 17.01
- over_400_change_1w: 1.26
- over_800_change_1w: -0.45
- over_1000_change_1w: 0.28
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,27.29,-0.1,18.14,-0.03,16.54,0.83,1,False,True
20260724,27.14,-0.15,18.52,0.38,15.48,-1.06,2,False,True
20260731,27.46,0.32,17.82,-0.7,14.56,-0.92,3,False,False
20260807,26.97,-0.49,18,0.18,15.59,1.03,4,False,True
20260814,27.25,0.28,18.96,0.96,15.66,0.07,5,True,True
20260821,26.63,-0.62,18.17,-0.79,15.71,0.05,6,False,True
20260828,26.61,-0.02,18.06,-0.11,16.39,0.68,7,False,True
20260904,25.97,-0.64,17.86,-0.2,14.61,-1.78,0,False,False
20260911,26.35,0.38,17.06,-0.8,13.77,-0.84,1,False,False
20260918,26.96,0.61,18,0.94,14.72,0.95,2,True,True
20260924,26.77,-0.19,19.98,1.98,16.73,2.01,3,False,True
20261002,28.03,1.26,19.53,-0.45,17.01,0.28,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 8027 | 鈦昇 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | stale_signal | 內容：依鈦昇三發行及轉換辦法第十八條規定辦理。 發行公司於115年10月19日至115年11月17日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)、依本公司國內第三次無擔保轉換公司債發行及轉換辦法第十八條第一項規定，本債券自111年10月14日起(發行滿三個月翌日起)至116年6月3日止(到期前四十日止)，若本債券流通在外餘額低於原發行總面額之10%時，本公司得於其後任何時間，以掛號寄發一份一個月 期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券人名冊所載者為準，對於其後因買賣或其他原因始取得本債券之 投資人，則以公告方式為之)，贖回價格訂為本債券面額，以現金收回其全部債券，且函請櫃檯買賣中心公告。本公司執行收回請求，應於債券收回基準日後五個營業日內，按債券面額以現金收回其流通在外之本債券。 (二)、轉換公司債停止過戶期間：不適用 (三)、通知及受理轉換公司債贖回期間：115年10月19日至115年11月17日 (四)、轉換公司債收回基準日：115年11月17日 (五)、轉換公司債終止櫃檯買賣日期:115年11月18日 (六)、掛號寄發債券收回通知書日期:115年10月19日 (七)、轉換債價款發放日：115年11月24日 (八)、債券收回手續 (1)、債權人應持全部之債券及原留印鑑於自債券收回通知之始日之前一營業日起至屆滿日之前一營業日止（即自民國115年10月16日起至民國115年11月16日）止親臨或郵寄該公司股務代理機構。 (2)、債權人請檢附 1.轉換公司債帳簿劃撥轉換/贖回/賣回申請書(申請書可至各證券商取得)，填妥持有人之匯款銀行帳號並加蓋集保帳戶印鑑 2.證券存摺 3.身分證正反面影本，至往來證券商辦理債券收回手續。 (3)若 台端已將所持有之「鈦昇三」申請轉換或出售，則本通知書自動無效。 (九)、如債券持有人不欲公司行使贖回權，擬請求將本轉換公司債轉換為普通股，最遲應於115年11月19日前至往來證券商辦理轉換手續。 (十)、公司股務代理機構:永豐金證券股份有限公司股務代理部，地址：100台北市博愛路17號3樓，電話:02-2381-6288 警語：請投資人注意，具有請求轉換資格者，如未於115年11月19日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 8027 | 鈦昇 | 2 | 2 | 4 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| status |
| --- |
| no rows |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
