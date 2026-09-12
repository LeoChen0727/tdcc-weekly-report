# INDIVIDUAL STOCK CHATGPT PACKET - 2357 華碩

## Metadata
- generated_at: 2026-09-12 22:16:03 Asia/Taipei
- stock_id: 2357
- stock_name: 華碩
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2357_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2357_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2357_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2357_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2357_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2357_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2357.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2357.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2357.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2357.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2357_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2357_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2357_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
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
- open: 930
- high: 930
- low: 912
- close: 924
- volume: 5904124
- ma5: 971.8
- ema23_primary: 942.47
- distance_to_ema23_pct: -1.96
- ma20: 961.65
- ma60: 825.15
- ma120: 744.15
- return_5d: -9.85
- return_20d: -7.23
- volume_ratio: 1.64
- distance_to_ma20_pct_auxiliary: -3.92
- distance_to_high_60_pct: -10.29

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,985,986,921,938,5643928,822.76,14.01,814.7,773.05,1.09
20260818,930,933,891,910,4643243,830.03,9.63,823.4,776.85,0.9
20260819,896,925,891,925,2985654,837.94,10.39,831.8,780.45,0.6
20260820,928,940,906,913,3211887,844.2,8.15,839,784.02,0.64
20260821,913,923,906,921,1887246,850.6,8.28,846.5,787.68,0.38
20260824,919,939,916,923,1674244,856.63,7.75,854.65,791.53,0.35
20260825,921,925,901,925,1976790,862.33,7.27,864.15,794.27,0.42
20260826,923,980,919,971,3391704,871.38,11.43,874.65,796.5,0.74
20260827,966,977,962,968,1739150,879.44,10.07,886.2,797.3,0.4
20260828,975,981,955,965,1844300,886.57,8.85,893.95,797.87,0.46
20260831,962,1005,951,999,5187639,895.94,11.5,903.95,799.65,1.28
20260901,1000,1025,987,1010,5653878,905.44,11.55,914.15,801.48,1.37
20260902,1000,1020,993,1010,3736142,914.15,10.48,922.75,804.25,0.92
20260903,1020,1025,962,971,3213248,918.89,5.67,930.4,806.27,0.8
20260904,988,1030,986,1025,5102743,927.73,10.48,940.8,810.08,1.26
20260907,1025,1025,981,999,5002793,933.67,7,949.85,813.67,1.2
20260908,992,992,956,968,4968506,936.53,3.36,956.3,816.72,1.17
20260909,966,985,963,979,1855419,940.07,4.14,962.65,819.83,0.44
20260910,982,989,972,989,2481872,944.15,4.75,965.25,823.13,0.6
20260911,930,930,912,924,5904124,942.47,-1.96,961.65,825.15,1.64
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 75.24
- over_600_ratio: 71.42
- over_800_ratio: 68.72
- over_1000_ratio: 65.37
- over_400_change_1w: 0.21
- over_800_change_1w: 0.35
- over_1000_change_1w: -0.12
- tdcc_consecutive_up_weeks: 10
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,73.12,-0.8,66.92,-0.83,63.05,-0.96,0,False,False
20260703,72.39,-0.73,65.85,-1.07,62.72,-0.33,0,False,False
20260709,72.44,0.05,66.14,0.29,62.5,-0.22,1,False,True
20260717,72.56,0.12,65.54,-0.6,61.91,-0.59,2,False,False
20260724,72.96,0.4,66.02,0.48,62.71,0.8,3,True,True
20260731,73.14,0.18,66.45,0.43,62.76,0.05,4,True,True
20260807,74.06,0.92,67.25,0.8,63.85,1.09,5,True,True
20260814,74.58,0.52,67.72,0.47,64.1,0.25,6,True,True
20260821,74.82,0.24,68.45,0.73,65.21,1.11,7,True,True
20260828,74.89,0.07,68.51,0.06,65.39,0.18,8,True,True
20260904,75.03,0.14,68.37,-0.14,65.49,0.1,9,False,True
20260911,75.24,0.21,68.72,0.35,65.37,-0.12,10,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2357 | 華碩 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/09/10 2.公司名稱:華碩電腦股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司海外第二次無擔保轉換公司債完成訂價 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 一、募集海外公司債總額、債券每張金額、發行價格及預定發行日期： （一）募集海外公司債總額：美金15億元，僅發行B券公司債。 （二）債券每張面額：美金20萬元，或如超過美金20萬元，以美金10萬元之整數倍 數發行。 （三）發行價格：按面額100%發行。 （四）預定發行日期：115年9月17日。  二、募集海外公司債之利率：票面利率為年利率0%。  三、募集海外公司債償還方法及期限： （一）償還方法：本債券除已被提前贖回、提前賣回並註銷或轉換外，發行公司應 於到期日，按本債券面額加計年利率為1.7% （按半年計算）之收益率（下稱 「到期贖回金額」），以美金將本債券贖回。 （二）期限：自發行日起滿5年之日為到期日，到期日為民國120年9月17日。  四、轉換辦法及重要約定事項： （一）轉換標的：本公司新發行之普通股。 （二）轉換期間：除提前將本債券贖回或賣回並註銷或停止轉換期間（定義如下） 外，債券持有人得於本債券發行日後屆滿三個月（不含發行日）之翌日起，至(1)到 期日前10日止或(2)債券持有人行使賣回權之賣回日或發行公司行使提前贖回權之贖 回日（不含本債券到期日）前第5個營業日止，依相關法令及受託契約之規定，隨時 向發行公司請求將本債券轉換為發行公司之普通股。依目前中華民國法令規定，前述 不得行使轉換權之停止轉換期間係指：A. 依中華民國法律停止過戶之期間，惟不 包括本公司股東常會及股東臨時會之停止過戶期間。 B. 若本公司辦理無償配 股、現金股息或現金增資時，自本公司無償配股停止過戶日、現金股息停止過戶日 或現金增資認股停止過戶首日前十五個營業日起，至權利分派基準日止。 C. 如 本公司辦理減資者，自本公司辦理減資之減資基準日起至減資換發股票開始交易日前 一日止。 D. 如本公司辦理股票變更面額者，自本公司辦理股票變更面額之停止 轉換起始日至新股換發股票開始交易日前一日止。 E.	其他依中華民國法令 或臺灣證券交易所規定之停止過戶期間。 前項(D)變更面額之停止轉換起始日係指向 經濟部申請變更登記之前一個營業日。本公司並應於該起始日前四個營業日公告停止 轉換期間。 前述有關停止過戶期間之法令如有修正，應依修正後法令辦理。 （三）轉換價格：轉換價格為新臺幣1,384.60元，轉換價格以訂價日民國115年9月 10日本公司於臺灣證券交易所普通股收盤價新臺幣989元之140%訂定之。 （四）轉換價格調整：本債券發行後，轉換價格應依受託契約（以下簡稱「受託契約」 ）相關反稀釋條款調整之。 （五）債券持有人賣回權：除下列情事外，本債券之持有人不得要求發行公司於到期 日前將其持有本債券全部或部分贖回：（1）除本債券被提前贖回、賣回並註銷或轉 換外，公司債債券持有人得於公司債發行屆滿2年及4年當日（即民國117年 9月17日及民國119年9月17日），要求本公司依本債券面額加計年利率 1.7%之利息補償金，且以每半年為計算基礎所得之金額（簡稱「提前賣回金額」） ，將本債券全部或部分贖回。（2）若本公司普通股在臺灣證券交易所終止上市，各債 券持有人得要求本公司依提前賣回金額將本債券全部或部分贖回。（3）若本公司發生 本債券受託契約（以下簡稱「受託契約」）所定義之控制權變動情事時，各債券持有人 得要求本公司依提前賣回金額將本債券全部或部分贖回。債券持有人行使前述賣回權， 及本公司受理債券持有人之賣回請求，應依據受託契約所訂賣回程序為之。提前賣回金 額將由本公司於受託契約所訂之付款日以現金支付。 （六）本公司之提前贖回權：除下列情事外，發行公司於本債券存續期間內不得於到期 日前任何時間將本債券全部或部分贖回：（1）公司債於民國118年9月17日起至 到期日前，如發行公司普通股於台灣證券交易所之收盤價格，連續三十個營業日中有二 十個交易日(如遇除權或除息者，於除權或除息交易日至除權或除息基準日之間，採用 之收盤價格，應先設算為除權或除息前之價格)達提前贖回金額（定義於後）除以本債 券面額再乘以當時轉換價格後所得之總數130%時，發行公司得以提前贖回金額贖回 全部或部份本債券。（2）超過百分之九十之本債券已被贖回、經債券持有人行使轉換 權、賣回並註銷時，發行公司得依提前贖回金額將尚流通在外之本債券全部贖回。（3） 因中華民國稅務法令修正，致使發行公司於發行日後因本債券而稅務負擔增加或必須支 付額外之利息費用或增加成本時，發行公司得依提前贖回金額提前將本債券全部贖回。 惟，發行公司通知提前贖回時，如本債券流通在外本金金額逾發行日本債券本金金額之 百分之十，則債券持有人得選擇是否參與贖回。倘債券持有人不參與贖回，該債券持有 人不得請求發行公司負擔額外之稅賦或費用。本公司行使提前贖回權，應依據受託契約 所訂之贖回程序為之，本公司將於受託契約所訂之贖回日以現金贖回本債券。提前贖回 金額係指本債券面額加計年利率1.7%之利息補償金，且以每半年為計算基礎所得之金額 。  五、發行及交易地點：新加坡交易所。  六、資金運用計畫及預計可能產生之效益：支應外幣購料之資金需求。  七、對股東權益之主要影響：本次所發行之海外無擔保轉換公司債若全部按發行後轉換 價格轉換為普通股，如全數轉換，則原股東股權之稀釋比率約為4.40%，其對原股東股 權稀釋比例效果尚屬有限。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260911 | 2357 | 華碩 | revenue_breakout_low_response | 營收爆發低反應股 | 17 | 11 | A_優先追蹤 |  |  | no_signal | stale_signal | 1.事實發生日:115/09/10 2.公司名稱:華碩電腦股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司海外第二次無擔保轉換公司債完成訂價 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 一、募集海外公司債總額、債券每張金額、發行價格及預定發行日期： （一）募集海外公司債總額：美金15億元，僅發行B券公司債。 （二）債券每張面額：美金20萬元，或如超過美金20萬元，以美金10萬元之整數倍 數發行。 （三）發行價格：按面額100%發行。 （四）預定發行日期：115年9月17日。  二、募集海外公司債之利率：票面利率為年利率0%。  三、募集海外公司債償還方法及期限： （一）償還方法：本債券除已被提前贖回、提前賣回並註銷或轉換外，發行公司應 於到期日，按本債券面額加計年利率為1.7% （按半年計算）之收益率（下稱 「到期贖回金額」），以美金將本債券贖回。 （二）期限：自發行日起滿5年之日為到期日，到期日為民國120年9月17日。  四、轉換辦法及重要約定事項： （一）轉換標的：本公司新發行之普通股。 （二）轉換期間：除提前將本債券贖回或賣回並註銷或停止轉換期間（定義如下） 外，債券持有人得於本債券發行日後屆滿三個月（不含發行日）之翌日起，至(1)到 期日前10日止或(2)債券持有人行使賣回權之賣回日或發行公司行使提前贖回權之贖 回日（不含本債券到期日）前第5個營業日止，依相關法令及受託契約之規定，隨時 向發行公司請求將本債券轉換為發行公司之普通股。依目前中華民國法令規定，前述 不得行使轉換權之停止轉換期間係指：A. 依中華民國法律停止過戶之期間，惟不 包括本公司股東常會及股東臨時會之停止過戶期間。 B. 若本公司辦理無償配 股、現金股息或現金增資時，自本公司無償配股停止過戶日、現金股息停止過戶日 或現金增資認股停止過戶首日前十五個營業日起，至權利分派基準日止。 C. 如 本公司辦理減資者，自本公司辦理減資之減資基準日起至減資換發股票開始交易日前 一日止。 D. 如本公司辦理股票變更面額者，自本公司辦理股票變更面額之停止 轉換起始日至新股換發股票開始交易日前一日止。 E.	其他依中華民國法令 或臺灣證券交易所規定之停止過戶期間。 前項(D)變更面額之停止轉換起始日係指向 經濟部申請變更登記之前一個營業日。本公司並應於該起始日前四個營業日公告停止 轉換期間。 前述有關停止過戶期間之法令如有修正，應依修正後法令辦理。 （三）轉換價格：轉換價格為新臺幣1,384.60元，轉換價格以訂價日民國115年9月 10日本公司於臺灣證券交易所普通股收盤價新臺幣989元之140%訂定之。 （四）轉換價格調整：本債券發行後，轉換價格應依受託契約（以下簡稱「受託契約」 ）相關反稀釋條款調整之。 （五）債券持有人賣回權：除下列情事外，本債券之持有人不得要求發行公司於到期 日前將其持有本債券全部或部分贖回：（1）除本債券被提前贖回、賣回並註銷或轉 換外，公司債債券持有人得於公司債發行屆滿2年及4年當日（即民國117年 9月17日及民國119年9月17日），要求本公司依本債券面額加計年利率 1.7%之利息補償金，且以每半年為計算基礎所得之金額（簡稱「提前賣回金額」） ，將本債券全部或部分贖回。（2）若本公司普通股在臺灣證券交易所終止上市，各債 券持有人得要求本公司依提前賣回金額將本債券全部或部分贖回。（3）若本公司發生 本債券受託契約（以下簡稱「受託契約」）所定義之控制權變動情事時，各債券持有人 得要求本公司依提前賣回金額將本債券全部或部分贖回。債券持有人行使前述賣回權， 及本公司受理債券持有人之賣回請求，應依據受託契約所訂賣回程序為之。提前賣回金 額將由本公司於受託契約所訂之付款日以現金支付。 （六）本公司之提前贖回權：除下列情事外，發行公司於本債券存續期間內不得於到期 日前任何時間將本債券全部或部分贖回：（1）公司債於民國118年9月17日起至 到期日前，如發行公司普通股於台灣證券交易所之收盤價格，連續三十個營業日中有二 十個交易日(如遇除權或除息者，於除權或除息交易日至除權或除息基準日之間，採用 之收盤價格，應先設算為除權或除息前之價格)達提前贖回金額（定義於後）除以本債 券面額再乘以當時轉換價格後所得之總數130%時，發行公司得以提前贖回金額贖回 全部或部份本債券。（2）超過百分之九十之本債券已被贖回、經債券持有人行使轉換 權、賣回並註銷時，發行公司得依提前贖回金額將尚流通在外之本債券全部贖回。（3） 因中華民國稅務法令修正，致使發行公司於發行日後因本債券而稅務負擔增加或必須支 付額外之利息費用或增加成本時，發行公司得依提前贖回金額提前將本債券全部贖回。 惟，發行公司通知提前贖回時，如本債券流通在外本金金額逾發行日本債券本金金額之 百分之十，則債券持有人得選擇是否參與贖回。倘債券持有人不參與贖回，該債券持有 人不得請求發行公司負擔額外之稅賦或費用。本公司行使提前贖回權，應依據受託契約 所訂之贖回程序為之，本公司將於受託契約所訂之贖回日以現金贖回本債券。提前贖回 金額係指本債券面額加計年利率1.7%之利息補償金，且以每半年為計算基礎所得之金額 。  五、發行及交易地點：新加坡交易所。  六、資金運用計畫及預計可能產生之效益：支應外幣購料之資金需求。  七、對股東權益之主要影響：本次所發行之海外無擔保轉換公司債若全部按發行後轉換 價格轉換為普通股，如全數轉換，則原股東股權之稀釋比率約為4.40%，其對原股東股 權稀釋比例效果尚屬有限。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2357 | 華碩 | 7 | 7 | 5 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2357 | 華碩 | 126 | 6 | 12757750.0 | 347220.0 | 36.74 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
