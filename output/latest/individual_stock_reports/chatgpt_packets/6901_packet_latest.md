# INDIVIDUAL STOCK CHATGPT PACKET - 6901 鑽石投資

## Metadata
- generated_at: 2026-08-22 22:28:52 Asia/Taipei
- stock_id: 6901
- stock_name: 鑽石投資
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
- date: 20260821
- open: 17
- high: 17.3
- low: 16.75
- close: 17.3
- volume: 2044834
- ma5: 16.77
- ema23_primary: 17.05
- distance_to_ema23_pct: 1.45
- ma20: 16.91
- ma60: 16.97
- ma120: 15.56
- return_5d: 4.85
- return_20d: 4.53
- volume_ratio: 0.83
- distance_to_ma20_pct_auxiliary: 2.29
- distance_to_high_60_pct: -22.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,16.5,17.45,16.4,17.4,2180207,17.8,-2.24,18.51,15.92,0.39
20260728,17.15,17.5,16.8,17.45,2233190,17.77,-1.8,18.48,15.98,0.41
20260729,17.5,17.5,16.2,16.75,2674716,17.68,-5.28,18.38,16.04,0.5
20260730,16.75,16.75,15.75,15.75,2410321,17.52,-10.12,18.24,16.07,0.46
20260731,16.6,16.6,16.25,16.3,1036603,17.42,-6.44,18.16,16.12,0.2
20260803,16.4,17.1,16.35,16.95,1305385,17.38,-2.49,18.06,16.19,0.27
20260804,16.3,16.9,16.15,16.85,1545085,17.34,-2.81,17.96,16.25,0.34
20260805,16.9,17.9,16.9,17.6,2108183,17.36,1.39,17.88,16.31,0.47
20260806,17.35,17.65,17.2,17.5,1203073,17.37,0.74,17.7,16.38,0.32
20260807,17.5,18.7,17.5,17.95,3162584,17.42,3.05,17.56,16.43,1.08
20260810,17,17,16.2,16.3,7060030,17.33,-5.92,17.44,16.47,2.54
20260811,16.25,16.85,16,16.85,5375340,17.29,-2.52,17.34,16.52,1.91
20260812,16.9,17.4,16.8,16.9,3765013,17.25,-2.05,17.23,16.57,1.33
20260813,17.2,17.6,17.15,17.35,2847724,17.26,0.51,17.14,16.63,1
20260814,17.45,17.45,16.4,16.5,2728261,17.2,-4.06,17.05,16.68,1.03
20260817,16.7,17,16.55,17,1493658,17.18,-1.06,17.01,16.73,0.58
20260818,16.95,17,16.45,16.55,1276460,17.13,-3.38,16.96,16.77,0.5
20260819,16.5,16.5,16.1,16.2,965144,17.05,-5,16.89,16.82,0.39
20260820,16.5,16.95,16.5,16.8,2046720,17.03,-1.36,16.88,16.89,0.82
20260821,17,17.3,16.75,17.3,2044834,17.05,1.45,16.91,16.97,0.83
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 82.84
- over_600_ratio: 81.74
- over_800_ratio: 81.09
- over_1000_ratio: 80.65
- over_400_change_1w: -0.12
- over_800_change_1w: -0.13
- over_1000_change_1w: -0.23
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,84.86,-0.03,84.03,0.12,83.6,0.02,1,False,True
20260612,84.81,-0.05,83.59,-0.44,83.15,-0.45,0,False,False
20260618,84.85,0.04,83.72,0.13,83.08,-0.07,1,False,True
20260626,84.71,-0.14,83.36,-0.36,82.82,-0.26,0,False,False
20260703,83.69,-1.02,82.27,-1.09,81.94,-0.88,0,False,False
20260709,83.79,0.1,82.13,-0.14,81.58,-0.36,1,False,False
20260717,83.19,-0.6,81.47,-0.66,80.93,-0.65,0,False,False
20260724,82.94,-0.25,81.25,-0.22,80.81,-0.12,0,False,False
20260731,83.13,0.19,81.17,-0.08,80.84,0.03,1,False,True
20260807,83.01,-0.12,81.34,0.17,80.9,0.06,2,False,True
20260814,82.96,-0.05,81.22,-0.12,80.88,-0.02,3,False,False
20260821,82.84,-0.12,81.09,-0.13,80.65,-0.23,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6901 | 鑽石投資 | pattern | 型態觀察 | 46.0 |  |  | base_building |  |  | stale_signal | 1.事實發生日:115/07/07 2.公司名稱:鑽石生技投資股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:   依據臺灣證券交易所股份有限公司112年6月29日臺證上一字第1121802934號   函規定，本公司股票初次上市時出具之承諾事項如下：   (一)於公開說明書特別記載事項乙節中揭露以下事項：       1.最近三年度與截至最近期業績變化之合理性。       2.與投資標的合一生技股份有限公司相互持股之緣由、適法性、合理性、營運         風險及因應措施。   (二)為降低相互持股對損益造成之影響，不再增加持有合一生技股份有限公司股份，       並於113年12月31日前處分所持合一生技股份有限公司所有股份。   (三)內部人及前十大股東承諾延長股票集中保管期間，上市屆滿2年後，每屆滿6個月       可領回四分之一，滿4年後始得全數領回。前述人員於上市後至集保期間屆滿前，       因盈餘轉增資或其他原因(如執行員工認股權及員工分紅等)而取得之股份，應       提交集中保管，並於最後一次領回日始得領回。   (四)上市後增設「提名委員會」，並於113年股東常會增選獨立董事達全體董事席次       三分之二以上。   (五)公開說明書應加強揭露下列事項：       1.生技創投公司的特性與投資風險(包括但不限於其投資標的所包括之未上市櫃         或非公開發行公司之公允價值欠缺透明度；其投資標的組合可能產生重大變動         等)。       2.公司未來投資標的之方針、策略、範圍、地區、決策過程及行使表決權之處理         原則及方法等。       3.封面載明「本公司業務性質為創業投資公司型態且以生技產業為主要投資標的         ，生技產業開發時程長，投入經費高且未保證一定能成功，請投資人特別注意         且詳細閱讀本公司公開說明書內容並審慎投資。」。       4.產業、營運及其他重要風險乙節載明「...本公司主要投資標的為生技類股，         其股價及公允價值受研發成果之影響甚大，因而產生較鉅幅之波動。因此若         公允價值下跌可能導致本公司營業收入為負數…」。   (六)經董事會通過修訂本公司「取得或處分資產處理程序」、「投資業務作業辦法」       及「投資業務風險控管辦法」之下列投資業務相關規範，「取得或處分資產處理       程序」並應提報最近一次股東會通過：       1.董事長核決權限由新台幣5億元調降為3億元，凡取得或處分投資之交易金額         超過3億元者，均須經投資審議委員會、審計委員會及董事會通過後始得為之。         前述金額應採累積計算，且母公司與子公司(若有)合併計算。       2.訂定明確投資標的退場機制：         (1)通知評估：就上市及上櫃投資標的之未實現獲利達原始投資成本3倍或未實            現損失達原始投資成本30%者，投資部發出通知或預警並擬訂持有或處分評            估方案，若評估為處分退場，即依核決權限執行(預估獲利金額且交易金額            在新台幣三億元(含)以下由董事長核定；預估獲利金額或交易金額在新台幣            三億元以上，須經投資審議委員會、審計委員會及董事會通過後始得為之)            ；若評估為繼續持有，應提報投資審議委員會同意。         (2)強制退場：若未實現獲利達原始投資成本5倍或未實現損失達原始投資成本            50%強制退場條件，投資部發出通知或預警並擬訂處分退場方案，依核決            權限執行 (同上段所述)。若決議不處分退場，應將例外管理方案提報投資            審議委員會、審計委員會、董事會決議執行，並定期於董事會報告執行情            形。   (七)上市後辦理資訊揭露如下：       1.每日於官網公告屬上市/櫃及興櫃股票之投資標的公允價值。       2.每月於官網及以重大訊息公告「所有投資標的」股數變動及公允價值變動、         本公司每股淨值、現金及約當現金餘額。       3.按季舉辦法人說明會，向投資人說明財務業務狀況及營收認列特性。       4.若公司連續3個月營業收入呈現負數，應發布重大訊息提醒投資人注意。 6.因應措施:   (一)相關內容均已於112年9月刊印之「現金增資發行新股辦理上市前公開承銷暨股票       初次上市用」公開說明書中作適當揭露，請詳公開資訊觀測站。   (二)已於113年10月25日完成處分所持合一生技股份有限公司所有股份。   (三)內部人及前十大股東已依規定延長股票集中保管期間，上市屆滿2年後，每屆滿       6個月可領回四分之一，滿4年後始得全數領回。前述人員因員工認股權而取得       之股份，亦已提交集中保管，並於最後一次領回日始得領回。   (四)已於112年10月13日董事會通過增設「提名委員會」，並於113年5月21日股東       常會全面改選第6屆董事，改選後獨立董事達全體董事席次三分之二以上，已於       113年8月1日就任。   (五)相關內容均已於112年9月刊印之「現金增資發行新股辦理上市前公開承銷暨股票       初次上市用」公開說明書中作適當揭露，請詳公開資訊觀測站。   (六)已於112年7月20日董事會通過修訂投資業務相關規範。另「取得或處分資產處理       程序」已提報113年5月21日股東常會通過。   (七)資訊揭露辦理情形如下：       1.已於112年9月1日起每日於官網公告屬上市/櫃及興櫃股票之投資標的公允         價值。       2.已每月於官網及以重大訊息公告「所有投資標的」股數變動及公允價值變動、         本公司每股淨值、現金及約當現金餘額。       3.已自112年第四季起按季舉辦法人說明會，向投資人說明財務業務狀況及營收         認列特性。       4.若連續3個月營業收入呈現負數，將發布重大訊息提醒投資人注意。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):    無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6901 | 鑽石投資 | 1 | 1 | 2 | 6 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
