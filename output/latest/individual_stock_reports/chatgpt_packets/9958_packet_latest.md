# INDIVIDUAL STOCK CHATGPT PACKET - 9958 世紀鋼

## Metadata
- generated_at: 2026-09-05 15:54:57 Asia/Taipei
- stock_id: 9958
- stock_name: 世紀鋼
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/9958_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/9958_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9958_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9958_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9958_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9958_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9958_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9958_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/9958_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/9958_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/9958_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/9958_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9958.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9958.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9958.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9958.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9958_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9958_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9958_latest.md?ref=main

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
- date: 20260904
- open: 88.6
- high: 89.1
- low: 87.3
- close: 88.1
- volume: 1659464
- ma5: 89.54
- ema23_primary: 97.78
- distance_to_ema23_pct: -9.9
- ma20: 98.57
- ma60: 108.32
- ma120: 108.8
- return_5d: -4.45
- return_20d: -22.38
- volume_ratio: 0.79
- distance_to_ma20_pct_auxiliary: -10.62
- distance_to_high_60_pct: -29.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,114.5,116.5,113.5,116,2267484,110.7,4.78,110.55,111.23,1.23
20260811,115.5,116,112,113.5,1786692,110.94,2.31,110.4,111.38,0.98
20260812,109,109,106,107,4177436,110.61,-3.26,109.8,111.41,2.18
20260813,106.5,106.5,104,104.5,2272545,110.1,-5.09,109.1,111.42,1.17
20260814,105,105.5,102.5,103,2039243,109.51,-5.94,108.7,111.45,1.07
20260817,103,104,102,102.5,1307328,108.92,-5.9,108.17,111.44,0.69
20260818,103,103.5,101,101,1815464,108.26,-6.71,107.47,111.43,0.95
20260819,100,100.5,99.1,99.5,2358541,107.53,-7.47,106.67,111.35,1.21
20260820,100,101.5,99.9,101,1454551,106.99,-5.6,106.22,111.28,0.75
20260821,101,104,101,102,1346793,106.57,-4.29,105.8,111.28,0.69
20260824,99.4,99.8,97.3,97.3,4841452,105.8,-8.03,105.22,111.19,2.36
20260825,96.6,96.7,94,94.8,2434862,104.88,-9.61,104.7,111.04,1.17
20260826,94.5,95.8,94.5,95.3,1084081,104.09,-8.44,104.27,110.88,0.54
20260827,95.3,95.3,94,94.1,2064876,103.25,-8.86,103.9,110.74,1
20260828,94,94,92,92.2,2521392,102.33,-9.9,103.28,110.5,1.2
20260831,91.3,91.4,90.2,90.3,2142011,101.33,-10.88,102.53,110.04,1
20260901,90.4,92,90.4,90.6,1612960,100.44,-9.79,101.78,109.53,0.74
20260902,90.6,91.2,90.3,90.3,1247578,99.59,-9.33,100.94,109.12,0.57
20260903,90.4,90.8,88.4,88.4,1656324,98.66,-10.4,99.84,108.7,0.76
20260904,88.6,89.1,87.3,88.1,1659464,97.78,-9.9,98.57,108.32,0.79
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 47.33
- over_600_ratio: 44.23
- over_800_ratio: 41.91
- over_1000_ratio: 41.22
- over_400_change_1w: -1.36
- over_800_change_1w: -0.39
- over_1000_change_1w: -0.39
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,53.4,0.3,45.59,-0.07,44.13,0.3,1,False,True
20260626,52.79,-0.61,45.09,-0.5,43.98,-0.15,0,False,False
20260703,52.73,-0.06,44.78,-0.31,43.64,-0.34,0,False,False
20260709,53.15,0.42,44.97,0.19,43.85,0.21,1,True,True
20260717,53.73,0.58,46.11,1.14,44.7,0.85,2,True,True
20260724,53.36,-0.37,45.63,-0.48,43.4,-1.3,0,False,False
20260731,53.12,-0.24,44.86,-0.77,43.1,-0.3,0,False,False
20260807,53.38,0.26,44.64,-0.22,43.22,0.12,1,False,True
20260814,52.38,-1,44.38,-0.26,43.33,0.11,2,False,True
20260821,50.99,-1.39,43.96,-0.42,42.57,-0.76,0,False,False
20260828,48.69,-2.3,42.3,-1.66,41.61,-0.96,0,False,False
20260904,47.33,-1.36,41.91,-0.39,41.22,-0.39,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 9958 | 世紀鋼 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/09/02 2.公司名稱:世紀鋼鐵結構股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由: (1) 本公司申報募集與發行現金增資普通股20,000,000股，每股面額10元，總額新臺幣 200,000,000元，業經金融監督管理委員會115年6月15日金管證發字第1150345675號函申 報生效在案。 (2) 考量近期受極端氣候及風災影響，已發生多次全台或部分縣市停班停課情形，為避 免增資相關作業時程受到停班影響，確保本次現金增資資金募集作業順利完成，以維護 股東權益，故向金融監督管理委員會申請延長募集期間三個月，展延至115年12月14日 以前募集完成，業經金融監督管理委員會115年9月1日金管證發字第1150354481號函准予 備查在案，募集期間延長至115年12月14日。 (3) 原定繳款日期及增資時程不變，如遇天然災害停班則順延，以維護股東繳款權益。 6.因應措施: 本次現金增資案如未能依原訂計畫時程完成募資作業，致已繳款原股東、員工及認股人 等之權益受影響，為確保原股東、員工及認股人等之權益，訂定相關補償方案如下： (1)適用對象：本次現金增資認購股款之原股東、員工及認股人等 (2)應退還股款之退還日期及方式 若因投資人繳款爭議、繳款作業延遲，或其他相關事由致影響股款繳納及資金募集時程 ，對於本補償方案公告日前已繳款之原股東、員工及認股人等，本公司將加計利息退還 其所繳納之股款，計算公式如下：本公司將加計利息退還其所繳納之股款，計算公式 如下： 認購股款×【1＋(自繳款日至實際退款日之天數(註1))×1.725%/365】 註1：應付款項將以郵寄支票方式或匯款方式支付；退款日期如有異動，本公司將另行公 告。 註2：前述年利率1.725%，係以台灣銀行115年8月28日公告之一年至未滿二年期定期儲蓄 存款牌告固定利率計算之。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 承諾書 本公司115年度現金增資發行新股案，業經金融監督管理委員會115年6月15日金管證發 字第1150345675號申報生效在案，擬申請展延資金募集時間三個月，為保障投資人權益 。 茲承諾若因投資人繳款爭議、繳款作業延遲，或其他相關事由致影響股款繳納及資金募 集時程，造成參與此次現金增資之原股東、員工及認股人等損害，就原股東、員工及認 股人等可能提出合理及具體理由主張其權利受損部分，本立書人同意依法負擔賠償之責 。 此    致 金融監督管理委員會 立書人(負責人)：賴文祥 中華民國115年8月28日；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 9958 | 世紀鋼 | 2 | 2 | 4 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 9958 | 世紀鋼 | 34 | 0 | 89020.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
