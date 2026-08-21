# INDIVIDUAL STOCK CHATGPT PACKET - 3033 威健

## Metadata
- generated_at: 2026-08-21 22:27:12 Asia/Taipei
- stock_id: 3033
- stock_name: 威健
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3033_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3033_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3033_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3033_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3033_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3033_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3033.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3033.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3033.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3033.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3033_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3033_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3033_latest.md?ref=main

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
- open: 45.15
- high: 45.85
- low: 44.75
- close: 45.45
- volume: 3464194
- ma5: 45.62
- ema23_primary: 47.43
- distance_to_ema23_pct: -4.17
- ma20: 46.87
- ma60: 48.97
- ma120: 43.02
- return_5d: -5.8
- return_20d: -9.1
- volume_ratio: 0.51
- distance_to_ma20_pct_auxiliary: -3.02
- distance_to_high_60_pct: -23.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,50.1,50.1,48.05,48.95,5940151,50,-2.11,50.24,48.71,0.48
20260728,47.45,47.75,45.7,45.95,7485587,49.66,-7.48,50.09,48.88,0.59
20260729,45.95,46.25,41.95,43.45,10669812,49.15,-11.59,49.8,48.97,0.82
20260730,43.05,43.85,41.85,42.1,6357321,48.56,-13.3,49.41,49.03,0.49
20260731,44.95,45.5,43.9,44.3,5181427,48.2,-8.1,49.11,49.06,0.4
20260803,44,47.3,43.7,46.7,5351033,48.08,-2.87,48.92,49.13,0.41
20260804,46.15,48.45,46,48.2,5701765,48.09,0.23,48.81,49.2,0.43
20260805,48.95,49.35,47.55,47.8,8248645,48.07,-0.55,48.73,49.26,0.62
20260806,46.35,48,46.05,47.85,6865812,48.05,-0.41,48.65,49.32,0.51
20260807,48.3,48.35,46.5,47.05,3661206,47.96,-1.91,48.52,49.39,0.27
20260810,47.7,49.85,47.6,49.35,7850970,48.08,2.64,48.44,49.44,0.62
20260811,49.35,51,49.35,50.4,8595689,48.27,4.41,48.43,49.48,0.69
20260812,50.6,52.8,50.2,50.3,8687589,48.44,3.84,48.16,49.5,0.78
20260813,50.9,50.9,48.35,48.6,14182861,48.46,0.3,47.88,49.5,1.62
20260814,48.5,50,48,48.25,6294886,48.44,-0.39,47.86,49.45,0.82
20260817,48.25,48.7,46.5,46.7,7886728,48.29,-3.3,47.8,49.35,1.09
20260818,46.8,46.95,45.5,45.6,4620879,48.07,-5.14,47.61,49.21,0.65
20260819,45,45.35,44.3,45,4460068,47.81,-5.88,47.35,49.14,0.64
20260820,45.45,45.7,44.9,45.35,4576464,47.61,-4.74,47.09,49.06,0.66
20260821,45.15,45.85,44.75,45.45,3464194,47.43,-4.17,46.87,48.97,0.51
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 44.05
- over_600_ratio: 41.02
- over_800_ratio: 38.98
- over_1000_ratio: 36.73
- over_400_change_1w: 0.43
- over_800_change_1w: 0.36
- over_1000_change_1w: 0.32
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,41.88,0.48,36.98,-0.16,35.38,-0.14,1,False,False
20260605,41.74,-0.14,36.94,-0.04,35.04,-0.34,2,False,False
20260612,41.08,-0.66,35.81,-1.13,34.26,-0.78,0,False,False
20260618,41.08,0,36.24,0.43,34.35,0.09,1,False,True
20260626,41.31,0.23,36.33,0.09,34.79,0.44,2,True,True
20260703,42.16,0.85,37.33,1,35.77,0.98,3,True,True
20260709,42.47,0.31,37.9,0.57,36.2,0.43,4,False,True
20260717,45.53,3.06,40.87,2.97,38.46,2.26,5,True,True
20260724,43.88,-1.65,38.56,-2.31,36.14,-2.32,0,False,False
20260731,43.25,-0.63,37.85,-0.71,35.09,-1.05,0,False,False
20260807,43.62,0.37,38.62,0.77,36.41,1.32,1,True,True
20260814,44.05,0.43,38.98,0.36,36.73,0.32,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3033 | 威健 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:115/07/13 2.被背書保證之: (1)公司名稱:Weikeng International Co., Ltd.(WKI) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):10,332,950 (5)本次新增背書保證之金額(仟元):321,500 (6)迄事實發生日止背書保證餘額(仟元):10,654,450 (7)被背書保證公司實際動支金額(仟元):8,076,872 (8)本次新增背書保證之原因: 因子公司WKI營運資金需求下,向台中銀行申請融資 額度(續約+新約),該銀行要求母公司威健實業股份有 限公司為子公司擔保,故背書保證金額增加. (1)公司名稱:WEIKENG TECHNOLOGY PTE LTD. (WTP) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):1,221,700 (5)本次新增背書保證之金額(仟元):578,700 (6)迄事實發生日止背書保證餘額(仟元):1,800,400 (7)被背書保證公司實際動支金額(仟元):992,637 (8)本次新增背書保證之原因: 因子公司WTP營運資金需求下,向匯豐銀行等申請 融資額度(續約+新約),該銀行要求母公司威健實業 股份有限公司為子公司擔保,故背書保證金額增加. 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,506,772 (2)累積盈虧金額(仟元):5,653,175 5.解除背書保證責任之: (1)條件: 子公司與銀行之授信契約到期,已無任何借貸行為且不續約, 即背書保證責任之解除. (2)日期: 解除日期：115/5   USD38,500,000.00    NTD500,000,000          115/6   USD10,000,000.00 6.背書保證之總限額(仟元): 31,948,674 7.迄事實發生日為止，背書保證餘額(仟元): 17,097,020 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 160.54 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 160.54 10.其他應敘明事項: WKI資本額：2,171,313仟元  WKI累積盈虧：5,512,109仟元 WTP資本額：335,459仟元    WTP累積盈虧：141,066仟元 新約(係指原舊約續展)董事會已先行通過,致舊約尚未到期之銀行背書保證額度重疊 其金額分別為：WKI：803,750仟元(115/7到期NTD160,750仟元,                              115/8到期NTD385,800仟元,                              115/10到期NTD257,200仟元)              WTP：160,750仟元(115/8到期NTD64,300仟元,                               115/10到期NTD96,450仟元)              WKS：661,780仟元(115/7到期NTD330,890仟元,                              115/9到期NTD330,890仟元)；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 3033 | 威健 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/07/13 2.被背書保證之: (1)公司名稱:Weikeng International Co., Ltd.(WKI) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):10,332,950 (5)本次新增背書保證之金額(仟元):321,500 (6)迄事實發生日止背書保證餘額(仟元):10,654,450 (7)被背書保證公司實際動支金額(仟元):8,076,872 (8)本次新增背書保證之原因: 因子公司WKI營運資金需求下,向台中銀行申請融資 額度(續約+新約),該銀行要求母公司威健實業股份有 限公司為子公司擔保,故背書保證金額增加. (1)公司名稱:WEIKENG TECHNOLOGY PTE LTD. (WTP) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):1,221,700 (5)本次新增背書保證之金額(仟元):578,700 (6)迄事實發生日止背書保證餘額(仟元):1,800,400 (7)被背書保證公司實際動支金額(仟元):992,637 (8)本次新增背書保證之原因: 因子公司WTP營運資金需求下,向匯豐銀行等申請 融資額度(續約+新約),該銀行要求母公司威健實業 股份有限公司為子公司擔保,故背書保證金額增加. 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,506,772 (2)累積盈虧金額(仟元):5,653,175 5.解除背書保證責任之: (1)條件: 子公司與銀行之授信契約到期,已無任何借貸行為且不續約, 即背書保證責任之解除. (2)日期: 解除日期：115/5   USD38,500,000.00    NTD500,000,000          115/6   USD10,000,000.00 6.背書保證之總限額(仟元): 31,948,674 7.迄事實發生日為止，背書保證餘額(仟元): 17,097,020 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 160.54 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 160.54 10.其他應敘明事項: WKI資本額：2,171,313仟元  WKI累積盈虧：5,512,109仟元 WTP資本額：335,459仟元    WTP累積盈虧：141,066仟元 新約(係指原舊約續展)董事會已先行通過,致舊約尚未到期之銀行背書保證額度重疊 其金額分別為：WKI：803,750仟元(115/7到期NTD160,750仟元,                              115/8到期NTD385,800仟元,                              115/10到期NTD257,200仟元)              WTP：160,750仟元(115/8到期NTD64,300仟元,                               115/10到期NTD96,450仟元)              WKS：661,780仟元(115/7到期NTD330,890仟元,                              115/9到期NTD330,890仟元)；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 3033 | 威健 | revenue_breakout_low_response | 營收爆發低反應股 | 19 | 14 | A_優先追蹤 |  |  | no_signal | stale_signal | 1.事實發生日:115/07/13 2.被背書保證之: (1)公司名稱:Weikeng International Co., Ltd.(WKI) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):10,332,950 (5)本次新增背書保證之金額(仟元):321,500 (6)迄事實發生日止背書保證餘額(仟元):10,654,450 (7)被背書保證公司實際動支金額(仟元):8,076,872 (8)本次新增背書保證之原因: 因子公司WKI營運資金需求下,向台中銀行申請融資 額度(續約+新約),該銀行要求母公司威健實業股份有 限公司為子公司擔保,故背書保證金額增加. (1)公司名稱:WEIKENG TECHNOLOGY PTE LTD. (WTP) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):1,221,700 (5)本次新增背書保證之金額(仟元):578,700 (6)迄事實發生日止背書保證餘額(仟元):1,800,400 (7)被背書保證公司實際動支金額(仟元):992,637 (8)本次新增背書保證之原因: 因子公司WTP營運資金需求下,向匯豐銀行等申請 融資額度(續約+新約),該銀行要求母公司威健實業 股份有限公司為子公司擔保,故背書保證金額增加. 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,506,772 (2)累積盈虧金額(仟元):5,653,175 5.解除背書保證責任之: (1)條件: 子公司與銀行之授信契約到期,已無任何借貸行為且不續約, 即背書保證責任之解除. (2)日期: 解除日期：115/5   USD38,500,000.00    NTD500,000,000          115/6   USD10,000,000.00 6.背書保證之總限額(仟元): 31,948,674 7.迄事實發生日為止，背書保證餘額(仟元): 17,097,020 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 160.54 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 160.54 10.其他應敘明事項: WKI資本額：2,171,313仟元  WKI累積盈虧：5,512,109仟元 WTP資本額：335,459仟元    WTP累積盈虧：141,066仟元 新約(係指原舊約續展)董事會已先行通過,致舊約尚未到期之銀行背書保證額度重疊 其金額分別為：WKI：803,750仟元(115/7到期NTD160,750仟元,                              115/8到期NTD385,800仟元,                              115/10到期NTD257,200仟元)              WTP：160,750仟元(115/8到期NTD64,300仟元,                               115/10到期NTD96,450仟元)              WKS：661,780仟元(115/7到期NTD330,890仟元,                              115/9到期NTD330,890仟元)；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3033 | 威健 | 28 | 6 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3033 | 威健 | 40 | 0 | 859610.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
