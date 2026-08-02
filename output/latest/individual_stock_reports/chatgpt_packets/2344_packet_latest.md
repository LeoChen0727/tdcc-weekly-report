# INDIVIDUAL STOCK CHATGPT PACKET - 2344 華邦電

## Metadata
- generated_at: 2026-08-02 22:26:37 Asia/Taipei
- stock_id: 2344
- stock_name: 華邦電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 315
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2344_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2344_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2344_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2344_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2344_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2344_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2344.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2344.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2344.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2344.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2344_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2344_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2344_latest.md?ref=main

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
- date: 20260730
- open: 123.5
- high: 133
- low: 117
- close: 118.5
- volume: 208317971
- ma5: 141.4
- ema23_primary: 160.57
- distance_to_ema23_pct: -26.2
- ma20: 162.72
- ma60: 161.09
- ma120: 132.38
- return_5d: -26.4
- return_20d: -37.63
- volume_ratio: 1.58
- distance_to_ma20_pct_auxiliary: -27.18
- distance_to_high_60_pct: -49.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,176,186,176,183.5,164178951,185.02,-0.82,189.07,138.99,0.69
20260703,180.5,188,177,184.5,141900944,184.98,-0.26,189.32,140.47,0.6
20260706,191,200,183,183,163686093,184.82,-0.98,190.38,142.01,0.71
20260707,184,186,172,174,142095545,183.91,-5.39,191.38,143.35,0.62
20260708,177.5,181.5,165,168.5,146196884,182.63,-7.74,191.97,144.59,0.64
20260709,173.5,184,170,176.5,160890217,182.12,-3.09,193.35,145.97,0.71
20260713,181.5,183,166,167,149251061,180.86,-7.66,193.88,147.25,0.67
20260714,170,172.5,156,164.5,135442057,179.5,-8.35,193.5,148.5,0.62
20260715,175.5,180.5,173.5,180.5,95140846,179.58,0.51,193.07,150.04,0.45
20260716,176,180.5,171,172,150613446,178.95,-3.88,191.82,151.48,0.75
20260717,159.5,162.5,155,155,110525648,176.95,-12.41,189.62,152.54,0.57
20260720,155,157,146,151,107223362,174.79,-13.61,186.25,153.55,0.58
20260721,156,158,152,155.5,104783854,173.18,-10.21,182.93,154.68,0.62
20260722,165,171,164.5,171,97387194,173,-1.16,180.9,156.06,0.61
20260723,172,172,157,161,157825138,172,-6.4,178.7,157.18,1.01
20260724,158.5,164,153.5,154.5,135375417,170.54,-9.41,175.45,158.16,0.9
20260727,155,161,150,160,110420180,169.66,-5.7,173.12,159.28,0.77
20260728,144,147,144,144,69129108,167.52,-14.04,170.18,160.19,0.49
20260729,137,137.5,130,130,86091045,164.4,-20.92,166.3,160.76,0.65
20260730,123.5,133,117,118.5,208317971,160.57,-26.2,162.72,161.09,1.58
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 68.57
- over_600_ratio: 67.38
- over_800_ratio: 66.33
- over_1000_ratio: 65.63
- over_400_change_1w: -0.82
- over_800_change_1w: -0.81
- over_1000_change_1w: -0.76
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,72.17,3.84,70.15,3.84,69.42,3.81,2,True,True
20260522,69.61,-2.56,67.5,-2.65,66.86,-2.56,0,False,False
20260529,74.03,4.42,71.87,4.37,71.13,4.27,1,True,True
20260605,73.98,-0.05,71.71,-0.16,71.05,-0.08,0,False,False
20260612,71.59,-2.39,69.2,-2.51,68.57,-2.48,0,False,False
20260618,74.46,2.87,72.13,2.93,71.35,2.78,1,True,True
20260626,73.41,-1.05,71.04,-1.09,70.33,-1.02,0,False,False
20260703,71.18,-2.23,68.86,-2.18,68.12,-2.21,0,False,False
20260709,69.89,-1.29,67.69,-1.17,66.93,-1.19,0,False,False
20260717,69.81,-0.08,67.58,-0.11,66.74,-0.19,0,False,False
20260724,69.39,-0.42,67.14,-0.44,66.39,-0.35,0,False,False
20260731,68.57,-0.82,66.33,-0.81,65.63,-0.76,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2344 | 華邦電 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  | put_inflow | stale_signal | 1.事實發生日:115/07/13 2.公司名稱:華邦電子股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:依本公司海外第四次無擔保轉換公司債發行及轉換辦法第十二(一)條規定， 本債券發行之日起屆滿三個月之翌日至到期日前，如本公司普通股於台灣證券交易所之 收盤價格，連續三十個營業日中有二十個交易日(如遇除權或除息者，於除權或除息交 易日至除權或除息基準日之間，採用之收盤價格，應先設算為除權或除息前之價格)達 提前贖回金額(定義於後)除以本債券面額再乘以當時轉換價格後所得之總數120%時，本 公司得以提前贖回金額贖回全部或部份本債券。 「提前贖回金額」係指公司依本債券面額加計年利率為-1.5%之利息補償金，且以每半 年為計算基礎所得之金額。 提前贖回金額將按固定匯率換算為新臺幣，並以該新臺幣金額按贖回當時匯率(參考上 午十一時Taipei Forex Inc.所顯示之定盤匯率)換算為美金償還。 6.因應措施:本公司將於115年8月12日提前贖回全部海外第四次無擔保轉換公司債。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2344 | 華邦電 | 14 | 2 | 5 | 10 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2344 | 華邦電 | 244 | 25 | 29940920.0 | 2946610.0 | 10.16 | put_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
