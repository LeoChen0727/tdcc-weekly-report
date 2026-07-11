# INDIVIDUAL STOCK CHATGPT PACKET - 3702 大聯大

## Metadata
- generated_at: 2026-07-11 22:27:19 Asia/Taipei
- stock_id: 3702
- stock_name: 大聯大
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3702_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3702_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3702.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3702.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3702.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3702.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3702_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3702_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3702_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- date: 20260709
- open: 106.5
- high: 109.5
- low: 106.5
- close: 106.5
- volume: 6821826
- ma5: 108.2
- ema23_primary: 108.81
- distance_to_ema23_pct: -2.12
- ma20: 108
- ma60: 108.93
- ma120: 91.71
- return_5d: -1.39
- return_20d: -2.29
- volume_ratio: 0.52
- distance_to_ma20_pct_auxiliary: -1.39
- distance_to_high_60_pct: -16.47

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,111,111.5,105.5,108.5,18045469,112.63,-3.66,115.83,103.82,1.18
20260612,111.5,111.5,104,105,20657601,111.99,-6.24,115.58,104.07,1.3
20260615,107,108.5,103.5,107.5,12127021,111.62,-3.69,115.42,104.31,0.76
20260616,109,109.5,106.5,109,10028040,111.4,-2.15,115.45,104.58,0.63
20260617,107,107.5,104.5,107,10172545,111.03,-3.63,114.85,104.84,0.65
20260618,107.5,113,106.5,112,20036329,111.11,0.8,114.28,105.19,1.38
20260622,113.5,114,110.5,112.5,8555913,111.23,1.14,114,105.56,0.61
20260623,112.5,113,108,108,6484321,110.96,-2.67,113.22,105.76,0.47
20260624,107,108,105.5,106.5,3749385,110.59,-3.7,112.47,105.95,0.28
20260625,107,109.5,106,107,10429116,110.29,-2.98,111.8,106.2,0.77
20260626,106,109,105,106.5,9602233,109.97,-3.16,111.05,106.47,0.71
20260629,108,108,103.5,104.5,7796543,109.52,-4.58,110.4,106.74,0.59
20260630,105.5,108.5,105,107,16810000,109.31,-2.11,109.83,107.03,1.23
20260701,107.5,113,105.5,110,51142000,109.36,0.58,109.38,107.39,3.31
20260702,108,109,106,108,17549000,109.25,-1.15,108.88,107.71,1.13
20260703,107,110,107,110,7349098,109.31,0.63,108.55,108.01,0.49
20260706,110,112.5,109.5,110,8221000,109.37,0.58,108.33,108.32,0.56
20260707,111.5,112.5,109,109,9681413,109.34,-0.31,108.38,108.61,0.7
20260708,109,110,104.5,105.5,6789094,109.02,-3.23,108.12,108.76,0.51
20260709,106.5,109.5,106.5,106.5,6821826,108.81,-2.12,108,108.93,0.52
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 84.22
- over_600_ratio: 82.16
- over_800_ratio: 80
- over_1000_ratio: 79.02
- over_400_change_1w: 0.02
- over_800_change_1w: -0.34
- over_1000_change_1w: -0.2
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,85.31,,82,,80.66,,0,False,False
20260508,85.45,0.14,82.15,0.15,80.98,0.32,1,True,True
20260515,85.47,0.02,82,-0.15,80.83,-0.15,2,False,False
20260522,85.52,0.05,81.86,-0.14,80.8,-0.03,3,False,False
20260529,85.24,-0.28,81.85,-0.01,80.63,-0.17,0,False,False
20260605,84.99,-0.25,81.56,-0.29,80.31,-0.32,0,False,False
20260612,84.76,-0.23,81.28,-0.28,80.14,-0.17,0,False,False
20260618,84.37,-0.39,80.5,-0.78,79.57,-0.57,0,False,False
20260626,84.2,-0.17,80.34,-0.16,79.22,-0.35,0,False,False
20260703,84.22,0.02,80,-0.34,79.02,-0.2,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3702 | 大聯大 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.證券名稱: 深圳中電港技術股份有限公司普通股 2.交易日期:115/3/30~115/7/10 3.董事會通過日期: 民國115年6月4日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易期間交易數量：4,521,098股 每股交易金額：人民幣28.75元 交易期間交易總金額：人民幣129,997仟元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益約人民幣109,855仟元 7.與交易標的公司之關係: 非本公司關係人 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 股數：普通股7,208,202股 持有金額：人民幣223,671仟元 持股比例：占普通股0.95% 權利受限情形：無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占公司最近期財務報表中總資產之比例：1.05% 占公司最近期財務報表中歸屬於母公司業主權益之比例：1.33% 營運資金數額：-14,481,673仟元 10.取得或處分之具體目的: 提升資金運用效益及投資獲利 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 115年6月4日 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260709 | 3702 | 大聯大 | revenue_breakout_low_response | 營收爆發低反應股 | 16.0 | 19.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.證券名稱: 深圳中電港技術股份有限公司普通股 2.交易日期:115/3/30~115/7/10 3.董事會通過日期: 民國115年6月4日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易期間交易數量：4,521,098股 每股交易金額：人民幣28.75元 交易期間交易總金額：人民幣129,997仟元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益約人民幣109,855仟元 7.與交易標的公司之關係: 非本公司關係人 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 股數：普通股7,208,202股 持有金額：人民幣223,671仟元 持股比例：占普通股0.95% 權利受限情形：無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占公司最近期財務報表中總資產之比例：1.05% 占公司最近期財務報表中歸屬於母公司業主權益之比例：1.33% 營運資金數額：-14,481,673仟元 10.取得或處分之具體目的: 提升資金運用效益及投資獲利 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 115年6月4日 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3702 | 大聯大 | 27 | 6 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3702 | 大聯大 | 28 | 0 | 1250310.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
