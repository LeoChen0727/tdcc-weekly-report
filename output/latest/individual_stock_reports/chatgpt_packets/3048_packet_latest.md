# INDIVIDUAL STOCK CHATGPT PACKET - 3048 益登

## Metadata
- generated_at: 2026-09-26 15:51:44 Asia/Taipei
- stock_id: 3048
- stock_name: 益登
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3048_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3048_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3048.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3048.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3048.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3048.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3048_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3048_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3048_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- open: 50.4
- high: 52
- low: 50
- close: 51.9
- volume: 1556204
- ma5: 50.98
- ema23_primary: 52.2
- distance_to_ema23_pct: -0.57
- ma20: 51.95
- ma60: 54.2
- ma120: 54.98
- return_5d: 2.98
- return_20d: -7.65
- volume_ratio: 1.3
- distance_to_ma20_pct_auxiliary: -0.11
- distance_to_high_60_pct: -22.31

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,57.3,57.9,55.6,55.6,3553464,56.09,-0.87,56.89,59.73,0.72
20260831,55.1,56.3,54.3,54.9,1406697,55.99,-1.94,57.09,59.52,0.29
20260901,54.8,55.6,54.6,54.8,1294083,55.89,-1.95,57.05,59.33,0.32
20260902,54.7,55,54,54,1041777,55.73,-3.11,56.83,59.12,0.31
20260903,54.2,54.4,52.4,52.4,1604527,55.45,-5.51,56.53,58.8,0.49
20260904,53.4,53.8,52.7,53.4,1031546,55.28,-3.4,56.33,58.47,0.36
20260907,54.1,54.1,53.2,53.5,716778,55.13,-2.96,56.13,58.11,0.26
20260908,53.4,53.9,51.9,52,1473165,54.87,-5.24,55.8,57.76,0.58
20260909,52.3,52.6,51.5,51.6,1104961,54.6,-5.49,55.39,57.39,0.52
20260910,51.2,51.6,50.7,51.4,1130620,54.33,-5.4,54.92,57.06,0.66
20260911,50.5,51,50.1,50.2,1079726,53.99,-7.02,54.49,56.69,0.69
20260914,49.5,50.8,49.3,50.2,700043,53.67,-6.47,54.1,56.3,0.48
20260915,50.2,50.3,49.4,49.4,669936,53.32,-7.35,53.8,55.92,0.49
20260916,49.8,50.8,49.6,50.4,630681,53.07,-5.04,53.48,55.6,0.51
20260917,50.5,51.2,50.3,50.4,2037514,52.85,-4.64,53.2,55.29,1.62
20260918,51.2,51.2,50.6,51,619483,52.7,-3.22,52.95,55.03,0.5
20260921,51,51.6,50.7,51.1,735187,52.56,-2.78,52.72,54.83,0.6
20260922,51.8,51.9,50.3,50.5,833056,52.39,-3.61,52.46,54.64,0.7
20260923,51,51,50.1,50.4,803288,52.23,-3.5,52.17,54.44,0.68
20260924,50.4,52,50,51.9,1556204,52.2,-0.57,51.95,54.2,1.3
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 48.04
- over_600_ratio: 44.86
- over_800_ratio: 43.21
- over_1000_ratio: 41.9
- over_400_change_1w: -0.12
- over_800_change_1w: 0.14
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,50.7,-0.55,46.1,-1.1,45.1,-0.78,0,False,False
20260717,50.78,0.08,46.35,0.25,45.35,0.25,1,True,True
20260724,51.32,0.54,46.34,-0.01,45.02,-0.33,2,False,False
20260731,51.36,0.04,46.46,0.12,44.88,-0.14,3,False,True
20260807,49.53,-1.83,44.36,-2.1,43.42,-1.46,0,False,False
20260814,49.68,0.15,44.35,-0.01,42.99,-0.43,1,False,False
20260821,49.3,-0.38,44.46,0.11,43.12,0.13,2,False,True
20260828,49.24,-0.06,43.69,-0.77,42.72,-0.4,0,False,False
20260904,48.69,-0.55,42.77,-0.92,41.46,-1.26,0,False,False
20260911,48.57,-0.12,42.73,-0.04,41.46,0,1,False,False
20260918,48.16,-0.41,43.07,0.34,41.8,0.34,2,False,True
20260924,48.04,-0.12,43.21,0.14,41.9,0.1,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3048 | 益登 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.證券名稱: 蜜望實企業股份有限公司普通股(8043) 2.交易日期:115/7/8~115/7/15 3.董事會通過日期: 民國115年5月13日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量(股):1,983,000 每股平均價格(新台幣元): 160.02 交易總金額(新台幣元):317,321,500 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分為出售透過其他綜合損益按公允價值衡量之金融資產， 處分結果將計入資產負債表之權益項下，不影響本公司當期損益。 7.與交易標的公司之關係: 無。 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 數量：2,119,398股 金額：146,874仟元 持股比例：2.65% 權利受限情形：無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占總資產比例：3.13% 占母公司業主權益比例：18.91% 營運資金：6,603,994仟元 10.取得或處分之具體目的: 財務投資。 11.本次交易表示異議董事之意見: 無。 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用。 14.監察人承認或審計委員會同意日期: 民國 115年 5月 13日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 3048 | 益登 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.證券名稱: 蜜望實企業股份有限公司普通股(8043) 2.交易日期:115/7/8~115/7/15 3.董事會通過日期: 民國115年5月13日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量(股):1,983,000 每股平均價格(新台幣元): 160.02 交易總金額(新台幣元):317,321,500 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分為出售透過其他綜合損益按公允價值衡量之金融資產， 處分結果將計入資產負債表之權益項下，不影響本公司當期損益。 7.與交易標的公司之關係: 無。 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 數量：2,119,398股 金額：146,874仟元 持股比例：2.65% 權利受限情形：無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占總資產比例：3.13% 占母公司業主權益比例：18.91% 營運資金：6,603,994仟元 10.取得或處分之具體目的: 財務投資。 11.本次交易表示異議董事之意見: 無。 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用。 14.監察人承認或審計委員會同意日期: 民國 115年 5月 13日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 3048 | 益登 | revenue_breakout_low_response | 營收爆發低反應股 | 11 | 42 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.證券名稱: 蜜望實企業股份有限公司普通股(8043) 2.交易日期:115/7/8~115/7/15 3.董事會通過日期: 民國115年5月13日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量(股):1,983,000 每股平均價格(新台幣元): 160.02 交易總金額(新台幣元):317,321,500 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分為出售透過其他綜合損益按公允價值衡量之金融資產， 處分結果將計入資產負債表之權益項下，不影響本公司當期損益。 7.與交易標的公司之關係: 無。 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 數量：2,119,398股 金額：146,874仟元 持股比例：2.65% 權利受限情形：無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占總資產比例：3.13% 占母公司業主權益比例：18.91% 營運資金：6,603,994仟元 10.取得或處分之具體目的: 財務投資。 11.本次交易表示異議董事之意見: 無。 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用。 14.監察人承認或審計委員會同意日期: 民國 115年 5月 13日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3048 | 益登 | 1 | 1 | 1 | 5 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3048 | 益登 | 28 | 1 | 118110.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
