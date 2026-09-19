# INDIVIDUAL STOCK CHATGPT PACKET - 2455 全新

## Metadata
- generated_at: 2026-09-19 15:52:43 Asia/Taipei
- stock_id: 2455
- stock_name: 全新
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2455_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2455_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2455_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2455_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2455_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2455_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2455.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2455.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2455.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2455.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2455_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2455_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2455_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: high_level_consolidation
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260918
- open: 545
- high: 563
- low: 520
- close: 556
- volume: 20026752
- ma5: 532
- ema23_primary: 489.06
- distance_to_ema23_pct: 13.69
- ma20: 497.35
- ma60: 394.98
- ma120: 375.62
- return_5d: 7.96
- return_20d: 36.95
- volume_ratio: 1.64
- distance_to_ma20_pct_auxiliary: 11.79
- distance_to_high_60_pct: -1.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,401.5,405.5,381.5,381.5,3076652,371.77,2.62,363.05,359.64,0.28
20260825,381.5,419.5,374.5,419.5,4279618,375.75,11.64,368.9,359.6,0.4
20260826,419,430,415,428,3496416,380.1,12.6,376.68,359.81,0.33
20260827,429,450,426.5,433,4766593,384.51,12.61,385.05,360.38,0.46
20260828,438,442,431.5,434,2121492,388.63,11.67,392.15,360.71,0.21
20260831,428,477,428,477,32356290,396,20.45,399.95,361.96,2.81
20260901,490,524,474,524,28052088,406.67,28.85,408.5,364.04,2.22
20260902,515,552,509,542,34014193,417.94,29.68,416.2,367.08,2.46
20260903,541,555,520,525,21442379,426.86,22.99,423.85,369.25,1.63
20260904,548,548,492.5,528,24125544,435.29,21.3,432.05,372.12,1.77
20260907,525,525,491,500,3476203,440.68,13.46,437.82,375.12,0.26
20260908,528,535,506,515,4653069,446.88,15.24,445.2,377.84,0.34
20260909,536,552,523,533,2499264,454.05,17.39,452.62,380.57,0.19
20260910,533,545,527,532,1564218,460.55,15.51,460.02,382.68,0.12
20260911,514,527,499.5,515,1842066,465.09,10.73,466.8,384.13,0.14
20260914,497,535,493,535,1719569,470.91,13.61,472.7,386.12,0.13
20260915,528,536,506,520,1671642,475,9.47,477.82,387.96,0.15
20260916,515,534,506,515,19718194,478.34,7.66,483.75,389.91,1.75
20260917,535,566,515,534,28618653,482.98,10.56,489.85,392.19,2.41
20260918,545,563,520,556,20026752,489.06,13.69,497.35,394.98,1.64
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 57.16
- over_600_ratio: 51.65
- over_800_ratio: 44.88
- over_1000_ratio: 40.71
- over_400_change_1w: -0.31
- over_800_change_1w: -0.97
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,51.48,-0.61,40.4,-0.31,37.99,-0.84,0,False,False
20260709,49.43,-2.05,38.19,-2.21,34.9,-3.09,0,False,False
20260717,50.5,1.07,37.71,-0.48,34.44,-0.46,1,False,False
20260724,51.5,1,38.98,1.27,36.16,1.72,2,True,True
20260731,50.27,-1.23,39.84,0.86,36.64,0.48,3,False,True
20260807,51.82,1.55,40.77,0.93,38.49,1.85,4,True,True
20260814,51.78,-0.04,41.14,0.37,37.48,-1.01,5,False,True
20260821,51.06,-0.72,39.92,-1.22,36.32,-1.16,0,False,False
20260828,52.32,1.26,43,3.08,37.34,1.02,1,True,True
20260904,57.11,4.79,46.05,3.05,41.01,3.67,2,True,True
20260911,57.47,0.36,45.85,-0.2,40.72,-0.29,3,False,False
20260918,57.16,-0.31,44.88,-0.97,40.71,-0.01,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2455 | 全新 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | no_signal | continued_overheated | 內容：依全新二發行及轉換辦法第十八條規定辦理。 發行公司於115年10月19日至115年11月17日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)、依本公司「國內第二次無擔保可轉換公司債發行及轉換辦法」第十八條第一項規定，本公司普通股收盤價連續三十個營業日超過當時轉換價格達百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本債券面額，以現金收回其全部債券，並函請櫃檯買賣中心公告。本公司執行收回請求，應於債券收回基準日後五個營業日內，按債券面額以現金收回流通在外之本轉換公司債。 (二)、依本公司「國內第二次無擔保可轉換公司債發行及轉換辦法」第十八條第三項規定，若債券持有人於「債券收回通知書」所載債券收回基準日前，未以書面回覆本公司股務代理機構(於送達時即生效力，採郵寄者以郵戳日為憑)者，本公司將於債券收回基準日後五個營業日內，按債券面額以現金收回流通在外之本轉換公司債。 (三)、本公司國內第二次無擔保轉換公司債行使贖回權暨終止櫃檯買賣日之相關事宜如下： (1)、掛號寄發債券收回通知書日期：115年10月19日。 (2)、通知及受理轉換公司債贖回期間：115年10月19日至115年11月17日。 (3)、轉換公司債收回基準日：115年11月17日。 (4)、轉換公司債終止櫃檯買賣日期：115年11月18日。 (5)、債券收回價款及發放日期：按債券面額以現金收回，並統一於115年11月24日以匯款或郵寄支票方式支付予各申請人，匯費(郵資)自收回價金中直接扣除。 (四)、債券收回手續暨應備文件 (1)、轉換公司債帳簿劃撥轉換/贖回/賣回申請書(申請書可至各證券商取得，註明：贖回，並填妥持有人之匯款銀行帳號及加蓋集保帳戶印鑑）。 (2)、證券存摺，向往來券商辦理債券收回手續，由往來券商向臺灣集中保管結算所股份有限公司(下稱集保公司）提出申請，集保公司於接受申請後送交本公司股務代理機構，於送達時即生效力，且不得申請撤回。 (3)、債權人得自債券收回通知之始日115年10月19日之前一營業日（115年10月16日）起至屆滿日（115年11月17日）之前一營業日（115年11月16日）止，由債券持有人向往來券商辦理贖回手續。 (五)、本公司股務代理機構:台新綜合證券股份有限公司股務代理部(地址：台北市建國北路一段96號B1，電話：02-25048125)。 警語：請投資人注意，具有請求轉換資格者，如未於115年11月19日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 2455 | 全新 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | continued_overheated | 內容：依全新二發行及轉換辦法第十八條規定辦理。 發行公司於115年10月19日至115年11月17日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)、依本公司「國內第二次無擔保可轉換公司債發行及轉換辦法」第十八條第一項規定，本公司普通股收盤價連續三十個營業日超過當時轉換價格達百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本債券面額，以現金收回其全部債券，並函請櫃檯買賣中心公告。本公司執行收回請求，應於債券收回基準日後五個營業日內，按債券面額以現金收回流通在外之本轉換公司債。 (二)、依本公司「國內第二次無擔保可轉換公司債發行及轉換辦法」第十八條第三項規定，若債券持有人於「債券收回通知書」所載債券收回基準日前，未以書面回覆本公司股務代理機構(於送達時即生效力，採郵寄者以郵戳日為憑)者，本公司將於債券收回基準日後五個營業日內，按債券面額以現金收回流通在外之本轉換公司債。 (三)、本公司國內第二次無擔保轉換公司債行使贖回權暨終止櫃檯買賣日之相關事宜如下： (1)、掛號寄發債券收回通知書日期：115年10月19日。 (2)、通知及受理轉換公司債贖回期間：115年10月19日至115年11月17日。 (3)、轉換公司債收回基準日：115年11月17日。 (4)、轉換公司債終止櫃檯買賣日期：115年11月18日。 (5)、債券收回價款及發放日期：按債券面額以現金收回，並統一於115年11月24日以匯款或郵寄支票方式支付予各申請人，匯費(郵資)自收回價金中直接扣除。 (四)、債券收回手續暨應備文件 (1)、轉換公司債帳簿劃撥轉換/贖回/賣回申請書(申請書可至各證券商取得，註明：贖回，並填妥持有人之匯款銀行帳號及加蓋集保帳戶印鑑）。 (2)、證券存摺，向往來券商辦理債券收回手續，由往來券商向臺灣集中保管結算所股份有限公司(下稱集保公司）提出申請，集保公司於接受申請後送交本公司股務代理機構，於送達時即生效力，且不得申請撤回。 (3)、債權人得自債券收回通知之始日115年10月19日之前一營業日（115年10月16日）起至屆滿日（115年11月17日）之前一營業日（115年11月16日）止，由債券持有人向往來券商辦理贖回手續。 (五)、本公司股務代理機構:台新綜合證券股份有限公司股務代理部(地址：台北市建國北路一段96號B1，電話：02-25048125)。 警語：請投資人注意，具有請求轉換資格者，如未於115年11月19日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 2455 | 全新 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | continued_overheated | 內容：依全新二發行及轉換辦法第十八條規定辦理。 發行公司於115年10月19日至115年11月17日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)、依本公司「國內第二次無擔保可轉換公司債發行及轉換辦法」第十八條第一項規定，本公司普通股收盤價連續三十個營業日超過當時轉換價格達百分之三十(含)時，本公司得於其後三十個營業日內，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本債券面額，以現金收回其全部債券，並函請櫃檯買賣中心公告。本公司執行收回請求，應於債券收回基準日後五個營業日內，按債券面額以現金收回流通在外之本轉換公司債。 (二)、依本公司「國內第二次無擔保可轉換公司債發行及轉換辦法」第十八條第三項規定，若債券持有人於「債券收回通知書」所載債券收回基準日前，未以書面回覆本公司股務代理機構(於送達時即生效力，採郵寄者以郵戳日為憑)者，本公司將於債券收回基準日後五個營業日內，按債券面額以現金收回流通在外之本轉換公司債。 (三)、本公司國內第二次無擔保轉換公司債行使贖回權暨終止櫃檯買賣日之相關事宜如下： (1)、掛號寄發債券收回通知書日期：115年10月19日。 (2)、通知及受理轉換公司債贖回期間：115年10月19日至115年11月17日。 (3)、轉換公司債收回基準日：115年11月17日。 (4)、轉換公司債終止櫃檯買賣日期：115年11月18日。 (5)、債券收回價款及發放日期：按債券面額以現金收回，並統一於115年11月24日以匯款或郵寄支票方式支付予各申請人，匯費(郵資)自收回價金中直接扣除。 (四)、債券收回手續暨應備文件 (1)、轉換公司債帳簿劃撥轉換/贖回/賣回申請書(申請書可至各證券商取得，註明：贖回，並填妥持有人之匯款銀行帳號及加蓋集保帳戶印鑑）。 (2)、證券存摺，向往來券商辦理債券收回手續，由往來券商向臺灣集中保管結算所股份有限公司(下稱集保公司）提出申請，集保公司於接受申請後送交本公司股務代理機構，於送達時即生效力，且不得申請撤回。 (3)、債權人得自債券收回通知之始日115年10月19日之前一營業日（115年10月16日）起至屆滿日（115年11月17日）之前一營業日（115年11月16日）止，由債券持有人向往來券商辦理贖回手續。 (五)、本公司股務代理機構:台新綜合證券股份有限公司股務代理部(地址：台北市建國北路一段96號B1，電話：02-25048125)。 警語：請投資人注意，具有請求轉換資格者，如未於115年11月19日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2455 | 全新 | 4 | 4 | 4 | 6 | 11 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2455 | 全新 | 14 | 0 | 2506860.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
