# INDIVIDUAL STOCK CHATGPT PACKET - 6015 宏遠證

## Metadata
- generated_at: 2026-09-26 15:52:44 Asia/Taipei
- stock_id: 6015
- stock_name: 宏遠證
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 262
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6015_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6015_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6015_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6015_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6015_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6015_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6015.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6015.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6015.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6015.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6015_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6015_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6015_latest.md?ref=main

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
- date: 20260924
- open: 17.8
- high: 17.85
- low: 17.55
- close: 17.6
- volume: 1951000
- ma5: 17.74
- ema23_primary: 17.07
- distance_to_ema23_pct: 3.11
- ma20: 17.11
- ma60: 16.5
- ma120: 16.42
- return_5d: 1.44
- return_20d: 9.66
- volume_ratio: 0.74
- distance_to_ma20_pct_auxiliary: 2.86
- distance_to_high_60_pct: -6.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,16.3,16.75,16.3,16.4,2381000,15.95,2.85,15.74,17.01,1.56
20260831,16.15,16.2,15.8,16.2,1594000,15.97,1.46,15.78,16.91,1.06
20260901,16.35,16.75,16.35,16.6,2370000,16.02,3.63,15.83,16.81,1.49
20260902,16.5,16.55,16.2,16.3,908000,16.04,1.6,15.85,16.74,0.58
20260903,16.4,16.85,16.35,16.4,2104000,16.07,2.04,15.89,16.7,1.31
20260904,16.65,16.85,16.45,16.8,2319000,16.13,4.13,15.97,16.68,1.4
20260907,17.05,17.1,16.55,16.85,2173000,16.19,4.06,16.06,16.66,1.32
20260908,17.75,17.9,17.55,17.85,5927000,16.33,9.3,16.2,16.65,3.16
20260909,18.2,18.2,17.25,17.45,5632000,16.42,6.25,16.27,16.63,2.78
20260910,17.25,17.4,17.1,17.15,1390000,16.48,4.04,16.33,16.61,0.71
20260911,16.8,17.15,16.75,16.95,2035000,16.52,2.58,16.36,16.58,1.05
20260914,16.85,17.4,16.75,17.35,1721000,16.59,4.57,16.43,16.57,0.88
20260915,17.25,17.25,16.75,16.85,1668000,16.61,1.42,16.48,16.53,0.84
20260916,16.8,17.2,16.8,17,1125000,16.65,2.13,16.56,16.5,0.57
20260917,17.15,17.55,17.1,17.35,2645000,16.7,3.86,16.64,16.49,1.28
20260918,17.4,17.6,17.3,17.6,3165000,16.78,4.89,16.72,16.48,1.46
20260921,17.6,18.1,17.5,17.85,5622000,16.87,5.82,16.82,16.49,2.33
20260922,18.05,18.25,17.75,17.8,3710000,16.95,5.04,16.94,16.5,1.45
20260923,18,18.1,17.8,17.85,2354000,17.02,4.87,17.03,16.5,0.9
20260924,17.8,17.85,17.55,17.6,1951000,17.07,3.11,17.11,16.5,0.74
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 51.29
- over_600_ratio: 47.34
- over_800_ratio: 45.89
- over_1000_ratio: 44.78
- over_400_change_1w: 0.01
- over_800_change_1w: -0.19
- over_1000_change_1w: 0.5
- tdcc_consecutive_up_weeks: 10
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,50.3,0.21,44.8,-0.17,43.41,-0.17,1,False,False
20260717,49.82,-0.48,44.23,-0.57,42.21,-1.2,0,False,False
20260724,49.61,-0.21,44.38,0.15,41.88,-0.33,1,False,True
20260731,49.41,-0.2,44.17,-0.21,42.09,0.21,2,False,True
20260807,49.61,0.2,44.03,-0.14,42.21,0.12,3,False,True
20260814,49.77,0.16,44.11,0.08,42.03,-0.18,4,False,True
20260821,49.91,0.14,43.89,-0.22,41.59,-0.44,5,False,False
20260828,49.65,-0.26,43.7,-0.19,42.05,0.46,6,False,True
20260904,51.05,1.4,45.79,2.09,44.2,2.15,7,True,True
20260911,51.05,0,45.7,-0.09,44.38,0.18,8,False,True
20260918,51.28,0.23,46.08,0.38,44.28,-0.1,9,False,True
20260924,51.29,0.01,45.89,-0.19,44.78,0.5,10,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6015 | 宏遠證 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 內容：依宏遠證二發行及轉換辦法第十八條規定辦理。 發行公司於115年10月12日至115年11月10日行使債券贖回權，贖回權價格為債券面額之100.0000% 內容：依宏遠證二發行及轉換辦法第十八條規定辦理。 (一)、依本公司國內第二次無擔保轉換公司債發行及轉換辦法(簡稱： 宏遠證二 ，代碼：60152 )第十八條第(二)項規定，本轉換公司債發&#64008;滿三個月翌日(113年4月6日)至發&#64008;期間屆滿前四十日止(117年11月26日)，若本轉換公司債流通在外餘額低於原發行總額之10%時，本公司得於其後任何時間，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本債券面額，以現金收回其全部債券，並函請櫃檯買賣中心公告本公司贖回權之行使。本公司執行收回請求時，應於債券收回基準日後五個營業日內，按債券面額以現金贖回其流通在外之本轉換公司債。 (二)、本轉換公司債贖回權行使相關資訊規定如下： 1、債券收回價款：每張按債券面額100,000元，以現&#63754;贖回債券面額。 2、掛號寄發債券收回通知書日期：115 &#63886;10 月12日。 3、轉換債收回基準日：115年11月10日。 4、轉換債終止上櫃買賣日：115年11月11日。 5、債券收回期間：115年10月12日至115年11月10日，因本債券為無實體發行，故請自115年10月8日至115年11月9日止向往來證券商辦理贖回手續，逾期恕不受理。 (三)、債券收回程序： 1、本轉換債採無實體發行，請檢附以下文件至原交易券商辦理債券贖回手續，由交易券商於收件後向臺灣集中保管結算所提出申請，於送達時即生效力，且不得申請撤銷。 (1)『有價證券轉(交)換/買(贖/賣)回/註銷/認股/履約/兌回帳簿劃撥作業申請書』127表單（註明贖回）（可由各券商取得)，並加蓋集保帳戶印鑑。 (2)證券存摺。 2、債券收回之相關稅賦暨利息所得扣取補充保費：因本次收回無利息補償，故&#63847;適用。 3、轉換債價款發放日：115年11月17日，採匯款方式撥入債權人留存於交易證券商之款項劃撥帳號者，本公司將收回價款扣除匯費後，以匯款方式支付各債券持有人。 4、債權人若已將持有之轉換公司債申請轉換或出售，則本通知書自動無效。 5、如債券持有人不欲公司行使贖回權，擬請求將本轉換公司債轉換為普通股，最遲應於115年11月12日前至往來證券商辦理轉換手續。 6、公司股務代理機構（包括地址及電話）: 宏遠證券股份有限公司股務代理部，地址：台北市大安區信義路四段236號3樓，電話：(02)2326-8818 警語：請投資人注意，具有請求轉換資格者，如未於115年11月12日前以書面至往來證券商辦理請求轉換普通股，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 6015 | 宏遠證 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 內容：依宏遠證二發行及轉換辦法第十八條規定辦理。 發行公司於115年10月12日至115年11月10日行使債券贖回權，贖回權價格為債券面額之100.0000% 內容：依宏遠證二發行及轉換辦法第十八條規定辦理。 (一)、依本公司國內第二次無擔保轉換公司債發行及轉換辦法(簡稱： 宏遠證二 ，代碼：60152 )第十八條第(二)項規定，本轉換公司債發&#64008;滿三個月翌日(113年4月6日)至發&#64008;期間屆滿前四十日止(117年11月26日)，若本轉換公司債流通在外餘額低於原發行總額之10%時，本公司得於其後任何時間，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本債券面額，以現金收回其全部債券，並函請櫃檯買賣中心公告本公司贖回權之行使。本公司執行收回請求時，應於債券收回基準日後五個營業日內，按債券面額以現金贖回其流通在外之本轉換公司債。 (二)、本轉換公司債贖回權行使相關資訊規定如下： 1、債券收回價款：每張按債券面額100,000元，以現&#63754;贖回債券面額。 2、掛號寄發債券收回通知書日期：115 &#63886;10 月12日。 3、轉換債收回基準日：115年11月10日。 4、轉換債終止上櫃買賣日：115年11月11日。 5、債券收回期間：115年10月12日至115年11月10日，因本債券為無實體發行，故請自115年10月8日至115年11月9日止向往來證券商辦理贖回手續，逾期恕不受理。 (三)、債券收回程序： 1、本轉換債採無實體發行，請檢附以下文件至原交易券商辦理債券贖回手續，由交易券商於收件後向臺灣集中保管結算所提出申請，於送達時即生效力，且不得申請撤銷。 (1)『有價證券轉(交)換/買(贖/賣)回/註銷/認股/履約/兌回帳簿劃撥作業申請書』127表單（註明贖回）（可由各券商取得)，並加蓋集保帳戶印鑑。 (2)證券存摺。 2、債券收回之相關稅賦暨利息所得扣取補充保費：因本次收回無利息補償，故&#63847;適用。 3、轉換債價款發放日：115年11月17日，採匯款方式撥入債權人留存於交易證券商之款項劃撥帳號者，本公司將收回價款扣除匯費後，以匯款方式支付各債券持有人。 4、債權人若已將持有之轉換公司債申請轉換或出售，則本通知書自動無效。 5、如債券持有人不欲公司行使贖回權，擬請求將本轉換公司債轉換為普通股，最遲應於115年11月12日前至往來證券商辦理轉換手續。 6、公司股務代理機構（包括地址及電話）: 宏遠證券股份有限公司股務代理部，地址：台北市大安區信義路四段236號3樓，電話：(02)2326-8818 警語：請投資人注意，具有請求轉換資格者，如未於115年11月12日前以書面至往來證券商辦理請求轉換普通股，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6015 | 宏遠證 | 8 | 8 | 5 | 8 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
