# INDIVIDUAL STOCK CHATGPT PACKET - 8932 智通*

## Metadata
- generated_at: 2026-07-23 22:28:47 Asia/Taipei
- stock_id: 8932
- stock_name: 智通*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 164
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8932_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8932_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8932_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8932_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8932_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8932_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8932_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8932_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8932_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8932_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8932_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8932_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8932.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8932.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8932.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8932.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8932_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8932_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8932_latest.md?ref=main

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
- date: 20260717
- open: 125
- high: 128.5
- low: 117
- close: 117
- volume: 8228000
- ma5: 120.6
- ema23_primary: 112.51
- distance_to_ema23_pct: 3.99
- ma20: 111.85
- ma60: 102.36
- ma120: 119.71
- return_5d: -1.27
- return_20d: 17
- volume_ratio: 1.27
- distance_to_ma20_pct_auxiliary: 4.6
- distance_to_high_60_pct: -10

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,101,102.5,99.5,100,2074000,100.12,-0.12,101.1,93.69,1.06
20260622,100,103,99.2,100,2254000,100.11,-0.11,101.05,94,1.1
20260623,100.5,102.5,98.5,100.5,2195000,100.14,0.36,100.8,94.27,1.02
20260624,100,106,99.6,104.5,4260000,100.5,3.98,100.95,94.64,1.8
20260625,104,114.5,102.5,114.5,11167000,101.67,12.62,101.67,95.18,3.82
20260626,120,122.5,109.5,111,20303000,102.45,8.35,102.38,95.65,5.16
20260629,111.5,113,103.5,105,8351000,102.66,2.28,102.6,96.06,1.92
20260630,105,110,104,108.5,3124000,103.15,5.19,102.85,96.5,0.69
20260701,108.5,110,105.5,108,2690000,103.55,4.3,103.12,96.96,0.58
20260702,107,109.5,106,107.5,1293000,103.88,3.48,103.52,97.39,0.28
20260703,107,108,105,105.5,2340000,104.02,1.43,103.79,97.76,0.49
20260706,106.5,116,106,116,6761000,105.01,10.46,104.49,98.32,1.32
20260707,115,118.5,112.5,115,7723000,105.85,8.65,105.22,98.89,1.45
20260708,116,123.5,115,119.5,10148000,106.98,11.7,106.11,99.52,1.79
20260709,122.5,122.5,116.5,118.5,6901000,107.94,9.78,107.11,100.03,1.17
20260713,118.5,119.5,113,115,3881000,108.53,5.96,107.95,100.49,0.66
20260714,113,115,110,115,4207000,109.07,5.44,108.38,100.97,0.76
20260715,116,126.5,114.5,126.5,9534000,110.52,14.46,109.55,101.58,1.67
20260716,124.5,130,124.5,129.5,12490000,112.1,15.52,111,102.09,2.02
20260717,125,128.5,117,117,8228000,112.51,3.99,111.85,102.36,1.27
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 80.6
- over_600_ratio: 78.9
- over_800_ratio: 76.53
- over_1000_ratio: 75.08
- over_400_change_1w: 0.2
- over_800_change_1w: 0.02
- over_1000_change_1w: -0.47
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.21,,72.84,,71.39,,0,False,False
20260508,78.16,-0.05,72.82,-0.02,71.57,0.18,1,False,True
20260515,79.17,1.01,73.71,0.89,72.48,0.91,2,True,True
20260522,79.26,0.09,74.07,0.36,72.82,0.34,3,False,True
20260529,79.92,0.66,75.07,1,73.3,0.48,4,True,True
20260605,80.03,0.11,74.84,-0.23,73.33,0.03,5,False,True
20260612,80.17,0.14,75.14,0.3,73.35,0.02,6,False,True
20260618,80.28,0.11,75.66,0.52,74.16,0.81,7,True,True
20260626,81.44,1.16,76.56,0.9,74.84,0.68,8,True,True
20260703,80.6,-0.84,76.24,-0.32,74.75,-0.09,0,False,False
20260709,80.4,-0.2,76.51,0.27,75.55,0.8,1,False,True
20260717,80.6,0.2,76.53,0.02,75.08,-0.47,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8932 | 智通* | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | continued_2_3d | 1.股東會決議日:115/06/26 2.許可從事競業行為之董事姓名及職稱: 董事 (1)永讚開發投資(股)公司代表人：鍾富瑋 (2)永讚開發投資(股)公司代表人：林俊儀 (3)永讚開發投資(股)公司代表人：TAN TIONG MING (4)宏達開發投資(股)公司代表人：黃偉特 (5)宏達開發投資(股)公司代表人：蔡焜煌 (6)宏達開發投資(股)公司代表人：Vincent Wong Mun Seng 獨立董事 (1)李天行　 (2)張居德 (3)劉慧儀 3.許可從事競業行為之項目: 董事 (1)永讚開發投資(股)公司代表人：鍾富瑋    永讚開發投資(股)公司 董事長    金銓富投資有限公司 董事長    富勛投資有限公司 董事長    智捷醫學科技股份有限公司 董事    雙都經貿股份有限公司 董事    龍邦國際興業股份有限公司 獨立董事    笙泉科技股份有限公司 董事長 (2)永讚開發投資(股)公司代表人：林俊儀    恆理致遠國際法律事務所 所長    宣德科技股份有限公司 獨立董事    金益鼎企業股份有限公司 獨立董事    新潤興業股份有限公司 獨立董事    台翰精密科技股份有限公司 獨立董事    台灣運動彩券股份有限公司 董事    笙泉科技股份有限公司 董事 (3)永讚開發投資(股)公司代表人：TAN TIONG MING    聯和科創股份有限公司 董事    沛聯(北京)科技有限公司 董事    GLOBAL LINE NETWORK SDN BHD – CEO    GLOBAL LINE NETWORK LTD. – Director    GLOBAL LINE INNOVATION PTE LTD. – Director    Bharat Line Innovations Pvt Ltd. – Director    Beerupii Innovation Pvt. Ltd. – Director (4)宏達開發投資(股)公司代表人：黃偉特    易邦建設有限公司 董事    億邦開發股份有限公司 董事    蘭邦投資股份有限公司 董事長    暟富投資股份有限公司 董事長    巨興醫學科技股份有限公司 董事長    澳迪科技股份有限公司 董事長 (5)宏達開發投資(股)公司代表人：蔡焜煌    宏達開發投資(股)公司 董事長    金愛投資有限公司 董事    楚芬投資有限公司 董事    智捷醫學科技股份有限公司 董事    聯和科創股份有限公司 董事長    GLOBAL LINE INNOVATION PTE LTD. – Director    Bharat Line Innovations Pvt Ltd. – Director    Beerupii Innovation Pvt. Ltd. – Director    華智數位娛樂股份有限公司 董事    HuaZhi Software Private Ltd. – Director    笙泉科技股份有限公司 董事 (6)宏達開發投資(股)公司代表人：Vincent Wong Mun Seng    Vincenology Solution – Founder    Vincenology (M) Sdn Bhd – Managing Director    A Plus Network – Managing Director    TG Agrosolutions Limited – Director    Binary Reliance Sdn Bhd – Director 獨立董事 (1)李天行　    勝德國際研發股份有限公司 董事 (2)張居德    張居德律師事務所 主持律師    坤悅開發股份有限公司 獨立董事    元檜投資有限公司 董事 (2)劉慧儀    台亞風能股份有限公司 法人董事代表人    台灣銘板股份有限公司 獨立董事    瀚軒股份有限公司 獨立董事    亞洲新能源(開曼)(股)公司 營運管理總監 4.許可從事競業行為之期間:任職本公司董事之職務期間。 5.決議情形（請依公司法第209條說明表決結果）: 贊成權數：217,011,081權 反對權數：141,485權 無效權數：0權 棄權與未投票權數：14,636,621權 贊成本案之表決權數占總表決權數93.62%，本案照案通過。 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用 7.所擔任該大陸地區事業之公司名稱及職務:不適用 8.所擔任該大陸地區事業地址:不適用 9.所擔任該大陸地區事業營業項目:不適用 10.對本公司財務業務之影響程度:不適用 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用 12.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8932 | 智通* | 3 | 1 | 3 | 6 | 10 | continued_2_3d | 連續 3 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
