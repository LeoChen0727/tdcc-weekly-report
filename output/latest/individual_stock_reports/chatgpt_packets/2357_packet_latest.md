# INDIVIDUAL STOCK CHATGPT PACKET - 2357 華碩

## Metadata
- generated_at: 2026-08-10 22:26:52 Asia/Taipei
- stock_id: 2357
- stock_name: 華碩
- packet_status: standard_180d_window_packet
- latest_price_date: 20260807
- price_rows: 321
- current_main_price_date: 20260807
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260807-01698d0b1c2355ac
- official_tdcc_signal_date: 20260807
- latest_tdcc_date: 20260807
- tdcc_rows: 15
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
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- confidence_level: high
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
- decision_score_high
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
- date: 20260807
- open: 816
- high: 825
- low: 805
- close: 817
- volume: 4616536
- ma5: 815.6
- ema23_primary: 766.44
- distance_to_ema23_pct: 6.6
- ma20: 756.8
- ma60: 748.27
- ma120: 659.18
- return_5d: 0.86
- return_20d: 19.44
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: 7.95
- distance_to_high_60_pct: -15.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260713,706,725,703,704,6768399,718.28,-1.99,728.65,701.9,1.22
20260714,710,710,690,703,4883592,717,-1.95,724.55,703.8,0.88
20260715,705,720,705,712,3769668,716.59,-0.64,720.55,705.68,0.68
20260716,710,715,698,715,2700767,716.45,-0.2,716.75,707.52,0.49
20260717,705,719,700,700,4776948,715.08,-2.11,711.6,709.2,0.86
20260720,705,711,688,688,3669278,712.83,-3.48,706.55,710.52,0.69
20260721,700,739,698,736,5540625,714.76,2.97,703.95,712.82,1.02
20260722,740,772,740,757,5556494,718.28,5.39,702.55,715.68,1.03
20260723,759,773,759,769,3640645,722.5,6.44,702.45,718.7,0.68
20260724,760,780,760,771,3099430,726.55,6.12,703.6,721.75,0.6
20260727,778,778,735,760,3709649,729.33,4.2,706.55,724.62,0.74
20260728,748,763,734,735,3774159,729.81,0.71,708.15,727.18,0.76
20260729,750,771,736,761,7000149,732.41,3.9,711.2,730.02,1.42
20260730,762,762,722,737,5046040,732.79,0.57,715.2,732.47,1.12
20260731,773,810,767,810,9733283,739.22,9.57,722.35,735.48,2.08
20260803,790,813,786,799,3979413,744.2,7.36,728.55,738.15,0.84
20260804,781,816,781,806,4052111,749.35,7.56,734.85,740.75,0.85
20260805,813,859,813,838,5273869,756.74,10.74,743.6,743.28,1.09
20260806,830,843,806,818,4064934,761.85,7.37,750.15,745.7,0.85
20260807,816,825,805,817,4616536,766.44,6.6,756.8,748.27,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 74.06
- over_600_ratio: 70.3
- over_800_ratio: 67.25
- over_1000_ratio: 63.85
- over_400_change_1w: 0.92
- over_800_change_1w: 0.8
- over_1000_change_1w: 1.09
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,72.13,-0.02,66.11,-0.49,62.38,0,0,False,False
20260529,72.95,0.82,66.94,0.83,62.85,0.47,1,True,True
20260605,74.56,1.61,68.53,1.59,64.27,1.42,2,True,True
20260612,73.95,-0.61,68.37,-0.16,64.4,0.13,3,False,True
20260618,73.92,-0.03,67.75,-0.62,64.01,-0.39,0,False,False
20260626,73.12,-0.8,66.92,-0.83,63.05,-0.96,0,False,False
20260703,72.39,-0.73,65.85,-1.07,62.72,-0.33,0,False,False
20260709,72.44,0.05,66.14,0.29,62.5,-0.22,1,False,True
20260717,72.56,0.12,65.54,-0.6,61.91,-0.59,2,False,False
20260724,72.96,0.4,66.02,0.48,62.71,0.8,3,True,True
20260731,73.14,0.18,66.45,0.43,62.76,0.05,4,True,True
20260807,74.06,0.92,67.25,0.8,63.85,1.09,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2357 | 華碩 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  | call_inflow | stale_signal | 1.董事會決議日期:115/07/10 2.減資緣由:考量公司營運需求，調整資本結構並返還股款。 3.減資金額:巴西幣340,000,000元。 4.消除股份:340,000,000股。 5.減資比率:61.88%。 6.減資後股本:巴西幣209,469,000元。 7.預定股東會日期:115/07/10 8.預計減資新股上市後之上市普通股股數:不適用。 9.預計減資新股上市後之上市普通股股數占已發行普通股比率 （減資後上市普通股股數/減資後已發行普通股股數）:不適用。 10.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者， 請說明股權流通性偏低之因應措施:不適用。 11.減資基準日:待當地主管機關核准註冊變更生效後完成。 12.其他應敘明事項: (1)ACBZ以股東會代董事會通過決議。 (2)ACBZ係華碩間接100%持股之重要子公司。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260717 | 2357 | 華碩 | revenue_breakout_low_response | 營收爆發低反應股 | 11.0 | 39.0 | D_降級_TDCC轉弱 |  |  | call_inflow | stale_signal | 1.董事會決議日期:115/07/10 2.減資緣由:考量公司營運需求，調整資本結構並返還股款。 3.減資金額:巴西幣340,000,000元。 4.消除股份:340,000,000股。 5.減資比率:61.88%。 6.減資後股本:巴西幣209,469,000元。 7.預定股東會日期:115/07/10 8.預計減資新股上市後之上市普通股股數:不適用。 9.預計減資新股上市後之上市普通股股數占已發行普通股比率 （減資後上市普通股股數/減資後已發行普通股股數）:不適用。 10.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者， 請說明股權流通性偏低之因應措施:不適用。 11.減資基準日:待當地主管機關核准註冊變更生效後完成。 12.其他應敘明事項: (1)ACBZ以股東會代董事會通過決議。 (2)ACBZ係華碩間接100%持股之重要子公司。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2357 | 華碩 | 2 | 2 | 4 | 6 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2357 | 華碩 | 93 | 5 | 6084950.0 | 126600.0 | 48.06 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
