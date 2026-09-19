# INDIVIDUAL STOCK CHATGPT PACKET - 2344 華邦電

## Metadata
- generated_at: 2026-09-19 22:15:59 Asia/Taipei
- stock_id: 2344
- stock_name: 華邦電
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
- date: 20260918
- open: 177
- high: 179.5
- low: 173.5
- close: 179.5
- volume: 138585216
- ma5: 167.6
- ema23_primary: 173.64
- distance_to_ema23_pct: 3.37
- ma20: 176.28
- ma60: 171.65
- ma120: 150.88
- return_5d: 4.66
- return_20d: -0.83
- volume_ratio: 1.06
- distance_to_ma20_pct_auxiliary: 1.83
- distance_to_high_60_pct: -20.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,179.5,184.5,175.5,177,99392300,170.55,3.78,164.07,173.82,0.66
20260825,172,179,168.5,179,92923853,171.26,4.52,165.82,174.18,0.62
20260826,179.5,182.5,178,181.5,85770151,172.11,5.46,168.4,174.4,0.57
20260827,184,190,183,186,139732644,173.27,7.35,171.78,174.43,0.95
20260828,188.5,192,180.5,181.5,153443947,173.95,4.34,174.35,174.49,1
20260831,179.5,186,176,182.5,398679210,174.67,4.49,176.32,174.54,2.34
20260901,183.5,184,175.5,176,136605515,174.78,0.7,177.28,174.78,0.8
20260902,173.5,180,171.5,179,83567943,175.13,2.21,177.78,175.19,0.51
20260903,181.5,185.5,168,169,161434224,174.62,-3.22,177.68,175.4,1
20260904,174,176,165.5,174,100505993,174.57,-0.32,178.2,175.82,0.63
20260907,181,183.5,178,180,118922555,175.02,2.85,178.22,176.21,0.76
20260908,185,192,183.5,188,222260653,176.1,6.76,178.72,176.47,1.41
20260909,190.5,190.5,180.5,183,140400625,176.68,3.58,179.03,176.38,0.91
20260910,181,182.5,178,179.5,67914754,176.91,1.46,179.15,176.08,0.46
20260911,173,173.5,170.5,171.5,74789115,176.46,-2.81,178.55,175.62,0.54
20260914,166.5,167.5,160,160,123411883,175.09,-8.62,177.47,174.65,0.89
20260915,162.5,164,158.5,159.5,71179694,173.79,-8.22,176.62,173.61,0.54
20260916,163.5,169.5,163.5,169,83218538,173.39,-2.53,176.68,172.9,0.64
20260917,177,180,170,170,120007010,173.11,-1.8,176.35,172.32,0.93
20260918,177,179.5,173.5,179.5,138585216,173.64,3.37,176.28,171.65,1.06
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 67.54
- over_600_ratio: 66.16
- over_800_ratio: 65.02
- over_1000_ratio: 64.01
- over_400_change_1w: -2.16
- over_800_change_1w: -2.08
- over_1000_change_1w: -2.08
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,71.18,-2.23,68.86,-2.18,68.12,-2.21,0,False,False
20260709,69.89,-1.29,67.69,-1.17,66.93,-1.19,0,False,False
20260717,69.81,-0.08,67.58,-0.11,66.74,-0.19,0,False,False
20260724,69.39,-0.42,67.14,-0.44,66.39,-0.35,0,False,False
20260731,68.57,-0.82,66.33,-0.81,65.63,-0.76,0,False,False
20260807,69.96,1.39,67.81,1.48,67.16,1.53,1,True,True
20260814,68.96,-1,66.79,-1.02,66.07,-1.09,0,False,False
20260821,69.68,0.72,67.51,0.72,66.79,0.72,1,True,True
20260828,70.64,0.96,68.52,1.01,67.78,0.99,2,True,True
20260904,67.97,-2.67,65.54,-2.98,64.57,-3.21,0,False,False
20260911,69.7,1.73,67.1,1.56,66.09,1.52,1,True,True
20260918,67.54,-2.16,65.02,-2.08,64.01,-2.08,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2344 | 華邦電 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | repeated_but_no_breakout | 1.證券名稱: 新唐科技股份有限公司普通股 2.交易日期:115/8/19~115/9/17 3.董事會通過日期: 民國115年8月6日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 1.交易單位數量：2,898,000股 2.每單位價格：每股新台幣114.49元 3.交易總金額：新台幣331,778,468元 6.處分利益（或損失）（取得有價證券者不適用）: 不適用 7.與交易標的公司之關係: 本公司為交易標的公司之母公司 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 累積持有數量：224,452,635股 金額：新台幣5,798,973仟元 持股比例：49.61% 權利受限情形：無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占總資產比例:44.7% 占歸屬於母公司業主之權益之比例:70%(詳其他敘明事項) 最近期財務報表中營運資金數額：新台幣14,242,402仟元 10.取得或處分之具體目的: 為集團長期穩健發展 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 民國115年8月6日 15.前已就同一件事件發布重大訊息日期: 補充115年08月06日公告 16.其他敘明事項: 迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 包含本公司115年9月16日公告取得Infineon Technologies LLC旗下NOR Flash與 F-RAM事業經重組後之100%股權，交易總金額約為美金1,120,000,000元（美金兌新 臺幣匯率以31.6估算，約新台幣35,392,000,000元），惟本交易尚須依法取得相關 主管機關之核准、許可、同意、備查或申報程序（如適用），並達成或經合法豁免 Stock Purchase Agreement約定之各項交割先決條件。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 2344 | 華邦電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.證券名稱: 新唐科技股份有限公司普通股 2.交易日期:115/8/19~115/9/17 3.董事會通過日期: 民國115年8月6日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 1.交易單位數量：2,898,000股 2.每單位價格：每股新台幣114.49元 3.交易總金額：新台幣331,778,468元 6.處分利益（或損失）（取得有價證券者不適用）: 不適用 7.與交易標的公司之關係: 本公司為交易標的公司之母公司 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 累積持有數量：224,452,635股 金額：新台幣5,798,973仟元 持股比例：49.61% 權利受限情形：無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占總資產比例:44.7% 占歸屬於母公司業主之權益之比例:70%(詳其他敘明事項) 最近期財務報表中營運資金數額：新台幣14,242,402仟元 10.取得或處分之具體目的: 為集團長期穩健發展 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 民國115年8月6日 15.前已就同一件事件發布重大訊息日期: 補充115年08月06日公告 16.其他敘明事項: 迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 包含本公司115年9月16日公告取得Infineon Technologies LLC旗下NOR Flash與 F-RAM事業經重組後之100%股權，交易總金額約為美金1,120,000,000元（美金兌新 臺幣匯率以31.6估算，約新台幣35,392,000,000元），惟本交易尚須依法取得相關 主管機關之核准、許可、同意、備查或申報程序（如適用），並達成或經合法豁免 Stock Purchase Agreement約定之各項交割先決條件。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2344 | 華邦電 | 35 | 10 | 5 | 10 | 20 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 20 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2344 | 華邦電 | 402 | 42 | 43855350.0 | 827740.0 | 52.98 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
