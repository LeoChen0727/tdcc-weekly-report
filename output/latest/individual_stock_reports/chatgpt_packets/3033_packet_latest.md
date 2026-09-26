# INDIVIDUAL STOCK CHATGPT PACKET - 3033 威健

## Metadata
- generated_at: 2026-09-26 15:51:42 Asia/Taipei
- stock_id: 3033
- stock_name: 威健
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
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
- date: 20260924
- open: 41.6
- high: 41.85
- low: 41.1
- close: 41.8
- volume: 1650028
- ma5: 41.67
- ema23_primary: 42.98
- distance_to_ema23_pct: -2.74
- ma20: 42.62
- ma60: 46.35
- ma120: 45.27
- return_5d: 0
- return_20d: -7.52
- volume_ratio: 0.53
- distance_to_ma20_pct_auxiliary: -1.93
- distance_to_high_60_pct: -29.63

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,45.75,46.05,45.05,45.05,3494460,46.79,-3.71,47.05,48.64,0.59
20260831,45.05,45.05,44.15,44.55,2659811,46.6,-4.4,46.94,48.55,0.46
20260901,44.7,44.95,44.2,44.25,3621107,46.4,-4.64,46.74,48.42,0.63
20260902,44.15,44.8,43.8,44.65,2360401,46.26,-3.48,46.59,48.37,0.43
20260903,44.7,45,44.1,44.15,2823183,46.08,-4.19,46.4,48.25,0.54
20260904,44.55,44.65,43.55,43.95,3416436,45.9,-4.26,46.25,48.15,0.66
20260907,44.3,44.55,43.2,43.25,4248723,45.68,-5.33,45.94,48.04,0.84
20260908,43.5,43.7,42.8,43.3,2464313,45.48,-4.8,45.59,47.94,0.52
20260909,43.05,43.1,41.3,41.85,10098275,45.18,-7.37,45.16,47.81,2.1
20260910,41.95,42.25,41.45,42.05,2958922,44.92,-6.39,44.84,47.69,0.7
20260911,41.5,41.95,41.35,41.55,2044160,44.64,-6.92,44.5,47.57,0.51
20260914,41.4,41.75,40.25,41.4,2824456,44.37,-6.69,44.24,47.44,0.75
20260915,41.25,41.6,40.8,40.8,2357253,44.07,-7.42,44,47.26,0.64
20260916,41.1,41.55,40.95,41.5,1557663,43.86,-5.38,43.82,47.12,0.44
20260917,41.85,42,41.2,41.8,3684896,43.69,-4.32,43.65,46.98,1.06
20260918,42.1,42.3,41.6,41.6,2451771,43.51,-4.4,43.45,46.85,0.72
20260921,41.85,42.05,41.5,41.9,1680935,43.38,-3.41,43.21,46.73,0.52
20260922,42.3,42.35,41.4,41.45,2226519,43.22,-4.09,42.98,46.61,0.7
20260923,42.5,42.8,41.5,41.6,3228684,43.08,-3.44,42.79,46.48,1.02
20260924,41.6,41.85,41.1,41.8,1650028,42.98,-2.74,42.62,46.35,0.53
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 39.16
- over_600_ratio: 36.4
- over_800_ratio: 34.55
- over_1000_ratio: 32.11
- over_400_change_1w: -0.37
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.79
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,42.47,0.31,37.9,0.57,36.2,0.43,4,False,True
20260717,45.53,3.06,40.87,2.97,38.46,2.26,5,True,True
20260724,43.88,-1.65,38.56,-2.31,36.14,-2.32,0,False,False
20260731,43.25,-0.63,37.85,-0.71,35.09,-1.05,0,False,False
20260807,43.62,0.37,38.62,0.77,36.41,1.32,1,True,True
20260814,44.05,0.43,38.98,0.36,36.73,0.32,2,True,True
20260821,42.43,-1.62,37.48,-1.5,35.56,-1.17,0,False,False
20260828,41.53,-0.9,37.16,-0.32,35.62,0.06,1,False,True
20260904,40.88,-0.65,36.41,-0.75,34.53,-1.09,0,False,False
20260911,39.54,-1.34,34.61,-1.8,32.57,-1.96,0,False,False
20260918,39.53,-0.01,34.6,-0.01,32.9,0.33,1,False,True
20260924,39.16,-0.37,34.55,-0.05,32.11,-0.79,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3033 | 威健 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/07/13 2.被背書保證之: (1)公司名稱:Weikeng International Co., Ltd.(WKI) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):10,332,950 (5)本次新增背書保證之金額(仟元):321,500 (6)迄事實發生日止背書保證餘額(仟元):10,654,450 (7)被背書保證公司實際動支金額(仟元):8,076,872 (8)本次新增背書保證之原因: 因子公司WKI營運資金需求下,向台中銀行申請融資 額度(續約+新約),該銀行要求母公司威健實業股份有 限公司為子公司擔保,故背書保證金額增加. (1)公司名稱:WEIKENG TECHNOLOGY PTE LTD. (WTP) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):1,221,700 (5)本次新增背書保證之金額(仟元):578,700 (6)迄事實發生日止背書保證餘額(仟元):1,800,400 (7)被背書保證公司實際動支金額(仟元):992,637 (8)本次新增背書保證之原因: 因子公司WTP營運資金需求下,向匯豐銀行等申請 融資額度(續約+新約),該銀行要求母公司威健實業 股份有限公司為子公司擔保,故背書保證金額增加. 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,506,772 (2)累積盈虧金額(仟元):5,653,175 5.解除背書保證責任之: (1)條件: 子公司與銀行之授信契約到期,已無任何借貸行為且不續約, 即背書保證責任之解除. (2)日期: 解除日期：115/5   USD38,500,000.00    NTD500,000,000          115/6   USD10,000,000.00 6.背書保證之總限額(仟元): 31,948,674 7.迄事實發生日為止，背書保證餘額(仟元): 17,097,020 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 160.54 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 160.54 10.其他應敘明事項: WKI資本額：2,171,313仟元  WKI累積盈虧：5,512,109仟元 WTP資本額：335,459仟元    WTP累積盈虧：141,066仟元 新約(係指原舊約續展)董事會已先行通過,致舊約尚未到期之銀行背書保證額度重疊 其金額分別為：WKI：803,750仟元(115/7到期NTD160,750仟元,                              115/8到期NTD385,800仟元,                              115/10到期NTD257,200仟元)              WTP：160,750仟元(115/8到期NTD64,300仟元,                               115/10到期NTD96,450仟元)              WKS：661,780仟元(115/7到期NTD330,890仟元,                              115/9到期NTD330,890仟元)；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 3033 | 威健 | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 39 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.事實發生日:115/07/13 2.被背書保證之: (1)公司名稱:Weikeng International Co., Ltd.(WKI) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):10,332,950 (5)本次新增背書保證之金額(仟元):321,500 (6)迄事實發生日止背書保證餘額(仟元):10,654,450 (7)被背書保證公司實際動支金額(仟元):8,076,872 (8)本次新增背書保證之原因: 因子公司WKI營運資金需求下,向台中銀行申請融資 額度(續約+新約),該銀行要求母公司威健實業股份有 限公司為子公司擔保,故背書保證金額增加. (1)公司名稱:WEIKENG TECHNOLOGY PTE LTD. (WTP) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):1,221,700 (5)本次新增背書保證之金額(仟元):578,700 (6)迄事實發生日止背書保證餘額(仟元):1,800,400 (7)被背書保證公司實際動支金額(仟元):992,637 (8)本次新增背書保證之原因: 因子公司WTP營運資金需求下,向匯豐銀行等申請 融資額度(續約+新約),該銀行要求母公司威健實業 股份有限公司為子公司擔保,故背書保證金額增加. 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,506,772 (2)累積盈虧金額(仟元):5,653,175 5.解除背書保證責任之: (1)條件: 子公司與銀行之授信契約到期,已無任何借貸行為且不續約, 即背書保證責任之解除. (2)日期: 解除日期：115/5   USD38,500,000.00    NTD500,000,000          115/6   USD10,000,000.00 6.背書保證之總限額(仟元): 31,948,674 7.迄事實發生日為止，背書保證餘額(仟元): 17,097,020 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 160.54 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 160.54 10.其他應敘明事項: WKI資本額：2,171,313仟元  WKI累積盈虧：5,512,109仟元 WTP資本額：335,459仟元    WTP累積盈虧：141,066仟元 新約(係指原舊約續展)董事會已先行通過,致舊約尚未到期之銀行背書保證額度重疊 其金額分別為：WKI：803,750仟元(115/7到期NTD160,750仟元,                              115/8到期NTD385,800仟元,                              115/10到期NTD257,200仟元)              WTP：160,750仟元(115/8到期NTD64,300仟元,                               115/10到期NTD96,450仟元)              WKS：661,780仟元(115/7到期NTD330,890仟元,                              115/9到期NTD330,890仟元)；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3033 | 威健 | 49 | 26 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3033 | 威健 | 36 | 1 | 143580.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
