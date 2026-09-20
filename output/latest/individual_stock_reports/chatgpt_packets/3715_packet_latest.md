# INDIVIDUAL STOCK CHATGPT PACKET - 3715 定穎投控

## Metadata
- generated_at: 2026-09-20 22:17:02 Asia/Taipei
- stock_id: 3715
- stock_name: 定穎投控
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3715_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3715_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3715_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3715_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3715_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3715_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3715.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3715.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3715.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3715.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3715_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3715_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3715_latest.md?ref=main

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
- date: 20260918
- open: 122
- high: 122.5
- low: 118.5
- close: 118.5
- volume: 3411215
- ma5: 120.1
- ema23_primary: 120.85
- distance_to_ema23_pct: -1.95
- ma20: 120.9
- ma60: 126.16
- ma120: 152.46
- return_5d: -3.66
- return_20d: 10.75
- volume_ratio: 0.54
- distance_to_ma20_pct_auxiliary: -1.99
- distance_to_high_60_pct: -36.46

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,107,112.5,107,108,2600297,116.46,-7.26,109.92,142.72,0.45
20260825,107.5,110,104,109.5,2964744,115.88,-5.5,110.19,141.66,0.52
20260826,110,115,108.5,114,3086079,115.72,-1.49,110.99,140.52,0.58
20260827,115,119,114.5,116.5,4874712,115.78,0.62,112.27,139.57,0.94
20260828,120,126.5,116.5,125,7894954,116.55,7.25,113.53,138.75,1.47
20260831,122,126,119.5,120.5,11778173,116.88,3.1,114.33,137.95,2.06
20260901,123.5,132.5,123.5,132.5,9357457,118.18,12.11,115.72,137.32,1.59
20260902,132,132.5,124,124.5,12492024,118.71,4.88,116.47,136.63,2.04
20260903,125.5,126.5,117.5,118,5543430,118.65,-0.55,116.55,135.69,0.93
20260904,122,122.5,115.5,118,3581294,118.6,-0.5,116.72,134.95,0.61
20260907,119,121.5,117,119.5,3273965,118.67,0.7,116.42,134.17,0.57
20260908,124.5,130.5,124,126.5,12850292,119.32,6.01,116.65,133.5,2.22
20260909,126.5,138,125,135,16952441,120.63,11.91,117.5,132.94,2.7
20260910,132.5,133,126,127,9421993,121.16,4.82,117.97,132.21,1.46
20260911,122,124,122,123,3109049,121.31,1.39,118.33,131.32,0.49
20260914,119.5,123.5,119,120.5,2749798,121.25,-0.62,118.6,130.35,0.44
20260915,120.5,123.5,119,119.5,3599210,121.1,-1.32,119.08,129.1,0.58
20260916,121.5,123.5,120,123.5,2451847,121.3,1.81,119.88,128.16,0.4
20260917,125,125.5,118.5,118.5,4150799,121.07,-2.12,120.33,127.14,0.67
20260918,122,122.5,118.5,118.5,3411215,120.85,-1.95,120.9,126.16,0.54
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 28.74
- over_600_ratio: 26.21
- over_800_ratio: 22.79
- over_1000_ratio: 20.25
- over_400_change_1w: -0.47
- over_800_change_1w: -0.5
- over_1000_change_1w: -1.06
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,36.61,-1.76,30.92,-1.12,29.98,-1.11,0,False,False
20260709,31.82,-4.79,25.82,-5.1,23.24,-6.74,0,False,False
20260717,29.9,-1.92,24.04,-1.78,21.79,-1.45,0,False,False
20260724,29.38,-0.52,24.26,0.22,21.11,-0.68,1,False,True
20260731,29.75,0.37,24.34,0.08,21.47,0.36,2,False,True
20260807,29.59,-0.16,24.54,0.2,22.01,0.54,3,False,True
20260814,29.21,-0.38,22.91,-1.63,20.7,-1.31,0,False,False
20260821,29.2,-0.01,23.34,0.43,20.83,0.13,1,False,True
20260828,29.6,0.4,23.79,0.45,21.24,0.41,2,True,True
20260904,28.31,-1.29,23.86,0.07,20.56,-0.68,3,False,True
20260911,29.21,0.9,23.29,-0.57,21.31,0.75,4,False,True
20260918,28.74,-0.47,22.79,-0.5,20.25,-1.06,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3715 | 定穎投控 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.股東臨時會日期:115/09/17 2.重要決議事項: (1)關於公司發行H股股票並在香港聯合交易所有限公司上市的議案 (2)關於公司發行H股股票並在香港聯合交易所有限公司上市方案的議案 (3)關於公司轉為境外募集股份有限公司的議案 (4)關於公司發行H股股票募集資金使用計畫的議案 (5)關於H股股票發行上市決議有效期的議案 (6)關於提請股東會授權董事會及其授權人士全權處理與本次H股股票發行上市有關 事項的議案 (7)關於公司發行H股之前滾存利潤分配方案的議案 (8)關於就公司發行H股股票並上市修訂公司章程及相關議事規則的議案 (8-1)《公司章程（草案）》 (8-2)《股東會議事規則（草案）》 (8-3)《董事會議事規則（草案）》 (9)關於就公司發行H股股票並上市制定和修訂公司內部治理制度的議案 (9-1)《對外投資管理制度（草案）》 (9-2)《對外擔保管理制度（草案）》 (9-3)《關聯（連）交易管理制度（草案）》 (9-4)《募集資金管理辦法（草案）》 (9-5)《獨立董事工作制度（草案）》 (9-6)《累積投票制實施細則（草案）》 (9-7)《董事、高級管理人員薪酬管理制度（草案）》 (9-8)《股息政策（草案）》 (10)關於聘請H股發行上市審計機構的議案 (11)關於投保董事、高級管理人員及其他相關責任人員招股說明書責任保險的議案 (12)關於調整董事會席位並修訂《公司章程》及其附件《董事會議事規則》的議案 (13)關於劃分董事角色及職能的議案 (14)關於增選第二屆董事會獨立董事的議案 (15)關於提名第二屆董事會非獨立董事候選人的議案 3.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 3715 | 定穎投控 | revenue_breakout_low_response | 營收爆發低反應股 | 20 | 11 | A_優先追蹤 |  |  | no_signal | stale_signal | 1.股東臨時會日期:115/09/17 2.重要決議事項: (1)關於公司發行H股股票並在香港聯合交易所有限公司上市的議案 (2)關於公司發行H股股票並在香港聯合交易所有限公司上市方案的議案 (3)關於公司轉為境外募集股份有限公司的議案 (4)關於公司發行H股股票募集資金使用計畫的議案 (5)關於H股股票發行上市決議有效期的議案 (6)關於提請股東會授權董事會及其授權人士全權處理與本次H股股票發行上市有關 事項的議案 (7)關於公司發行H股之前滾存利潤分配方案的議案 (8)關於就公司發行H股股票並上市修訂公司章程及相關議事規則的議案 (8-1)《公司章程（草案）》 (8-2)《股東會議事規則（草案）》 (8-3)《董事會議事規則（草案）》 (9)關於就公司發行H股股票並上市制定和修訂公司內部治理制度的議案 (9-1)《對外投資管理制度（草案）》 (9-2)《對外擔保管理制度（草案）》 (9-3)《關聯（連）交易管理制度（草案）》 (9-4)《募集資金管理辦法（草案）》 (9-5)《獨立董事工作制度（草案）》 (9-6)《累積投票制實施細則（草案）》 (9-7)《董事、高級管理人員薪酬管理制度（草案）》 (9-8)《股息政策（草案）》 (10)關於聘請H股發行上市審計機構的議案 (11)關於投保董事、高級管理人員及其他相關責任人員招股說明書責任保險的議案 (12)關於調整董事會席位並修訂《公司章程》及其附件《董事會議事規則》的議案 (13)關於劃分董事角色及職能的議案 (14)關於增選第二屆董事會獨立董事的議案 (15)關於提名第二屆董事會非獨立董事候選人的議案 3.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3715 | 定穎投控 | 21 | 10 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3715 | 定穎投控 | 215 | 5 | 2283830.0 | 142740.0 | 16.0 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
