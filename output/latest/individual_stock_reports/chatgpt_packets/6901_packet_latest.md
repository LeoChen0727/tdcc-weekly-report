# INDIVIDUAL STOCK CHATGPT PACKET - 6901 鑽石投資

## Metadata
- generated_at: 2026-07-18 21:45:37 Asia/Taipei
- stock_id: 6901
- stock_name: 鑽石投資
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 11
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6901_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6901_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6901_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6901_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6901_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6901_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6901_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6901_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6901_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6901_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6901_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6901_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6901.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6901.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6901.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6901.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6901_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6901_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6901_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when tdcc_rows >= 8 and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
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
- date: 20260717
- open: 19
- high: 19.7
- low: 18.1
- close: 18.35
- volume: 6631224
- ma5: 18.85
- ema23_primary: 18.15
- distance_to_ema23_pct: 1.09
- ma20: 18.58
- ma60: 15.57
- ma120: 15.61
- return_5d: -11.57
- return_20d: 13.62
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: -1.24
- distance_to_high_60_pct: -18.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,16.25,17.2,16.2,16.55,3578798,14.94,10.79,14.54,14.11,1.03
20260622,17,17.7,16.8,17.35,4672867,15.14,14.6,14.71,14.17,1.29
20260623,17.85,17.85,16.9,16.95,2854478,15.29,10.86,14.89,14.22,0.78
20260624,17,17.4,16.65,17.25,2548661,15.45,11.63,15.12,14.27,0.7
20260625,17.8,18.95,17.65,18.95,6532285,15.74,20.36,15.45,14.35,1.72
20260626,19.7,20.6,18.2,18.3,16609805,15.96,14.68,15.75,14.43,3.65
20260629,17.95,18.75,17.65,18.05,4722512,16.13,11.89,16.03,14.5,1
20260630,18.3,18.95,18.1,18.8,4732556,16.35,14.95,16.32,14.58,0.96
20260701,18.85,19.85,18.2,18.45,5671396,16.53,11.62,16.58,14.65,1.11
20260702,18.35,18.8,17.85,17.95,3341169,16.65,7.82,16.76,14.71,0.65
20260703,18.15,19.5,18.05,18.9,6163355,16.84,12.27,16.98,14.8,1.18
20260706,19.6,20.55,18.8,18.9,7345426,17.01,11.13,17.21,14.88,1.33
20260707,18.9,19.25,18.45,19.15,3603819,17.19,11.43,17.38,14.97,0.68
20260708,21.05,21.05,20.35,21.05,17031772,17.51,20.23,17.63,15.1,3.12
20260709,22.2,22.4,20.65,20.75,19124395,17.78,16.72,17.86,15.21,3.11
20260713,20.8,20.8,18.7,18.75,9787884,17.86,4.99,18,15.28,1.51
20260714,18.55,19.15,18,18.8,4747871,17.94,4.81,18.13,15.35,0.72
20260715,18.85,19.4,18.6,19.25,3449094,18.05,6.67,18.29,15.43,0.52
20260716,19,19.55,18.65,19.1,2533712,18.13,5.32,18.47,15.5,0.38
20260717,19,19.7,18.1,18.35,6631224,18.15,1.09,18.58,15.57,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 83.19
- over_600_ratio: 82.02
- over_800_ratio: 81.47
- over_1000_ratio: 80.93
- over_400_change_1w: -0.5
- over_800_change_1w: -0.8
- over_1000_change_1w: -1.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,85.55,,84.76,,84.22,,0,False,False
20260508,85.4,-0.15,84.52,-0.24,84.19,-0.03,0,False,False
20260515,85.08,-0.32,84.44,-0.08,83.91,-0.28,0,False,False
20260522,84.98,-0.1,84.18,-0.26,83.63,-0.28,0,False,False
20260529,84.89,-0.09,83.91,-0.27,83.58,-0.05,0,False,False
20260605,84.86,-0.03,84.03,0.12,83.6,0.02,1,False,True
20260612,84.81,-0.05,83.59,-0.44,83.15,-0.45,0,False,False
20260618,84.85,0.04,83.72,0.13,83.08,-0.07,1,False,True
20260626,84.71,-0.14,83.36,-0.36,82.82,-0.26,0,False,False
20260703,83.69,-1.02,82.27,-1.09,81.94,-0.88,0,False,False
20260717,83.19,-0.5,81.47,-0.8,80.93,-1.01,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6901 | 鑽石投資 | pattern | 型態觀察 | 54.0 |  |  | pullback_right_side |  |  | stale_signal | 1.事實發生日:115/07/07 2.公司名稱:鑽石生技投資股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:   依據臺灣證券交易所股份有限公司112年6月29日臺證上一字第1121802934號   函規定，本公司股票初次上市時出具之承諾事項如下：   (一)於公開說明書特別記載事項乙節中揭露以下事項：       1.最近三年度與截至最近期業績變化之合理性。       2.與投資標的合一生技股份有限公司相互持股之緣由、適法性、合理性、營運         風險及因應措施。   (二)為降低相互持股對損益造成之影響，不再增加持有合一生技股份有限公司股份，       並於113年12月31日前處分所持合一生技股份有限公司所有股份。   (三)內部人及前十大股東承諾延長股票集中保管期間，上市屆滿2年後，每屆滿6個月       可領回四分之一，滿4年後始得全數領回。前述人員於上市後至集保期間屆滿前，       因盈餘轉增資或其他原因(如執行員工認股權及員工分紅等)而取得之股份，應       提交集中保管，並於最後一次領回日始得領回。   (四)上市後增設「提名委員會」，並於113年股東常會增選獨立董事達全體董事席次       三分之二以上。   (五)公開說明書應加強揭露下列事項：       1.生技創投公司的特性與投資風險(包括但不限於其投資標的所包括之未上市櫃         或非公開發行公司之公允價值欠缺透明度；其投資標的組合可能產生重大變動         等)。       2.公司未來投資標的之方針、策略、範圍、地區、決策過程及行使表決權之處理         原則及方法等。       3.封面載明「本公司業務性質為創業投資公司型態且以生技產業為主要投資標的         ，生技產業開發時程長，投入經費高且未保證一定能成功，請投資人特別注意         且詳細閱讀本公司公開說明書內容並審慎投資。」。       4.產業、營運及其他重要風險乙節載明「...本公司主要投資標的為生技類股，         其股價及公允價值受研發成果之影響甚大，因而產生較鉅幅之波動。因此若         公允價值下跌可能導致本公司營業收入為負數…」。   (六)經董事會通過修訂本公司「取得或處分資產處理程序」、「投資業務作業辦法」       及「投資業務風險控管辦法」之下列投資業務相關規範，「取得或處分資產處理       程序」並應提報最近一次股東會通過：       1.董事長核決權限由新台幣5億元調降為3億元，凡取得或處分投資之交易金額         超過3億元者，均須經投資審議委員會、審計委員會及董事會通過後始得為之。         前述金額應採累積計算，且母公司與子公司(若有)合併計算。       2.訂定明確投資標的退場機制：         (1)通知評估：就上市及上櫃投資標的之未實現獲利達原始投資成本3倍或未實            現損失達原始投資成本30%者，投資部發出通知或預警並擬訂持有或處分評            估方案，若評估為處分退場，即依核決權限執行(預估獲利金額且交易金額            在新台幣三億元(含)以下由董事長核定；預估獲利金額或交易金額在新台幣            三億元以上，須經投資審議委員會、審計委員會及董事會通過後始得為之)            ；若評估為繼續持有，應提報投資審議委員會同意。         (2)強制退場：若未實現獲利達原始投資成本5倍或未實現損失達原始投資成本            50%強制退場條件，投資部發出通知或預警並擬訂處分退場方案，依核決            權限執行 (同上段所述)。若決議不處分退場，應將例外管理方案提報投資            審議委員會、審計委員會、董事會決議執行，並定期於董事會報告執行情            形。   (七)上市後辦理資訊揭露如下：       1.每日於官網公告屬上市/櫃及興櫃股票之投資標的公允價值。       2.每月於官網及以重大訊息公告「所有投資標的」股數變動及公允價值變動、         本公司每股淨值、現金及約當現金餘額。       3.按季舉辦法人說明會，向投資人說明財務業務狀況及營收認列特性。       4.若公司連續3個月營業收入呈現負數，應發布重大訊息提醒投資人注意。 6.因應措施:   (一)相關內容均已於112年9月刊印之「現金增資發行新股辦理上市前公開承銷暨股票       初次上市用」公開說明書中作適當揭露，請詳公開資訊觀測站。   (二)已於113年10月25日完成處分所持合一生技股份有限公司所有股份。   (三)內部人及前十大股東已依規定延長股票集中保管期間，上市屆滿2年後，每屆滿       6個月可領回四分之一，滿4年後始得全數領回。前述人員因員工認股權而取得       之股份，亦已提交集中保管，並於最後一次領回日始得領回。   (四)已於112年10月13日董事會通過增設「提名委員會」，並於113年5月21日股東       常會全面改選第6屆董事，改選後獨立董事達全體董事席次三分之二以上，已於       113年8月1日就任。   (五)相關內容均已於112年9月刊印之「現金增資發行新股辦理上市前公開承銷暨股票       初次上市用」公開說明書中作適當揭露，請詳公開資訊觀測站。   (六)已於112年7月20日董事會通過修訂投資業務相關規範。另「取得或處分資產處理       程序」已提報113年5月21日股東常會通過。   (七)資訊揭露辦理情形如下：       1.已於112年9月1日起每日於官網公告屬上市/櫃及興櫃股票之投資標的公允         價值。       2.已每月於官網及以重大訊息公告「所有投資標的」股數變動及公允價值變動、         本公司每股淨值、現金及約當現金餘額。       3.已自112年第四季起按季舉辦法人說明會，向投資人說明財務業務狀況及營收         認列特性。       4.若連續3個月營業收入呈現負數，將發布重大訊息提醒投資人注意。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):    無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 6901 | 鑽石投資 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/07 2.公司名稱:鑽石生技投資股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:   依據臺灣證券交易所股份有限公司112年6月29日臺證上一字第1121802934號   函規定，本公司股票初次上市時出具之承諾事項如下：   (一)於公開說明書特別記載事項乙節中揭露以下事項：       1.最近三年度與截至最近期業績變化之合理性。       2.與投資標的合一生技股份有限公司相互持股之緣由、適法性、合理性、營運         風險及因應措施。   (二)為降低相互持股對損益造成之影響，不再增加持有合一生技股份有限公司股份，       並於113年12月31日前處分所持合一生技股份有限公司所有股份。   (三)內部人及前十大股東承諾延長股票集中保管期間，上市屆滿2年後，每屆滿6個月       可領回四分之一，滿4年後始得全數領回。前述人員於上市後至集保期間屆滿前，       因盈餘轉增資或其他原因(如執行員工認股權及員工分紅等)而取得之股份，應       提交集中保管，並於最後一次領回日始得領回。   (四)上市後增設「提名委員會」，並於113年股東常會增選獨立董事達全體董事席次       三分之二以上。   (五)公開說明書應加強揭露下列事項：       1.生技創投公司的特性與投資風險(包括但不限於其投資標的所包括之未上市櫃         或非公開發行公司之公允價值欠缺透明度；其投資標的組合可能產生重大變動         等)。       2.公司未來投資標的之方針、策略、範圍、地區、決策過程及行使表決權之處理         原則及方法等。       3.封面載明「本公司業務性質為創業投資公司型態且以生技產業為主要投資標的         ，生技產業開發時程長，投入經費高且未保證一定能成功，請投資人特別注意         且詳細閱讀本公司公開說明書內容並審慎投資。」。       4.產業、營運及其他重要風險乙節載明「...本公司主要投資標的為生技類股，         其股價及公允價值受研發成果之影響甚大，因而產生較鉅幅之波動。因此若         公允價值下跌可能導致本公司營業收入為負數…」。   (六)經董事會通過修訂本公司「取得或處分資產處理程序」、「投資業務作業辦法」       及「投資業務風險控管辦法」之下列投資業務相關規範，「取得或處分資產處理       程序」並應提報最近一次股東會通過：       1.董事長核決權限由新台幣5億元調降為3億元，凡取得或處分投資之交易金額         超過3億元者，均須經投資審議委員會、審計委員會及董事會通過後始得為之。         前述金額應採累積計算，且母公司與子公司(若有)合併計算。       2.訂定明確投資標的退場機制：         (1)通知評估：就上市及上櫃投資標的之未實現獲利達原始投資成本3倍或未實            現損失達原始投資成本30%者，投資部發出通知或預警並擬訂持有或處分評            估方案，若評估為處分退場，即依核決權限執行(預估獲利金額且交易金額            在新台幣三億元(含)以下由董事長核定；預估獲利金額或交易金額在新台幣            三億元以上，須經投資審議委員會、審計委員會及董事會通過後始得為之)            ；若評估為繼續持有，應提報投資審議委員會同意。         (2)強制退場：若未實現獲利達原始投資成本5倍或未實現損失達原始投資成本            50%強制退場條件，投資部發出通知或預警並擬訂處分退場方案，依核決            權限執行 (同上段所述)。若決議不處分退場，應將例外管理方案提報投資            審議委員會、審計委員會、董事會決議執行，並定期於董事會報告執行情            形。   (七)上市後辦理資訊揭露如下：       1.每日於官網公告屬上市/櫃及興櫃股票之投資標的公允價值。       2.每月於官網及以重大訊息公告「所有投資標的」股數變動及公允價值變動、         本公司每股淨值、現金及約當現金餘額。       3.按季舉辦法人說明會，向投資人說明財務業務狀況及營收認列特性。       4.若公司連續3個月營業收入呈現負數，應發布重大訊息提醒投資人注意。 6.因應措施:   (一)相關內容均已於112年9月刊印之「現金增資發行新股辦理上市前公開承銷暨股票       初次上市用」公開說明書中作適當揭露，請詳公開資訊觀測站。   (二)已於113年10月25日完成處分所持合一生技股份有限公司所有股份。   (三)內部人及前十大股東已依規定延長股票集中保管期間，上市屆滿2年後，每屆滿       6個月可領回四分之一，滿4年後始得全數領回。前述人員因員工認股權而取得       之股份，亦已提交集中保管，並於最後一次領回日始得領回。   (四)已於112年10月13日董事會通過增設「提名委員會」，並於113年5月21日股東       常會全面改選第6屆董事，改選後獨立董事達全體董事席次三分之二以上，已於       113年8月1日就任。   (五)相關內容均已於112年9月刊印之「現金增資發行新股辦理上市前公開承銷暨股票       初次上市用」公開說明書中作適當揭露，請詳公開資訊觀測站。   (六)已於112年7月20日董事會通過修訂投資業務相關規範。另「取得或處分資產處理       程序」已提報113年5月21日股東常會通過。   (七)資訊揭露辦理情形如下：       1.已於112年9月1日起每日於官網公告屬上市/櫃及興櫃股票之投資標的公允         價值。       2.已每月於官網及以重大訊息公告「所有投資標的」股數變動及公允價值變動、         本公司每股淨值、現金及約當現金餘額。       3.已自112年第四季起按季舉辦法人說明會，向投資人說明財務業務狀況及營收         認列特性。       4.若連續3個月營業收入呈現負數，將發布重大訊息提醒投資人注意。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):    無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6901 | 鑽石投資 | 2 | 2 | 4 | 9 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
